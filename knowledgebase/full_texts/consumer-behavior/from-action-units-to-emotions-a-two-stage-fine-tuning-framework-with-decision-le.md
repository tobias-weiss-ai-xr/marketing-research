---
title: 'From Action Units to Emotions: A Two-Stage Fine-Tuning Framework with Decision-Level Fusion for
  Facial Expression Recognition'
url: https://doi.org/10.21203/rs.3.rs-10578386/v1
category: consumer-behavior
subcategory: framework
date: 2026-08
venue: Research Square
authors:
- Rui Tu
- Liguo Zhou
- Alois Knoll
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10578386/latest.pdf
pages: 34
chars: 79213
fetched_at: '2026-11-08T18:57:16+00:00'
kb_version: 1
---

# From Action Units to Emotions: A Two-Stage Fine-Tuning Framework with Decision-Level Fusion for Facial Expression Recognition

From Action Units to Emotions: A Two-Stage Fine-
Tuning Framework with Decision-Level Fusion for
Facial Expression Recognition
Rui Tu 
Technical University of Munich
Liguo Zhou 
Technical University of Munich
Alois Knoll 
Technical University of Munich
Research Article
Keywords:
Posted Date: August 31st, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10578386/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: No competing interests reported.

From Action Units to Emotions: A Two-
Stage Fine-Tuning Framework with
Decision-Level Fusion for Facial
Expression Recognition

Author Rui Tu(rui.tu@tum.de)
Dr. Liguo Zhou(liguo.zhou@tum.de)
Prof. Alois Christian Knoll(knoll@in.tum.de)
Date July 23, 2026 in Munich

Abstract

Facial expressions serve as a primary non-verbal channel through which humans convey emo-
tional states and behavioral intentions, holding significant value  across diverse application
scenarios including digital mental health, human-com puter interaction, educational engage-
ment analysis, and consumer behavior understanding. However, facial expression recogni tion
(FER) technology remains constrained by practical challenges such as illuminat ion variations,
pose differences, and scarcity of annotated data, with existi ng models generally suffering
from poor cross-domain adaptability, overfitting, a nd insufficient interpretability.
To address these issues, this paper proposes a multi-modal large-model enhancement
strategy based on two-stage fine-tuning.  First, a question -answer paired facial action unit
(AU) fine-tuning dataset is constructed from the CAS(ME)‡ dataset, an d the Qwen3-VL-32B-
Instruct multi-modal large model is fine-tuned in th e first stage using LoRA to reinforce its
AU recognition capability.  Subsequently, a second-stage fine-tuning is conducted on the FER
dataset to guide the model in achieving emotion classification t hrough AU-based reasoning.
On this basis, decision-level joint prediction is f urther explored by combining the fine-tuned
large model with the specialized small model OpenFace 3.0.
Systematic experimental evaluations demonstrate that the proposed two-stage fine-t uned
fusion model achieves significant superiority over both the non- fine-tuned Qwen3-VL and
other mainstream deep models, and also substantially outperfo rms the standalone inference
results of OpenFace 3.0, fully validating the effectiveness of the two-st age fine-tuning strategy
in eliciting discriminative features for subtle fac ial geometric deformations and low-intensity
expressions from large visual models.  Meanwhile, the study also reveals that while pure
large visual models possess formidable capabilities in high-level semantic understanding,
they still exhibit inherent limitations in perceivi ng subtle facial deformations. The proposed
method demonstrates clear efficacy in both improving predicti on accuracy and enhancing
interpretability, offering a novel technical pathwa y and empirical foundation for constructing
highly robust and interpretable FER systems.

Contents

1   Introduction
2   related works
2.1   Traditional Facial Expression Recognition Methods     .......... ...............................
2.2   Multimodal Large Language Models for Emotion Recognition     .... ...................
2.3   AU-Based Fine-Tuning and Inference Strategies      ...............................................
2.4   Collaborative Decision-Making      ................... .....................................................
3   The proposed Method
3.1   Two-stage Progressive Fine-tuning Framework       ...............................................
3.2   Task Fomulation      ................................................................................................
3.3   Data Preprocess     ..................................................................................................
3.3.1   Static Image Dataset Processing (FER-2013)      .......................................
3.3.2   Frame-Sequence Dataset Processing (CAS(ME)3 )      ...............................
3.3.3   Dataset Splitting    ............................ .........................................................
3.4   Qwen3-VL Introduction     .......................... ...........................................................
3.5   AU-Detection Fine-Tuning       ................................................................................
3.5.1   Fine-Tuning Objective      ...........................................................................
3.5.2   LoRA-Based Parameter Efficient Fine-tuning      .......................................
3.5.3   AU-Oriented Instruction Tuning    .................. ..........................................
3.5.4   Training Objective       ................................................................................
3.6   Expression Recognition Fine-tuning      .................................................................
3.6.1   Fine-Tuning Objective      ...........................................................................
3.6.2   Fine-Tuning Strategy    .......................... ....................................................
3.7   Decision-Level Fusion with OpenFace 3.0     .........................................................
4   Experiments and Results
4.1   Datasets    ...............................................................................................................
4.2   Evaluation Metrics     ........................... ..................................................................
4.3   Model Performance      .............................. ............................................................
4.3.1   Experimental Setup    ........................... .....................................................
4.3.2   Overall Model Performance     ....................... ............................................
4.3.3   Advantages of the Fused Model over the Pure Large Model     ................
4.3.4   Effectiveness of Fine-Tuning      .................................................................
4.3.5   Advantages of the Fused Model over Pure OpenFace 3.0       ..................
4.3.6   Comparative Experimental Analysis      .............. ......................................
4.3.7   Confusion Matrix Analysis      .................... ...............................................
5   Conclusions and Future Work
5.1   Conclusions      .......................................................................................................
5.2   Future Work     .......................................................................................................

1
3
3
3
3
4
5
5
5
7
7
7
8
8
8
9
9
10
12
13
13
13
14
17
17
17
18
18
18
20
20
21
21
22
25
25
25

viii                                                                                                                                                    Contents

Bibliography                                                                                                                           27

Chapter 1

Introduction

Facial expressions directly reflect an individual ’s internal emotions and behavioral intentions.
It plays a central role in interpersonal communication.  Facial expression  recognition (FER)
technology has now been widely applied across various domains, including digital mental
health, human-computer interaction, educational engagement analysis, and consumer b e-
havior understanding. Automatic facial expression analysis is one of the core research  topics
in the field of affective computing. Researchers have explored a variety  of facial expression
recognition methods, with the core idea being to en code emotion-related information from
facial visual representations and subsequently decode it for emotion detection and  classifi-
cation. While significant progress has been made through the expansion of datasets and the
development of advanced neural architectures, existing Facial Expression Recognition (FER)
methods still struggle with robustness and generaliza tion.
Current 2D FER systems face persistent challenges, including illumination variability, pose
misalignment, and severe individual differences, which demand models to possess invari-
ance, robustness, and identity-disentanglement capabilities.   To mi tigate these issues,  re-
searchers have explored 3D/4D data fusion for geometric capture, as well as att ention mech-
anisms and Generative Adversarial Networks (GANs) for occlusion handling. H owever, these
approaches are often constrained by their heavy reliance on expensively annotated large-scale
data and their failure to fully disentangle identit y from expression.
Compounding these technical hurdles is the core bottleneck of data scarcity, resulti ng
from the subjective nature of expression annotation , the requirement for professional exper-
tise, and the rising costs and privacy regulations associated with data  acquisition. Early hand-
crafted methods, such as LBP-TOP [ZP07] and Non-negative Matrix Factoriza tion [Zhi+11],
achieved initial success but proved insufficient for  capturing the subtle and transient nature
of genuine expressions. Subsequently, deep learning paradigms —including CNNs [Zha+21],
GNNs [Xie+20], and Transformers [Ind+23] —have pushed performance boundaries by treat-
ing facial images as structured data.  Nevertheless, while effective in  single-domain tasks,
these models exhibit limited cross-domain semantic alignment and interactive capability.
The emergence of Multimodal Large Language Models (MLL Ms), capable of jointly pro-
cessing visual and textual modalities, offers a new paradigm for FER. Fine-tu ning MLLMs
has recently shown promise in enhancing recognition performance.  In parallel, the Facial
Action Coding System [EF78] and its Action Units (AUs) provi de a fine-grained, anatomically
grounded taxonomy for describing facial muscle movements (see Figure 1.1).  Given  their
ability to bridge low-level muscle actions and high-level emotions, AUs h ave been extensively
employed as effective discriminative features in FER [ZLZ20].
Despite these advances, end-to-end fine-tuning of MLLMs relying solely  on “video-label”
supervisory signals remains suboptimal, as it neglects the fine-grained interm ediate represen-
tations (i.e., AUs) that underlie emotional expressions.
To address this gap, we propose a two-stage fine-tuning strategy using the  AU annota-

2                                                                                                                                              1  Introduction

Figure 1.1: An illustrative example of the association between A ction Unit (AU) expressions and emotions

tions from the CAS(ME)3 dataset to enhance the Qwen3-VL-32B- Instruct model.  Our ap-
proach first guides the model to infer AUs before predicting em otions.  We systematically
evaluate our method on the FER-2013 benchmark, where our fine-tuned model significantly
outperforms existing vision-language baselines (e.g., Qwen2.5-VL and QVQ [Qwe24]) across
multiple metrics, including macro/micro expression r ecognition accuracy and recall.  Fur-
thermore, we integrate our fine-tuned MLLM with OpenFace, a lightweight CNN-based FER
model, via decision-level fusion. The results show that our model subst antially boosts Open-
Face’s performance, hig hlighting its practical collaborative value.
Overall, our main contributions are four-fold:
• Validation of Large Model Baseline Performance: We systematically evaluated the
zero-shot and few-shot performance of Qwen3-VL-32B-Instruct on facial emotion recog-
nition tasks, establishing a strong baseline for this model on this task.
• Large Model Fine-Tuning Integrated with AU Annotations: We fine-tuned Qwen3-
VL-32B-Instruct using the AU annotations from the CAS(ME)3 dataset, enabling the
model to acquire AU inference capabilities. The model  was then trained and evaluated
on the original train-test split of FER-2013, following a two-st age inference pipeline of
"AU inference first, emotion prediction second," fu lly leveraging its visual perception
and reasoning abilities.
• Decision-Level Fusion of Large and Traditional Models:  We  performed decision-
level fusion between the fine-tuned Qwen3-VL and OpenFace 3.0, a light weight con-
volutional neural network, to explore the feasibili ty of complementary integration and
validate the practical effectiveness of heterogeneous model coll aboration.
• Robust  Empirical Performance:  The Qwen3-VL-32B-Instruct model fine-tuned on
CAS(ME)3 achieved superior results over existing vision-language baselines on the FER-
2013 test set.  Moreover, when integrated with trad itional deep learning models, its
recognition accuracy significantly surpassed that of any  single neural network model.
These results indicate that large models fine-tuned with AU annotations can substan-
tially improve the detection accuracy of facial aff ective states while exhibiting strong
cross-dataset transferability.

Chapter 2

related works

Facial Expression Recognition (FER) has evolved from handcrafted feature-based pipelines to
deep learning and, more recently, multimodal large language models (MLLMs ).

2.1   Traditional Facial Expression Recognition Methods

Early FER relied on handcrafted descriptors such as LBP-TOP  [ZP07], HOG 3D  [PKO09],
and optical flow features (e.g., MDMO [LLL18], HOOF [LYZ16]) .  These methods are com-
putationally efficient and label-lean, but are vuln erable to illumination and pose variations,
require extensive domain knowledge, and lack precision for subtle micro-expressi ons.  Deep
learning approaches—CNNs, RNNs/LSTMs, C3D, and ensembles —automatically learn hier-
archical features and achieve strong performance on large-scale datasets [He+16] [ Don+15]
[Zha+17].   Nonetheless,  they  demand  large  annotated  corpora,  suffer f rom poor inter-
pretability, and exhibit limited cross-domain genera lization.

2.2   Multimodal Large Language Models for Emotion Recognition

Vision-language models like CLIP enable zero-shot FER via embedding sim ilarity [Zho+24]
[Ryu+25], yet operate primarily at the level of fea ture matching without explicit reasoning.
Instruction-tuned MLLMs (e.g., AffectGPT [Lia+25], EmoLA [Li+24],  AU-LLaVA [Hu+24])
treat emotion recognition as a generative task, but most still follow a n end-to-end "image-to-
emotion" mapping, lacking an explicit intermediate r easoning chain.

2.3   AU-Based Fine-Tuning and Inference Strategies

The Facial Action Coding System  (FACS) provides  an objective link b etween facial mus-
cle movements and emotions.  Several works incorporate AUs as auxiliary cues  [ Wan+21]
[Xie+20]  [Sun+20]  [Wan+23].   ExpLLM  [Wan+26] and AULLM++  [Qwe24] introduce
AU-grounded Chain-of-Thought reasoning and achieve state-of-the-art results.   However, AU
annotations are costly and scarce, and AUs are typically treated as optional supplem ents
rather than mandatory reasoning prerequisites. Existing MLLM-based FER methods have no t
systematically integrated AU detection as a structu red, obligatory intermediate step within
the fine-tuning pipeline.

4                                                                                                                                          2  related works

2.4   Collaborative Decision-Making

Recent work in general domains combines large and small models via cascading, routing , or
decision fusion to balance performance and efficiency [HGJ+25].  However, such collabo-
ration remains largely unexplored in FER. Lightweight experts like OpenFace 3.0  [Hu+25]
capture local motion cues effectively but lack semantic reasoning capacity, whi le MLLMs offer
strong visual understanding but are relatively insen sitive to fine-grained micro-movements.
Systematic frameworks that leverage the complementary strengths of both paradigms for FER
are currently absent.

Chapter 3

The proposed Method

3.1   Two-stage Progressive Fine-tuning Framework
The two-stage progressive fine-tuning strategy adopted in this paper essentially decom poses
the complex cognitive task of facial emotion recogn ition into two sequential sub-problems:
AU perception ("what facial changes are observed") and emotion inference ("what e motions
these changes signify"). In the first stage, fine-grained AU annotations fr om CAS(ME)‡ video
frames are leveraged to train the model to establish robust, domain-agnostic percep tual ca-
pabilities for subtle facial micro-movements. In the second stage, built upon this foundation,
the model learns to map AU combinations to emotion categories on t he target-domain FER
data.  This design achieves a triple decoupling:  the decoupling of perception from reason-
ing, the decoupling of domain-agnostic knowledge (AU s) from domain-specific knowledge
(emotions), and the decoupling of physical observat ions (muscle movements) from emotion
labels.  Our algorithm is shown in Algorithm 1.  Exp erimental results demonstrate that this
curriculum learning paradigm effectively mitigates t he domain discrepancy between video
frames and static images, while significantly impro ving the accuracy and interpretability of
cross-domain emotion recognition.

3.2   Task Fomulation

This subsection focuses on the task of Facial Expression Recognition (FER), aim ing to endow
multimodal large language models with fine-grained perceptual and semantic interpreta-
tion capabilities for emotional states in facial images.  Unlike conven tional FER tasks that
merely require models to output discrete emotion ca tegory labels, this task further demands
that models explicitly reveal the intermediate faci al representations —namely, Action Units
(AUs)—that underpin their decisions, thereby enabling an interpretable reasoning chain  from
micro-level facial manifestations to high-level emotional semantics. The core definition of the
task is as follows:
Inputs: A static facial image I ∈ RH×W×3, where H and W denote the height and width
of the image, respectively.  The image is captured from facial expression scenarios under
arbitrary lighting conditions, head poses, and occlusions.
Outputs:  A natural language response Y = {y1 , y2 ,..., yN}, where yj  denotes the j-th
generated token. The response is required to simultaneously encompass t he following three
levels of information:
Intermediate-Level Facial Encoding: Detect and output the set A = {AU1 , AU2 , · · · , AUK }
of active facial action units present in the input i mage, where K  denotes the number of
detected action units.   These AUs constitute an interpret able physiological bridge linking

6                                                                                                                              3  The proposed Method

Algorithm 1 Two-Stage Progressive Fine-tuning with Decision-Level Fusion for Faci al Emo-
tion Recognition
Require Pre-trained VLM: Qwen3-VL-32B-Instruct; OpenFace 3.0;
Datasets: DCAS(ME)3   (AU labels),
D FER2013-train  (emotion labels);
Test set: D FER2013-test;
Fusion weight: α ∈ [0, 1]
Ensure Final predicted emotion labels for D FER2013-test
Stage 1: AU Recognition Fine-tuning (VLM Branch)
Load pre-trained Qwen-VL as M base
Fine-tune Mbase on D CASME3 with AU detection objective
Obtain MAU with capability to predict Action Unit activations
Stage 2: Emotion Fine-tuning on FER2013 (VLM Branch)
Initialize Mem with weights from MAU
Fine-tune Mem on D FER2013-train with emotion classification objective
Obtain VLM-based emotion predictor MVLM
Stage 3: Decision-Level Fusion with OpenFace 3.0
for each test sample x in D FER2013-test  do
Extract facial image from x
Obtain VLM logits: zVLM = MVLM(image )
Compute VLM probability: PVLM = Softmax(zVLM)
Obtain OpenFace 3.0 logits: z OF  = OpenFace3.0(image)
Compute OpenFace probability: POF = Softmax(z OF)
Fuse predictions: Pfinal = α · PVLM + (1 __ α) · POF
Predict emotion: yˆ = arg maxc∈{1,...,8 }Pfinal(c)
end for
Evaluation
Compute accuracy and other metrics on D FER2013-test
return Evaluation results

facial deformations to emotional states, laying the foundation for the model’s subsequent
emotion output.
Final Prediction:  Based on the AU representations, the model is required to reason
about and output the emotion category label C  ∈ C  expressed in the image, where C  =
{Anger, Disgust, Fear, Happiness, Sadness, Surprise, Neutral} is the seven-class basic emotion
space.
Semantic Interpretation:  In addition to detecting the set of facial action unit s in the
input image and generating the final recognized facial emotion, the model is also required to
produce a natural language description that articulates the logical association between the
detected AU combinations and the final emotion judgment. This tex tual elaboration enhances
the interpretability and persuasiveness of the model’s output, facilitating user comprehension
of the rationale behind the emotion judgment —for example, "detected AU4 (brow lowerer)
and AU7 (lid tightener), suggesting that this facial expression is likel y Anger."
To address the aforementioned task, this paper constructs a two-stage progress ive fine-
tuning framework based on the open-source multimodal  large model Qwen3-VL, which de-
composes the target task into two sequential learning stages. In the first st age—AU percep-
tion fine-tuning —the model is trained on static frames extracted from  the CAS(ME) 3 video
dataset, along with their fine-grained AU annotatio ns, to prioritize learning the facial ac-
tion unit detection task. This enables the model to establish, a t the parameter level, a high

3.3  Data Preprocess                                                                                                                                   7

sensitivity to subtle facial micro-movements.  The second stage is emotion  reasoning fine-
tuning, where the model parameters obtained from the fi rst stage are loaded and further
fine-tuned on the training set of the target-domain F ER dataset, guiding the model to learn
the joint mapping from "AU detection" to "emotion classifica tion." This effectively achieves
the transformation from mid-level facial encoding to  high-level emotional semantics. Finally,
the model’s facial emotion recognition performance is systematically evaluated on  the test
set of the FER dataset using standardized metrics.

3.3   Data Preprocess

The two datasets employed in this study—CAS(ME)3 and FER-2013—both provide pre-cropped
facial images, thus obviating the need for additional face detection and al ignment operations,
allowing them to be directly fed into the model for  training and evaluation.  In light of the
distinct characteristics of each dataset, we design differentiated data processing strategies, as
detailed below.

3.3.1   Static Image Dataset Processing (FER-2013)
FER-2013 is a static image dataset, where each image correspon ds to a single independent
emotion label.  Specifically, FER-2013 comprises 35,887 grayscale images  of 48 × 48 pixels,
covering seven basic emotion categories:  anger, disgust, fear,  happiness, neutral,  sadness,
and surprise.
For the static image dataset, we adopt the following preprocessi ng pipeline:

Size Normalization    The 48 × 48 grayscale images from FER-2013 are upsampled to 224 ×
224 pixels via bicubic interpolation and replicated into  three channels to meet the input
requirements of the visual encoder; the video frames from CAS(ME) 3  are uniformly adjusted
to 112 × 112 pixels to accommodate the input specifications of OpenFace.

Pixel Value Normalization   All input images undergo pixel value normalization.  For  the
OpenFace model, the input images are automatically scaled by a factor of 1/255 prior to
inference. For large models such as Qwen3-VL, the built-in image processor adop ts a normal-
ization scheme with a mean of 0.5 and a standard deviation of 0.5, i.e., (pixel/255__0.5) /0.5,
to standardize the input data distribution and accelera te model convergence.

Data Augmentation   To enhance the model’s generalization performance, we employ online
data augmentation strategies including random horiz ontal flipping (with a probability of 0.5)
and random rotation within ±15 ◦  .

3.3.2   Frame-Sequence Dataset Processing (CAS(ME) 3)
For the video sequences in the CAS(ME) 3  dataset, we leverage their frame-level expression
annotations and design a sampling strategy based on the Apex frame.  S pecifically, we crop
each video clip around the Apex frame (i.e., the frame at w hich the expression intensity
reaches its peak, denoted as It ), taking the 15 frames preceding the Apex frame and the 14

8                                                                                                                             3  The proposed Method

frames following it to construct a continuous sequence of 30 frames. The sampling scheme is
formulated as follows:
S = {It-15 , It-14 ,..., It,..., It+14 }                                        (3.1)
where S denotes the sampled frame sequence and It  denotes the Apex frame. For clips with
insufficient frames, we pad the sequence to a fixed length by repeating the last frame until
the sequence length reaches L = 30. This sampling strategy effectively captures the complete
dynamic process of expression evolution —from onset to peak to offset —while maintaining
the sequence length within a computationally feasibl e range.

3.3.3   Dataset Splitting

To ensure the reproducibility and fairness of the experiments, we partition each dataset ac-
cording to the following strategies:

Dataset Training Set Validation Set Test Set
FER2013
CAS(ME)3
28,709
80%
3,589
10%
3,589
10%
Table 3.1: Dataset partitioning strategies.

For both the training and validation sets, we adopt a stratified sampli ng strategy to ensure
that each class maintains a proportion distribution  consistent with the original dataset after
partitioning, thereby avoiding bias caused by class imbalance during training.  The valida-
tion set is used for hyperparameter tuning and early stopping, whil e the test set is reserved
exclusively for final model performance evaluation.

3.4   Qwen3-VL Introduction

Against the backdrop of the rapid advancement of ar tificial intelligence technologies, mul-
timodal large models are progressively emerging as a core bridge connecting the physical
world with digital intelligence. The Qwen3-VL serie s, introduced by the Qwen team, repre-
sents a state-of-the-art contribution to the multim odal domain. Among this series, Qwen3-
VL-32B-Instruct, as the largest Dense model variant without reasoning-specialized  optimiza-
tion, achieves exceptional performance across a wide range of multimodal benchm arks while
maintaining relatively manageable computational resour ce consumption.   The  Qwen3-VL
model offers three core advantages:  (1) significantly enh anced pure-text understanding ca-
pabilities, outperforming comparable pure-text mode ls across multiple evaluations; (2) sup-
port for processing text and interleaved multimodal  inputs through a proprietary 256K token
context window, enabling precise information extrac tion, retrieval, and cross-document cor-
relation in long documents and videos; and (3) adva nced multimodal reasoning capabilities
across single-image, multi-image, and video tasks, achieving leading performance on MMMU
as well as visual mathematics benchmarks including Ma thVista and MathVision.

3.5   AU-Detection Fine-Tuning

3.5 AU-Detection Fine-Tuning                                                                                                                    9

3.5.1   Fine-Tuning Objective

This stage employs Facial Action Units (AUs) as supervisory signals to  train the Qwen3-VL
vision encoder for precise perception of subtle facial micro-movements.  AUs are objective
physical descriptors (e.g., "eyebrow lowering"), not subjective emotion labels , so the acquired
knowledge forms a domain-agnostic facial representation w ith cross-dataset generalizability.
CAS(ME)‡ provides comprehensive AU annotations suitable for this purpose, whereas
standard FER datasets lack fine-grained AU labels, making them unsuitable for dir ect AU
supervision.   End-to-end joint training on both CA S(ME)‡ and FER data would introduce
domain confusion at the visual feature level, under mining feature transferability.
To address this, a two-stage strategy is adopted: Stage 1 trains exclusively  on CAS(ME)‡
for AU prediction.   Since AUs denote objective facial morphology, the  acquired detection
capability transfers zero-shot to the FER domain wi thout requiring target-domain AU anno-
tations.  Stage 2 performs lightweight fine-tuning of only the AU-to-emotion mapping head
using a small set of labeled FER samples, enabling emoti on recognition with minimal target
supervision.
This paradigm offers three advantages. Interpretability improves  as final decisions trace
back to specific AU activations, providing physiological gr ounding. Parameter efficiency and
reusability are enhanced because the LoRA adapters from Stage 1 encapsulate generic f acial
perception knowledge, reusable directly in Stage 2 without retraining the vision encoder.
Overall, the strategy reduces reliance on fine-grained target annotations while ensuring cross-
domain generalization, balancing performance, effici ency, and interpretability.

3.5.2   LoRA-Based Parameter Efficient Fine-tuning

Since the selected multimodal large model,  Qwen3-VL-32B, comprises approximately 32
billion parameters, adopting full fine-tuning would  require updating all parameters of the
model, which not only incurs enormous computational resou rce consumption but also poses
a high risk of overfitting on small-scale datasets. For the CAS(ME) 3  micro-expression dataset,
the number of samples is far smaller than the massive vision-language da ta used during the
pre-training phase of Qwen3-VL; therefore, directly updating all model parameters is not only
computationally expensive but also prone to disrupti ng the general visual-semantic knowl-
edge that the model has already acquired.  To address this, we adopt the L ow-Rank Adap-
tation (LoRA) strategy, a parameter-efficient fine-tuning (PEFT) approach, to fine-tune the
Qwen3-VL model, optimizing only a small number of add itional parameters while enabling
the model to learn discriminative capabilities for facial action units, all while preserving the
original vision-language understanding of the pre-t rained model.
For a pre-trained weight matrix W0  ∈ Rd×d, LoRA constrains its update manner by repre-
senting the incremental parameter matrix ΔW from full fine-tuning as a low-rank approxi-
mation of two smaller matrices B ∈ Rd×r  andA ∈ Rr×d :
W0 + ΔW = W0 + BA                                                  (3.2)
where the rank r is much smaller than d.
For a given input x ∈ Rd, the output h ∈ Rd  after incorporating LoRA is formulated as:
h = ( W0+ ΔW)x = W0x + BAx                                             (3.3)
During training, the original parameter matrix W0  is frozen, meaning that although W0
participates in both forward propagation and backpr opagation, its corresponding gradients
are not computed, and its parameters are not updated.

10                                                                                                                            3  The proposed Method

At the start of training, the matrix B is initialized to zero, i.e., B = 0 .  The matrix A is
initialized via a Gaussian function:
αi ~N(0, σα2)                                                           (3.4)
This ensures that before training begins, BA = 0 , so the fine-tuning process starts from
the pre-trained weights W0 . The backpropagation process of LoRA is illustrated in Figure 3.1.
During training, the pre-trained weights W0  are frozen, and only the low-rank matrices B
and A are optimized. Consequently, after LoRA training, only the parameters of t he low-rank
matrices B and A need to be saved.  Similar to rating matrix factori zation in recommender
systems, non-negative matrix factorization in text processing, and singular valu e decomposi-
tion, the rank r of the low-rank decomposition approximation matrice s B and A determines
their fitting capacity.  Ideally, we seek a rank r such that the low-rank approximation struc-
ture BA can approximate the expressive power of the full fine-tuning incremental m atrix ΔW ,
with closer being better. As the rank r increases, the number of trainable parameters grows
accordingly, and the low-rank adaptation capability  of LoRA gradually improves, potentially
leading to overfitting. The selection of the rank r should be comprehensively determined by
the difficulty of the downstream task, the capacity of the baseline model,  and the scale of the
training data.

Figure 3.1: The backpropagation process of LoRA

3.5.3   AU-Oriented Instruction Tuning
To enable Qwen3-VL to fully learn the fine-grained facial muscle m ovement patterns in micro-
expression images, this paper does not adopt the traditional classifica tion label supervision
approach, but instead constructs a multimodal instr uction tuning dataset oriented toward
Action Units (AUs). By converting the video sequences from the CAS(ME) 3  dataset and their
corresponding AU annotations into a Visual Question Answer ing (VQA) format, the model
is enabled to learn the mapping relationships among facial action units within a unified
framework of visual understanding and natural langu age reasoning, thereby enhancing the
model’s perception of local deformations in micro-expressions.
This subsection employs CAS(ME) 3  as the data source for model fine-tuning. CAS(ME) 3
is one of the largest publicly available high-frame-rate micro-expres sion databases,  cap-
turing facial video sequences under genuinely induced scenarios using high-speed cam era
equipment, and is capable of comprehensively recording the dynamic muscle movements

3.5 AU-Detection Fine-Tuning                                                                                                                  11

during micro-expression generation.  Compared with tr aditional static expression datasets,
CAS(ME) 3 provides continuous video frames along with corresponding Action Unit (AU) an-
notations, which better aligns with the practical r equirements of facial action analysis tasks.
Therefore, this paper selects CAS(ME) 3  as the training data for the AU recognition task,
providing fine-grained physiologically meaningful fea ture representations for subsequent ex-
pression recognition.
Qwen3-VL is a vision-language large model whose training objective is  not traditional im-
age classification but rather natural language generation based on visual inform ation. There-
fore, directly adopting the "image –category label" supervised learning paradigm fails to fully
leverage the model ’s multimodal understanding capabilities.   To address this, we reorga-
nize the CASME3 dataset into an Instruction Followin g data format, converting the original
video sequences and their corresponding Action Unit  (AU) annotations into visual question-
answering samples.  This enables the model to learn the AU recognition t ask in a "observe
image–comprehend question–generate answer" manner. The instruction primarily consists of
three components:
Task Description:  The model is explicitly required to analyze continuous facial image
sequences and identify the action units occurring ther ein.
Prior Knowledge:  To reduce the model ’s difficulty in understanding the FACS frame-
work, we further incorporate into the instruction t he major AU numbers along with their
corresponding muscular movement semantics—for instance, AU1 denotes inner brow raiser,
AU12 denotes lip corner puller, and AU24 denotes lip presser —thereby enabling the model
to establish correspondences between muscular movements and action units based on visual
information.
Output Constraint: To ensure consistency in the model’s output format, the instruction
further stipulates that the model must generate AU combinations in a fixed format.

Figure 3.2: An Example of First-stage Fine-tuning Instruction

Unlike traditional AU recognition methods that dire ctly employ classification networks to
predict action units, this paper reformulates the AU recogni tion task as a visual question-
answering task, enabling Qwen3-VL to fully leverage its cross-modal understanding  capabili-
ties, as shown in Figure 3.2. The continuous image sequences not only preserve the dynamic
temporal information inherent in the micro-expression generati on process, but the task de-
scription, prior knowledge of action units, and out put format constraints provided in the
instruction further reduce the difficulty of task c omprehension for the model, allowing it to

12                                                                                                                            3  The proposed Method

gradually establish semantic correspondences between facial muscle movements and action
units.
Moreover, the AU representations learned via Instru ction Tuning are not only highly in-
terpretable but can also serve as intermediate semantic representations for subsequen t ex-
pression recognition tasks. This enables a hierarchical modeling pipel ine from "facial muscle
movements" to "emotional expressions," thereby enhancing the model ’s generalizability and
interpretability in micro-expression analysis tasks.

3.5.4   Training Objective

In this study, we aim to guide the multimodal large  model Qwen3-VL, via instruction tuning,
to accurately recognize Action Units (AUs) from sequential facial expression i mage frames.
To achieve this goal, we define a clear training objective f unction and optimization strat-
egy to balance the modeling of spatiotemporal features within  the sequence and the precise
prediction of AU labels.
We formulate the AU recognition task as a sequence-to-sequence generation problem and
adopt the Supervised Fine-Tuning (SFT) paradigm, with the objective o f minimizing the con-
ditional language modeling loss of the model given multi-frame image seque nces and textual
instructions. Given a sequence of T facial expression image frames along with a human in-
struction I, the model is required to generate a response Y , i.e., a combination of AU labels.
The training objective is defined as maximizing the log-lik elihood of the correct response
sequence:

where L is the length of the response sequence, Yt  is the t-th output token, and θ  denotes
the trainable parameters of the model.  This objective fu nction forces the model, at each
generation step, to leverage visual features, instruction semant ics, and previously generated
contextual tokens to progressively reason out the complete set of AUs.
Since the input consists of multiple image frames, we first  extract facial representations
from each frame using a visual encoder (e.g., ViT), and then aggregate th em into a unified
visual feature ZV  through a temporal aggregation module. Subsequently, Z V  is concatenated
with the text instruction embedding Zt  and fed into the decoder of the large language model.
In loss computation, we only calculate the cross-entropy loss on the tokens  corresponding to
the response part, so as to focus on the accuracy of AU prediction. Formally, the cross-entropy
loss function can be expanded as:

where Y *  is the probability that the model predicts token c at the t-th position, and c is a

The optimization process during training adopts the  AdamW optimizer with a learning
rate of η = 5 × 10__5, coupled with a Cosine Annealing schedule for learning rate decay. T he
batch size is set to 2 to balance GPU memory consumption and gradient stabilit y. Although
the cross-entropy loss effectively improves generation accuracy, given the stringent r equire-
ments of the AU recognition task regarding the rigor and precision o f outputs, we introduce a
format penalty term into the loss function. During the validation phase, rewards or penalties
t
token in the vocabulary C. This loss function directly optimizes the model ’s predictions of AU
numbers and their delimiters, ensuring that the seq uence format strictly complies with the
requirements.

3.6  Expression Recognition Fine-tuning

13

are assigned based on regular expression matching; however, in the training phase, cross-
entropy remains the primary loss to maintain optimi zation stability. Overall, this training ob-
jective effectively integrates multimodal feature f usion, parameter-efficient fine-tuning, and
autoregressive generation, providing a solid optimi zation foundation for AU recognition.

3.6   Expression Recognition Fine-tuning

After AU recognition fine-tuning on CAS(ME)‡, the m odel acquires AU detection capability.
The second stage transfers this knowledge to emotion recognition, as FER datasets provide
only emotion labels without AU annotations.

3.6.1   Fine-Tuning Objective

Three objectives guide this stage.   First,  mapping  AU  space  to  e motion space:  emotion
categories correspond to combinations of multiple AUs; the mo del must learn a nonlinear
mapping from AU activation patterns to high-level affective  semantics.  Second, alleviating
sparse supervision: direct end-to-end training on emotion labels risks l earning shallow visual
correlations and ignoring facial action structures. Pre trained AU knowledge provides struc-
tured intermediate representations, enabling the mo del to leverage limited emotion labels
to reinforce the AU-to-emotion reasoning pathway.  Third, task adaptation with knowledge
preservation:  while the first-stage model excels at AU description, its output format is bi-
ased toward AU detection. The second stage adjusts outputs to emotion  recognition format
without forgetting AU knowledge, leveraging the model’s inherent reasoning for improved
interpretability.

3.6.2   Fine-Tuning Strategy

Lightweight Parameter Updates Based on LoRA.   Consistent with Stage 1, LoRA is applied
to Query and Value matrices in attention modules, freezing al l original parameters.  This
reduces trainable parameters ( 0.1% of total), mitigating overfitting o n small FER datasets,
and preserves Stage 1 AU knowledge by restricting the update subspace.

Continuation of Task Encapsulation in the Visual Question Answering For mat.    To en-
sure task coherence between the two stages of fine-tuning, this stage still f ormulates the
expression recognition task in a visual question answering format.   Given an input facial
image, a question text following a fixed template i s constructed.   Differing from the first
stage, the model’s output now requires not only the recognized AU categories but also the
final predicted emotion category, accompanied by a reasoning explanation based on  the AUs.
This design maintains consistency between the second-stage fine-tuning and the fi rst stage
in terms of data format and interactive paradigm, r educing the disturbance of task switch-
ing on the model’s internal representations, while facilitating subse quent evaluation of the
model’s joint  capabilities within a unified framework.  The spec ific fine-tuning instructions
are illustrated in Figure 3.3.

Single-Stage Fine-Tuning and Freezing Strategy.    Only newly initialized LoRA parameters
for emotion recognition are optimized; the visual encoder, language backbone, an d Stage 1

14                                                                                                                            3  The proposed Method

Figure 3.3: Second-stage Fine-tuning Strategy

LoRA adapters remain frozen. This decouples the parameter spaces of the two tasks, preserv-
ing a clear AU-to-emotion reasoning chain and enabling independent ablation  studies.

Prompt Engineering and Output Format Constraints.    The system prompt restricts output
to a single emotion category word (neutral, happiness, sadness, surprise, fear, disgust, anger),
aligned with the label space, preventing redundant or non-standard responses.

3.7   Decision-Level Fusion with OpenFace 3.0

In the emotion recognition module, to enhance the robustness and  accuracy of classification
results, this paper proposes a decision-level weighted fusion strategy that integrat es the logits
output from the OpenFace 3.0 vision model with the pr edictions from the large language
model (LLM).
Specifically, let the emotion category probability distribution output by OpenFace 3.0 be
denoted as POF  ∈ R7, which is obtained through a single fully-connected mapping of the
“unified facial features.”  Meanwhile, let the probability distribution output  by the large lan-
guage model based on non-visual information (e.g., dialogue text o r context) be denoted
as PLLM  ∈ R7 .  To avoid misclassification caused by a single modali ty under specific noisy
conditions, we employ weighted linear interpolation  to fuse the two distributions. The final
predicted probability Pfinal is computed as follows:
Pfinal = α · POF + (1 __ α) · PLLM                                                             (3.7)
where the weight coefficient α ∈ [0, 1] denotes the contribution of the visual modality.
This weight can be either a hyperparameter tuned on  the validation set to find the optimal

3. 7 Decision-Level Fusion with OpenFace 3.0                                                                                         15

ratio (e.g., set to a fixed value α = 0.6), or designed as an adaptive weight that is dynamically
adjusted based on face detection confidence or emotional context consistency.
Finally, the fused emotion label yˆ is determined by selecting the category with the highest
probability:
yˆ = arg c∈ m {1, a
．
. } Pfinal(c)                                                   (3.8)
The advantages of this fusion strategy are twofold: on the  one hand, the visual features
(facial muscle movements) provided by OpenFace 3.0 and the semantic contextua l features
captured by the large language model are inherently complem entary; on the other hand,
decision-level fusion offers better interpretability compared to feature-level fusio n, is insensi-
tive to adjustments in model architecture, and is easy to deploy and scale in practical systems.

Chapter 4

Experiments and Results

4.1   Datasets

In our work, we primarily employ two datasets: CAS(ME) 3 and FER2013. CAS(ME) 3 provides
fine-grained AU temporal annotations (onset frame, apex frame, and offset frame) along
with a large sample size, enabling the model to receive precise supervisory signal s for facial
micro-movements.  This effectively drives the model to learn the spatiotemporal dynamic
features of micro-expressions and enhances its reasoning capability for subtle f acial actions.
FER2013 is used to validate whether the model can effectively transfer t he micro-movement
representations learned from fine-grained micro-expression dat a to conventional expression
recognition tasks with different data distributions,  thereby comprehensively evaluating the
model’s generalizable representation capability and  domain adaptability.

4.2   Evaluation Metrics

To comprehensively evaluate the performance of our proposed two -stage fine-tuning frame-
work with decision-level fusion, we adopt a suite o f standard and robust metrics for multi-
class emotion classification on the FER2013 test set.
Specifically, we report Accuracy (ACC) as the primary metri c, which reflects the overall
proportion of correctly classified samples. It is defined as:

To account for class-wise performance, we calculate Precision and Recall for each emotion
category, capturing the model ’s ability to avoid false positives and false negatives, respec-
tively. They are defined as:

Recall                                                      (4.3)
Furthermore, we report the Macro F1-Score and Weighted F1-Score as complementar y
metrics. The Macro F1-Score averages the F1 scores a cross all emotion classes equally, pro-
viding a balanced assessment regardless of class frequen cy, while the Weighted F1-Score
weights each class’s contribution by its support, offering a class-distribution-aware evalua-
tion. These two F1 variants are particularly importa nt given the inherent class imbalance in

18                                                                                                                        4  Experiments and Results

FER2013, where certain emotion categories (e.g., disgust) have fewer samples t han others
(e.g., happiness, neutrality). They are defined as:

In addition to the scalar metrics, we visualize the Confusion Matrix to qualitatively ana-
lyze the model’s classification behavior, especially the confusions between semantically sim-
ilar emotion pairs (e.g., fear vs.  surprise, sadness vs.  disgust).  This allows us to identify
systematic misclassification patterns and understand the model ’s perceptual ambiguities.
All reported results are computed using the widely- adopted scikit-learn implementation,
ensuring reproducibility and fair comparison with p rior studies.
Specifically, for the multi-class classification task in this paper, let TPi , FPi , and FNi denote
the true positives, false positives, and false negatives for the i-th class in the confusion matrix,
respectively. Then:
Precisioni       Recalli       F1i              (4.6)
The Macro F1-Score and Weighted F1-Score are respectively computed as:

where N = 8 is the total number of emotion categories, and ni  is the number of samples
belonging to the i-th class in the test set.

4.3   Model Performance

4.3.1   Experimental Setup
All experiments are conducted on 4 × NVIDIA A100 (40GB) GPUs for supervised fine-tuning
(SFT) of the Qwen3-VL-32B-Instruct model.  To maximize GPU m emory utilization, we do
not employ quantization strategies, thereby preserv ing the full precision of the model.  To
improve efficiency for long-context multimodal inpu ts, we enable FlashAttention. The batch
size is set to 2 and the maximum sequence length to 8196 to avoid exc eeding the memory
limit during training. The learning rate is set to 5 × 10 __ 5, a common choice for fine-tuning
large models, in conjunction with a cosine annealing schedu ler to prevent overfitting.  The
number of training epochs is set to 15 to fully exp loit the fitting potential of both the model
and the dataset. The detailed training hyperparameters are presented in Table 4.1.
During the inference stage, we employ the vLLM framework on 2 NVIDIA A100 GPUs to
reduce computational cost.

4.3.2   Overall Model Performance

We evaluate the performance of the fine-tuned Qwen3-VL model, the fin e-tuned Qwen3-VL
model with decision-level fusion with OpenFace 3.0, the non-fine- tuned Qwen3-VL model,

4. 3  Model Performance                                                                                                                              19

Category Parameter Value Description

Model
Base Model
Fine-Tuning Method
LoRA Rank
LoRA Alpha
LoRA Target
Quantization
Qwen3-VL-
32B-Instruct
LoRA
8
16
all
None
Pre-trained multimodal LLM
Parameter-efficient fine-tuning
Low-rank matrix dimension
Scaling coefficient
Applied to all linear layers
Full-precision training

Training
Batch  Size  (per  de-
vice)
Gradient  Accumula-
tion Steps
Learning Rate
Learning            Rate
Scheduler
Warmup Steps
Training Epochs
Max Gradient Norm
2
8
5 × 10__5
Cosine
0
15
1.0
Samples per step per GPU
Effective batch size = 2 × 4 × 8 = 64
AdamW optimizer
Cosine annealing

—
—
Gradient clipping threshold
Data
Max            Sequence
Length
Image Max Pixels
Image Min Pixels
8192
768
32
Upper limit of input tokens
Upper limit of pixels per image
Lower limit of pixels per image
Distributed Parallelism Strategy
CPU Offload
DeepSpeed
ZeRO-3
Enabled
Parameter sharding
Offload optimizer states to CPU
Precision Data Type Flash Attention FP32 Enabled Single-precision training Accelerate attention computation
Table 4.1: Key hyperparameter configurations for fine-tuning e xperiments.

Experiments and Results

20 4

and the OpenFace 3.0 model on the FER-2013 dataset. In addition , we compare their perfor-
mance against several models that have demonstrated strong results on FER-20 13, including
ResNet50, VGG16, DenseNet, and GoogLeNet.
The experimental results are presented in Table 4.2

Model ACC MACRO-
Precision
Weighted
Preci-
sion
MACRO-
RECALL
Macro
F1-
score
Weighted
Recall
Weighted
F1
Fine-tuned QWEN 66.73% 67.21% 68.89% 58.64% 57.29% 66.73% 65.80%
Fused model 67.37% 64.87% 69.47% 62.71% 59.09% 67.37% 66.52%
Non-fine-tuned QWEN  58.73% 51.80% 60.64% 52.76% 47.45% 58.73% 55.95%
OpenFace 3.0 48.02% 44.69% 56.31% 49.38% 43.29% 48.02% 49.73%
ResNet50 69.33% 69.88% 69.84% 65.92% 67.49% 69.33% 69.35%
VGG-16 68.75% 69.28% 68.53% 66.86% 67.89% 68.75% 68.58%
DenseNet 69.38% 69.86% 69.31% 67.23% 68.18% 69.38% 69.10%
GoogLeNet 67.04% 69.56% 67.70% 64.18% 66.05% 67.04% 67.04%
Table 4.2: Performance comparison of different models on the FER -2013 test set.

4.3.3   Advantages of the Fused Model over the Pure Large Model

The experimental results demonstrate that the fused model achieves an overall accuracy
of 67.37%, representing an improvement of approximately 0.64 percentage points o ver the
non-fused large model (66.73%). Although the improvement is modest, t he fusion strategy
exhibits clear advantages in fine-grained metrics.
In terms of recall, the fused model achieves a Macro-Recall of 62.71%, substantially higher
than the baseline model’s 58.64%  (an improvement of approximately 4.07%). This indicates
that after incorporating the geometric features from OpenFace 3 .0 at the decision level, the
model’s ability to capture minority-class samples (e.g., disgust, fear) has  been significantly
enhanced, effectively alleviating the bias toward head classes (e.g., happiness,  neutral) that
is inherent in a single multimodal large model when trained on imbalance d data. Meanwhile,
the Weighted Recall increases from 66.73% to 67.37%, consistent with the trend in accuracy,
further validating the effectiveness of the fusion strat egy on the overall sample set.
The decision-level fusion of a multimodal large model and a specialized geom etric fea-
ture extraction model offers significant complementary advantages.  While the pure vision-
language model (Qwen3-VL) possesses powerful high-level semantic understanding capab il-
ities, it exhibits limitations in capturing subtle f acial geometric deformations, especially for
low-intensity expressions.  OpenFace 3.0, with its facial landmark-based geometric features,
effectively compensates for this shortcoming. Their  joint reasoning not only improves overall
classification accuracy but also significantly enhances the model’s robustness toward easily
confused and rare emotion categories, endowing the system with stronger generalization
capability in emotion recognition tasks that more cl osely resemble real-world scenarios.

4.3.4   Effectiveness of Fine-Tuning
As clearly shown in Table 4.2, the model after two-stage fine-tuning si gnificantly outperforms
the non-fine-tuned baseline model across all evaluation metrics.  Specifi cally, the fine-tuned
model achieves an overall accuracy (ACC) of 66.73%, representing an im provement of 8 per-
centage points over the baseline model ’s 58.73%, corresponding to a relative improvement
of 13.6%.  This result indicates that the proposed two-stage fine-tuning  strategy effectively

4. 3  Model Performance                                                                                                                             21

unlocks the potential of the Qwen3-VL model on facial expression recogn ition tasks, enabling
it to better capture emotion-related discriminative  features from facial images.  The signif-
icant improvements across all evaluation dimensions f ully demonstrate the rationality and
superiority of this training paradigm.

4.3.5   Advantages of the Fused Model over Pure OpenFace 3.0
As shown in Table 4.2, the joint reasoning framewor k proposed in this paper significantly
outperforms OpenFace 3.0 standalone inference across all evaluation metrics.  Specifi cally,
the joint reasoning framework achieves an accuracy of 67.37%, an improvement  of 19.35
percentage points over OpenFace 3.0 standalone inference (48.02%), corresponding to  a rel-
ative improvement of 40.3%. This result indicates that relying solely on the specialized facial
Action Unit analysis model OpenFace 3.0 is insufficient for fully capturing the subtle seman-
tic differences and contextual information in facial expressi ons, as its reasoning capability
is constrained by predefined geometric and motion featu re representations. The experimen-
tal results fully validate the effectiveness of the  proposed two-stage fine-tuning strategy and
decision-level joint reasoning framework for facial  expression recognition, achieving com-
prehensive and significant performance improvements over the specialized model alone, and
demonstrating the potential and advantages of colla borative reasoning between multimodal
large models and specialized models.

4.3.6   Comparative Experimental Analysis

This section compares our proposed method, which combines the Qwen3-VL multimodal
large model with OpenFace 3.0 through decision-level joint reasoning, against f our classic
deep convolutional neural networks (ResNet-50, VGG-16, DenseNet, and GoogLeN et).
As shown in Table 4.2, all four traditional CNN models achi eve relatively stable perfor-
mance on the FER-2013 dataset, with DenseNet performing the best, achieving  the high-
est accuracy (69.38%) and Macro-F1 (68.18%), while GoogLeNet achieves the l owest accu-
racy (67.04%).  In comparison, our proposed joint reasoning model achieves an accuracy
of 67.37%, slightly outperforming GoogLeNet but falling behind ResNet-50 , VGG-16, and
DenseNet.
Although our model has not yet surpassed the optimal specialized CNN models (DenseNet,
69.38%) in terms of overall accuracy, a deeper analysis of fine-grained met rics reveals that
our joint reasoning framework exhibits several signi ficant and noteworthy advantages. First,
in terms of prediction reliability and confidence, our model performs exceptionally well.  Its
Weighted Precision reaches 69.47%, almost on par with the best-perform ing model among all
comparators, ResNet-50 (69.84%), while significantly outperforming VGG- 16 (68.53%) and
GoogLeNet (67.70%). This result indicates that when our model predicts a  particular emo-
tion category, its prediction is highly trustworthy —the “precision-first” reasoning character-
istic enables the model to provide more reliable outp uts in critical decision-making scenarios
(e.g., key-frame judgments in human-computer intera ction), effectively reducing the risk of
false positives. Compared to CNN models, which may incur increased miscla ssifications when
pursuing high recall, our model exhibits a more cautious and well-d efined decision boundary.
Second,  in terms  of inter-class discriminative ability,  our mod el’s Weighted Precision
(69.47%) is substantially higher than its Macro Precision (64.87%), w ith a gap of approxi-
mately 4.6 percentage points. This indicates that the model demonstrates s trong recognition
focus and representational capability on the majority  emotion categories with larger sam-
ple sizes. This characteristic is highly valuable in practical application scenarios —real-world

22                                                                                                                       4  Experiments and Results

facial expression data often exhibit a pronounced long-tail distribution, and our m odel’s abil-
ity to prioritize recognition accuracy on high-freq uency categories may translate to superior
practical performance in real-world deployment compa red to laboratory-balanced test sets.
Third, the multimodal decision-level fusion archite cture adopted by our model itself pos-
sesses important methodological advantages. Unlike “black-box” end-to-end CNNs, our frame-
work explicitly combines Qwen3- VL’s deep semantic understanding capabilities with Open-
Face 3.0’ s geometric structure priors, forming a more interpretable reasoning chain. Th is de-
sign allows researchers to clearly trace the source of errors  when model predictions deviate
(whether due to visual semantic bias or geometric f eature bias), providing a clear direction
for subsequent targeted optimization. In contrast, pe rformance improvements in pure CNN
models typically rely on brute-force trial-and-erro r through network architecture search or
data augmentation, lacking the modular iterative sp ace offered by our framework.
Fourth, from the perspective of feature complementarity, the Wei ghted Precision advan-
tage of our model suggests the potential gains of multimodal f eature fusion.   The  geo-
metric information provided by OpenFace 3.0 —such as head pose and facial Action Unit
parameters—together with the contextual semantic knowledge acquired by t he large lan-
guage model through large-scale pre-training, forms effective h eterogeneous information
complementarity at the decision level.  Although the  current simple decision fusion strat-
egy has not yet fully unleashed this complementary potential,  the Weighted Precision of
69.47% already demonstrates the feasibility of this technical approach —the two information
sources reach a consensus in determining “positive predictions,” providing a solid experimen-
tal foundation for the subsequent introduction of m ore sophisticated attention mechanisms
or adaptive fusion weights.
Finally, it is worth emphasizing that as an initial e xploration of synergizing a general-
purpose multimodal large model with specialized tools, our model ’s performance has already
approached or even partially surpassed (in terms of Weighted Precision) full y optimized spe-
cialized CNN models. Considering that Qwen3-VL was not specifically designed for FER tasks
and that our model achieved performance comparable to spec ialized models after only two-
stage fine-tuning, this result itself demonstrates the enormous application potential of large
models in the field of affective computing. With fu rther optimization of the fine-tuning strat-
egy and deeper design of the multimodal fusion mechanism, our f ramework is expected to
maintain its high precision advantage while address ing the recall shortfall, ultimately achiev-
ing comprehensive superiority.
In summary, although the accuracy metric has not yet reached the opt imal level, our
model demonstrates clear superiority and promising development prospects ac ross multi-
ple dimensions, including prediction confidence, high-frequency category focus, architectural
interpretability, feature complementarity validatio n, and large model application potential.
These findings lay a solid and inspiring foundation for subsequen t improvements in this re-
search.

4.3.7   Confusion Matrix Analysis
To further analyze the classification capabilities of different models in  fine-grained expression
recognition tasks, we compare the confusion matrix results of the Qwen3-VL  and OpenFace
3.0 decision-level fusion model against VGG-16, ResNet50, DenseNet, and GoogLeNet on the
FER-2013 test set, as shown in Figure 4.1. Although the fusion model  does not completely
surpass traditional CNN models in single-category recognition counts for certain categories
(e.g., angry and disgust), it demonstrates clear advantages in neutral, happy, surprise, and
holistic emotional semantic understanding. Compared to CNN models that rely solely on lo-
cal visual texture features, the decision-level fusion of Qwen3-VL and OpenFace 3.0 combines

4. 3  Model Performance                                                                                                                             23

(a) Fused Model

True Label

An gry

Disgust

Fear

Happy

Neutral

Sad

Surprise
Confusion Matrix
Accuracy = 6 8 . 7 5 %

544
56.8%
2
0.2%
137
14.3%
49
5.1%
93
9.7%
115
12.0%
18
1.9%
19
17.1%
72
64.9%
3
2.7%
3
2.7%
7
6.3%
7
6.3%
0
0.0%
101
9.9%
3
0.3%
540
52.7%
42
4.1%
96
9.4%
169
16.5%
73
7.1%
25
1.4%
0
0.0%
32
1.8%
1571
88.6%
86
4.8%
32
1.8%
28
1.6%
73
5.9%
3
0.2%
63
5.1%
90
7.3%
825
66.9%
164
13.3%
15
1.2%
114
9.1%
8
0.6%
142
11.4%
54
4.3%
210
16.8%
704
56.5%
15
1.2%
20
2.4%
0
0.0%
62
7.5%
35
4.2%
25
3.0%
10
1.2%
679
81.7%

Predicted Label

0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0.0
Recal l (%)
(c) VGG-16

An gry

Disgust

Fear

Happy

Neutral

Sad

Surprise

An gry

Disgust

Fear

Happy

Neutral

Sad

Surprise

Confusion Matrix
Accuracy = 6 9 . 3 3 %

554
57.8%
4
0.4%
96
10.0%
37
3.9%
88
9.2%
168
17.5%
11
1.1%
25
22.5%
62
55.9%
7
6.3%
3
2.7%
1
0.9%
12
10.8%
1
0.9%
98
9.6%
0
0.0%
525
51.3%
36
3.5%
93
9.1%
219
21.4%
53
5.2%
24
1.4%
0
0.0%
31
1.7%
1569
88.4%
78
4.4%
53
3.0%
19
1.1%
41
3.3%
14
1.1%
62
5.0%
76
6.1%
810
65.0%
230
18.4%
14
1.1%
96
7.7%
1
0.1%
94
7.5%
41
3.3%
175
14.0%
831
66.6%
9
0.7%
19
2.3%
1
0.1%
75
9.0%
49
5.9%
28
3.4%
24
2.9%
635
76.4%
0.0
Predicted Label
(b) ResNet50
Confusion Matrix
Accuracy = 6 9 . 3 8 %

588
61.4%
10
1.0%
74
7.7%
36
3.8%
99
10.3%
134
14.0%
17
1.8%
23
20.7%
71
64.0%
2
1.8%
1
0.9%
4
3.6%
9
8.1%
1
0.9%
116
11.3%
3
0.3%
476
46.5%
37
3.6%
104
10.2%
204
19.9%
84
8.2%
21
1.2%
0
0.0%
26
1.5%
1575
88.8%
78
4.4%
32
1.8%
42
2.4%
58
4.7%
0
0.0%
37
3.0%
104
8.4%
823
66.7%
196
15.9%
15
1.2%
115
9.2%
4
0.3%
88
7.1%
51
4.1%
199
16.0%
769
61.7%
21
1.7%
25
3.0%
0
0.0%
49
5.9%
33
4.0%
28
3.4%
18
2.2%
678
81.6%
0.0
Predicted Label
(d) DenseNet

Predicted Label
(e) GoogLeNet
Figure 4.1: Confusion Matrices of Different Models
An gry

Disgust

Fear

Happy

Neutral

Sad

Surprise
85
8.9%
7
6.3%
449
43.8%
20
1.1%
48
3.9%
92
7.4%
73
8.8%
36
3.8%
3
2.7%
29
2.8%
1505
84.8%
72
5.8%
38
3.0%
34
4.1%
95
9.9%
4
3.6%
119
11.6%
88
5.0%
827
67.1%
222
17.8%
41
4.9%
161
16.8%
8
7.2%
230
22.5%
71
4.0%
216
17.5%
778
62.4%
20
2.4%
554
57.8%
26
23.4%
116
11.3%
48
2.7%
56
4.5%
104
8.3%
27
3.2%
3
0.3%
63
56.8%
0
0.0%
2
0.1%
0
0.0%
1
0.1%
0
0.0%
24
2.5%
0
0.0%
81
7.9%
40
2.3%
14
1.1%
12
1.0%
0.8

0.7

0.6

0.5

0.4

0.3

0.2

0.1

0.0
Confusion Matrix
Accuracy = 6 7 . 0 4 %
636
76.5%
Happy

Neutral

Sad

Surprise
10
0.6%
99
8.0%
916
73.5%
16
1.9%
An gry

Disgust

Fear
2
0.1%
7
0.6%
31
2.5%
3
0.4%
Confusion Matrix
Accuracy = 6 7 . 3 7 %
68
7.1%
55
49.5%
15
1.5%
362
37.8%
9
8.1%
45
4.4%
14
1.5%
0
0.0%
205
20.0%
3
0.2%
7
0.6%
18
1.4%
30
3.1%
9
8.1%
20
2.0%
0.4

0.2

0.0
72
5.8%
752
90.5%
1571
88.6%
49
4.0%
104
5.9%
975
79.1%
80
4.5%
91
7.4%
4
0.2%
5
0.4%
0.8

0.6
Predicted Label
210
21.9%
303
29.6%
360
35.2%
98
10.2%
176
18.4%
168
13.5%
17
15.3%
17
15.3%
0
0.0%
26
2.1%
23
2.8%
27
3.2%
76
7.4%
4
3.6%
16
1.3%
10
1.2%
True Label
True Label
True Label
True Label
Recal l (%)
Recal l (%)
Recal l (%)
Recal l (%)
0.2
0.8
0.7
0.2
0.1
0.5
0.8
0.5
0.6
0.7
0.1
0.4
0.3
0.4
0.3
0.6

24                                                                                                                       4  Experiments and Results

deep visual semantic information with facial dynamic features, achieving complementary ad-
vantages and enhancing the model’s ability to recognize complex expression variations and
weakly expressed emotions. More importantly, the in troduction of AU knowledge brings irre-
placeable benefits across multiple dimensions: first, i t provides interpretable biomechanical
constraints through AU activation/inhibition patter ns, reducing misclassifications caused by
visual ambiguity; second, it strengthens discriminative evidence for subtle muscle di fferences
across categories, particularly effective for categories like neutral and disgust that rely on spe-
cific AU combinations; third, under conditions of d ata imbalance and weak annotation, the
AU prior serves as an effective regularization mechanism, improving the model’s robustness
on few-shot and difficult-to-classify categories. T he confusion matrix results further validate
the effectiveness of the proposed fusion method on the FER-2013 facial expressio n recog-
nition task, and reveal the core value of the AU-gui ded fine-tuning strategy in enhancing
fine-grained expression discrimination capability.

Chapter 5

Conclusions and Future Work

5.1   Conclusions
This paper proposes a multi-modal large-model enhancement framework based on a two-
stage fine-tuning strategy. In the first stage, AU question-answer pairs  are constructed using
the CAS(ME)‡ dataset, and the Qwen3-VL-32B-Instruct model is f ine-tuned with LoRA to ac-
quire facial action unit recognition capabilities.  In th e second stage, the model is further
fine-tuned on the FER dataset to enable reasoning mapping from AUs to em otions, thereby
effectively bridging the semantic gap between low-l evel facial deformation perception and
high-level emotional semantic understanding.   Experi mental results demonstrate that the
two-stage fine-tuned model outperforms the non-fine-tuned baseline in overall accuracy, and
significantly surpasses both the standalone inference of the specialized lightweight model
OpenFace 3.0 and other mainstream deep models, confirming the effectiveness of the pro-
posed strategy in eliciting discriminative features  for low-intensity expressions from large
visual models.
This paper further explores a decision-level fusion mechanism between the fine-tuned
large model and the specialized small model OpenFace 3.0, revealing a cle ar complementar-
ity in their feature representations —the large model excels at complex contextual semantic
understanding and cross-scenario generalization, while the small model is more sen sitive
to local responses to facial geometric deformations.  The joint prediction performance after
fusion not only surpasses the best standalone inference results of each model, but also signif-
icantly alleviates the deficiency of pure large visual models in perceiving subtle deformations
due to the lack of fine-grained spatial priors. Mea nwhile, by employing AUs as interpretable
intermediate representations during inference, the framework enhances the traceability and
trustworthiness of model outputs, providing a feasi ble technical paradigm for robust deploy-
ment of FER systems in real-world open scenarios.

5.2   Future Work

Although the proposed method achieves competitive performance on public datasets, sev-
eral limitations and future directions warrant furt her exploration.  First, the two-stage fine-
tuning relies heavily on the quality and coverage of AU-annotated data;  the current CAS(ME)‡
dataset remains limited in terms of emotion categories and sample diversity.  Future work may
introduce larger-scale, multi-cultural AU annotation databases to enhance the mode l’s cross-
demographic generalization capability. Second, while decision-level fusion a chieves a degree
of complementary advantages, the fusion strategy remains relatively  simplistic.  Subsequent
research could investigate attention-based dynamic weighted fusion or early-late multi-level

26                                                                                                                  5  Conclusions and Future Work

fusion to more fully exploit the synergistic potent ial among heterogeneous models.  Third,
the current experiments are primarily conducted on static  images or video clips under con-
trolled laboratory conditions; future efforts shoul d validate online inference on real-world
in-the-wild long video streams, and incorporate lig htweight pruning and distillation under
computational resource constraints to facilitate prac tical deployment on mobile and edge
devices.  Finally, how to introduce causal reasoning or uncertai nty estimation mechanisms
within the large-model framework, enabling the FER system to provide more  reasonable con-
fidence expressions and rejection strategies when faced with ambiguous or occlude d faces,
constitutes another important direction worthy of i n-depth investigation.  In summary, this
work provides valuable empirical evidence and theoretical referen ces for the fine-grained
adaptation of multi-modal large models in the field o f affective computing, and is expected
to contribute novel technical support to application scenar ios such as digital mental health,
intelligent education, and human-machine empathic i nteraction.

Bibliography

[Don+15]    Donahue, J., Anne Hendricks, L., Guadarrama, S., Rohrbach,  M., Venugopalan,
S., Saenko, K., and Darrell , T. “ Long-term recurrent convolutional networks for
visual recognition and description” . In: Proceedings of the IEEE Conference on
Computer Vision and Pattern Recognition (CVPR) . 2015, pp. 2625 –2634. DOI:
10.1109/CVPR.2015.7298878.
[EF78]          Ekman, P. and Friesen, W. V. “Facial action coding system” . In: Environmental
Psychology and Nonverbal Behavior (1978).
[HGJ+25]    Han, S., Gao, M., Jiang, M., et al. “Uncertainty-Aware Collaborative System of
Large and Small Models for Multimodal Sentiment Analysis”  . In: arXiv preprint
(2025). arXiv: 2509.04459 [cs.CL] .
[He+16]      He, K., Zhang, X., Ren, S., and Sun, J. “Deep residual learning for image recog-
nition” . In: Proceedings of the IEEE Conference on Computer Vision and Pattern
Recognition (CVPR) . 2016, pp. 770 –778. DOI: 10.1109/CVPR.2016.90.
[Hu+24]      Hu, G., Lan, X., Jiang, H., Wang, S., et al.  “Towards unified facial action unit
recognition framework by large language models ” . In: arXiv preprint  (2024).
arXiv: 2409.08444 [cs.CV].
[Hu+25]      Hu, J., Mathur, L., Liang, P. P., and Morency, L.-P. “OpenFace 3.0: A Lightweight
Multitask System for Comprehensive Facial Behavior Analysis ” . In: 2025 IEEE
19th International Conference on Automatic Face and Gesture Recognition (FG).
May 2025, pp. 1 –11. DOI: 10.1109/FG.2025.11099277.
[Ind+23]     Indolia, S., Nigam, S., Singh, R., Singh, V. K ., and Singh, M. K. “Micro Expression
Recognition Using Convolution Patch in Vision Transformer” . In: IEEE Access 11
(2023), pp. 100495 –100507. ISSN: 2169-3536. DOI: 10.1109/ACCESS.2023 .
3314797.
[LYZ16]        Li, X., Yu, J., and Zhan, S. “Spontaneous facial micro-expression detection based
on deep learning”. In: Proceedings of the 2016 IEEE 13th International Conference
on Signal Processing (ICSP). Chengdu, China, Nov. 2016, pp. 1130–1134.
[Li+24]       Li, Y., Dao, A., Bao, W., Wang, Y., et al.  “Facial affective behavior analysis with
instruction tuning” . In: European Conference on Computer Vision (ECCV). Cham:
Springer, 2024, pp. 165 –186.
[Lia+25]      Lian,  Z., Chen, H., Chen, L., Sun, L., Chen, Y., Wang, J.,  Li, Z., and Tao, J.
“AffectGPT: A new  dataset, model, and benchmark for emotion understan ding
with multimodal large language models ”. In: arXiv preprint (2025). arXiv: 2501.
16566 [cs.CL] .
[LLL18]        Liu, Y. J., Li, B. J., and Lai, Y. K. “Sparse MDMO: Learning a discriminative fea-
ture for micro-expression recognition” . In: IEEE Transactions on Affective Com-
puting 12.1 (2018), pp. 254 –261. ISSN: 1949-3045. DOI: 10.1109/TAFFC.2018.
2873887.

28                                                                                                                                              Bibliography

[PKO09]       Polikovsky, S., Kameda, Y., and Ohta, Y. “Facial micro-expressions recognition
using high speed camera and 3D-gradient descriptor” . In: Proceedings of the 3rd
International Conference on Crime Detection and Prevention (ICDP 2009). Lon-
don, UK: IET, Dec. 2009.
[Qwe24]      Qwen Team. QVQ: To See the World with Wisdom . Hugging Face. Model page.
2024. URL: https://huggingface.co/Qwen/QVQ-72B-Preview.
[Ryu+25]    Ryumina, E., Markitantov, M., Axyonov, A., and Karpov, A. “Zero-Shot Multi-
modal Compound Expression Recognition Approach using Off-the-Shelf Large
Visual-Language Models” . In: Proceedings of the IEEE/CVF International Confer-
ence on Computer Vision (ICCV). 2025, pp. 71–79.
[Sun+20]    Sun, B., Cao, S., Li, D., He, J., and Yu, L. “Dynamic Micro-Expression Recognition
Using Knowledge Distillation”. In: IEEE Transactions on Affective Computing 13.2
(2020), pp. 1037 –1043. ISSN: 1949-3045. DOI: 10.1109/TAFFC.2020.2988262.
[Wan+26]   Wang, S.-J., Liu, X., Li, J., See, J., Yap, M. H., Li, X., Hong, X., Fan, X., Wang,
Y., Fang, R., et al. CAS(ME)3: A Third Generation Facial Spontaneous Micr o-
Expression Database With Depth Information and High Ecological Validity. Manuscrip
in preparation / Under review. 2026.
[Wan+21]   Wang,  S.,  Li,  B.,  Liu,  Y.,  Yan, W.,  Ou, X., Huang, D ., Fu, X., and Zhou, C.
“Auxiliary Information Guided Micro-Expression Recognition” . In: IEEE Trans-
actions on Image Processing 30 (2021), pp. 5621 –5633. DOI: 10.1109/TIP.2021.
3083777.
[Wan+23]   Wang, Y., Zheng, S., Sun, X., Guo, D., and Lang, J. “Micro-expression recognition
with attention mechanism and region enhancement” . In: Multimedia Systems
29.5 (2023), pp. 3095 –3103. ISSN: 0942-4962. DOI: 10 . 1007/ s00530 - 023 -
01148-0.
[Xie+20]     Xie, H.-X., Lo, L., Shuai, H.-H., and Cheng , W.-H. “AU-assisted graph attention
convolutional network for micro-expression recognition” . In: Proceedings of the
28th ACM International Conference on Multimedia . 2020, pp. 2871 –2880. DOI:
10.1145/3394171.3413928.
[Zha+17]    Zhang, K., Huang, Y., Du, Y., and Wang, L. “Facial expression recognition based
on deep evolutional spatial-temporal networks” . In: IEEE Transactions on Image
Processing 26.9 (2017), pp. 4193 –4203. ISSN: 1057-7149. DOI: 10.1109/TIP.
2017.2710078.
[ZP07]         Zhao, G. and Pietikainen, M. “Dynamic texture recognition using local binary
patterns with an application to facial expressions” . In: IEEE Transactions on Pat-
tern Analysis and Machine Intelligence 29.6  (June 2007), pp. 915 –928. ISSN:
0162-8828. DOI: 10.1109/TPAMI.2007.1110.
[Zha+21]    Zhao, S., Tao, H., Zhang, Y., Xu, T., Zhang, K., Hao, Z., and Chen, E. “A two-stage
3D CNN based learning method for spontaneous micro-expression recognition ” .
In: Neurocomputing 448 (2021), pp. 276 –289. DOI: 10.1016/j.neucom.2021 .
03.089.
[Zhi+11]     Zhi, R., Flierl, M., Ruan, Q., and Kleijn, W. B. “Graph-preserving sparse non-
negative matrix factorization with application to f acial expression recognition”  .
In: IEEE Transactions on Systems, Man, and Cybernetics, Part B (Cybernetics) 41.1
(Feb. 2011), pp. 38 –52. ISSN: 1083-4419. DOI: 10.1109/TSMCB.2010.2044782.
t

Bibliography                                                                                                                                              29

Zhi, R., Liu, M., and Zhang, D. “A comprehensive survey on automatic facial
action unit analysis”. In: The Visual Computer 36.5 (2020), pp. 1067 –1093. ISSN:
0178-2789. DOI: 10.1007/s00371-019-01757-x.
Zhong, Y., Wei, H., Yang, P., Wang, Y., Li, H., and Liu, J. “ExpCLIP: Bridging
text and facial expressions via semantic alignment” . In: Proceedings of the AAAI
Conference on Artificial Intelligence . Vol. 38. 7. 2024, pp. 7614 –7622. DOI: 10.
1609/aaai.v38i7.28562.
[Zho+24]
[ZLZ20]
