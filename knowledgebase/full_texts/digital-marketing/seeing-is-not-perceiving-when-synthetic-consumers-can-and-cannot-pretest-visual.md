---
title: 'Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing'
url: https://arxiv.org/abs/2609.25677
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- "Yi-Lin Tsai</name>\n      <arxiv:affiliation>Arvin</arxiv:affiliation>\n    </author>\n    <author>\n\
  \      <name> Yung-Hsiu</name>\n      <arxiv:affiliation>Arvin</arxiv:affiliation>\n    </author>\n\
  \    <author>\n      <name> Lai"
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.25677
pages: 58
chars: 127219
fetched_at: '2026-11-08T13:19:07+00:00'
kb_version: 1
---

# Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest Visual Marketing

Seeing Is Not Perceiving:
When Synthetic Consumers Can and Cannot Pretest Visual
Marketing
Yi-Lin Tsai∗ Yung-Hsiu (Arvin) Lai∗
Department of Management and Marketing, The University of Melbourne
yilin.tsai@unimelb.edu.au yunghsiu.lai@unimelb.edu.au
Abstract
Marketers now deploy generative AI agents as synthetic consumers to pretest visual assets such
as logos, packaging, and advertising at a fraction of human-panel cost. However, this procedure
assumes that a model seeing a visual cue can also perceive its consumer meaning, which is largely
untested. We stress-test the assumption using six canonical visual marketing experiments, varying
the two levers managers control: model generation (GPT-4o-mini vs. GPT-5.4-mini) and input
format (plain text vs. JSON). Every resulting configuration passed the manipulation checks;
however, none of the configurations reproduced more than two of the six human effects, and the
remainder were nonsignificant. The one exception was a significant reversal of the human pattern.
Providing conceptual or empirical evidence through in-context learning steers average responses
towardthehumaneffect. Yetsteeringhasalimit: evenwhenitsucceeds,aconfigurationreproduces
lessthanhalfofthenaturalspreadofhumanresponsesandsounderstatesconsumerheterogeneity.
We integrate these results into an AI governance protocol (Calibrate, Intervene, Deploy) that
delineates when synthetic consumers can responsibly screen creatives and when human panels
remain necessary.
Keywords:synthetic consumers; silicon sampling; generative AI; visual marketing; in-context
learning; AI governance
∗The authors contributed equally to this work.
1
arXiv:2609.25677v1  [cs.AI]  22 Sep 2026

1. Introduction
Marketing persuades through the eye. Virtually every advertisement contains visual stimuli, and
muchofmarketingcommunicationworksthroughvisualsalone: alogo’sshape,apackage’scolor,
a product image. The pictorial element of an ad captures attention independent of its size (Pieters
& Wedel, 2004), and the mere presence of an image lifts consumer engagement with brand posts
(Li & Xie, 2020). Generative AI has lowered the cost of creating these assets: 37% of marketers
alreadyusegenerativetools(Thormundsson,2024),andtheoutputincreasinglyrivalsprofessional
creative work (Hartmann et al., 2025). The binding constraint has therefore shifted downstream,
from creating variants to evaluating them. For instance, which of fifty logo drafts will consumers
read as authentic or exciting? Getting that read wrong is costly. The same visual choice can raise
engagementforonebrandanddepressitforanother,whichiswhyrecentworkurgesfirmstopretest
visual assets before deployment (Adam & Yang, 2026). Nowadays vendors also sell an answer:
synthetic consumers. These AI agents, prompted to respond to a stimulus as a human respondent
would,promisecreativepretestingatafractionofthecostandtimeofahumanpanel(e.g.,Toluna,
2025).
On text-based tasks, the record appears to justify the promise. Large language models (LLMs)
have reproduced human behavior in economic games and market scenarios (Horton et al., 2026),
matched the response patterns of opinion polls (Argyle et al., 2023), and generated willingness-to-
pay estimates close to human benchmarks (Brand et al., 2023). In the strongest demonstration to
date,anLLMpredictedtheoutcomesof70preregisteredsurveyexperimentsaboutasaccuratelyas
pooled human forecasters (Ashokkumar et al., 2026). This practice has a name, silicon sampling:
prompting an LLM to answer as a specified human respondent would (Sarstedt et al., 2024). A
managerwhohaswatchedthesemodelspredictinghumansurveydatamayreasonablyassumethat
evaluating a logo or ad copy is a short step away.
However,thisextrapolationtothevisualdomain,wherecreativebudgetsareprimarilyallocated,
remainslargelyuntested,evenasgenerativeAIspreadsthroughthemarketing-researchtoolkitfaster
thanitsvalidityisestablished(Joerling,2026). Avisualcueinfluencesconsumerjudgmentthrough
implicit semantic associations rather than the explicit reasoning that text benchmarks reward. We
therefore distinguish seeing, the literal extraction of an image’s physical features, from perceiving,
themappingofthosefeaturesontolatentconsumermeaning. Consumersimplicitlyassociatefaded,
less-saturatedcolorswithtemporallydistantevents(Leeetal.,2017);amodelcanreportanimage’s
saturation level exactly and still miss what the fading signals about time. Our data show that the
gap is not hypothetical. With no intervention, a widely used commercial model judged a product
bearinganangularlogosignificantlymorecomfortablethanthesameproductwithacircularlogo,
reversing a canonical finding in visual marketing (Jiang et al., 2016). A manager who trusted that
pretest would select the wrong design. Deployed without validation, a synthetic consumer is not a
shortcut. Instead, it becomes a governance risk (Gao et al., 2025; Sarstedt et al., 2024).
A reversal of this kind changes the question a firm faces. Before trusting a synthetic consumer
with a visual asset, a manager needs to know where the agent’s judgment fails, whether it can be
repaired, and what the repaired agent still cannot deliver. We therefore ask: (1) Where and why
does a synthetic consumer’s judgment of a visual asset diverge from the human benchmark, even
when it sees the cue? (2) Can evidence from the human benchmark steer a misaligned synthetic
consumer back toward it, and does success depend on how the agent is configured? and (3) When
steering succeeds, does the agent reproduce the full distribution of human responses?
2

To answer these questions, we stress-test synthetic consumers in six canonical visual market-
ing experiments, spanning logo descriptiveness, shape, symmetry, and stability as well as color
saturation in the image, with each panel matched to the original study’s human sample (69 to 220
respondentsperstudy; morethan800syntheticrespondentsperconfiguration). Allsixbenchmark
experiments were preregistered. Each runs in every cell of a two (model generation: GPT-4o-mini
vs. GPT-5.4-mini) by two (input format: plain text vs. JSON) design, the two levers a marketer
controls in practice. To test steering, we then supply in-context evidence in two doses: conceptual
evidence states the original study’s theory, and empirical evidence adds its statistics, the upper
bound of steering a firm could attempt. Each synthetic respondent returns a numerical rating and
a textual rationale. Topic-modeling the rationales allows us to separate seeing from perceiving.
This research makes three contributions. First, in response to calls to validate generative AI
outputs before marketers rely on them (Grewal et al., 2025; Sarstedt et al., 2024), we extend
silicon sampling to the visual domain and show that synthetic consumers see reliably but perceive
inconsistently. Allfourconfigurationspassedeveryvisualmanipulationcheck,yetnonereproduced
more than two of the six benchmark effects, and the rationales trace the failures to missing or
competing semantic associations. Unlike in the text domain, this is a gap to which marketers
should be alert.
Second, responding to calls to evaluate silicon samples on distributions rather than averages
alone (Bisbee et al., 2024; Peng et al., 2025), we document where steering succeeds and where it
stops. Evidencefromthehumanbenchmarkpullsaverageresponsesbacktowardthehumaneffect,
farmoreeffectivelyforthenewermodelgeneration. However,recoveringconsumerheterogeneityis
adifferentmatter: noconfigurationreproducesevenhalfofthenaturalspreadofhumanresponses,
and varying persona demographics does not restore it. Calibrated synthetic consumers therefore
suit average-effect questions and remain unreliable for segmentation or targeting.
Third, we integrate the diagnosis and this boundary into a three-step governance protocol
(Calibrate, Intervene, Deploy), answering calls for control mechanisms in responsible generative
AIuse(Aroraetal.,2025;Blanchardetal.,2025). Theprotocoldelineatesthedecisionsacalibrated
agent can support; however, only a human panel can reveal how consumers will differ.
2. Theoretical background
2.1. Synthetic consumers as simulators of human behavior
Research on silicon sampling answers recent calls to validate generative AI outputs (Grewal et al.,
2025)bytestingwhetherLLMscanserveasproxiesforhumansubjects. However, assummarized
in Table 1, the extent to which these silicon samples can faithfully simulate human behavior
remains contested (Blythe et al., 2025). Gao et al. (2025) show that models diverge from human
participants in economic games and that their answers are sensitive to the wording of the prompt.
More importantly, previous replications have relied predominantly on unimodal, textual inputs
(Argyle et al., 2023; Bisbee et al., 2024; Brand et al., 2023; Horton et al., 2026). The closest
exception is Yoo et al. (2025), which provides a field guide that replicates the research stages
of 35 published articles, including image stimuli from original studies. Their goal, however, is
informal demonstration rather than a test of how models perceive visual cues. Moreover, few of
these studies test whether human-like outcomes rest on the semantic associations that underlie the
humanpathways. GoliandSingh(2024)andAroraetal.(2025)comeclosestbypairingnumerical
3

outcomes with topic models of the language models’ text. Our research extends this paradigm
to the visual domain and pairs mediation analysis with topic modeling, allowing us to ask not
only whether a model reproduces a human outcome but also whether it reproduces the semantic
association underlying the human pathway.
Table 1. Comparison of prior silicon-sample studies
Study Target Domain Input
Theory
Testing Mitigation Mechanism Analysis
Argyle et al.
(2023)
Political survey responses Text No None None
Bisbee et al.
(2024)
Public opinion polling Text No ICL None
Brand et al.
(2023)
Willingness-to-pay Text Yes Fine-tuning a None
Li et al. (2024) Perceptual brand mapping Text Yes ICL (few-shot) None
Goli and Singh
(2024)
Intertemporal preferences Text Yes CoT Topic Model
Toubia et al.
(2025)
Personal traits and
cognition
Text Yes ICL (zero-shot) None
Peng et al.
(2025)
19 behavioral domains Text Yes None None
Arora et al.
(2025)
Qualitative in-depth
interviews
Text No ICL (few-shot)
+ RAG
Topic Model
Yoo et al.
(2025)b
Research-process
demonstrations
Image +
text
Yes None None
Ashokkumar et
al. (2026)
Preregistered survey
experiments
Text Yes None None
Horton et al.
(2026)
Behavioral Economics,
fairness, status quo
Text Yes Persona
calibration
None
This research Perception of visual design Image +
text
Yes ICL (evidence-
based)
Mediation analysis +
topic model
a Human-response data were used to fine-tune the model’s weights.b A field guide for research process; image
stimuli were uploaded where the replicated article used them, and the authors note their comparisons are not exact,
high-powered replications.
2.2. Technical priors versus psychological priors in visual perception
Visual marketing relies heavily on implicit inferences, where subtle design elements (e.g., logo
shape) can trigger latent psychological associations (e.g., perceived comfort) that extend beyond
literal visual recognition (Labrecque & Milne, 2012). The true consumer meaning of a visual
cue is rarely discernible from its surface alone. A picture of a scented object improves product
evaluations by evoking olfactory imagery (Sharma & Estes, 2024), and presenting products jointly
ratherthanseparately liftsevaluationsthroughconsumption imageryandpsychologicalownership
(Zhao & Xia, 2021). In both cases, the effect runs through a simulation in the consumer’s mind,
not through anything a feature detector could read off the pixels. The same surface cue can
also mean opposite things in different brand contexts (Adam & Yang, 2026; Chen et al., 2025),
or move behavior only when its form matches consumers’ internal representations (Kim et al.,
4

2023). Consequently, evaluating whether a synthetic consumer reproduces these associations
requires distinguishing between what the model technically sees and what it actually perceives. A
model trained predominantly on descriptive image–text pairs may read the geometry without the
association it carries for a consumer. Existing AI frameworks in marketing already separate the
processingofobjectivedatafromtheresponsetoemotion(Huang&Rust,2021). Consumersshare
a similar belief, viewing AI as strong in logic but weaker in emotional connection (Xu & Mehta,
2022). The dissociation is visible in field data: an image model trained on objective style labels
predicts them near-perfectly (96.9% accuracy) yet collapses to 62.5% when retrained to predict
human familiarity perceptions of the same images (Xie et al., 2025).
Drawing on Bayesian cognitive modeling, which formalizes human perception and learning
as probabilistic updates (Griffiths et al., 2008), we conceptualize the split between seeing and
perceivingastwolearnedpriorsthatasyntheticconsumerbringstoavisualasset: atechnicalprior
and a psychological prior. We define a prior not as a conscious cognitive state or a parameter we
directly estimate, but as a baseline tendency to interpret a visual cue one way rather than another.
Thetechnicalprioristhebaselinetendencytoextractphysicalfeatures,suchasalogo’sgeometryor
an image’scolor saturation. Thepsychological prior isthe learnedstatistical association thatmaps
those physical features onto latent consumer meaning, such as authenticity or excitement. This
splitmirrorshowhumanvisualperceptionseparatesanimage’sphysicalfeaturesfromitssemantic
meaning (Sample et al., 2020). Image–text training data may describe what an image shows more
often than how it makes a consumer feel, so a model’s technical prior can sometimes overshadow
its psychological prior. A single visual cue can also support several learned associations, so a
model may express a competing psychological prior that is coherent but differs from the human
benchmark. Asyntheticconsumermaythereforepassallvisualrecognitiontestswhilemissingthe
implicit association that humans would form. Whether these two priors dissociate in practice, and
howfarthegapcanbeclosed,aretheempiricalquestionsoursixbenchmarkexperimentsquantify.
2.3. In-context evidence as a steering mechanism
To better activate the target psychological prior, we use In-Context Learning (ICL), a prompt-
based method that does not modify any model weights (Brown et al., 2020). While prior studies
show Chain-of-Thought (CoT) prompting can improve performance on explicit logical tasks (Goli
& Singh, 2024; Kojima et al., 2022) and theory development (Yoo et al., 2025), these step-by-
step rationalizations target explicit reasoning rather than the implicit associations that drive visual
marketing. Similarly,whileRetrieval-AugmentedGeneration(RAG)isrobustforfact-basedqueries
(Aroraetal.,2025),retrievaltargetsfactsratherthanimplicitpsychologicalassociations. Methods
that update the model’s weights, such as fine-tuning on human responses (Brand et al., 2023) or
structured computer-vision models (Dew et al., 2022), may steer a model further, but they need
trainingdataandmodelaccessthatmostpractitionersdonothave. WethereforeselectICL,treating
it as a mechanism for implicit Bayesian inference (Xie et al., 2022). Embedding expert conceptual
orempiricalknowledgedirectlyintothepromptactsascontextualevidence,whichallowsustoshift
the associations the model expresses at a low computational cost. A language model’s tendency
to echo its prompt is what makes steering possible in the first place, but how far that steering
extends when the judgment target is an image rather than text has not been tested. In practice, a
marketer is unlikely to retrain a closed commercial model; she chooses which model generation
to license and how to structure the stimulus input, and text-domain work shows model output is
5

sensitivetoboth(Bisbeeetal.,2024;Heetal.,2024;Toubiaetal.,2025). Wethereforeevaluatethe
robustness of ICL across model generations and input formats. Beyond mean accuracy, given that
LLM-generatedoutputsconsistentlysufferfromvarianceshrinkage(Pengetal.,2025),weevaluate
how effectively this in-context evidence can restore the natural heterogeneity of human responses.
The two priors, the steering mechanism, and the variance concern map one-to-one onto our
research questions posed in Section 1: perceptual misalignment despite accurate seeing (RQ1),
evidence-based steering and its dependence on model generation and input format (RQ2), and
recovery of the full distribution of human responses rather than the mean alone (RQ3). The
answers are integrated into the governance protocol developed in Section 6.
3. Methodology
To compare synthetic consumers’ visual judgments with established human benchmarks, we re-
ran six visual marketing experiments with synthetic respondents. The visual stimuli for these
experiments were drawn directly from six marketing studies. All of our benchmark experiments
were preregistered before data collection (Web Appendix A). For each experiment, two types of
data were collected: (1) a numerical rating mirroring the original study’s dependent variable, and
(2) a textual rationale explaining the basis for that rating. This approach allows us to assess both
the statistical alignment of the output and the semantic associations behind it.
3.1. Overview of the studies
To test the boundary between seeing and perceiving, we selected six canonical studies based on
four criteria: (1) publication in a premier marketing journal (e.g.,Journal of Consumer Research;
Journal of Marketing Research), (2) publicly available visual stimuli, (3) a focus on perceptual
variation rather than objective performance measures (e.g., measuring response time of an LLM
predictionisnotmeaningful),and(4)anestablishedcitationrecordpriorto2020,sothatthefindings
constitute recognizable benchmarks. We also prioritized studies that specified a psychological
pathway, which allows us to compare an outcome with the pathway behind it. We treat the
published results from these six studies as an operational benchmark for comparison with LLM
outputs,notasabsolutegroundtruth. Table2summarizesthesestudies. Fulldetailsonhypotheses
and stimuli are provided in Web Appendix B.
6

Table 2. Summary of the six benchmark studies
# Paper Journal Stimuli Source a Sample Size Citation Countb Human Perception
1 Luffarelli, Mukesh,
and Mahmood
(2019)
JMR 1 180 156 High logo descriptiveness is
associated with high brand
authenticity.
2 Lee et al. (2017) JCR 2A 108 113 Consumers select less-saturated
(more-saturated) images for
temporallydistant(near) events.
3 Jiang et al. (2016) JCR 2 69 380 A circular (angular) logo is
associated with higher (lower)
comfort and lower (higher)
durability.
4 Luffarelli,
Stamatogiannakis,
and Yang (2019)
JMR 1B 220 215 Logo asymmetry is associated
with enhanced excitement.
5 Hagtvedt and Brasel
(2017)
JCR 3 80 237 High color saturation is
associated with a bigger
product size.
6 Rahinel and Nelson
(2016)
JCR 2A 154 67 An unstable logo is associated
with greater utility for
safety-oriented products.
a StimuliSourcegivesthestudy(andstimulusset)intheoriginalarticlefromwhichthestimuliweretaken(e.g.,2A=
Study 2A).b The numbers of citations were obtained in April 2025 from Google Scholar, before our data collection
began.
3.2. Research design using AI participants
We used a four-stage workflow that includes Design, Data Collection, Analysis, and Diagnosis
(Figure 1). This workflow generates the data for the zero-shot baselines that address RQ1.
7

Figure 1. Research design for the AI participants.
3.3. Design and data collection
During the Design phase, we selected two GPT models to serve as synthetic consumers (hereafter,
AI participants): GPT-4o-mini (released in July 2024) and the newer GPT-5.4-mini (released in
March2026),twoversionsofthesamemodelline. 1 Wealsoraneachmodelontwoinputformats:
plain text (TXT) and JSON. This allows us to assess whether perceptual alignment varies between
thetwomodelgenerationsorsimplywithstructuringthepromptinterface. Unlessotherwisenoted,
the main text reports the plain-text runs of each model, GPT-4o-mini (TXT) and GPT-5.4-mini
(TXT).
Toensurethevalidityofoursynthetic-consumersampling,wemadethefollowingconfiguration
decisionsontheparameterstheAPIexposedatthetime. First,wesetthemodeltemperatureto1.0,
theAPIdefaultandthemidpointofits0to2range,sothatresponsesvaryacrossparticipants(Arora
1API model identifiers: gpt-4o-mini and gpt-5.4-mini-2026-03-17.
8

et al., 2025). Second, we kept nucleus sampling (top_p) at its default value of 1. Lowering this
value would cut off the model’s less likely answers and artificially narrow the range of responses
it can produce (OpenAI, 2024). Third, we did not specify a seed parameter due to the realities
of commercial APIs. Although seed-fixing is a customary practice in simulations, the API does
not return the same output even when identical seeds are applied (OpenAI, 2024). Finally, to
support the statistical independence of our synthetic sample, we followed Blanchard et al. (2025)
by initiating a separate API call for every individual AI participant, rather than batch-generating
multiple personas within a single context window, so no context carries over between participants.
The Data Collection phase includes multiple conversations (i.e., API calls) to mirror human
informationprocessing. SeeFigure2foranillustration. InStep1,weinstantiatedtheparticipant’s
persona by providing a demographic profile (age, gender, location) and foundational instructions.
Each AI participant was assigned a demographic profile consistent with the sample used in the
original study. For the studies drawn from U.S. adult samples (Studies 1, 2, and 4), age was
sampled uniformly from 18 to 65, and gender was balanced between male and female. For the
studies drawn from undergraduate samples (Studies 3, 5, and 6), the persona was specified as
an undergraduate student with an age sampled uniformly from an undergraduate range. The
demographic distributions for each study, including the range used in each, are reported in Web
Appendix C. In Step 2, the AI participant was randomly assigned a visual stimulus presented as
a 512×512-pixel PNG file. This resolution was chosen to preserve sufficient visual detail while
maintaining computational efficiency (Hartmann et al., 2025). In Step 3, we prompted the AI to
provide zero-shot numerical ratings for the key dependent variables from the original study. Zero-
shot prompting entails instructing an LLM to perform a task without prior examples of the desired
output (Brown et al., 2020), so that the AI’s ratings reflect the associations the model expresses
withoutanybenchmarkinformation. Thiswasfollowedbyarequestforatextualrationaleforeach
rating in Step 4. Finally, we administered a numerical manipulation check to ensure the stimulus
wasperceivedasintended(Step5). Weadoptedthissequencetomitigatedemandeffects: inquiries
about specific visual features could otherwise cue the model to the manipulated feature before the
focal dependent-variable ratings.
We kept each call stateful by passing the entire prior conversation history (e.g., the assigned
persona, the stimulus, and all previous answers) as input to the next step, keeping responses
consistent with the assigned persona and prior ratings. As shown in Figure 2, the API call for the
Step 4 rationale was explicitly conditioned on the context from Steps 1 to 3. This entire process
was repeated to match the original study’s sample size, rounded up where an odd total could not
be split evenly across conditions.
9

Step 1 : Simulate an AI participant with prompt
You are a {age} {gender} participant who lives in the {locations}.
Please take a moment to look at the logo carefully and wait for my prompt.
{ } : Randomize the AI participant’s demographic
LLM understands the instructions
No problem!
Step 2 : Assign an experiment condition
Market Logos
(512 x 512 pixels)
Less Descriptive More Descriptive
LLM sees the image and waits for the questions
I’ve taken a moment to look at the image. Please go ahead with your questions!
Step 3 : Survey the AI participant (main effect)
Please rate the following attributes based on your impression of the logo.:

1.  Authenticity: To what extent does this logo make the brand seem authentic?
    (1 = Not at all, 9 = Very authentic) 
2. Trustworthiness: To what extent does this logo make the brand seem
    trustworthy? (1 = Not at all, 9 = Very trustworthy) 
3. Credibility: To what extent does this logo make the brand seem credible?
    (1 = Not at all, 9 = Very credible)
LLM provides ratings
Here are my impressions based on the logo:
1.  Authenticity: 6 
2. Trustworthiness: 5 
3. Credibility: 6
Step 4 : Survey the AI participant (rationale for main effect)
Please explain the rationale behind your ratings for the previous questions, including (1 )  Authenticity, (2 )
Trustworthiness, and (3 )  Credibility
LLM provides rationale for main effect
Here’s the rationale behind the ratings : 
1. Authenticity (6 ):  The logo clearly indicates the brand ' s focus on basketball through its imagery
and wording.... . 
2. Trustworthiness (5 ):  The logo communicates a serious intention to represent a specific
industry, but it lacks attributes ... .
3. Credibility (6 ):  Associating with basketball equipment suggests a certain level of expertise,
contributing to credibility. However....
Step 5 : Survey the AI participant (manipulation check)
To what extent does this logo seem descriptive to you?
(1 = Not at all descriptive, 9 = Very descriptive)
LLM provides ratings
I would rate the logo as 6 in terms of descriptiveness.
Step 6 : Extract and Record AI participant’s responses
Ratings for main effect
1. Authenticity: 6 
2. Trustworthiness: 5 
3. Credibility: 6

Rationale for main effect
1. Authenticity (6): The logo clearly indicates the brand's focus on basketball through its imagery and wording..... 
2. Trustworthiness (5): The logo communicates a serious intention to represent a specific industry, but it lacks attributes ....
3. Credibility (6): Associating with basketball equipment suggests a certain level of expertise, contributing to credibility. However....
Manipulation check
4. Descriptive: 6
Figure 2. An example of surveying AI participants using the visual stimuli from Study 1 in
Luffarelli, Mukesh, and Mahmood (2019), implemented through the API.
3.4. Analysis and diagnosis
We replicated the original statistical analyses (e.g., ANOVA) to estimate the main effects using the
AI-generated data. A configuration reproduces a human effect when the AI participants show an
association between the independent and dependent variables that is both statistically significant
and directionally consistent with the original human subjects’ findings. For studies that proposed
10

mediators, we followed the original PROCESS models (Hayes, 2022) using the AI’s numerical
ratings, with the same mediator and outcome measures as the original studies.
The textual rationales (Steps 4 and 6, Figure 2) provide another source of diagnostic data. Our
analysisservestwokeypurposes. First,itverifiesthatthemodelsidentifythetargetvisualfeatures
(e.g., shape or color saturation). Second, the analysis captures nuances that fixed-point rating
scales cannot flexibly represent (Zhang et al., 2024). In instances where an AI fails to reproduce a
human main effect, this diagnostic layer allows us to distinguish the sources of the misalignment.
For example, we can tell if the model defaults to a literal description of image features, or if it
identifies the visual cue but expresses an alternative semantic association (e.g., a more descriptive
logo elicits “professionalism” instead of the intended “ease of processing”). While this procedure
mimics human think-aloud protocols (Ericsson & Simon, 1980), LLM-generated explanations can
beplausibleyetsystematicallyunfaithfultothemodel’sactualdecisionprocess(Turpinetal.,2023).
We therefore treat rationales with the caution recommended for AI-generated outputs (Tomaino et
al., 2025), as observable artifacts rather than the model’s actual thought process.
To analyze these short textual rationales (typically 200–2,000 characters), we needed an NLP
pipeline that could overcome high semantic sparsity. Traditional bag-of-words models like Latent
DirichletAllocation(LDA;Bleietal.,2003)oftenperformpoorlyonshorttextsbecausetheyignore
syntaxandcontextualmeaning(Zhaoetal.,2011). AlthoughBidirectionalEncoderRepresentations
from Transformers (BERT; Devlin et al., 2019) resolves this issue, its native architecture is not
optimized for measuring direct sentence-level similarity. Therefore, we encoded the documents
using Sentence-BERT (SBERT; Reimers & Gurevych, 2019) and clustered them using BERTopic
(Grootendorst, 2022). Moreover, unlike embedding-based alternatives that require researchers to
pre-specifythenumberoftopics,BERTopicusesadensity-basedclusteringalgorithmtodetermine
thenumberofdistincttopics. Givenourper-conditionsamplesizes,thispipelinetypicallyproduced
two to ten topics per condition (technical details are available in Web Appendix D).
4. Results
Table 3 summarizes the zero-shot results of six studies for the plain-text configurations; results for
allfourconfigurationsappearinTable5andWebAppendixE.First,atzero-shot,allconfigurations
passedthemanipulationchecks(e.g.,correctlyidentifyingcircularlogos). Second,wefindthatnone
ofthefourconfigurationssuccessfullyreproducedmorethantwoofthesixcanonicaleffects. Both
GPT-4o-mini configurations reproduced Study 1’s effect, and both GPT-5.4-mini configurations
reproduced the same two: Studies 3 and 5. Notably, 4o-mini (TXT) also generated a statistically
significant directional reversal of a human finding in Study 3. Predicting the opposite of human
judgmentposesagreateroperationalriskthananulleffect,asthesyntheticagentoutputscanleadto
a flawed managerial recommendation. By synthesizing the textual rationales across these failures,
we identify two sources of AI perceptual misalignment. The first is that LLMs successfully
recognize visual features but restrict their evaluation to objective aesthetic properties without
triggering the downstream semantic associations that carry the human effect (e.g., Study 2). The
secondisthatLLMsrecognizethevisualcuebutactivateacompetingpsychologicalpriordifferent
fromthehumanbenchmark(e.g.,Studies1and3). Thiszero-shotperformancethusanswersRQ1.
Amodelthatseesamarketing-relevantvisualcuedoesnotreliablyperceiveitsconsumermeaning
as humans do.
11

Table 3. Zero-shot main effects and manipulation checks by model generation (plain-text
configurations)
4o-mini (TXT) 5.4-mini (TXT)
Study Main effect Manipulation check Main effect Manipulation check
1 (Authenticity)+(<.001)+(<.001)−(.586)+(<.001)
2 (Selected saturation)+(.631)+(<.001)+(.288)+(<.001)
3 (Comfort)−(.012)+(<.001)+(.022)+(<.001)
3 (Durability)−(.177)+(<.001)−(.321)+(<.001)
4 (Excitement)−(.736)+(<.001)−(.383)+(<.001)
5 (Size estimation)+(.052)+(<.001)+(.010)+(<.001)
6 (Utility)−(.136)+(.004)−(.844)+(.017)
Note: Parentheses after study numbers give the dependent variable. “+/−” indicates a direction consistent
(inconsistent) with the human finding; for manipulation checks,+indicates the manipulated feature was rated in the
intended direction (e.g., angular logos rated as more angular). Bold marks significant effects (𝑝 <.05). Study 6’s
main effect is driven by its simple effect within safety-oriented products. JSON results were statistically
indistinguishable at zero-shot; complete results for all four configurations appear in Table 5 and Web Appendix E.
One concern is that reproduction success might simply reflect the model’s prior exposure
to well-known studies.2 If the models were simply recalling these studies, the most-cited and
oldest effects should reproduce best, and none should reverse. We observe the opposite. Most
studies fail at zero-shot and one reverses (Study 3). An exploratory logistic regression predicting
reproduction success from citation count, paper age, sample size, and model likewise finds no
significant predictors, though with only six studies this check has limited power. Given the small
differences in zero-shot results across input formats within each model, we report the findings on
the plain-text configurations. For parsimony, we abbreviate these runs as 4o-mini and 5.4-mini.
4.1. Detailed findings by study
4.1.1. Study1: LogodescriptivenessandbrandauthenticityHumansperceivehighlydescrip-
tive logos as more authentic in Luffarelli, Mukesh, and Mahmood (2019). 4o-mini successfully
reproduced this main effect (MLess_Desc [SDLess_Desc] = 6.198 [.405] vs. MMore_Desc = 6.424 [.354],
F(1, 167) = 14.828,p <.001,𝜂 2 = .082; see Figure 3), with an effect size close to the human
benchmark (𝜂2 = .091). However, while the original study found that ease of processing mediated
this relationship, this indirect effect was not significant for 4o-mini (𝛽=−.053, 95% CI [−.134,
.016]). Logo descriptiveness did not significantly predict ease of processing. Post-hoc textual
analysis revealed that 4o-mini linked its authenticity ratings to “professionalism,” emphasizing
polished design, rather than to ease of processing. This is an example of triggering an alternative
psychological prior, despite the same outcome as the human benchmark.
5.4-mini, in contrast, showed no significant main effect (MLess_Desc [SDLess_Desc] = 4.356 [.507]
vs. MMore_Desc = 4.293 [.970], F(1, 178) = .298,p =.586,𝜂2 = .002). The post-hoc analysis shows
that5.4-minifocusedongeneraldesignqualityratherthanlogodescriptiveness,whichexplainsthe
2GPT-4o-mini training cutoff: October 2023; GPT-5.4-mini training cutoff: August 2025.
12

null result.
5.890
4.820
6.424 6.198
4.293 4.356
p < .001 p < .001 p = .586
1
2
3
4
5
6
7
8
9
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Authenticity Rating
Condition More descriptive logo Less descriptive logo
Figure 3. Authenticity rating by logo descriptiveness.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals. Error bars for the human sample are omitted because the original study
does not report the corresponding standard deviations.
4.1.2. Study2: ColorsaturationandtemporaldistanceHumansassociatelesssaturatedimages
with distant future events (Lee et al., 2017). However, neither 4o-mini nor 5.4-mini reproduced
this association. Neither model showed a significant main effect (4o-mini: MNear [SDNear] = 2.815
[.211] vs. MDistant= 2.796 [.188]; F(1, 106) = .231,p =.631,𝜂2 = .002. 5.4-mini: MNear[SDNear] =
2.080 [.266] vs. MDistant = 2.025 [.274]; F(1, 106) = 1.143,p =.288,𝜂2 = .011; Figure 4), despite
passing the manipulation checks (Table 3; the check measures are described in Web Appendix
B). The results suggest that while LLMs could recognize the visual difference and understand
the temporal prompts, they registered saturation as an aesthetic property but did not connect it to
temporal distance, the association that carries the human effect.
13

2.280 2.080
2.815 2.796
2.080 2.025
p = .030 p = .631 p = .288
1.0
1.5
2.0
2.5
3.0
3.5
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Saturation Levels
Condition Near Distant
Figure 4. Selected saturation by temporal distance.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals.
4.1.3. Study 3: Logo shape and product attributesStudy 3 provides the sharpest contrast
between the two model generations. We used logo shape (circular vs. angular) as the independent
variabletoassesstheimpactonperceivedcomfortanddurability,asinJiangetal.(2016). 4o-mini
ratedproductswithangularlogosmorecomfortablethanthosewithcircularlogos,areversalofthe
human findings (Mangular [SDangular] = 6.829 [.514] vs. Mcircular = 6.514 [.507], F(1, 68) = 6.635,p
= .012,𝜂2 = .089; Figure 5). Additionally, 4o-mini associated circular logos with higher perceived
durability. This estimate, though not statistically significant, was directionally opposite to the
human data (Mangular [SDangular] = 7.343 [.838] vs. Mcircular = 7.600 [.736]; F(1, 68) = 1.861,p=
.177,𝜂 2=.027;Figure6). Inthepost-hoctextanalysis,4o-miniprovidedanalternativeexplanation
by associating an angular logo with “better support” and, therefore, a “more comfortable” sofa.
5.4-mini, in contrast, reproduced the human association on comfort, rating products with
circularlogosasmorecomfortablethanthosewithangularlogos(M circular[SDcircular]=5.314[.471]
vs. Mangular = 5.000 [.642], F(1, 68) = 5.456,p= .022,𝜂2 = .074; Figure 5). The effect size is
slightly larger than the human benchmark (human benchmark:𝜂2 = .071). However, 5.4-mini
failedtoreproducethedurabilityeffect,showingnosignificantdifferencebetweenshapes(M circular
[SDcircular] = 7.000 [.000] vs. Mangular = 6.971 [.169]; F(1, 68) = 1.000,p= .321,𝜂2 = .014). The
circular cell shows zero variance, so we read this test only descriptively. We further find that
the semantic association underlying the pathway showed the same split: For 4o-mini, logo shape
did not predict perceived softness, whereas for 5.4-mini, the indirect effect through softness was
significantforcomfort,asinthehumanbenchmark(TableE3,WebAppendixE).Intherationales,
5.4-mini judged the sofas on “softness” and “comfort,” the benchmark mediator, whereas 4o-mini
explained comfort through “support.” This difference matches their replication outcomes.
14

6.440 5.850 6.514 6.829 5.314 5.000
p < .05 p = .012 p = .022
1
2
3
4
5
6
7
8
9
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Comfortableness Rating
Condition Circular logo Angular logo
Figure 5. Perceived comfort by logo shape.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals.
3.430 4.190
7.600 7.343 7.000 6.971
p < .05 p = .177 p = .321
1
2
3
4
5
6
7
8
9
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Durability Rating
Condition Circular logo Angular logo
Figure 6. Perceived durability by logo shape.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals.
4.1.4. Study 4: Logo asymmetry and perceived excitementHumans associate asymmetrical
images with perceived excitement (Luffarelli, Stamatogiannakis, & Yang, 2019). Neither model
reproduced this association. 4o-mini did not associate logo asymmetry with excitement (MSymm
[SDSymm] = 4.859 [.511] vs. MAsym = 4.836 [.514], F(1, 217) = .114,p =.736,𝜂2 = .001; see
Figure 7). 5.4-mini showed no significant association either, and its estimate was directionally
15

reversed (MSymm [SDSymm] = 3.099 [1.031] vs. MAsym = 2.978 [1.023], F(1, 218) = .765,p =.383,
𝜂2 = .003). Neither model reproduced the main effect, and at zero-shot neither model met the
association criterion for the benchmark’s arousal pathway, which requires a replicated main effect
first (see details in Table E4, Web Appendix E).
3.110
3.740
4.859 4.836
3.099 2.978
p < .001 p = .736 p = .383
1
2
3
4
5
6
7
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Excitement Rating
Condition Symmetrical Asymmetrical
Figure 7. Excitement rating by logo symmetry.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals. Error bars for the human sample are omitted because the original study
does not report the corresponding standard deviations.
4.1.5. Study 5: Color saturation and size estimationHumans associate a more color-saturated
product with a larger estimated size (Hagtvedt & Brasel, 2017). Despite not meeting the repro-
duction criterion, 4o-mini produced a directionally consistent effect with a borderline significant
p-valueandasmallereffectsizethanthehumanbenchmark(M High_Saturation[SDHigh_Saturation]=15.026
[.362] vs. MLow_Saturation= 14.811 [.569], F(1, 74) = 3.895,p =.052,𝜂2 = .050; human benchmark:
𝜂2 = .087; see Figure 8). 5.4-mini reproduced the association (MHigh_Saturation [SDHigh_Saturation] =
14.950 [.316] vs. MLow_Saturation = 14.600 [.778], F(1, 78) = 6.949,p =.010,𝜂2 = .082), with an
effect size closer to humans’.
We followed up by testing whether 5.4-mini, the model that reproduced the main effect, also
reproducedtheassociationsunderlyingthebenchmarkpathway. Theindirecteffectofsaturationon
size through attention, the benchmark pathway in Hagtvedt and Brasel (2017), was not significant
(𝛽= .022, 95% CI [−.169, .226]). In a separate model for the upstream link, the indirect effect of
saturation on attention through arousal was significant (𝛽= .334, 95% CI [.241, .433]; mediation
outcomesaresummarizedinTableE5,WebAppendixE).Themodelthusreproducedtheupstream
links,saturationheighteningarousalanddrawingattention,butattentiondidnotcarrythroughtoa
largersizeestimate. ThisreinforcesthatevenwhenanLLMreproducesamaineffect,thesemantic
association it expresses can deviate from the one underlying the human effect.
16

15.280 14.410 15.026 14.811 14.950 14.600
p < .01 p = .052 p = .010
10
12
14
16
18
20
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Size Rating (Inches)
Condition High saturation Low saturation
Figure 8. Perceived size by color saturation.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals.
4.1.6. Study 6: Logo stability and perceived utilityStudy 6 tests whether the effect of logo
stabilityonperceivedutilitydependsontheproductcategory. RahinelandNelson(2016)showthat
anunstablelogo(e.g.,asquarerotatedonitsvertex)signalsaneedforsafety,therebyincreasingthe
perceived utility of safety-oriented products. We followed their mixed design, with logo stability
and category type as between-subjects factors and product replicate as a within-subjects factor.
Perceived utility is measured as the mean of the usefulness, importance, and usage-likelihood
ratings, averaged over the six products within a category. First, as a background check consistent
withthehumanbenchmark,bothmodelsratedsafety-orientedproductsasmoreusefulthanneutral
products (4o-mini: MSafety= 8.059 vs. MNeutral= 6.977, F(1, 157) = 1373.659,p <.001,𝜂2 = .897;
5.4-mini: MSafety = 7.159 vs. MNeutral = 6.184, F(1, 152) = 324.094,p <.001,𝜂2 = .681). Neither
model, however, showed a main effect of logo stability on perceived utility (4o-mini: F(1, 157) =
.020,p =.888,𝜂 2 = .000; 5.4-mini: F(1, 152) = .481,p =.489,𝜂2 = .003).
Second,weexaminedthelogo-stability×category-typeinteraction. For4o-mini,theinteraction
was significant (F(1, 155) = 4.373,p =.038,𝜂2 = .027), but its source differs from the human
benchmark: The utility rating was lower under the unstable logo in the safety-oriented category
(Munstable [SDunstable] = 8.032 [.141] vs. Mstable = 8.086 [.179], F(1, 78) = 2.269,p =.136,𝜂 2
= .028; see Figure 9) and higher in the neutral category (Munstable [SDunstable] = 7.011 [.188] vs.
Mstable = 6.944 [.215], F(1, 77) = 2.164,p =.145,𝜂2 = .027), with neither simple effect reaching
significance. For 5.4-mini, the interaction was not significant (F(1, 150) = 2.366,p =.126,𝜂2 =
.016); the unstable logo did not increase utility for safety-oriented products (Munstable [SDunstable]
= 7.151 [.407] vs. Mstable = 7.168 [.364], F(1, 74) = .039,p =.844,𝜂2 = .001) but did so in the
neutralcategory(M unstable[SDunstable]=6.258[.261]vs. M stable=6.110[.287],F(1,76)=5.691,p=
.020,𝜂 2 =.070),thecategorywherehumansshownoeffect. Insum,neithermodelreproducedthe
patterninthehumanbenchmarkthatanunstablelogoraisesutilityforsafety-orientedproductsbut
17

not neutral products. 4o-mini’s interaction reflects a crossover pattern opposite to the benchmark,
and 5.4-mini expresses the effect in the wrong category.
5.490 5.000
8.032 8.086
7.151 7.168
p = .004 p = .136 p = .844
1
2
3
4
5
6
7
8
9
Human GPT-4o-mini (TXT) GPT-5.4-mini (TXT)
Perceived Utility
Condition Unstable Stable
Figure 9. Perceived utility by logo stability for safety-oriented products.
Note: Bars show zero-shot (no-intervention) condition means for the human benchmark, 4o-mini, and 5.4-mini. Error
bars represent the 95% confidence intervals. Error bars for the human sample are omitted because the original study
does not report the corresponding standard deviations.
4.2. Robustness of findings
We conducted five robustness checks. First, to assess the stability of the results, we repeated each
between-subjects experiment five times and each within-subjects experiment twice. The results
were stable across these runs (Table F1, Web Appendix F, illustrates with Study 1), so each cell in
the main text reports a single run and the full set of replicates is available on request.
Second, we assessed temperature sensitivity by re-running Study 1 across a range of temper-
atures (0.5, 1.0, and 1.5). The manipulation checks and main effects remained directionally and
statistically consistent (Table F2, Web Appendix F). The response variance stayed narrow across
temperature settings.
Third, we investigated whether different image resolutions affected the LLMs’ judgments. We
foundthatthemanipulationchecksandthemaineffectsremainedstable(TableF3,WebAppendix
F), suggesting our results are not an artifact of the 512×512 standard.
Fourth,amethodologicalconcerninprogrammaticexperimentsisserialcorrelationacrosscon-
secutiveAPIcalls,whichviolatestheindependenceassumption. Weassessedtheserialcorrelation
by modeling the rating𝑌𝑟𝑖 of thei-th AI participant in replicateras a function of the preceding
participant’s rating𝑌𝑟,𝑖−1 in the same replicate:
𝑌𝑟𝑖 =𝛽𝐶𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛 𝑟𝑖+𝜆𝑌 𝑟,𝑖−1+𝜂𝑟+𝜀 𝑟𝑖.
Astatisticallysignificantcarryovercoefficient(𝜆)wouldindicateaviolationoftheindependence
18

assumption. We included the binary condition indicator (𝐶𝑜𝑛𝑑𝑖𝑡𝑖𝑜𝑛𝑟𝑖) and replicate fixed effects
(𝜂𝑟) to capture the potential difference across experiment replicates. Standard errors are clustered
at the replicate level. Table F4, Web Appendix F, shows that the coefficients of carryover (𝜆) are
not significantly different from zero for any dependent variable in Study 1.
Fifth, we investigated potential heterogeneous effects in personas by adding (de-meaned) age,
gender, and their interactions with the treatment to each study’s canonical specification (full spec-
ifications and coefficients in Tables C2–C7, Web Appendix C). These terms were almost all non-
significant, and the few exceptions showed no consistent pattern across configurations. The only
exceptionisStudy4,whereolderpersonasgavelowerexcitementratingsinallfourconfigurations.
In summary, we do not detect systematic heterogeneity in treatment effects across the assigned
personas.
5. Mitigating perceptual misalignment through in-context learning
When a synthetic consumer fails to reproduce a human benchmark, we conceptualize this as a
conflictbetweenthetwopriorsintroducedinourtheoreticalframework. Withoutexplicitguidance,
a model may default to its technical prior (e.g., treating “color saturation” purely as an aesthetic
attribute) or activate a competing psychological prior (e.g., linking an “angular logo” to “support”
ratherthantotheintended“softness”). Wealsoshowedthatanalyzingthemodel’stextualrationales
reveals which specific prior has been anchored onto.
To mitigate this misalignment between AI outputs and human perception, we use ICL, an
accessible intervention that practitioners can implement directly via prompting. Following Xie et
al. (2022), we theoretically ground ICL as a process of implicit Bayesian inference that supplies
necessarycontextualevidencetoshiftthemodel’sprobabilitydistributiontowardthetargethuman-
likepsychologicalprior. Inthissection,weaddressRQ2byexaminingwhetherinjectingconceptual
orempiricalin-contextevidencecansuccessfullysteeramisalignedsyntheticconsumertowardthe
humanbenchmark,andwhethersuccessdependsonhowtheagentisconfigured(modelgeneration
and input format).
5.1. Testing the effectiveness of prompts with conceptual vs. empirical evidence
Tosteerthemodelfromitstechnicaldefaulttowardtheintendedpsychologicaltarget,wedesigned
two forms of evidence-based prompts. We integrated the intervention text directly into the system
promptduringtheinitialpersonainstantiationphase(Step1,Figure2),alongsidethedemographic
profile and before the visual stimulus, priming the AI participant to evaluate the subsequent image
through the lens of the provided information (Table 4):
(1) Conceptual Evidence: We provided the models with the abstract section of the original
research, which outlines the theoretical links to the psychological prior. The text provides
the relevant constructs and the directional nature of the association, but deliberately omits
quantitative statistics. This condition tests whether a purely qualitative, theoretical account
is sufficient to recalibrate the model.
(2) Empirical Evidence: We prompted the model with the specific statistical findings typically
reported in the results section of the original research. In addition to the conceptual links,
19

we supplied concrete distributional evidence featuring explicit input-output mappings (Xie
etal.,2022). Becausethispromptexplicitlycontainsthebenchmarkstatistics,thiscondition
does not aim to assess spontaneous reproduction; rather, it measures the upper bound of
how effectively concrete evidence can steer the model. Conceptually, this mirrors how
a marketing manager might use historical campaign data or market research findings to
construct a behavioral digital twin of a specific consumer segment.
Table 4. Comparison of in-context learning (ICL) intervention conditions
Conceptual Evidence Empirical Evidence
What It TestsEvaluates whether a qualitative, directional
account is sufficient to improve benchmark
alignment.
Establishes the upper bound of calibration
when the model receives precise
distributional statistics.
Information
Provided
Theoretical constructs, key terminology, and
directional hypotheses.
Descriptive statistics (means, SDs),
inferential statistics (𝐹-tests,𝑝-values), and
exact input-output mappings.
OperationalizationIntegration of the target study’s published
abstract into the system prompt.
Integration of the target study’s results
section into the system prompt.
Prompt Example
(Study 1)
Logosfrequentlyincludetextualand/orvisual
design elements that are descriptive of the
type of product/service that brands market...
more (vs. less) descriptive logos are easier to
process and thus elicit stronger impressions
of authenticity, which consumers value.
The more descriptive logos (M = 5.89)
elicited significantly stronger impressions of
authenticitythanthelessdescriptivelogos(M
= 4.82; F(1, 176) = 17.69, p < .001)...
mediated moderation regression analysis
with ease of processing as the mediator...
Asnotedinourtheoreticalbackground,theinputformatcandictatehowevidenceisprocessed
by the model. In a plain-text structure, statistical figures are embedded within narrative sentences,
requiring the model to parse the text to extract them. On the other hand, the JSON format isolates
individual statistics under pre-specified fields. This distinction is particularly important for the
empirical evidence condition, given it is dense with quantitative data. Here, we defined the JSON
schema (Table E8, Web Appendix E) based on the shared structural components of the six studies.
As a validation check, an independent LLM tasked with mapping the plain-text sentences back to
this schema reproduced our categorizations with an accuracy rate of 80% to 94%.
5.2. Mean-level alignment after intervention
We first assessed whether prompts with contextual evidence helped align the models’ inferential
conclusions(maineffects)withhumanbaselinesacrossthesixstudies. Table5showsoutcomesof
everyformat×modelconfiguration. Wefindthatbothconceptualandempiricalevidencegenerally
steered the models toward the human benchmark. Notably, empirical evidence yielded the most
consistent gains, though its effectiveness varied substantially across model generations.
Specifically, empirical evidence moved a majority of configurations to directional consistency
with the human benchmark. In Study 6, for example, all configurations became directionally
consistent, with both GPT-5.4-mini formats reaching statistical significance. Prompts leveraging
conceptual evidence also recovered directionally consistent main effects in several previously null
or reversed cells. Study 2 provides a clear illustration. All four configurations transitioned from
20

null effects at zero-shot to significant effects aligned with human data (𝜂2 =.176for 4o-mini and
.049for 5.4-mini in the plain-text condition).
Despite thesedirectional improvements, the recovered effectsizes were consistentlyattenuated
compared to the original human studies. In Study 1, empirical evidence shifted 5.4-mini from a
nominally reversed null to a significant positive effect; yet, the recovered effect sizes (𝜂2 =.048
and𝜂 2=.034) remained roughly half the magnitude of the human benchmark (𝜂2=.091).
Furthermore, the pattern of success in alignment was not uniform. Study 4 is the only instance
where the newer model failed to recover the effect across all configurations, whereas the older
model successfully recovered it when provided with empirical evidence. A notable anomaly
occurred in Study 5, where 4o-mini never achieved significance, and the contextual interventions
effectivelyattenuatedthemaineffectratherthanstrengtheningit(TableE5,WebAppendixE).The
models passed100%of the manipulation checks under both evidence conditions, indicating that
the interventions recalibrated the models’ psychological priors without impairing their capabilities
in visual recognition.
21

Table 5. Main effects after prompt-based interventions by format×model
GPT-4o-mini (TXT) GPT-4o-mini (JSON) GPT-5.4-mini (TXT) GPT-5.4-mini (JSON)
Study No Int. Concep. Empir. No Int. Concep. Empir. No Int. Concep. Empir. No Int. Concep. Empir.
1 (Authenticity)+(<.001)+(<.001)+(<.001)+(<.001)+(<.001)+(<.001)−(.586)+(.420)+(.003)−(.793)+(.466)+(.013)
2 (Selected saturation)+(.631)+(<.001)+(.006)+(.202)+(<.001)+(.008)+(.288)+(.022)+(<.001)+(.373)+(.035)+(<.001)
3 (Comfort)−(.012)+(.291)+(.603)−(.110)+(.220)+(.133)+(.022)+(<.001)+(<.001)+(.009)+(<.001)+(<.001)
3 (Durability)−(.177)−(.258)−(.534)−(.229)−(.197)−(.512)−(.321)+(<.001)+(<.001)−(.321)+(<.001)+(<.001)
4 (Excitement)−(.736)+(.595)+(.048)−(.230)+(.714)+(.014)−(.383)−(.821)−(.833)−(.562)+(.826)−(.772)
5 (Size estimation)+(.052)+(.150)+(.146)+(.055)+(.189)+(.314)+(.010)+(.060)+(.037)+(.002)+(.060)+(.029)
6 (Utility)−(.136)+(.264)+(.111)−(.401)+(.581)+(.443)−(.844)+(<.001)+(.005)−(.874)+(.006)+(.001)
Note: “No Int./Concep./Empir.”=No Intervention / prompt with conceptual evidence / prompt with empirical evidence. “+/−” indicates the main-effect direction
consistent/inconsistent with the human finding (shown even when𝑛.𝑠.); parentheses contain p-values; bold marks significant effects (𝑝 <.05). Parentheses after
each study number give the dependent variable. Study 6 reports utility for the safety-oriented product category, measured as the mean of the usefulness,
importance, and usage-likelihood ratings. The JSON empirical cells use the fully tagged version of Table E8, Web Appendix E. Complete results appear in Tables
E1–E6, Web Appendix E.
22

5.3. The model generation matters more than the input format
Regarding the configuration levers in RQ2, we found that in zero-shot settings, the two input
formats yielded statistically indistinguishable results, with no single configuration superior for
baseline alignment. Under intervention, however, model generation became a determining factor.
When provided with empirical evidence, 5.4-mini successfully reproduced the human effect in six
of the seven experimental cells (two of which were already aligned at zero-shot), whereas 4o-mini
reproduced the human effect in three (one already aligned at zero-shot). These success rates
were identical across both input formats within each respective model. Overall gains were most
pronounced in the newer 5.4-mini, and 4o-mini showed robust improvement primarily under the
empirical evidence condition. For conceptual evidence, the JSON input wraps the same abstract
within a fixed prefix and suffix, so the structural difference between formats is just a few framing
tokens. However,becauseempiricalevidencecontainssignificantlydenserquantitativebackground
text,wefurtherinvestigatedwhetheralignmentwassensitivetothechoiceofJSONstyle. 3 5.4-mini
successfullyrecoveredthesamestudiesregardlessofthecomplexityofJSONstyle,whereas4o-mini
showeddegradedperformancewhentheevidencewastaggedtoogranularly. Therefore,alignment
is less contingent on the mere presence of JSON formatting than on the schema’s granularity, a
sensitivityuniquetotheoldermodel. ThispatternechoesHeetal.(2024),whofindthatsensitivity
to input formatting declines as model capability increases.
5.4. Reproduction of the underlying semantic associations
We next posed a stricter test: can contextual evidence also lead the model to reproduce the
semantic association underlying the original study’s psychological pathway (i.e., its mediator),
beyond merely reproducing the main effects? A pathway’s semantic association was deemed
successfully reproduced if (1) the main effect was reproduced in that cell, (2) the indirect effect
was statistically significant, and (3) the mediator (or its semantic synonym) appeared among the
keywordsofthatdependentvariable’sthreelargesttopics. Wetestedthefivepsychologicalpathways
in each cell (i.e., ease of processing in Study 1, softness in Study 3 with two DVs, arousal in Study
4, and attention in Study 5). 5.4-mini steadily improved as we added evidence. In both formats,
it went from recovering at most one of the five associations at baseline (zero-shot) to three out of
five when given empirical evidence. In contrast, 4o-mini barely reacted to the interventions, never
recovering more than one pathway.
As an additional check, we measured how prominently the models discussed the mediator in
theirrationales. UsingBERTopic,whichsummarizestopicsusingkeywordlists,wegroupedwords
with the same root (e.g.,soft,softness,softer) into a single item. We then calculated the share of
thesekeywordsthatmatchedthemediator. Topreventpathwayswithmultipledependentvariables
from dominating the results, we averaged these shares equally across the five pathways. For 5.4-
mini,thismediatorsharesteadilyincreasedinbothformatsasevidencewasadded(e.g.,risingfrom
12.4% to 19.6% in JSON). 4o-mini’s share stayed flat in both formats (JSON: 14.7% to 13.0%;
TXT: 15.0% to 13.4%), matching almost no real improvement in actual association recovery (0 to
1 out of 5) (Table 6).
3We supplied the identical empirical evidence across three varying JSON styles: no tags, section headings only,
and the fully granular schema detailed in Table E8, Web Appendix E. Results by style are available upon request.
23

Table 6. Reproduction of the semantic associations underlying the human pathways, and
mediator-keyword presence, by format×model
Associations reproduced (out of 5) Keyword-group share (%)
Configuration No Intervention Conceptual Empirical No Intervention Conceptual Empirical
4o-mini TXT 0/5 0/5 1/5 15.0 11.9 13.4
4o-mini JSON 1/5 0/5 1/5 14.7 11.5 13.0
5.4-mini TXT 1/5 2/5 3/5 13.2 19.6 21.8
5.4-mini JSON 0/5 2/5 3/5 12.4 16.0 19.6
Note: An association counts as reproduced when it meets three conditions: (1) The main effect is reproduced in that
cell; (2) The indirect effect is significant; (3) The mediator or a synonym (e.g., soft or cushioned for softness) appears
among the keywords of that DV’s three largest topics. “Keyword-group share” is the unweighted mean of the five
pathway shares. A pathway’s share is the proportion of keyword groups in its DV’s three largest topics that contain
the mediator, counting words with the same root as one group. Averaging with equal weight keeps pathways with
more dependent variables from dominating the figure. For example, 12.4% for 5.4-mini JSON at zero-shot is the
mean of its five pathway shares (13/93, 7/29, 4/54, 9/54, and 0/54 keyword groups containing the mediator, for
Studies 1, 3-comfort, 3-durability, 4, and 5, respectively).
5.5. Variance shrinkage persists in every configuration
Next, we checked whether any configuration reproduced the natural spread of human responses
to address RQ3. We used two distribution-level metrics from Peng et al. (2025): Glass’sΔ =
(𝑋 LLM−𝑋 Human)/SDHuman,whichmeasuresthestandardizeddiscrepancyofthemean,andtheSD
Ratio=SD LLM/SDHuman, which measures how well the variances align. Both metrics require the
humanstandarddeviation,sowecalculatedthemforeachformat×modelconfigurationacrossthe
eightconditioncellsthatreportone: thetwoconditionsineachofStudies2,3-comfort,3-durability,
and 5 (Figure 10).
24

5.4-mini JSON
5.4-mini TXT
4o-mini JSON
4o-mini TXT
0.0 0.5 1.0 1.5
Panel A: |Glass’s Δ|
No intervention Conceptual Empirical
5.4-mini JSON
5.4-mini TXT
4o-mini JSON
4o-mini TXT
0.2 0.4 0.6 0.8 1.0
Panel B: SD Ratio
No intervention Conceptual Empirical
Figure 10.|Glass’sΔ|(Panel A) and SD Ratio (Panel B) by format×model across the three
interventions.
Note: Each row represents a single GPT configuration. Each point denotes the mean across the eight condition cells
(±1SE); the error bars describe between-cell heterogeneity, not sampling uncertainty. The dashed line marks the
human benchmark (|Glass’sΔ|=0; SD Ratio=1).
25

We observed two patterns. First, adding empirical evidence moved every configuration closer
tothehumanmean,shrinking|Glass’sΔ|towardzeroacrossallfoursetups. However,thisimprove-
mentwasnotstatisticallysignificantwithinanysinglesetup(e.g.,4o-mini(TXT):𝐹(2,14)=1.788,
p=.203). Second, the narrow spread of responses is not a cost of our calibration process; it is
a persistent flaw across the board. All twelve combinations of configuration and intervention
produced an SD Ratio below1.0, and every zero-shot value fell below.50. This shows that the
synthetic responses were already far too uniform before we introduced any evidence.4
The interventions did not consistently worsen this shrinkage. For 5.4-mini, the SD Ratio
increasedslightlytowardthehumanbaselineunderempiricalevidence(TXT:.335→.400;JSON:
.354→.493). For 4o-mini, it decreased (TXT:.430→.283; JSON:.498→.326). Ultimately,
synthetic consumers systematically fail to capture human heterogeneity across all configurations
(Bisbee et al., 2024), and neither the model, the format, the prompt, nor the sampling temperature
resolved it (see Table F2, Web Appendix F for the temperature check).
This shrinkage appears to be an inherent feature of these agents, even with variation in demo-
graphic personas—the standard way the industry generates synthetic samples. In-context learning
can only soften this shrinkage instead of fixing it completely.
6. General discussion
Our research investigates the boundary conditions of using LLMs as reliable proxies for human
consumers. Our zero-shot benchmarks of canonical visual marketing effects showed that models
reliablyseevisualfeaturesyetfrequentlyfailtoperceivetheconsumermeaningthosefeaturescarry
(RQ1). This misalignment, however, can often be steered. By injecting conceptual or empirical
evidence via in-context learning (ICL), we can calibrate the AI toward human benchmarks, with
gains that depend more on the underlying model generation than on the input format (RQ2). Yet, a
criticallimitationpersists: Whileevidence-basedpromptingcorrectsthemaineffects,thesimulated
responses suffer from substantial variance shrinkage (RQ3).
Despitethislimitation,acalibratedagentremainsausefultoolforrapid,early-stagescreeningof
visual cues. In the managerial implications, we translate these findings into a governance protocol
that teams with basic analytics capacity can run, and we illustrate it with a case study.
6.1. Theoretical implications
First, we extend the silicon sampling literature to the visual domain, testing whether LLMs can
simulate not only textual preferences but the multimodal interpretation of visual marketing assets.
While text-based LLMs show promise in mimicking human responses (Ashokkumar et al., 2026),
this success does not carry over to these assets, where model judgments systematically depart
from the human benchmark. The results provide empirical content to the distinction between a
model’s technical prior and its psychological prior. By integrating numerical ratings with textual
rationales,weidentifyrecurringsourcesofmisalignment. Inourmanipulationchecks,weobserved
novisualrecognitionerrors. Instead,themisalignmentsstemfrommissingorcompetingsemantic
associations, in which the AI defaults to a technical or an alternative psychological interpretation.
4TheGPT-4o-mini(JSON)averageunderconceptualevidenceapproaches1.0onlybecauseofoneoutlier. Cell-level
values are available upon request.
26

The broader implication is that recognizing a visual cue, reproducing the human outcome, and
reproducing the semantic association that underlies the human psychological pathway are distinct
tasks. Success in one does not guarantee success in the next.
Second,weevaluatehowdifferenttypesofin-contextevidenceactivatethetargetpsychological
prior. We show that providing empirical evidence (e.g., statistical findings) steers the model
towardthehumanbenchmarkmoreeffectivelythanconceptualevidence. Forthenewermodel,the
empiricalpromptalsoreproducedthesemanticassociationunderlyingthehumanpathwayinthree
ofthefivetests,fromamaximumofoneatzero-shot. Theoldermodel,conversely,neverproduced
more than one successful reproduction. Importantly, as shown in Section 5.5, these interventions
do not restore response variance. Consequently, calibrated synthetic consumers are suitable for
mean-level comparisons only.
6.2. Managerial implications
Our six benchmark experiments show that the text-domain record behind synthetic consumers
breaksdownatvisualjudgment,whereamodelcandescribeanimageaccuratelyyetmiss,orreverse,
the meaning consumers assign to it. However, the practitioners most receptive to AI are precisely
those least equipped to audit it (Tully et al., 2025). We therefore develop a governance protocol
paired with cautionary guidelines for deploying visual AI agents (Figure 11). It complements
recentguidanceonhowtoimplementGenAImethodsandwhentheyaddvalue(Joerling,2026)by
addressing the prior question of whether an agent’s judgments can be trusted at all. This protocol
establishescleargatingcriteriatodeterminewhenasyntheticconsumerisreliableandwhenhuman
oversight is required. A configuration passes calibration only by reproducing a historical human
benchmark, at the original study’s sample size, in both direction and significance. Comparing the
reproducedeffectsizeagainstthebenchmark,asthecasestudybelowillustrates,providesafurther
check. If it fails, the protocol triggers an ICL intervention. If that intervention does not resolve the
misalignment, the task reverts to a human panel.
The protocol places calibration before intervention for two reasons. Analytically, intervention
is blind without a benchmark. Until an agent’s output is compared against known human data, a
manager cannot know whether it needs steering or whether steering overcorrected. Even effects
already validated with human subjects require this step; furthermore, visual effects are context-
dependent, so re-testing is advised in each deployment context (Kim et al., 2023). Our results
show that some misalignments resist even the strongest evidence prompt, and that an uncalibrated
agent can be confidently wrong. Economically, calibration is a one-time fixed cost: Once a given
model generation and input format are validated for a stimulus domain and target judgment (e.g.,
logo authenticity), the agent screens subsequent creative variants at near-zero marginal cost. The
investment thus directly relieves the evaluation bottleneck that motivates synthetic consumers in
the first place. It recurs only when the configuration changes, such as when the vendor updates the
model or the firm moves to a new stimulus domain or target judgment.
Thisgovernanceiscriticalbecausepractitionerscannotrelyontheanthropomorphicassumption
that AI perceives visual assets through a human psychological lens, a view that aligns with recent
workwarningagainsttreatingAIasadirecthumansubstitute(Gaoetal.,2025). Anewermodelis
noguaranteeofalignment: thelatestGPTgenerationwasnotuniformlybetteratzero-shot,though
it responded far more to steering. Because behavior shifts from version to version, the practice
of calibration is what survives model turnover, and firms must rerun it on whichever model they
27

deploy.
This calibration should also cover the prompt architecture. Although plain text and JSON did
not differ statistically in our studies, the older model degraded when the empirical evidence was
tagged too finely, so the protocol treats the JSON schema as one more parameter to validate rather
than a fixed default.
Finally, because response variance remains systematically below human levels in every config-
uration, strategic decisions that hinge on consumer heterogeneity should always return to a human
panel.
Calibration
Baseline Assessment via Human Benchmarks
Zero-Shot Evaluation
Benchmark LLM against
Known Human Data
NoAlignment?
Main effect and Mediation
Y es
Intervention
Model Steering via In-Context Learning
Prompt Interventions
Supply Conceptual or Empirical
Evidence; Choice of Format
Alignment?
Main effect and Mediation
No
Alternative
InterventionY es
Application to Novel Managerial Stimuli
Deployment
Figure 11. The three-step governance protocol (Calibrate, Intervene, Deploy) for deploying
synthetic consumers.
6.2.1. A governance protocol case studyConsider a manager using GenAI to design an “au-
thentic” running shoe logo. She first generates two options: one less descriptive and one more
descriptive (Figure 12). To validate these designs, she plans to use a synthetic panel to predict
consumerperceptionsofauthenticity. Shereachesforanewmodel,GPT-5.4-mini,ontheassump-
tion that a state-of-the-art system will read the logos as her customers would. However, aware of
the potential for misalignment between human and model perceptions, she applies the three-step
28

governance protocol to verify the agent before deployment.
Less Descriptive More Descriptive
Figure 12. AI-generated logos for a running shoe brand. Both images were created with ChatGPT
(OpenAI) as stimuli for the case study.
Step 1: Calibration.The manager first calibrates the agent on a reference benchmark with
known human data (e.g., historical in-house results or published research). She picks Luffarelli,
Mukesh, and Mahmood (2019), whose descriptiveness–authenticity effect (𝜂2 =.091) closely
mirrors her screening question, and evaluates GPT-5.4-mini (TXT) on the study’s original stimuli.
Atzero-shot, themodelshowsnosignificantmaineffect(𝑝=.586,𝜂 2=.002; Table3), indicating
a misalignment with the benchmark. She therefore advances to the intervention stage.
Step 2: Intervention.She re-runs the check on the original stimuli, this time supplying the
model with evidence from the benchmark study. She has learned that empirical evidence is more
helpfulinmitigatingthismisalignmentinhuman-AIperceptionthanconceptualevidence(Table5).
On the one hand, the empirical prompt restores the human main effect (𝑝=.003) with an effect
size of𝜂2=.048, roughly half the human benchmark. On the other hand, the conceptual prompt
does not reach significance under this configuration (𝑝=.420). Based on this finding, she selects
the empirical prompt for GPT-5.4-mini (TXT) and moves forward.
Step 3: Deployment.Having validated the prompt against a task with a known human
benchmark, she now applies it to her own logo pair (Figure 12). She runs the same data-collection
pipeline, simulating 160 AI participants (80 per logo) in each prompt condition (zero-shot versus
thevalidatedempiricalprompt;fullresultsinTableE7,WebAppendixE). 5Atzero-shot,GPT-5.4-
mini (TXT) again shows no significant main effect on her logos (MLess_Desc [SDLess_Desc]=4.567
[.493] vs. MMore_Desc =4.504 [.495], F(1, 158)=.641,𝑝=.425,𝜂 2 =.004), despite clearly
distinguishing between the two descriptiveness levels (manipulation check: t(158)=33.353,𝑝 <
.001,𝜂 2=.876). This outcome reproduces the misalignment we saw, but on new visual assets this
time.
After the empirical prompt, the more descriptive logo is rated as more authentic (MLess_Desc
[SDLess_Desc]=6.033[.755]vs. M More_Desc=6.442[.491],F(1,158)=16.444,𝑝 <.001,𝜂 2=.094).
Shereadstheoutputasadirectionalsignalratherthanahumaneffectsize,sincenohumanbaseline
5For completeness, the manager also evaluates the conceptual prompt on the novel stimuli. Although this prompt
restores the directional main effect, it amplifies the effect size more than fourfold (𝜂2 =.408). This overshoot
underscores the instability of the intervention with only conceptual evidence.
29

exists for her proprietary logos. Because the agent’s variance remains below human levels, she
ranks designs on average authenticity and takes no segmentation decision from it.
6.3. Limitations and future research
First, our empirical scope focuses on generic demographic personas across two models from a
singlevendor’slow-costtier,evaluatingnumericalratingsofstaticimages. Itisunclearwhetherthe
reportedalignmentgapsandvarianceshrinkagewouldbeofsimilarmagnitudeinflagshipmodels,
alternative platforms (e.g., Claude, Gemini), or agents conditioned on richer, high-dimensional
profiles, as in Toubia et al. (2025) and Peng et al. (2025). Extending this governance protocol to
dynamic video creatives remains a natural next step for assessing its broader applicability.
Second, we operationalize alignment using published literature rather than absolute ground
truth. Giventhereplicationcrisisinbehavioralscience(Simmonsetal.,2011),anAI’sinabilityto
reproduce a finding may reflect instability in the original human effect rather than a shortcoming
of the model’s perception capability. Furthermore, all six benchmarks predate the training cutoffs
for bothmodels. However, ratherthan undermining ourfindings, this potentialprior dataexposure
strengthens our core argument: Even if the models possessed latent memory of the published
results, they still failed to reproduce most of the human effects at zero-shot. Evaluating models
on future, post-cutoff visual experiments could nonetheless distinguish true perceptual alignment
from memorized retrieval.
Third, our protocol evaluates models purely on their behavioral inputs and outputs, without
attempting to unpack the AI black box. We therefore do not claim that the AI processes visual
information through the same internal mechanisms as humans, and because our empirical prompt
supplies the benchmark statistics, the resulting alignment demonstrates steerability rather than
spontaneousagreement. Futureresearchcaninvestigatewhethercalibratedagentscanmovebeyond
rating images to generating assets that operationalize these latent psychological principles.
Use of generative AI
Duringthepreparationofthismanuscript,theauthorsusedAI(Claude)forcopyeditingandstylistic
refinement. After the use of this tool, the authors reviewed and revised the manuscript and take
fullresponsibilityforthefinalpublishedarticle. Thisdeclarationconcernsmanuscriptpreparation
only; the use of large language models as experimental subjects is part of the study’s methodology
and is reported in Section 3.
30

References
Aaker, J. L. (1997). Dimensions of brand personality.Journal of Marketing Research,34(3),
347–356. https://doi.org/10.1177/002224379703400304
Adam, Z., & Yang, Z. (2026). Breaking the mold: How visual atypicality shapes brand-generated
imagevirality.InternationalJournalofResearchinMarketing,43,436–456. https://doi.org/
10.1016/j.ijresmar.2025.07.005
Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out of
one, many: Using language models to simulate human samples.Political Analysis,31(3),
337–351. https://doi.org/10.1017/pan.2023.2
Arora, N., Chakraborty, I., & Nishimura, Y. (2025). AI–human hybrids for marketing research:
Leveraging large language models (LLMs) as collaborators.Journal of Marketing,89(2),
43–70. https://doi.org/10.1177/00222429241276529
Ashokkumar, A., Hewitt, L., Ghezae, I., & Willer, R. (2026). Large language models can
predict the results of social science experiments.Nature. (Advance online publication)
https://doi.org/10.1038/s41586-026-10742-x
Bisbee,J.,Clinton,J.D.,Dorff,C.,Kenkel,B.,&Larson,J.M. (2024). Syntheticreplacementsfor
humansurveydata? Theperilsoflargelanguagemodels.PoliticalAnalysis,32(4),401–416.
https://doi.org/10.1017/pan.2024.5
Blanchard, S. J., Duani, N., Garvey, A. M., Netzer, O., & Oh, T. T. (2025). New tools, new
rules: A practical guide to effective and responsible generative AI use for surveys and
experiments in research.Journal of Marketing,89(6), 119–139. https://doi.org/10.1177/
00222429251349882
Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation.Journal of Machine
Learning Research,3, 993–1022.
Blythe, P. A., Kulis, C., McGraw, A. P., Haenlein, M., Hewett, K., Yoo, K., ... Huber, J. (2025).
Comments on “AI and the advent of the cyborg behavioral scientist”.Journal of Consumer
Psychology,35(2), 316–328. https://doi.org/10.1002/jcpy.1453
Brand, J., Israeli, A., & Ngwe, D. (2023).Using LLMs for market research.Working Paper
No. 23-062, Harvard Business School. https://doi.org/10.2139/ssrn.4395751
Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., ... Amodei, D. (2020).
Languagemodelsarefew-shotlearners.AdvancesinNeuralInformationProcessingSystems,
33, 1877–1901.
Chen, S., Ponomarenko, V., Lv, L., & Ahlstrom, D. (2025). Visual complexity, brand gender,
and ad effectiveness.International Journal of Research in Marketing,42(2), 365–390.
https://doi.org/10.1016/j.ijresmar.2024.09.004
Devlin,J.,Chang,M.-W.,Lee,K.,&Toutanova,K.(2019).BERT:Pre-trainingofdeepbidirectional
transformers for language understanding. InProceedings of the 2019 Conference of the
NorthAmericanChapteroftheAssociationforComputationalLinguistics: Humanlanguage
technologies (NAACL-HLT)(pp. 4171–4186).
Dew,R.,Ansari,A.,&Toubia,O.(2022).Lettinglogosspeak: Leveragingmultiviewrepresentation
learning for data-driven branding and logo design.Marketing Science,41(2), 401–425.
https://doi.org/10.1287/mksc.2021.1326
Ericsson, K. A., & Simon, H. A. (1980). Verbal reports as data.Psychological Review,87(3),
215–251. https://doi.org/10.1037/0033-295X.87.3.215
31

Gao, Y., Lee, D., Burtch, G., & Fazelpour, S. (2025). Take caution in using LLMs as human
surrogates.ProceedingsoftheNationalAcademyofSciences,122(24),e2501660122. https://
doi.org/10.1073/pnas.2501660122
Goli, A., & Singh, A. (2024). Frontiers: Can large language models capture human preferences?
Marketing Science,43(4), 709–722. https://doi.org/10.1287/mksc.2023.0306
Grewal, D., Satornino, C. B., Davenport, T., & Guha, A. (2025). How generative AI is shaping
the future of marketing.Journal of the Academy of Marketing Science,53(3), 702–722.
https://doi.org/10.1007/s11747-024-01064-3
Griffiths, T. L., Kemp, C., & Tenenbaum, J. B. (2008). Bayesian models of cognition. In R. Sun
(Ed.),The Cambridge handbook of computational psychology(pp. 59–100). Cambridge
University Press. https://doi.org/10.1017/CBO9780511816772.006
Grootendorst,M. (2022).BERTopic: Neuraltopicmodelingwithaclass-basedTF-IDFprocedure.
arXiv. https://doi.org/10.48550/arXiv.2203.05794
Hagtvedt, H., & Brasel, S. A. (2017). Color saturation increases perceived product size.Journal
of Consumer Research,44(2), 396–413. https://doi.org/10.1093/jcr/ucx039
Hartmann,J.,Exner,Y.,&Domdey,S. (2025). Thepowerofgenerativemarketing: Cangenerative
AI create superhuman visual marketing content?International Journal of Research in
Marketing,42(1), 13–31. https://doi.org/10.1016/j.ijresmar.2024.09.002
Hayes, A. F. (2022).Introduction to mediation, moderation, and conditional process analysis: A
regression-based approach(3rd ed.). New York, NY: Guilford Press.
He, J., Rungta, M., Koleczek, D., Sekhon, A., Wang, F. X., & Hasan, S. (2024).Does prompt
formatting have any impact on LLM performance?arXiv. https://doi.org/10.48550/
arXiv.2411.10541
Horton,J.J.,Filippas,A.,&Manning,B.S. (2026).Largelanguagemodelsassimulatedeconomic
agents: Whatcan welearn fromHomo silicus?WorkingPaper No.31122, National Bureau
of Economic Research. https://doi.org/10.3386/w31122
Huang, M.-H.,&Rust, R.T. (2021). Astrategicframeworkforartificialintelligenceinmarketing.
JournaloftheAcademyofMarketingScience,49(1),30–50. https://doi.org/10.1007/s11747
-020-00749-9
Jiang, Y., Gorn, G. J., Galli, M., & Chattopadhyay, A. (2016). Does your company have the right
logo? How and why circular- and angular-logo shapes influence brand attribute judgments.
Journal of Consumer Research,42(5), 709–726. https://doi.org/10.1093/jcr/ucv049
Joerling, M. (2026). Integrating GenAI interactions in marketing studies: A methodological
guide.International Journal of Research in Marketing,43, 28–47. https://doi.org/10.1016/
j.ijresmar.2025.12.003
Kim,J.,Zhao,M.,&Soman,D.(2023).Convergingvsdiverging: Theeffectofvisualrepresentation
of goal structure on financial decisions.International Journal of Research in Marketing,
40(2), 362–377. https://doi.org/10.1016/j.ijresmar.2022.09.003
Kojima, T., Gu, S. S., Reid, M., Matsuo, Y., & Iwasawa, Y. (2022). Large language models are
zero-shotreasoners.AdvancesinNeuralInformationProcessingSystems,35,22199–22213.
Kupor, D. M., & Tormala, Z. L. (2015). Persuasion, interrupted: The effect of momentary
interruptions on message processing and persuasion.Journal of Consumer Research,42(2),
300–315. https://doi.org/10.1093/jcr/ucv018
Labrecque, L. I., & Milne, G. R. (2012). Exciting red and competent blue: The importance
of color in marketing.Journal of the Academy of Marketing Science,40(5), 711–727.
32

https://doi.org/10.1007/s11747-010-0245-y
Labroo, A. A., Dhar, R., & Schwarz, N. (2008). Of frog wines and frowning watches: Semantic
priming, perceptual fluency, and brand evaluation.Journal of Consumer Research,34(6),
819–831. https://doi.org/10.1086/523290
Lee, A. Y., & Aaker, J. L. (2004). Bringing the frame into focus: The influence of regulatory fit
on processing fluency and persuasion.Journal of Personality and Social Psychology,86(2),
205–218. https://doi.org/10.1037/0022-3514.86.2.205
Lee, H., Fujita, K., Deng, X., & Unnava, H. R. (2017). The role of temporal distance on the color
of future-directed imagery: A construal-level perspective.Journal of Consumer Research,
43(5), 707–725. https://doi.org/10.1093/jcr/ucw051
Li, P., Castelo, N., Katona, Z., & Sarvary, M. (2024). Frontiers: Determining the validity of large
language models for automated perceptual analysis.Marketing Science,43(2), 254–266.
https://doi.org/10.1287/mksc.2023.0454
Li,Y.,&Xie,Y. (2020). Isapictureworthathousandwords? Anempiricalstudyofimagecontent
and social media engagement.Journal of Marketing Research,57(1), 1–19. https://doi.org/
10.1177/0022243719881113
Luffarelli, J., Mukesh, M., & Mahmood, A. (2019). Let the logo do the talking: The influence
of logo descriptiveness on brand equity.Journal of Marketing Research,56(5), 862–878.
https://doi.org/10.1177/0022243719845000
Luffarelli,J.,Stamatogiannakis,A.,&Yang,H. (2019). Thevisualasymmetryeffect: Aninterplay
oflogodesignandbrandpersonalityonbrandequity.JournalofMarketingResearch,56(1),
89–103. https://doi.org/10.1177/0022243718820548
Mehrabian, A., & Russell, J. A. (1974).An approach to environmental psychology. Cambridge,
MA: MIT Press.
Morhart,F.,Malär,L.,Guèvremont,A.,Girardin,F.,&Grohmann,B. (2015). Brandauthenticity:
An integrative framework and measurement scale.Journal of Consumer Psychology,25(2),
200–218. https://doi.org/10.1016/j.jcps.2014.11.006
Napoli, J., Dickinson, S. J., Beverland, M. B., & Farrelly, F. (2014). Measuring consumer-
based brand authenticity.Journal of Business Research,67(6), 1090–1098. https://doi.org/
10.1016/j.jbusres.2013.06.001
OpenAI. (2024).Chat completions.https://platform.openai.com/docs/api-reference/chat/create.
(accessed March 13, 2025)
Peng, T., Gui, G., Merlau, D. J., Fan, G. J., Ben Sliman, M., Brucks, M., ... Toubia, O. (2025).
A mega-study of digital twins reveals strengths, weaknesses and opportunities for further
improvement.arXiv. https://doi.org/10.48550/arXiv.2509.19088
Pieters, R., & Wedel, M. (2004). Attention capture and transfer in advertising: Brand, pictorial,
and text-size effects.Journal of Marketing,68(2), 36–50. https://doi.org/10.1509/jmkg.68
.2.36.27794
Rahinel, R., & Nelson, N. M. (2016). When brand logos describe the environment: Design
instability and the utility of safety-oriented products.Journal of Consumer Research,43(3),
478–496. https://doi.org/10.1093/jcr/ucw039
Reimers,N.,&Gurevych,I. (2019). Sentence-BERT:SentenceembeddingsusingSiameseBERT-
networks. InProceedingsofthe2019ConferenceonEmpiricalMethodsinNaturalLanguage
Processing and the 9th International Joint Conference on Natural Language Processing
(EMNLP-IJCNLP)(pp. 3982–3992).
33

Russell,J.A.,Weiss,A.,&Mendelsohn,G.A. (1989). Affectgrid: Asingle-itemscaleofpleasure
andarousal.JournalofPersonalityandSocialPsychology,57(3),493–502. https://doi.org/
10.1037/0022-3514.57.3.493
Sample,K.L.,Hagtvedt,H.,&Brasel,S.A. (2020). Componentsofvisualperceptioninmarketing
contexts: Aconceptualframeworkandreview.JournaloftheAcademyofMarketingScience,
48(3), 405–421. https://doi.org/10.1007/s11747-019-00684-4
Sarstedt, M., Adler, S. J., Rau, L., & Schmitt, B. (2024). Using large language models to
generatesiliconsamplesinconsumerandmarketingresearch: Challenges,opportunities,and
guidelines.Psychology&Marketing,41(6),1254–1270. https://doi.org/10.1002/mar.21982
Sharma, V., & Estes, Z. (2024). Seeing is smelling: Pictures improve product evaluations by
evokingolfactoryimagery.InternationalJournalofResearchinMarketing,41(2),282–307.
https://doi.org/10.1016/j.ijresmar.2024.02.001
Simmons, J. P., Nelson, L. D., & Simonsohn, U. (2011). False-positive psychology: Undis-
closed flexibility in data collection and analysis allows presenting anything as significant.
Psychological Science,22(11), 1359–1366. https://doi.org/10.1177/0956797611417632
Thormundsson, B. (2024).Generative AI adoption rate at work in the United States 2023, by in-
dustry.https://www.statista.com/statistics/1361251/generative-ai-adoption-rate-at-work-by
-industry-us/. (accessed November 17, 2025)
Toluna.(2025).Toluna’sACTInstantAIushersinaneweraofbeyond-limitsadtestingwithsynthetic
personas.https://www.businesswire.com/news/home/20251028193410/en/. (BusinessWire
press release, October 28, 2025; accessed June 23, 2026)
Tomaino, G., Cooke, A. D. J., & Hoover, J. (2025). AI and the advent of the cyborg behavioral
scientist.Journal of Consumer Psychology,35(2), 297–315. https://doi.org/10.1002/jcpy
.1452
Toubia, O., Gui, G. Z., Peng, T., Merlau, D. J., Li, A., & Chen, H. (2025). Database report:
Twin-2K-500: A data set for building digital twins of over 2,000 people based on their
answers to over 500 questions.Marketing Science,44(6), 1446–1455. https://doi.org/
10.1287/mksc.2025.0262
Tully, S. M., Longoni, C., & Appel, G. (2025). Lower artificial intelligence literacy pre-
dicts greater AI receptivity.Journal of Marketing,89(5), 1–20. https://doi.org/10.1177/
00222429251314491
Turpin, M., Michael, J., Perez, E., & Bowman, S. R. (2023). Language models don’t always say
whattheythink: Unfaithfulexplanationsinchain-of-thoughtprompting.AdvancesinNeural
Information Processing Systems,36, 74952–74965.
Xie, P., Kim, E., Lam, S. Y., & Reza, S. (2025). Herding behavior in NFT auction: The role of
visual complexity and familiarity.International Journal of Research in Marketing,42(3),
684–710. https://doi.org/10.1016/j.ijresmar.2024.08.007
Xie, S. M., Raghunathan, A., Liang, P., & Ma, T. (2022). An explanation of in-context learning as
implicit Bayesian inference.International Conference on Learning Representations.
Xu, L., & Mehta, R. (2022). Technology devalues luxury? Exploring consumer responses to AI-
designedluxuryproducts.JournaloftheAcademyofMarketingScience,50(6),1135–1152.
https://doi.org/10.1007/s11747-022-00854-x
Yoo, K., Haenlein, M., & Hewett, K. (2025). A whole new world, a new fantastic point of view:
Charting unexplored territories in consumer research with generative artificial intelligence.
Journal of the Academy of Marketing Science,53(3), 723–759. https://doi.org/10.1007/
34

s11747-025-01097-2
Zhang, J. Z., Li, H. A., & Allenby, G. M. (2024).Supervised mediation analysis.Working paper,
SSRN. https://doi.org/10.2139/ssrn.5654790
Zhao, M., & Xia, L. (2021). Joint or separate? The effect of visual presentation on imagery
and product evaluation.International Journal of Research in Marketing,38(4), 935–952.
https://doi.org/10.1016/j.ijresmar.2020.11.007
Zhao, W. X., Jiang, J., Weng, J., He, J., Lim, E.-P., Yan, H., & Li, X. (2011). Comparing Twitter
andtraditionalmediausingtopicmodels. InAdvancesininformationretrieval: Proceedings
of the 33rd European Conference on IR Research (ECIR)(pp. 338–349). https://doi.org/
10.1007/978-3-642-20161-5_34
35

Web Appendix
Seeing Is Not Perceiving: When Synthetic Consumers Can and Cannot Pretest
Visual Marketing
Web Appendix A: Pre-registration for studies
Thissection containsall thestudies thatwere registeredon aspredicted.org. Linksare listedbelow
by study.
Study 1
A. Without any interventions: https://aspredicted.org/ghd5-p8kc.pdf
B. Prompt with Conceptual Evidence: https://aspredicted.org/7wys-msff.pdf
C. Prompt with Empirical Evidence: https://aspredicted.org/tdpx-28tg.pdf
Robustness checks (Study 1)
A. Different temperatures: https://aspredicted.org/8hkf-kfnw.pdf
B. Different resolutions of the visual stimuli: https://aspredicted.org/rsgz-pcmg.pdf
C. Test with AI-generated stimuli: https://aspredicted.org/qbfx-mnrv.pdf
Study 2
A. Without any interventions: https://aspredicted.org/bfdz-nc7f.pdf
B. Prompt with Conceptual Evidence: https://aspredicted.org/d455-q65j.pdf
C. Prompt with Empirical Evidence: https://aspredicted.org/pc4z-b2p3.pdf
Study 3
A. Without any interventions: https://aspredicted.org/v3pb-zpf8.pdf
B. Prompt with Conceptual Evidence: https://aspredicted.org/8r8w-972x.pdf
C. Prompt with Empirical Evidence: https://aspredicted.org/pjk7-xgpk.pdf
Study 4
A. Without any interventions: https://aspredicted.org/r7hf-f7xx.pdf
B. Prompt with Conceptual Evidence: https://aspredicted.org/qk4f-p3g2.pdf
C. Prompt with Empirical Evidence: https://aspredicted.org/ydkv-7ynq.pdf
36

Study 5
A. Without any interventions: https://aspredicted.org/8wp3-httb.pdf
B. Prompt with Conceptual Evidence: https://aspredicted.org/kydc-6jnz.pdf
C. Prompt with Empirical Evidence: https://aspredicted.org/d5dr-g8vm.pdf
Study 6
A. Without any interventions: https://aspredicted.org/w7qb-5zhq.pdf
B. Prompt with Conceptual Evidence: https://aspredicted.org/srzm-prxf.pdf
C. Prompt with Empirical Evidence: https://aspredicted.org/dfzj-7x3s.pdf
37

Web Appendix B: Description of studies and visual stimuli
Thissection summarizesthe objectives, samplesizes, research designs, andimportant variablesof
each study we investigated, along with the visual stimuli from the original papers.
B.1 Study 1: Based on Study 1 in Luffarelli, Mukesh, and Mahmood (2019)
Main Questions/Hypotheses
This study examined whether more (vs. less) descriptive logos elicit stronger impressions of
brand authenticity. It also investigated whether this effect occurs because such logos are easier to
process, testing ease of processing as a mediator.
Methods
We adopted the same stimuli and target sample size (N = 180)6 as Luffarelli, Mukesh, and
Mahmood (2019). The synthetic consumers mirrored the demographics of the original human
sample recruited via Amazon Mechanical Turk. The study was a 2 (logo descriptiveness: less
vs. more)×2 (brand scenarios: basketball equipment manufacturer vs. running shoe brand)
between-subjects design.
AI participants were randomly assigned to one of four conditions. After being presented with
the assigned logo (Figure B1), they rated brand authenticity on three nine-point scales (authentic,
trustworthy,andcredible;1=“notatall,”9=“very”;adaptedfromMorhartetal.,2015,andNapoli
et al., 2014), which were then averaged into a single measure. Next, AI participants assessed ease
of processing on two nine-point scales (1 = “not at all fluent/not at all eye-catching,” 9 = “very
fluent/very eye-catching”; adapted from Labroo et al., 2008, and Lee & Aaker, 2004), which were
averaged into a single measure. Next, AI participants provided textual rationales for their ratings.
Finally, they completed the manipulation check by rating perceived descriptiveness (1 = “not at all
descriptive,” 9 = “very descriptive”).
Figure B1. Visual stimuli from Study 1 in Luffarelli, Mukesh, and Mahmood (2019)
Basketball equipment manufacturer Running shoe brand
Less
descriptiveness
More
descriptiveness
Less
descriptiveness
More descriptiveness
B.2 Study 2: Based on Study 2A in Lee et al. (2017)
Main Questions/Hypotheses
6Target sample sizes follow the original studies, rounded up where an odd total could not be split evenly across
conditions (Study 3: 70 rather than 69; Study 6 for GPT-4o-mini (TXT): 160 rather than 154). Because GPT
occasionally refuses to answer, the realized sample sizes deviate slightly from the target in some configurations.
38

This study examined whether temporal distance (distant vs. near future) influences visual
imagery. The specific hypothesis was that AI participants imagining distant-future events would
select images with lower color saturation (i.e., more black-and-white) to represent their mental
images, compared to those imagining near-future events, who would select more saturated images.
Methods
We adopted the same stimuli and target sample size (N = 108) as Lee et al. (2017). The study
used a 2 (temporal distance: distant vs. near) between-subjects design, with 3 (scenario types:
hotel, theater, and park) as a within-subjects factor.
AIparticipantswererandomlyassignedtoeitherthe“distant”(e.g.,ayearfromnow)or“near”
(e.g., a week from now) condition. For each of the three scenarios (e.g., staying in a hotel), they
chose one of three photo versions, which varied in color saturation (low, medium, or high; see
Figure B2), presented in a random order. They were prompted to indicate which image “most
closelyresembledwhattheyhadimaginedforeachscenario.” Thesechoiceswerecodedas1(low
saturation), 2 (medium saturation), and 3 (high saturation), respectively, for analysis. After that,
they were prompted to provide the rationale for their selection of each scenario’s image. Finally,
after responding to each of the three scenarios, they were prompted to rate perceived temporal
distance (1 = “very near,” 9 = “very far”) on a nine-point scale as the manipulation check.
Figure B2. Visual stimuli from Lee et al. (2017)
Hotel
(Saturation level: low→medium→high)
Theater
Park
39

Hotel
(Saturation level: low→medium→high)
B.3 Study 3: Based on Study 2 in Jiang et al. (2016)
Main Questions/Hypotheses
This study examined the effect of logo shape (circular vs. angular) on judgments of product
comfort and durability. The original authors hypothesized that circular logos increase perceived
comfortableness, whereas angular logos increase perceived durability, and that these effects are
mediated by activated associations of perceived softness or hardness.
Methods
Weadoptedthesamevisualstimuliandtargetsamplesize(N=69)asinStudy2ofJiangetal.
(2016). This study used a 2 (logo shape: circular vs. angular) between-subjects design.
AI participants were randomly assigned to view an advertisement for a sofa featuring either a
circular or angular logo (Figure B3). Following exposure to the ad, they rated the softness of the
sofa’sbackcushion, seatcushion, andarmsonnine-pointscales(1=“veryhard,” 9=“verysoft”).
They then rated the product’s comfortableness (1 = “not at all comfortable/cozy/cushiony,” 9 =
“very comfortable/cozy/cushiony”) and durability (1 = “not at all durable/enduring/long-lasting,”
9 = “very durable/enduring/long-lasting”). After that, they provided the textual rationale for each
rating. Finally, they completed a manipulation check rating perceived circularity (1 = “not at all
circular,” 9 = “very circular”).
Figure B3. Visual stimuli from Jiang et al. (2016)
40

Angular logo Circular logo
B.4 Study 4: Based on Study 1B in Luffarelli, Stamatogiannakis, and Yang (2019)
Main Questions/Hypotheses
Thisstudyexaminedwhetherasymmetricallogosareperceivedasmoreexcitingthansymmet-
rical logos. The authors hypothesized that this effect is mediated by logo-evoked arousal.
Methods
We adopted the experimental stimuli and target sample size (N = 220) from Study 1B of
Luffarelli, Stamatogiannakis, and Yang (2019). The study used a 2 (logo symmetry: symmetrical
vs. asymmetrical)×4 (logo pair) between-subjects design (Figure B4).
AI participants were randomly assigned to one of two conditions, with four logo-pair repli-
cates. After being presented with their assigned logo, they were first prompted to rate the logo on
five excitement-related adjectives using a seven-point scale (trendy, cool, daring, imaginative, and
exciting; 1 = “not at all,” 7 = “very”; Aaker, 1997). These ratings were averaged into a measure
of logo-evoked perception of excitement. Next, they were prompted to indicate how they felt
whenviewingthelogousingseven-pointscales(“aroused/unaroused,”“stimulated/relaxed,”“fren-
zied/sluggish,” “jittery/dull,” “wide-awake/sleepy”; Mehrabian & Russell, 1974). These responses
were averaged into a single measure of logo-evoked arousal. After that, they were prompted to
provide the rationale for each rating. Finally, they were prompted to rate perceived asymmetry on
a nine-point scale (1 = “not at all asymmetrical,” 9 = “very asymmetrical”) as the manipulation
check.
41

Figure B4. Visual stimuli from Luffarelli, Stamatogiannakis, and Yang (2019)
Logo pair A Logo pair B
Symmetrical Asymmetrical Symmetrical Asymmetrical
Logo pair C Logo pair D
Symmetrical Asymmetrical Symmetrical Asymmetrical
B.5 Study 5: Based on Study 3 in Hagtvedt and Brasel (2017)
Main Questions/Hypotheses
This study examined how a product’s color saturation (high vs. low) influences visual estima-
tions of its size. The authors hypothesized that highly saturated objects increase attention, leading
to larger size estimates. The study also measured arousal and attention as mediating variables.
Methods
Weadoptedtheexperimentalstimuliandtargetsamplesize(N=80)fromStudy3ofHagtvedt
and Brasel (2017). The study used a 2 (color saturation: high vs. low) between-subjects design.
AI participants were randomly assigned to view an image of a red laptop with either high or
low saturation (see Figure B5). First, AI participants estimated the laptop’s screen size on a scale
with 1-inch increments (10 to 20 inches). Next, they rated the extent to which the laptop was
“attention-getting” and “captured their attention” (1 = “not at all,” 7 = “definitely”); these items
were averaged into an attention scale. AI participants also reported arousal and mood using the
affectgrid(Kupor&Tormala,2015;Russelletal.,1989). Followingthesemeasures,theyprovided
textual rationales. Finally, they completed a manipulation check rating perceived saturation (1 =
“very low,” 7 = “very high”).
Figure B5. Visual stimuli from Hagtvedt and Brasel (2017)
42

Low saturation High saturation
B.6 Study 6: Based on Study 2A in Rahinel and Nelson (2016)
Main Questions/Hypotheses
This study examined the interactive effect of logo stability (unstable vs. stable) and product
category on perceived utility. Rahinel and Nelson (2016) hypothesized that an unstable logo (e.g.,
a square rotated on its vertex) signals a need for safety, thereby increasing the perceived utility of
safety-oriented products. This effect was expected to be attenuated or absent in neutral product
categories.
Methods
Weadoptedtheexperimentalstimuliandtargetsamplesize(N=154)fromStudy2AofRahinel
and Nelson (2016). The study used a 2 (logo stability: unstable vs. stable)×2 (category type:
safety-oriented vs. neutral)×6 (product replicate) mixed design.
AI participants were randomly assigned to view a logo for an online company, manipulated to
appeareitherstable(squareonbase)orunstable(squareonvertex; seeFigureB6). AIparticipants
then rated the perceived utility of six products on three nine-point items (“how important the
product is,” “how useful the product is,” “how likely the product is to be used”; 1 = “not at all,” 9
= “very”), which were averaged into a composite index. Depending on the condition, the products
were either safety-oriented (e.g., “security system”) or neutral (e.g., “lawn care”). Following these
ratings, AI participants provided textual rationales. Finally, they completed a manipulation check
rating perceived instability (1 = “not at all,” 9 = “very”).
Figure B6. Visual stimuli from Rahinel and Nelson (2016)
43

Stable logo Unstable logo
44

Web Appendix C: Heterogeneity analysis by personas
This appendix reports whether the synthetic consumers’ judgments vary with their assigned per-
sonas. BecausethefourGPTformat×modelconfigurations(4o-T,4o-J,5.4-T,5.4-J)arethefocus
of the main text, all tables report these four configurations. C.1 reports the realized demographic
composition. C.2 fits regression models of the outcome variable(s) from each study with age,
gender in assigned personas, and their interactions with the treatment added to the study’s speci-
fication, and reports the four demographic coefficients𝛾1–𝛾4. Across studies, the age and gender
main effects and their treatment interactions are almost all non-significant, and the few that reach
𝑝 < .05show no consistent pattern across configurations, except a small negative age effect on
excitement that appears in all four configurations in Study 4 (Table C5). The treatment effects are
therefore essentially homogeneous across the assigned demographics.
C.1 Demographic composition
Table C1. Demographic distribution of each study
Study Config Age𝑀(SD) Age range % female
1 4o-T 41.5 (13.9) 18–65 49.3
1 4o-J 41.3 (13.8) 18–65 50.2
1 5.4-T 42.2 (14.3) 18–65 47.8
1 5.4-J 41.2 (14.2) 18–65 51.3
2 4o-T 40.4 (13.7) 18–65 47.2
2 4o-J 40.8 (14.1) 18–65 50.6
2 5.4-T 41.9 (13.7) 18–65 50.6
2 5.4-J 42.1 (14.0) 18–65 48.5
3 4o-T 19.9 (1.4) 18–22 53.3
3 4o-J 20.1 (1.4) 18–22 49.0
3 5.4-T 20.1 (1.4) 18–22 46.2
3 5.4-J 20.0 (1.4) 18–22 47.1
4 4o-T 42.2 (13.8) 18–65 48.5
4 4o-J 41.2 (14.1) 18–65 52.0
4 5.4-T 41.9 (13.8) 18–65 50.5
4 5.4-J 43.3 (13.8) 18–65 52.4
5 4o-T 21.4 (2.3) 18–25 51.7
5 4o-J 21.5 (2.3) 18–25 43.8
5 5.4-T 21.4 (2.4) 18–25 49.6
5 5.4-J 21.3 (2.3) 18–25 49.6
6 4o-T 20.4 (1.8) 18–23 46.8
6 4o-J 20.5 (1.7) 18–23 46.5
6 5.4-T 20.5 (1.7) 18–23 48.9
6 5.4-J 20.5 (1.7) 18–23 46.5
Note: Config labels: 5.4-J/5.4-T=GPT-5.4-mini with JSON/TXT input; 4o-J/4o-T=GPT-4o-mini with JSON/TXT
input. The samples are about 50% female by design. Distributions are pooled across the three interventions, which
drew new personas from the same sampling rule.
45

C.2 Demographic effects and treatment-effect heterogeneity
Tables C2–C7 report, per study, the combined-model demographic coefficients𝛾1–𝛾4 (age main,
treatment×age, gendermain, treatment×gender)atzero-shot, withsignificanteffects inbold; (DV)
marks the study’s dependent variable. Subscript𝑖indexes AI participants. Studies 2 and 6 include
within-subjects factors, so those models add a participant random intercept𝑢𝑖.
Table C2. Study 1: Logo descriptiveness and brand authenticity (DV)
𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-T−.005 (.002) .044 .001 (.004) .000−.004 (.051) .000−.007 (.102) .000
4o-J .001 (.002) .002−.002 (.004) .001 .032 (.053) .002−.036 (.106) .001
5.4-T .005 (.003) .024 .006 (.005) .008 .024 (.078) .001−.074 (.155) .001
5.4-J .005 (.003) .027 .002 (.005) .001−.080 (.070) .008−.134 (.140) .005
Note: For age,𝛾is the change per extra year from the mean; for gender,𝛾is the female-minus-male difference (Male
=0, Female=1).Replicateis a binary indicator that denotes the two stimulus groups as in the original study.
Authenticity𝑖 =
𝛽0+𝛽 1Desc𝑖+𝛽 2Replicate𝑖+𝛽 3Desc𝑖×Replicate𝑖+𝛾 1Age𝑖+𝛾 2Desc𝑖×Age𝑖+𝛾 3Gender𝑖+𝛾 4Desc𝑖×Gender𝑖+𝜀 𝑖.
Table C3. Study 2: Temporal distance and color saturation (DV)
𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-T−.000 (.001) .000−.004 (.003) .006 .016 (.041) .001−.039 (.081) .001
4o-J−.002 (.001) .020 .001 (.003) .001 .068 (.041) .026−.012 (.082) .000
5.4-T .001 (.002) .001 .004 (.004) .003 .091 (.054) .009−.017 (.107) .000
5.4-J−.002 (.002) .003.008 (.004).014−.043 (.051) .002−.010 (.101) .000
Note: For age,𝛾is the change per extra year from the mean; for gender,𝛾is the female-minus-male difference (Male
=0, Female=1).Scene 𝑠 is the image scene (hotel, theater, or park), and𝑢𝑖 is a participant random intercept. Partial
𝜂2 for these mixed models is𝐹df1/(𝐹df 1+df 2)from the Type-III𝐹-test with Satterthwaite degrees of freedom.
SelSat𝑖𝑠 =𝛽 0+𝛽 1Temporal𝑖+𝛽 2Scene𝑠+𝛽 3Temporal𝑖×Scene𝑠+𝛾 1Age𝑖+𝛾 2Temporal𝑖×Age𝑖+𝛾 3Gender𝑖+
𝛾4Temporal𝑖×Gender𝑖+𝑢 𝑖+𝜀 𝑖𝑠.
Table C4. Study 3: Logo shape and product attributes (DV)
𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config DV𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-T Comfort .007 (.044) .000−.076 (.087) .012 .150 (.125) .022 .368 (.251) .033
4o-T Durability−.046 (.068) .007−.068 (.137) .004−.211 (.196) .018 .348 (.392) .012
4o-J Comfort−.037 (.051) .008 .019 (.103) .001.440 (.139).136 .451 (.278) .039
46

𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config DV𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-J Durability .130 (.072) .048−.186 (.144) .025−.375 (.195) .054 .465 (.391) .022
5.4-T Comfort−.046 (.059) .009 .059 (.119) .004 .053 (.145) .002 .061 (.290) .001
5.4-T Durability .016 (.012) .026−.032 (.024) .026 .016 (.030) .005−.032 (.060) .005
5.4-J Comfort .003 (.050) .000−.009 (.100) .000.288 (.141).061−.385 (.283) .028
5.4-J Durability−.007 (.010) .007−.014 (.021) .007 .036 (.030) .023 .072 (.059) .023
Note: For age,𝛾is the change per extra year from the mean; for gender,𝛾is the female-minus-male difference (Male
=0, Female=1). DV 𝑖 =𝛽 0+𝛽 1Shape𝑖+𝛾 1Age𝑖+𝛾 2Shape𝑖×Age𝑖+𝛾 3Gender𝑖+𝛾 4Shape𝑖×Gender𝑖+𝜀 𝑖 (DV=
Comfort or Durability).
Table C5. Study 4: Logo asymmetry and brand excitement (DV)
𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-T−.006 (.001).088 .003 (.003) .007 .017 (.038) .001−.072 (.076) .004
4o-J−.004 (.001).049 .005 (.003) .017−.013 (.038) .001−.091 (.077) .007
5.4-T−.008 (.002).061 .002 (.004) .001−.034 (.057) .002−.022 (.114) .000
5.4-J−.007 (.002).069−.001 (.004) .000 .065 (.052) .008−.031 (.103) .000
Note: For age,𝛾is the change per extra year from the mean; for gender,𝛾is the female-minus-male difference (Male
=0, Female=1).Pairis the logo pair. Excitement𝑖 =
𝛽0+𝛽 1Asym𝑖+𝛽 2Pair𝑖+𝛽 3Asym𝑖×Pair𝑖+𝛾 1Age𝑖+𝛾 2Asym𝑖×Age𝑖+𝛾 3Gender𝑖+𝛾 4Asym𝑖×Gender𝑖+𝜀 𝑖.
Table C6. Study 5: Color saturation and estimated size (DV)
𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-T .022 (.024) .012 .012 (.049) .001−.198 (.109) .045 .384 (.218) .042
4o-J−.000 (.039) .000 .063 (.079) .010 .093 (.179) .004 .229 (.359) .006
5.4-T .022 (.030) .007−.029 (.059) .003−.048 (.138) .002 .331 (.276) .019
5.4-J−.050 (.036) .026 .001 (.072) .000−.129 (.160) .009−.099 (.319) .001
Note: For age,𝛾is the change per extra year from the mean; for gender,𝛾is the female-minus-male difference (Male
=0, Female=1).
Size𝑖 =𝛽 0+𝛽 1Saturation𝑖+𝛾 1Age𝑖+𝛾 2Saturation𝑖×Age𝑖+𝛾 3Gender𝑖+𝛾 4Saturation𝑖×Gender𝑖+𝜀 𝑖.
Table C7. Study 6: Logo stability and utility (DV)
47

𝛾1 Age𝛾 2 Age×T𝛾 3 Gender𝛾 4 Gen×T
Config𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2 𝛾(SE)𝜂 2
4o-T .006 (.008) .003−.000 (.016) .000 .025 (.030) .005 .086 (.059) .014
4o-J−.003 (.009) .001−.018 (.019) .006 .037 (.031) .009 .032 (.062) .002
5.4-T−.000 (.016) .000 .060 (.032) .023 .061 (.055) .008−.033 (.111) .001
5.4-J .003 (.020) .000−.027 (.040) .003 .026 (.070) .001−.133 (.140) .006
Note: For age,𝛾is the change per extra year from the mean; for gender,𝛾is the female-minus-male difference (Male
=0, Female=1).Replicateis the repeated stimulus set (𝑗indexes the rated products), and𝑢𝑖 is a participant random
intercept. Partial𝜂 2 for these mixed models is𝐹df1/(𝐹df 1+df 2)from the Type-III𝐹-test with Satterthwaite
degrees of freedom. Utility𝑖 𝑗 =𝛽 0+Stability 𝑖×ProductType𝑗×Replicate 𝑗 (full factorial)+𝛾 1Age𝑖+
𝛾2Stability𝑖×Age𝑖+𝛾 3Gender𝑖+𝛾 4Stability𝑖×Gender𝑖+𝑢 𝑖+𝜀 𝑖 𝑗.
48

Web Appendix D: BERTopic and LLM-assisted topic models
D.1 Natural language pipeline
1. Semantic Embedding: We first converted each rationale (pre-processed to remove conversa-
tionalartifacts)intoahigh-dimensionalvectorusingasentence-transformer. Thisembedding
captures the rationale’s contextual meaning, not just its keywords. For instance, in Study 3,
thismodelunderstandsthat“circular,”“curved,”and“smoothlycontoured”aresemantically
similar concepts, clustering them even if they do not share words.
2. TopicClustering: WefollowedthestandardBERTopicpipeline(Grootendorst,2022),which
applies UMAP for dimensionality reduction and HDBSCAN for clustering.7 This process
groups rationales into semantically coherent and conceptually distinct topics. Consistent
with best practices for a smaller corpus, we set the minimum topic size to 5 and the number
of neighbors to 15 to capture granular topics. We also varied these key hyperparameters for
robustness checks.
3. Topic Representation: We identified keywords for each topic using a class-based metric that
selectswordsthatarebothfrequentwithinatopicandrareacrossothertopics. 8 Forexample,
Topic 0 in one model’s Study 1 was represented by: “context (.621), professional (.583),
credibility (.581), logo (.579)....” In addition to these keywords, a byproduct of BERTopic’s
clusteringistheidentificationofthemostrepresentativedocumentsforeachtopic(i.e.,those
closest to the topic’s cluster centroid). We used this feature to enhance the objectivity and
scalability of the labeling procedure, using an LLM to assist with topic labeling. For each
topic, we prompted GPT-4o-mini with the three most representative documents and asked it
to generate a concise, descriptive label. For example, the LLM-generated label for the topic
above highlighted a lack of “additional context or branding elements” as a factor influencing
“credibility,” an insight that emerged directly from the data-driven clustering.
D.2 Example of prompt for GPT-assisted topics
We used the following prompt with GPT-4o-mini to assist with topic description based on the
representative documents selected by BERTopic. “I have a dataset of logo design evaluations,
containing rationales about different features. These evaluations consist of free-text responses,
rangingfromshortcommentstodetailedanalyses. Pleaseidentifythesinglemaintopicmentioned
in these comments. Return a topic name and topic description. The topic name should be short,
but descriptive. The topic description should be a complete sentence. A good topic description
lookslikethis:'Thereareconcernsaboutauthenticitybecausethelogodesignsareoverlyminimal.'
ReturnthetopicnameanddescriptionasaPythondictionarywithasinglekey-valuepairlikethis:
7HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise) is the default clustering
algorithm in BERTopic. Unlike algorithms like K-Means, it does not require the number of topics (clusters) to be
pre-specified. Itdeterminesthenumberofclusters(topics)byidentifyingdenseregionsofdocumentsintheembedding
space and classifies the sparser data points as outliers (i.e., not belonging to a specific topic).
8Themetric,c-TF-IDF(Class-basedTermFrequency-InverseDocumentFrequency),isaversionofTF-IDFadapted
for topic modeling. It treats all documents belonging to one topic as one combined “class.” Then it calculates a score
based on how frequent a word is in its parent topic, while also penalizing words that appear frequently in other topics.
A high score thus indicates a word is both highly descriptive of and unique to the topic.
49

{{'topic_name':'<topicName>','topic_description':'<topicDescription>'}} If you cannot find a
good topic label, just say,'No topic identified.'”
50

Web Appendix E: Prompt intervention templates and results after
interventions
E.1 Prompt templates
Prompt with Conceptual Evidence
“You are a {demographics['age']}-year-old {demographics['gender']} participant who lives in
the {demographics['location']}. Please take a moment to look at the image carefully and wait for
myprompt. Beforeansweringthesurveyquestionsbelow,pleasereadandinternalizethefollowing
background: [The abstract of the study is inserted here.] Once you have fully processed that
background, please proceed to answer the following survey questions based on it.”
Prompt with Empirical Evidence
“You are a {demographics['age']}-year-old {demographics['gender']} participant who lives in
the {demographics['location']}. Please take a moment to look at the image carefully and wait for
myprompt. Beforeansweringthesurveyquestionsbelow,pleasereadandinternalizethefollowing
background: [Results and statistics from the relevant study are inserted here.] Once you have fully
processed that background, please proceed to answer the following survey questions based on it.”
E.2 Detailed results by study after prompt interventions
This section reports the main-effect results after the prompt interventions for all four GPT format
×model configurations (4o-T, 4o-J, 5.4-T, 5.4-J; labels as in Table C1, Web Appendix C), under
No Intervention, the prompt with conceptual evidence, and the prompt with empirical evidence.
Dir(𝑝)givesthemain-effectdirectionandits𝑝-value(+/−=directionconsistent/inconsistentwith
the human finding), with bold marking𝑝 < .05; Med. gives the mediation verdict (full or partial)
for the four studies with a hypothesized mediator (Tables E1, E3, E4, and E5); a dot means that
no mediation is established, either because the main effect is not significant, so the test is not
interpreted, or because the indirect effect is not significant; and (DV) marks the study’s dependent
variable. Unless noted otherwise, each Dir(𝑝) comes from a one-way ANOVA on the study’s
dependentvariable,𝜂 2istheeffectsizefromthattest,andeachconfiguration’ssamplesizematches
the original study’s (Web Appendix B). Tables E1–E6 report all four configurations; Table E7
reports the case-study deployment, which uses GPT-5.4-mini (TXT) only. The tables in Web
Appendix F follow the same conventions.
51

Table E1. Study 1: Logo descriptiveness and brand authenticity (DV)
No Intervention Conceptual Empirical
Config More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 Med. More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 Med. More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 Med.
4o-T 6.424(.354) 6.198(.405)+(<.001).082 . 6.622(.334) 6.447(.303)+(<.001).071 . 6.562(.269) 6.295(.504)+(<.001).100 .
4o-J 6.470(.227) 6.209(.431)+(<.001).125 partial 6.674(.299) 6.457(.162)+(<.001).172 . 6.610(.196) 6.345(.359)+(<.001).178 .
5.4-T 4.293(.970) 4.356(.507)−(.586) .002 . 6.485(.618) 6.419(.478)+(.420) .004 . 6.856(.669) 6.519(.839)+(.003).048 partial
5.4-J 4.370(1.101) 4.404(.483)−(.793) .000 . 6.648(.660) 6.585(.483)+(.466) .003 . 6.630(.709) 6.333(.865)+(.013).034 partial
Note: Study1(DV:brandauthenticity); More/Less=more-vs.less-descriptivelogocondition. RowsarethefourGPTconfigurations; cellsreportconditionmeans
(SD).
Table E2. Study 2: Temporal distance and color saturation (DV)
No Intervention Conceptual Empirical
Config Near𝑀(SD) Dist.𝑀(SD) Dir(𝑝)𝜂 2 Near𝑀(SD) Dist.𝑀(SD) Dir(𝑝)𝜂 2 Near𝑀(SD) Dist.𝑀(SD) Dir(𝑝)𝜂 2
4o-T 2.815(.211) 2.796(.188)+(.631) .002 1.642(.488) 1.259(.334)+(<.001).176 2.975(.088) 2.877(.245)+(.006).068
4o-J 2.852(.211) 2.799(.213)+(.202) .015 1.420(.338) 1.117(.196)+(<.001).234 2.932(.150) 2.815(.280)+(.008).065
5.4-T 2.080(.266) 2.025(.274)+(.288) .011 1.167(.222) 1.080(.158)+(.022).049 1.852(.280) 1.469(.255)+(<.001).342
5.4-J 2.043(.243) 2.000(.259)+(.373) .007 1.136(.229) 1.056(.155)+(.035).041 1.901(.392) 1.321(.310)+(<.001).407
Note: Study 2 (DV: selected color saturation); Near/Dist.=temporally near vs. distant event condition.
52

Table E3. Study 3: Logo shape and product attributes (DV)
No Intervention Conceptual Empirical
Config Circ.𝑀(SD) Ang.𝑀(SD) Dir(𝑝)𝜂 2 Med. Circ.𝑀(SD) Ang.𝑀(SD) Dir(𝑝)𝜂 2 Med. Circ.𝑀(SD) Ang.𝑀(SD) Dir(𝑝)𝜂 2 Med.
4o-T Comf. 6.514(.507) 6.829(.514)−(.012).089 . 6.543(.611) 6.371(.731)+(.291) .016 . 6.629(.598) 6.559(.504)+(.603) .004 .
4o-T Dur. 7.600(.736) 7.343(.838)−(.177) .027 . 7.657(.482) 7.514(.562)−(.258) .019 . 5.029(.296) 4.971(.460)−(.534) .006 .
4o-J Comf. 5.743(.611) 5.971(.568)−(.110) .037 . 6.818(.528) 6.531(1.218)+(.220) .024 . 6.429(.608) 6.235(.431)+(.133) .033 .
4o-J Dur. 7.429(.739) 7.200(.833)−(.229) .021 . 7.545(.794) 7.188(1.355)−(.197) .026 . 5.000(.594) 4.912(.514)−(.512) .006 .
5.4-T Comf. 5.314(.471) 5.000(.642)+(.022).074 full 6.571(.698) 4.686(.631)+(<.001).674 full 6.857(.355) 5.114(.676)+(<.001).728 partial
5.4-T Dur. 7.000(.000) 6.971(.169)−(.321) .014 . 6.286(.458) 6.800(.406)+(<.001).266 full 3.971(.169) 5.686(.900)+(<.001).643 partial
5.4-J Comf. 5.657(.482) 5.286(.667)+(.009).095 . 6.457(.741) 4.657(.539)+(<.001).665 full 6.457(.505) 5.257(.852)+(<.001).430 full
5.4-J Dur. 7.029(.169) 7.000(.000)−(.321) .014 . 6.371(.598) 6.800(.406)+(<.001).153 partial 3.686(.471) 5.429(1.145)+(<.001).505 partial
Note: Study 3; Circ./Ang.=circular vs. angular logo condition; Comf./Dur.=perceived comfort and perceived durability (DVs), reported as separate rows per
configuration.
Table E4. Study 4: Logo asymmetry and brand excitement (DV)
No Intervention Conceptual Empirical
Config Asym.𝑀(SD) Symm.𝑀(SD) Dir(𝑝)𝜂 2 Med. Asym.𝑀(SD) Symm.𝑀(SD) Dir(𝑝)𝜂 2 Med. Asym.𝑀(SD) Symm.𝑀(SD) Dir(𝑝)𝜂 2 Med.
4o-T 4.836(.514) 4.859(.511)−(.736) .001 . 4.731(.579) 4.687(.645)+(.595) .001 . 5.027(.370) 4.901(.552)+(.048).018 full
4o-J 4.860(.492) 4.943(.515)−(.230) .007 . 5.229(.271) 5.213(.362)+(.714) .001 . 5.022(.472) 4.856(.514)+(.014).028 full
5.4-T 2.978(1.023) 3.099(1.031)−(.383) .003 . 3.865(1.192) 3.899(1.039)−(.821) .000 . 3.753(1.178) 3.785(1.125)−(.833) .000 .
5.4-J 3.135(1.091) 3.218(1.047)−(.562) .002 . 4.041(1.093) 4.009(1.082)+(.826) .000 . 3.996(1.209) 4.040(1.018)−(.772) .000 .
Note: Study 4 (DV: brand excitement); Asym./Symm.=asymmetrical vs. symmetrical logo condition.
53

Table E5. Study 5: Color saturation and estimated size (DV)
No Intervention Conceptual Empirical
Config High𝑀(SD) Low𝑀(SD) Dir(𝑝)𝜂 2 Med. High𝑀(SD) Low𝑀(SD) Dir(𝑝)𝜂 2 Med. High𝑀(SD) Low𝑀(SD) Dir(𝑝)𝜂 2 Med.
4o-T 15.026(.362) 14.811(.569)+(.052) .050 . 15.000(.000) 14.892(.458)+(.150) .028 . 15.000(.000) 14.949(.223)+(.146) .027 .
4o-J 15.179(.854) 14.844(.515)+(.055) .052 . 15.051(.320) 14.972(.167)+(.189) .023 . 15.000(.000) 14.974(.160)+(.314) .013 .
5.4-T 14.950(.316) 14.600(.778)+(.010).082 . 15.075(.350) 14.950(.221)+(.060) .045 . 15.350(.580) 15.125(.335)+(.037).055 .
5.4-J 14.900(.441) 14.400(.871)+(.002).118 . 15.050(.316) 14.925(.267)+(.060) .045 . 15.150(.362) 15.000(.226)+(.029).060 full
Note: Study 5 (DV: estimated product size); High/Low=high vs. low color-saturation condition.
Table E6. Study 6: Logo stability and utility (DV)
No Intervention Conceptual Empirical
Config Unst.𝑀(SD) St.𝑀(SD) Dir(𝑝)𝜂 2 Unst.𝑀(SD) St.𝑀(SD) Dir(𝑝)𝜂 2 Unst.𝑀(SD) St.𝑀(SD) Dir(𝑝)𝜂 2
4o-T Safety 8.032(.141) 8.086(.179)−(.136) .028 7.799(.206) 7.744(.214)+(.264) .017 7.977(.151) 7.910(.185)+(.111) .039
4o-J Safety 8.136(.089) 8.160(.148)−(.401) .009 7.849(.631) 7.762(.747)+(.581) .004 7.905(.780) 7.679(1.459)+(.443) .010
5.4-T Safety 7.151(.407) 7.168(.364)−(.844) .001 7.952(.240) 7.679(.286)+(<.001).214 7.568(.404) 7.279(.474)+(.005).100
5.4-J Safety 7.922(.347) 7.933(.284)−(.874) .000 7.098(.351) 6.810(.524)+(.006).097 7.611(.425) 7.150(.741)+(.001).130
Note: Study 6; Unst./St.=unstable vs. stable logo condition. Rows report the logo-stability simple effect within the safety-oriented product category (Safety),
based on the three-item utility composite averaged over the six products in the category; the interaction and neutral-category results for the no-intervention runs
appear in the main text.
54

Table E7. Case study: Running-shoe logo descriptiveness and brand authenticity (DV)
No Intervention Conceptual Empirical
Config More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2
5.4-T 4.504(.495) 4.567(.493)−(.425) .004 6.404(.366) 5.650(.533)+(<.001).408 6.442(.491) 6.033(.755)+(<.001).094
Note: Case-study deployment (main text, managerial implications): the stimuli are the two AI-generated running-shoe logos (More/Less=more- vs.
less-descriptive design), not stimuli from a published study. GPT-5.4-mini (TXT) is the configuration validated in the case study;𝑁=160per intervention column
(80 per logo). Because no human baseline exists for these logos,+marks a direction consistent with the Study 1 human benchmark (more descriptive→more
authentic).
55

Table E8. Tag definitions and examples for the empirical evidence (statistics) prompt
Tag Section Definition Additional fields Example
labelboth Section heading none “1. Method” / “2. Results”
samplemethod Participant
demographics and
sample size
none “We recruited 180 individuals
(𝑀𝑎𝑔𝑒 =34; 46% female) on
MTurk” (S1)
designmethod Experimental
design structure
none “a 2 (descriptiveness)×2
(replicate) between-participant
experiment” (S1)
measuresmethod Dependent
measures and
corresponding
reliabilities
construct,
reliability
construct: authenticity;
reliability:𝛼=.94(S1)
proceduremethod Experimental task
and cover story
shown to
participants
none imagine three scenarios, then pick
the matching image (S2)
manipulationmethod Operationalization
of the independent
variable
none stable=square on its base;
unstable=diamond (S6)
analysisresults Statistical modeling
approach
none a 2×2 ANOVA with authenticity
as the dependent variable (S1)
effectsresults Focal statistical
findings
dv,iv,comparison,
statistic,p,
effect_size
dv: size estimate;iv: color
saturation;comparison: high
(𝑀=15.28) vs. low (𝑀=14.41);
statistic:𝐹(1,75)=7.13;p:
<.01;effect_size:𝜂 2=.09
(S5)
mediationresults Mediation analysis
results
model,mediator,iv,dv,
path_a,path_b,
indirect,direct
model: PROCESS Model 4
(Hayes, 2022);mediator:
arousal;iv: logo asymmetry;dv:
excitement;path_a:𝑏=.41;
path_b:𝑏=.72;indirect:
95% CI [.07, .54];direct:
𝑏=.33(S4)
auxiliaryboth Supporting
analyses
none “six participants were excluded for
failing the attention check” (S4)
Note: The JSON schema comprises two primary sections:methodandresults. Every tag preserves its source
sentence verbatim within a basetextfield. The “Additional fields” column denotes nested key-value pairs used to
extract specific parameters (e.g., statistics, variable names) from that sentence. “None” indicates the tag retains only
the basetextfield (e.g.,auxiliarylacks nested fields due to high structural variance across studies). The
constructfield undermeasuresdefines the latent variable and its reliability, whereas thedvfield undereffects
references that measure during hypothesis testing. If a single source sentence satisfies multiple tags (e.g.,
simultaneously reporting sample size and design), it is assigned to the primary tag, with the secondary tag pointing to
it via reference to prevent data duplication. S1 (Study 1) through S6 (Study 6) denote the specific study from which
the example is drawn.
56

Web Appendix F: Robustness of findings
Therobustnesschecksbelowre-runtheStudy1replication(logodescriptiveness→brandauthen-
ticity)withGPT-4o-mini(TXT),theconfigurationreportedinthemaintext;TablesF1andF3were
run at temperature=1. MC/ME=manipulation check (perceived descriptiveness)/main effect
(authenticity). Dir(𝑝) and𝜂 2 follow the conventions of Web Appendix E; sample sizes match the
original study’s (Web Appendix B).
Table F1. Test-retest reliability for 5 different runs
Main Effect Manipulation Check
Run More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2
1 6.424(.369) 6.211(.417)+(.001).068 7.532(.502) 7.085(.422)+(<.001).191
2 6.424(.354) 6.198(.405)+(<.001).082 7.553(.500) 7.131(.485)+(<.001).156
3 6.464(.316) 6.263(.434)+(.001).065 7.568(.499) 7.173(.495)+(<.001).138
4 6.457(.309) 6.267(.414)+(.001).064 7.513(.503) 7.106(.464)+(<.001).152
5 6.427(.355) 6.294(.356)+(.015).035 7.565(.522) 7.083(.445)+(<.001).199
Note: Five independent reruns of the Study 1 replication under identical settings (GPT-4o-mini (TXT), temperature=
1, 512-pixel stimuli); the main text reports a single run from this set.
Table F2. Different temperature settings
Main Effect Manipulation Check
Temperature More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2
.5 6.422(.291) 6.238(.454)+(.002).056 7.547(.501) 7.046(.504)+(<.001).201
1.0 6.424(.354) 6.198(.405)+(<.001).082 7.553(.500) 7.131(.485)+(<.001).156
1.5 6.468(.286) 6.263(.426)+(.001).075 7.486(.602) 7.013(.554)+(<.001).145
Note: The Study 1 replication re-run at three temperature settings (GPT-4o-mini (TXT), 512-pixel stimuli); 1.0 is the
API default used in the main text.
Table F3. Resolution of the visual stimuli: 256, 512, 1024
Main Effect Manipulation Check
Pixel More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2 More𝑀(SD) Less𝑀(SD) Dir(𝑝)𝜂 2
256 6.461(.326) 6.228(.422)+(<.001).088 7.573(.498) 7.105(.450)+(<.001).198
512 6.424(.354) 6.198(.405)+(<.001).082 7.553(.500) 7.131(.485)+(<.001).156
1024 6.528(.209) 6.318(.396)+(<.001).099 7.646(.481) 7.267(.518)+(<.001).127
Note: The Study 1 replication re-run at three stimulus resolutions (GPT-4o-mini (TXT), temperature=1); 512 pixels
is the standard used in the main text.
57

Table F4. Testing the carryover of ratings among consecutive API calls (Study 1: 4o-mini
(TXT))
Authenticity Trustworthiness Credibility Descriptiveness
More descriptive condition
𝛽.082 .114 .379 .430
Standard error .025 .016 .026 .016
p-value .030 .002<.001<.001
Carryover
𝜆.016 .019−.000 .007
Standard error .050 .040 .029 .040
p-value .763 .659 .988 .866
Replicate Fixed Effect Yes Yes Yes Yes
N 814 814 814 814
R-squared .016 .025 .101 .168
Note: OLS estimates for Study 1, 4o-mini (TXT), pooled across the five experiment replicates (N = 814). Each
column regresses the rating𝑌𝑟𝑖 of participant𝑖in replicate𝑟on the binary condition indicator (𝛽; more vs. less
descriptive logo), the preceding participant’s rating on the same measure (𝜆, the carryover coefficient), and replicate
fixed effects. Standard errors are clustered at the replicate level. A𝜆indistinguishable from zero indicates no
carryover between consecutive API calls.
58
