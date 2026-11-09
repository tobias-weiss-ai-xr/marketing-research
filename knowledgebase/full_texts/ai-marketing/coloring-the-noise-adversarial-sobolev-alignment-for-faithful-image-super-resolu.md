---
title: 'Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution'
url: https://arxiv.org/abs/2605.23264
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Hongbo Wang
- Huaibo Huang
- Pin Wang
- Jinhua Hao
- Chao Zhou
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.23264
pages: 23
chars: 72158
fetched_at: '2026-11-08T13:26:21+00:00'
kb_version: 1
---

# Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution

Coloring the Noise: Adversarial Sobolev Alignment for Faithful
Image Super Resolution
Hongbo Wang †1 2 3 Huaibo Huang 1 2 Pin Wang 1 2 Jinhua Hao 3 Chao Zhou 3 Ran He 1 2
Code: https://github.com/wafer-bob/ASASR
Abstract
Generative priors in Image Super-Resolution (SR)
often compromise faithful restoration, we at-
tribute this limitation to a fundamental spectral
misalignment between isotropic objectives and
the intrinsic natural image manifold. While Di-
rect Preference Optimization offers a path to align-
ment, its reliance on spectrally flat Gaussian noise
fails to distinguish authentic high-frequency de-
tails from hallucinations. To bridge this geo-
metric gap, we proposeASASR, a theoretically
grounded framework that recasts the generative
flow into a Sobolev-induced Riemannian geom-
etry by explicitly coloring the noise transition
kernel to mirror natural spectral decay. Driving
this geometric alignment, we integrate a paramet-
ric adversary grounded in the Riesz Representa-
tion Theorem, which synthesizes targeted neg-
ative samples equivalent to worst-case Sobolev
gradients to direct optimization along the tangent
space of plausible structural failures. Extensive
evaluations demonstrate that ASASR outperforms
leading generative baselines, particularly in pre-
serving spectral consistency and structural fidelity,
offering a robust solution that effectively mitigates
artifacts.
1. Introduction
Image Super-Resolution (SR) functions as a fundamental
inverse problem, aiming to reconstruct high-quality (HQ)
images from their degraded low-quality (LQ) counterparts.
†Work was done during an internship at Kuaishou. 1MAIS
& NLPR, Institute of Automation, Chinese Academy of Sci-
ences, Beijing, China 2School of Artificial Intelligence, Univer-
sity of Chinese Academy of Sciences, Beijing, China 3Kuaishou
Technology, Beijing, China. Correspondence to: Huaibo Huang
<huaibo.huang@cripac.ia.ac.cn>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
Leveraging the powerful generative priors of large-scale
vision models (Saharia et al., 2022; Rombach et al., 2022;
Esser et al., 2024; Labs, 2024), recent approaches have
achieved significant breakthroughs in synthesizing realistic
textures (Wu et al., 2024; Yu et al., 2024). However, the pre-
vailing supervised training paradigm imposes a fundamental
ceiling on faithful restoration, as it inherently anchors the
optimization process to synthetic degradation priors rather
than the authentic natural image manifold. Given that real-
world degradation is often unknown and ill-posed, standard
methods act by enforcing strict pixel-wise alignment on syn-
thetic data pairs. This rigid dependency compels the model
to overfit to artificial degradation assumptions, ef fectively
prioritizing the memorization of synthetic patterns over the
capture of authentic natural textures.
To explicitly penalize such stochastic deviations and enforce
manifold adherence, adapting Direct Preference Optimiza-
tion (DPO) (Rafailov et al., 2024) offers a potential path
alignment. However, we attribute the limited efficacy of
standard DPO in SR to a fundamental geometric flaw: its
reliance on naive isotropic Gaussian parameterization (Ho
et al., 2020). Specifically, as shown in Fig. 3, our analysis
reveals that this spectrally flat prior diverges sharply from
the intrinsic spectral decay of natural images (Field, 1987;
Rahaman et al., 2019). While acceptable for Text-to-Image
(T2I) synthesis, this spectral misalignment proves detri-
mental for Super-Resolution, which demands strict high-
frequency fidelity. Consequently, lacking the inductive bias
to differentiate authentic details from spurious noise, such
isotropic objectives inevitably yield high-frequency artifacts
that violate the data manifold.
In response to these challenges, we proposeASASR:
AdversarialSobolevAlignment forSuper-Resolution, a
theoretically grounded framework that induces natural man-
ifold constraints for faithful image super-resolution. Specif-
ically, we introduceSobolev Spectral Rectification (SSR)to
color the noise in the data representation, parameterizing
the transition kernel via Colored Gaussian Noise defined
by a structured covariance matrix that explicitly mirrors the
spectral density of natural textures. Crucially, we derive
that this alignment with natural statistics fundamentally re-
1
arXiv:2605.23264v2  [cs.CV]  26 Jun 2026

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
DP2OSR DiT4SR ASASR
Real-ESRGAN SeeSRStableSRSwinIR
SUPSRLQ Input
Figure 1.Visual comparison with state-of-the-art SR methods. The proposed ASASR achieves superior perceptual quality, generating
more realistic textures and faithful structural details from the low-quality input.
shapes the optimization objective, mathematically evolving
the implicit distance metric into the Sobolev norm H s. By
traversing the solution space within this Sobolev-induced
Riemannian geometry, the model gains a frequency-aware
inductive bias, enabling the precise rectification of structural
artifacts that are otherwise invisible to isotropic priors.
However, the geometric precision established by SSR re-
mains dormant without challenging supervisory signals to
drive it. A critical bottleneck in standard DPO paradigms
stems from the scarcity of informative negative samples,
where static pairs often fail to capture the subtle structural
nuances required for the ill-posed nature of super-resolution.
To transcend this limitation, we introduceAdversarial Mani-
fold Guidance (AMG), a parametric adversary that character-
izes the manifold of realistic artifacts to synthesize targeted,
semantically aligned negatives on the fly. Integrating this dy-
namic supervision establishes our Adversarial Sobolev DPO
(AS-DPO) framework. Grounded in the Riesz Representa-
tion Theorem, we demonstrate that AS-DPO leverages these
perturbations as worst-case Sobolev gradients, steering op-
timization along the tangent space of plausible perceptual
failures.
To empirically validate our framework, we conduct ex-
tensive evaluations on super-resolution benchmarks and
downstream high-level vision tasks, benchmarking ASASR
against leading diffusion-based and GAN-based approaches.
Beyond conventional distortion and perceptual metrics, we
also evaluate spectral fidelity to assess how closely the gen-
erated frequency profiles match the ground truth. Our results
demonstrate that ASASR achieves superior performance in
balancing fidelity and realism and boosting downstream
accuracy, successfully reconstructing high-frequency tex-
tures that align with natural image statistics while effectively
mitigating artifacts.
Our contributions can be summarized as follows:
• We identify the spectral disparity between isotropic
generative priors and natural image statistics as a criti-
cal bottleneck in SR, and propose ASASR, a geometry-
aware framework designed to bridge this gap by en-
forcing strict manifold adherence.
• We introduce Sobolev Spectral Rectification to color
transport noise, reshaping the implicit optimization
metric to align with natural spectral statistics and rec-
tify frequency-biased hallucinations.
• We propose Adversarial Manifold Guidance to synthe-
size targeted negatives, proving that these perturbations
constitute worst-case Sobolev gradients specifically
driving optimization along the tangent space of plausi-
ble failures.
• Extensive evaluations demonstrate that ASASR
achieves superior performance over leading genera-
tive methods, particularly in preserving spectral consis-
tency and fine-grained structural fidelity.
2. Background
Flow Matching.We construct our approach within the
Flow Matching framework (Lipman et al., 2023), adapted
here for conditional generation. Let x1 ∼q(x 1|c) denote
the high-resolution data distribution conditioned on the low-
resolution input c, and let x0 ∼p(x 0) =N(0,I) be the
prior noise distribution. We define a conditional probability
path between noise and data via linear interpolation:
xt = (1−t)x 0 +tx 1, t∈[0,1],(1)
Differentiating with respect to time yields the conditional
vector field ut(x|x0,x 1) =x 1 −x 0. To approximate this
field, a velocity network vθ(xt, t,c)is trained by minimiz-
ing the conditional flow matching objective:
LCFM(θ) =E t,x0,x1
h
∥vθ(xt, t,c)−(x 1 −x 0)∥2
i
,(2)
Direct Preference Optimization.To align the generative
prior with human perception, we employ DPO (Rafailov
et al., 2024) using preference triplets D={(c,x w 1 ,x l 1)}.
To circumvent intractable likelihood computation, we ex-
tend the objective to the trajectory space governed by ODE.
2

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Isotropous
Gaussian
Anisotropic
Gaussian
Projection
NaturalManifold
Euclidean
Projection
NaturalManifold
Spatially
Separated
Co-located
DPO Direction
(a) General SR System (c) ASASR (Ours) Sobolev Alignment
(b) Adversarial DPO Direction
NaturalManifold
AdversarialLearning Adversarial Net
Baselines
DPO
 Direction
Sobolev
SpaceSpace
Supervised Learning Gaussian Parameterization Spectral DiscrepancyData ManifoldLQDistribution GTDistribution
Figure 2.Conceptual illustration of spectral misalignment and our proposed ASASR.(a)Standard SR frameworks always assume an
isotropic Euclidean space, a simplification that neglects the intrinsic spectral nature of real-world data. This geometric mismatch projects
the generated candidate xhq onto a manifold disjoint from the ground truth xgt, resulting in the significant spectral discrepancy (hatched
region).(b)To bridge this geometric gap, we characterize the manifold of realistic artifacts using diverse baseline hypotheses (green
nodes). The adversary Aϕ approximates the distribution of these plausible inconsistencies by learning the mapping from xgt, effectively
encoding generative artifact patterns into a learnable prior.(c)Our ASASR framework integrates this targeted guidance within a reshaped
Sobolev geometry. By enforcing an anisotropic Gaussian prior, we rectify the optimization landscape, ensuring the projection trajectory is
spectrally accurate and co-located with the target distribution, effectively resolving the misalignment in (a).
By optimizing over the resulting deterministic evolution
pathsx 0:1, the trajectory-wise loss is defined as:
LDPO(θ) =−E (c,xw 1 ,xl 1)∼D
"
logσ

β
"
log pθ(xw 0:1|c) pref(xw 0:1|c) −log pθ(xl 0:1|c) pref(xl 0:1|c) #!# , (3)
where σ(·) denotes the logistic sigmoid function, the tem-
perature hyperparameterβcontrols regularization.
Sobolev Space.The Sobolev space H s(Ω) (Adam &
Fournier, 2003) provides a rigorous basis for quantifying
regularity on Ω⊂R 2. Unlike the standard L2 framework
that treats pixel intensity independently,H s(Ω) explicitly in-
corporates smoothness constraints. Ideally viewed through
a spectral lens, H s is defined by a strict decay condition on
Fourier coefficients, ensuring that signal energy is predomi-
nantly concentrated in low-frequency modes. Formally, as-
suming periodic boundaries with frequency vector ω∈Z 2
and coefficients ˆf(ω), the space is defined fors≥0as:
H s(Ω) =  f∈L 2 : X
ω
(1 +∥ω∥ 2)s| ˆf(ω)| 2 <∞ 	 ,(4)
where the term (1 +∥ω∥ 2)s acts as a frequency-dependent
penalty enforcing natural spectral distribution. This space is
equipped with the inner product and norm:
⟨f, g⟩H s =
X
ω
(1 +∥ω∥ 2)s ˆf(ω) ∗ˆg(ω),(5)
∥f∥ 2 H s =⟨f, f⟩H s ,(6)
3. Manifold Rectification in Sobolev Space
3.1. The Spectral Deficiency of Euclidean DPO
To make the optimization of Eq. (3) tractable, we approxi-
mate the continuous probability flow using standard Euler
integration. Following the Flow Matching formulation, we
parameterize the local transitions for the ideal posterior q
and the policy pψ as Gaussian approximations centered on
the deterministic ODE trajectories:
q(xt−∆t|xt,x 1) =N

xt − x1 −x t 1−t ∆t, η2∆tI  ,(7)
pψ(xt−∆t|xt,c) =N

xt −v ψ(xt, t,c)∆t, η2∆tI  ,(8)
where ψ∈ {θ,ref}, η represents an auxiliary variance pa-
rameter for the likelihood definition. Crucially, this isotropic
parametrization implies an underlying Euclidean geometry.
Let γθ denote the residual between the model prediction
and the target vector field:
γθ(xt,c) :=v θ(xt,c)−v q(xt),(9)
Consequently, the log-likelihood ratio objective reduces to
a difference of squaredℓ 2 norms:
log pθ(xt−∆t|xt,c) pref(xt−∆t|xt,c) ∝ −  ∥γθ∥2 2 − ∥γref∥2 2  ,(10)
However,we trace the root of the identified spectral misalign-
ment to this reliance on the ℓ2 norm. Invoking Parseval’s
theorem, we can express the spatial error in the frequency
domain as:
∥γθ∥2 2 =∥F(γ θ)∥2 2 = 1 M N X k 1|{z} weight · ∥ˆγθ[k]∥2,(11)
3

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
where F denotes the Fourier transform, ˆγθ[k] represents the
spectral error component at frequency index k, ˆγθ(ω) rep-
resents the spectral error component at frequency ω, M and
N denote the spatial dimensions of the image. This identity
explicitly demonstrates that the optimization imposes a uni-
form weighting across the entire spectrum. Such spectral
indifference proves catastrophic in practice. As visualized
in Fig. 3, the standard ℓ2 objective fails to counteract the
inherent spectral bias of neural networks (Rahaman et al.,
2019), causing the learned distribution to diverge signifi-
cantly from natural image statistics in the high-frequency
region. This spectral deficit is not merely theoretical; it
directly manifests as the loss of fine texture and artifacts.
Detailed derivation is provided in Appendix A.1.
3.2. Reshaping Optimization Geometry via Sobolev
Spectral Rectification
To mitigate the frequency-agnostic nature of standard Eu-
clidean objectives, we proposeSobolev Spectral Rectifica-
tion, a method that reshapes the underlying optimization
geometry by substituting the isotropic noise assumption
with colored Gaussian noise. Formally, we generalize the
transition kernels in Eqs. (7)–(8) by replacing the identity
covarianceIwith a structured spectral operatorΣ s:
Σs =F −1diag  (1 +∥ω∥ 2 2)−s F,(12)
This structured covariance induces a fundamental shift in the
optimization metric. As the Gaussian likelihood is governed
by the Mahalanobis distance, the learning signal is shaped
by the precision matrix Σ−1 s . While Σs acts as a low-pass
filter, its inverse Σ−1 s amplifies high-frequency components,
thereby imposing strictly higher penalties on fine-grained
discrepancies. Analytically, Σ−1 s recovers the Sobolev in-
ner product operator as introduced in Eq. (5), effectively
lifting the optimization from flat Euclidean space to the
weighted Sobolev manifoldH s(Ω). Consequently, the log-
likelihood ratio in Eq. (24) can be explicitly reformulated
as a difference of squared Sobolev norms:
log pθ(xt−∆t |x t,c) pref(xt−∆t |x t,c) ∝ −  ∥γθ∥2 H s −∥γ ref∥2 H s  ,(13)
This formulation offers a compelling physical interpretation:
the preference optimization is driven by the spectral energy
of the restoration errors conditioned on c. We define the
Sobolev Energy Gap,∆EH s, to quantify the policy’s relative
advantage in recovering frequency-weighted details:
∆EH s (xt,c) :=∥γ θ(xt,c)∥ 2 H s − ∥γref(xt,c)∥ 2 H s ,(14)
Since Gaussian likelihoods imply a reward r∝ −∥γθ∥2 H s,
maximizing preference is mathematically equivalent to mini-
mizing the energy difference ∆EH s (xw)−∆E H s (xl). Sub-
stituting this energy margin into the logistic loss yields our
(b) Real-WorldDataset(a) SyntheticDataset
High-Frequency
Region
High-Frequency
Region
Misalignment Misalignment
Figure 3.Power Spectral Density analysis relative to the Natural
Dataset. The ℓ2 baseline exhibits noticeable decay in high frequen-
cies, illustrating the spectral bias inherent to Euclidean constraint.
In contrast, our Sobolev constraint closely aligns with the empirical
distribution, effectively preserving fine-grained structural fidelity.
final objective, the S-DPO:
LS-DPO(θ) =−E (c,xw 1 ,xl 1)∼D,t∼U(0,T)
h
logσ

β
h
∆EH s (xl t,c)−∆E H s (xw t ,c) ii , (15)
Detailed derivation is provided in Appendix A.2.
4. Adversarial Manifold Guidance
4.1. AS-DPO for Aligned Preference Learning
With the S-DPO objective established, acquiring suitable
preference data is critical. Standard SR datasets are incom-
patible, offering regression-oriented pairs (xLQ,x GT) rather
than comparative triplets. Furthermore, existing T2I pref-
erence datasets suffer from weak spatial correspondence:
since they rank distinct seeds, differences stem from seman-
tic layout rather than restoration quality (Lu et al., 2025; Zhu
et al., 2025). This prevents xl from serving as a spatially
aligned negative, obscuring genuine structural degradation.
In response to these challenges, we introduceAdversar-
ial Manifold Guidance (AMG), a parametric adversary Aϕ
designed to capture the manifold of realistic artifacts for
on-the-fly preference synthesis. To train Aϕ, we leverage
outputs from standard baselines as proxies to approximate
realistic artifacts, optimizing the network to faithfully mimic
typical reconstruction failures found in real-world models.
With this trained adversary, we employ a coupled sampling
strategy to ensure strict semantic alignment. Starting from
an intermediate winner state xw t along the conditional path
(Eq. (1)), the adversary predicts a velocity field vϕ that
steers the trajectory toward a degraded estimate bxa 1. By
forecasting the terminal state via linear extrapolation, we
4

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
win loss
 win loss
win loss win loss
Figure 4.Visualization of targeted negatives synthesized. These
samples constitute realistic structural artifacts, such as text defor-
mations and architectural distortions, serving as hard negatives.
derive:
bxa 1 =x w t + (1−t)·v ϕ(xw t , t,c),(16)
Critically, to enforce semantic alignment, we re-project this
degraded estimate back to the flow state xa t using theidenti-
calnoise realizationx 0 from the winner branch:
xa t = (1−t)x 0 +t bxa 1,(17)
By strictly enforcing a shared noise realization (t,ϵ) across
both trajectories, the resulting pair (xw t ,x a t ) achieves pre-
cise semantic alignment. This constraint effectively gener-
ates a counterfactual negative sample, isolating perceptual
degradations directly tied to the image content rather than
random stochastic variations. Integrating this aligned gen-
eration strategy into our framework, we reformulate the
objective in Eq. (29) into its adversarial variant, termed
AS-DPO:
LAS-DPO(θ) =−E (c,xw 1 )∼D,x a 1 ∼Aϕ, t∼U(0,T)
h
log
σ

β
h
∆EH s (xa t ,c)−∆E H s (xw t ,c) ii , (18)
4.2. Exploiting Model Confidence in Structural Artifacts
While coupled sampling ensures semantic alignment, pref-
erence learning efficacy depends on the informativeness
of negative samples. A critical pathology in generative
models is their tendency to exhibitMisaligned Confidence:
assigning low residual energy (high likelihood) not only to
ground truth data but also to samples containing significant
structural degradations. We term theseSpectral Artifacts:
coherent structural hallucinations patterns—such as textural
distortions or aliasing—that the model fails to penalize due
to the inherent biases of theℓ 2 training objective.
To construct informative hard negatives, our AMG targets
Misaligned Confidence—a pathology where models assign
high likelihood (low residual) to structurally degraded sam-
ples. Unlike standard adversaries that maximize loss to gen-
erate noise, Aϕ seeks to expose these blind spots. Specif-
ically, we search for perturbations that minimize the Eu-
clidean residual energy JL2—mimicking the model’s intrin-
sic confidence—while forcefully deviating from the ground
truth trajectory via a Sobolev constraint.
Proposition 4.1.We formulate the synthesis of the hard
negative xa t as minimizing the Euclidean residual energy
JL2 (x) :=∥γ θ(x)∥2 2, subject to a structural trust region
defined by the Sobolev norm ∥δt∥H s ≤ε t. The optimal
adversarial perturbationδ ∗ t is given by:
δ∗ t =−ε t Σs∇xJL2 p ⟨ ∇xJL2 ,Σ s∇xJL2 ⟩L2 ,(19)
This formulation addresses the core challenge of preference
learning: distinguishing between realistic details and model
hallucinations. By driving the perturbation along the nega-
tive gradient of the ℓ2 energy, the adversary actively seeks
states where the model is deceptively confident despite the
presence of visual degradation. Crucially, the spectral pre-
conditioner Σs prevents the adversary from collapsing into
trivial random noise (which is easily filtered). Instead, it
steers the generation towards coherent structural artifacts,
structured errors that mimic the model’s intrinsic failure
modes, thereby providing high-value training signals for
S-DPO. Detailed derivation is provided in Appendix B.1.
Since computing Eq. (19) explicitly is intractable, we em-
ploy a parametric adversary Aϕ. The following proposition
guarantees its theoretical validity.
Proposition 4.2.Let ϕ∗ be the parameters minimizing
the expected energy E[JL2 (xt +A ϕ(xt))] subject to
∥Aϕ∥H s ≤ε t. Assuming sufficient representational capac-
ity, the adversary implicitly recovers the optimal Sobolev
direction:
Aϕ∗ (xt) =−ε t
Σs∇xJL2
∥Σs∇xJL2 ∥H s
≡δ ∗ t ,(20)
where the sufficient representational capacity assumption
only means that the parametric adversary can approximate
the Sobolev-optimal direction in function space. More de-
tails are provided in Appendix B.2. Minimizing the en-
ergy loss is locally equivalent to minimizing the inner prod-
uct ⟨∇xJL2 ,A ϕ⟩L2. Through spectral duality, this forces
the network to align anti-parallel to the Sobolev gradient
∇H s x JL2, thereby distilling the optimal spectral descent step
into a single forward pass. Detailed derivation is provided
in Appendix B.2.
5

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Table 1.Quantitative comparison with state-of-the-art real-world SR methods on both synthetic and real-world benchmarks. Best and
second best performance are highlighted inredandblue, respectively.
Datasets Metrics BSRGAN Real- ESRGAN SwinIR- GAN StableSR DiffBIR FaithDiff SeeSR SUPSR Dream- Clear DP2O-SR DiT4SRASASR
DIV2K-Val
PSNR↑ 20.3621.1120.43 19.93 19.85 19.82 20.46 19.66 19.79 19.60 19.0120.60
SSIM↑ 0.56370.58700.5678 0.5528 0.4720 0.5167 0.5411 0.4902 0.5137 0.5064 0.50500.6171
LPIPS↓ 0.3899 0.3147 0.3214 0.30160.3748 0.3189 0.3325 0.3721 0.3206 0.3130 0.32990.2784
DISTS↓ 0.2410 0.2191 0.2181 0.2040 0.2273 0.20830.19860.2328 0.2076 0.2042 0.20870.2038
MANIQA↑ 0.3097 0.3726 0.3505 0.4224 0.5252 0.4349 0.5187 0.5354 0.4878 0.5810 0.45070.6519
MUSIQ↑ 54.51 61.24 58.70 66.30 66.57 70.5970.5964.65 60.66 70.58 68.1071.40
CLIPIQA+↑ 0.5641 0.6126 0.5883 0.6702 0.6897 0.67670.72220.6753 0.6356 0.7142 0.69910.7521
LSDIR-Val
PSNR↑ 16.8817.1216.87 16.54 16.80 16.7116.9116.36 16.19 16.55 15.91 16.83
SSIM↑ 0.44130.4528 0.4464 0.4012 0.3909 0.4093 0.4208 0.3710 0.4010 0.4049 0.3887 0.4448
LPIPS↓ 0.3992 0.3453 0.3572 0.3285 0.3819 0.3239 0.3366 0.3884 0.33350.31530.35610.2854
DISTS↓ 0.2410 0.2235 0.2209 0.2047 0.2123 0.1956 0.1917 0.2247 0.19420.18760.19750.1757
MANIQA↑ 0.3549 0.4271 0.3874 0.4736 0.5678 0.4435 0.55460.63920.6203 0.6299 0.49880.6372
MUSIQ↑ 63.09 67.53 65.12 70.80 70.26 71.8373.2669.18 68.01 73.11 71.6973.97
CLIPIQA+↑ 0.6184 0.6756 0.6571 0.7089 0.7375 0.7095 0.7451 0.7420 0.72200.77730.71060.7761
RealSR
PSNR↑ 23.32 24.0124.44 23.06 23.75 23.58 23.51 23.35 23.64 23.35 21.7824.09
SSIM↑ 0.73010.7340 0.7461 0.6772 0.6173 0.6757 0.6944 0.6342 0.6845 0.6602 0.6292 0.7221
LPIPS↓ 0.2788 0.27330.2535 0.3047 0.3713 0.2895 0.3001 0.3706 0.3225 0.3159 0.31880.2497
DISTS↓ 0.2248 0.20690.1938 0.2152 0.2424 0.2108 0.2214 0.2482 0.2417 0.2221 0.22340.1986
MANIQA↑ 0.4001 0.3764 0.3476 0.4334 0.5047 0.4666 0.5400 0.4502 0.42320.58490.46020.5730
MUSIQ↑ 63.83 60.43 58.76 65.44 65.15 68.6569.1259.19 57.50 69.09 67.9471.78
CLIPIQA+↑ 0.5939 0.5878 0.5532 0.6506 0.6725 0.6529 0.6915 0.6131 0.58370.71340.66540.7200
DrealSR
PSNR↑ 25.1326.2826.22 25.82 24.81 25.13 25.96 24.7726.2425.46 23.72 25.77
SSIM↑ 0.75830.7771 0.7753 0.7177 0.5893 0.6736 0.7411 0.6249 0.7189 0.6845 0.6439 0.7356
LPIPS↓ 0.3038 0.28800.2737 0.3276 0.4806 0.3597 0.3163 0.4347 0.3555 0.3555 0.37000.2874
DISTS↓ 0.2292 0.20870.2037 0.2277 0.2962 0.2409 0.2295 0.2767 0.3558 0.2414 0.24440.2023
MANIQA↑ 0.3587 0.3434 0.3309 0.3901 0.4981 0.4584 0.5047 0.4158 0.31510.56410.44350.6067
MUSIQ↑ 59.25 54.28 52.77 59.18 59.81 66.21 64.72 54.52 42.8268.7164.6968.36
CLIPIQA+↑ 0.5935 0.5540 0.5355 0.6193 0.6518 0.6604 0.6716 0.5888 0.51760.67710.66740.6803
Table 2.Quantitative comparison on downstream tasks: OCR, Object Detection, Instance Segmentation, and Semantic Segmentation tasks.
Best and second best performance are highlighted inredandblue, respectively.
Task Metrics GT LQ BSRGAN Real- ESRGAN SwinIR- GAN StableSR DiffBIR FaithDiff SeeSR SUPSR Dream- Clear DP2O-SR DiT4SRASASR
OCR Precision↑ 64.87 33.75 41.83 44.82 48.06 42.77 44.48 41.90 45.74 48.7952.0050.74 51.3552.73 Recall↑ 50.32 3.81 4.11 7.61 7.31 21.77 23.74 31.71 29.33 36.78 23.9540.0329.9845.91
Object
Detection
APb ↑ 48.32 12.53 15.00 19.36 18.04 24.66 23.81 29.52 28.06 28.04 27.1733.5128.2035.62
APb 50 ↑ 68.00 20.64 23.61 30.12 28.60 38.06 36.82 45.24 43.57 43.80 40.7149.9144.4452.64
APb 75 ↑ 52.91 12.96 15.74 20.23 18.86 25.46 25.20 30.52 29.34 29.52 28.6936.0029.1838.56
Instance
Segmentation
APm ↑ 42.52 11.03 13.03 16.89 15.29 21.60 20.57 25.24 23.98 24.20 23.3729.2224.0730.98
APm 50 ↑ 65.29 18.96 22.08 28.00 26.32 35.49 34.08 41.81 39.56 40.82 38.3446.7740.3449.18
APm 75 ↑ 46.27 11.12 13.22 17.26 15.28 22.28 20.83 25.39 24.96 24.65 23.9930.5424.9733.09
Semantic
Segmentation
mIoU↑ 49.39 25.18 21.74 28.85 25.86 37.31 34.8241.7239.11 39.16 36.47 41.54 37.5743.33
PixAcc↑ 82.17 69.72 66.24 72.16 71.25 77.52 75.9378.8177.75 77.12 77.13 78.72 76.3280.24
5. Experiments
5.1. Experimental Setup
Training Datasets.We leverage the widely adopted
DIV2K (Lim et al., 2017) and LSDIR (Li et al., 2023)
datasets for training. To synthesize LQ input images, we
employ the higher-order degradation pipeline introduced
in Real-ESRGAN (Wang et al., 2021), strictly aligning the
hyperparameters with (Wu et al., 2024; Ai et al., 2024).
Testing Datasets.We evaluate generalization on both syn-
thetic and real-world benchmarks. For synthetic testing, we
sample 3,000 patches from DIV2K and LSDIR using the
training degradation pipeline. Real-world performance is
assessed on RealSR (Cai et al., 2019) and DRealSR (Wei
et al., 2020). Across all protocols, HQ and LQ resolutions
are standardized to512×512and128×128, respectively.
Metrics.Following (Wu et al., 2024; Ai et al., 2024), we
adopt PSNR and SSIM (calculated on the Y channel of trans-
6

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Real-ESRGAN StableSR SeeSR SUPSR DP2O-SR DiT4SR ASASR
LQ GT
LQ GT Real-ESRGAN StableSR SeeSR SUPSR DP2O-SR DiT4SR ASASR
LQ Real-ESRGAN StableSR SeeSR SUPSR DP2O-SR DiT4SR ASASR
LQ Real-ESRGAN StableSR SeeSR SUPSR DP2O-SR DiT4SR ASASR
Figure 5.Qualitative comparisons on both synthetic (the first two rows) and real-world (the last two rows) benchmarks.
formed YCbCr space) as reference-based distortion metrics,
LPIPS (Zhang et al., 2018) and DISTS (Ding et al., 2020) as
reference-based perceptual metrics, MANIQA (Yang et al.,
2022), MUSIQ (Ke et al., 2021) and CLIPIQA (Wang et al.,
2022) as no-reference metrics.
Baselines.We evaluate our proposed method against state-
of-the-art approaches covering diverse generative paradigms.
Specifically, we compare with representative GAN-based
methods, including BSRGAN (Zhang et al., 2021), Real-
ESRGAN (Wang et al., 2021), and SwinIR-GAN (Liang
et al., 2021). To assess performance against the most re-
cent generative priors, we evaluate Diffusion-based models
StableSR (Wang et al., 2024), DiffBIR (Lin et al., 2024),
FaithDiff (Chen et al., 2024), SeeSR (Wu et al., 2024),
SUPSR (Yu et al., 2024), DreamClear (Ai et al., 2024),
DP2OSR (Wu et al., 2025) and DiT4SR (Duan et al., 2025).
Implementation Details.We perform all experiments with
a scaling factor of ×4. Both the ASASR and the Adversarial
Network leverage the FLUX.1-dev (Labs, 2024) backbone,
fine-tuned via LoRA (Hu et al., 2021) ( r= 16, α= 16 ).
For the DPO alignment of ASASR, we adopt the AdamW
optimizer with a learning rate of 1e−5 . To train the Ad-
versarial Network, we curate a dataset by running inference
with Real-ESRGAN, SeeSR, and SUPSR on a random 25%
subset of DIV2K, LSDIR, RealSR, and DRealSR; this net-
work is optimized using AdamW with a learning rate of
5e−5 . The Sobolev parameter s is empirically set to 1.5.
All models are trained on 8 NVIDIA H800 GPUs. More
details are detailed in Appendix C.1.
5.2. Comparison with State-of-the-Art Methods
Quantitative Comparisons.Tab. 1 presents comparisons
against state-of-the-art methods. On synthetic datasets,
our approach achieves superior perceptual scores (LPIPS,
DISTS) and, unlike typical generative models prone to struc-
tural distortion, secures top ranks in SSIM, striking an opti-
mal fidelity-perception balance. On real-world benchmarks,
our model consistently dominates reference-free metrics
(MANIQA, MUSIQ, CLIPIQA+) while maintaining leading
full-reference performance. These results confirm that our
method significantly outperforms competitors, producing
restorations that are both photorealistic and structurally faith-
ful to the intrinsic image manifold. Moreover, to further val-
idate the effectiveness and generality of our method, we con-
duct additional experiments with different backbone models,
including SD1.5 (Rombach et al., 2022) and SDXL (Podell
et al., 2023). These experiments demonstrate that the per-
formance gains of our method do not rely on the FLUX
backbone. We also evaluate our method on more challeng-
ing real-world datasets, including RealLQ250 (Ai et al.,
2024), which contains diverse real-world low-quality im-
ages that are absent from our training data, and Bringing Old
Films Back to Life (Wan et al., 2022), a more challenging
dataset consisting of degraded old film frames. The results
7

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Real-ESRGAN StableSR SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT
36.59 39.92 38.50 36.41 40.39 43.92 27.35
Figure 6.Visual and Spectral Fidelity.Top:Super-resolution results.Bottom:FFT spectra with GT-difference insets annotated with
LSD scores. ASASR achieves the lowest LSD (27.35), quantitatively confirming its superior alignment with the ground truth spectral
distribution, evidenced by minimal residuals compared to baselines.
Table 3.Ablation study on different guidance and alignment strategies. We report perceptual metrics and downstream task performance.
Best values are highlighted inbold.
Methods PSNR↑SSIM↑LPIPS↓DISTS↓ MANIQA↑MUSIQ↑CLIPIQA+↑ Recall↑AP b ↑AP m ↑mIoU↑
Sobolev Guidance 20.60 0.6171 0.2784 0.2088 0.6519 71.40 0.7521 45.91 35.62 30.98 43.33
Eulidean Guidance 18.34 0.5742 0.3115 0.2337 0.6184 67.25 0.7196 41.64 34.18 29.74 42.15
Adversarial DPO Alignment 20.60 0.6171 0.2784 0.2088 0.6519 71.40 0.7521 45.91 35.62 30.98 43.33
DPO Alignment w/ Supervised Data 20.08 0.5723 0.3109 0.2345 0.6047 68.82 0.7163 40.16 32.49 28.51 40.26
Only Supervised Learning 19.96 0.5642 0.3135 0.2388 0.6012 69.15 0.7058 40.33 31.95 28.72 39.85
are provided in Appendix C.2.
Qualitative Comparisons.Visual comparisons in Fig. 5
demonstrate ASASR’s superiority on synthetic data, where
it restores sharp geometries and facial details without the
aliasing seen in baselines. In real-world scenarios, it ro-
bustly handles unknown degradations, synthesizing authen-
tic textures while suppressing artifacts. Furthermore, Fig. 6
substantiates this spectral fidelity, where ASASR achieves
the lowest Log-Spectral Distance (LSD) and minimal resid-
uals, confirming that our model faithfully reconstructs the
intrinsic frequency decay of natural images. Additional
comparisons are in Appendix C.4.
User Study.We conducted a comprehensive user study with
50 participants to evaluate restoration quality across 64 test
images. Users were tasked with ranking our method against
baselines based on visual naturalness and fidelity. Results
shows that our model consistently outperforms all competi-
tors achieving a Top-1 ratio of 91.1%. See Appendix C.3
for visualization and details.
Downstream Tasks Evaluation.To validate whether se-
mantic information is preserved under degraded inputs,
we conduct downstream evaluations on COCO (Lin et al.,
2015) for object detection and instance segmentation,
ADE20K (Zhou et al., 2017) for semantic segmentation,
and ICDAR 2024 Occluded RoadText (George Tom et al.,
2024) for OCR. We adopt representative and widely used
architectures for these tasks, including Mask R-CNN (He
et al., 2018), SegFormer-B5 (Xie et al., 2021), and Pad-
dleOCR v3 (Li et al., 2022), respectively. For evaluation,
COCO images are standardized to 512×512 , while crop-
ping is applied to ADE20K and a 2,000-frame subset of
ICDAR to better preserve local structures and fine-grained
textual details. Using the identical degradation pipeline as
in training, our method achieves SOTA performance across
all metrics (Tab. 2), indicating stronger fidelity in preserving
high-level semantic structures under challenging degrada-
tions. Detailed quantitative results and additional analyses
are provided in Appendix C.4.
5.3. Ablation Study
We perform ablation studies to scrutinize the contributions
of our guidance and alignment mechanisms, as detailed in
Tab. 3. Across perceptual (PSNR, SSIM, LPIPS, DISTS),
quality (MANIQA, MUSIQ, CLIPIQA+), and semantic
metrics (Recall, AP, mIoU), our full method consistently
outperforms ablated versions. Regarding guidance,Sobolev
Guidance(Full Model) yields significantly superior results
compared toEuclidean Guidance(w/o SSR), validating its
optimization effectiveness. Similarly, for alignment,Ad-
versarial DPO(Full Model) demonstrates a clear advan-
tage over bothOnly Supervised Learning(w/o SSR&AMG)
and standardDPO w/ Supervised Data(w/o AMG). The
comparison among these variants highlights the coupling
between SSR and AMG: AMG supplies realism-oriented
alignment, whereas SSR provides a spectrally aware ge-
8

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
0 0.5 1.0 1.5 2.0 4.0
Scale s
0.27
0.28
0.29
0.30
0.31
LPIPS
Sobolev
Euclid
0 0.5 1.0 1.5 2.0 4.0
Scale s
0.205
0.210
0.215
0.220
0.225
0.230
0.235
DISTS
Sobolev
Euclid
0 0.5 1.0 1.5 2.0 4.0
Scale s
0.615
0.620
0.625
0.630
0.635
0.640
0.645
0.650
0.655
MANIQA
Sobolev
Euclid
0 0.5 1.0 1.5 2.0 4.0
Scale s
67
68
69
70
71
72
MUSIQ
Sobolev
Euclid
Figure 7.Impact analysis on the Sobolev index s. We select s= 1.5 (marked by star) as the optimal trade-off between structural fidelity
and texture realism.
ometry that regularizes its optimization trajectory. As a
result, applying AMG without SSR may introduce aggres-
sive high-frequency details that benefit perceptual realism
less consistently and can impair distortion-oriented metrics,
while their combination enables alignment to improve per-
ceptual quality without sacrificing reconstruction fidelity.
Notably, substantial gains in downstream tasks confirm that
our strategies enhance photorealism while preserving the
semantic integrity essential for high-level vision.
In addition, we conduct sensitivity analysis on the Sobolev
index s. As shown in Fig. 7, while stronger regularity
(s≥2 ) benefits reference-based metrics via aggressive
smoothing, it degrades perceptual quality by erasing high-
frequency textures. We thus adopt s= 1.5 as the optimal
equilibrium between fidelity and realism.
6. Related Work
The evolution of image super-resolution has shifted from
GAN-based training (Zhang et al., 2021; Wang et al., 2021;
Liang et al., 2021) toward exploiting large-scale genera-
tive priors (Wang et al., 2024; Lin et al., 2024; Wu et al.,
2024; Yu et al., 2024), which provide stronger natural image
priors for blind and real-world restoration. This paradigm
now encompasses diverse architectures, including Diffusion
Transformers (Cheng et al., 2024; Duan et al., 2025), autore-
gressive models (Qu et al., 2025), as well as Gaussian (Hu
et al., 2024) and spiking (Xiao et al., 2025) formulations,
reflecting a broad trend toward leveraging more expressive
generative backbones. Recent advances further improve
practical usability through efficient distillation (Xu et al.,
2025; Li et al., 2025a), while semantic or textual guidance
has been introduced to enhance controllability and preserve
high-level content (Chen et al., 2025; Hu et al., 2025; Zuo
et al., 2025). Despite their impressive perceptual quality,
generative SR models remain prone to hallucinated textures
and structurally inconsistent details, especially under severe
or out-of-distribution degradations. To address this issue, re-
cent studies explore alignment strategies (Chen et al., 2024;
Li et al., 2025b) and DPO-style adaptations that encourage
outputs to better match human or perceptual preferences.
Notably, DP2O-SR (Wu et al., 2025) steers generation via
aggregated IQA metrics; however, such heuristic optimiza-
tion lacks a principled theoretical foundation, disconnecting
the proxy objective from the intrinsic geometric structure of
the natural image manifold.
7. Conclusion
We propose ASASR to bridge the spectral gap between
isotropic generative priors and the natural image manifold.
By enforcing Sobolev Spectral Rectification, our method
constrains optimization within a Riemannian geometry that
respects the characteristic spectral decay of natural images,
thereby promoting perceptually plausible yet structurally
faithful restoration. This process is driven by a Riesz-
grounded adversary, which leverages worst-case Sobolev
gradients to identify and rectify structural deviations that
are often overlooked by conventional pixel- or perception-
level objectives. Extensive experiments demonstrate that
ASASR achieves a superior fidelity-realism balance across
diverse degradations and backbones. More broadly, our
framework provides a rigorous spectral-geometric blueprint
for addressing hallucination and alignment challenges in
ill-posed inverse problems.
Impact Statement
This work presents a robust framework for high-fidelity im-
age super-resolution with significant potential for consumer
imaging deployment. By effectively mitigating spectral
artifacts, our method empowers mobile imaging systems
to overcome hardware limitations like digital zoom and
low-light noise. Furthermore, as user-generated content
platforms (e.g., photo-logs) expand, our approach serves as
a vital cloud-based tool to revitalize compressed uploads.
By democratizing access to professional-grade restoration,
we aim to preserve the visual integrity of digital archives
and foster a high-quality digital ecosystem.
9

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Acknowledgement
This work was supported by National Natural Science
Foundation of China (Grant Nos. 62425606, 62576342,
62550062, 32341009), Beijing Natural Science Foundation
(4252054, L257008), Beijing Nova Program (20230484276,
20240484601). These contributions have been instrumental
in enabling the advancement of this work.
References
Adam, R. A. and Fournier, J. J.Sobolev Spaces. 2003.
Ai, Y ., Zhou, X., Huang, H., Han, X., Chen, Z., You, Q.,
and Yang, H. DreamClear: High-Capacity Real-World
Image Restoration with Privacy-Safe Dataset Curation.
InNeurIPS, 2024.
Cai, J., Zeng, H., Yong, H., Cao, Z., and Zhang, L. To-
ward Real-World Single Image Super-Resolution: A New
Benchmark and A New Model. InICCV, 2019.
Chen, C., Abdolshah, M., Shevchenko, V ., Li, H., Xu, C.,
and Purkait, P. SRSR: Enhancing Semantic Accuracy
in Real-World Image Super-Resolution with Spatially
Re-Focused Text-Conditioning. InNeurIPS, 2025.
Chen, J., Pan, J., and Dong, J. FaithDiff: Unleashing Diffu-
sion Priors for Faithful Image Super-resolution. InCVPR,
2024.
Cheng, K., Yu, L., Tu, Z., He, X., Chen, L., Guo, Y ., Zhu,
M., Wang, N., Gao, X., and Hu, J. Effective Diffusion
Transformer Architecture for Image Super-Resolution. In
AAAI, 2024.
Ding, K., Ma, K., Wang, S., and Simoncelli, E. P. Im-
age Quality Assessment: Unifying Structure and Texture
Similarity.IEEE Trans. Pattern Anal. Mach. Intell., 2020.
Duan, Z.-P., Zhang, J., Jin, X., Zhang, Z., Xiong, Z., Zou, D.,
Ren, J. S., Guo, C., and Li, C. DiT4SR: Taming Diffusion
Transformer for Real-World Image Super-Resolution. In
ICCV, 2025.
Esser, P., Kulal, S., Blattmann, A., Entezari, R., M ¨uller,
J., Saini, H., Levi, Y ., Lorenz, D., Sauer, A., Boesel, F.,
Podell, D., Dockhorn, T., English, Z., Lacey, K., Good-
win, A., Marek, Y ., and Rombach, R. Scaling Rectified
Flow Transformers for High-Resolution Image Synthesis.
InICML, 2024.
Field, D. J. Relations between the statistics of natural images
and the response properties of cortical cells.J. Opt. Soc.
Am. A, 4(12), 1987.
George Tom, Minesh Mathew, Dimosthenis Karatzas, Ajoy
Mondal, C. V . Jawahar, and Jerod Weinman. ICDAR2024
Challenge on Occluded Roadtext. InICDARW, 2024.
He, K., Gkioxari, G., Doll ´ar, P., and Girshick, R. Mask
R-CNN. InICCV, 2018.
Ho, J., Jain, A., and Abbeel, P. Denoising Diffusion Proba-
bilistic Models. InNeurIPS, 2020.
Hu, E. J., Shen, Y ., Wallis, P., Allen-Zhu, Z., Li, Y ., Wang,
S., Wang, L., and Chen, W. LoRA: Low-Rank Adaptation
of Large Language Models. InICLR, 2021.
Hu, J., Xia, B., Chen, B., Yang, W., and Zhang, L.
GaussianSR: High Fidelity 2D Gaussian Splatting for
Arbitrary-Scale Image Super-Resolution. InAAAI, 2024.
Hu, Q., Fan, L., Luo, Y ., Yu, Y ., Guo, X., and Fan, Q. Text-
Aware Real-World Image Super-Resolution via Diffusion
Model with Joint Segmentation Decoders. InNeurIPS,
2025.
Ke, J., Wang, Q., Wang, Y ., Milanfar, P., and Yang, F.
MUSIQ: Multi-scale Image Quality Transformer. In
ICCV, 2021.
Labs, B. F. Flux. https://github.com/
black-forest-labs/flux, 2024.
Li, C., Liu, W., Guo, R., Yin, X., Jiang, K., Du, Y ., Du, Y .,
Zhu, L., Lai, B., Hu, X., Yu, D., and Ma, Y . PP-OCRv3:
More Attempts for the Improvement of Ultra Lightweight
OCR System.arXiv:2206.03001, 2022.
Li, J., Cao, J., Guo, Y ., Li, W., and Zhang, Y . One Diffusion
Step to Real-World Super-Resolution via Flow Trajectory
Distillation. InICML, 2025a.
Li, Y ., Zhang, K., Liang, J., Cao, J., Liu, C., Gong, R.,
Zhang, Y ., Tang, H., Liu, Y ., Demandolx, D., Ranjan, R.,
Timofte, R., and Van Gool, L. LSDIR: A Large Scale
Dataset for Image Restoration. InCVPRW, 2023.
Li, Y ., Liang, D., Ding, T., and Huang, S.-J. StructSR:
Refuse Spurious Details in Real-World Image Super-
Resolution. InAAAI, 2025b.
Liang, J., Cao, J., Sun, G., Zhang, K., Gool, L. V ., and Tim-
ofte, R. SwinIR: Image Restoration Using Swin Trans-
former. InICCVW, 2021.
Lim, B., Son, S., Kim, H., Nah, S., and Lee, K. M. En-
hanced Deep Residual Networks for Single Image Super-
Resolution. InCVPRW, 2017.
Lin, T.-Y ., Maire, M., Belongie, S., Bourdev, L., Girshick,
R., Hays, J., Perona, P., Ramanan, D., Zitnick, C. L., and
Doll´ar, P. Microsoft COCO: Common Objects in Context.
InECCV, 2015.
10

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Lin, X., He, J., Chen, Z., Lyu, Z., Dai, B., Yu, F., Ouyang,
W., Qiao, Y ., and Dong, C. DiffBIR: Towards Blind
Image Restoration with Generative Diffusion Prior. In
ECCV, 2024.
Lipman, Y ., Chen, R. T. Q., Ben-Hamu, H., Nickel, M., and
Le, M. Flow Matching for Generative Modeling. InICLR,
2023.
Lu, Y ., Wang, Q., Cao, H., Xu, X., and Zhang, M. Smoothed
Preference Optimization via ReNoise Inversion for Align-
ing Diffusion Models with Varied Human Preferences. In
ICML, 2025.
Podell, D., English, Z., Lacey, K., Blattmann, A., Dockhorn,
T., M¨uller, J., Penna, J., and Rombach, R. SDXL: Improv-
ing Latent Diffusion Models for High-Resolution Image
Synthesis. InICLR, 2023.
Qu, Y ., Yuan, K., Hao, J., Zhao, K., Xie, Q., Sun, M., and
Zhou, C. Visual Autoregressive Modeling for Image
Super-Resolution. InICML, 2025.
Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning,
C. D., and Finn, C. Direct Preference Optimization: Your
Language Model is Secretly a Reward Model. InNeurIPS,
2024.
Rahaman, N., Baratin, A., Arpit, D., Draxler, F., Lin, M.,
Hamprecht, F., Bengio, Y ., and Courville, A. On the
Spectral Bias of Neural Networks. InICML, 2019.
Rombach, R., Blattmann, A., Lorenz, D., Esser, P., and
Ommer, B. High-resolution image synthesis with latent
diffusion models. InCVPR, 2022.
Saharia, C., Chan, W., Saxena, S., Li, L., Whang, J., Den-
ton, E., Ghasemipour, S. K. S., Ayan, B. K., Mahdavi,
S. S., Gontijo-Lopes, R., Salimans, T., Ho, J., Fleet, D. J.,
and Norouzi, M. Photorealistic Text-to-Image Diffusion
Models with Deep Language Understanding. InNeurIPS,
2022.
Wan, Z., Zhang, B., Chen, D., and Liao, J. Bringing Old
Films Back to Life. InCVPR, 2022.
Wang, J., Chan, K. C. K., and Loy, C. C. Exploring CLIP
for Assessing the Look and Feel of Images. InAAAI,
2022.
Wang, J., Yue, Z., Zhou, S., Chan, K. C. K., and Loy, C. C.
Exploiting Diffusion Prior for Real-World Image Super-
Resolution. InIJCV, 2024.
Wang, X., Xie, L., Dong, C., and Shan, Y . Real-ESRGAN:
Training Real-World Blind Super-Resolution with Pure
Synthetic Data. InICCVW, 2021.
Wei, P., Xie, Z., Lu, H., Zhan, Z., Ye, Q., Zuo, W., and
Lin, L. Component Divide-and-Conquer for Real-World
Image Super-Resolution. InECCV, 2020.
Wu, R., Yang, T., Sun, L., Zhang, Z., Li, S., and Zhang,
L. SeeSR: Towards Semantics-Aware Real-World Image
Super-Resolution. InCVPR, 2024.
Wu, R., Sun, L., Zhang, Z., Wang, S., Wu, T., Yi, Q., Li, S.,
and Zhang, L. DP2O-SR: Direct Perceptual Preference
Optimization for Real-World Image Super-Resolution. In
NeurIPS, 2025.
Xiao, Y ., Yuan, Q., Jiang, K., Huang, W., Zhang, Q., Zheng,
T., Lin, C.-W., and Zhang, L. Spiking Meets Attention:
Efficient Remote Sensing Image Super-Resolution with
Attention Spiking Neural Networks. InNeurIPS, 2025.
Xie, E., Wang, W., Yu, Z., Anandkumar, A., Alvarez, J. M.,
and Luo, P. SegFormer: Simple and Efficient Design for
Semantic Segmentation with Transformers. InNeurIPS,
2021.
Xu, J., Li, W., Sun, H., Li, F., Wang, Z., Peng, L., Ren, J.,
Yang, H., Hu, X., Pei, R., and Heng, P.-A. Fast Image
Super-Resolution via Consistency Rectified Flow. In
ICCV, 2025.
Yang, S., Wu, T., Shi, S., Lao, S., Gong, Y ., Cao, M., Wang,
J., and Yang, Y . MANIQA: Multi-dimension Attention
Network for No-Reference Image Quality Assessment.
InCVPR, 2022.
Yu, F., Gu, J., Li, Z., Hu, J., Kong, X., Wang, X., He, J.,
Qiao, Y ., and Dong, C. Scaling Up to Excellence: Practic-
ing Model Scaling for Photo-Realistic Image Restoration
In the Wild. InCVPR, 2024.
Zhang, K., Liang, J., Gool, L. V ., and Timofte, R. Designing
a Practical Degradation Model for Deep Blind Image
Super-Resolution. InICCV, 2021.
Zhang, R., Isola, P., Efros, A. A., Shechtman, E., and Wang,
O. The Unreasonable Effectiveness of Deep Features as
a Perceptual Metric. InCVPR, 2018.
Zhou, B., Zhao, H., Puig, X., Fidler, S., Barriuso, A., and
Torralba, A. Scene Parsing through ADE20K Dataset. In
CVPR, 2017.
Zhu, H., Xiao, T., and Honavar, V . G. DSPO: Direct Score
Preference Optimization for Diffusion Model Alignment.
InICLR, 2025.
Zuo, Y ., Zheng, Q., Wu, M., Jiang, X., Li, R., Wang, J.,
Zhang, Y ., Mai, G., Wang, L. V ., Zou, J., Wang, X., Yang,
M.-H., and Tu, Z. 4KAgent: Agentic Any Image to 4K
Super-Resolution. InNeurIPS, 2025.
11

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
A. Derivation of the S-DPO Objective
In this section, we rigorously derive the S-DPO objective. We first establish the velocity-space probabilistic formulation to
recover the standard ℓ2 preference objective, ensuring stability in the continuous-time limit. We then introduce the Sobolev
Spectral Rectification to generalize this into the frequency-aware S-DPO loss, while addressing the theoretical considerations
regarding boundary conditions.
A.1. Continuous-Time Velocity-Space Formulation
To adapt Direct Preference Optimization (DPO) to the continuous Flow Matching framework without succumbing to the
vanishing Signal-to-Noise Ratio (SNR) inherent in discrete SDE approximations, we model the generative process as a
probabilistic policy defined on the tangent bundle (velocity space).
Standard Flow Matching defines the generative process via an ODE: dxt =v(x t, t)dt, targeting the conditional vector field
ut(x|x1) = (x1 −x t)/(1−t) . We define the policy pθ(·|xt) as an isotropic Gaussian distribution over the instantaneous
velocityv∈R d, centered at the model predictionv θ:
pθ(v|xt,c) :=N  v;v θ(xt, t,c), η2I  ,(21)
whereη 2 is a temperature parameter. In this framework, the “optimal action” is the deterministic target velocityu t.
The instantaneous log-likelihood ratio at time t compares the probability of the optimal velocity ut under the policy pθ
versus the referencep ref:
Rt(xt) := log pθ(ut|xt,c) pref(ut|xt,c) ,(22)
Expanding the Gaussian densities, the normalization constants cancel out, leaving the difference of squared Euclidean
norms:
Rt(xt) =

− 1 2η2 ∥ut −v θ∥2 2

−

− 1 2η2 ∥ut −v ref∥2 2

= 1 2η2  ∥vref −u t∥2 2 − ∥vθ −u t∥2 2  , (23)
Let γψ :=v ψ(xt)−u t denote the vector field residual. Since the target ut is deterministic (derived from boundary
conditions), this evaluation is free from stochastic transition noise, ensuring numerical stability as ∆t→0 . Absorbing
constants into the proportionality, we recover theℓ 2-based objective:
log pθ(xt−∆t|xt,c) pref(xt−∆t|xt,c) ∝ Rt(xt)∝ −  ∥γθ∥2 2 − ∥γref∥2 2  ,(24)
A.2. Sobolev Spectral Rectification and S-DPO
To mitigate the frequency-agnostic nature of the ℓ2 norm, we proposeSobolev Spectral Rectification. We generalize the
isotropic assumption by replacing the scalar varianceη 2Iwith a structured spectral covarianceΣ s.
In our framework, the reference policy is parameterized on the Sobolev manifold. We define the likelihood of the reference
policyp ref directly in this space:
pref(v|xt) :=N(v;v ref(xt), η2Σs),(25)
This formulation ensures that the trained policy pθ and the reference pref share the same support and curvature defined by
Σs. Consequently, the regularization in S-DPO penalizes deviations from the reference weights weighted by their spectral
importance, rather than Euclidean distance.
The policy is now modeled as pθ(v) =N(v;v θ, η2Σs). The determinant term det(2πη 2Σs) depends only on fixed
hyperparameters and cancels out in the ratio. The log-likelihood ratio becomes the difference of Mahalanobis distances:
RH s t (xt) =− 1 2η2  ∥γθ∥2 Σ−1 s − ∥γref∥2 Σ−1 s  ,(26)
12

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Recall that Σs =F −1DsF, where Ds(ω) = (1 +∥ω∥ 2 2)−s. The inverse operator is Σ−1 s =F −1D−1 s F. By Plancherel’s
theorem, the quadratic form for any residualγis:
∥γ∥2 Σ−1 s =γ ⊤F −1D−1 s Fγ= (Fγ) HD−1 s (Fγ)
=
X
ω
(1 +∥ω∥ 2 2)s · |ˆγ(ω)| 2 ≡ ∥γ∥2 H s , (27)
Substituting the Sobolev norm equivalence back into the ratio, we define the Sobolev Energy Gap:
∆EH s (xt,c) :=∥γ θ∥2 H s − ∥γref∥2 H s ,(28)
Finally, incorporating the standard DPO logistic loss structure over the preference dataset D (where winners xw should have
higher likelihood than losersx l), we arrive at the S-DPO objective:
LS-DPO(θ) =−E (c,xw 1 ,xl 1)∼D,t∼U(0,T)
h
logσ

β
h
∆EH s (xl t,c)−∆E H s (xw t ,c) ii ,(29)
Note that the sign inversion inside the sigmoid (xl −x w) arises because we minimize the energy (residual) to maximize
likelihood.
B. Proof of Proposition in Adversarial Manifold Guidance
B.1. Proof of Proposition 1: Sobolev Geometry of Hard Negatives
In this section, we provide the rigorous derivation for the optimal hard negative perturbation presented in Proposition 1. As
argued in Section 4.2, the adversary targets the model’sspectral blind spotsby seeking perturbations that minimize the
Euclidean residual energy (mimicking the model’s intrinsic bias) while strictly adhering to a structural trust region defined
by the Sobolev norm.
We seek a perturbation δt that induces structural deviation yet remains indistinguishable to the isotropic baseline. Mathemat-
ically, this corresponds to finding a state within a Sobolev trust region ∥δt∥H s ≤ε t that minimizes the model’s Euclidean
residual energy JL2. This optimization targets the model’s null space, identifying artifacts that improperly minimize the
training objective. The problem is formulated as:
min
δt
JL2 (xw t +δ t)s.t.∥δ t∥H s ≤ε t,(30)
Consider the first-order Taylor expansion of the objective aroundx w t :
JL2 (xw t +δ t)≈ JL2 (xw t ) +⟨∇ xJL2 ,δ t⟩L2 ,(31)
where ∇xJL2 is the standard Euclidean gradient. Since the zero-order term is constant, the problem reduces to minimizing
the linear alignment term⟨∇ xJL2 ,δ t⟩L2 subject to the constraint.
Crucially, the constraint is governed by the Sobolev inner product. Using the spectral operator definition Σs =F −1DsF,
the constraint can be rewritten in terms of theL 2 inner product via the inverse operatorΣ −1 s :
∥δt∥2 H s =⟨δ t,δ t⟩H s =⟨δ t,Σ −1 s δt⟩L2 ≤ε 2 t ,(32)
To solve this constrained optimization, we construct the LagrangianL(δ t, λ)with a Lagrange multiplierλ >0:
L(δt, λ) =⟨∇xJL2 ,δ t⟩L2 + λ 2  ⟨δt,Σ −1 s δt⟩L2 −ε 2 t  ,(33)
Taking the Fr´echet derivative with respect toδ t and setting it to zero:
∂L
∂δ t
=∇ xJL2 +λΣ −1 s δ∗ t = 0,(34)
13

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
SinceΣ −1 s is a symmetric positive-definite operator, it is invertible. We solve for the optimal unnormalized direction:
δ∗ t =− 1 λ Σs∇xJL2 ,(35)
To determine the scalar multiplier λ, we invoke the active constraint condition ∥δ∗ t ∥H s =ε t. Substituting Eq. (35) into the
squared norm:
∥δ∗ t ∥2 H s =⟨δ ∗ t ,Σ −1 s δ∗ t ⟩L2
= 1 λ2 ⟨Σs∇xJL2 ,Σ −1 s Σs∇xJL2 ⟩L2
= 1 λ2 ⟨∇xJL2 ,Σ s∇xJL2 ⟩L2 ,
(36)
Solving for1/λyields the scaling factorε t/∥Σs∇xJL2 ∥H s. Substituting this back gives the closed-form solution:
δ∗ t =−ε t Σs∇xJL2 p ⟨∇xJL2 ,Σ s∇xJL2 ⟩L2 ,(37)
Geometric Interpretation and the Role of Preconditioning.This result formally elucidates the role of Σs as a spectral
preconditioner. The term Σs∇xJL2 corresponds to theNatural Gradienton the Sobolev manifold. Mathematically, the
Euclidean gradient ∇xJL2 resides in the dual space and often contains high-frequency stochastic noise. By the Riesz
Representation Theorem, Σs acts as the canonical isomorphism mapping this irregular dual vector back to the primal space
H s.
Crucially, this preconditioning does not merely ”smooth” the image in a naive sense; rather, it enforcesspectral regularity.
Even if the raw gradient points towards unstructured noise (a common property of neural network gradients), the operator
Σs filters these incoherent components. This ensures that the resulting perturbation δ∗ t manifests asstructurally consistent
degradations—such as recurring artifacts or texture distortions—rather than imperceptible noise. This justifies the use
of our parametric adversary Aϕ (Proposition 2), which learns to approximate these coherent failure patterns to effectively
penalize model hallucinations.
B.2. Proof of Proposition 2: Theoretical Consistency of the Parametric Adversary
In this section, we provide the rigorous proof for Proposition 2, demonstrating that a parametric adversary Aϕ trained to
minimize the expected residual energy under a Sobolev constraint implicitly recovers the optimal Sobolev descent direction
derived in Proposition 1.
Optimization in Velocity Space.In our Flow Matching formulation, the adversary Aϕ is parameterized as a correction to
thevelocity field vθ. While Proposition 1 characterizes the optimal descent direction δt in the state space, the parametric
realization requires translating this geometric guidance into the velocity domain. To ensure numerical stability across the
entire time horizon t∈[0,1] and avoid singularities associated with time-dependent Jacobians near the boundaries, we
impose the Sobolev trust region directly on the velocity potential. Consequently, the optimization problem is formalized as:
min
ϕ
Ext [J(x t + ∆x(Aϕ))]s.t.∥A ϕ(xt)∥H s ≤ε,(38)
where∆x(A ϕ)denotes the state deviation induced by the velocity perturbationA ϕ over a discretization step∆t.
Linearization via Euler Integration.Consider the first-order Taylor expansion of the energy function for a small step ∆t:
J(x t + ∆x)≈ J(xt) +⟨∇ xJ,∆x⟩ L2 ,(39)
Under the standard Euler integration scheme, the velocity perturbation Aϕ induces a linear state update ∆x≈ Aϕ ·∆t .
Substituting this relationship into the expansion, and noting that J(x t) is independent of ϕ, the objective reduces to
minimizing the inner product:
min
ϕ
Ext [⟨∇xJ,A ϕ ·∆t⟩ L2 ]s.t.∥A ϕ∥H s ≤ε,(40)
14

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Assuming sufficient representational capacity (i.e., Aϕ acts as a universal approximator), minimizing the expected loss is
equivalent to minimizing the objective pointwise for each xt. Absorbing the scalar ∆t into the effective step size, we solve
the following constrained variational problem for a fixed state:
Aϕ∗ = arg min
v∈H s
⟨∇xJ,v⟩ L2 s.t.∥v∥ H s ≤ε,(41)
Solution via Spectral Duality.To solve this, we leverage the duality between the L2 and H s spaces. Using the definition of
the Sobolev inner product⟨u,v⟩ L2 =⟨Σ su,v⟩ H s, we rewrite the objective functional:
⟨∇xJ,v⟩ L2 =⟨Σ s∇xJ,v⟩ H s ,(42)
The term ∇H s x J :=Σ s∇xJ can be interpreted as thenatural Sobolev gradient. The optimization is now formulated
entirely within the geometry of the Hilbert spaceH s:
min
v
⟨∇H s x J,v⟩ H s s.t.∥v∥ H s ≤ε,(43)
By the Cauchy-Schwarz inequality in Hilbert spaces, the inner product is minimized when v is strictlyanti-parallelto the
gradient direction and lies on the boundary of the feasible set. Therefore, the optimal solution is:
Aϕ∗ =−ε Σs∇xJ ∥Σs∇xJ ∥H s ,(44)
Equivalence to Proposition 1.Finally, we verify that this velocity-based solution matches the state perturbation derived in
Proposition 1. We expand the Sobolev norm in the denominator:
∥Σs∇xJ ∥2 H s =⟨Σ s∇xJ,Σ s∇xJ ⟩H s
=⟨Σ s∇xJ,Σ −1 s (Σs∇xJ)⟩ L2 (viaΣ −1 s )
=⟨Σ s∇xJ,∇ xJ ⟩L2
=⟨∇ xJ,Σ s∇xJ ⟩L2 (symmetry ofΣ s),
(45)
Substituting this norm back into Eq. (44) yields:
Aϕ∗ =−ε Σs∇xJp ⟨∇xJ,Σ s∇xJ ⟩L2 ,(46)
This expression is identical to Eq. (19) in Proposition 1. This confirms that minimizing the energy loss with a bounded
velocity network implicitly learns the optimal Sobolev-preconditioned descent direction.
B.3. Empirical Examination of the Capacity Assumption
Prop. 4.2 characterizes the Sobolev-optimal perturbation in function space, while the sufficient-capacity assumption is only
used to connect this functional optimum to its neural parameterization. To examine whether this assumption is reasonable in
practice, we vary the capacity of the adversary by changing the LoRA size and report the resulting performance in Tab. 4.
The results show that increasing adversary capacity from very small adapters yields clear gains, while performance largely
saturates once the adapter becomes moderately expressive. This behavior is consistent with Prop. 4.2: the adversary does not
require arbitrarily large capacity, but only sufficient expressiveness to realize or closely approximate the Sobolev-optimal
direction.
C. More Experiments
C.1. More Implementation Details
Supplementing the experimental configurations outlined in the main text, we provide further engineering specifics to
facilitate reproducibility. To optimize training throughput and memory efficiency, we employBF16mixed-precision training
15

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Table 4.Effect of adversary capacity under different LoRA sizes. Performance improves with capacity in the small-adapter regime and
largely saturates beyond moderate sizes.
Adversary Capacity Params. PSNR↑SSIM↑MANIQA↑CLIPIQA+↑
(4,4) ∼7.4M 19.43 0.6026 0.6328 0.7349
(8,8) ∼14.8M 20.54 0.6158 0.6487 0.7498
(16,16) ∼29.5M 20.60 0.6171 0.6519 0.7521
(32,32) ∼59.0M20.610.6170 0.6517 0.7524
(64,64) ∼118.0M 20.58 0.6167 0.65150.7525
with gradient checkpointing enabled on the FLUX.1-dev backbone. For the inference stage, we adopt a 28-step sampling
schedule to balance generation quality and latency.
A component of our training infrastructure is the management of the reference policy required by the DPO objective. To
instantiate the reference model pref without duplicating the massive parameters of FLUX.1-dev, we adopt a Dual-LoRA
strategy. Specifically, we maintain the pre-trained SFT weights as a frozen LoRA adapter (MSFT) to define the reference
distribution. Simultaneously, we introduce a separate, zero-initialized LoRA adapter (MDPO) to parameterize the policy
update. Thus, the learning process starts explicitly from the SFT baseline, ensuring optimization stability. The final inference
weights are the algebraic sum of the base parameters and both adapters.
To better accommodate the non-periodic nature of natural images, we implement the spectral operator F using the Discrete
Cosine Transform (DCT-II). By implicitly enforcing Neumann boundary conditions via symmetric reflection, the DCT basis
avoids potential boundary discontinuities associated with the periodic assumption of the DFT. This ensures better continuity
at the image boundaries and maintains the regularity consistent with the Sobolev norm∥ · ∥H s.
Optimization is conducted with an effective global batch size of 512, achieved via a per-device batch size of 8 and 8 gradient
accumulation steps across the GPU cluster. We utilize a linear warmup of 200 steps to stabilize early training dynamics,
and the DPO KL penalty coefficient β is set to 2000. Finally, regarding data processing, all input images are normalized to
[−1,1] , and we use empty text prompts during training to force the model to rely exclusively on image-conditional cues for
restoration.
Table 5.Performance Analysis on NVIDIA A800. We evaluate the memory efficiency, latency, and Model Flops Utilization (MFU) of the
FLUX.1 DEV model during the super-resolution task. The metrics are averaged over 100 inference runs excluding warm-up.
Metric Value Unit Description
Avg. Latency 19.60 s/img Inference time per image
Peak VRAM 33.02 GB Max memory usage (96.2% Eff.)
Total Compute 2.85 PFLOPs Total floating-point ops per img
MFU 46.6 % Model Flops Utilization (Est.)
Furthermore, we also conduct performance experiments. Tab. 5 presents the quantitative analysis of the inference efficiency.
Our implementation achieves a high Model Flops Utilization (MFU) of 46.6%, indicating effective hardware saturation on
the A800 GPU. The peak VRAM usage reaches 33.02 GB with a 96.2% memory efficiency, demonstrating that our system
maximizes the available memory bandwidth. With an average latency of 19.60 seconds per image, the system maintains a
practical throughput for high-resolution generation tasks.
C.2. More Quantitative Experiments
To further examine the generality of our method across different generative backbones, we conduct additional experiments
using SD1.5 and SDXL, as shown in Tab. 6. The consistent improvements over the corresponding SFT baselines indicate
that the effectiveness of our method is not specific to the FLUX backbone.
In addition, to evaluate the out-of-distribution generalization ability of our method, we further test on two more challenging
real-world datasets: RealLQ250 and Bringing Old Films Back to Life. As shown in Tab. 7 and Tab. 8, our method achieves
competitive or superior performance across multiple non-reference image quality metrics, demonstrating its robustness on
diverse real-world degradations beyond the training distribution.
16

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Table 6.Quantitative comparison of different backbones and methods.
Backbone Methods PSNR↑SSIM↑MANIQA↑CLIPIQA+↑
SD1.5 SFT 18.52 0.4873 0.4236 0.6142
SD1.5 +SSR+AMG19.14 0.5207 0.4891 0.6658
SDXL SFT 19.31 0.5284 0.5473 0.6824
SDXL +SSR+AMG19.92 0.5681 0.6104 0.7289
FLUX SFT 19.96 0.5642 0.6012 0.7058
FLUX (ours) +SSR+AMG 20.60 0.6171 0.6519 0.7521
Table 7.Quantitative comparison on RealLQ250. We compare ASASR with representative real-world image super-resolution methods
using non-reference image quality assessment metrics.
Methods NIQE↓MANIQA↑MUSIQ↑CLIPIQA+↑
DP2O-SR 4.02 0.4494 69.87 0.7042
SeeSR 4.41 0.4992 70.57 0.7104
DreamClear3.550.4351 66.76 0.7116
DiT4SR 4.35 0.4094 63.45 0.6829
ASASR 3.64 0.5168 71.16 0.7202
C.3. User Study
To conduct a holistic evaluation of restoration quality, we organized a user study involving 50 participants to assess perceptual
realism and semantic fidelity. We randomly sampled 64 low-quality images from the test sets, processing them with ASASR
and six competitive baselines (DiT4SR, DP2OSR, SUPIR, SeeSR, StableSR, RealESRGAN) to generate comparative
groups. For each of the 64 test images, participants were presented with the low-quality reference and asked to rank the
restored images within each group based on visual naturalness, detail precision, and the absence of artifacts. To ensure
fairness, the method labels were anonymized, and the initial display order was randomized.
To quantitatively analyze the subjective feedback, we adopted two metrics: V ote Percentage (Top-1 Ratio) and Top-K Ratio.
The former measures the frequency with which a method is ranked first. For the latter, we calculate the frequency that a
methodiappears within the top-krankings. The Top-K ratioR k i is formally defined as:
Rk i = 1 N
NX
j=1
⊮(rankij ≤k),(47)
where N denotes the total number of evaluation groups, rankij represents the ranking of method i in the j-th group (where 1
indicates the best), and⊮(·)is the indicator function.
As illustrated in Fig. 8, ASASR outperforms all baselines by a substantial margin. In the Top-1 Ratio analysis (Fig. 8(a)), our
method secured 91.1% of the first-place votes, indicating an overwhelming user preference. Furthermore, the Top-K Ratio
results (Fig. 8(b)) demonstrate that ASASR is consistently ranked among the top choices across all k levels, highlighting the
stability and reliability of our geometry-aware restoration framework.
C.4. More Super-Resolution Experimental Results
To provide a more comprehensive evaluation of the experimental performance of ASASR, we present additional visual
comparisons in this section. These include qualitative results on Synthesis Datasets (Fig.9) and Real-World Datasets
(Fig. 10). Furthermore, we provide visualization results for downstream high-level vision tasks, specifically illustrating
OCR performance on the RoadText1K dataset (Fig. 11), object detection and instance segmentation on the COCO dataset
(Fig. 12), and semantic segmentation on the ADE dataset (Fig. 13).
17

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
Table 8.Quantitative comparison on Bringing Old Films Back to Life. We evaluate ASASR against representative restoration and
super-resolution methods on degraded old film frames using non-reference image quality assessment metrics.
Methods NIQE↓MANIQA↑MUSIQ↑CLIPIQA+↑
DP2O-SR 5.42 0.2621 32.32 0.5195
SeeSR 5.88 0.1159 36.70 0.2819
DreamClear 4.97 0.3842 45.58 0.4271
DiT4SR 4.51 0.4694 52.67 0.5004
ASASR 4.46 0.5036 54.42 0.6078
(a)Top-1 Ratio (b) Top-K Ratio
Figure 8.Visualization of user study results. (a)Top-1 selection ratio, where ASASR secures a dominant 91.1% of user votes.(b)
Top-K cumulative rankings, demonstrating that our method is consistently favored as the highest-quality restoration among competing
baselines across all K levels.
18

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
LQ GT BSRGAN
SeeSRFaithDiff
SwinIR-GAN
DP2O-SRSUPSR
DiffBIR
ASASRDiT4SR
StableSRReal-ESRGAN
LQ GT BSRGAN
SeeSRFaithDiff
SwinIR-GAN
DP2O-SRSUPSR
DiffBIR
ASASRDiT4SR
StableSRReal-ESRGAN
LQ GT BSRGAN
SeeSRFaithDiff
SwinIR-GAN
DP2O-SRSUPSR
DiffBIR
ASASRDiT4SR
StableSRReal-ESRGAN
Figure 9.Visual comparisons on synthesis datasets.We compare ASASR against state-of-the-art GAN-based and diffusion-based
methods. As observed, our method achieves superior structural fidelity, effectively reconstructing complex architectural geometries
(1st row) and legible text (3rd row) while maintaining natural textures (2nd row), avoiding the structural distortions and hallucinations
common in competing generative priors.
19

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
LQ BSRGAN
SeeSRFaithDiff
SwinIR-GAN
DP2O-SRSUPSR
DiffBIR
ASASRDiT4SR
StableSRReal-ESRGAN
LQ BSRGAN
SeeSRFaithDiff
SwinIR-GAN
DP2O-SRSUPSR
DiffBIR
ASASRDiT4SR
StableSRReal-ESRGAN
LQ BSRGAN
SeeSRFaithDiff
SwinIR-GAN
DP2O-SRSUPSR
DiffBIR
ASASRDiT4SR
StableSRReal-ESRGAN
Figure 10.Visual comparisons on real-world datasets.ASASR demonstrates robust generalization capabilities on challenging real-world
scenes. Unlike baselines that often produce over-smoothed textures (e.g., SwinIR) or hallucinated artifacts (e.g., StableSR), our method
successfully restores intricate high-frequency details, such as feather textures (1st & 3rd rows) and distant architectural features (2nd row),
striking an optimal balance between noise suppression and perceptual photorealism.
20

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
Figure 11.Visualization of OCR results on the RoadText1K dataset.To evaluate semantic preservation, we apply a pre-trained text
detector on images restored by different methods. ASASR reconstructs clearer, sharper text characters compared to other generative
models, enabling more accurate text detection (red bounding boxes) that closely aligns with the Ground Truth, whereas competing
methods often lead to missed detections or false positives due to character corruption.
21

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
Figure 12.Visualization of object detection and instance segmentation on the COCO dataset.We visualize the detection bounding
boxes and segmentation masks predicted on restored images. ASASR preserves the structural integrity of objects, such as human limbs
(1st & 2nd rows) and animal boundaries (3rd row), resulting in more precise segmentation masks and higher confidence scores compared
to baselines that suffer from semantic drift or boundary blurring.
22

Coloring the Noise: Adversarial Sobolev Alignment for Faithful Image Super Resolution
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
GT BSRGAN Real-ESRGAN SwinIR-GAN StableSR DiffBIR
FaithDiff SeeSR SUPSR DP2O-SR DiT4SR ASASR
Figure 13.Visualization of semantic segmentation on the ADE20K dataset.The results illustrate the impact of restoration quality on
scene parsing. ASASR effectively recovers distinct object boundaries and consistent semantic regions (e.g., the car in the 2nd row and
furniture in the 3rd row), leading to cleaner segmentation maps with fewer artifacts compared to other diffusion-based counterparts, which
often introduce noise that confuses the segmentation model.
23
