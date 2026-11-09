---
title: 'DiffUE: Enhancing Utility-Unlearnability Trade-off of Unlearnable Examples via Diffusion Autoencoders'
url: https://arxiv.org/abs/2607.10580
category: privacy-data
subcategory: framework
date: 2026-07
venue: arXiv (Cornell University)
authors:
- Syed Irfan Ali Meerza
- Oktay Ozturk
- Amir Sadovnik
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.10580
pages: 18
chars: 49807
fetched_at: '2026-11-08T13:00:33+00:00'
kb_version: 1
---

# DiffUE: Enhancing Utility-Unlearnability Trade-off of Unlearnable Examples via Diffusion Autoencoders

DiffUE: Enhancing Utility-Unlearnability
Trade-off of Unlearnable Examples via Diffusion
Autoencoders
Syed Irfan Ali Meerza 1,4,∗,† , Oktay Ozturk 1,† , Amir Sadovnik 2 , and Jian
Liu1,3
1 University of Tennessee, Knoxville, TN, USA
2 Oak Ridge National University, Knoxville, TN, USA
3 University of Georgia, Athens, GA, USA
4 Virginia Commonwealth University, Richmond, V A, USA
Abstract.AI models are increasingly trained on personal images scraped
from social media and public platforms, often without consent, leading
to serious privacy violations, such as unauthorized facial recognition and
targeted advertising. To counter this, researchers have developed un-
learnable examples (UEs), images modified with imperceptible noise to
prevent AI models from extracting meaningful information. However,
existing UE methods primarily rely on pixel-space noise, which can be
bypassed by relearning strategies such as adversarial training, image
transformation, and compression. While some techniques improve ro-
bustness, they often come at the expense of significant degradation in
image utility and perceptual quality. In this paper, we introduceDiffUE
to overcome these limitations by injecting noise into the semantic space
of images instead of the pixel space. Instead of corrupting pixel values,
DiffUEmodifies high-level semantic features of images, ensuring robust
unlearnability while preserving visual quality and utility. By leveraging
a diffusion-based autoencoder framework to manipulate semantic fea-
tures,DiffUEgenerates purposeful, natural-looking modifications that
effectively resist advanced relearning strategies. Extensive experiments
on four datasets, CIF AR-10, CIF AR-100, CelebA-HQ, and ImageNet, as
well as a subjective user study, demonstrate thatDiffUEsignificantly
enhances the trade-off between image quality and unlearnability, offering
a more robust and effective solution for safeguarding personal data in an
increasingly exploitative AI landscape.
1 Introduction
The success of state-of-the-art deep learning models relies heavily on vast datasets,
often sourced fromfree-to-useonline platforms without explicit consent. This
unauthorized acquisition poses significant risks, as seen in cases where personal
data, including facial images and medical records, have been exploited in com-
mercial AI models [7,3]. Public concern about these practices has spurred in-
terest in privacy protections, reinforced by regulations such as GDPR [33] and
⋆ Work done while at the University of Tennessee, Knoxville.
† These authors contributed equally.
arXiv:2607.10580v1  [cs.CV]  12 Jul 2026

2 Meerza et al.
2/255 (64.4%) 4/255 (61.2%) 8/255 (60.1%) 16/255 (57.2%) 2/255 (57.2%) 4/255 (45.4%) 8/255 (35.2%) 16/255 (17.2%)
2/255 (38.1%) 4/255 (38.5%) 8/255 (34.9%) 16/255 (18.5%) 0.10 (57.2%) 0.20 (57.2%) 0.35 (57.2%) 0.45 (57.2%)
EM REM
SEM DIFFUE
Fig. 1: Usability vs. unlearnability comparison under adversarial training with
an adversarial perturbation radius ofρ a = 4/255. We comparedDiffUEwith
three baselines: EM [9], REM [4] and SEM [20]. The number below each image
represents the defensive noise radii (ρ u) applied (the defensive noise ofDiffUE
is in the semantic space), with the value in parentheses indicating the test ac-
curacy achieved. Lower accuracy reflects greater unlearnability. Note that we
intentionally selected images with a light background to better visualize pertur-
bation artifacts in existing UE methods.
CCPA [10]. However, these regulations focus primarily on data collection and
governance rather than addressing the core issue: once data are acquired and in-
tegrated into AI training pipelines, few mechanisms exist to prevent its continued
use. To bridge this gap, recent research has introduced the concept of making
data unlearnable to AI models. Huanget al.[9] proposed unlearnable examples
(UE), a technique that adds imperceptible noise to the data, causing models to
fail in extracting useful information. This approach useserror-minimizing(EM)
noise to yield near-zero loss during training, tricking the model into “learning”
nothing from the protected data.
Built on this foundation, subsequent research has focused on enhancing the
robustness of UEs. For instance, Fuet al.[4] proposed robust unlearnable ex-
amples (REM), resilient to adversarial training techniques that could otherwise
make standard UEs learnable. Similarly, Liuet al.[20] further improved the
stability of these robust UEs by designing defensive noise that resists random
perturbations, thus eliminating the need for complex adversarial perturbation.
Expanding on this idea, Renet al.[27] enhanced the transferability of error-
minimizing noise using the Classwise Separability Discriminant to maximize
model confusion across different data categories. Moreover, application-specific
adaptations of unlearnable examples have emerged, targeting areas such as dif-
fusion models [40], time series data [13], and medical image segmentation [19].
Yet, despite their promise, UEs still struggle with two critical challenges that
hinder their effectiveness:
(1) F ragility of UEs:Recent studies have exposed significant vulnerabilities in
the robustness of UEs. Existing methods rely on error-minimizing noise to render
images uninformative to AI models. However, researchers have proposed different
relearning strategies based on adversarial training [32] or image transformations
like resizing, compression, and grayscale conversion [21,26]. These methods can

DiffUE: Enhancing Utility-Unlearnability Trade-off 3
significantly weaken the effectiveness of error-minimization noise, rendering these
defenses unreliable for long-term data security.
(2) Poor Usability for Real-W orld Applications:While some approaches
have attempted to enhance the robustness of UEs by introducing adversarial
perturbation [4] or by stabilizing the UEs using random perturbation [20], they
often lead to significant image degradation as unlearnability increases. Stronger
noise improves protection but makes images unusable for photographers, artists,
and social media users who rely on high-quality visuals. Grainy, artifact-ridden
images are impractical for professional work and unappealing for casual sharing.
It is evident from Fig. 1 that the robustness comes with the cost of perceptual
quality for these methods. Moreover, pixel-space noise disrupts format consis-
tency, leading to compression artifacts and post-processing errors.
DiffUE.To address the aforementioned limitations, we proposeDiffUE,
a robust defense framework that achieves greatly improved trade-offs between
data perceptual quality and unlearnability. Our method is particularly effective
against various state-of-the-art data relearning strategies, such as adversarial
training/augmentations [4], grayscale conversion [21], data purification [12], and
image transformation [26]. Unlike conventional methods that apply pixel-space
noise,DiffUEoperates in the semantic space, leveraging a pre-trained diffusion
autoencoder [25]. Specifically, it encodes an input imagexinto a high-level se-
mantic representationz sem and a stochastic codex T , then optimizes a defensive
semantic noisez δ to make the image unlearnable. The final imagex u is recon-
structed through a Conditional Denoising Diffusion Implicit Model (DDIM) [30]
decoding process. This optimization process ensures thatx u induces a near-zero
loss in a surrogate model, ensuring that models fail to extract meaningful fea-
tures. To maintain both robustness and visual quality, we conduct empirical
studies to determine the noise radiusρ u ensuring that semantic space pertur-
bations translate into effective pixel domain disruptions, changing the image’s
intrinsic features. By aligning the image’s intrinsic features with model gradient
space,DiffUEenhances resistance against adversarial retraining, image trans-
formations, and lossy compression. Unlike unnatural, high-frequency “static”
artifacts [41] introduced by pixel-based noise, our method guides semantic mod-
ifications along the learned image manifold, creating coherent variations such as
gentle lighting shifts or subtle tone adjustments. These semantic changes align
closely with human perception, appearing natural [35].
Extensive experiments with multiple UE baselines, various relearning strate-
gies, and diverse settings across four datasets demonstrate the superior effective-
ness of our system, particularly in challenging relearning scenarios.
2 Related Work
Unlearnable Examples.Unlike poisoning attacks [1,16,29], which degrade
model performance by injecting malicious data, unlearnable examples (UEs) [9]
defensively add imperceptible perturbations to render data uninformative for
training, thereby limiting generalization. Early work explored diverse UE mech-
anisms, including channel/appearance manipulations [21] and robustness to ad-

4 Meerza et al.
versarial training via Robust Unlearnable Examples (REM) [4]. Subsequent ef-
forts improved transferability and stability across models and training pipelines [27,20]
and extended UEs to generative diffusion models [40].
More recent work has shifted toward stronger robustness, guarantees, and
broader modalities. Menget al.[24] proposed semantic Deep Hiding using in-
vertible neural networks to produce more resilient UE perturbations, while Zhu
et al.[42] studied the detectability of UEs and corresponding defenses, highlight-
ing a growing arms race. Wanget al.[34] provided a certification framework and
constructed provably unlearnable examples, offering formal learnability guar-
antees. Beyond images, Meerzaet al.[23] introduced HarmonyCloak, extending
unlearnable examples to the music domain by leveraging psychoacoustic masking
and semantic guidance to protect audio content from generative music models
while preserving perceptual quality. Wuet al.[37] introduced Temporal Un-
learnable Examples for protecting personal video data against tracking-based
exploitation, and Liet al.[18] investigated versatile transferable UE genera-
tors across challenging shifts (e.g., architectures and resolutions). Despite these
advances, achieving strong robustness against adaptive retraining while preserv-
ing perceptual quality and maintaining broad real-world effectiveness remains
challenging.
Relearning from UEs.Recent research has explored countermeasures that
attempt to restore learnability to UEs [2,12,26]. One of the earliest approaches
by Taoet al.[32] showed that Adversarial Training (AT) can weaken UE pro-
tections by introducing adversarial perturbations during training. Building on
this idea, Qinet al.proposed UEraser [26], which combines data augmentation
with adversarial training to improve model generalization on protected data.
Other methods adopt alternative strategies. Liuet al.[21] demonstrated that
grayscale transformations can neutralize channel-specific UE noise, improving
model robustness. Diffusion-based purification has also gained attention: Jianet
al.proposed LUE [12], which uses joint-conditional diffusion to restore learnabil-
ity, while Dolatabadiet al.introducedA vatar[2], a diffusion-based approach
that removes defensive noise from UEs. These countermeasures highlight the
ongoing arms race between privacy-preserving defenses and adaptive learning
strategies, underscoring the need for more resilient UE techniques.
3 Preliminaries
3.1 Diffusion Autoencoders
Diffusion autoencoders unify the strengths of denoising diffusion probabilistic
models (DPMs) [8] and Denoising Diffusion Implicit Models (DDIMs) [30] to
enable high-fidelity image reconstructions from semantically structured latent
codes. DPMs progressively corrupt images with Gaussian noise and use a U-Net
denoiser to learn the reverse process, while DDIMs offer a faster, deterministic
variant.
Building on this foundation, diffusion autoencoders [25] introduce a seman-
tically structured latent space that enhances controllability and interpretability.
The encoder decomposes an imagex 0 into two latent variables: a high-level se-
mantic codez sem =E(x 0) and a low-level stochastic latentx T . The semantic

DiffUE: Enhancing Utility-Unlearnability Trade-off 5
Semantic
Encoder(𝓔)
𝑧𝑑𝑒𝑓
Conditional  DDIM
Decoder (𝒟)
Input
Image (𝑥0)
Stochastic code
𝑥𝑇
𝑥𝑇 → 𝑥𝑇−1 ′ → ⋯ → 𝑥𝑢
Unlearnable Image
(𝑥𝑢)
Surrogate Model
(𝑔)
Update defensive noise (𝑧𝛿)
Conditional DDIM
Encoder
𝑥0 → 𝑥1 → ⋯ → 𝑥𝑇
ℒ𝑢𝑙𝑒 = ℒ +
𝑧𝑠𝑒𝑚
𝑧𝑀
For manipulation
(optional)
+
𝑧𝛿  = ෑ
𝜖
(𝑧𝛿 − 𝛼 ⋅ 𝑠𝑖𝑔𝑛(∇ℒ𝑢𝑙𝑒))
Linear Attribute
Classifier
𝛾 ⋅ 𝐷
Fig. 2: Overview ofDiffUE:DiffUEleverages a diffusion autoencoder to en-
code the input image into a semantic codez sem and a stochastic codex T . It
then iteratively optimizes a defensive semantic codez δ so that the resulting un-
learnable imagex u, generated by the conditional DDIM decoding process, tricks
the surrogate modelg θ into believing there is nothing to learn.
codez sem, a compact 512-dimensional vector, captures global, non-spatial se-
mantics akin to the style vector in StyleGAN [15], whilex T preserves local and
textural details via reverse DDIM encoding. During decoding, the model recon-
structs the image using a DDIM-based generative process conditioned on both
zsem andx T :
pθ(x0:T |zsem) =p(x T )
TY
t=1
pθ(xt−1|xt, zsem), (1)
wherep θ(xt−1|xt, zsem) =N(f θ(xt, t, zsem),0) fort= 1, and follows the DDIM
update for othert. The conditional mean functionf θ integrates the semantics
zsem to guide denoising, enabling the model to generate coherent and diverse
outputs consistent with the encoded structure.
This dual-latent formulation, comprising semanticz sem and stochasticx T ,
enables disentangled control over content and style, supporting tasks such as se-
mantic interpolation, content-preserving manipulation, and reconstruction, while
preserving the high-fidelity synthesis capabilities enabled by diffusion models.
3.2 Unlearnable Examples
Conventionally, the process of crafting UEs for classification models involves
modifying each data sample to make the model’sclassification lossas close
to zero as possible. Thiszero-lossapproach essentially tricks the model into
perceiving these samples as trivial or uninformative, thereby suppressing any
gradients that could guide effective learning [9]. To achieve this, consider a data
samplexwith labely, the defender can crafterror-minimizingnoiseδthat,
when added tox, minimizes the model’s learning potential for this sample. The
noiseδis generated by solving a bi-level optimization problem:
arg min
θ
Ex,y[min δ L(gθ(x+δ), y)]s.t.∥δ∥ p ≤ρ, (2)
whereg θ denotes the classification model,Lis the cross-entropy loss, and the
noise magnitude∥δ∥is bounded byρ.

6 Meerza et al.
4 Design of DiffUE
4.1 Overview of DiffUE
The overall pipeline ofDiffUEis depicted in Fig. 2.DiffUEutilizes a diffusion-
based autoencoder architecture [25], comprising a semantic encoderEand a
conditional DDIM, which contains a stochastic encoder and an image decoder
D. In this process, an input imagex 0 is encoded into a high-level semantic
representationz sem and a stochastic codex T that captures low-level variations.
The objective is to optimize a defensive semantic noisezδ such that the perturbed
semantic representationz def =z sem +z δ produces an unlearnable imagex u,
causing the surrogate modelgto experience near-zero loss. Givenx 0, we can
generate the defensive noisez δ by solving the bi-level optimization problem:
arg min
θ
E(x0,y)

min
zδ
L(gθ(D(E(x 0) +z δ, xT )), y)

,
s.t.||zδ||p ≤ρ u,
(3)
wherez sem =E(x 0),x u =D(E(x 0) +z δ, xT ) andρ u is the noise bound. This
formulation is a min-min bi-level optimization problem where the inner mini-
mization seeks to findz δ, constrained by anL p-norm, that minimizes the model’s
classification loss, while the outer minimization optimizes the model parameters
θto further reduce the loss.
To generate effective unlearnable examples, it is crucial to understand the
model’s learning dynamics, specifically the gradient trajectory of parametersθ
during training. Thus,θmust be partially trained initially to reflect the model’s
typical behavior. This enablesδto be optimized in alignment with learning
dynamics, guiding the model toward low training loss. Unlike adversarial exam-
ples, which induce prediction failures, hereδis crafted to create the illusion of
successful learning. Specifically, we optimizeθforQsteps before updatingδ.
This process repeats until the model achieves an error rate below a predefined
thresholdλ, terminating the training.
Additionally, the conditional DDIM is conditioned on the defensive semantic
codez def =z sem +z δ, with the noise prediction networkf(x T , T, zdef ) esti-
mating noise at each step, whereTindicates the number of noise addition and
removal steps. During the decoding phase, the deterministic generative process
reconstructs the final imagex u based on the conditioned input.
4.2 Defensive Noise in the Semantic Space
InDiffUE, we focus on generating defensive noise within the semantic space
of diffusion autoencoders. To achieve this, we inject noise into the semantic
space using the first-order optimization method, Projected Gradient Descent
(PGD) [22]. PGD works by iteratively adjusting the input in the direction of
the gradient of a loss function, ensuring that each step stays within a defined
perturbation limit. The constrained inner minimization problem is solved with
the following update rule:
zδ(t+1) =Π ρu (zδ(t) −η·sign(∇ zδ Lule)), (4)
whereL ule represents the loss function defined asL ule =L(g θ(D(E(x 0) +
zδ, xT )), y), wheretis the current step of the perturbation, andηis the step

DiffUE: Enhancing Utility-Unlearnability Trade-off 7
size. The functionΠ ρu is a projection function that ensures the noisez δ remains
within the allowed perturbation rangeρ u by clipping it if it exceeds the limit.
In our framework, PGD iteratively refines the noisez δ, to hinder the surrogate
modelg θ’s learning.
Benefits of Injecting Semantic Noises.Semantic perturbations offer a unique
advantage over pixel-level noise by creating subtle adjustments that alter an im-
age’s underlying attributes without introducing detectable spatial patterns. Hu-
man perception, which processes high-level attributes non-linearly, can naturally
integrate and overlook these subtle semantic changes, making them impercep-
tible [35]. In contrast, pixel-space perturbations introduce noticeable patterns
perceived as foreign elements [31]. Neural networks, however, respond sensitively
even to minor semantic adjustments, directly impacting the linear feature space
of model predictions. Thus, effective unlearnable behavior can be achieved with
a smaller perturbation budget, reducing pixel-space distortion and allowing our
method to outperform previous approaches in visual quality and robustness.
Moreover, semantic perturbations inherently improve robustness by altering
high-level attributes instead of pixel-level noise. This makes them less vulnerable
to pixel-domain augmentations [31] and filtering techniques [39] commonly used
to counteract defensive effects. Since these semantic changes do not present fixed
spatial patterns, isolating or removing them becomes considerably more chal-
lenging. In the domain of adversarial examples [38], photorealistic perturbations
that closely align with the natural characteristics of image objects have proven to
be resilient to adversarial training. Using semantic-space transformations,Dif-
fUEimproves the trade-off between perceptual quality and unlearnability while
enhancing robustness against pixel-space attacks.
4.3 UEs via Controlled Modifications
Adding noise in the semantic space allows for subtle, meaningful adjustments to
an image that is generally more acceptable to human observers than pixel-level
noise. This enables controlled modifications, such as attribute or style adjust-
ments, allowing users to share visually enhanced images online. In this work, we
focus on two modification types: attribute manipulation (e.g., adding a smile)
and style manipulation (e.g., adjusting tone or contrast), where defensive noise
zδ alters specific image features.
By manipulating semantic features, our approach can also leverage targeted
semantic directions to create purposeful, visible modifications, ensuring both
unlearnability and perceptual changes. To achieve this, we adjust the defensive
semantic codez def in the direction of the desired modification, determined by
the weight vector of a linear classifier trained to distinguish positive and negative
instances of the attribute or style. For example, to add a smile, we use a classi-
fier that takes semantic features of an image as input and distinguishes between
smiling and non-smiling faces. The classifier’s weight vector, which captures the
relationship between the semantic features associated with smiling, is then used
to guide the defensive noise in that direction. Similarly, for style changes, such
as applying certain filter effects, the classifier weights capture the characteristic
patterns of these effects in semantic space. The modified loss function incorpo-

8 Meerza et al.
rating these controlled changes for effective unlearnability is as follows:
Lule =L(g θ(D(E(x 0) +z δ, xT )), y) +γ·(1−cos(z δ, zM )), (5)
wherez M is the desired semantic direction calculated by normalizing the weight
vector of the relevant classifierw cls/||wcls||,cos(.) denotes the cosine similarity,
γis a scaling factor that modulates the degree of desired modifications, and the
cosine similarity is defined asDin Fig. 2. Cosine similarity aligns the noise vec-
tor in the target direction (direction of the semantics of the desired effectz M ),
allowing for controlled, intentional adjustments within the semantic space. This
approach enhances practical usability while maintaining resistance to unautho-
rized usage.
5 Experiments
5.1 Experimental Setup
Datasets and Model Architecture.We conducted experiments on three ma-
jor vision benchmark datasets: CIF AR-10, CIF AR-100 [17], and the first 100
classes of ImageNet [28]. For data augmentation, we applied random cropping
and horizontal flipping. For the experiment of controlled modifications, we used
the CelebA-HQ dataset [14], and ImageNet [28]. The proposed method and base-
lines were evaluated across various vision tasks using ResNet18 [5] as a surrogate
model. We use a pre-trained DiffAE [25] model trained on different datasets. Fol-
lowing prior UE works, DiffUE employs an iterative bi-level optimization pro-
cedure with 10 PGD inner steps per surrogate model update, and optimization
continues until the surrogate model reaches over 99% training accuracy.
UE Baselines.We compareDiffUEwith state-of-the-art approaches for gen-
erating UEs. Specifically, we evaluate against error-minimizing noise (EM) [9],
which is the first work in the field of UEs and directly applies error minimization
noise to the images. We also include robust error-minimizing noise (REM) [4],
which adds noise designed to reduce adversarial training loss, and stable error-
minimizing noise (SEM) [20], which generates unlearnable noise that is resilient
to random perturbations. These baselines represent the foundational UE genera-
tion paradigms widely adopted in prior literature, and many subsequent methods
build upon or extend these error-minimization frameworks.
T echniques Used for Robustness Evaluation.To assess the robustness of
our method, we apply Mean and Gaussian filters to test the resilience of our
images against noise-filtering approaches. We evaluate our approach using recent
state-of-the-art relearning techniques designed to counter UEs and restore their
learnability. Specifically, we testedAdversarial T raining[32], which introduces
adversarial noise to bypass defensive noise and recover learnability in UEs. We
also usedGrayScale[21], a method that converts UEs to grayscale to neutralize
color-channel noise,UEraser[26], which employs adversarial augmentations to
reintroduce learnability, as well asLUE[12], which uses a diffusion purification
model to eliminate unlearnable noise from images. Additionally, we evaluate the
effectiveness of our approach under common lossy image compression formats,
such as JPEG, WebP, and HEIC.

DiffUE: Enhancing Utility-Unlearnability Trade-off 9
Input Image
DIFFUE EM REM SEM
Fig. 3: Visualization of noise types and crafted examples for the ImageNet Subset.
5.2 Semantic Noise Radii Selection
Unlike existing UE methods that constrain noise levels in the pixel space (e.g.,
2/255, and 4/255),DiffUEintroduces defensive noise in the semantic space,
where the noise boundary (i.e.,ρ u in Equation 3) cannot be directly mapped
to the pixel space due to non-linear transformations between the two spaces.
Moreover, defensive noise in the semantic space generates more photorealistic
pixel-level changes, as illustrated in Fig. 3. Even with the same amount of pixel
modifications,DiffUEcan more effectively conceal perturbations within the
original images. Therefore, instead of relying on pixel-level perturbation bounds
to assess perceptual impact, as in existing studies, we use widely adopted metrics
to quantify image perceptual quality (see section 5.5 for details).
To ensure the semantic noise radius is set to a reasonable value, we empirically
measure the maximum pixel changes induced by a given noise level for each
dataset. Specifically, we perturb 50 of the 512 dimensions of the semantic code
and analyze their impact on the reconstructed image in the pixel space. Based
on the analysis on 2,000 samples per dataset, we set the semantic noise radius
to 0.20 for CIF AR-10/100 and 0.35 for ImageNet, corresponding to a maximum
pixel shift of 4/255.
While increasing the noise radius can further enhance unlearnability, it may
also distort the image’s semantics. Although the utility-unlearnability trade-off
could be further optimized through fine-tuning, we did not adjust the radius
further, as our chosen setting already achieves significantly stronger unlearn-
ability and robustness against relearning, even when compared to baselines with
perturbation radius of 8/255, while also achieving higher perceptual quality.
5.3 Effectiveness of DiffUE
We applied various UE methods to the entire training set, setting the defen-
sive perturbation radiusρ u to 8/255 for all baselines. ForDiffUE, semantic
noise radii (ρ u) were determined empirically for each dataset: 0.2 for CIF AR-10
and CIF AR-100, and 0.35 for the ImageNet Subset, targeting a maximum pixel-
level change of 4/255, corresponding to a 50% smaller noise budget than the
baselines. REM and SEM jointly optimize defensive perturbations with an ad-
ditional noise component, namely adversarial perturbation (radiusρ a) in REM
and random perturbation (radiusρ r) in SEM. We evaluate differentρ a andρ r

10 Meerza et al.
Table 1: Test accuracy (%) of models trained on data protected by different
noise strategies under adversarial training with varying perturbation radii. The
defensive perturbation radiusρ u is fixed for all the methods. The training ad-
versarial perturbation radiusρ a andρ r for REM and SEM are adjusted. A lower
test accuracy indicates better protective effectiveness.
Dataset Adv.Train. Clean EMDiffUE REM SEM
ρt ρa = 0 2/255 4/255ρ r = 0 2/255 4/255
CIF AR-10
0 95.64 11.9810.7913.22 23.91 31.27 18.92 18.51 25.14
2/255 89.24 20.9612.5968.54 35.37 37.75 20.82 23.97 26.65
4/255 86.92 76.9517.1186.55 75.47 64.64 73.57 46.19 46.85
CIF AR-100
0 85.321.762.17 2.11 9.82 19.3 9.81 4.09 18.61
2/255 76.76 67.293.7851.81 10.44 18.35 52.52 10.44 12.56
4/255 72.19 64.594.9265.93 61.29 32.22 60.64 47.52 26.19
ImageNet Subset
0 82.541.892.11 3.45 9.13 17.74 4.15 8.14 10.11
2/255 73.22 70.6712.4548.56 30.22 31.40 35.21 33.22 36.22
4/255 70.23 67.8617.2065.58 57.23 45.49 57.32 38.11 38.57
Table 2: Test accuracy (%) of various methods trained on the unlearnable
CIF AR-10 dataset, evaluated under different filtering techniques and relearn-
ing strategies.
Method Filters Relearning strategies Mean Gaussian GrayScale UEraser LUE
Clean90.65 91.26 91.65 92.78 91.17
EM37.87 32.71 83.23 90.23 90.33
REM29.92 28.53 63.87 87.39 89.57
SEM28.55 24.22 34.23 81.56 89.29
DiffUE 13.32 12.43 13.99 14.19 33.97
values during unlearnable image generation and subsequently perform adversar-
ial training with varying adversarial radiiρ t. Table 1 reports the resulting test
accuracies on clean data. Asρ t increases, models trained on baseline unlearn-
able datasets achieve higher test accuracy, indicating that stronger adversarial
training makes these methods less effective. For example, withρ t = 4/255, test
accuracy reaches 76.95%, 64.64%, and 46.85% for EM, REM (ρ a = 4/255), and
SEM (ρ r = 4/255), respectively, on CIF AR-10. In contrast,DiffUEmaintains
a low accuracy of 17.11%, demonstrating greater resistance to adversarial train-
ing. A similar trend appears on the ImageNet Subset, whereDiffUEremains
at 17.20% while REM and SEM increase to 45.49% and 38.57%, respectively.
Fig. 3 illustrates the generated perturbations. Unlike pixel-based noise,DiffUE
produces perceptually realistic perturbations that preserve visual fidelity while
making the protective signal more difficult for adversarial training and filtering
methods to remove.
5.4 Robustness Evaluation
We further evaluate the robustness ofDiffUEand baseline methods against
real-world transformations that could compromise data protection. Table 2 com-

DiffUE: Enhancing Utility-Unlearnability Trade-off 11
Table 3: Impact of image compression on different defensive noise evaluated on
different datasets. Table shows the test accuracy (%) of various methods.
Method CIF AR-10 ImageNet No Comp. JPEG WebP HEIC No Comp. JPEG WebP HEIC
EM 11.98 45.22 55.57 35.62 1.8934.21 41.98 37.57
REM 13.22 38.12 41.78 34.95 3.45 33.45 43.22 37.12
SEM 18.92 32.92 35.96 23.89 4.15 18.33 29.45 17.22
DiffUE 10.79 17.22 18.05 18.11 2.114.12 7.88 5.11
Table 4: Comparison of perceptual metrics with state-of-the-art methods on
CelebA-HQ and ImageNet. The defensive perturbation radius forDiffUEis set
toρ u = 0.25 for CelebA-HQ andρ u = 0.35 for ImageNet, while EM, REM, and
SEM use a perturbation radius ofρ u = 8/255 andρ a = 4/255 for REM and
ρr = 4/255 for SEM.
Dataset MethodEM REM SEMDiffUE
CelebA-HQ
FID(↓) 11.612 10.971 10.1455.355
SSIM(↑) 0.704 0.561 0.6110.814
PSNR(↑) 30.112 29.411 29.87132.438
T est Acc.(↓) 55.98% 54.27% 52.14%50.22%
ImageNet
FID(↓) 10.583 11.226 11.8745.492
SSIM(↑) 0.682 0.389 0.5760.781
PSNR(↑) 29.091 23.295 29.04432.934
T est Acc.(↓)1.89% 17.74% 10.11% 2.11%
pares the resilience of various unlearnable noise methods under different filtering
techniques and relearning strategies. The table shows thatDiffUEachieves the
lowest test accuracy across all filtering techniques (Mean: 13.32%, Gaussian:
12.43%) and remains more resistant to relearning strategies such as UEraser
(14.19%) and LUE (33.97%), compared to the next-best method (SEM: 81.56%
under UEraser, 89.29% under LUE). This highlights the robustness ofDiffUE
against pixel-domain filtering and augmentation.
Given that most images undergo lossy compression before online sharing, we
also assess the impact of compression on unlearnable noise in Table 3.DiffUE
exhibits minimal degradation when compressed with JPEG (17.22% CIF AR-
10, 4.12% ImageNet) or WebP (18.05% CIF AR-10, 7.88% ImageNet), whereas
pixel-based baselines degrade significantly (e.g., EM: 45.22% CIF AR-10, 34.21%
ImageNet for JPEG). By avoiding pixel-space noise,DiffUEmaintains unlearn-
ability under real-world transformations.
5.5 Perceptual Quality Evaluation
We argue that UEs should maintain high perceptual quality so users can use
them without compromises. To assess perceptual quality, we use three metrics:
Frechet Inception Distance (FID) [6] for naturalness, Structural Similarity In-
dex Measure (SSIM) [36] for similarity to the clean image, and Peak Signal-
to-Noise Ratio (PSNR) [11] for image quality under noise. Table 4 compares

12 Meerza et al.
PlaneCarBirdCatDeerDogFrogHorseShipTruck
Predicted labels
Plane
Car
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck True labels
955 4 9 6 5 2 3 2 5 9
6 952 6 1 10 7 3 3 8 4
3 5 960 4 4 5 3 4 7 5
6 8 4 947 6 6 2 8 8 5
1 8 8 5 962 2 1 5 4 4
3 6 2 11 5 946 8 5 7 7
5 74 30 106128176 6 139331 5
2 3 2 4 5 4 8 962 6 4
4 5 3 7 2 11 5 5 956 2
0 7 5 5 6 1 4 7 3 962
(a) Single Class
PlaneCarBirdCatDeerDogFrogHorseShipTruck
Predicted labels
Plane
Car
Bird
Cat
Deer
Dog
Frog
Horse
Ship
Truck True labels
948 6 10 7 4 2 3 3 6 11
6 7 34 25 12 512105138 43 118
4 5 951 7 5 6 4 5 8 5
7 9 4 941 7 7 3 8 9 5
2 9 8 5 958 3 2 5 5 3
13 14 11 514 25 9 135173 52 54
9 11 17 49 141198 8 132310125
4 4 4 6 5 6 9 957 7 4
6 6 4 9 3 12 7 6 950 5
2 8 6 6 8 4 5 9 5 947 (b) Multiple Classes
Fig. 4: Classwise unlearnability analysis. In (a), we have perturbed only one class
and kept the other classes clean, and in (b), we have perturbed multiple classes.
unlearnable examples generated by various methods on CelebA-HQ and Ima-
geNet. On CelebA-HQ,DiffUEachieves the lowest FID (40–50% reduction)
with the highest PSNR (32.438) and the highest SSIM (0.814), indicating nat-
ural unlearnable examples with low perceptual noise. On ImageNet,DiffUE
shows similar trends, with a 40–50% FID improvement and higher SSIM and
PSNR than baselines.
5.6 Class-wise Unlearnability Analysis
We evaluateDiffUE’s class-specific effect by applying it solely to the ‘Frog’
class in CIF AR-10, keeping other classes untouched. A ResNet-18 model trained
on this partially protected dataset shows poor classification on ‘Frog’ test sam-
ples, mispredicting them as ‘Horse’, ‘Dog’, or ‘Cat’ (Fig. 4a). Meanwhile, perfor-
mance on untouched classes remains stable, confirming thatDiffUEselectively
impairs learning without inducing domain shift. Extending this to three classes
(‘Car’, ‘Dog’, ‘Frog’), the confusion matrix in Fig. 4b shows similar degradation
for protected classes, while others retain high accuracy. This demonstratesDif-
fUE’s effectiveness under multi-class settings and its fine-grained control over
unlearnability.
5.7 Defensive Noise as Controlled Modifications
DiffUEuses a diffusion autoencoder to guide defensive perturbations toward
realistic photo edits, enhancing both unlearnability and perceptual quality. Un-
like untargeted noise, which is dispersed in semantic space, control modification
aligns perturbations with specific attributes for visible changes. We train a classi-
fier on CelebA-HQ semantic codes (zsem) to identify attributes, using its weights
to steer the noise. For implementation, we use a binary gender classifier and set
the perturbation radiusρ u to 0.35, which is higher than the radius used for
untargeted noise (0.25).
DiffUEuses a diffusion autoencoder to guide defensive perturbations to-
ward realistic photo edits, enhancing both unlearnability and perceptual quality.

DiffUE: Enhancing Utility-Unlearnability Trade-off 13
Fig. 5: Defensive noise as attribute modification
Table 5: Test accuracy on CIF AR-10/100 with different model architectures.
Dataset Model Clean EM REM SEMDiffUE
CIF AR-10
VGG-16 85.34 81.50 68.10 54.5525.33
RN-18 86.92 76.95 64.64 46.8517.11
RN-50 87.24 79.80 71.22 52.0020.05
DN-121 84.85 81.70 72.15 55.6021.75
CIF AR-100
VGG-16 61.45 59.77 54.45 59.1111.65
RN-18 72.19 64.59 32.22 26.194.92
RN-50 67.45 69.42 62.78 29.419.03
DN-121 52.65 59.89 66.68 50.7010.98
Unlike untargeted noise, which is dispersed in semantic space, controlled modifi-
cation aligns perturbations with specific attributes for visible changes. We train
a classifier on CelebA-HQ semantic codes (z sem) to identify attributes, using its
weights to steer the noise. For implementation, we use a binary gender classi-
fier and set the perturbation radiusρ u to 0.35, which is higher than the radius
used for untargeted noise (0.25). The controlled semantic edits are an optional
demonstration of semantic-space controllability and are not used in the default
DiffUEconfiguration.
Fig. 5 illustrates the impact of attribute and style manipulations on clean
test accuracy. For example, curly hair (51.8%) and black hair (52.1%) modifica-
tions reduce accuracy to near-random levels, demonstrating strong unlearnabil-
ity. Beyond experimental validation, this method helps protect personal images
from unauthorized AI training. Attribute modifications can subtly alter profile
pictures without degrading quality. By balancing privacy and image integrity,
DiffUEenables users to share visually appealing content while minimizing AI
exploitation risks.
5.8 T ransferability Analysis
To investigate the transferability of different noise methods across neural archi-
tectures, we selected ResNet-18 as the source model for generating unlearnable
examples (UEs). The impact of the generated noise was evaluated on target mod-

14 Meerza et al.
VGG-16 RN-18 RN-50 DN-121
Clean ImageSEMDIFFUE
Fig. 6: Comparison of the spatial regions in the input image that contribute to
classification for each model when trained on clean and unlearnable examples.
els, including VGG-16, ResNet-50, and DenseNet-121. All transferability exper-
iments were conducted on the CIF AR-10 and CIF AR-100 datasets, as shown in
Table 5.DiffUEdemonstrated superior performance in generating highly trans-
ferable UEs, achieving the lowest test accuracies in all cases. This highlights its
effectiveness in surpassing existing methods such as REM and SEM.
Transferring UEs to models with different architectures reduces their effec-
tiveness due to differences in feature representations between the source and tar-
get models. As architectural disparity increases, UEs become less effective. For
example, ResNet-50, which is structurally similar to ResNet-18, retains higher
performance with UEs than VGG-16, which differs significantly in design. This
highlights the role of architectural similarity in UE transferability. To further
analyze this effect, we examine Grad-CAM visualizations of models trained on
clean images and unlearnable examples. Fig. 6 presents results for the same input
image using models trained under both settings.
When trained on clean images, all models consistently focus on the same
discriminative region, the dog’s face. In contrast, when trained on UEs generated
usingDiffUE, the models shift their attention to other regions unrelated to the
dog’s face. Notably, even though the unlearnable examples were generated using
a ResNet-18 surrogate, the altered attention patterns are consistent across all
tested architectures, demonstrating the strong transferability ofDiffUE. By
comparison, models trained on unlearnable datasets generated by SEM show
less consistent attention shifts, different architectures focus on different regions,
and in many cases still attend to the dog’s face, indicating that SEM exhibits
weaker transferability thanDiffUE.
5.9 User Study
We conducted a user study to assess the perceptual quality and user preference of
DiffUEcompared to baseline methods. A total of 56 participants were recruited

DiffUE: Enhancing Utility-Unlearnability Trade-off 15
Table 6: User study comparison ofDiffUEwith baselines across perceptual
metrics.
Method Naturalness(↑) Acceptability (↑) Artifact(↓) Preference(↓)
Clean 4.90±0.10 98.5% 1.10±0.15 -
EM 3.76±0.05 56.5% 3.97±0.12 2.86
REM 2.91±0.19 19.2% 4.23±0.07 3.79
SEM 3.11±0.35 61.5% 3.31±0.10 2.13
DiffUE4.65±0.12 98.5% 1.22±0.10 1.22
via online flyers posted in photography, digital art, and content creation forums
(e.g., Reddit), including 26 photographers, 13 digital artists, and 17 social media
content creators. Participants independently completed the study on their own
devices.
Each participant was shown 20 randomized image sets containing portraits (3
sets contain the participant’s own portraits) and landscape images, with each set
containing a clean image and four unlearnable versions (EM, REM, SEM with
ρu = 4/255 andDiffUEwithρ u = 0.35). They rated each image using a 5-point
Likert scale on naturalness and artifact visibility, and responded to a yes/no
question regarding its usability. They were also asked to rank the four UE images
from each set based on overall preference. As shown in Table 6,DiffUEachieved
a naturalness score of 4.65±0.12, closely matching the clean images (4.90±
0.10), and maintained high usability at 98.5%. In contrast, baseline methods
such as REM and EM received significantly lower acceptability scores of 19.2%
and 56.5%, respectively, along with higher artifact ratings.DiffUEalso ranked
best in overall preference with an average rank of 1.22, clearly outperforming the
other baselines. These results indicate thatDiffUEdelivers near-clean visual
quality while preserving robust privacy characteristics.
6 Conclusion
To confront the challenge of developing robust unlearnable examples, we intro-
duceDiffUE, a defense framework that operates at the semantic level to pre-
serve both unlearnability and visual realism. Built on a diffusion autoencoder,
DiffUEinjects controlled perturbations into the semantic space, producing im-
ages that appear natural yet remain unlearnable even against advanced adver-
sarial relearning strategies. Experimental evaluations demonstrate thatDiffUE
consistently achieves higher robustness than existing methods against state-of-
the-art relearning attacks while preserving data usability across various applica-
tions, establishing a reliable path toward privacy-preserving data in adversarial
environments.
7 Acknowledgment
We would like to thank our anonymous reviewers and shepherd for their in-
sightful feedback. This work is supported in part by NSF CNS-2114161, ECCS-
2132106, CBET-2130643, and CNS-2403529.

16 Meerza et al.
References
1. Biggio, B., Nelson, B., Laskov, P.: Poisoning attacks against support vector ma-
chines. arXiv preprint arXiv:1206.6389 (2012)
2. Dolatabadi, H.M., Erfani, S., Leckie, C.: The devil’s advocate: Shattering the il-
lusion of unexploitable data using diffusion models. In: 2024 IEEE Conference on
Secure and Trustworthy Machine Learning (SaTML). pp. 358–386. IEEE (2024)
3. Edwards, B.: Artist finds private medical record photos in popular AI training data
set. https://arstechnica.com/information-technology/2022/09/artist-finds-private-
medical-record-photos-in-popular-ai-training-data-set/ (2022), [Accessed 22-06-
2026]
4. Fu, S., He, F., Liu, Y., Shen, L., Tao, D.: Robust unlearnable examples: Protect-
ing data against adversarial learning. In: International Conference on Learning
Representations (2022)
5. He, K., Zhang, X., Ren, S., Sun, J.: Deep residual learning for image recognition. In:
Proceedings of the IEEE conference on computer vision and pattern recognition.
pp. 770–778 (2016)
6. Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., Hochreiter, S.: Gans trained
by a two time-scale update rule converge to a local nash equilibrium. Advances in
neural information processing systems30(2017)
7. Hill, K.: The secretive company that might end privacy as we know it. In: Ethics
of Data and Analytics, pp. 170–177. Auerbach Publications (2020)
8. Ho, J., Jain, A., Abbeel, P.: Denoising diffusion probabilistic models. NeurIPS
(2020)
9. Huang, H., Ma, X., Erfani, S.M., Bailey, J., Wang, Y.: Unlearnable examples:
Making personal data unexploitable. In: ICLR (2021)
10. Illman, E., Temple, P.: California consumer privacy act. The Business Lawyer
75(1), 1637–1646 (2019)
11. Instruments, N.: Peak signal-to-noise ratio as an image quality metric (2013)
12. Jiang, W., Diao, Y., Wang, H., Sun, J., Wang, M., Hong, R.: Unlearnable examples
give a false sense of security: Piercing through unexploitable data with learnable
examples. In: Proceedings of the 31st ACM International Conference on Multime-
dia. pp. 8910–8921 (2023)
13. Jiang, Y., Ma, X., Erfani, S.M., Bailey, J.: Unlearnable examples for time series. In:
Pacific-Asia Conference on Knowledge Discovery and Data Mining. pp. 213–225.
Springer (2024)
14. Karras, T., Aila, T., Laine, S., Lehtinen, J.: Progressive growing of gans for im-
proved quality, stability, and variation. arXiv preprint arXiv:1710.10196 (2017)
15. Karras, T., Laine, S., Aila, T.: A style-based generator architecture for generative
adversarial networks. In: Proceedings of the IEEE/CVF conference on computer
vision and pattern recognition. pp. 4401–4410 (2019)
16. Koh, P.W., Liang, P.: Understanding black-box predictions via influence functions.
In: International conference on machine learning. pp. 1885–1894. PMLR (2017)
17. Krizhevsky, A., Hinton, G., et al.: Learning multiple layers of features from tiny
images (2009)
18. Li, Z., Cai, J., Xu, G., Zheng, H., Li, Q., Zhou, F., Yang, S., Ling, C., Wang, B.:
Versatile transferable unlearnable example generator. Advances in Neural Infor-
mation Processing Systems38, 17495–17522 (2026)
19. Lin, X., Yu, Y., Xia, S., Jiang, J., Wang, H., Yu, Z., Liu, Y., Fu, Y., Wang,
S., Tang, W., et al.: Safeguarding medical image segmentation datasets against

DiffUE: Enhancing Utility-Unlearnability Trade-off 17
unauthorized training via contour-and texture-aware perturbations. arXiv preprint
arXiv:2403.14250 (2024)
20. Liu, Y., Xu, K., Chen, X., Sun, L.: Stable unlearnable example: Enhancing the ro-
bustness of unlearnable examples via stable error-minimizing noise. In: Proceedings
of the AAAI Conference on Artificial Intelligence. vol. 38, pp. 3783–3791 (2024)
21. Liu, Z., Zhao, Z., Kolmus, A., Berns, T., van Laarhoven, T., Heskes, T., Larson, M.:
Going grayscale: The road to understanding and improving unlearnable examples.
arXiv preprint arXiv:2111.13244 (2021)
22. Madry, A., Makelov, A., Schmidt, L., Tsipras, D., Vladu, A.: Towards deep learning
models resistant to adversarial attacks. In: International Conference on Learning
Representations (2018)
23. Meerza, S.I.A., Sun, L., Liu, J.: Harmonycloak: Making music unlearnable for gen-
erative ai. In: 2025 IEEE Symposium on Security and Privacy (SP). pp. 430–448.
IEEE (2025)
24. Meng, R., Yi, C., Yu, Y., Yang, S., Shen, B., Kot, A.C.: Semantic deep hiding
for robust unlearnable examples. IEEE Transactions on Information Forensics and
Security (2024)
25. Preechakul, K., Chatthee, N., Wizadwongsa, S., Suwajanakorn, S.: Diffusion au-
toencoders: Toward a meaningful and decodable representation. In: Proceedings of
the IEEE/CVF conference on computer vision and pattern recognition. pp. 10619–
10629 (2022)
26. Qin, T., Gao, X., Zhao, J., Ye, K., Xu, C.Z.: Learning the unlearnable: Ad-
versarial augmentations suppress unlearnable example attacks. arXiv preprint
arXiv:2303.15127 (2023)
27. Ren, J., Xu, H., Wan, Y., Ma, X., Sun, L., Tang, J.: Transferable unlearnable
examples. arXiv preprint arXiv:2210.10114 (2022)
28. Russakovsky, O., Deng, J., Su, H., Krause, J., Satheesh, S., Ma, S., Huang, Z.,
Karpathy, A., Khosla, A., Bernstein, M., et al.: Imagenet large scale visual recog-
nition challenge. International journal of computer vision115(3), 211–252 (2015)
29. Shafahi, A., Huang, W.R., Najibi, M., Suciu, O., Studer, C., Dumitras, T., Gold-
stein, T.: Poison frogs! targeted clean-label poisoning attacks on neural networks.
In: NeurIPS (2018)
30. Song, J., Meng, C., Ermon, S.: Denoising diffusion implicit models. In: International
Conference on Learning Representations (2021)
31. Song, Y., Shu, R., Kushman, N., Ermon, S.: Constructing unrestricted adversar-
ial examples with generative models. Advances in neural information processing
systems31(2018)
32. Tao, L., Feng, L., Yi, J., Huang, S.J., Chen, S.: Better safe than sorry: Preventing
delusive adversaries with adversarial training. In: Advances in neural information
processing systems. pp. 16209–16225 (2021)
33. Voigt, P., Von dem Bussche, A.: The eu general data protection regulation (gdpr).
A Practical Guide, 1st Ed., Cham: Springer International Publishing10(3152676),
10–5555 (2017)
34. Wang, D., Xue, M., Li, B., Camtepe, S., Zhu, L.: Provably unlearnable data ex-
amples. arXiv preprint arXiv:2405.03316 (2024)
35. Wang, S., Chen, S., Chen, T., Nepal, S., Rudolph, C., Grobler, M.: Generating se-
mantic adversarial examples via feature manipulation in latent space. IEEE Trans-
actions on Neural Networks and Learning Systems (2023)
36. Wang, Z., Bovik, A.C., Sheikh, H.R.: Structural similarity based image quality
assessment. In: Digital Video image quality and perceptual coding, pp. 225–242.
CRC Press (2017)

18 Meerza et al.
37. Wu, Q., Yu, Y., Kong, C., Liu, Z., Wan, J., Li, H., Kot, A.C., Chan, A.B.: Tem-
poral unlearnable examples: Preventing personal video data from unauthorized
exploitation by object tracking. In: Proceedings of the IEEE/CVF International
Conference on Computer Vision. pp. 11110–11121 (2025)
38. Xiao, C., Li, B., Zhu, J., He, W., Liu, M., Song, D.: Generating adversarial examples
with adversarial networks. In: Proceedings of the Twenty-Seventh International
Joint Conference on Artificial Intelligence (IJCAI). pp. 3905–3911 (2018)
39. Xie, C., Wu, Y., Maaten, L.v.d., Yuille, A.L., He, K.: Feature denoising for im-
proving adversarial robustness. In: Proceedings of the IEEE/CVF conference on
computer vision and pattern recognition. pp. 501–509 (2019)
40. Zhao, Z., Duan, J., Hu, X., Xu, K., Wang, C., Zhang, R., Du, Z., Guo, Q., Chen,
Y.: Unlearnable examples for diffusion models: Protect data from unauthorized
exploitation. arXiv preprint arXiv:2306.01902 (2023)
41. Zhu, P., Osada, G., Kataoka, H., Takahashi, T.: Frequency-aware gan for adver-
sarial manipulation generation. In: Proceedings of the IEEE/CVF international
conference on computer vision. pp. 4315–4324 (2023)
42. Zhu, Y., Yu, L., Gao, X.S.: Detection and defense of unlearnable examples. In:
Proceedings of the AAAI Conference on Artificial Intelligence. vol. 38, pp. 17211–
17219 (2024)
