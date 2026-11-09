---
title: Enabling and Understanding Personalization in AI-Generated Advertising Imagery
url: https://arxiv.org/abs/2609.12697
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Victor Kolominsky-Rabas
- Leopold Müller
- Claudius Budcke
- Claas Christian Germelmann
- Niklas Kühl
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.12697
pages: 22
chars: 86003
fetched_at: '2026-11-08T13:20:30+00:00'
kb_version: 1
---

# Enabling and Understanding Personalization in AI-Generated Advertising Imagery

ENABLING ANDUNDERSTANDINGPERSONALIZATION IN
AI-GENERATEDADVERTISINGIMAGERY
PREPRINT
Victor Kolominsky-Rabas*1,2, Leopold Müller1,2, Claudius Budcke1,
Claas Christian Germelmann1, and Niklas Kühl1,2
1University of Bayreuth, Universitätsstraße 30, 95447 Bayreuth, Germany
2Fraunhofer FIT, Wittelsbacherring 10, 95444 Bayreuth, Germany
ABSTRACT
Personalized marketing traditionally matches static products to customers, while dynamic creative op-
timization focuses mainly on AI-driven text personalization or basic product image modifications. We
address this gap by developing and implementing an AI-based framework that generates personalized
advertising imagery directly from customer data. We evaluate this framework in a two-stage within-
subject study with N= 100 participants across four products and three levels of personalization,
varied by the amount and specificity of customer data used. Participants rated each image on attitude
toward the advertisement, attitude toward the product, and purchase intention. Results show that
participants perceive differences across personalization levels and evaluate AI-generated advertising
imagery most positively at a moderate level of personalization. High personalization increases
perceived personalization, which is positively associated with all three outcome measures, but also
increases perceived creepiness, which is negatively associated with the outcomes and dominates the
total effect.
Keywordsgenerative artificial intelligence·online advertising·personalization
1 Introduction
Traditional digital personalized marketing uses customer data to optimize a single parameter: the match between a static
product and a specific customer [20, 66, 67]. However, generative artificial intelligence (GenAI) introduces a second
parameter, allowing the product’s presentation to be dynamically generated for the viewer. If a customer who loves
cycling but is not an environmentalist is in the market for a new electric vehicle, artificial intelligence (AI) can adapt
the marketing material for the vehicle as a “sports-utility tool” rather than an “eco-friendly car”. This shift in focus
is enabled by the immense capabilities of modern GenAI systems. They have reopened the possibility of one-to-one
communication—but at an unprecedented scale. For the first time, digital advertisements can be tailored not only to a
segment but to the fine-grained details of a single individual.
Personalization is a powerful lever in digital marketing because it increases relevance, engagement, and profitability [20].
Yet most personalization to date has focused on recommendation systems—that is, delivering an advertisement
the customer is likely to be interested in—rather than tailoring the advertisement’s content itself to the individual
customer [82]. The actual content of advertisements has typically been tailored only to broad market segments, while
more granular tailoring has been constrained by the high costs of producing conventional marketing materials.
Literature shows that dynamic creative optimization (DCO) enables scalable personalization of advertising content by
recombining predefined assets in real time [6, 54], but it is limited to adjustable elements or small sets of preset images.
Recent advances in message personalization demonstrate that large language models (LLMs) can generate persuasive,
psychologically tailored text at scale [60]. Related work shows that GenAI-based personalized video advertisements can
increase engagement compared with personalized image ads and generic non-personalized video ads [45]. However, this
work focuses on personalized video messages based on purchase histories and click engagement, rather than on fully
∗victor.kolominsky-rabas@fit.fraunhofer.de
arXiv:2609.12697v1  [cs.AI]  11 Sep 2026

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
AI-generated advertising imagery, real customer profiles, and different depths of visual personalization. For advertising
imagery, research remains narrow. A few studies generate advertising imagery, but most rely on inpainting that modifies
backgrounds around a fixed product image [24, 89] rather than creating new scenes in which the product is embedded
and set in context. Research on synthetic advertising has highlighted that AI-based manipulation and generation
technologies, such as deepfakes and generative adversarial networks, can create advertising content automatically
and may enable new forms of hyperpersonalization [18]. Moreover, emerging empirical work has begun to examine
how customers respond to AI-generated advertisements, for example in the context of disclosure and luxury-brand
authenticity [85], while broader marketplace-level research shows that GenAI affects the production, consumption,
and substitution of creative goods such as stock imagery [34]. However, these studies do not investigate how GenAI
can be used to personalize advertising imagery from real individual customer data, nor how different levels of such
personalization affect marketing outcomes. To date, no study has systematically examined the use of GenAI for creating
personalized advertising imagery, based on real customer data, or varied the level of personalization. It is unclear a)
how such personalization would be implemented on a technical level and b) whether such personalization is beneficial
for marketing purposes. To address this, we derive two research questions:
RQ1How can we design a technical framework providing AI-generated personalized advertising imagery?
RQ2 How does the level of personalization in AI-generated advertising imagery influence attitude toward the
advertisement, attitude toward the product and purchase intention?
Figure 1 provides an overview of our research design across the process of AI-generated personalized advertising
imagery, linking the technical framework (RQ1) to the empirical evaluation of attitude toward the advertisement
(ATA), attitude toward the product (ATP) and purchase intention (PI) at different levels of personalization (RQ2). To
answer RQ1, we examine current manual workflows for creating traditional advertising imagery. Inspired by this, we
develop a technical framework for AI-generated personalized advertising imagery and implement it combining a widely
accessible, state-of-the-art LLM with a text-to-image (T2I) generator. Personalization is implemented across three levels
(L0–L2) that range from a non-personalized baseline to hyperpersonalized outputs—realized by varying the amount and
specificity of customer data fed into the framework. To address RQ2, we develop three hypotheses: H1 tests whether
personalization affects ATA, ATP and PI across L0–L2, H2 tests improvements relative to the non-personalized baseline,
and H3 tests for an inverted-U relationship in which moderate personalization is most effective while excessive tailoring
reduces effectiveness. We conduct a two-stage study (consisting of survey 1 and survey 2) with a within-subjects design
of N= 100 participants using four exemplary products. Survey 1 collects real participant data used as input for the
implemented framework for AI-generated personalized advertising imagery. The generated personalized advertising
imagery is evaluated in survey 2 using established items to measure ATA, ATP and PI.
Customer
Data
GenAI
Customer
feedsintogenerates
personalizes
∊{L1, L2}
Research Question 1
How canwemakethisworkon a technicallevel?
How doesthisinfluenceATA, ATP and PI?
Research Question 2
ProcessofAI-
generated
personalized
advertising
imagery
Survey 2Survey 1
Customer
Advertisement ATA, ATP, PI
presentedto exhibits
Framework for AI-generated Personalized Advertising Imagery
Figure 1: Overview of the research design along the process of AI-generated personalized advertising imagery. To
answer RQ1, we develop and implement a technical framework that transforms customer data into personalized
advertising imagery at different levels of personalization (L0–L2). This framework is a prerequisite for answering RQ2,
as it produces the advertisements evaluated in our two-stage study: Survey 1 captures participant data as framework
input, and survey 2 presents the resulting images to the same participants and measures ATA, ATP and PI.
Results show that participants perceive differences in the levels of personalization, which confirms our assumption that
GenAI is able to incorporate customer data into generated advertising imagery and vary its level of personalization.
Across ATA, ATP, and PI, light personalization (L1) produces the most favorable responses. The stronger level of
2

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
personalization (L2) does not add additional benefit and can reduce ATA, ATP and PI. Confirmatory analyses support H1
for all three main constructs. H2 is only partially confirmed for ATA and ATP (through positive impact at L1 only) and
tests show significant effects for ATA and ATP for H3 as well. An exploratory analysis reveals an underlying mechanism
in which perceived personalization and perceived creepiness strongly influence ATA, ATP and PI. In summary, this
work contributes to the state-of-the-art in four ways.
1. We introduce a technical framework, along with its implementation, that couples an LLM with a T2I generator
to produce advertising imagery from real customer data and demonstrate its feasibility.
2. Our work provides a controlled within-subjects evaluation based on real participant profiles at the image level
and tests effects on ATA, ATP and PI complemented by manipulation checks of perceived personalization and
perceived creepiness.
3. We offer evidence that light personalization outperforms stronger personalization, which aligns with the
personalization-paradox [3] and yields practical guidance for the low-cost, scalable deployment of personalized
image-based advertising with GenAI.
4. We propose an explanation for the diminishing returns of personalization in AI-generated personalized
advertising imagery by connecting perceived creepiness with limitations of current GenAI model capabilities.
The remainder of this paper is organized as follows. Section 2 reviews the relevant literature on personalized marketing
and GenAI, establishing the theoretical foundation. Section 3 describes the research design and implementation of the
technical framework, as well as the development of the hypotheses. Section 4 presents the study design for survey 1
and survey 2, with the results reported in Section 5. Finally, Section 6 discusses and interprets the results, addresses
theoretical and practical implications, and suggests directions for future research. Section 7 concludes the work.
2 Background & related work
Personalization in marketing aims to enhance the customer experience and increase revenue by making advertisements
more relevant to individual customers [20, 46]. Higher relevance can increase attention, clicks, and purchases [ 59,
27, 7]. At the same time, personalization can become counterproductive when it is perceived as obtrusive or privacy-
invasive [35, 58]. This tension is known as the personalization-paradox: using more customer data can increase
relevance, but it can also trigger privacy concerns and reactance [4, 14]. Understanding how different forms and degrees
of personalization affect customer responses is therefore central to personalized marketing.
From recommendation to creative personalization.A large body of work optimizes allocation by matching existing
advertisements to users through recommendation systems [20, 66, 67]. This improves who sees which advertisements,
while the content itself often remains template-based. Modern GenAI provides two pillars for the shift to personalized
content. Transformer LLMs enable controllable text generation and prompt construction [15]. Diffusion models enable
high-fidelity image synthesis from text prompts [77, 9]. Together, they support scalable, automated pipelines that shift
from showing existing advertisements to the right person to generating a personalized advertisement for any given
person.
Dynamic creative optimization.DCO automates the assembly of creatives from modular assets, which enables
large-scale adaptation while keeping production costs manageable [ 54]. In practice, services such as Facebook’s
dynamic ads [62] operationalize this approach by linking product catalogs to user intent signals and composing variants
at impression time to improve relevance and click-through-rate (CTR). Academic work frames the selection of products
and creatives as a joint optimization problem and shows that algorithmic policies can outperform heuristic, rule-based
settings that are still common [6]. Early generative systems illustrate a transition point. Instead of only recombining
assets, like the previous approaches, they start to produce tailored visuals from predicted user attributes, for example,
personality-driven imagery generated with StyleGANs [30]. The key limitation remains that most DCO pipelines select
or lightly adapt predefined elements, rather than create completely new scenes that reflect highly individual user details.
GenAI-driven message personalization.Conceptual work positions GenAI as a driver of hyper-personalization
across text, image, video, and audio [70]. Empirical studies show that LLMs can generate persuasive messages that align
with user characteristics [51]. Large-scale experiments demonstrate that psychologically tailored messages outperform
generic or mismatched messages, with effects that persist even when the AI origin is known [ 60]. These findings
establish that GenAI can craft effective, personalized text at scale, motivating testing of whether analogous benefits
carry over when personalization is enacted visually.
3

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
Customer responses to AI-generated advertising.A related stream examines synthetic and AI-generated advertising
more broadly. Campbell et al. [18] provide a framework for understanding customer responses to manipulated and
synthetic advertising, including deepfakes and AI-generated ads. Recent empirical work shows that AI-generated
advertisements can shape customer responses, for example through disclosure effects and perceived authenticity in
luxury advertising [85]. Beyond advertising, marketplace-level research shows that GenAI affects creative goods
markets such as stock imagery by changing production, variety, sales, and substitution between GenAI and non-GenAI
content [34]. These studies establish the relevance of AI-generated advertising and imagery, but they do not examine how
advertising images can be personalized from real individual customer data or how different levels of such personalization
affect marketing outcomes.
GenAI-driven image personalization.Research on GenAI-driven image personalization in marketing remains
nascent and heterogeneous. Several systems chain an LLM with a T2I model to automate prompt design for banners and
product visuals, although personalization often refers to better product matching rather than user-specific scenes [86].
Other pipelines keep the product pixels fixed and personalize the surrounding context through inpainting or controlled
background changes, which can increase online CTR in field tests [ 24, 89]. Brand-alignment approaches fine-tune
diffusion models to match brand personality and funnel objectives, but they operate primarily at the brand level
rather than the individual level [ 43]. Comparative studies show that GenAI-generated images can rival or surpass
human-created images in quality and performance, including real-world CTR, but the generated content is typically
generic rather than tailored to individual user profiles [39]. Where personalization appears, it often relies on coarse
segments or narrow psychographic splits, such as introversion versus extraversion, and evaluations sometimes use
automated semantic similarity measures such as CLIP instead of human outcome measures [82, 81, 75].
Across these strands of research, prior work provides important building blocks but leaves three limitations. First,
recommendation-based personalization and DCO mostly optimize allocation or recombine predefined assets rather
than generate fully novel advertising scenes grounded in individual profiles [66, 67, 20, 54, 6]. Second, GenAI-based
personalization has been studied mainly for text, peripheral image edits, brand-level generation, or coarse segments
rather than individualized visual narratives [60, 24, 89, 43, 86]. Third, evaluations often prioritize CTR, marketplace
outcomes, or automated similarity measures instead of user-centered advertising effectiveness constructs such as
ATA, ATP, and PI [39, 82, 75]. Thus, to the best of our knowledge, no study has systematically investigated how
GenAI-based personalization of advertising imagery affects customer responses. In particular, prior work has not tested
fully AI-generated personalized advertising imagery that embeds products into customer-tailored visual narratives, uses
real individual customer data, explicitly varies the depth of personalization, and evaluates its effects on established
marketing outcomes.
3 Research development
In this section, we introduce the technical framework for AI-based personalized advertising imagery and its implemen-
tation to answer RQ1. We then develop the hypotheses to address RQ2, where the framework is applied.
3.1 AI-based personalized advertising imagery: Framework and implementation
First, we conceptualize the framework, by defining relevant steps along the creative workflow in advertising [17] and
then link the conceptual framework to its technical implementation, aiming for full automation. We then discuss how a
controlled variation in personalization is achieved.
3.1.1 Conceptual framework for AI-generated personalized advertising imagery
The framework aims to generate personalized advertising imagery by embedding products within customer-tailored
visual narratives, i.e. images that combine visual cues relatable to the target customer with the product in a familiar
environment. The framework is designed to address RQ1. To achieve this objective in a realistic scenario, where each
individual customer can be addressed, the framework must fully automate all steps that vary between customers so that
the system can scale.
The framework consists of three sequential steps (A, B, C), illustrated in Figure 2. The three steps are derived from the
conventional creative workflow, which consists of strategy development, creative briefing, creative work, and campaign
roll-out [17, 48]. Creative workflow typically begins with strategy development, e.g., identifying the target audience.
The creative workflow then proceeds to creative briefing, which defines the conceptual properties the final advertisement
should convey. This is followed by creative work, the actual production of marketing content, and finally campaign
roll-out [17, 48]. Within the framework, key steps of the creative workflow are automated. Strategy development
commonly includes the creation of personas: detailed fictitious customer profiles that portray a typical customer derived
4

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
from preceding market research. The framework adapts this step, but instead of generalized personas, the framework
creates an individual persona description derived directly from the customer data of a single individual. The framework
also replaces the conventional processes of preparing a creative brief and executing creative work with two distinct
AI models. The created persona description is combined with fixed product information and processed by the first AI
model, an LLM, to generate a personalized image prompt that specifies in detail how the final image should look and
feel. We see this image prompt in step prompt generation as analogous to the creative brief produced by a marketing
team, which would typically be forwarded to a design agency. In the final step, image generation, we automate the
creative work and the image prompt, together with a reference image of the product, is passed to the T2I model, which
uses it to generate the final hyperpersonalized advertising imagery. With our framework, all dynamic components that
vary across customers are fully automated, enabling the generation of personalized advertising images for any number
of customers and products.
Dynamic Component AI Model Static Component
Persona Creation
(A)
Prompt Generation
(B)
Customer Data
Product
Information
Product
Information
Image
Prompt
Prompt
Generation
Image Generation
(C)
Product
Image
Personalized
Image
Image
Generation
Figure 2: The framework for personalized image generation consists of three central components: the persona creation
(A), the image prompt generation (B), and the generation of the personalized image (C).
3.1.2 Technical implementation of the framework for AI-generated personalized advertising imagery
The conceptual framework is implemented in Python, depicted in Figure 3.It executes the three steps introduced above.
In step persona creation (A), the structured customer data is processed by a rule-based Python script that embeds the
values into predefined natural-language text snippets. An example of such a generated persona description is:“The
persona is a female individual, 35 years old, born in the United States, currently living in Bakersfield, United States. ”
In step prompt generation (B), the previously created persona description is inserted into a predefined user prompt
template, which serves as input to the LLM. This template also includes placeholders for product information, which
are dynamically filled at runtime, such as the product name and product type, e.g. “Polestar 4” and “electric vehicle”.
The resulting user prompt is then combined with a system prompt and passed to an LLM, operationalized through
OpenAI’s model gpt-5. From there, the LLM generates a natural-language description of the intended personalized
visual scenario, following the instructions in the system and user prompts, which include the persona description and
product information. This image description provides scenario guidance for the final advertising image. In step image
generation (C), the previously generated scenario guidance is inserted into a predefined user prompt template tailored
for the T2I model. This step is implemented using OpenAI’s gpt-image-1 model, which additionally accepts a reference
image of the advertised product to ensure accurate visual depiction. Alongside the model, prompt, and reference image,
additional parameters such as image quality (high) and resolution (1024x1536) are specified. The T2I model then
transforms these inputs into the final personalized advertising image through a one-shot generation process.
Prompt template design.The prompt templates serve as the central control mechanism of the implemented framework.
They keep creative instructions constant across products and personalization levels while allowing product- and customer-
specific variation through dynamically filled placeholders. The implementation uses separate prompt templates for
the LLM and the T2I generator, as shown in Figure 3, with placeholders for product name, product type, and persona
5

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
Customer Data
Persona
Description
Product
Information
Product
Image
LLM T2I Model
Persona Creation
(A)
Image Generation
(C)
Prompt Generation
(B)
System
Prompt
User
Prompt
Scenario
Guidance
System
Prompt
User
Prompt
Rule-Based
Python Script
Personalized
Image
Dynamic Component AI Model Static Component
Figure 3: The technical implementation of the framework for AI-generated personalized advertising imagery oper-
ationalizes the three steps of the framework with a rule-based Python script for persona creation (A), an LLM for
scenario guidance generation (B), and a T2I model for generating the personalized image (C).
description. To ensure consistent outputs, the templates use techniques such as role prompting, Markdown formatting,
XML tags, and negative prompts to prevent unwanted textual elements such as slogans or graphic overlays [72, 65].
Personalization.To isolate the central manipulation, the prompt templates remain identical across all levels of
personalization. Variation is introduced only through the persona description created in the persona creation step. For
L0, no customer data are included, making it the non-personalized baseline. For L1 and L2, the rule-based Python
script creates persona descriptions that differ in the amount and specificity of customer data. The LLM then translates
these persona descriptions into scenario guidances, which are used by the T2I model to generate images with increasing
levels of personalization. The rationale is that customer data can be ordered along a continuum from general to highly
individual information and grouped into increasingly specific market segments, up to the market of one. Since templates
remain constant across levels, systematic differences in the resulting images stem from the customer data used as input,
apart from inherent variation in GenAI outputs. Personalization is therefore not imposed directly at the image level,
but emerges from the amount and specificity of the customer data. This setup isolates the intended manipulation and
enables a controlled test of how different degrees of personalization influence ATA, ATP, and PI.
3.2 Hypothesis development
In this section, we outline the conceptual foundation of the empirical study, specifying what is being investigated and
why. It defines the study’s independent and dependent variables, introduces exploratory constructs, and explains how
marketing communication success is operationalized.
3.2.1 Study variables
To answer RQ2, the independent variable is the level of personalization, operationalized through differently personalized
images. To measure the effect of the levels of personalization, we use three different constructs. In addition, exploratory
variables enable further investigation into factors that may shape or moderate responses to AI-generated personalized
content.
Independent variable: Level of personalization.The independent variable is the level of personalization, oper-
ationalized through three advertising images per product generated by the framework described above. The levels
range from L0 to L2: L0 is a generic, non-personalized baseline without customer data; L1 uses general demographic
and geographic information; and L2 adds more specific sociodemographic, lifestyle, household, pet ownership, and
appearance-related attributes. Thus, the conditions differ only in the amount and specificity of customer data used as
input. The levels are conceptually defined rather than equidistant and follow a logic of increasing individualization
from general to highly specific customer information [ 88]. All included customer information is relevant for con-
6

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
ventional market segmentation and is either currently collected or technically feasible to collect in digital marketing
contexts [48, 37, 6].
Dependent variables: Attitude toward the ad, attitude toward the product and purchase intention.The
dependent variables in this study reflect ATA, ATP and PI, key marketing outcome constructs commonly used in
advertising research [64, 16, 57]. We select three constructs for confirmatory hypothesis testing due to their widespread
use and empirical validation as indicators of advertising effectiveness. Each offers a unique perspective on customer
response:
• Attitude toward the advertisementcaptures participants’ affective evaluation of the advertisement as a
stimulus, reflecting a predisposition to respond positively or negatively to the advertisement during a specific
exposure occasion [57].
• Attitude toward the productcaptures both affective and cognitive evaluations of the advertised offering,
representing the customer’s overall evaluative judgment of the product [16].
• Purchase intentioncaptures the customer’s stated likelihood of buying the advertised product, representing a
forward-looking indicator of behavioral intent [64].
The order of these measures reflects a hierarchy rooted in the widely acknowledged hierarchy-of-effects model proposed
by Lavidge and Steiner [50].
Exploratory variables.In addition to the dependent variables used for hypothesis testing, this study includes
exploratory measures to enrich the interpretation of participants’ perceptions and responses to AI-generated personalized
images.
• Perceived personalization: Assesses whether participants recognize the intended level of personalization
(L0–L2).
• Perceived creepiness: Excessive personalization may evoke feelings of creepiness, which is associated with
privacy concerns and a sense of being overly monitored [63, 71, 49, 35]. In AI-generated images, perceptual
dissonance can arise when stimuli appear human-like but not fully convincing [13]. This reflects the uncanny
valley effect, where images that are almost but not fully human elicit discomfort and aversion [29].
3.2.2 Confirmatory hypotheses
We derive three confirmatory hypotheses to answer RQ2. They investigate the effect of image personalization on ATA,
ATP and PI, and rest on theoretical and empirical foundations.
Advertising images generated by GenAI can perform on par with or outperform human-designed imagery [ 39, 43].
Prior work shows positive effects of personalization from recommendation [ 69], through DCO [ 6], to language-
model personalization and GenAI-based image personalization [24, 86]. Given the novelty of GenAI-driven image
personalization, hypothesis 1 (H1) tests for any effect, and hypothesis 2 (H2) examines the expectation of an overall
positive effect.
H1 There is an effect of image personalization on marketing communication success.Non-directional. At least
one mean outcome across the three levels of personalization (L0–L2) differs.
H2 There is a positive effect of image personalization on marketing communication success.Directional. At least
one mean outcome across the three levels of personalization (L0–L2) differs in a positive direction.
Evidence for a positive effect includes field experiments, where matching appeals to personality traits increased clicks
by up to 40% and purchases by up to 50% [59]. GenAI-enabled message personalization improves engagement across
domains [60]. In display advertising, higher content personalization raises CTR early in the decision process [ 10].
Tailored offerings elicit favorable attitudes [36], and micro-level cues such as a customer’s name strengthen attention
and memorability [1]. For visual content, AI-generated creatives can align with customer preferences and facilitate
conversions, though effects on perceived authenticity can be mixed [80, 68].
Personalization may also reach a tipping point. Reactance arises when advertisements expose uniquely identifiable
details [58], and greater data usage can heighten privacy concerns [ 4, 14]. Perceived creepiness rises from low to
moderate personalization and remains elevated at high levels [28]. AI-generated visuals can face tensions between
appeal and authenticity [80, 68]. Hyper-realistic faces are vulnerable to uncanny valley effects when subtle imperfections
7

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
occur [29], which is relevant for higher levels of personalization where human figures are generated from customer-
specific traits. Stylized or cartoon-like visuals can avoid this by lowering expectations for realism [29]. Together, these
findings suggest a “sweet spot” of personalization. Therefore, we define hypothesis 3 (H3):
H3 The relationship between image personalization and marketing communication success follows an inverted-U
pattern.Directional, non-linear. The moderate level of personalization (L1) enhances marketing outcomes
most effectively, while excessive personalization (L2) may reduce effectiveness due to customer resistance or
perceived intrusiveness.
3.2.3 Pre-registration and ethical approval
To ensure transparency and methodological rigor, the study was preregistered on theOpen Science Framework(OSF)
prior to data collection. The preregistration was created and registered on August 20, 2025. The full preregistration
can be accessed here: https://osf.io/uz5je/overview?view_only=2907997569564d73b62de212cd048d47.
Additionally, the study received ethical approval from the Ethics Committee of the University of Bayreuth on May 28,
2025, prior to data collection. All participants provided informed consent and were compensated in accordance with
Prolific’s [74] ethical guidelines.
4 Study design
We now turn to the study’s implementation: how we select products, measure our dependent and exploratory variables,
design the two surveys, and recruit participants.
4.1 Product selection
For the study, we need to select products to include in the advertising imagery. The selection follows three criteria
to ensure a diverse yet balanced set that allows for generalizable insights into AI-generated personalized advertising.
First, we apply the FCB Grid [ 87] as a theoretically grounded framework. The FCB Grid distinguishes products
along the degree of involvement in the purchase decision (low vs. high) and the dominant decision driver (thinking
vs. feeling) [87]. We select one product from each quadrant to cover different types of purchase decisions. Second,
the selection seeks to balance potential demographic interests by combining products that stereotypically attract male,
female, and gender-neutral interests. Third, expected visual portrayals generated by the framework are considered,
aiming to balance likely indoor and outdoor depictions across products.
The reference images used in the image generation step are obtained from publicly available product images and are
cited in Table 1. We select the Polestar 4 as an informative high-involvement product, the RIMOW A Original Cabin as
an affective luxury product, Tide Ultra Hygienic Clean as a habitual everyday product, and Lindt Lindor Truffles as a
self-satisfaction product [22, 83, 33].
FCB quadrant Product Product category
Informative Polestar 4 [73] Electric vehicle
Affective RIMOW A Original Cabin [76] Luxury suitcase
Habitual Tide Ultra Hygienic Clean [84] Laundry detergent
Self-satisfaction Lindt Lindor Truffles [56] Chocolates
Table 1: Reference products used in the image generation step. For copyright reasons, the original product images are
not reproduced in the manuscript.
4.2 Measurement of dependent variables
All three constructs (ATA, ATP and PI) are measured on a five-point Likert scale with single-item adaptations from
validated multi-item scales to reduce participant burden [8, 32]. The order of measurement follows the hierarchy-of-
effects model [50], progressing from conative to affective to stimulus-focused evaluation. ATA is based on the five-item
scale by Lee and Mason [52] as reported by Bruner et al. [16]. ATP draws on the seven-item scale originating from
Shamdasani et al. [79] as cited in Bruner et al. [16]. PI uses items summarized by Bruner et al. [16] that build on work
by Bower [11] and Bower and Landreth [12]. The exact single-item wordings are listed below. The product description
for PI is adjusted, depending on the specific product.
8

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
•PI: “If I were looking for an electric vehicle, based on this image, I would consider purchasing this product.”
•ATP: “This image makes me feel positive toward the product.”
•ATA: “The advertisement image is appealing to me.”
4.3 Measurement of exploratory variables
All exploratory constructs are measured with concise single-item formulations on a five-point Likert scale, adapted
to the context of AI-generated personalized images where applicable. Perceived personalization is adapted from
Kalyanaraman and Sundar [44]. Perceived creepiness condenses the multi-item semantic differential by De Keyzer et al.
[28] and reflects uncanny responses in near-human visuals [13, 29]. The exact wordings are listed below.
•Perceived personalization: “The scene featured in the image targets me as a unique individual.”
•Perceived creepiness: “I find this advertisement image creepy.”
4.4 Survey implementation
The study is conducted using two online surveys. In survey 1, participants provide personal information that serves
as input for the generation of personalized advertisement images. In survey 2, these images are presented back to the
identical participants, who then evaluate them across the dependent and exploratory variables described in the preceding
sections. Both surveys are created and administered with LimeSurvey hosted on a department-managed server to ensure
data security and compliance with institutional requirements.
4.4.1 Survey 1: Data collection
Survey 1 is designed to collect participant details that are subsequently used for generating personalized advertising
imagery.
Data collection criteria.To decide which details are collected from the participants in survey 1, three criteria are
applied to justify their inclusion. (1) The data point must be relevant for image generation. (2) The data point must be
relevant for market segmentation. (3) The details collected must be, at least in theory, collectible in real-world practice.
Structure of survey 1.Survey 1 collects participant information used as input for personalized image generation and
is divided into five question groups:basic information,life stage,lifestyle,environment, andstyle. Basic information
coversgender,age,country of residency,city of residency,country of birth,ethnicity, andfamily origin/background.
Life stage capturesoccupation type,occupation title,income class,relationship status,number of children, andage
groups of children. Lifestyle collectsregular activities and hobbiesas free-text input to support realistic scenario
generation. Environment covershousing type,residence area,climate,attention check, andpet ownershipwithpet type
if applicable. Finally, style captureshair style,hair color,beard stylewhere applicable,body type,glasses wearer,
color preference, andstyle preference. These variables are included because they are relevant for image generation,
correspond to established segmentation dimensions, and are in principle collectible or inferable in digital marketing
contexts [48, 37, 88, 25, 55, 6, 2].
4.4.2 Survey 2: Image evaluation
In survey 2, participants evaluate the AI-generated advertisement images. A selection of four AI-generated advertise-
ments from the survey are shown in Figure 4. No generated images are manually filtered, replaced, or excluded before
survey 2. Thus, participants evaluate the complete output of the automated generation pipeline, including occasional
visual artifacts or low-quality generations.
Structure of survey 2.First, for each product, participants rate all three levels of personalization (L0–L2) on a
fixed set of five items. These include the three dependent variables used for hypothesis testing (PI, ATP, and ATA)
and two exploratory items: a manipulation check of perceived personalization and a measure of perceived creepiness.
Therefore, each product evaluation section contains 5 items ×3 images = 15 Likert ratings. After completing a product
evaluation section, participants proceed to the next until all four products are evaluated. The order of the product
evaluation pages is randomized to avoid biased responses from product order effects. Items within each product
evaluation section are deliberately not randomized, as they are commonly presented in the sequence suggested by the
hierarchy-of-effects model [50]. Participants were not explicitly informed before or during the image evaluation tasks
that the presented advertisement images were generated using AI. This is important because prior work shows that
perceived or communicated AI involvement can itself influence evaluations of generated content [47, 85].
9

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
Electric vehicle Luxury suitcase Laundry detergent Chocolates
Figure 4: Fully AI-generated advertising imagery with the highest level of personalization (L2) for all products over
four different participant personas.
Evaluation of images.The evaluation setup is identical across all product evaluation sections, with only the product
name and corresponding images varying. Each evaluation is presented in a tabular layout: the leftmost column displays
one image per row, followed by the five-point Likert response options (strongly disagree to strongly agree). Images are
always displayed at full size, so each image is always fully visible. The question text remains fixed directly beneath the
navigation bar, and the Likert labels stay anchored at the top of the table. This guarantees that evaluation criteria are
always visible, reducing cognitive load and supporting accurate responses. The layout is optimized with the feedback
from several pre-studies.
4.5 Recruitment strategy
Participants are recruited via Prolific [74]. Participation is restricted to desktop devices to safeguard data quality [78, 5].
The introduction page of each survey states the terms and conditions, the use of attention checks, and the consequences
of failing them. Screening in survey 1 requires participants to be between 18 and 99 years old, native English speakers,
and located in the United States. For survey 2, no additional screening is used, since access is limited to the saved group
from survey 1. The sample distribution mode is set to “standard”.
5 Results
The following section presents the sample characteristics and the study’s empirical findings.
5.1 Sample characteristics
The final sample consists of N= 100 participants. In total, 122 individuals initially submit responses for survey 1, with
3 excluded due to failed attention checks. From the remaining 119 individuals, 107 return to survey 2. After 7 further
exclusions due to failed attention checks, 100 participants are included in the final analyses. Participants rated images
across three levels of personalization over four different products resulting in a total of1,200 ratings. Participants have a
mean age of 44.5 years (SD= 13.1 ), with ages ranging from 22 to 84 years. The gender distribution is balanced, with
53 male (53%) and 47 female (47%) participants. Zero participants selected the “diverse” option. The large majority
are U.S. citizens (92 participants, 92%), in line with the screening criteria. Ethnic background is reported as 79 White
(79%), 8 Mixed (8%), 6 Asian (6%), 5 Black (5%), and 2 Other (2%). The final sample consists exclusively of native
English speakers. 75 participants (75%) indicate working either full-time, part-time, or self-employed, 13 participants
(13%) report being unemployed, 9 participants (9%) report being retired, and 3 participants (3%) report being university
students. The median completion time for survey 1 is 4.6 minutes (M= 5.2 , SD= 2.6 , range = 1.8–18.9). The
median completion time for survey 2 is 9.8 minutes (M= 10.4 , SD= 4.1 , range = 3.8–23.8). Compensation is in
line with Prolific’s guidelines for fair hourly payment at £8.57/hr for survey 1 and £8.47/hr for survey 2. No major
technical issues were observed during the study.
10

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
5.2 Analysis
We test our hypotheses using a repeated-measures ANOV A for H1 and planned one-tailed paired t-tests for H2 and
H3. The effects of perceived personalization and perceived creepiness are also evaluated using a repeated-measures
ANOV A. We test the sphericity assumption using Mauchly’s test for all repeated-measures ANOV As [61]. When
violated, we apply Greenhouse-Geisser corrections to the degrees of freedom [ 38]. An overview of the means and
standard deviations across levels and constructs is shown in Figure 5 with the exact values reported in Table 6. For all
three constructs results increase from L0 to L1 and decrease again at the highest level L2. Notably, the mean values at
L2 are lower than the baseline L0 for each construct.
$ 7$ $ 73 3,








6FRUH

/ / /
Figure 5: Mean and standard deviation by construct and level of personalization.
Hypothesis 1.The repeated-measures ANOV A reveal a significant effect of level of personalization on ATA, ATP,
and PI (see Table 2), supporting H1 that levels of personalization differ in their effects for all constructs.
ConstructF(d f 1, d f2)p-valueη 2 GG
ATA16.68(1.46,144.94)< .001.046
ATP10.01(1.31,130.11)< .001.026
PI17.84(1.31,129.37)< .001.043
Table 2: Repeated-measures ANOV A results for H1. Greenhouse-Geisser corrected degrees of freedom are reported
due to sphericity violations in all constructs.
Hypothesis 2.We use two planned one-tailed paired t-tests to test whether any of the levels of personalization L1
or L2 exceed the baseline L0, for all three constructs. Our prediction is partially confirmed. The results support H2
for ATA and ATP. For both, L1 is significantly higher than L0 (see Table 3). For PI we do not observe a significant
increase of L1 over L0. For all three constructs L2 does not significantly exceed the baseline. In all three cases, the
observed means for L2 were numerically lower than the baseline condition (see Table 6), resulting in the non-significant
one-tailed comparisons.
Hypothesis 3.In H3, we predict that the constructs, based on levels of personalization, follow an inverted-U pattern,
with a moderate level of personalization (L1) outperforming extreme levels (L0, L2). To test for the inverted-U pattern,
we use two planned one-tailed paired t-tests (L1> L0, L1> L2). Results provide mixed support: L1 significantly
exceeds L0 for ATA and ATP, but not for PI—as already indicated in H2. For all three constructs, L1 is significantly
greater than L2, as shown in Table 3. Thus, H3 is supported only for ATA and ATP, as the inverted-U pattern is not
observed for PI.
11

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
Construct Comparisont(99)p d
ATAL1> L05.28< .001.38
L2> L0−1.98.975.21
L1> L25.31< .001.49
ATPL1> L04.67< .001.28
L2> L0−1.45.925.15
L1> L24.18< .001.37
PIL1> L0 1.38.085.09
L2> L0−3.69.999.39
L1> L25.52< .001.44
Table 3: Planned one-tailed paired t-tests for H2 (level > L0) and H3 (L1> L0, L1> L2). One-tailed p-values. H2
is supported if at least one comparison is significant per construct. H3 is supported if L1 is significantly greater than
both L0 and L2.
Exploratory analysis.A repeated measures ANOV A confirms that levels of personalization significantly affect
perceived personalization, as well as perceived creepiness. For both, we test differences with post-hoc, Holm-Bonferroni
corrected pairwise comparisons. As shown in Table 4, the tests reveal that each personalized condition is perceived
as significantly more personalized than the previous (L2 > L1 > L0). The same behavior is observed for perceived
creepiness. Each personalized condition is perceived as significantly more creepy than the previous. These results
suggest that higher levels of personalization lead to greater perceived differences, but at the same time elicit greater
concerns among participants.
Construct Comparisont(99)p d
Perceived personalizationL1> L07.05< .001 0.41
L2> L05.97< .001 0.67
L2> L12.94.004 0.28
Perceived creepinessL1> L02.92.004 0.23
L2> L07.27< .001 0.89
L2> L16.96< .001 0.71
Table 4: Post-hoc pairwise comparisons (Holm-Bonferroni corrected p-values) for perceived personalization and
perceived creepiness.
To better understand the interaction between levels of personalization and the different constructs, we conduct a
parallel multilevel mediation analysis, using linear mixed-models, to examine the mechanisms through which levels of
personalization affect the main constructs via the mediators perceived personalization and perceived creepiness. Using
cluster bootstrap (5,000 iterations) with random intercepts for participants, we estimate unique indirect effects for each
level of personalization relative to baseline (L0). Path coefficients show that the levels of personalization (L1, L2)
increase both perceived personalization and perceived creepiness, though creepiness does not show a significant effect
on L1. We provide a concise overview in Table 5. The two mediators, in turn, predict constructs in opposite directions,
as shown in Table 5.
Indirect effects reveal a critical nonlinear pattern: At L1, perceived personalization and perceived creepiness produce a
net positive indirect effect for ATA and ATP, as connection benefits outweigh creepiness costs, while the indirect effect
for PI at L1 and the indirect effects across all constructs at L2 are not significantly different from zero. These results
are driven by strongly increasing creepiness perceptions that overwhelm personalization gains (see Table 7). The total
effects confirm a peak for the moderate level of personalization. ATA and ATP are increased at L1 relative to L0, while
PI does not reach statistical significance. At L2, ATA and PI decrease, while the effect is not significant for ATP. A
concise overview of these results is presented in Table 7. These findings demonstrate the personalization-paradox in our
setting and show that moderate personalization enhances outcomes through a feeling of personal relevance but higher
levels trigger creepiness reactions that produce net negative effects.
12

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
PathbSEp
Level of personalization→mediators
L1→perceived personalization.47.11< .001
L2→perceived personalization.81.11< .001
L1→perceived creepiness.14.10.189
L2→perceived creepiness.83.10< .001
Mediators→outcomes
Perceived personalization→ATA.39.04< .001
Perceived creepiness→ATA−.56.04< .001
Perceived personalization→ATP.35.03< .001
Perceived creepiness→ATP−.49.04< .001
Perceived personalization→PI.31.03< .001
Perceived creepiness→PI−.49.04< .001
Table 5: Path coefficients of the parallel multilevel mediation model. The upper panel reports the effects of level of
personalization on the mediators, and the lower panel reports the effects of the mediators on the outcome constructs.
6 Discussion
This study examined whether GenAI can generate personalized advertising imagery from customer data and how
different levels of personalization affect ATA, ATP, and PI. The results demonstrate the feasibility of the framework and
show that moderate personalization (L1) improves ATA and ATP, whereas stronger personalization (L2) does not add
benefit and can reduce outcomes. For ATA and ATP, the results therefore indicate an inverted-U pattern. The framework
also successfully produces visibly different levels of personalization, as illustrated in Figure 6 and Figure 8.
L0 L1 L2
Figure 6: From left to right: Showcase of different levels of personalization, L0–L2, for the same participant persona
and product.
The mediation analysis shows that perceived personalization and perceived creepiness operate as competing mechanisms.
Perceived personalization positively predicts ATA, ATP, and PI, whereas perceived creepiness has a slightly stronger
negative effect. At L1, personalization benefits outweigh creepiness costs for ATA and ATP. At L2, however, increasing
creepiness neutralizes these benefits across all three constructs. This pattern supports the personalization-paradox in the
context of AI-generated advertising imagery and suggests that stronger visual personalization can undermine its own
relevance benefits.
Notably, the decline from L1 to L2 cannot be explained by perceived creepiness alone. As shown in Table 7, the
direct effects of personalization also diminish sharply: the positive direct effects of L1 disappear at L2 for ATA and
ATP, while PI even shows a negative direct effect at L2. One explanation could be reduced image quality at higher
personalization. Additional customer information may increase prompt complexity and lead to “catastrophic neglect”,
13

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
where the model fails to represent parts of the image correctly [ 21, 31]. Distorted features, implausible scenes, or
other visual artifacts may therefore reduce advertising effectiveness and simultaneously increase perceived creepiness.
Beyond these technical limitations, stronger personalization may also increase algorithm aversion, as customers can be
less willing to rely on algorithms for subjective tasks [19]. Thus, the negative effect of strong personalization likely
reflects the personalization-paradox, current technical limitations of GenAI-based image generation, and algorithm
aversion in a subjective advertising context. Future implementations may require more selective customer data use,
specialized models, or automated quality-control mechanisms before deployment.
The fact that H1 and H2 are supported only for ATA and ATP, but not for PI, is consistent with a hierarchy-of-effects
perspective. While personalization affects earlier attitudinal responses, such as ATA and ATP, the effect does not extend
to PI, which represents a more downstream and behavior-proximal outcome [50].
Theoretical implications.Our findings contribute to several areas of research. First, we extend the research on
personalized marketing, specifically the topics of personalized advertising and DCO. Our results also clarify the
contribution of this study relative to the growing literature on AI-generated advertising. Prior work has shown that
synthetic advertising represents a new generation of advertising manipulation enabled by AI [18], and that customer
responses to AI-generated advertisements can be negative when the use of AI conflicts with brand expectations [85]. We
extend this literature by shifting attention away from comparison of AI-generated and human-created advertisements to
the degree of personalization within AI-generated visual content. This distinction is theoretically important because
personalization depth introduces a second evaluative tension: the same customer data that can increase relevance may
also increase creepiness and thereby reduce ATA, ATP, and PI. Previous research in the field of DCO focuses mainly
on generating personalized advertising text with AI [60, 70]. Different marketing slogans or image descriptions are
generated for individual customers based on their data. Other work replaces parts of the images with GenAI, based
on context [89, 24]. Our study goes beyond this approach. We fully generate the imagery with AI, given a product,
and include high levels of personalization, based on customer data. We embed customer preferences and portrayals
into the product to improve personalization. We show that this approach can yield positive results on ATA and ATP,
thereby confirming the general feasibility with our technical framework. In line with the broader argument that GenAI
enables novel personalization interventions by making large-scale creative personalization technically feasible [53],
our results demonstrate that personalization can be enacted directly at the level of fully generated visuals rather than
being limited to modular asset recombination or partial edits. Previous research in personalized advertising finds that
personalized advertising improves customer attention and interaction, as well as increasing purchases [59, 60], and we
confirm a similar behavior with fully AI-generated content. In addition, our findings contribute to the literature on the
privacy-paradox [3, 20, 23, 4, 35] in the domain of fully AI-generated advertising imagery. The observed behavior is a
trade-off between shared information and gains in personalization. Customers weigh intrusiveness in their personal data
against the added value from personalized advertisements. We observe the same behavior for our AI-generated images.
However, we note that the diminishing returns we observe in our study could also stem from different factors, such as
image quality.
Practical implications.Targeting customers with data-driven advertisements is already standard practice [ 20, 66, 67],
fueled by the growth of AI and the abundance of data available from customer interactions or directly from social
media. This development is part of a broader shift in marketing practice driven by new digital technologies that change
how firms create, deliver, and optimize marketing value [42]. While marketers have become excellent at matching the
right product to the right customer, personalizing the actual creative content of an advertisement remains expensive.
Usually, brands will limit themselves to a small handful of advertisement variations because the production cost of
advertisements, especially advertising imagery, is high [39]. GenAI eliminates this barrier, allowing for the automated
creation of advertisement assets at scale. Research shows that AI-generated advertisements can now match or even
outperform human-made ones [39]. This presents a marketing innovation [42] with new opportunities for personalized
marketing: Companies can now tailor both content and presentation to individual interests and personalities without the
high overhead. Our study shows that moderate personalization is well-received, allowing marketers to optimize both
the recommendation and the creative content. Instead of only focusing on finding the right audience, marketers can
now simultaneously tailor the advertisement itself to that audience, creating a far more precise alignment between the
product and the customer. This development also has implications for platforms. We argue that a bottleneck in current
personalization efforts is modest quality of AI-generated images, which diminishes the potential returns. We present a
selection of faulty images in Figure 7. However, if these technical challenges are solved, the gains could be significantly
higher. Platforms such as Instagram or Facebook sit at the intersection of marketers and customers. They own the
data, host the advertisements, and have an active user base. This positions platform providers to offer AI-generated
personalized advertisements as a core service. They have the infrastructure and the technical expertise to build these
systems, allowing them to move beyond simply being the channel for advertisement distribution. By leveraging their
existing data infrastructure and building their own advertising models, they can offer a new service that manages both
14

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
parts of the match—automatically building the right advertisement for the right customer the moment it is shown. This
allows platforms to move from simple distribution to actively optimizing every variable to find the best possible result
for every customer. In summary, in the future, these platforms can leverage customer data for two decisions: which
product to present to which customer, and what level of personalization they choose to have the optimal result.
Electric vehicle Luxury suitcase Laundry detergent Chocolates
Figure 7: Some images contain obvious flaws such as the reversed trunk on the electric vehicle, misplaced or distorted
regions for the luxury suitcase or text-generation errors in the laundry detergent and chocolate logo. All displayed
images are generated with the strong level of personalization (L2) over different products, with major flaws highlighted
in red.
Future research.Future research should refine the understanding of personalization in AI-generated advertising
imagery in four directions. First, studies should isolate individual customer attributes, such as demographic, lifestyle,
or appearance-related cues, to identify which inputs increase perceived personalization without increasing perceived
creepiness or reducing ATA, ATP, and PI. Second, future work should examine how directly customers should be visually
represented in personalized advertisements, ranging from abstract lifestyle cues to visually similar persons or direct
customer depictions. This would clarify how customer likeness affects perceived personalization, perceived creepiness,
ATA, ATP, and PI. Third, research should investigate boundary conditions under which deeper personalization becomes
beneficial or harmful. Our findings suggest that stronger personalization can reduce marketing outcomes, consistent with
the personalization-paradox [3, 20]. Yet this effect may depend on data-use expectations, perceived appropriateness,
platform context, disclosure, consent mechanisms, and product category [3, 26]. Finally, future work should separate
the effects of personalization depth from image quality. Higher personalization may increase generation complexity
and produce artifacts, which can reduce ATA, ATP, and PI and increase perceived creepiness. Systematic quality
assessments, controlled artifact manipulations, and automated quality-control mechanisms could improve the reliability
of personalized image generation.
Ethical considerations.AI-generated personalized advertising raises ethical concerns related to privacy, trust, and
customer autonomy [41, 40]. First, personalization depends on customer data, yet customers may not be fully aware of
the extent to which such data are collected, processed, or inferred. This challenges informed consent, especially when
customers lack the technical understanding needed to evaluate how their data are used [90]. AI-based marketing can
further intensify privacy risks when data are collected without sufficient consent, leaked or de-anonymized, or used to
infer sensitive attributes from customer and interaction data [41]. Second, AI-generated advertising may erode trust
when generated content misrepresents products or brand promises. Hallucinated, exaggerated, or overly polished product
presentations can create expectations that do not match reality. Similarly, visual flaws in generated advertising imagery
may negatively affect brand perception. Both cases can damage the brand–customer relationship by undermining
credibility. Third, GenAI-based personalization can threaten customer autonomy by shaping choice architectures in
highly persuasive or manipulative ways [40]. Personalized advertising may bypass reflective decision-making when
emotionally engaging content is optimized toward persuasion rather than informed choice, potentially contributing
to unnecessary or uncontrolled spending [60, 90]. To address these risks, marketers and platforms should implement
meaningful transparency and governance mechanisms that support intelligibility, accountability, and appropriate human
oversight in ethically salient marketing contexts [40].
15

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
7 Conclusion
This paper examines whether GenAI enables scalable creative personalization in advertising imagery and whether
increasing personalization improves marketing outcomes. We address this gap by proposing and implementing
a fully automated framework that transforms real customer data into personalized advertising imagery through a
three-step pipeline (persona creation, prompt generation with an LLM, and image synthesis with a T2I model). We
operationalize personalization across three levels (L0–L2) that systematically vary the amount and specificity of
user information, enabling a controlled test of personalization depth in AI-generated visuals. In a preregistered two-
stage within-subjects study with N= 100 participants and four products, we find that participants reliably perceive
differences in personalization across conditions, confirming that GenAI incorporates customer data into generated
imagery. Personalization affects ATA, ATP, and PI, but the effect is not monotonic. Light personalization (L1) yields
the highest descriptive values for ATA, ATP, and PI and significantly outperforms the non-personalized baseline (L0) for
ATA and ATP. In contrast, strong personalization (L2) does not improve outcomes and can reduce them. To explain these
diminishing returns, we show that perceived personalization and perceived creepiness operate as competing mechanisms.
Higher levels of personalization increase perceived personalization, which positively predicts ATA, ATP, and PI, but
they also increase perceived creepiness, which negatively predicts the three measures and grows more strongly at high
personalization. The resulting net effect favors L1, where connection benefits outweigh creepiness costs, whereas high
personalization shifts the balance toward less favorable reactions. These findings extend the personalization-paradox to
fully AI-generated advertising imagery and provide actionable guidance: effective GenAI-driven image personalization
is achievable, but it benefits from conservative use of personal cues. Future research should refine personalization
strategies at the attribute level, improve robustness and visual fidelity under richer profile inputs, and investigate
boundary conditions such as product types, disclosure strategies, and platform contexts to determine when deeper
personalization becomes acceptable and beneficial.
Declaration of generative AI and AI-assisted technologies in the manuscript preparation
process
During the preparation of this work, the authors used ChatGPT, Claude, Gemini and DeepL Write in order to assist with
language refinement and clarity. After using these tools, the authors reviewed and edited the content as needed and take
full responsibility for the content of the published article.
16

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
A Appendix
L0 L1 L2
M SD M SD M SD
ATA 3.56 .76 3.86 .85 3.35 1.23
ATP 3.59 .75 3.80 .80 3.44 1.14
PI 3.71 .71 3.78 .82 3.34 1.11
Table 6: Descriptive statistics by construct and level of personalization.
Contrast Effect Coef. 95% CI
ATAL1vsL0Indirect via perceived personalization.18[.13, .25]
Indirect via perceived creepiness−.08[−.14,−.03]
Total indirect.10[.02, .19]
Direct (c′).20[.10, .31]
Total (c).31[.20, .42]
L2vsL0Indirect via perceived personalization.31[.21, .43]
Indirect via perceived creepiness−.46[−.63,−.30]
Total indirect−.15 [−.35, .05]
Direct (c′)−.07 [−.26, .12]
Total (c)−.21[−.43,−.002]
ATPL1vsL0Indirect via perceived personalization.17[.11, .23]
Indirect via perceived creepiness−.07[−.13,−.02]
Total indirect.10[.02, .18]
Direct (c′).12[.03, .21]
Total (c).22[.13, .31]
L2vsL0Indirect via perceived personalization.28[.19, .39]
Indirect via perceived creepiness−.40[−.57,−.26]
Total indirect−.12 [−.31, .07]
Direct (c′)−.03 [−.20, .14]
Total (c)−.15 [−.35, .05]
PIL1vsL0Indirect via perceived personalization.14[.09, .20]
Indirect via perceived creepiness−.07[−.13,−.02]
Total indirect.07 [−.01, .15]
Direct (c′)−.01 [−.11, .08]
Total (c).07 [−.03, .16]
L2vsL0Indirect via perceived personalization.25[.16, .35]
Indirect via perceived creepiness−.40[−.57,−.26]
Total indirect−.16 [−.35, .02]
Direct (c′)−.21[−.38,−.05]
Total (c)−.37[−.56,−.17]
Table 7: Mediation effects by level of personalization. Values are standardized effects with 95% bootstrap confidence
intervals. Bold values in the coefficient column indicate confidence intervals excluding zero.
17

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
L0
L1
L2
Electric
vehicle
Luxury
suitcase
Laundry
detergent
Chocolates
Figure 8: Example advertisements for all four products (columns) across levels of personalization (rows), generated
from different participant personas.
18

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
References
[1] Hisham Abdel Monem. 2021. The effectiveness of advertising personalization.Journal of Design Sciences and
Applied Arts2, 1 (2021), 114–121.
[2] Ayana Adilova and Pakizar Shamoi. 2024. Personalized Aesthetic Assessment: integrating fuzzy logic and color
preferences.IEEE Access(2024).
[3] Elizabeth Aguirre, Dominik Mahr, Dhruv Grewal, Ko De Ruyter, and Martin Wetzels. 2015. Unraveling the
personalization paradox: The effect of information collection and trust-building strategies on online advertisement
effectiveness.Journal of retailing91, 1 (2015), 34–49.
[4] Elizabeth Aguirre, Anne L Roggeveen, Dhruv Grewal, and Martin Wetzels. 2016. The personalization-privacy
paradox: implications for new media.Journal of consumer marketing33, 2 (2016), 98–110.
[5] Ioannis Andreadis. 2015. Web surveys optimized for smartphones: Are there differences between computer and
smartphone users?methods, data, analyses9, 2 (2015), 16.
[6] Lennart Baardman, Elaheh Fata, Abhishek Pani, and Georgia Perakis. 2021. Dynamic creative optimization in
online display advertising.Available at SSRN 3863663(2021).
[7] Hyejin Bang, Dongwon Choi, Bartosz W Wojdynski, and Yen-I Lee. 2019. How the level of personalization
affects the effectiveness of personalized ad messages: the moderating role of narcissism.International Journal of
Advertising38, 8 (2019), 1116–1138.
[8] Lars Bergkvist and John R Rossiter. 2007. The predictive validity of multiple-item versus single-item measures of
the same constructs.Journal of marketing research44, 2 (2007), 175–184.
[9] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce
Lee, Yufei Guo, et al. 2023. Improving image generation with better captions.Computer Science. https://cdn.
openai. com/papers/dall-e-3. pdf2, 3 (2023), 8.
[10] Alexander Bleier and Maik Eisenbeiss. 2015. Personalized online advertising effectiveness: The interplay of what,
when, and where.Marketing Science34, 5 (2015), 669–688.
[11] Amanda B Bower. 2001. Highly attractive models in advertising and the women who loathe them: The implications
of negative affect for spokesperson effectiveness.Journal of advertising30, 3 (2001), 51–63.
[12] Amanda B Bower and Stacy Landreth. 2001. Is beauty best? Highly versus normally attractive models in
advertising.Journal of advertising30, 1 (2001), 1–12.
[13] Kimberly A Brink, Kurt Gray, and Henry M Wellman. 2019. Creepiness creeps in: Uncanny valley feelings are
acquired in childhood.Child development90, 4 (2019), 1202–1214.
[14] Nancy Howell Brinson and Matthew S Eastin. 2016. Juxtaposing the persuasion knowledge model and pri-
vacy paradox: An experimental look at advertising personalization, public policy and public understanding.
Cyberpsychology: Journal of Psychosocial Research on Cyberspace10, 1 (2016).
[15] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Nee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al . 2020. Language models are few-shot learners.
Advances in neural information processing systems33 (2020), 1877–1901.
[16] Gordon C Bruner, Paul J Hensel, and Karen E James. 2005. Marketing scales handbook. American Marketing
Association Chicago, IL.
[17] Leslie Butterfield. 2009.Excellence in advertising. Routledge.
[18] Colin Campbell, Kirk Plangger, Sean Sands, and Jan Kietzmann. 2022. Preparing for an era of deepfakes and
AI-generated ads: A framework for understanding responses to manipulated advertising.Journal of Advertising
51, 1 (2022), 22–38.
[19] Noah Castelo, Maarten W Bos, and Donald R Lehmann. 2019. Task-dependent algorithm aversion.Journal of
marketing research56, 5 (2019), 809–825.
[20] Shobhana Chandra, Sanjeev Verma, Weng Marc Lim, Satish Kumar, and Naveen Donthu. 2022. Personalization
in personalized marketing: Trends and ways forward.Psychology & Marketing39, 8 (2022), 1529–1562.
[21] Hila Chefer, Yuval Alaluf, Yael Vinker, Lior Wolf, and Daniel Cohen-Or. 2023. Attend-and-excite: Attention-
based semantic guidance for text-to-image diffusion models.ACM transactions on Graphics (TOG)42, 4 (2023),
1–10.
[22] Hyuk Jun Cheong. 2017. Revisiting an advertising theory: the FCB grid in the 21st century. American Academy
of Advertising, 157.
19

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
[23] Julien Cloarec. 2020. The personalization–privacy paradox in the attention economy.Technological Forecasting
and Social Change161 (2020), 120299.
[24] Ádám Tibor Czapp, Mátyás Jani, Bálint Domián, and Balázs Hidasi. 2024. Dynamic product image generation
and recommendation at scale for personalized e-commerce. InProceedings of the 18th ACM Conference on
Recommender Systems. 768–770.
[25] Michael R Czinkota, Masaaki Kotabe, Demetris Vrontis, and SM Riad Shams. 2021. Market segmentation,
positioning, and branding. InMarketing Management: Past, Present and Future. Springer, 283–340.
[26] Judith Irene Maria De Groot. 2022. The personalization paradox in Facebook advertising: The mediating effect of
relevance on the personalization–brand attitude relationship and the moderating effect of intrusiveness.Journal of
Interactive Advertising22, 1 (2022), 57–74.
[27] Freya De Keyzer, Nathalie Dens, and Patrick De Pelsmacker. 2022. How and when personalized advertising leads
to brand attitude, click, and WOM intention.Journal of Advertising51, 1 (2022), 39–56.
[28] Freya De Keyzer, Guda Van Noort, and Sanne Kruikemeier. 2022. Going too far? How consumers respond to
personalized advertising from different sources.Journal of Electronic Commerce Research23, 3 (2022), 138–159.
[29] Claude Draude. 2011. Intermediaries: reflections on virtual humans, gender, and the Uncanny Valley.AI & society
26, 4 (2011), 319–327.
[30] Aleksandr Farseev, Qi Yang, Andrey Filchenkov, Kirill Lepikhin, Yu-Yi Chu-Farseeva, and Daron-Benjamin Loo.
2021. Somin. ai: Personality-driven content generation platform. InProceedings of the 14th ACM international
conference on Web search and data mining. 890–893.
[31] Huan Fu and Guoqing Cheng. 2024. Enhancing semantic mapping in text-to-image diffusion via Gather-and-Bind.
Computers & Graphics125 (2024), 104118.
[32] Christoph Fuchs and Adamantios Diamantopoulos. 2009. Using single-item measures for construct measurement
in management research: Conceptual issues and application guidelines.Die Betriebswirtschaft69, 2 (2009), 195.
[33] Tim Glowa. 2002. White paper: advertising process models.Calgary, AB: North Country Research Inc(2002).
[34] Samuel Goldberg and H Tai Lam. 2025. Generative ai in equilibrium: Evidence from a creative goods marketplace.
Equilibrium: Evidence from a Creative Goods Marketplace (February 24, 2025)(2025).
[35] Avi Goldfarb and Catherine Tucker. 2011. Online display advertising: Targeting and obtrusiveness.Marketing
Science30, 3 (2011), 389–404.
[36] Ronald E Goldsmith and Jon B Freiden. 2004. Have it your way: consumer attitudes toward personalized
marketing.Marketing Intelligence & Planning22, 2 (2004), 228–239.
[37] Google. 2025. Privacy Policy – Privacy & Terms – Google. https://policies.google.com/privacy?hl=en#infocollect.
[38] Samuel W. Greenhouse and Seymour Geisser. 1959. On Methods in the Analysis of Profile Data.Psychometrika
24, 2 (1959), 95–112. doi:10.1007/BF02289823
[39] Jochen Hartmann, Yannick Exner, and Samuel Domdey. 2025. The power of generative marketing: Can generative
AI create superhuman visual marketing content?International Journal of Research in Marketing42, 1 (2025),
13–31.
[40] Erik Hermann. 2022. Artificial intelligence and mass personalization of communication content—An ethical and
literacy perspective.New media & society24, 5 (2022), 1258–1277.
[41] Erik Hermann. 2022. Leveraging artificial intelligence in marketing for social good—An ethical perspective.
Journal of Business Ethics179, 1 (2022), 43–61.
[42] Donna L Hoffman, C Page Moreau, Stefan Stremersch, and Michel Wedel. 2022. The rise of new technologies in
marketing: A framework and outlook. 6 pages.
[43] Tijmen Jansen, Mark Heitmann, Martin Reisenbichler, and David A Schweidel. 2023. Automated alignment:
Guiding visual generative AI for brand building and customer engagement.Available at SSRN(2023).
[44] Sriram Kalyanaraman and S Shyam Sundar. 2006. The psychological appeal of personalized content in web
portals: Does customization affect attitudes and behavior?Journal of Communication56, 1 (2006), 110–132.
[45] Anuj Kapoor and Madhav Kumar. 2025. Frontiers: Generative AI and personalized video advertisements.
Marketing Science44, 4 (2025), 733–747.
[46] Jihoon Jay Kim, Taeyeon Kim, Bartosz W Wojdynski, and Hyoyeun Jun. 2022. Getting a little too personal?
Positive and negative effects of personalized advertising on online multitaskers.Telematics and Informatics71
(2022), 101831.
20

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
[47] Samsun Knight, Yakov Bart, and Minwen Yang. 2023. Generative AI and the Perceived Quality of User-Generated
Content: Evidence from Online Reviews.Northeastern U. D’Amore-McKim School of Business Research Paper
4621982 (2023).
[48] Philip Kotler and Kevin Lane Keller. 2016.Marketing Management(15 [edition] ed.). Pearson, Boston.
[49] Kevin Krause and Andrea Groeppel-Klein. 2026. Technically feasible, ethically questionable? Psychological
pitfalls of digital eavesdropping.Journal of Business Research204 (2026), 115839.
[50] Robert J Lavidge and Gary A Steiner. 1961. A model for predictive measurements of advertising effectiveness.
Journal of marketing25, 6 (1961), 59–62.
[51] Gun Ho Lee, Kyoung Jun Lee, Baek Jeong, and Taekyung Kim. 2024. Developing personalized marketing service
using generative AI.IEEE Access12 (2024), 22394–22402.
[52] Yih Hwai Lee and Charlotte Mason. 1999. Responses to information incongruency in advertising: The role of
expectancy, relevancy, and humor.Journal of consumer research26, 2 (1999), 156–169.
[53] Aurélie Lemmens, Jason Roos, Sebastian Gabel, Eva Ascarza, Hernán Bruno, Brett Gordon, Ayelet Israeli,
Elea McDonnell Feit, Carl Mela, and Oded Netzer. 2025. Personalization and targeting: How to experiment, learn
& optimize.International Journal of Research in Marketing(2025).
[54] Guandong Li and Xian Yang. 2024. Two-stage dynamic creative optimization under sparse ambiguous samples
for e-commerce advertising.SN Computer Science5, 8 (2024), 990.
[55] Yining Li, Chen Huang, Chen Change Loy, and Xiaoou Tang. 2016. Human attribute recognition by deep
hierarchical contexts. InEuropean conference on computer vision. Springer, 684–700.
[56] Lindt & Sprüngli. 2013. Lindt Lindor Milk Chocolate Truffles, 600g. https://www.amazon.de/
Lindt-Lindor-Milk-Chocolate-Truffles/dp/B00BHFD8YCAccessed: January 22, 2026.
[57] Richard J Lutz. 1985. Affective and cognitive antecedents of attitude toward the ad: A conceptual framework.
Psychological processes and advertising effects(1985), 45–64.
[58] Miguel Malheiros, Charlene Jennett, Snehalee Patel, Sacha Brostoff, and Martina Angela Sasse. 2012. Too close
for comfort: A study of the effectiveness and acceptability of rich-media personalized advertising. InProceedings
of the SIGCHI conference on human factors in computing systems. 579–588.
[59] Sandra C Matz, Michal Kosinski, Gideon Nave, and David J Stillwell. 2017. Psychological targeting as an
effective approach to digital mass persuasion.Proceedings of the national academy of sciences114, 48 (2017),
12714–12719.
[60] Sandra C Matz, Jacob D Teeny, Sumer S Vaid, Heinrich Peters, Gabriella M Harari, and Moran Cerf. 2024. The
potential of generative AI for personalized persuasion at scale.Scientific Reports14, 1 (2024), 4692.
[61] John W Mauchly. 1940. Significance test for sphericity of a normal n-variate distribution.The Annals of
Mathematical Statistics11, 2 (1940), 204–209.
[62] Meta. 2026. Advantage+ catalog ads (formerly dynamic ads). Facebook for Business. https://www.facebook.
com/business/m/one-sheeters/dynamic-adsAccessed: 2026-02-01.
[63] Robert S Moore, Melissa L Moore, Kevin J Shanahan, Alisha Horky, and Britney Mack. 2015. Creepy marketing:
Three dimensions of perceived excessive online privacy violation.Marketing Management Journal25, 1 (2015),
42–53.
[64] Donald G Morrison. 1979. Purchase intentions and purchase behavior.Journal of marketing43, 2 (1979), 65–74.
[65] Leopold Müller, Nina Schwarz, Lars Böcking, Andreas Bereczuk, Hanno Stagge, Wolfgang Kratsch, and Niklas
Kühl. 2025. Data-centric fine-tuning of small language models for automatic extraction of technical requirements.
IEEE access(2025).
[66] Kyle B Murray and Gerald Häubl. 2009. Personalization without interrogation: Towards more effective interactions
between consumers and feature-based recommendation agents.Journal of Interactive Marketing23, 2 (2009),
138–146.
[67] Maxim Naumov, Dheevatsa Mudigere, Hao-Jun Michael Shi, Jianyu Huang, Narayanan Sundaraman, Jongsoo Park,
Xiaodong Wang, Udit Gupta, Carole-Jean Wu, Alisson G Azzolini, et al. 2019. Deep learning recommendation
model for personalization and recommendation systems.arXiv preprint arXiv:1906.00091(2019).
[68] Nizar Nazrin, Farah Merican Isahak Merican, Nurul Shima Taharuddin, and Nor Idayu Ibrahim. 2025. How
AI-generated images impact consumer perceptions and brand identity.Idealogy Journal10, 1 (2025), 291–298.
21

Enabling and Understanding Personalization in AI-Generated Advertising ImageryPREPRINT
[69] Bhavik Pathak, Robert Garfinkel, Ram D Gopal, Rajkumar Venkatesan, and Fang Yin. 2010. Empirical analysis
of the impact of recommender systems on sales.Journal of Management Information Systems27, 2 (2010),
159–188.
[70] Dimple Patil. 2024. Generative artificial intelligence in marketing and advertising: Advancing personalization and
optimizing consumer engagement strategies.Available at SSRN 5057404(2024).
[71] Alisa Petrova, Lucia Malär, Wayne Hoyer, and Harley Krohmer. 2025. The Phenomenon of Creepiness in a Digital
Marketing World.Psychology & Marketing(2025).
[72] James Phoenix and Mike Taylor. 2024.Prompt engineering for generative AI. " O’Reilly Media, Inc.".
[73] Polestar. 2024. Polestar 4 offiziell in Europa und Australien eingeführt. https://media.polestar.com/ch/
de/media/pressreleases/666140Accessed: January 22, 2026.
[74] Prolific. 2025. Prolific.https://www.prolific.com. Version accessed January 2026. London, UK.
[75] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry,
Amanda Askell, Pamela Mishkin, Jack Clark, et al . 2021. Learning transferable visual models from natural
language supervision. InInternational conference on machine learning. PmLR, 8748–8763.
[76] Rimowa. 2026. Original Cabin S. https://www.rimowa.com/de/en/luggage/colour/silver/cabin-s/
92552004.htmlAccessed: January 22, 2026.
[77] Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. 2022. High-resolution
image synthesis with latent diffusion models. InProceedings of the IEEE/CVF conference on computer vision and
pattern recognition. 10684–10695.
[78] Stephan Schlosser and Anja Mays. 2018. Mobile and dirty: Does using mobile devices affect the data quality and
the response process of online surveys?Social Science Computer Review36, 2 (2018), 212–230.
[79] Prem N Shamdasani, Andrea JS Stanaland, and Juliana Tan. 2001. Location, location, location: Insights for
advertising placement on the web.Journal of Advertising Research41, 4 (2001), 7–21.
[80] Geeta Sharma and Dr Ruhi Lal. 2024. User Engagement and Perception on social media: An Analysis of
AI-Generated vs Human-Generated Images in Digital Advertising Campaigns.Available at SSRN 4998135
(2024).
[81] Veronika Shilova, Ludovic Dos Santos, Flavian Vasile, Gaëtan Racic, and Ugo Tanielian. 2023. Adbooster:
Personalized ad creative generation using stable diffusion outpainting. InWorkshop on Recommender Systems in
Fashion and Retail. Springer, 73–93.
[82] Paweł Smoli´nski, Joseph Januszewicz, and Jacek Winiarski. 2023. Towards completely automated advertisement
personalization: An integration of generative AI and information systems. In31st International Conference on
Information Systems Development (ISD 2023). Instituto Superior Técnico.
[83] Ching-I Teng, Li-Shia Huang, and Pin-Chun Hsieh. 2010. How to use technical terms in ads? An FCB grid
perspective.British Journal of Management21, 4 (2010), 1044–1056.
[84] Tide. 2020. Tide Hygienic Clean Heavy Duty 10X Free Power PODS, Laundry Detergent Soap, Original
Scent, 60 Count. https://www.amazon.co.uk/Tide-Hygienic-Detergent-Original-Compatible/dp/
B08QBV9DJ5Accessed: January 22, 2026.
[85] Rita Ngoc To, Yi-Chia Wu, Parichehr Kianian, and Zhe Zhang. 2025. When AI doesn’t sell Prada: Why using
AI-generated advertisements backfires for luxury brands.Journal of Advertising Research65, 2 (2025), 202–236.
[86] Shanu Vashishtha, Abhinav Prakash, Lalitesh Morishetti, Kaushiki Nag, Yokila Arora, Sushant Kumar, and
Kannan Achan. 2024. Chaining text-to-image and large language model: A novel approach for generating
personalized e-commerce banners. InProceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery
and Data Mining. 5825–5835.
[87] Richard Vaughn. 1980. How advertising works: A planning model.Journal of advertising research20, 5 (1980),
27–33.
[88] William L. Wilkie. 1994.Consumer Behavior. New York : Wiley.
[89] Hao Yang, Jianxin Yuan, Shuai Yang, Linhe Xu, Shuo Yuan, and Yifan Zeng. 2024. A new creative generation
pipeline for click-through rate with stable diffusion model. InCompanion Proceedings of the ACM Web Conference
2024. 180–189.
[90] Ingo Zettler and Cecilie Fenja Strandsbjerg. 2025. Personalized interventions.Current opinion in Psychology
(2025), 102147.
22
