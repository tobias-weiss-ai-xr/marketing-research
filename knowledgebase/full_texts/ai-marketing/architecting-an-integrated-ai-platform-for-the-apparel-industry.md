---
title: Architecting an Integrated AI Platform for the Apparel Industry
url: https://doi.org/10.11648/j.ajist.20250903.14
category: ai-marketing
subcategory: framework
date: 2025-09
venue: American Journal of Information Science and Technology
authors:
- P. K. Majumdar
source: openalex-oa
pdf_url: http://article.sciencepg.com/pdf/j.ajist.20250903.14
pages: 17
chars: 83949
fetched_at: '2026-11-08T19:45:58+00:00'
kb_version: 1
---

# Architecting an Integrated AI Platform for the Apparel Industry

American Journal of Information Science and Technology
2025, V ol. 9, No. 3, pp. 194-210
https://doi.org/10.11648/j.ajist.20250903.14

*Corresponding author:
Received: 25 July 2025; Accepted: 11 August 2025; Published: 13 September 2025

Copyright: © The Author(s), 2025. Published by Science Publishing Group. This is an Open Access article, distributed
under the terms of the Creative Commons Attribution 4.0 License ( http://creativecommons.org/licenses/by/4.0/), which
permits unrestricted use, distribution and reproduction in any medium, provided the original work is properly cited.

Research Article
Architecting an Integrated AI Platform for the Apparel
Industry
Partha Majumdar*
Department of Computer Science, Swiss School of Business and Management, Geneva, Switzerland

Abstract
This research article proposes an integrated AI platform designed to revolutionise the apparel industry. The platform, envisioned
as a comprehensive ecosystem, aims to enhance every stage of the apparel value chain, from design ideati on to marketing and
supply chain management. The architecture is built around three core components: an AI-Powered Design Studio, an Intelligent
Production & Supply Chain Backbone, and a Hyper -Personalised Marketing & Engagement Engine. The AI -Powered Design
Studio leverages generative AI, deep learning, and computer vision to transform the design process. A Trend Forecasting Engine
utilises diverse data sources (social media, e -commerce, runway shows) to predict trends with high accuracy, providing
data-driven insights that directly inform the AI Co -Creation Suite. This suite employs GANs, diffusion models, and
sketch-to-image translation to generate design variations, refine concepts, and simulate fabric drape and fit, resulting in faster
design cycles and  commercially viable products. A Hyper -Personalisation Module further enhances this by generating
personalised designs tailored to individual customer styles and body measurements, bridging the "aspiration gap" between
desired and attainable styles. The In telligent Production & Supply Chain Backbone focuses on efficiency and sustainability. A
Material Optimisation and Waste Reduction System uses computer vision to detect fabric defects and optimise cutting layouts,
minimising waste. Predictive inventory man agement and AI -powered logistics orchestration, combined with blockchain
technology for enhanced traceability, create a responsive and transparent supply chain. Automated quality control, utilising
computer vision, reduces defects and enables predictive ma intenance of machinery, optimising production efficiency. A
Sustainability and Circularity Management Dashboard provides a holistic view of environmental and social impact, facilitating
data-driven decision-making and transparency for consumers. Finally, the Hyper-Personalised Marketing & Engagement Engine
uses AI to deliver tailored experiences. A Personalised Marketing and Dynamic Campaign Engine, powered by a Customer Data
Platform (CDP) and a "Latent Style" algorithm, provides personalised product recom mendations, marketing messages, and
promotions. An Automated Content Generation Engine generates marketing assets (product descriptions, social media posts,
email copy) at scale, while a Unified Consumer Insights Platform provides real-time market analysis. Conversational AI, through
chatbots and virtual stylists, enhances customer support and creates personalised interactions. The use of 3D digital twins a nd
virtual prototyping, including virtual try -on (VTO) capabilities, enhances consumer engagement and reduces return rates. The
article concludes with a phased implementation roadmap, prioritising data infrastructure, key modules with high ROI (such as
waste reduction), and subsequent integration of generative design and personalisation. The overall goal i s a symbiotic
relationship between human creativity and AI's efficiency, resulting in a future-ready apparel industry characterised by enhanced
speed, sustainability, and personalisation. Case studies of industry leaders like Zara, Stitch Fix, H&M, and Nik e illustrate the
successful application of similar AI strategies.

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

195
Keywords
Artificial Intelligence in Fashion, Generative AI for Apparel Design, Supply Chain Optimisation, Personalised Marketing,
Hyper-Personalisation

1. Executive Summary
This article outlines a comprehensive solution architecture
for a generative AI-driven platform aimed at transforming the
apparel industry. Envisioned as an integrated ecosystem, the
platform covers the entire value chain, from initial design
ideas to production optimisation and targeted marketing. By
combining machine learning, computer vision, natu ral la n-
guage processing, and generative models, it will enable a p-
parel companies to reach new heights in creativity, efficiency,
personalisation, and sustainability. The document details the
techniques and technologies needed to develop three core
components:
1) The AI -Powered Design Studio , which speeds up
trend-responsive creativity;
2) The Intelligent Production & Supply Chain Backbone ,
promoting efficiency and sustainability; and
3) The Hyper -Personalised Marketing & Engagement
Engine, strengthening customer rel ationships and
maximising commercial results. This blueprint acts as
both a strategic and technical guide for creating a f u-
ture-ready system that offers a robust competitive edge
in the digital-first fashion industry.
2. Part I: Solution Architecture for
Generative AI in Apparel Design
This initial segment of the solution architecture concentrates
on developing a network of interconnected AI tools that funda-
mentally transform the design process. Its goal is to shift from a
linear, intuition-based workflow to a more integrated, d a-
ta-driven, and generative approach. This system aims to reduce
design cycles, boost the commercial potential of new collections,
and support personalisation at an unparalleled scale.
2.1. The Trend Forecasting Engine: From Data
to Design Intelligence
The foundation of a commercially successful apparel line is
its precise alignment with market desires and cultural zeitgeist.
This module will serve as the platform's sensory organ, co n-
tinuously ingesting and analysing vast, multimodal d ata
streams to predict and quantify fashion trends before they
reach market saturation. It moves beyond simple observation
to provide actionable, data -driven intelligence that directly
informs the creative process.
The proposed solution is an automated, mu lti-source intel-
ligence engine that synthesises data from runway shows,
global social media platforms, e -commerce sites, search e n-
gine queries, and direct consumer feedback to generate d y-
namic trend reports [21]. These reports will not only identify
what is trending (e.g., "Y2K Revival," "Quiet Luxury") but
also quantify its velocity, target demographic, geographic
penetration, and predicted lifespan [30, 32]. The engine's
output is designed to serve as a direct, data -driven input for
the AI Co -Creation Suite, creating a seamless link between
market intelligence and creative execution.
To achieve this, a combination of sophisticated techniques
and technologies will be employed:
1) Social & Web Analysis: The engine will utilise Natural
Language Processing (NL P) and sentiment analysis
models to process immense volumes of unstructured
text from social media platforms like TikTok, Inst a-
gram, and Pinterest, as well as fashion blogs and
product reviews. This allows the system to gauge co n-
sumer sentiment towards spe cific styles, colours, m a-
terials, and brands in real time [21]. Concurrently,
Time-series analysis  and predictive modelling  tech-
niques, such as Long Short -Term Memory (LSTM)
networks, will be applied to search query data from
sources like Google Trends and  e-commerce market
data from platforms like Trendalytics. This analysis will
forecast trend trajectories, distinguishing between
fleeting microtrends and significant macro shifts [21].
2) Visual Analysis: Computer Vision (CV) models, specif-
ically Convolutional Neural Networks (CNNs) , will
conduct large-scale analysis of visual data. These models
will be trained on millions of images from runway shows,
street style blogs, and social media posts to detect and
classify over 2,000 distinct fashion attributes, including
silhouettes (e.g., A-line, oversized), patterns (e.g., floral,
plaid), cuts, colours, and fabrics [33]. This provides a
quantitative, objective measure of visual trends that
complements the text-based sentiment analysis.
3) Generative AI for Trend Synthesis: The platform will
leverage large -scale Generative AI models such as
ChatGPT-4 and DALL-E 3 to synthesise and visualise
predicted trends. For instance, by feeding quantified
trend keywords and attributes (e.g., "gender flu idity,"
"asymmetrical hemlines," "recycled nylon") into a
model like ChatGPT, the system can generate detailed

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

196
textual descriptions and creative concepts. These d e-
scriptions can then be used as prompts for image ge n-
eration models like DALL -E 3 to create vi sual mood
boards and initial design concepts, effectively tran s-
lating raw data into creative inspiration [60].
4) Platform Integration: To enrich the platform's propri e-
tary data pool and benchmark its findings, it will int e-
grate via API with leading trend for ecasting services.
Platforms like WGSN, Heuritech, and T-Fashion provide
specialised, high-accuracy forecasts [21]. Heuritech, for
example, analyses millions of social media images daily
to quantify trend trajectories across different consumer
segments (fr om celebrity influencers to mainstream
consumers) and provides predictive insights up to 24
months in advance, claiming over 90% accuracy [33].
The core strategic strength of this engine isn't just its ability
to predict trends but its capacity to enable prescriptive design.
Instead of merely indicating that "cargo pants are trending," it
produces a comprehensive, actionable brief. The process
begins by integrating data from various sources: social media
velocity data from a T -Fashion-like analysis, consume r sen-
timent from NLP, and runway aesthetics through computer
vision, creating a complete "trend profile." This profile details
not only the "what" (cargo pants), but also the "who" (Gen Z
urban females), the "how" (attributes like low-rise silhouettes
and recycled nylon fabric), and the "when" (a +35% e n-
gagement rise with a forecasted peak in 6 months). This d e-
tailed profile shifts from being a passive insight to a dynamic
design constraint—serving as a creative brief that feeds d i-
rectly into the generative  design module. This transforms a
market signal into an active instruction, such as: "Generate 15
design variations of low -rise cargo pants in recycled nylon
targeting Gen Z urban females for the upcoming
Spring/Summer season." This streamlined, data -driven pr o-
cess from market signal to initial design significantly reduces
the risk of creating commercially unviable products, ensuring
creative efforts are aligned with market realities from the start.
2.2. The AI Co-Creation Suite: Augmenting
Designer Creativity
This module is the platform's creative hub, acting as an
effective' co-pilot" that enhances the designer's expertise and
intuition. It quickly generates ideas, visualises, and refines
designs, turning abstract concepts, mood boards, and initial
sketches into photorealistic, ready -for-production visuals
much faster than conventional methods.
The solution features a unified design interface that co m-
bines multiple generative AI modes. Designers can co m-
municate through natural language prompts, uploa d visual
materials such as mood boards and fabric swatches, or import
2D technical flat sketches. The system then produces n u-
merous design variations within seconds. Importantly, it a l-
lows for an iterative refinement process, where designers can
choose a generated concept and easily modify it with simple
commands like "change the neckline to a V-neck," "apply this
denim texture," or "make the silhouette more fitted." This
enables a smooth, conversational workflow between the d e-
signer and the AI.
A portfolio  of specialised generative models powers the
suite's capabilities:
1) Generative Adversarial Networks (GANs): The pla t-
form will implement a variety of GAN architectures
tailored for specific fashion design tasks. StyleGANs
are capable of generating novel, hig h-resolution, and
highly realistic fashion images from a latent space,
ideal for creating entirely new concepts [22, 38]. Con-
ditional GANs (CGANs) will be used to generate i m-
ages based on specific inputs, such as a clothing cat e-
gory ("dress"), a textual de scription, or a sketch,
providing greater control over the output [69]. For
tasks like applying new textures or patterns to existing
garment sketches, CycleGANs are the ideal choice due
to their proficiency in unpaired image -to-image trans-
lation [38]. More advanced frameworks, like the pr o-
posed DFDGAN, can even generate a compatible
fashion item to complete an existing outfit, demo n-
strating a sophisticated understanding of style compa t-
ibility [38].
2) Diffusion Models: To achieve the highest fidelity in
translating complex, descriptive prompts into images,
the suite will integrate with state -of-the-art
text-to-image diffusion model APIs, such as OpenAI's
DALL-E 3 or Midjourney. These models excel at inte r-
preting nuanced and abstract language (e.g., "a futuristic
trench coat inspired by brutalist architecture with bi o-
luminescent details"), making them powerful tools for
initial brainstorming and concept exploration [60].
3) Sketch-to-Image Translation: A critical component fo r
bridging traditional and digital workflows is the incl u-
sion of specialised models that transform 2D fashion
flat drawings or hand sketches into realistic product
images. This allows designers to maintain their fami l-
iar sketching process while leveraging AI for rapid,
photorealistic visualisation. Tools like New Arc AI [42]
and VisualHound [53] specialise in this capability, e n-
abling designers to prototype and evaluate designs e f-
ficiently before committing to physical sampling.
4) Platform Integration: The suite can be built upon or
integrated with existing end -to-end platforms like
Resleeve.ai [55] or AiDA [2]. These platforms offer
comprehensive solutions for synthesising diverse i n-
puts—such as mood boards, colour palettes, fabric
prints, and sketches —into cohesive and harmonious
fashion collections, potentially accelerating the deve l-
opment of the suite by over 60% [2].
A truly effective AI suite must mirror the natural workflow
of a designer, which is not a single action but a journey from
an abstract idea to a concrete product. Therefore, the suite is
best structured as a "Creative Exploration Funnel," guiding

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

197
the designer from broad exploration to refined execution. This
workflow approach respects the creative process while e m-
bedding technical and commercial guardrails at each stage.
The funnel begins at its widest point with divergent ideation.
A designer might start w ith a text prompt derived from the
Trend Forecasting Engine, such as "Generate concepts for
'dopamine dressing' for Spring 2026." The system would
employ a diffusion model to create 50 diverse, visually rich
concepts, providing a broad field of creative possibilities. [65,
71]
In the next stage, the designer selects three of these co n-
cepts and creates rough sketches to refine the silhouettes and
key details. These sketches are then fed into the
sketch-to-image tool, which acts as the funnel's mid -section,
translating the rough ideas into 10 refined, realistic garment
images for each concept. This stage is about convergent r e-
finement, grounding the initial ideas in a more manufactur a-
ble form. Finally, the top five designs are passed to the a d-
vanced fabric sim ulation module to test their drape, fit, and
movement with specific, available textiles. This final stage of
the funnel validates the design's physical feasibility. This
structured workflow allows AI to augment creativity at each
critical phase—from unconstrained brainstorming to practical
refinement—ensuring the final output is both innovative and
commercially viable.
2.3. The Hyper-Personalisation Module:
Designing for the Individual
This module represents a paradigm shift from mass-market
design to designing for an audience of one. It connects the
creative process directly to the end consumer, enabling the
creation of personalised product recommendations and, ult i-
mately, bespoke, custom-fit garments at scale. The goal is to
move beyond simply recomme nding existing stock to gene r-
ating unique items tailored to a single user's style, preferences,
and physique.
The solution is a system that ingests and analyses indivi d-
ual customer data —including purchase history, browsing
behaviour, style preferences deri ved from quizzes or visual
inputs, and body measurements —to generate personalised
design recommendations or create made -to-measure patterns
[42]. This capability allows a brand to offer a level of service
previously reserved for high-end bespoke tailoring.
The technical foundation of this module includes:
1) Recommendation Engines: The system will employ a
sophisticated recommendation engine using a hybrid of
collaborative filtering and content -based filtering  al-
gorithms, drawing inspiration from the highly su c-
cessful models used by Stitch Fix [62]. The engine will
analyse a user's complete data profile to predict their
affinity for certain styles, colours, fits, and price points.
A key component will be a proprietary AI model, si m-
ilar to Stitch Fix's "StyleFil e," which creates a mu l-
ti-layered, nuanced style profile (e.g., "70% Classic, 20%
Edgy, 10% Boho") for each customer, moving beyond
simplistic labels [75].
2) Biometric Analysis: The module will use Computer
Vision algorithms to analyse user -submitted photos or
videos to extract key body measurements and predict
body shape with a high degree of accuracy [35]. This
biometric data is crucial for generating custom -fit pat-
terns automatically, a feature that can drastically reduce
return rates, which are often driven by poor fit.
3) Personalised Generative Design: The true innovation
of this module lies in combining the outputs of the
recommendation engine and biometric analysis with
generative models (GANs or Diffusion Models). For
example, suppose a user's "StyleFile " indicates a pre f-
erence for "bohemian" styles and their biometric ana l-
ysis identifies a pear -shaped body. In that case, the
system can generate a unique boho -style dress design
with a silhouette (e.g., an A -line skirt with a fitted
bodice) that is specifically flattering to that body type.
4) Platform Integration: To create a seamless and enga g-
ing user experience, the module will integrate with
personal styling applications like Style DNA  [64] or
Alta [4], which help users digitise their wardrobes and
understand their style. Furthermore, integration with
virtual try-on (VTO) solutions, such as those offered by
Vue.ai [70] will allow users to instantly visualise these
personalised designs on a virtual avatar of themselves.
A significant opportunity this module addresses is the "as-
piration gap"—the distance between the clothes a customer
aspires to wear (e.g., what they save on a Pinterest board) and
what they actually feel confident buying. A customer might
see a high-fashion look on a runway model and love the style
but dismiss it with the thought, "That would never look good
on me," or "I have nothing in my closet to wear with that."
This module can bridge that gap. The process begins when a
user uploads an image of an aspirational garment. The pla t-
form's AI us es computer vision to deconstruct the core style
attributes of the garment —its silhouette, texture, and key
details [62]. Simultaneously, the system accesses the user's
biometric data (from a photo scan) and their digital wardrobe
(from past purchases).
The generative engine then creates a new, unique design.
This design captures the essence of the aspirational look but is
intelligently re-proportioned to flatter the user's specific body
shape. Furthermore, it can be generated in a colour palette that
complements items the user already owns, instantly solving
the "what to wear it with" problem. This transforms the pla t-
form from a simple retailer into a true personal stylist, making
aspirational style immediately accessible and actionable,
thereby increasing purchase confidence, customer satisfaction,
and brand loyalty.
2.4. Advanced Pattern and Fabric Simulation
This final module in the design pillar serves as the critical

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

198
bridge between digital creativity and physical reality. It e n-
sures that AI-generated concepts are grounded in the laws of
physics and are manufacturable before any physical resources
are committed. This validation step is crucial for preventing
the creation of designs that are beautiful on screen but unfe a-
sible or unflattering as physical garments.
The solution is an integrated simulation environment where
designers can test generated patterns for material efficiency
and visualise how different fabrics will drape, stretch, and
move on a realistic 3D avatar. It functions as the final quality
gate of the digital design process, providing confidence in the
manufacturability and aesthetic integrity of a collection.
This environment will be built using the following tec h-
nologies:
1) Pattern Recognition and Validation: The system will
use Computer Vision (CNNs) to analyse the 2D patterns
extracted from AI-generated 3D models. It will ensure
the patterns are coherent, geometrically sound, and can
be translated into viable cutting layouts [11]. As a brand
protection measure, the system can also run visual
similarity matches against a proprietary database of
existing patterns to flag potential intellectual property
infringement before a design goes into production [11].
2) Fabric Physics Simulation: The core of this module is a
sophisticated physics -based rend ering engine that a c-
curately simulates cloth behaviour. This requires
building a comprehensive digital library of fabrics,
where each material is defined by its specific physical
properties (e.g., weight, stiffness, bend resistance,
stretch, and friction). CLO 3D is the established indus-
try standard for this technology, allowing designers to
create true -to-life 3D garments, visualise fit and si l-
houette with high accuracy, and conduct virtual fittings
on customizable avatars [19].
3) Custom Simulation Solutions: For highly specialised or
performance-intensive simulation needs, custom sof t-
ware solutions like Evolve Cloth Simulation can be
developed. Such a system might use Python scripting
within a 3D environment like Blender, combined with
hybrid CPU and GPU processing, to automate and
dramatically accelerate the rendering of complex cloth
physics for large batches of designs [5].
4) 3D Avatar Generation: The simulation environment
will be integrated with technology that can create rea l-
istic, dimensionally accurate 3D avatars of customers
from just a few photos or a set of body measurements.
This enables precise virtual fittings within the simul a-
tion environment, allowing designers to check how a
garment will fit on a variety of body types or even on a
specific client for bespoke orders.
The most profound impact of this module is its creation of a
"digital twin" for each garment. This high -fidelity 3D asset,
finalised in the simulation environment, is not merely a design
tool; it becomes a f oundational element for the entire dow n-
stream value chain. This single asset serves as the single
source of truth, eliminating data silos and a massive duplic a-
tion of effort that plagues traditional workflows. In a trad i-
tional process, a design sketch is m anually interpreted by a
pattern maker, who creates a physical sample. This sample is
then separately photographed for marketing, and its technical
specifications are manually documented for manufacturing, a
sequence of disconnected and often inconsistent steps.
In the proposed system, the AI-generated design is finalised
as a single, high-fidelity 3D model in a platform like CLO 3D.
This same file is then used across departments. The produ c-
tion module (detailed in Part II) can directly extract the 2D
pattern pieces from the 3D model for use in automated cutting
machines. The marketing module (detailed in Part III) uses the
same 3D model to power e -commerce virtual try -on experi-
ences [18], generate limitless photorealistic on-model images
using tools li ke Botika without a physical photoshoot [14],
and create engaging AR filters for social media campaigns.
This "digital twin" approach ensures absolute consistency
from design to marketing, dramatically reduces the cost and
time of asset creation, and accel erates the overall
time-to-market. A design change made to the digital twin is
instantly reflected in the assets available to every other part of
the business.
Table 1. Technology and Technique Matrix for Apparel Design.
Requirement Core AI Technique(s) Key Technologies / Platforms Data Dependencies Success Metrics (KPIs)
Trend
Forecasting
NLP, Computer Vision,
Time-Series Analysis,
Predictive Modelling
Heuritech, WGSN, T-Fashion,
ChatGPT-4, DALL-E 3 API,
TensorFlow (LSTMs)
Social media
text/images, search
queries, e-commerce
sales data, runway
photos
Forecast accuracy > 90%; 50%
reduction in trend research time;
20% increase in full-price
sell-through of trend-led items.
AI
Co-Creation
Generative Adversarial
Networks (GANs),
Diffusion Models, Im-
age-to-Image Transla-
tion
DALL-E 3 API, Midjourney,
Resleeve.ai, VisualHound,
AiDA, Custom Style-
GAN/CycleGAN models
Text prompts, mood
boards, 2D sketches,
trend engine outputs
10x increase in design variations
per brief; 60% reduction in con-
cept-to-visualisation time [2]; 25%
increase in designer-rated novelty
of concepts.

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

199
Requirement Core AI Technique(s) Key Technologies / Platforms Data Dependencies Success Metrics (KPIs)
Hy-
per-Personalis
ation
Collaborative/Content-
Based Filtering,
Computer Vision,
Generative AI
Stitch Fix-style algorithms,
Style DNA, Vue.ai, Custom
CNNs for biometrics
Customer profiles,
purchase/browsing
history, user-submitted
photos, style quizzes
30% reduction in return rates
[47]; 15% increase in customer
retention [66]; 20% increase in
Average Order Value (AOV).
Pattern &
Fabric Simu-
lation
Computer Vision
(CNNs), Physics-Based
Rendering, 3D Model-
ling
CLO 3D, Evolve Cloth Sim-
ulation, Blender, Unity
AI-generated design
files, digital fabric
library with physical
properties
95% reduction in physical sample
production [19]; 50% reduction in
time from design lock to produc-
tion-ready tech pack.

3. Part II: Solution Architecture for
Production and Supply Chain
Optimisation
This part of the blueprint details the technologies required
to build a lean, agile, and sustainable production and supply
chain ecosystem. The goal is to leverage AI to minimise waste,
reduce costs, enhance quality, and create a highly responsive
system that can adapt to the rapid shifts in demand identified
by the design and marketing engines.
3.1. The Material Optimisation and Waste
Reduction System
This system directly confronts pre -consumer waste, a si g-
nificant source of both financial loss and environmental de g-
radation in the apparel industry. Its focus is on optimising the
use of raw mat erials from the moment they enter the factory
through to the final cut, ensuring maximum value is extracted
from every yard of fabric.
The proposed solution is an AI -driven system that aut o-
mates three critical processes: first, the real -time detection of
defects in raw fabric rolls to prevent flawed material from
ever entering the production line; second, the algorithmic
optimisation of cutting patterns to maximise fabric yield; and
third, demand -driven production planning to eliminate the
costly and wasteful practice of overproduction.
The technical components of this system include:
1) Fabric Defect Detection: This involves implementing
Computer Vision  systems, such as those commercia l-
ised by Smartex [74]. High-resolution cameras are i n-
stalled on textile production machinery or inspection
lines. AI models, trained on vast datasets of fabric i m-
ages, analyse the material feed in real -time to detect,
classify, and map defects like stains, holes, tears,
weaving irregularities, or dyeing inconsistencies [59].
By catching these problems at the source, the system
prevents the waste of labour and energy on materials
that would ultimately be discarded. This early detection
can improve fabric yield and has been shown by
Smartex to have prevented millions of kilograms  of
fabric waste [74].
2) Optimised Cutting Layouts (Nesting): To minimise scrap
material during the cutting phase, the system will utilise
advanced optimisation algorithms and machine learning
to solve the computationally complex "nesting problem."
The system takes the 2D shapes of all pattern pieces re-
quired for a production run and calculates the most effi-
cient layout on the fabric roll, fitting them together like a
complex puzzle to minimise the space between them [59].
This automated process can reduce fabric waste by up to
20% compared to manual methods and can save a small
factory tens of thousands of dollars annually [28].
3) Demand Forecasting for Waste Prevention: The system
will be deeply integrated with the demand forecasting
models from the Trend Engine and real-time sales data
from the marketing platform. By producing quantities
that are closely aligned with actual, predicted demand,
the system fundamentally addresses the problem of
overproduction, which is a primary driver of
post-consumer waste, cos tly markdowns, and excess
inventory [54].
A truly intelligent system does not just reduce waste; it
treats waste as a valuable data source, creating a feedback
loop for continuous improvement. The data on the type, fr e-
quency, and location of fabric defects  can be aggregated and
fed back to suppliers, providing objective evidence to i m-
prove raw material quality or negotiate better terms. For
example, suppose the computer vision system consistently
flags a "dye streak" defect in fabric from Supplier A. In tha t
case, it can automatically generate a quality report showing
that this supplier has a 7% higher defect rate for this issue than
Supplier B. This empowers the sourcing team with concrete
data for decision-making.
Similarly, data on cutting scraps can info rm future design
choices. If the nesting algorithm finds that a specific A-line skirt
design consistently results in an 18% scrap rate, this metric is
logged as an attribute of that design. The AI Co-Creation Suite
can then flag this design as "material in efficient" and prompt
designers to consider variations that might nest more efficiently
in future collections. This transforms the system from a simple
cost-saving tool into an intelligent, self -improving ecosystem

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

200
that optimises the entire design-to-production pipeline for both
sustainability and profitability [49].
3.2. Intelligent Supply Chain and Logistics
Orchestration
This module aims to create a predictive, adaptive, and
transparent supply chain, moving beyond the traditional,
reactive model to a "Ju st-In-telligent" system that anticipates
disruptions and optimises flow from end to end [3].
The solution is a centralised platform that provides
end-to-end visibility and predictive control over inventory,
logistics, and supplier performance. It will auto mate and
optimise critical decisions related to stock replenishment,
shipping routes, and warehouse management, ensuring that
the right products are in the right place at the right time.
The enabling techniques and technologies are:
1) Predictive Inventory Management: The system will use
predictive analytics and machine learning  to forecast
demand at a highly granular level—per SKU, per store,
per day. This allows for automated, dynamic inventory
replenishment strategies that significantly reduce the
risk of both stockouts (lost sales) and overstocking
(tied-up capital and waste) [31]. The operational models
of industry leaders like Zara and Nike serve as key
benchmarks. [6] These companies use AI to analyse
real-time sales data, returns information, and regional
trends to tailor merchandise assortments to each store,
maximising sales and minimising markdowns [41].
2) Logistics and Route Optimisation: To enhance eff i-
ciency and reduce environmental impact, the platform
will apply Reinforcement Learning or other advanced
optimisation algorithms to plan the most efficient
transportation routes. The system will analyse a mult i-
tude of variables in real time, including traffic cond i-
tions, weather forecasts, fuel costs, and delivery
schedules, to minimise transportation expenses and
carbon emissions by up to 30% [9, 12].
3) Automated Warehousing : The platform will integrate
with AI-powered robotics and automation systems for
tasks like picking, packing, and sorting within distr i-
bution centres. This is a core component of Nike's di g-
itally-enabled supply chain, which uses over 1,000
"cobots" to red uce labour costs, increase order fulfi l-
ment speed, and improve accuracy [8].
4) Supply Chain Traceability: To meet growing consumer
and regulatory demands for transparency, the system will
implement Blockchain technology. This creates a secure,
immutable, and auditable record of a product's entire
journey, from the sourcing of raw materials to the final
consumer. This technology is instrumental in verifying
sustainability claims, combating counterfeiting, and
building profound consumer trust [67].
A truly intelligent supply chain extends its predictive c a-
pabilities beyond its operations to integrate with its suppliers
dynamically. The platform should not only monitor internal
data but also ingest external data streams —such as news
reports, weather patterns, and shipping lane congestion r e-
ports—linked to key supplier locations. An NLP module
could detect news of a potential labour strike affecting a
primary fabric mill. The system would immediately flag all
production orders  dependent on that mill and calculate the
potential delay. Simultaneously, it would query its database of
pre-vetted secondary suppliers, check their current capacity
and material availability via API, and calculate the cost -time
trade-off of shifting prod uction. It could then present the
supply chain manager with a "Plan B" recommendation:
"High risk of 2 -week delay from Supplier A. Recommend
shifting 40% of Order #123 to Supplier C. Estimated impact:
3-day delay, 4% cost increase. Approve?" This transforms the
supply chain from a fragile, reactive chain of events into a
resilient, proactive, and intelligent network.
3.3. Automated Quality Control and Defect
Management
This module embeds quality control directly into the fabric
of the production line, trans forming it from a manual,
end-of-pipe inspection process into an automated, continuous,
and data-rich system.
The solution consists of a network of high -resolution
cameras integrated at critical points in the garment assembly
process—for example, after major stitching operations,
printing, or embroidery application. A central AI system
analyses the video feeds from these cameras in real -time to
identify and flag manufacturing defects as they occur. [34]
The core technologies driving this module are:
1) Computer Vision for Defect Detection: This is the cen-
tral technology. The system will utilise Convolutional
Neural Network (CNN) -based models trained to ide n-
tify a comprehensive library of garment defects. This
includes stitching errors (e.g., skipped stitches , seam
puckering, incorrect tension), colour inconsistencies,
fabric flaws (e.g., pilling, snags, holes), and misalig n-
ments in prints or embroidery [15]. The accuracy of
these systems can be up to 30% higher than manual
inspection [7, 68].
2) Real-Time Processing and Alerts: The system must
process image data with extremely low latency to keep
pace with high-speed production lines. When a defect is
detected, it triggers an immediate alert to human ope r-
ators via a dashboard or can even signal the production
machinery to stop automatically. This prevents the
creation of a long run of faulty items and allows for
immediate correction [37].
3) Continuous Learning: The system is designed to i m-
prove over time through an active learning loop. When
an operator confirms or corrects a defect flagged by the
AI, this feedback is used to retrain and fine -tune the
model. This process continuously increases the system's

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

201
accuracy and reduces the rate of false positives, making
it more reliable and efficient with every production run
[15]. Specialised solutions in this space, such as De-
fectGuard by Brightpoint AI, offer comprehensive
platforms for this purpose [15].
The data generated by this automated QC system offers
value far beyond simple defect detection; it can be used as a
proxy for machine health to enable predictive maintenance.
For instance, a sudden spike in a specific type of stitching
error—say, a 15% increase in "skipped stitch" d e-
fects—originating from a particular sewing station is a strong
statistical indicator that the machine at that station requires
maintenance, often before it experiences a complete failure.
The system can detect this anomalous pattern, cross-reference
it with a database of known machine failure signatures, and
identify a high corre lation with a specific mechanical issue
like needle misalignment. It can then automatically generate a
maintenance ticket in the factory's management system:
"High probability of needle misalignment at Sewing Station
#7. Proactive inspection recommended." This shifts the fa c-
tory's maintenance strategy from a fixed schedule or a reactive
(after-breakdown) model to a data -driven, predictive one,
which minimises costly production downtime and ensures
more consistent product quality.
3.4. The Sustainability and Circularity
Management Dashboard
This module provides a holistic, data -driven view of the
company's environmental and social impact, providing the
tools to actively manage, improve, and report on sustainability
performance.
The solution is a centralised dashboard that aggregates data
from across the entire platform to track key sustainability
metrics in real time. It will provide tools for product lifecycle
analysis, recommend sustainable material alternatives to d e-
signers, and support circular economy ini tiatives like textile
reuse and recycling.
The key technologies enabling this dashboard include:
1) AI for Lifecycle Analysis (LCA): The system will use AI
models to analyse the complete lifecycle of a garment.
By integrating data from the blockchain -based tracea-
bility system (for raw material origins), production
systems (for energy and water usage), and logistics (for
transportation emissions), it can calculate a detailed
environmental footprint—including carbon emissions,
water usage, and chemical impact —for each product
[57].
2) Sustainable Material Recommendation: The platform
will leverage AI to analyse vast databases of materials,
cross-referencing their performance characteristics with
their sustainability certifications (e.g., GOTS, FSC,
Oeko-Tex). When a designer is selecting a fabric, the
system can automatically suggest more eco -friendly
alternatives that have similar properties in terms of
performance, drape, and feel, making sustainable
choices easier and more accessible [57].
3) AI for Circularity: To support a circular economy, the
system will employ computer vision and AI to automate
the sorting of post-consumer textiles for recycling [29].
Identifying fabric composition (e.g., 100% cotton vs. a
polyester-cotton blend) from an image is a critical and
difficult step for effective recycling, and AI can automate
this process with high accuracy. The system can also
suggest creative ways to repurpose cutting scraps from
the production floor into new products, such as accesso-
ries or patchwork details, minimising waste [44].
The data aggregated in this dashboard can be repurposed for
powerful consumer-facing marketing, turning what is often
seen as a compliance cost centre into a significant revenue
driver and brand differentiator. The platform can automatically
generate a "sustainability score" or a "product passport" for
each garment. For example, the dashboard might calculate that
a specific t-shirt used 30% less water than a conventional one
and was made with 100% organic cotton from a certified
fair-trade farm (with data verified by the blockchain traceability
module). This information can be automatically packaged into
a consumer-friendly format. When a customer scans a QR code
on the garment's tag in -store or online, it could link to a
"Product Passport" webpage. This page would visually display
the garment's journey, its key sustainability metrics, and pe r-
haps even the story of the people who made it. This level of
radical transparency builds immense brand trust and loyalty,
particularly with environmentally conscious consumers, and
can justify a premium price point. It creates a direct, tangible
link between back-end operational improvements and front-end
brand value.
Table 2. Technology and Technique Matrix for Production & Supply Chain.
Requirement Core AI Technique(s) Key Technologies / Platforms Data Dependencies Success Metrics (KPIs)
Material
Optimisation
Computer Vision,
Optimisation
Algorithms, Predictive
Analytics
Smartex, Custom Nesting
Algorithms (e.g., based on
Python libraries)
Fabric roll images, 2D
pattern files, demand
forecasts
15-20% reduction in fabric
waste [28]; 5% reduction in raw
material costs; 25% reduction in
overproduction. [58]
Intelligent Sup- Predictive Analytics, Custom models (emulating Real-time sales data, logis- 20% reduction in inventory

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

202
Requirement Core AI Technique(s) Key Technologies / Platforms Data Dependencies Success Metrics (KPIs)
ply Chain Reinforcement Learn-
ing, Blockchain
Zara/Nike), ERP integration,
Hyperledger/Ethereum
tics data, supplier perfor-
mance, external data
(weather, news)
holding costs [66]; 15% reduc-
tion in shipping costs; 50% im-
provement in forecast accuracy.
Automated
Quality Control
Computer Vision
(CNNs), Real-time
Image Processing
DefectGuard, Custom models
on platforms like Tensor-
Flow/PyTorch
High-resolution video feeds
from production line
30% increase in defect detection
rate [72]; 90% reduction in
manual inspection costs; 10%
reduction in customer returns
due to defects.
Sustainability &
Circularity
AI for LCA, Computer
Vision for Sorting, Rec-
ommendation Engines
Custom dashboards, integra-
tion with Higg Index,
AI-powered sorting tech
Supply chain traceability
data (blockchain), material
properties database,
post-consumer textile images
20% reduction in overall carbon
footprint; 10% increase in use of
recycled materials; achieve
100% supply chain transparency.

4. Part III: Solution Architecture for
Marketing and Customer Engagement
Optimisation
This final part of the blueprint outlines the technologies for
creating a highly efficient, data -driven, and pe rsonalised
marketing and customer experience engine. The objective is
to leverage AI to understand and engage customers on an
individual level, automate content creation at scale, and create
immersive shopping experiences that drive both loyalty and
sales.
4.1. The Personalised Marketing and Dynamic
Campaign Engine
This engine forms the core of the customer-facing strategy,
enabling a shift from traditional, broad -stroke marketing
segmentation to true hyper-personalisation at scale.
The solution is a system  that analyses a unified customer
profile to deliver personalised product recommendations,
marketing messages, and dynamic offers across all channels,
including email, website, mobile app, and social media. This
ensures that every customer interaction is r elevant and val u-
able.
The key techniques and technologies include:
1) AI-Powered Personalisation Engine: The platform will
build a sophisticated recommendation system inspired
by the pioneering work of Stitch Fix [62]. This involves
creating a "Latent Style" algorithm that synthesises
both explicit data (from style quizzes and user profiles)
and implicit data (browsing history, purchase patterns,
items added to cart) to develop a deep, nuanced unde r-
standing of each customer's unique style DNA. [61].
This engine will power personalised product carousels
on the website, "complete the look" suggestions based
on past purchases, and dynamic, individually curated
email content.
2) Customer Data Platform (CDP): The implementation
of a CDP is a foundational pr erequisite. This platform
will ingest and unify customer data from all touc h-
points—e-commerce transactions, in -store visits, app
usage, social media interactions, customer service
calls—into a single, persistent, and actionable profile
for each customer.
3) Dynamic Pricing and Promotions: The engine will use
AI algorithms to adjust prices or generate personalised
promotions dynamically. These adjustments will be
based on a real -time analysis of factors like product
demand, inventory levels, competitor pricing,  and an
individual customer's price sensitivity and purchase
history. This capability has been shown to increase
revenues by up to 10% and gross margins by 5% [17].
4) Targeted Campaign Automation: The platform will
leverage AI to analyse the customer base, i dentify mi-
cro-segments, and create highly targeted advertising
campaigns for platforms like Facebook and Instagram.
This data-driven approach significantly improves return
on ad spend (ROAS) by reducing wasted expenditure
on irrelevant audiences [17].
The engine's strategic value lies in its ability to be proactive
and lifecycle-aware, not just reactive. By modelling the cu s-
tomer lifecycle, it can anticipate needs and trigger persona l-
ised interactions at key moments of transition. A standard
personalisation engine recommends products based on past
behaviour. [56] A more advanced engine, like that of Stitch
Fix, understands a customer's latent style. However, a truly
proactive engine models the customer's state. It recognises
subtle shifts in browsing behavio ur that signal a significant
life event.
For example, the system might detect that a customer's
browsing patterns are shifting from "business casual" and
"evening wear" to "athleisure" and "maternity clothes." It can
infer a potential lifestyle change, suc h as a pregnancy or a
shift to remote work. Instead of merely showing more of the
newly browsed categories, it can trigger a highly personalised

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

203
and empathetic marketing campaign: "Your Style is Evolving.
Discover our new 'Comfort & Play' collection, perfe ct for
your next chapter." This demonstrates a deep understanding
of the customer's life journey, fostering a much stronger
emotional connection and brand loyalty than simple product
recommendations ever could.
4.2. The Automated Content Generation Engine
This module directly addresses the immense operational
challenge of creating high -quality, on-brand marketing co n-
tent at the scale required for hyper -personalisation. [23] It is
not feasible for human teams to write unique product d e-
scriptions or social media posts for thousands of products and
millions of individual customers.
The solution is a generative AI tool for the automated cr e-
ation of a wide array of marketing assets, including compe l-
ling product descriptions, engaging social media captions,
SEO-optimised blog posts, and personalised email copy.
The core techniques are:
1) Natural Language Generation (NLG): The system will
utilise large language models (LLMs) specifically for
text generation. The key to success is moving beyond
generic, public models like the standard ChatGPT.
2) Fine-Tuning LLMs: The most critical technique is to
fine-tune a powerful base model (such as GPT -4 or
Microsoft's T-NLG [16]) on the company's proprietary
data. This involves creating a high-quality dataset of the
brand's best-performing marketing copy, most effective
product descriptions, and comprehensive style guides.
By training on this data, the fine-tuned model learns the
brand's specific voice, tone, terminology, and stylistic
nuances, enabling it to generate new content t hat is
consistently and authentically on-brand [26].
3) Multi-Modal Generation: The engine's capability will
extend beyond text to the generation of visual content.
The system can take a single product image (or a 3D
digital twin) and automatically generate a  multitude of
on-model lifestyle shots using tools like Botika [14] or
Modelia [50]. This allows the creation of diverse ma r-
keting imagery featuring different models, backgrounds,
and poses without the need for physical photoshoots. It
can even be used to create entire artistic campaign
visuals in collaboration with AI artists, as seen with
brands like Casablanca Paris [45].
This NLG engine provides a powerful solution to the "cold
start" problem in e -commerce—marketing a brand -new
product that has no sales history, customer reviews, or u s-
er-generated content. When a new dress is added to the i n-
ventory with only basic technical specifications, the NLG
engine can instantly generate a rich set of marketing assets. It
receives the product attributes (fabric: silk; colour: emerald
green; silhouette: A-line; details: puff sleeves) and the target
"StyleFile" (e.g., "Romantic," "Classic "). The fine -tuned
model then generates a compelling, on -brand product d e-
scription: "Float through your next garden party in our 'E s-
meralda' dress. Crafted from lustrous emerald silk, its timeless
A-line silhouette is given a touch of modern romance with
delicate puff sleeves..." Simultaneously, it can generate five
different social media captions, each targeting a different
angle (e.g., sustainability, event dressing, styling tips) and
suggest relevant hashtags. This instantly populates the pro d-
uct page an d marketing channels with rich, SEO -friendly
content, allowing the new product to be discovered and sold
without the typical lag time.
4.3. The Unified Consumer Insights Platform
This module acts as the central nervous system for the
marketing organisation , providing a real -time, 360 -degree
view of the market, competitors, and consumer sentiment. It
aggregates disparate data streams into a single source of truth
for strategic decision-making.
The solution is a central analytics hub that integrates data
from marketing campaigns, social media platforms, customer
service interactions, and sales channels. It will use AI to a u-
tomatically surface actionable insights and trends, providing a
crucial feedback loop to the design, production, and marke t-
ing engines.
Key technologies include:
1) NLP for Sentiment Analysis: The platform will apply
advanced NLP algorithms to analyse unstructured text
from customer reviews, social media comments, and
chatbot transcripts. This will allow the system to qua n-
tify consumer sentiment  towards the brand, specific
products, and marketing campaigns, identifying areas
of strength and weakness [20].
2) Real-Time Analytics and Visualisation: The hub will
use business intelligence tools like Tableau or Power BI,
enhanced with AI -driven insights,  to create dynamic
dashboards. These dashboards will track key perfo r-
mance indicators (KPIs) in real time, allowing marke t-
ers to monitor campaign performance and make agile
adjustments.
3) Competitive Intelligence: The platform will leverage AI
to continuously monitor competitors' marketing activ i-
ties, pricing strategies, new product launches, and
consumer sentiment. It will provide automated alerts
and comparative analysis, ensuring the brand remains
competitive. Platforms like T-Fashion (TrendGenius)
offer s pecialised services in this area, providing cu s-
tomised analytics and AI -generated recommendations
based on a comprehensive view of the market [50].
4.4. Conversational AI for Enhanced Customer
Experience
This module provides scalable, 24/7, and personalise d
customer support and styling advice, transforming customer
service from a cost centre into a loyalty -building and rev e-

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

204
nue-generating function.
The solution is an integrated system of AI -powered chat-
bots and virtual stylists capable of handling a wide spe ctrum
of customer interactions, from simple order tracking and
return processing to complex, nuanced styling queries.
The enabling technologies are:
1) NLU-Powered Chatbots: The platform will implement
advanced chatbots that use Natural Language Unde r-
standing (NLU) to comprehend user intent, not just
isolated keywords. This allows for more natural, h u-
man-like, and effective conversations [40]. Leading
chatbot platforms like Yep AI  have demonstrated si g-
nificant success in the fashion space, with case studies
showing they can resolve up to 70% of inquiries aut o-
matically while achieving customer satisfaction rates
over 90% [73].
2) Integration with Personalisation Engine: To be truly
effective, the chatbot must be deeply integrated with the
customer's unified profile  in the CDP and the perso n-
alisation engine. It must have real -time access to the
customer's purchase history, browsing behaviour, and
style preferences to provide genuinely tailored product
recommendations and styling advice [13].
3) Seamless Human Handoff: The system will be arch i-
tected for a smooth and intelligent handoff to a human
agent when dealing with complex, sensitive, or high-value
issues. The full conversation history and customer profile
will be instantly provided to the human agent, ensuring a
seamless and context-aware transition.
4.5. Virtual Prototyping for Immersive
Marketing
This module leverages the 3D "digital twin" assets created
in the design phase to create highly engaging and effective
marketing experiences. These experiences not only c aptivate
customers but also provide them with the confidence to pu r-
chase, significantly reducing return rates.
The solution is a pipeline for deploying the digital twin of
each garment as an interactive marketing asset. This includes
virtual try-on (VTO) o n e-commerce product pages, AR fi l-
ters for social media, and AI-generated on-model imagery for
campaigns. [43]
The key technologies are:
1) 3D Rendering and Augmented Reality (AR): The
high-fidelity 3D models (e.g., from CLO 3D) serve as
the basis for VTO exp eriences. By using WebAR
technology, these experiences can be made accessible
directly in a user's mobile browser, eliminating the
friction of requiring an app download [18]. Advanced
Computer vision and machine learning  algorithms are
essential for accura tely tracking the user's body in r e-
al-time and overlaying the virtual garment realistically,
accounting for movement and drape [18]. The adoption
of such immersive visualisation has been shown to r e-
duce returns by up to 40% [10].
2) AI-Generated On -Model Imag ery: The platform will
integrate with services like Botika [14] or ZMO.ai. [53].
These services can take a flat product photo or, more
powerfully, the 3D digital twin, and generate an u n-
limited number of hyper -realistic, on -model images.
This allows the brand to showcase products on a diverse
range of models, in various poses, and against multiple
backgrounds, all without the immense cost and logi s-
tical complexity of traditional photoshoots.
3) Virtual Showrooms and Events: The same 3D assets
can be used to create fully immersive virtual fashion
shows or digital showrooms, allowing brands to reach a
global audience and create memorable brand exper i-
ences, as has been explored by companies like H&M
[39].
The virtual try -on feature is more than just a conversion
tool; it is a powerful data collection engine that creates a
virtuous cycle, or "flywheel." Every time a user virtually
"tries on" an item, they are generating a rich stream of data
about fit preference, style combinations, and purchase intent.
This data is a goldmine that can be fed back into the perso n-
alisation and design engines. For example, if a user virtually
tries on five different dresses, spends the most time viewing
Dress A, and pairs it with a specific pair of shoes (another
VTO item) but ultima tely does not purchase, the system
captures this entire interaction.
This data enriches the user's profile; the personalisation
engine learns that they are drawn to the style of Dress A and
that they see it as compatible with those particular shoes. This
can trigger a proactive follow-up, such as a personalised email
an hour later: "Still thinking about this look? Here are two
other dresses with a similar silhouette you might love." When
aggregated across thousands of users, this data reveals po w-
erful insights. It can identify which items are frequently tried
on but not purchased, signalling potential issues with price,
description, or perceived fit that the merchandising team can
then address. It also uncovers popular but unexpected outfit
combinations that can inform future styling guides and ma r-
keting campaigns, creating a powerful, self -improving feed-
back loop.

Table 3. Technology and Technique Matrix for Marketing & Customer Engagement.
Requirement Core AI Technique(s) Key Technologies / Platforms Data Dependencies Success Metrics (KPIs)
Personalised Recommendation Custom "Latent Style" models Unified customer 40% increase in AOV [66]; 15% lift

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

205
Requirement Core AI Technique(s) Key Technologies / Platforms Data Dependencies Success Metrics (KPIs)
Marketing Engines, AI-driven
Segmentation,
Dynamic Pricing
(Stitch Fix-style), CDP, AI
pricing tools
profiles, behavioural
data, sales history
in customer retention [66]; 25%
increase in campaign conversion
rates.
Automated
Content Gen
Natural Language
Generation (NLG),
Fine-Tuned LLMs,
Generative Vision
Fine-tuned GPT-4/T-NLG,
Botika, Modelia, DALL-E 3
API
Brand style guides,
historical marketing
copy, product imag-
es/attributes
80% reduction in time to create
product descriptions; 50% reduction
in content creation costs; 90% cost
savings on model photography. [14]
Consumer
Insights
NLP for Sentiment
Analysis, Real-time
Analytics
T-Fashion, Custom dashboards
(Tableau/Power BI with AI)
Social media data,
customer reviews,
chatbot logs, sales data
95% accuracy in sentiment classifi-
cation; 50% faster identification of
emerging market trends; real-time
campaign performance tracking.
Conversational
AI
Natural Language Un-
derstanding (NLU),
Generative AI Chatbots
Yep AI, other advanced chatbot
platforms with CRM integra-
tion
Customer service logs,
product catalog, cus-
tomer profiles
70% automated resolution of customer
queries [73]; 30% reduction in custom-
er service operational costs [51]; 90%+
customer satisfaction score. [73]
Virtual Proto-
typing
3D Rendering, Aug-
mented Reality (AR),
Computer Vision
CLO 3D, WebAR SDKs,
Botika, ZMO.ai
3D "digital twin" gar-
ment files, user camera
feed
40% reduction in return rates [10]; 30%
increase in conversion for products
with VTO [17]; 90% reduction in
physical sample photography costs.

5. Part IV: Strategic Implementation and
Integration Roadmap
A platform of this scope and complexity cannot be built as a
single, monolithic project. A strategic, phased implementation is
critical for managing risk, demonstrating value incrementally,
and ensuring successful adoption across the organisation. The
roadmap is designed to deliver tangible wins at each stage,
building momentum for subsequent, more complex integrations.
5.1. Phase 1: Foundational Data and Core
Insights (Months 1-6)
The initial phase focuses on establishing the essential data
infrastructure and launching high -impact, low -dependency
modules that can provide immediate value and demonstrate
the potential of AI.
1) Actions:
a. Implement a Customer Data Platform (CDP) : The
first and most critical  step is to unify all existing
customer data from e -commerce, retail, and marke t-
ing channels into a single source of truth. This is the
non-negotiable prerequisite for all future personal i-
sation efforts.
b. Deploy the Trend Forecasting Engine: Concurrently,
the platform will begin ingesting and analysing public
data from social media, search trends, and fashion
media. This will generate initial trend reports that can
provide immediate value to the design and mercha n-
dising teams, helping them validate their int uition
with data.
c. Pilot Automated Quality Control on a Single Produc-
tion Line: To demonstrate clear and measurable ROI, a
pilot program using a vendor solution like Defec t-
Guard [15] should be implemented on one production
line. The goal is to prove the bus iness case through
quantifiable reductions in fabric waste and improv e-
ments in final product quality.
2) Strategic Rationale : This phase adheres to the "think
big, start small, and iterate often" framework [52]. By
securing early wins in areas with clear, measurable
ROI, such as waste reduction, the project can build
crucial momentum and secure executive buy -in for
the more complex and capital -intensive phases to
follow.
5.2. Phase 2: Generative Design and
Personalisation (Months 7-18)
With the data foundation in place, the second phase focuses
on building out the creative and customer -facing generative
tools that form the core of the platform's innovative offering.
1) Actions:
a. Develop the AI Co -Creation Suite : Integrate
text-to-image and sketch -to-image tools to create a
functional co-pilot for the design team, accelerating
their ideation and visualisation processes.
b. Launch the Personalisation Engine: Begin with foun-
dational personalisation features powered by the CDP.
This includes deploying personalised product recom-

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

206
mendation carousels on the e-commerce site and creat-
ing dynamic, personalised email marketing campaigns.
c. Introduce Virtual Prototyping : Begin the process of
creating 3D digital twins for a single, high -volume
product category. Deploy a virtual try-on (VTO) pilot
for this category to test the technology and gather user
feedback.
2) Strategic Rationale: As the platform begins to use and
generate more sensitive customer data, including style
preferences and potentially biometric information, es-
tablish ing robust data governance, privacy, and
security protocols is paramount. Building and
maintaining consumer trust is critical for the
long-term success of any personalisation strategy
[46].
5.3. Phase 3: Full Value Chain Integration
(Months 19-36)
The fina l phase focuses on connecting all the individual
modules into a seamless, self-improving, and fully integrated
ecosystem that spans the entire value chain.
Table 4. AI in Action: Industry Case Study Snapshot.
Company Primary AI Application Area Key Technologies & Strategies Reported Outcomes / Key Differentiators Source
Zara Supply Chain & Inventory Optimisation AI-driven demand forecasting, RFID tags, Real-time analytics, AMPL for optimisation "Just-In-telligent" supply chain; 1-week design-to-store turnaround; Optimised store-level inventory. [25]
Stitch Fix Hyper-Personalisation & Styl- ing
"Latent Style" algorithms, NLP on
customer feedback, Hu-
man-in-the-loop styling, "StyleFile"
profiles
Data-driven personal styling at scale; 30%
reduction in returns; 15% boost in reten-
tion.
[75]
H&M Customer Engagement & Trend Adoption AI chatbots, AI-driven personalisa- tion, Generative AI for marketing imagery, Investment in Smartex 30% increase in customer engagement; Use of digital twins for creative cam- paigns; Proactive waste reduction. [6]
Nike D2C Strategy & Supply Chain Automation
AI for demand forecasting, Robot-
ics ("cobots") in warehouses, AR
for virtual try-on (Nike Fit),
Blockchain for traceability
"Consumer Direct Acceleration";
AI-driven inventory positioning; Enhanced
D2C personalisation.
[24]
Smartex Production Waste Reduction Computer Vision, AI-powered de- fect detection cameras Prevents fabric waste at the source; Claims to have saved 1 million kg of fabric; Backed by H&M and Amazon. [74]

1) Actions:
a. Deploy the Intelligent Supply Chain System: Integrate
the demand forecasts from the trend and marketing
engines with the inventory and logistics optimis a-
tion systems to create a truly demand -driven supply
chain.
b. Roll out Hyper -Personalisation: Expand beyond
recommendations to use customer data for the ge n-
eration of personalised designs and custom -fit ga r-
ment options, offering a truly bespoke service.  [48,
63].
c. Integrate all Feedba ck Loops : The final and most
crucial step is to ensure that all data flows are bid i-
rectional. Data from marketing (e.g., VTO engag e-
ment rates), production (e.g., waste data, defect rates),
and customer service (e.g., chatbot logs) must be fed
back into the  design and forecasting engines. This
creates a true learning system that continuously o p-
timises itself.
d. Strategic Rationale: The ultimate goal of this int e-
grated platform is to create a symbiotic relationship
between human expertise and machine intelligen ce
[27]. The AI systems are designed to handle scale,
complex data processing, and initial content gener a-
tion, freeing up human designers, stylists, and strat e-
gists to focus on the tasks they do best: creativity,
empathy, strategic thinking, and building genuine
customer relationships. [1, 36] The platform is a tool
to augment, not replace, human talent.
Abbreviations
2D Two Dimensional
3D Three Dimensional
AI Artificial Intelligence

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

207
AOV Average Order Value
API Application Programming Interface
AR Augmented Reality
CDP Customer Data Platform
CGAN Conditional Generative Adversarial Network
CNN Convolutional Neural Network
CRM Customer Relationship Management
CV Computer Vision
FSC Forest Stewardship Council
GAN Generative Adversarial Network
GOTS Global Organic Textile Standard
LCA Lifecycle Analysis
LLM Large Language Model
LSTM Long Short-Term Memory
NLG Natural Language Generation
NLP Natural Language Processing
NLU Natural Language Understanding
QC Quality Control
RFID Radio Frequency Identification
ROAS Return on Ad Spend
ROI Return on Investment
SDK Software Development Kit
SKU Stock Keeping Unit
VTO Virtual Try On
Y2K Year 2000
Author Contributions
Partha Majumdar is the sole author. The author read and
approved the final manuscript.
Conflicts of Interest
The author declares no conflicts of interest.
References
[1] 383 Design Studio  (2025). NewArc AI's NEW FEATURE is a
TOTAL Gamechanger for Fashion Designers.
https://www.youtube.com/watch?v=VT4xLEY_bX0
[2] AiDA (n.d.). AiDA - Code-Create. Retrieved July 25, 2025,
from https://code-create.com.hk/aida/
[3] AIX (2023, September 23). Case Study: Zara’ s Comprehen-
sive Approach to AI and Supply Chain Management . R e-
trieved July 25, 2025, from
https://aiexpert.network/case-study-zaras-comprehensive-appr
oach-to-ai-and-supply-chain-management/
[4] Alta (n.d.). Your personal AI stylist that truly gets you . R e-
trieved July 25, 2025, from https://www.altadaily.com/
[5] Aman, M. (n. d.). Evolve Cloth Simulation | AI -Powered Dig-
ital Fashion & Cloth Physics . Retrieved July 25, 2025, from
https://www.mominaman.com/evolve-cloth-simulation.html
[6] AMPL (n.d.). Zara Case Study: Mastering Fashion with O p-
timized Supp ly Chains . Retrieved August 22, 2025, from
https://ampl.com/solutions/customers-and-case-studies/case-st
udy-with-zara-mastering-fashion-with-optimized-supply-chai
ns/
[7] API4 (2024, December 20). Transforming Quality Control
with Computer Vision . Retrieved Jul y 25, 2025, from
https://medium.com/@API4AI/transforming-quality-control-
with-computer-vision-aeca6613e267
[8] Apparel Robotics (n. d.). The next step in automated, flexible,
apparel manufacturing. Retrieved July 25, 2025, from
https://www.apparelrobotics.com/
[9] Arora, N., Anant, B. C., & Chaudhary, K. (2023, October 10).
Optimizing Supply Chains in the Fashion & Textile Industry
through AI. Retrieved July 25, 2025, from
https://www.researchgate.net/publication/381109666_Optimiz
-ing_Supply_Chains_in_the_Fashion_Textile_Industry_throu
gh_AI_AI_and_the_Fashion_Industry
[10] Augmented and Virtual Reality (2025, February 3). How
Augmented Reality (AR) Impacts the Fashion Industry . R e-
trieved July 25, 2025, from
https://hqsoftwarelab.com/blog/augmented-reality-in-fashion/
[11] Banerjee, P. (2023, October 27). Refashioning the Fashion
Landscape: Harnessing the Potential of Computer Vision and
AI. Retrieved July 25, 2025, from
https://fractal.ai/article/reshaping-fashion-with-computer-visio
n-and-ai
[12] Baukh, O. (2024, September 11). The Role of AI in Optimizing
Supply Chain Management in the Fashion Industry. Retrieved
July 25, 2025, from
https://techpacker.com/blog/design/how-artificial-intelligence-
is-revolutionizing-the-fashion-industry/
[13] Borreani, L. (2024, October 2). A Real-Life Use Case: How AI
Chatbots Are Being Used in the Fashion E -Commerce Indus-
try. Retrieved July 25, 2025, from
https://zipchat.ai/post/why-integrate-an-ai-chatbot-on-your-fas
hion-brand-e-commerce-store
[14] Botika (n.  d.). AI generated models for fashion . Retrie ved
July 25, 2025, from https://botika.io/
[15] brightpoint.ai (n. d.). AI-Powered Garment Defect Detection for
Quality Control and Cost Savings. Retrieved July 25, 2025, from
https://www.brightpoint.ai/post/ai-powered-garment-defect-detect
ion-for-quality-control-and-cost-savings
[16] Choudhury, D. (2020, February 13). Turing-NLG: A
17-billion-parameter language model by Microsoft. Microsoft.
Retrieved July 25, 2025, from
https://www.microsoft.com/en-us/research/blog/turing-nlg-a-1
7-billion-parameter-language-model-by-microsoft/
[17] Choudhury, D. (n.d.). How AI and ML are revolutionising
virtual marketing & advertising for fashion brands . Retrieved
July 25, 2025, from
https://www.infosysbpm.com/blogs/bpm-analytics/how-ai-and
-ml-are-revolutionising-virtual-marketing-advertising-for-fash
ion-brands.html

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

208
[18] Claudio (2025, June 10). AR Clothing: The Future of Fashion
Retail and Virtual Try -Ons. Retrieved July 25, 2025, from
https://yordstudio.com/how-ar-clothing-is-making-fashion-ret
ail-evolve/
[19] CLO (n.d.). 3D Fashion Design Software . Retrieved July 25,
2025, from https://www.clo3d.com/
[20] Cogent Infotech (n.d.). How NLG Can Help You in Digital
Marketing. Retrieved July 25, 2025, from
https://www.cogentinfo.com/resources/how-nlg-can-help-you-
in-digital-marketing
[21] Constructor Team (2025, May 22). How to Use AI for Fashion
& Apparel Trend Forecasting. Retrieved July 25, 2025, from
https://constructor.com/blog/using-ai-for-fashion-and-apparel-
trend-forecasting
[22] DasGupta, G. (2025). FashionGAN: Revolutionizing Fashion
Design with Generative Adversarial Networks. Journal Of
Technology, 14(9).
https://technologyjournal.net/wp-content/uploads/1-JOT1353.
pdf
[23] Data Science Salon (n.d.). How Stitch Fix uses AI to predict
what style a customer will love. Retrieved July 25, 2025, from
https://roundtable.datascience.salon/how-stitch-fix-uses-ai-to-
predict-what-style-a-customer-will-love
[24] designveloper (2025, June 21). Nike Digital Transformation:
A Case Study of Modern  Commerce. Retrieved July 25, 2025,
from
https://www.designveloper.com/blog/nike-digital-transformation/
[25] digitaldefynd (2025). 7 Ways Zara is Using AI. Retrieved July
25, 2025, from
https://digitaldefynd.com/IQ/ways-zara-using-ai/
[26] Duan, T. (2023, March 6) . A New Era of Creativity: E x-
pert-in-the-loop Generative AI at Stitch Fix . Stitch Fix. R e-
trieved July 25, 2025, from
https://multithreaded.stitchfix.com/blog/2023/03/06/expert-in-
the-loop-generative-ai-at-stitch-fix/
[27] Duboe, M. (n.d.). How Stitch Fix Uses Data Science and
Machine Learning to Deliver Personalization at Scale . R e-
trieved July 25, 2025, from
https://etailwest.wbresearch.com/blog/how-stitch-fix-uses-dat
a-science-and-machine-learning-to-deliver-personalization-at-
scale
[28] everlighten (2024, Septemb er 7). How AI -powered Fa b-
ric-Cutting Can Help You Save up to $100,000 for Your Small
Garment Factories and Brands?  Retrieved July 25, 2025,
from
https://everlighten.com/blogs/blog/how-ai-powered-fabric-cut
ting-can-help-you-save-up-to-100-000-for-your-small-garmen
t-factories-and-brands
[29] Faghih, E., Saki, Z., & Moore, M. (2025, May 8). A System-
atic Literature Review —AI-Enabled Textile Waste Sorting .
Retrieved July 25, 2025, from
https://www.mdpi.com/2071-1050/17/10/4264
[30] Gehlot, A. (2025, April 2). AI Fashion Trend Forecasting:
Revolutionizing the Retail Industry . Retrieved July 25, 2025,
from
https://medium.com/@apoorv-gehlot/ai-fashion-trend-forecast
ing-revolutionizing-the-retail-industry-c0cab5978e7d
[31] Ginsberg, B. (n.d.). The Role of AI in Optimizing Supply
Chain Management in the Fashion Industry . Retrieved July
25, 2025, from
https://apparelmagic.com/the-role-of-ai-in-optimizing-supply-
chain-management-in-the-fashion-industry/
[32] Gruter, L. (n.d.). AI and Fashion Forecasting: A New A p-
proach to Predicting Tren ds. Retrieved July 25, 2025, from
https://www.xyzparis.xyz/blog/ai-and-fashion-forecasting-a-n
ew-approach-to-predicting-trends
[33] Heuritech (n.d.). Heuritech: Fashion trend forecasting &
prediction with AI. Retrieved July 25, 2025, from
https://heuritech.com/
[34] High, M. (2025, May 19). Smartex: Transforming Textile
Manufacturing With AI. Retrieved July 25, 2025, from
https://manufacturingdigital.com/news/how-smartex-h-m-ama
zon-are-using-ai-to-cut-fashion-waste
[35] Imprint Connect (2025, June 6). Custom Apparel in the Age of
AI: What You Need to Know . Retrieved July 25, 2025, from
https://imprintconnect.com/blogs/news/custom-apparel-age-ai
[36] Inside Fashion (2024, October 1). Chatbots and Virtual Sty l-
ists: Fashion’ s New Customer Support Tech. Retri eved July
25, 2025, from
https://www.purelondon.com/pure-london-blog/chatbots-virtu
al-stylists-fashions-new-customer-support-tech
[37] Jain, P. (2025, June 20). How Computer Vision Can Improve
Quality Control in Manufacturing . Retrieved July 25, 2025,
from
https://webmobtech.com/blog/computer -vision -quality -co
ntrol -manufacturing/
[38] Jung, J., Kim, H., & Park, J. (2025, January 7). Deep Fashion
Designer: Generative Adversarial Networks for Fashion Item
Generation Based on Many -to-One Image Translation . R e-
trieved July 25, 2025, from
https://www.mdpi.com/2079-9292/14/2/220
[39] Kang, J. (2025, August 21). Top Examples of Augmented R e-
ality (AR) in Fashion Retail. Retrieved August 22, 2025, from
https://www.netguru.com/blog/augmented-reality-fashion-reta
il-examples
[40] Kaput, M . (2024, February 28). Natural Language Gener a-
tion (NLG): Everything You Need to Know. Retrieved July 25,
2025, from
https://www.marketingaiinstitute.com/blog/the-beginners-guid
e-to-using-natural-language-generation-to-scale-content-mark
eting
[41] Lakshmi, A. (2024, November 15). Case Study 1: H&M’s
Product Personalization and AI . Retrieved July 25, 2025,
from
https://assets.nextleap.app/submissions/HMCASESTUDY-a9
a1a010-651b-49e4-b667-a2103e16b244.pdf

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

209
[42] Majumdar, P. (2025, July 12). Strength Focused AI Integr a-
tion: A Dharmic Approach to Human -Machine Harmony. Re-
trieved July 25, 2025, from
https://www.researchgate.net/publication/393843541_Strengt
h_Focused_AI_Integration_A_Dharmic_Approach_to_Huma
n-Machine_Harmony
[43] Mattan, M. (2025, January 15). Augmented Reality in Fashion:
Transforming Retail with AR Mirrors and Virtual Try -Ons.
Retrieved July 25, 2025, from
https://www.brandxr.io/augmented-reality-in-fashion-transfor
ming-retail-with-ar-mirrors-and-virtual-try-ons
[44] Milano Unica (2024, May 2). Artificial intelligence and su s-
tainability in the textile industry . Retrieved July 25, 2025,
from
https://www.milanounica.it/en/artificial-intelligence-and-susta
inability-in-the-textile-industry
[45] Min, Y. W. O., & Jin, B. E. (2024, June 3). Here’s How the
Fashion Industry Is Using AI. Retrieved July 25, 2025, from
https://textiles.ncsu.edu/news/2024/06/heres-how-the-fashion-
industry-is-using-ai/
[46] Mirror Size (n.d.). Custom Fits in Clicks: AI's Role in
Made-to-Measure Apparel. Retrieved August 22, 2025, from
https://www.mirrorsize.com/blogs/custom-fits-in-clicks-ais-ro
le-in-made-to-measure-apparel
[47] Muritala, A. (2025, April 12). The Rise of H y-
per-Personalisation in Fashion: How AI and Digital Tools
Are Transforming Custom Clothing . Retrieved July 25, 2025,
from
https://www.fibre2fashion.com/industry-article/10382/the-gro
wing-demand-for-hyper-personalisation-in-fashion-how-ai-an
d-digital-design-tools-are-enabling
[48] Neuron Expert (n.d.). Revolutionizing Retail: AI -Driven Per-
sonalization at Stitch Fix . Retrieved July 25, 2025, from
https://neuron.expert/news/stitch-fix-taps-ai-to-redefine-its-bu
siness-model-and-the-consumers-wardrobe/10704/en/
[49] Pattnaik, S. (n.d.). Gen AI: A Game Changer For Sustainable
Fashion? Retrieved July 25, 2025, from
https://www.palo-it.com/en/blog/gen-ai-game-changer-for-sus
tainable-fashion
[50] Perez, C. (2024, December 17). Best AI Tools for Apparel and
Fashion Brands in 2025 . Retrieved July 25, 2025, from
https://modelia.ai/blog/ai-tools-for-apparel
[51] Potor, M. (2025, February 13). AI chatbots in e -commerce:
Advantages, examples, and tips for companies . Retrieved
August 22, 2025, from
https://sinch.com/blog/ai-chatbots-in-e-commerce/
[52] Puckett, M. (2025, June 30). Why People – Not Just AI – Are
Your Greatest Fashion Supply Chain Advantage . Retrieved
August 22, 2025, from
https://www.cgsinc.com/blog/why-people-not-just-ai-are-your
-greatest-fashion-supply-chain-advantage
[53] RealSpace3D (n.d.). Top 10 AI -Powered Fashion Designer
Tools Shaping the Future of Fashion. Retrieved July 25, 2025,
from
https://www.realspace3d.com/blog/top-10-ai-powered-fashion
-designer-tools-shaping-the-future-of-fashion/
[54] refabric (2025, March 7). AI-Powered Minimalism: How
Fashion AI is Leading the Zero -Waste Movement . Retrieved
July 25, 2025, from
https://blog.refabric.com/fashion-ai-minimalism-zero-waste/
[55] Resleeve (n.d.). Best AI Fashion Design Generator | AI
For Designers . Retrieved July 25, 2025, from
https://resleeve.ai/
[56] Resleeve AI (n.d.). How Does Personalized Apparel Design
Work with AI? Retrieved July 25, 2025, from
https://resleeve.ai/personalized-apparel-design/
[57] Rohil, A. (n.d.). AI in Fashion: How AI Can Revolutionize
Sustainability of Fashion?  Retrieved July 25, 2025, from
https://carbontrail.net/blog/how-ai-can-revolutionize-sustaina
bility-of-fashion/
[58] Rosenthal, B., Federowski, R., Wu, E., & Leong, C. (2024).
From waste to worth - Using technology and AI to drive su s-
tainability and waste reduction in the fashion value chain .
Roland Burger. Retrieved July 25, 2025, from
https://www.rolandberger.com/publications/publication_pdf/R
oland-Berger_From-waste-to-worth_Fashion.pdf
[59] scip (n.d.). AI in Textile Manufacturing: Enhancing Efficiency
and Sustainability. Retrieved July 25, 2025, from
https://www.scip.org/news/674390/AI-in-Textile-Manufacturi
ng-Enhancing-Efficiency-and-Sustainability-.htm
[60] Singsit, J. (2025, July 21). Study explores Gen AI’s potential in
fashion design, trend forecasting. Retrieved July 25, 2025, from
https://www.just-style.com/news/ai-fashion-study-forecasting/
[61] Stitch Fix (2022, June 14). Behind the Seams: Integrating our
algorithms to create personalized, dynamic shoppable emails .
Retrieved July 25, 2025, from
https://newsroom.stitchfix.com/blog/dynamic-shoppable-emails/
[62] Stitch Fix (n.d.). Algorithm Tour . Retrieved July 25, 2025,
from https://algorithms-tour.stitchfix.com/
[63] Stitch Fix (n.d.). About Us: Our Start and Company Values .
Retrieved July 25, 2025, from
https://www.stitchfix.com/about
[64] Style DNA (n.d.). Your Personal AI Stylist App . Retrieved
July 25, 2025, from https://styledna.ai/
[65] T-Fashion (n.d.). T-Fashion | Fashion Trend Forecasting
Platform | See What's Next . Retrieved July 25, 2025, from
https://tfashion.ai/
[66] tacticone (2025, January 17). Stitch Fix: Revolutionizing R e-
tail with Generative AI. Retrieved July 25, 2025, from
https://www.tacticone.co/blog/stitch-fix-revolutionizing-retail
-with-generative-ai
[67] Talonic (n.d.). AI for Fashion Data Analytics: Sustainable
Supply Chains. Retrieved July 25, 2025, from
https://www.talonic.com/blog/ai-for-fashion-data-analytics-su
stainable-supply-chains

American Journal of Information Science and Technology http://www.sciencepg.com/journal/ajist

210
[68] TechnoLynx (2025, February 13). Computer Vision for Quali-
ty Control in Manufacturing . Retrieved July 25, 2025, from
https://www.technolynx.com/post/computer-vision-for-quality
-control-in-manufacturing
[69] Thai, P. K., Bandaru, S. J., Sharma, A., & Devala, A. (2025).
Fashion image generation using generative adversarial neural
network. World Journal of Advanced Research and Reviews .
https://doi.org/10.30574/wjarr.2025.25.1.0123
[70] Vue (n.d.). Personalized AI Outfit Recommendation Solution .
Retrieved July 25, 2025, from
https://www.vue.ai/products/outfit-recommendations/
[71] WSGN (n.d.). WGSN | Trend Forecasting & Analytics
2025-2032. Retrieved July 25, 2025, from
https://www.wgsn.com/en
[72] Yashika (2024, October 23). The Role of AI-Powered Machine
Vision Systems in Textile Quality Control . Retrieved July 25,
2025, from
https://www.robrosystems.com/blogs/post/the -role -of-ai-
pow-
ered -machine -vision -systems -in-textile -quality -control
[73] Yep AI (2025, June 17). A Real -Life Use Case: How AI
Chatbots Are Being Used in the Fashion E -Commerce Indus-
try. Retrieved July 25, 2025, from
https://www.yepai.io/blog-posts/a-real-life-use-case-how-ai-c
hatbots-are-being-used-in-the-fashion-e-commerce-industry
[74] Zulhusni, M. (2025, May 22). How AI is helping the fashion
industry cut fabric waste . Retrieved July 25, 2025, from
https://sustainability-news.net/climate-nature/waste-managem
ent/how-ai-is-helping-the-fashion-industry-cut-fabric-waste/
[75] Zwieglinska, Z. (2024, October 4). Stitch Fix introduces
AI-driven customer pro files amid revenue decline . Retrieved
July 25, 2025, from
https://www.glossy.co/fashion/stitch-fix-introduces-ai-driven-
customer-profiles-amid-revenue-decline/
