---
title: A Cyber-Physical System Approach to Adaptive Visual Branding in Cultural Institutions
url: https://doi.org/10.56578/jemse050304
category: brand
subcategory: empirical
date: 2026-09
venue: Journal of Engineering Management and Systems Engineering
authors:
- Ievgeniia Kyianytsia
- Dmytro Yatsiuk
- Halyna Aldankova
source: openalex-oa
pdf_url: https://library.acadlore.com/JEMSE/2026/5/3/JEMSE_05.03_04.pdf
pages: 14
chars: 65062
fetched_at: '2026-11-08T19:19:11+00:00'
kb_version: 1
---

# A Cyber-Physical System Approach to Adaptive Visual Branding in Cultural Institutions

Journal of Engineering Management and Systems
Engineering
https://www.acadlore.com/journals/JEMSE
A Cyber-Physical System Approach to Adaptive Visual Branding in
Cultural Institutions
Ievgeniia Kyianytsia1*
 , Dmytro Yatsiuk 1
 , Halyna Aldankova 1
 , Oleksii Horobets 2
 , Vladyslav Slipchenko 2
 ,
Viktor Dobrovolskyi3
1 Department of Journalism and Advertising, State University of Trade and Economics, 02156 Kyiv, Ukraine
2 Department of Marketing, State University of Trade and Economics, 02156 Kyiv, Ukraine
3 Department of Theater Arts Organization Named of I. D. Bezgin, Kyiv National I. K. Karpenko-Kary Theatre,
Cinema and Television University, 01054 Kyiv, Ukraine
* Correspondence: Ievgeniia Kyianytsia (ievgeniiakyianytsia@gmail.com)
Received: 07-16-2026 Revised: 08-14-2026 Accepted: 08-22-2026
Citation: I. Kyianytsia, D. Yatsiuk, H. Aldankova, O. Horobets, V. Slipchenko, and V. Dobrovolskyi, “A cyber-
physical system approach to adaptive visual branding in cultural institutions,”J. Eng. Manag. Syst. Eng. , vol. 5, no.
3, pp. 340–353, 2026. https://doi.org/10.56578/jemse050304.
 2026 by the author(s). Published by Acadlore Publishing Services Limited, Hong Kong. This article is available for free download
and can be reused and cited, provided that the original published version is credited, under the CC BY 4.0 license.
Abstract: Immersive technologies are increasingly used by cultural institutions to create context-sensitive visitor
experiences, yet conventional media branding pipelines rely largely on predefined visual assets and provide limited
support for real-time adaptation. This study investigates how generative artificial intelligence (AI) can be integrated
into an adaptive systems architecture while preserving institutional visual identity. A mixed-method design was
employed, comprising an analysis of immersive branding pipelines, case studies of five cultural institutions, the
development of two prototype application scenarios, and an evaluation by nine experts. The proposed architecture
connected contextual data acquisition, generative processing, constraint validation, immersive rendering, and user
feedback within a closed-loop workflow. A Validator module was introduced to examine generated outputs against
predefined color and geometric constraints and to initiate regeneration or fallback procedures when violations were
detected. The case analysis produced a mean adaptivity score of 4.2 out of 10 for the existing implementations.
Expert evaluation of the proposed architecture yielded mean scores of 4.78 for personalization, 4.56 for visual
identity flexibility, and 3.89 for brand consistency. Generation latency ranged from 1.2 to 1.8 s in the augmented
reality (AR) scenario and from 2.5 to 4.0 s in the virtual reality (VR) scenario. The findings indicate that generative
AI can be incorporated into a feedback-controlled branding pipeline without removing deterministic control over
core visual elements. The proposed architecture provides a systems engineering basis for coordinating content
generation, identity validation, and immersive delivery, while the observed latency and limited evaluation sample
identify priorities for edge deployment and larger-scale experimental validation.
Keywords: Systems engineering; Adaptive digital systems; Generative artificial intelligence; Immersive media;
Feedback control; Visual identity management; Cultural institutions
1 Introduction
During the last decade, digitalization of the cultural sector has become systemic, transforming traditional
approaches to preservation and representation of cultural heritage. Cultural institutions gradually transform from
static web representations to branched interactive digital environments [1, 2]. The implementation of augmented
reality (AR) and virtual reality (VR) technologies has enabled the creation of new strategies of audience engagement in
the leading museums and galleries of the world. World institutions, in particular Louvre Abu Dhabi, Tate Modern, and
the Smithsonian Institution, actively implement immersive scenarios for the development of visual communication
of their own brands. The use of artificial intelligence (AI)-driven AR/VR tools enables the establishment of an
emotional connection with a visitor and enhances recognizability of the institution in media space [3].
However, scaling such solutions is accompanied by a principal dilemma concerning visual content controllability [4,
5]. While the complexity of the immersive scenario grows, ensuring stability of the visual identity of a brand in
a dynamic environment becomes more and more difficult [6]. Thus, traditional methods of scenario development
often appear to be too inflexible to respond promptly to changing interaction contexts [7]. In view thereof, there is
https://doi.org/10.56578/jemse050304
340

an objective need to develop new technological mechanisms for the management of visual assets [8]. The necessity
of a similar transformation is stipulated by the disparity between the high speed of user request generation and
the limited possibilities of manual immersive content editing. In this context, transition to intellectual automation,
able to maintain aesthetic environmental coherence without direct intervention of the developer, acquires special
attention [9].
Available scientific studies in this domain cluster around two main directions: technical implementation of AR/VR
systems and general branding strategies [10, 11]. However, the overlap between these areas remains fragmented,
resulting in three main research gaps that are not adequately addressed by existing work. First, methodological
deficits are observed in the operationalization of visual content adaptability criteria; most developments propose
static models that are not adjusted for the dynamics of immersive environments and do not consider the potential
of modern intellectual systems. Second, there is a technological gap in architectural solutions—mechanisms for
seamless integration of generative AI into real-time media branding pipelines are not substantiated. Third, empirical
data are lacking on how high variability of adaptive scenarios affects the stability of audience perception of an
institution’s visual identity. These controversies between the growing potential of generative technologies and
the lack of systemic tools for control over brand integrity define the relevance of this study. The current work
aims to overcome these gaps by modeling an intellectual system for visual brand personalization without loss of
recognizability.
To rigorously frame this integration challenge within the systems engineering paradigm, the problem is formalized
as a constrained optimization task within a feedback control framework. Let x ∈ Rd denote the generated visual
output (e.g., a branding texture), where d is the dimensionality of the output feature space (e.g., pixels or latent
representation); let c ∈ Rm represent the contextual input vector (user geolocation, time, behavioral profile), where
m is the number of contextual features; and let B denote the feasible set of visual outputs satisfying the immutable
brand constraints—specifically, colorimetric tolerances ( ∆E < 3.0 in Commission Internationale de l’ ´eclairage
L*a*b* (CIELAB) color space) and geometric constraints (logo contour integrity). The objective is defined as
maximizing contextual personalization P (x, c) while strictly enforcing x ∈ B. This formulation transforms the
inherently stochastic inference of latent diffusion models into a deterministic stabilization problem: maintaining
output stability under stochastic inputs. The Validator module is conceptualized as a supervisory controller that
continuously monitors the output, computes deviations from B, and triggers corrective actions (regeneration or
fallback) via a negative feedback loop. This control-theoretic perspective positions the Validator not as a simple
quality filter, but as a genuine control-theoretic contribution—a feedback stabilizer that ensures brand consistency
despite the inherent randomness of generative processes. Consequently, the proposed architecture is not merely
a design tool but a closed-loop cyber-physical system that maintains brand stability under dynamic environmental
conditions.
The study aimed to substantiate the possibilities of the use of generative AI for adaptive management of visual
AR/VR scenarios in processes of media branding of cultural institutions. To achieve the aim, the following three
research tasks were set: (1) To identify the criteria of adaptability of AR/VR scenarios, affecting recognizability
of the brand of cultural institutions in a dynamic media environment. (2) To define architectural principles of
integration of generative AI models into pipelines of development of AR/VR visual branding elements. (3) To
analyze the potential influence of the proposed approach on the brand identity flexibility and its perception by the
audience of cultural institutions.
To ensure methodological consistency and the fixation of content gaps in the scientific discourse, two research
questions were formulated.
Q1: How can generative AI operatively change parameters of AR/VR scenarios to maintain the consistency of
cultural institution branding in different interaction contexts?
Q2: What are the limitations of modern generative models for the creation of visual branding patterns in virtual
and augmented spaces of cultural institutions?
The following assumption was proposed as a hypothesis (H1). The use of generative AI for adaptive control of
AR/VR scenarios can potentially improve the consistency of visual elements of media branding of cultural institutions
compared to static solutions, provided that the Validator module is activated to enforce brand constants.
The scientific novelty of the study consists in the development of an architectural pipeline that integrates
generative AI with immersive environments through a feedback-controlled validation mechanism. Unlike static
branding approaches, the proposed system enables real-time personalization while enforcing deterministic constraints
on brand constants via structured prompt engineering and controlled diffusion methods.
1.1 Evolution of Immersive Technologies within the Context of Visitors’ Experience
The modern paradigm of functioning of cultural institutions is characterized by a gradual transition to an Industry
5.0 model. In their work, Orea-Giner et al. [12] define a human-centric approach as a priority of similar innovative
transformation in interaction with AI. The basic principles of AR/VR implementation for enhancing the visitor
341

experience at cultural heritage sites are viewed as a basis of digital transformation of the museum sphere in the study
of Basheer et al. [13]. Herewith, the effectiveness of similar systems directly depends on the depth of emotional
engagement. Thus, Chang and Suh [14] demonstrate that feelings of presence and immersiveness are above all
achieved through high-quality digital storytelling.
Theoretical developments of recent years are directed at overcoming barriers between the virtual and physical
worlds via multi-sensor interaction. In particular, in their article Gayathri and Nam [15] analyze the impact of
vibrotactile feedback on the quality of user experience in virtual museums. In turn, Srdanovi ´c et al. [16] studied
a gamified mobile application with elements of AR as an effective tool for cultural heritage preservation in the
metaverse. The analysis of the mentioned approaches reveals significant controversy between the pursuit of maximal
multisensor immersiveness and the architectural rigidity of software systems. Models proposed in the works of
Gayathri and Nam [15] and Basheer et al. [13] are oriented to static assets, compiled in advance, which makes
dynamic transformation of the scene in real time impossible under the influence of changing context. Moreover,
according to Chang and Suh [14], the conception of storytelling fully relies on human-authored linear scenarios,
creating technological bottlenecks while attempting to scale the content. The limitation of the available solutions
lies in the lack of feedback between the level of emotional engagement of users and the algorithmic generation of the
environment, which makes the design of systems with high-level context reactivity relevant.
1.2 Media Branding and Visual Identity of Cultural Institutions
The technological aspect of branding systems integration into the digital space requires a transition from
descriptive marketing concepts to the analysis of data-transmission architecture. The study by Ferreiro-Rosende
et al. [17] and the work by Rosende [18] view visual identity as a set of static media components, translation of which
is limited by traditional web interfaces. A similar approach creates critical vulnerabilities while attempting to render
brand elements in immersive computing environments due to the risk of geometric and colorimetric distortions. Li et
al. [19] offer an alternative cognitive-digital model, substantiating the necessity of transformation of visual markers
into adaptive stimuli, based on the Stimulus–Organism–Response (SOR) model. However, the mentioned work lacks
an algorithmic description of automated control pipelines.
At the same time, in the field of strategic management automation, Saura et al. [4] argue that effective system
personalization requires predictive AI models capable of dynamically adjusting content-output parameters. The
operation of such models depends not only on predictive accuracy but also on the architecture through which
contextual data, algorithmic decisions, system responses, and user feedback are coordinated. Yan et al. [20]
demonstrated that collaborative control architectures, which combine behavioral input from users with AI-driven
decision-making, can support adaptive system behavior in immersive VR settings. This system engineering
perspective is directly relevant to immersive media branding, where generated visual content must be continuously
evaluated against contextual requirements and predefined identity constraints. Accordingly, modern media branding
should be considered not merely as a visual design activity, but as an adaptive information system requiring
coordinated generation, validation, feedback, and control mechanisms.
1.3 Generative AI as an Adaptive Management Tool
AI integration into the cultural sphere opens up opportunities for qualitative heritage documentation. In his work,
Bhimavarapu [21] focuses on the potential of computer vision for interactive communication with art objects. The use
of a complex of neural networks for the recognition of visitors’ emotions in the system of Kwon and Yu [22] creates
preconditions for the development of dynamic interfaces. However, Martusciello et al. [23] propose a reference
architecture combining generative models with AR pipelines for gamified cultural heritage applications. The most
relevant for this article is the experience of Troussas et al. [24], who note that real adaptability may be achieved only by
the implementation of human-centric AI models capable of cognitive cooperation. Analysis of available architectural
solutions indicates the presence of a serious technological controversy between recognition and generation models.
According to Kwon and Yu [22], the emotion recognition system functions as an analytical tool (classifier), which
does not have a direct interface with a graphics rendering pipeline. In contrast to this, the reference architecture of
Martusciello et al. [23] ensures integration of generative models with AR systems, but completely neglects the issue
of graphic constants preservation, which causes the appearance of uncontrolled stochastic artifacts during diffusion.
According to Troussas et al. [24], human-centric models offer conceptual output through cognitive collaboration,
but do not contain formalized mathematical criteria for evaluation of visual coherence of generated content. Thus,
there is a need for the development of a new computing model of an AI pipeline, combining contextual reactivity
with algorithmic limitation of generation space for preservation of brand parameters.
1.4 Identification of a Scientific Problem
Despite the active development of immersive technologies, mechanisms of flexible management of visual identity
in immersive environments remain conceptually undefined. Most available approaches are based on static scenarios,
342

which limit possibilities for immediate adaptation of branding elements to the changing interaction context. Lack
of formalized criteria of evaluation of such variability prevents the creation of comprehensive architectural models,
able to consistently integrate intellectual generation into digital pipelines. Analysis of publications enables outlining
a scientific problem, which is the controversy of the stochastic nature of generative AI and the deficits of tools of
automated control over visual coherence of the brand in real time. Available IT solutions do not ensure dynamic
adaptation at the platform infrastructure level. The scientific novelty of the work is in the development of the
intellectual pipeline architecture, balancing personalization of the immersive experience with strict compliance with
graphic constants.
In summary, the reviewed literature reveals a consistent pattern: existing approaches prioritize either immersiveness
or generative capacity, but rarely combine both under controlled conditions. The proposed architecture addresses
these limitations by introducing an imperative validation layer that operates as a supervisory controller, transforming
stochastic inference into a deterministic control problem while preserving adaptive personalization.
2 Methodology
2.1 Study Procedure
The study was conducted as a mixed-type theoretical-applied study. A convergent parallel design was selected
because it enabled the simultaneous collection of quantitative expert evaluations and qualitative narratives for AI
pipeline verification, which enabled achieving the aim of the work. The selected design enabled elaboration on the
issue of the lack of established architectural solutions at the intersection of generative AI, AR/VR scenarios, and
media branding of cultural institutions. The procedure was conducted in three consecutive phases. The first phase
(June–December 2024) was focused on the analysis of the available cases of media branding of cultural institutions
with the use of AR/VR technologies. The second phase (2025) provided development of the author’s case on the
basis of the outlined adaptivity criteria. The third phase (January–April 2026) was directed at expert evaluation of the
effectiveness of the proposed solution. Each phase formed the foundation for the next one and fixed the intermediate
results.
2.2 Sample Formation
The sample included five cases of media branding of museums and galleries, where immersive scenarios are used
for visual communication. The search for the sites was conducted via specialized platforms MuseumNext and XR
Today by keywords ‘museum AR VR branding’ for the period of 2022–2024. The primary pool of 18 institutions
underwent filtration based on the inclusion criteria: availability of technical documentation, branding integration
into the extended reality (XR) space, and availability of video recordings of sessions. Guide applications without
elements of space tracking and projects of local galleries without international certification were excluded from the
search. The sample included Louvre Abu Dhabi (United Arab Emirates), Tate Modern (Great Britain), and National
Museum of Korea (Republic of Korea). Van Gogh: The Immersive Experience (global tour) and Mus ´eum national
d’histoire naturelle (France) were also included.
The case of Louvre Abu Dhabi was selected due to its public engagement with immersive AR technologies,
as documented in the museum’s official exhibition materials and announcements [25]. The case of Tate Modern
represents the experience of three-dimensional reconstruction of the space (Modigliani VR) with integration of the
narrative markers of the brand [26]. The National Museum of Korea was included as an example of the creation of the
intellectual platform of curation K–Museum on the basis of algorithms of the Electronics and Telecommunications
Research Institute (ETRI) [27, 28]. Project Van Gogh: The Immersive Experience demonstrates possibilities of
scaling 360-degree projections and VR beyond traditional museums [29]. The case of Mus ´eum national d’histoire
naturelle demonstrates the work of permanent VR exposition for strengthening the brand of institutional outreach [30].
The expert panel was formed using the method of targeted selection with consideration of field-specific
competence and absence of conflicts of interest. The panel included nine specialists. Five experts had experience
in the practical design of AR/VR applications in the area of culture and entertainment. Four experts specialized in
studies of media branding and visual communication of cultural institutions. Panel inclusion criteria provided at least
three years of professional experience in the relevant sphere, presence of realized projects or publications in peer-
reviewed publications, and confirmed participation in professional unions. Exclusion criteria were direct engagement
in one of the five analyzed cases. Panel formation was conducted via professional networks—ResearchGate and
LinkedIn. The procedure involved analysis of the Hirsch index (minimum 3 for researchers) and the presence of
at least two developed commercial XR systems. Expert evaluation was conducted individually, without collective
discussion, to avoid dominance of separate thoughts and the effect of group conformism.
2.3 Methods and Instruments of the Study
1. Multiple-case study method (Task 1). Content analysis of video protocols and technical documentation from
five selected cases was performed. An immersive interaction session, lasting 15 minutes, was defined as the unit of
343

analysis. A codebook, comprising five criteria (scene personalization, contextual reactivity, brand symbol stability,
visual coherence, and transition flexibility), was applied. Evaluation was conducted on a scale: 0 (parameter absent),
1 (partial occurrence), 2 (complete conformity). Intercoder reliability was verified using Cohen’s kappa coefficient,
with a minimum value of 0.84 obtained, confirming high consistency.
2. While developing their own case (Task 2, Q1), a method of pipeline component analysis with subsequent
synthesis of integration points was used. An architecture for an adaptive AR/VR scenario, incorporating generative
AI, was designed and subdivided into four operational components: content data collection, prompt construction,
visual element generation, and scene compositing.
3. Expert evaluation (Task 3, Q2, H1). A matrix of criteria, the architecture of the developed case, and a
comparative analysis of static and dynamic solutions were provided to a panel of nine experts. Evaluation was
performed across four categories: visual identity flexibility, brand consistency, personalization, and risk of visual
artifacts, utilizing a five-point Likert scale. Semi-structured interviews, consisting of three thematic blocks, were
conducted and recorded for subsequent thematic analysis. Audio data were transcribed to facilitate the identification
of qualitative patterns.
4. Statistical data analysis. Quantitative data derived from expert evaluation were processed using descriptive
statistics via the IBM SPSS Statistics v.28 software package. Kendall’s coefficient of concordance (W ) was calculated
to determine the level of expert consensus. Paired comparison methods were employed to analyze static versus
dynamic solutions regarding variability and resource expenditure. H1 was executed using the Wilcoxon signed-rank
test for paired samples (p <0.05), providing a rigorous statistical basis for the comparison of branding consistency.
H1 was conducted in the form of an examination of architectural compatibility parameters. This process involved
three stages: (1) logical analysis and compliance with adaptability criteria; (2) comparison with expert evaluations,
where the hypothesis was considered statistically supported if the mean value of the brand consistency evaluation for
the dynamic scenario exceeded that of the static scenario at a significance level of p <0.05 (Wilcoxon signed-rank
test); and (3) comparative analysis of literature data. The hypothesis was considered fully confirmed only if positive
results were obtained at all three stages.
3 Results
3.1 Criteria of Virtual Content Adaptivity
Empirical data of the content analysis, represented in Table 1, enable stating a critically low level of adaptivity
in most active international digital projects. The cumulative parameter of the technological flexibility of available
solutions is only 4.2 points out of a maximum of 10, which indicates the predominance of static approaches
to rendering graphic constants. Academic platforms demonstrate high parameters of visual coherence, but are
absolutely rigid in terms of personalization and dynamic generation of content in real time.
Table 1. Cumulative points of adaptivity of visual content in cases (maximum 10 points)
Case Personalization Reactivity Stability Coherence Transition Flexibility Sum
Louvre Abu Dhabi 1 0 2 2 0 5
Tate Modern 2 0 1 2 1 6
National Museum of
Korea 1 0 2 1 0 4
Van Gogh: The
Immersive Experience 2 0 0 1 1 4
Mus´eum national
d’histoire naturelle 0 0 1 1 0 2
Source: Calculated by the authors on the basis of content analysis of video protocols and technical documentation of the sample. The
documentation includes references [25–30].
The results of case analysis in Table 1 enable verification of the performance of the first task. The mean parameter
of adaptivity is 4.2 out of 10 points, indicating dominance of static approaches. Tate Modern received the highest
points for personalization, Louvre Abu Dhabi—for symbol stability. This may indicate the priority of preservation
of brand constants in available solutions. The revealed absence of contextual reactivity in all examples indicates a
systematic gap in adaptivity. The findings enable the formation of requirements for the design of an adaptive pipeline.
3.2 Architectural Principles and Development of the Author’s Model
Based on the revealed gaps, the architecture of an adaptive scenario was developed. It includes four basic
components of the intellectual pipeline: a module of context data collection, a block of prompt formation, a
344

generative module, and a rendering system. The full engineering stack of model architecture, in addition to the
the aforementioned components, contains two overlapping infrastructure elements—the Application (XR client
interface) and the Validator (an imperative control module for brand graphic constants). Two use scenarios for the
architecture are described below (Figure 1 and Figure 2).
Figure 1. Dynamic AR-filter for a cultural event
Note: AI = artificial intelligence; AR = augmented reality; PNG = Portable Network Graphics.
Figure 2. Personalized virtual exposition
Note: AI = artificial intelligence; VR = virtual reality.
The system retrieves data on the visitor’s time and geolocation to form a unique branding layer. The Unified
Modeling Language (UML) sequence diagram (Figure 1) reflects the following logic. A user initiates a request
by pointing the camera at the marker. The application registers a request and activates the context model, which
transmits data about evening time and the event of the exposition opening to the prompt generator. A generative
model receives the instruction and returns the unique texture in Portable Network Graphics (PNG) format. Rendering
overlays the received image on the video feed in real time. Prompt specification: ‘Golden gradient with a dark blue
shade, integrated logo of the museum as a light silhouette, style of an abstract ornament, evening lighting, without
text, high contrast, 512× 512 pixels, strength = 0.75’ (where strength denotes the denoising intensity of the diffusion
model, on a scale from 0 to 1, controlling the degree of deviation from the conditioned input).
The system adapts the VR environment on the basis of the duration of fixation of the user’s perspective on the
objects of a certain style. The UML sequence diagram (Figure 2) reflects the following elements: behavior tracker
fixes the interest of a user in the Baroque style and transmits the updated profile to the prompt formation module.
345

The generative module creates new branding textures with relevant ornaments. The VR system replaces the hall’s
background textures without interrupting the session. Prompt specification: ‘ Museum branding texture, Baroque
ornaments, gilded accents, dark-green background, integrated logo, tileable, 1024 × 1024.’ Negative prompt:
‘Shape distortion, text, low resolution.’
Encoding external conditions, such as lighting and viewer position, as text descriptors enables dynamic adjustment
of the visual scenario without loss of brand identity. Approbation of the architectural scheme on two typical usage
models confirmed its versatility. The proposed adaptation logic is internally consistent and fully corresponds to
earlier defined criteria.
3.3 Validator Module Specification
The Validator module serves as the core deterministic enforcement mechanism within the proposed cyber-physical
architecture. Unlike the generative module, which operates stochastically, the Validator is implemented as a rule-
based system (not a machine learning classifier) to ensure predictable, deterministic control over brand constants. Its
decision logic is structured as a two-stage verification pipeline: geometric integrity check and colorimetric fidelity
check.
Algorithm 1 Algorithm of the image validation module
1: Input: generated image (PNG), ref logo (PNG), brand profile (JavaScript Object Notation (JSON))
2: Output: validated image (PNG), status (ACCEPT | RETRY | FALLBACK)
3: CONSTANTS:
4: max retries = 3
5: geometric threshold = 0.85
6: ∆Ethreshold = 3.0
7: FUNCTION validate(generated):
8: // Stage 1: Geometric check
9: gen contours = OpenCV.findContours(generated)
10: ref contours = OpenCV.findContours(ref logo)
11: similarity = HuMomentIntersection(gen contours, ref contours)
12: if similarity < geometric threshold then
13: RETURN FAIL
14: end if
15: // Stage 2: Colorimetric check (CIELAB)
16: gen lab = RGB to CIELAB(generated)
17: ref lab = RGB to CIELAB(ref logo)
18: ∆E = CIE76(gen lab, ref lab)
19: if ∆E ≥ ∆Ethreshold then
20: RETURN FAIL
21: end if
22: RETURN PASS
23: FUNCTION main(generated, retry count = 0):
24: result = validate(generated)
25: if result == PASS then
26: RETURN (generated, ACCEPT)
27: else
28: if retry count < max retries then
29: augmented prompt = augment prompt(errors)
30: new generated = generate(augmented prompt)
31: RETURN main(new generated, retry count + 1)
32: else
33: RETURN (static fallback asset, FALLBACK)
34: end if
35: end if
Geometric integrity check . The generated texture is processed using contour detection via the Open Source
Computer Vision Library (OpenCV), specifically the findContours algorithm. The extracted contours are compared
against the reference brand logo contours using Hu moment invariants. The similarity score is computed as the
normalized intersection over union (IoU) of the matched contours. The validation passes if IoU≥ 0.85 (the predefined
threshold in the current implementation).
346

Colorimetric fidelity check. The generated texture and the reference logo are converted from the red-green-blue
(RGB) to the CIELAB color space. The color difference is calculated using the CIE76 formula (∆E). The validation
passes if ∆E <3.0, which corresponds to the perceptual tolerance threshold for brand color consistency.
If both checks pass, the texture is accepted and passed to the rendering pipeline. If either check fails, the
Validator triggers a regeneration loop. A negative prompt is augmented with specific constraints (e.g., “preserve
logo geometry”, “correct color balance”) and the generative model is invoked again. Up to three retries are
permitted. If all retries fail, the system executes a graceful degradation fallback: a pre-approved static branding asset
is substituted to maintain user experience without violating brand guidelines. The formal pseudocode specification
of the validation logic is provided in Algorithm 1:
This imperative validation logic ensures that the stochastic inference of the generative model is constrained within
the deterministic boundaries of institutional brand identity.
3.4 Results of Expert Evaluation
The third phase provided expert evaluation of the influence of the proposed architecture. The expert panel,
consisting of nine specialists, evaluated the proposed architecture. Statistical parameters are presented in Table 2.
Table 2. Mean experts’ grades (scale 1–5)
Category Mean (M) Standard Deviation (SD)
Visual identity flexibility 4.56 0.53
Brand consistency 3.89 0.78
Personalization 4.78 0.44
Risk of the appearance of visual artifacts 3.33 0.87
Kendall’s coefficient of concordance is W = 0.62 at p <0.05. This indicates an acceptable level of consensus
among experts. Thematic analysis gave the following results: three thematic categories were outlined from the open
commentaries of the experts.
Category I: technical limitations. Experts indicated a 1.5–3 s generation delay as a critical factor for AR
scenarios in real time. The stochastic nature of the output data complicated the accurate reproduction of logos
and brand symbols. The frequency of artifacts’ appearance was evaluated as moderate during the use of negative
prompts.
Category II: content limitations. Generative models demonstrated limited ability to observe strict geometric
brandbook requirements. Reproduction of accurate color parameters (∆E <3.0) without additional post-processing
presented a problem.
Category III: organizational risks. The experts noted uncertainty regarding copyright ownership of generated
content as a barrier for commercial use. The necessity of technical expertise for setting prompts limited solution
scalability.
Limitations of modern generative models for the creation of visual branding patterns in virtual and augmented
spaces of cultural institutions were systematized according to three types. Technical limitations (performance,
stochastic nature) were crucial for real-time scenarios. Content limitations (color accuracy, geometry) were partially
compensated by prompt engineering and post-processing. Organizational limitations (legal uncertainty, expert
dependence) required institutional solutions beyond the technological sphere.
3.5 Comparative Characteristics of the Developed Scenarios
To systematize the results of architectural modeling, a comparison of scenarios based on the key parameters of
scenario realization was conducted. The data, presented in Table 3, demonstrate differences in generation delay
and personalization depth. Both scenarios may be useful for different types of immersive interactions in cultural
institutions.
Table 3. Technical parameters of adaptive scenarios
Comparison Parameters Scenario 1 (AR-filter) Scenario 2 (VR Exposition)
Main content source External environment User’s behavior
Generation difficulty Low (2D-patterns) High (3D-texture)
Latency range 1.2–1.8 s 2.5–4.0 s
Brand stability level High (masks) Average (stylization)
Prompt update frequency Trigger-based Stream-based
Note: 2D = two-dimensional; 3D = three-dimensional; AR = augmented reality; VR = virtual reality.
347

Comparative analysis indicates that scenario 1 is more suitable for quick visual communication, where the
rendering rate during mass festival events and short excursion routes is crucial. By contrast, scenario 2 ensures
deeper immersiveness due to the complex transformation of the surroundings, which requires greater computational
capacity and is optimal for stationary VR installations for individual visitors. The revealed difference in delays
illustrates technical limitations, systematized in the response to Q2.
Mathematical verification of H1 was conducted through statistical comparison of the expert evaluation of brand
consistency for the proposed dynamic model against the averaged baseline parameters derived from the five static
case studies (Louvre Abu Dhabi, Tate Modern, National Museum of Korea, Van Gogh: The Immersive Experience,
and Mus´eum national d’histoire naturelle). These static baseline parameters were obtained from the content analysis
of technical documentation and video protocols (Table 1), representing the existing level of brand consistency
in traditional approaches. The comparison was performed using the Wilcoxon signed-rank test. An exploratory
comparison (Wilcoxon signed-rank test) suggested higher brand consistency for the dynamic pipeline than for the
averaged static baseline ( Z = -2.04, p <0.05) under the condition of Validator module activation; however, this
result should be interpreted cautiously, because the static baseline parameters and the dynamic system evaluations
were not obtained under fully identical paired experimental conditions. Six of the nine experts rated the dynamic
system with 4 or 5 points for brand consistency, while three experts noted persistent risks of stochastic distortions
during stream generation. H1 is therefore considered partially supported, with the qualification that the comparison
was exploratory. This underscores that the Validator is not an optional add-on but a critical component for achieving
brand stability.
While the primary evaluation of the proposed architecture relied on expert assessment of visual quality, an
approximate performance analysis was conducted based on the system specifications and empirical observations
from the case studies. The average generation latency for 512 × 512 textures was observed in the range of 1.2–1.8 s
for AR-filter scenarios and 2.5–4.0 s for VR exposition scenarios (Table 3). These values are consistent with typical
inference times for latent diffusion models (Stable Diffusion 1.5) running on a consumer-grade graphics processing
unit (GPU), such as an NVIDIA RTX 3060. Memory usage is estimated at approximately 4–6 GB of video random
access memory (VRAM) for model inference, with an additional 1–2 GB for prompt processing and rendering buffers.
All generative model invocations were performed using local inference on a dedicated GPU-enabled workstation,
eliminating dependence on Internet connectivity or cloud server bandwidth. Consequently, application programming
interface (API) call success rates were not applicable to this setup.
4 Discussion
Combining generative AI with museum branding fundamentally changes principles of visual communication,
ensuring the transition from static logos to dynamic adaptive systems. The findings on the high personalization
potential in AR and VR are consistent with the findings of Liu and Sutunyarak [31], according to which immersiveness
becomes a determining factor of the formation of the user’s intention to return to the museum. This confirms the
ability of the developed architecture to optimize quantitative parameters of user engagement. However, this reveals
the issue of blurring the boundaries between institutional branding and purely entertaining content. Complete
absence of content reactivity in available museum cases, revealed during the study, supports critical conclusions of
Li and Othman [32] that the potential of virtual environments remains only partially realized due to technological
conservatism.
Comparison of the modeled scenarios with the results of Javdani Rikhtehgar et al. [33] indicates that eye-tracking
mechanisms are an effective trigger for user engagement. However, the approach proposed in the work offers a
qualitatively new interaction level: the method of structured prompting according to Karnatak et al. [34] is used
instead of content selection from the fixed database. Such a solution enables the generation of a unique design in real
time, which fully corresponds to the conception of a comprehensive museum experience, described by Philippopoulos
et al. [35]. Implementation of the algorithmic design enables cultural institutions to avoid visual monotony, which
is characteristic of prolonged use of static VR assets.
The study’s results partially supported H1 while revealing critical technical limitations. Contrary to the optimistic
forecasts on AI integration in museum education by Tseng and Lin [36], practical tests in this study exposed severe
performance limitations. A multi-second generation delay ruins AR immersion, highlighting the conflict between
visual detail and acceptable latency, and forcing a shift in priority toward processing speed over asset resolution.
To overcome the latency barrier, several engineering strategies are required. Standard latency thresholds must
be maintained at under 100 ms for AR real-time interaction, whereas VR scenarios tolerate up to 300 ms. Model
optimization techniques, including quantization from 16-bit floating-point format (FP16) to 8-bit integer format
(INT8) and knowledge distillation, effectively reduce inference time by 40–60%. Furthermore, Edge AI deployment
via hardware like NVIDIA Jetson or Google Coral enables on-site processing that eliminates cloud communication
delays. Implementing these approaches involves a direct trade-off where lower model precision reduces fidelity to
enable real-time performance, forcing AR to prioritize speed while VR accepts higher latency for visual quality.
348

In addition, visual artifacts identified during expert evaluations refute claims that base AI models are ready for
autonomous museum deployment. Control superstructures such as Uni-ControlNet [37] and Blip-diffusion [38] are
essential to preserve brand reliability by injecting spatial and semantic constraints directly into the latent diffusion
process, firmly fixing geometry and color coordinates amidst stochastic generation. Disagreements among expert
evaluations confirm the professional community’s reluctance to grant AI full autonomy over institutional visual
identities.
From a strategic marketing perspective, while AI enables high brand flexibility as indicated by Cui et al. [39],
unguided adaptivity risks brand integrity and recognizability. Dynamic branding requires designers to shift from
creators of static forms to curators of algorithmic rules. Ultimately, AI integration in media remains a compromise
between reactivity and technical constraints, where combining generative capabilities with deterministic controls
represents the most viable path for modern museums.
The theoretical significance of the study lies in redefining media branding in immersive environments—not as
a static set of graphic constants, but as an adaptive system capable of self-adjustment through automated control
mechanisms. The proposed model “user → context → AI” extends visual communication theory by introducing the
concept of algorithmic supervision of brand integrity. The evaluation criteria developed in this study contribute to
filling the methodological gap in analyzing digital brands in dynamic environments.
The practical significance of the results is determined by the possibility of their direct implementation into the
work of cultural and marketing institutions. Developed architectural scenarios and UML diagrams are ready for use
as a technical base for the development of AR filters and VR expositions of the new generation. The use of generative
AI for asset creation in real time enables significantly optimizing expenses for production, as the need for initial
drawing of dozens of static variants of design is eliminated. Recommendations concerning the use of controlled
diffusion methods provide designers with tools for the protection of brand recognizability from the mistakes of neural
networks. Eventually, the results of the study offer an effective mechanism of user loyalty improvement through
the creation of a unique, personalized experience, which makes the cultural project more competitive in the modern
media space.
Regarding system robustness and graceful degradation, the proposed architecture incorporates several fault-
tolerance mechanisms. First, the Validator module’s regeneration loop (up to three retries with augmented prompts)
serves as a first-line defense against stochastic failures, such as visual artifacts or geometric distortions. If regeneration
fails, the system executes a graceful fallback to a pre-approved static branding asset, ensuring that the user experience
is maintained without violating brand guidelines. Second, for network-dependent operations, the system is designed
with a local cache of static assets; in the event of network interruption, the system automatically switches to offline
mode, serving cached content while logging the incident for later review. Third, to mitigate the risk of hallucinations
from the generative model, the Validator’s rule-based checks act as a guardrail, rejecting any output that fails to meet
geometric or colorimetric tolerances. These mechanisms collectively ensure that the system degrades gracefully
rather than failing catastrophically, maintaining a baseline user experience even under adverse conditions.
From a practical deployment perspective, several operational considerations emerge. First, infrastructure
requirements include a GPU-enabled server (minimum 8 GB VRAM) for local inference, or a cloud-based API
subscription with sufficient throughput for peak visitor loads. Second, staff training is essential: museum personnel
must be able to curate prompt templates and adjust Validator thresholds (e.g., geometric tolerance IoU ≥ 0.85,
colorimetric tolerance ∆E <3.0) to align with evolving brand guidelines. Third, maintenance overhead includes
periodic review of generated assets, monitoring of validation failure rates, and updates to the static fallback asset
library. While exact cost estimates depend on specific deployment scenarios, the architecture is designed to minimize
manual intervention, reducing the long-term cost of asset production compared to fully manual pipelines. Museums
should allocate initial investment in hardware and training, with operational costs scaling primarily with usage
volume.
Concerning sustainability and lifecycle thinking, generative AI models are computationally intensive. Estimated
energy consumption for a single inference (512× 512, 20 diffusion steps) on an NVIDIA RTX 3060 is approximately
0.5–0.8 Wh per generation. For a museum with moderate visitor traffic (e.g., 500 AR interactions per day),
daily energy consumption is projected at 250–400 Wh, equivalent to the energy usage of a typical household
refrigerator over the same period. Model retraining is not required for the core generative model, as pre-trained latent
diffusion models are used with prompt engineering for adaptation; however, retraining of the Validator’s geometric
constraints may be needed quarterly to accommodate brand updates. Data governance considerations include the
storage of generated assets (for quality auditing) and visitor interaction logs (for personalization). These should be
managed in accordance with General Data Protection Regulation (GDPR) or local data protection regulations, with
explicit consent mechanisms for tracking user behavior. The proposed architecture includes data retention policies
that anonymize user data after 30 days, minimizing privacy risks while retaining sufficient data for performance
monitoring.
349

4.1 Limitations
Despite extensive coverage and reproduction of the methodological apparatus, the study had some limitations that
can affect the interpretation of results. Above all, they are stipulated by rapid technological development and specifics
of hardware design, which currently do not enable realizing the potential of the proposed architecture in real time
comprehensively. High latency during high-quality visual assets generation was the main technical barrier. Although
the developed scenarios provide immediate reaction to the context change, in practice, there is a few-second pause
between data receipt from sensors and the adapted branding display. Moreover, the study utilized local GPU-based
inference rather than cloud computing; however, the current implementation requires a dedicated workstation with
sufficient computational resources (minimum 8 GB VRAM), which may limit deployment in resource-constrained
settings. Scaling to high visitor volumes would require either upgrading local hardware or transitioning to cloud-
based infrastructure, which would introduce new dependencies on Internet connectivity and server bandwidth. In
the latter case, performance would depend on network stability and cloud service availability.
Another methodological limitation concerns the comparison with static models. Experts did not evaluate static
alternatives directly under identical conditions; instead, the static baseline was derived from averaged parameters of
the five case studies. This indirect comparison introduces a potential bias, as the static systems were not assessed
by the same panel using the same evaluation framework. Future work should include a controlled experiment where
experts rate both dynamic and static outputs in a paired comparison design to enable more rigorous hypothesis
testing.
Another limitation concerns the representativeness of the case sample. The selected institutions, namely Louvre
Abu Dhabi, Tate Modern, National Museum of Korea, Van Gogh: The Immersive Experience, and Mus´eum national
d’histoire naturelle, represent top-tier, heavily funded organizations. While these cases provide rich empirical
data on advanced immersive branding practices, their scale and resources are not typical of the broader cultural
sector. Consequently, the findings may not be directly generalizable to smaller museums or cultural institutions
with limited budgets, technical infrastructure, or staffing. Future research should explore the applicability of the
proposed architecture in resource-constrained settings, potentially through lightweight implementations or cost-
reduced hardware configurations.
The composition of the expert panel presents another methodological limitation. The panel consisted of nine
specialists primarily from design and branding backgrounds, with expertise in AR/VR application design and visual
communication. While their assessment of visual quality, brand consistency, and personalization is highly valuable,
the panel lacked systems architects, software engineers, or museum IT professionals. This introduces a potential bias,
as the experts’ ability to judge technical feasibility and implementation complexity is limited. To mitigate this, the
architectural decisions were validated through formal modeling (UML sequence diagrams) and the Validator module
was specified with pseudocode to demonstrate technical viability. However, future studies should include a broader
range of expertise, particularly from engineering and IT domains, to provide a more comprehensive evaluation of
both aesthetic and technical dimensions.
From the perspective of visual identity, the stochastic nature of generative models presented a significant
limitation. The risk of appearance of visual artifacts or unpredicted distortions of brand symbols persists under
the condition of implementation of control methods (Uni-ControlNet, Blip-diffusion). Analysis is also limited by a
relatively small expert sample, which can add subjective elements to the final evaluation of system coherence and
stability.
5 Conclusions
The conducted study gives grounds to assume that the integration of generative artificial intelligence into the
architecture of media branding of museums can help to overcome some limitations of static visual systems. Analysis
of the available cases indicates quite a low average adaptivity level (4.2 out of a maximum of 10 points) and absence
of contextual reactivity in the study examples.
The proposed architecture, evaluated through AR-filter and VR-exhibition scenarios, demonstrated the feasibility
of generating personalized content in real time. Expert evaluation indicated relatively high effectiveness of the
proposed approach to personalization (M = 4.78) and visual identity flexibility (M = 4.56). Hypothesis on possible
higher brand consistency at AI use compared to static solutions was partially supported. The consistency parameter
was 3.89. An exploratory comparison (Wilcoxon signed-rank test) suggested that this value exceeded the averaged
baseline of traditional methods ( p <0.05 for the dynamic system with the Validator active); however, this finding
should be interpreted cautiously due to the lack of fully paired experimental conditions. Herewith, technical barriers
were revealed.
In particular, texture-generation delay remained 1.2–4.0 s, which may be noticeable for immersive experience.
Further studies’ perspectives may include the development of methods for the minimization of stochastic mistakes
of AI for achieving more accurate logo reproduction (∆E <3.0). Implementation of local computing models (Edge
AI) for the reduction of latency and improvement of autonomy of museum systems will probably require a separate
350

study. Practical deployment strategies include model quantization, knowledge distillation, and edge computing
architectures, each offering distinct trade-offs between generation speed and visual fidelity. For AR scenarios,
latency reduction below 100 ms is prioritized, while VR applications may tolerate higher latency in exchange for
enhanced quality. Creation of legal protocols for the regulation of the issue of copyright to dynamically generated
branding content also remains relevant.
Author Contributions
Conceptualization, I.K. and D.Y.; methodology, I.K. and H.A.; software, V.D.; validation, H.A. and V.D.; formal
analysis, D.Y. and H.A.; investigation, V.D.; resources, O.H. and V.S.; data curation, H.A.; writing—original draft
preparation, I.K. and D.Y.; writing—review and editing, V.S. and V.D.; visualization, V.S.; supervision, O.H.; project
administration, O.H. All authors have read and agreed to the published version of the manuscript.
Informed Consent Statement
All nine expert participants provided written informed consent prior to their involvement in the study. The
consent form detailed the purpose of the research, the evaluation procedures, the audio recording of semi-structured
interviews, and the subsequent transcription of the recorded data. Participants were assured that all data would
be anonymized and treated confidentially. They explicitly consented to the publication of aggregated, anonymized
results.
Ethical Approval
The institution of the authors, the State University of Trade and Economics, does not have an Ethics Committee
or other authorized body responsible for formal ethical review of research of this type. In accordance with the
applicable institutional requirements and relevant regulatory provisions, formal ethical approval was not required for
this type of study. Therefore, no formal ethical approval or exemption document was issued.
Data Availability
The data used to support the research findings are available from the corresponding author upon request.
Conflicts of Interest
The authors declare no conflicts of interest.
References
[1] J. Liao, “Research on the application of generative artificial intelligence in ‘teaching, learning, doing and
creating’ of intangible cultural heritage creation,” J. Sociol. Educ., vol. 1, no. 10, 2025.
[2] I. Kyianytsia, Mediaology: Social Communications. Kyiv, Ukraine: State University of Trade and Economics,
2025.
[3] M. Ribeiro, J. Santos, J. Lobo, S. Ara´ ujo, L. Magalh˜aes, and T. Ad˜ao, “VR, AR, gamification and AI towards
the next generation of systems supporting cultural heritage: Addressing challenges of a museum context,” in
Proceedings of the 29th International ACM Conference on 3D Web Technology , New York, NY, USA, 2024,
pp. 1–10. https://doi.org/10.1145/3665318.3677172
[4] J. R. Saura, V. Ratten, and V. Jeremic, “Digital cognition in predictive marketing personalization: A conceptual
framework,” Psychol. Mark., vol. 43, no. 5, pp. 1228–1260, 2026. https://doi.org/10.1002/mar.70109
[5] I. Bakhov, Y. Terebushko, O. Osaulchyk, O. Ryhina, and V. Vedenieiev, “Cultural challenges in education:
Strategies for consideration of various intercultural aspects in the educational process,” Multidiscip. Sci. J. ,
vol. 6, p. 2024ss0207, 2024. https://doi.org/10.31893/multiscience.2024ss0207
[6] F. Kayaalp, Z. B. Namlı, and E. Meral, “My museum: A study of pre-service social studies teachers’ experience
in designing virtual museums,” Educ. Inf. Technol., vol. 29, no. 18, pp. 24 047–24 085, 2024. https://doi.org/
10.1007/s10639-024-12742-8
[7] M. Konstantakis and E. Iakovaki, “ARIA: An AI-supported adaptive augmented reality framework for cultural
heritage,” Information, vol. 17, no. 1, p. 90, 2026. https://doi.org/10.3390/info17010090
[8] R. G. Boboc, E. B ˘autu, F. Gˆırbacia, N. Popovici, and D. M. Popovici, “Augmented reality in cultural heritage:
An overview of the last decade of applications,” Appl. Sci., vol. 12, no. 19, p. 9859, 2022. https://doi.org/10.3
390/app12199859
[9] Y. Wu, Q. Jiang, H. E. Liang, and S. Ni, “What drives users to adopt a digital museum? A case of virtual
exhibition hall of National Costume Museum,”SAGE Open, vol. 12, no. 1, 2022. https://doi.org/10.1177/2158
2440221082105
351

[10] B. Fanini, A. Pagano, E. Pietroni, D. Ferdani, E. Demetrescu, and A. Palombini, “Augmented reality for
cultural heritage,” in Springer Handbook of Augmented Reality . Cham: Springer, 2023, pp. 391–420.
https://doi.org/10.1007/978-3-030-67822-7 16
[11] M. Mahadevan, H. A, and S. J, “Cultural preservation using immersive technologies: A new approach,” Int. J.
Innov. Res. Humanit. Technol., vol. 9, no. 1, pp. 1–12, 2026. https://doi.org/10.67228/3071561X/IJIRHT-V9I
1P101
[12] A. Orea-Giner, A. Mu ˜noz-Maz´on, T. Villac´e-Molinero, and L. Fuentes-Moraleda, “Cultural tourist and user
experience with artificial intelligence: A holistic perspective from the Industry 5.0 approach,”J. Tour. Futures,
vol. 12, no. 2, pp. 268–285, 2026. https://doi.org/10.1108/JTF-04-2022-0115
[13] S. Basheer, S. Farooq, V. Hassan, Y. M. Malik, and M. A. Reshi, “Augmented reality and virtual reality in
cultural heritage tourism enhancing visitor experiences,” inExploring Culture and Heritage Through Experience
Tourism. IGI Global Scientific Publishing, 2023, pp. 13–34. https://doi.org/10.4018/978-1-6684-9957-3.ch
002
[14] S. Chang and J. Suh, “The impact of digital storytelling on presence, immersion, enjoyment, and continued
usage intention in VR-based museum exhibitions,” Sensors, vol. 25, no. 9, p. 2914, 2025. https://doi.org/10.3
390/s25092914
[15] R. Gayathri and S. Nam, “Enhancing user experience in virtual museums: Impact of finger vibrotactile
feedback,” Appl. Sci., vol. 14, no. 15, p. 6593, 2024. https://doi.org/10.3390/app14156593
[16] P. Srdanovi ´c, T. Skala, and M. Mari ˇcevi´c, “Inheritage—A gamified mobile application with AR and VR for
cultural heritage preservation in the metaverse,” Appl. Sci., vol. 15, no. 1, p. 257, 2024. https://doi.org/10.339
0/app15010257
[17] ´E. Ferreiro-Rosende, L. Fuentes-Moraleda, and N. Morere-Molinero, “Artists brands and museums:
Understanding brand identity,” Mus. Manag. Curatorsh. , vol. 38, no. 2, pp. 157–174, 2023. https://doi.or
g/10.1080/09647775.2021.1914143
[18] E. F. Rosende, “Museum brand identity model approach: An online Delphi study,” Methaodos Rev. Cienc.
Soc., vol. 10, no. 2, pp. 160–176, 2022. https://doi.org/10.17502/mrcs.v10i2.544
[19] J. Li, L. Zhou, and W. Wei, “Analyzing factors influencing learning motivation in online virtual museums using
the SOR model: A case study of the National Museum of Natural History,” Information, vol. 16, no. 7, p. 573,
2025. https://doi.org/10.3390/info16070573
[20] H. Yan, S. Hao, J. Zhang, and T. Huang, “Design and optimization of human-AI collaborative control systems
for interactive spatial narratives in virtual reality,” J. Eng. Appl. Sci., vol. 73, no. 242, 2026. https://doi.org/10
.1186/s44147-026-01037-z
[21] U. Bhimavarapu, “Enhancing cultural heritage documentation with AI and computer vision,” in Indigenous
Knowledge Management in the Open Science Framework. IGI Global Scientific Publishing, 2026, pp. 77–100.
https://doi.org/10.4018/979-8-3373-0204-1.ch004
[22] D. H. Kwon and J. M. Yu, “Real-time multi-CNN-based emotion recognition system for evaluating museum
visitors’ satisfaction,” ACM J. Comput. Cult. Herit., vol. 17, no. 1, pp. 1–18, 2024. https://doi.org/10.1145/36
31123
[23] F. Martusciello, H. Muccini, and A. Bucchiarone, “A reference architecture for gamified cultural heritage
applications leveraging generative AI and augmented reality,” arXiv preprint, p. arXiv:2506.04090, 2025.
https://doi.org/10.48550/arXiv.2506.04090
[24] C. Troussas, A. Krouska, and C. Sgouropoulou, “A novel framework of human–computer interaction and
human-centered artificial intelligence in learning technology,” inHuman-Computer Interaction and Augmented
Intelligence. Cognitive Systems Monographs. Cham: Springer, 2025. https://doi.org/10.1007/978-3-031-84
453-9 9
[25] Louvre Abu Dhabi, “Art Here 2025: Rintaro Fuse,” 2025. https://www.louvreabudhabi.ae/en/exhibitions/art-h
ere-2025-rintaro-fuse
[26] J. Richardson, “Virtual reality is a big trend in museums, but what are the best examples of museums using
VR?” MuseumNext, 2024. https://www.museumnext.com/article/how-museums-are-using-virtual-reality/
[27] National Museum of Korea, “Immersive Digital Gallery Information.” https://www.museum.go.kr/ENG/conte
nts/E0203010000.do
[28] National Research Council of Science and Technology, “ETRI leads standardization for ’Cultural Heritage
Digital Sovereignty’,” EurekAlert!, 2025. https://www.eurekalert.org/news-releases/1097981
[29] Van Gogh Expo, “Van Gogh exhibit in Spokane: The immersive experience.” https://vangoghexpo.com/spok
ane/
[30] J. Richardson, “Virtual reality is a big trend in museums, but what are the best examples of museums using
VR?” MuseumNext, 2024. https://www.museumnext.com/article/how-museums-are-using-virtual-reality/
352

[31] Q. Liu and C. Sutunyarak, “The impact of immersive technology in museums on visitors’ behavioral intention,”
Sustainability, vol. 16, no. 22, p. 9714, 2024. https://doi.org/10.3390/su16229714
[32] Y. F. Li and M. K. Othman, “Investigating the behavioural intentions of museum visitors towards VR: A
systematic literature review,” Comput. Hum. Behav., vol. 155, p. 108167, 2024. https://doi.org/10.1016/j.chb.
2024.108167
[33] D. Javdani Rikhtehgar, S. Wang, H. Huitema, J. Alvares, S. Schlobach, C. Rieffe, and D. Heylen, “Personalizing
cultural heritage access in a virtual reality exhibition: A user study on viewing behavior and content preferences,”
in Adjunct Proceedings of the 31st ACM Conference on User Modeling, Adaptation and Personalization ,
Limassol, Cyprus, 2023, pp. 379–387. https://doi.org/10.1145/3563359.3596666
[34] N. Karnatak, A. Baranes, R. Marchant, H. Zeng, T. Butler, and K. Olson, “Expanding the generative AI design
space through structured prompting and multimodal interfaces,” arXiv preprint, p. arXiv:2504.14320, 2025.
https://doi.org/10.48550/arXiv.2504.14320
[35] P. I. Philippopoulos, I. C. Drivas, N. D. Tselikas, K. N. Koutrakis, E. Melidi, and D. Kouis, “A holistic
approach for enhancing museum performance and visitor experience,” Sensors, vol. 24, no. 3, p. 966, 2024.
https://doi.org/10.3390/s24030966
[36] J. L. Tseng and C. C. Lin, “Leveraging artificial intelligence in museum education: Innovations and challenges
for promoting sustainable development goals,”Taiwan Educ. Rev. Mon., vol. 13, no. 11, pp. 19–32, 2024.
[37] S. Zhao, D. Chen, Y. C. Chen, J. Bao, S. Hao, L. Yuan, and K. Y. K. Wong, “Uni-ControlNet: All-in-one
control to text-to-image diffusion models,” in Advances in Neural Information Processing Systems, 2023, pp.
11 127–11 150. https://proceedings.neurips.cc/paper files/paper/2023/hash/2468f84a13ff8bb6767a67518fb59
6eb-Abstract-Conference.html
[38] D. Li, J. Li, and S. C. H. Hoi, “BLIP-Diffusion: Pre-trained subject representation for controllable text-to-
image generation and editing,” inAdvances in Neural Information Processing Systems, 2023, pp. 30 146–30 166.
https://proceedings.neurips.cc/paper files/paper/2023/hash/602e1a5de9c47df34cae39353a7f5bb1-Abstract-C
onference.html
[39] Y. Cui, P. van Esch, and S. Phelan, “How to build a competitive advantage for your brand using generative AI,”
Bus. Horiz., vol. 67, no. 5, pp. 583–594, 2024. https://doi.org/10.1016/j.bushor.2024.05.003
353
