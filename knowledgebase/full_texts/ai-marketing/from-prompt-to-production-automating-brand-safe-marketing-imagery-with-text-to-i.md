---
title: From Prompt to Production:Automating Brand-Safe Marketing Imagery with Text-to-Image Models
url: https://arxiv.org/abs/2602.13349
category: ai-marketing
subcategory: empirical
date: 2026-02
venue: ''
authors:
- Parmida Atighehchian
- Henry Wang
- Andrei Kapustin
- Boris Lerner
- Tiancheng Jiang
source: arxiv
pdf_url: https://arxiv.org/pdf/2602.13349
pages: 17
chars: 46538
fetched_at: '2026-11-08T13:11:44+00:00'
kb_version: 1
---

# From Prompt to Production:Automating Brand-Safe Marketing Imagery with Text-to-Image Models

From Prompt to Production: Automating Brand-Safe Marketing Imagery with
Text-to-Image Models
Parmida Atighehchian Henry Wang Andrei Kapustin Boris Lerner Tiancheng Jiang
Taylor Jensen Negin Sokhandan
Amazon Web Services
{patigheh, yuanhenw, kapustan, blerner, tjiangg, tdjensen, ngnsl }@amazon.com
Abstract
Text-to-image models have made signiﬁcant strides, pro-
ducing impressive results in generating images from tex-
tual descriptions. However , creating a scalable pipeline for
deploying these models in production remains a challenge.
Achieving the right balance between automation and hu-
man feedback is critical to maintain both scale and quality.
While automation can handle large volumes, human over-
sight is still an essential component to ensure that the gen-
erated images meet the desired standards and are aligned
with the creative vision. This paper presents a new pipeline
that offers a fully automated, scalable solution for gener-
ating marketing images of commercial products using text-
to-image models. The proposed system maintains the qual-
ity and ﬁdelity of images, while also introducing sufﬁcient
creative variation to adhere to marketing guidelines. By
streamlining this process, we ensure a seamless blend of ef-
ﬁciency and human oversight, achieving a 30.77% increase
in marketing object ﬁdelity using DINOV2 and a 52.00%
increase in human preference over the generated outcome.
1. Introduction
The rapid advancement of generative artiﬁcial intelligence
has transformed content creation workﬂows across indus-
tries, with marketing and advertising emerging as partic-
ularly active domains [ 10, 12]. Recent breakthroughs in
text-to-image generation models have enabled high-quality
visual creation from natural language descriptions, lead-
ing to widespread experimentation in commercial applica-
tions [4, 8, 10, 12, 13]. Despite these advances, integrating
such models into production marketing workﬂows remains
challenging, limiting their practical deployment at scale.
The transition from experimental AI-generated content
to production-ready marketing materials reveals critical
gaps in current approaches. While text-to-image models
excel at producing visually appealing content, they strug-
gle to consistently meet the stringent requirements of pro-
fessional marketing applications of a commercial product
(like a shoe), where adherence to brand guidelines, prod-
uct ﬁdelity, and scalable workﬂows is paramount. Here,
brand guidelines mean accurate representation of product-
speciﬁc features (e.g., colorways, logos, stitching). Ef-
forts to address these limitations through architectural in-
novations such as ControlNet [ 21], adapters [ 5], and IP-
Adapters [19] provide improved control but fall short of de-
livering the comprehensive solution required for enterprise
use.
We identify three fundamental challenges preventing
current generative AI systems from achieving production-
grade marketing content generation:
Alignment with brand guidelines : Marketing content
must adhere to brand speciﬁcations (e.g., colors, back-
ground features) while preserving product characteristics
without alteration. The inherent variability of generative
models can compromise brand consistency and product ac-
curacy. Control mechanisms such as ControlNet [ 21] and
ﬁne-tuning methods like AnyDoor [ 2] offer structural guid-
ance. However, they cannot guarantee the pixel-level ﬁ-
delity required for marketing campaigns, where even small
deviations can compromise brand integrity. Outpainting
models aim to maintain reference object ﬁdelity, but com-
mon failure cases include duplicating objects, hallucina-
tions (i.e. generating spurious elements), or ignoring the
object entirely.
Predictable outcome and quality consistency : A com-
mon solution for campaign creation is to incorporate out-
painting. However, seamlessly integrating products into
scenes remains challenging and varies signiﬁcantly based
on product and scene characteristics. Skilled creators can
iteratively reﬁne generations using visual heuristics, prompt
tuning, and trial and error, but creators rarely achieve qual-
ity outcomes on the ﬁrst attempt.
Scalability and workﬂow integration : Production
workﬂows demand consistent, high-throughput content
arXiv:2602.13349v1  [cs.CV]  12 Feb 2026

generation with minimal human oversight. Current ap-
proaches require repeated manual iteration, prompt engi-
neering, and quality checks, creating bottlenecks that hinder
scalability. Reliance on constant human input makes these
systems impractical for enterprise campaigns that require
hundreds of variations.
To address these challenges, we present a novel end-
to-end automated system for generating composite market-
ing images that respect brand guidelines while enabling
scalable and robust workﬂows. Our approach creates a
production-ready workﬂow by deferring human validation
to the ﬁnal stage and automating all intermediate genera-
tions and quality assessments through an agentic pipeline.
Our system introduces several key innovations: (1) a
structured prompt decomposition mechanism that converts
complex marketing requirements into machine-readable
speciﬁcations, (2) an intelligent asset retrieval system with
specialized guardrails for content types, (3) a rich caption
generator and a multi-modal composition planer that de-
termines optimal product placement and scaling, (4) a grid
search approach for marketing image variants, and (5) an
intelligent quality control pipeline that evaluates content
across multiple dimensions without human intervention. By
treating the core generation module as plug-and-play, the
system adapts to diverse industry needs at scale.
Section 3 details each pipeline module. Our experiments
show that the proposed approach achieves signiﬁcant gains
in generation quality compared to existing methods, while
maintaining strict adherence to brand guidelines and com-
position standards. The system handles diverse marketing
scenarios and provides the scalability required for enterprise
deployment.
2. Related Work
While various research efforts have explored improving
control over text-to-image generation, to our knowledge, no
prior work has proposed a scalable workﬂow with compre-
hensive testing for production-ready deployment. We there-
fore review the most relevant approaches to object com-
positing (the core component of our system), particularly
in the context of marketing applications.
2.1. Fine-tuned Object Insertion and Harmoniza-
tion
ICLight [ 22] is a diffusion-based framework for illumina-
tion harmonization and editing that operates on uncurated,
in-the-wild data. ICLight enforces light transport consis-
tency, enabling physically plausible relighting and compo-
sitional edits. However, ICLight can alter product textures
and colors, creating a challenge for brand-sensitive mar-
keting content. AnyDoor [ 2] enables zero-shot object-level
customization by teleporting a target object into a new scene
at a user-speciﬁed location without per-object ﬁne-tuning. It
balances identity preservation with local variations in light-
ing and pose. ObjectStitch [ 16] similarly performs object
insertion using conditional diffusion, with adjustments such
as geometry correction, color harmonization, and shadow
synthesis. Despite these capabilities, AnyDoor and Ob-
jectStitch struggle to maintain strict object ﬁdelity, limiting
their reliability in marketing scenarios.
2.2. Training-free Insertion
Insert Diffusion [ 6] proposes a training-free approach for
inserting objects into scenes. However, the method re-
quires manual positioning and scaling, and a second dif-
fusion pass, which can cause unwanted pixel-level manipu-
lation.
2.3. Outpainting
Inpaint Anything [ 20] introduces a modular inpainting
framework built around a “clicking and ﬁlling” paradigm:
objects can be removed, replaced, or preserved while mod-
ifying the background based on user prompts. While ﬂexi-
ble, the method relies on manual object selection, prevent-
ing full automation. More broadly, outpainting models of-
ten hallucinate artifacts near objects or replicate them un-
naturally within the scene, further complicating their use in
marketing image generation.
Overall, while prior methods advance object composit-
ing and harmonization, they fall short of generating brand-
consistent, production-ready marketing content without ex-
tensive manual reﬁnement. Section 3 details how our
pipeline overcomes these limitations through systematic
generation and artifact ﬁltering.
3. Method
We present an automated system for generating high-
quality composite marketing images from natural language
prompts. Our approach translates marketing requirements
into visually compelling product compositions via a four-
stage pipeline: structured prompt analysis, intelligent as-
set retrieval, composition planning and variation generation,
and multi-modal quality assessment.
3.1. System Overview
Given a marketing prompt such as ”Shoe on the ﬂoor on
an urban street at sunset” , the system automatically: (1)
decomposes the prompt into structured components, (2) re-
trieves relevant visual assets, (3) determines optimal com-
position parameters using a caption generator and a multi-
modal advisor, generates multiple image variations, and (4)
performs comprehensive quality ﬁltering to select the top-k
ﬁnal images. This automation minimizes manual interven-
tion while maintaining professional-grade quality (Figure
1.)

Figure 1. Overview of our pipeline. The pipeline starts with decomposing the user query. It then retrieves relevant visual assets, and
rewrites the initial prompts for optimized image generation quality. The visual assets are scaled and positioned at various positions of the
canvas to maximize generation diversity. After generation, candidate images are ﬁltered and ranked based on rubric scores and aesthetic
scores.
3.2. Structured Prompt Decomposition
Complex marketing prompts often contain multiple seman-
tic elements and implicit requirements. We address this by
converting natural language prompts into machine-readable
speciﬁcations using a large language model. Our decompo-
sition module extracts three key components: (1) primary
product - the main item being promoted, (2) background
elements - environmental context and scene descriptors, (3)
theme - the promotional context or occasion. This struc-
tured representation ensures all speciﬁed elements are con-
sidered during asset retrieval and composition planning.
The decomposition process uses few-shot prompting with
predeﬁned output schemas to maintain consistency across
diverse input formats.
3.3. Multi-modal Asset Retrieval with Guardrails
Precise asset selection is critical for composite image gen-
eration. We employ a two-tier retrieval system with special-
ized guardrails for different asset types.
3.3.1. Product Asset Retrieval
Product assets are retrieved using similarity-based dense
vector representations. Candidates are ﬁltered by a similar-
ity threshold τp = 0.39, empirically optimized to balance
precision and recall, ensuring visually and semantically ap-
propriate products.
3.3.2. Background Asset Retrieval with LLM Validation
Background selection is more complex due to subjective
scene appropriateness. While similarity scores provide an
initial ranking, they often miss nuanced contextual require-
ments. After retrieving the top- k most relevant matches,
we employ an LLM-based validation step that evaluates se-
mantic alignment between each candidate background Bi
and promptP :
R(Bi,P ) = LLMvalidator(Bi,P )∈ 0, 1 (1)
This step ensures robust selection by considering con-
text, theme, and visual compatibility.
3.4. Caption Generator
The caption generator is an LLM agent prompted to pro-
duce descriptive captions that guide image generation and
composition planning. It considers the background, pri-
mary product, and theme to emphasize the product while
positioning other elements appropriately. If a relevant back-
ground is found, the caption generator uses the image to
enrich the text with additional visual features. Otherwise,
it relies on the user query. This caption not only is used
for image generation but also plays an important role in the
composition planning stage.

3.5. Intelligent Composition Planning
Our composition module determines optimal object place-
ment, scaling, and spatial relationships using multi-modal
analysis and grid search.
3.5.1. Multi-modal Composition Analysis
A critical design decision is the ability to continue with the
image generation even if a background match is not found.
Using either an empty canvas or a resized background, the
multi-modal advisor leverages the generated caption to rec-
ommend scaling factors for the product in the scene:
Given a background-ﬁlled or an empty canvas C, the
product object O, and the generated caption Ca our com-
position advisor analyzes both visual and textual elements
to determine optimal scaling factors:
S ={sw,s h} =fadvisor(C,O,Ca ) (2)
wheresw andsh represent the recommended width and
height scaling factors relative to the canvas dimensions.
3.5.2. Variation Generation Strategy
To maximize creative diversity, products are systematically
placed across canvas regions (left, center, right thirds) with
rotation anglesθ∈{ 0◦, 15◦, 345◦}. This ensures broad ex-
ploration of the composition space while maintaining visual
coherence.
3.5.3. Scene Generation
For marketing campaign generation, maintaining product ﬁ-
delity is crucial. Our scene generation module is designed
as a plug-and-play component that works with any image
generation model accepting reference images and captions.
For marketing applications, the generative model must pre-
serve product ﬁdelity while properly integrating objects into
scenes. Given these base performance requirements, any
outpainting, insertion and harmonization, or object compo-
sition model is suitable.
This module takes a product-on-canvas composition and
extend the background while preserving visual integrity.
Although the original background cannot be maintained,
our feature-rich caption generation injects key background
characteristics back into the scene, enabling better product
composition. This approach ensures seamless product inte-
gration with realistic lighting and perspective relationships.
The image variants encourage the model to sample di-
versely from its learned latent space. This systematic ex-
ploration of the latent space increases the probability of
generating high-quality marketing images by leveraging the
model’s full generative capacity.
3.6. Multi-Stage Quality Control Pipeline
Quality assessment evaluates semantic accuracy, visual re-
alism, and aesthetic appeal. Our pipeline combines rule-
based validation with learned metrics and is fully customiz-
able for different use cases.
3.6.1. Multi-modal Quality Controller
Our primary quality ﬁlter employs a multi-modal Large
Language Model that evaluates generated images across
four primary critical dimensions:
1. Caption Alignment: V eriﬁcation that all elements spec-
iﬁed in the prompt are accurately depicted in the gener-
ated image.
2. Product Uniqueness: Conﬁrmation that the scene con-
tains exactly one instance of the product—a safeguard
against common model hallucinations (e.g., unintended
duplicates)
3. Physical Realism: Assessment of object placement con-
sistency with real-world physics and spatial relation-
ships.
4. Lighting Consistency: Evaluation of shadow and reﬂec-
tion accuracy relative to the scene’s lighting conditions.
Each criterion receives a binary score ci ∈ {0, 1}. In
most production setups, the overall score is computed as
below:
G =
4∏
i=1
ci (3)
This multiplicative formulation ensures that images failing
any critical criterion are ﬁltered out, maintaining high qual-
ity standards. Where data is sufﬁcient, we recommend us-
ing a weighted average, where the weights are optimized to
the use case in hand. In Section 4, we use a hierarchical
approach to relax the less critical guardrails for our setup.
Since the generative model is probabilistic, this component
is a way to trigger a retry if necessary in a production setup
and have a safe fall back.
3.6.2. Aesthetic and Semantic Quality Assessment
For critical applications such as marketing image creation,
we recommend maintaining human oversight while mini-
mizing intervention to enable scalable deployment. To fa-
cilitate scaling, the number of ﬁnal images presented for
human review is conﬁgurable through a hyperparameter k.
When more thank candidates pass the guardrail evaluation,
they undergo additional quality assessment using comple-
mentary metrics:
Aesthetic Scoring : We employ a pre-trained aesthetic
quality model [ 14] that processes CLIP [ 9] visual features
to predict aesthetic scores. Images below the set aesthetic
threshold are ﬁltered out.
CLIP-based Semantic Alignment: We optionally mea-
sure text-image alignment using CLIP similarity between
generated images and prompt descriptions as an additional
ﬁlter. The CLIP [ 9] score is computed as:

CLIP(I,T ) = w· max(0, cos(ϕ(I),ψ (T ))) (4)
whereϕ(I) andψ(T ) are the CLIP encodings of image
I and textT , respectively, andw = 2.5 is a scaling factor.
To reduce the cost overhead and latency, we chose to
incorporate metrics that need minimal computation power.
However, each of the modules are fully customizable and
can be adapted to different sets of requirements.
3.6.3. Combined Quality Ranking
Final image ranking combines aesthetic and semantic qual-
ity scores:
Qﬁnal =α·Qaesthetic +β·QCLIP (5)
where α and β are weighting parameters that can be
adjusted based on application requirements. This multi-
faceted approach ensures that selected images excel across
both perceptual quality and semantic accuracy dimensions.
The complete pipeline processes multiple image vari-
ations and returns only those meeting all quality criteria,
ranked by their combined quality scores.
4. Experiments
4.1. Baseline
We select baseline candidates based on their ability to per-
form outpainting and harmonization using reference images
and prompts. Below is the list of our selected candidates:
• ICLight [22]: ICLight represents state-of-the-art object-
scene compositing with specialized ﬁne-tuning for light-
ing and shadow adjustment. Unlike standard outpaint-
ing models that focus solely on semantic alignment,
ICLight’s illumination capabilities enable more natural
product integration.
• Inpaint Anything [ 20]: Replace Anything module from
the Inpaint Anything framework segments the object of
interest from the background. It then replaces the back-
ground with a text-guided inpainting model. This model
requires an input to select the object for segmentation (a
“clicking and ﬁlling” paradigm). In our image variants,
the object location is determined. We use this prior place-
ment knowledge to automate the object selection.
• Amazon Nova Canvas [ 1]: Nova Canvas receives the
product on an empty canvas. Additionally, it has capabil-
ities to accept a mask image or a mask prompt to mask
out the product and perform text guided outpainting on
the scene. For simplicity, we use the mask-prompt in our
experiments.
We compare our approach to these baselines along two
verticals critical to our application domain: (1) Product Fi-
delity and (2) Scene Integration.
4.2. Data
We use the Amazon-Berkeley Objects (ABO) dataset [ 3]
as the primary source for product images. The ABO
dataset contains high-quality, multi-view images of real-
world products across diverse categories with annotations.
These product images are clean and have a white back-
ground which eliminates the need for any preprocessing.
We select 21 distinct categories, ranging from clothing and
accessories to household items to cover a diverse range of
items. We sample a minimum of 10 images per category
if there are a sufﬁcient number of images to sample from.
If the number of images in a category is less than 10, we
include all of them in our test dataset. Our ﬁnal sampled
dataset consists of 206 images representing 21 different cat-
egories.
To further increase our test sample size, we send each
product type to a Visual Language Model (VLM) and ask
the model to generate 5 rich, diverse and creative captions
for scenes that the product can ﬁt in. With 5 captions per
product, we have a total of 1030 product-caption pairs for
our experiments.
4.3. Experiment setup
We evaluate all three baselines on the same set of 1,030
product–caption pairs. Each method requires a mask im-
age specifying product placement. In real-world work-
ﬂows, designers typically adjust product position and ro-
tation through repeated trials until a visually coherent result
is achieved. Our pipeline automates this process by placing
the product at multiple positions and rotations on an empty
canvas, enabling the model to generate diverse variations in
a single batch. This increases the likelihood of obtaining a
high-quality composition without manual intervention.
To ensure fair comparison, we restrict each baseline to a
single ﬁxed placement–rotation conﬁguration, which repre-
sents a non-automated workﬂow where no iterative adjust-
ment is performed. By contrasting one-shot baseline out-
puts with our multi-variation pipeline, we directly test the
contribution of automated variation generation.
For pipeline evaluation, we initialize from ground-truth
product–caption pairs, bypassing retrieval and captioning,
and begin at the composition stage. The setup follows Sec-
tion 3.5, using an empty canvas. The ﬁnal pipeline outputs
are selected through our quality assessment module. In this
experiment, we follow algorithm 1 to progressively relax
the lower-priority rules if needed, while keeping rules 2 and
3 strict (see Section 3.6 for the list of rules).
Figure 2 shows a comparison of our pipeline generated
images against the baseline models’ generations (additional
results can be found in Supplementary Material section 1.1,
Figures 1, 2, and 3).

Algorithm 1 Find images aligned with guidelines.
1: Input: A list of lists containing 4 binary scores
2: Output: A list of image indices matching the one of
the best pattern, or∅
3: patterns← [[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 0]]
4: for eachpattern inpatterns do
5: indices←{i|scores[i] = pattern}
6: ifindices̸=∅ then
7: returnindices
8: end if
9: end for
10: return∅
4.4. Quantitative Results
We use the following metrics to evaluate performance
across the three key axes:
• Product Fidelity: We use DINOv2 [ 7] features and MS-
SSIM [ 17] to evaluate how well the original product is
preserved in the generated image. To do so, one needs
to isolate the generated product from the scene. We ac-
complish this by using Amazon Nova Pro [ 1] as an im-
age analyzer agent to predict bounding box coordinates
around the product, which are then passed with the im-
age to SAM2 [ 11] for segmentation. We then compare
the extracted object with the ground-truth product using
the cosine similarity of DINOv2 features and calculated
MS-SSIM values. DINOv2 similarity score captures both
semantic and ﬁne-grained visual similarities, while MS-
SSIM provides a strong signal of structural ﬁdelity, de-
tecting distortions or visual degradation. Combined, these
two metrics offer a robust measure of product ﬁdelity in
the generated scenes.
• Overall text to image alignment : We compute the
HPSv2 [ 18] to measure the overall quality of the image
and alignment with text. While not a direct measure of
quality for images, HPSv2 correlates strongly with hu-
man visual preference.
Tables 1 report results for each baseline and their integra-
tion into our pipeline. Across all models, our pipeline con-
sistently improves both structural similarity and DINOv2
scores, supporting our claim that object size and placement
play a critical role in outpainting quality. Although we ob-
serve a slight drop in HPSv2 for ICLight, our human evalua-
tion indicates a strong preference for pipeline-generated im-
ages. This drop is partly explained by our pipeline’s design:
when no images pass the quality check, the output defaults
to a score of 0. This effect is more pronounced in mod-
els like ICLight, where the baseline often alters an object’s
texture or color. In such cases, the baseline still receives
a score for its output, even if it deviates from ﬁdelity re-
quirements, while the pipeline registers no result (see Lim-
itations 4.6). Consequently, more test cases yield zero out-
puts on the pipeline side, lowering the average HPSv2. In
contrast, we observe a slight improvement in HPSv2 for Re-
place Anything. This improvement stems from selecting
more effective product placement and rotation, which en-
ables better integration. The baseline Replace Anything fre-
quently hallucinates around products, whereas our pipeline
mitigates this by providing stronger initialization.
4.5. Qualitative Evaluation
Evaluating image quality remains a challenging task. While
numerous metrics exist, each captures only limited aspects,
and none adequately assess whether an object is convinc-
ingly integrated into a scene—critical for inpainting and
outpainting. Consequently, we rely on qualitative evalu-
ation through a user study. We employ Amazon Ground
Truth Labeling Service [ 15] to compare images generated
by the baseline model and our pipeline.
We randomly sample 50 generation pairs per model,
shufﬂe them, and collect responses from ﬁve annotators per
pair. For each task, the annotators are shown a caption, the
original product image, and two generated images depicting
the product within the described scene. They are instructed
to choose the best generated outcome according to the fol-
lowing criteria (in order of importance):
Carefully read the provided caption and look at the pro-
vided reference image for the product. Compare the two
generated images and select the one that matches the below
criteria best. The requirements are listed in the order of im-
portance. Make sure to move down to the next requirement
only if both of the images have equivalent performance on
the current requirement.
1. Integration of product in the scene
2. Maintaining product look and ﬁdelity
3. Alignment with caption: The generated image clearly
demonstrates the elements described in the caption and
their relative positions in the scene.
Since our pipeline has a strict quality assessment mod-
ule, there exist cases where none of the generated images
passed our agentic quality assessment. During sampling im-
age pairs, if we sample a rare case like this, we take a note
and consider an extra win for the baseline model when the
preference rate based on annotations is calculated.
As shown in Figure 3, the results for three of our test
models show a clear preference of the pipeline over the
baseline run of the models.
In summary, our numerical metrics show a consistent
improvement of the pipeline compared to the base model
in maintaining product’s integrity and our human evalua-
tion results further show that when choosing a proper base
model for the task in hand, pipeline can signiﬁcantly help
the model to generate more quality images.

Table 1. Comparison of metrics across three models with and without the proposed pipeline. V alues are mean ± std.
IClight Nova Canvas Replace Anything
Metric Baseline Pipeline (ours) Baseline Pipeline (ours) Baseline Pipeline (ours)
hpsv2 0.240 ± 0.024 0 .231 ± 0.063 0 .232 ± 0.030 0 .233 ± 0.024 0 .213 ± 0.036 0.221 ± 0.027
ms ssim 0.239 ± 0.210 0.282 ± 0.179∗ 0.382 ± 0.269 0.422 ± 0.219∗ 0.289 ± 0.228 0.334 ± 0.103∗
dinov2 0.401 ± 0.282 0.589 ± 0.274∗ 0.645 ± 0.213 0.781 ± 0.185∗ 0.538 ± 0.235 0.669 ± 0.196∗
Note. ∗ Statistically signiﬁcant improvement over baseline ( p < 0.05, paired t-test).
Reference
(image)
Nova
Baseline vs Pipeline
ICLight
Baseline vs Pipeline
Replace Anything
Baseline vs Pipeline
Baseline
Pipeline
Baseline
Pipeline
Baseline
Pipeline
Prompt: Low angle view of luggage positioned on a busy city sidewalk with towering skyscrapers and bustling pedestrians in the background; dramatic
evening light from street lamps casting long shadows.
Baseline
Pipeline
Baseline
Pipeline
Baseline
Pipeline
Prompt: Low-angle view of a sofa in a contemporary ofﬁce with glass walls and polished concrete ﬂoors, under bright ﬂuorescent overhead lighting.
Figure 2. Baseline vs. pipeline outputs across three models for multiple product references. Prompts span the full width below each image
row.
4.6. Limitations
We identify two primary sources of failure in our pipeline:
dataset limitations and base model limitations.
4.6.1. Dataset Limitations
The ABO dataset contains a small number of mis-labeled
product images. Although infrequent, these errors can con-
fuse the generation process and lead to nondeterministic

Figure 3. Preference rates for Baseline (light blue) vs. Pipeline
(dark blue) across different models.
outputs (see Supplementary Material, Section 1.2, Figures
7, 8, and 9).
4.6.2. Base Model Limitations
The majority of failure cases stem from the underlying gen-
erative models. First, such models often hallucinate by gen-
erating spurious element around the masked region. In our
set of baseline models we observe this failure case mostly
in the outcomes of Replace Anything (see Supplementary
Material, Section 1.2, Figure 4). Our placement strategy re-
duces - but does not eliminate - this effect, and when the
base model fails, the pipeline inherits these errors.
Second, when the reference product appears relatively
too small in the scene, models tend to ignore the object en-
tirely. The model in this case might generate a different
instance of the product, or omit it altogether. Our current
quality module detects the latter case (rule number 2 in Sec-
tion 3.6) but does not explicitly check for product similar-
ity to balance cost and latency. Repeated cases of this error
type would require the integrating of an object ﬁdelity test
into the Quality Control Module (see Supplementary Mate-
rial, Section 1.2, Figures 5, and 6).
Finally, individual base models exhibit their own quirks.
For example, despite being trained to preserve object fea-
tures, our experiments reveal pixel-level changes to prod-
ucts when using ICLight as the image generator. Partic-
ularly, ICLight often alters product texture or color when
adjusting illumination. Since such behaviors are model-
speciﬁc, we recommend testing the base model on a small
subset of data to surface recurring issues and adjusting the
quality checks accordingly (see Supplementary Material,
Section 1.2, Figure 10).
5. Conclusion and Future Work
In this paper, we introduce a modular pipeline for scal-
able generation of marketing images. Although tailored to
marketing, the design is highly customizable and can be
adapted to a wide range of content-creation tasks that fol-
low visual guidelines. By automating the iterative genera-
tion process and enforcing quality through guardrail checks,
our approach reduces the need for constant human over-
sight. Instead, human effort is focused where it is most
valuable—making ﬁnal selections from images that already
satisfy predeﬁned criteria. While our current system fo-
cuses primarily on maintaining product integrity and visual
composition, brands often require adherence to strict and di-
verse guidelines such as color palettes, copy style, and lay-
out constraints. Future work includes extending the pipeline
to automatically incorporate these brand-speciﬁc rules, en-
abling more comprehensive compliance and further stream-
lining large-scale production workﬂows. We view this work
as a step toward the productionization of image generation,
enabling deployment at scale and addressing real industry
needs.
References
[1] Amazon. Amazon nova: Foundation models for general in-
telligence. https://aws.amazon.com/nova/, 2025.
5, 6
[2] Xi Chen, Lianghua Huang, Y u Liu, Y ujun Shen, Deli Zhao,
and Hengshuang Zhao. Anydoor: Zero-shot object-level im-
age customization, 2024. 1, 2
[3] Jasmine Collins, Shubham Goel, Kenan Deng, Achlesh-
war Luthra, Leon Xu, Erhan Gundogdu, Xi Zhang, Tomas
F Y ago Vicente, Thomas Dideriksen, Himanshu Arora, et al.
Abo: Dataset and benchmarks for real-world 3d object un-
derstanding. In Proceedings of the IEEE/CVF conference
on computer vision and pattern recognition , pages 21126–
21136, 2022. 5
[4] Black Forest Labs. Flux. https://github.com/
black-forest-labs/flux , 2024. 1
[5] Chong Mou, Xintao Wang, Liangbin Xie, Y anze Wu, Jian
Zhang, Zhongang Qi, Ying Shan, and Xiaohu Qie. T2i-
adapter: Learning adapters to dig out more controllable abil-
ity for text-to-image diffusion models, 2023. 1
[6] Phillip Mueller, Jannik Wiese, Ioan Craciun, and Lars Mikel-
sons. Insertdiffusion: Identity preserving visualization of ob-
jects through a training-free diffusion architecture, 2024. 2
[7] Maxime Oquab, Timoth ´ee Darcet, Th ´eo Moutakanni, Huy
V o, Marc Szafraniec, V asil Khalidov, Pierre Fernandez,
Daniel Haziza, Francisco Massa, Alaaeldin El-Nouby, et al.
Dinov2: Learning robust visual features without supervision.
arXiv preprint arXiv:2304.07193, 2023. 6
[8] Dustin Podell, Zion English, Kyle Lacey, Andreas
Blattmann, Tim Dockhorn, Jonas M ¨uller, Joe Penna, and
Robin Rombach. Sdxl: Improving latent diffusion mod-
els for high-resolution image synthesis. arXiv preprint
arXiv:2307.01952, 2023. 1
[9] Alec Radford, Jong Wook Kim, Chris Xu, Greg Brockman,
Patrick McLeavey, and Ilya Sutskever. Learning transferable
visual models from natural language supervision. In Inter-
national Conference on Machine Learning (ICML) , 2021. 4

[10] Aditya Ramesh, Prafulla Dhariwal, Alex Nichol, Casey Chu,
and Mark Chen. Hierarchical text-conditional image gener-
ation with clip latents, 2022. 1
[11] Nikhila Ravi, V alentin Gabeur, Y uan-Ting Hu, Ronghang
Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman
R¨adle, Chloe Rolland, Laura Gustafson, et al. Sam 2:
Segment anything in images and videos. arXiv preprint
arXiv:2408.00714, 2024. 6
[12] Robin Rombach, Andreas Blattmann, Dominik Lorenz,
Patrick Esser, and Bj ¨orn Ommer. High-resolution image
synthesis with latent diffusion models. In Proceedings of
the IEEE/CVF conference on computer vision and pattern
recognition, pages 10684–10695, 2022. 1
[13] Chitwan Saharia, William Chan, Saurabh Saxena, Lala
Li, Jay Whang, Emily Denton, Seyed Kamyar Seyed
Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi,
Rapha Gontijo Lopes, Tim Salimans, Jonathan Ho, David J
Fleet, and Mohammad Norouzi. Photorealistic text-to-image
diffusion models with deep language understanding, 2022. 1
[14] christoph schuhmann. improved-aesthetic-predictor public.
https : / / github . com / christophschuhmann /
improved-aesthetic-predictor , 2023. 4
[15] Amazon Web Services. Amazon sagemaker ground
truth. https://aws.amazon.com /sagemaker/
groundtruth/, 2024. 6
[16] Yizhi Song, Zhifei Zhang, Zhe Lin, Scott Cohen, Brian Price,
Jianming Zhang, Soo Y e Kim, and Daniel Aliaga. Object-
stitch: Generative object compositing, 2022. 2
[17] Z. Wang, E.P . Simoncelli, and A.C. Bovik. Multiscale struc-
tural similarity for image quality assessment. In The Thrity-
Seventh Asilomar Conference on Signals, Systems & Com-
puters, 2003, pages 1398–1402 V ol.2, 2003. 6
[18] Xiaoshi Wu, Yiming Hao, Keqiang Sun, Yixiong Chen, Feng
Zhu, Rui Zhao, and Hongsheng Li. Human preference score
v2: A solid benchmark for evaluating human preferences of
text-to-image synthesis. arXiv preprint arXiv:2306.09341 ,
2023. 6
[19] Hu Y e, Jun Zhang, Sibo Liu, Xiao Han, and Wei Y ang. Ip-
adapter: Text compatible image prompt adapter for text-to-
image diffusion models, 2023. 1
[20] Tao Y u, Runseng Feng, Ruoyu Feng, Jinming Liu, Xin Jin,
Wenjun Zeng, and Zhibo Chen. Inpaint anything: Segment
anything meets image inpainting, 2023. 2, 5
[21] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Adding
conditional control to text-to-image diffusion models, 2023.
1
[22] Lvmin Zhang, Anyi Rao, and Maneesh Agrawala. Scal-
ing in-the-wild training for diffusion-based illumination har-
monization and editing by imposing consistent light trans-
port. In The Thirteenth International Conference on Learn-
ing Representations, 2025. 2, 5

1 Supplementary Material
1.1 Additional success examples from the Pipeline
Reference
(image + prompt)
Baseline Pipeline
Prompt: Wide-angle view of a bag positioned on a moss-covered fallen l og in a dense forest clearing surrounded by towering
pine trees and scattered wildﬂowers, soft diﬀused natural l ight ﬁltering through the canopy above.
Prompt: Low-angle perspective of a drinking cup sitting on sandy bea ch dunes with ocean waves and seashells visible in the
distance, golden hour sunlight casting long dramatic shado ws across the scene.
Prompt: Medium shot of a table positioned in a sleek modern oﬃce space with glass walls, minimalist decor, and polished
marble ﬂoors, illuminated by clean white ﬂuorescent lighti ng and natural daylight, professional photo
Figure 1: Additional success cases where pipeline improves generate d image output quality for ICLight. Left:
reference. Middle/Right: generated images from baseline and pipelin e
1

Reference
(image + prompt)
Baseline Pipeline
Prompt: Close-up shot of a broom leaning against white kitchen cabin ets in a modern home interior, ceramic tiles reﬂecting
soft morning sunlight streaming through nearby windows, ph oto
Prompt: Medium shot of a chair sitting on pristine white sand at a trop ical beach with crystal clear turquoise water, swaying
palm trees in the background, and bright midday sunlight cre ating sharp contrasts and vibrant colors in this paradisiac al coastal
scene.
Prompt: Close-up shot of a hat resting on weathered cobblestones in a bustling city street with vintage brick buildings and
iron lampposts in the background, warm golden hour sunlight casting long shadows across the urban scene, professional s treet
photography style
Prompt: Medium shot of a microphone positioned on a wooden desk in a co zy home oﬃce setup with bookshelves, houseplants,
and a laptop computer nearby, soft natural daylight streami ng through a nearby window creating gentle shadows and a warm ,
inviting atmosphere for podcasting.
Figure 2: Additional success cases where pipeline improves generate d image output quality for Nova Canvas.
Left: reference. Middle/Right: generated images from baseline and pip eline
2

Reference
(image + prompt)
Baseline Pipeline
Prompt: Close-up shot of a bag resting on weathered cobblestones in a bustling European marketplace with vendors and colorful
awnings creating a vibrant backdrop, warm golden hour sunli ght casting long shadows across the ancient stone surface.”
Prompt: Close-up shot of a hat resting on weathered cobblestones in a bustling city street with vintage brick buildings and
iron lampposts in the background, warm golden hour sunlight casting long shadows across the urban scene, professional s treet
photography style
Prompt: Close-up angled shot of a chair positioned in a cozy library c orner surrounded by towering bookshelves ﬁlled with
leather-bound volumes, a vintage Persian rug beneath, and w arm amber lighting from antique brass lamps creating an inti mate
scholarly atmosphere.
Figure 3: Additional success cases where pipeline improves generate d image output quality for Replace
Anything. Left: reference. Middle/Right: generated images from baseli ne and pipeline
3

1.2 Failure Cases
Figure 4 illustrates Replace Anything’s tendency to hallucinate sp urious objects, likely from over-compensation
for prompt alignment and scene integration. Figures 5 and 6 show cases whe re the reference object is ig-
nored—a common failure in outpainting/harmonization models that we did not ob serve with Nova Canvas in
our experiments. Figures 7a, 7b, and 8 depict failures caused by misali gnment between the ABO category la-
bel and the product image; because our captions use the label as the prod uct reference, this mismatch creates
ambiguity. The models outcome in this case is unpredictable. Outpai nting models (Nova Canvas, Replace
Anything) often retain the reference image while also inserting a cat egory-consistent instance or, as in the
cup example, produce a semantic compromise. ICLight-being ﬁne-tu ned for harmonization—frequently dis-
cards the reference entirely. Finally, Figure 9 shows an ICLight-s peciﬁc failure in which objects are recolored
to match the scene’s palette.
Reference
(image + prompt)
Baseline Pipeline
Prompt: Medium shot of a chair sitting on pristine white sand at a trop ical beach with crystal clear turquoise water, swaying
palm trees in the background, and bright midday sunlight cre ating sharp contrasts and vibrant colors in this paradisiac al coastal
scene
Prompt: Wide-angle view of a landline phone positioned on a red vinyl b ooth table inside a retro American diner with checkered
ﬂoor tiles, chrome ﬁxtures, and neon signs glowing in the bac kground, bright ﬂuorescent lighting casting even illumina tion
throughout the space.
Prompt: Close-up shot of shoes resting on weathered concrete paveme nt in a bustling urban street with blurred city buildings
and storefronts in the background, warm golden hour sunligh t casting long shadows across the sidewalk, photo
Figure 4: Failure cases for Replace Anything - hallucination. Left: refe rence. Middle/Right: generated
images from baseline and pipeline
4

Reference
(image + prompt)
Baseline Pipeline
Prompt: Low-angle perspective of a broom resting against weathered brick wall in narrow urban alleyway, dramatic evening
light from street lamp casting long shadows across wet pavem ent, photo
Prompt: Low-angle photograph of wine bottle partially buried in whi te sand dunes with desert landscape and distant mountains
visible on the horizon under bright midday sun creating dram atic shadows and harsh contrasts.
Figure 5: Failure cases for Replace Anything - Object Ignored. Left: ref erence. Middle/Right: generated
images from baseline and pipeline. In the above cases the model generat ed another instance of the object.
Reference
(image + prompt)
Baseline Pipeline
Prompt: Close-up shot of a broom leaning against white kitchen cabin ets in a modern home interior, ceramic tiles reﬂecting
soft morning sunlight streaming through nearby windows, ph oto
Prompt: Wide-angle view of a toaster positioned on a wooden picnic tab le in a mountain campsite with pine trees and tents
visible in the background, bright natural daylight illumin ating the outdoor breakfast setup.
Figure 6: Failure cases for ICLight - Object Ignored. Left: reference. M iddle/Right: generated images from
baseline and pipeline. In the ﬁrst case the baseline completely ign ored the reference image while the pipeline
version generated another instance. In the second case, the toaster is ﬂ oating in the air in the baseline image
and is completely ignored in the pipeline generated image.
5

Reference
(image + prompt)
Baseline Pipeline
Prompt: Medium shot of luggage resting on sandy beach with palm trees swaying and turquoise ocean waves in background,
bright tropical sunlight creating vibrant colors and gentl e shadows on white sand, photo
Prompt: Overhead shot of a drinking cup placed on a rustic wooden tabl e in a cozy cafe setting with pastries and newspapers
scattered around, warm ambient lighting from vintage penda nt lamps.
(a) Failure cases for ICLight - Product Mismatch. Left: reference. M iddle/Right: generated images from baseline
and pipeline. The ﬁrst example shows a bag labeled as “Luggage ” in the ABO dataset. The baseline completely
disregards the reference image. In the second row, a stack of cups la beled as “Drinking Cup” confuses the model,
leading both the baseline and the pipeline to ignore the provid ed image reference.
Reference
(image + prompt)
Baseline Pipeline
Prompt: Medium shot of luggage resting on sandy beach with palm trees swaying and turquoise ocean waves in background,
bright tropical sunlight creating vibrant colors and gentl e shadows on white sand, photo
Prompt: Eye-level photograph of a drinking cup positioned on a sleek glass desk in a modern oﬃce space with computer
monitors and oﬃce supplies nearby, bright ﬂuorescent light ing creating clean reﬂections.
(b) Failure cases for Nova Canvas - Product Mismatch. Left: referenc e. Middle/Right: generated images from
baseline and pipeline. In the ﬁrst row, the bag is labeled as “Lu ggage” in the ABO dataset. The baseline image
shows the model generating a generic piece of luggage, reﬂectin g confusion from the label. In the second row, a
stack of reusable cups labeled as “Drinking Cup” results in the mo del generating coﬀee cups, capturing only a loose
semantic resemblance to the reference image.
6

Reference
(image + prompt)
Baseline Pipeline
Prompt: Medium shot of luggage resting on sandy beach with palm trees swaying and turquoise ocean waves in background,
bright tropical sunlight creating vibrant colors and gentl e shadows on white sand, photo
Prompt: Overhead shot of a drinking cup placed on a rustic wooden tabl e in a cozy cafe setting with pastries and newspapers
scattered around, warm ambient lighting from vintage penda nt lamps.
Figure 8: Failure cases for Replace Anything - Product Mismatch. Left: reference. Middle/Right: gener-
ated images from baseline and pipeline. In the ﬁrst row, label confusi on causes both methods to generate
additional luggage around the reference image. In the second row, while th e stack of cups is preserved in
the baseline, the model inserts an extra cup on the table, and the pi peline produces a paper cup instead..
7

Reference
(image + prompt)
Baseline Pipeline
Prompt: Bird’s eye view of a chair placed on a concrete urban rooftop t errace overlooking a bustling cityscape with skyscrapers,
busy streets below, and potted plants around the edges, illu minated by dramatic sunset lighting casting long shadows ac ross
the industrial setting.
Prompt: Medium shot of luggage resting on sandy beach with palm trees swaying and turquoise ocean waves in background,
bright tropical sunlight creating vibrant colors and gentl e shadows on white sand, photo
Prompt: Overhead shot of shoes placed on polished white marble ﬂoor i n a minimalist modern interior with clean geometric
lines, sleek furniture, and bright even lighting from reces sed ceiling ﬁxtures, photo
Figure 9: Failure cases for ICLight - Color Change. Left: reference. Middl e/Right: generated images from
baseline and pipeline.
8
