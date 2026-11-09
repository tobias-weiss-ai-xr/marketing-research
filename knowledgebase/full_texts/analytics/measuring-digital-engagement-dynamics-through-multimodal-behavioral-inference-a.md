---
title: 'Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics
  framework'
url: https://doi.org/10.1057/s41270-026-00505-y
category: analytics
subcategory: framework
date: 2026-07
venue: Journal of Marketing Analytics
authors:
- Charlotte De Sainte Maresville
- Christine Petr
- Olfa Haggui
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1057/s41270-026-00505-y.pdf
pages: 18
chars: 89453
fetched_at: '2026-11-08T17:31:49+00:00'
kb_version: 1
---

# Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics framework

ORIGINAL ARTICLE
Journal of Marketing Analytics
https://doi.org/10.1057/s41270-026-00505-y
  Charlotte De Sainte Maresville
charlotte.de-sainte-maresville@univ-ubs.fr
1 IAE Bretagne Sud, Vannes, France
2 Odaptos, Montpellier, France
Abstract
Digital marketing analytics capture behavioral outcomes—clicks, dwell time, conversions—but offer limited insight into
how engagement unfolds during interaction. This research develops a multimodal framework that infers engagement-
related behavioral configurations from synchronized gesture, gaze, facial, vocal, and linguistic signals, across two overlap -
ping samples of video-mediated sessions (N = 34 and N = 40). Stress-related activation is robustly and negatively associated
with attentional stabilization, a result that withstands collinearity diagnostics, bootstrap resampling, and alternative model
specifications. Its positive association with intentional engagement is also observed at the session level, but is substantially
weaker once features shared across indicators are removed and does not hold at finer temporal resolution—underscoring
that not all engagement associations are equally robust to measurement overlap. Multimodal indicators add explanatory
power beyond attention-based metrics within the framework, though this should be read as internal incremental contribu -
tion pending external validation. This research offers a transparent behavioral inference framework and a methodological
template for testing the robustness and temporal structure of such indicators, and identifies external validation as the next
step toward establishing them as measures of engagement.
Keywords Digital engagement · marketing analytics · multimodal data · behavioral inference · digital consumer
behavior
Received: 14 April 2026 / Accepted: 23 June 2026
© The Author(s) 2026
Measuring digital engagement dynamics through multimodal
behavioral inference: a marketing analytics framework
Charlotte De Sainte Maresville1  · Christine Petr1 · Olfa Haggui2 · Felipe Restrepo2
Prior research highlights the instability of these pro -
cesses. Media multitasking, information overload, and
digital fatigue can disrupt attentional continuity (Chang and
Thorson 2023; Yap et al. 2021), while periods of height -
ened activation may instead intensify cognitive effort and
strengthen goal-directed behavior. Engagement trajectories
therefore often involve alternating phases of stabilization,
disruption, recovery, and re-engagement—dynamics that
conventional analytics, reliant on aggregated outcomes or
self-report, struggle to capture. Building robust tools for
measuring engagement as a temporally structured phenom-
enon requires not only theoretically motivated indicators,
but a clear empirical account of what these indicators can
and cannot yet demonstrate—a distinction this paper treats
as central rather than incidental.
Multimodal data collection offers a promising avenue
here. Gaze patterns, facial expressions, vocal character -
istics, linguistic cues, and micro-gestures provide fine-
grained, temporally sensitive traces of engagement as
it unfolds moment by moment (Smidts et al. 2014; He
et al. 2021). But the availability of such data does not
Introduction
Digital marketing environments generate increasingly rich
behavioral data, enabling firms to track clicks, scrolling
trajectories, dwell time, and conversion events (Wedel and
Kannan 2016; Davenport et al. 2020). Yet a fundamental
limitation remains: these widely used indicators reveal what
consumers do but offer limited insight into how engagement
unfolds in real time. As digital environments grow more
immersive and cognitively demanding (Chang and Thorson
2023; Pizzi et al. 2025), engagement is increasingly under-
stood not as a static state but as a dynamic process marked
by continuous fluctuations in attention, cognitive effort,
affective activation, and behavioral adaptation.

C. De Sainte Maresville et al.
automatically yield meaningful measures of engagement. A
central challenge lies in transforming heterogeneous signals
into theoretically interpretable indicators—and in verifying
that indicators built from overlapping behavioral signals do
not generate associations among themselves simply as an
artifact of shared measurement inputs. Without this verifica-
tion, the resulting indicators risk being treated as measures
of engagement when they may, in part, be redescriptions of
the same underlying signals.
This requires moving beyond direct observation toward
behavioral inference, while treating the validity of that
inference as an empirical question rather than an assump -
tion. Engagement may be conceptualized as a latent, evolv-
ing process that manifests indirectly through converging
behavioral signals—consistent with embodied cognition
and consumer neuroscience research showing that cogni -
tive and affective processes are partially expressed through
observable behavior (Barsalou 2008; Krishna 2011; Smidts
et al. 2014; He et al. 2021). Because these indicators are
derived from behavior rather than validated against inde -
pendent criteria, claims about what they measure are scoped
accordingly throughout this paper.
Building on this perspective, the present research devel -
ops a transparent multimodal behavioral inference frame -
work integrating gaze, facial, vocal, linguistic, and gestural
signals into theory-driven indicators of attention-related
activity, stress-related activation, and regulatory processes.
A central objective is to examine the role of stress-related
activation, for which prior literature offers competing pre -
dictions: overload perspectives suggest it disrupts atten -
tional continuity (Yap et al. 2021), while effort-mobilization
perspectives suggest it intensifies goal-directed engagement
(Baumeister et al. 1998). Rather than assuming a uniform
effect, this research examines whether stress-related activa-
tion is differentially associated with distinct engagement
components—and, critically, whether any such pattern can
be distinguished from artifacts of shared measurement con-
struction and from purely contemporaneous co-occurrence.
The framework is evaluated across two studies based on
overlapping samples (N = 34 and N = 40, with 33 of 40 par -
ticipants common to both; see Sect.  “Study Design, Sample,
and Relationship to Study 1”). Study 1 maps micro-gestural
expressions onto theoretically grounded engagement cat -
egories. Study 2 extends this through multimodal inference,
examining relationships among stress-related activation,
attentional stabilization, and intentional engagement, and
assessing whether multimodal indicators add explanatory
value beyond attention-based measures. The central find -
ings are subjected to robustness checks addressing measure-
ment overlap, sample sensitivity, and temporal ordering.
This research contributes to marketing analytics in
four ways. First, it specifies a fully reported, transparent
procedure for transforming heterogeneous behavioral sig -
nals into engagement indicators, including the complete
gesture-to-category classification underlying Study 1. Sec -
ond, it advances a process-oriented view of engagement and
directly tests its temporal structure rather than inferring it
from session-level aggregates alone. Third, it documents
a differentiated pattern in which stress-related activation
is robustly associated with lower attentional stabilization,
while its association with intentional engagement proves
considerably more sensitive to how indicators are con -
structed. Fourth, it offers a methodological template—com-
bining collinearity diagnostics, models suited to bounded
proportional data, feature-overlap analysis, and segment-
level temporal testing—for assessing whether behaviorally
inferred engagement indicators reflect genuine dynamics
rather than measurement artifacts.
Literature review and hypotheses
development
Theoretical framework and multimodal
engagement
Digital consumer engagement has traditionally been con -
ceptualized as a static outcome: click-through rates, time on
page, conversion events, consistent with marketing analyt -
ics’ dominant focus on exposure and response metrics. Yet
engagement is more appropriately understood as a dynamic,
temporally evolving process. Consumers continuously real-
locate cognitive resources in response to changing stimuli
and task demands, alternating between sustained attention,
cognitive effort, exploration, and fragmentation (Chang and
Thorson 2023; Pizzi et al. 2025). Aggregated outcome mea-
sures remain largely insensitive to this temporal variation.
Dual-process theories of persuasion offer a useful foun -
dation: cognitive processing depends jointly on motivation
and capacity, which determine whether individuals engage
in systematic or heuristic processing (Petty & Cacioppo,
1984). Digital interaction is also associated with stress-
related activation, for which two perspectives compete.
Overload theories suggest activation reflects excessive
demand, fragmenting attention and reducing processing
continuity (Yap et al. 2021), whereas self-regulation and
effort-mobilization theories propose that moderate strain
can instead function as a challenge signal that mobilizes
effort and reinforces goal-directed processing (Baumeister
et al. 1998). This tension suggests activation may disrupt
or intensify engagement depending on which dimension of
engagement is examined, a possibility this paper treats as a
hypothesis to be tested rather than resolved by assumption.

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
Resolving this requires moving beyond outcome-based
measurement toward process-oriented behavioral infer -
ence, integrating gaze, facial, vocal, linguistic, and ges -
tural signals that provide fine-grained, time-sensitive traces
of interaction (Smidts et al. 2014; He et al. 2021). This is
consistent with embodied cognition and consumer neurosci-
ence research suggesting cognitive and affective processes
are partially expressed through observable behavior (Barsa-
lou 2008; Krishna 2011). No single cue reveals engagement
on its own. Gaze concentration, vocal intensity, and motor
activity are each ambiguous in isolation, so engagement is
inferred from converging patterns across channels.
Accordingly, engagement indicators are conceptualized
as behavioral configurations derived from the convergence
of multiple observable cues, without assuming direct obser-
vation of internal psychological states. Three dimensions
recur across the engagement, self-regulation, and cognitive-
processing literatures and anchor the present framework:
attention-related indicators (allocation and stability of
cognitive resources), stress-related activation (arousal and
strain generated by task demands), and regulatory activity
(behavioral adjustment toward restoring goal-directed pro -
cessing under strain). These dimensions are not assumed
to operate independently. Engagement emerges from their
interaction over time, and is examined here through two
outcomes, attentional stabilization and intentional engage -
ment, that may respond differently to the same underlying
activation processes.
Figure 1 illustrates the proposed conceptual framework,
linking multimodal behavioral indicators of attention,
stress-related activation, and regulatory activity to these two
engagement outcomes.
Attention-related behavioral indicators and
distraction
Attention is a central mechanism underlying sustained
engagement. Stable cognitive allocation facilitates sys -
tematic processing and sustained task involvement (Petty
& Cacioppo, 1984), while competing stimuli and infor -
mational density make attentional persistence increasingly
vulnerable to disruption in digital environments (Chang and
Thorson 2023). Attention cannot be directly observed, but
prior research associates sustained gaze allocation, reduced
motor dispersion, and stable posture with greater concen -
tration, and frequent behavioral shifts with distraction and
fragmentation (Barsalou 2008; Krishna 2011). Information-
overload research further suggests that attentional instabil -
ity increases switching and interruption (Yap et al. 2021).
H1. Attention-related behavioral indicators are negatively
associated with distraction during digital interaction.
Stress-related activation and engagement outcomes
As outlined above, overload and effort-mobilization per -
spectives generate competing predictions about stress-
related activation. Rather than assuming a uniform effect,
the present framework treats attentional stabilization and
intentional engagement as partially distinct processes that
may respond differently to the same activation. Stress-
related activation can be approximated through converging
indicators such as arousal fluctuations, affective variation,
vocal intensity, and behavioral adjustment, documented in
prior research. These indicators do not directly measure
psychological stress but provide behavioral configurations
consistent with activation-related processes.
Fig. 1 A multimodal marketing
analytics framework for inferring
digital engagement dynamics

C. De Sainte Maresville et al.
For attentional stabilization, the overload account is
unambiguous: heightened activation should fragment atten-
tion and reduce processing continuity.
H2a.  Stress-related behavioral indicators are negatively
associated with attentional stabilization during digital
interaction.
For intentional engagement, the effort-mobilization
account predicts a positive association, but this prediction is
harder to dissociate empirically from a methodological con-
cern specific to behaviorally inferred indicators. If the fea -
tures used to construct a stress-related tag overlap with those
used to construct an intentional-engagement tag, a positive
association could emerge mechanically rather than reflect -
ing an independent behavioral process. This study therefore
treats the effort-mobilization prediction as a hypothesis to
be evaluated jointly against both the data and this alternative
explanation, rather than as a finding to be confirmed by a
single model specification (see Sect.  “Regulatory Activity:
H3 and H4”).
H2b.  Stress-related behavioral indicators are positively
associated with intentional engagement during digital
interaction; this association should be evaluated against
the alternative possibility that it reflects shared measure -
ment construction rather than an independent behavioral
process.
Regulatory activity and attentional stabilization
Engagement stability also depends on regulatory capacity.
Self-regulation theories suggest individuals continuously
adjust cognitive and behavioral responses to maintain goal-
directed activity under changing conditions (Baumeister et
al. 1998), and regulatory resources may determine whether
activation contributes to sustained engagement or instead
produces instability and switching (Petty & Cacioppo,
1984). Because regulatory processes are difficult to observe
directly, the present framework conceptualizes regulatory
activity through behavioral configurations indicative of
stabilization or reorganization following heightened activa-
tion, interpreted as potential manifestations of self-regula -
tion rather than direct measurements of it.
H3. Regulatory behavioral indicators are positively associ-
ated with attentional stabilization during digital interaction.
H4. Regulatory behavioral indicators moderate the rela -
tionship between stress-related activation and attentional
stabilization, such that the negative association is weaker
when regulatory activity is higher.
Incremental validity of multimodal engagement
indicators
Traditional analytics measures, such as duration, click-
through rates, scrolling depth, and average arousal (Wedel
and Kannan 2016), may obscure meaningful variation,
since interactions with similar duration or activity levels
can reflect markedly different underlying processes. Mul -
timodal behavioral analytics aims to capture this variation
by integrating converging signals across modalities (Smidts
et al. 2014; He et al. 2021), but its contribution depends
on explaining variance beyond simpler attention-based
measures. Within the present framework, this is tested by
comparing models predicting an engagement outcome from
an attention-based indicator alone against models that add
a multimodal indicator. Because both predictors originate
from the same tagging pipeline, the resulting test should be
interpreted as evidence of internal incremental contribution
within the framework, not as validity against an external,
independently measured engagement criterion, a distinction
made explicit when interpreting the results (Sect.  “ Results
Concerning H5: Incremental Validity of Multimodal
Engagement Indicators”).
H5. Multimodal engagement indicators explain incremen -
tal variance in engagement outcomes beyond baseline
attention-based metrics, within the present measurement
framework.
Study 1
Methods
Study design and data structure
Study 1 adopts an observational design to examine whether
fine-grained behavioral data can be systematically orga -
nized into interpretable engagement indicators in digitally
mediated interactions. Rather than relying on experimen -
tal manipulation, the study leverages naturally occurring
behavioral traces captured during video-mediated ses -
sions. The objective is not to infer latent psychological
states directly, but to establish a behavioral measurement
layer linking observable micro-behaviors to theoretically
grounded engagement categories (Smidts et al. 2014; He et
al. 2021).
The dataset consists of 34 webcam-recorded interaction
sessions, each involving a single participant responding
to structured interview prompts under non-scripted condi -
tions, recorded at 20 frames per second. The primary unit of
analysis is the temporally localized micro-gesture sequence,

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
preserving the sequential structure of behavioral activity
rather than collapsing it into session-level aggregation at
the outset. Behavioral sequences are first detected at the
gesture level and subsequently organized into higher-order
engagement categories through the theory-driven mapping
procedure described below, with categories defined prior to
statistical analysis.
Accordingly, Study 1 pursues three objectives: assess -
ing whether micro-gestural signals can be reliably detected
and classified, developing a transparent procedure for map-
ping observed behaviors onto engagement categories, and
evaluating the resulting indicators descriptively ahead of
their integration into the multimodal framework developed
in Study 2.
Gesture detection and behavioral extraction
An automated gesture recognition framework extracted
micro-gestural features from continuous video, combin -
ing visual appearance features from RGB frames (spatio-
temporal convolutional architecture) with skeletal motion
information (graph-based representation of body joints)
within a unified recognition framework. The system identi -
fies 37 categories of upper-body micro-gestures, including
head movements, posture adjustments, and hand-to-face
behaviors, detected continuously throughout each session
as temporally segmented sequences. Model performance,
evaluated on a benchmark gesture-recognition dataset,
reached 83.7% Top-1 accuracy and 95.6% Top-5 accuracy,
consistent with contemporary gesture-recognition systems;
this accuracy bears on the reliability of gesture detection
itself, not on the validity of the subsequent mapping from
gestures to engagement categories, which is evaluated sepa-
rately below.
The gesture-recognition framework operates strictly at
the level of observable behavior: it does not infer atten -
tion, stress, or engagement directly. Gesture detection and
engagement inference are therefore treated as two distinct
analytical steps.
Theory-driven construction of engagement categories and
mapping procedure
Five engagement categories were specified a priori from
recurring constructs in the embodied cognition, nonverbal
communication, attention, and interaction-behavior litera -
tures (Barsalou 2008; Burgoon et al., 2016; Krishna 2011;
Mehrabian and Williams 1969), rather than derived induc -
tively from the data. Focused Attention reflects sustained
task orientation, indexed by stable body orientation and
reduced movement variability (Petty & Cacioppo, 1984;
Barsalou 2008). Reflective Processing captures internally
oriented evaluation, indexed by reduced interactional activ-
ity or contemplative posture (Krishna 2011). Distracted
refers to behavioral variability potentially associated with
attentional fragmentation, indexed by frequent posture
changes and movement dispersion (Chang and Thorson
2023; Yap et al. 2021). Interactive captures synchronization
with the ongoing interaction, indexed by conversational
alignment and responsive gestures (Burgoon et al., 2016).
Tired represents reduced cognitive energy or diminished
responsiveness, indexed by decreased movement energy.
These categories are not mutually exclusive psychological
states but theoretically informed behavioral configurations
that can co-exist and vary across contexts.
Each of the 37 detected gestures was assigned to one of
these five categories using mapping rules established ex ante
from the same literature, rather than inferred from the pres-
ent data, following a conservative strategy in which gestures
were assigned only when behavioral characteristics clearly
matched predefined criteria. Table 1 reports the complete
mapping, including every detected gesture, its dominant
assigned category, and its classification purity (the propor -
tion of occurrences of that gesture assigned to its dominant
category, out of 4,177 classified gesture-phrase instances
across the 40 available recording files). Classification purity
exceeds 90% for 29 of the 37 gestures and reaches 100% for
13 of them, indicating that the mapping is close to determin-
istic for most gestures rather than probabilistic.
From gesture sequences to session-level indicators
Following classification, each temporally segmented inter -
action unit was assigned to one of the five categories, pro -
ducing a sequence of behavioral states per participant.
Engagement indicators were then operationalized as pro -
portional measures: for each participant, the number of seg-
ments assigned to a category was divided by the total number
of classified segments, yielding five indicators ranging from
0–1 and summing to 1 per participant. This controls for vari-
ation in session length, preserves the relative distribution of
states within each interaction, and represents engagement
as a multidimensional profile rather than a single aggregate
score. These indicators should not be interpreted as direct
measures of psychological states, but as the relative preva -
lence of theoretically informed behavioral configurations.
Sample characteristics
The Study 1 dataset comprised 34 video-mediated ses -
sions retained from an initial pool of 40 recordings. The
six excluded sessions did not meet the inclusion criterion
of adequate frontal gaze orientation: participants who
spent insufficient time looking directly at the camera did

C. De Sainte Maresville et al.
not generate reliable gaze-based signal and were excluded
prior to analysis. Participants were users of a commercial
facereading tool who consented to having their interaction
data used for model development beyond their personal use;
no dedicated recruitment took place and no compensation
was provided. Sessions consisted of semi-structured human-
to-human video interviews covering everyday topics.
The full pool of 40 participants (20 female, 20 male)
ranged in age from 19–60 years (M = 36.9, SD = 11.2) and
represented a wide range of occupational backgrounds,
including students, salaried employees, independent profes-
sionals, and retirees. Educational attainment ranged from
vocational qualification to doctoral degree, with the larg -
est subgroup holding a five-year university degree ( n = 15).
Self-reported video-mediated communication (VMC)
experience varied considerably: 50% reported high or very
high familiarity with video-based interaction, while 22%
reported low or very low familiarity, providing heteroge -
neity in digital interaction background. Session duration
ranged from 1.5–26.5 min (M = 11.7 min, SD = 5.6). Explor-
atory descriptive analyses by gender and, at an aggregated
continental level, by region were conducted to identify
potential heterogeneity rather than to test formal group dif -
ferences. Given the observational design and modest sample
size, Study 1 does not seek to establish causal relationships;
its primary objective is methodological, namely evaluating
whether multimodal behavioral traces can be systematically
transformed into interpretable engagement indicators.
Results, study 1
Distribution of behavioral engagement categories
Tables 2 and 3 report the aggregated distribution of the five
engagement categories, separately for male and female par-
ticipants. Among male participants, Focused represented
48.6% of classified segments, followed by Distracted
Table 1 Complete mapping between detected gestures and engage -
ment categories
Detected gesture Dominant
category
Classifica-
tion
purity
N
occur-
rences
Fixed Focused 98.6% 883
Frequent movement Distracted 96.2% 630
Tilt right/left Reflective 97.3% 475
Hands forming a pyramid Focused 100.0% 364
Turn right/left Interactive 99.2% 355
Speech-correlated hand
movement
Interactive 96.1% 206
Down right/left Tired 98.9% 182
Support the head Tired 100.0% 159
Lateral movement Interactive 95.9% 123
Up right/left Reflective 99.1% 106
Covering the face with
hands
Interactive 95.6% 91
Forward bending Focused 96.2% 79
Touching or supporting the
chin
Reflective 97.1% 69
Touching or scratching neck Tired 95.0% 60
Touching the lips Focused 93.9% 49
Shaking shoulders Interactive 97.4% 38
Shake Distracted 100.0% 32
Scratching the head/face Distracted 100.0% 31
Fingers interwined Focused 93.5% 31
Holding items Distracted 90.0% 30
Touching the forehead Tired 88.9% 27
Covering the mouth with
a hand
Interactive 100.0% 24
Pinching the bridge of the
nose
Tired 95.5% 22
Hands with palms up Focused 86.4% 22
Playing or adjusting hair Distracted 100.0% 17
Backward bending Reflective 93.3% 15
Rubbing the eyes Tired 100.0% 12
Retract Reflective 100.0% 11
Pointing with thumb Distracted 88.9% 9
Sitting straightly Focused 100.0% 7
Dusting off clothes Distracted 100.0% 5
Nod Focused 100.0% 5
Rubbing the temple Tired 100.0% 4
Putting arms behind body Tired 100.0% 1
Folding arms Reflective 100.0% 1
Slowly closing and opening
hand
Reflective 100.0% 1
Tugging or pulling the ear Distracted 100.0% 1
Classification purity indicates the proportion of occurrences of a
given gesture assigned to its dominant category, computed over 4177
classified gesture-phrase instances across the 40 available recording
files. Purity exceeds 90% for 29 of the 37 gestures and reaches 100%
for 13 of them
Table 2  Distribution of engagement categories, male participants
(Study 1)
Engagement category Percentage (%)
Focused 48.6
Distracted 34.2
Interactive 10.1
Reflective 5.4
Tired 1.7
Total 100
Table 3 Distribution of engagement categories, female participants
(Study 1)
Engagement category Percentage (%)
Focused 31.8
Interactive 26.2
Reflective 25.3
Distracted 11.7
Tired 5.0
Total 100

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
(34.2%), Interactive (10.1%), Reflective (5.4%), and Tired
(1.7%), a profile dominated by task-oriented attentional
activity with periodic distraction. Among female partici -
pants, Focused also led (31.8%), but the distribution was
markedly more balanced: Interactive accounted for 26.2%,
Reflective for 25.3%, Distracted for only 11.7%, and Tired
for 5.0%.
These descriptive patterns indicate that the tagging
framework captures heterogeneity in engagement configu -
rations rather than producing uniform classifications. Given
the modest sample size, these comparisons remain explor -
atory and are not intended to establish formal gender dif -
ferences. At a broad continental level (Table 4), American
participants displayed higher Focused (42.5%) and Dis -
tracted (28.7%) proportions, while European participants
showed greater Interactive (24.8%) and Reflective (13.6%)
proportions, descriptive evidence that the framework is sen-
sitive to contextual variation.
Descriptive statistics and correlational structure
Session-level descriptive statistics and pairwise correla -
tions were computed across the five categories (Tables 5
and 6). Focused exhibited the highest average prevalence
(M = 34.6%, SD = 27.6), followed by Distracted (M = 25.7%,
SD = 24.0), Interactive (M = 19.6%, SD = 14.4), Reflective
(M = 14.7%, SD = 23.3), and Tired (M = 5.5%, SD = 8.5);
the large standard deviations indicate that some participants
displayed concentrated engagement patterns while others
distributed more evenly across categories.
Focused is negatively associated with Distracted
(r = − 0.42), Interactive ( r = − 0.36), and Reflective
(r = − 0.47), while Distracted is moderately negatively asso-
ciated with Reflective ( r = − 0.35). Interactive and Reflec -
tive show near-zero association (r = − 0.05), supporting their
distinction despite conceptual proximity. These correlations
indicate that the categories form a structured behavioral sys-
tem rather than independent or randomly assigned labels,
consistent with the theoretical expectations underlying their
construction.
Hypothesis test for H1
H1 predicts that attention-related behavioral indicators
are negatively associated with distraction. A session-level
OLS model with Distracted as the dependent variable and
Focused as the predictor shows a negative, significant asso-
ciation (β = −0.417, t = − 2.598, p = 0.014, R2 = 0.174). This
is consistent with the correlational evidence above and pro-
vides an initial validation of the tagging procedure, in the
limited sense that two theoretically opposing categories,
constructed from largely non-overlapping behavioral cues
(sustained orientation versus movement dispersion), exhibit
the expected empirical relationship.
H1 is supported. This result speaks to the internal coher-
ence of the Study 1 categories; it does not by itself estab-
lish that these categories track the psychological constructs
they are named after, a question addressed more directly
through the robustness analyses in Study 2.
Transition to study 2
Study 1 provides preliminary support for the behavioral
measurement framework: the categories display meaningful
variability across participants and contexts, their pairwise
relationships align with theoretical expectations, and the
Focused/Distracted association supports the internal coher -
ence of the measurement layer. Study 1 remains descriptive,
however, and does not address how engagement dimen -
sions jointly relate to broader dynamics, nor whether stress-
related activation disrupts attentional stability, reinforces
goal-directed engagement, or both.
Study 2 moves from measurement validation to explana-
tory modeling. Using a larger multimodal dataset integrat -
ing video, audio, gaze, and linguistic indicators, it examines
how stress-related activation, fixation behavior, attentional
stabilization, intentional engagement, and regulatory activ -
ity relate to one another, and subjects these relationships to
the robustness checks motivated by the measurement con -
cerns raised above.
Table 4 Exploratory distribution of engagement categories by geo -
graphic region
Continent Focused (%) Distracted
(%)
Interactive
(%)
Reflec-
tive
(%)
Americas 42.5 28.7 18.9 7.1
Europe 36.9 22.4 24.8 13.6
Table 5  Descriptive statistics of behavioral engagement categories
(Study 1, N = 34)
Engagement category Mean (%) SD Min Max
Focused 34.6 27.6 0.0 97.8
Distracted 25.7 24.0 0.0 100.0
Interactive 19.6 14.4 0.0 70.9
Reflective 14.7 23.3 0.0 87.9
Tired 5.5 8.5 0.0 45.1
Table 6  Correlation matrix of behavioral engagement categories
(Study 1, N = 34)
Focused Distracted Interactive Reflective Tired
Focused 1.00 −0.42 −0.36 −0.47 −0.18
Distracted −0.42 1.00 −0.22 −0.35 −0.13
Interactive −0.36 −0.22 1.00 −0.05 0.23
Reflective −0.47 −0.35 −0.05 1.00 −0.16
Tired −0.18 −0.13 0.23 −0.16 1.00

C. De Sainte Maresville et al.
Study 2
Methods
Study design, sample, and relationship to study 1
Study 2 builds on the measurement framework validated in
Study 1, extending it through multimodal behavioral infer -
ence. The analytical objective is to investigate whether
theoretically derived behavioral configurations exhibit
relationships consistent with the proposed engagement
framework, and to subject these relationships to a series of
robustness checks addressing the measurement concerns
raised in Sects.  “Literature Review and Hypotheses Devel-
opment” and “Study 1”.
The unit of analysis is the interaction session ( N = 40),
drawn from sessions with complete multimodal informa -
tion across video, audio, gaze, and linguistic channels.
The sample overlaps substantially with Study 1: of the 40
participants in Study 2, 33 match Study 1 participants by
exact identifier, and a further 5 are very likely the same
individuals under alternate file naming (82.5% exact over -
lap, up to 95% accounting for naming variants); two cases
remain unresolved. Participant characteristics are described
fully in Sect.  “Sample Characteristics”; in brief, the 40-ses-
sion sample (20 female, 20 male; age M = 36.9, SD = 11.2,
range 19–60) comprised users of a commercial facereading
tool who had consented to secondary use of their interac -
tion data, spanning diverse occupational and educational
backgrounds and varying levels of prior video-mediated
communication experience. Sessions were semi-structured
human-to-human video interviews and averaged 11.7 min
in duration (SD = 5.6).
Study 1 and Study 2 are therefore best understood as a
measurement-development phase and an explanatory phase
applied to largely the same sample, rather than as fully
independent studies, and results are interpreted accordingly
throughout.
Multimodal signals were first analyzed at the segment
level to identify behavioral configurations, then aggre -
gated into session-level proportional indicators, preserv -
ing comparability across interactions of varying duration.
Because several indicators originate from partially overlap-
ping multimodal streams, the analyses are not intended to
establish causal effects among fully independent constructs;
this overlap is treated as an empirical question rather than
an assumption, and is tested directly in Sect.  “ Regulatory
Activity: H3 and H4” by reconstructing indicators from dis-
joint feature subsets. All session-level models are estimated
using OLS as the primary specification; where bounded,
sparse proportional outcomes raise concerns about OLS
assumptions, results are cross-checked against fractional
logit models with robust standard errors (Sect.  “ Results
Concerning H2a: Stress and Attentional Stabilization ”),
and against participant-clustered segment-level models that
exploit the temporal ordering of segments within sessions
(Sect.  “Regulatory Activity: H3 and H4”).
Multimodal tag construction and operationalization
Segment-level engagement indicators were derived from
synchronized video, audio, gaze, and textual data. Each ses-
sion was decomposed into temporally bounded segments,
within which visual attention metrics, affective indicators
(valence, arousal), vocal characteristics, facial expression
signals, and linguistic markers were extracted and stan -
dardized. Tag construction followed a theory-driven fusion
procedure: candidate indicators were identified from prior
literature, behavioral rules were specified ex ante, and oper-
ational thresholds were conservatively calibrated within the
observed data distribution. No tag was assigned on the basis
of a single cue; classification required convergence across
at least two modalities within the same segment. Table 7
summarizes the operationalization procedure for all six
tags, including the specific behavioral indicators, literature-
informed benchmarks, and classification rule for each.
Dependent variables and robustness strategy
The analyses focus on two primary outcomes: attentional
stabilization, operationalized as the session-level propor -
tion of ATTENTION_HIGH segments, and intentional
engagement, operationalized as the proportion of INTEN -
TION_POS segments. FIXATION is examined as a poten -
tial intermediate mechanism; INTENTION_NEG and
REGULATION_ACTIVE, both sparse and right skewed,
are retained for exploratory analyses only. All dependent
variables represent behavioral configurations inferred from
multimodal evidence, not direct measurements of latent psy-
chological states; the strength of this inference is assessed
empirically rather than assumed, through the feature-over -
lap and temporal analyses reported below.
Three additions extend the original analytical strategy
in response to measurement concerns raised during review.
First, participant gender (20 female, 20 male) is introduced
as a covariate and interaction term in the H2a and H2b mod-
els, to assess whether the central associations generalize
across subgroups. Second, total session duration is intro -
duced as a covariate, as a partial proxy for task duration
and fatigue in the absence of direct measures of prompt
difficulty or interviewer identity. Third, collinearity and
influence diagnostics (variance inflation factors, condition
indices, bootstrap confidence intervals, leave-one-out esti -
mation) are reported for the H2a model, given that STRESS,

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
FIXATION, and REGULATION_ACTIVE are constructed
from overlapping behavioral signals.
Analytical models
H1 was assessed in Study 1 via a session-level regression of
Distracted on Focused. In Study 2, H2a was tested by regress-
ing ATTENTION_HIGH on STRESS, first alone and then
together with FIXATION and REGULATION_ACTIVE;
H2b was tested analogously for INTENTION_POS, with
a fuller model additionally including ATTENTION_HIGH.
H3 was assessed through the direct association between
REGULATION_ACTIVE and ATTENTION_HIGH, and
H4 through an interaction model between STRESS and
REGULATION_ACTIVE; given the low prevalence of
REGULATION_ACTIVE, both are interpreted cautiously.
H5 was tested through nested models comparing the
explanatory power of ATTENTION_HIGH alone against
ATTENTION_HIGH plus STRESS in predicting INTEN -
TION_POS, evaluated through ΔR2.
Beyond these original specifications, two additional
tests were conducted to directly evaluate the measurement
concerns motivating this revision. First, the H2a and H2b
associations were re-estimated using fractional logit mod -
els with robust standard errors, appropriate for outcomes
bounded in [0,1], and subjected to bootstrap, leave-one-out,
and variance-inflation diagnostics. Second, segment-level
models examined whether STRESS at a given segment
predicts ATTENTION_HIGH or INTENTION_POS at the
following segment or two segments later, using participant-
clustered logistic regression and permutation tests, to assess
whether the session-level associations reflect a temporally
ordered process or only contemporaneous co-occurrence.
All continuous predictors were standardized prior to esti -
mation; given the modest sample size and observational
design, results throughout are interpreted as associative
rather than causal.
Results
Convergent validity: human coding of a stratified segment
sample
To provide partial evidence that the algorithmic tags capture
behavioral signals recognizable independently of the pipe -
line itself, a stratified blind-coding procedure was conducted
on a subsample of 144 segments drawn from the full data -
set (4391 segments, 40 sessions). Segments were stratified
across the four combinations of STRESS × INTENTION_
POS values and additionally oversampled for ATTEN -
TION_HIGH = 1, covering 37 of the 40 participants; the
order was randomized prior to coding. One of the authors
coded each segment on three 0–2 scales—STRESS_per -
ceived, INTENTION_perceived, and ATTENTION_per -
ceived—based solely on the transcript text, without access
to any algorithmic tag values (blind coding). Scale anchors
were defined from the same theoretical criteria as the tags in
Table 7: STRESS_perceived captured signs of strain or acti-
vation in speech patterns (hesitations, urgency, self-correc -
tion); INTENTION_perceived captured approach-oriented,
positively engaged language; ATTENTION_perceived
Table 7 Theoretical grounding and operationalization of multimodal engagement tags
Tag Construct Modalities Behavioral indicators Classification rule
ATTENTION_HIGH Sustained atten-
tional allocation
Gaze, pos-
ture, gesture
Fixation duration, gaze
entropy, scanpath transitions,
motor stability
Sustained fixation, low gaze dispersion, stable
posture, converging across indicators (Just &
Carpenter, 1976; Rayner, 1978; Wedel & Piet-
ers, 2008)
STRESS Cognitive strain
and activation
V oice, face,
gaze, text
Arousal, valence, vocal
intensity, blink variability,
stress-related language
Elevated activation and strain confirmed by ≥ 2
independent modalities (Healey & Picard, 2005;
Yap et al. 2021)
FIXATION Concentrated
attentional
capture
Gaze, affec-
tive signals
Fixation duration, dwell time,
emotional salience
Prolonged visual concentration co-occurring
with affective activation toward a target (Lang
et al., 1997; Smidts et al. 2014)
INTENTION_POS Approach-
oriented
engagement
Text, voice,
face, gaze
Positive sentiment, approach
language, positive valence and
tone, target-oriented gaze
≥ 2 modalities converging toward approach ori-
entation, including ≥ 1 semantic/affective indica-
tor (Petty & Cacioppo, 1984; Krishna 2011)
INTENTION_NEG Avoidance-
oriented
engagement
Text, voice,
face, gaze
Negative sentiment, avoidance
language, negative affect, gaze
avoidance
Multiple modalities jointly indicating avoidance
tendencies (Elliot, 2006)
REGULATION_ACTIVE Self-regulation
and recovery
after activation
V oice, text,
gaze, face
Arousal recovery, attentional
refocusing, self-correction
language
Multimodal signals of behavioral reorganization
or stabilization (Baumeister et al. 1998; Gross,
1998)
Thresholds are conservative decision rules calibrated within the observed dataset, not universal psychological cut-offs; classification requires
convergence across ≥ 2 modalities. Full literature benchmarks and additional examples appear in Appendix A

C. De Sainte Maresville et al.
captured the coherence and focus of the verbal response.
Results are reported in Table 17.
STRESS and INTENTION_POS show statistically sig -
nificant positive correspondence between the algorithmic
classification and independent human perception (r = 0.367
and r = 0.307, both p < 0.001), with notably higher human-
perceived activation and approach orientation in algorithmi-
cally tagged segments than in untagged ones. In both cases,
Cohen’s κ falls in the “fair agreement” range (κ = 0.242 and
κ = 0.225), which is consistent with the expectation that a
text-only coding will capture only a fraction of the multi -
modal signal embedded in the algorithmic tags, which also
incorporate gaze, voice, and facial features not accessible
through the transcript alone.
ATTENTION_HIGH shows no significant correspon -
dence with human text-based coding ( r = − 0.069, p =
0.411). This result is interpretable given that this tag is
constructed primarily from gaze and postural features—
behavioral channels that leave limited traces in speech tran-
scripts. The absence of text-based agreement does not by
itself invalidate the ATTENTION_HIGH tag, but it means
that text-based human coding is not an appropriate valida -
tion method for this particular construct; its validity rests
instead on the theoretical and empirical evidence reported
in Sect.  “ Results Concerning H2a: Stress and Attentional
Stabilization”.
Three limitations of this validation procedure should
be noted. First, the coding was conducted by one of the
authors, which introduces potential familiarity bias even in
blind conditions. Second, human coding was restricted to
the transcript text and could not draw on the vocal, facial,
and gaze channels that the algorithmic system integrates;
the agreement statistics therefore constitute a lower bound
rather than an unbiased estimate of true correspondence.
Third, this procedure provides convergent evidence for the
face validity of the tags in terms of behavioral recogniz -
ability, not criterion validity against an independent mar -
keting outcome—the latter remains a necessary next step,
as discussed in Sect.  “Limitations and Avenues for Future
Research”.
Descriptive statistics and correlational structure
Table 8 reports on session-level descriptive statistics.
ATTENTION_HIGH exhibits the highest mean preva -
lence (M = 0.230, SD = 0.217), with considerable variability
across sessions. STRESS occurs less frequently on average
(M = 0.062, SD = 0.087) but shows meaningful dispersion,
consistent with activation-related configurations emerging
episodically. INTENTION_NEG is highly skewed, and
REGULATION_ACTIVE remains comparatively infre -
quent, consistent with the conservative classification crite -
ria described in Sect.  “Multimodal Tag Construction and
Operationalization”.
Table 9 reports the correlation structure. STRESS is
strongly positively associated with FIXATION ( r = 0.708)
and with INTENTION_POS ( r = 0.593) and negatively
associated with ATTENTION_HIGH ( r = − 0.257). Taken
at face value, this configuration suggests that stress-related
activation co-occurs with greater localized concentration
and stronger intentional engagement while being associ -
ated with lower attentional stabilization. However, because
STRESS, FIXATION, and ATTENTION_HIGH partially
share underlying behavioral inputs (Sect.  “Multimodal Tag
Construction and Operationalization ”; Table 7), these cor -
relations alone cannot establish whether the pattern reflects
genuine behavioral co-variation or measurement overlap.
Section  “Regulatory Activity: H3 and H4 ” addresses this
question directly by reconstructing STRESS from feature
subsets to disjoint from those used for ATTENTION_HIGH
and INTENTION_POS.
Results concerning H2a: stress and attentional stabilization
In the baseline model, STRESS is negatively but non-
significantly associated with ATTENTION_HIGH (β
= −0.645, p > 0.05). When FIXATION and REGULA -
TION_ACTIVE are added (Model 2), the associa -
tion strengthens and becomes significant (β = −1.472,
Table 8 Descriptive statistics of multimodal engagement tags (N = 40)
Variable Mean SD Min Max
ATTENTION_HIGH 0.230 0.217 0.000 0.976
STRESS 0.062 0.087 0.000 0.451
FIXATION 0.006 0.010 0.000 0.049
INTENTION_POS 0.021 0.028 0.000 0.122
INTENTION_NEG 0.038 0.124 0.000 0.750
REGULATION_ACTIVE 0.009 0.019 0.000 0.091
Table 9 Correlation matrix of multimodal engagement tags (N = 40)
INT_POS INT_NEG FIXATION STRESS ATT_HIGH REG_ACTIVE
INTENTION_POS 1.000 −0.065 0.465 0.593 −0.117 −0.070
INTENTION_NEG −0.065 1.000 0.064 −0.012 −0.211 −0.086
FIXATION 0.465 0.064 1.000 0.708 0.031 0.005
STRESS 0.593 −0.012 0.708 1.000 −0.257 −0.123
ATTENTION_HIGH −0.117 −0.211 0.031 −0.257 1.000 −0.037
REGULATION_ACTIVE −0.070 −0.086 0.005 −0.123 −0.037 1.000

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
p = 0.011); FIXATION is itself positively associated
with ATTENTION_HIGH (β = 9.672, p = 0.046). This
large FIXATION coefficient reflects its small variance
(SD = 0.010, roughly 22 times smaller than SD = 0.217
for ATTENTION_HIGH) rather than an unusually strong
effect; standardized coefficients are reported alongside
unstandardized ones in Table 10 to aid comparison.
Because STRESS, FIXATION, and REGULATION_
ACTIVE share measurement inputs, this model was sub -
jected to a full diagnostic battery rather than reported
at face value, summarized in Table 11. Variance infla -
tion factors are modest (all below 2.1), and the design
matrix condition index does not exceed 2.47, both well
below conventional concern thresholds. A 5000-sample
bootstrap yields a 95% confidence interval for the stan -
dardized STRESS coefficient that excludes zero. Leave-
one-out re-estimation across all 40 sessions produces no
sign reversal, and the five sessions with the highest Cook’s
distance (JenniferC, ArlenaJ, JohnP, CARIASOS, Eliza -
bethZ, each exceeding the conventional 4/N threshold)
leave the coefficient’s sign and approximate magnitude
intact when removed individually, indicating that no sin -
gle session drives the result. Re-estimating Model 2 as a
fractional logit with robust standard errors, appropriate
given the bounded, sparse nature of these proportions,
preserves both the sign and significance of STRESS.
Adding gender as a covariate (20 female, 20 male) leaves
the STRESS coefficient materially unchanged, with no
significant STRESS × gender interaction; adding session
duration as a covariate likewise leaves it unchanged.
H2a is supported, and unlike the original correlational
pattern alone, this conclusion withstands the collinearity,
sampling, and specification checks that the shared mea-
surement structure of these tags makes necessary.
Regulatory activity: H3 and H4
H3 predicts that REGULATION_ACTIVE is positively
associated with ATTENTION_HIGH; the estimated coef -
ficient is negative and non-significant (β = −1.289, p >
0.05). H3 is not supported.  H4 predicts that REGU -
LATION_ACTIVE moderates the STRESS–ATTEN -
TION_HIGH association; the interaction term is positive
but non-significant (β = 75.414, p = 0.209), and the main
effect of STRESS approaches but does not reach signifi -
cance in this specification (β = −1.378, p = 0.051). H4 is
not supported.
Both null findings should be interpreted considering
REGULATION_ACTIVE’s low prevalence (M = 0.009,
SD = 0.019; present in only 13 of 40 sessions at the seg -
ment level), which limits statistical power regardless
of the true underlying effect. The conservative, conver -
gence-based classification criterion further reduces the
number of observable regulatory episodes. These results
do not imply that regulatory processes are irrelevant to
engagement dynamics; they may instead operate at a finer
temporal grain than session-level aggregates can capture
or require classification criteria more sensitive than those
used here (Table 12).
Table 10 Regression models predicting ATTENTION_HIGH (N = 40)
Predictor Model 1 b
(SE)
Model 2 b (SE) Model
2 stan-
dard-
ized β
Constant 0.270***
(0.041)
0.276*** (0.044) –
STRESS −0.645
(0.392)
−1.472**
(0.547)
−0.128
FIXATION – 9.672* (4.684) 0.097
REGULATION_ACTIVE – −1.289 (1.787) −0.024
R2 0.066 0.169 –
*p < 0.05, **p < 0.01, **p < 0.001. Robustness diagnostics reported
in text above
Table 11 Robustness diagnostics for the H2a model (Standardized
STRESS Coefficient)
Diagnostic Result Threshold / benchmark
Variance inflation factor
(STRESS)
02.07 Concern at > 5; serious
at > 10
Condition index (design
matrix)
2.47 (max) Concern at > 30
Bootstrap 95% CI (5,000
resamples)
[− 0.259,
− 0.033]
Excludes zero
Leave-one-out coefficient
range
−0.158 to
− 0.092
No sign reversal across
40 refits
Highest Cook’s distance JenniferC,
D = 0.232
Threshold (4/N) = 0.100;
5 sessions exceed it,
none reverses the result
Fractional logit (robust
SE) re-estimation
b = − 0.839, p
= 0.009
Sign and significance
preserved
Gender-controlled model b = − 0.119, p
= 0.019
STRESS × gender inter-
action ns (p = 0.452)
Duration-controlled model b = − 0.129, p
= 0.011
Coefficient materially
unchanged
Table 12  Moderation analysis predicting ATTENTION_HIGH
(N = 40)
Predictor β SE t p
Constant 0.304 0.050 06.08 < 0.001
STRESS −1.378 0.683 −2.02 0.051
REGULATION_ACTIVE −1.789 1.987 −0.90 0.374
STRESS ×
REGULATION_ACTIVE
75.414 58.953 1.28 0.209
Model R 2 = 0. 1 1 1 . Note. Unstandardized OLS coefficients; interac-
tion term tests whether regulatory activity attenuates the STRESS–
ATTENTION_HIGH association

C. De Sainte Maresville et al.
Results concerning H2b: stress-related activation and
intentional engagement
At the session level, STRESS is the strongest predictor
of INTENTION_POS. In the baseline model, STRESS is
positively and significantly associated with INTENTION_
POS (β = 0.191, p < 0.001, R2 = 0.352), and the association
remains significant when FIXATION, ATTENTION_HIGH,
and REGULATION_ACTIVE are added (β = 0.173, p =
0.016; Table 13). None of the additional indicators reach
significance in the full model. STRESS does not signifi -
cantly predict INTENTION_NEG (β = −0.399, p = 0.264),
suggesting the association is specific to approach-oriented
engagement.
Taken at face value, this pattern would suggest that
the same activation-related configuration is associated
with lower attentional stabilization and higher intentional
engagement, consistent with a dual-process account. How -
ever, H2a and H2b differ in an important respect identified
during review: STRESS and INTENTION_POS share more
of their underlying feature basis than STRESS and ATTEN-
TION_HIGH do. A logistic model predicting each tag from
the eleven raw segment-level features (valence, arousal,
gaze, audio, video, text) produces feature-coefficient sig -
natures whose cosine similarity is 0.55 for STRESS and
INTENTION_POS, compared with 0.57 for STRESS and
ATTENTION_HIGH, a similar magnitude that does not by
itself distinguish the two relationships and motivates the
more direct test below.
To assess whether the STRESS–INTENTION_POS asso-
ciation survives outside this shared feature basis, STRESS
was reconstructed five times from progressively restricted,
non-overlapping modality subsets (all fused features, as in
the original tags; gaze only; voice only; text only; video/face
only), and each reconstructed version was correlated with
session-level INTENTION_POS and ATTENTION_HIGH
(Table 14). The STRESS–INTENTION_POS correlation
collapses in every subset ( r = 0.015 to 0.179, all non-sig -
nificant), compared with r = 0.593 for the original, fully
fused tag. The STRESS–ATTENTION_HIGH correlation
is more resilient, remaining negative in four of five subsets
and significant in two (gaze: r = − 0.419, p = 0.007; video/
face: r = − 0.430, p = 0.006), compared with r = − 0.257 for
the original tag.
This asymmetry indicates that the positive STRESS–
INTENTION_POS association reported above is substan -
tially attenuated, and in most reconstructions statistically
indistinguishable from zero, once the shared gaze and
video features linking the two tags are removed. The
negative STRESS–ATTENTION_HIGH association is
comparatively more robust to this manipulation, consis -
tent with the broader robustness pattern reported for H2a
in Sect.  “ Results Concerning H2a: Stress and Attentional
Stabilization”. H2b is therefore only partially supported:
a positive association between stress-related activation
and intentional engagement is observed using the tags as
originally constructed, but this association does not clearly
survive when the two tags are built from non-overlapping
behavioral evidence, and should accordingly be treated as a
measurement-dependent finding rather than an established
Table 13 Regression models predicting INTENTION_POS (N = 40)
Predictor Model 1 β (SE) Model 2 β (SE)
Constant 0.009 (0.004) 0.008 (0.007)
STRESS 0.191*** (0.042) 0.173* (0.069)
FIXATION – 0.229 (0.568)
ATTENTION_HIGH – 0.002 (0.019)
REGULATION_ACTIVE – −0.005 (0.206)
R2 0.352 0.356
*p < 0.05, **p < 0.01, **p < 0.001
Table 14 STRESS reconstructed from disjoint feature subsets: correla-
tion with INTENTION_POS and ATTENTION_HIGH
STRESS
feature
subset
r
(INTENTION_POS)
p r (ATTENTION_
HIGH)
p
All
fused
features
(original
tag)
0.593 < 0.001 −0.257 0.095
Gaze
only
0.140 0.391 −0.419 0.007
V oice
only
0.179 0.270 0.030 0.852
Text
only
0.061 0.709 −0.092 0.574
Video/
face
only
0.015 0.925 −0.430 0.006
STRESS reconstructed via logistic regression on the indicated fea -
ture subset only, then aggregated to session-level mean probability;
correlated with the original session-level ATTENTION_HIGH and
INTENTION_POS proportions
Table 15 Segment-level temporal tests: STRESS at segment t predict-
ing outcomes at t, t + 1, and t + 2
Outcome Contempo-
raneous (t)
t + 1 t + 2
ATTENTION_HIGH b = − 0.842,
p = 0.024
b = − 0.318,
p = 0.392
one-sided
perm. p = 0.119
INTENTION_POS b = + 1.368,
p < 0.001
b = + 0.542,
p = 0.169
one-sided
perm. p =
0.942
Segment durations average 5.5 s (median 4.4s); t + 1 corresponds to
roughly 4–5 s later, t + 2 to roughly 10 s later. Contemporaneous and
t + 1 estimates from participant-clustered logistic regression with
sandwich standard errors; t + 2 entries report one-sided permuta -
tion p-values (5000 within-participant shuffles) for the hypothesized
direction

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
behavioral pattern, pending the external validation dis -
cussed in Sect.  5.4.
Temporal ordering: does STRESS precede changes in
ATTENTION_HIGH or INTENTION_POS?
The associations above are contemporaneous and ses -
sion-level, leaving open whether stress-related activation
precedes, follows, or merely co-occurs with changes in
attentional stabilization or intentional engagement, as the
theoretical framework’s dynamic-process framing implies
it should. This was tested directly using the segment-level
sequence within each session (4391 segments, 40 sessions).
Participant-clustered logistic regressions confirm the con -
temporaneous pattern at the segment level: STRESS at
segment t is associated with lower ATTENTION_HIGH
(b = − 0.842, p = 0.024) and higher INTENTION_POS
(b = + 1.368, p < 0.001) at the same segment t, matching the
session-level results above.
The pattern does not extend to the following segment.
STRESS at segment t does not significantly predict ATTEN-
TION_HIGH at segment t + 1 (b = − 0.318, p = 0.392) or
t + 2, nor INTENTION_POS at t + 1 (b = 0.542, p = 0.169)
or t + 2, whether or not the model controls for the autocorre-
lated level of the outcome at t. Permutation tests that shuffle
each participant’s STRESS sequence while preserving their
marginal rate and the outcome sequence confirm these null
results in the hypothesized direction (one-sided p = 0.997
for ATTENTION_HIGH at t + 1; p = 0.884 for INTEN -
TION_POS at t + 1; Table 15).
This result does not contradict the theoretical account
that stress-related activation and engagement co-evolve; it
indicates that the present data, at a temporal resolution of
several seconds, cannot establish the sequencing implied
by that account. The associations documented in this paper
should accordingly be read as contemporaneous, not as
evidence that STRESS precedes the changes in ATTEN -
TION_HIGH or INTENTION_POS with which it co-
occurs. Finer-grained or longer-window temporal models
(e.g., change-point detection, hidden Markov models) may
be better suited to this question but require larger samples
than the present one to estimate reliably.
Results concerning H5: incremental validity of multimodal
engagement indicators
Nested models predicting INTENTION_POS show that
ATTENTION_HIGH alone explains little variance (R 2 =
0.014, non-significant), whereas adding STRESS increases
explanatory power substantially (R 2 = 0.353, ΔR2 = 0.339;
STRESS: β = 0.194, p < 0.001; Table 16). Within the pres -
ent framework, this demonstrates that STRESS captures
information about INTENTION_POS that ATTENTION_
HIGH does not. However, because both predictors are
derived from the same multimodal tagging pipeline rather
than from an outcome independent of it, and because Sect.
“Results Concerning H2b: Stress-Related Activation and
Intentional Engagement” shows that the STRESS–INTEN -
TION_POS relationship itself is sensitive to which features
construct STRESS, this incremental contribution should
be interpreted as internal to the measurement framework.
H5 is supported only in this internal sense ; establishing
incremental validity against an external engagement crite -
rion, such as self-reported engagement, task performance,
or a marketing outcome independent of the tagging system,
remains a necessary next step and is discussed in Sect.  5.4.
Discussion
This research advances a process-oriented perspective
on digital engagement by demonstrating how multimodal
behavioral data can be transformed into interpretable indica-
tors of engagement, while treating the validity of that infer-
ence as an empirical question subject to direct test rather
than as an assumption. Across two studies, engagement is
not adequately represented by a single behavioral dimen -
sion: it emerges as a configuration combining attention-
related, stress-related, and intentional indicators inferred
from gesture, gaze, vocal, affective, and linguistic signals.
Table 16  Nested regression models predicting INTENTION_POS
(N = 40)
Predictor Model 1 β (SE) Model 2 β (SE)
Constant 0.024 (0.007)*** 0.007 (0.007)
ATTENTION_HIGH −0.015 (0.021) 0.005 (0.018)
STRESS – 0.194*** (0.044)
R2 0.014 0.353
ΔR2 – 0.339
*p < 0.05, **p < 0.01, **p < 0.001
Table 17 Convergent validity: correspondence between human coding
and algorithmic tags (N = 144 segments)
Tag Mean
human
rating
(algo = 1)
Mean
human
rating
(algo = 0)
Point-
biserial
r
p Cohen’s
κ
STRESS 0.93 0.46 0.367 < 0.001 0.242
INTENTION_
POS
1.33 0.87 0.307 < 0.001 0.225
ATTENTION_
HIGH
1.46 1.55 − 0.069 0.411 −0.095
Human ratings are on a 0–2 scale; algo tags are binary. Point-biserial
r computed between the binary algorithmic tag and the continuous
human rating. Cohen’s κ computed using a conservative binarization
of human ratings (≥ 2 = present). Coding was blind: the coder had no
access to algorithmic tag values at the time of rating

C. De Sainte Maresville et al.
The central finding, summarized in Fig. 2, concerns the
differentiated but asymmetric role of stress-related activa -
tion. Stress-related behavioral configurations are robustly
and negatively associated with attentional stabilization, an
association that survives collinearity diagnostics, bootstrap
resampling, leave-one-out estimation, alternative model
specifications, gender and duration controls, and partial
reconstruction from feature subsets disjoint from those used
to build ATTENTION_HIGH. The same configurations are
positively associated with intentional engagement and with
fixation behavior when the tags are used as originally con -
structed, but these associations are substantially weaker, and
in most tested reconstructions statistically indistinguish -
able from zero, once shared gaze and video features are
removed. Neither the robust nor the fragile association is
detectable once the segment-level data are examined with
a true temporal lag, indicating that all of these findings are
best described as contemporaneous rather than sequential.
Together, these results support a multidimensional view of
engagement, in which attentional stabilization and inten -
tional engagement need not move together, but they caution
against treating every observed association within such a
framework as equally robust: distinguishing genuine behav-
ioral co-variation from measurement-construction artifacts
is not a peripheral methodological step but a precondition
for interpreting any single result.
The incremental validity analyses show that a multimodal
indicator (STRESS) explains substantial additional variance
in INTENTION_POS beyond an attention-based indicator
alone, within the present tagging framework. Because both
indicators originate from the same pipeline, and because the
STRESS–INTENTION_POS relationship itself proved sen-
sitive to feature construction, this result demonstrates inter-
nal incremental contribution rather than validity against an
external engagement criterion; the distinction matters for
how the finding should be used going forward.
The analyses provide only limited support for the role
of regulatory activity: neither the direct nor the moder -
ating effects of REGULATION_ACTIVE reached sig -
nificance, plausibly reflecting its low prevalence (43
segments across 13 of 40 sessions) rather than its theo -
retical irrelevance. Regulatory mechanisms may operate
over shorter temporal windows than the session-level
aggregates used here can resolve.
An explicit distinction between observable behav -
ioral configurations and latent psychological states runs
throughout this research: the proposed framework does
not claim to directly measure attention, stress, intention,
or regulation, and the robustness analyses reported here
exist precisely because that distinction has empirical
consequences. Engagement tags should be interpreted
as probabilistic behavioral representations, evaluated
against the alternative explanation of measurement over -
lap whenever they are used as evidence, rather than as
psychological diagnoses to be taken at face value.
Theoretical implications
This research contributes to digital marketing analytics
by reconceptualizing engagement as a dynamic process
and, more specifically, by showing that this reconceptu -
alization requires testing temporal sequencing directly
rather than inferring it from session-level aggregates;
the segment-level analysis in Sect.  “Temporal Ordering:
Does STRESS Precede Changes in ATTENTION_HIGH
or INTENTION_POS? ” illustrates both the value and the
current limits of this approach with the present sample
size.
Fig. 2 Summary of stress-related
activation’s associations with
engagement outcomes, by robust-
ness level

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
Second, it contributes a transparent intermediate layer
linking behavioral data to theoretical constructs, together
with a replicable diagnostic procedure, namely feature-
overlap analysis, collinearity and influence diagnostics, and
temporal testing, for distinguishing genuine associations
among such indicators from artifacts of shared measure -
ment construction. This procedure is applicable beyond the
present framework to other multimodal behavioral infer -
ence systems facing the same construct-validity concern.
Third, the findings extend embodied cognition per -
spectives in marketing (Barsalou 2008; Krishna 2011;
Elder and Krishna 2012) by treating bodily and behav -
ioral traces as inputs to behavioral inference about
ongoing engagement, while showing that this infer -
ence is more secure for some constructs than others: the
STRESS–ATTENTION_HIGH association generalizes
better across feature reconstructions than the STRESS–
INTENTION_POS association does.
Fourth, regarding theories of cognitive activation, the
results offer qualified support for a dual-process account
in which activation disrupts attentional continuity while
potentially mobilizing goal-directed engagement. The
disruption side of this account is comparatively well
supported by the present data; the mobilization side is
observed but not yet established as independent of mea -
surement construction, a distinction that should inform
how the dual-process account is cited going forward.
Managerial implications
The proposed framework offers a complementary analyt -
ical layer to outcome metrics such as clicks, dwell time,
and conversions, providing visibility into how engage -
ment evolves during interaction, particularly in conversa -
tional commerce, virtual customer service, and other rich
interpersonal digital contexts. The distinction between
attentional stabilization and intentional engagement sug -
gests that users may remain involved even as attentional
continuity decreases, cautioning against attention-only
engagement monitoring. Given the present findings,
managers should treat the attentional-stabilization signal
as the more dependable of the two: it withstood every
robustness check applied here, while the positive link to
intentional engagement should be treated as provisional
pending external validation, not yet as a basis for opera -
tional decisions such as triggering interventions when
activation rises. More broadly, these indicators should
function as decision-support inputs that complement,
rather than replace, established performance metrics and
managerial judgment.
Limitations and avenues for future research
Several limitations qualify these contributions. The sessions
were collected in a relatively controlled, interview-based
context; generalization to field settings such as e-commerce
or social media requires direct testing. The engagement
indicators remain behavioral inferences rather than fully
validated psychological measures. A partial convergent
validity check through blind human coding of transcript
segments (Sect.  “Convergent Validity: Human Coding of
a Stratified Segment Sample”) found significant but modest
correspondence for STRESS (r = 0.367) and INTENTION_
POS (r = 0.307), providing initial evidence that these tags
capture behaviorally recognizable signals; no such evidence
was obtainable for ATTENTION_HIGH through text-based
coding given its non-verbal construction, and no self-report,
physiological, or independent marketing-outcome criterion
was available against which to benchmark any of the three
tags. This remains the most consequential limitation of the
present work, directly underlying the qualified interpreta -
tion of H2b and H5 above. Establishing such external vali -
dation, for instance against self-reported engagement, task
performance, or purchase-relevant outcomes, is the neces -
sary next step before these indicators can be used as mea -
sures of engagement in applied settings.
Study 1 and Study 2 draw on substantially overlapping
samples (33 to 38 of 40 participants in common); they are
best read as sequential phases of measurement develop -
ment and explanatory testing on largely the same data, not
as independent replications, and the reported associations
await replication on an independent sample. REGULA -
TION_ACTIVE’s low prevalence limited the power avail -
able to test H3 and H4; larger and more diverse samples
would also support demographic and contextual modera -
tors left unexamined here. Finally, the temporal analysis in
Sect.  “Temporal Ordering: Does STRESS Precede Changes
in ATTENTION_HIGH or INTENTION_POS? ”, while a
direct response to the concern that session-level aggrega -
tion obscures sequencing, is itself constrained by the avail -
able segment granularity (several seconds) and sample size;
longer-window or change-point models, applied to larger
datasets, may yet detect sequencing that the present analysis
could not.
Conclusion
This research developed and tested a multimodal behavioral
inference framework for capturing digital engagement as
a process rather than a static outcome, integrating gesture,
gaze, vocal, affective, and linguistic signals into theoreti -
cally grounded, transparently documented indicators. The

C. De Sainte Maresville et al.
central finding is asymmetric rather than uniformly sup -
portive of the initial dual-process hypothesis: stress-related
activation is robustly associated with lower attentional sta -
bilization across an extensive battery of robustness checks,
while its association with intentional engagement, though
present in the original specification, is substantially weaker
once shared measurement construction is accounted for,
and neither association holds once a genuine temporal lag
is introduced.
Beyond these substantive results, the central contribution
of this research is methodological: a transparent procedure
for linking behavioral signals to engagement constructs,
paired with an explicit diagnostic strategy, namely feature-
overlap testing, collinearity and influence diagnostics, and
segment-level temporal analysis, for evaluating whether
such indicators reflect genuine behavioral dynamics or arti-
facts of how they were built. This distinction is offered as
a template applicable beyond the present framework. The
findings suggest that advancing digital marketing analyt -
ics toward process-oriented measurement requires not only
richer behavioral data, but also the routine application of
this kind of scrutiny, and ultimately, external validation
against independent engagement criteria, before behav -
iorally inferred indicators can be treated as measures of
engagement rather than as descriptions of behavior.
Appendix
Appendix A. Multimodal tag construction:
literature benchmarks, behavioral rules, and
classification examples
The objective of this appendix is to provide detailed opera -
tionalization information for each of the six multimodal
engagement tags reported in the main analyses, including
literature-informed benchmarks, specific behavioral deci -
sion criteria, and illustrative classification examples. This
information supplements the condensed overview in Table 7
of the main text.
General classification principles
All tags follow three principles applied consistently
across the dataset. First, multimodal convergence: no tag is
assigned based on a single behavioral signal; classification
requires convergent evidence from at least two indepen -
dent modalities within the same temporal segment. Second,
theory-driven interpretation: candidate indicators and deci -
sion thresholds were identified from prior literature prior to
data analysis, not derived inductively from the present data.
Third, conservative assignment: segments where signals are
weak, contradictory, or insufficient for reliable classification
remain untagged rather than being forced into a category,
which accounts for the low prevalence of several tags.
ATTENTION_HIGH. Sustained attentional allocation
Modalities: gaze, posture, gesture
Literature benchmarks : Sustained attentional fixations
in human-computer interaction research typically exceed
200–300 ms, with longer fixation durations associated with
deeper processing (Just & Carpenter, 1976; Rayner, 1978).
Wedel and Pieters ( 2008) demonstrate that gaze entropy
decreases under focused cognitive engagement. Stable pos-
tural and motor activity co-occurs with sustained task ori -
entation in embodied cognition research (Barsalou 2008).
Classification criteria : A segment is tagged ATTEN -
TION_HIGH when the following indicators converge: (a)
fixation duration and dwell allocation within or above the
literature-informed attentive range; (b) gaze entropy below
the session median, indicating stable rather than wandering
visual attention; (c) limited scanpath transitions, reflecting
focus on a primary target; (d) stable postural and motor
activity, with low movement variability. At least three of
these four indicators must be present simultaneously.
Illustrative example: A participant maintains steady eye
contact with the interaction target throughout the segment;
minimal head movement is detected, and gaze entropy is
low. Speech continues at a stable rate without hesitation.
This configuration is tagged ATTENTION_HIGH.
STRESS. Cognitive strain and activation under task
demands
Modalities: voice, face, gaze, text.
Literature benchmarks: Healey and Picard ( 2005) iden-
tify elevated arousal, increased vocal intensity, and blink-
rate variability as robust physiological correlates of stress.
D'Mello and Graesser (2012) document negative affect,
hesitation, and self-correction in speech as linguistic mark -
ers of cognitive load. Yap et al. (2021) link gaze instabil -
ity and increased scanpath entropy to information overload
conditions.
Classification criteria : A segment is tagged STRESS
when at least two of the following four modalities simul -
taneously indicate elevated activation and cognitive strain:
(a) voice: elevated arousal estimate and/or increased vocal
intensity relative to the session baseline; (b) face: negative
valence, facial tension, or elevated blink-rate variability; (c)
gaze: increased gaze entropy or instability relative to session
baseline; (d) text: stress-related linguistic markers including
hedging, self-correction, or negative affect language. The
multimodal convergence requirement means that a stress -
ful topic alone (text only) or a tense facial expression alone
(face only) is insufficient for tag assignment.
Illustrative example: A participant's vocal intensity rises
while their speech includes hesitations and self-corrections
("I mean... no, actually..."). Facial analysis simultaneously

Measuring digital engagement dynamics through multimodal behavioral inference: a marketing analytics…
indicates elevated arousal and a negative valence peak. Two
modalities converge; the segment is tagged STRESS.
FIXATION. Concentrated attentional capture
Modalities: gaze, affective signals.
Literature benchmarks: Lang et al. (1997) demonstrate
that emotionally salient stimuli produce longer fixations
and stronger attentional capture. Pieters and Wedel ( 2008)
show that fixation duration increases for stimuli with high
motivational relevance. Smidts et al. (2014) link sustained
gaze concentration to heightened engagement with a focal
stimulus.
Classification criteria: A segment is tagged FIXATION
when prolonged visual concentration on a target is accom -
panied by elevated affective activation. Specifically: (a)
fixation duration substantially exceeds the session median;
(b) gaze is concentrated on a primary region with minimal
switching; (c) affective indicators from facial or vocal chan-
nels are simultaneously elevated. FIXATION differs from
ATTENTION_HIGH in requiring affective co-activation,
not just attentional stability.
Illustrative example : A participant’s gaze dwells on a
specific screen region for an extended period while facial
affect indicates positive valence and elevated arousal. The
co-occurrence of sustained gaze and affective activation
triggers the FIXATION tag.
INTENTION_POS. Approach-oriented engagement
Modalities: text, voice, face, gaze.
Literature benchmarks: Petty and Cacioppo ( 1984) link
approach motivation with positive affect, elaborative pro -
cessing, and goal-directed language. Krishna ( 2011) docu-
ments approach-oriented behavioral correlates in consumer
interaction contexts. Rios et al. (2023) identify positive sen-
timent and target-oriented attention as indicators of motiva-
tional engagement.
Classification criteria : A segment is tagged INTEN -
TION_POS when at least two modalities converge toward
approach orientation, including at least one semantic or
affective indicator: (a) text: positive sentiment score or
approach-oriented language (expressions of interest, desire,
commitment); (b) voice: positive vocal tone and/or rising
prosodic contour; (c) face: positive valence, approach-
compatible affect; (d) gaze: target-oriented attention co-
occurring with the above. The requirement for at least one
semantic/affective indicator prevents purely gaze-based or
vocal-only classification.
Illustrative example: A participant says “I really want to
try that, it sounds great” with positive vocal intonation and
a sustained positive facial expression. Text and face con -
verge; the segment is tagged INTENTION_POS.
INTENTION_NEG. Avoidance-oriented engagement
Modalities: text, voice, face, gaze.
Literature benchmarks : Elliot ( 2006) defines avoid -
ance motivation as behavioral and cognitive orientation
away from an aversive stimulus, associated with negative
affect, withdrawal, and reduced approach behavior. Krishna
(2011) documents gaze avoidance and negative affective
expressions as correlates of avoidance-oriented consumer
behavior.
Classification criteria : A segment is tagged INTEN -
TION_NEG when multiple modalities simultaneously indi-
cate avoidance tendencies: (a) text: negative sentiment or
avoidance-oriented language (expressions of reluctance,
rejection, or withdrawal); (b) voice: negative vocal tone, flat
or declining prosodic contour; (c) face: negative valence,
avoidance-compatible affect; (d) gaze: reduced target atten-
tion or active gaze avoidance. Convergence across at least
two modalities is required.Illustrative example: A partici -
pant says “I don't really see the point, it just seems com -
plicated” in a flat tone while facial affect indicates negative
valence. Text and face converge; the segment is tagged
INTENTION_NEG.
REGULATION_ACTIVE. Behavioral self-regulation
and recovery
Modalities: voice, text, gaze, face.
Literature benchmarks : Baumeister et al. ( 1998) con -
ceptualize self-regulation as the deliberate adjustment of
behavior to restore goal-directed processing following dis -
ruption. Gross (1998) and Gross and John (2003) document
emotional regulation as a process involving cognitive reap-
praisal and behavioral stabilization.Classification criteria: A
segment is tagged REGULATION_ACTIVE when multi -
modal signals indicate behavioral reorganization or recov -
ery following a prior activation episode: (a) a reduction
in arousal relative to the immediately preceding segment;
(b) restoration of gaze stability; (c) verbal expressions of
self-monitoring or self-correction; (d) emotional stabiliza -
tion in facial affect. The temporal context (occurring after
activation) is part of the classification criterion, not just the
instantaneous signal configuration. This conservative crite -
rion explains REGULATION_ACTIVE's low prevalence in
the dataset.
Illustrative example : Following a high-arousal seg -
ment, a participant pauses and says “actually, let me recon-
sider that.” Arousal estimates drop, gaze restabilizes, and
a verbal self-correction is detected. The segment is tagged
REGULATION_ACTIVE.
Acknowledgements The authors thank colleagues for informal discus-
sions that contributed to the development of this research. The authors
also acknowledge Odaptos for providing access to the video-mediated
interaction data used in this study.
Funding Open access funding provided by Université de Bretagne
Sud. This research was supported by a CIFRE doctoral fellowship
funded by the ANRT (Association Nationale de la Recherche et de la
Technologie) in partnership with Odaptos. No specific grant number is
associated with this funding.

C. De Sainte Maresville et al.
Declarations
Conflict of interest  The authors declare no competing interests. Two
authors are affiliated with Odaptos, which provided access to the data
used in this research; however, this affiliation did not influence the
study design, analysis, or interpretation of the results.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
References
Barsalou, L.W. 2008. Grounded cognition. Annual Review of Psychol-
ogy 59: 617–645.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 1 4 6 / a n n u r e v . p s y c h . 5 9 . 1 0 3 0
0 6 . 0 9 3 6 3 9     .
Baumeister, R.F., E. Bratslavsky, M. Muraven, and D. M. Tice. 1998.
Ego depletion: Is the active self a limited resource? Journal of
Personality and Social Psychology 74(5):1252–1265.  h t t  p s : /  / d o  i .
o  r g / 1 0 . 1 0 3 7 / 0 0 2 2 - 3 5 1 4 . 7 4 . 5 . 1 2 5 2     .
Burgoon, J. K., Guerrero, L. K., & Floyd, K. 2016. Nonverbal Com -
munication. Routledge https:/ /doi.or g/10.43 24/97 81315663425
Chang, Y ., and E. Thorson. 2023. Media multitasking, counterargu -
ing, and brand attitude: Testing the mediation effects of advertis-
ing attention and cognitive load. Computers in Human Behavior
139:107544. https:/ /doi.or g/10.10 16/j. chb.2022.107544.
Davenport, T., A. Guha, D. Grewal, and T. Bressgott. 2020. How arti-
ficial intelligence will change the future of marketing. Journal of
the Academy of Marketing Science 48(1):24–42.  h t t  p s : /  / d o  i . o  r g / 1
0 . 1 0 0 7 / s 1 1 7 4 7 - 0 1 9 - 0 0 6 9 6 - 0     .
Elder, R.S., and A. Krishna. 2012. The “visual depiction effect” in
advertising: Facilitating embodied mental simulation through
product orientation. Journal of Consumer Research  38(6):988–
1003. https:/ /doi.or g/10.10 86/66 1531.
Elliot, A.J. 2006. The Hierarchical Model of Approach-Avoidance
Motivation. Motivation and Emotion 30:111–116.  h t t  p s : /  / d o  i . o  r g /
1 0 . 1 0 0 7 / s 1 1 0 3 1 - 0 0 6 - 9 0 2 8 - 7
Gross, J. J. 1998. The Emerging Field of Emotion Regulation : An
Integrative Review. Review of General Psychology 2(3):271-299
https:/ /doi.or g/10.10 37/10 89-2680.2.3.271
Healey, J. A., & Picard, R. W. 2005. Detecting Stress During Real-
World Driving Tasks Using Physiological Sensors. IEEE Trans-
actions on Intelligent Transportation Systems  6(2):156-166
https:/ /doi.or g/10.11 09/TI TS.2005.848368
He, L., T. Freudenreich, W. Yu, M. Pelowski, and T. Liu. 2021. Meth-
odological structure for future consumer neuroscience research.
Psychology & Marketing 38(8):1161–1181.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
0 2 / m a r . 2 1 4 7 8     .
Krishna, A. 2011. An Integrative Review of Sensory Marketing:
Engaging the Senses to Affect Perception, Judgment and Behav -
ior (SSRN Scholarly Paper 2552068). Social Science Research
Network. https:/ /papers .ssrn.c om/ab stract=2552068
Lang, P. J., Bradley, M. M., & Cuthbert, B. N. 1997. Motivated atten-
tion: Affect, activation, and action. In P. J. Lang, R. F. Simons, &
M. T. Balaban (Eds.), Attention and orienting: Sensory and moti-
vational processes (pp. 97–135). Lawrence Erlbaum Associates.
Mehrabian, A., and M. Williams. 1969. Nonverbal concomitants of
perceived and intended persuasiveness. Journal of Personality
and Social Psychology  13(1):37–58.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 3 7 / h 0
0 2 7 9 9 3     .
Pizzi, G., S. Matta, F. Caboni, and D.W. Stewart. 2025. Immersive and
generative technology: New tools for marketing, new tools for
consumer response. Psychology & Marketing 42(12):3236–3250.
https:/ /doi.or g/10.10 02/ma r.70036.
Petty, R. E., & Cacioppo, J. T. 1984. The effects of involvement on
responses to argument quantity and quality: Central and periph -
eral routes to persuasion. Journal of Personality and Social Psy -
chology 46(1):69–81 https:/ /doi.or g/10.10 37/00 22-3514.46.1.69
Rayner, K. 1978. Eye movements in reading and information process-
ing. Psychological Bulletin 85(3):618–660.  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
3 7 / 0 0 3 3 - 2 9 0 9 . 8 5 . 3 . 6 1 8
Smidts, A., M. Hsu, A.G. Sanfey, M.A.S. Boksem, R.B. Ebstein, S.A.
Huettel, J.W. Kable, U.R. Karmarkar, S. Kitayama, B. Knutson, I.
Liberzon, T. Lohrenz, M. Stallen, and C. Yoon. 2014. Advancing
consumer neuroscience. Marketing Letters 25(3):257–267. https:/
/doi.or g/10.10 07/s1 1002-014-9306-1.
Wedel, M., and P.K. Kannan. 2016. Marketing analytics for data-rich
environments. Journal of Marketing 80(6):97–121.
Wedel, M., & Pieters, R. 2008. A review of eye-tracking research in
marketing. In N. K. Malhotra (Ed.), Rev
Yap, S.-F., Y . Xu, and L. Tan. 2021. Coping with crisis: The paradox
of technology and consumer vulnerability. International Journal
of Consumer Studies 45(6):1239–1257.  h t t p s : / / d o i . o r   g / 1 0 . 1 1 1 1 / i j
c s . 1 2 7 2 4     .
Zhu, Z., H. Sun, and C. Guo. 2026. Fix-Me or Grow-Me? Implicit
mindsets shape educational product preferences. Psychology &
Marketing https:   //d oi. or g/10 .10  02/mar.70097
Publisher’s note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
Charlotte De Sainte Maresville  is a doctoral researcher at the IAE,
Université Bretagne Sud (UBS). Through a CIFRE partnership with
Odaptos, her research explores how facial expressions influence per -
ception, engagement, and behaviour in digital environments.Chris -
tine Petr is Professor of Marketing at the IAE, Université Bretagne
Sud (UBS), and a researcher at the LEGO Laboratory. Her research
focuses on consumer behaviour, digital transformation, tourism, and
human–machine interaction. Olfa Haggui received her PhD in Com -
puter Vision and Machine Learning in 2020. She is a researcher at
Odaptos, where she develops computer vision and machine learning
solutions. Her research interests include machine learning, deep learn-
ing, and image processing. Felipe Restrepo is co-founder of Odaptos
with Maximilien Joannides. Both develops AI-driven methodologies
to improve usability testing and digital user experiences.
