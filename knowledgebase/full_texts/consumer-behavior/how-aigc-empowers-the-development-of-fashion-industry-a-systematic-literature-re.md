---
title: 'How AIGC empowers the development of fashion industry: a systematic literature review and future
  research directions'
url: https://doi.org/10.1186/s40691-026-00479-6
category: consumer-behavior
subcategory: case-study
date: 2026-07
venue: Fashion and Textiles
authors:
- Rufan Lin
- Yihan Yu
- Fan Xia
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1186/s40691-026-00479-6.pdf
pages: 36
chars: 109045
fetched_at: '2026-11-08T18:30:41+00:00'
kb_version: 1
---

# How AIGC empowers the development of fashion industry: a systematic literature review and future research directions

Open Access
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you
modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of
it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise
in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted
by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy
of this licence, visit http:// creat iveco mmons. org/ licen ses/ by- nc- nd/4. 0/.
REVIEW
Lin et al. Fashion and Textiles           (2026) 13:32
https://doi.org/10.1186/s40691-026-00479-6
Fashion and Textiles
How AIGC empowers the development
of fashion industry: a systematic literature
review and future research directions
Rufan Lin1, Yihan Yu2, Fan Xia2 and Manhao Guan1*
Abstract
With the rapid diffusion of AIGC technologies, the fashion industry has entered a new
phase of technology-enabled transformation across multiple application scenarios.
Using a Systematic Literature Review approach, this study analyzes 163 publications
retrieved from Web of Science, EBSCO, IEEE Xplore, and Scopus to examine the research
landscape, technological pathways, thematic focuses, and future directions of AIGC
in fashion. The results indicate that related research has grown rapidly since 2022,
forming an overall international trend of multi-center distribution and broad participa-
tion; relevant studies are widely distributed in interdisciplinary journals, and empirical
case studies and quantitative research are currently the dominant paradigms. The
technological evolution reveals a gradual paradigm shift from GAN-based approaches
toward Diffusion Models and Large Language Models (LLMs). Research themes primar-
ily focus on Intelligent Design & Customization, Trend Forecasting & Consumer Behav-
ior, AI & Fashion Education, Law & Ethics, and Sustainable Fashion Design; furthermore,
based on qualitative analysis, a three-layer framework of "Application–Design–Attrib-
ute" is constructed to elucidate the advantages and risks of AIGC in the fashion indus-
try. Finally, this study proposes future research agendas such as advancing the three-
layer architecture and building multi-agent collaborative systems. This research
contributes to a deeper understanding of how AIGC empowers the fashion industry
and provides a reference for related research.
Keywords: Artificial Intelligence-Generated Content (AIGC), Fashion industry,
Systematic Literature Review (SLR), Human-AI collaboration, Multi-agent systems,
Sustainable fashion
Introduction
Artificial Intelligence-Generated Content (AIGC) has triggered profound changes in
the fashion industry (Carvalho et al., 2019; Jang & Ha, 2023), and has been extensively
integrated into fashion design, production, and market operations (An et al., 2023; Choi
et al., 2023; Lee et al., 2020). In the design stage, AIGC collaborates with humans (Ke
& Wang, 2024), playing a significant role in shortening design cycles, enhancing crea -
tive efficiency, and enriching design expressiveness (Kouslis et al., 2025); in the produc -
tion stage, AI-driven systems can optimize manufacturing processes, reduce costs, and
*Correspondence:
guanmh@zju.edu.cn
1 College of Computer Science
and Technology, Zhejiang
University, Hangzhou 310018,
Zhejiang, China
2 School of Fashion Design &
Engineering, Zhejiang Sci-Tech
University, Hangzhou 310018,
Zhejiang, China

Page 2 of 36Lin et al. Fashion and Textiles           (2026) 13:32
improve resource utilization efficiency (Oh & Kim, 2023; Ramos et al., 2023); in the mar-
ket operations stage, the data analytics capabilities of AI enhance the accuracy of person-
alized recommendations and trend forecasting (Dubey et al., 2020), and the explanatory
mechanisms of AI systems also help improve user satisfaction in fashion recommenda -
tion systems (Yeo et al., 2026). In addition, AIGC is gradually entering fashion educa -
tion, supporting students’ learning processes in design ideation and creative exploration,
and promoting the development of human–AI collaboration-oriented pedagogy (An &
Park, 2026).
Against this backdrop, a growing body of scholarship has started to examine the
specific functions of AIGC within fashion-related contexts. Previous review work has
already outlined several application scenarios of AIGC in fashion. For example, Giri
et al. (2019) thematically summarized fashion-related research based on methods such
as machine learning, and reviewed the main application scenarios and future trends.
Chakraborty et al. (2021) investigated fashion recommendation systems, analyzing their
algorithmic models and filtering techniques. In studies closer to the consumer side, Pil -
larisetty and Mishra (2022) focused on the role of artificial intelligence in enhancing
customer experience, covering chatbots, personalized recommendations, and virtual
try-ons. At the supply chain and production levels, Giovanni et al. (2025) reviewed pro -
duction planning and control, highlighting the potential of AI and meta-heuristic algo -
rithms in achieving ethical and sustainable production in Industry 5.0. Karimova et al.
(2026) explored AI-driven digital supply chains from the perspective of social sustain -
ability, emphasizing their key role in optimizing transparency and supporting ethical
labor practices.
Overall, existing studies provide an important foundation for understanding the appli-
cation of AI in the fashion field, but there is still a lack of systematic integration regard -
ing the development trajectory, core issues, and the relationship between the advantages
and risks of AIGC in the fashion industry. To address this, this study employs a System -
atic Literature Review (SLR) to review the relevant literature and conducts the analysis
around the following questions:
RQ1: What is the overall research landscape of AIGC in the fashion industry?
RQ2: What are the technological evolution characteristics and main research themes
of AIGC in the fashion industry?
RQ3: What are the core advantages and potential risks of AIGC in empowering the
fashion industry?
RQ4: What are the future research directions for the AIGC-empowered fashion
industry?
To further clarify the analytical object and scope of this study, and given that the use
of terminology and concepts has not yet been fully unified (Figoli et al., 2025), this study
adopts the term " AIGC" and defines it as a comprehensive intelligent system centered on
generative models and integrated with trend forecasting and consumer insights (Baek
et  al., 2022; Karimova et  al., 2026). Based on this definition, the scope of the fashion
industry discussed in this paper covers design, production, marketing, education, as well
as ethics- and sustainability-related contexts.
The contributions of this study are reflected in three main aspects. First, it integrates
research progress on AIGC across different segments from the perspective of the

Page 3 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

fashion industry as a whole, thereby extending existing studies that have largely focused
on specific scenarios. Second, it traces the developmental trajectory of AIGC in the fash-
ion industry from the perspective of technological evolution, revealing its evolutionary
characteristics from data-driven analysis and visual simulation to semantic co-creation.
Third, based on thematic analysis, it constructs a three-layer analytical framework of
" Application-Design-Attribute" to explain the advantages, risks, and future research
directions of AIGC-enabled fashion. This study seeks to provide a clearer analytical path
for understanding the mechanisms through which AIGC empowers the fashion industry
and to offer a reference for future research.
Methods and Materials
This study adopts the Systematic Literature Review (SLR) method (Diekemper, 2015;
Page et  al., 2021), following the PRISMA (Preferred Reporting Items for Systematic
Reviews and Meta-Analyses) guidelines (Moher et al., 2009). This approach provides a
standardized framework for literature screening and evaluation. Based on this frame -
work, a coding scheme is developed to extract structured information, including publi -
cation volume, publication years, and journal categories, for quantitative and visualized
analysis. For unstructured texts, qualitative inductive analysis is used for further discus -
sion. The overall research framework is illustrated in Fig. 1.
Fig. 1 Research framework

Page 4 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Initial literature search
To ensure the literature search complies with the requirements of the PRISMA guide -
lines (Moher et al., 2009), and drawing on relevant studies (Jabari et al., 2024; Ramos
et  al., 2023), four core databases—Web of Science, EBSCO, IEEE Xplore, and Sco -
pus—were selected as literature sources. Referring to existing studies, this study
formulated a search strategy to balance the coverage and relevance of the retrieval
results (Chan et al., 2024; Giri et al., 2019; Ramos et al., 2023). Taking Web of Science
as an example, the search query was defined as: TS = (" Artificial Intelligence" OR AI
OR "Machine Learning" OR "Deep Learning" OR "Generative Design" OR " AI Fash -
ion" OR "Digital Fashion" OR "Fashion Technology" OR "Virtual Fashion" OR "Fashion
Innovation") AND TS = ("Fashion Design" OR " Apparel Design" OR "Clothing Design"
OR "Fashion Industry" OR " AI in Fashion" OR "Fashion Technology" OR "3D Fashion
Design" OR "Fashion Metaverse"), with a time range from January 2015 to December
20, 2025.
Manual screening
The initial search results contained literature that was irrelevant to the research topic.
To ensure the relevance and quality of the included literature, manual screening was
conducted, and inclusion criteria were established (Table  1) to enhance the scientific
rigor and efficiency of the selection process.
Manual screening involved two steps. First, irrelevant studies were excluded by
screening titles and abstracts. The research team screened and removed duplicates
across the four databases over a period of 3 weeks, retaining 183 articles. Second, full-
text reading was conducted to accurately identify studies aligned with the research
topic. After 2  weeks, 163 articles were finally retained (see Appendix A). The com -
plete screening process is illustrated in Fig.  2. To extract literature characteristics,
the research team established a structured coding framework after manual screening
(Manzo et al., 2025). Table 2  presents the specific coding scheme.
Table 1 Inclusion criteria
Type Inclusion criteria
Research scope criteria ① The study must focus on AIGC and fashion Industry, including but not
limited to AI-driven design tools
② Articles that only mention AI and fashion industry in the background
or in minor sections are excluded
Literature quality criteria ① Only original research articles and review papers are included; pre-
prints are excluded
② The full text must be accessible and retrievable from authoritative
databases
③ The article must contain complete metadata (abstract, authors,
keywords, references, etc.)
④ The article must be peer-reviewed; editorials, opinions, letters, and
notes are excluded

Page 5 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Qualitative content analysis and thematic synthesis
To identify the core advantages and potential risks of AIGC in the fashion industry
(RQ3), this study adopted a qualitative content analysis and thematic synthesis approach,
drawing on the staged coding logic of grounded theory and supported by NVivo 11 soft -
ware. First, Open Coding was employed to extract initial categories and concepts from
the text; subsequently, Axial Coding was performed to synthesize initial categories into
Fig. 2 PRISMA flowchart for including studies to review
Table 2 Lists of codes for the analysis of selected articles
Research
question
Category Code
RQ1 Metadata Title; Author information; Year of publication; Source
Research type Qualitative Research; Quantitative Research; Theoretical Research; Case-Based and
Experimental Research; Mixed Methods Research
RQ2 Research themes Intelligent Design & Customization; Trend Forecasting & Consumer Behavior; AI &
Fashion Education; Law & Ethics; Sustainable Fashion Design
RQ3 Core advantages Describes the advantages of AIGC in the fashion industry, including but not
limited to supporting design innovation, optimizing production processes, and
enhancing market responsiveness
Potential risks Describes the risks of AIGC in the fashion industry, including but not limited to
intellectual property disputes, the weakening of design originality, and data bias
issues

Page 6 of 36Lin et al. Fashion and Textiles           (2026) 13:32
main categories of core advantages and potential risks; finally, Selective Coding was
applied to construct an application logic framework for AIGC in the fashion industry.
The detailed process and results are presented in “Grounded Analysis for Advantages
and Risks (RQ3)” section and Appendix B (Tables 6, 7, 8, 9).
Performance analysis (RQ1)
Performance analysis, as an important method for revealing disciplinary development
trends, helps objectively present the field’s evolutionary trajectory (Chen et  al., 2024).
From a data-driven perspective, this study analyzes the publication year distribution,
research types, research methods, and countries of publication to uncover the develop -
ment landscape of this field (Jabari et al., 2024).
Year distribution, research type, and research method
First, the annual distribution of the included literature was analyzed, as shown in Appen-
dix C, Fig.  7A. The results show that related research began to increase significantly in
2022 and peaked in 2025. This explosive growth trend is closely tied to the evolution
of AIGC; the breakthrough of generative technologies represented by Diffusion Mod -
els around 2022 greatly lowered the barrier for image generation and design applica -
tions, thereby driving the rapid emergence of application-layer research. Concurrently,
research has gradually expanded from early algorithmic optimization to more diverse
themes such as law and ethics. Given that data collection for this study ended in Decem-
ber 2025, some studies may not have been included due to database indexing lags; there-
fore, the actual total publication volume for 2025 is expected to be higher than current
statistics, and it is reasonable to predict that research in this field will continue to main -
tain an upward trend in 2026.
Among the included studies, 141 were Original Articles and 22 were Review Arti -
cles. Further classification of the 141 original articles was performed based on research
type, referencing Chen et al. (2024), which categorized studies into five types: Quanti -
tative Research, Qualitative Research, Mixed Research, Case-Based and Experimental
Research, and Theoretical Research (see Table  3). As there is some degree of overlap
among different studies, this study adopts the definition of mixed research proposed by
Johnson and Onwuegbuzie (2004), whereby a study is classified as mixed research only
Table 3 Classification criteria
Research type Classification criteria
Quantitative research Analyzes the effects of AIGC, design efficiency, and user preferences through numerical
data and statistical methods to provide quantifiable evidence
Qualitative research Uses interviews, case studies, and similar qualitative approaches to explore perceptions of
AIGC technology and its influencing factors among designers, consumers, or experts
Case-based and
experimental
research
Employs case analysis or experimentation to validate the practical value of AIGC in opti-
mizing design processes, enhancing creativity, and enabling personalized customization
Theoretical research Focuses on the theoretical construction of AIGC in fashion design and explores its inte-
gration with traditional design thinking to offer innovative academic perspectives
Mixed research Combines quantitative and qualitative methods, integrating interviews with statistical
analysis to uncover the complex and multidimensional characteristics of AIGC-related
design research

Page 7 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

when quantitative and qualitative components are relatively balanced. The statistical
results of research types are detailed in Appendix C, Fig. 7B.
As shown in Appendix C, Fig.  7B, AIGC research in fashion industry is dominated by
Case-Based and Experimental Research and Quantitative Research, followed by Mixed
Research, Theoretical Research, and Qualitative Research. This characteristic corre -
sponds with the Thematic Analysis in “Thematic analysis (RQ2)” section, where Intel -
ligent Design & Customization is currently the largest research theme. Such studies
focus on the development and practical implementation of generative algorithms, and
their validation logic relies on empirical paradigms: on the one hand, quantitative data
are needed to establish the technical advantages of models in various performance indi -
cators; on the other hand, specific experimental cases (Case-Based) are used to dem -
onstrate the aesthetic value and practical potential of the effects (Cao et  al., 2024; Li
et al., 2025a, 2025b; Lu et al., 2025; Yan et al., 2024a). In contrast, theoretical research
is relatively scarce; however, with the rise of social science topics such as "Law & Eth -
ics" and "Fashion Education," the construction of theoretical frameworks is expected to
grow gradually in the future, thereby providing stronger theoretical support for practical
research.
Source and country
Academic journals serve as key platforms for advancing the frontiers of scholarly dis -
ciplines. This study involves 110 journals in total, with those publishing three or more
articles displayed in Appendix C, Fig. 7C.
In the study of the AIGC-empowered fashion industry, journals from various disci -
plines play distinct roles. Among them, environmental and sustainable development
journals such as Sustainability have published a significant amount of relevant research.
In the textile and clothing field, journals such as Fashion and Textiles, Textile Research
Journal, Clothing and Textiles Research Journal, and International Journal of Clothing
Science and Technology constitute important publishing venues for this theme. Mean -
while, engineering and computer science journals such as Applied Sciences, Applied
Mathematics and Nonlinear Sciences, and IEEE Access mainly focus on the algorithmic
methods and technical implementation of AIGC (Bao et al., 2023; Deng & Chen, 2025;
Huang, 2024); Multimedia Tools and Applications and IEEE Transactions on Circuits
and Systems for Video Technology focus on visual generation and multimodal modeling
issues (Gu et al., 2023). Finally, the International Journal of Human–Computer Interac -
tion primarily focuses on research related to interactive experience.
To further analyze the international research distribution of AIGC in the fashion
industry, the countries of publication were identified. In terms of overall distribution,
China, South Korea, and the United States have higher publication volumes. Meanwhile,
countries such as India, Italy, the United Kingdom, Malaysia, and Turkey also demon -
strate relatively active research participation. Notably, several smaller countries such as
Andorra have provided diverse perspectives in research themes and methods; although
their contributions are fewer in number, they are equally valuable in promoting global
knowledge exchange and technological innovation. Overall, the research presents an
international trend of multi-center distribution and broad participation.

Page 8 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Evolution of key AIGC technologies and characteristics of fashion applications
(RQ2)
The above growth trend indicates that the rapid expansion of AIGC in the fashion indus-
try is closely associated with technological progress. To clarify the mechanisms behind
this trend, this section examines how AIGC in fashion has evolved across different tech -
nological stages. It should be noted that while AIGC applications span every link of the
industrial chain, the iteration from discriminative analysis to generative creation is most
distinct within the fashion design sector; furthermore, intelligence at the design end
serves as a critical engine driving supply chain optimization and marketing innovation.
Therefore, this section takes design and content production as the primary observational
lens.
Based on a review of the included literature and combined with the evolutionary pat -
terns of AIGC in the fields of computer vision and natural language processing, this
study summarizes the technological evolution of AIGC in the fashion industry into three
stages: the Preliminary Stage, the Simulation Stage, and the Creative Stage.
Preliminary stage: data‑driven trend insight
In the fashion field, the early integration of AI mainly relied on Discriminative Mod -
els, such as Convolutional Neural Networks (CNNs) and Recurrent Neural Networks
(RNNs). Although such technologies do not directly belong to the generative paradigm,
their capability to parse unstructured data established the foundation for subsequent
AIGC to understand semantics. Therefore, this study defines it as an indispensable Pre -
liminary Stage in the evolutionary process of AIGC. At this stage, the relevant technolo -
gies primarily served as analytical observers rather than creators (Zhao et al., 2024).
Specifically, Convolutional Neural Networks (CNNs) effectively capture the silhouette
structure, texture details, and styling features of clothing through hierarchical feature
extraction mechanisms (Kim et al., 2024); while Recurrent Neural Networks (RNNs) and
their variants (e.g., LSTM) excel at modeling sequential data, used to analyze changes in
consumer preferences and sales trends (Swaminathan & Venkitasubramony, 2024). Such
predictions remained essentially analyses based on existing data; their outputs were
typically presented as numerical indicators, trend curves, or static reports, and did not
directly participate in brand strategy, content generation, or consumer interaction. The
technological path is illustrated in Fig.  3, which aims to highlight the technical mecha -
nisms of discriminative models in the Preliminary Stage, rather than to describe a spe -
cific network design.
Simulation stage: virtual try‑on and style transfer
The introduction of Generative Adversarial Networks (GANs) marked the first wave of
automated visual generation. Through adversarial training between the generator and
the discriminator, GANs enable the generator to gradually approximate the real data dis-
tribution, thereby synthesizing fashion images with structural consistency and stylistic
features, as shown in Fig.  4. Leveraging this mechanism, GANs have achieved break -
throughs in tasks such as Virtual Try-On (VTON) and style transfer (Gu et  al., 2023;
Zhou et  al., 2024). However, such generation remains essentially a reconstruction and

Page 9 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

transfer of existing visual data, rather than original design based on semantic intent.
Furthermore, the application of GANs in professional design faces an inherent con -
tradiction: despite high efficiency, they frequently encounter issues such as mode col -
lapse (Yan et al., 2024a). Although the generation results at this stage still rely heavily on
established structures and training distributions, their value is no longer limited to the
predictive data itself, but rather provides visual and comparable alternatives for market -
ing decisions.
Creative stage: high‑fidelity design and semantic co‑creation
In recent years, AIGC has shifted towards a generative paradigm based on Diffu -
sion Models. Compared to adversarial training, its iterative denoising mechanism
possesses superior stability (Chen & Ma, 2025), as shown in Fig.  5. Unlike the visual
simulation of the previous stage, this stage realizes Zero-shot Generation capabili -
ties based on natural language, enabling models to generate novel designs without
Fig. 3 Phase 1: Preliminary stage—data-driven trend insight
Fig. 4 Phase 2: Simulation stage—virtual try-on and style transfer

Page 10 of 36Lin et al. Fashion and Textiles           (2026) 13:32
retraining for specific styles, thereby enhancing the openness of creation and pro -
duction flexibility (Aghilar et al., 2025; Deng & Chen, 2025). In high-fidelity applica -
tion scenarios such as virtual try-on, diffusion models are gradually replacing GANs
as the mainstream technological path. IDM-VTON, proposed by Choi et al. (2025),
achieves high-fidelity virtual try-on in real-world (in-the-wild) scenarios by fusing
clothing semantic features into the cross-attention and self-attention layers of dif -
fusion models; it also demonstrates good generalization capabilities. From the per -
spective of broader fashion generation applications, diffusion models such as Stable
Diffusion have become an important technological foundation, while platforms such
as Midjourney have further promoted the adoption of this paradigm in design prac -
tice (Chen & Ma, 2025; Zhang & Liu, 2024).
Furthermore, research has begun to extend generative models into Fashion Agents
capable of continuous interaction and task coordination (Deng & Chen, 2025). Typi -
cally utilizing Large Language Models (LLMs) as the core decision-making unit,
these agents are responsible for context maintenance and multi-task coordination.
For example, the DressCode system proposed by He et al. (2024) utilizes LLMs as
design assistants to achieve 3D clothing synthesis and editing through natural lan -
guage interaction. Similarly FashionGPT also demonstrates the potential of using
LLMs for task planning (Gao et al., 2024; He et al., 2024).
Overall, this stage marks a shift of AIGC from “market prediction” to “market par -
ticipation. ” Generative systems integrated with LLMs are not only capable of pro -
cessing multimodal data, but can also identify consumers’ latent needs more deeply
and support personalized recommendations and brand co-creation through forms
such as chatbots (Ranjan & Upadhyay, 2025).
Fig. 5 Phase 3: Creative stage—high-fidelity design and semantic co-creation

Page 11 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Thematic analysis (RQ2)
Following the previous discussion of the technological evolution of AIGC in the fash -
ion industry, this Section further classifies the existing literature by theme to reveal the
core issues and distribution characteristics of current research. Based on the systematic
synthesis, existing studies are categorized into five groups (see Table  4 and Appendix C,
Fig. 7D); for publications covering multiple themes, classification is determined by their
primary research focus.
Intelligent design & customization
Under the theme of Intelligent Design & Customization, research mainly focuses on four
dimensions: algorithm optimization, semantic systems, visual perception, and consumer
co-creation.
At the level of generative algorithms, the research focus is shifting from image syn -
thesis to controllable design. Early Generative Adversarial Networks (GANs) mainly
addressed feature decoupling and compatibility issues; for instance, Zhou et al. (2024)
proposed the BC-GAN framework, which utilizes a compatibility discriminator to
improve outfit coordination, while CTS-GAN introduced by Yan et al. (2024b) achieved
feature separation of color and texture. To meet the rigorous requirements of profes -
sional design for details, studies have introduced Low-Rank Adaptation (LoRA) and
Table 4 Thematic classification criteria for selected articles
This classification does not include review-type studies
Research theme Classification criteria Number
of
articles
Intelligent Design & Customization Studies on AI applications in fashion design, including
intelligent design generation (e.g., sketch generation, style
innovation, data-driven design) and personalized customi-
zation (e.g., fashion recommendation, made-to-measure
tailoring, and virtual try-on). Related technologies involve
GANs, deep learning, computer vision, AI recommender
systems, and 3D modeling
75
Trend Forecasting & Consumer Behavior Category 1: Fashion Trend Forecasting. Studies on the
application of AI, machine learning, and related technolo-
gies in predicting fashion trends, product sales, and market
demand, covering trend analysis, historical data mining,
and quantitative forecasting
10
Category 2: Digital Marketing and Consumer Behavior.
Focuses on the role of AI in understanding consumer
behavior, digital marketing, and brand decision-making,
including sentiment analysis, social media interaction, per-
sonalized recommendation, and e-commerce experiences
39
AI & Fashion Education Explores the application of AI in fashion design education,
including its impact on student creativity, design skills, cur-
riculum reform, and digital pedagogy
6
Law & Ethics Investigates legal and ethical concerns in AI-driven fashion,
including data privacy, intellectual property, algorithm
transparency, and fairness, with emphasis on industry regu-
lation and consumer rights
5
Sustainable Fashion Design Explores the role of AI in promoting sustainability in
fashion through eco-friendly material selection, intelligent
manufacturing, supply chain optimization, and carbon
footprint control
6

Page 12 of 36Lin et al. Fashion and Textiles           (2026) 13:32
diffusion models to enhance generation stability (Chen & Ma, 2025; Gu et al., 2023). To
address the challenge of sketch-to-garment conversion, Lee et al. (2025) proposed Diffu-
seDesigner, which achieves highly controllable sketch generation. At the level of design
assistance, Li et  al. (2025a , 2025b) proposed a clothing color harmony evaluation and
recommendation model, providing support for color decision-making in fashion design.
Related research is gradually shifting from early-stage image generation toward control -
lable generation and decision support for professional tasks.
At the system application and semantic level, AIGC is evolving into a tool with com -
prehension capabilities. Various intelligent assisted design systems have also been devel-
oped, such as iDesigner (Zhang & Liu, 2024), StyleWe (Wu et al., 2024), and CoCoStyle
(Kim et al., 2024). Research also explores culture-specific generation; the CDGFD frame-
work combines Large Language Models (LLMs) with GANs, introducing the concept of
"Digital Cousins" to improve semantic and structural consistency issues in ethnic fash -
ion design (Deng & Chen, 2025).
Advancements in visual perception technology provide support for precise design and
recommendation. Zhang et al. (2024) proposed a hybrid ResNet–Transformer architec -
ture to optimize women’s shirt style recognition. In addition, Pan et al. (2024) improved
the accuracy and robustness of automatic classification for women’s trousers based on
an optimized Swin Transformer model. With the increasing demand for understand -
ing the spatial structure of clothing, Mrinali and Gupta (2025) introduced Cloth-net, a
hybrid architecture of Dense Vision Transformer and adversarial networks, enhancing
the classification accuracy of complex 2D-3D clothing and providing technical support
for more precise recommendation engines. Overall, improvements in visual recognition
and structural understanding are providing a stronger foundation for precise design sup-
port, product management, and personalized recommendation.
Finally, the research perspective is extending from "designer-led tools" to "Consumer-
Centric Co-creation". Lee and Kim (2024) point out that empowering consumers to
participate in customization through AI can alleviate their bias against AI products. In
terms of interaction implementation, AI-based chatbots have surpassed traditional cus -
tomer service functions and are evolving into co-creators; meanwhile, the generation
model based on editing cues developed by Song et  al. (2024) allows users to perform
local modifications on clothing through semantic instructions.
Trend forecasting and consumer behavior
Under the theme of Trend Forecasting & Consumer Behavior, based on the character -
istics of the literature, the relevant studies can mainly be divided into two categories:
Fashion Trend Forecasting and Digital Marketing and Consumer Behavior. The former
focuses on macro- and micro-level market demand forecasting, whereas the latter cent -
ers on consumer interaction and brand strategy.
Fashion trend forecasting
AIGC is reshaping fashion trend forecasting. Anitha and Neelakandan (2025) conducted
a systematic review of demand forecasting methods for fashion products, emphasiz -
ing the critical role of advanced algorithms in responding to market changes. In terms
of specific technical applications, Chan et  al. (2025) utilized an adaptive neuro-fuzzy

Page 13 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

inference system to analyze IoT data for real-time prediction of market trends. Beyond
market data, style evolution is also core to forecasting; Dong and Fu (2024) combined
big data with ant colony algorithms to visually analyze the evolution of traditional cloth -
ing design styles, providing a unique historical and cultural perspective for trend fore -
casting. Furthermore, Zhao et al. (2024) proposed the Neo-Fashion forecasting system,
which integrates computer vision and machine learning to identify trends in color, style,
and garment combinations, applying innovation diffusion theory to optimize fashion
forecasting and providing more precise analytical tools for the industry.
Digital marketing and consumer behavior
The influence of artificial intelligence on marketing and consumer behavior is increas -
ingly significant (Guerra-Tamez et  al., 2024). Alotaibi et  al. (2025) proposed a deep
learning framework based on hybrid Transformers and RNNs, significantly improving
the accuracy of fashion sentiment analysis on social media platforms and providing real-
time public opinion monitoring tools for brand management. Ranjan and Upadhyay
(2025) studied the role of AI chatbots in brand–consumer co-creation, finding that they
enhance personalized recommendations, customer experience, and brand loyalty. Ruiz-
Viñals et  al. (2024) examined the impact of AI on Gen Z consumers’ online purchase
intentions, identifying perceived quality, attitudes toward AI, and perceived usefulness
as key influencing factors. Liu et al. (2025) explored the application of digital technol -
ogies such as blockchain, artificial intelligence, and virtual reality in fashion market -
ing and analyzed their impact on marketing strategies, product design, and consumer
experience. Chien et al. (2025) proposed a 3D fashion design recommendation system
integrating generative AI and consumer electronics technologies, aimed at enhanc -
ing personalized recommendations and body-fit matching to improve online shopping
experiences.
AI & Fashion Education
Under the theme of AI & Fashion Education, research mainly focuses on the impact of
AIGC on fashion education content, teaching models, and student competency develop-
ment. Lim et al. (2023) conducted a theoretical study on the coexistence model of AIGC
as a resource for educational transformation, highlighting its potential in fashion educa -
tion. Jung and Suh (2024) argued that AI-based curricula can enhance students’ digital
literacy, entrepreneurial mindset, problem-solving, and communication skills. In addi -
tion, Kim (2024) examined the impact of AI collaboration on visual thinking and crea -
tivity in fashion design education. Research by Lee (2025) indicates that AI tools serve
not only as technical aids but also as cultural bridges, helping students more effectively
integrate multicultural elements within an interdisciplinary context, thereby enhancing
the inclusivity and innovative depth of design.
Law & Ethics
Under the theme of Law & Ethics, existing research mainly focuses on issues such as
privacy protection, intellectual property, algorithmic transparency, and responsibil -
ity attribution in the application of AIGC in the fashion industry. Manchiraju (2025)
pointed out that ensuring the responsible integration of AI requires enhanced privacy

Page 14 of 36Lin et al. Fashion and Textiles           (2026) 13:32
protection, transparency, and cybersecurity, as well as updated legal standards to safe -
guard consumer trust and support sustainable industry development. Rockett et  al.
(2025) explored the impact of the Fashion 4.0 and regulatory requirements on the indus-
try, arguing that AI helps the industry adapt to complex environments and promotes
innovation and sustainable development. Regarding intellectual property and legal regu -
lation, McEwan (2024) proposed the establishment of an AI rights registration system to
address issues related to intellectual property and copyright. Niyompatama and Lapa -
toura (2025) pointed out a significant lag in current laws regarding defining the bounda -
ries between human creation and AI generation, and emphasized the need to further
clarify the attribution of originality in human–AI collaborative works.
Sustainable Fashion Design
Under the theme of Sustainable Fashion Design, existing research mainly focuses on
how AIGC enhances the sustainability of the fashion industry through production opti -
mization, inventory management, and resource allocation. Studies show that AI can not
only improve production efficiency, reduce costs, and decrease textile waste, but also
optimize the allocation of natural and human resources, thereby promoting both envi -
ronmental and social sustainability (Sinha et al., 2024; Dong et al., 2025; Thomassey &
Zeng, 2018).
Grounded analysis for advantages and risks (RQ3)
Building on the previous thematic synthesis, this section further employs qualitative
coding analysis to explore how the advantages and risks of AIGC in the fashion industry
are co-constructed.
The core themes of Advantages identified include: Intelligent Design Support, Person -
alization and User Experience, Data-Driven Trend and Market Analysis, Smart Manu -
facturing and Supply Chain, Education and Knowledge Sharing, and Sustainable Fashion
and Green Design. The themes of potential Risks include: Ethical Challenges, Socio-Cul -
tural Risks, Privacy and Security Risks, Consumer Mistrust and Misguidance, and Tech -
nological Monopoly.
Based on these themes, a conceptual map integrating the advantages and risks of
AIGC in the fashion industry was constructed, as shown in Fig.  6. The identified main
categories were further organized into three levels: the Application Scenario Layer, the
Design Model Layer, and the Attribute Layer. Given that some themes show a certain
degree of association across different levels, this study assigned them to the level that
best reflects their operational mechanisms and analytical significance.
First, the Application Scenario Layer mainly refers to consumer-oriented contexts.
Therefore, Personalization & User Experience Enhancement, one of the identified core
advantages, is categorized into this layer, as its value realization relies heavily on con -
sumers’ acceptance, usage, and trust of AIGC fashion products. Meanwhile, Education
& Knowledge Sharing at this layer is more reflected in the long-term empowerment of
future design education. However, precisely because the Application Scenario Layer
directly faces consumers, the risk of Consumer Mistrust and Misguidance is particularly
prominent at this level (Wang et al., 2025), mainly manifesting as information overload
and inconsistencies between virtual presentation and real-world effects.

Page 15 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

In the Design Model Layer, the focus is on design generation and collaborative mecha-
nisms. Consequently, the identified advantage themes—Intelligent Design Support and
Sustainable Fashion & Green Design—are categorized into this layer. At the same time,
Ethical Challenges and Socio-Cultural Risks also mainly unfold here, manifesting as design
bias, designers’ over-reliance on technology, rigid thinking, and the erosion of subjectivity
(Surbakti, 2025).
Finally, the Attribute Layer refers to the data and system foundation upon which AIGC in
the fashion industry depends, rather than directly intervening in design applications or fac-
ing consumers. Based on this definition, Data-Driven Trend & Market Analysis and Intel-
ligent Production & Supply Chain Optimization are categorized into this layer. Among the
risk themes in this layer, the capture of massive amounts of data by intelligent technologies
is prone to causing Privacy & Security Risks; meanwhile, the concentration of key resources
also triggers concerns about Tech Monopoly, which is closely related to the high depend-
ence of large model training on computing power and data scale.
In summary, the application of AIGC in the fashion industry is a multi-dimensional
process, and its value realization possesses a dual nature. From the Attribute Layer to the
Application Scenario Layer, each level is accompanied by corresponding challenges: tech-
nology and data accumulation bring efficiency improvements but also trigger privacy and
monopoly concerns; intelligent generation optimizes design processes yet introduces ethi-
cal and bias issues; and personalized services enhance consumer experiences while simul-
taneously leading to a crisis of trust. Objectively recognizing this status quo of coexisting
advantages and risks is crucial for the rational application of AIGC in the industry.
Discussion (RQ4)
Based on the perspective of coexisting advantages and risks and the three layers con -
structed in “Grounded analysis for advantages and risks (RQ3)” section, this study fur -
ther discusses the future directions of AIGC in the fashion industry.
Fig. 6 A qualitative analytical framework of advantages and risks of AIGC in the fashion industry

Page 16 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Application scenario layer
Currently, Personalization & User Experience stands as a major advantage of AIGC, yet
its development is accompanied by risks such as Consumer Mistrust and Misguidance.
In practical application, personalized experiences often remain limited to surface-level
product recommendations, making it difficult to effectively capture consumers’ implicit
needs (Jang & Ha, 2023; Shirkhani et al., 2023). A key direction lies in repositioning the
role of AIGC, upgrading it from a simple recommendation tool to an intermediary sys -
tem that connects consumers’ implicit needs.
Subsequent work can proceed from two dimensions: “physical fidelity” and “cognitive
adaptation. ” At the level of physical fidelity, combining VR/AR to construct Digital Ava-
tars with dynamic feedback, and optimizing fabric physical properties, will become an
important direction for mitigating virtual try-on discrepancies and enhancing consumer
trust. This requires collaboration between academia and industry to drive the establish -
ment of universal Digital Asset Standards, ensuring that what consumers "see" is physi -
cally what they "get". Regarding cognitive adaptation, excessive information can reduce
decision quality and exacerbate consumer cognitive fatigue (Shirkhani et al., 2023; Wang
et al., 2025). Therefore, a more worthwhile direction is to achieve a more reasonable bal-
ance between personalization and cognitive controllability through dynamic filtering
and recommendation mechanisms.
Meanwhile, "Education & Knowledge Sharing" at this layer is more reflected in the
long-term empowerment of future design education. To avoid risks such as learn -
ing dependency and the weakening of originality potentially caused by AIGC, future
work may further focus on developing critical pedagogical frameworks. AIGC should
be redefined as a Heuristic Tool, aimed at enhancing rather than replacing students’
design thinking. When generative systems are widely used for fashion generation and
scheme expansion, learners’ design decisions may gradually shift from "problem-driven
exploration" to "result-oriented selection," thereby weakening the reflective understand -
ing of the fashion design process itself (Kim, 2024). Jang (2026) shows that although AI
improves efficiency, it may also weaken students’ creative autonomy and satisfaction
with outcomes. Therefore, the research focus should shift from “whether to use AI” to
“how it intervenes in different stages of design thinking."
Design model layer
In terms of Intelligent Design Support, AI models lack a precise understanding of design
logic and cultural semantics. Furthermore, existing models still exhibit deficiencies in
Professional Capabilities (Shi et  al., 2025). For instance, models often misinterpret a
Corset as a wide Belt based on surface pixels, lacking a deep understanding of fashion
history and structural logic (Deshmukh et al., 2024). When handling structural crafts -
manship, models can generate a visually perfectly fitting "seamless suit," but may omit
necessary darts transfer or closure structures (like plackets and buttonholes) required
for physical wearing, rendering the design unwearable from an engineering perspec -
tive. Moreover, when responding to precise instructions such as "narrow the neckline by
2 cm," current probability-based models still often struggle to respond consistently.
Therefore, the core of the future agenda lies not in simple design generation, but in
constructing more semantically accurate and more controllable design systems (Yan

Page 17 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

et  al., 2023). A more worthwhile direction is to develop vertical AIGC design frame -
works that transform domain knowledge—such as garment morphological standards,
craftsmanship logic, or brand archival records—into structured knowledge graphs or
other computable forms (Chen & Ma, 2025), thereby promoting structurally more rea -
sonable generation results.
Regarding Sustainable Fashion & Green Design, a key direction lies in integrating Life
Cycle Assessment (LCA) into the process, thereby assisting designers in making more
environmentally friendly material and process choices at the conceptual stage (Ramos
et al., 2023).
Meanwhile, the Design Model Layer is also where Ethical Challenges and Socio-Cul -
tural Risks are concentrated. Model outputs are often presented as reasonable solutions,
thereby weakening human critical reflection and questioning of key decisions. There -
fore, the research focus should further shift toward internal responsibility allocation
and decision traceability mechanisms within models (Amershi et  al., 2019), while also
attending to the cultural mapping relationship between training data and outputs, so as
to avoid inadvertently reinforcing stereotypes and weakening cultural diversity in gener -
ated results.
Attribute layer
At the attribute level, future optimization should mainly focus on model stability, the
integration of system constraints, and underlying data governance. Regarding Data-
Driven Trend & Market Analysis, subsequent work may further focus on enhancing
model stability under uncertain conditions to avoid misinterpreting short-term fluc -
tuations as long-term trends. In terms of Intelligent Production & Supply Chain Opti -
mization, incorporating constraints such as production flexibility, inventory risks, and
environmental costs into models will help support more robust operational modes (Gio-
vanni et al., 2025; Dong et al., 2025).
Meanwhile, in response to increasingly severe Privacy & Security Risks, a key direc -
tion lies in exploring the application of privacy-preserving computing technologies in
the fashion industry, thereby strengthening the foundation of trust at the technical level.
Addressing Tech Monopoly, subsequent work may further focus on decentralized data
governance models to avoid market polarization caused by data monopolies, thereby
fostering diversity and fair competition across the entire fashion ecosystem (Rockett
et al., 2025).
Fashion agent
Relying solely on the optimization of individual layers remains insufficient to address the
collaborative needs at the industry level. Therefore, a more worthwhile direction lies in
further integrating the capabilities of different layers into a Fashion Agent framework.
In the future, agents in the fashion industry are poised to transcend the functional limi -
tations of single layers, shifting from individual intelligence to Multi-Agent Collabora -
tion Systems by organically integrating consumer insights, design generation, and data
constraints.
A key issue lies in investigating how Agents establish Semantic Alignment across
different layers; for instance, automatically translating vague consumer emotional

Page 18 of 36Lin et al. Fashion and Textiles           (2026) 13:32
descriptions from the Application Layer—such as "breathable and with good drape"—
into precise industrial material parameters in the Attribute Layer, like "100% Tencel with
a weight below 120 g," and further mapping them into geometric meshes consistent with
gravity simulation in the Design Layer, thereby eliminating the semantic gap between
layers. In addition, virtual studios composed of a "Creative Director Agent," a "Pattern
Maker Agent," and a "Market Analyst Agent" can also be constructed. Research may fur-
ther explore Adversarial Debate and Negotiation mechanisms among agents to simulate
real-world industrial decision-making processes.
Conclusions
This study conducted a systematic review of 163 publications related to AIGC in the field
of the fashion industry and carried out the analysis around four core research questions.
First, regarding the overall research landscape (RQ1), research in this field has grown
rapidly since 2022. China, South Korea, and the United States are the primary contribut-
ing countries, presenting an international trend of multi-center distribution and broad
participation. Relevant findings are widely distributed across interdisciplinary journals.
Second, regarding technological evolution characteristics and major research themes
(RQ2), AIGC technology is undergoing a paradigm shift from Generative Adversarial
Networks (GANs) to Diffusion Models and Large Language Models (LLMs). Research
themes cover five major directions: Intelligent Design & Customization, Trend Fore -
casting & Consumer Behavior, AI & Fashion Education, Law & Ethics, and Sustainable
Fashion Design. Third, regarding advantages and risks (RQ3), this study constructed a
framework of " Application Scenario—Design Model—Attribute Layer" based on qualita-
tive analysis and multi-stage coding, elucidating the characteristic of "the coexistence
of efficiency enhancement and risks" in AIGC in the fashion industry. Finally, concern -
ing the future research agenda (RQ4), this study argues that the further development of
AIGC in the fashion industry should not rely solely on isolated technological optimiza -
tion, but should advance toward cross-layer collaboration and system integration.
This study acknowledges the following limitations and directions for improvement:
First, regarding literature retrieval, limited by database indexing boundaries and the
retrieval framework, some non-English research findings and non-indexed publica -
tions may have been excluded. Moreover, the relatively limited sample size may affect
the generalizability of the findings. Future research is encouraged to expand the scope
of multilingual retrieval. Second, qualitative coding analysis and thematic classification
are susceptible to researchers’ cognitive influence (Jabari et al., 2024), which may lead
to subjective judgment bias (Mohiuddin Babu et al., 2024). Future studies may employ
quantitative semantic analysis techniques (Wang et al., 2016) to develop automated clas-
sification models.
Appendix
Appendix A
See Table 5.

Page 19 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Table 5 List of selected articles for Systematic Literature Review
Rank Title Journal Country Publishing year
1 The ethical thread: AI’s role in the
tapestry of fashion
AI & Society America 2025
2 Demand Forecasting New Fashion
Products: A Review Paper
Journal of Forecasting India 2025
3 Modelling intended product
demand in fashion retail using IoT
and AI
International Journal of
Business Information
Systems
Australia 2025
4 Cloth-net: improved hybrid
adversarial network with dense
vision transformer for 2D-3D image
classification for accurate cloth
recommendation engine
International Journal of
Clothing Science and
Technology
India 2025
5 Understanding the Differences in
an AI-Based Creativity Support Tool
Between Creativity Types in Fashion
Design
International Journal of
Human–Computer Interac-
tion
South Korea 2025
6 Value co-creation by interactive AI
in fashion E-commerce
Cogent Business and
Management
India 2025
7 CDGFD: Cross-Domain Generaliza-
tion in Ethnic Fashion Design Using
LLMs and GANs: A Symbolic and
Geometric Approach
IEEE Access China 2025
8 Diffusedesigner: sketch-based con-
trollable clothing image generation
Fashion and Textiles South Korea 2025
9 Digital Technologies in the Sustain-
able Design and Development of
Textiles and Clothing-A Literature
Review
Sustainability Croatia 2025
10 Global initiatives for industry 4.0
implementation and progress
within the textileand apparel
manufacturing sector: a compre-
hensive review
International Journal of
Computer Integrated
Manufacturing
Malaysia 2025
11 Advanced Planning Systems in
Production Planning Control: An
Ethical and Sustainable Perspective
in Fashion Sec
Applied Sciences Italy 2025
12 From the Shallows to the Shelves
and Back: A Review, Synthesis, and
Research Agenda for Socially Sus-
tainable, AI-Driven Digital Fashion
Supply Chains
Business Ethics, the Envi-
ronment & Responsibility
Germany 2025
13 From Industry 4.0 to Industry 6.0:
Tracing the Evolution of Industrial
Paradigms Through the Lens of
Management Fashion Theory
Systems Norway 2025
14 It is giving inspiration: A survey
paper on generative AI in fashion
Fashion, Style & Popular
Culture
Portugal 2025
15 AI-driven computational creativity
in fashion design: a review
Textile Research Journal China 2025
16 Generative AI in fashion design
creation: a copyright analysis of
AI-assisted designs
Journal of Intellectual
Property Law & Practice
England 2025
17 Imperatives of using artificial intel-
ligence in modern clothing design:
Systematic review
Fashion, Style & Popular
Culture
Ukraine 2025
18 Qualitative-empirical insights into
generative AI for textile design in
the fashion design process
International Journal of
Design Creativity and
Innovation
China 2025

Page 20 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Table 5 (continued)
Rank Title Journal Country Publishing year
19 Technology as cultural translator:
artificial intelligence adaptation
and reconstruction in Global South
fashion design
AI & Society China 2025
20 "Make an Effort and Show Me the
Love!" Understanding Consumer
Aversion to AI Fashion Design
Through the Lens of Schema
Theory
Clothing and Textiles
Research Journal
America 2025
21 A Generative Artificial Intelligence
(GenAI) System for Fashion Design:
A Case Study
IEEE Transactions on Engi-
neering Management
China 2025
22 AI vs. human design in fashion:
critical role of product innovative-
ness in shaping consumer attitudes
Journal of Fashion Market-
ing and Management
America, New Zea-
land, South Korea
2025
23 Unveiling the Barriers and Drivers
of Virtual Fashion Adoption: Net-
nographic Insights from Instagram
Discourse
Clothing and Textiles
Research Journal
South Korea,
America
2025
24 Design characteristics, preferences,
and satisfaction toward virtual
fashion using augmented reality
International Journal of
Fashion Design, Technol-
ogy and Education
South Korea,
America
2025
25 OrnAsia: A dataset of asian orna-
ments for image classification and
cultural identification
Data in Brief Bangladesh 2025
26 From Algorithm to Reality: Explor-
ing Chinese Consumers’ Accept-
ance of Physicalized AI-Generated
Clothing in the Context of Sustain-
able Fashion
Sustainability China 2025
27 Exploring the generative AI poten-
tial in the fashion design process:
an experimental experience on
the collaboration between fashion
design practitioners and generative
AI tools
European Journal of
Cultural Management and
Policy
Italy 2025
28 Mind the gap: virtual fashion shows
and generational disparities
International Journal of
Fashion Design, Technol-
ogy and Education
Lebanon 2025
29 Leveraging Artificial Intelligence for
ESG Reporting: A Case Study in the
European Fashion Industry
Business Strategy and the
Environment
Italy 2025
30 A Study of the Effect of AI-Gen-
erated Image Recommendation
Services on Purchasing Intentions
for Online Shopping
Journal of Electronic Com-
merce in Organizations
France 2025
31 Effectiveness of AI Technologies
in Reducing Textile Waste in the
Fashion Industry
Textile Research Journal South Korea 2025
32 Real-Time Artificial Intelligence (AI)
and Augmented Reality (AR)-Driven
Virtual Saree Dressing: Mirroring
Reality in Fashion Technology
Journal of Advances in
Information Technology
England, India,
China
2025
33 A Systematic Review of Reimagin-
ing Fashion and Textiles Sustain-
ability with AI: A Circular Economy
Approach
Applied Sciences Australia 2025
34 Fashion AI across the value chain:
A comprehensive literature review
and future agenda
Journal of Global Scholars
of Marketing Science
South Korea, China 2025

Page 21 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Table 5 (continued)
Rank Title Journal Country Publishing year
35 Empowering students through
generative AI and cultural diversity
in interdisciplinary fashion design
education
Research Journal of Textile
and Apparel
America 2025
36 Made-In: An immersive human-
in-the-loop analytics platform for
enhancing creative processes in
fashion
Computer Vision and
Image Understanding
Italy 2025
37 Effective Fashion Design Collection
Implementation with Generative AI:
ChatGPT and Dall-E
Clothing and Textiles
Research Journal
South Korea 2025
38 Scouting emerging AI applications
in fashion heritage and archival
practices
European Journal of
Cultural Management and
Policy
Italy 2025
39 Digital Fashion and Sustainability:
Impact on Generation Z Consumer
Behavior in Croatia
Revista Mediterránea de
Comunicación/Mediterra-
nean Journal of Commu-
nication
Croatia 2025
40 Consumers’ perceived benefits, bar-
riers and opportunities on technol-
ogy driven fashion marketing
Qualitative Market
Research
Turkiye 2025
41 Emotional and Functional Values
of Generative AI in Fashion: Effects
on User Satisfaction and Continued
Use
International Journal of
Human–Computer Interac-
tion
South Korea, China 2025
42 Bidirectional feature modulation
fusion for fashion design using
latent diffusion models
The Visual Computer China 2025
43 How Does Human-AI Co-Creation
Design Help Luxury Brands Win
Consumers’ Favor?
Journal of Consumer
Behaviour
China 2025
44 The development of an aesthetic
language for fashion: Improving
efficacy for emerging generative AI
contexts
Fashion, Style & Popular
Culture
America 2025
45 From couture to code: Reimagining
fabric development through AI-
enhanced material narratives
Fashion, Style & Popular
Culture
England 2025
46 Innovative solutions to fashion’s
biggest problems—the impact of
artificial intelligence on solutions
for Sustainable Development
Goals 9 and 12. A case study from
London College of Fashion
International Journal of
Educational Management
England 2025
47 Establishing colour harmony evalu-
ation and recommendation model
for clothing colour matching based
on machine learning and deep
learning
Fashion and Textiles China 2025
48 CRGAN: A Context-Aware Clothing
Design and Recommendation Sys-
tem for Young Sri Lankan Females
Using Generative Adversarial
Networks
IEEE Access Sri Lanka, China 2025
49 Mapping the Research Agenda
for Sustainable Fashion Design:
Constructing Knowledge Maps
Through Bibliometric Analysis and
LDA Machine Learning
SAGE Open China 2025

Page 22 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Table 5 (continued)
Rank Title Journal Country Publishing year
50 Fabric defect detection: a hybrid
CNN-LSTM approach using TGANet
for improved classification and
traceability
Industria Textila India 2025
51 The application and optimization of
style transfer neural network based
on deep learning in fashion design
Systems and Soft Comput-
ing
Malaysia, China 2025
52 Gen Z and AI-Generated Fash-
ion Ads: A Qualitative Study to
Understanding Female Consumer
Perceptions and Reactions
Journal of Internet Com-
merce
America 2025
53 Generative AI in Fashion: Overview ACM Transactions on
Intelligent Systems and
Technology
China 2025
54 Analyzing the adoption of AIGC
tools in fashion design: An S-O-R
framework integrating task-tech-
nology fit
PLOS ONE China, Malaysia 2025
55 Mapping the digital transformation
in the fashion industry: the past,
present and future
Journal of Fashion Market-
ing and Management
America 2025
56 FS-control: Artistic fashion design
with discriminated and conditional
diffusion model
Computers & Graphics China 2025
57 Autoregressive multimodal
transformer for zero-shot sales
forecasting of fashion products
with exogenous data
Applied Intelligence South Korea 2025
58 Garment pattern generation
method based on Diffusion Model
and 3D reconstruction technology
Textile Research Journal China 2025
59 Collaborative garment design
through group chatting with gen-
erative industrial large models
Advanced Engineering
Informatics
China 2025
60 An End-to-End Deep Learning
System for Automated Fashion Tag-
ging: Segmentation, Classification,
and Hierarchical Labeling
IEEE Access Turkiye 2025
61 Reimagining luxury fashion
through AI-driven design
Asia–Pacific Journal of
Marketing and Logistics
South Korea,
America
2025
62 Plastic to apparel: an analysis of sus-
tainable purchasing intention using
a machine learning ensemble
Humanities and Social Sci-
ences Communications
Philippines 2025
63 Improving Fashion Sentiment
Detection on X through Hybrid
Transformers and RNNs
CMC: Computers, Materials
& Continua
Saudi Arabia 2025
64 Texture-preserving multimodal
fashion image editing with diffu-
sion models
Knowledge-Based Systems China 2025
65 Example-based approach for auto-
matic garment pattern generation
Textile Research Journal China 2025
66 Automated fashion style genera-
tion model based on image recog-
nition techniques
Journal of Computational
Methods in Sciences and
Engineering
China 2025
67 Fashion Customization: Image Gen-
eration Based on Editing Clue
IEEE Transactions on Cir-
cuits and Systems for Video
Technology
China 2024
68 BC-GAN: A Generative Adversarial
Network for Synthesizing a Batch of
Collocated Clothing
IEEE Transactions on Cir-
cuits and Systems for Video
Technology
China 2024

Page 23 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Table 5 (continued)
Rank Title Journal Country Publishing year
69 Towards enhanced creativity in
fashion: integrating generative
models with hybrid intelligence
Frontiers in Artificial Intel-
ligence
Russia, Andorra,
Italy
2024
70 Collocated Clothing Synthesis with
GANs Aided by Textual Information:
A Multi-Modal Framework
ACM Transactions on
Multimedia Computing,
Communications, and
Applications
China 2024
71 Learning to Disentangle the Colors,
Textures, and Shapes of Fashion
Items: A Unified Framework
IEEE Transactions on
Multimedia
China 2024
72 The Influence of Artificial Intel-
ligence on Generation Z’s Online
Fashion Purchase Intention
Journal of Theoretical and
Applied Electronic Com-
merce Research
Spain 2024
73 Optimization of automatic classifi-
cation for women’s pants based on
the swin transformer model
Fashion and Textiles China 2024
74 StyleWe: Towards Style Fusion in
Generative Fashion Design with
Efficient Federated AI
Proceedings of the ACM
on Human–Computer
Interaction
China 2024
75 Development of Automatic Balanc-
ing Application for Fashion Com-
pany Using Artificial Intelligence
Tekstilec Saudi Arabia,
Tunisia
2024
76 Artificial Intelligence in the Fashion
and Apparel Industry
Tekstilec India 2024
77 HAIGEN: Towards Human-AI Col-
laboration for Facilitating Creativity
and Style Generation in Fashion
Design
Proceedings of the ACM
on Interactive, Mobile,
Wearable and Ubiquitous
Technologies
China 2024
78 CoCoStyle: Mixed initiative co-
creative system to support creative
process of fashion design
SoftwareX South Korea 2024
79 Enhancing Soft Skills through Gen-
erative AI in Sustainable Fashion
Textile Design Education
Sustainability South Korea 2024
80 Role of artificial intelligence and
augmented reality in fashion indus-
try from consumer perspective:
Sustainability through waste and
return mitigation
Engineering Applications
of Artificial Intelligence
Turkey 2024
81 Creating an AI fashioner through
deep learning and computer vision
Evolving Systems Turkey 2024
82 The application of hierarchical per-
ception technology based on deep
learning in 3D fashion design
Heliyon China 2024
83 Clothing image attribute editing
based on generative adversarial
network, with reference to an
upper garment
International Journal of
Clothing Science and
Technology
China 2024
84 Unlocking the Potential of Artificial
Intelligence in Fashion Design and
E-Commerce Applications: The
Case of Midjourney
Journal of Theoretical and
Applied Electronic Com-
merce Research
America 2024
85 Human vs. AI: The battle for
authenticity in fashion design and
consumer response
Journal of Retailing and
Consumer Services
America 2024
86 iDesigner: making intelligent
fashion designs
Multimedia Tools and
Applications
China 2024

Page 24 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Table 5 (continued)
Rank Title Journal Country Publishing year
87 A Novel Approach for Prediction
of Consumer Buying Behaviour
of Luxury Fashion Goods Using
Machine Learning Algorithms
International Journal of
Intelligent Systems and
Applications in Engineering
India 2024
88 The Effects of Artificial Intelligence
on the Fashion Industry—Oppor-
tunities and Challenges for Sustain-
able Transformation
Sustainable Development Poland 2024
89 Development of Women’s Shirt
Style Recognition Model (WSSRM)
based on a ResNet and Transformer
integrated method
Textile Research Journal China 2024
90 Explore the Fashion Industry’s
Behavioral Intention to Use Artificial
Intelligence Generated Content
Tools Based on the UTAUT Model
International Journal of
Human–Computer Interac-
tion
China 2024
91 Digital transformation in the
fashion industry: new horizons for
marketing and fashion design
Asian Journal of Technol-
ogy Innovation
China, Malaysia 2024
92 AI enabled business decisions that
enhance sustainability impact of an
apparel and fashion supply chain
Technology Analysis and
Strategic Management
India 2024
93 Human-Centric GenAI Garment
Designer: 3D Fashion Design Rec-
ommendations
IEEE Consumer Electronics
Magazine
China, America,
South Africa
2024
94 Research on the Application
of Deep Learning Algorithm of
Artificial Intelligence to 3D Clothing
Design in Computerized Virtual
Reality Environment
Applied Mathematics and
Nonlinear Sciences
China 2024
95 An intelligent generative method
of fashion design combining
attribute knowledge and Stable
Diffusion Model
Textile Research Journal China 2024
96 MFR-CNN: A modified faster R-CNN
approach based on bounding box
and reliable score for cloth image
retrieval
Multimedia Tools and
Applications
India 2024
97 AI in fashion: a literature review Electronic Commerce
Research
Greece 2024
98 Artificial Intelligence Enabled
Apparel Design Research
Applied Mathematics and
Nonlinear Sciences
China 2024
99 Artificial Intelligence-Based Conver-
sational Agents Used for Sustain-
able Fashion: Systematic Literature
Review
International Journal of
Human–Computer Interac-
tion
England 2024
100 Decoding Gen Z: AI’s influence
on brand trust and purchasing
behavior
Frontiers in Artificial Intel-
ligence
Mexico 2024
101 Cross-Cultural Applications of Big
Data and Artificial Intelligence in
Fashion Design
Computer-Aided Design
and Applications
China 2024
102 An application of generative AI for
knitted textile design in fashion
The Design Journal China 2024
103 Artificial Intelligence Technology
Helps Spread Costume Design and
Arts and Crafts Culture
Applied Mathematics and
Nonlinear Sciences
China 2024

Page 25 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Table 5 (continued)
Rank Title Journal Country Publishing year
104 Visual Analysis of the Evolution of
Traditional Chinese Ethnic Clothing
Design Styles Based on Big Data
and Artificial Intelligence
Applied Mathematics and
Nonlinear Sciences
China 2024
105 Artificial intelligence-powered
digital solutions in the fashion
industry: a mixed-methods study
on AI-based customer services
International Journal of
Fashion Design, Technol-
ogy and Education
America 2024
106 The evolution of Chinese traditional
ethnic clothing design style based
on interactive dichroism algorithm
Applied Mathematics and
Nonlinear Sciences
China 2024
107 Deep learning techniques in mod-
ern women’s smart clothing design
Applied Mathematics and
Nonlinear Sciences
China 2024
108 Demand forecasting for fashion
products: A systematic review
International Journal of
Forecasting
India 2024
109 The role of artificial intelligence in
shaping the future of Agile fashion
industry
Production Planning &
Control
England, Australia,
Bangladesh
2024
110 Neo-Fashion: A Data-Driven Fash-
ion Trend Forecasting System Using
Catwalk Analysis
Clothing and Textiles
Research Journal
America 2024
111 Generative Artificial Intelligence in
Collaborative Ideation: Educational
Insight From Fashion Students
IEEE Access South Korea 2024
112 DiffFashion: Reference-Based Fash-
ion Design With Structure-Aware
Transfer by Diffusion Models
IEEE Transactions on
Multimedia
China 2024
113 Mixing and Matching Elements
for Intelligent Fashion Design: A
Generative Adversarial Network
With Structure and Texture Disen-
tanglement
IEEE Transactions on Con-
sumer Electronics
China 2024
114 Multimodal High-Order Relation-
ship Inference Network for Fashion
Compatibility Modeling in Internet
of Multimedia Things
IEEE Internet of Things
Journal
China 2024
115 Learning to Synthesize Compat-
ible Fashion Items Using Semantic
Alignment and Collocation Clas-
sification: An Outfit Generation
Framework
IEEE Transactions on Neural
Networks and Learning
Systems
China, Singapore 2024
116 Enhancing Soft Skills through Gen-
erative AI in Sustainable Fashion
Textile Design Education
Sustainability South Korea 2024
117 AI Technology Integrated Educa-
tion Model for Empowering
Fashion Design Ideation
Sustainability South Korea 2024
118 The allure of rarity: investigating
the impact of consumers’ perceived
scarcity in AI-designed clothing on
purchase intentions
International Journal of
Fashion Design, Technol-
ogy and Education
America 2024
119 The Effects of Artificial Intelligence
on the Fashion Industry—Oppor-
tunities and Challenges for Sustain-
able Transformation
Climate Change: Towards a
Sustainable Future
Poland 2024
120 Texture Brush for Fashion Inspira-
tion Transfer: A Generative Adver-
sarial Network With Heatmap-
Guided Semantic Disentanglement
IEEE Transactions on Cir-
cuits and Systems for Video
Technology
America 2023

Page 26 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Table 5 (continued)
Rank Title Journal Country Publishing year
121 Fashion 4.0 and emerging design-
ers: leveraging data and AI to
drive creativity, innovation and
compliance in global supply chain
regulation
Journal of Intellectual
Property Law & Practice
UK, Japan, Japan 2023
122 Developing a Generalized Regres-
sion Forecasting Network for the
Prediction of Human Body Dimen-
sions
Applied Sciences Switzerland 2023
123 Artificial intelligence and sustain-
ability in the fashion industry: a
review from 2010 to 2022
SN Applied Sciences Ecuador, Venezuela,
America
2023
124 Developing an AI-based automated
fashion design system: reflect-
ing the work process of fashion
designers
Fashion and Textiles South Korea 2023
125 Conceptual framework of hybrid
style in fashion image datasets for
machine learning
Fashion and Textiles South Korea 2023
126 Automatic generation of paramet-
ric patterns from grading patterns
using artificial intelligence
International Journal of
Clothing Science and
Technology
South Korea 2023
127 Product Design Enhancement for
Fashion Retailing
Service Science America, China 2023
128 Study of AI-Driven Fashion Recom-
mender Systems
SN Computer Science Sweden, Malaysia 2023
129 Dress-up: deep neural framework
for image-based human appear-
ance transfer
Multimedia Tools and
Applications
Tunisia, Saudi Ara-
bia, South Africa
2023
130 A Survey of Artificial Intelligence in
Fashion
IEEE Signal Processing
Magazine
China 2023
131 Toward Intelligent Fashion Design:
A Texture and Shape Disentangled
Generative Adversarial Network
ACM Transactions on
Multimedia Computing,
Communications, and
Applications
China 2023
132 Application of virtual reality
technology based on artificial intel-
ligence in fashion design style
International Journal of
System Assurance Engi-
neering and Management
South Korea, China 2023
133 AI-driven innovation in ethnic
clothing design: an intersection
of machine learning and cultural
heritage
Electronic Research Archive China 2023
134 A New Perspective on the Textile
and Apparel Industry in the Digital
Transformation Era
Textiles Finland, Austria,
Japan
2022
135 How complex systems get
engaged in fashion design creation:
Using artificial intelligence
Thinking Skills and Creativ-
ity
South Korea 2022
136 Color Trend Analysis using Machine
Learning with Fashion Collection
Images
Clothing and Textiles
Research Journal
South Korea 2022
137 A Semi-Supervised Learning
Approach for Automatic Detection
and Fashion Product Category Pre-
diction with Small Training Dataset
Using FC-YOLOv4
Applied Sciences Thailand 2022
138 Perception of Innovative Ameri-
cage of AI in Optimizing Customer
Purchasing Experience within the
Sustainable Fashion Industry
Sustainability Serbia, Switzerland,
India
2022

Page 27 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Table 5 (continued)
Rank Title Journal Country Publishing year
139 Would Your Clothes Look Good on
Me? Towards Transferring Clothing
Styles with Adaptive Instance
Normalization
Sensors Italy 2022
140 Deep Learning for Demand Fore-
casting in the Fashion and Apparel
Retail Industry
Forecasting Sweden, China 2022
141 Investigating the impact of
AI-powered technologies on
Instagrammers’ purchase decisions
in digitalization era–A study of the
fashion and apparel industry
Technological Forecasting
and Social Change
Malaysia, England,
Bangladesh, France
2022
142 Digital design of regional character-
istic apparel pattern driven by GAN
Industria Textila China 2022
143 Outdoor Clothing Design for Traf-
fic Safety Based on Big Data and
Artificial Intelligence
Journal of Advanced Trans-
portation
China 2022
144 An Adaptive Recommendation
Algorithm of Intelligent Clothing
Design Elements Based on Large
Database
Mobile Information
Systems
China 2022
145 Development of a hat style rec-
ognition system based on image
processing and machine learning
Industria Textila China 2022
146 A novel approach of boundary
preservative apparel detection and
classification of fashion images
using deep learning
Mathematical Methods in
the Applied Sciences
Pakistan, Norway 2022
147 TileGAN: category-oriented
attention-based high-quality tiled
clothes generation from dressed
person
Neural Computing and
Applications
China 2020
148 Fashion analysis and understanding
with artificial intelligence
Information Processing &
Management
China 2020
149 Development of fashion product
retrieval and recommendations
model based on deep learning
Electronics South Korea 2020
150 A Bibliometric Survey of Fashion
Analysis using Artificial Intelligence
Library Philosophy and
Practice
India 2020
151 Readily design and try-on garments
by manipulating segmentation
images
Electronics South Korea 2020
152 Using the convolution neural net-
work attempts to match Japanese
women’s Kimono and obi
International Journal of
Advanced Computer Sci-
ence and Applications
Japan 2020
153 Sportive fashion trend reports: A
hybrid style analysis based on deep
learning techniques
Sustainability South Korea 2021
154 Artificial intelligence in the fashion
industry: consumer responses to
generative adversarial network
(GAN) technology
International Journal of
Retail & Distribution Man-
agement
South Korea,
America
2021
155 Data generating garments using
low cost sensors
AATCC Journal of Research China 2021
156 Developing a framework of artificial
intelligence for fashion forecasting
and validating with a case study
International Journal of
Enterprise Network Man-
agement
India 2021
157 ClothGAN: generation of fashion-
able Dunhuang clothes using
generative adversarial networks
Connection Science China 2021

Page 28 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Table 5 (continued)
Rank Title Journal Country Publishing year
158 E-commerce sites with outfit
composition using deep learning
method
International Journal of
Innovative Technology and
Exploring Engineering
India 2019
159 Toward AI fashion design: An
Attribute-GAN model for clothing
match
Neurocomputing China, Canada 2019
160 Fashion product classification
through deep learning and com-
puter vision
Applied Sciences Italy 2019
161 Product innovation design based
on deep learning and Kansei
engineering
Applied Sciences China, America 2018
162 Defining the main features of
clothing to apply deep learning in
apparel design
Vlákna a Textil Ukraine 2018
163 Intelligent fashion styling using
genetic search and neural clas-
sification
International Journal of
Clothing Science and
Technology
Turkey 2015

Page 29 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Appendix B
See Tables 6, 7, 8, and 9.
Table 6 Open coding of advantages
Preliminary category Initial concept
Automated design generation AIGC can automatically generate design solutions, reducing
repetitive tasks and improving design efficiency
Creative assistance and inspiration expansion Provides diverse visual references, expands the creative bounda-
ries of designers, and enhances personalized expression
Intelligent optimization and market fit Optimizes design proposals based on trend analysis to increase
market acceptance
Personalized fashion customization Generates clothing designs tailored to individual styles using user
preferences and body data
Virtual try-on and material simulation Offers virtual try-on and fabric simulation through 3D modeling,
enhancing the shopping experience
Real-time trend forecasting Analyzes social media and sales data to forecast trends and sup-
port brand decision-making
Smart material recommendation Recommends eco-friendly and sustainable materials through big
data analytics, promoting green fashion
Production process optimization Enhances production efficiency and reduces inventory through AI
forecasting and automation tools
Efficient collaboration and remote co-design Enables intelligent collaboration among designers, suppliers, and
manufacturers, accelerating product realization
Intelligent learning and iterative design AIGC learns from user feedback and market data to iteratively
refine design solutions
Empowerment in fashion education Supports intelligent teaching and personalized learning to train
future fashion designers
Sustainable design optimization Simulates environmental impacts of materials and designs to
enhance sustainable fashion strategies
Circular fashion and recycling innovation AIGC facilitates recyclable fashion design and redesign of used
garments, enhancing fashion sustainability
Table 7 Open coding of potential risks
Original category Initial concept
Intellectual property risk Risks to design originality, copyright infringement, intellectual property theft
Privacy protection Leakage of user data privacy, misuse of personal information
Design ethics Ethical issues in the design process, unethical design practices
Technological dependence Overreliance on AI-generated designs, lack of human creative thinking
Technological monopoly AI design technologies controlled by a few companies, limiting innovation and fair
competition
Bias and discrimination Gender, racial, and cultural biases in AI algorithms leading to unfair design out-
comes
Creativity risk Lack of innovation and homogeneity in AI-generated designs
Virtual misrepresentation Errors in virtual try-on and inaccurate visualizations mislead consumers
Customer trust Lack of consumer trust in AI-generated designs, trust crisis
Information overload Design recommendation systems cause information overload, making it difficult for
consumers to choose the most suitable design
Algorithmic bias Algorithmic bias in the AI design process results in recommendations skewed
toward certain styles or cultural backgrounds
Social responsibility issues Neglect of social responsibility, environmental sustainability, and cultural adapt-
ability in AI design

Page 30 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Table 8 Axial coding of core advantages
Major category Original category Relational meaning
Intelligent design support Automated design generation Enhances creative efficiency and
accuracy through AI-generated
design solutions
Creative assistance and inspiration Provides design inspiration, expand-
ing the creative boundaries of
designers
Intelligent optimization and market
fit
Optimizes design outcomes based
on data analysis to better meet
market demands
Personalization and user experi-
ence
Personalized fashion customization Offers highly personalized fashion
designs tailored to user preferences
Virtual try-on and material simula-
tion
Enhances purchasing decisions via
immersive virtual fitting and material
simulation
Data-driven trend and market
analysis
Real-time trend forecasting Enables accurate trend predictions
through AI and big data analysis
Smart material recommendation Recommends optimal materials
based on product characteristics and
market demand
Smart manufacturing and supply
chain
Production process optimization Assists in production management
to increase efficiency and reduce
resource waste
Efficient collaboration and remote
co-design
Enables intelligent, cross-regional
collaboration, improving flexibility in
production
Education and knowledge sharing Intelligent learning and iterative
design
Enhances design learning and
iteration through AI-driven feedback
loops
Empowerment in fashion educa-
tion
Optimizes teaching methods and
knowledge dissemination via AI
technologies
Sustainable fashion and green
design
Sustainable design optimization Evaluates environmental impacts
and supports eco-friendly material
selection
Circular fashion and recycling
innovation
Supports reuse and recycling of dis-
carded materials, enhancing circular
fashion practices

Page 31 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Appendix C
See Fig. 7 .
Table 9 Axial coding of potential risks
Major category Original category Relational meaning
Ethical challenges Design ethics Ethical dilemmas in the design process,
including moral decision-making and uneth-
ical design behavior
Technological dependence Overreliance on AIGC tools may reduce
designers’ independence and creative
diversity
Creative risk Issues of originality in AI-generated design,
such as insufficient creativity or deviation
from design intent
Socio-cultural risks Bias and discrimination Gender, racial, or cultural bias embedded
in AI algorithms may lead to unfair design
outcomes
Social responsibility AI-generated designs may neglect social
responsibility, resulting in negative impacts
like over-commercialization or insensitivity
to social contexts
Privacy and security risks Privacy protection Risks related to the collection, storage, and
use of personal data in the AI-driven design
process
Intellectual property risk Ambiguities in copyright ownership of AI-
generated content, potentially infringing on
creators’ intellectual property rights
Consumer mistrust and misguidance Virtual misrepresentation AI-generated visuals (e.g., virtual try-ons)
may mislead consumers by failing to accu-
rately reflect real-world outcomes
Algorithmic bias Biased algorithms may favor certain groups
or cultures, reducing fairness and introduc-
ing flaws into the design process
Customer trust Consumers may lack trust in AI-generated
designs due to perceptions of impersonality
or artificiality
Information overload Excessive AI-generated content may over-
whelm consumers, complicating decision-
making processes
Technological monopoly Technological monopoly AIGC dominance in key technologies or
markets may restrict competition and limit
designer or consumer choices

Page 32 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Acknowledgements
Not applicable.
Author contributions
RL conceptualized the study, designed the methodology, conducted the investigation, curated the data, performed the
formal analysis, and drafted the manuscript. YY contributed to the investigation, data curation, formal analysis, and draft-
ing of the manuscript. FX contributed to the investigation, project administration, and supervision. MG contributed to
the investigation, project administration and supervision. All authors read and approved the final manuscript.
Funding
This work was supported by the National Natural Science Foundation of China (52505043).
Data availability
The data that support the findings of this study are available in the references cited within this article. The datasets used
during the current study are available from the corresponding author on reasonable request.
Declarations
Ethics approval and consent to participate
Not applicable.
Competing interests
The authors declare that they have no competing interests.
Received: 26 May 2025   Accepted: 11 May 2026
References
Aghilar, P ., Anelli, V. W., Trizio, M., Di Sciascio, E., & Di Noia, T. (2025). Training-free, identity-preserving image editing for
fashion pose alignment and normalization. Expert Systems with Applications, 293, Article 128579. https:// doi. org/
10. 1016/j. eswa. 2025. 128579
Fig. 7 Overview of research status

Page 33 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Alotaibi, B., Almutarie, A., Alotaibi, S., & Alotaibi, M. (2025). Improving fashion sentiment detection on X through
hybrid transformers and RNNs. Computers, Materials & Continua, 84(3), 4451–4467. https:// doi. org/ 10. 32604/ cmc.
2025. 066050
Amershi, S., Weld, D., Vorvoreanu, M., Fourney, A., Nushi, B., Collisson, P ., Suh, J., Iqbal, S., Bennett, P . N., Inkpen, K.,
Teevan, J., Kikin-Gil, R., & Horvitz, E. (2019). Guidelines for human-AI interaction. In Proceedings of the 2019 CHI
Conference on Human Factors in Computing Systems (pp. 1–13). Association for Computing Machinery. https://
doi. org/ 10. 1145/ 32906 05. 33002 33
An, H., Lee, K. Y., Choi, Y., & Park, M. (2023). Conceptual framework of hybrid style in fashion image datasets for
machine learning. Fashion and Textiles, 10(1), Article 18. https:// doi. org/ 10. 1186/ s40691- 023- 00338-8
An, H., & Park, M. (2026). AI tools and fashion design education: Instructor perspectives on student challenges and
design process tool support. Fashion and Textiles, 13(1), Article 3. https:// doi. org/ 10. 1186/ s40691- 025- 00452-9
Anitha, S., & Neelakandan, R. (2025). Demand forecasting new fashion products: A review paper. Journal of Forecast-
ing, 44(2), 270–280. https:// doi. org/ 10. 1002/ for. 3192
Baek, E., Haines, S., Fares, O. H., Huang, Z., Hong, Y., & Lee, S. H. M. (2022). Defining digital fashion: Reshaping the field
via a systematic review. Computers in Human Behavior, 137, Article 107407. https:// doi. org/ 10. 1016/j. chb. 2022.
107407
Bao, C., Miao, Y., Chen, J., & Zhang, X. (2023). Developing a generalized regression forecasting network for the predic-
tion of human body dimensions. Applied Sciences, 13(18), Article 10317. https:// doi. org/ 10. 3390/ app13 18103 17
Cao, S., Chai, W., Hao, S., Zhang, Y., Chen, H., & Wang, G. (2024). DiffFashion: Reference-based fashion design with
structure-aware transfer by diffusion models. IEEE Transactions on Multimedia, 26, 3962–3975. https:// doi. org/ 10.
1109/ TMM. 2023. 33182 97
Carvalho, A., Levitt, A., Levitt, S., Khaddam, E., & Benamati, J. (2019). Off-the-shelf artificial intelligence technologies
for sentiment and emotion analysis: A tutorial on using IBM natural language processing. Communications of the
Association for Information Systems, 44, 918–943. https:// doi. org/ 10. 17705/ 1CAIS. 04443
Chakraborty, S., Hoque, M. S., Rahman Jeem, N., Biswas, M. C., Bardhan, D., & Lobaton, E. (2021). Fashion recommendation
systems, models and methods: A review. Informatics, 8(3), Article 49. https:// doi. org/ 10. 3390/ infor matic s8030 049
Chan, C. O., Lau, H., & Fan, Y. (2025). Modelling intended product demand in fashion retail using IoT and AI. Interna-
tional Journal of Business Information Systems, 48(1), 54–71. https:// doi. org/ 10. 1504/ IJBIS. 2025. 144080
Chan, H. H. Y., Henninger, C., Boardman, R., & Blazquez Cano, M. (2024). The adoption of digital fashion as an end product:
A systematic literature review of research foci and future research agenda. Journal of Global Fashion Marketing, 15(1),
155–180. https:// doi. org/ 10. 1080/ 20932 685. 2023. 22510 33
Chen, X., Hu, Z., & Wang, C. (2024). Empowering education development through AIGC: A systematic literature review.
Education and Information Technologies, 29(13), 17485–17537. https:// doi. org/ 10. 1007/ s10639- 024- 12549-7
Chen, Y., & Ma, J. (2025). An intelligent generative method of fashion design combining attribute knowledge and Stable
Diffusion model. Textile Research Journal, 95(11–12), 1231–1254. https:// doi. org/ 10. 1177/ 00405 17524 12895 78
Chien, W.-C., Cho, H.-H., & Zeadally, S. (2025). Human-centric GenAI garment designer: 3D fashion design recommenda-
tions. IEEE Consumer Electronics Magazine, 14(5), 103–114. https:// doi. org/ 10. 1109/ MCE. 2024. 34925 10
Choi, W., Jang, S., Kim, H. Y., Lee, Y., Lee, S., Lee, H., & Park, S. (2023). Developing an AI-based automated fashion design
system: Reflecting the work process of fashion designers. Fashion and Textiles, 10(1), Article 39. https:// doi. org/ 10.
1186/ s40691- 023- 00360-w
Choi, Y., Kwak, S., Lee, K., Choi, H., & Shin, J. (2025). Improving diffusion models for authentic virtual try-on in the wild. In
A. Leonardis, E. Ricci, S. Roth, O. Russakovsky, T. Sattler, & G. Varol (Eds.), Computer vision—ECCV 2024 (pp. 206–235).
Springer Nature Switzerland.
De Giovanni, M., Lazoi, M., Bandinelli, R., & Fani, V. (2025). Advanced planning systems in production planning control: An
ethical and sustainable perspective in fashion sector. Applied Sciences, 15(13), Article 7589. https:// doi. org/ 10. 3390/
app15 137589
Deng, M., & Chen, L. (2025). CDGFD: Cross-domain generalization in ethnic fashion design using LLMs and GANs: A sym-
bolic and geometric approach. IEEE Access, 13, 7192–7207. https:// doi. org/ 10. 1109/ ACCESS. 2024. 35244 44
Deshmukh, G., De, S., Sehgal, C., Gupta, J. S., & Mittal, S. (2024). Dressing the imagination: A dataset for AI-powered transla-
tion of text into fashion outfits and a novel NeRA adapter for enhanced feature adaptation (Version 5). arXiv. https://
doi. org/ 10. 48550/ ARXIV. 2411. 13901
Diekemper, R. L. (2015). Development of the documentation and appraisal review tool for systematic reviews. World
Journal of Meta-Analysis, 3(3), 142. https:// doi. org/ 10. 13105/ wjma. v3. i3. 142
Dong, W., Liang, J., & Suh, S. (2025). Effectiveness of AI technologies in reducing textile waste in the fashion industry.
Textile Research Journal, 96(3–4), 428–451. https:// doi. org/ 10. 1177/ 00405 17525 13575 82
Dong, X., & Fu, J. (2024). Visual analysis of the evolution of traditional Chinese ethnic clothing design styles based on big
data and artificial intelligence. Applied Mathematics and Nonlinear Sciences, 9(1), Article 20230743. https:// doi. org/ 10.
2478/ amns. 2023.2. 00743
Dubey, A., Bhardwaj, N., Abhinav, K., Kuriakose, S. M., Jain, S., & Arora, V. (2020). AI assisted apparel design (Version 2).
arXiv. https:// doi. org/ 10. 48550/ ARXIV. 2007. 04950
Figoli, F. A., Facchin, A., Gobbo, B., & Mattioli, F. (2025). Richness and ambiguity: Mapping artificial intelligence labels
in human-AI collaboration research. In M. Karyda, D. Çay, Á. K. Bakk, R. Dezső, & J. Hemmings (Eds.), EKSIG 2025:
Data as experiential knowledge and embodied processes. Design Research Society. https:// doi. org/ 10. 21606/ eksig
2025. 126
Gao, D., Ma, Y., Liu, S., Song, M., Jin, L., Jiang, W., Wang, X., Ning, W., Yu, S., Xuan, Q., Cai, X., & Yang, L. (2024). FashionGPT:
LLM instruction fine-tuning with multiple LoRA-adapter fusion. Knowledge-Based Systems, 299, Article 112043.
https:// doi. org/ 10. 1016/j. knosys. 2024. 112043
Giri, C., Jain, S., Zeng, X., & Bruniaux, P . (2019). A detailed review of artificial intelligence applied in the fashion and apparel
industry. IEEE Access, 7, 95376–95396. https:// doi. org/ 10. 1109/ ACCESS. 2019. 29289 79
Gu, X., Yao, Q., Gong, X., & Kuang, Z. (2023). iDesigner: Making intelligent fashion designs. Multimedia Tools and Applica-
tions, 83(11), 32835–32855. https:// doi. org/ 10. 1007/ s11042- 023- 16780-1

Page 34 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Guerra-Tamez, C. R., Kraul Flores, K., Serna-Mendiburu, G. M., Chavelas Robles, D., & Ibarra Cortés, J. (2024). Decoding Gen
Z: AI’s influence on brand trust and purchasing behavior. Frontiers in Artificial Intelligence, 7, Article 1323512. https://
doi. org/ 10. 3389/ frai. 2024. 13235 12
He, K., Yao, K., Zhang, Q., Yu, J., Liu, L., & Xu, L. (2024). DressCode: Autoregressively sewing and generating garments from
text guidance. ACM Transactions on Graphics, 43(4), Article 72. https:// doi. org/ 10. 1145/ 36581 47
Huang, G. (2024). Artificial intelligence enabled apparel design research. Applied Mathematics and Nonlinear Sciences, 9(1),
Article 20241200. https:// doi. org/ 10. 2478/ amns- 2024- 1200
Jabari, S., Shaikh, A., Genç, Ç., Buruk, O., Virkki, J., & Hamari, J. (2024). A systematic literature review on computational
fashion wearables. International Journal of Human-Computer Interaction, 40, 6913-6940. https:// doi. org/ 10. 1080/
10447 318. 2023. 22690 07
Jang, S. Y. (2026). From designer to curator: Cognitive and creative trade-offs in GenAI-assisted design. Fashion and
Textiles, 13(1), Article 12. https:// doi. org/ 10. 1186/ s40691- 026- 00459-w
Jang, S. Y., & Ha, J. (2023). Presenting fabrics in digital environment: Fashion designers’ perspectives on communicating
tactile qualities of the fabrics. Fashion and Textiles, 10(1), Article 6. https:// doi. org/ 10. 1186/ s40691- 022- 00328-2
Johnson, R. B., & Onwuegbuzie, A. J. (2004). Mixed methods research: A research paradigm whose time has come. Educa-
tional Researcher, 33(7), 14–26. https:// doi. org/ 10. 3102/ 00131 89X03 30070 14
Jung, D., & Suh, S. (2024). Enhancing soft skills through generative AI in sustainable fashion textile design education.
Sustainability, 16(16), Article 6973. https:// doi. org/ 10. 3390/ su161 66973
Karimova, G., LeMay, S. A., Müller, A., & Klumpp, M. (2026). From the shallows to the shelves and back: A review, synthesis,
and research agenda for socially sustainable, AI-driven digital fashion supply chains. Business Ethics, the Environment
& Responsibility, 35(2), 1230–1246. https:// doi. org/ 10. 1111/ beer. 12839
Ke, H., & Wang, Y. (2024). Deep learning techniques in modern women’s smart clothing design. Applied Mathematics and
Nonlinear Sciences, 9(1), Article 20230065. https:// doi. org/ 10. 2478/ amns. 2023.1. 00065
Kim, M., Joo, M., & Han, K. (2024). CoCoStyle: Mixed initiative co-creative system to support creative process of fashion
design. SoftwareX, 27, Article 101857. https:// doi. org/ 10. 1016/j. softx. 2024. 101857
Kim, S. J. (2024). Generative artificial intelligence in collaborative ideation: Educational insight from fashion students. IEEE
Access, 12, 49261–49274. https:// doi. org/ 10. 1109/ ACCESS. 2024. 33821 94
Kouslis, E., Papachristou, E., Stavropoulos, T. G., Papazoglou Chalikias, A., Chatzilari, E., Nikolopoulos, S., & Kompatsiaris,
I. (2025). AI in fashion: A literature review. Electronic Commerce Research, 25, 4071–4102. https:// doi. org/ 10. 1007/
s10660- 024- 09872-z
Lee, G., & Kim, H.-Y. (2024). Human vs. AI: The battle for authenticity in fashion design and consumer response. Journal of
Retailing and Consumer Services, 77, Article 103690. https:// doi. org/ 10. 1016/j. jretc onser. 2023. 103690
Lee, J. (2025). Empowering students through generative AI and cultural diversity in interdisciplinary fashion design
education. Research Journal of Textile and Apparel. https:// doi. org/ 10. 1108/ RJTA- 02- 2025- 0017
Lee, J., Kim, J., & Lee, H. (2025). Diffusedesigner: Sketch-based controllable clothing image generation. Fashion and
Textiles, 12(1), Article 26. https:// doi. org/ 10. 1186/ s40691- 025- 00426-x
Lee, L. W., Dabirian, A., McCarthy, I. P ., & Kietzmann, J. (2020). Making sense of text: Artificial intelligence-enabled
content analysis. European Journal of Marketing, 54(3), 615–644. https:// doi. org/ 10. 1108/ EJM- 02- 2019- 0219
Li, H., Wu, J., Chen, Z., Xu, W., & He, L. (2025a). FS-control: Artistic fashion design with discriminated and conditional
diffusion model. Computers & Graphics, 131, Article 104304. https:// doi. org/ 10. 1016/j. cag. 2025. 104304
Li, H.-C., Wang, L.-K., Chang, Y.-K., & Huang, K.-Y. (2025). Establishing colour harmony evaluation and recommendation
model for clothing colour matching based on machine learning and deep learning. Fashion and Textiles, 12(1),
Article 27. https:// doi. org/ 10. 1186/ s40691- 025- 00433-y
Lim, W. M., Gunasekara, A., Pallant, J. L., Pallant, J. I., & Pechenkina, E. (2023). Generative AI and the future of education:
Ragnarök or reformation? A paradoxical perspective from management educators. The International Journal of
Management Education, 21(2), Article 100790. https:// doi. org/ 10. 1016/j. ijme. 2023. 100790
Liu, Y., Shaari, N., & Zhang, L. (2025). Digital transformation in the fashion industry: New horizons for marketing and
fashion design. Asian Journal of Technology Innovation, 33, 1137-1157. https:// doi. org/ 10. 1080/ 19761 597. 2024.
24354 65
Lu, Z., Guo, J., Liu, S., & Yin, Z. (2025). Bidirectional feature modulation fusion for fashion design using latent diffusion
models. The Visual Computer, 41(11), 8553–8567. https:// doi. org/ 10. 1007/ s00371- 025- 03884-y
Manchiraju, S. (2025). The ethical thread: AI’s role in the tapestry of fashion. AI & SOCIETY , 40(5), 4029–4034. https://
doi. org/ 10. 1007/ s00146- 024- 02151-3
Manzo, D. S. H., Jiang, Y., Elyan, E., & Isaacs, J. (2025). Artificial intelligence-based conversational agents used for
sustainable fashion: Systematic literature review. International Journal of Human–computer Interaction, 41, 4640-
4652. https:// doi. org/ 10. 1080/ 10447 318. 2024. 23529 20
McEwan, A. (2024). Article intelligence in the fashion industry. University of Pittsburgh Law Review. https:// doi. org/ 10.
5195/ lawre view. 2024. 1059
Moher, D., Liberati, A., Tetzlaff, J., Altman, D. G., The PRISMA Group. (2009). Preferred reporting items for systematic
reviews and meta-analyses: The PRISMA statement. PLoS Medicine, 6(7), Article e1000097. https:// doi. org/ 10.
1371/ journ al. pmed. 10000 97
Mohiuddin Babu, M., Akter, S., Rahman, M., Billah, M. M., & Hack-Polay, D. (2024). The role of artificial intelligence in
shaping the future of agile fashion industry. Production Planning & Control, 35(15), 2084–2098. https:// doi. org/ 10.
1080/ 09537 287. 2022. 20608 58
Mrinali, A., & Gupta, P . (2025). Cloth-net: Improved hybrid adversarial network with dense vision transformer for
2D–3D image classification for accurate cloth recommendation engine. International Journal of Clothing Science
and Technology, 37(3), 402–442. https:// doi. org/ 10. 1108/ IJCST- 05- 2024- 0110
Niyompatama, M. J., & Lapatoura, I. (2025). Generative AI in fashion design creation: A copyright analysis of AI-
assisted designs. Journal of Intellectual Property Law & Practice, 20(10), 654–666. https:// doi. org/ 10. 1093/ jiplp/
jpaf0 45

Page 35 of 36
Lin et al. Fashion and Textiles           (2026) 13:32

Oh, J., & Kim, S. (2023). Automatic generation of parametric patterns from grading patterns using artificial intel-
ligence. International Journal of Clothing Science and Technology, 35(6), 889–903. https:// doi. org/ 10. 1108/
IJCST- 07- 2022- 0102
Page, M. J., McKenzie, J. E., Bossuyt, P . M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A.,
Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson,
E., McDonald, S., & Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic
reviews. BMJ, 372, Article n71. https:// doi. org/ 10. 1136/ bmj. n71
Pan, S., Wang, P ., & Yang, C. (2024). Optimization of automatic classification for women’s pants based on the Swin
Transformer model. Fashion and Textiles, 11(1), Article 42. https:// doi. org/ 10. 1186/ s40691- 024- 00408-5
Pillarisetty, R., & Mishra, P . (2022). A review of AI (artificial intelligence) tools and customer experience in online fash-
ion retail. International Journal of E-Business Research, 18(2), 1–12. https:// doi. org/ 10. 4018/ IJEBR. 294111
Ramos, L., Rivas-Echeverría, F., Pérez, A. G., & Casas, E. (2023). Artificial intelligence and sustainability in the fash-
ion industry: A review from 2010 to 2022. SN Applied Sciences, 5(12), Article 387. https:// doi. org/ 10. 1007/
s42452- 023- 05587-2
Ranjan, A., & Upadhyay, A. K. (2025). Value co-creation by interactive AI in fashion e-commerce. Cogent Business &
Management, 12(1), Article 2440127. https:// doi. org/ 10. 1080/ 23311 975. 2024. 24401 27
Rockett, E., Fenwick, M., & Jurcys, P . (2025). Fashion 4.0 and emerging designers: Leveraging data and AI to drive crea-
tivity, innovation and compliance in global supply chain regulation. Journal of Intellectual Property Law & Practice,
20(2), 111–121. https:// doi. org/ 10. 1093/ jiplp/ jpae1 10
Ruiz-Viñals, C., Pretel-Jiménez, M., Del Olmo Arriaga, J. L., & Miró Pérez, A. (2024). The influence of artificial intelligence
on Generation Z’s online fashion purchase intention. Journal of Theoretical and Applied Electronic Commerce
Research, 19(4), 2813–2827. https:// doi. org/ 10. 3390/ jtaer 19040 136
Shi, W., Wong, W., & Zou, X. (2025). Generative AI in fashion: Overview. ACM Transactions on Intelligent Systems and
Technology, 16(4), Article 74. https:// doi. org/ 10. 1145/ 37180 98
Shirkhani, S., Mokayed, H., Saini, R., & Chai, H. Y. (2023). Study of AI-driven fashion recommender systems. SN Com-
puter Science, 4(5), Article 514. https:// doi. org/ 10. 1007/ s42979- 023- 01932-9
Sinha, P ., Sharma, M., & Agrawal, R. (2024). AI enabled business decisions that enhance sustainability impact of an
apparel and fashion supply chain. Technology Analysis & Strategic Management. https:// doi. org/ 10. 1080/ 09537
325. 2024. 24244 28
Song, D., Zeng, J.-H., Liu, M., Li, X.-Y., & Liu, A.-A. (2024). Fashion customization: Image generation based on editing
clue. IEEE Transactions on Circuits and Systems for Video Technology, 34(6), 4434–4444. https:// doi. org/ 10. 1109/
TCSVT. 2023. 33384 59
Surbakti, F. P . S. (2025). Systematic literature review on generative AI: Ethical challenges and opportunities. Interna-
tional Journal of Advanced Computer Science and Applications, 16(5), 307–315. https:// doi. org/ 10. 14569/ IJACSA.
2025. 01605 30
Swaminathan, K., & Venkitasubramony, R. (2024). Demand forecasting for fashion products: A systematic review.
International Journal of Forecasting, 40(1), 247–267. https:// doi. org/ 10. 1016/j. ijfor ecast. 2023. 02. 005
Thomassey, S., & Zeng, X. (Eds.). (2018). Artificial intelligence for fashion industry in the big data era. Springer Singapore.
https:// doi. org/ 10. 1007/ 978- 981- 13- 0080-6
Wang, Y., Luo, H., & Liu, H. (2025). Research on the application of AIGC technology in e-commerce platforms advertis-
ing. International Journal of Asian Social Science Research, 2(2), 32–41. https:// doi. org/ 10. 70267/ ijassr. 250202. 3241
Wang, Y., Valipour, M., & Zatarain, O. A. (2016). Quantitative semantic analysis and comprehension by cognitive
machine learning. International Journal of Cognitive Informatics and Natural Intelligence, 10(3), 13–28. https:// doi.
org/ 10. 4018/ IJCINI. 20160 70102
Wu, D., Wu, M., Li, Y., Jiang, J., Li, X., Deng, H., Liu, C., & Li, Y. (2024). StyleWe: Towards style fusion in generative fashion
design with efficient federated AI. Proceedings of the ACM on Human-Computer Interaction, 8, Article 515. https://
doi. org/ 10. 1145/ 36870 54
Yan, H., Zhang, H., Shi, J., & Ma, J. (2024a). Mixing and matching elements for intelligent fashion design: A generative
adversarial network with structure and texture disentanglement. IEEE Transactions on Consumer Electronics, 70(1),
358–370. https:// doi. org/ 10. 1109/ TCE. 2023. 33295 74
Yan, H., Zhang, H., Shi, J., Ma, J., & Xu, X. (2023). Toward intelligent fashion design: A texture and shape disentangled
generative adversarial network. ACM Transactions on Multimedia Computing, Communications, and Applications,
19(3), Article 107. https:// doi. org/ 10. 1145/ 35675 96
Yan, H., Zhang, H., & Zhang, Z. (2024b). Learning to disentangle the colors, textures, and shapes of fashion items: A
unified framework. IEEE Transactions on Multimedia, 26, 5615–5629. https:// doi. org/ 10. 1109/ TMM. 2023. 33380 50
Yeo, H., Noh, T., & Han, K. (2026). LLM-generated content-based explanations for user experience in fashion recom-
mender systems. Fashion and Textiles, 13(1), Article 16. https:// doi. org/ 10. 1186/ s40691- 026- 00464-z
Zhang, Y., & Liu, C. (2024). Unlocking the potential of artificial intelligence in fashion design and e-commerce applica-
tions: The case of Midjourney. Journal of Theoretical and Applied Electronic Commerce Research, 19(1), 654–670.
https:// doi. org/ 10. 3390/ jtaer 19010 035
Zhang, Y., Wang, B., Hong, Y., & Zhang, S. (2024). Development of women’s shirt style recognition model (WSSRM)
based on a ResNet and Transformer integrated method. Textile Research Journal, 95(13–14), 1516–1525. https://
doi. org/ 10. 1177/ 00405 17524 12905 21
Zhao, L., Li, M., & Sun, P . (2024). Neo-Fashion: A data-driven fashion trend forecasting system using catwalk analysis.
Clothing and Textiles Research Journal, 42(1), 19–34. https:// doi. org/ 10. 1177/ 08873 02X21 10042 99
Zhou, D., Zhang, H., Ma, J., & Shi, J. (2024). BC-GAN: A generative adversarial network for synthesizing a batch of col-
located clothing. IEEE Transactions on Circuits and Systems for Video Technology, 34(5), 3245–3259. https:// doi. org/
10. 1109/ TCSVT. 2023. 33182 16

Page 36 of 36Lin et al. Fashion and Textiles           (2026) 13:32
Publisher’s Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Rufan Lin is a PhD candidate at the College of Computer Science and Technology, Zhejiang University.
Yihan Yu is a graduate student at the School of Fashion Design and Engineering, Zhejiang Sci-Tech
University.
Fan Xia is a professor at the School of Fashion Design and Engineering, Zhejiang Sci-Tech University.
Manhao Guan is an assistant professor at the College of Computer Science and Technology, Zhejiang
University.
