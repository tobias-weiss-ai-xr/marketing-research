---
title: 'From Latent Influence to Language: Diffusion-Oriented Content Generation via Audience-Susceptible
  Features'
url: https://arxiv.org/abs/2608.19809
category: social-media
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Jiaying Lei
- Shengqi Dang
- Runqian Bai
- Ziqing Qian
- Nan Cao
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.19809
pages: 9
chars: 38996
fetched_at: '2026-11-08T12:57:06+00:00'
kb_version: 1
---

# From Latent Influence to Language: Diffusion-Oriented Content Generation via Audience-Susceptible Features

From Latent Influence to Language:
Diffusion-Oriented Content Generation via Audience-Susceptible Features
Jiaying Lei1,2, Shengqi Dang1,2, Runqian Bai1, Ziqing Qian1, Nan Cao1,2∗
1Tongji University
2Shanghai Innovation Institute
Abstract
The rapid growth of multimodal user-generated content on
social media has made information diffusion a critical fac-
tor for advertisers and brand marketers. However, manually
tailoring content to resonate with specific audiences is labor-
intensive and heuristic-driven. While recent generative mod-
els offer promising capabilities for automatic content gener-
ation, existing approaches for diffusion-oriented content gen-
eration still struggle to effectively translate numeric diffusion
influence signals into actionable guidance that captures la-
tent audience susceptibility and accounts for heterogeneous
audience interests. To address these challenges, we propose
DOCG-AS, a three-stage framework for diffusion-oriented
contentgeneration.Itfirstperformsimplicitfeatureoptimiza-
tion on the realistic content manifold to discover an optimal
propagation feature vector. Then, it explicitly decodes this
vector using a learnable decoder into interpretable audience-
susceptible features described in natural language, providing
guidance for content generation. Finally, it leverages multiple
sets of audience-susceptible features obtained from different
optimization initializations to rewrite the user’s input into
the final multimodal content. Experiments demonstrate that
DOCG-ASconsistentlyoutperformsstate-of-the-artbaselines
in terms of predicted diffusion influence.
Introduction
Therapidproliferationofsocialmediahasledtoanunprece-
dented surge in multimodal user-generated content, intensi-
fying competition for limited audience attention. On these
platforms, information propagates through complex user in-
teractions(Kempe,Kleinberg,andTardos2003),fundamen-
tally shaping practices in influencer marketing, digital ad-
vertising, and brand communication. As a result, diffusion-
oriented content—content designed to maximize informa-
tionspread—hasemergedasacriticalobjective(Bergerand
Milkman 2012). In practice, creators predominantly rely on
heuristic strategies, manually adjusting linguistic and visual
presentation to align with audience preferences (Barcelos,
Dantas,andSénécal2018;Dangetal.2026).However,such
adhocprocessesarelabor-intensiveandfailtosystematically
capture the latent factors governing audience engagement.
Recentadvancesingenerativemodels(Achiametal.2023;
Rombachetal.2022)haveenabledhigh-fidelitytextandim-
∗Corresponding author.
age synthesis, offering new opportunities for scalable con-
tent generation. This has spurred growing interest in per-
suasive and engagement-driven content generation (Coppo-
lillo et al. 2025; Matz et al. 2024). Nevertheless, existing
approaches exhibit notable limitations: most optimize for
coarse, audience-agnostic engagement metrics, while oth-
ers restrict personalization to textual modalities at the trait
or persona level (Pillai, Fokkens, and van Atteveldt 2025).
Consequently,theproblemofmultimodalcontentgeneration
tailored to diffusion within specific audience segments re-
mainsinsufficientlyexplored.Recentwork(Qianetal.2026)
takesaninitialstepbyformalizingdiffusion-orientedcontent
generation (DOCG) and proposing a reinforcement learning
(RL)frameworktooptimizetextandimagesundertheguid-
ance of the predicted influence score. Although promising,
thisparadigmhaslimitations:(1)theactionspacedefinedin
its RL process is predetermined and drawn from an unvali-
datedmarketingframework(i.e.,theSTEPPSmodel(Berger
and Milkman 2012)); (2) the generation process incurs sub-
stantial computational overhead due to the heavy estimation
required for iterative generation and evaluation. These limi-
tations underscore the need for a more flexible and efficient
approach to tackling DOCG.
Despiterecentadvancesingenerativemodeling,diffusion-
orientedcontentgenerationremainsfundamentallychalleng-
ing due to three core issues.(1) Elusive latent susceptibil-
ity.Information diffusion within a target audience is gov-
erned by higher-order, implicit factors that are difficult to
disentangle from observational data. For example, a movie
post may spread because a sarcastic question is paired with
a high-contrast still.(2) Non-actionable diffusion signals.
Although computational information diffusion models pro-
vide estimates of propagation (e.g., influence score), such a
score may show whether a post is more likely to spread than
another,butnothowtoadjustitscontent(e.g.,emotionaltone
and headline) for improved diffusion performance.(3) Het-
erogeneous and context-dependent preferences.Beyond
shared coarse preferences (e.g., movie enthusiasm), users
exhibit significant intra-group divergence along secondary
dimensions (e.g., avant-garde vs. classical tastes). This het-
erogeneity induces an optimization landscape with multiple
local maxima, which hinders content optimization.
To address these challenges, we propose a novel three-
stage framework for diffusion-oriented content generation
arXiv:2608.19809v1  [cs.SI]  20 Aug 2026

via audience-susceptible feature discovery, which takes a
target audience group and source content as inputs. The
first module,implicit feature optimization, identifies the
propagation-optimal feature vectore ∗ (i.e., the latent rep-
resentation that maximizes diffusion within the audience)
usinganinfluenceindicatortrainedonlarge-scaleuserinter-
action data. The second module,explicit feature decoding,
mapse ∗ into structured natural-language descriptions along
eightwell-established,reliabledimensions(theme,structure,
rhetoric, and emotion for both textual and visual modalities,
asillustratedinFigure2)viaalearnableLLM-baseddecoder,
thereby bridging continuous latent representations with dis-
crete, controllable semantics. The third module,audience-
susceptiblecontent generation,uses multipledecodedfea-
ture sets obtained from diverse optimization initializations
tocaptureaudienceheterogeneityandrewritestheinputinto
engaging multimodal content using off-the-shelf generative
models. Experiments and a user study demonstrate substan-
tialimprovementsinpredicteddiffusioninfluenceandhuman
preferencewhilepreservingthesourcecontent’scoreintent.
Our contributions are summarized as follows:
•Weproposeanovelthree-stageframeworkformultimodal
diffusion-oriented content generation via audience-
susceptible feature discovery.
•We introduce an implicit feature optimization method
that identifies propagation-optimal features on the realis-
ticcontentmanifold,jointlyimprovingdiffusioninfluence
while maintaining semantic plausibility.
•We develop an explicit feature decoding mechanism
that maps continuous optimal features to structured, in-
terpretable natural-language representations, effectively
bridging latent optimization and the discrete semantic
space of LLMs.
•We design an audience-susceptible content generation
strategy that leverages diverse decoded feature sets to
model audience heterogeneity and enables controllable
multimodal content rewriting.
Related Work
We review related work from two perspectives: (1) content-
level factors for promoting information diffusion and (2)
diffusion-oriented content generation.
Content-Level Factors for Promoting Diffusion
A large body of research shows that multiple factors in-
fluence the effectiveness of information diffusion. For the
textual modality, information value and linguistic style af-
fect how widely a message spreads (Džanko et al. 2025),
while content organization and specific wording also play
importantroles(Gligorić,Anderson,andWest2019;Borgh-
outsetal.2024).Engagement-orientedtextrewritingfurther
demonstratesthatchangesinlinguisticstylecansignificantly
alterapost’spredictedengagement(Pillai,Fokkens,andvan
Atteveldt 2025). For the visual modality, the mere presence
of images or videos can increase retweeting behavior (Xie
andLiu2022),andmorefine-grainedautomatedvisualanal-
ysis further reveals that objects, scenes, people, facial or
bodilycues,andvariousvisualattributesallinfluencesocial
media effects (Peng, Lock, and Ali Salah 2024). Beyond de-
picted content, image color, visual quality, and the volume,
variety,anddynamismofvisualelementsarealsocloselyre-
latedtouserengagement,viewers’emotionalresponses,and
subsequent behavioral responses (Yu and Egger 2021; Ka-
nuri,Hughes,andHodges2024;Philp,Jacobson,andPancer
2022; Chan, Chen, and Leung 2023).
Building on these findings, we construct eight con-
tent dimensions for the DOCG task. Compared with
the diffusion-oriented editing dimensions defined in De-
signed2Spread (Qian et al. 2026), our dimensions more
clearly separate content, organization, expression, and au-
dience response across both text and image modalities.
Diffusion-Oriented Content Generation
Recent work has explored automatically generating content
optimizedforsocialmediaspread.Earlyapproachesfocuson
maximizinggenericengagementsignals.Forinstance,some
methods fine-tune large language models against simulated
diffusion feedback (Coppolillo et al. 2025) or align genera-
tion with popularity indicators such as the number of likes
and retweets (Yu, Li, and Xu 2024), while others inject net-
work structure into prompts to amplify post influence (Zhao
et al. 2025). A step further, personality-aligned text genera-
tionhasbeenshowntoelicitstrongerpersuasiveresponsesat
thetraitlevel(Matzetal.2024),yetittargetscoarse-grained
audience segments rather than specific groups.
The most recent work (Qian et al. 2026) explicitly tack-
lesmultimodaldiffusion-orientedcontentgeneration.Itpro-
poses a reinforcement learning framework that rewrites text
orimagesusingapredefinedsetofeditingactions,guidedby
a content-level influence indicator. However, this paradigm
suffers from three key limitations. First, its hand-crafted ac-
tion primitives cannot discover latent susceptibility patterns
beyondhumanspecification.Second,itoptimizesagainstan
opaque scalar reward that offers no interpretable guidance
for generation. Third, its deterministic policy overlooks the
inherent heterogeneity of audience preferences.
In contrast, our approach addresses these limitations di-
rectly. We replace hand-crafted actions with implicit feature
optimization on the realistic content manifold to uncover la-
tentsusceptibilitypatterns.Wedecodetheoptimizedfeatures
into structured natural-language descriptions, providing in-
terpretable guidance. Finally, we adopt multi-start optimiza-
tion to capture audience heterogeneity, all within a unified
multimodal generation pipeline.
Method
In this section, we present the proposed three-stage frame-
workforgeneratingengagingmultimodalcontentc ∗ tailored
to a target audience groupU, conditioned on input content
cin. As illustrated in Figure 1, the framework takes as input
(1) a target audience groupUand (2) source contentc in,
and proceeds through three modules: (1)Implicit Feature
Optimization,whichidentifiesapropagation-optimalfeature
vectorontherealisticcontentmanifoldgivenU;(2)Explicit
FeatureDecoding,whichconvertstheoptimizedfeatureinto

Figure1:Pipelineoftheproposedframeworkforgeneratingengagingmultimodalcontentc ∗ tailoredtoatargetaudiencegroup
U, conditioned on input contentcin.
Figure 2: An illustrative example of a social media post and its corresponding natural-language descriptions across the eight
defined semantic dimensions.
audience-susceptible features, namely structured and inter-
pretablenatural-languagedescriptionsspanningmultiplese-
mantic dimensions; and (3)Audience-Susceptible Content
Generation, which leverages the decoded features to rewrite
cin into engaging multimodal contentc∗.
Implicit Feature Optimization
In this step, we aim to identify the latent feature represen-
tation (denoted ase ∗) that maximizes diffusion influence
within the target audience groupU. We base this on an in-
fluenceindicatorL U (e)adaptedfrom(Qianetal.2026)(we
slightly modify the formulation to fit our setting; details are
providedinSupplementaryMaterial).Specifically,L U (e)is
trained on real Twitter/X data that capture users’ diffusion
behaviors through observed retweets. It estimates the influ-
ence of a messagec, encoded ase=E(c), by averaging
the predicted pairwise propagation probabilitiespij among
users inU:
LU (e) = 1 |U|(|U| −1) X i,j∈U
i̸=j
pij(e)(1)
Next, we derive the optimal featuree∗ by maximizing the
influence indicatorL U (e)under a realism constraint that
discourages out-of-distribution feature drift, formulated as:
e∗ = arg max
e
LU (e) +λRvmf (e)(2)
whereR vmf (e)isamanifoldregularizerthatconstrainseto
lie in high-density regions of the distribution of real-world
content features, thereby promoting semantically valid and
realizable representations, andλ >0is a regularization
weight that balances the two terms. Specifically,Rvmf (e)is
defined via a von Mises-Fisher (vMF) kernel density esti-
mator (Banerjee et al. 2005) over a set ofKreference mul-
timodal posts{c k}K k=1 sampled from a real-world dataset
associated with the target audienceU:
Rvmf (e) =τ·log
KX
k=1
exp
 e⊤E(c k)
τ

(3)
whereτ >0controls the concentration of the estimator,
andE(·)is a pre-trained multimodal encoder (Qwen3-VL-
Embedding-8B (Li et al. 2026) in our implementation) that
maps raw content to normalized feature representations. We
furtherℓ 2-normalizeeafter each gradient update to keep it
ontheunithypersphere.Maximizingthisregularizerencour-
ageseto align with high-density regions of the empirical
feature distribution, thereby discouraging drift into out-of-
distribution areas and ensuring semantic plausibility.
Explicit Feature Decoding
Inthisstep,wedesignadecoderDbasedonalargelanguage
model(LLM)thattranslatestheoptimizedfeaturee ∗intoex-
plicit audience-susceptible featuresfU, expressed as struc-
turednatural-languagedescriptions,enablinginterpretability
and facilitating downstream content generation. This design
is motivated by two considerations: (1) LLMs encode rich
prior knowledge of linguistic and rhetorical patterns, en-
ablingthegenerationofcoherentandsemanticallygrounded
descriptions; and (2) expressing the decoded features in nat-
ural language makes them directly usable by downstream

LLM-based generation modules, eliminating the need for
additional interfaces or adaptation layers.
Specifically, based on our literature review, we define
four semantic dimensions for both textual and visual modal-
ities: theme, structure, rhetoric, and emotion. This yields
eight modality-specific dimensions: {Textual Theme,Visual
Theme,Textual Structure,Visual Structure,Textual Rhetoric,
Visual Rhetoric,Textual Emotion,Visual Emotion}, as il-
lustrated in Figure 2. We describe the decoder’s architecture
and training paradigm in detail below.
Formally, the decoding process is defined as:
fU =D(e ∗),(4)
whereDtranslates the numerical feature vectore ∗ into
natural-language descriptionsfU in two steps.
First,weprojecte ∗ intothetokenembeddingspaceofthe
LLM(Qwen3-14B(Yangetal.2025)inourimplementation)
via a cross-attention projector:
p= Proj(e ∗;W p),(5)
wherepis a sequence of vectors representing the projection
ofe ∗ in the LLM’s token embedding space, also referred to
as soft prompt tokens (Lester, Al-Rfou, and Constant 2021),
andW p denotes the learnable projection parameters. The
softprompttokenscanbedirectlyfedintotheLLMasinput,
enabling the LLM to interpret the semantic meaning ofe∗
through autoregressive generation.
Next, we adopt Low-Rank Adaptation (LoRA) (Hu et al.
2022) to fine-tune the LLM in a parameter-efficient manner
for more contextually grounded and meaningful feature de-
coding in the social media domain. The decoding process is
then defined as:
D(e∗) = LLMD ⟨pins,p⟩;W l  ,(6)
whereLLM D(·)denotes the autoregressive decoding pro-
cess of the LLM, which takes as input the token embed-
dingsp ins of a predefined instruction (e.g., “describe the
textual and visual theme, structure, rhetoric, and emotion
of this post”) concatenated withp, and outputs the decoded
featuresasstructurednatural-languagedescriptions.W l de-
notes the LoRA parameters, and the instruction serves as a
task-specific prompt to guide the decoding process.
To train the decoderD, we first construct a large-scale
trainingcorpusS={(c i, fi)}N i=1,whereeachempiricalpost
ci isannotatedbyGPT-5(OpenAI2025)withtargetnatural-
language descriptionsf i across the applicable textual and
visual dimensions. During training, we feedei =E(c i)into
the decoder, and optimizeDusing the standard token-level
cross-entropy loss for autoregressive language modeling:
Ldec =− 1 N
NX
i=1
MiX
j=1
logP D

yi,j |y i,<j,e i

,(7)
where each target featurefi is tokenized into a sequence
ofM i tokens{y i,1, yi,2, . . . , yi,Mi },P D(· | ·)denotes the
next-token distribution induced by the decoder, andyi,<j
represents the previously generated tokens.E(·)is the same
pre-trained multimodal encoder introduced above.
We jointly optimize the projection parametersWp and
the LoRA adaptersW l in an end-to-end manner, aligning
numerical features with the LLM’s semantic space while
improving linguistic quality and structural consistency. To
furtherenhancerobustness,weinjectGaussiannoiseintoe i
during training, encouraging the decoder to remain stable
under feature perturbations.
Audience-Susceptible Content Generation
Finally, we generate the optimal multimodal contentc∗ that
maximizes diffusion influence within the target audience,
conditioned on the decoded audience-susceptible features
fU and the source contentc in. Notably, the optimization
objective in Eq. (2) is inherently non-convex, so different
initializationsmayconvergetodistinctlocaloptimae ∗.This
suggests that the audienceUis characterized by multiple
coexisting interest modes rather than a single homogeneous
preference. Capturing such diversity is essential for accu-
rately modeling audience heterogeneity and for generating
highly effective, audience-susceptible content.
Toaccountforthis,insteadofrelyingonasinglesolution,
we consider multiple audience-susceptible feature optima
{e∗ 1,e ∗ 2, . . . ,e∗ m}obtained by solving Eq. (2) frommdi-
verse initialization points{E(c1),E(c 2), . . . ,E(cm)}. Here,
{c1, c2, . . . , cm}areseedpostsselectedfromthedatasetvia
farthest-point traversal (Gonzalez 1985) to ensure coverage
and diversity. Based on these feature optima, we generatem
candidate multimodal posts{c (i)}m i=1, with eachc (i) con-
taining textual contentc(i) t and visual contentc(i) v :
⟨c(i) t , p(i)⟩=G text  cin,D(e ∗ i )  ,(8)
c(i) v =G img  p(i) ,(9)
whereG text(·)denotesalargelanguagemodelthatgenerates
textualcontentandanimage-generationpromptp (i),G img(·)
denotesatext-to-imagegeneratorthatsynthesizesvisualcon-
tent (GPT-4o (Hurst et al. 2024) and FLUX.2 (Black Forest
Labs 2025), respectively, in our implementation).D(·)is
the decoder introduced in Eq. (6). Specifically,Gtext uses
D(e∗ i )torewritec in accordingtothedecodedtextualtheme,
structure, rhetoric, and emotion, while generatingp(i) based
onc in and the corresponding decoded visual features along
the same four dimensions. The final output is chosen as the
candidate with the highest predicted diffusion influence:
c∗ = arg max
c(i), i∈{1,...,m}
LU

E(c (i))  .(10)
Experiments
We evaluate the proposed framework through quantitative
andqualitativecomparisonswithbaselines,auserstudy,and
ablation studies.
Experimental Setups
Implementation Details.We implement the three mod-
ules of our framework as follows. For feature optimization,
wesettheregularizationweightλ= 5.0andthetemperature
τ= 0.05, and optimize each candidate via gradient ascent

Figure3:QualitativecomparisonwithbaselinesonMovie.Eachmultimodalpostisannotatedwithitspredictedinfluencescore.
Dataset Method Diffusion Gain (%)↑Consistency↑
Movie
LLM-Zero-shot 0.55±0.600.8722±0.0031
LLM-Instruction 1.15±0.61 0.8680±0.0030
IC-L 1.30±0.13 0.8654±0.0061
Designed2Spread 4.49±0.13 0.8648±0.0010
Ours 16.51±0.410.7783±0.0257
SpaceX
LLM-Zero-shot 2.72±2.01 0.8622±0.0027
LLM-Instruction 5.44±2.13 0.8546±0.0036
IC-L 6.91±2.750.8637±0.0042
Designed2Spread 12.01±1.72 0.8580±0.0037
Ours 40.70±2.010.7756±0.0052
Table1:ComparisonresultsonMovieandSpaceX(mean±
standard deviation over three runs; best results in bold).
using the AdamW optimizer with a learning rate of0.5for
300steps. For feature decoding, the feature decoderDcom-
prises a cross-attention projector that maps the optimized
featuree ∗ into16soft prompt tokens, which are prepended
to a Qwen3-14B backbone quantized to 4-bit NF4. The pro-
jectorparametersW p andtheLoRAadaptersW l withrank
16andα= 32arejointlyfine-tunedforupto30epochs,with
Gaussiannoiseofstandarddeviationσ= 0.005injectedinto
ei during training to enhance robustness. For content gener-
ation, we adopt a multi-start strategy withm= 6for Movie
andm= 10for SpaceX. Theminitialization points are se-
lected from the seed tweets via farthest-point traversal, with
the seed post having the highestLU selected first.
Baselines.We compare our approach with four baselines
spanningthreecategories,distinguishedbytheirlevelofau-
dience awareness and whether training is required (see Sup-
plementary Material): (1)Audience-agnostic.LLM-Zero-
shotdirectly prompts an LLM to rewrite the input content
without any audience-specific guidance.LLM-Instruction
augments the prompt with manually specified dimension-
level instructions, but still lacks explicit modeling of the tar-
getaudience.(2)Audience-aware,training-free.In-Context
Learning (IC-L)(Brown et al. 2020) retrieves, for each au-
dience group, high- and low-influence messages (measured
byL U) as positive and negative exemplars, respectively,
to guide generation via few-shot prompting. (3)Audience-
aware,training-based.Designed2Spread(Qianetal.2026)
employs a single-agent rewriting framework, leveraging
STEPPS(BergerandMilkman2012)andapredefinedvisual-
empiricalfeatureactionspacetoiterativelyoptimizecontent
fordiffusion.Forafaircomparison,allmethodsusethesame
text-generation LLM and image generator, with identical in-
ference settings, to produce the final multimodal content.
Datasets.WeconstructtwoTwitter/Xdatasets,eachrepre-
sentingadistinctinterest-drivenaudiencegroup.TheMovie
dataset focuses on movie-related discussions and contains
124,336users and2,910,600tweets (1,699,675with im-
ages).TheSpaceXdatasettargetsSpaceX-relatedtopicsand
comprises89,663usersand2,217,930tweets(620,025with
images). Following prior work (Qian et al. 2026), data col-
lection proceeds in three steps: we first retrieve5,000seed
tweets for each topic (posted between July 2024 and De-
cember 2025) via keyword-based search, then construct the

target audience group by identifying users who directly en-
gage with these tweets, and finally aggregate the historical
posts of these users to form the dataset.
Forfeatureoptimization,thevMFkerneldensityestimator
inEq.(3)usesallseedtweetsasthereferenceset.Forfeature
decoding, we train a separate decoder for each dataset on
its own annotated corpus, comprising both seed tweets and
additional relevant content, with a3:7ratio of text-only to
multimodalpostsandatotalof75,000annotatedpostsacross
the two datasets (see Supplementary Material). For content
generation, we use GPT-5 to produce200short advertise-
ments for non-tangible products and services as evaluation
inputs. Among them, the160samples with the highest pre-
dictedinfluenceL U areusedtotrainDesigned2Spread,while
the remaining40form a shared test set for all methods.
Metrics.Followingpriorwork(Qianetal.2026),weeval-
uatethegeneratedcontentc ∗ usingtwocomplementarymet-
rics. (1)Diffusion Gain: the relative percentage increase in
the predicted diffusion influence score of the generated con-
tentc ∗ overtheinputcontentc in,measuringimprovementin
expected propagation. (2)Consistency: the cosine similarity
betweenthefeaturerepresentationsofc ∗andc in,quantifying
the degree to which the generated content remains semanti-
cally consistent with the input.
Comparison Results
Quantitative Comparison.Table 1 summarizes the per-
formance of methods in terms ofDiffusion GainandCon-
sistency.OurapproachconsistentlyachievesthehighestDif-
fusion Gain across both datasets, with a substantial margin
over all baselines. On theMoviedataset, it attains a gain
of16.51%, substantially outperforming the strongest base-
line. The advantage is even more pronounced onSpaceX,
where our method reaches40.70%, compared to12.01%
for Designed2Spread,6.91%for IC-L, and5.44%for LLM-
Instruction. In terms of Consistency, our method achieves
0.7783on Movie and0.7756on SpaceX, slightly lower
than more conservative baselines (e.g., LLM-Zero-shot at
0.8722). This reflects an inherent trade-off: maximizing au-
dience resonance requires non-trivial modifications to the
original content, which reduces consistency with the input.
Importantly, these scores remain reasonably high, while the
qualitativecomparisonfurtherconfirmsthatourmethodpre-
serves the core message and semantics despite adapting the
textualandvisualpresentation.Thesamepatternisobserved
across additional LLM backbones (details are provided in
Supplementary Material).
Qualitative Comparison.Figure 3 illustrates the effec-
tiveness of our framework in translating latent audience-
susceptible features into coherent multimodal content. In
contrast to standard baselines (e.g., LLM-Zero-shot, IC-L),
which tend to produce generic text and imagery closely
aligned with the literal prompt, our method adaptively re-
shapes both narrative and visual semantics to enhance audi-
enceresonance.Forexample,intheretirementplanningsce-
nario (left), baseline methods generate predictable “sunny
beach” visuals accompanied by conventional promotional
Dataset Method Diffusion Gain (%)↑Consistency↑
Movie
w/oR vmf 14.92±0.68 0.7771±0.0147
w/o Feature Opt. 16.07±0.40 0.7697±0.0107
w/o Feature Decoding 7.96±0.440.8663±0.0016
w/o Multi-Start 11.57±0.34 0.8170±0.0102
Ours 16.51±0.410.7783±0.0257
SpaceX
w/oR vmf 33.83±1.47 0.8115±0.0102
w/o Feature Opt. 37.90±0.51 0.7914±0.0074
w/o Feature Decoding 23.84±0.400.8520±0.0027
w/o Multi-Start 34.00±0.25 0.8081±0.0007
Ours 40.70±2.010.7756±0.0052
Table 2: Ablation results on Movie and SpaceX (mean±
standard deviation over three runs; best results in bold).
language. By contrast, our approach introduces a high-
arousalnarrativehook(e.g.,framinglifeasa“stressedmovie
character”) together with a dramatic, high-contrast visual
composition, effectively positioning the service as a com-
pellingresolutiontouncertainty.Similarly,forthehealthcare
prompt (right), while Designed2Spread relies on abstract,
impersonal digital motifs, our framework produces content
groundedinrelatable,empatheticcontexts—combiningcon-
versationaltextwithwarm,intimatedomesticimagery.These
results demonstrate that our diffusion-oriented framework
goes beyond surface-level prompt alignment by operational-
izinglatentaudience-susceptiblepatternstogenerateseman-
tically coherent and engaging content.
UserStudy.Tocomplementtheabovemetricswithhuman
perception, we conducted a user study on the Prolific plat-
form(Prolific2026)toassesswhetherourgeneratedcontent
is more likely to be shared in realistic settings. We recruited
50participantswhoactivelyengagewithmovie-relatedcon-
tentonTwitter/X.Eachparticipantevaluatedabout100pairs
of multimodal posts, where each pair consisted of one post
generated by our method and one by the strongest baseline,
Designed2Spread, presented in randomized order. For each
pair, participants selected the version they would be more
willing to repost, comment on, or share. Following (Qian
et al. 2026), we report the mean participant-levelRepost
Preference Rate(RPR), defined for each participant as the
proportion of comparisons in which our method is preferred
overthebaseline.Ourapproachachievesameanparticipant-
level RPR of64.27%, significantly above chance under a
one-sided one-samplet-test against0.5(p= 6.94×10 −7).
These results further demonstrate that our framework pro-
duces more engaging multimodal content from the perspec-
tive of real users (see Supplementary Material).
Ablation Study
We evaluate the vMF regularizer in Feature Optimization
and the contribution of the three main modules.
w/o vMF Regularization (Rvmf).TheR vmf term con-
strains the optimized featuree∗ to high-density regions of
the realistic content manifold. Removing it reduces Diffu-
sion Gain on both datasets, including a drop from40.70%
to33.83%on SpaceX, as the optimization may drift toward
out-of-distribution regions. Although Consistency increases

Figure 4: Audience-specific generations for Movie and
SpaceXfromthesamesourcecontent.Eachgeneratedmulti-
modalpostisannotatedwithitspredictedinfluencescorefor
thecorrespondingdataset,whilethesourcepostisannotated
with both scores in Movie/SpaceX order.
to0.8115on SpaceX, the decoded features are less effec-
tive at increasing predicted diffusion influence. This result
demonstrates the importance of vMF regularization for ob-
taining influential and plausible features.
w/oFeatureOptimization.WeremoveFeatureOptimiza-
tion by directly decoding each initial representationE(ci)
without solving Eq. (2). Diffusion Gain decreases from
16.51%to16.07%on Movie and from40.70%to37.90%
on SpaceX. Consistency changes only slightly, decreasing
from0.7783to0.7697onMovieandincreasingfrom0.7756
to0.7914on SpaceX. These results show that Feature Opti-
mizationconsistentlyimprovespredicteddiffusioninfluence,
while its effect on semantic preservation exhibits no clear
trend across datasets.
w/o Feature Decoding.We remove the decoderD, run
LLM-Zero-shotmtimes, and retain the candidate with the
highestL U, matching our method’s number of content-
generationcallswhileremovingfeatureguidance.Thisvari-
ant causes the largest reduction in Diffusion Gain, reaching
only7.96%on Movie and23.84%on SpaceX. Although
Consistency increases to0.8663and0.8520, the generated
contentbecomesmoreconservativeandlessinfluential.This
confirms that Feature Decoding is crucial for translating op-
timized representations into audience-specific guidance.
w/o Multi-Start Generation.We use a single initializa-
tion and generate all candidates from the resulting decoded
feature. Diffusion Gain decreases to11.57%on Movie and
34.00%on SpaceX, indicating that a single optimum can-
notcaptureheterogeneousaudienceinterests.Despitehigher
Consistency scores of0.8170and0.8081, the resulting con-
tent achieves lower predicted diffusion influence. This result
highlightsthevalueofmulti-startexplorationforidentifying
diverse and influential generation directions.
Figure5:Trade-offbetweenDiffusionGainandConsistency.
Discussion
The performance of our framework is closely linked to the
diversity of susceptible features. To determine the optimal
numberoffeaturesm,weconductasensitivityanalysisover
m∈ {1,2, . . . ,100}. As illustrated in Figure 5, Diffusion
Gainincreaseswithmbeforeplateauing,whileConsistency
with the original content generally decreases. This trade-
off reflects a tension in diffusion-oriented generation, where
improving diffusion may require departing from the source
semantic space. Based on the “elbows” of the curves, we
selectm= 6for Movie andm= 10for SpaceX to balance
engagement potential and message integrity.
Beyondthisquantitativetrade-off,Figure4illustrateshow
theframeworkadaptssourcecontenttodifferenttargetaudi-
ences. For the “Pet Insurance” example, the Movie version
introduces cinematic metaphors such as “auditioning for an
action movie” and high-drama visual compositions. In con-
trast, the SpaceX version employs technical and aspirational
cues such as “came through like liftoff,” accompanied by
launch-inspired visual rhetoric. These results demonstrate
that our diffusion-oriented approach does not merely apply
generic enhancements; instead, it reconfigures content se-
mantics to align with the latent susceptibility patterns of the
target audience, thereby facilitating multimodal persuasion.
Conclusion
We present a three-stage framework for diffusion-oriented
content generation via audience-susceptible feature discov-
ery. For a target audience group, the framework optimizes
propagation-aware latent features on the realistic content
manifold,decodesthemintostructurednatural-languagede-
scriptions, and uses these descriptions to guide multimodal
content generation conditioned on the source content. Ex-
periments on two real-world social media datasets show
substantial gains in predicted diffusion influence, while ab-
lation studies validate the contribution of each module. A
user study further shows that participants prefer our gener-
ated content over that of the strongest baseline. Together,
these results demonstrate the value of translating latent in-
fluence signals into interpretable and actionable guidance
foraudience-awarecontentrewriting.Nevertheless,applica-
tionsinsensitivedomainsrequirestrongersafeguardsagainst
misleading or harmful content. Future work will further in-
vestigate robustness, fairness, safety, and human oversight.

References
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; et al. 2023. Gpt-4 technical report.arXiv
preprint arXiv:2303.08774.
Banerjee,A.;Dhillon,I.S.;Ghosh,J.;Sra,S.;andRidgeway,
G. 2005. Clustering on the Unit Hypersphere using von
Mises-Fisher Distributions.Journal of Machine Learning
Research, 6(9).
Barcelos,R.H.;Dantas,D.C.;andSénécal,S.2018. Watch
yourtone:Howabrand’stoneofvoiceonsocialmediainflu-
encesconsumerresponses.JournalofInteractiveMarketing,
41(1): 60–80.
Berger, J.; and Milkman, K. L. 2012. What makes online
content viral?Journal of marketing research, 49(2): 192–
205.
Black Forest Labs. 2025. FLUX.2: Frontier Visual Intelli-
gence. https://bfl.ai/blog/flux-2.
Borghouts, J.; Huang, Y.; Hopfer, S.; Li, C.; and Mark, G.
2024.Wordingmatters:theeffectoflinguisticcharacteristics
and political ideology on resharing of COVID-19 vaccine
tweets.ACMTransactionsonComputer-HumanInteraction,
31(4): 1–23.
Brown,T.;Mann,B.;Ryder,N.;Subbiah,M.;Kaplan,J.D.;
Dhariwal,P.;Neelakantan,A.;Shyam,P.;Sastry,G.;Askell,
A.; et al. 2020. Language models are few-shot learners.Ad-
vances in neural information processing systems, 33: 1877–
1901.
Chan, I. C. C.; Chen, Z.; and Leung, D. 2023. The more the
better? Strategizing visual elements in social media market-
ing.Journal of Hospitality and Tourism Management, 54:
268–289.
Coppolillo,E.;Cinus,F.;Minici,M.;Bonchi,F.;andManco,
G. 2025. Engagement-driven content generation with large
language models. InProceedings of the 31st ACM SIGKDD
Conference on Knowledge Discovery and Data Mining V. 2,
369–379.
Dang,I.C.;Kwan,C.M.;Jia,J.S.;andShi,Y.2026. When
Words Meet Visuals: How Content Composition Drives So-
cial Media Engagement for Marketer-Generated Content.
Journal of Marketing Research, 63(1): 167–190.
Džanko, L.; Suitner, C.; Erseghe, T.; Nikadon, J.; and For-
manowicz, M. 2025. Linguistic features influencing infor-
mation diffusion in social networks: A systematic review.
Computers in Human Behavior Reports, 18: 100626.
Gligorić,K.;Anderson,A.;andWest,R.2019.Causaleffects
ofbrevityonstyleandsuccessinsocialmedia.Proceedings
of the ACM on human-computer interaction, 3(CSCW): 1–
23.
Gonzalez, T. F. 1985. Clustering to minimize the maximum
interclusterdistance.Theoreticalcomputerscience,38:293–
306.
Hu,E.J.;Shen,Y.;Wallis,P.;Allen-Zhu,Z.;Li,Y.;Wang,S.;
Wang,L.;andChen,W.2022. LoRA:Low-RankAdaptation
of Large Language Models. InInternational Conference on
Learning Representations.
Hurst, A.; Lerer, A.; Goucher, A. P.; Perelman, A.; Ramesh,
A.; Clark, A.; Ostrow, A.; Welihinda, A.; Hayes, A.; Rad-
ford, A.; et al. 2024. Gpt-4o system card.arXiv preprint
arXiv:2410.21276.
Kanuri,V.K.;Hughes,C.;andHodges,B.T.2024. Standing
out from the crowd: When and why color complexity in so-
cial media images increases user engagement.International
Journal of Research in Marketing, 41(2): 174–193.
Kempe, D.; Kleinberg, J.; and Tardos, É. 2003. Maximizing
thespreadofinfluencethroughasocialnetwork. InProceed-
ings of the ninth ACM SIGKDD international conference on
Knowledge discovery and data mining, 137–146.
Lester, B.; Al-Rfou, R.; and Constant, N. 2021. The power
of scale for parameter-efficient prompt tuning. InProceed-
ingsofthe2021conferenceonempiricalmethodsinnatural
language processing, 3045–3059.
Li, M.; Zhang, Y.; Long, D.; Chen, K.; Song, S.; Bai, S.;
Yang, Z.; Xie, P.; Yang, A.; Liu, D.; et al. 2026. Qwen3-
VL-EmbeddingandQwen3-VL-Reranker:AUnifiedFrame-
workforState-of-the-ArtMultimodalRetrievalandRanking.
arXiv preprint arXiv:2601.04720.
Matz, S. C.; Teeny, J. D.; Vaid, S. S.; Peters, H.; Harari,
G.M.;andCerf,M.2024. ThepotentialofgenerativeAIfor
personalized persuasion at scale.Scientific Reports, 14(1):
4692.
OpenAI. 2025. GPT-5. https://openai.com/index/
introducing-gpt-5/.
Peng,Y.;Lock,I.;andAliSalah,A.2024. Automatedvisual
analysis for the study of social media effects: Opportunities,
approaches, and challenges.Communication Methods and
Measures, 18(2): 163–185.
Philp,M.;Jacobson,J.;andPancer,E.2022.Predictingsocial
mediaengagementwithcomputervision:Anexaminationof
foodmarketingonInstagram.JournalofBusinessResearch,
149: 736–747.
Pillai, R. G.; Fokkens, A.; and van Atteveldt, W. 2025.
Engagement-driven persona prompting for rewriting news
tweets. InProceedings of the 31st International Conference
on Computational Linguistics, 8612–8622.
Prolific. 2026. Prolific: Participant recruitment for online
research. https://www.prolific.com. Accessed: 2026-05-06.
Qian, Z.; Lei, J.; Dang, S.; and Cao, N. 2026. Designed to
Spread:AGenerativeApproachtoEnhanceInformationDif-
fusion. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 40, 944–952.
Rombach,R.;Blattmann,A.;Lorenz,D.;Esser,P.;andOm-
mer, B. 2022. High-resolution image synthesis with latent
diffusion models. InProceedings of the IEEE/CVF confer-
ence on computer vision and pattern recognition, 10684–
10695.
Xie, J.; and Liu, L. 2022. Identifying features of source
andmessagethatinfluencetheretweetingofhealthinforma-
tion on social media during the COVID-19 pandemic.BMC
Public Health, 22(1): 805.
Yang,A.;Li,A.;Yang,B.;Zhang,B.;Hui,B.;Zheng,B.;Yu,
B.;Gao,C.;Huang,C.;Lv,C.;etal.2025. Qwen3technical
report.arXiv preprint arXiv:2505.09388.

Yu, E.; Li, J.; and Xu, C. 2024. RePALM: Popular Quote
Tweet Generation via Auto-Response Augmentation. In
Findings of the Association for Computational Linguistics:
ACL 2024, 9566–9579.
Yu,J.;andEgger,R.2021. Colorandengagementintouristic
Instagrampictures:Amachinelearningapproach.Annalsof
Tourism Research, 89: 103204.
Zhao, Y.; Wang, Y.; Cheng, X.; Tumlin, A. M.; Liu, Y.; Xia,
D.; Jiang, M.; and Derr, T. 2025. Amplifying Your Social
Media Presence: Personalized Influential Content Genera-
tion with LLMs.arXiv preprint arXiv:2505.01698.
