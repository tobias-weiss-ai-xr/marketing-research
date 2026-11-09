---
title: 'KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Demographically Fair Text-to-Image Generation'
url: https://arxiv.org/abs/2606.01282
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Farbod Davoodi
- Seyed Reza Tavakoli Shiyadeh
- Pooria Safaei
- Sana Harighi
- Parsa Gholami
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.01282
pages: 19
chars: 67425
fetched_at: '2026-11-08T13:06:11+00:00'
kb_version: 1
---

# KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Demographically Fair Text-to-Image Generation

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for
Demographically Fair Text-to-Image Generation
‘
Farbod Davoodi * 1 Seyed Reza Tavakoli Shiyadeh* 1 Pooria Safaei 1 Sana Harighi 2 Parsa Gholami 3
Amirali Amini 3 Kimia Vanaei1 Emad Firoozi 4 Parham Abed Azad 3 Babak Khalaj 4 Siavash Ahmadi 5
Amir Hossein Payberah 6 Mohammad Hossein Rohban 3 Soheil Kolouri 7 Ali Diba 1
Abstract
Text-to-Image (TTI) systems are now everyday
infrastructure for journalism, education, adver-
tising, and public communication, and the de-
mographic and cultural stereotypes they inherit
from training data—rendering women, people of
colour, older adults, and non-Western cultures
as under-represented or caricatured—become a
population-level harm at deployment scale. Ex-
isting mitigations either require costly retrain-
ing, infeasible for the closed-source backbones
that dominate consumer products, or rely on
fixed demographic templates that ignore cultural
context.ixed demographic templates that ignore
cultural context. We presentKG-FairDiff, a
model-agnostic, inference-time framework that
formalises fairness-aware prompt refinement as
a constrained optimisation problem and opera-
tionalises it as a closed-loop pipeline: a knowl-
edge graph of ∼1,200 culture- and bias-related
triples retrieves structured context, an LLM
rewriter proposes refinements, and a validator
accepts only prompts that reduce a divergence-
based fairness loss while preserving semantic fi-
delity to the user’s original intent. We prove a
*Equal contribution 1Qatar Computing Research Institute,
Hamad Bin Khalifa University, Doha, Qatar 2Department of Elec-
tronics, Information and Bioengineering, Politecnico di Milano,
Milan, Italy 3Department of Computer Engineering, Sharif Univer-
sity of Technology, Tehran, Iran4Department of Electrical Engi-
neering, Sharif University of Technology, Tehran, Iran5Electronics
Research Institute, Sharif University of Technology, Tehran, Iran
6Department of Computing and Learning Systems (CLS) at KTH
Royal Institute of Technology 7Department of Computer Science,
College of Connected Computing, Vanderbilt University Depart-
ment of Electrical and Computer Engineering, Vanderbilt Uni-
versity. Correspondence to: Ali Diba <adiba@hbku.edu.qa>,
Siavash Ahmadi<s.ahmadi@sharif.edu>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
finite-termination bound for the refinement loop,
contribute a mathematically consistent evaluation
suite linking Bias-P/Bias-W to divergence from
target distributions and ENS to KL divergence,
and audit eight widely-deployed backbone gener-
ators. KG-FairDiff substantially reduces gender,
race, age, and intersectional disparities while pre-
serving prompt semantics, offering a practical,
deployment-ready route to more equitable genera-
tive AI.
1. Introduction
Text-to-Image (TTI) systems have moved from re-
search demonstrations to everyday visual-production
infrastructure—illustrating news articles, generating stock
imagery, accompanying classroom materials, and answer-
ing “show me a. . . ” queries for a global audience (Miao
et al., 2024; Shin & Jang, 2024; Anonymous, 2024). As
deployment scales, so does the social weight of these sys-
tems’ default behaviours, and a growing body of audits
shows that those defaults are systematically skewed (Luc-
cioni et al., 2023; Vice et al., 2025; Wan & et al., 2024):
CEOs are rendered as White men, scientists as young East
Asian men, nurses as women, and many cultural traditions
are erased or caricatured in favour of Western-centric vi-
sual priors (Karkkainen & Joo, 2021; Wang & et al., 2023).
The harm is not the failure of any single image but the
population-scalerepetition of narrow representations across
large numbers of generations.
Mitigating this harm sits at the intersection of trustworthy AI
and AI for social good: it requires auditing what deployed
models produce, intervening under realistic deployment con-
straints, and demonstrating measurable benefit without new
failure modes. Existing approaches fall short on at least one
of these axes. Dataset rebalancing and latent-space regulari-
sation (Kim et al., 2025; Li et al., 2024; Esposito et al., 2023)
require access to training data or model internals, which
is infeasible for closed-source generators. Lighter-weight
prompt-level methods such as MinorityPrompt (Um & Ye,
1
arXiv:2606.01282v1  [cs.CV]  31 May 2026

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
2024) and PreciseDebias (Clemmer et al., 2024) typically
rely on fixed demographic templates and ignore structured
cultural knowledge, leaving images culturally tokenistic
rather than specific. Cultural benchmarks (Shi & et al.,
2024; Liu et al., 2025) document this gap but do not provide
a closed-loop intervention, and related work on retrieval-
grounded prompt optimisation (Cui et al., 2025; Su et al.,
2024) has not yet been brought to bear on fairness-aware
TTI generation.
We proposeKG-FairDiff, a knowledge-graph-guided
prompt refinement framework designed for realistic TTI
deployment. It runs entirely at inference time and treats the
generator as a black box, so it applies to both proprietary
and open-weight backbones. A triple-embedded knowledge
graph of ∼1,200 culture- and bias-related triples retrieves
structured context for a prompt; an LLM rewriter proposes
refinements; and a closed-loop validator accepts only those
that reduce a divergence-based fairness loss while keeping
cosine similarity to the user’s original prompt above a fi-
delity threshold. The combination of structured cultural
grounding and an explicit acceptance rule improves rep-
resentation without inducing semantic drift or superficial
demographic insertion. The paper contributions are as fol-
lows: a fidelity threshold. The combination of structured
cultural grounding and an explicit acceptance rule improves
representation without inducing semantic drift or superfi-
cial demographic insertion. The paper contributions are as
follows:
1. Formulation and algorithm.We formalise fairness-
aware prompt refinement as a constrained optimisation
problem with explicit fairness, semantic-fidelity, and
style-preservation terms, and give an iterative refine-
ment algorithm with a finite termination bound under
a monotone-improvement assumption on the validator.
2. A reusable knowledge graph for fairness-aware
prompting.We construct and release a hand-curated
KG of ∼1,200 triples spanning stereotype, counter-
stereotype, and cultural grounding relations, sourced
from the McGillNLP Bias Dataset and CultureBank
and double-annotated for factual accuracy and cultural
sensitivity.
3. An evaluation suite with theoretical grounding.We
provide a mathematically consistent evaluation frame-
work that links Bias-P/Bias-W to divergence from tar-
get distributions, relates ENS to KL divergence, and
uses Wasserstein / Gromov–Wasserstein alignment to-
gether with CLIP directional similarity to assess se-
mantic preservation supporting the evidence standards
needed to credibly claim social benefit.
4. An audit of eight deployed generators against three
prompt-level baselines.On a 100-prompt benchmark
spanning 50 occupations from the U.S. BLS taxon-
omy, KG-FairDiff improves fairness across gender,
race, age, and intersectional axes on eight backbones
(GPT-Image-1, Qwen-VL-2512, SD 3.5 Large, Zim-
age, SD Lightning, Gemini 3 Pro, Gemini 2.5 Flash,
GPT-5-image) and outperforms MinorityPrompt, Pre-
ciseDebias, and FairImagen e.g., up to20× larger Bias-
W reductions and 13× larger ENS gains over Minori-
tyPrompt.
5. Isolation of the KG component and honest failure
analysis.An ablation across (embedding model, LLM
rewriter) pairs shows that KG retrieval contributes inde-
pendently of the rewriter, and we transparently report
regressions on SD 3.5 Large and Gemini 3 Pro, at-
tributing them to safety-filter interactions and conflict
between intersectional cultural cues.
2. Related Work
Systematic stereotyping in TTI is characterised by Masrouri
et al. (Masrourisaadat et al., 2024), Miao et al. (Miao et al.,
2024), and Gallegos et al. (Gallegos & et al., 2024). Wan
et al. (Wan & et al., 2024) present a survey classifying bias
sources. Vice et al. (Vice et al., 2025) audit over 100 TTI
models. Wang et al. (Wang & et al., 2023) propose T2IAT
for bias measurement. D’Inc `a et al. (D’Inc `a et al., 2024)
introduce OpenBias. Lee et al. (Lee et al., 2024) propose
HEIM, a holistic benchmark. Weng et al. (Weng et al., 2025)
analyse TTI bias from a causal mediation perspective. Pre-
rak (Prerak, 2024) surveys bias mitigation methods across
multiple model families.
TTI-specific intervention strategiesinclude adversarial
fine-tuning (Esposito et al., 2023), data filtering (Kim et al.,
2025), fairness-aware conditioning (Li et al., 2024), and
self-contrastive fine-tuning (Liu et al., 2024). Friedrich et
al. (Friedrich et al., 2025) propose Fair Diffusion. Bonna
et al. (Bonna et al., 2025) introduce DebiasPI. Sahili
et al. (Sahili et al., 2025) propose FairCoT, which uses
chain-of-thought reasoning to improve fairness. Zhang et
al. (Zhang et al., 2023) present ITI-GEN. Dai et al. (Dai
et al., 2024) provide large-scale multimodal face datasets
relevant to demographic fairness evaluation.
Cultural groundingis recognised as a distinct fairness
axis in TTI, separate from the broader LLM bias litera-
ture (Bang et al., 2024; Gallegos & et al., 2024; Lin et al.,
2024; Fan et al., 2025). CultureVLM (Liu et al., 2025),
Culture-TRIP (Jeong et al., 2025), CultureBank (Shi & et al.,
2024), CDEval (Wang & et al., 2024), CIVICS (Pistilli et al.,
2024), and Naous et al. (Naous & et al., 2024) provide rel-
evant benchmarks and analyses. Vasilev et al. (Vasilev &
et al., 2024) demonstrate culture-specific T2I dataset adap-
tation.
2

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
3. Method
KG-FairDiff places fairness intervention entirely at the
prompt level, leaving the underlying generator untouched
and therefore deployable on any black-box TTI backbone.
The pipeline (Figure 1) has three stages: (i) we build a
knowledge graph encoding both stereotypical associations
to be countered and culturally grounded concepts to be pre-
served; (ii) at inference time, a prompt is iteratively rewrit-
ten under guidance from KG-retrieved triples and accepted
only if a closed-loop validator confirms both a fairness im-
provement and sufficient semantic fidelity to the original;
(iii) the accepted prompt is then passed to the unmodified
generator. The remainder of this section formalises the
resulting constrained optimization problem, specifies the
knowledge graph and rewrite–validate loop, and proves a
finite-termination bound for the refinement procedure.
3.1. Problem Formulation
Let p∈ P be a text prompt and let a TTI model induce
x∼G(· |p) , where G denotes a single backbone gen-
erator from the set G of all backbone generators. Let
hG :X → AG be an attribute classifier with nG =|A G|
categories. The prompt-induced attribute distribution is
πp(a) =P x∼G(·|p)[hG(x) =a] , and P denotes the space
of all valid text prompts withp 0 ∈ Pthe initial (unrefined)
prompt.
Fairness loss.For neutral prompts we use a uniform target
uG(a) = 1/nG:
Lfair(p;G) =D(π p∥uG(·)), (1)
whereD(·∥·)denotes KL divergence.
Semantic fidelity.Let e(·) be a text embedding function.
Given an initial promptp 0 ∈ P, we require:
sim(p, p0) = ⟨e(p), e(p0)⟩ ∥e(p)∥2∥e(p0)∥2 ≥τ. (2)
Constrained optimisation.Let G denote the set of back-
bone generators, wG ≥0 their associated weights, and
Lstyle(p) a style-preservation regulariser. Given p0, we
seek:
p∗ ∈arg min
p∈P
X
G∈G
wG Lfair(p;G) +λL style(p)
s.t.sim(p, p 0)≥τ.
(3)
where Lstyle(p) penalises stylistic drift (e.g., over-
specification of demographics), and λ≥0 is a trade-off
weight.
Handling demographic-restricted prompts.When the
initial prompt p0 already contains explicit demographic at-
tributes (e.g., “a female nurse”), our framework treats those
attributes as hard constraints and restricts the search space
P accordingly: the rewriter is instructed to preserve all
explicit demographic mentions while introducing diversity
only along the remaining, unconstrained attribute axes. This
prevents the framework from overriding user-specified de-
mographics. The example in Fig. 1 involves an attribute-
neutral prompt (no gender or age specified), and the intro-
duction of “male” and “middle-aged” in the refined prompt
represents one possible diverse completion rather than a pre-
scribed demographic; we acknowledge this as a limitation
and discuss it further in Section 4.3.
3.2. Knowledge Graph and Retrieval
We represent domain knowledge as a directed labelled multi-
graph K= (V,R,E) . Triples encode stereotypical associa-
tions (to be countered) and culturally grounded concepts (to
be preserved).
KG Construction.The KG comprises approximately 1,200
hand-curated triples spanning three categories: (i)stereo-
type triplesdrawn from the McGillNLP Bias Dataset (Gal-
legos & et al., 2024), encoding known occupational and
demographic stereotypes; (ii)counter-stereotype triples
asserting the inverse associations, manually authored to
directly negate each stereotype triple; and (iii)cultural
grounding triplessourced from CultureBank (Shi & et al.,
2024), encoding non-Western cultural concepts, attire, and
practices. Triples follow the schema g non-Western cul-
tural concepts, attire, and practices. Triples follow the
schema (subject, relation, object) with rela-
tion types stereotyped as, counter stereotype,
and associated culture. Each triple was reviewed
by at least two annotators for factual accuracy and cultural
sensitivity. Retrieval returns top-k triples by cosine similar-
ity:Retrieve k(p) = TopKt∈E cos(vp, vt).
3.3. Prompt Rewrite and Closed-Loop Validation
Given retrieved triples T= Retrieve k(p), a rewrite op-
erator produces p′ = Ψ(p, T). A validator assigns score
S(p)∈[0,1] reflecting bias intensity, representational inclu-
sivity, and cultural appropriateness. A prompt is accepted
if S(p)≥γ and sim(p, p0)≥τ . Algorithm 1 gives the full
procedure.
We acknowledge a potential circularity: using GPT-4o both
as the rewriter Ψ and the validator S means the model eval-
uates its own outputs. In practice, the rewrite and validation
calls use distinct system prompts with complementary ob-
jectives (generation vs. critique), and the downstream quan-
titative fairness metrics (Bias-W, KL, ENS) provide external
validation. Nevertheless, we recognise this as a limitation
3

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Figure 1.KG-FairDiff pipeline.Stage 1: knowledge graph construction. Stage 2: iterative prompt optimisation. Stage 3: fairness-
constrained TTI generation.
Algorithm 1 Iterative Prompt Refinement
Input:Promptp 0, KGK, thresholdsγ, τ, max itersT max
Output:Refined promptp ∗
1p (0) ←p 0 fort= 0, . . . , Tmax −1do
2T (t) ←Retrieve k(p(t)) ˜p(t) ←Ψ(p (t), T(t)) if
S(˜p(t))≥γandsim(˜p (t), p0)≥τthen
3return˜p (t)
4p (t+1) ←˜p(t)
5returnp (Tmax)
and discuss alternatives such as using a held-out LLM or
human evaluation in Section 4.3.
3.4. Theoretical Analysis
Under a monotone-improvement assumption on the valida-
tor, the loop terminates in at most T≤ ⌈(γ−S(p (0)))/ϵ⌉
iterations. Minimising KL divergence to uniform is equiva-
lent to maximising Shannon entropy and ENS. By convexity
of the ℓ2 norm, dataset-level bias (Bias-W) cannot exceed
average per-prompt bias (Bias-P). Formal proofs are pro-
vided in the Appendix.
3.5. Stopping Criteria
We derive a worst-case termination guarantee under a suffi-
cient condition on the validator. Assume the validator score
increases by at least ϵ >0 whenever it is below threshold—
a condition that holds if the LLM rewriter makes measurable
progress on each iteration:
S(p(t+1))≥min n S(p(t)) +ϵ,1 o wheneverS(p (t))< γ.
(4)
Under this assumption the loop terminates in at most
T≤
 γ−S(p (0))
ϵ

(5)
iterations or atT max.
Remark.The monotone-improvement assumption is suf-
ficient but not necessary: the algorithm still terminates at
Tmax without it. The S need not be monotone in practice
(race KL spikes at Iteration 3), confirming that the bound
is conservative rather than tight. Empirical correlation be-
tween S(p) and downstream fairness metrics (Bias-W, KL,
ENS) across prompts and iterations is left for future work;
establishing this connection rigorously would strengthen the
theoretical grounding of the validator as a proxy forL fair.
4

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Figure 2.Qualitative comparison for Prompt Comparison. Left: an image generated with the generic prompt. Right: an image generated
with the enhanced prompt.
4. Experiments
4.1. Setup
Models and data.We construct a benchmark of 100
occupation-focused prompts covering 50 distinct profes-
sions drawn from the U.S. Bureau of Labor Statistics occu-
pational taxonomy, selected to span a wide range of gender-
and race-stereotyped roles (e.g., CEO, nurse, engineer, do-
mestic worker). For each profession, two prompt variants
are generated: a minimal variant (“Generate an image of a
[profession]”) and a context-rich variant (“Generate a close-
up image of a group of [professions] who are smiling at
my camera full face”). We produce 10 images per prompt
per condition with Stable Diffusion v1.5, SD v3-lightning,
GPT-image-1, and four other generators.
Knowledge graph.The KG comprises approximately
1,200 hand-curated triples spanning stereotype, counter-
stereotype, and cultural grounding triples drawn from Cul-
tureBank (Shi & et al., 2024) and the McGillNLP Bias
Dataset.
Retrieval and rewriter.We retrieve k= 5 nearest triples
using text-embedding-3-small. The LLM rewriter and val-
idator are GPT-4o with γ= 0.75 , τ= 0.80 , and Tmax = 5.
Threshold justification.The acceptance thresholds γ=
0.75 and τ= 0.80 were selected via a grid search on a
held-out development set of 20 prompts (not included in the
main evaluation). We swept γ∈ {0.60,0.70,0.75,0.80}
and τ∈ {0.70,0.75,0.80,0.85} and selected the combina-
tion that maximised the average improvement in Bias-W
while keeping the semantic fidelity loss (measured by∆W 2 2 )
below 0.005.
Attribute measurement.Demographic attributes are es-
timated using FairFace (Karkkainen & Joo, 2021). We
report Bias-P, Bias-W (Jiang et al., 2024), ENS, DKL, and
ICAD (Li et al., 2024).
4.2. Comparison with Prompt-Level Baselines
KG-FairDiff substantially outperforms Minori-
tyPrompt (Um & Ye, 2024) and PreciseDebias (Clemmer
et al., 2024). For MinorityPrompt, our method achieves
Bias-W reductions up to 20× larger (e.g., −0.1396 vs.
−0.0037 for Race) and ENS gains up to 13× larger.
Detailed comparison tables are provided in the Appendix.
MinorityPrompt (Um & Ye, 2024).optimises prompts to
sample low-density regions of the text-conditional distribu-
tion in T2I diffusion models. We regenerate images using
Stable Diffusion following their experimental protocol. As
Table 1 shows, Minority yields only marginal improvements:
Bias-W forRacedecreases by just −0.0037 andGender
bias slightly increases (+0.0028). ENS and KL reductions
are similarly limited. Table 1 quantifies the gap: our method
achieves Bias-W reductions up to 20× larger (e.g. −0.1396
vs. −0.0037 for Race) and ENS gains up to 13× larger (e.g.
+8.79 vs. +0.68 for Race–Gender–Age). Although Minor-
ity increases detected faces (+123), these do not translate
into meaningful fairness gains.
PreciseDebias (Clemmer et al., 2024).We apply their au-
tomatic prompt engineering approach with Stable Diffusion
following their protocol. Table 2 reports the changes relative
to baseline.
FairImagen (Fu et al., 2025).We use HuggingFace’s Sta-
ble Diffusion 3 pipeline following their protocol. Table 3
reports the changes relative to baseline.
4.3. Ablation Study
Semantic fidelity.The mean W 2 2 changes by ∆ ¯W 2 2 =
0.0011 on average after refinement, confirming that fairness-
aware rewriting preserves cross-modal semantic alignment.
More details can be found at Appendix D
Effect of KG-guided retrieval vs. plain LLM rewrit-
5

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Table 1.Changes relative to baseline: MinorityPrompt (Um & Ye, 2024) vs. KG-FairDiff. ∆ =Method−Baseline ; negative ∆ for
Bias-P, Bias-W, KL indicates improvement; positive∆ for ENS and ICAD indicates improvement. Both methods are evaluated using
Stable Diffusion following MinorityPrompt’s experimental protocol on the same 100-prompt set. The Faces Detected row reports the total
change in FairFace-detected faces after refinement. Bold values indicate the better result for each metric–attribute pair.
Attribute Bias-P↓ Bias-W↓ ENS↑ KL Divergence↓ ICAD↑
∆Minority∆KG-FairDiff ∆Minority∆KG-FairDiff ∆Minority∆KG-FairDiff ∆Minority∆KG-FairDiff ∆Minority∆KG-FairDiff
Race −0.0045−0.0374 −0.0037−0.1396 +0.03 +1.56 −0.0276−0.8229 +0.406−0.398
Gender +0.0072−0.0827 +0.0028−0.0783 +0.00 +0.05 +0.0014−0.0272 +0.147 +0.485
Age −0.0090−0.0305 −0.0189−0.0745 +0.29 +1.55 −0.1344−0.5758 +0.430+0.149
Race–Gender −0.0006−0.0275 −0.0017−0.0686 +0.07 +2.75 −0.0290−0.7755 +0.211−0.044
Race–Age −0.0042−0.0135 −0.0074−0.0494 +0.42 +5.73 −0.1588−1.2131 +0.373−0.191
Gender–Age −0.0037−0.0163 −0.0097−0.0303 +0.45 +2.40 −0.1170−0.5042 +0.238−0.425
Race–Gender–Age −0.0020−0.0077 −0.0037−0.0232 +0.68 +8.79 −0.1443−1.0997 +0.230−0.607
Faces Detected +123(Minority) −395(KG-FairDiff) – – –
Table 2.Changes relative to baseline: PreciseDebias (Clemmer et al., 2024) vs. KG-FairDiff. ∆ =Method−Baseline ; negative ∆ for
Bias-P, Bias-W, KL indicates improvement; positive∆ for ENS indicates improvement. Both methods are applied with Stable Diffusion
following PreciseDebias’s automatic prompt engineering protocol. Bold values indicate the better result for each metric–attribute pair.
Attribute Bias-P↓ Bias-W↓ ENS↑ KL Divergence↓
∆Precise∆KG-FairDiff ∆Precise∆KG-FairDiff ∆Precise∆KG-FairDiff ∆Precise∆KG-FairDiff
Race +0.03−0.00 −0.10−0.13 +1.84+1.56 −0.61−0.82
Gender +0.24 +0.01 −0.03−0.07 +0.06+0.06 -0.03−0.02
Age +0.04−0.02 +0.01−0.07 −0.31 +1.55 +0.10−0.57
Race–Gender +0.06−0.00 −0.05−0.06 +2.80+2.75 −0.57−0.77
Race–Age +0.02−0.00 −0.01−0.04 +2.83 +5.73 −0.45−1.21
Gender–Age +0.06−0.00 +0.00−0.03 −0.18 +2.40 +0.02−0.50
Race–Gender–Age +0.02 +0.00 −0.00−0.02 +4.14 +8.79 −0.45−1.09
Table 3.Changes Relative to Baseline: FairImagen(Fu et al., 2025) vs. KG-FairDiff.Absolute ∆ = (Method) − (Baseline).
FairImagen† was evaluated using the HuggingFace Stable Diffusion 3 pipeline following the original protocol (Fu et al., 2025); KG-
FairDiff was evaluated on SD v1.5. Since the backbone generators differ, comparisons are indicative only. Dashes (—) indicate attribute
groups not evaluated by FairImagen.
Attribute Group ∆Bias-P↓ ∆Bias-W↓ ∆ENS↑ ∆KL↓ ∆ICAD↑
FI† KGF FI† KGF FI† KGF FI† KGF FI† KGF
Race −0.0003−0.03 −0.0181−0.1396 +4.5548+1.56 −0.7867−0.8229 +0.2345 +1.03
Gender −0.0001−0.11 +0.0018−0.0783 −0.3096 +0.05 +0.0150−0.0272 -0.0948−0.23
Race+Gender −0.0001−0.03 −0.0025−0.0686 +1.8712 +2.75 −0.2231−0.7755 +0.0027 +0.85
†FairImagen evaluated on SD v3; KG-FairDiff on SD v1.5; direct comparison is indicative only.
ing.A natural question is whether the fairness gains
stem from GPT-4o rewriting alone or specifically from
KG-guided retrieval. In our LLM/embedding ablation (Ta-
ble 4), we observe that the quality of retrieved context (em-
bedding model) interacts significantly with the rewriting
quality: switching from text-embedding-3-large
to qwen-embedding-4b increases the keyword bias re-
duction from ∆≈ −40to ∆≈ −77, a gap that cannot be
explained by the LLM rewriter alone since the same GPT-
4o model is compared across rows. This strongly suggests
that the KG-retrieval step contributes independently to the
observed gains.
Table 5 show that KG-FairDiff does not uniformly im-
prove all metrics across all generators. In particular, for
SD 3.5 Large (Gender: Bias-W 0.04→0.18 , and ENS
1.99→1.86 ) and Gemini 3 Pro (R+G: KL 0.79→1.01 ),
several metrics worsen after refinement. We attribute these
regressions to two factors. First, these generators have
strong built-in safety and diversity filters that may partially
conflict with the refined prompt’s explicit demographic de-
scriptors, leading to compositional incoherence. Second,
for intersectional attribute groups (e.g., Race+Gender+Age),
the KG triples retrieved are drawn primarily from the indi-
vidual stereotype categories; when multiple demographic
axes are jointly optimised, the retrieved triples may pull the
prompt in mutually inconsistent directions (e.g., adding both
East Asian and Middle Eastern cultural cues for the same
professional role), causing some images to depict a narrower
demographic slice. Addressing these failure modes through
conflict-aware KG retrieval and generator-specific threshold
tuning is an important direction for future work.
Table 5 reports the full Baseline vs. KG-FairDiff results
for all eight generators. KG-FairDiff does not uniformly
improve all metrics across all generators. In particular, for
6

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Table 4.Ablation study on LLM and Embedding Model com-
binationsEach group of four rows corresponds to a different
(embedding model, LLM rewriter) pairing.Keywordscores mea-
sure prompt-level lexical bias reduction;LLMscores measure
the LLM validator’s bias assessment (lower is better). ∆ =
Enhanced−Original ; larger negative ∆ indicates greater bias
reduction. All configurations use Tmax = 5 refinement iterations.
Embedding LLM KWorig KWenh KW∆ LLMorig LLMenh LLM∆
text-embedding-3-large GPT-4o
13 8370 35 9055
13 9077 35 9055
13 8370 30 9060
13 10087 35 9257
qwen-embedding-4b qwen-3.5-27b
13 9077 15 8873
13 7158 11 8978
13 8370 13 9582
13 10087 14 9480
qwen-embedding-8b qwen-3.5-27b
13 8572 20 7252
13 9077 18 8870
13 7663 25 9166
13 8370 30 8353
qwen-embedding-4b qwen-3-32b
13 8875 25 8358
13 8370 31 8554
13 6956 33 9057
13 7865 30 8656
SD 3.5 Large (Gender: Bias-W 0.04→0.18 , and ENS
1.99→1.86 ) and Gemini 3 Pro (R+G: KL 0.79→1.01 ),
several metrics worsen after refinement. We attribute these
regressions to two factors. First, these generators have
strong built-in safety and diversity filters that may partially
conflict with the refined prompt’s explicit demographic de-
scriptors, leading to compositional incoherence. Second,
for intersectional attribute groups (e.g., Race+Gender+Age),
the KG triples retrieved are drawn primarily from the indi-
vidual stereotype categories; when multiple demographic
axes are jointly optimised, the retrieved triples may pull the
prompt in mutually inconsistent directions (e.g., adding both
East Asian and Middle Eastern cultural cues for the same
professional role), causing some images to depict a narrower
demographic slice. Addressing these failure modes through
conflict-aware KG retrieval and generator-specific threshold
tuning is an important direction for future work.
Face-detection drop.A notable decrease in FairFace-
detected faces is observed after refinement. Refined prompts
introduce more compositional variety, and some images de-
pict non-Western phenotypes for which FairFace’s detector
has lower recall. Crucially, all refined prompts produce at
least one detectable face.
Geo-cultural diversity.The KG triples and the example in
Fig. 1 illustrate that KG-FairDiff can introduce non-Western
cultural cues into generated images. We emphasise, how-
ever, that our current experiments do not include a dedicated
geo-cultural benchmark or metric; the cultural fairness claim
is thereforeindicativerather than rigorously demonstrated.
Establishing whether the framework achieves equitable cov-
erage across world cultures would require a purpose-built
evaluation suite (e.g., using CultureVLM (Liu et al., 2025)
or Culture-TRIP (Jeong et al., 2025)), which we leave for
future work.
Limitations.Key limitations include: (i) reliance on
automated attribute classifiers (FairFace) whose recall is
lower for non-Western phenotypes; (ii) a curated KG with
limited coverage that may not represent all cultural groups
equitably; (iii) unvalidated validator calibration, as the cor-
relation between S(p) and downstream fairness metrics has
not been rigorously measured; (iv) the use of GPT-4o as
both rewriter and validator introduces circularity, which
could be addressed with a held-out LLM or human evalua-
tors in future work; and (v) the absence of a pure LLM-only
rewriting baseline, which would more precisely isolate the
contribution of KG retrieval. Future work will focus on scal-
ing the knowledge graph, improving validator calibration,
and incorporating human evaluation.
5. Conclusion
We have introduced KG-FairDiff, a knowledge graph-
guided prompt refinement framework designed to system-
atically mitigate demographic and cultural bias in text-to-
image generation. Unlike prior approaches that require
model retraining, dataset curation, or access to model inter-
nals, KG-FairDiff operates entirely at inference time and is
compatible with any black-box TTI generator.
Extensive experiments across eight backbone generators—
spanning proprietary (GPT-Image-1, GPT-5-image, Gem-
ini 3 Pro, Gemini 2.5 Flash), open-weight (SD v1.5,
SD 3.5 Large, SD Lightning), and specialised (Qwen-VL-
2512, Zimage) systems—demonstrate that KG-FairDiff
consistently and substantially reduces distributional bias
across gender, race, age, and all intersectional axes. Com-
pared to prompt-level baselines, our method achieves Bias-
W reductions up to 20× larger than MinorityPrompt and
consistently outperforms PreciseDebias across nearly all
metric–attribute pairs, while preserving cross-modal se-
mantic fidelity (∆ ¯W 2 2 = 0.0011). CLIP Directional Sim-
ilarity analysis confirms that refined prompts successfully
steer image generation in the intended diversity direction
(Sdir = +0.071overall).
Future directions.Several promising avenues remain. Scal-
ing the knowledge graph to broader cultural coverage—
particularly for under-represented regions in Africa, South
Asia, and Latin America—is a priority. Developing a ded-
icated geo-cultural fairness benchmark, analogous to Cul-
tureVLM or Culture-TRIP, would enable more rigorous
evaluation of cultural representational equity. Rigorous
calibration of the LLM validator against downstream fair-
ness metrics, and the introduction of a held-out evaluator
to address the rewriter–validator circularity, are important
methodological improvements. Finally, extending the frame-
work to video generation and multimodal grounding tasks
represents a natural next step as generative AI systems con-
tinue to expand in scope and societal impact.
7

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Table 5.Ablation across all eight image generators, Baseline (B) vs. KG-FairDiff (K).Lower is better for Bias-P, Bias-W, KL; higher
is better for ENS, ICAD.Bold= better result. A horizontal rule separates the two groups.
Generator AttrBias-P Bias-W KL ENS ICAD
B K B K B K B K B K
Race0.130.170.120.150.560.683.973.52 4.314.77
Gender 0.09 0.13 0.050.010.00 0.00 1.981.994.915.34
Age 0.200.150.160.131.010.713.254.41 4.914.49
GPT-Image-1 R+G 0.11 0.11 0.06 0.07 0.58 0.74 7.83 6.64 3.664.23
R+A 0.060.050.03 0.03 1.72 1.85 11.25 9.89 3.924.13
G+A 0.130.090.090.081.150.825.657.864.284.42
R+G+A 0.040.030.02 0.02 1.95 2.02 17.82 16.68 3.223.65
Race 0.300.270.300.181.490.901.562.824.514.88
Gender 0.26 0.37 0.170.060.060.001.871.985.025.30
Age 0.22 0.24 0.15 0.17 0.95 1.17 3.44 2.78 5.065.12
Qwen-VL-2512 R+G 0.190.170.160.101.571.092.884.684.51 4.15
R+A 0.08 0.09 0.060.052.522.335.046.074.61 4.33
G+A 0.15 0.17 0.10 0.10 1.351.304.634.854.72 4.33
R+G+A 0.060.050.03 0.03 2.932.706.688.444.47 3.99
Race 0.270.230.240.211.150.972.212.634.79 4.86
Gender 0.270.210.04 0.18 0.00 0.06 1.99 1.86 4.784.84
Age 0.270.240.270.221.721.361.602.294.97 4.63
SD 3.5 Large R+G 0.170.140.12 0.12 1.161.074.364.764.514.56
R+A 0.090.070.080.062.922.463.385.374.214.45
G+A 0.170.140.130.121.811.542.933.824.78 4.25
R+G+A 0.060.040.040.033.032.696.078.494.124.17
Race 0.290.210.18 0.20 0.900.882.822.884.774.89
Gender 0.320.200.040.000.00 0.00 1.992.005.385.51
Age 0.240.190.190.151.150.792.834.044.59 4.36
Zimage R+G 0.200.130.10 0.10 0.96 0.97 5.35 5.25 4.84 4.49
R+A 0.090.070.05 0.05 2.272.186.457.074.50 3.98
G+A 0.160.110.110.091.331.034.716.404.70 4.18
R+G+A 0.060.040.03 0.03 2.492.4610.4010.724.46 3.77
Race 0.220.190.190.160.720.573.383.924.474.60
Gender 0.140.060.060.010.00 0.00 1.981.994.884.99
Age 0.200.170.150.120.900.633.644.774.73 4.46
SD Lightning R+G 0.140.120.090.080.740.596.637.724.10 4.02
R+A 0.06 0.06 0.040.031.671.3211.8216.754.14 4.10
G+A 0.130.110.090.071.070.776.158.324.59 4.33
R+G+A 0.04 0.04 0.020.011.861.4819.5528.613.89 3.75
Race 0.200.180.15 0.16 0.67 0.75 3.55 3.28 5.17 4.94
Gender 0.230.010.01 0.02 0.00 0.00 1.99 1.99 5.385.46
Age 0.190.170.150.130.81 0.82 3.97 3.94 5.41 5.36
Gemini 3 Pro R+G 0.140.110.08 0.10 0.79 1.01 6.32 5.05 4.69 4.45
R+A 0.06 0.06 0.03 0.03 1.67 1.80 11.85 10.32 4.72 4.09
G+A 0.120.100.07 0.07 0.83 0.93 7.78 7.03 4.75 4.56
R+G+A 0.04 0.04 0.02 0.02 1.83 2.21 20.15 13.78 4.04 3.53
Race 0.21 0.21 0.14 0.17 0.62 0.78 3.73 3.19 4.78 4.44
Gender 0.110.060.00 0.05 0.00 0.00 1.99 1.98 4.88 4.86
Age 0.240.210.220.171.391.072.243.054.414.53
Gemini 2.5 Flash R+G 0.13 0.13 0.07 0.09 0.66 0.86 7.18 5.88 4.23 3.83
R+A 0.070.060.04 0.04 2.092.007.778.454.15 3.62
G+A 0.14 0.14 0.11 0.11 1.491.384.034.504.40 4.16
R+G+A 0.04 0.04 0.02 0.03 2.25 2.54 13.27 9.86 3.84 3.69
Race0.130.170.120.150.560.683.973.52 4.314.77
Gender 0.09 0.13 0.050.010.00 0.00 1.981.994.915.34
Age 0.200.150.160.131.010.713.254.414.91 4.49
GPT-5-image R+G 0.11 0.11 0.06 0.07 0.58 0.74 7.83 6.64 3.664.23
R+A 0.060.050.03 0.03 1.72 1.85 11.25 9.89 3.924.13
G+A 0.130.090.090.081.150.825.657.864.284.42
R+G+A 0.040.030.02 0.02 1.95 2.02 17.82 16.68 3.223.65
8

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Impact Statement
This work addresses a critical and well-documented societal
harm: the systematic amplification of demographic stereo-
types in text-to-image (TTI) generation systems. As these
systems are increasingly deployed in high-stakes contexts—
including media production, hiring visualisations, educa-
tional materials, and public communications—their ten-
dency to reproduce racial, gender, and age-based stereo-
types has direct negative consequences for the populations
they misrepresent or erase. By providing a training-free,
inference-time, model-agnostic debiasing framework, KG-
ree, inference-time, model-agnostic debiasing framework,
KG-FairDiff significantly lowers the practical barrier to
deploying fairer AI-generated imagery without requiring
access to model weights or costly retraining pipelines.
KG-FairDiff promotes representational equity by actively
countering stereotypical associations retrieved from struc-
tured knowledge sources. The framework introduces non-
Western cultural cues, occupational counter-stereotypes,
and intersectional diversity into generated images. Broad
adoption of such prompt-level debiasing tools could mean-
ingfully increase the cultural and demographic breadth of
AI-generated visual content worldwide. The framework
is also inherently interpretable: every refinement step is
grounded in explicit KG triples with documented prove-
nance, enabling practitioners to audit and contest individual
decisions.rounded in explicit KG triples with documented
provenance, enabling practitioners to audit and contest indi-
vidual decisions.
Acknowledgement
This work was supported by funding from QCRI/HBKU.
References
Anonymous. Diverse diffusion: Enhancing image diversity
in text-to-image generation.Submitted to Transactions
on Machine Learning Research, 2024. URL https:
//openreview.net/forum?id=F0J1N6M5N9.
Bang, Y ., Chen, D., Lee, N., and Fung, P. Measuring politi-
cal bias in large language models: What is said and how
it is said, 2024. URL https://arxiv.org/abs/
2403.18932.
Bonna, S., Huang, Y .-C., Novozhilova, E., Paik, S., Shan,
Z., Feng, M. Y ., Gao, G., Tayal, Y ., Kulkarni, R., Yu, J.,
Divekar, N., Ghadiyaram, D., Wijaya, D., and Betke, M.
DebiasPI: Inference-time debiasing by prompt iteration
of a text-to-image generative model. InComputer Vision
– ECCV 2024 Workshops, volume 15643 ofLecture Notes
in Computer Science, pp. 68–83. Springer, 2025. doi:
10.1007/978-3-031-92648-8 5.
Clemmer, C., Ding, J., and Feng, Y . Precisedebias:
An automatic prompt engineering approach for gen-
erative ai to mitigate image demographic biases. In
2024 IEEE/CVF Winter Conference on Applications of
Computer Vision (WACV), pp. 8581–8590, 2024. doi:
10.1109/W ACV57701.2024.00840.
Cui, W., Li, Z., Sun, H., Lopez, D., Das, K., Malin,
B. A., Kumar, S., and Zhang, J. A survey of au-
tomatic prompt optimization with instruction-focused
heuristic-based search algorithm, 2025. URL https:
//arxiv.org/abs/2502.18746.
Dai, D., Li, Y ., Liu, Y ., Jia, M., YuanHui, Z., and Wang, G.
15m multimodal facial image-text dataset, 2024. URL
https://arxiv.org/abs/2407.08515.
D’Inc`a, M., Peruzzo, E., Mancini, M., Xu, D., Goel, V ., Xu,
X., Wang, Z., Shi, H., and Sebe, N. OpenBias: Open-set
bias detection in text-to-image generative models. InPro-
ceedings of the IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition (CVPR), pp. 12225–12235,
June 2024.
Dominguez-Catena, I., Paternain, D., and Galar, M. Metrics
for dataset demographic bias: A case study on facial
expression recognition.IEEE Trans. Pattern Anal. Mach.
Intell., 46(8):5209–5226, August 2024. ISSN 0162-8828.
doi: 10.1109/TPAMI.2024.3361979. URL https://
doi.org/10.1109/TPAMI.2024.3361979.
Esposito, P., Atighehchian, P., Germanidis, A., and Ghadi-
yaram, D. Mitigating stereotypical biases in text to im-
age generative systems, 2023. URL https://arxiv.
org/abs/2310.06904.
Fan, Z., Chen, R., and Liu, Z. Biasguard: A reasoning-
enhanced bias detection tool for large language mod-
els, 2025. URL https://arxiv.org/abs/2504.
21299.
Friedrich, F., Brack, M., Struppek, L., Hintersdorf, D.,
Schramowski, P., Luccioni, S., and Kersting, K. Au-
diting and instructing text-to-image generation models
on fairness.AI and Ethics, 5(3):2103–2123, 2025. doi:
10.1007/s43681-024-00531-5.
Fu, Z., Brown, R., Shao, S., Rawal, K., Delaney, E., and
Russell, C. Fairimagen: Post-processing for bias mit-
igation in text-to-image models, 2025. URL https:
//arxiv.org/abs/2510.21363.
Gallegos, I. O. and et al. Bias and fairness in large language
models: A survey.Computational Linguistics, 2024. doi:
10.1162/coli a 00524. URL https://doi.org/10.
1162/coli_a_00524.
9

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Jeong, S., Choi, I., Yun, Y ., and Kim, J. Culture-trip:
Culturally-aware text-to-image generation with iterative
prompt refinement, 2025. URL https://arxiv.
org/abs/2502.16902.
Jiang, Y ., Lyu, Y ., He, Z., Peng, B., and Dong, J. Mitigat-
ing social biases in text-to-image diffusion models via
linguistic-aligned attention guidance. InACM Multime-
dia 2024, 2024. URL https://openreview.net/
forum?id=rtjZHEOcHx.
Karkkainen, K. and Joo, J. Fairface: Face attribute dataset
for balanced race, gender, and age for bias measurement
and mitigation. InProceedings of the IEEE/CVF Winter
Conference on Applications of Computer Vision, 2021.
Kim, E., Kim, S., Park, M., Entezari, R., and Yoon, S. Re-
thinking training for de-biasing text-to-image generation:
Unlocking the potential of stable diffusion, 2025. URL
https://arxiv.org/abs/2408.12692.
Lee, T., Yasunaga, M., Meng, C., Mai, Y ., Park, J. S., Gupta,
A., Zhang, Y ., Narayanan, D., Teufel, H., Bellagente,
M., et al. Holistic evaluation of text-to-image models.
InAdvances in Neural Information Processing Systems,
volume 36, 2024. URL https://arxiv.org/abs/
2311.04287.
Li, J., Hu, L., Zhang, J., Zheng, T., Zhang, H., and
Wang, D. Fair text-to-image diffusion via fair mapping,
2024. URL https://openreview.net/forum?
id=vDJ4tzczlG.
Lin, L., Wang, L., Guo, J., and Wong, K.-F. Investigating
bias in llm-based bias detection: Disparities between llms
and human perception, 2024. URL https://arxiv.
org/abs/2403.14896.
Liu, S., Jin, Y ., Li, C., Wong, D. F., Wen, Q., Sun, L., Chen,
H., Xie, X., and Wang, J. Culturevlm: Characterizing
and improving cultural understanding of vision-language
models for over 100 countries, 2025. URL https://
arxiv.org/abs/2501.01282.
Liu, Z., Schaldenbrand, P., Okogwu, B.-C., Peng, W., Yun,
Y ., Hundt, A., Kim, J., and Oh, J. Scoft: Self-contrastive
fine-tuning for equitable image generation, 2024. URL
https://arxiv.org/abs/2401.08053.
Luccioni, S., Akiki, C., Mitchell, M., and Jernite, Y . Sta-
ble bias: Evaluating societal representations in diffusion
models. InThirty-seventh Conference on Neural Informa-
tion Processing Systems Datasets and Benchmarks Track,
2023. URL https://openreview.net/forum?
id=qVXYU3F017.
Masrourisaadat, N., Sedaghatkish, N., Sarshartehrani, F.,
and Fox, E. A. Analyzing quality, bias, and performance
in text-to-image generative models, 2024. URL https:
//arxiv.org/abs/2407.00138.
Miao, Z., Wang, J., Wang, Z., Yang, Z., Wang, L., Qiu,
Q., and Liu, Z. Training diffusion models towards di-
verse image generation with reinforcement learning. In
Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 2024.
Naous, T. and et al. Having beer after prayer? mea-
suring cultural bias in large language models. InPro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long Pa-
pers). Association for Computational Linguistics, 2024.
doi: 10.18653/v1/2024.acl-long.862. URL https:
//aclanthology.org/2024.acl-long.862/.
Pistilli, G., Leidinger, A., Jernite, Y ., Kasirzadeh, A., Luc-
cioni, A. S., and Mitchell, M. Civics: Building a dataset
for examining culturally-informed values in large lan-
guage models, 2024. URL https://arxiv.org/
abs/2405.13974.
Prerak, S. Addressing bias in text-to-image generation: A
review of mitigation methods. In2024 Third International
Conference on Smart Technologies and Systems for Next
Generation Computing (ICSTSN), 2024. doi: 10.1109/
ICSTSN61422.2024.10671230.
Sahili, Z. A., Patras, I., and Purver, M. Faircot: Enhancing
fairness in diffusion models via chain of thought reason-
ing of multimodal language models, 2025. URL https:
//openreview.net/forum?id=WGWoRZb0pT.
Shi, W. and et al. CultureBank: An online
community-driven knowledge base towards cultur-
ally aware language technologies. InFindings
of the Association for Computational Linguistics:
EMNLP 2024. Association for Computational Linguis-
tics, 2024. doi: 10.18653/v1/2024.findings-emnlp.
288. URL https://aclanthology.org/2024.
findings-emnlp.288/.
Shin, J. and Jang, H. Data augmentation techniques us-
ing text-to-image diffusion models for enhanced data
diversity. In2024 15th International Conference on In-
formation and Communication Technology Convergence
(ICTC), 2024. doi: 10.1109/ICTC62082.2024.10827311.
Su, W., Tang, Y ., Ai, Q., Wu, Z., and Liu, Y . Dragin:
Dynamic retrieval augmented generation based on the
information needs of large language models, 2024. URL
https://arxiv.org/abs/2403.10081.
10

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Um, S. and Ye, J. C. Minorityprompt: Text to
minority image generation via prompt optimization,
2024. URL https://openreview.net/forum?
id=98dyxUoI3q.
Vasilev, V . A. and et al. Craft: Cultural russian-oriented
dataset adaptation for focused text-to-image genera-
tion.Doklady Mathematics, 2024. doi: 10.1134/
s1064562424602324. URL http://dx.doi.org/
10.1134/S1064562424602324.
Vice, J., Akhtar, N., Hartley, R., and Mian, A. Exploring
bias in over 100 text-to-image generative models, 2025.
URLhttps://arxiv.org/abs/2503.08012.
Wan, Y . and et al. Survey of bias in text-to-image genera-
tion: Definition, evaluation, and mitigation, 2024. URL
https://arxiv.org/abs/2404.01030.
Wang, J. and et al. T2IAT: Measuring valence and
stereotypical biases in text-to-image generation. In
Findings of the Association for Computational Linguis-
tics: ACL 2023. Association for Computational Lin-
guistics, 2023. doi: 10.18653/v1/2023.findings-acl.
160. URL https://aclanthology.org/2023.
findings-acl.160/.
Wang, Y . and et al. CDEval: A benchmark for measuring the
cultural dimensions of large language models. InProceed-
ings of the 2nd Workshop on Cross-Cultural Considera-
tions in NLP. Association for Computational Linguistics,
2024. doi: 10.18653/v1/2024.c3nlp-1.1. URL https:
//aclanthology.org/2024.c3nlp-1.1/.
Weng, Z., Gao, Z., Andrews, J., and Zhao, J. Images speak
louder than words: Understanding and mitigating bias in
vision-language model from a causal mediation perspec-
tive, 2025. URL https://arxiv.org/abs/2407.
02814.
Zhang, C., Chen, X., Chai, S., Wu, C. H., Lagun, D., Beeler,
T., and De la Torre, F. ITI-GEN: Inclusive text-to-image
generation. InProceedings of the IEEE/CVF Interna-
tional Conference on Computer Vision (ICCV), pp. 3969–
3980, October 2023.
11

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Appendix Overview
This appendix consolidates the theoretical foundations, metric definitions, and extended experimental analyses that support
the main results of the paper. Each section expands on concepts introduced in the main text, providing formal guarantees,
mathematical relationships, and empirical validation of the proposed framework.
Theoretical Derivations (Section A).This section presents the formal guarantees underlying the iterative refinement
process and fairness metrics. TheENS–KL Relationship(Section A.1) proves the equivalence between maximizing entropy-
based diversity (ENS) and minimizing KL divergence to a uniform distribution, formally linking diversity objectives to
information-theoretic principles. TheBias-P and Bias-Wdefinitions (Section A.2) introduce per-prompt and dataset-level
bias metrics and prove that dataset-level bias is upper-bounded by the average per-prompt bias, providing a theoretical
consistency guarantee. Finally,Cross-Modal Alignment via Wasserstein Distance(Section A.3) formulates semantic
alignment between prompts and generated images using optimal transport, capturing geometry-aware similarity beyond
cosine-based measures.
Evaluation Metric Definitions (Section B).This section provides complete formal definitions of all evaluation metrics
used in the experiments. TheIntra-Class Attribute Diversity (ICAD)metric (Section B.1) defines a centroid-based measure
of intra-prompt visual diversity, quantifying variation among generated images for the same prompt. The definitions of
Bias-P and Bias-W(Section B.2) are revisited for completeness, with reference to their theoretical relationship. TheENS
and KL Divergenceformulation (Section B.3) reiterates their equivalence and explains how KL divergence to a uniform
distribution serves as a principled measure of demographic balance.
CLIP Directional Similarity (Section C).This section introduces a metric for evaluating whether prompt refinements
induce the intended semantic shift in generated images. The formal definition (Section C.1) expresses directional similarity
as the cosine alignment between text-space and image-space transformations. Its interpretation (Section C.2) clarifies
how scores reflect alignment quality, ranging from agreement to protesting shifts. Implementation details (Section C.3)
describe the use of a high-capacity vision–language model for embedding extraction. Experimental results (Section C.4)
report consistent positive alignment across professions while highlighting variability depending on prompt specificity. The
conclusion (Section C.5) summarizes that this metric provides quantitative evidence of effective prompt steering.
Optimal-Transport-Based Multimodal Alignment (Section D).This section presents a comprehensive framework
for measuring alignment between text and image modalities using optimal transport theory. The feature extraction and
normalization process (Section D) ensures stable representations across modalities. The optimal transport formulation defines
how probability mass is matched between image patches and text tokens. TheWasserstein Distancecaptures direct semantic
correspondence, while theGromov–Wasserstein Distancemeasures structural consistency through intra-modal relationships.
TheFused Gromov–Wasserstein Distancecombines both perspectives into a unified objective. The iteration-wise analysis
demonstrates that while direct semantic alignment may fluctuate, structural alignment improves consistently, with later
iterations achieving the best overall balance.
Qualitative Comparison (Section E).This section complements the quantitative analysis with visual examples com-
paring outputs before and after prompt enhancement. These results provide intuitive evidence of improved diversity and
representation, with additional examples available via the external link provided in the appendix.
A. Theoretical Derivations
This appendix provides the full proofs and formal derivations summarised in Section 3.4 of the main paper.
A.1. ENS–KL Relationship
The following theorem, drawn from (Dominguez-Catena et al., 2024), establishes the equivalence between maximising
diversity (ENS) and minimising KL divergence to the uniform distribution.
Theorem A.1.Let p(a) be the empirical distribution over categories a∈ AG, u(a) = 1/nG the uniform distribution, and
H(p) =− P a p(a) lnp(a)the Shannon entropy. Then:
DKL(p∥u) = lnn G −H(p). (6)
12

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Consequently, definingENS = exp(H(p)):
ENS =n G exp(−DKL(p∥u)). (7)
Proof.By definition of KL divergence:
DKL(p∥u) =
X
a
p(a) ln p(a) u(a) = X a p(a) ln  nG ·p(a) 
= lnn G +
X
a
p(a) lnp(a) = lnn G −H(p). (8)
Exponentiating both sides givesexp(H(p)) =n G exp(−DKL(p∥u)), which is the stated result.
Thus minimising KL divergence to uniform is equivalent to maximising entropy/ENS. ENS ranges from 1 (all outputs
collapse to one category) ton G (perfectly uniform representation).
A.2. Bias-P and Bias-W: Formal Definitions and Relationship
The Bias-P and Bias-W metrics were introduced by Jiang et al. (Jiang et al., 2024) to quantify demographic skew at the
per-prompt and dataset levels, respectively.
Letˆpi(a)be the empirical attribute distribution for promptiand¯p(a) = 1 |P| P i ˆpi(a)the dataset-level distribution:
Bias-P = 1 |P| X i

1
nG
X
a∈AG

ˆpi(a)− 1 nG
2!1/2
,(9)
Bias-W =

1
nG
X
a∈AG

¯p(a)− 1 nG
2!1/2
. (10)
Proposition A.2.Bias-W≤Bias-P.
Proof. Define fi = (ˆpi −u) where u is the uniform vector of length nG, and note that ¯p−u= 1 |P| P i fi. By the triangle
inequality for theℓ 2 norm:  1 |P| X i fi  2 ≤ 1 |P| X i ∥fi∥2. (11)
Dividing both sides by √nG yieldsBias-W≤Bias-P.
Hence dataset-level bias cannot exceed average per-prompt bias, making Bias-W a lower bound on Bias-P across any prompt
set.
A.3. Cross-Modal Alignment via Wasserstein Distance
We measure semantic fidelity between refined prompts and their generated images via the squared 2-Wasserstein distance,
defined as follows.
Let X={x i}n i=1 be CLIP ViT-L/14 patch-token embeddings of the generated image with uniform weightsµi = 1/n, and
Y={y j}m j=1 the token embeddings of the refined prompt with importance weights νj derived from softmax-normalised
attention scores of the final CLIP text encoder layer, satisfyingP i µi = P j νj = 1. The squared 2-Wasserstein distance is:
W 2 2 (X, Y) = min π∈Π(µ,ν)
nX
i=1
mX
j=1
πij ∥xi −y j∥2 2, (12)
where the feasible transport set is
Π(µ, ν) =
n
π∈R n×m +

 P j πij =µ i, P i πij =ν j o . (13)
13

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Smaller W 2 2 indicates stronger semantic alignment between the refined prompt and the generated image, providing a
geometry-aware complement to cosine-based CLIP scores. We report mean±std ofW 2 2 across all prompt–image pairs.
B. Evaluation Metric Definitions
For completeness, we provide the full formal definitions of all evaluation metrics used in the experimental evaluation.
B.1. Intra-Class Attribute Diversity (ICAD)
ICAD (Li et al., 2024) measures the intra-prompt visual diversity of a set of generated images. For a prompt c, let Sc denote
the set of CLIP ViT-L/14 image embeddings produced for that prompt. The per-prompt ICAD score is the mean ℓ2 distance
of each image embedding from the prompt-level centroid:
ICAD(c) = 1 |Sc| X ek∈Sc ∥ek −¯ec∥2 ,¯e c = 1 |Sc| X ei∈Sc ei. (14)
The dataset-level ICAD is averaged over all prompts:
ICAD = 1 |D| X c∈D ICAD(c), (15)
where D is the full prompt set. Higher ICAD indicates greater intra-prompt visual diversity; the centroid ¯ec is computed
over the entireS c before the norm is taken, so the formula yields zero only when all images are identical.
B.2. Bias-P and Bias-W
See Appendix A.2 for full formal definitions and the proof thatBias-W≤Bias-P.
B.3. Effective Number of Species (ENS) and KL Divergence
See Appendix A.1 for the formal definitions and the proof of the ENS–KL equivalence. KL divergence to the uniform
reference is computed as:
DKL(p∥u) =
X
a∈AG
p(a) ln(nG ·p(a)), (16)
where p(a) is the empirical attribute frequency and u(a) = 1/n G. Lower KL divergence indicates better demographic
balance relative to a uniform target.
C. CLIP Directional Similarity
C.1. Definition
CLIP Directional Similarity repurposes the joint vision–language embedding space of CLIP to measure directional alignment
between a text-space editing direction and the corresponding image-space response.
Given a base promptT − and an enhanced promptT +, andNmatched image pairs generated from each, the score is:
Sdir = 1 N
NX
i=1
cos

ϕI (I + i )−ϕ I (I − i )| {z }
∆Ii
, ϕT (T +)−ϕ T (T −)| {z }
∆T

 , (17)
where ϕT (·) and ϕI (·) denote the ℓ2-normalised text and image encodings, and cos(·,·) is the cosine similarity. Both
difference vectors are therefore unit-normalised before the dot product is taken.
14

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Table C1.CLIP Directional Similarity — per-profession summary (N= 100pairs each).
Profession Pairs Min Max Avg Std
Doctors 100+0.029 +0.105 +0.0630±0.017
Nurses 100−0.046 +0.125 +0.0462±0.031
Engineers 100+0.048 +0.164 +0.0994±0.021
Scientists 100+0.008 +0.135 +0.0803±0.025
Overall 400−0.046 +0.164 +0.0708±0.028
C.2. Interpretation
Score Meaning
+1Visual shift perfectly mirrors the textual shift
0Orthogonal — no measurable visual correlation
−1Visual shift opposes the textual shift
A positive score confirms that the enhanced prompt successfully pushed the generated images in a direction that is
semantically consistent with the additional diversity content injected into the text. A score near zero would indicate that the
model ignored the new textual cues.
C.3. Implementation
The evaluation uses SigLIP 2 Giant (google/siglip2-giant-opt-patch16-384), a ViT-Giant/16 model trained
with the SigLIP 2 objective (2 B parameters, 1152-dimensional embeddings, float16 precision). SigLIP 2 provides
stronger image–text alignment than standard CLIP-ViT-H/14 on diversity-heavy prompts, making it better suited for this
evaluation task.
C.4. Experimental Results
Setup.
• Input prompts: 4 base prompts (Doctors, Nurses, Engineers, Scientists).
• Image pairs per row:N= 100, generated with matched seeds.
• Generation model: Qwen-Image-2512.
• Embedding model: SigLIP 2 Giant.
Per-Row Results.Table C1 summarises the directional similarity scores. TheMinandMaxcolumns report the single-pair
extremes across all 100 seeds, giving a sense of the score distribution, whileAvgis the primary metric (Equation 17).
Discussion.All four professions yield a positive overall average ( Sdir = +0.071), confirming that the enhanced prompts
consistently move the image generator in the intended direction.
Engineers (+0.099) and Scientists (+0.080) show the strongest alignment. The enhanced prompts for these professions
introduce many concrete, visually grounded elements (cultural garments, tools, lab coats with motifs) that the diffusion
model can latch on to.
Doctors (+0.063) and Nurses (+0.046) score lower. The Nurses prompt is the only row containing negative per-pair scores
(min =−0.046 ), suggesting that some image pairs exhibit a visual drift orthogonal or even contrary to the textual direction.
This is likely because subtle narrative elements in the enhanced prompt (e.g.wristbands, passport photos) are harder for the
model to render consistently.
Across all rows the score distribution is right-skewed with a long positive tail, indicating that while most seed pairs produce a
modest positive alignment signal, a subset of seeds yields notably strong alignment — reaching up to +0.164 for Engineers.
15

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
C.5. Conclusion
The overall directional similarity of +0.071 provides quantitative evidence that RAG-enhanced prompts succeed in steering
text-to-image generation toward more diverse and representative outputs. The metric is sensitive enough to distinguish
between professions and prompt styles, making it a practical tool for iterative prompt refinement. Future work should
examine whether higher scores also translate to improved perceptual diversity as rated by human evaluators.
D. Optimal-Transport-Based Multimodal Alignment
D.1. Feature Extraction and Anisotropy Correction
Let I denote an input image and T denote the corresponding text prompt. A Vision Transformer (ViT) is used to extract
image-patch features, while a Text Transformer (e.g., CLIP) is used to extract token-level text features.
D.1.1. IMAGE PROCESSING FLOW
The image I is divided into a sequence of M patches. After passing through the Vision Transformer and discarding the
global classification token, we obtain raw local patch representations
˜V∈R M×d ,
where d is the embedding dimension. Let ˜vi ∈R d denote the raw representation of patch i. To mitigate representation
anisotropy, feature-wise Z-score standardization is applied:
vi = ˜vi −µ ˜vi
σ˜vi +ϵ ,∀i∈ {1, . . . , M}, (18)
where µ˜vi and σ˜vi are the mean and standard deviation across the embedding dimensions of patch i, and ϵ= 10 −5 is a small
constant for numerical stability. The final set of image patch embeddings is
V={v i}M i=1.
Explanation.Equation (18) normalizes each patch embedding by centering it around zero and scaling it by its standard
deviation. This reduces anisotropy in the visual embedding space and produces more stable feature representations for
transport-based comparison.
D.1.2. TEXT PROCESSING FLOW
Similarly, the text prompt T is tokenized into a sequence. After passing through the Text Transformer, the Start-of-Sequence
(SOS) and End-of-Text (EOT) tokens are discarded, yielding N valid token embeddings
˜U∈R N×d .
Let ˜uj ∈R d denote the raw representation of token j. Applying the same Z-score standardization gives
uj = ˜uj −µ ˜uj
σ˜uj +ϵ ,∀j∈ {1, . . . , N}, (19)
and the final set of text token embeddings is
U={u j}N j=1.
Explanation.Equation (19) applies the same normalization strategy to the textual embeddings. Using the same stabiliza-
tion for both modalities makes the subsequent alignment process more comparable and robust.
D.2. Optimal Transport Alignment
To measure the alignment between the visual patches V and textual tokens U, uniform marginal distributions are defined
over the image patches and text tokens:
pi = 1 M ,∀i, q j = 1 N ,∀j. (20)
16

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Let Π(p, q)denote the transport polytope containing all valid joint probability couplings π∈R M×N + satisfying the marginal
constraints:
Π(p, q) =


π∈R M×N +

 NX j=1 πi,j =p i ∀i, MX i=1 πi,j =q j ∀j    . (21)
Explanation.Equation (20) assigns equal mass to each image patch and each text token. Equation (21) defines the
feasible set of transport plans that preserve these marginals, ensuring that the transport solution distributes probability mass
consistently across both modalities.
D.3. Wasserstein Distance (WD)
The Wasserstein Distance evaluates direct cross-domain semantic alignment between visual and textual features. The
semantic cost matrix M∈R M×N is defined using cosine distance:
Mi,j = 1− ⟨vi, uj⟩ ∥vi∥2 ∥uj∥2 . (22)
The optimal transport plan minimizes the total semantic cost:
W(V, U) = min
π∈Π(p,q)
MX
i=1
NX
j=1
πi,jMi,j. (23)
Explanation.Equation (22) measures how dissimilar each image patch is from each text token in the shared embedding
space. Equation (23) then finds the transport plan that minimizes the total cross-modal semantic mismatch. Therefore, a
lower WD indicates better direct semantic agreement between the generated image content and the text prompt.
D.4. Gromov–Wasserstein Distance (GWD)
Unlike WD, the Gromov–Wasserstein Distance measures structural isomorphism by comparing intra-domain geometric
relationships rather than direct cross-domain features. The intra-image and intra-text cost matrices are defined using
normalized squared Euclidean distances:
C V i,i′ = ∥vi −v i′∥2 2 maxk,l ∥vk −v l∥2 2 , C U j,j′ = ∥uj −u j′∥2 2 maxk,l ∥uk −u l∥2 2 . (24)
Using the squared loss
L(a, b) = (a−b)2, (25)
the Gromov–Wasserstein objective becomes
GW(V, U) = min
π∈Π(p,q)
MX
i=1
MX
i′=1
NX
j=1
NX
j′=1
L

C V i,i′, CU j,j′  πi,jπi′,j′. (26)
Explanation.Equation (24) captures pairwise relations within the image modality and within the text modality. Equa-
tion (26) compares these two relational structures through the transport plan. Lower GWD means that the internal
organization of image features is more consistent with the internal organization of textual features, even when direct feature
matching is not perfect.
D.5. Fused Gromov–Wasserstein Distance (FGWD)
The Fused Gromov–Wasserstein Distance jointly considers direct semantic matching and structural similarity. A hyperpa-
rameter α∈[0,1] controls the trade-off between the Wasserstein term and the Gromov–Wasserstein term:
F GWα(V, U) = min π∈Π(p,q)
MX
i=1
NX
j=1
πi,j

(1−α)M i,j +α
MX
i′=1
NX
j′=1
L

C V i,i′, CU j,j′  πi′,j′

 . (27)
17

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Explanation.Equation (27) combines the direct semantic mismatch term from WD with the structural consistency term
from GWD. When α→0 , the objective approaches standard WD and prioritizes direct feature matching. When α→1 , it
approaches pure GWD and prioritizes structural alignment. Thus, FGWD provides a holistic multimodal alignment score
that reflects both semantic fidelity and relational coherence.
D.6. Iteration-wise Quantitative Results
Table D2 summarizes the Optimal Transport-based metrics across five generative iterations. Since these metrics represent
transport costs or distances, lower values indicate better alignment between the generated images and the corresponding text
prompts.
Table D2.Iteration-wise Optimal Transport alignment metrics. Lower values indicate better multimodal alignment.
Iteration Image Count WD GWD FGWD
iteration 14 0.748961 0.023537 0.404259
iteration 25 0.754772 0.018855 0.405986
iteration 32 0.763011 0.016279 0.408596
iteration 450.7453710.017281 0.399026
iteration 54 0.7463530.014763 0.398786
Explanation of the quantitative trends.The standard Wasserstein Distance (WD), defined in Equation (23), reflects
direct semantic feature matching between image patches and text tokens. Its evolution is non-linear: WD increases
from iteration 1 to iteration 3, reaching its largest value at iteration 3, and then decreases sharply in
iteration 4 and remains low in iteration 5. This indicates that direct semantic matching becomes temporarily
more difficult in the middle iterations, but improves again in the later stages.
The Gromov–Wasserstein Distance (GWD), defined in Equation (26), measures the compatibility of internal structural
relationships between the visual and textual modalities. In contrast to WD, GWD shows an overall decreasing trend
from iteration 1 to iteration 5, with only a slight increase at iteration 4. This suggests that the internal
relational structure of the generated images becomes progressively more consistent with the structure of the text prompts
over successive iterations.
The Fused Gromov–Wasserstein Distance (FGWD), defined in Equation (27), balances both semantic correspondence and
structural similarity. Its trend broadly follows the behavior of WD, peaking at iteration 3 and improving afterward.
The minimum FGWD is obtained at iteration 5, indicating the strongest overall multimodal alignment when both
direct feature agreement and structural coherence are taken into account.
Overall interpretation.Taken together, these results show that the iterative generation process improves multimodal
alignment over time. Although the best pure semantic score (WD) is achieved at iteration 4, the best structural
score (GWD) and the best overall fused score (FGWD) are obtained at iteration 5. Therefore, iteration 5 can
be interpreted as the most balanced and robust final iteration when both semantic fidelity and structural consistency are
considered jointly.
E. Qualitative comparison
In this section, we present results from the generated images for a prompt using a before-and-after prompt-enhancement
setup. More images are provided in this link 1
E.1. Prompt Comparison
Generic prompt.Generate a close-up image of a group of Doctors who are smiling at my camera full face.
Enhanced prompt.[”Generate a vibrant, close-up image showcasing the unity in diversity amongst a group of Doctors
from various corners of the world. They should be arrayed in a way that celebrates not just professional camaraderie but a
1https://drive.google.com/drive/folders/1bP4u2bjupUGT9KMm9X7gHPLx4p1LLBsX
18

KG-FairDiff: Knowledge Graph-Guided Prompt Refinement for Fair TTI
Figure E1.Qualitative comparison for Prompt Comparison 1. Left: an image generated with the generic prompt. Right: an image
generated with the enhanced prompt.
rich blend of cultural identities. Let’s see youthful Indian interns buzzing with vigor, middle-aged Korean specialists attired
in traditional Hanbok, expressing warmth with their radiant smiles, and sage Greek practitioners wearing the ceremonious
attire associated with their graduation. Woven into this tapestry, capture also a dedicated Singaporean surgeon and a
resilient American doctor who uses sign language, both effortlessly partaking in the group’s jovial exchange. Include
a charming visual dialogue that hints at shared interests, like some Doctors caught in a spirited debate about a popular
North Korean talk show or others peering through vintage cameras, capturing the moment for posterity, a nod to their
collective love for photography. Let the image represent various socioeconomic backgrounds and pay careful attention to
individuals’ expressions, authentically displaying their shared joy, commitment, and inherent strength. Each face, unique
and expressive, counteracts stereotypes, their smiles not forced but natural, a testimony to their collective dedication and
shared missionforced but natural, a testimony to their collective dedication and shared mission”]
19
