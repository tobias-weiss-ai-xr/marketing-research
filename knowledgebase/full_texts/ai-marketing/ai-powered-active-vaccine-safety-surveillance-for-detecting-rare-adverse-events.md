---
title: 'AI-Powered Active Vaccine Safety Surveillance for Detecting Rare Adverse Events of Special Interest
  (AESI) Following Pandemic Vaccinations: A Scoping Review'
url: https://doi.org/10.21203/rs.3.rs-10428840/v1
category: ai-marketing
subcategory: case-study
date: 2026-08
venue: Research Square
authors:
- Lukman Ade Chandra
- Dhite Bayu Nugroho
- Jarir At Thobari
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10428840/latest.pdf
pages: 18
chars: 51823
fetched_at: '2026-11-08T18:37:28+00:00'
kb_version: 1
---

# AI-Powered Active Vaccine Safety Surveillance for Detecting Rare Adverse Events of Special Interest (AESI) Following Pandemic Vaccinations: A Scoping Review

AI-Powered Active Vaccine Safety Surveillance for
Detecting Rare Adverse Events of Special Interest (AESI)
Following Pandemic Vaccinations: A Scoping Review
Lukman Ade Chandra 
The University of Melbourne
Dhite Bayu Nugroho 
Universitas Gadjah Mada
Jarir At Thobari 
Universitas Gadjah Mada
Gerardo Luis Dimaguila 
Murdoch Children's Research Institute
Jim Buttery 
The University of Melbourne
Article
Keywords: artiﬁcial intelligence, AESI, active surveillance, vaccine, pandemic
Posted Date: August 6th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10428840/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.   Read Full
License
Additional Declarations: No competing interests reported.
Page 1/18

Abstract
Introduction: Pandemic vaccination requires rapid and systematic post-marketing safety monitoring, particularly to
detect rare, complex adverse events of special interest (AESI) that are often not identiﬁed during early clinical trials.
Artiﬁcial intelligence has the potential to strengthen active vaccine safety surveillance by enabling the large-scale
use of both structured and unstructured data.
Objective: This scoping review aims to map the evidence on the use of AI in active surveillance for AESI following
pandemic vaccination, particularly COVID-19 and inﬂuenza vaccines.
Methods: This scoping review was conducted in accordance with the PRISMA-ScR guidelines. Literature searches
were performed in PubMed, Ovid-Embase, Web of Science, Scopus, Google Scholar, and through hand searching up
to 30 April 2026. Eligible studies were primary studies that applied AI methods, including machine learning, deep
learning, natural language processing, or hybrid models, in active vaccine safety surveillance to detect AESI or
health outcomes of interest following pandemic vaccination. Data were narratively extracted according to study
characteristics, data sources, AI methods, AI roles, safety outcomes, implications, and limitations.
Results: Of 20,098 records identiﬁed, 20 studies met the inclusion criteria. Most studies were published in 2021–
2022, with 13 studies (65.0%), and the majority focused on COVID-19 vaccines, with 17 studies (85.0%). The most
frequently investigated outcomes were multiple or broad AESI and maternal outcomes. The most common data
source was electronic health records, including clinical notes and imaging reports, used in 9 studies (45.0%),
followed by social media or online platforms in 6 studies (30.0%), as well as claims databases, online surveys, and
physiological monitoring data. AI was used for case detection, extraction of adverse events from free text, risk
prediction, signal screening, social listening, and early signal exploration. Its role remained predominantly supportive
for signal detection and prioritisation.
Conclusion: This review demonstrates that AI enhances active vaccine safety surveillance through dual case
detection and strategic support. By leveraging diverse health data, AI accelerates candidate identiﬁcation, clinical
information extraction, and early signal prioritisation of AESI. These ﬁndings strengthen global post-marketing
surveillance frameworks, guiding future research towards optimal and reliable AI implementation.
INTRODUCTION
During a pandemic, vaccination represents a critical public health strategy to attenuate disease burden, preserve
healthcare system capacity, and support disease control. However, emergency conditions necessitate accelerated
vaccine development and rapid deployment. Regulatory decisions, including emergency use authorisations, are
inherently reliant on limited short-term eﬃcacy and safety proﬁles available at the time of licensure.1 Under these
circumstances, adverse events of special interest (AESIs) are of paramount concern. Due to their low incidence,
stringent diagnostic criteria, and the requirement for large observation cohorts, AESIs are exceptionally challenging
to detect during pre-licensure clinical trials.2
Post-marketing experience during recent health emergencies has demonstrated that several rare AESIs become
discernible only after vaccines are widely deployed across real-world populations. Notable examples include
myocarditis and pericarditis following mRNA vaccines, Guillain-Barré syndrome and thrombosis with
thrombocytopenia syndrome linked to adenoviral vector platforms, and narcolepsy among monitored AESI
categories in pandemic vaccine safety work.3,4 These historical precedents highlight that rare safety signals
Page 2/18

demand continuous, systematic post-marketing surveillance to ensure population safety and maintain public trust.
To address these needs, active vaccine safety surveillance is essential. Unlike passive reporting systems, which
suffer from inherent under-reporting and reporting bias, active surveillance proactively gathers population-level data
across diverse digital sources, including electronic health records, administrative claims databases, disease
registries, and sentinel hospital networks.5 Active systems can support near real-time signal detection, reﬁnement,
validation, and investigation, but they require epidemiologic methods, infrastructure, and expert review capacity.6 In
resource-constrained settings, particularly low- and middle-income countries, fragmented data systems and limited
surveillance capacity remain major barriers to rapid and sustainable monitoring. 5
Advances in artiﬁcial intelligence (AI) offer transformative potential to strengthen active safety surveillance by
accelerating signal detection, veriﬁcation, and validation across large-scale datasets. This application facilitates
automated candidate case identiﬁcation, accelerate early signal detection, and standardise informal descriptions
into clinical terminology, although current methods still need stronger validation.7 Furthermore, AI methodologies
are increasingly directed towards complex, clinically critical outcomes indicative of AESIs, including myocarditis,
pericarditis, anaphylaxis, and other serious adverse events captured in real-world data.4,8 Predictive algorithms,
transformer-based models, and generative AI are being evaluated for adverse-event extraction, symptom
normalisation, and support for signal management or causality-oriented review workﬂows.8 Despite these
promising developments, AI deployment speciﬁcally tailored for AESI surveillance remains nascent, and the
evidence base is still fragmented across techniques, data sources, and outcomes. Given this fragmentation,
comprehensively mapping the current evidence on AI applications in active vaccine safety surveillance is justiﬁed.
Therefore, this scoping review aims to synthesise and map evidence on the utility of AI in active surveillance for
AESIs following pandemic vaccination, speciﬁcally targeting diseases such as COVID-19 and pandemic inﬂuenza.
RESULTS
A total of 20 studies were included from 20,098 records identiﬁed through bibliographic databases and other
sources, including hand searching (Fig. 1). Most studies were published during the early phase of the COVID-19
pandemic, particularly in 2021 (30.0%) and 2022 (35.0%). This pattern was consistent with the vaccine focus of the
included studies, as the majority investigated AESI following COVID-19 vaccination (85.0%). In terms of study
setting, the evidence was largely concentrated in high-income countries, particularly the United States (45.0%) and
South Korea (15.0%), although four studies (20.0%) conducted surveillance at a global or multinational scale.
Regarding health outcomes of interest, more than half of the studies examined multiple or broadly deﬁned vaccine
adverse events (55.0%), rather than focusing on a single or speciﬁc AESI. Pregnancy and reproductive outcomes
accounted for 20.0% of studies, thrombotic events for 15.0%, while cardiovascular or vascular side effects and
allergic or haematological reactions each accounted for 5.0%. The general characteristics of the included studies
are summarised in Table 1.
Page 3/18

Table 1
Characteristics of included studies (n = 20)
Characteristics N Studies (%)
Years of publication  
2021 6 (30.0)
2022 7 (35.0)
2023 4 (20.0)
2024 1 (5.0)
2025 2 (10.0)
Country setting  
United States 9 (45.0)
Global/multinational coverage 4 (20.0)
South Korea 3 (15.0)
Jordan 1 (5.0)
United Kingdom 1 (5.0)
Taiwan 1 (5.0)
Netherlands 1 (5.0)
Data Source  
Electronic health records, including clinical notes and imaging reports 9 (45.0)
Social media/online platforms 6 (30.0)
Administrative/claims databases 2 (10.0)
Online surveys 2 (10.0)
Physiological/clinical monitoring data 1 (5.0)
Vaccine of interest  
COVID-19 vaccines 17 (85.0)
Inﬂuenza vaccines 2 (10.0)
COVID-19 and inﬂuenza vaccines 1 (5.0)
AESI investigated  
Multiple/unspeciﬁed AESI 11 (55.0)
Pregnancy and reproductive outcomes 4 (20.0)
Thrombotic events, including DVT, CVST, and VTE 3 (15.0)
Cardiovascular or vascular side effects 1 (5.0)
Allergic/hematologic reactions 1 (5.0)
Page 4/18

Data sources in AI-based surveillance
A diverse range of data sources was utilised in AI-based vaccine safety surveillance. Electronic health records
(EHRs)—comprising clinical notes and imaging reports—represented the most prevalent data source, accounting for
nine studies (45.0%). These EHRs encompassed unstructured clinical data, such as physicians’ notes, radiology
reports, ultrasound ﬁndings, and imaging documentation, which served to identify clinical outcomes requiring
medical conﬁrmation. Speciﬁcally, venous duplex ultrasound reports were applied to identify acute deep vein
thrombosis, whilst diagnostic imaging studies were used to detect venous thromboembolism.9,10 Furthermore,
structured ICD and vaccination data were combined with free-text notes to ascertain cerebral venous sinus
thrombosis, and clinical notes were leveraged to detect spontaneous abortion, an outcome not consistently
captured by diagnostic codes alone.11,12 Additionally, EHR clinical notes were deployed to extract rare or serious
adverse events, such as anaphylaxis, myocarditis, and pericarditis.13–15
In addition to EHRs, 6 studies (30.0%) used social media or online platforms as data sources, primarily to capture
post-vaccination complaints, public sentiment, and self-reported suspected adverse events. Twitter and Facebook
were analysed to identify vaccine safety-related mentions and sentiment trends.16 Twitter content was processed to
extract suspected adverse events, and Korean-language Twitter posts were examined for brand-speciﬁc vaccine
surveillance.17,18 Furthermore, social media and online support group content spanning multiple countries and
languages was evaluated, whilst Twitter and online media were leveraged alongside VAERS as a reference
comparator rather than a primary data source.19,20 Table 2 presents a detailed description of the AI methodologies
used for active surveillance and AESI detection in each included study.
Page 5/18

Table 2
AI methodologies for active surveillance of AESI (n = 20)
Author/year Data source AI role/function AI methods Implication and
challenges of AI
Chen et al.,
2022
Physiological
signals: radial
BP waveform,
PPG, clinical
tests, ECG,
chest X-ray,
side-effect
assessment
Detection of
cardiovascular/vascular
side effects
Supervised ML: pulse
harmonic indices,
LDA, SVM, MLP, Naïve
Bayes, DT, RF, LR,
KNN; pulse-variability
score
May detect subtle
vascular/cardiovascular
changes, but limited by
small sample, few
cases, BNT162b2
focus, and need for
larger validation.
Choi et al.,
2025
NHIS
claims/outcome
data linked with
KDCA
vaccination
history
Risk prediction Ensemble ML: GBM + 
logistic regression;
train/test split; 5-fold
CV
Supports AUB risk
stratiﬁcation, but
limited by no external
validation, class
imbalance, surveillance
bias, and
generalisability issues.
Daluwatte
et al., 2022
Social media
and online
support groups
from 190
countries, 61
languages
AE mention detection Keyword ﬁltering,
machine translation,
PubMedBERT-NER,
MedDRA mapping
Enables multilingual
real-time AE monitoring,
but mentions are
unvalidated, noisy, and
non-representative.
Gaddh et
al., 2023
EHRs and
diagnostic
imaging studies
Automated VTE case
detection
Validated NLP
algorithms on
imaging
documentation
Enables large-scale VTE
ascertainment from
imaging reports, but
depends on report
quality, with possible
NLP misclassiﬁcation
and limited
transparency.
Hatmal et
al., 2021
Online survey
via Facebook,
Instagram,
WhatsApp
Side-effect severity
prediction
MLP, XGBoost, RF, K-
star; 5-fold CV
Predicts self-reported
symptom severity, but
limited by self-
reporting, social media
sampling bias, and lack
of clinical veriﬁcation.
Hatmal et
al., 2022
Online survey
via social media
across 22 Arab
countries
Side-effect prediction GB, RF, XGBoost, MLP,
KNN, SVM, AdaBoost,
PNN; feature-
importance analysis
Enables regional
proﬁling of post-
vaccination symptoms,
but constrained by
online sampling bias,
self-reporting, and no
clinical conﬁrmation.
Houghton
et al., 2021
Mayo Clinic
EMR and
venous duplex
ultrasound
reports
Case
detection/outcome
ascertainment
Validated NLP for
acute DVT in
ultrasound reports
Automates rare
thrombotic event
extraction from imaging
reports, but may involve
NLP misclassiﬁcation
and requires manual
validation.
Hussain et
al., 2022
Twitter and
Facebook posts
Case detection,
sentiment analysis,
early signal generation
Keyword/thematic
ﬁltering; hybrid
sentiment model
Enables near-real-time
pharmacovigilance, but
limited by non-
representative users,
Page 6/18

Author/year Data source AI role/function AI methods Implication and
challenges of AI
using VADER,
TextBlob, BERT
misinformation, and
lack of clinical ground
truth.
Kim et al.,
2021
NHIS claims
linked with
KDCA elderly
inﬂuenza
vaccination
records
Active safety
monitoring and signal
screening
RF classiﬁer, feature-
importance ratio,
bootstrapping, LIME
Supports scalable,
explainable surveillance
using linked claims
data, but has modest
discrimination and
uncertain sensitivity.
Klein et al.,
2022
Public Twitter
posts from
users
announcing
pregnancy
Automated cohort
identiﬁcation
Rule-based
NLP/regex;
pregnancy timeline
inference; outcome-
tweet detection
Shows feasibility of
real-time pregnancy
safety cohorts from
social media, but
limited by small
sample, self-reporting,
and no causal
inference.
Matson et
al., 2023
Mayo Clinic
multistate
hospital EHR
notes and
vaccination
records
AE extraction and
signal screening
NLP curation of
clinician-reported AEs
from unstructured
EHR notes
Enables scalable
paediatric vaccine
safety surveillance
beyond structured
codes, but limited by
single-system data and
AE undercapture.
McMurry et
al., 2021
Mayo Clinic
hospital EHR
clinical notes
Automated AE
extraction
Deep neural network
NLP; augmented
curation of clinician
free-text notes
Supports near-real-time
surveillance from
clinical notes, but
limited by routine-note
underreporting and
single-system data.
Niesen et
al., 2021
Mayo Clinic EHR
clinical notes
and vaccination
records
AE extraction and post-
dose safety
quantiﬁcation
BERT-based
augmented curation;
high-conﬁdence AE
labels; manual review
for rare severe AEs
Scales booster-dose
safety monitoring with
manual adjudication,
but limited by selection
bias and restricted
phenotype coverage.
Park et al.,
2023
Korean-
language
Twitter posts
Brand-speciﬁc
surveillance and
sentiment monitoring
Korean text
preprocessing,
LDA/hierarchical LDA,
TF-IDF, topic
modelling,
SentiStrength
Supports brand-speciﬁc
AE discourse
monitoring, but limited
by no medical
conﬁrmation,
representativeness
issues, and context
loss.
Pawlowski
et al., 2021
Mayo Clinic
EHRs with
ICD/vaccination
data and free-
text notes
CVST case
ascertainment
NLP for positive
CVST diagnoses plus
ICD-code search
Reduces missed CVST
cases using hybrid NLP
and structured data, but
limited by small event
counts and possible
misclassiﬁcation.
Piekos et
al., 2023
Multicentre
EHRs with
imported state
immunisation
records
Predictive proﬁling of
vaccination/booster
status
Supervised ML
classiﬁcation;
outcomes from
structured EHR ﬁelds
Identiﬁes vaccination
uptake determinants
and supports
pregnancy safety
analyses, but limited by
Page 7/18

Author/year Data source AI role/function AI methods Implication and
challenges of AI
single-system data and
no external validation.
Portelli et
al., 2022
English-
language
Twitter data via
Twitter API
Social media
surveillance, suspected
AE extraction,
sentiment monitoring
RoBERTa sentiment
model; SpanBERT + 
CRF AE extraction;
geolocation/factuality
analysis
Monitors vaccine
opinions and suspected
AEs, but limited by non-
representative data,
unveriﬁed AEs, and
possible model
confusion.
van der
Weg et al.,
2025
EHRs from
LUMC/Haga
plus Lareb
spontaneous
reports
Targeted case
identiﬁcation and signal
detection augmentation
CTcue NLP/text
mining;
structured/free-text
EHR search; manual
veriﬁcation/expert
review
Enhances signal
detection through
proactive EHR case
ﬁnding, but requires
manual veriﬁcation and
is limited by incomplete
data and hospital
scope.
Xie et al.,
2022
EMRs,
especially free-
text clinical
notes, plus
diagnosis codes
and chart-
reviewed cases
Spontaneous abortion
case detection
NLP algorithm for
extracting
spontaneous abortion
from clinical notes
Improves pregnancy-
related AESI detection
beyond diagnosis
codes, but limited by
lower speciﬁcity, no
causal assessment,
and adaptation needs.
Yun et al.,
2024
Twitter/online
media; VAERS
as reference
comparator
Social media side-
effect signal
exploration and gap
comparison
Text/graph mining:
keyword extraction,
co-occurrence, TF-IDF,
Word2Vec, cosine
similarity, PageRank,
Louvain clustering,
ICD-10 grouping
Reveals known and
emerging side-effect
concerns, but limited by
unveriﬁed claims,
misinformation, and
inability to establish
causality.
Roles of AI methods in active surveillance
AI roles varied across the included studies and could be grouped according to their primary surveillance function,
ranging from case detection, clinical case identiﬁcation, outcome ascertainment, and adverse event (AE) extraction
to functions not primarily focused on direct AE detection, such as risk prediction, signal screening, cohort
identiﬁcation, and social signal exploration. Studies that used AI to support AE detection were mainly based on
EHRs, clinical notes, and imaging reports. Within this group, natural language processing (NLP) was the most
frequently used method to extract clinical outcomes from unstructured data. Validated NLP algorithms were used to
detect acute deep vein thrombosis from ultrasound reports and venous thromboembolism from diagnostic imaging
studies.9,10A hybrid approach combining structured data and free-text notes was used to ascertain cerebral venous
sinus thrombosis cases (Pawlowski et al., 2021), while NLP applied to clinical notes was used to detect
spontaneous abortion events that may not always be captured by diagnosis codes.11,12 Other studies used deep
neural network NLP, BERT-based augmented curation, and NLP curation to extract rare or serious adverse events
from EHR notes, including anaphylaxis, myocarditis, pericarditis, and cerebral venous sinus thrombosis.13–15 In
addition, CTcue NLP/text mining was used for targeted case identiﬁcation and signal detection augmentation
through structured and free-text EHR searches, followed by manual veriﬁcation.21
Page 8/18

AI functions not primarily centred on direct AE detection included risk prediction, signal screening, cohort
identiﬁcation, and social media-based signal exploration. In risk prediction studies, supervised machine learning
was used to predict or proﬁle speciﬁc outcomes, such as abnormal uterine bleeding using ensemble ML based on
GBM and logistic regression, anaphylaxis and agranulocytosis using random forest, feature-importance ratio,
bootstrapping, and LIME, and cardiovascular or vascular side effects using supervised ML based on physiological
signals, including LDA, SVM, MLP, Naïve Bayes, decision tree, random forest, logistic regression, and KNN.22–24
Online survey studies used several machine learning algorithms, including MLP, XGBoost, random forest, K-star,
gradient boosting, SVM, KNN, AdaBoost, and PNN, to predict post-vaccination side effects or symptom severity.25,26
In pregnancy-related contexts, supervised ML was used for predictive proﬁling of vaccination or booster status,
while rule-based NLP and regular expressions were used for automated cohort identiﬁcation from Twitter users who
announced pregnancy.27,28 In social media-based studies, AI was used for social listening, sentiment monitoring,
adverse-event mention detection, and signal exploration through keyword ﬁltering, VADER, TextBlob, BERT,
PubMedBERT-NER, MedDRA mapping, RoBERTa, SpanBERT-CRF, topic modelling, TF-IDF, Word2Vec, PageRank,
Louvain clustering, and graph mining.16–20
Implications and considerations of AI for surveillance
Based on Table 2, the implications of AI use across the mapped studies can be summarised into several categories.
In studies based on EHRs, clinical notes, and imaging reports, AI was primarily used to support case extraction,
case ascertainment, and the identiﬁcation of adverse events from unstructured clinical data. This approach was
applied to outcomes such as acute deep vein thrombosis, venous thromboembolism, cerebral venous sinus
thrombosis, spontaneous abortion, anaphylaxis, myocarditis, and pericarditis.9–15 Another study used structured
and free-text EHR searches for targeted case identiﬁcation and signal detection augmentation, followed by manual
veriﬁcation.21 In machine learning-based studies, AI was used for risk prediction, proﬁling, or screening of speciﬁc
outcomes and populations, including abnormal uterine bleeding, anaphylaxis, agranulocytosis, cardiovascular or
vascular side effects, and the severity of post-vaccination symptoms based on online surveys.22–26 Meanwhile,
studies based on social media and online platforms used AI to monitor adverse-event mentions, sentiment, public
discourse, pregnancy cohort identiﬁcation, and signal or side-effect issue exploration from online data.16–20,28
The challenges and limitations of AI use also varied according to data source and analytical purpose. In studies
based on EHRs and imaging reports, the main challenges included potential NLP misclassiﬁcation, dependence on
the quality of clinical documentation or imaging reports, data coverage limited to speciﬁc health systems, and the
need for manual veriﬁcation in selected cases.9,10,13–15,21 In machine learning-based prediction and screening
studies, reported limitations included small sample size or limited outcome events, class imbalance, moderate
discriminatory performance, lack of external validation, and limited generalisability.22–24,27 In studies based on
social media and online surveys, commonly reported challenges included representation bias, self-reporting bias,
lack of clinical conﬁrmation, potential misinformation or duplicate reporting, and limited ability to distinguish
complaints, public perceptions, and safety signals requiring further evaluation.16–20,25,26,28
DISCUSSION
General ﬁndings
Page 9/18

This scoping review demonstrates that the application of AI to enhance active vaccine safety surveillance has
expanded, particularly in the context of pandemic vaccination. The majority of mapped studies were published
between the early phase and the post-implementation phase of COVID-19 vaccination (2021–2022). The heightened
demand for proactive safety surveillance during the COVID-19 period stemmed from accelerated vaccine
development and the critical necessity for post-authorisation safety monitoring.29,30 Although vaccine safety was
evaluated during early- to late-stage clinical trials, the Global Advisory Committee on Vaccine Safety (GACVS)
emphasised the imperative for robust pharmacovigilance once vaccines were deployed population-wide.31,32 This is
essential because pre-licensure clinical trials—characterised by limited durations and relatively small sample sizes—
are frequently inadequate for detecting rare adverse events, including AESIs, which typically emerge only following
widespread implementation.30,32 In this context, safety surveillance systems, particularly active surveillance, rapidly
evolved during the COVID-19 pandemic by expanding and intensifying signal detection mechanisms.
Broadly, the application of AI in AESI surveillance falls into two principal functions. The primary function focuses
directly on case detection, encompassing clinical case identiﬁcation, medical outcome ascertainment, and adverse
event extraction from unstructured medical narratives. Conversely, the second function addresses strategic non-
detection supporting roles, such as risk prediction, signal screening, cohort identiﬁcation, proﬁle mapping, and
social listening. This division aligns with the trajectory of modern pharmacovigilance automation, wherein AI is
employed both for individual-level AESI case validation and population-level safety signal detection and screening.33
These functions facilitate the continuous processing of structured and unstructured data from diverse sources,
thereby enabling AI to mitigate several limitations inherent in passive reporting systems, including under-reporting,
constrained incidence estimation, and limited temporal and contextual characterisation of events.7,34 Moving
forward, the utility of AI for cross-source data harmonisation and causality assessment support should be
expanded to foster the development of increasingly integrated and adaptive vaccine safety surveillance systems for
pandemic preparedness.
AI for AESI case detection and outcome ascertainment from
clinical data
In active vaccine safety surveillance, real-world clinical data—particularly EHRs—constitute an essential resource for
detecting and validating AESI cases, as these data capture clinical events during routine care and provide detailed
contextual information. The necessity for rich clinical data sources is particularly pronounced in AESI contexts,
given that post-vaccination active surveillance aims not only to identify rare events but also to evaluate outcome
validity and temporal relationships between vaccination and clinical onset through detection, veriﬁcation, and
validation approaches that frequently vary across studies and healthcare systems.35 However, surveillance
approaches reliant solely on administrative diagnostic codes exhibit critical limitations; structured codes are
susceptible to reduced precision and under-coding, whereas many clinical safety signals are documented primarily
within free-text narratives.36,37
Consequently, NLP and text mining offer substantial utility in extracting clinical information from free text—including
clinical notes, discharge summaries, radiology reports, and follow-up telephone records—enabling complex event
phenotypes to be identiﬁed with higher sensitivity than through administrative data alone. Literature indicates that
applying NLP/machine learning to EHRs not only extracts adverse events from clinical narratives but also enhances
the detection of under-reported events and uncovers signals undetectable from structured data alone.38,39
Methodological advancements have progressed from rule-based systems to ML, deep learning, and transformer-
based models, with evidence demonstrating that ClinicalBERT-based models exhibit superior cross-corpus
Page 10/18

generalisability for drug–adverse drug event relation extraction compared with classical methods.36,38 Nevertheless,
event detection from clinical text remains non-trivial, as models must discern not only drug and event entities but
also their interrelationships, including complex causal contexts and temporal sequences.
AI for AESI risk prediction, screening, and prioritisation
Beyond case detection, the mapped studies indicate that AI is also utilised for risk prediction, screening, and
prioritisation of AESIs or related outcomes, primarily employing supervised machine learning and ensemble models
to identify event proﬁles, severity levels, or high-priority monitoring cohorts. This pattern aligns with broader
developments in pharmacovigilance, where AI is leveraged for signal detection, risk stratiﬁcation, and the
automated processing of safety data from heterogeneous health data sources.33,34,39 Within AESI surveillance, the
role of machine learning models is not to establish a clinical diagnosis, but rather to prioritise signals, outcomes, or
subpopulations for further review. This approach offers the potential to predict AESIs or post-vaccination reactions
for speciﬁc vaccines based on evaluated predictors, enabling active monitoring to focus earlier on higher-risk
cohorts.40
Furthermore, AI has the capacity to expand monitoring from passive case identiﬁcation to early AESI anticipation, as
predictive models can integrate claims data, electronic health records, and clinical characteristics to detect risk
patterns that conventional methods fail to capture easily.34,41 This potential is supported by ﬁndings that ensemble
models, such as random forest and XGBoost, in multinational vaccine surveillance studies effectively predict
outcomes while identifying associated risk factors, thereby demonstrating AI's utility in accelerating initial screening
and follow-up prioritisation.25 This enhances signal management eﬃciency and ultimately supports a more
proactive, personalised surveillance model by identifying individuals who may require closer post-vaccination
observation.
However, because AESIs are generally rare, predictive modelling faces distinct challenges, including low event
counts, severe class imbalance, and the risk of performance degradation when deployed in novel populations.41,42
This is particularly relevant given that ML-based prediction model studies frequently under-report methodologies
and performance metrics, including external validation, calibration, fairness, and subgroup heterogeneity.42 For AESI
surveillance, AI is therefore best conceptualised as a tool for risk stratiﬁcation and prioritisation support rather than
a standalone basis for case determination or individual causal inference; implementation decisions still necessitate
thorough clinical and epidemiological validation.
AI for social listening and early exploration of AESI-related signals
The application of AI has rapidly expanded across social media platforms and online forums for social listening,
sentiment analysis, adverse-event mention detection, speciﬁc cohort identiﬁcation, and early signal exploration. A
range of computational methods—including NLP, machine learning, large language models (LLMs), Named Entity
Recognition (NER), concept normalisation to clinical ontologies such as MedDRA, topic modelling, and text/network
analytics—have been employed to isolate, classify, normalise, and characterise informal user-generated
narratives.43,44 Compared with sources such as spontaneous reporting systems or formal medical records, which
suffer from administrative lags before data become available for analysis, social media provides near-real-time
user-generated data capable of capturing patient experiences, perceptions, and symptom descriptions post-
Page 11/18

vaccination.19 This advantage enables systems to detect early systemic responses or rare adverse effects at an
early stage, prior to conventional pharmacovigilance signal validation.
In the context of AESIs, social media analysis is positioned as an exploratory instrument and early warning system
rather than a foundation for medical diagnosis conﬁrmation. Signal extraction from social media presents
substantial challenges due to patient language being highly informal, non-technical, idiomatic, and variable across
online communities; consequently, lexicon- or keyword-based approaches risk missing numerous adverse-event
mentions.43,45 Thus, AESI signals may be identiﬁed incidentally when the extracted vaccine safety mentions indicate
AESI trends at suﬃcient frequencies. These initial signals provide a crucial informational basis that can be rapidly
validated, ﬁltered for misinformation, or cross-referenced with scientiﬁc evidence published in global literature.46
This early signal mapping function is particularly vital for regions facing limitations in integrated clinical databases
or national vaccine safety data. Accordingly, while social media-based AI cannot replace oﬃcial pharmacovigilance
systems due to clinical validity and veriﬁcation constraints, it acts as an effective adjunct data source, bridging
information gaps and accelerating public health safety surveillance responses.
Methodological challenges and potential of AI for AESI vaccine
safety surveillance
The application of AI in detecting AESIs faces distinct methodological challenges stemming from the rare incidence
of events, adherence to stringent case deﬁnitions, and the requirement for temporal certainty post-vaccination (28).
In clinical data processing, NLP techniques are susceptible to misclassiﬁcation and validation constraints due to
EHR heterogeneity, incomplete corpora, and the absence of standardised validation methodologies and criteria.2,7 In
predictive modelling, low positive case counts induce severe class imbalance and calibration vulnerability;
simulations demonstrate that conventional class imbalance corrections can lead to risk overestimation and equal or
inferior calibration compared with uncorrected models.41,47 Meanwhile, on social media, primary constraints include
self-reporting bias, poor user representativeness, lack of clinical diagnostic conﬁrmation, high data noise, temporal
uncertainty, and health misinformation or content promoting vaccine scepticism.46,47
Despite these challenges, AI presents substantial opportunities as a clinical decision-support system to automate
active vaccine safety surveillance. AESIs can be detected through multiple active surveillance modalities, including
cohort event monitoring, sentinel surveillance, data linkage, and digital or participant-centred approaches such as
mHealth and eHealth.48 Within these frameworks, AI can contribute to initial stages by extracting candidate cases,
screening signals, supporting outcome prioritisation, and identifying populations requiring further evaluation. Future
implications highlight the necessity of strengthening AESI deﬁnition standardisation, cross-source data
interoperability, external validation, model transparency, and standardised clinical veriﬁcation mechanisms. Brighton
Collaboration/SPEAC case deﬁnitions can provide an important foundation for outcome standardisation because
they are designed to harmonise the collection and analysis of vaccine safety data across the vaccine life cycle and
different resource settings, while allowing case classiﬁcation according to levels of diagnostic certainty.49
Developing minimum data sets and metadata is crucial to ensure data consistency and comparability across
studies and healthcare systems. Furthermore, future research must expand to low- and middle-income countries to
address disparities in infrastructure capacity and resources. Consequently, the implementation of AI in active
vaccine safety surveillance should not focus solely on algorithmic sophistication, but must encompass data
readiness, outcome standardisation, model validation, and seamless integration into clinical and epidemiological
veriﬁcation workﬂows.
Page 12/18

CONCLUSION
This scoping review mapped evidence on AI methodologies used in active vaccine safety surveillance to detect and
monitor AESIs following pandemic vaccination. The ﬁndings indicate that AI has been deployed across two main
functions: case detection and supportive non-detection functions. The methodologies utilised encompass NLP, text
mining, supervised machine learning, ensemble models, explainable AI, sentiment analysis, topic modelling, and
graph-based analytics applied to diverse data sources, including EHRs, clinical notes, imaging reports, claims
databases, online surveys, physiological data, social media, and online platforms. The primary implication of this
review is that AI can expand vaccine safety surveillance capacity by enabling faster and broader utilization of
structured and unstructured data. In the context of rare and complex AESIs, AI can support candidate case
identiﬁcation, clinical information extraction, signal prioritisation, and the early exploration of emerging issues
across large populations. This evidence provides a foundation for strengthening active vaccine safety surveillance
systems, particularly in countries developing or enhancing their health data infrastructure and post-marketing
vaccine safety monitoring frameworks. Future research should evaluate which AI methods provide the most
applicable and reliable utility for AESI vaccine safety surveillance systems. Sharing methodological experiences and
lessons learned from AI routinely implemented within speciﬁc centres or national frameworks will be invaluable for
advancing future vaccine safety surveillance.
METHODS
Eligibility criteria
This scoping review was conducted in accordance with the Preferred Reporting Items for Systematic Reviews and
Meta-Analyses extension for Scoping Reviews (PRISMA-ScR). Eligible studies included primary research that
incorporated AI within an active vaccine safety surveillance system. In this review, AI was deﬁned as computer-
based systems and algorithms that simulate selected aspects of human cognitive functions. Studies were required
to explicitly describe the use of computational or algorithmic approaches, such as machine learning, deep learning,
rule-based natural language processing (NLP), or hybrid models, to support the detection, assessment, or
monitoring of vaccine safety outcomes using various data sources.The vaccines of interest in this review were
restricted to vaccines used in pandemic settings, as deﬁned by the World Health Organization (WHO). The selection
of vaccine types was determined by consensus among the authors. Based on this consensus, the vaccines of
interest were inﬂuenza and COVID-19 vaccines, as both have been widely used in pandemic contexts. Vaccine
safety surveillance methods were required to involve active surveillance, deﬁned as systematic and proactive
detection using structured data sources, such as electronic health records (EHRs), registries, and claims databases,
or unstructured data sources, such as social media and clinical notes. The target outcomes were AESI cases or
diagnoses according to the Safety Platform for Emergency Vaccines (SPEAC), including maternal and neonatal
outcomes related to vaccination during pregnancy, identiﬁed through diagnosis codes, clinical notes, mentions, or
MedDRA terms. AESI were deﬁned as pre-speciﬁed medical conditions with biological plausibility or historical
associations with vaccines or vaccine platforms, and which are prioritised for monitoring following mass
immunisation. Exclusion criteria included speciﬁc study designs, such as clinical trials, reviews, and case reports, as
well as studies in which the primary surveillance data source was a self-reporting passive surveillance database.
Search strategy, selecting studies, and data collection
Page 13/18

A comprehensive literature search was conducted across peer-reviewed and grey literature sources. Electronic
databases included PubMed, Embase, Web of Science, and Scopus. Grey literature was identiﬁed through Google
Scholar and targeted manual searching of reference lists from relevant reviews and key articles. The search strategy
combined terms related to: (1) pandemic-relevant vaccines, namely inﬂuenza and COVID-19 vaccines; (2) AESI
based on SPEAC; and (3) artiﬁcial intelligence. No language restrictions were applied, and the search period covered
all records from database inception to 30 April 2026. Study selection was conducted in two stages: title and
abstract screening, followed by full-text screening. Two reviewers (LAC and DBN) independently conducted both
stages. Disagreements were resolved through discussion, with involvement of a third reviewer when required.
Studies for which the full text was unavailable were excluded from the review. The study selection process, from
searching to ﬁnal inclusion, was presented using a PRISMA ﬂow diagram.
Data extraction was independently performed by two reviewers using a structured web-based electronic form. The
extraction form consisted of two main sections: general study characteristics and AI-related methodological details.
General study characteristics included author, year, setting, data source, vaccine of interest, and AESI detected. AI
methodological details included the name of the data source, AI roles or functions, AI methods, ﬁndings, study
results, implications, and notes on the use of AI. Data were synthesised narratively using tables and descriptive
summaries, with a focus on mapping AI methods for active surveillance of rare vaccine adverse events, particularly
potential data sources, the roles of AI, and the strengths and limitations of AI implementation.
Declarations
Data availability
Data will be provided on request to the corresponding author.
Acknowledgements
The authors extend their sincere thanks to research assistant (Ican Saﬁra and Ika Agustin) for the support with full-
text retrieval during data extraction, as well as the LPDP Scholarship for supporting the lead author’s academic
studies
Authors contribution
LAC, JB, and JA conceived and designed the study framework. LAC and DBN carried out the systematic literature
search, study screening, and data extraction. LAC and JB synthesised the data and authored the initial draft of the
manuscript. JB, GLD, and JA contributed to data interpretation, provided critical revisions for key intellectual
content, and supervised the manuscript preparation. All authors reviewed, reﬁned, and approved the ﬁnal
manuscript for submission.
Funding statement
No funding
Declaration of competing interest
The authors declare that they have no personal or ﬁnancial conﬂicts of interest that could have inﬂuenced the
preparation or publication of this manuscript.
Page 14/18

Supplementary data
Supplementary data to this article can be accessed online at…..
References
1. Excler, J.-L., Saville, M., Berkley, S. & Kim, J. H. Vaccine development for emerging infectious diseases. Nat.
Med. 27, 591–600 (2021).
2. Buttery, J. P. & Clothier, H. Information systems for vaccine safety surveillance. Hum. Vaccin. Immunother. 18,
2100173 (2022).
3. Pires, C. Serious Adverse Reactions to COVID-19 vaccines in Portugal up to July 2021: thrombosis with
thrombocytopenia syndrome, myocarditis/pericarditis, and Guillain-Barré syndrome. Biomedical and
biopharmaceutical research: jornal de investigação biomédica e biofarmacêutica 19, (2022).
4. Padilla-Flores, T., Sampieri, A. & Vaca, L. Incidence and management of the main serious adverse events
reported after COVID‐19 vaccination. Pharmacol. Res. Perspect. 12, e1224 (2024).
5. Chandra, L. A., Nugroho, D. B., Thobari, J. A., Dimaguila, G. L. & Buttery, J. Active surveillance methods to
identify adverse events of special interest (AESIs) following vaccination against pandemic diseases: A scoping
review. Vaccine 77, 128341 (2026).
6. Mues, K. E. et al. A review of methodologic & data considerations for vaccine safety surveillance in the wake of
the COVID-19 pandemic. Vaccine 64, 127691 (2025).
7. Golder, S. et al. Leveraging natural language processing and machine learning methods for adverse drug event
detection in electronic health/medical records: a scoping review. Drug Saf. 48, 321–337 (2025).
8. Dong, G. et al. Optimizing signal management in a vaccine adverse event reporting system: a proof-of-concept
with COVID-19 vaccines using signs, symptoms, and natural language processing. Drug Saf. 47, 173–182
(2024).
9. Houghton, D. E. et al. Deep vein thrombosis after COVID-19 vaccinations. Blood 138, 291 (2021).
10. Gaddh, M. et al. Comparison of Venous Thromboembolism Outcomes after COVID-19 and Inﬂuenza
Vaccinations. TH Open 7, e303–e308 (2023).
11. Pawlowski, C. et al. Cerebral Venous Sinus Thrombosis is not Signiﬁcantly Linked to COVID-19 Vaccines or Non-
COVID Vaccines in a Large Multi-State Health System. J Stroke Cerebrovasc Dis 30, 105923 (2021).
12. Xie, F. et al. Identifying Spontaneous Abortion from Clinical Notes within a Large Integrated Healthcare System.
SN COMPUT. SCI. 3, (2022).
13. Matson, R. P. et al. Paediatric safety assessment of BNT162b2 vaccination in a multistate hospital-based
electronic health record system in the USA: a retrospective analysis. Lancet Digit. Heal. 5, e206–e216 (2023).
14. McMurry, R. et al. Real-time analysis of a mass vaccination effort conﬁrms the safety of FDA-authorized mRNA
COVID-19 vaccines. Med 2, 965–978.e5 (2021).
15. Niesen, M. J. M. et al. Three doses of COVID-19 mRNA vaccination are safe based on adverse events reported
in electronic health records. medRxiv 2011–2021 (2021).
16. Hussain, Z. et al. Artiﬁcial Intelligence-Enabled Social Media Analysis for Pharmacovigilance of COVID-19
Vaccinations in the United Kingdom: Observational Study. JMIR Public Health Surveill 8, e32543- (2022).
17. Park, S. & Suh, Y. K. A Comprehensive Analysis of COVID-19 Vaccine Discourse by Vaccine Brand on Twitter in
Korea: Topic and Sentiment Analysis. J Med Internet Res 25, e42623- (2023).
Page 15/18

18. Portelli, B. et al. Monitoring User Opinions and Side Effects on COVID-19 Vaccines in the Twittersphere:
Infodemiology Study of Tweets. J. Med. Internet Res. 24, (2022).
19. Daluwatte, C. et al. Application of a language model tool for COVID-19 vaccine adverse event monitoring using
web and social media content: Algorithm development and validation study. JMIR infodemiology 4, e53424
(2024).
20. Yun, S., Jeong, J. & Kim, J. COVID-19 Vaccine Side Effect Analysis by Leveraging Social Media: Focusing on
Connectivity and Cluster Characteristics of Vaccine Side Effects. IEEE Trans. Computat. Soc. Syst. 11, 6487–
6500 (2024).
21. van der Weg, W. et al. Strengthening spontaneous reporting-based signal detection during a pandemic with
cases from electronic health records using a natural language processing tool. Vaccine 62, (2025).
22. Choi, Y. et al. Artiﬁcial intelligence models predicting abnormal uterine bleeding after COVID-19 vaccination. Sci
Rep 15, 7081 (2025).
23. Kim, Y. et al. Machine Learning Approach for Active Vaccine Safety Monitoring. J Korean Med Sci 36, e198-
(2021).
24. Chen, C. C. et al. Machine Learning Analyses Revealed Distinct Arterial Pulse Variability According to Side
Effects of Pﬁzer-BioNTech COVID-19 Vaccine (BNT162b2). J Clin Med 11, (2022).
25. Hatmal, M. M. et al. Reported adverse effects and attitudes among Arab populations following COVID-19
vaccination: a large-scale multinational study implementing machine learning tools in predicting post-
vaccination adverse effects based on predisposing factors. Vaccines (Basel). 10, 366 (2022).
26. Hatmal, M. M. et al. Side Effects and Perceptions Following COVID-19 Vaccination in Jordan: A Randomized,
Cross-Sectional Study Implementing Machine Learning for Predicting Severity of Side Effects. Vaccines (Basel)
9, (2021).
27. Piekos, S. N. et al. Effect of COVID-19 vaccination and booster on maternal-fetal outcomes: a retrospective
cohort study. Lancet Digit Health 5, e594–e606 (2023).
28. Klein, A. Z., O’Connor, K. & Gonzalez-Hernandez, G. Toward Using Twitter Data to Monitor COVID-19 Vaccine
Safety in Pregnancy: Proof-of-Concept Study of Cohort Identiﬁcation. JMIR Form Res 6, e33792- (2022).
29. Cole, A. et al. Safety surveillance and challenges in accelerated COVID-19 vaccine development. Ther. Adv. Drug
Saf. 13, 20420986221116452 (2022).
30. Piché-Renaud, P., Morris, S. K. & Top, K. A. A narrative review of vaccine pharmacovigilance during mass
vaccination campaigns: Focus on myocarditis and pericarditis after COVID‐19 mRNA vaccination. Br. J. Clin.
Pharmacol. 89, 967–981 (2023).
31. Zuber, P. L. F. et al. Evolving pharmacovigilance requirements with novel vaccines and vaccine components.
BMJ Glob. Health 6, e003403 (2021).
32. Hodel, K. V. S. et al. Pharmacovigilance in vaccines: Importance, main aspects, perspectives, and challenges—A
narrative review. Pharmaceuticals 17, 807 (2024).
33. Salas, M. et al. The use of artiﬁcial intelligence in pharmacovigilance: a systematic review of the literature.
Pharmaceut. Med. 36, 295–306 (2022).
34. Algarvio, R. C., Conceição, J., Rodrigues, P. P., Ribeiro, I. & Ferreira-da-Silva, R. Artiﬁcial intelligence in
pharmacovigilance: a narrative review and practical experience with an expert-deﬁned Bayesian network tool.
Int. J. Clin. Pharm. 47, 932–944 (2025).
35. Kochhar, S. & Salmon, D. A. Planning for COVID-19 vaccines safety surveillance. Vaccine 38, 6194–6198 (2020).
Page 16/18

36. Zitu, M. M. et al. Artiﬁcial intelligence for opioid safety surveillance from clinical text: a clinically focused review.
J. Clin. Med. 15, 1649 (2026).
37. Borjali, A. et al. Natural language processing with deep learning for medical adverse event detection from free-
text medical narratives: A case study of detecting total hip replacement dislocation. Comput. Biol. Med. 129,
104140 (2021).
38. Sharan, A. et al. Operational lessons learned in conducting an international study on pharmacovigilance in
pregnancy in resource-constrained settings: The WHO Global Vaccine Safety Multi-Country Collaboration
project. Vaccine X 11, 100160 (2022).
39. De Abreu Ferreira, R. et al. A pilot, predictive surveillance model in pharmacovigilance using machine learning
approaches. Adv. Ther. 41, 2435–2445 (2024).
40. Kolajo, T. & Daramola, O. J. Predicting COVID-19 Post-vaccination Mortality in Persons with Cardiovascular
Disease Risk Factors Using Explainable AI. in HC@ AIxIA 130–145 (2024).
41. Chalabianloo, N. et al. Machine learning methods for predicting adverse drug events: A systematic review. Br. J.
Clin. Pharmacol. 92, 422–444 (2026).
42. Karampatea, A., Kassandros, K., Constantinides, T. & Kontogiorgis, C. Systematic review of AI-based models in
pharmacoepidemiology for adverse drug event prediction and detection. Frontiers in Drug Safety and Regulation
6, 1773186 (2026).
43. Guellil, I. et al. Detecting adverse drug events in social media: A brief literature review. SN Comput. Sci. 7, 199
(2026).
44. Tricco, A. C. et al. Utility of social media and crowd-intelligence data for pharmacovigilance: a scoping review.
BMC Med. Inform. Decis. Mak. 18, 38 (2018).
45. Golder, S., O’Connor, K., Wang, Y. & Hernandez, G. G. The role of social media for identifying adverse drug events
data in pharmacovigilance: protocol for a scoping review. JMIR Res. Protoc. 12, e47068 (2023).
46. Lopes, L. P. N., Ramos-Silva, A., de Castro, A. G. & de Matos, G. C. Potential utility of social media in
pharmacovigilance to identify adverse events and safety signals: a scoping review. Research in Social and
Administrative Pharmacy (2026).
47. Li, Y. et al. Improving entity recognition using ensembles of deep learning and ﬁne-tuned large language models:
A case study on adverse event extraction from VAERS and social media. J. Biomed. Inform. 163, 104789 (2025).
48. ShamaeiZadeh, P. A., Jaimes, C. V., Knoll, M. D., Espié, E. & Chandler, R. E. Landscape review of active vaccine
safety surveillance activities for COVID-19 vaccines globally. Vaccine X 18, 100485 (2024).
49. Munoz, F. M. et al. Vaccine-associated enhanced disease: case deﬁnition and guidelines for data collection,
analysis, and presentation of immunization safety data. Vaccine 39, 3053–3066 (2021).
Figures
Page 17/18

Figure 1
PRISMA ﬂow diagram
Page 18/18
