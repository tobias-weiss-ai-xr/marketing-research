---
title: 'Product Design Using Generative Adversarial Network: Incorporating Consumer Preference and External
  Data'
url: https://arxiv.org/abs/2405.15929
category: consumer-behavior
subcategory: empirical
date: 2024-05
venue: ''
authors:
- Hui Li
- Jian Ni
- Fangzhu Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.15929
pages: 50
chars: 102169
fetched_at: '2026-11-08T13:06:19+00:00'
kb_version: 1
---

# Product Design Using Generative Adversarial Network: Incorporating Consumer Preference and External Data

Product Design Using a Generative Adversarial
Network: Incorporating Consumer Preferences and
External Data
Hui Li∗, Jian Ni †, Fangzhu Yang‡
May 22, 2025
Abstract
The rise of generative artificial intelligence (AI) has facilitated automated product
design but often neglects valuable consumer preference data within companies’ internal
datasets. Additionally, external sources such as social media and user-generated con-
tent (UGC) platforms contain substantial untapped information on product design and
consumer preferences, yet remain underutilized. We propose a novel framework that
transforms the product design paradigm to be data-driven, automated, and consumer-
centric. Our method employs a semi-supervised deep generative architecture that sys-
tematically integrates multidimensional consumer preferences and heterogeneous exter-
nal data. The framework is both generative and preference-aware, enabling companies
to produce consumer-aligned designs with enhanced cost efficiency. Our framework
trains a specialized predictor model to comprehend consumer preferences and utilizes
predicted popularity metrics to guide a continuous conditional generative adversarial
network (CcGAN). The trained CcGAN can directionally generate consumer-preferred
designs, circumventing the expenditure associated with testing suboptimal candidates.
Using external data, our framework offers particular advantages for start-ups or other
resource-constrained companies confronting the “cold-start” problem. We demonstrate
the framework’s efficacy through an empirical application with a self-operated photog-
raphy chain, where our model successfully generated superior photo template designs.
We also conduct web-based experiments to verify our method and confirm its effective-
ness across varying design contexts.
Keywords: Product design, generative models, deep learning, user-generated content (UGC)
∗HKU Business School, University of Hong Kong, Hong Kong. Email: huil1@hku.hk.
†Pamplin College of Business, Virginia Tech. Email: jiann@vt.edu.
‡Economics Division, Bates White. Email: Fangzhu517@hotmail.com.
1
arXiv:2405.15929v3  [econ.GN]  21 May 2025

INTRODUCTION
Product design is crucial for firms to attract consumers and succeed. Traditionally, this
involves hiring professional designers to create small batches of new designs, which is costly
and lacks scalability. To evaluate attractiveness of new designs, companies need to gather
consumer feedback through focus groups, surveys, and market tests, such as A/B tests or
theme clinics. Theme clinics are usually expensive, with vehicle design tests costing over
$100,000 (Burnap et al. 2023). After collecting feedback, firms analyze it using techniques
such as conjoint analysis (Green and Srinivasan 1990), choice modeling (McFadden 1986),
and preference mapping (Urban and Hauser 1993). The insights derived from the analyses
are then used to refine designs to maximize market share or profits (Allenby and Rossi
1998). This iterative, manual process results in significant delays from concept development
to market launch.
The rapid advancement of generative AI has the potential to significantly accelerate the
product design process. In the design generation phase, generative AI enables industrial
designers to quickly explore a wider array of ideas and develop initial concepts much faster
than traditional methods (McKinsey & Company, 2023). For instance, generative AI text-
to-image tools like DALL-E, Stable Diffusion, and Midjourney can be used to design clothing
of a specific style through iterative prompting. 1
However, a significant gap exists in current AI applications for product design: the design
generation stage lacks systematic integration of large-scale consumer preferences (Burnap
et al. 2023). AI tools are typically used either before design generation to analyze consumer
data and identify needs or after to predict demand for new designs (Dzyabura and Hauser
2011; Toubia et al. 2003). During design generation, consumer preferences are either missing
or incorporated in a limited, ad hoc manner. Although text-to-image tools enable design
generation through iterative prompting, these prompts are not systematically generated and
1https://openai.com/index/dall-e-3/ ,https://stability.ai/news/stable-diffusion-3 ,https:
//www.midjourney.com/home
1

may fail to capture diverse consumer tastes. Additionally, the attractiveness of the generated
designs to consumers remains uncertain. Predicting consumer demand occurs after design
creation, potentially leading to wasted resources on developing and testing unpopular designs.
In contrast to the lack of incorporating consumer preferences into generative AI appli-
cations, rich consumer preference information exists in user-generated content (UGC) and
remains underutilized by companies in practice. UGC naturally contains valuable consumer
insights, as users voluntarily create content. For instance, social media and UGC sites host
numerous user-taken photos in various settings, indicating user preferences for those back-
grounds. These images can help understand consumer evaluations of new photo backgrounds
and serve as inputs for training generative models to create new photo background designs.
Despite the wide availability of UGC data, their usage in marketing is mostly descriptive
and focuses on extracting preferences or predicting demand. Prescriptive usage of UGC
for product design is scant both in marketing academia and in practice. There is no clear
guidance on using unstructured UGC data for direct unstructured product designs.
Additionally, finding a scalable solution to integrate consumer preferences and leverage
UGC data poses challenges. Developing a generative AI algorithm can be expensive, poten-
tially unaffordable for many companies. Training such algorithms requires large datasets,
which may be unavailable to small or startup companies facing a “cold-start” problem. Fur-
thermore, even after training, generating new designs can be costly due to the high time
costs and prices of generative AI tools (see the literature review for a detailed discussion).
Our study addresses existing gaps by focusing on three key questions: (1) How can
consumer preference information be integrated into the product design process to guide
generative AI in creating appealing designs? (2) How can firms utilize the rich design and
preference data in UGC during the design generation stage, particularly for those facing
“cold-start” issues? (3) How can the design generation process be automated systematically,
scalably, and cost-effectively?
We propose a novel framework to transform the product design process in the era of gen-
2

erative AI. Our approach utilizes a semi-supervised deep generative framework based on Gen-
erative Adversarial Network (GAN) to automatically and cost-effectively create consumer-
preferred product designs. Compared to other generative models such as diffusion models
(see the literature review for a detailed comparison), our model offers several advantages: 1)
it generates realistic images; 2) it is prompt-free, eliminating the need for textual prompts;
3) it incorporates large-scale consumer preferences; 4) it leverages UGC; 5) it enables fast
and cost-effective design generation; 2 6) it is tailored for personalized design generation.
To illustrate the practical application of our framework, we conduct an empirical study
with a self-operated photography chain in China. This company operates photo booths in
major city shopping malls, allowing customers to select templates, take photos, and print
them. As the photo templates are key products, it is crucial for the company to design
appealing ones to attract customers. Traditionally, this would involve hiring professional de-
signers and conducting costly consumer tests for each design. As a start-up with limited re-
sources and internal data, the company faces a “cold-start” problem. Our framework enables
the company to systematically integrate revealed preferences from both internal consumer
choices and external UGC sources, facilitating rapid and concurrent design generation and
evaluation. This approach transforms the process from a sequential design-then-test method
to an integrated design-with-preferences strategy, fundamentally changing how firms can
develop consumer-oriented products in the era of generative AI.
The self-operated photography chain provides us internal dataset that contains 2195
consumers who had taken at least one photo between October 2017 and August 2018. For
each consumer, we observe her full order history, including her selected photo templates and
the photos taken with these chosen templates. The mapping from internal consumers to
their chosen templates represents internal consumer preference. We further collect external
images from UGC websites. These external images are of similar types to those of the
internal images, with humans taking photos in front of various backgrounds. They represent
2Our trained model can generate a new design in just 0.01 seconds using a consumer-grade laptop, whereas
state-of-the-art diffusion models require at least 10 seconds and rely on 2 to 3 enterprise-grade GPUs.
3

both existing external designs and external consumer preferences.
We apply our proposed framework to this empirical context. The framework includes a
predictor model that learns consumer preferences and a generative model that uses these
predictions to guide design generation. We present variations of the generative model to
highlight the framework’s benefits, starting with a deep convolutional GAN (DCGAN) that
generates new designs from internal and external existing designs in UGC without incorpo-
rating consumer preferences. Next, we integrate consumer preferences into the generative
process by adapting continuous conditional GAN (CcGAN) from Ding et al. (2020) to our
context. Unlike traditional GANs, CcGAN can directionally generate specific types of images
by using image labels as additional inputs to train the generator, making it ideal for incor-
porating consumer preferences. We first train a predictor model with historical consumer
choice data to learn preferences, then use these predicted choice probabilities as additional
input labels to train the CcGAN. Importantly, we modify the original CcGAN in Ding et al.
(2020) to accommodate the ordinal nature of consumer preference labels. The trained Cc-
GAN is then instructed to generate new product designs with higher choice probabilities.
We explore two CcGAN versions: an enhanced model using only internal consumer prefer-
ences for training the predictor and an advanced model utilizing both internal and external
preferences, representing our final framework version. We show that the advanced model
can be easily adapted to create personalized designs for individual consumers.
The performance of the generated templates is evaluated through three methods. First,
a distance-based metric is employed to assess the similarity of the generated templates to
popular existing ones. Popular templates share common features that consumers favor. We
use the Caffe BVLC reference model (Jia et al.,2014) to obtain embeddings for both existing
and generated templates. We calculate the distance between generated templates and the
most popular and unpopular existing templates. A smaller (larger) distance to the most
popular (unpopular) templates suggests higher potential popularity. Second, consumer eval-
uations are gathered through an online survey where participants choose between existing
4

and newly generated templates, simulating a real-world photo booth environment to gauge
direct consumer preferences. Lastly, we use the trained predictor to calculate the choice
probabilities of the generated templates, providing an analytical measure of their expected
popularity based on historical data and consumer behavior patterns. Together, these meth-
ods offer a comprehensive evaluation of the templates’ performance by considering similarity
to established popular templates, direct consumer feedback, and predictive analytics.
The evaluation methods consistently indicate that the advanced model, which integrates
both internal and external consumer preferences, performs the best. The designs generated
by this model are predicted to be more favored by consumers, as confirmed by the distance-
based metric, real consumer feedback, and the predictor model. The external dataset plays
a crucial role in this process. It provides valuable training inputs for the generative models,
enabling them to incorporate new product features from external designs and address the
limitation of style variations in the internal data. Additionally, the rich external preferences
allow the predictor model to identify popular features from external sources, guiding the
generative model to create novel and attractive designs that are absent in the internal data.
Two key insights emerge from the analyses: First, relying solely on internal preferences is
insufficient. Incorporating external preferences is crucial as they offer additional insights into
how consumers evaluate external designs. Without this information, the generative model
may fail to integrate popular features from external designs that are missing in internal
ones. Second, adapting the CcGAN model to acknowledge the ordinal nature of consumer
preference labels is essential; without this adaptation, the generated designs perform worse.
We further conduct a personalized design generation exercise. We randomly select an
internal consumer and use the predictor model to estimate his choice probabilities, termed
personalized popularity labels. We use these personalized labels to re-train the general
advanced model. This personalized CcGAN is used to generate new templates tailored to
the consumer’s preferences. The personalized CcGAN outperforms the general CcGANs,
demonstrating our model’s capability of conducting personalized design generation.
5

Our study bridges quantitative marketing research with generative AI advancements.
While marketing literature has focused on understanding consumer preferences to guide
human designers (Hauser and Clausing 1988; Griffin and Hauser 1993), and computer science
has developed generative capabilities without systematic preference integration (Brock et al.
2018), our work merges these approaches to create a framework that is both generative
and preference-aware. This integration enables product design processes to be data-driven,
automated, and consumer-centric, establishing a new paradigm that transforms how firms
make product design decisions.
Managerially, our work offers an automated product design solution that is particularly
beneficial for smaller start-up firms facing cold-start issues and budget constraints. Firms
typically possess internal data regarding their existing product designs and consumer choices.
Our framework allows them to systematically, scalably, and cost-effectively integrate product
design ideas and consumer preferences from external websites. It also dynamically evolves as
more internal and external data are incorporated, enabling firms to quickly adapt to shifts
in consumer demand.
The framework transforms traditional product design in three key ways: First, it provides
a superior alternative to industry practices relying solely on pure generative models, which
ignore consumer tastes during design generation, necessitating ex post facto screening of
unpopular designs. Our method generates designs preferred by consumers ex ante, reducing
time and resources spent on less appealing options. Second, it offers an effective solution for
product design ideation, moving beyond reliance on human designers with limited capacity.
By leveraging UGC, it captures real-time preferences from a broad user base. Third, it pro-
vides a cost-effective way to obtain consumer evaluations of new designs by using UGC as a
source of self-revealed and dynamic consumer preferences, contrasting with traditional costly
surveys. This approach is applicable in other settings, such as video meeting backgrounds,
where consumer preference information and external resources are abundant.
6

Literature Review
Our paper contributes to the literature on the usage of UGC in marketing. Most of these
studies were descriptive and focused on analyzing UGC to extract information and gain in-
sights for firm operations. Some of them have analyzed textual content. For example, Netzer
et al. (2012) extracted brand associations from UGC on forums. Culotta and Cutler (2016)
extracted the social connections of brands on Twitter. Other works analyzed visual content
(Zhang and Luo, 2023; Zhang et al., 2017; Pavlov and Mizik, 2019) . For instance, Liu et al.
(2020) analyzed consumer-generated images on social media to study the brand perceptions
of consumers. We contribute to the literature by going one step further, from descriptive to
prescriptive work. Our generative model not only extracts information from unstructured
UGC but also uses this information to make unstructured product design decisions for firms.
We contribute to the literature on deep learning models in marketing. Most studies in
this area use unstructured data to generate structured firm insights. For instance, Liu et al.
(2020) collected unstructured image data from social media and used a deep convolutional
neural network (CNN) to extract and predict consumer perceptions of brand attributes.
Our work differs in that we employ unstructured data to directly generate unstructured
firm decisions (i.e., product designs as images) . Our proposed framework goes beyond the
descriptive task and provides prescriptive solutions for the product design decisions of firms.
We also contribute to the nascent literature on deep generative models in marketing. A
few works have used deep generative models to create new product designs. For example,
Dew et al. 2022 used multiview representation learning to design brand logos. Burnap
et al. 2023 proposed a model to augment the commonly used aesthetic design process by
predicting aesthetic scores and automatically generating innovative and appealing product
designs; the predictor model and the generator models were separately trained. Our work
differs in that we incorporate consumer preference information into the generation process
so that the predictor model guides the generative model. We also introduce and adapt the
CcGAN model to the marketing field, allowing us to systematically incorporate consumer
7

preferences in an automated and large-scale manner. In addition, while previous works
generated one aspect of product designs such as logos (Dew et al., 2022) or the aesthetic
appearances of cars (Burnap et al., 2023), we directly design the entire product (i.e., the
photo templates are the products of the firm). This setting allows us to abstract away from
other design factors that might influence consumer choices.
Relationship to other generative models
Our work builds on GAN models, which offer distinct advantages over other generative
models like diffusion models. While diffusion models excel in producing high-resolution im-
ages with fine details, they are more suited for generating surreal scenes and struggle with
practical imagery commonly used for information sharing and creation. 3 Additionally, diffu-
sion models are computationally intensive and slower due to their iterative denoising process.
State-of-the-art diffusion models require at least 10 seconds to generate one image and rely
on 2 to 3 enterprise-grade GPUs. Advanced models like GPT-4o image generation, launched
in March 2025, can produce high-quality realistic images but require textual prompts and
take 30-60 seconds per image, with some taking up to 2 minutes. 4 In contrast, GANs gen-
erate more realistic images, are less computationally demanding, simpler to implement and
tune, and enable faster generation, making them more suitable for our goal of large-scale
product design generation. 5 Our trained model can generate a new design in just 0.01 sec-
onds using a consumer-grade laptop, which is 1,000 times faster than diffusion models. In
addition, considering the difference in hardware requirements, the generation cost can be
8,000 to 12,000 times lower. 6
Another advantage of the GAN models lies in their conceptual attractiveness. Continuous
3https://openai.com/index/introducing-4o-image-generation/
4https://help.openai.com/en/articles/8932459-creating-images-in-chatgpt
5https://www.geeksforgeeks.org/generative-adversarial-networks-gans-vs-diffusion-models/
6Our model can generate an image in 0.01 seconds using a consumer-grade laptop. The cost of using an A WS G4
instance (equivalent to a consumer-grade laptop GPU) is $1.461 to generate 1 million images. In contrast, diffusion
models need 3 enterprise-grade GPUs to generate an image in 10 seconds. The cost for 3* A100 GPUs on A WS is
$12,291 to produce 1 million images. Alternatively, generative AI services like DALL-E 2 charge $18,000 for 1 million
images, while Stable Diffusion 3 costs $35,000 for the same amount of images. The online appendix provides more
calculation details.
8

diffusion models predominantly operate within non-equilibrium thermodynamic frameworks,
utilizing score matching methods that progressively transform noise distributions through
iterative denoising processes governed by stochastic differential equations. This paradigm
inherently embraces non-equilibrium dynamics, where the generative process follows irre-
versible trajectories through probability density spaces. In contrast, our CcGAN architec-
ture extends the min-max game-theoretic framework, which fundamentally aligns with the
equilibrium-seeking conceptualizations prevalent in marketing and applied microeconomics.
This allows our model to converge toward Nash equilibria where generator and discriminator
functions achieve optimal strategic responses to each other, mirroring the equilibrium-based
analytical constructs that underpin consumer preference modeling and market clearing mech-
anisms in microeconomics. The theoretical congruence between CcGAN’s adversarial opti-
mization and economic equilibrium concept is further corroborated by the self-play theorem
proving systems (exemplified by DeepSeek’s architecture), which demonstrate that adversar-
ial self-competition frameworks with primitive reward-punishment signals can systematically
converge toward optimal solutions through iterative strategic adaptation. This mathematical
homology between adversarial generative models and strategic equilibrium-seeking economic
agents provides our framework with superior interpretability within established paradigms,
while maintaining competitive generative performance compared to diffusion-based alterna-
tives.
Our paper relates to the literature on image generation incorporating human preference,
which is a rapidly growing research area in computer vision. State-of-the-art models mainly
use diffusion-based models, as seen in works like Xu et al. (2023) and Wallace et al. (2024).
Our model differs in the following ways. First, existing works focus on text-to-image diffusion
models, in which human preference is represented by prompt alignment, or human ratings
on how well the generated images align with specific text prompts (Xu et al. 2023). By
nature, this type of human preference differs from consumer preferences in marketing, which
focus on the mapping between images and consumers’ tastes. Second, human preference
9

in diffusion models only captures the average person’s preference and overlooks consumer
diversity. For instance, in Xu et al. (2023), preference is vertical, meaning everyone agrees
on image quality rankings. In contrast, marketing highlights horizontal preference, where
consumers have varying tastes in image styles. Our model addresses this by capturing
diverse preferences among heterogeneous consumers. Importantly, our model is well designed
for personalized design generation, which we demonstrate using a personalization exercise.
Third, diffusion models usually require textual prompts as inputs, limiting their ability to
capture large-scale consumer preferences. Our model directly uses unstructured images from
consumer data as inputs without textual prompts. Consumer preference is captured by the
mapping between consumers and their chosen images in an unstructured and flexible way.
Fourth, diffusion models incorporate human preference through an iterative reward feedback
process, which is time-consuming. Our model, based on GANs, uses a min-max operation in
training, significantly accelerating design generation without iterative denoising. It reduces
both training and inference costs for companies.
CONCEPTUAL FRAMEWORK
Overview of the Conceptual Framework
We propose a semi-supervised deep generative framework for systematically and cost-
effectively generating consumer-preferred product designs. Our model offers three key ad-
vantages. First, it enables firms to utilize external product designs from sources like social
media and image websites, benefiting startups with limited internal designs. Second, it inte-
grates consumer preferences from a firm’s internal data to ensure generated designs align with
consumer interests. Third, it incorporates external consumer preference information, allow-
ing firms to access and leverage the abundant consumer insights available in user-generated
content (UGC). To demonstrate these three advantages, we present three versions of the
generative model. The first is a baseline model that uses product designs from both inter-
nal and external sources, showcasing the benefit of leveraging external designs from UGC.
10

The second variant enhances the baseline by incorporating consumer preference data from
a firm’s internal sources, illustrating how internal preferences can guide the generation of
more appealing designs. The third variant is the complete model, integrating product de-
sign and consumer preference information from both internal and external sources, thereby
demonstrating all three advantages of our framework. This subsection outlines the concepts
and workflows of the three models, with implementation details provided in the following
subsections.
Figure 1: Proposed Machine Learning Model for Generating New Designs
Baseline model: DCGAN without consumer preferences
The baseline model uses existing product designs from both internal and external sources,
as shown in Figure 1. The internal datasets of firms contain existing product designs that
can be used as generative model inputs. However, these internal designs are usually limited
in both quantity and style variety, especially for start-up firms that face cold-start problems.
To overcome this difficulty, we gather existing product designs from external sources such
11

as UGC on social media and image websites. UGC contains a rich set of images and image
features. Utilizing UGC as inputs not only increases the size of the training dataset but also
introduces new image features to the generative process; both of these factors enhance the
performance of the generative model.
Following industry standards, we use GANs (Goodfellow et al., 2014) to generate new
product designs in the baseline model. We choose GAN models over other generative models
such as fully visible belief networks (FVBNs) (Frey, 1998) and variational autoencoders
(V AEs) (Kingma and Welling, 2013; Rezende et al., 2014) because GANs were designed
to avoid the many disadvantages associated with other generative models. As we focus on
image synthesis-based tasks, we use the DCGAN (Radford et al., 2015), which is considered
one of the most important steps forward in terms of designing and training stable GANs.
Enhanced model: CcGAN with internal consumer preferences
Although the baseline model can generate new product designs in an automated, scalable,
and efficient manner, it does not incorporate consumer preference information. Therefore,
the newly generated designs may not fit consumer needs, and consumers may choose not to
buy these new products. This is a general limitation encountered in most GAN applications
in practice: GANs are used in an engineering sense without incorporating business insights
and consumer needs.
We propose an enhanced generative model that incorporates consumer preference in-
formation into the generative process in an automated and large-scale manner. To our
knowledge, this is one of the first studies to incorporate consumer preferences into a gen-
erative model. Most of the previous studies used consumer preference information only in
prediction tasks. For example, Burnap et al. (2023) used consumer preference information to
train a predictor model and applied the predictor model to predict how consumers perceived
new product designs; the new product designs, however, were generated without incorporat-
ing consumer preference information. We differ in that we incorporate consumer preference
information jointly in the predictor model and generator model. In particular, the predic-
12

tor model captures consumer preferences and is used to guide the process of designing new
products in the generator model. Therefore, the generator model can generate new products
that are more likely to be preferred by consumers in a targeted manner.
The internal consumer preference information that we incorporate into the model comes
from consumers’ historical product choices in the internal data of firms. Our empirical appli-
cation is employed as an example. The internal data of the firm contains the photo templates
that a particular consumer chose and the corresponding photos taken by the consumer with
the chosen templates. Each photo taken contains both the consumer’s appearance and the
chosen photo template. These consumer choices represent the types of product designs that
a particular consumer prefers.
We first train a predictor model to learn the internal preferences of consumers, which we
incorporate into the generative process. The predictor model utilizes the historical photos
taken by internal consumers as inputs. It learns a mapping between a consumer’s appear-
ance (i.e., her facial traits) and her preferred product designs, assuming that consumers
with similar appearances will prefer similar product designs. To address the high dimen-
sionality of the target problem, we preprocess the observed consumer faces and product
designs using embedding models, obtaining low-dimensional vector representations for both
consumer appearances and product designs. Using these embeddings as inputs, we train a
deep prediction model to capture high-level abstractions in the prediction task. We call this
predictor model with internal preferences “Prediction Model 1,” as illustrated in Figure 1.
The trained predictor model can be used to predict the popularity of any given product de-
sign. Specifically, for each pair consisting of a product design and an internal consumer, the
trained predictor calculates the probability that this consumer will choose the corresponding
product. By averaging over the selection probabilities among all internal consumers, we can
obtain a popularity measure of the particular product.
The trained predictor model is further integrated into the generator model in a semi-
supervised deep learning framework. We employ a conditional GAN model (Mirza and
13

Osindero, 2014), which extends the traditional GAN by enabling the conditional generation
of outputs. Intuitively, the traditional GAN can use a set of dog images to produce a new set
of dog images, but one cannot instruct the model to create images of a specific type of dog.
The conditional GAN allows one to condition the network on additional information such
as class labels. During training, the conditional GAN takes images with labels (bulldogs,
golden retrievers, etc.) as inputs and learns the differences between the images with different
labels. In this way, it gains the ability to generate new images with a specific label (a specific
type of dog).
The conditional GAN is well suited for our task because it allows us to incorporate
consumer preferences and generate new product designs that are more likely to be chosen by
consumers. In our context, we use the popularity measures derived from the predictor model
as additional inputs (i.e., class labels of product designs). The predicted popularity levels
guide the training procedure of the conditional GAN so that internal consumer preferences
are incorporated into the generative model. Once the generative model is trained, we can
instruct the model to generate new product designs with higher popularity levels. In this
way, the conditional GAN can generate new designs that are more appealing to consumers.
A key contribution of our proposed framework is that we introduce the conditional GAN
to marketing applications and adapt it to suit our context. First, conditional GAN models
typically use categorical labels as additional inputs, while the predicted popularity measures
in our context are continuous class labels. To address this issue, we employ the CcGAN that
was introduced by Ding et al. (2020). The CcGAN is an extension of the conditional GAN
model, and it was designed to generate images based on continuous, scalar conditions. By
redefining the conventional conditional GAN approach to make it suitable for continuous
scenarios and introducing a novel method that can integrate continuous labels into the
generation process, the CcGAN outperforms the conditional GAN in terms of effectively
handling continuous labels.
Second, rather than using CcGAN from Ding et al. (2020) as-is, we modify it to suit our
14

context by accounting for the ordinal nature of popularity labels. In Ding’s applications, the
continuous labels represent yaw angles of 3-D chair models and human ages, which do not
imply preference (e.g., age 15 is neither better nor worse than age 30). However, in our case,
higher popularity levels indicate greater consumer preference; we aim to generate designs
with higher popularity. To address this, we adapt CcGAN to recognize the ordinal nature
of popularity labels by modifying its loss function to include label weights. Further details
are provided in the following subsections.
Advanced model: CcGAN with internal and external consumer preferences
One limitation of the enhanced model is that the predictor model is trained only on
internal consumer choices and lacks exposure to diverse design styles that are not present
in the internal data. Consequently, the predictor model may struggle to understand how
consumers evaluate new design styles from the external product designs. Even if the gener-
ative model is trained on both internal and external product designs and is able to produce
“out-of-the-box” styles (i.e., styles that are not present in the internal designs), the predictor
model may not recognize their attractiveness, which limits the performance of the CcGAN.
Another limitation of the enhanced model is that it does not fully utilize the informa-
tion contained in external UGC. By nature, UGC data inherently contain rich consumer
preference information, as users voluntarily generate the content. In our context of photo
templates, the UGC on social media and image websites usually contains a vast set of photos
taken by individual users in front of various backgrounds. This type of image represents not
only a rich trove of product design data (i.e., the backgrounds in the case of photo templates)
but also a valuable source of consumer preference information. The fact that an individual
user chose to take photos in front of a particular background means that the user likes the
background. As such, the external images can also be used to train the predictor model to
understand how consumers evaluate new features in external product designs.
We propose an advanced model that integrates both internal and external consumer
preferences when generating new product designs. While the previous studies used external
15

images as extra inputs for training their generative models (Burnap et al., 2023), we further
exploit the consumer preferences revealed in the external data to train both the predictive and
generative models. Therefore, we can make the most of the available UGC since it contains
rich consumer preference information. Such an approach also saves firms the significant
time and money they would have spent on conducting ex post consumer product tests. As
discussed in Burnap et al. (2023), firms often employ A/B tests, or “theme clinics”, to ask
consumers to evaluate different aesthetic designs to improve their product designs. These
theme clinics are costly, as firms usually spend more than $100,000 to conduct a single
vehicle design test. Therefore, utilizing consumer preferences derived from external UGC
is especially useful for start-up firms with limited resources. By directly using the existing
consumer preference information contained in UGC, our proposed model significantly reduces
the cost of gathering consumer preference information.
The advanced model follows a workflow similar to that of the enhanced model except
for the fact that the predictor model is trained on both internal and external consumer
preferences. Following the same logic as that used for the internal data, the predictor model
learns the mappings between the users’ appearances and the backgrounds in the UGC images.
Upon pooling the mappings between the consumer appearances and product designs in both
the internal and external datasets, the trained prediction model captures a larger set of
consumers and their preferences over a wider variety of product designs. The predictor
model is labeled “Prediction Model 2” in Figure 1. Compared with Prediction Model 1, this
version can recognize popular out-of-sample features from external designs.
The remainder of the workflow is the same as that of the enhanced model. We use
the trained predictor model to compute average choice probabilities for each product. The
average choice probability of a product serves as its popularity measure and is then used as a
continuous label in the CcGAN, guiding the model to generate popular images. Importantly,
the new predictor model overcomes the limitations of the previous predictor model, which
only recognizes popular product features within internal consumer preferences. The new
16

popularity measure represents a wider range of consumer preferences over a wider range
of product designs. Consequently, the CcGAN with both internal and external consumer
preferences is able to generate new product designs that better incorporate the new features
acquired from the external data.
As shown in Figure 1, the external dataset serves two purposes. First, the product
features obtained from the external data enhance the training processes of GAN models.
This addresses the issue regarding the limited style variations contained in the internal data
by introducing additional style diversity to train the GAN models to generate improved
designs. Second, the rich trove of external preferences inherent in the external data guides
the GAN models to generate more appealing designs that go beyond the scope of the internal
preferences and designs.
Comparing the three models highlights the advantages of integrating external designs
and consumer preferences into product design generation. Our full model, CcGAN with
internal and external consumer preferences, is a semi-supervised deep generative framework
that automatically and cost-effectively creates consumer-preferred designs. Unlike previous
studies that used consumer preference data solely for predictor models, we incorporate this
data into both predictor and generator models. Predicted popularity serves as both a label
and an input for the generator, enabling it to create products likely to appeal to target
consumers. Additionally, we utilize UGC from external sources to enrich the generative
model with diverse designs and new features absent from internal data. The extensive
consumer preference information in UGC enhances the model’s ability to identify popular
features not evident in internal consumer data.
Prediction Model
This subsection describes the detailed procedure for training the prediction model, as
shown in Equation 1. The primary inputs of the prediction model consist of consumer
appearances (i.e., consumer faces in our empirical context) and product designs (i.e., photo
17

templates or backgrounds in our empirical context). Given the high dimensionality of the
input data, we preprocess the given images by embedding them into a lower-dimensional
vector space. For consumer faces, we follow the deep neural network implemented by the
OpenFace project (Amos et al., 2016). As illustrated in the online appendix, this architecture
was trained for facial recognition. It first detects and crops faces from a given image. Then,
it produces a 128-dimensional intermediate layer through a deep neutral network, which
represents a low-dimensional embedding of the face image. For the product design images,
we adopt the Caffe BVLC reference model (Jia et al., 2014) to obtain image embeddings.
This model uses the CNN designed by Alex Krizhevsky (AlexNet) with some modifications,
as shown in the online appendix. It provides pretrained general networks that can be used to
obtain low-dimensional embeddings of image characteristics. Using the pretrained weights
of the Caffe BVLC reference model, we can directly go to fully connected (fc) layer 8 to
obtain a 1000-dimensional intermediate layer that captures the visual characteristics of the
input product design image.
Consumer faces
OpenFace
− − − − − − →128-dimensional vector: − →X i
Product design images
Caffe BVLC
− − − − − − − − →1000-dimensional vector: − →V j
Other product characteristics − →Z j


 Concatenated input vector
(1)
Let the vector − →X i denote the 128-dimensional embedding of consumer i’s face. Let the
vector − →V j denote the 1000-dimensional embedding of product design j. Let the vector − →Z j
denote any other low-dimensional product characteristics that affect consumer’s product
choices. We concatenate these three vectors to form the final input vector for training the
predictor model. Let Yij denote the outcome variable, or the choice outcome for consumer-
product pair ( i, j). Yij = 1 if consumer i chooses product j, and Yij = 0 otherwise. The
predictor model is trained to learn the nonlinear relationship between the input and output
18

variables:
Yij = f (− →X i, − →V j, − →Z j|θ, ε),
where θ is the model parameter to be estimated. Since the prediction task is a classification
problem with relatively high-dimensional inputs, we adopt a random forest to estimate the
model parameter θ. After obtaining the trained predictor, we can use it to calculate the
probability that consumer i will choose product j:
pij(bθ) = Pr(Yij = 1|− →X i, − →V j, − →Z j; bθ)
By averaging over the choice probabilities of all consumers in the sample, we can obtain an
aggregate popularity measure for product j:
Pj(bθ) = 1 N X i∈I pij(bθ), (2)
where I denotes the total consumer set andN is the size of the consumer base. The aggregate
popularity measure is later incorporated into the constructed generative models to guide the
process of generating new product designs. 7
We train two prediction models: one with internal preferences only and another with both
internal and external preferences. We train these two prediction models via similar training
processes. The difference is that Prediction Model 1 is trained with internal consumer
appearances and product designs only, while Prediction Model 2 is trained using both internal
and external consumer appearances and product designs. Note that external consumers are
used in the training stage of Prediction Model 2 but not in the prediction stage; when
using the trained models to calculate the aggregate popularity measures, we average over
the choice probabilities of the internal consumers only for both Prediction Models 1 and 2.
7Using aggregate popularity labels guides generative models to create designs with higher average popularity.
Using individual popularity labels, as demonstrated in the personalization section, enables personalized design gen-
eration for specific consumers.
19

This is because we are interested in predicting whether the internal consumers of firms prefer
the new template designs. The external consumer preference information still enhances the
performance of Prediction Model 2 by training the model to recognize popular design features
in external designs. The underlying assumption is that external consumers with similar
appearances to those of the internal consumers share similar preferences. Therefore, learning
the preferences of the external consumers helps us infer internal consumers’ preferences for
the new design features from the external designs.
Generative Models
This subsection describes the detailed procedure for training the generative models.
When training the baseline model without consumer preferences, we adopt the standard
and well-established model architecture of the DCGAN method (Radford et al.,2015) to
generate new images. This model takes existing internal and external designs as real image
inputs and identifies a set of parameters that enables the samples generated from random
noises to closely resemble the training data. As the training process is unsupervised and
lacks consumer preference information, the generated images are not necessarily preferred
by consumers.
When training the enhanced model with internal preferences, we estimate a conditional
GAN model and let the internal consumer preferences guide the generator to produce
consumer-preferred designs. Specifically, we build on the CcGAN model developed by Ding
et al. (2020) which is designed for image generation based on continuous labels and utilizes
a novel empirical generator loss and a unique label input method.
Let M r and M g denote the numbers of real and generated Images, respectively. Let
x ∈ Xdenote an image with a size of d × d. Let y ∈ Ydenote the corresponding label.
We pool together the existing internal and external product designs to form a group of real
images as input images, yielding a sample size of M r. For each image j in the input group,
20

we use Prediction Model 1 to calculate its aggregate popularity measure:
yj = Pj(bθ1), (3)
where bθ1 is the estimated parameter of Prediction Model 1 and Pj(bθ1) is defined in Equation
2. This popularity measure serves as a continuous class label and is fed into both the
generator and the discriminator in the CcGAN to guide the generator when creating new
designs. Specifically, building on Ding et al. (2020), we define the hard vicinal discriminator
loss (HVDL) as
bL(D) = − C1
M r
M r X
j=1
M r X
i=1
Eϵr∼N (0,σ2)
h
wr j · 1 {|yr j +ϵr−yr i |≤κ} N r yr j +ϵr,κ log(D(xr i , yr j + ϵr)) i
− C2
M g
M g X
j=1
M g X
i=1
Eϵg∼N (0,σ2)
h
wg j · 1 {|yg j +ϵg−yg i |≤κ} N r yg j +ϵg,κ log(1 − D(xg i , yg j + ϵg)) i , (4)
where C1 and C2 are constants, xr i and xg i stand for real and generated images, respectively,
yr i and yg i are the popularity labels of xr i and xg i , yr j and yg j are target labels in the datasets,
and ϵr and ϵg are normally distributed random noises. N r yr j +ϵr,k is the number of the yr i that
satisfies |yr j + ϵr − yr i | ≤κ. The label weights {wr j , wg i } are defined to be proportional to the
labels as {wr j = ky r j , wg j = ky g j }, where k is a hyper-parameter that takes a positive value.
The loss function for the generator is defined as
bL(G) = − 1 M g
M g X
i=1
wg i · Eϵg∼N (0,σ2)log(D(G(zi, yg i + ϵg), yg i + ϵg)), (5)
where zi is random noise that follows a normal distribution N (0, I). As demonstrated in
Ding et al. (2020), employing the HVDL allows us to train the discriminator using the images
near y rather then solely relying on images labeled y. This approach addresses the scarcity
of real images for each label value. Additionally, we adopt the innovative input method in
Ding et al. (2020) to incorporate labels into the model. Specifically, in the generator, we
21

add the labels to the feature map of the first linear layer in an elementwise manner. In the
discriminator, we first project the labels to a latent space through an additional linear layer.
We then integrate these embedded labels into the discriminator via label projection.
An important modification we made to Ding et al. (2020) is the introduction of label
weights, {wr j , wg j , wg i }, to the loss functions. In Ding’s work, the continuous labels, such
as yaw angles of 3-D chair models and human ages, do not imply preference. However, in
our context, higher popularity levels indicate greater consumer preference, and we aim to
generate designs with higher popularity. To enable CcGAN to recognize the ordinal nature
of popularity labels, we include label weights, with higher popularity labels assigned larger
weights, indicating their greater importance for the algorithm. As demonstrated in the
result sections, incorporating these label weights significantly enhances the performance of
the generative model.
In summary, combining Equations 3, 4, and 5, we integrate consumer preferences into the
generation process by directly incorporating the popularity measure Pj(bθ) from the predictor
model into the loss functions of both the discriminator and the generator of the CcGAN.
This setup allows us to instruct the generator to create new images with a specific popularity
level.
The advanced model incorporating both internal and external preferences is trained using
a procedure similar to that of the enhanced model. The only difference is that we use the
aggregate popularity measures from Prediction Model 2, Pj(bθ2), as additional input labels
to be fed into the generator and the discriminator. As Prediction Model 2 is trained on both
internal and external consumer choices, the new CcGAN is able to incorporate new design
features from the external sources that are appealing to the internal consumers.
22

INSTITUTIONAL SETTING AND DATA
Institutional Background
As an empirical application, we apply our proposed framework to a real business setting:
a self-operated photography chain in China. The company operates self-operated photo
booths in approximately twenty shopping malls in major cities. The photo booths allow
consumers to choose photo templates, take photos with the chosen templates, and print
their photos. The photo booths are self-operated, so consumers follow the instructions on
the photo booth machines. Figure 2 shows the interface of such a photo machine. Four
photo categories can be selected: main (single), friends, family, and lovers. We focus on the
“main” category in our analysis, which is designed for one consumer to take photos.
The decision process of the consumers is as follows. Upon entering the photo booth, the
consumers are asked to choose photo themes. Several pages of themes are available for the
consumers to choose from. The themes range from general topics such as “modern” and
“classic” to very specific topics such as “fruits” and “flowers”. The company constantly
introduces new themes and ranks these themes by recency, with the more recent themes
placed on the first pages on the screen. After clicking on a specific theme, the consumers
are presented with all templates under this theme in a pop-out window, and they choose the
template(s) with which they will take photos. Each template is typically a combination of a
background and a foreground without human subjects involved. For example, Figure 3 shows
four photo templates, two from the “traditional Chinese” theme and two from the “graffiti”
theme. The templates within a specific theme share a similar style, while templates across
themes can differ substantially from each other. After choosing the templates, consumers pay
for a time window (10, 30, or 60 minutes) and use the time to take photos with the chosen
templates. The company charges consumers based on the time they use to take photos, not
the number of templates chosen. Consumers can choose an unlimited number of templates
and take photos as long as they finish within the paid time window.
23

Figure 2: Interface of the Self-Operated Photography Booth
Figure 3: Examples of Photo Templates
(a) Graffiti Theme (b) Traditional Chinese Theme
As it is in its early development stage, the company does not have a systematic and cost-
effective way to design new themes or new templates due to internal resource limitations.
The company hires outside designers to create new designs without incorporating consumers’
aesthetic preferences. The process of ideating the new themes and designs is not systematic,
either, except that holiday-related themes are introduced during holiday seasons. The com-
pany manages existing and new designs in a relatively unsophisticated and ad hoc manner:
they introduce new designs at a constant pace and remove existing themes that turn out to
be unpopular. Our proposed framework can help the company generate new designs in a
24

systematic, cost-effective, and automated way. In particular, the generation process incor-
porates consumers’ heterogeneous preferences and leverages valuable designs and preference
information derived from external sources.
Internal Data
The internal dataset obtained from the company contains two parts. The first part
includes the original template images that the company offered to customers, without the
presence of consumers inside the images. The company offered 83 photo themes in total
during the observation period. Each theme contains 1 to 13 templates, yielding a total
of 585 templates across all the themes. The second part of the internal dataset contains
the complete order histories of 2195 consumers who had taken at least one photo between
October 2017 and August 2018. For each consumer, we observe their selected themes and
templates and the photos taken with the chosen templates. We also observe the ranking
orders of the themes offered on the screen at the times they made their choices.
The internal data patterns suggest that the templates vary significantly in popularity
both across themes and within the same theme, potentially due to different design features
and heterogeneous consumer preferences. The variation in template popularity, especially
the presence of low-popularity templates, suggests that the company needs to improve the
attractiveness of its template designs. As another piece of evidence, the internal dataset
shows that only 2195 out of the 6038 registered consumers ended up taking photos in the
booth after browsing the photo template options. Among the 2195 consumers, fewer than
100 consumers made multiple store visits, and only 15% of the consumers had repeated
time purchases. These numbers suggest that the company can benefit from incorporating
consumer preferences to generate better designs that are appealing to consumers.
25

External Data
To leverage the existing designs and consumer preference information derived from ex-
ternal sources, we further collect an external dataset from two main sources: social media
and online image websites. Social media reflects various aspects of consumer tastes, whereas
image websites contain a variety of photos with different themes. We collect specific types
of photos from these websites, i.e., photos taken by individual users in front of specific types
of backgrounds, which are similar to the photo-taking setting in our case. The backgrounds
in these external photos can serve as additional design templates for training the generative
model. The mappings between the individuals and the backgrounds in these photos can
serve as additional consumer preference information to train the prediction model.
After gathering the external images with human objects and backgrounds, we preprocess
the images before they are used as inputs for the proposed model. Specifically, training the
model requires a set of pure templates without human objects and a set of consumer face
images, while the raw external images we collect are combinations of template backgrounds
and consumer faces, so we need to separate the two components. For each external image,
we remove the human object in it and inpaint the remaining part of the image to obtain
a complete background image, which is similar to the pure template images in the internal
dataset. Additionally, we save the cropped human faces as new images, which are similar to
the consumer face images in the internal dataset. Figure 4 presents examples of the internal
templates, raw external photos, inpainted external templates, and cropped consumer faces,
all from the graffiti theme. As shown in the graphs, the collected external images are similar
in style to the internal images and have sufficient variations. The inpainting process works
well and can generate high-quality templates and consumer face images.
26

Figure 4: Examples of Graffiti Templates: Internal vs. External
(a) Internal images (b) External images (raw, inpainted, cropped)
APPLYING MODEL TO PRACTICE
We apply the proposed model to generate new product designs for the unmanned photo
gallery firm. This section describes the implementation details.
Training the Prediction Model
The feature embeddings of consumer faces and background templates serve as the inputs
for the prediction model. Regarding the consumer face features, most consumers took more
than one photo, so multiple face images are available for each consumer. We first obtain
the embedding of each face image. We then average across the embeddings of the same
consumer to obtain a 128-dimensional facial vector − →X i for that consumer. With respect to
the template features, in addition to the 1000-dimensional embeddings of the visual char-
acteristics − →V j, we also include the display ranking of each template on the screen − →Z j, as
its display ranking affects its probability of being chosen. Concatenating − →X i, − →V j, and − →Z j
yields a 1129-dimensional feature input for training the prediction model.
27

Consumer faces
OpenFace
− − − − − − →128-dimensional vector: − →X i
Photo templates
Caffe BVLC
− − − − − − − − →1000-dimensional vector: − →V j
Template display rankings scalar: − →Z j


 1129-dimensional input vector
(6)
The output variable of the prediction model is constructed from the consumers’ revealed
preferences, namely, their template choices. In our setting, consumers first choose a theme
among all themes; only one template from each theme is displayed as the cover picture for
each theme at this stage. Once consumers click on the chosen theme, they can browse all
templates in the chosen theme and choose some of the templates to take photos. We as-
sume that consumers choose among templates they have browsed (i.e., cover-page templates
of each theme and all templates within the chosen theme). Each choice observation is a
consumer-template pair consisting of one consumer and one template she has browsed. If
she chose the template, the observation counts towards a positive sample. If she did not
choose, the observation counts towards a negative sample. Consumers make binary choices
for each browsed templates and can choose multiple templates since consumers can select an
unlimited number of themes and templates within the paid time window. The chosen tem-
plates belonging to the chosen theme naturally serve as the positive samples. The unchosen
templates belonging to the chosen theme serve as the negative samples because consumers
browse them but decide not to take photos with them. For the unchosen themes, the cover-
page templates count toward the negative samples because consumers browse them upon
choosing the themes and do not choose them. However, the other templates belonging to
the unchosen themes do not count as negative samples and are not included in the analysis
because consumers do not have a chance to see them. Overall, the output variable Yij for
28

consumer i and template j is constructed as follows:
Yij =



1 if template j is chosen by consumer i
0 if template j is not chosen but belongs to a chosen theme
0 if template j is the cover-page template of an unchosen theme
(7)
Given the definitions of the input and output variables, we estimate Prediction Model
1 using internal consumer preferences only. We focus on photo samples from the category
“Main (single),” which includes 931 consumers and 33,804 consumer-template pairs. Each
pair consists of one consumer and one template that the consumer has browsed. Out of these
33,804 pairs, 3,629 are positive samples, and 30,175 are negative samples. A positive sample
indicates that the consumer chose the template, while a negative sample indicates that the
consumer browsed but did not choose the template. Negative samples can include templates
from both the unchosen templates of the chosen themes and the cover-page templates of the
unchosen themes. It’s important to note that a template can appear in both the positive and
negative samples, depending on the consumer it is paired with. In our data, every internal
template has been chosen by at least one consumer, meaning each internal template is part
of both the negative and positive samples. The company offered 83 photo themes and 585
photo templates during the observation period. Therefore, there are 585 unique internal
templates in both the positive and negative samples for training the prediction model.
We retain 40% of the observations as the test set and use the remaining data for training
the model. The training and test sets include 20,282 and 13,522 observations, respectively.
As positive samples only account for 10.7% of the total sample size, an unbalanced sample
problem is encountered. To alleviate this problem, we upsample the minority class to 18,000
to better match the majority class. We concatenate the upsampled minority class and the
majority class to form the final training set and train the model using a random forest. The
number of trees in the forest is set to 100. The class weights are set to be balanced.
We estimate Prediction Model 2 using both internal and external consumer preferences.
29

Specifically, external UGC data contain photos taken by individual users in front of various
backgrounds. Each photo represents a user’s chosen background and thus serves as a positive
sample for the prediction model. Taking the graffiti theme as an example. There are 1375
external photos in the graffiti them, each representing a unique consumer and a unique
external template. There are 1375 unique consumers and 1375 unique external templates.
These 1375 consumer-template pairs serve as positive samples. Combining these with the
33,804 internal observations yields a sample size of 35,179 consumer-template pairs. We
use 70% of the observations, or 24,625 pairs, as the training set. Among them, 2,544 are
positive samples, and 22,081 are negative samples. To address the unbalanced sample issue,
we upsample the minority class to 20,000 to align with the majority class. We estimate
Prediction Model 2 using a random forest again, maintaining the same hyperparameters as
those employed in Prediction Model 1.
Training the Generative Models and Generating New Designs
Given the trained prediction model, we proceed to training the generator models and
generate new designs. While we train the prediction model using samples from all template
themes, we train separate generative models for different themes. For illustrative purposes,
we present the generative results for the graffiti theme, as it is one of the most popular
themes in the data. We present the results for other themes (e.g., the traditional Chinese
theme) in the online appendix to show the generalizability of our method to different themes.
To train the DCGAN model, we combine the existing templates acquired from the internal
and external sources, resulting in 1388 training templates for the graffiti theme, 13 of which
are from internal data. We exclude images with extreme height or width values. The final
training set contains 1321 images. Since the size of our training data is relatively small
and the performance of GANs heavily deteriorates in this case, we adopt the differential
augmentation (DiffAugment) method proposed by Zhao et al. (2020). As the authors pointed
out, the performance of a GAN depends heavily on the sample size of the input training data
30

because the discriminator will be simply memorizing the exact training set given the small
sample size. The DiffAugment method imposes various types of differentiable augmentation
on both real and generated samples. It is able to generate high-fidelity images using only
100 images without pretraining, which sufficiently trains the model using a relatively small
training set.
We produce output images with dimensions of 128 × 128. The latent dimensionality is
set to 100, as is the standard value for the DCGAN. We use a batch size of 32 for training
the model, with the learning rate set to 2 × e−4, and the sizes of the feature maps in the
generator and discriminator are both 64. To obtain stable results, we train the DCGAN for
5000 epochs, implementing 275 , 000 iterations in total.
To train the CcGAN with internal consumer preferences, we start by using Prediction
Model 1 to calculate aggregate popularity levels for the 1388 existing templates. This model
requires display rankings as inputs, which are only available for internal templates because
external templates from UGC websites aren’t displayed in the firm’s system. We address this
issue by simulating rankings for the external templates based on the empirical distribution
of internal template rankings. To compare generative models, we normalize each popularity
level by dividing it by the maximum value within each model, resulting in normalized levels
from 0 to 1, which serve as continuous input labels for the generator.
We use the HVDL as the discriminator loss, where the specific loss functions are defined
in Equations 4 and 5. Regarding the hyperparameters of the HVDL, we use the rule-of-
thumb formulae to select them, i.e., σ ≈ 0.028 and κ ≈ 0.192. The label weight parameter
k = 10. The CcGAN is trained for 20,000 iterations with a constant learning rate of 10 −4
and a batch size of 64. The dimensions of the latent GAN are set to 256, and the discrimi-
nator updates twice in one iteration. To solve the small sample size problem, we adopt the
DiffAugment method during the training process, similar to what we did in the DCGAN
case. After training the CcGAN, we instruct the generator to produce new template designs
with different popularity labels, where label=1 indicates the most-preferred class.
31

To train the CcGAN with internal and external preferences, we employ Prediction Model
2 to calculate popularity levels for the existing templates and use the normalized popularity
labels as inputs to the generator. The hyperparameters of the HVDL, σ ≈ 0.019 and
κ ≈ 0.143, follow the rule-of-thumb formulae. The label weight parameter k = 10.
PREDICTION MODEL PERFORMANCE
This section presents performance tests for our prediction models, which are trained and
evaluated on templates from all themes.
Predicting consumer choices
We first show that our prediction model is able to predict observed consumer choices.
Figure 5 presents the observed and predicted numbers of adoptions for three internal tem-
plates in the test set. We can see that the true and predicted numbers of adoptions are quite
close to each other, suggesting that our prediction model is able to capture consumer prefer-
ences for different template designs. Our model is also able to predict choices of individual
consumers, which we show in the online appendix.
Figure 5: Examples of the Predicted Numbers of Template Adoptions
Predicting design popularity
We then conduct a preliminary visual assessment to show that our prediction model is
able to predict the popularity levels of different template designs. We identify the internal
32

templates that are most (least) preferred by consumers based on their observed numbers
of adoptions (row 1 of Figure 6). We then compare their styles with those of the external
templates that our model predicts to have the highest (lowest) average choice probabilities
(row 2 using Prediction Model 1 and row 3 using Prediction Model 2). We find that the
external templates with high (low) predicted choice probabilities exhibit similar styles to the
most (least) popular internal templates, suggesting that the predicted popularity levels are
valid and accurate.
Figure 6: Comparing the Observed and Predicted Popularity Levels
Most-Preferred Templates Least-Preferred Templates
Observed
Prediction
Model 1
Prediction
Model 2
Prediction accuracy tests against benchmark models
Next, we conduct prediction accuracy tests for Prediction Models 1 and 2 on the test
set. As shown in Table 1, Prediction Model 1 achieves an overall accuracy of 0 .793 and
a balanced accuracy of 0 .791. The model’s false-negative rate (FNR) the false-positive
rate (FPR) are both low, indicating a reasonably high accuracy in predicting consumers’
template choices based on facial traits. Incorporating external preferences further improves
the model’s performance. Prediction Model 2’s overall accuracy increases to 0 .806, with a
balanced accuracy of 0.825, and both FNR and FPR are lower. We also compare our method
with the logistic lasso model, a common benchmark for handling binary outcomes and high-
33

dimensional (1001+128+1 in our case) input data. Our proposed model outperforms the
benchmark, confirming its superiority in predicting consumer template choices.
Table 1: Prediction Accuracy Achieved on the Test Set
Prediction Model 1 Prediction Model 2 Benchmark
Training Acc. Balanced FNR FPR Acc. Balanced FNR FPR Acc. Balanced Input Acc. Acc. Acc.
Internal pref. 0.793 0.791 0.212 0.206 0.767 0.789only
Internal and 0.806 0.825 0.148 0.202 0.78 0.815external pref.
Note: This table presents the prediction accuracies, balanced accuracy rates, false-negative rates, and
false-positive rates for the test set using three models: Prediction Model 1 (trained on internal preferences),
Prediction Model 2 (trained on both internal and external preferences), and a benchmark logistic lasso
model. The benchmark model is evaluated with internal preferences in the first row and both internal and
external preferences in the second row.
GENERATIVE MODEL V ALIDITY CHECKS
Face validity: Generating meaningful designs
We first demonstrate the face validity of the generative models by showing their ability
to generate meaningful product designs. Specifically, we need to show that our new model-
generated designs are derived from the same theme as that of the input designs (i.e., graffiti).
We start with a simple visual assessment. Figure 7 compares the real images and the new
images generated by the trained DCGAN. We can see that the generated images are similar
in style to the real images. At the same time, the generated images exhibit sufficient style
variations, which guarantees that no modal collapse occurs during the training process.
In addition to this simple visual examination, we use a pretrained image classifier,
ResNet18 (He et al., 2016), to conduct transfer learning to validate the meaningfulness
of our DCGAN-generated images. Intuitively, if the generated images are indeed from the
same theme as that of the real images (i.e., graffiti), ResNet18 should be able to classify them
into the same category as that of the real images. First, we retrain the classifier to recognize
34

Figure 7: Real vs. DCGAN-Generated Images
(a) Real
 (b) DCGAN-Generated
graffiti and nongraffiti images using 100 real graffiti images (both internal and external, with
label = 1) and 70 real nongraffiti images (internal, with label = 0) as inputs. Second, we test
the validity of the retrained classifier on a test set consisting of real images. The classifier has
an accuracy rate of 97.2% when classifying the images into graffiti and nongraffiti categories.
The false-negative rate and false-positive rate are both very low (2.4% and 3.4%) on the test
set, further validating the ability of the classifier to predict the graffiti category. Finally, we
use this retrained classifier to predict the labels for the set of generated graffiti images and
present the hit rate, defined as the percentage of the generated images that are predicted to
be in the graffiti category (i.e., label = 1). We find that the hit rate is 99%, meaning that
almost all the generated images are classified into the graffiti category by the classifier. This
means that our generative model is able to produce meaningful designs with high fidelity.
Controllably generating designs with certain popularity levels
Our proposed framework allows for generating designs with specific popularity levels,
unlike traditional GAN models. We use the CcGAN model with internal consumer prefer-
ences to generating new designs from the least-preferred and most-preferred classes. The
first row of Figure 8 shows that both classes produce graffiti-style images, passing the face
validity check. The least-preferred class features simpler shapes and patterns, while the
35

most-preferred class has more intricate designs, consistent with internal images.
Additionally, we generate new designs using the CcGAN model with both internal and
external preferences. The second row of Figure 8 shows more pronounced style differences
between the classes. The least-preferred class exhibits simpler colors and shapes, while the
most-preferred class displays more intricate and colorful designs, better exemplifying the
graffiti theme. This indicates that incorporating external preferences enhances the quality
of generated images in the most-preferred class.
Figure 8: CcGAN-Generated Images
CcGAN with Internal Preferences Only
(a) Least-Preferred Class (b) Most-Preferred Class
CcGAN with Internal and External Preferences
(a) Least-Preferred Class (b) Most-Preferred Class
As our CcGAN models utilize continuous popularity labels, they are able to generate
a range of images with continuous popularity levels. Figure 9 displays the progression of
the generated images ranging from the lowest to the highest popularity level. The top row
shows the images generated by CcGAN with the internal preferences, while the bottom row
shows the images generated by CcGAN with both internal and external preferences. The
style of the generated images gradually changes as the popularity level increases. Images
with higher popularity levels have more sophisticated and clearer patterns, especially for the
images generated by CcGAN with both preferences.
36

Figure 9: Generated Graffiti Images with Continuous Labels
Note: The top row shows the images generated by the CcGAN with internal preferences only,
while the bottom row shows the images generated by the CcGAN with both internal and external
preferences.
GENERATIVE MODEL PERFORMANCE TESTS
After validating the generative models’ capability to controllably generate designs, we
now assess their effectiveness in generating designs favored by consumers, which is the pri-
mary objective of our framework. We conduct three types of performance tests: a distance-
based metric comparing designs to known popular ones, an online consumer survey, and
choice probability assessments using prediction models.
Distance-based metric
We propose a distance-based metric as an indicator of popularity. The core idea is that
popular templates share common features, suggesting that consumers tend to favor certain
types of templates. By measuring the similarity between newly generated images and existing
popular templates, we can determine their potential appeal. If the new templates closely
resemble the popular ones, they are more likely to be attractive to consumers. Additionally,
if they differ significantly from unpopular templates, their chances of being well-received also
increase. The metric provides an independent assessment of model performance because it
does not rely on any model within our framework. Instead, it leverages the intrinsic similarity
37

among the image features to suggest popularity.
We start by identifying the most and least popular templates among existing internal and
external templates, which serve as the targets for measuring the distances. For internal tem-
plates, popularity is determined by the number of consumers selecting each template—the
most popular template is chosen by the largest number, while the least popular is chosen by
the smallest. For external templates, direct consumer choice data isn’t available since each
external image corresponds to a unique consumer’s choice of a unique template. Instead,
we assign a popularity score based on visual similarity to frequently observed patterns in
the external dataset. Patterns that are repeatedly seen among external templates indicate
popularity among external consumers. To identify these popular patterns, we use the Caffe
BVLC reference model to obtain feature embeddings for all external templates to capture
their semantic and visual characteristics. These embeddings are clustered using KMeans
into ten clusters, with the cluster centers representing common or popular visual archetypes.
An external template’s popularity score is calculated by computing the cosine similarity be-
tween its embedding and each cluster center, averaging these similarities. This score reflects
the image’s alignment with popular patterns — images with higher scores are more similar
to common archetypes and are thus deemed more popular, while those with lower scores
deviate from typical patterns.
The calculation procedure of the distance-based metric is as follows. Denote the most
popular internal and external templates j ∈ Jand the least popular internal and external
templates k ∈ K. First, we use the Caffe BVLC reference model to obtain feature embeddings
of the new templates generated by different generative models and the most and least popular
existing templates. Second, we calculate the distance between each generated template i and
each of the most and least popular existing templates. We further normalize the distances
to be within the range of [0, 1]. Let dij and dik denote the normalized distances between
template i and the most popular template j and the least popular template k, respectively.
Finally, we calculate the distance-based metric for each generated template and average the
38

results over all templates generated from the same generative model to obtain a measure for
each generative model. To summarize, the distance-based metric for each generative model
is defined as
D = 1 N
NX
i=1
n X
j∈J
d2 ij + X
k∈K
(1 − dik)2
o
,
where N denotes the total number of templates generated by each generative model, J
denotes the set of the most popular internal and external templates, and K denotes the set
of the least popular internal and external templates. This distance-based metric decreases
when the generated templates are more (less) similar to the most (least) popular existing
templates. The smaller the distance-based metric is, the better.
We calculate the distance-based metric for four sets of images: 1) the internal original
templates; 2) 100 new templates generated by DCGAN; 3) 100 new templates generated
by CcGAN with internal preference from the most-preferred class; 4) 100 new templates
generated by CcGAN with internal and external preferences from the most-preferred class.
Table 2 presents the mean and median distance-based metrics for each set of images.
Table 2: Distance-Based Metric: Mean and Median
Statistics Internal original images DCGAN CcGAN with internal preference CcGAN with internal and external preferences (no label weights) CcGAN with internal and external preferences
Mean 1.32 1.26 1.25 1.18 1.14
Median 1.38 1.25 1.22 1.19 1.13
Note: This table presents the mean and median distance-based metrics for images generated by different
GAN models. Smaller values indicate higher popularity.
We find that CcGAN with internal and external preferences performs the best, followed
by CcGAN with internal preference and DCGAN. All generative models outperform the
original internal templates provided by the company. Specifically, DCGAN (Column 2 of
Table 2) performs the worst among the generative models because it does not account for
consumer preferences. CcGAN with internal preference (Column 3 of Table 2) performs
better as it is guided by Prediction Model 1, which captures internal preferences, enabling
it to generate templates more appealing to internal consumers. However, this improvement
39

is limited because Prediction Model 1 is trained solely on internal preferences and fails to
fully recognize the appeal of new features from external templates. Consequently, any novel
features from external templates that differ from popular internal features are perceived as
unpopular by Prediction Model 1.
CcGAN with both internal and external preferences (Column 5 of Table 2) performs the
best by integrating external preference information through Prediction Model 2. This inte-
gration allows CcGAN to fully exploit appealing features from external templates. Specifi-
cally, Prediction Model 2 learns the types of features consumers prefer in external templates.
The underlying assumption is that external consumers who resemble internal consumers
have similar preferences, so external consumer preferences can inform those of internal con-
sumers. Consequently, Prediction Model 2 can identify which external features might appeal
to internal consumers, guiding CcGAN to integrate popular features from both internal and
external sources, leading to the greatest improvement in model performance.
It is noteworthy that the label weights in the loss functions (Equations 4 and 5) play a
crucial role in enhancing the attractiveness of generated templates. We modify the CcGAN
from Ding et al. (2020) by incorporating label weights to account for the ordinal nature of
labels in our context. To demonstrate their impact, we trained the CcGAN without label
weights. Figure 10 shows sample templates from this version, which appear less sophisti-
cated and more blurred compared to those in Figure 8. The distance-based metric for this
CcGAN without label weights (Column 4 of Table 2) indicates worse performance compared
to the full model with label weights (Column 5 of Table 2). These findings underscore that
incorporating label weights significantly enhances the quality of the generated images.
Overall, the results reveal three key insights: (1) Integrating consumer preference in-
formation enhances performance, with CcGAN consistently outperforming DCGAN. (2) In-
cluding external consumer preferences is essential for improving image quality, as it helps the
predictor model identify and incorporate appealing external features. (3) Adapting CcGAN
to recognize the ordinal nature of labels is crucial for generating high-quality designs.
40

Figure 10: CcGAN-Generated Images without Label Weights
CcGAN (internal preferences) without label weights
(a) Least-Preferred Class (b) Most-Preferred Class
CcGAN (internal and external preferences) without label weights
(a) Least-Preferred Class (b) Most-Preferred Class
Online consumer survey
We further obtain direct consumer evaluation on the generated designs through an online
survey on Credamo, a leading survey platform in China. 8 Mimicking a self-operated photo
booth, respondents choose from photo templates, including original internal templates and
those generated by the three generative models. As there are many original and newly
generated templates, we randomly select 4 generated templates per generative model (denote
as A1-A4 for CcGAN with internal and external preferences, B1-B4 for CcGAN with internal
preference, C1-C4 for DCGAN) and 2 templates from the 13 internal ones (denoted as D1
and D2). This fixed set of templates is used for the survey.
In the survey, respondents are introduced to a self-operated photo booth concept where
they select photo templates as backgrounds for pictures. They are informed that their
choices will help design popular backgrounds, aiding photo studios in optimizing services.
Respondents imagine entering a self-service photo booth to take personal photos. They are
presented with 8 templates (similar number of templates per theme are presented in the real
8https://www.credamo.com/#/dataMarket
41

business setting) and asked to choose the 2 most suitable backgrounds. The 8 templates
include: 2 from CcGAN with internal and external preferences (randomly from A1-A4), 2
from CcGAN with internal preference (randomly from B1-B4), 2 from DCGAN (randomly
selected from C1-C4), and 2 internal original templates (D1-D2). The display order is ran-
domized, and the set of templates varies per respondent. Each respondent participates in one
choice occasion. The survey includes attention checks and basic demographic questions, and
responses failing attention checks are excluded. The final sample includes 288 respondents.
A sample survey is provided in the online appendix.
Table 3 presents the template-level and model-level choice probabilities from the survey
data. Template-level choice probability is calculated as the number of times a template
is chosen divided by the number of times it is shown. Model-level choice probability is
calculated as the number of times templates from a specific model are chosen divided by the
number of times they are shown. We find that CcGAN with internal and external preferences
performs the best. The survey results also show that the consumer sample in the survey
has similar preferences to the internal consumers, as both groups prefer the internal original
image D2 over D1, giving us confidence that the online survey reflects consumer evaluations
obtained in the photo booth setting.
Table 3: Consumer Survey: Choice Probabilities
Choice probabilities CcGAN with internal and external preferences CcGAN with internal preference DCGAN Internal original images
Model-level 33.0% 23.3% 16.0% 27.8%
Image-level A1: 24.7% B1: 23.5% C1: 19.2% D1: 17.0%
A2: 45.2% B2: 22.7% C2: 11.4% D2: 38.5%
A3: 36.0% B3: 23.7% C3: 18.4%
A4: 26.1% B4: 23.1% C4: 15.0%
Model-predicted popularity
As an alternative performance test, we use our trained prediction model to evaluate the
performance of the generative models. We focus on the same four sets of images as in the
42

distance-based metric test. For each image, we calculate consumers’ choice probabilities
using our trained prediction models. To maintain consistency between the prediction and
generation models, we use Prediction Model 1 (Prediction Model 2) to evaluate the perfor-
mance of the CcGAN with internal preferences only (with internal and external preferences).
Averaging over the choice probabilities of images within each model, we obtain the model-
specific average predicted choice probabilities as shown in Table 4(a). Choice probabilities
of original internal images are normalized to 1 in the first column, with percentage changes
shown in other columns.
The results are consistent with those in the distance-based metric test. As shown in
Table 4(a), CcGAN with internal and external preferences shows the largest performance
improvement over the internal original images (9.13%) because Prediction Model 2 allows
it to fully incorporate popular features from both internal and external sources. CcGAN
with internal preference only shows a limited performance improvement (2%) as Prediction
Model 1 is trained solely on internal preferences and cannot fully recognize out-of-the-box
features from external templates. DCGAN does not perform well. 9
Incorporating label weights is important; CcGANs without label weights (Table 4(b))
show a smaller improvement in predicted choice probabilities compared to CcGANs with
label weights (Table 4(a)).
PERSONALIZED DESIGN GENERATION
Our proposed framework is well suited for personalized design generation. The CcGAN
with both internal and external preferences is trained based on population-wide popularity
labels (i.e., the average choice probabilities across consumers). We can use this general
CcGAN as a pre-trained model and re-train it using personalized popularity labels to obtain a
9DCGAN does not perform well when evaluated by Prediction Model 1. Although DCGAN incorporates new
design features from external templates, Prediction Model 1 cannot recognize the attractiveness of these new features
and treats them as unpopular. Thus, DCGAN-generated templates perform worse than the original internal images
(-1.61%). DCGAN performs better (4.47%) when evaluated by Prediction Model 2, as this model can recognize
popular features from external sources in the DCGAN-generated templates.
43

Table 4: Average Predicted Choice Probabilities
(a)
Evaluation Methods Internal DCGAN CcGAN with CcGAN with Internal Original Images Internal Preference and External Preference
Prediction Model 1 1.00 -1.61% 2.00% N.A.
Prediction Model 2 1.00 4.47% N.A. 9.13%
(b)
Evaluation Methods Internal CcGAN with CcGAN with Internal Original Images Internal Preference and External Preference
(no label weights) (no label weights)
Prediction Model 1 1.00 0.72% N.A.
Prediction Model 2 1.00 N.A. 5.37%
Notes: This table presents the average choice probabilities predicted for real images and images generated
using different GAN models. The first (second) row shows the choice probabilities predicted by Prediction
Model 1 (Prediction Model 2). Choice probabilities of real internal images are normalized to 1 in the first
column, with percentage changes shown in other columns.
personalized CcGAN. For a target consumer, we first use the trained predictor to calculate his
choice probabilities for each input image, call these probabilities the personalized popularity
labels. We then use these personalized labels to guide the re-training of the generative model.
The re-trained generative model is now able to conduct personalized design generation by
directionally generating new images that is preferred by this specific consumer.
We randomly choose one of the existing internal consumers and conduct a personalization
exercise for him. Figure 11(a) shows the target consumer and the photo he took with
the chosen internal template. We use the trained predictor model to calculate his choice
probabilities for each input internal and external templates. We then use these probabilities
as personalized popularity labels to re-train the general CcGAN for 8000 iterations. This
gives us the personalized CcGAN for this consumer. We instruct the personalized CcGAN
to generate new templates from the most preferred class.
To evaluate the performance of the generated personalized templates, we define a per-
sonalized distance-based metric by calculating the distance of each generated template to a
set of target images that represent the target consumer’s most- and least-preferred existing
templates. The calculation procedure is similar to the previous distance-based metric test,
44

Figure 11: Personalized Design Generation
but the target images are redefined to be personalized: 1) the internal template chosen by the
target consumer, representing his most-preferred internal template; 2) the internal template
chosen by the internal consumer who looks the least similar to him (based on the distance
of their facial appearance embeddings), representing his least-preferred internal template; 3)
the external template chosen by the most similar external consumer, representing his most-
preferred external template; and 4) the external template chosen by the least similar external
consumer, representing his least-preferred external template. Figure 11(b) displays the four
target images. Intuitively, consumers who resemble the focal consumer are likely to share
similar preferences, making their choices more appealing to him. Indeed, we find that his
most-preferred templates share similar patterns, which are different from his least-preferred
templates. The personalized distance-based metric measures how similar the personalized
templates are to his most- and least-preferred templates. A smaller metric represents better
performance.
We use the trained personalized CcGAN to generate 100 personalized designs. Figure
45

11(c) shows sample personalized designs. Table 5 presents the means and medians of the
personalized distance-based metrics by the personalized and non-personalized models. We
find that the personalized CcGAN with both preferences performs the best, followed by the
general CcGAN with both preferences, and the DCGAN performs the worst. The results
suggest that incorporating personalized preference yields even better designs than incorpo-
rating population-level preference in terms of generating designs that are attractive to a
specific consumer.
Table 5: Personalized Distance-Based Metrics: Mean and Median
Statistics DCGAN CcGAN with internal and external preferences CcGAN with internal and external preferences (personalized)
Mean 1.22 1.10 0.97
Median 1.22 1.05 0.96
Note: This table presents the mean and median distance-based metrics for images generated by different
GAN models. Smaller values indicate the generated templates are visually similar to popular internal
templates and distinct from unpopular ones, suggesting higher consumer popularity.
CONCLUSION
In this paper, we propose a novel framework to transform the product design process in
the era of generative AI. The unique contribution of our work is that our proposed model sys-
tematically incorporates consumer preferences and external UGC into the design generation
process. Two important managerial insights emerge from our results. First, it is benefi-
cial to incorporate consumer preference information into the generation process because it
can guide the generator to directionally generate consumer-preferred designs. Second, it is
not sufficient to incorporate only external designs; external preference information is also
required for the generative model to fully incorporate new appealing features from external
designs.
Our framework offers a superior alternative to the prevailing industry practice that relies
solely on pure generative models without considering consumer preferences. The proposed
model is preference-aware, cost-effective, automated, and scalable, generating new designs
46

in a controllable and targeted way. The new designs are more likely to be preferred by
consumers ex ante, unlike the traditional method of creating many designs and discarding
unpopular ones later. Our approach saves resources by avoiding less appealing designs.
Our framework provides an effective solution to the product design ideation problem.
Traditional methods depend heavily on professionally trained human designers, who have
limited capacity and may struggle to produce high-quality designs on a large scale. Addi-
tionally, these designers might not always be fully attuned to the latest consumer demands
and often cannot systematically learn the preferences of a broad audience. Our approach en-
hances the traditional design process by incorporating existing designs from external sources,
which can complement human efforts. User-generated content (UGC) images, in particular,
can be viewed as real-time design ideas created by individual users, offering a rich and diverse
source for ideation.
Our framework provides a cost-effective way to evaluate new product designs by using
user-generated content (UGC) instead of traditional consumer surveys. UGC offers a vast,
real-time repository of consumer preferences that inform design decisions. This data is highly
relevant as it is voluntarily generated by consumers, abundant, readily available online, and
constantly updated, helping firms stay aligned with evolving consumer demands. UGC is
particularly beneficial for start-ups lacking resources for costly traditional design methods,
reducing financial burdens and offering a dynamic, authentic reflection of consumer tastes.
In conclusion, our findings highlight the benefits for industry practitioners of integrating
consumer preferences and external UGC into generative models. Unlike pure GAN-based
methods, our approach utilizes external preference data from UGC to enhance design pro-
cesses and extract valuable consumer insights without costly surveys. This framework is
widely applicable in artistic, creative, and other domains with diverse consumer preferences.
Future research could investigate embedding consumer preferences into generative models
across various contexts, expanding understanding of the effectiveness and scalability of these
approaches.
47

REFERENCES
Allenby, G. and Rossi, P. (1998). Marketing models of consumer heterogeneity. Marketing Science,
89(1):57–78.
Amos, B., Ludwiczuk, B., Satyanarayanan, M., et al. (2016). Openface: A general-purpose face
recognition library with mobile applications. CMU School of Computer Science, 6(2):20.
Brock, A., Donahue, J., and Simonyan, K. (2018). Large scale gan training for high fidelity natural
image synthesis. arXiv preprint arXiv:1809.11096.
Burnap, A., Hauser, J. R., and Timoshenko, A. (2023). Product aesthetic design: A machine
learning augmentation. Marketing Science.
Culotta, A. and Cutler, J. (2016). Mining brand perceptions from twitter social networks.Marketing
Science, 35(3):343–362.
Dew, R., Ansari, A., and Toubia, O. (2022). Letting logos speak: Leveraging multiview represen-
tation learning for data-driven branding and logo design. Marketing Science, 41(2):401–425.
Ding, X., Wang, Y., Xu, Z., Welch, W. J., and Wang, Z. J. (2020). Ccgan: Continuous conditional
generative adversarial networks for image generation. In International conference on learning
representations.
Dzyabura, D. and Hauser, J. (2011). Active machine learning for consideration heuristics.Marketing
Science, 30(5):801–819.
Frey, B. J. (1998). Graphical models for machine learning and digital communication. MIT press.
Goodfellow, I., Pouget-Abadie, J., Mirza, M., Xu, B., Warde-Farley, D., Ozair, S., Courville, A.,
and Bengio, Y. (2014). Generative adversarial nets. Advances in neural information processing
systems, 27.
Green, P. and Srinivasan, V. (1990). Conjoint analysis in marketing: new developments with
implications for research and practice. Journal of Marketing Research, 54(4):3–19.
Griffin, A. and Hauser, J. (1993). The voice of the customer. Marketing Science, 12(1):1–27.
Hauser, J. and Clausing, D. (1988). The house of quality. Harvard Business Review, 66(3):63–73.
He, K., Zhang, X., Ren, S., and Sun, J. (2016). Deep residual learning for image recognition. In
Proceedings of the IEEE conference on computer vision and pattern recognition, pages 770–778.
Jia, Y., Shelhamer, E., Donahue, J., Karayev, S., Long, J., Girshick, R., Guadarrama, S., and
Darrell, T. (2014). Caffe: Convolutional architecture for fast feature embedding.arXiv preprint
arXiv:1408.5093.
Kingma, D. P. and Welling, M. (2013). Auto-encoding variational bayes. arXiv preprint
arXiv:1312.6114.
Liu, L., Dzyabura, D., and Mizik, N. (2020). Visual listening in: Extracting brand image portrayed
on social media. Marketing Science, 39(4):669–686.
McFadden, D. (1986). The choice theory approach to market research.Marketing Science, 5(4):275–
297.
McKinsey & Company (2023). Generative ai fuels creative physical product design, but is no magic
wand. https://www.mckinsey.com/capabilities/mckinsey-digital/our-insights/
generative-ai-fuels-creative-physical-product-design-but-is-no-magic-wand .
Accessed on 2024-05-13.
Mirza, M. and Osindero, S. (2014). Conditional generative adversarial nets. arXiv preprint
arXiv:1411.1784.
48

Netzer, O., Feldman, R., Goldenberg, J., and Fresko, M. (2012). Mine your own business: Market-
structure surveillance through text mining. Marketing Science, 31(3):521–543.
Pavlov, E. and Mizik, N. (2019). Increasing consumer engagement with firm-generated social
media content: The role of images and words. Technical report, working paper, Foster School
of Business, University of Washington.
Radford, A., Metz, L., and Chintala, S. (2015). Unsupervised representation learning with deep
convolutional generative adversarial networks. arXiv preprint arXiv:1511.06434.
Rezende, D. J., Mohamed, S., and Wierstra, D. (2014). Stochastic backpropagation and approxi-
mate inference in deep generative models. In International conference on machine learning,
pages 1278–1286. PMLR.
Toubia, O., Hauser, J., and Simester, D. (2003). Polyhedral methods for adaptive choice-based
conjoint analysis. Journal of Marketing Research, 40(1):116–131.
Urban, G. and Hauser, J. (1993). Design and marketing of new products. Prentice Hall.
Wallace, B., Dang, M., Rafailov, R., Zhou, L., Lou, A., Purushwalkam, S., Ermon, S., Xiong, C.,
Joty, S., and Naik, N. (2024). Diffusion model alignment using direct preference optimization.
In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pages 8228–8238.
Xu, J., Liu, X., Wu, Y., Tong, Y., Li, Q., Ding, M., Tang, J., and Dong, Y. (2023). Imagereward:
Learning and evaluating human preferences for text-to-image generation. Advances in Neural
Information Processing Systems, 36:15903–15935.
Zhang, M. and Luo, L. (2023). Can consumer-posted photos serve as a leading indicator of restau-
rant survival? evidence from yelp. Management Science, 69(1):25–50.
Zhang, S., Lee, D., Singh, P. V., and Srinivasan, K. (2017). How much is an image worth? airbnb
property demand estimation leveraging large scale image analytics.
Zhao, S., Liu, Z., Lin, J., Zhu, J.-Y., and Han, S. (2020). Differentiable augmentation for data-
efficient gan training. Advances in neural information processing systems, 33:7559–7570.
49
