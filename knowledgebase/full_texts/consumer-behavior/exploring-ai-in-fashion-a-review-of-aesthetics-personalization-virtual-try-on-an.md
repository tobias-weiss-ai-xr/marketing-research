---
title: 'Exploring AI in fashion: a review of aesthetics, personalization, virtual try-on, and forecasting'
url: https://arxiv.org/abs/2101.08301
category: consumer-behavior
subcategory: empirical
date: 2026-03
venue: Multimedia Systems
authors:
- Laila Khalid
- Wei Gong
source: arxiv
pdf_url: https://arxiv.org/pdf/2101.08301
pages: 45
chars: 115720
fetched_at: '2026-11-08T12:57:04+00:00'
kb_version: 1
---

# Exploring AI in fashion: a review of aesthetics, personalization, virtual try-on, and forecasting

Exploring AI in Fashion: A Review of Aesthetics,
Personalization, Virtual Try-On, and Forecasting
Laila Khalid and Wei Gong
Department of Computer Science, University of Science and Technology
of China, 96, JinZhai Road, Hefei, 230026, Anhui, China.
*Corresponding author(s). E-mail(s): weigong@ustc.edu.cn;
Contributing authors: laila@mail.ustc.edu.cn;
Abstract
Fashion-focused artificial intelligence has rapidly advanced in recent years,
driven by deep learning and its deployment in recommender systems, detection,
retrieval, and analytics. Yet several consumer-facing domains remain compar-
atively under-surveyed despite their practical impact. This work provides a
comprehensive review of methods, datasets, and evaluation metrics across four
such domains: aesthetics, personalization, virtual try-on, and forecasting. We
synthesize technical approaches spanning representation learning, preference
modeling, image transformation, and time-series analysis; relate them to down-
stream recommender systems and user experience; and highlight cross-domain
dependencies (e.g., aesthetics-informed personalization, trend-informed recom-
mendations). We also catalog commonly used datasets and metrics, including
those from object detection and image segmentation pipelines, where relevant
to try-on and visual understanding. Finally, we identify open challenges and
promising directions for integrated AI-driven fashion systems.
Keywords:Deep Learning, Recommendation Systems, Aesthetics, Personalization,
Virtual Try-On, Fashion Forecasting
1 Introduction
The fashion industry has undergone a dramatic transformation in recent years, with
trends emerging and becoming obsolete within days. The integration of Internet
shopping has brought unprecedented revenue growth to this sector, creating exciting
1
arXiv:2101.08301v2  [cs.CV]  19 Mar 2026

opportunities for analyzing visual features in clothing. These visual features, encom-
passing color, texture, pattern, silhouette, and style elements, form the foundation of
fashion design and directly influence individual consumer preferences and purchasing
decisions. Today’s artificial intelligence algorithms have evolved beyond simple prod-
uct recommendations to genuinely evaluate the compatibility and aesthetics of fashion
items [1, 2], effectively making AI systems primary curators of style rather than human
experts alone.
Recent research has explored diverse approaches to fashion AI, spanning implicit
user feedback systems [3], scenario-oriented recommendations [4], probabilistic mul-
timedia ontologies [5], hidden Markov models for behavior characterization [6], and
collaborative filtering with visual attention mechanisms [7]. Other work has focused
on curating compatible garments [8–10], employing Generative Adversarial Networks
for clothing synthesis [11], or recommending complete outfit combinations [12]. Stud-
ies have also examined item interchangeability and compatibility confidence [13, 14],
human perception of beauty and aesthetics [15–18], and fashion assessment in social
networks [19].
Despite these rapid advances, existing surveys have predominantly organized the
field around technical tasks, such as detection, segmentation, retrieval, and synthesis,
rather than around the functional objectives that these technologies serve. While tech-
nically oriented taxonomies are valuable for understanding algorithmic approaches,
they obscure a more fundamental question:How do AI systems collectively support
the end-to-end fashion consumption experience?We argue that a more insightful
organization emerges when we consider fashion AI through the lens of the consumer
decision-making journey and the closed-loop system that supports it.
This survey introduces a novel organizing framework centered on four inter-
connected application domains:aesthetics,personalization,virtual try-on, and
fashion forecasting. These domains were not selected arbitrarily but represent
the essential stages of a complete fashion AI ecosystem that mirrors and supports
consumer behavior:
1.Aestheticsforms the foundational layer, addressing how AI systems learn and
evaluate visual appeal, style coherence, and compatibility. Before any recommenda-
tion can be made, systems must understand what constitutes “good” fashion, the
implicit rules governing color harmony, style consistency, and visual balance that
make outfits appealing.
2.Personalizationbuilds upon aesthetic understanding by tailoring these princi-
ples to individual users. While aesthetics captures universal or culturally-shared
notions of style, personalization recognizes that fashion is inherently subjective,
what appeals to one consumer may not appeal to another. This stage translates
general aesthetic knowledge into individual preference models.
3.Virtual try-onserves as the validation and visualization layer, enabling consumers
to assess personalized recommendations on their own bodies before purchase. This
domain addresses the critical gap between digital browsing and physical reality,
reducing uncertainty and enabling informed decisions.
4.F ashion forecastingcloses the loop by predicting future trends, informing what
styles and items should enter the recommendation pipeline. Forecasting ensures that
2

aesthetic models and personalization systems remain current, while also helping
consumers consider the longevity and relevance of their choices.
Together, these four domains form aclosed-loop system: forecasting anticipates
what will be desirable, aesthetics evaluates whether items meet quality and compati-
bility standards, personalization matches items to individual users, and virtual try-on
validates choices, with consumer feedback and market outcomes cycling back to inform
future forecasts. This interdependence means that advances in one domain directly
enable or constrain progress in others, making an integrated understanding essential
for researchers and practitioners alike.
This survey fills a gap in the literature not merely by covering under-explored
topics, but by providing a principled framework that reveals how disparate research
threads connect to form a functioning fashion AI system. Previous surveys, including
the comprehensive work by Cheng et al. [20], have catalogued technical approaches
within recommendation, analysis, detection, and synthesis. Our contribution differs
in its organizing logic: rather than asking “what techniques exist?”, we ask “what
functions must a complete fashion AI system perform, and how do they interrelate?”
This functional perspective offers researchers a roadmap for identifying bottlenecks,
understanding dependencies, and prioritizing future work.
Our study compiles highly-referenced and influential papers published between
2013 and 2025, organized as follows: Section 2 reviews related surveys and positions
our contribution. Section 3 covers aesthetics, the foundational understanding of visual
appeal and style principles. Section 4 discusses personalization methods that tailor
experiences to individual users. Section 5 presents virtual try-on technologies that
simulate how clothing appears on users. Section 6 provides an overview of forecasting
methods for predicting future trends. Section 7 outlines future directions, and Section 8
presents concluding remarks.
2 Related Work and Comparative Analysis
In this section, we position our survey within the broader landscape of fashion
AI research, comparing our approach with existing surveys and highlighting the
distinctive nature of our selected domains.
2.1 Previous Fashion AI Surveys
Fashion AI has garnered significant attention from researchers, resulting in several
survey papers that examine specific technological aspects. Cheng et al. [20] provided
a thorough overview of intelligent fashion breakthroughs spanning detection, analysis,
synthesis, and recommendation, cataloging 200 pivotal works. While comprehensive,
this survey did not examine the interconnections between these domains or their col-
lective impact on the consumer experience. A more compact version of this can be
seen in this study by Chen et al. [21].
Image retrieval in fashion contexts was extensively covered by Islam et al. [22],
examining techniques for finding visually similar or complementary fashion items. This
3

T able 1Prior Relevant Survey Works In Fashion
W ork F ocus Key Highlights
Cheng et al. [20] Recommendation,
Style Analysis,
Synthesis, Detec-
tion
200 pivotal works, offering a thorough
overview of intelligent fashion break-
throughs spanning detection, analysis,
synthesis, and recommendation.
Chen et al. [21] Fashion analysis,
Recommendation,
Synthesis, Virtual
Try-On
Explores cutting-edge techniques such
as makeup transfer and virtual try-on,
outlining future directions.
Islam et al. [22] Image Retrieval Heightened attention on Fashion Image
Retrieval (FIR). Proposes future exten-
sions to include diverse fashion items
like watches, body ornaments, and
accessories.
Ding et al. [23] Recommendation,
Personalized rec-
ommendation
Fashion recommendation in computa-
tional fashion research, addressing per-
sonalized product, mix-and-match, and
outfit recommendations.
Giri et al. [24] Supply chain AI methods, such as machine learn-
ing and image recognition, at various
supply chain stages and business per-
spectives (B2B/B2C).
Chakraborty et al. [25] Recommendation
Systems
Examines existing studies, offering
insights into methods, algorithmic
models, and filtering techniques.
Jain et al. [26] Fashion Trend
Analysis
Exploration of novel concepts like fash-
ion creativity and cultural inclusivity in
the fashion domain.
Ghodhbani et al. [27] Virtual Try-On Review outlines challenges such as
shape, pose, and texture, providing
a comprehensive overview of research
advancements.
Song et al. [28] Virtual Try-On First systematic image-based virtual
try-on survey with unified evaluation,
covering pipeline architectures, person
representation, and clothing warping
strategies.
survey concentrated on Fashion Image Retrieval (FIR) techniques rather than the
subjective aspects of fashion aesthetics or personalization.
Supply chain applications of AI were explored by Giri et al. [24], focusing on
machine learning and image recognition at various supply chain stages from business-
to-business and business-to-consumer perspectives. This work addressed industry
operations rather than consumer-facing technologies.
4

Fig. 1Integrated Fashion AI Framework showing domain interconnections and information flow
between aesthetics, personalization, virtual try-on, and forecasting systems.
Recommendation systems received dedicated attention in [25] and [23], offering
insights into methods, algorithmic models, and filtering techniques. These surveys
primarily focused on the technical aspects of recommendation without broader
integration with aesthetic principles or visualization technologies.
Fashion trend analysis was examined by Jain et al. [26], exploring novel concepts
like fashion creativity and cultural inclusivity. While related to our forecasting domain,
this work did not connect trend analysis to other consumer-facing technologies.
Virtual try-on technologies were reviewed by Ghodhbani et al. [27], outlining
challenges such as shape, pose, and texture while providing an overview of research
advancements. Similarly, Chen et al. [21] also explore cutting-edge techniques, includ-
ing virtual try-on. Work by Song et al. [28] provides the first systematic image-based
virtual try-on survey with unified evaluation. However, this work focuses specifically on
the technical aspects of virtual try-on methods rather than examining their integration
with other fashion AI domains or their role in consumer-facing applications.
In summary, while existing surveys have made valuable contributions by deeply
examining specific technological aspects of fashion AI, they have typically treated these
domains as separate technical challenges. Our work differs fundamentally by exam-
ining aesthetics, personalization, virtual try-on, and forecasting as an interconnected
ecosystem that collectively shapes the consumer fashion experience. This approach
enables us to identify cross-domain synergies and technical opportunities that would
be missed in a more isolated analysis.
5

2.2 Integrated Framework for Fashion AI Domains
To address the limitations of existing surveys, we propose an integrated framework
that connects the four core domains of fashion AI. This framework demonstrates how
aesthetics, personalization, virtual try-on, and forecasting work together to create a
comprehensive consumer experience.
As illustrated in Figure 1, our selected domains exhibit technical indepen-
dence while maintaining application interdependence. Each domain employs distinct
technical approaches:
• Aestheticsprimarily employs visual perception models and style representation
learning
• Personalizationutilizes preference learning and adaptive recommendation systems
• Virtual T ry-Onfocuses on image transformation, garment physics, and synthesis
techniques
• F orecastingleverages time series analysis and trend detection methodologies
2.3 Cross-Domain Integration Analysis
The four domains of fashion AI—aesthetics, personalization, virtual try-on, and
forecasting—exhibit significant interdependencies that create both opportunities and
challenges for integrated system development.
T able 2Cross-Domain Integration Analysis: How Each Domain Addresses Gaps in Others
Domain Key Challenges How Other Domains Help
Aesthetics Subjective evaluation, con-
text dependency
Personalization:User preference model-
ing
Virtual T ry-on:Real-time visual feed-
back
F orecasting:Trend-aware aesthetics
Personalization Cold-start problem, prefer-
ence drift
Aesthetics:Universal beauty principles
Virtual T ry-on:Interactive preference
learning
F orecasting:Trend-based personalization
Virtual Try-On Realism, pose diversity, gar-
ment fit
Aesthetics:Visual quality assessment
Personalization:User-specific adapta-
tion
F orecasting:Trend-aware garment selec-
tion
Forecasting Cold-start for new products,
external signal integration
Aesthetics:Visual trend analysis
Personalization:User behavior patterns
Virtual T ry-on:User interaction data
This technical diversity means each domain can be (and often has been) studied
in isolation. However, when deployed together, these domains create an integrated
6

Fig. 2Technical Architecture of Fashion AI Domains showing direct connections between aesthetics,
personalization, virtual try-on, and forecasting systems with cross-domain learning pathways.
system with circular influence patterns where outputs from one domain become inputs
for another (Figure 2).
3 Aesthetics In Fashion
Aesthetics in fashion serves as the foundational layer that influences all other AI
domains, establishing universal principles of visual appeal, style compatibility, and aes-
thetic judgment that inform personalization, virtual try-on, and forecasting systems.
7

The aesthetic principles developed here create the visual language that enables effec-
tive personalization, realistic virtual try-on experiences, and accurate trend prediction.
This section examines core technical approaches, including aesthetic evaluation meth-
ods, representation learning for aesthetics, and context-aware aesthetic modeling;
explores learning paradigms from supervised methods to cross-domain knowledge
transfer; and analyzes application domains covering compatibility assessment, con-
sumer preference modeling, and aesthetic evaluation frameworks. The framework
illustrated in Figure 3 demonstrates how aesthetic principles are captured and applied
across the fashion AI ecosystem.
Fig. 3Fashion Aesthetics framework for visual analysis and style recognition.
3.1 Core Technical Approaches
Aesthetics in fashion represents a foundational element that shapes both design princi-
ples and consumer perception. According to The Stanford Encyclopedia of Philosophy
[29], the term “aesthetic” originated in the 18th century, referring to objects, judg-
ments, attitudes, experiences, or values related to beauty. The concept typically
emerges from taste, with 18th-century theory emphasizing rationalist discourse on
beauty and the influence of individualism on virtuosity. In the fashion domain, aes-
thetics provide essential building blocks—establishing rules of beauty, laws of taste,
and artistic expression used by designers to create harmonious and appealing looks.
They help define a designer’s or brand’s genre and flair, influencing color selection,
fabric choices, and content direction, ultimately determining which audience a design
appeals to.
Aesthetic evaluation approaches have advanced significantly with the evolution
of computer vision technology. Neuroaesthetics [19] made a notable contribution by
examining various fashionability factors, including outfit type and gender, garment
type, user and setting characteristics, and fashionability scoring. Their Conditional
8

Random Field (CRF) model and bag-of-words approach provided comprehensive
feedback based on these combined factors. Their analysis of 144,169 user posts con-
taining images, text, and metadata established valuable resources for subsequent
research. The importance of aesthetic evaluation is underscored by Magic Closet [30],
who determined that individuals wearing well-coordinated, visually appealing attire
were perceived as having higher status, demonstrating the social impact of fashion
aesthetics.
Representation learning for aesthetics has seen innovative approaches that capture
complex visual properties. VF-ISS-A WS (Visual Features-Image Scale Space-Aesthetic
Weighted Space) [31] is a framework that positions aesthetics in a continuous image-
scale space (2D space) as an intermediate level of representation. This structure
facilitates higher-level perception of aesthetic effects. They employed a Stacked Denois-
ing Autoencoder Guided by Correlative Labels (SDAE-GCL), effectively mapping
visual features into this image scale space using both labeled and unlabeled datasets.
The SDAE-GCL’s denoising optimization mechanism removes random noise from ini-
tial inputs, improving accuracy and experimental reliability. Another approach, DCF A
(Dynamic Collaborative Filtering model with Aesthetic Features) [32], recognized that
different individuals express different aesthetic characteristics and recommended ten-
sor factorization models for personalizing aesthetic attributes to ensure comprehensive
aesthetic coverage.
Context-aware aesthetic modeling represents an important direction, acknowledg-
ing that fashion aesthetics are situational. The Trip Outfits Advisor [33] pioneered
an investigation into relationships between location attributes and apparel attributes,
developing recommendations for location-oriented apparel in online travel photos. This
work highlighted that wearing fashionable outfits in inappropriate contexts can under-
mine their aesthetic value. Similar contextual awareness is demonstrated in DeepStyle
[34], which presented an innovative end-to-end method using a neural network archi-
tecture to model joint multi-modal space representation, where visual and linguistic
signals are transformed together. This approach addresses the challenge of formulat-
ing natural queries for specific fashion searches across multiple modalities, such as
“this dress but silk made.” FHSI (Fuzzy Perceptual Color Model) [35] examined the
context dependency of color aesthetics, specifically focusing on color harmonies and
color impressions in art and fashion domains. This work introduced a novel fuzzy
perceptual color model that aligns with human perception and enables effective mod-
eling of aesthetic judgments. Community-based aesthetic learning has emerged as a
novel approach for large-scale aesthetic preference modeling. PMTM (Probabilistic
Multi-Topic Model) [36] segments clients into aesthetic quality communities based
on shared dress color preferences. The model employs geometry-based feature selec-
tion to capture aesthetic tendencies using visual, semantic, and textual features in
a 457-dimensional representation. The system identifies tightly connected aesthetic
communities through graph-based frameworks and dense graph mining techniques,
achieving 85.7% accuracy on a dataset of over one million clients across 18 aesthetic
communities.
9

3.2 Learning Paradigms
Fashion aesthetic modeling has employed diverse learning approaches to capture the
subjective and multifaceted nature of aesthetic judgment.
Supervised learning methods have been widely applied to aesthetic modeling tasks.
Traditional approaches focused on training matching principles—for instance, pairing
a red t-shirt with white jeans rather than green ones. More sophisticated supervised
approaches like the one used by Neuroaesthetics [19] employed CRF to model fashion-
ability factors. F ARM (Fashion Aesthetic Recommendation Model) [37] is an improved
framework incorporating supervised generation loss to better encode aesthetic infor-
mation. This approach illustrates the challenge of balancing multiple objectives, as
generation quality may divert attention from recommendation performance, creating
a trade-off between visual aesthetic enhancement and effective recommendation.
Feature extraction and fusion techniques provide alternative approaches to aes-
thetic learning. Several studies have examined recommending fashion garments that
complete incomplete outfits [8, 10]. Earlier methods primarily focused on selecting
garments from databases that coordinate well with query items [9, 10, 38]. The hybrid
multilabel Convolutional Neural Network (CNN) and Support Vector Machine (SVM)
(mCNN-SVM) approach in Trip Outfits Advisor [33] demonstrates how multiple tech-
niques can be combined to learn associations between clothes and contextual factors.
These methods excel at capturing specific aspects of aesthetics but may struggle with
integrating broader fashion principles.
Cross-domain knowledge transfer represents an advanced paradigm for aesthetic
learning. ACDN (Aesthetic Cross-Domain Networks) [39] introduced a deep network
that shares parameters characterizing personal aesthetic preferences and transfers
knowledge between domains. This approach leverages an aesthetic network to extract
features and integrates them into a cross-domain network for transferring domain-
independent preferences. Network cross-connections enable dual knowledge transfer
across domains. This paradigm recognizes that aesthetic preferences often transcend
specific fashion categories and contexts. Taking standardization further, the A100
framework [40] presents Aesthetic 100 as an industry standard with systematic prin-
ciples and guidelines for performance testing at both characteristic and general
levels.
FHSI [35] employed a fuzzy-based learning approach to investigate the context
dependency of aesthetic principles. They integrated fuzzy set theory with color space
modeling to create the fuzzy perceptual color model, a novel color representation
framework that accommodates the inherent imprecision and subjectivity of human
color perception. Their experimental methodology compared aesthetic evaluations
across different contexts (art and fashion) to determine which aesthetic principles
remained consistent and which varied. Their findings revealed that color harmony—a
fundamental aspect of aesthetic appeal—exhibited a high degree of universality. This
suggests that despite contextual differences, certain fundamental aesthetic principles
remain consistent across domains.
Weakly-supervised community learning represents an advanced paradigm for aes-
thetic modeling. PMTM [36] employs weak supervision to link client tags with
10

aesthetic community memberships, using Jensen-Shannon divergence to measure sim-
ilarity between aesthetic profiles. The approach constructs affinity graphs reflecting
client relationships and applies specialized algorithms to identify tightly connected
subgroups defined by shared dress color preferences. This method addresses the chal-
lenge of modeling subjective aesthetic preferences at scale while maintaining individual
variation within broader aesthetic communities.
3.3 Application Domains
Aesthetic principles in fashion influence multiple application areas, each leveraging
different aspects of visual appeal and harmony.
Compatibility assessment represents a fundamental application of fashion aes-
thetics. Previous research has predominantly addressed recognition issues, such as
matching street scene items to in-store inventory [41–44]. While this represents only a
portion of the fashion recognition challenge, it directly benefits retailers. From a differ-
ent perspective, recommendations can suggest interchangeable items rather than single
garments that fit multiple outfits [13, 14]. These approaches indirectly incorporate
aesthetic principles without explicitly addressing them. DeepStyle’s [34] Siamese net-
work approach enables retrieval of items with similarity across multiple feature spaces
from multimedia databases, supporting aesthetic-based matching across modalities.
Consumer preference modeling applies aesthetic principles to understand and pre-
dict individual choices. When appearance-oriented consumers purchase products, their
decision criteria focus on whether items look good or satisfy aesthetic needs. ACDN
[39] addressed this challenge by enhancing the modeling of individual inclinations
from an aesthetic viewpoint through cross-domain recommendation methods. Their
Feed-Forward Neural Network (FFNN) and Inception Local Global Network (ILGNet)
approaches demonstrated improved performance in capturing personal aesthetic pref-
erences. These applications recognize the subjective nature of aesthetic judgment while
identifying patterns that can inform personalized recommendations.
Aesthetic evaluation frameworks provide standardized approaches to assessing
fashion aesthetics. The A100 framework [40] presents an industry standard (A100),
which provides an elaborate characterization of AI models’ aesthetic capabilities. This
framework includes systematic aesthetic principles and guidelines for performance
testing at both characteristic and general levels, establishing a definitive evaluation
approach. The framework employs two multiple-choice examinations—LAT (Liberal-
ism Aesthetic Test) and AAT (Academicism Aesthetic Test)—to address bottom-up
and top-down fashion aesthetic criteria. Such frameworks help standardize aesthetic
assessment in an inherently subjective domain.
FHSI [35] expands application domains by providing tools for cross-context aes-
thetic evaluation. Their fuzzy color representation model enables automated extraction
of color palettes that correspond to specific aesthetic impressions like “elegant,”
“formal,” or “romantic.” By examining the context-dependency of these aesthetic prin-
ciples, their research provides valuable insights for applications spanning e-commerce,
marketing, architectural and interior design, product design, fashion, web design,
art, and merchandising. Their findings that color harmony is largely universal while
11

T able 3Taxonomy of Aesthetic Methods in Fashion: Technical Classification and Evaluation
W ork Approach Paradigm Domain
Aesthetic Evaluation Approaches
Magic Closet [30]
(2012)
Status-based fashion
evaluation
Supervised matching
principles
Outfit recommen-
dation with status
impact
Neuroaesthetics [19]
(2015)
Multi-factor fashion-
ability analysis
Conditional Random
Field with bag-of-
words
Comprehensive fash-
ion evaluation
Representation Learning for Aesthetics
VF-ISS-A WS [31]
(2016)
Continuous image-
scale space mapping
Stacked Denois-
ing Autoencoder
(SDAE-GCL)
High-level aesthetic
effect modeling
DCF A [32]
(2018)
Brain-inspired aes-
thetic modeling
Deep structure with
tensor factorization
Aesthetic-aware rec-
ommendation
F ARM [37]
(2019)
Visual-aesthetic
information integra-
tion
Co-supervision learn-
ing with deep CNN
Fashion compatibil-
ity with aesthetic
enhancement
Context-Aware and Multi-Modal Aesthetics
Trip Outfit [33]
(2017)
Location-apparel
attribute association
Hybrid CNN-SVM
with multi-label
learning
Location-specific
outfit recommenda-
tion
DeepStyle [34]
(2019)
Multi-modal joint
representation
Siamese network
with feature fusion
Cross-modal fashion
retrieval
ACDN [39]
(2020)
Aesthetic preference
transfer
Cross-domain net-
works (ACDN)
Cross-domain recom-
mendation
A100 [40]
(2022)
Standardized aes-
thetic assessment
Systematic testing
framework (A100)
Comprehensive aes-
thetic evaluation
FHSI [35]
(2022)
Fuzzy perceptual
color modeling
Fuzzy-based context
comparison
Cross-domain aes-
thetic evaluation
PMTM [36]
(2025)
Community-based
aesthetic learning
with probabilistic
multi-topic modeling
Weakly-supervised
learning with graph-
based clustering
Personalized aes-
thetic community
identification
impressions are partially context-dependent have significant implications for devel-
oping automated aesthetic assessment systems that can function effectively across
different visual domains.
Aesthetic community identification represents a novel application domain for per-
sonalized recommendations. PMTM [36] demonstrated automatic identification of
aesthetic quality communities through their probabilistic multi-topic model. The
system segments clients into communities based on shared dress color preferences,
enabling community-aware aesthetic assessment tools. This approach provides insights
for e-commerce personalization and trend analysis, where understanding both individ-
ual and community-level aesthetic preferences is crucial for effective recommendation
systems.
12

T able 4Evaluation Methods and Datasets in Fashion Aesthetics Research
W ork Metrics Dataset Key Contribution
Magic Closet [30] Status per-
ception
Custom Connecting visual outfit
appeal to social status
perception
Neuroaesthetics
[19]
Accuracy,
Precision,
Recall, IOU,
L1
Fashion144k Comprehensive fashion-
ability factors analysis
VF-ISS-A WS [31] MSE, MAE Custom (Amazon,
JD, Style, NWFW)
2D continuous image-
space for high-level
aesthetics
Trip Outfit [33] Macro-F,
mAP, AP,
AUC
Fashionista, CCP,
ColorfulFashion,
Journey Outfit
Context-aware clothing
recommendation for loca-
tions
DCF A [32] Recall,
NDCG
Amazon Clothing Neural network with ten-
sor factorization for aes-
thetics
F ARM [37] AUC, MRR FashionVC, Exp-
Fashion
Layer-to-layer matching
for aesthetic information
DeepStyle [34] Euclidean
and L1,
Cosine, Chi
Squared
Polyvore Joint representation of
visual and linguistic sig-
nals
ACDN [39] HR, NDCG,
MRR
Amazon Cross-domain aesthetic
preference modeling
A100 [40] LAT and
AAT tests
Maryland, Fash-
ionVC, Mytheresa,
UTZappos50k
Standardized aesthetic
capability testing frame-
work
FHSI [35] Fuzzy sim-
ilarity,
Harmony
score
Custom Context-dependency anal-
ysis of color aesthetics
PMTM [36] BER, F1,
Precision,
Recall
Custom (1M+
clients, 18 aesthetic
communities)
Community-based aes-
thetic preference modeling
with multi-modal features
3.4 Datasets and Evaluation
The fashion aesthetics field lacks a single universally adopted dataset, with researchers
typically using either hybrid datasets or custom collections. Many researchers create
proprietary datasets by scraping websites like Amazon, JD, Style, and NWFW. The
Fashionista Dataset, containing 158,235 images from chictopia.com obtained in 2011,
represents a notable resource, though it lacks annotations and is stored in tab-delimited
13

text files that must be combined to form a unified table. Other significant cross-
domain datasets include Clothing Co-Parsing (CCP) and Colorful Fashion by Yang
et al. [45], Journey Outfit Dataset by Trip Outfits Advisor [33], ExpFashion in NOR
(Neural Outfit Recommendation) [46], Polyvore, released in Bidirectional Long Short-
Term Memory (Bi-LSTM) [8], and Fashion144k, introduced in Neuroaesthetics [19].
FHSI [35] employed custom datasets comprising 1,276 paintings by 10 artists from
different movements and periods alongside 10,000 highly-liked fashion images for their
investigation of color aesthetics across contexts.
Evaluation of aesthetic models primarily employs benchmark metrics including
Mean Average Precision (mAP), average similarity score, Mean Reciprocal Rank
(MRR), Area Under the Curve (AUC), Intersection over Union (IoU), Balanced Error
Rate (BER), and L1-norm regularization. These metrics collectively provide compre-
hensive views of model precision and consistency in representing aesthetic qualities,
demonstrating how effectively models capture and depict aesthetic preferences. Quan-
titative measures are sometimes combined with qualitative assessments from fashion
experts or public feedback to form more holistic evaluations. This combination of quan-
titative and qualitative assessment creates a more complete picture of model quality
and applicability.
4 Personalization in Fashion
Personalization in fashion builds upon the aesthetic foundations established in the
previous section to create tailored experiences that adapt to individual user prefer-
ences and behavioral patterns. This domain bridges universal aesthetic principles with
individual taste, incorporating insights from both aesthetics and forecasting to deliver
recommendations that are both visually appealing and personally relevant. This
section explores core technical approaches, including preference modeling, user rep-
resentation learning, and recommendation generation techniques; examines learning
paradigms from collaborative filtering to hybrid methods; and analyzes applica-
tion domains spanning individual item recommendation, outfit recommendation, and
preference-aware interfaces. The framework presented in Figure 4 demonstrates how
these components work together to create adaptive, personalized fashion experiences.
4.1 Core Technical Approaches
Personalization has become a critical aspect of the fashion industry, enabling expe-
riences tailored to individual preferences and needs. The global apparel market has
shown remarkable growth, with projected revenue of 1.7 trillion dollars [47], repre-
senting a significant year-on-year increase of 13.7 percent. This growth highlights
the industry’s resilience and potential for innovation, particularly in personalization
technologies.
Preference modeling approaches form the foundation of fashion personalization sys-
tems. Wang et al. [48] demonstrated that emotional connections to fashion products
can override rational considerations in purchase decisions. Their work utilized fuzzy
decision trees to model these emotional factors alongside personalized body forms.
14

Fig. 4Personalization framework for user-centric recommendations.
More structured methods for capturing preferences include the functional tensor fac-
torization approach FPITF (Functional Pairwise Interaction Tensor Factorization)
[49], which transforms multi-modal feature vectors of fashion items into a shared
latent space where fashion-eye interactions are modeled. This method decomposes
high-order feature vector interactions into pairwise combinations, enabling a more
effective fashion item ranking. FashionDPO [50], a direct preference optimization
approach, fine-tunes diffusion models for fashion image generation by learning from
human preference data. Their method addresses the challenge of aligning AI-generated
fashion content with human aesthetic preferences through direct optimization of pref-
erence signals, enabling more personalized and aesthetically pleasing fashion image
generation.
User representation learning has advanced significantly with deep neural networks
showing promising results for image content representation, as demonstrated in semi-
nal works by [51], [52], [53], and [54]. A notable development in this area is DeepStyle
[55], which conceptualizes fashion items as having two components: style and cate-
gory. Their approach leverages CNN extracted visual information, removing category
information to isolate style cues, thus creating more nuanced user preference profiles.
VECF (Visually Explainable Collaborative Filtering) [56] further enhanced user rep-
resentation by developing an attention model that focuses on important regions in
fashion images while incorporating user review information. More recently, MG-PFCM
(Metapath-Guided Personalized Fashion Compatibility Modeling) [57], a multi-modal
content-oriented user embedding module, was proposed that derives user embeddings
15

based on the multi-modal contents of their interacted items, addressing the challenge
of representing users with limited content information.
Recommendation generation techniques have evolved into sophisticated systems
combining multiple factors. Many methods approach this challenge through either
pairwise compatibility metrics, as seen in works by [13], [58], and [2], or by model-
ing outfits as sets or ordered sequences. The latter approach is exemplified by Li et
al. [59], who classified outfits as popular or unpopular, and the Bi-LSTM [8] model
for sequential outfit generation. Advanced recommendation approaches include the
visually-aware model DVBPR (Deep Visually-aware Bayesian Personalized Ranking)
[60], which uses image content and Generative Adversarial Network (GAN) technol-
ogy to generate personalized recommendations that match user preferences. TOG
(Template-guided Outfit Generation) [61] introduced the concept of “templates” (cat-
egory combinations) to capture users’ coordination preferences in fashion outfits,
enabling more refined modeling of user preferences at both template and item levels.
MG-PFCM [57] is a metapath-guided approach that incorporates item attributes as
an important entity type, addressing a gap in previous personalized fashion compat-
ibility modeling methods. In a significant advancement, DiFashion [62], a generative
outfit recommender model, leverages diffusion models to actually generate new fash-
ion items tailored to users’ preferences, rather than merely recommending existing
products. StyleMe [63], an AI-aided fashion design system, enables personalized cloth-
ing sketches and style transfer. The system employs a GAN framework with two
components: a sketch generation model with adaptive channel feature normalization
and channel attention modules to learn designer-specific styles, and a style transfer
model that decouples content features from sketches and style features from ref-
erence images. PFNet [64] uniquely integrates attribute-aware personalized fashion
editing with explainable compatibility analysis. It employs an unsupervised garment
attribute decoupling network that uses hierarchical style control and mutual informa-
tion minimization to independently encode attributes without requiring labeled data,
addressing a significant limitation of previous approaches that relied on supervised
information.
4.2 Learning Paradigms
The evolution of personalization systems in fashion has involved diverse learning
approaches, each addressing different aspects of the personalization challenge.
Collaborative filtering methods have been widely adopted, with He et al. [65]
developing a theme-based, scalable model that incorporates both visual data (prod-
uct photos) and textual data (user comments). Their one-class collaborative filtering
approach accounts for time-dependent dynamics, providing insights into aesthetic
characteristics and fashion trends. These methods excel at capturing patterns across
user behaviors but often struggle with the “cold start” problem for new users or items.
Content-based approaches overcome some limitations of collaborative filtering by
focusing on item attributes. DVBPR [60] utilized Siamese CNNs with Bayesian Per-
sonalized Ranking to build upon prior visually-aware recommendation systems. Their
end-to-end learning strategy enables direct modeling of visual preference patterns.
16

T able 5Taxonomy of Personalization Methods in Fashion: Technical Classification and Evaluation
W ork Approach Paradigm Domain
Preference Modeling Approaches
Wang et al. [48]
(2014)
Fuzzy decision trees
modeling emotional
factors
Knowledge-driven
with design exper-
tise
Preference-aware interface
with body form considera-
tion
FPITF [49]
(2015)
Tensor factorization of
multi-modal features
Collaborative fil-
tering with latent
space mapping
Individual item recom-
mendation with ranking
He et al. [65]
(2016)
Time-dependent user
preference modeling
One-class collabo-
rative filtering
Individual item recom-
mendation with trend
analysis
FashionDPO
[50]
(2025)
Multi-expert feedback
with DPO
Direct preference
optimization with
low rank adapta-
tion
Personalized outfit gen-
eration with enhanced
diversity
Visual and Multi-modal Representation
DVBPR [60]
(2017)
Visually-aware prefer-
ence modeling
Siamese CNNs with
Bayesian ranking
Individual item recom-
mendation with visual
similarity
DeepStyle [55]
(2017)
Style-category decom-
position
CNN-based with
feature disentangle-
ment
Style representation with
category awareness
VECF [56]
(2019)
Region-aware atten-
tion modeling
Multimodal atten-
tion network with
LSTM
Individual item recom-
mendation with visual
explanations
Advanced Outfit and Ensemble Recommendation
Bi-LSTM [8]
(2017)
Sequential outfit mod-
eling
Bidirectional
LSTM
Complete outfit genera-
tion
POG [66]
(2019)
Joint user-outfit pref-
erence integration
Transformer archi-
tecture
Outfit recommendation
with user preference bal-
ancing
FHN [67]
(2019)
Binary code learning
for fast retrieval
Hashing network
with set composi-
tion
Outfit recommendation
with efficient matching
HFGN [68]
(2020)
Hierarchical relation-
ship modeling
Graph neural net-
work
Outfit recommendation
with user-item-outfit con-
nections
LPAE [69]
(2021)
Anchored preference
representation
Stacked self-
attention with
latent vectors
Outfit recommendation
for cold-start users
MG-PFCM [57]
(2022)
Metapath-guided het-
erogeneous graph
Graph attention
with metapath-
guided learning
Personalized compat-
ibility modeling with
attribute awareness
TOG [61]
(2023)
Template-guided pref-
erence modeling
Joint learning with
user-template-item
interactions
Personalized outfit gener-
ation with compatibility
balancing
StyleMe [63]
(2023)
GAN-based dual-
model framework with
feature normalization
Hybrid gener-
ative modeling
with style-content
decoupling
Designer-specific sketch
generation and style
transfer
PFNet [64]
(2024)
Unsupervised
attribute decoupling
with compatibility-
aware attention
Multi-task learning
with hierarchical
style control and
global perception
Attribute-aware fashion
editing with explainable
compatibility analysis
DiFashion [62]
(2024)
Conditional diffusion
model
Parallel generation
with multi-
condition guidance
Generative outfit recom-
mendation with personal-
ized image synthesis
17

These approaches are particularly valuable in fashion, where visual attributes are
paramount to user preferences.
Hybrid and advanced methods represent the current state-of-the-art in personaliza-
tion learning. POG (Personalized Outfit Generation) [66] pioneered an industrial-scale
approach that integrates user preferences for both individual items and complete
outfits through a Transformer architecture. Taking a different approach, HFGN
(Hierarchical Fashion Graph Network) [68] identified limitations in conventional com-
patibility matching approaches that fail to model the relationships among users,
outfits, and items. They address this by constructing a hierarchical structure link-
ing user-outfit interactions and outfit-item mappings. For users with limited data,
the LPAE (Learnable Personalized Anchor Embedding) [69] framework uses anchored
latent vectors (anchors) to represent user preferences in the outfit space, with item
interactions captured through stacked self-attention. Another work, TOG [61] jointly
learns user-template interaction, user-item interaction, and outfit compatibility. MG-
PFCM [57] presents a metapath-guided heterogeneous graph learning approach to
better capture the high-order relations among various entities (users, items, and
attributes). Most recently, DiFashion [62], a novel generative paradigm for outfit rec-
ommendation, was proposed, which utilizes diffusion models. This work features three
specialized conditions (category prompt, mutual condition, and history condition) to
guide the parallel generation of multiple fashion images that exhibit high fidelity,
compatibility, and personalization, representing a significant shift from traditional
retrieval-based methods. StyleMe [63] is a dual-model GAN framework that addresses
both personalization of sketch generation and style transfer for fashion design. This
approach is notable for its data efficiency, requiring relatively few designer-specific
sketches (around 100 per designer) while maintaining style consistency, making it prac-
tical for real-world fashion design applications where extensive designer-specific data
may be limited. PFNet [64] introduces a multi-task fashion learning approach that
combines unsupervised attribute disentanglement with explainable compatibility mod-
eling. The method overcomes the limitation of requiring supervised attribute labels
through a novel hierarchical style control mechanism with regularization constraints
to reduce attribute correlation. FashionDPO [50] represents a significant advancement
in preference-based learning paradigms by introducing direct preference optimization
for fashion diffusion models. This approach learns directly from human preference
comparisons rather than relying on traditional supervised learning signals, enabling
the model to capture better aesthetic preferences and generate fashion content that
better aligns with human taste through direct optimization of preference rankings.
4.3 Application Domains
Fashion personalization technologies have been applied across multiple domains, each
addressing different aspects of the user experience.
Individual item recommendation represents the most common application domain.
FPITF [49] proposes a system that ranks fashion items based on computed favorabil-
ity scores derived from millions of pairwise feature vector combinations. This approach
enables highly personalized single-item recommendations tailored to individual user
18

preferences. The methods typically focus on finding items that match a user’s estab-
lished style preferences while potentially introducing novel elements that align with
those preferences.
Outfit recommendation extends personalization beyond single items to complete
ensembles. POG [66] made significant advances in this domain; the model simulta-
neously considers outfit coordination and individual user preferences. Similarly, FHN
(Fashion Hashing Network) [67] collected user-labeled information and outfit data
from fashion-focused social media to generate personalized outfit recommendations.
These systems must balance aesthetic coherence with personalized style preferences—a
more complex challenge than single-item recommendation. Extending personalization
to outfit generation, TOG [61] addressed the challenge of both personalizing and
ensuring compatibility in newly generated outfits with their multi-step generation
framework that first predicts templates based on user preferences. MG-PFCM [57]
focused on personalized fashion compatibility modeling, addressing whether a bottom
(top) matches a given top (bottom) for a specific user. This approach uniquely incor-
porated attribute entities, which contain rich semantics that previous methods had
overlooked in the compatibility estimation process. Taking outfit recommendation to
a new level, DiFashion [62] introduced Generative Outfit Recommendation (GOR),
which transcends the limitations of existing fashion products by generating entirely
new fashion items that can be composed into visually compatible outfits tailored to
users’ unique fashion tastes.
Preference-aware fashion interfaces represent emerging applications that adapt
the entire fashion shopping experience. While not explicitly detailed in the current
literature, this domain encompasses systems that modify search results, browsing expe-
riences, and visual presentations based on user preferences. These applications leverage
the preference modeling and recommendation techniques to create holistic personal-
ized experiences that extend beyond simple product recommendations. StyleMe [63]
extended preference-aware interfaces to the design process itself with an interactive
environment that enables rapid generation of personalized sketches and exploration of
diverse style options through reference-guided style transfer. Meanwhile, PFNet [64]
is a novel application domain that bridges personalized fashion editing with compati-
bility analysis, enabling users to interactively edit clothing attributes while receiving
real-time feedback on the compatibility of their designs with reference garments.
This approach represents a significant advancement in preference-aware fashion inter-
faces by providing attribute-level compatibility explanations, helping users understand
which specific aspects (color, pattern, style, shape) of their edited designs contribute
to or detract from overall compatibility with other items. FashionDPO [50] extends
preference-aware interfaces to generative fashion design through its direct preference
optimization framework. The system enables users to generate personalized fashion
images that align with their aesthetic preferences by learning directly from human
preference data, creating a new paradigm for AI-assisted fashion design that prioritizes
human taste and aesthetic judgment in the generation process.
19

T able 6Evaluation Methods and Datasets in Fashion Personalization Research
W ork Metrics Dataset Key Contribution
Wang et al. [48] Human evaluation CAD generated Emotion-driven personal-
ization with body form
awareness
FPITF [49] NDCG Polyvore Functional tensor factor-
ization for user-item inter-
action modeling
He et al. [65] AUC Amazon.com Time-dependent dynam-
ics for improving recom-
mendation quality
DVBPR [60] AUC Amazon.com,
Tradesy.com
End-to-end learning with
Siamese-CNN architec-
ture
Bi-LSTM [8] Compatibility pre-
diction
Polyvore Bidirectional LSTM for
fashion compatibility
learning
POG [66] FITB, Compatibil-
ity Prediction (CP)
Taobao’s iFashion
Dataset
Transformer-based
encoder-decoder for per-
sonalized outfit generation
FHN [67] AUC, NDCG,
FITB
Polyvore Dataset Hashing method for effi-
cient personalized set rec-
ommendation
VECF [56] F1, HR, NDCG Amazon.com Attention modeling for
important visual regions
with user reviews
HFGN [68] HR, NDCG, Recall,
Precision
Taobao’s iFashion
Dataset
Graph-based modeling of
user-outfit-item relation-
ships
LPAE [69] AUC, NDCG Polyvore Anchor-based representa-
tion for new users with
limited data
MG-PFCM [57] AUC, MRR IQON3000 Metapath-guided graph
learning for attribute-
aware compatibility
modeling
TOG [61] Precision, Recall,
NDCG, CEE
iFashion, Polyvore-
U
Template-guided pref-
erence learning for
personalized outfit gener-
ation
StyleMe [63] FID, LPIPS,
Human evaluation
Custom fashion
dataset
Dual GAN framework for
personalized sketch gener-
ation and style transfer
PFNet [64] AUC, HR@K, User
study
FashionVC,
Polyvore-Maryland
Unsupervised attribute
decoupling and explain-
able compatibility
modeling with global per-
ception
DiFashion [62] FID, IS, Cosine
Similarity, CIS,
LPIPS, Human
evaluation
iFashion, Polyvore-
U
Diffusion-based generative
outfit recommendation
with multi-conditional
guidance
FashionDPO
[50]
IS, IS Accuracy,
Compatibility, Per-
sonalization
iFashion, Polyvore-
U
Multi-expert feedback
with DPO framework
20

4.4 Datasets and Evaluation
Several key datasets have emerged for evaluating personalized fashion recommenda-
tion systems. The Taobao iFashion Dataset, introduced in POG [66], stands as the
largest publicly available resource, containing 1.01 million outfits and 583K individual
clothing items. The Polyvore dataset, released in Bi-LSTM [8], and the Amazon.com
dataset also serve as important benchmarks in the field. The IQON3000 dataset,
used by MG-PFCM [57], provides valuable evaluation resources with rich attribute
information for each fashion item. DiFashion [62] utilized modified versions of the
iFashion and Polyvore-U datasets specifically adapted for generative outfit recommen-
dation tasks. These diverse datasets enable comprehensive evaluation across different
recommendation scenarios and user populations.
The effectiveness of personalization models is assessed through various established
metrics. Overall performance is commonly measured using AUC and ROC (Receiver
Operating Characteristic) curve, which evaluate the models’ prediction and discrimi-
nation abilities for individual users. More specific aspects of recommendation quality
are evaluated using Normalized Discounted Cumulative Gain (NDCG), which mea-
sures ranking quality; Fill-in-the-Blank (FITB), which tests the ability to complete
outfits; F1 score, which balances precision and recall; and Hit Ratio (HR), which mea-
sures the frequency of relevant recommendations. TOG [61] introduced Compatibility
Evaluation Experts (CEE) to quantitatively evaluate the compatibility of generated
outfits, moving beyond the limitations of human evaluation or single-perspective met-
rics. MG-PFCM [57] employed MRR to assess the effectiveness of complementary item
retrieval in personalized fashion compatibility modeling. DiFashion [62] introduced a
comprehensive evaluation framework for generative models, incorporating metrics for
image fidelity (Fr´ echet Inception Distance (FID), Inception Score (IS), CLIP Score),
similarity (Learned Perceptual Image Patch Similarity (LPIPS), CLIP Image Score
(CIS)), compatibility (compatibility evaluator), and personalization.
5 Virtual Try-On
Virtual try-on technology represents a critical bridge between aesthetic assessment
and user decision-making in the fashion consumer journey, leveraging both the aes-
thetic principles and personalization insights developed in previous sections. As users
progress from discovery and exploration to evaluation, virtual try-on systems provide
visual feedback necessary for informed purchasing decisions while incorporating per-
sonalized preferences. This section examines core technical approaches spanning image
transformation, body representation, and generative enhancement methods; explores
learning paradigms from supervised to advanced generative approaches; and analyzes
application domains including fixed-pose, multi-pose, and interactive try-on systems.
The framework illustrated in Figure 5 demonstrates how these technical components
integrate to create seamless user experiences.
21

Fig. 5Virtual Try-On framework for 3D fitting and size prediction.
5.1 Core Technical Approaches
Virtual try-on technology has evolved through several distinct technical approaches,
each addressing specific challenges in realistic garment rendering and transformation.
Image transformation techniques form the foundation of many virtual try-on sys-
tems. The pioneering work VITON (Virtual Try-On Network) [70] introduced a
coarse-to-fine warping framework that seamlessly transfers clothing items onto per-
son images. This approach uses a multi-task encoder-decoder network to create initial
visualizations, followed by refinement stages. Building on this foundation, CP-VTON
(Characteristic-Preserving Virtual Try-On Network) [71] introduced the Geometric
Matching Module (GMM) to better align garments with body shapes while pre-
serving clothing characteristics. More recent advancements include the SD-VITON
(Sequential Deformation VITON) [72] framework, which addresses texture squeezing
artifacts through disentangled appearance flow prediction, and the Progressive Infer-
ence Paradigm in PG-VTON (Progressive Generation VITON) [73], which separates
the try-on process into distinct specialized modules for improved performance.
Body and garment representation approaches have significantly improved the real-
ism of virtual try-on systems. Initially, representations were simplistic, but VITON-HD
(VITON High Definition) [74] introduced clothing-agnostic person representation,
allowing the model to reduce dependency on the original clothing worn by the person.
VTNFP (Virtual Try-on Network with Feature Preservation) [75] employs a three-
stage design that generates detailed body segmentation maps to delineate both body
parts and clothing regions. Addressing specific anatomical challenges, CP-VTON+
(Characteristic-Preserving VTON Plus) [76] features enhanced skin labeling to bet-
ter handle neck and chest areas previously misidentified as background. The semantic
understanding of clothing-body relationships was further advanced by ACGPN (Adap-
tive Content Generating and Preserving Network) [77], which explicitly models the
spatial layout to preserve occlusion relationships naturally.
Generative enhancement methods represent the cutting edge of virtual try-on
technology. Recent works have incorporated sophisticated generative techniques to
improve visual quality. C-VTON (Context-driven VITON) [78] employs conditional
normalization layers, leveraging contextual information to guide the generation pro-
cess. StableVITON [79] adapts pre-trained diffusion models for try-on tasks, using
22

zero cross-attention blocks to condition intermediate features. Skin texture realism
has been enhanced through specialized approaches like StyleGAN2-based inpainting
in PG-VTON [73], allowing for more natural transitions between garments and body
parts. Recent advances in diffusion-based virtual try-on include OOTDiffusion (Out-
fitting Fusion based Diffusion) [80], which introduced an innovative outfitting fusion
architecture that eliminates redundant warping processes through self-attention lay-
ers, providing precise alignment between garment features and target human bodies
while incorporating outfitting dropout for enhanced controllability. FITMI [81] inte-
grates virtual try-on with recommendation systems, providing personalized try-on
experiences through Latent Diffusion Model (LDM)-based approaches with text inver-
sion networks and automatic dataset selection capabilities. MV-VTON (Multi-View
Virtual Try-On Network) [82] further advanced this paradigm by introducing multi-
view virtual try-on capabilities through view-adaptive selection mechanisms and joint
attention blocks for pose-aware clothing feature extraction, enabling comprehensive
try-on experiences across different viewing angles.
5.2 Learning Paradigms
The evolution of virtual try-on systems has been characterized by increasingly sophis-
ticated learning approaches that balance supervision requirements with generation
quality.
Supervised approaches dominated early virtual try-on systems, relying on paired
data of clothing items and person images. VITON [70] employs a multi-task encoder-
decoder network trained with direct supervision to generate initial try-on results.
CP-VTON [71] introduced composition mask learning to better control which parts
of the aligned clothing should be preserved in the final synthesized image. LA-VITON
(Looking-Attractive VITON) [83] enhanced geometric matching through grid interval
consistency loss, demonstrating how specialized loss functions can improve specific
aspects of the try-on process. These supervised methods establish strong baselines but
often require carefully prepared training data.
Weakly-supervised methods emerged to address limitations in training data avail-
ability and quality. SwapNet [86] pioneered this direction, transferring garment
information across images with arbitrary clothing, body poses, and shapes without
requiring ideal paired data. VTNFP [75] incorporates self-attention mechanisms to
make correlation matching more robust, enabling the model to better understand
relationships between different image regions despite imperfect supervision. These
approaches demonstrate greater flexibility in real-world scenarios where perfectly
paired data may be unavailable.
Advanced generative methods represent the current state-of-the-art in learning
approaches. While conditional GANs have been widely used for image synthesis in
virtual try-on, recent work has introduced more sophisticated techniques. Stable-
VITON [79] uses attention total variation loss to produce sharper attention maps
for more precise preservation of clothing details. SD-VITON [72] developed a dis-
entangled appearance flow prediction that separates the optimization objectives for
different aspects of the transformation process. Wear-Any-Way [85] introduced sparse
23

T able 7Taxonomy of Virtual Try-On Methods: Technical Classification and Evaluation
W ork Approach Paradigm Domain
Image Transformation Techniques
VITON [70]
(2018)
Coarse-to-fine
warping with
multi-task encoder-
decoder
Supervised with
refinement network
Fixed-pose with frontal-
view try-on
CP-VTON [71]
(2018)
Geometric Match-
ing Module (GMM)
with composition
mask
Supervised with
cloth characteristic
preservation
Fixed-pose with improved
detail retention
LA-VITON [83]
(2019)
Enhanced GMM
with grid interval
consistency loss
Supervised with
occlusion handling
Fixed-pose with improved
alignment
SD-VITON [72]
(2024)
Sequential Defor-
mation framework
with disentangled
flow prediction
Adversarial with
specialized TV loss
High-resolution with anti-
squeezing mechanism
Body and Garment Representation
VTNFP [75]
(2019)
Three-stage design
with body segmen-
tation mapping
Self-attention
enhanced with con-
ditional GAN
Fixed-pose with improved
body part preservation
CP-VTON+ [76]
(2020)
Enhanced GMM
with explicit skin
labeling
Supervised with
improved segmen-
tation
Fixed-pose with better
neck/chest handling
ACGPN [77]
(2020)
Semantic layout
preservation with
adaptive generation
Second-order
constraint on Thin-
Plate Spline
Fixed-pose with occlusion
relationship modeling
VITON-HD [74]
(2021)
Clothing-agnostic
person representa-
tion
Misalignment-
aware
normalization
High-resolution synthesis
(1024×768)
Multi-Pose and Advanced Generation
MG-VTON [84]
(2019)
Multi-stage pose-
guided appearance
transformation
Conditional parsing
with Warp GAN
Multi-pose adaptation
with large variations
C-VTON [78]
(2022)
Context-driven
image generation
Conditional nor-
malization layers
Context-aware try-on
with environmental cues
PG-VTON [73]
(2024)
Progressive infer-
ence paradigm with
three specialized
modules
StyleGAN2-based
skin inpainting
Fixed-pose with advanced
skin preservation
Wear-Any-Way [85]
(2024)
Dual U-Net with
sparse correspon-
dence alignment
Interactive point-
based control
mechanism
User-controllable try-on
with style manipulation
StableVITON [79]
(2024)
Zero cross-
attention blocks for
feature condition-
ing
Diffusion model
adaptation
Fixed-pose with fine detail
preservation
OOTDiffusion [80]
(2025)
Outfitting fusion
with self-attention
alignment
Latent diffusion
with outfitting
dropout
Fixed-pose with enhanced
controllability
FITMI [81]
(2025)
LDM with text
inversion and
mask-aware skip
connections
Latent diffusion
with recommenda-
tion integration
Commercial application
with user experience focus
MV-VTON [82]
(2025)
View-adaptive
selection with joint
attention
Diffusion-based
multi-view genera-
tion
Multi-view try-on with
pose adaptation
24

correspondence alignment that enables precise user control over garment appear-
ance. OOTDiffusion [80] further advanced this paradigm with outfitting fusion that
combines latent diffusion with self-attention mechanisms for improved controllability
and alignment precision, while FITMI [81] introduced commercial-focused learning
paradigms that integrate latent diffusion models with recommendation systems for
personalized user experiences, and MV-VTON [82] developed multi-view learning
paradigms that adapt clothing features based on person pose through view-adaptive
selection mechanisms with hard-selection and soft-selection processes for global and
local feature extraction.
5.3 Application Domains
Virtual try-on technology has expanded across several application domains, each
addressing different user needs and technical challenges.
Fixed-pose try-on represents the foundational application, where clothing is trans-
ferred onto person images in standard poses—typically frontal views. Early VITON
approaches focused on this scenario due to its relative simplicity. Significant progress
has been made in high-resolution synthesis, with VITON-HD [74] achieving impres-
sive results at 1024×768 resolution. Within this domain, attention has increasingly
focused on detail preservation techniques for accurately rendering logos, patterns, and
textures that are critical for realistic visualization. While constrained in pose varia-
tion, fixed-pose try-on systems offer practical value for e-commerce applications where
standardized product presentation is common.
Multi-pose adaptation extends virtual try-on capabilities to handle diverse body
positions and viewing angles. MG-VTON [84] addresses this challenge by disentangling
the warping of clothes’ appearance from pose manipulation. This approach handles
large pose variations by processing these aspects in multiple distinct stages. Multi-
pose systems must address complex challenges, including self-occlusions and significant
garment deformations that occur when the body is in non-standard positions. These
systems provide more versatile try-on experiences that better reflect real-world usage
scenarios where clothing appearance changes substantially with body movement.
Interactive try-on systems represent the frontier of virtual try-on applications,
offering unprecedented user control. Wear-Any-Way [85] revolutionized this domain
with precise manipulation of how garments are worn through a point-based control
system. Their dual U-Net architecture with sparse correspondence alignment allows
users to interactively adjust features like sleeve rolling, coat opening, and tucking
styles. This transition from passive visualization to interactive manipulation marks a
significant advancement in user experience, moving virtual try-on systems closer to
the flexibility of physical fitting rooms. Commercial virtual try-on systems represent
a significant application domain, exemplified by FITMI [81], which integrates latent
diffusion models with recommendation systems, providing automatic dataset selection
and customized preprocessing pipelines with advanced pose processing techniques and
recommendation system integration, demonstrating the practical application of vir-
tual try-on technology in commercial settings. MV-VTON [82] addresses multi-view
applications in online shopping, enabling customers to see try-on results from multi-
ple angles through their system with view-adaptive selection mechanisms that handle
25

complex pose scenarios. OOTDiffusion [80] contributes to e-commerce applications
through its outfitting fusion approach, providing enhanced controllability for fash-
ion retail and online shopping platforms with personalized garment recommendation
systems.
5.4 Datasets and Evaluation
There are multiple datasets on the horizon now, but most of the works leverage
the VITON dataset [70]. It comprises 16,253 frontal-view women and top clothing
image pairs. For high-resolution usage, VITON-HD [74] is available with an image
size of 1024×768 comprising 13,679 frontal-view women and top clothing image pairs.
Another noticeably famous dataset is the MPV dataset, introduced in MG-VTON
[84], which contains 35,687 person images and 13,524 clothes images. Each person’s
image in MPV has different poses. The image is in the resolution of 256×192. Deep-
Fashion [87] is also a famous one that is frequently utilized. It contains over 800,000
diverse fashion images ranging from shop images to unconstrained consumer photos,
constituting the largest visual fashion analysis database. Each image in this dataset is
labeled with 50 categories, 1,000 descriptive attributes, a bounding box, and clothing
landmarks. Others include DressCode [88], Digital Wardrobe [89], TailorNet Dataset
[90], CLOTH3D [91], 3DPeople [92], THUman Dataset [93], FashionOn [94] and VVT
dataset [95].
The evaluation metrics used to measure the performance of existing fashion try-on
model modules include IS, which estimates realism and diversity of generated images.
Other commonly used measures include the Structural Similarity Index (SSIM), VGG-
based Perceptual Distance (PD), Perceptual Distance to Target Clothing (PD(TC)),
Total Variation (TV), pairwise A/B testing, Hyper Image Quality Assessment (hyper-
IQA), Kernel Inception Distance (KID), and the L1 loss function. In recent works, we
see LPIPS used in the paired setting, and FID adopted in the unpaired setting.
6 Fashion Forecasting
Fashion forecasting represents the forward-looking dimension of fashion AI, synthesiz-
ing insights from aesthetics, personalization, and virtual try-on to predict future trends
and market dynamics. This domain completes the fashion AI ecosystem by providing
temporal context that informs all other domains, enabling trend-aware personalization,
future-relevant virtual try-on options, and aesthetic evolution prediction. This section
explores core technical approaches, including time series analysis, visual attribute
analysis, and sales and consumer behavior modeling; examines learning paradigms
from unsupervised methods to transformer-based approaches; and analyzes applica-
tion domains covering visual trend prediction, commercial performance forecasting,
and social media trend analysis. The framework presented in Figure 6 demonstrates
how these components integrate to create predictive capabilities that enhance the
entire fashion AI system.
26

T able 8Evaluation Methods and Datasets in Virtual Try-On Research
W ork Metrics Dataset Key Contribution
VITON [70] IS VITON First image-based vir-
tual try-on framework
LA-VITON [83] IS, SSIM VITON Improved geometric
matching accuracy
VTNFP [75] A/B test VITON Three-stage design for
accurate detail capture
MG-VTON [84] A/B test, SSIM, IS MPV, DeepFashion Multi-pose handling
with self-occlusion res-
olution
CP-VTON+ [76] IoU, SSIM, LPIPS VITON Neck and chest area
preservation
ACGPN [77] SSIM, IS VITON, CPVI-
TON
Adaptive content
preservation based on
pose
VITON-HD [74] FID, LPIPS VITON-HD First high-resolution
(1024×768) approach
C-VTON [78] SSIM, FID VITON Context-guided syn-
thesis for improved
realism
SD-VITON [72] FID, KID, LPIPS,
SSIM
VITON-HD Resolution of texture
squeezing artifacts
PG-VTON [73] FID, IS, hyperIQA,
SSIM
VITON Top-down inference
pipeline for robust try-
on
Wear-Any-Way [85] FID, KID, SSIM,
LPIPS
Custom, VITON-
HD
First manipulable try-
on with interactive
control
StableVITON [79] FID, KID, SSIM,
LPIPS
VITON-HD, Dress-
Code
End-to-end try-on
with pre-trained diffu-
sion models
OOTDiffusion [80] FID, KID, SSIM,
LPIPS
VITON-HD, Dress-
Code
Outfitting fusion with
self-attention align-
ment
FITMI [81] FID, IS, User expe-
rience metrics
DressCode,
VITON-HD
Commercial virtual
try-on with recom-
mendation system
MV-VTON [82] SSIM, LPIPS, FID,
KID
MVG, VITON-HD,
DressCode
Multi-view virtual try-
on with pose adapta-
tion
27

Fig. 6Forecasting framework for trend prediction and market analysis.
6.1 Core Technical Approaches
Fashion forecasting involves predicting emerging trends and styles that will dominate
the industry in the near future using AI technologies. These approaches analyze exten-
sive data on current fashion trends, consumer behavior, social media activity, and
economic indicators using sophisticated algorithms and ML models.
Time series analysis forms a foundational approach in fashion forecasting, cap-
turing the temporal evolution of styles and trends. Fashion Forward [96] pioneered
an unsupervised approach to predicting future style popularity from fashion images.
Their model demonstrates capabilities for imagining new style combinations that will
gain popularity, identifying style dynamics (distinguishing between trendy and clas-
sic elements), and identifying key visual attributes that will dominate future fashion
landscapes. Building on this foundation, KERN (Knowledge Enhanced Recurrent Net-
work) [97] was developed as a tool for modeling time series data using a deep Recurrent
Neural Network (RNN) architecture. This approach integrates various internal and
external knowledge from the fashion domain alongside technical capabilities, creating
a comprehensive system that accounts for the industry’s unique challenges, including
the rapid pace of change and multiple influential factors.
Visual attribute analysis represents another critical technical approach in fashion
forecasting. The GeoStyle framework [98] automatically identifies clothing and style
attributes in images and analyzes their spatial and temporal trends. Their framework
demonstrated more accurate long-term trend forecasts for numerous fashion attributes
and styles compared to prior approaches. This technique involves extracting visual
features from fashion images and tracking their evolution across time and geographic
regions. Similarly, Lo et al. [99] developed methods relying on social media data of
individual outfit looks, predicting popularity with high accuracy by analyzing visual
elements.
Sales and consumer behavior modeling approaches complement visual analysis by
incorporating market data. Loureiro et al. [100] developed a deep learning approach
28

to predict fashion industry sales and forecast future performance of new products.
This method acknowledges that, despite fashion’s short product lifecycle, inventory
and purchase strategies can be informed by historical data from retailers’ databases.
These approaches focus less on visual elements and more on market performance
patterns, connecting trend analysis to business outcomes. More recently, Giri et al.
[101] proposed an intelligent forecasting system that combines image feature attributes
extracted using deep learning with sales data to predict future demand for new fashion
products. Their model uses machine learning clustering to identify product groups
based on sales patterns and image similarity, then employs neural networks to classify
new items and predict their sales profiles by finding the best match in established
clusters. Sousa et al. [102] developed a two-stage approach to forecast demand for new
products using censored data, employing Random Forest, Deep Neural Networks, and
Support Vector Regression algorithms to predict demand for new products, with an
additional model that weighted demands from historically similar products.
Exogenous knowledge integration has emerged as a promising approach in fash-
ion forecasting, as demonstrated by GTM-Transformer (Google Trends Multimodal
Transformer) [103] , which introduced a non-autoregressive transformer model that
systematically probes Google Trends time series data and combines it with multimodal
product information to forecast sales of new fashion items. This model encodes Google
Trends data representing product attribute popularity, then uses cross-attention to
understand which portions of these exogenous signals are most relevant to the sales
forecast. This approach effectively addresses the cold-start problem of forecasting for
brand-new products without sales history, showing that the most useful exogenous
information comes from 7-10 months prior to the product’s planned release, typically
the end of the previous year’s corresponding fashion season.
6.2 Learning Paradigms
Fashion forecasting employs diverse learning methodologies to capture the complex
dynamics of trend evolution and consumer preferences.
Unsupervised learning approaches offer advantages in discovering patterns without
pre-defined categories. Fashion Forward [96] demonstrated the effectiveness of unsu-
pervised methods in forecasting style popularity from fashion images, allowing the
model to identify emergent patterns rather than being constrained by predetermined
trend categories. This paradigm is particularly valuable in fashion, where novel styles
may not fit existing classifications. Unsupervised approaches can uncover unexpected
connections and emergent trends that supervised methods might miss.
Supervised prediction models provide alternative approaches when labeled data is
available. Chakraborty et al. [105] proposed an approach using logistic regression to
predict patterns and outfits based on Instagram posts from New York Fashion Week.
Similarly, Lo et al. [99] utilized Paper Doll Parsing models, InceptionV3, and LSTM
architectures in a supervised manner to predict outfit popularity. These approaches
leverage labeled datasets to train models that can predict specific aspects of future
fashion trends based on historical patterns. Giri et al. [101] demonstrated the effective-
ness of combining supervised classification with unsupervised clustering to categorize
fashion items based on their visual features and sales profiles, using neural networks
29

T able 9Taxonomy of Fashion Forecasting Methods: Technical Classification and Evaluation
W ork Approach Paradigm Domain
Time Series Analysis Approaches
Fashion Forward
[96] (2017)
Visual style evolu-
tion modeling
Unsupervised fash-
ion image analysis
Visual trend pre-
diction
KERN [97]
(2020)
Knowledge
enhanced recurrent
network
Deep RNNs with
domain knowledge
integration
Fine-grained fash-
ion element trends
Neo-Fashion [104]
(2021)
Periodic mode drift
prediction
Walk model analy-
sis with big data
Macroscopic
fashion season fore-
casting
Visual Attribute Analysis
Lo et al. [99]
(2019)
Social media outfit
analysis
Paper Doll Parsing
with LSTM
Outfit popularity
prediction
GeoStyle [98]
(2019)
Spatio-temporal
attribute tracking
Parametric model
with Gaussian mix-
ture
Long-term style
attribute forecast-
ing
Chakraborty et al.
[105] (2020)
Fashion week image
analysis
Logistic regression Runway-to-retail
trend prediction
Sales and Consumer Behavior Modeling
Loureiro et al. [100]
(2018)
Historical sales pat-
tern analysis
Deep learning with
multiple metrics
Commercial perfor-
mance forecasting
Giri et al. [101]
(2022)
Image features with
sales data integra-
tion
Hybrid: unsuper-
vised clustering
with neural net-
work classification
New product
demand forecasting
GTM-Transformer
[103]
(2024)
Exogenous knowl-
edge integration
with multimodal
data
Non-autoregressive
transformer
First-order inven-
tory optimization
Sousa et al. [102]
(2024)
Censored demand
modeling with
Expectation-
Maximization
(EM)
Two-stage method-
ology: EM for
demand estimation
+ ML for forecast-
ing
New product
demand forecast-
ing with substitute
analysis
to achieve 72.4% classification accuracy in predicting which sales pattern cluster a
new item would follow. Sousa et al. [102] employed a two-stage supervised learn-
ing approach where the first stage transforms censored sales data into true demand
estimates, while the second stage applies supervised learning algorithms (Random For-
est, Deep Neural Networks, Support Vector Regression) to predict demand for new
products.
Knowledge-enhanced methods integrate domain expertise with data-driven
approaches. KERN [97] represents a sophisticated example, combining deep recurrent
30

neural networks with fashion domain knowledge. This integration enhances the model’s
ability to account for industry-specific factors that purely data-driven approaches
might miss. Similarly, Neo-Fashion [104] presented a periodic mode drift prediction
scheme using walk model analysis for information-driven fashion trend forecasting,
incorporating domain understanding of fashion seasons. These approaches recognize
that effective fashion forecasting requires both technical capabilities and industry
knowledge.
Transformer-based methodologies have recently been applied to fashion fore-
casting, with GTM-Transformer [103] demonstrating its effectiveness through a
non-autoregressive transformer architecture. Unlike autoregressive approaches that
can suffer from error compounding, their model generates the entire sales forecast
at once by learning effective representations of both the product and exogenous
data sources. The authors show that this non-autoregressive design provides a 4.4%
improvement in forecasting accuracy compared to equivalent autoregressive implemen-
tations, highlighting the advantages of transformers’ parallel processing capabilities
for fashion forecasting tasks.
6.3 Application Domains
Fashion forecasting technologies address various industry needs, each with specific
focus and impact.
Visual trend prediction focuses on anticipating the evolution of style elements.
According to theories of fashion innovation, new ideas typically originate in the
designer’s arena before undergoing trickle-down, trickle-across, and trickle-up pro-
cesses. These ideas maintain relevance for at least one selling season, with successful
trends lasting longer. Seasonal trends are heavily influenced by catwalk appear-
ances, where they emerge as major items, colors, shapes, or styling approaches before
declining over the subsequent 6-12 months as consumers adopt newer trends. The
Neo-Fashion system [104] addressed the complex problem of mode drift prediction at
the macroscopic level for fashion seasons, moving beyond single-element prediction to
consider colors, fabrics, styles, and intricate details collectively.
Commercial performance forecasting translates trend predictions into business
implications. Loureiro et al.’s [100] deep learning approach specifically targets sales
prediction, helping businesses anticipate market performance. This application domain
connects aesthetic and style trends to their commercial impact, supporting inven-
tory planning, pricing strategies, and production decisions. Such forecasting helps
businesses balance creative innovation with market viability, ensuring that products
not only follow emerging trends but also meet consumer demand. Giri et al. [101]
advanced this domain by developing a model capable of predicting weekly sales for
new fashion items without historical data, addressing a critical industry challenge
of inventory management for newly launched products. Building on this foundation,
GTM-Transformer [103] introduced a technique that directly addresses the “first-order
problem” in fashion retail - determining optimal initial inventory quantities for new
products before their market launch. Their approach demonstrated a 17.5% reduction
in monetary discrepancy compared to traditional ordering policies, potentially saving
31

millions in inventory costs when scaled across a fashion retailer’s product catalog, high-
lighting the substantial business impact of advanced forecasting technologies. Sousa et
al. [102] focused specifically on forecasting demand for new products in fashion retail-
ing, utilizing a comprehensive dataset from a European fashion retailer comprising
63.6 million records across 684 products from 2015-2016 bag collections.
Social media trend analysis leverages digital platforms’ growing influence on fashion
dissemination. Lo et al.’s [99] study capitalizes on social media data to predict outfit
popularity, recognizing these platforms as excellent vehicles for showcasing and circu-
lating fashion trends to mass audiences. Similarly, Chakraborty et al.’s [105] approach
analyzes Instagram posts from fashion events to predict future patterns. This applica-
tion acknowledges that fashion runway shows provide inspiration for high-street and
fast-fashion retailers, with social media accelerating trend dissemination and adoption.
6.4 Datasets and Evaluation
Fashion prediction relies heavily on diverse datasets, emphasizing variety due to the
strong connection between prediction accuracy and consumer purchasing behavior.
DeepFashion [87] stands as one of the most popular datasets, offering comprehen-
sive coverage with rich consumer data and versatile annotations for clothes detection,
attribute prediction, fashion landmark estimation, and few-shot learning tasks. Social
media-inspired datasets include Lookbook [106], Insta NYFW-19 dataset [105], Neo-
Fashion Dataset [104], and the StreetStyle dataset [107] from Instagram, and the
Flickr 100M dataset [108]. These resources capture the interplay between social media
platforms and fashion runways. KERN [97] utilizes the Fashion Institute of Technol-
ogy (FIT) dataset, which combines characteristics of institutional fashion knowledge
with web-based data, merging the advantages of both knowledge and data-driven fore-
casting approaches. Giri et al. [101] utilized proprietary retail data from a European
fashion retailer, comprising sales information and product images for 290 fashion items
over a two-year period (2015-2016), demonstrating the value of industry collaborations
for obtaining real-world commercial data.
Addressing the critical need for public datasets in new product sales forecasting,
GTM-Transformer [103] introduced VISUELLE, a comprehensive multimodal dataset
containing 5,577 real fashion products from an Italian fast-fashion company. Each
product in VISUELLE is associated with an image, textual metadata (category, color,
fabric), 12 weeks of sales data, and three related Google Trends time series describ-
ing the popularity of product attributes. This enables benchmarking for new-product
forecasting under realistic cold-start conditions.
Evaluation metrics for fashion forecasting focus primarily on prediction accuracy
across various dimensions. Common metrics include Root Mean Square Error (RMSE),
Mean Absolute Percentage Error (MAPE), Mean Absolute Error (MAE), and Mean
Squared Error (MSE). For performance measurement, MAE and MAPE compare pre-
dictions against ground truth values to evaluate accuracy, while mAP assesses ranking
performance. KL divergence provides insight into feature deviation from baselines,
measuring how much each feature independently differs from expected patterns. MSE
often serves as an objective function during training, while Cosine Similarity Error
(CSE) indicates how closely predictions match actual ground truth patterns, reflecting
32

the system’s ability to capture trends correctly. For classification tasks within fore-
casting systems, metrics such as Classification Accuracy (CA), F1 score, precision,
recall, and AUC of ROC curves help evaluate how well models categorize items into
appropriate trend clusters or sales pattern groups. Recent advancements in evaluation
methodology introduced in GTM-Transformer [103] include the Weighted Absolute
Percentage Error (W APE), which expresses forecasting accuracy as a ratio of the
sum of absolute errors to the sum of actual values, and the tracking signal (TS)
measure, which quantifies forecasting bias by detecting systematic over- or underes-
timation. Additionally, the Edit Distance with Real Penalty (ERP) metric evaluates
a model’s ability to capture the actual dynamics of sales curves beyond simple point-
wise accuracy. These expanded evaluation approaches provide a more comprehensive
assessment of forecasting models, addressing both prediction accuracy and practical
business utility.
7 Future Work and Considerations
This study focuses on some less emphasized but potentially important areas within the
fashion industry. But a more detailed analysis is necessary to look at the psychological
factors and changing dynamics of the needs and wants of Generation Z. Fashion is
transient, so newness stands at the risk of obsolescence. Besides, our study did not
cover the heterogeneity in people’s tastes, which varies because of differences in gender
stereotypes and cultural influences. Fashion technology needs to adjust and make
room for emerging gender identities. The cultural impact on fashion will have an effect
on everything, starting from aesthetic preferences to cultural artifacts, rituals, and
appearance-based social norms. Clothes almost all the time are a symbol of heritage,
a reflection of religious beliefs, or a manifestation of ethnic identity. Three of these
elements will end up creating the identity of the person wearing it, within the context
of one cultural group, be it local or national. Thus, there needs to be a focus on that
as well.
The topic of “fashion” has not historically been taken seriously in discussions in
academia. But for many people, especially those who wear their identities on their
sleeves, the way they present their gender has a profound effect on what they feel com-
fortable wearing. Our literature reviews and structure in the future will be radically
revised to be more inclusive of all individuals in our target audience. Additionally,
another vital step going forward is promoting cultural sensitivity and diversity within
fashion aesthetics. This includes recognizing and celebrating cultural influence in
design as well as avoiding cultural appropriation, in order to create a more inclusive
and respectful fashion industry; one that weaves a narrative of respect and appre-
ciation for one another. Future applications could mean the creation of gender-free
fashion design and style; a means for an individual to reach with expression.
8 Conclusion
Our survey synthesized developments across aesthetics, personalization, virtual try-on,
and fashion forecasting, connecting these domains to the practical needs of recom-
mender systems. We highlighted how aesthetic modeling and cross-domain visual
33

T able 10Evaluation Methods and Datasets in Fashion Forecasting Research
W ork Metrics Dataset Key Contribution
Fashion Forward [96] MAE,
MAPE
DeepFashion First unsupervised
approach for visual style
popularity prediction
Loureiro et al. [100] R², RMSE,
MAPE,
MAE, MSE
Private com-
pany data
Deep learning for fashion
industry sales forecasting
Lo et al. [99] MSE, CSE Lookbook
dataset
Social media-based outfit
popularity prediction
GeoStyle [98] MAE,
MAPE
StreetStyle
and Flickr
100M
Spatial and temporal
trend analysis of fashion
attributes
KERN [97] MAE,
MAPE
Fashion
Trend
Dataset
(FIT)
Integrating domain
knowledge with recurrent
neural networks
Chakraborty et al. [105] MSE Instagram
posts of New
York Fash-
ion Week
(NYFW)-19
Fashion week social media
analysis for trend predic-
tion
Neo-Fashion [104] mAP Neo-Fashion
Dataset
Comprehensive fashion
season forecasting beyond
individual elements
Giri et al. [101] RMSE,
MAE, CA,
F1, AUC
European
fashion
retailer data
Image-based sales profile
prediction for new fashion
products
GTM-Transformer [103] W APE,
MAE, Time
Series, ERP
VISUELLE Exogenous knowledge
integration for new prod-
uct sales forecasting
Sousa et al. [102] MAE,
MAPE,
RMSE, R²
European
fashion
retailer
Two-stage censored
demand forecasting for
new products
understanding can inform compatibility and ranking, how personalization leverages
preference learning to tailor retrieval and generation, how virtual try-on integrates
with detection/segmentation and retrieval to enhance user decision-making, and how
forecasting informs trend-aware recommendations and inventory planning. We out-
lined shared datasets and evaluation metrics and identified open challenges for building
cohesive, user-centric, AI-driven fashion platforms.
The cross-domain integration analysis reveals significant opportunities for advanc-
ing fashion AI through unified approaches that leverage the strengths of each
domain while addressing their individual limitations. Future research should priori-
tize the development of integrated frameworks that can effectively combine aesthetic
34

assessment, personalized recommendations, realistic virtual try-on, and trend-aware
forecasting to create truly intelligent fashion systems that serve user needs across the
entire fashion lifecycle.
Declarations
Ethical Approval
Not applicable.
Consent to Participate
Not applicable.
Consent to Publish
Not applicable.
Data Availability
Not applicable.
Authors Contributions
Both authors contributed to the study conception and design. The first author con-
ducted the survey and analysis. The second author supervised the project. Both
authors read and approved the final manuscript.
Funding
The authors did not receive support from any organization for the submitted work.
Competing Interests
The authors have no relevant financial or non-financial interests to disclose.
9 Appendix A: Literature Search Methodology
This survey employed a systematic literature review approach to identify rele-
vant research works in AI fashion technologies. The search was conducted using
Google Scholar as the primary search engine. We used combinations of keywords
including “artificial intelligence,” “machine learning,” “deep learning,” “fashion,”
“clothing,” “apparel,” “personalization,” “recommendation,” “virtual try-on,” “aes-
thetic,” “style,” and “forecasting.“ Publications were limited to the period 2013-2025
to capture both foundational works and recent advancements.
35

References
[1] Iwata, T., Wanatabe, S., Sawada, H.: Fashion coordinates recommender system
using photographs from fashion magazines., pp. 2262–2267 (2011). https://doi.
org/10.5591/978-1-57735-516-8/IJCAI11-377
[2] Veit, A., Kovacs, B., Bell, S., McAuley, J., Bala, K., Belongie, S.: Learning visual
clothing style with heterogeneous dyadic co-occurrences (2015) https://doi.org/
10.1109/ICCV.2015.527
[3] Nguyen, H., Havig, M., Schistad, H., Almenningen, T., Kofod-Petersen, A.,
Langseth, H., Ramampiaro, H.: Learning to rank for personalised fashion
recommender systems via implicit feedback. (2014). https://doi.org/10.1007/
978-3-319-13817-6 6
[4] Shen, E., Lieberman, H., Lam, F.: What am i gonna wear?: Scenario-oriented rec-
ommendation, pp. 365–368 (2007). https://doi.org/10.1145/1216295.1216368
[5] Ghosh, H., Ajmani, S., Mallik, A., Chaudhury, S.: An ontology based personal-
ized garment recommendation system. (2013). https://doi.org/10.1109/WI-IAT.
2013.143
[6] Li, H., Cai, F., Liao, Z.: Content-based filtering recommendation algorithm using
hmm, pp. 275–277 (2012). https://doi.org/10.1109/ICCIS.2012.112
[7] Nogueira, E., Melo, E., Faria, E., Guliato, D.: Ikb-ms: A collaborative filtering
approach associated with human visual attention for clothing recommendation,
pp. 149–156 (2015). https://doi.org/10.1145/2820426.2820430
[8] Han, X., Wu, Z., Jiang, Y.-G., Davis, L.S.: Learning fashion compatibility with
bidirectional lstms. In: ACM Multimedia (2017)
[9] Hsiao, W.-L., Grauman, K.: Learning the latent” look”: Unsupervised discovery
of a style-coherent embedding from fashion images. In: Proceedings of the IEEE
International Conference on Computer Vision, pp. 4203–4212 (2017)
[10] Hsiao, W.-L., Grauman, K.: Creating capsule wardrobes from fashion images
(2017)
[11] Shih, Y.-S., Chang, K.-Y., Lin, H.-T., Sun, M.: Compatibility family learning for
item recommendation and generation. In: Proceedings of the AAAI Conference
on Artificial Intelligence, vol. 32 (2018)
[12] Song, X., Feng, F., Liu, J., Li, Z., Nie, L., Ma, J.: Neurostylist: Neural compat-
ibility modeling for clothing matching, pp. 753–761 (2017). https://doi.org/10.
1145/3123266.3123314
[13] McAuley, J., Targett, C., Shi, Q., Hengel, A.: Image-based recommendations on
36

styles and substitutes (2015) https://doi.org/10.1145/2766462.2767755
[14] Vasileva, M., Plummer, B., Dusad, K., Rajpal, S., Kumar, R., Forsyth, D.:
Learning type-aware embeddings for fashion compatibility (2018)
[15] Dhar, S., Ordonez, V., Berg, T.: High level describable attributes for predicting
aesthetics and interestingness, pp. 1657–1664 (2011). https://doi.org/10.1109/
CVPR.2011.5995467
[16] Gygli, M., Grabner, H., Riemenschneider, H., Nater, F., Van Gool, L.: The
interestingness of images, pp. 1633–1640 (2013). https://doi.org/10.1109/ICCV.
2013.205
[17] Isola, P., Xiao, J., Parikh, D., Torralba, A., Oliva, A.: What makes a photograph
memorable? IEEE transactions on pattern analysis and machine intelligence36
(2013) https://doi.org/10.1109/TPAMI.2013.200
[18] Khosla, A., Sarma, A.D., Hamid, R.: What makes an image popular? In: WWW
(2014)
[19] Simo-Serra, E., Fidler, S., Moreno-Noguer, F., Urtasun, R.: Neuroaesthetics
in Fashion: Modeling the Perception of Fashionability. In: Proceedings of the
Conference on Computer Vision and Pattern Recognition (CVPR) (2015)
[20] Cheng, W.-H., Song, S., Chen, C.-Y., Hidayati, S.C., Liu, J.: Fashion meets
computer vision: A survey. ACM Computing Surveys (CSUR)54(4), 1–41
(2021)
[21] Chen, H., Shuai, H., Cheng, W.: A survey of artificial intelligence in fashion.
IEEE Signal Processing Magazine40(3), 64–73 (2023) https://doi.org/10.1109/
MSP.2022.3233449 . Publisher Copyright:©1991-2012 IEEE.
[22] Islam, S.M., Joardar, S., Sekh, A.A.: A survey on fashion image retrieval. ACM
Comput. Surv. (2023) https://doi.org/10.1145/3636552 . Just Accepted
[23] Ding, Y., Lai, Z., Mok, P.Y., Chua, T.-S.: Computational technologies for fashion
recommendation: A survey. ACM Comput. Surv.56(5) (2023) https://doi.org/
10.1145/3627100
[24] Giri, C., Jain, S., Zeng, X., Bruniaux, P.: A detailed review of artificial intelli-
gence applied in the fashion and apparel industry. IEEE Access7, 95376–95396
(2019) https://doi.org/10.1109/ACCESS.2019.2928979
[25] Chakraborty, S., Hoque, M.S., Rahman Jeem, N., Biswas, M.C., Bardhan, D.,
Lobaton, E.: Fashion recommendation systems, models and methods: A review.
Informatics8(3) (2021) https://doi.org/10.3390/informatics8030049
[26] Jain, V., Wah, C.: Computer vision in fashion trend analysis and applications.
37

Journal of Student Research11(2022) https://doi.org/10.47611/jsrhs.v11i1.
2464
[27] Ghodhbani, H., Neji, M., Razzak, I., Alimi, A.: You can try without visit-
ing: a comprehensive survey on virtually try-on outfits. Multimedia Tools and
Applications81(2022) https://doi.org/10.1007/s11042-022-12802-6
[28] Song, D., Zhang, X., Zhou, J., Nie, W., Tong, R., Kankanhalli, M., Liu, A.-A.:
Image-based virtual try-on: A survey. International Journal of Computer Vision
133(12), 2692–2720 (2024)
[29] Shelley, J.: The Concept of the Aesthetic. The Stanford Encyclopedia of Philoso-
phy. Spring 2022 Edition, Edward N. Zalta (ed.) (2022). https://plato.stanford.
edu/archives/spr2022/entries/aesthetic-concept/
[30] Liu, S., Feng, J., Song, Z., Zhang, T., Lu, H., Xu, C., Yan, S.: Hi, magic closet,
tell me what to wear! In: Proceedings of the 20th ACM International Conference
on Multimedia, pp. 619–628 (2012)
[31] Jia, J., Huang, J., Shen, G., He, T., Liu, Z., Luan, H., Yan, C.: Learning to appre-
ciate the aesthetic effects of clothing. In: Proceedings of the AAAI Conference
on Artificial Intelligence, vol. 30 (2016)
[32] Yu, W., Zhang, H., He, X., Chen, X., Xiong, L., Qin, Z.: Aesthetic-based clothing
recommendation. In: Proceedings of the 2018 World Wide Web Conference, pp.
649–658 (2018)
[33] Zhang, X., Jia, J., Gao, K., Zhang, Y., Zhang, D., Li, J., Tian, Q.: Trip out-
fits advisor: Location-oriented clothing recommendation. IEEE Transactions on
Multimedia19(11), 2533–2544 (2017)
[34] Tautkute, I., Trzci´ nski, T., Skorupa, A.P., Brocki,  L., Marasek, K.: Deepstyle:
Multimodal search engine for fashion and interior design. IEEE Access7, 84613–
84628 (2019)
[35] Shamoi, P., Inoue, A., Kawanaka, H.: Color aesthetics and context-dependency.
In: 2022 Joint 12th International Conference on Soft Computing and Intelligent
Systems and 23rd International Symposium on Advanced Intelligent Systems
(SCIS&ISIS), pp. 1–8 (2022). IEEE
[36] Liu, C., Zhuang, J.: A probabilistic multi-topic model learned from aesthetic
quality communities for dress colors recommendation. IEEE Access13, 64930–
64947 (2025) https://doi.org/10.1109/ACCESS.2025.3559670
[37] Lin, Y., Ren, P., Chen, Z., Ren, Z., Ma, J., De Rijke, M.: Improving outfit
recommendation with co-supervision of fashion generation. In: The World Wide
Web Conference, pp. 1095–1105 (2019)
38

[38] He, R., Packer, C., McAuley, J.: Monomer: Non-metric mixtures-of-embeddings
for learning visual compatibility across categories. CoRR, vol. abs/1603.09473
(2016)
[39] Liu, J., Zhao, P., Zhuang, F., Liu, Y., Sheng, V.S., Xu, J., Zhou, X., Xiong,
H.: Exploiting aesthetic preference in deep cross networks for cross-domain rec-
ommendation. In: Proceedings of The Web Conference 2020, pp. 2768–2774
(2020)
[40] Zou, X., Pang, K., Zhang, W., Wong, W.: How good is aesthetic ability of a
fashion model? In: 2022 IEEE/CVF Conference on Computer Vision and Pattern
Recognition (CVPR), pp. 21168–21177 (2022)
[41] Kalantidis, Y., Kennedy, L., Li, L.-J.: Getting the look: Clothing recognition
and segmentation for automatic product suggestions in everyday photos. (2013).
https://doi.org/10.1145/2461466.2461485
[42] Kiapour, M., Han, X., Lazebnik, S., Berg, A., Berg, T.: Where to buy it:
Matching street clothing photos in online shops, pp. 3343–3351 (2015). https:
//doi.org/10.1109/ICCV.2015.382
[43] Yan, S.: Street-to-shop: Cross-scenario clothing retrieval via parts alignment and
auxiliary set, pp. 3330–3337 (2012)
[44] Vittayakorn, S., Yamaguchi, K., Berg, A., Berg, T.: Runway to realway: Visual
analysis of fashion. Proceedings - 2015 IEEE Winter Conference on Applica-
tions of Computer Vision, W ACV 2015, 951–958 (2015) https://doi.org/10.1109/
W ACV.2015.131
[45] Yang, W., Luo, P., Lin, L.: Clothing co-parsing by joint image segmentation and
labeling. In: Computer Vision and Pattern Recognition (CVPR), 2014 IEEE
Conference On (2013). IEEE
[46] Lin, Y., Ren, P., Chen, Z., Ren, Z., Ma, J., De Rijke, M.: Explainable out-
fit recommendation with joint outfit matching and comment generation. IEEE
Transactions on Knowledge and Data Engineering32(8), 1502–1516 (2019)
[47] Gitnux: Global Apparel Industry 2023: Statistics and trends (2023). https://
blog.gitnux.com/global-apparel-industry-statistics/
[48] Wang, L., Zeng, X., Koehl, L., Chen, Y.: Intelligent fashion recommender
system: Fuzzy logic in personalized garment design. IEEE Transactions on
Human-Machine Systems45(1), 95–109 (2014)
[49] Hu, Y., Yi, X., Davis, L.S.: Collaborative fashion recommendation: A functional
tensor factorization approach. In: Proceedings of the 23rd ACM International
Conference on Multimedia, pp. 129–138 (2015)
39

[50] Yu, M., Ma, Y., Wu, L., Wang, C., Li, X., Meng, L.: Fashiondpo:fine-tune
fashion outfit generation model using direct preference optimization. In: Pro-
ceedings of the 48th International ACM SIGIR Conference on Research and
Development in Information Retrieval. SIGIR ’25, pp. 212–222. Association for
Computing Machinery, New York, NY, USA (2025). https://doi.org/10.1145/
3726302.3729976
[51] Lecun, Y., Bottou, L., Bengio, Y., Haffner, P.: Gradient-based learning applied
to document recognition. Proceedings of the IEEE86, 2278–2324 (1998) https:
//doi.org/10.1109/5.726791
[52] Krizhevsky, A., Sutskever, I., Hinton, G.: Imagenet classification with deep con-
volutional neural networks. Neural Information Processing Systems25(2012)
https://doi.org/10.1145/3065386
[53] Chatfield, K., Simonyan, K., Vedaldi, A., Zisserman, A.: Return of the devil in
the details: Delving deep into convolutional nets. BMVC 2014 - Proceedings of
the British Machine Vision Conference 2014 (2014) https://doi.org/10.5244/C.
28.6
[54] Szegedy, C., Liu, W., Jia, Y., Sermanet, P., Reed, S., Anguelov, D., Erhan,
D., Vanhoucke, V., Rabinovich, A.: Going deeper with convolutions. The IEEE
Conference on Computer Vision and Pattern Recognition (CVPR), 1–9 (2015)
https://doi.org/10.1109/CVPR.2015.7298594
[55] Liu, Q., Wu, S., Wang, L.: Deepstyle: Learning user preferences for visual
recommendation. In: Proceedings of the 40th International ACM SIGIR Con-
ference on Research and Development in Information Retrieval. SIGIR ’17, pp.
841–844. Association for Computing Machinery, New York, NY, USA (2017).
https://doi.org/10.1145/3077136.3080658
[56] Chen, X., Chen, H., Xu, H., Zhang, Y., Cao, Y., Qin, Z., Zha, H.: Personalized
fashion recommendation with visual explanations based on multimodal attention
network: Towards visually explainable recommendation. In: Proceedings of the
42nd International ACM SIGIR Conference on Research and Development in
Information Retrieval, pp. 765–774 (2019)
[57] Guan, W., Jiao, F., Song, X., Wen, H., Yeh, C.-H., Chang, X.: Personalized fash-
ion compatibility modeling via metapath-guided heterogeneous graph learning.
In: Proceedings of the 45th International ACM SIGIR Conference on Research
and Development in Information Retrieval, pp. 482–491 (2022). ACM
[58] Song, X., Feng, F., Han, X., Yang, X., Liu, W., Nie, L.: Neural compati-
bility modeling with attentive knowledge distillation. The 41st International
ACM SIGIR Conference on Research and Development in Information Retrieval
(2018)
40

[59] Li, Y., Cao, L., Zhu, J., Luo, J.: Mining fashion outfit composition using an end-
to-end deep learning approach on set data. IEEE Transactions on Multimedia
PP(2016) https://doi.org/10.1109/TMM.2017.2690144
[60] Kang, W.-C., Fang, C., Wang, Z., McAuley, J.: Visually-aware fashion rec-
ommendation and design with generative image models. In: 2017 IEEE
International Conference on Data Mining (ICDM), pp. 207–216 (2017). IEEE
[61] Ding, Y., Mok, P.Y., Ma, Y., Bin, Y.: Personalized fashion outfit generation with
user coordination preference learning. Information Processing & Management
60(2), 103434 (2023)
[62] Xu, Y., Wang, W., Feng, F., Ma, Y., Zhang, J., He, X.: Diffusion models for gen-
erative outfit recommendation. In: Proceedings of the 47th International ACM
SIGIR Conference on Research and Development in Information Retrieval, pp.
1350–1359 (2024). ACM
[63] Wu, D., Yu, Z., Ma, N., Jiang, J., Wang, Y., Zhou, G., Deng, H., Li, Y.: Styleme:
Towards intelligent fashion generation with designer style. In: Proceedings of
the 2023 CHI Conference on Human Factors in Computing Systems, pp. 1–16
(2023). ACM
[64] Sun, K., Zhang, P., Zhang, J., Tao, J., Yuan, K.: Pfnet: Attribute-aware personal-
ized fashion editing with explainable fashion compatibility analysis. Information
Processing & Management61, 103540 (2024)
[65] He, R., McAuley, J.: Ups and downs: Modeling the visual evolution of fash-
ion trends with one-class collaborative filtering. In: Proceedings of the 25th
International Conference on World Wide Web, pp. 507–517 (2016)
[66] Chen, W., Huang, P., Xu, J., Guo, X., Guo, C., Sun, F., Li, C., Pfadler, A., Zhao,
H., Zhao, B.: Pog: personalized outfit generation for fashion recommendation
at alibaba ifashion. In: Proceedings of the 25th ACM SIGKDD International
Conference on Knowledge Discovery & Data Mining, pp. 2662–2670 (2019)
[67] Lu, Z., Hu, Y., Jiang, Y., Chen, Y., Zeng, B.: Learning binary code for person-
alized fashion recommendation. In: Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pp. 10562–10570 (2019)
[68] Li, X., Wang, X., He, X., Chen, L., Xiao, J., Chua, T.-S.: Hierarchical fashion
graph network for personalized outfit recommendation. In: Proceedings of the
43rd International ACM SIGIR Conference on Research and Development in
Information Retrieval, pp. 159–168 (2020)
[69] Lu, Z., Hu, Y., Chen, Y., Zeng, B.: Personalized outfit recommendation with
learnable anchors. In: Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pp. 12722–12731 (2021)
41

[70] Han, X., Wu, Z., Wu, Z., Yu, R., Davis, L.S.: Viton: An image-based virtual try-
on network. In: Proceedings of the IEEE Conference on Computer Vision and
Pattern Recognition, pp. 7543–7552 (2018)
[71] Wang, B., Zheng, H., Liang, X., Chen, Y., Lin, L., Yang, M.: Toward
characteristic-preserving image-based virtual try-on network. In: Proceedings of
the European Conference on Computer Vision (ECCV), pp. 589–604 (2018)
[72] Shim, S.-H., Chung, J., Heo, J.-P.: Towards squeezing-averse virtual try-on via
sequential deformation. In: Proceedings of the AAAI Conference on Artificial
Intelligence, vol. 38, pp. 4856–4863 (2024)
[73] Fang, N., Qiu, L., Zhang, S., Wang, Z., Hu, K.: Pg-vton: A novel image-based
virtual try-on method via progressive inference paradigm. IEEE Transactions
on Multimedia26, 6595–6608 (2024)
[74] Choi, S., Park, S., Lee, M., Choo, J.: Viton-hd: High-resolution virtual try-
on via misalignment-aware normalization. In: Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pp. 14131–14140
(2021)
[75] Yu, R., Wang, X., Xie, X.: Vtnfp: An image-based virtual try-on network
with body and clothing feature preservation. In: Proceedings of the IEEE/CVF
International Conference on Computer Vision, pp. 10511–10520 (2019)
[76] Minar, M.R., Tuan, T.T., Ahn, H., Rosin, P., Lai, Y.-K.: Cp-vton+: Clothing
shape and texture preserving image-based virtual try-on. In: CVPR Workshops,
vol. 3, pp. 10–14 (2020)
[77] Yang, H., Zhang, R., Guo, X., Liu, W., Zuo, W., Luo, P.: Towards photo-realistic
virtual try-on by adaptively generating-preserving image content. In: Proceed-
ings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 7850–7859 (2020)
[78] Fele, B., Lampe, A., Peer, P., Struc, V.: C-vton: Context-driven image-based
virtual try-on network. In: Proceedings of the IEEE/CVF Winter Conference
on Applications of Computer Vision, pp. 3144–3153 (2022)
[79] Kim, J., Gu, G., Park, M., Park, S., Choo, J.: Stableviton: Learning semantic
correspondence with latent diffusion model for virtual try-on. In: Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp.
8176–8185 (2024)
[80] Xu, Y., Gu, T., Chen, W., Chen, A.: Ootdiffusion: Outfitting fusion based latent
diffusion for controllable virtual try-on, vol. 39, pp. 8996–9004 (2025). https:
//doi.org/10.1609/aaai.v39i9.32973
42

[81] Samy, T.M., Asham, B.I., Slim, S.O., Abohany, A.A.: Revolutionizing online
shopping with fitmi: a realistic virtual try-on solution37(8), 6125–6144 (2025)
https://doi.org/10.1007/s00521-024-10843-6
[82] Wang, H., Zhang, Z., Di, D., Zhang, S., Zuo, W.: Mv-vton: Multi-view virtual
try-on with diffusion models. Proceedings of the AAAI Conference on Artificial
Intelligence39, 7682–7690 (2025)
[83] Lee, H.J., Lee, R., Kang, M., Cho, M., Park, G.: La-viton: A network for looking-
attractive virtual try-on. In: Proceedings of the IEEE/CVF International
Conference on Computer Vision Workshops, pp. 0–0 (2019)
[84] Dong, H., Liang, X., Shen, X., Wang, B., Lai, H., Zhu, J., Hu, Z., Yin, J.: Towards
multi-pose guided virtual try-on network. In: Proceedings of the IEEE/CVF
International Conference on Computer Vision, pp. 9026–9035 (2019)
[85] Chen, M., Chen, X., Zhai, Z., Ju, C., Hong, X., Lan, J., Xiao, S.: Wear-any-way:
Manipulable virtual try-on via sparse correspondence alignment. In: European
Conference on Computer Vision, pp. 124–142. Springer, Cham (2024)
[86] Raj, A., Sangkloy, P., Chang, H., Hays, J., Ceylan, D., Lu, J.: Swapnet: Image
based garment transfer. In: Computer Vision–ECCV 2018: 15th European Con-
ference, Munich, Germany, September 8–14, 2018, Proceedings, Part XII 15, pp.
679–695 (2018). Springer
[87] Liu, Z., Luo, P., Qiu, S., Wang, X., Tang, X.: Deepfashion: Powering robust
clothes recognition and retrieval with rich annotations. In: Proceedings of IEEE
Conference on Computer Vision and Pattern Recognition (CVPR) (2016)
[88] Morelli, D., Fincato, M., Cornia, M., Landi, F., Cesari, F., Cucchiara, R.:
Dress code: High-resolution multi-category virtual try-on. In: Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp.
2231–2235 (2022)
[89] Bhatnagar, B.L., Tiwari, G., Theobalt, C., Pons-Moll, G.: Multi-garment net:
Learning to dress 3d people from images. In: IEEE International Conference on
Computer Vision (ICCV) (2019). IEEE
[90] Patel, C., Liao, Z., Pons-Moll, G.: Tailornet: Predicting clothing in 3d as a func-
tion of human pose, shape and garment style. In: IEEE Conference on Computer
Vision and Pattern Recognition (CVPR) (2020). IEEE
[91] Bertiche, H., Madadi, M., Escalera, S.: Cloth3d: Clothed 3d humans. In:
European Conference on Computer Vision, pp. 344–359 (2020). Springer
[92] Pumarola, A., Sanchez, J., Choi, G., Sanfeliu, A., Moreno-Noguer, F.: 3DPeople:
Modeling the Geometry of Dressed Humans. In: International Conference in
43

Computer Vision (ICCV) (2019)
[93] Yu, T., Zheng, Z., Guo, K., Liu, P., Dai, Q., Liu, Y.: Function4d: Real-time
human volumetric capture from very sparse consumer rgbd sensors. In: IEEE
Conference on Computer Vision and Pattern Recognition (CVPR2021) (2021)
[94] Hsieh, C.-W., Chen, C.-Y., Chou, C.-L., Shuai, H.-H., Liu, J., Cheng, W.-H.:
Fashionon: Semantic-guided image-based virtual try-on with detailed human and
clothing information. In: Proceedings of the 27th ACM International Conference
on Multimedia, pp. 275–283 (2019)
[95] Dong, H., Liang, X., Shen, X., Wu, B., Chen, B.-C., Yin, J.: Fw-gan:
Flow-navigated warping gan for video virtual try-on. In: Proceedings of the
IEEE/CVF International Conference on Computer Vision, pp. 1161–1170
(2019)
[96] Al-Halah, Z., Stiefelhagen, R., Grauman, K.: Fashion forward: Forecasting
visual style in fashion. 2017 IEEE International Conference on Computer Vision
(ICCV), 388–397 (2017)
[97] Ma, Y., Ding, Y., Yang, X., Liao, L., Wong, W.K., Chua, T.-S.: Knowl-
edge enhanced neural fashion trend forecasting. In: Proceedings of the 2020
International Conference on Multimedia Retrieval, pp. 82–90 (2020)
[98] Mall, U., Matzen, K., Hariharan, B., Snavely, N., Bala, K.: Geostyle: Discover-
ing fashion trends and events. In: Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 411–420 (2019)
[99] Lo, L., Liu, C.-L., Lin, R.-A., Wu, B., Shuai, H.-H., Cheng, W.-H.: Dress-
ing for attention: Outfit based fashion popularity prediction. In: 2019 IEEE
International Conference on Image Processing (ICIP), pp. 3222–3226 (2019).
IEEE
[100] Loureiro, A.L., Migu´ eis, V.L., Silva, L.F.: Exploring the use of deep neural net-
works for sales forecasting in fashion retail. Decision Support Systems114, 81–93
(2018)
[101] Giri, C., Chen, Y.: Deep learning for demand forecasting in the fashion and
apparel retail industry. Forecasting4(2), 565–581 (2022) https://doi.org/10.
3390/forecast4020031
[102] Sousa, M.S., Loureiro, A.L.D., Migu´ eis, V.L.: Predicting demand for new prod-
ucts in fashion retailing using censored data. Expert Systems with Applications
259, 125313 (2025) https://doi.org/10.1016/j.eswa.2024.125313
[103] Skenderi, G., Joppi, C., Denitto, M., Cristani, M.: Well googled is half done:
Multimodal forecasting of new fashion product sales with image-based google
44

trends. Journal of Forecasting43(6), 1982–1997 (2024)
[104] Zhao, L., Li, M., Sun, P.: Neo-fashion: A data-driven fashion trend forecasting
system using catwalk analysis. Clothing and Textiles Research Journal, 0887302–
211004299 (2021)
[105] Chakraborty, S., Hoque, S.A., Kabir, S.F.: Predicting fashion trend using run-
way images: application of logistic regression in trend forecasting. International
Journal of Fashion Design, Technology and Education13(3), 376–386 (2020)
[106] Yoo, D., Kim, N., Park, S., Paek, A.S., Kweon, I.-S.: Pixel-level domain transfer.
In: European Conference on Computer Vision (2016)
[107] Matzen, K., Bala, K., Snavely, N.: Streetstyle: Exploring world-wide clothing
styles from millions of photos. arXiv preprint arXiv:1706.01869 (2017)
[108] Thomee, B., Shamma, D.A., Friedland, G., Elizalde, B., Ni, K., Poland,
D., Borth, D., Li, L.-J.: Yfcc100m: The new data in multimedia research.
Communications of the ACM59(2), 64–73 (2016)
45
