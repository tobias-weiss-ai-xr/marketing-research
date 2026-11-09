---
title: 'Artificial intelligence in tobacco control: A systematic scoping review of applications, challenges,
  and ethical implications'
url: https://doi.org/10.1016/j.ijmedinf.2025.105987
category: privacy-data
subcategory: empirical
date: 2025-05
venue: International Journal of Medical Informatics
authors:
- David B. Olawade
- Charity Aienobe-Asekharen
source: openalex-oa
pdf_url: https://ray.yorksj.ac.uk/id/eprint/12127/1/1-s2.0-S1386505625002047-main.pdf
pages: 19
chars: 125751
fetched_at: '2026-11-08T16:56:12+00:00'
kb_version: 1
---

# Artificial intelligence in tobacco control: A systematic scoping review of applications, challenges, and ethical implications

RaY
Research at the University of York St John
For more information please contact RaY at
ray@yorksj.ac.uk
Olawade, David B. and Aienobe-Asekharen, Charity A (2025)
Artificial intelligence in tobacco control: A systematic scoping review
of applications, challenges, and ethical implications. International
journal of medical informatics, 202. p. 105987.
Downloaded from: https://ray.yorksj.ac.uk/id/eprint/12127/
The version presented here may differ from the published version or version of record. If
you intend to cite from the work you are advised to consult the publisher's version:
https://doi.org/10.1016/j.ijmedinf.2025.105987
Research at York St John (RaY) is an institutional repository. It supports the principles of
open access by making the research outputs of the University available in digital form.
Copyright of the items stored in RaY reside with the authors and/or other copyright
owners. Users may access full text items free of charge, and may download a copy for
private study or non-commercial research. For further reuse terms, see licence terms
governing individual outputs.  Institutional Repositories Policy Statement

Review article
Artificial intelligence in tobacco control: A systematic scoping review of
applications, challenges, and ethical implications
David B. Olawade a,b,c,d,*, Charity A. Aienobe-Asekharen e,f
a Department of Allied and Public Health, School of Health, Sport and Bioscience, University of East London, London, United Kingdom
b Department of Research and Innovation, Medway NHS Foundation Trust, Gillingham ME7 5NY, United Kingdom
c Department of Public Health, York St John University, London, United Kingdom
d School of Health and Care Management, Arden University, Arden House, Middlemarch Park, Coventry CV3 4FJ, United Kingdom
e Department of Health Sciences, Brunel University of London, Uxbridge, United Kingdom
f School of Sport, Exercise and Health Sciences, Loughborough University, United Kingdom
ARTICLE INFO
Keywords:
Artificial Intelligence
Tobacco Control
Smoking
Cessation
Public Health
Predictive Modelling, Machine Learning,
Language Models
ABSTRACT
Background: Tobacco use remains a significant global health challenge, contributing substantially to preventable
morbidity and mortality. Despite established interventions, outcomes vary due to scalability issues, resource
constraints, and limited reach.
Objective: To systematically explore current artificial intelligence (AI) applications within tobacco control,
highlighting their usefulness, benefits, limitations, and ethical implications.
Method: This scoping review followed the Arksey and O’Malley framework and PRISMA-ScR guidelines. Five
major databases (PubMed, Scopus, Web of Science, IEEE Xplore, and PsycINFO) were searched for articles
published between January 2010 and March 2025. From 1,172 initial records, 57 studies met inclusion criteria
after screening.
Results: AI-driven tools, including machine learning and natural language processing, effectively monitor social
media for emerging tobacco trends and personalize smoking cessation interventions. Applications were pre-
dominantly focused on predictive modelling (using algorithms like XGBoost and SVM to predict e-cigarette use
and relapse risk), cessation support (employing chatbots and reinforcement learning to improve accessibility),
and social media surveillance (detecting synthetic nicotine promotions and analysing vaping trends). Approxi-
mately 22% of studies aligned with WHO FCTC Article 13 (tobacco advertising regulation), while 45% supported
Article 14 (cessation services). However, tobacco industry interference remains a critical challenge, with AI
technologies exploited to undermine public health initiatives, target vulnerable populations, and manipulate
policy discussions. Critical issues including algorithmic bias, privacy concerns, interpretability challenges, and
data quality must be addressed to ensure positive impact.
Conclusion: AI holds considerable promise for extending tobacco control if implemented ethically, transparently,
and collaboratively. Future directions emphasize explainable AI development, integration of real-time inter-
vention systems, global data inclusion, and robust cross-sector collaboration. While the current landscape shows
a laudable start, it reflects the need for more diverse skill sets to fully harness AI’s extensive prospects for tobacco
control and achieving tobacco endgame goals.
1. Introduction
The World Health Organization Framework Convention for Tobacco
Control (WHO FCTC) describes tobacco control as “a range of supply,
demand, and harm reduction strategies that aim to improve the health of
a population by eliminating or reducing their consumption of tobacco
products and exposure to tobacco smoke” [1]. These strategies seek to
decrease tobacco use and mitigate its significant health risks through
policies, legislation, and educational initiatives [2]. Implementation is
facilitated primarily through the WHO FCTC and MPOWER strategies
(Monitor tobacco use, Protect people from smoke, Offer help to quit,
Warn about dangers, Enforce bans, and Raise taxes), which serve as vital
* Corresponding author at: Department of Allied and Public Health, School of Health, Sport and Bioscience, University of East London, London, United Kingdom.
E-mail address: d.olawade@uel.ac.uk (D.B. Olawade).
Contents lists available at ScienceDirect
International Journal of Medical Informatics
journal homepage: www.elsevier.com/locate/ijmedinf
https://doi.org/10.1016/j.ijmedinf.2025.105987
Received 28 April 2025; Received in revised form 15 May 2025; Accepted 19 May 2025
International Journal of Medical Informatics 202 (2025) 105987
Available online 20 May 2025
1386-5056/© 2025 The Author(s). Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ).

tools for tracking global progress and facilitating tobacco use reduction
[3–5].
Tobacco use causes 8 million annual deaths globally, with 7 million
attributable to direct use and 1.2 million to secondhand smoke [6].
Despite MPOWER strategies, progress remains uneven, particularly in
low- and middle-income countries (LMICs) [5,7]. As highlighted in the
2024 Lancet Global Health commentary on tobacco endgame goals, the
persistent challenges of inconsistent implementation across countries
and unequal policy maintenance continue to hinder global health sys-
tems [8,9]. Traditional tobacco control methods, although effective to
varying degrees, frequently encounter limitations related to scalability,
cost-efficiency, reach, and sustained effectiveness. For instance, phar-
macological treatments may present side effects or compliance issues,
behavioural therapies require intensive resources, and health campaigns
may fail to effectively engage high-risk populations.
In response to these persistent challenges, Artificial Intelligence (AI)
has emerged as an innovative and powerful tool with the potential to
revolutionize approaches to tobacco control. AI encompasses computa-
tional technologies capable of analysing large-scale datasets, learning
from complex patterns, making predictive decisions, and facilitating
personalized interventions [10]. Its capabilities extend across various
domains with specific applications to tobacco control: Machine learning
(ML) enables predictive modelling of relapse risk and tobacco initiation
patterns; Natural language processing (NLP) automates surveillance of
illicit tobacco promotions on social media and analyses public sentiment
toward tobacco policies; Deep learning (DL) identifies tobacco imagery
in digital content and classifies smoking behaviors from multimodal
data sources; and Reinforcement learning optimizes personalized
cessation interventions based on user engagement patterns.
There has been widespread application of AI across the tobacco
control spectrum. Numerous studies have utilized AI for analysing
hospital records to detect and categorize smoking history [11–18],
predict effects of smoking after cancer diagnosis [19–24], measure
smoke exposure metrics [25], predict cardiovascular disease risk
[26,27], detect tobacco-related cancers [28–30], and identify tobacco
plant diseases [31]. Within healthcare and social services, AI has sup-
ported tobacco control by predicting smoking relapse and tobacco
dependence [32–35], classifying social smoking behaviours [36],
detecting smoking environments to prevent cravings [37], character-
izing e-cigarette emissions [38], and assessing secondhand and third-
hand smoke exposure [39].
While several narrowly-focused reviews have examined AI applica-
tions in specific tobacco control domains such as smoking detection
[25,37] or cessation interventions [40,41], there exists a notable gap in
comprehensive assessments that systematically evaluate AI across the
full spectrum of tobacco control efforts. Previous studies have typically
addressed isolated applications without examining alignment with
global tobacco control frameworks or addressing ethical implications
and industry interference. This lack of synthesis limits our understand-
ing of how AI technologies can be strategically integrated within
comprehensive tobacco control programs and policy frameworks.
This review systematically synthesizes evidence on AI applications in
tobacco control, evaluates their alignment with WHO FCTC articles, and
identifies ethical risks and industry exploitation concerns. By compre-
hensively mapping the current landscape, we address the urgent need to
understand how emerging technologies can support tobacco endgame
strategies, particularly in resource-constrained settings where tradi-
tional approaches face significant implementation barriers. The review
covers AI-based surveillance and detection methods, predictive
modeling for risk assessment, personalized intervention techniques, and
evaluation methods of policy effectiveness. Furthermore, we examine
industry interference, highlighting how tobacco companies leverage AI
to circumvent public health measures and influence public opinion.
Ultimately, this paper contributes to ongoing discussions around best
practices, ethical considerations, and policy recommendations by
providing evidence-based insights on the transformative role AI can play
in enhancing tobacco control strategies. By identifying existing chal-
lenges, implementation gaps, and future research opportunities, we aim
to inform strategic integration of AI within global tobacco control efforts
and accelerate progress toward achieving the WHO’s tobacco reduction
targets.
2. Method
This scoping review was conducted to systematically map the
existing literature on the application of artificial intelligence (AI) in
tobacco control and identify key themes, research gaps, and opportu-
nities for future study. The review followed the methodological frame-
work proposed by [42] and further refined by [43] incorporating the
PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and
Meta-Analyses extension for Scoping Reviews) guidelines.
2.1. Search strategy
A comprehensive search was conducted across five major electronic
databases: PubMed, Scopus, Web of Science, IEEE Xplore, and Google
Scholar. The search strategy employed precise Boolean operators and
keywords: (“artificial intelligence” OR “machine learning” OR “deep
learning” OR “natural language processing” OR “predictive modelling”)
AND (“tobacco control” OR “smoking cessation” OR “vaping” OR “e-
cigarettes” OR “tobacco policy”) AND (“public health” OR “interven-
tion” OR “surveillance” OR “prevention”). Studies published between
January 2010 and March 2025 were included to capture the evolution of
AI applications in tobacco research. Language was restricted to English-
language publications.
2.2. Eligibility criteria
Studies were selected based on a structured framework addressing
Population, Intervention, Comparison, and Outcomes (PICO):
Population:  Tobacco and nicotine users (including cigarettes, e-
cigarettes, heated tobacco products)  General population targeted by
tobacco control measures  Industry actors and regulatory bodies
involved in tobacco control.
Intervention:  AI tools including but not limited to machine
learning algorithms, deep learning models, natural language processing
systems, and predictive analytics  AI-enabled platforms such as chat-
bots, mobile applications, and decision support systems for tobacco
control.
Comparison:  Traditional tobacco control interventions (when
available)  No intervention (in observational studies)  Different AI
approaches compared within the same study.
Outcomes:  Cessation rates and behavioural changes  Surveillance
accuracy and efficiency  Policy impact assessment  Public health
outcomes  FCTC alignment and implementation effectiveness.
For this review, “tobacco control” was operationalized as any sys-
tematic approach to reducing tobacco consumption, preventing initia-
tion, promoting cessation, protecting non-smokers, or regulating
tobacco products through policy, education, or direct intervention.
Inclusion criteria:
• Empirical research or systematic reviews focusing on AI applications
in tobacco control interventions, surveillance, policy evaluation, or
cessation support
• Use of AI methods such as machine learning, deep learning, natural
language processing, or predictive modelling
• Published in peer-reviewed journals, conference proceedings, or
technical reports in English
• Explicit relevance to tobacco/nicotine products or smoking
behaviours
Exclusion criteria:
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
2

• Opinion pieces, editorials, or news articles without empirical data
• Studies that did not describe an AI component or failed to focus on
tobacco-related issues
• Research focused exclusively on genomic or molecular-level AI ap-
plications without direct behavioural relevance
• Studies where tobacco was only mentioned peripherally and not
central to the research question
2.3. Study selection and data extraction
Initial search results were imported into EndNote X9 reference
management software, where duplicates were removed. Titles and ab-
stracts were independently screened for relevance, followed by full-text
review of potentially eligible articles. Discrepancies were resolved
through discussion with a third reviewer. A standardized data extraction
form was developed in Microsoft Excel and used to chart information
from each included study, capturing:
1 Study characteristics (author, year, country, study design) 2. Study
aim and research questions 3. AI method and algorithm specifications 4.
Data sources and sample size 5. Main findings and conclusions 6. Re-
ported limitations 7. AI application area (surveillance, cessation, etc.) 8.
Alignment with WHO FCTC article(s) 9. Ethical considerations
addressed 10. Industry involvement or conflict of interest.
An initial total of 1,172 records was identified through systematic
database searches. After eliminating 347 duplicate entries, 825 unique
studies were subjected to preliminary screening based on their titles and
abstracts. This screening step focused on identifying relevance to the
scope and objectives of the review. From this pool, 288 articles were
shortlisted for full-text assessment according to the predefined inclusion
and exclusion criteria. Upon detailed evaluation, 57 studies were
deemed eligible and included in the final synthesis.
The 231 studies excluded after full-text review were categorized by
reason for exclusion: no AI component (n = 83), insufficient focus on
tobacco control (n = 65), opinion/editorial without empirical data (n =
29), focus limited to genomic applications (n = 38), and unavailable full
text (n = 16). The entire selection process spanning identification,
screening, eligibility assessment, and final inclusion is illustrated in the
PRISMA flow diagram (Fig. 1), ensuring a clear and systematic overview
of the review methodology.
2.4. Data synthesis
Given the heterogeneity of study designs, methodologies, and AI
techniques, a narrative synthesis approach was employed. Findings were
organized thematically under surveillance and monitoring, cessation
support, risk prediction, policy evaluation, and industry interference.
We further categorized studies by their alignment with specific WHO
FCTC articles (as shown in Fig. 2) to evaluate how AI applications
support global tobacco control frameworks. The WHO FCTC is an
evidence-based treaty that reaffirms the right of all people to the highest
Fig. 1. PRISMA flow diagram of the article selection process.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
3

standard of health and provides legal dimensions for international
health cooperation. Key articles relevant to this review include:
• Article 8: Protection from exposure to tobacco smoke
• Article 11: Packaging and labelling of tobacco products
• Article 12: Education, communication, and public awareness
• Article 13: Tobacco advertising, promotion, and sponsorship
• Article 14: Demand reduction measures concerning tobacco depen-
dence and cessation
• Article 20: Research, surveillance, and exchange of information
This approach facilitated an integrative summary of how AI is
currently leveraged in tobacco control and identified both strengths and
limitations of existing approaches.
2.5. Quality appraisal
As per scoping review methodological guidelines [44,45], a formal
risk of bias assessment was not conducted, as the primary aim was to
map the available evidence rather than assess the effectiveness of in-
terventions. However, studies were informally appraised for methodo-
logical clarity, transparency in AI application, and relevance to public
health outcomes. We evaluated whether studies provided sufficient in-
formation on:
I1 AI algorithm selection and specification
II1 Dataset characteristics, including size and representativeness
III1 Evaluation metrics and validation approach
IV1 Limitations and potential biases in the AI implementation
Studies with inadequate methodological detail or unclear AI imple-
mentations were contextualised accordingly during synthesis to main-
tain the integrity and reliability of the review’s conclusions but were
not excluded on this basis alone.
3. Results
The detailed characteristics and data extraction table provides a
concise summary of 57 recent studies exploring artificial intelligence
applications in tobacco control. Table 1 captures essential study details,
including aims, methodologies, AI algorithms, data sources, primary
outcomes, and noted limitations. The table highlights the diversity of AI
techniques such as machine learning, large language models, and topic
modelling across various data sources like social media, clinical trials,
and online interventions. This structured synthesis allows for easy
comparison of findings, methodologies, and potential gaps or biases,
facilitating a clearer understanding of current research trends and future
directions in AI-driven public health interventions.
3.1. AI in tobacco control
Artificial intelligence (AI) has significantly transformed traditional
approaches to tobacco control by enhancing capabilities in surveillance,
prevention, intervention, and policy evaluation. Leveraging sophisti-
cated techniques such as Natural Language Processing (NLP), machine
learning (ML), predictive analytics, and conversational AI, these tech-
nological innovations enable precise monitoring of tobacco-related be-
haviours, facilitate personalised cessation interventions, enhance
predictive risk assessment, and optimise policy impact assessments
[45,47,93]. AI-driven strategies offer scalable, real-time insights and
interventions, empowering public health authorities to proactively
respond to emerging trends and challenges associated with tobacco use,
thereby advancing global tobacco control efforts.
Table 2 summarises the primary artificial intelligence (AI) technol-
ogies, algorithms, and data types utilised within tobacco control. The
table standardizes AI technologies used in tobacco control research,
showing the relationship between specific algorithms, data sources,
application areas, alignment with WHO Framework Convention on To-
bacco Control (FCTC) articles, and representative studies from the
literature review. Each technology is detailed alongside specific algo-
rithms, relevant data types, common data sources, and typical applica-
tion areas. For instance, natural language processing leverages
sentiment analysis to evaluate social media data [72], while deep
learning uses convolutional neural networks (CNN) to analyse image
data [61]. This table underscores the interdisciplinary nature of AI,
illustrating how different data streams and analytical methods combine
effectively to support targeted public health responses.
Several key themes emerged from the reviewed literature, which
indicates the evolving role of artificial intelligence in tobacco control.
These themes inform both current practice and future potential in public
Fig. 2. WHO FCTC Articles addressed Using AI. Note: Percentages exceed 100% as some studies aligned with more than one FCTC Article.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
4

Table 1
Characteristics and Data Extraction of Included Studies on AI Applications in Tobacco Control.
Reference Study Aim/Purpose AI Method/
Algorithm
Data Sources / Sample
Size
Main Findings/
Conclusions
Limitations Reported/
Comments
Relevant
WHO FCTC
Articles
[44] Evaluate adherence of
ChatGPT-generated
responses to smoking
cessation guidelines
Content analysis of
LLM (ChatGPT-3.5)
outputs
100 cessation-related
prompts analyzed
ChatGPT responses aligned
moderately well with CDC
guidelines; varied by prompt
specificity
AI’s consistency and safety
require further testing for
clinical reliability
Article 14,
Article 12
[45] Evaluate ChatGPT’s
effectiveness in providing
vaping cessation support.
Generative AI
(ChatGPT)
10 Reddit vaping
questions evaluated by
expert panel (n = 5).
ChatGPT provided highly
accurate and empathetic
responses suitable for
cessation interventions.
Limited to small query set;
unclear real-world
applicability.
Article 14
[46] Identify factors predicting e-
cigarette use in never-
smokers
ML models (e.g.,
logistic regression,
decision trees)
U.S. adult population
survey data
Peer influence, age, media
exposure were top
predictors
Cross-sectional design
limits causal inference
Article 20
[47] To identify predictors of
electronic nicotine delivery
system (ENDS) initiation
among tobacco-naive young
adults using machine
learning
Machine learning
classification
algorithms (e.g.,
logistic regression,
decision trees, etc.)
PATH study data; N =
2,944 tobacco-naive
young adults
Susceptibility to ENDS,
cigarette use, marijuana use,
and social media exposure
were top predictors
Model interpretability and
generalizability may be
limited; cross-sectional
variables used for
prospective prediction
Article 20
[48] Evaluate conversational AI
interventions’ effectiveness
for smoking cessation.
Meta-analysis Systematic review of
RCTs from 6 databases
(since 2005).
Conversational AI
significantly improved
cessation rates at 6-month
follow-up.
High heterogeneity among
studies included.
Article 14
[49] Analyze adolescent attitudes
toward JUUL using Twitter
data
Topic modeling and
sentiment analysis
Public tweets mentioning
JUUL
Found majority expressed
curiosity or usage; health
concerns secondary
Age verification of users not
possible; informal language
challenged classification
Article 12,
Article 13
[50] Explore AI potential in
improving anti-smoking
campaign effectiveness.
Conceptual overview
(predictive analytics,
personalized
interventions, social
network analysis)
N/A (Perspective article,
no empirical study
conducted).
AI can enhance campaign
effectiveness through
personalised and predictive
interventions.
No empirical validation
provided; theoretical
recommendations only.
Article 12
[51] To systematically review
ML-based predictors of
smoking cessation across
experimental studies.
Systematic Review,
Multiple Machine
Learning Techniques
Review of prior smoking
cessation ML studies; N =
varies
Common predictive
features: motivation,
nicotine dependence, app
use patterns, craving levels.
Heterogeneity of datasets
and ML methods limited
meta-analysis.
Article 14,
Article 20
[52] Examine regional variations
in tobacco-related tweets
Topic modeling (LDA),
sentiment analysis
Geotagged Twitter data Found differing themes and
sentiment trends across
regions; informed place-
based policy
Data sparsity in less active
areas
Article 20,
Article 12
[53] Characterization of e-
cigarette aerosols using a
field-portable holographic
microscope
Image analysis and
classification via AI-
enhanced microscopy
Vape shop aerosol
samples
Provided real-time aerosol
particle analysis; useful for
public exposure risk
assessment
Lab validation required;
limited to one vape shop
context
Article 8,
Article 20
[54] To explore how AI and
LLMs, particularly ChatGPT,
can assist in the
management of tobacco
dependence and cessation.
Review and expert
commentary on LLMs
like ChatGPT in
cessation support
Not a primary study;
discusses application
contexts and existing
capabilities
AI, especially ChatGPT,
shows promise in enhancing
accessibility to cessation
support, especially in
underserved populations
Need for rigorous
evaluation, regulation, and
integration with health
systems; risks of
misinformation
Article 14
[55] Identify target audiences for
hookah prevention
campaigns
Supervised Machine
Learning (Gradient
Boosting, Random
Forest)
Multinational Adult
Tobacco Survey + focus
group feedback
ML predicted demographics
most receptive to campaign
messages
Limited generalizability
across cultures/regions;
focus on hookah only
Article 12
[56] To analyze the content and
themes of e-cigarette-related
conversations on Twitter
using social listening
methods
Natural Language
Processing (NLP),
content analysis
Tweets related to e-
cigarettes; 87,963 tweets
collected over 2 months
Promotional content
dominated discussions; user
conversations revealed
themes around quitting,
flavors, and perceptions of
safety
Limited to publicly
available tweets; potential
sampling bias; did not
analyze sentiment in depth
Article 12,
Article 13
[57] Predict individual outcomes
of smoking cessation
treatments
Machine Learning
(Logistic regression,
decision trees, SVM)
Cessation trial data from
757 individuals
ML models predicted
successful quitters based on
early behavioral and
psychological data
Lacks external validation;
limited demographic
diversity in training data
Article 14
[58] To explore the role of
chatbots and virtual
assistants in improving
tobacco cessation services,
especially post-pandemic.
Conversational AI,
Virtual Assistants
Review of case studies
and applications
(qualitative evidence)
Chatbots increase
accessibility and user
engagement; shown useful
during public health
emergencies like COVID-19.
Conceptual overview; lacks
quantitative analysis and
empirical validation.
Article 14,
Article 12
[59] Predict tobacco-related
tweet topics around COP9.
LDA, Random Forest,
sentiment analysis
Tweets captured via DMI-
TCAT around COP9 event.
Achieved 91.87 % accuracy
in topic prediction;
sentiment correlated with
retweet frequency.
Study limited to specific
event (COP9); short-term
insights only.
Article 20
[60] Enhance sentiment and
intent analysis in public
health using fine-tuned
Fine-tuned Large
Language Models (e.g.,
BERT, RoBERTa)
Tobacco and e-cigarette-
related tweets (size not
explicitly stated)
Fine-tuned LLMs
significantly improved
accuracy in detecting
Generalizability limited by
training data; challenges
with sarcasm and
Article 12,
20
(continued on next page)
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
5

Table 1 (continued)
Reference Study Aim/Purpose AI Method/
Algorithm
Data Sources / Sample
Size
Main Findings/
Conclusions
Limitations Reported/
Comments
Relevant
WHO FCTC
Articles
LLMs on tobacco-related
tweets
nuanced sentiment and
intent; valuable for public
health surveillance
ambiguous language in
tweets
[37] Identifying smoking
environments from images
of daily life using deep
learning
Deep learning (CNNs
for image
classification)
Photographs from
smoking participants’
daily environments
Model accurately detected
smoking-related cues in
personal environments;
implications for relapse
prevention
Contextual factors in image
interpretation not explored
in depth
Article 8,
Article 14
[61] Use ML for detecting
tobacco point-of-sale
advertising in retailer
photographs.
Image classification
(Inception V3), Object
detection (YOLO V3)
Large dataset of tobacco
retailer photographs
(West Virginia &
Washington, DC).
Successfully classified and
located tobacco advertising
in photographs using deep
learning.
Geographic limitation;
effectiveness in diverse
settings unclear.
Article 13
[62] Assess ML-based
recommender system’s
effect on cessation
Recommender system
integrated with viral
peer referral model
RCT with 1747 adult
smokers
Cessation rates improved
with combined ML + peer
network design
Not all peer-referrals
reached intended targets;
sample bias possible
Article 14
[36] Examination of social
smoking classifications
using a machine learning
approach
Machine Learning
classification models
Survey data on smoking
behavior; n = unspecified
ML revealed nuanced social
smoking typologies;
potential to inform tailored
interventions
Did not assess long-term
cessation outcomes; sample
size not detailed
Article 14,
Article 20
[41] Review machine learning
applications in tobacco
research.
Scoping review Literature search of 74 ML
studies across multiple
databases.
Rapid growth of ML use in
tobacco research since 2018;
common in cessation tech
and social media analysis.
English-language
restriction; potential
publication bias.
Article 20
[63] Discuss AI applications for
smoking cessation in
pregnancy
AI-assisted behavioral
interventions
(conceptual)
Review-based; no primary
data
AI can personalize
pregnancy-safe cessation
programs; emphasizes
ethical frameworks and risk
stratification
Perspective only; lacks
empirical validation or
technical implementation
Article 14
[64] Identify nicotine gum-
related topics using Twitter
data.
Top2Vec topic
modelling
Twitter API collected
tweets; validation with
1000 tweets.
Smoking/vaping cessation
most common topic; minor
themes included branding,
health concerns, COVID-19
relief.
Twitter data limitations;
possible selection bias.
Article 12
[32] To predict the first smoking
lapse during a quit attempt
using real-time data and
machine learning
Machine Learning
(Gradient Boosting
Machine, Elastic Net,
Random Forest, etc.)
Data from a mobile app
used by 209
socioeconomically
disadvantaged adults
during cessation
ML models accurately
predicted first lapse within
first 3 days of quit attempt;
real-time factors like urge to
smoke and stress were
strong predictors
Generalizability to other
populations unclear; mobile
app data may not capture
all contextual factors
Article 14,
Article 20
[65] Identify predictors of
response to digital smoking
cessation intervention using
machine learning.
LASSO regression National sample; adult
smokers with depressive
symptoms; randomised
controlled trial (RCT).
Time spent on app predicted
smoking reduction;
educational attainment
moderated depressive
outcomes.
Limited to smokers with
depressive symptoms;
generalizability unknown.
Article 14
[66] Explore vaping risk
perceptions on Twitter
during EVALI
Mixed methods (topic
modeling + qualitative
coding)
Twitter data (EVALI
timeline)
Identified shifts in user
sentiment and
misconceptions during crisis
Difficult to isolate tweet
authors’ demographics
Article 12
[67] Track compliance with e-
cigarette warning labels on
Instagram
Deep Learning (CNN
for object detection,
YOLO for image
annotation)
Instagram posts related to
e-cigarettes (exact sample
not specified)
Deep learning accurately
identified label violations;
many posts lacked visible
warnings
Focus on images only; no
content/contextual
interpretation of posts
Article 11
[68] Characterize vaping content
on Instagram
Unsupervised ML
(clustering, image
recognition)
Vaping-related Instagram
posts
Identified promotional
themes, youth appeal
elements; aided in policy-
targeted content tracking
Image-focused only; limited
textual metadata
Article 13
[69] Evaluate LLM accuracy in
sentiment analysis of social
media on heated tobacco
products (HTPs).
GPT-3.5 & GPT-4
Turbo
1000 social media
messages (Facebook &
Twitter).
GPT-4 Turbo achieved
higher accuracy than GPT-
3.5 in sentiment evaluation.
Limited platforms; unclear
broader generalisability.
Article 20
[70] Classify e-cigarette content
on YouTube via machine
learning.
NLP, supervised ML
(embedding, BLSTM)
YouTube videos identified
through specific search
terms.
Videos often featured
product reviews and
promotional offers (43.2 %).
Limited analysis to
YouTube platform only.
Article 13
[71] Explore generative AI use in
tobacco control via social
media.
Generative AI
(theoretical insights
and practical
examples)
N/A (Perspective article). Generative AI useful for
social media analysis,
misinformation detection;
potential industry misuse
noted.
Theoretical and
commentary-based; no
specific methodology
reported.
Article 12,
Article 20
[72] Develop AI to identify
tobacco-promoting content
on Turkish Twitter.
BERT-based model 177,684 tweets
(quantitative); qualitative
analysis of 200 tweets.
BERT model identified
tobacco-promoting content
accurately; 39.9 % of tweets
promoted tobacco.
Limited to Turkish language
tweets; cultural specificity.
Article 13
[73] To build a deep learning
model for detecting smoking
Multimodal Deep
Learning (CNN + RNN
architecture)
Custom small-scale
dataset: biosignals, user
logs, image features
Model accurately detects
smoking events with high
Performance may not
generalize; tested on limited
Article 20
(continued on next page)
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
6

Table 1 (continued)
Reference Study Aim/Purpose AI Method/
Algorithm
Data Sources / Sample
Size
Main Findings/
Conclusions
Limitations Reported/
Comments
Relevant
WHO FCTC
Articles
behavior from multimodal
small-scale datasets.
precision, even from small
datasets.
population with controlled
inputs.
[74] Identify e-cigarette content
on TikTok using topic
modeling
BERTopic
(transformer-based
topic modeling)
2347 TikTok videos with
e-cigarette hashtags
Most content focused on
product promotion and vape
tricks; minority on health
effects or warnings
Lacks cross-platform
comparison; sample drawn
from specific keywords
Article 13
[75] Classify image content in e-
cigarette-related TikTok
videos
Unsupervised Machine
Learning (Image
Clustering with CNN
embeddings + K-
means)
1220 TikTok video frames
(image dataset)
Clustered images into
promotional, social, and
neutral content types;
promotional content
dominated
No audio/text analysis;
visual focus limits content
understanding
Article 13
[76] Analyze anti-tobacco
campaign message
engagement on Facebook
using ML
Machine Learning
Classification (Support
Vector Machine, Naïve
Bayes, Decision Trees)
Facebook posts from CDC
Tips campaign (n = 3,835
posts)
Identified which post
features (tone, visual
content, themes) influenced
engagement; positive tone
and visual posts had higher
interaction
Limited to Facebook;
engagement does not
directly translate to
behavior change
Article 12
[77] To analyze public response
to e-cigarette regulations
using NLP and topic
modeling
NLP, Latent Dirichlet
Allocation (LDA) topic
modeling, sentiment
analysis
Twitter data; exact size
not reported
Identified dominant topics
and sentiments following
policy changes; highlighted
negative sentiment spikes
during regulation
announcements
Challenges with filtering
bots, sarcasm, and non-
English content; difficulty
interpreting unsupervised
topics
Article 20
[78] Assess user experience of
virtual human (Florence) for
tobacco cessation during
COVID-19.
AI conversational
agent
Web-based survey of 115
global users (49
countries).
Positive user experience,
increased intent to pursue
recommended cessation
services.
Convenience sample;
potential self-selection bias.
Article 14
[79] Test feasibility of AI
conversational agent for
medication adherence
Conversational AI
prototype with ML
behavior tracking
Mixed methods trial on
varenicline users
Promising user engagement
and intent to adhere;
informed digital health tool
refinement
Still in feasibility phase;
outcome data pending
Article 14
[39] Assessing secondhand and
thirdhand smoke exposure
in infants using ML and
biomarkers
Machine learning
integration of
questionnaire and
biomarker data
Canadian infant cohort;
survey and biomarker
data
ML identified key exposure
predictors; potential for
environmental health
monitoring
Generalizability may be
limited by cohort
composition
Article 8,
Article 20
[80] To assess whether Reddit
discussions could detect
early signals of vaping-
associated lung injury
(EVALI)
Qualitative NLP
methods, trend
analysis
Reddit posts mentioning
vitamin E acetate and
Dank Vapes
Increase in mentions of
vitamin E acetate preceded
CDC alert; Reddit can serve
as early surveillance tool
Retrospective study; cannot
infer causality; potential
sampling bias from
subreddit selection
Article 20
[81] Detect vaping-related tweets
during 2019 EVALI outbreak
Supervised ML
classifiers (e.g., logistic
regression, random
forest)
Vaping-related tweets
during EVALI (Twitter
API)
ML detected vaping
discourse spikes during
health alerts; potential for
early warning
Limited to public tweets;
lacked location tagging
Article 20
[82] Apply predictive analytics to
tobacco cessation
Data mining
techniques
(association rules,
classification)
Survey/interview data
from tobacco users
Predicted relapse risk and
intervention timing
Exploratory study; lacked
clinical integration
Article 14
[83] Identify and analyze
synthetic nicotine
promotions on Instagram
Natural Language
Processing (NLP),
supervised text
classification
Instagram posts related to
synthetic nicotine
products
Promotional content often
lacked warning labels and
used youth-targeted
language
Instagram’s evolving API
access limits repeatability;
focus on English-language
content
Article 13
[84] Evaluate AI and ML tools for
screening public health-
relevant content on social
media
Generative AI (e.g.,
ChatGPT), ML
classifiers (e.g., logistic
regression)
Diverse social media
content; specific sample
details not provided
Highlighted utility of AI for
automating content
moderation and screening;
proposed framework for
integrating generative
models with traditional ML
Data privacy and ethical
concerns in deployment;
model performance
depends on prompt quality
and training data bias
Article 12
[85] Simulate adolescent
responses to vaping-
prevention messaging via
AI.
AI simulation model
(LLM) trained on
adolescent ratings
Adolescents rated vaping
prevention messages (46
text-only; 220 text/image
combined).
AI accurately predicted
adolescent effectiveness
ratings; visual information
significantly enhanced
model predictions.
Sample diversity limited;
controlled study conditions.
Article 12
[86] To discuss the role of AI in
supporting tobacco
cessation strategies during
the COVID-19 pandemic
Artificial Intelligence
(general applications),
including digital
health platforms and
chatbots
Not based on original
dataset; perspective piece
referencing global trends
and technologies
AI tools such as chatbots and
digital interventions can aid
cessation efforts by offering
scalable, accessible support
during health system strain
Perspective article; lacks
empirical data or specific
algorithmic evaluation;
conceptual overview only
Article 14
[87] Predict e-cigarette use and
dependence in youth
Supervised ML (e.g.,
XGBoost, logistic
regression)
Survey data from Ontario
high school students
Accurate risk stratification
model; top predictors
included peer use and
depression
Self-report bias; lack of
biological markers
Article 20
(continued on next page)
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
7

health policy and intervention design.
3.1.1. Social media surveillance and sentiment analysis
By leveraging AI for social media surveillance and sentiment anal-
ysis, public sentiment, misinformation, and marketing trends can be
tracked to facilitate faster regulatory response, and media campaign
adjustments. Artificial intelligence models, particularly Natural Lan-
guage Processing (NLP) and machine learning (ML) algorithms, have
significantly improved the surveillance of tobacco use patterns. By sys-
tematically analysing large datasets derived from social media platforms
such as Twitter, Reddit, Instagram, and various online forums, these AI-
driven tools provide timely identification of emerging tobacco-related
trends, such as the rapid uptake of e-cigarettes and vaping devices
[56,80,91]. NLP algorithms, for example, can extract critical insights by
identifying recurring themes, phrases, or keywords indicative of
tobacco-related behaviours and public sentiments.
AI-driven analysis of Twitter and other social media platforms has
demonstrated substantial promise for tobacco control surveillance and
policymaking [56,60,64]. Using natural language processing (NLP),
sentiment analysis, and machine learning classifiers, researchers sys-
tematically evaluate public reactions to tobacco control measures such
as anti-smoking legislation, and public health campaigns [77,85]. For
example, AI techniques have been instrumental in tracking responses to
smoke-free laws, identifying public sentiment shifts, and detecting
Table 1 (continued)
Reference Study Aim/Purpose AI Method/
Algorithm
Data Sources / Sample
Size
Main Findings/
Conclusions
Limitations Reported/
Comments
Relevant
WHO FCTC
Articles
[88] Explore link between media
coverage and support for
Tobacco 21 policies
Supervised and
unsupervised ML on
media content
News articles and online
commentary
Identified correlation
between news frequency
and policy awareness
Causality not confirmed;
time-lag effects not fully
explored
Article 12
[89] To identify which features in
cessation apps correlate
with successful quitting
using ML.
Supervised Machine
Learning Models
Experimental dataset
from cessation app users
(sample size not stated)
Goal-setting, reminders, and
coaching tools positively
associated with quitting
success.
Potential selection bias;
feature usage self-reported;
secondary analysis limits
causal inference.
Article 14
[90] To review how machine
learning has been integrated
into various aspects of
tobacco control research.
Machine Learning
(general overview of
techniques)
Tobacco-related ML
studies and databases
(review)
ML has improved disease
prediction, biomarker
identification, and cessation
support; future potential
noted.
Non-systematic review; no
original data analysis
performed.
Article 20
[91] Evaluate GPT-4o in
detecting vaping themes in
social media.
GPT-4o multimodal AI 102 Instagram/TikTok
micro-influencer videos.
GPT-4o accurately detected
vaping and related
promotional contexts (87
%-99 %).
Small, niche sample;
generalisability limited.
Article 13
[92] Examine early adolescent
vaping through ML risk
modeling
Machine Learning
(decision tree, random
forest)
Cross-sectional adolescent
survey data
Predicted initiation
likelihood; social influences
key predictors
Model may not generalize
outside studied region
Article 20
[93] To identify Reddit users
contemplating vaping
cessation for targeted digital
interventions
Large Language
Models (LLMs),
classification with
prompt-based tuning
Reddit posts from vaping-
related subreddits
LLMs successfully identified
users likely to engage with
cessation content; provides a
pipeline for digital health
outreach
Ethical concerns over user
consent and potential
intervention biases
Article 14
[94] Explore targeted marketing
toward marginalized groups
via cigar tweets
Computational content
analysis with NLP and
engagement prediction
models
Public & protected cigar-
related tweets; user-level
metadata (sample not
specified)
Targeted tweets had higher
engagement among
minority groups; suggested
intentional marketing bias
Cannot confirm industry
intent; access to protected
tweets limited verification
Article 13
[95] Automated detection of
hookah imagery on
Instagram
CNN + SVM hybrid
model
Instagram posts with
hookah-related hashtags
High accuracy in hookah
image recognition;
supported surveillance and
trend tracking
Focused on visual data only;
lacked behavioral context
Article 13
Table 2
AI Technologies, Algorithms, and Data Types Used in Tobacco Control.
AI Technology Algorithms Datasets Applications WHO FCTC Article Representative
References
Machine Learning
(ML)
Random Forest, Support Vector
Machine (SVM), Gradient
Boosting, Logistic Regression,
XGBoost
Electronic Health Records
(EHRs), Survey data, Social
media data, Public health
databases
Risk prediction, User behavior
classification, Relapse
forecasting, Population
screening
Article 14
(Cessation), Article
20 (Research)
[47,57,65,87,92]
Natural Language
Processing (NLP)
Sentiment Analysis, Topic
Modeling (LDA), BERT, Named
Entity Recognition, Text
classification
Twitter/Reddit posts, Clinical
text notes, Tobacco policy
documents, Health forum
discussions
Trend monitoring, Public
sentiment analysis, Marketing
detection, Policy text analysis
Article 13
(Advertising), Article
20 (Research)
[44,59,72,80]
Deep Learning Convolutional Neural Network
(CNN), Recurrent Neural
Network (RNN), Transformer
models
Image/video data, Physiological
sensor streams, Multimodal
social media content
Content analysis, Facial
recognition, Emotion detection,
Warning label compliance
Article 11
(Packaging), Article
13 (Advertising)
[25,37,61,67,73]
Reinforcement
Learning
Q-learning, Deep Reinforcement
Learning
User interaction logs, Mobile app
engagement data, Behavioral
patterns
Personalized interventions, User
engagement optimization,
Adaptive messaging
Article 14 (Cessation) [57,62,79,89]
Large Language
Models
GPT-3.5/4, ChatGPT, BERT Conversational data, Health
information databases, Clinical
guidelines
Cessation chatbots, Health
communication, Content
analysis, Education
Article 12
(Education), Article
14 (Cessation)
[44,45,54,69,93]
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
8

covert promotional strategies deployed by e-cigarette companies
[67,72,77]. These analyses offer public health authorities actionable
insights, enabling timely interventions to counteract misinformation,
evaluate the effectiveness of messaging, and enhance regulatory mea-
sures against aggressive tobacco product marketing, particularly toward
vulnerable groups and youth.
Sentiment analysis, a subset of NLP, has become particularly valu-
able for understanding public attitudes and reactions toward tobacco
control measures and new tobacco products. By assessing sentiment in
real-time, policymakers and public health practitioners can respond
swiftly and effectively to public concerns, misinformation, or promo-
tional content. Studies have successfully utilised sentiment analysis to
gauge public response toward tobacco legislation, taxation, health
warnings, and the introduction of novel tobacco products [64,69,77]
thereby assisting regulatory bodies in making informed, data-driven
decisions.
3.1.2. Conversational AI and digital cessation support
AI technology has been instrumental in developing innovative, per-
sonalised tools for smoking cessation. Mobile health applications pow-
ered by AI—such as Quit Genius and SmokeFree—use advanced
reinforcement learning algorithms and predictive analytics to customise
interventions according to individual user profiles, behaviours, and risk
factors [48,58,78]. These apps monitor user progress and behavioural
patterns in real-time, offering tailored motivational messages, coping
strategies, and rewards, significantly enhancing user engagement and
quit rates.
Furthermore, conversational AI, in the form of chatbots and virtual
health assistants, has emerged as an effective approach to deliver im-
mediate, continuous support for individuals attempting to quit tobacco
[48,78]. Virtual assistants utilise sophisticated dialogue systems to
simulate empathetic and personalised interactions, provide immediate
responses to user queries, track moods and cravings, and proactively
offer relapse prevention strategies. Such technologies not only improve
accessibility and scalability of cessation services but also provide vital
support during high-risk relapse periods.
3.1.3. Predictive risk modelling and personalized interventions
Predictive modelling, another crucial AI application, has demon-
strated substantial promise in identifying individuals at high risk for
tobacco initiation and those who require cessation support [47,51,65].
AI-driven predictive models leverage extensive datasets from electronic
health records (EHRs), genetic markers, behavioural assessments, and
socio-demographic variables to create comprehensive risk profiles. By
analysing complex patterns within these datasets, machine learning al-
gorithms can accurately forecast individual vulnerability to tobacco
initiation, and those needing needed cessation support based on
behavioural, demographic, and psychosocial inputs.
The use of predictive risk modelling aligns closely with precision
medicine, enabling healthcare providers to deliver highly personalised
and targeted preventive measures or interventions tailored specifically
to the individual’s risk profile. For instance, healthcare systems have
implemented these predictive tools to proactively identify patients who
may benefit from early cessation counselling, pharmacotherapy, or
other supportive services, thereby optimising resource allocation and
enhancing overall effectiveness [48,51,63].
3.1.4. Policy surveillance, evaluation and public health messaging
Studies revealed AI could be used in policy surveillance and
compliance monitoring. This could be done by assessing media cover-
age’s influence on policy support [77,88], automating the tracking of
tobacco-related regulations or policy impacts [88] and evaluating
platform-level visual warning compliance [61,67]. These applications
offer a scalable method for real-time policy surveillance, though chal-
lenges persist in understanding intent and context solely from visual or
textual data.
AI techniques have also advanced the evaluation of tobacco control
policies and the delivery of adaptive public health messaging
[50,71,96]. Through sophisticated modelling and simulation, AI systems
can predict the potential impacts of various tobacco control measur-
es—such as advertising restrictions, smoke-free laws, and packaging
regulations on different population groups. These models help policy-
makers anticipate behavioural and economic outcomes, refine policy
implementation strategies, and preempt potential unintended
consequences.
Moreover, AI’s ability to continuously analyse real-time engagement
and behavioural data facilitates highly dynamic and adaptive public
health messaging campaigns [71,96]. AI algorithms can optimise
communication strategies by rapidly assessing message performance
across various demographics, social platforms, or geographic areas. This
capability allows health campaigns to promptly adjust messaging con-
tent, timing, and delivery methods to maximise public impact, ensuring
messages are resonant, culturally sensitive, and effectively targeted to
high-risk groups or communities that may otherwise be difficult to
engage through traditional methods.
3.2. Distribution of AI methodologies across tobacco control applications
Machine learning emerged as the most widely used AI technology,
employed in 68 % (n = 39) of included studies. These applications
typically focused on classification tasks, risk prediction models, and
pattern recognition within diverse datasets. Natural language processing
(NLP) was utilized in 35 % (n = 20) of studies, primarily for social media
surveillance, sentiment analysis, and content evaluation of tobacco-
related messaging. Deep learning approaches featured in 21 % (n =
12) of studies, with convolutional neural networks (CNNs) being the
most common architecture for image analysis applications such as
detecting tobacco imagery in social media and compliance monitoring
of warning labels.
Less frequently utilized methodologies included reinforcement
learning (12 %, n = 7), which was predominantly applied in personal-
ized cessation interventions and adaptive health messaging, and large
language models (LLMs) (9 %, n = 5), which represented the newest
technological wave focused on conversational agents for cessation
support and comprehensive content analysis. Table 3 provides a detailed
breakdown of the AI methodologies and their distributions across the
Table 3
Distribution of AI Methodologies Across Included Studies.
AI Technology Number
of Studies
(%)
Primary Algorithms Major Application
Areas
Machine
Learning
39 (68 %) Random Forest,
Support Vector
Machine, Gradient
Boosting, Logistic
Regression
Risk prediction, user
behavior
classification, policy
impact assessment
Natural
Language
Processing
20 (35 %) Sentiment Analysis,
Topic Modeling,
BERT, Named Entity
Recognition
Social media
surveillance, public
sentiment analysis,
marketing detection
Deep Learning 12 (21 %) Convolutional Neural
Networks, Recurrent
Neural Networks,
Transformer models
Image analysis,
multimodal data
integration,
behavioral pattern
recognition
Reinforcement
Learning
7 (12 %) Q-learning, Deep
Reinforcement
Learning
Personalized cessation
interventions,
adaptive health
messaging
Large Language
Models
5 (9 %) GPT-3.5, GPT-4,
ChatGPT, BERT
Cessation support
chatbots, content
analysis, health
communication
Note: Percentages exceed 100% as many studies employed multiple AI technologies.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
9

included studies.
3.2.1. Temporal trends in AI adoption
Fig. 3 illustrates the temporal evolution of AI applications in tobacco
control from 2010 to 2025. A notable inflection point occurred around
2018, with a significant acceleration in publications employing AI for
tobacco control purposes. The most substantial growth was observed in
machine learning applications, which showed a 320 % increase between
2018–2022 compared to 2013–2017. Studies utilizing deep learning
methodologies began appearing predominantly after 2019, while large
language models represent the newest technological wave, with all
identified applications emerging after 2022.
A significant finding was the growing trend toward methodological
integration, with 42 % (n = 24) of studies employing multiple AI tech-
nologies within the same application. The most common integration
pattern combined machine learning with NLP (19 %, n = 11), particu-
larly for social media surveillance applications that required both con-
tent classification and sentiment analysis.
Our analysis revealed substantial diversity in data sources utilized
across studies. Social media platforms served as the primary data source
for 46 % (n = 26) of studies, with Twitter/X being the most frequently
utilized platform (28 %, n = 16), followed by Instagram (12 %, n = 7)
and Reddit (9 %, n = 5). Electronic health records provided data for 25
% (n = 14) of studies, primarily those focused on risk prediction and
personalized interventions. Survey data, mobile application usage data,
and image/video datasets were also commonly utilized.
Computational infrastructure requirements varied considerably,
with most machine learning studies utilizing standard statistical pack-
ages, while deep learning applications typically required more sophis-
ticated GPU-based computing environments. Notably, only 5 studies (9
%) reported the computational resources required for model develop-
ment and deployment, highlighting a significant gap in methodological
reporting that could impact reproducibility and practical
implementation.
3.2.2. Thematic mapping of AI applications in tobacco control
Beyond methodological classification, our review identified four
primary thematic domains where AI is being applied across the tobacco
control landscape. These domains represent distinct intervention tar-
gets, stakeholder groups, and implementation contexts that shape how
AI technologies are being leveraged to advance tobacco control
objectives.
It’s important to note that the thematic categorization presented here
differs from the WHO FCTC article alignment shown in Fig. 2. While
Fig. 2 presents the distribution of all 57 studies by their alignment with
specific FCTC articles (with some studies aligning with multiple arti-
cles), our thematic analysis categorizes each study into one primary
application domain based on its main focus. Therefore, the numbers and
percentages in this section represent the primary thematic classification
of each study, whereas Fig. 2 shows all.
3.2.2.1. Surveillance and monitoring (n = 24, 42 %). The largest the-
matic cluster focused on surveillance and monitoring applications,
where AI technologies enable automated, large-scale analysis of
tobacco-related behaviours, marketing activities, and public discourse.
Key applications within this domain included:
• Social media monitoring of emerging products and trends (n = 14)
• Sentiment analysis toward tobacco control policies (n = 9)
• Detection of illicit or non-compliant marketing content (n = 7)
• Geographic and demographic pattern identification (n = 5)
Machine learning classifiers and NLP techniques dominated this
domain, with a growing integration of computer vision approaches for
image and video content analysis. These surveillance applications pri-
marily aligned with WHO FCTC Articles 13 (tobacco advertising, pro-
motion, and sponsorship) and 20 (research, surveillance, and exchange
of information), while some also supported Article 12 (education,
communication, and public awareness) as a secondary alignment.
3.2.2.2. Cessation support and intervention (n = 19, 33 %). The second-
largest thematic cluster encompassed cessation support and intervention
applications, where AI enables personalized, scalable approaches to
smoking cessation. Key applications included:
• Digital cessation chatbots and virtual assistants (n = 8)
Fig. 3. Temporal Evolution of AI Technologies in Tobacco Control (2010–2025). This figure illustrates the temporal evolution of AI applications in tobacco control
from 2010 to 2025. A notable inflection point occurred around 2018, with significant acceleration in publications employing AI for tobacco control purposes,
particularly in machine learning applications. Deep learning methodologies began appearing predominantly after 2019, while large language models represent the
newest technological wave, with all identified applications emerging after 2022.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
10

• Predictive modelling of relapse risk (n = 7)
• Personalized intervention matching (n = 6)
• Real-time craving and trigger detection (n = 4)
Reinforcement learning and predictive analytics were prominently
featured within this domain, alongside conversational AI applications
utilizing large language models in more recent studies. These applica-
tions primarily aligned with WHO FCTC Article 14 (demand reduction
measures concerning tobacco dependence and cessation). While Fig. 2
shows 26 studies (45 %) with Article 14 alignment, only 19 studies had
cessation support as their primary focus. The remaining 7 studies had
cessation as a secondary application while primarily focusing on sur-
veillance (n = 4), policy support (n = 2), or education (n = 1).
3.2.2.3. Policy and regulatory support (n = 9, 16 %). A smaller but
significant cluster focused on policy and regulatory applications, where
AI tools assist in policy development, implementation, and evaluation.
Key applications included:
• Impact assessment of proposed regulations (n = 5)
• Compliance monitoring with existing policies (n = 4)
• Policy effectiveness modelling (n = 3)
• Regulatory text analysis and comparison (n = 2)
This domain featured diverse methodological approaches, with ma-
chine learning and NLP being most common. These applications aligned
with multiple WHO FCTC articles including Articles 8 (protection from
exposure to tobacco smoke), 11 (packaging and labelling of tobacco
products), and 13 (tobacco advertising, promotion, and sponsorship).
3.2.2.4. Education and communication (n = 5, 9 %). The smallest the-
matic cluster focused on education and communication applications,
where AI enhances the development and delivery of anti-tobacco
messaging. Key applications included:
• Message tailoring and optimization (n = 3)
• Audience segmentation for targeted campaigns (n = 2)
• Educational content personalization (n = 2)
Machine learning and NLP dominated this domain, with emerging
applications of large language models for content generation. These
applications primarily aligned with WHO FCTC Article 12 (education,
communication, and public awareness). Fig. 2 shows 13 studies (22 %)
with Article 12 alignment, but only 5 studies had education and
communication as their primary focus. The remaining 8 studies included
Article 12 as a secondary alignment while primarily focusing on sur-
veillance (n = 5) or cessation support (n = 3).
Our thematic analysis reveals that AI applications in tobacco control
remain unevenly distributed across potential domains, with surveillance
and cessation support receiving the most attention, while policy support
and education applications represent emerging areas with significant
growth potential.
The synthesis of methodological approaches and thematic domains
provides a comprehensive landscape view of how AI is transforming
tobacco control across multiple dimensions. This integrated perspective
highlights both the current state of development and critical gaps that
require further research and implementation attention.
3.3. Case studies and applications
The integration of Artificial Intelligence (AI) into tobacco control is
exemplified by several innovative case studies and real-world applica-
tions. These cases illustrate how advanced AI technologies, including
facial recognition, machine learning (ML), and natural language pro-
cessing (NLP), are actively transforming public health practices by
enabling comprehensive surveillance of tobacco-related attitudes and
behaviours. The following case studies highlight the practicality, effec-
tiveness, and potential of AI-driven approaches in addressing the com-
plexities of tobacco use.
3.3.1. AI applications in tobacco industry interference
Tobacco industry interference (TII) represents a significant and
persistent barrier to effective global tobacco control. Historically, to-
bacco corporations have employed diverse strategies, including influ-
encing research outcomes, manipulating data, infiltrating regulatory
processes, and shaping public perceptions to maintain market domi-
nance [97,98]. Understanding and addressing these tactics are essential
for ensuring AI-driven tobacco control measures remain unbiased,
effective, and ethically aligned with public health goals.
Table 4 integrates essential information on key organisations, AI-
based tools, and ethical and regulatory frameworks guiding AI appli-
cations in tobacco control. It provides a clear overview of organisations
Table 4
AI-based Tools, Key Organisations, and Ethical Frameworks in Tobacco Control.
Organisation/
Initiative
Country/
Region
AI-based
Tools and
Projects
Key AI
Features
Relevant
Ethical or
Regulatory
Guidelines
Truth
Initiative
USA Digital
cessation tools
and chatbot
interventions
Predictive
analytics,
conversational
AI
WHO
Framework
Convention
on Tobacco
Control
(FCTC), FDA
Digital
Health Plan
Quit Sense UK Personalised
smoking
cessation
application
Reinforcement
learning,
behavioural
analytics
GDPR, WHO
Ethics and
Governance
of AI
WHO Digital
Health
Initiative
Global Florence:
Artificial
Intelligence
bot to support
smoking
cessation
Advanced
neural
network-based
cognitive
architecture
with real-time
emotional
responsiveness
WHO Ethics
and
Governance
of AI for
Health,
Article 5.3 of
WHO FCTC
SmokeFree
App Ltd
Global SmokeFree
cessation
mobile app
Real-time
analytics,
predictive
relapse alerts
GDPR, IEEE
Ethical
Framework
National
Cancer
Institute
(NCI) ¡
Smokefree.
gov
USA Text-based
quit programs
and
SmokefreeTXT
Predictive
messaging
algorithms,
user behavior
tracking
HIPAA, U.S.
Health IT
regulations,
FDA
guidance
Health
Promotion
Board
(HPB)
Singapore “I Quit”
Programme
with digital
support tools
Behavior-based
AI tracking,
progress
analytics
Singapore
PDPA, WHO
FCTC
Canadian
Cancer
Society
Canada “Break It Off
Cessation
Campaign”
and “Quit
Coach” apps
Gamified
interventions,
push-based
behavioral
reminders
PIPEDA,
Canadian
Centre for
Ethics in AI
(Montreal
Declaration)
My Life My
Quit
(National
Jewish
Health)
USA MyQuit app
and integrated
telehealth
coaching
Machine
learning for
quit plan
personalization
HIPAA, FDA
Digital
Health
Framework
Be He@lthy,
Be Mobile
(WHO-ITU)
Global mCessation
initiative (SMS
and app-
based)
Scalable AI-
based
messaging
systems
WHO Ethics
and
Governance
of AI, WHO
FCTC
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
11

such as the Truth Initiative, the UK NIHR (Quit Sense), and the WHO
Digital Health Initiative, each actively deploying AI technologies for
prevention, intervention, and monitoring efforts. The table identifies
distinct AI features like conversational AI, facial recognition, predictive
modelling, and real-time analytics used in these tools. Additionally, it
aligns each initiative with pertinent ethical standards and regulatory
frameworks, such as the WHO Framework Convention on Tobacco
Control (FCTC), FDA Digital Health Innovation Action Plan, and the
European Union’s General Data Protection Regulation (GDPR). Thus,
this comprehensive summary underscores the critical interplay between
technological innovation, organisational efforts, and ethical compliance
essential for responsible and effective public health interventions.
3.3.2. Corporate rebranding and digital innovation
In response to global shifts toward harm reduction and smoke-free
alternatives, tobacco companies have strategically leveraged AI tech-
nologies to promote alternative nicotine delivery systems such as heated
tobacco products and e-cigarettes [99]. For example, Altria utilizes
machine learning algorithms to analyse consumer behaviour and pur-
chasing patterns, enabling more personalized and targeted marketing
strategies [100]. British American Tobacco (BAT) has also expanded its
product range to include synthetic nicotine pouches, leveraging digital
insights to inform product development and marketing approaches
[101]. These technological advancements are part of a broader industry-
wide strategy wherein tobacco companies reposition themselves as
stakeholders in tobacco harm reduction, while continuing to market and
expand their portfolio of novel nicotine products [102]. Such reposi-
tioning efforts allow tobacco firms to gain access to regulatory conver-
sations and influence tobacco control policy under the guise of
innovation and risk reduction. These approaches allow tobacco com-
panies to present their products as innovative, technologically
advanced, and potentially less harmful, thus reinforcing nicotine
addiction under a veneer of modernity and safety [103,104]. Such AI-
driven tactics pose ethical and regulatory challenges, raising serious
concerns regarding youth exposure, product normalisation, and
perpetuation of addiction cycles.
3.3.3. Data manipulation and research influence
Tobacco corporations have historically sought to influence research
agendas and outcomes [104,106], a pattern now extending into AI-
focused research. Companies frequently fund studies emphasising the
purported reduced harm of their newer products [103,104] deliberately
minimising associated health risks. AI-based simulations and predictive
models financed by industry sources risk producing biased or misleading
results, which can distort evidence-based policymaking and compromise
public health efforts. Additionally, proprietary datasets owned by to-
bacco companies, utilised in their AI research, are typically inaccessible
to independent investigators or regulatory agencies, further limiting
transparency and rigorous independent assessment.
3.3.4. Algorithmic targeting of vulnerable groups
A critical ethical concern associated with tobacco industry-driven AI
technology is the targeted exploitation of vulnerable populations. AI
algorithms, employing extensive behavioural data analytics, enable the
precise targeting of demographic groups at greater susceptibility to
nicotine addiction—such as adolescents, low-income communities, or
individuals with mental health disorders. By algorithmically profiling
these populations and delivering personalised, compelling messaging,
tobacco companies can exacerbate health disparities and undermine
global public health efforts aimed at reducing tobacco use and its related
harms.
3.3.5. Undermining AI-Based tobacco control measures
AI-enabled tobacco control strategies such as real-time social media
monitoring, sentiment analysis, and trend prediction have themselves
become targets for industry interference. Tobacco companies can
employ bots, coordinated misinformation campaigns, and automated
promotional content dissemination to flood digital platforms, skewing
data analysed by public health AI systems. Such tactics deliberately
distort public opinion metrics and undermine the credibility of AI sur-
veillance tools designed to inform policy decisions, thus reducing their
effectiveness and reliability as instruments for tobacco control.
3.3.6. Regulatory evasion and lobbying
The tobacco industry can expand its use of AI into sophisticated
lobbying and regulatory evasion practices. AI tools can assist tobacco
corporations in monitoring legislative developments, analysing policy
trends, and framing strategic lobbying communications designed to in-
fluence legislators and undermine public health initiatives [105,106].
Additionally, advanced AI-driven opinion-mining and content optimi-
sation technologies enable the targeted discrediting of tobacco control
advocates and health organisations, strategically diminishing their in-
fluence and credibility. This undermines public trust in health author-
ities and contributes significantly to delays in the adoption and
enforcement of AI-supported tobacco control policies.
3.4. Safeguarding AI for public health
Given the substantial risks posed by tobacco industry interference,
safeguarding the integrity and effectiveness of AI applications in tobacco
control has become increasingly important. A critical component of this
safeguarding involves maintaining strict transparency and indepen-
dence in AI research. Researchers and public health institutions must
ensure that their studies and interventions remain entirely free from
tobacco industry funding or influence (WHO FCTC Article 5.3 – Imple-
menting public health policies devoid of tobacco industry influence),
clearly disclosing funding sources and methodologies to avoid conflicts
of interest and preserve scientific credibility.
Public health organisations should also prioritise developing and
utilising open-source AI tools, which promote transparency, accessi-
bility, and independent verification. Open-source systems reduce the
risk of manipulation by commercial interests, allowing independent
researchers and regulators to verify findings, methods, and outcomes,
thereby enhancing public trust and scientific robustness. Robust data
governance policies and regulatory frameworks are essential for pro-
tecting AI-driven public health initiatives. Such policies must clearly
define data collection standards, secure data handling procedures, and
rigorous auditing processes. Effective data governance prevents industry
manipulation of AI datasets, ensures unbiased analyses, and safeguards
sensitive health data against misuse or exploitation.
Moreover, international collaboration plays a pivotal role in estab-
lishing ethical standards for AI in tobacco control in line with vital
health policies such as the WHO FCTC Article 22 which encourages
parties to share technical, scientific and legal knowledge towards
achieving the WHO FCTC objectives and SDG 17- which emphasizes the
importance of collaboration between developed and developing nations
to achieve the Sustainable Development Goals.
Global partnerships and consistent regulatory alignment with the
WHO Framework Convention on Tobacco Control (FCTC) particularly
Article 5.3, which explicitly calls for protecting public health policies
from tobacco industry interference are essential. Coordinated global
actions can help standardise ethical AI practices, enhance surveillance
capabilities, and promote equitable and effective tobacco control in-
terventions worldwide. By proactively adopting these comprehensive
protective strategies, public health systems can leverage the immense
potential of AI technologies effectively, ensuring that such innovations
remain ethically sound, unbiased, and optimally beneficial to global
tobacco control efforts.
3.4.1. Applying AI to extend the WHO FCTC
Cessation (Article 14) and Research (Article 20) dominate due to the
data-driven nature of AI and machine learning. Education and
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
12

Communication (Article 12) using AI-powered message targeting, user
education, and campaign enhancement is also addressed. Also, Promo-
tion and Advertising (Article 13) is a strong area where AI is used to
monitor and counteract digital tobacco marketing, particularly among
youth. On the other hand, underexplored areas such as labeling, tax
policies, or secondhand and thirdhand smoke protections present po-
tential for future AI-focused research.
The use of varied artificial intelligence models was noticeably
skewed towards predictive modelling, cessation support and social
media surveillance. While this is a laudable start, it reflects the need for
more divergent skill set to fully harness the extensive prospects that AI
offers for tobacco control. For example, the available literature did not
address how AI could facilitate WHO FCTC 22 to foster stronger gov-
ernment policy, collaboration and automated knowledge sharing to-
wards achieving tobacco endgame [8,9] especially as Article 20 was
strongly addressed.
4. Discussion
4.1. Critical analysis of AI in tobacco control: innovation versus ethical
risks
The findings of this review reveal a complex landscape where AI
technologies simultaneously offer unprecedented opportunities for to-
bacco control while introducing significant ethical and implementation
challenges. Our analysis highlights the need for nuanced consideration
of both innovation potential and associated risks within specific appli-
cation contexts.
4.1.1. Innovation potential
The integration of multimodal AI approaches represents one of the
most promising innovations identified in this review. Studies like
Engelhard et al. [37] demonstrate how deep learning algorithms can
identify smoking environments from images of daily life with high ac-
curacy, potentially enabling just-in-time interventions during high-risk
moments for relapse. This capability to process and integrate diverse
data streams (visual, textual, and behavioral) enables a more compre-
hensive understanding of tobacco use contexts than previously possible
with traditional surveillance methods.
Similarly, conversational AI applications are transforming cessation
support through personalized, scalable interventions. The emergence of
large language models, though still in early application stages, shows
particular promise for addressing accessibility barriers. Chow et al. [54]
emphasize AI’s potential to reduce disparities in accessing quality
cessation services, particularly benefiting regions with limited health-
care resources. This ability to provide continuous, adaptive support
through digital interfaces addresses a critical gap in traditional cessation
programs, which often struggle with engagement sustainability and
personalization at scale. The ability to provide continuous, adaptive
support through digital interfaces addresses a critical gap in traditional
cessation programs, which often struggle with engagement sustainabil-
ity and personalization at scale.
Predictive modelling applications have demonstrated impressive
capabilities in identifying at-risk populations before tobacco initiation.
For instance, Atuegwu et al. [47] achieved high accuracy in predicting
electronic nicotine delivery system initiation among tobacco-naive
young adults, potentially enabling targeted prevention efforts. This
proactive capability represents a significant shift from reactive ap-
proaches that intervene only after tobacco use has begun.
4.1.2. Ethical risks and challenges
Despite these promising innovations, our findings also reveal sub-
stantial ethical concerns and implementation challenges. A particularly
troubling pattern is the potential for corporate misuse of AI technolo-
gies. Wu et al. [94] documented how machine learning algorithms have
been employed to enable targeted marketing of cigar products toward
historically marginalized communities, with higher engagement rates
among minority groups suggesting intentional bias in marketing algo-
rithms. This finding aligns with tobacco industry’s historical targeting of
vulnerable populations, now amplified through AI’s precision targeting
capabilities.
The emergence of generative AI tools like ChatGPT presents a
double-edged sword for tobacco control. While these systems can pro-
vide personalized cessation advice and enhance health communication,
they also risk amplifying misinformation if not integrated with evidence-
based frameworks. Abroms et al. [44] found that ChatGPT-generated
responses to cessation queries aligned only moderately well with CDC
guidelines, with accuracy varying substantially based on prompt speci-
ficity. This inconsistency raises concerns about the potential for AI
systems to disseminate inaccurate health information at scale if not
properly validated against clinical guidelines.
Privacy concerns represent another significant ethical challenge.
Many AI applications in tobacco control rely on continuous monitoring
of user behaviour through smartphones, social media, or wearable de-
vices. While this enables personalized interventions, it also creates risks
of surveillance overreach and data misuse. Few studies explicitly
addressed user consent processes or data governance frameworks, sug-
gesting a concerning gap in ethical implementation.
Perhaps most problematic is the persistent issue of algorithmic bias.
Our review found limited consideration of how AI systems might
perform differently across diverse populations. Given documented dis-
parities in tobacco use across racial, socioeconomic, and geographic
dimensions, AI systems trained on non-representative datasets risk
exacerbating existing inequities rather than reducing them. Sharp et al.
[84] highlight this concern, noting that social media screening tools
with algorithmic bias could disproportionately flag content from mi-
nority communities, potentially leading to discriminatory outcomes.
4.2. Policy implications and governance recommendations
Our findings point to several critical policy implications and gover-
nance recommendations to maximize AI’s benefits while mitigating
associated risks.
4.2.1. Transparency and accountability frameworks
Regulators must mandate transparency in AI-driven marketing sur-
veillance and detection systems. We recommend establishing compre-
hensive transparency requirements that include regular algorithmic
audits, particularly for systems that monitor or analyse tobacco-related
content on social media and digital platforms. These audits should assess
potential biases in detection algorithms and ensure equal enforcement
across different population groups and tobacco product categories.
Public health authorities should establish clear guidelines for validating
AI-driven cessation tools against established clinical standards before
deployment. This would address the inconsistency in quality noted
across digital cessation applications and ensure alignment with
evidence-based practices. Such validation frameworks should include
minimum performance standards across diverse user populations to
ensure equitable effectiveness.
4.2.2. Ethical data governance
Our findings suggest an urgent need for ethical frameworks gov-
erning data collection and use in AI-driven tobacco surveillance. We
recommend WHO-compliant data governance standards that protect
individual privacy while enabling public health monitoring. These
standards should include explicit informed consent processes, clear
limitations on data use, and appropriate anonymization techniques to
prevent re-identification of individuals. Given the significant privacy
implications of continuous behavioural monitoring, regulatory bodies
should establish specific guidelines for AI applications that track indi-
vidual tobacco use behaviours. These guidelines should address data
minimization principles, storage limitations, and user control over
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
13

personal data, while facilitating legitimate public health surveillance.
4.2.3. Equity and access considerations
To address potential disparities in access to AI-driven cessation tools,
policymakers should ensure equity in digital cessation tool development
and distribution. This includes incentivizing the development of low-
bandwidth applications suitable for regions with limited internet con-
nectivity and supporting the adaptation of AI tools for diverse linguistic
and cultural contexts. Resource allocation for AI implementation should
prioritize underserved communities with high tobacco burden. This
could include dedicated funding for community-based organizations to
adapt and implement AI tools in partnership with local stakeholders,
ensuring culturally appropriate implementation.
4.3. Future research directions
Our review identifies several critical gaps in the current literature
that future research should address to advance the field of AI in tobacco
control.
4.3.1. Methodological Priorities
Longitudinal studies of AI intervention effectiveness represent an
urgent research need. Most current studies employ cross-sectional de-
signs or short follow-up periods, limiting understanding of sustained
impact. Future research should employ robust experimental designs
with extended follow-up periods to assess long-term outcomes of AI-
driven interventions. Greater methodological transparency in AI
implementation is essential. Future studies should provide detailed
reporting of algorithm selection rationales, training data characteristics,
validation procedures, and performance metrics across demographic
subgroups to facilitate reproducibility and comparative evaluation.
4.3.2. Context-specific research
Research in low- and middle-income countries (LMICs) should be
prioritized, given the disproportionate tobacco burden these regions
face. Current applications are heavily concentrated in high-income set-
tings despite 80 % of tobacco users residing in LMICs [6]. Future
research should explore context-appropriate AI implementations that
address unique challenges in these settings, including limited digital
infrastructure and different tobacco use patterns. Industry interference
patterns require more systematic investigation. Given evidence of to-
bacco industry exploitation of AI technologies, future research should
specifically examine how industry actors leverage AI for marketing,
product development, and policy interference to inform targeted regu-
latory responses.
4.3.3. Emerging technology applications
Explainable AI approaches represent a promising direction for
enhancing transparency and trust. Future research should focus on
developing interpretable AI models that can provide clear explanations
for their predictions and recommendations, particularly in clinical and
policy decision support contexts. Real-time intervention systems that
integrate multiple data streams warrant further investigation. Building
on promising work in just-in-time adaptive interventions, researchers
should explore systems that combine physiological, environmental, and
behavioural data to deliver precisely timed cessation support. Genera-
tive AI applications for health communication and education deserve
careful evaluation. As large language models continue to evolve,
research should assess their effectiveness for tobacco education and
behaviour change communication while establishing guardrails against
misinformation.
5. Challenges and limitations
While Artificial Intelligence (AI) offers significant promise for to-
bacco control, several critical challenges and limitations must be
acknowledged and addressed to ensure effective, ethical, and equitable
applications. These challenges include inherent biases and disparities,
privacy concerns and ethical dilemmas related to data usage, issues
surrounding interpretability and transparency, and complexities in data
quality and integration.
5.1. Bias and disparity
One of the most significant limitations of AI applications in health-
care, including tobacco control, is the potential for bias and disparity. AI
models depend heavily on the quality, diversity, and representativeness
of their training datasets. When datasets disproportionately represent
certain populations or exclude minority or vulnerable groups, AI sys-
tems can inadvertently perpetuate or exacerbate existing health dis-
parities [94]. This can lead to unequal access to or effectiveness of
interventions, potentially disadvantaging populations already facing
social or health inequities. Addressing these biases requires careful
dataset selection, inclusive representation, and continuous monitoring
of AI-driven outcomes across diverse demographic groups.
5.2. Privacy and ethical concerns
AI-driven tobacco control tools frequently rely on sensitive personal
data obtained from electronic health records, social media platforms,
wearable devices, and clinical interactions [18,49,56]. The utilisation of
this data raises substantial privacy and ethical concerns. Without robust
governance structures, there is a risk of data misuse, unauthorised sur-
veillance, or breaches that could compromise patient confidentiality and
trust. Additionally, ethical questions arise regarding informed consent
and the boundaries of personal privacy in the context of predictive an-
alytics, behavioural monitoring, and targeted interventions. Ensuring
ethical data management practices, stringent privacy protections, and
clear consent processes are vital to addressing these concerns effectively.
5.3. Interpretability
Many advanced AI models, particularly deep learning algorithms,
function as “black boxes,” making it challenging for healthcare pro-
viders, policymakers, and stakeholders to understand precisely how
predictive decisions or recommendations are derived. The lack of
transparency and interpretability can hinder trust and acceptance
among clinicians, patients, and public health officials, potentially
limiting the adoption and practical application of AI tools. Addressing
interpretability challenges requires advancements in explainable AI
methodologies, fostering clearer, understandable models, and providing
transparency about the data inputs, analytical processes, and decision-
making criteria underlying AI outputs.
5.4. Data quality and integration
The effectiveness and reliability of AI systems are significantly
dependent on the quality, completeness, and consistency of input
datasets. Incomplete, inaccurate, or inconsistent data can severely un-
dermine AI performance, leading to erroneous predictions, inappro-
priate recommendations, or compromised outcomes. Additionally,
integration challenges arise when combining diverse data types from
multiple sources, such as healthcare systems, social media, wearable
devices, or other digital platforms. Effective AI application necessitates
robust data governance frameworks, consistent data standards, rigorous
data cleaning procedures, and advanced methods for harmonising and
integrating heterogeneous data sources to maintain AI reliability and
generalisability.
6. Limitations of the review
While this scoping review provides a comprehensive synthesis of the
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
14

current landscape of artificial intelligence (AI) applications in tobacco
control, several limitations should be acknowledged. First, as a scoping
review, the primary aim was to map the breadth and nature of the
existing literature rather than to assess the quality of evidence or
perform a meta-analysis. Consequently, although informal appraisals of
methodological rigour were undertaken, no formal critical appraisal tool
was applied across studies, and findings should be interpreted
accordingly.
Second, the rapid pace of technological advancement in AI means
that relevant studies may have emerged after the final literature search
was conducted. Despite efforts to include the most up-to-date and rele-
vant sources, some emerging applications or tools may not have been
captured, particularly those in the grey literature or recently published
but not yet indexed. This is particularly relevant in the rapidly evolving
field of generative AI and large language models, where applications
specific to tobacco control are emerging at an accelerating rate.
Third, this review included only English-language publications,
which may have led to language bias and the exclusion of potentially
important studies published in other languages. Given the global burden
of tobacco use, the exclusion of non-English sources may underrepresent
contributions from low- and middle-income countries (LMICs) where
innovative applications of AI may be underreported in the English
literature. This limitation is particularly significant since LMICs bear
approximately 80 % of the global tobacco burden and may benefit most
from cost-effective AI solutions.
Fourth, heterogeneity in study designs, AI methodologies, outcome
measures, and reporting formats made it difficult to standardise com-
parisons or draw definitive conclusions about effectiveness, scalability,
or ethical implementation. Many studies used exploratory or theoretical
approaches rather than real-world evaluations, which limits general-
isability and applicability to policy and practice. This is reflected in the
predominance of proof-of-concept studies and prototype implementa-
tions rather than rigorously evaluated interventions with clearly re-
ported outcomes.
Fifth, the interdisciplinary nature of AI applications in tobacco
control created challenges in comprehensive literature identification.
Studies bridging computer science, public health, psychology, and pol-
icy domains may use varied terminology and be published in diverse
journals, potentially leading to incomplete coverage despite our sys-
tematic search strategy. Additionally, commercial AI applications in
tobacco control may not be publicly documented in academic literature,
creating a potential gap between research and practice.
Finally, our review focused primarily on the beneficial applications
of AI for tobacco control but may not have captured the full extent of AI
misuse by the tobacco industry due to limited transparency in industry
practices. The tobacco industry’s use of AI for marketing, product
development, and policy interference likely exceeds what is documented
in accessible literature, presenting an area for further investigation
through alternative research methodologies such as investigative
reporting and whistleblower accounts.
Despite these limitations, this scoping review represents an impor-
tant first step in systematically documenting the current state of AI ap-
plications in tobacco control and identifying critical gaps in the
literature. Future research should address these limitations through
multi-language reviews, primary research in underrepresented regions,
standardized reporting frameworks for AI interventions in tobacco
control, and innovative approaches to investigating industry use of these
technologies.
7. Conclusion
AI has transformative potential in tobacco control but requires
rigorous ethical oversight. This scoping review has identified diverse AI
applications across surveillance, cessation support, and policy domains,
with substantial promise for extending global tobacco control efforts. AI
has emerged as a transformative force with substantial potential to
revolutionise global efforts in tobacco control. Through innovative ap-
plications, including enhanced surveillance, personalised cessation
support, real-time monitoring, and strategic policy evaluation, AI tech-
nologies provide unprecedented opportunities to proactively address the
complexities associated with addiction and tobacco-related health is-
sues. AI’s capabilities to rapidly process extensive datasets, identify
critical patterns, and predict behavioural risks enable healthcare sys-
tems and public health organisations to design highly targeted, efficient,
and adaptable interventions that align with WHO FCTC implementation
goals.
However, realising the full potential of AI in this critical area of
public health is contingent upon addressing significant challenges and
ethical considerations. Ensuring transparency through explainable AI
models is essential for gaining trust among clinicians, policymakers, and
the public, facilitating widespread adoption and effective implementa-
tion. Moreover, ethical design principles, stringent data privacy mea-
sures, and rigorous governance frameworks must underpin AI
applications to protect vulnerable populations and prevent exacerbation
of existing health disparities. Particular attention must be paid to algo-
rithmic bias, data sovereignty, and protection against industry exploi-
tation of these technologies.
The future success of AI-driven tobacco control strategies also hinges
critically upon effective cross-sector collaboration and global inclusiv-
ity. Partnerships between technology developers, healthcare providers,
public health authorities, community stakeholders, and policymakers
are essential to ensuring that AI tools address real-world needs equitably
and ethically. Additionally, efforts must prioritise data diversity and
representation, particularly from low- and middle-income countries
disproportionately affected by rising tobacco use and emerging tobacco
products. Stakeholders must develop capacity-building initiatives to
empower LMIC researchers to develop contextually appropriate AI so-
lutions while ensuring accessibility beyond high-resource settings.
Overall, AI offers unprecedented opportunities to enhance the
effectiveness, scalability, and responsiveness of tobacco control in-
terventions. Yet, its sustainable and equitable integration into public
health requires careful consideration of ethical standards, comprehen-
sive data representation, transparent methodologies, and collaborative
global efforts. By addressing these critical factors, AI technologies can
significantly contribute to reducing the global burden of tobacco use,
ultimately improving health outcomes and promoting health equity
worldwide. As the tobacco endgame approaches in many countries,
strategic integration of AI within comprehensive tobacco control pro-
grams will be essential for countering industry innovation and achieving
public health goals.
Policymakers and technologists must collaborate to ensure trans-
parency, equity, and alignment with WHO FCTC goals. Funding bodies
should prioritize research that addresses identified gaps, particularly in
LMIC contexts, real-world implementation studies, and frameworks for
ethical AI governance in tobacco control. Through thoughtful develop-
ment and responsible deployment, AI can become a powerful ally in
achieving the WHO’s target of a 30 % reduction in tobacco use by 2025.
CRediT authorship contribution statement
David B. Olawade: Writing – original draft, Writing – review &
editing, Methodology, Project administration, Investigation, Data cura-
tion, Formal analysis, Conceptualization. Charity A. Aienobe-Ase-
kharen: Writing – review & editing, Writing – original draft, Validation,
Methodology, Investigation, Data curation, Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
15

References
[1] World Health Organization, “WHO Framework Convention on Tobacco Control
overview,” Who.int, 2021. https://fctc.who.int/convention.
[2] Union for International Cancer Control (UICC), Tobacco control | UICC,” www.
uicc.org. https://www.uicc.org/what-we-do/thematic-areas/tobacco-control.
[3] J. Chung-Hall, L. Craig, S. Gravely, N. Sansone, G.T. Fong, Impact of the WHO
FCTC over the first decade: a global evidence review prepared for the Impact
Assessment Expert Group, Tob. Control 28 (Suppl 2) (2018) 119–128, https://doi.
org/10.1136/tobaccocontrol-2018-054389.
[4] D.T. Levy, Z. Yuan, Y. Luo, D. Mays, Seven years of progress in tobacco control:
an evaluation of the effect of nations meeting the highest level MPOWER
measures between 2007 and 2014, Tob. Control 27 (1) (2018) 50–57, https://doi.
org/10.1136/tobaccocontrol-2016-053381.
[5] G. Lyle, D. Hendrie, Global smoking-related deaths averted due to MPOWER
policies implemented at the highest level between 2007 and 2020, Globalization
Health 20 (1) (2024), https://doi.org/10.1186/s12992-023-01012-w.
[6] World Health Organization, “Tobacco,” World Health Organization, 2023. https://
www.who.int/news-room/fact-sheets/detail/tobacco.
[7] T. Lancet, Tobacco control: far from the finish line, Lancet 398 (10315) (2021)
1939, https://doi.org/10.1016/S0140-6736(21)02650-7.
[8] T.L.G. Health, Tobacco endgame is closer than we think, Lancet Glob. Health 12
(6) (2024) 890, https://doi.org/10.1016/s2214-109x(24)00194-3.
[9] G. Thomson, R. Edwards, N. Wilson, T. Blakely, What are the elements of the
tobacco endgame? Tob. Control 21 (2) (2012) 293–295, https://doi.org/10.1136/
tc.2010.040881.
[10] D. Olawade, O.A. Bolarinwa, Y.A. Adebisi, S. Shongwe, The role of artificial
intelligence in enhancing healthcare for people with disabilities, Soc. Sci. Med.
364 (2024) 117560, https://doi.org/10.1016/j.socscimed.2024.117560.
[11] H. Ayadi, A. Elb´eji, V. Despotovic, G. Fagherazzi, Digital vocal biomarker of
smoking status using ecological audio recordings: results from the colive voice
study, Digital Biomarkers 8 (1) (2024) 159–170, https://doi.org/10.1159/
000540327.
[12] A. Caccamisi, L. Jørgensen, H. Dalianis, M. Rosenlund, Natural language
processing and machine learning to enable automatic extraction and classification
of patients’ smoking status from electronic medical records, Upsala J. Med. Sci.
125 (4) (2020) 316–324, https://doi.org/10.1080/03009734.2020.1792010.
[13] A. Evans, R. Hughes, L. Nolan, K. Little, L. Newbury-Davies, A.R. Davies, Profiles
of tobacco smokers and ex-smokers in a large-scale random sample survey across
wales: an unsupervised machine-learning cluster analysis, Lancet 402 (Suppl 1)
(2023) 7, https://doi.org/10.1016/S0140-6736(23)02070-6.
[14] D. R. Harris, D. W. Henderson, and A. Corbeau, “Improving the Utility of
Tobacco-Related Problem List Entries Using Natural Language Processing,” in
AMIA. Annual Symposium proceedings. AMIA Symposium, 2021, pp. 534–543.
Available: https://pubmed.ncbi.nlm.nih.gov/33936427/.
[15] H. Hegde, N. Shimpi, I. Glurich, A. Acharya, Tobacco use status from clinical
notes using natural language processing and rule based algorithm, Technol. Health
Care 26 (3) (2018) 445–456, https://doi.org/10.3233/thc-171127.
[16] P. Mamoshina, et al., Blood biochemistry analysis to detect smoking status and
quantify accelerated aging in smokers, Scient. Rep. 9 (1) (2019), https://doi.org/
10.1038/s41598-018-35704-w.
[17] E. L. Palmer, S. Hassanpour, J. P. Higgins, J. A. Doherty, and T. Onega, “Building
a tobacco user registry by extracting multiple smoking behaviors from clinical
notes,” vol. 19, no. 1. 2019. doi: 10.1186/s12911-019-0863-3.
[18] J. Patel, Z. Siddiqui, A. Krishnan, T. Thyvalikakath, Identifying patients’ smoking
status from electronic dental records data, Stud. Health Technol. Inform. 245
(2017) 1281.
[19] J.L.M. Amaral, A.J. Lopes, J.M. Jansen, A.C.D. Faria, P.L. Melo, An improved
method of early diagnosis of smoking-induced respiratory changes using machine
learning algorithms, Comput. Methods Programs Biomed. 112 (3) (2013) 441–454,
https://doi.org/10.1016/j.cmpb.2013.08.004.
[20] O. Fiste, I. Gkiozos, A. Charpidou, N.K. Syrigos, Artificial intelligence-based
treatment decisions: a new era for NSCLC, Cancers 16 (4) (2024) 831, https://doi.
org/10.3390/cancers16040831.
[21] A. Karlsson, et al., Impact of deep learning-determined smoking status on
mortality of cancer patients: never too late to quit, ESMO Open 6 (3) (2021)
100175, https://doi.org/10.1016/j.esmoop.2021.100175.
[22] Q. Ma, Y. Shen, W. Guo, K. Feng, T. Huang, Y. Cai, Machine learning reveals
impacts of smoking on gene profiles of different cell types in lung, Life (Basel,
Switzerland) 14 (4) (2024) 502, https://doi.org/10.3390/life14040502.
[23] S. Muro, et al., machine learning methods for the diagnosis of chronic obstructive
pulmonary disease in healthy subjects: retrospective observational cohort study,
JMIR Med. Inform. 9 (7) (2021) 24796, https://doi.org/10.2196/24796.
[24] X. Wang, et al., An explainable artificial intelligence framework for risk
prediction of COPD in smokers, BMC Public Health 23 (1) (2023), https://doi.
org/10.1186/s12889-023-17011-w.
[25] P. Belsare, V.Y. Senyurek, M.H. Imtiaz, S.T. Tiffany, E. Sazonov, DeepPuff:
Utilizing Deep Learning for Smoking Behavior Identification in Free-living
Environment, in: Annual International Conference of the IEEE Engineering in
Medicine and Biology Society. IEEE Engineering in Medicine and Biology Society.
Annual International Conference, 2023, pp. 1–5, https://doi.org/10.1109/
EMBC40787.2023.10340528.
[26] S. Barbieri, et al., Predicting cardiovascular risk from national administrative
databases using a combined survival analysis and deep learning approach, Int. J.
Epidemiol. 51 (3) (2022) 931–944, https://doi.org/10.1093/ije/dyab258.
[27] A. Khimani, A. Hornback, N. Jain, P. Avula, A. Jaishankar, M.D. Wang, Predicting
cardiovascular disease risk in tobacco users using machine learning algorithms,
in: Annual International Conference of the IEEE Engineering in Medicine and Biology
Society. IEEE Engineering in Medicine and Biology Society. Annual International
Conference, 2024, pp. 1–5, https://doi.org/10.1109/
EMBC53108.2024.10782885.
[28] T. Meeradevi, S. Sasikala, L. Murali, N. Manikandan, K. Ramaswamy, Lung cancer
detection with machine learning classifiers with multi-attribute decision-making
system and deep learning model, Scient. Rep. 15 (1) (2025), https://doi.org/
10.1038/s41598-025-88188-w.
[29] K.-M. Wang, K.-H. Chen, C.A. Hernanda, S.-H. Tseng, K.-J. Wang, How is the lung
cancer incidence rate associated with environmental risks? machine-learning-
based modeling and benchmarking, Int. J. Environ. Res. Public Health 19 (14)
(2022) 8445, https://doi.org/10.3390/ijerph19148445.
[30] Y. Zhan, et al., Identification and validation of the nicotine metabolism-related
signature of bladder cancer by bioinformatics and machine learning, Front.
Immunol. 15 (2024) 1465638, https://doi.org/10.3389/fimmu.2024.1465638.
[31] H. Zhu, B. Chu, C. Zhang, F. Liu, L. Jiang, Y. He, Hyperspectral Imaging for
presymptomatic detection of tobacco disease with successive projections
algorithm and machine-learning classifiers, Scient. Rep. 7 (1) (2017), https://doi.
org/10.1038/s41598-017-04501-2.
[32] E.T. H´ebert, et al., Predicting the first smoking lapse during a quit attempt: a
machine learning approach, Drug Alcohol Depend. 218 (2021) 108340, https://
doi.org/10.1016/j.drugalcdep.2020.108340.
[33] N. Kim, et al., Predictors of adherence to nicotine replacement therapy: Machine
learning evidence that perceived need predicts medication use, Drug Alcohol
Depend. 205 (2019) 107668, https://doi.org/10.1016/j.
drugalcdep.2019.107668.
[34] T. Singh, M. Truong, K. Roberts, S. Myneni, Sequencing conversational turns in
peer interactions: an integrated approach for evidence-based conversational
agent for just-in-time nicotine cravings intervention, Digital Health 10 (2024)
20552076241228430, https://doi.org/10.1177/20552076241228430.
[35] R. Suchting, E. T. H´ebert, P. Ma, D. E. Kendzor, and M. S. Businelle, “Using Elastic
Net Penalized Cox Proportional Hazards Regression to Identify Predictors of
Imminent Smoking Lapse,” vol. 21, no. 2. pp. 173–179, 2017. doi: 10.1093/ntr/n
tx201.
[36] F. Franzwa, L.A. Harper, K.G. Anderson, Examination of social smoking
classifications using a machine learning approach, Add. Behav. (2021) 107175,
https://doi.org/10.1016/j.addbeh.2021.107175.
[37] M.M. Engelhard, et al., Identifying smoking environments from images of daily
life with deep learning, JAMA Netw. Open 2 (8) (2019) 197939, https://doi.org/
10.1001/jamanetworkopen.2019.7939.
[38] E. Cetintas, et al., Characterization of exhaled e-cigarette aerosols in a vape shop
using a field-portable holographic on-chip microscope, Scient. Rep. 12 (1) (2022),
https://doi.org/10.1038/s41598-022-07150-2.
[39] J. Parks, et al., Assessing secondhand and thirdhand tobacco smoke exposure in
Canadian infants using questionnaires, biomarkers, and machine learning,
J. Eposure Sci. Environ. Epidemiol. (2021), https://doi.org/10.1038/s41370-021-
00350-4.
[40] M. Abo-Tabik, Y. Benn, N. Costen, Are machine learning methods the future for
smoking cessation apps? Sensors 21 (13) (2021) 4254, https://doi.org/10.3390/
s21134254.
[41] R. Fu, A. Kundu, M. N, Machine learning applications in tobacco research: a
scoping review, Tob. Control 32 (2023) 99–109.
[42] H. Arksey, L. O’Malley, Scoping studies: towards a methodological framework,
Int. J. Soc. Res. Methodol. 8 (1) (2005) 19–32, https://doi.org/10.1080/
1364557032000119616.
[43] D. Levac, H. Colquhoun, K.K. O’Brien, Scoping studies: advancing the
methodology, Implement. Sci. 5 (1) (2010) 69, https://doi.org/10.1186/1748-
5908-5-69.
[44] L.C. Abroms, A. Yousefi, C.N. Wysota, T.-C. Wu, D.A. Broniatowski, Assessing the
adherence of ChatGPT chatbots to public health guidelines for smoking cessation:
content analysis, J. Med. Internet Res. 27 (2025) 66896, https://doi.org/10.2196/
66896.
[45] S. Amin, C.T. Kawamoto, P. Pokhrel, Exploring the ChatGPT platform with
scenario-specific prompts for vaping cessation, Tob. Control (2023), https://doi.
org/10.1136/tc-2023-058009.
[46] N.C. Atuegwu, C. Oncken, R.C. Laubenbacher, M.F. Perez, E.M. Mortensen,
Factors associated with E-cigarette use in U.S. young adult never smokers of
conventional cigarettes: a machine learning approach, Int. J. Environ. Res. Public
Health 17 (19) (2020) 7271, https://doi.org/10.3390/ijerph17197271.
[47] N.C. Atuegwu, E.M. Mortensen, S. Krishnan-Sarin, R.C. Laubenbacher, M.D. Litt,
Prospective predictors of electronic nicotine delivery system initiation in tobacco
naive young adults: a machine learning approach, Prev. Med. Rep. 32 (2023)
102148, https://doi.org/10.1016/j.pmedr.2023.102148.
[48] H. Bendotti, S. Lawler, G.C.K. Chan, C. Gartner, D. Ireland, H.M. Marshall,
Conversational artificial intelligence interventions to support smoking cessation:
a systematic review and meta-analysis, Digital Health 9 (2023)
20552076231211634, https://doi.org/10.1177/20552076231211634.
[49] R. Benson, M. Hu, A.T. Chen, S. Nag, S.-H. Zhu, M. Conway, Investigating the
attitudes of adolescents and young adults towards JUUL: computational study
using twitter data, JMIR Public Health Surveill. 6 (3) (2020) 19975, https://doi.
org/10.2196/19975.
[50] S. Bhandari, B.C. Yemineni, K. Vadapalli, H. Kundu, A. Arya, R. Laddha,
Leveraging artificial intelligence for effective campaigns against smoking,
J. Pharm. Bioallied Sci. (2024), https://doi.org/10.4103/jpbs.jpbs_1359_24.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
16

[51] W.K. Bickel, et al., Predictors of smoking cessation outcomes identified by
machine learning, A Systematic Review 6 (2023) 100068, https://doi.org/
10.1016/j.addicn.2023.100068.
[52] C. Castillo-Toledo, et al., Regional insights on tobacco-related tweets: unveiling
user opinions and usage patterns, Front. Public Health 12 (2024) 1342460,
https://doi.org/10.3389/fpubh.2024.1342460.
[53] E. Cetintas, et al., Characterization of exhaled e-cigarette aerosols in a vape shop
using a field-portable holographic on-chip microscope, Scient. Rep. 12 (1) (2022),
https://doi.org/10.1038/s41598-022-07150-2.
[54] R. Chow, S. Jama, A. Cowan, S. Pakhale, Artificial intelligence and large language
models for the management of tobacco dependence, Ann. Am. Thorac. Soc. 22 (2)
(2025) 305–309, https://doi.org/10.1513/AnnalsATS.202405-552RL.
[55] K.-H. Chu, J. Colditz, M. Malik, T. Yates, B. Primack, Identifying Key target
audiences for public health campaigns: leveraging machine learning in the case of
hookah tobacco smoking, J. Med. Internet Res. 21 (7) (2019) 12443, https://doi.
org/10.2196/12443.
[56] H. Cole-Lewis, et al., Social listening: a content analysis of e-cigarette discussions
on twitter, J. Med. Internet Res. 17 (10) (2015) 243, https://doi.org/10.2196/
jmir.4969.
[57] L.N. Coughlin, A.N. Tegge, C.E. Sheffer, W.K. Bickel, A machine-learning approach
to predicting smoking cessation treatment outcomes, Nicotine Tob. Res. (2018),
https://doi.org/10.1093/ntr/nty259.
[58] V. Deepika, S. P. Jodalli, and B. R. Anvinash, “The role of chatbots and virtual
assistants in enhancing tobacco cessation services.” 2025. doi: 10.3389/
fdgth.2025.1503227.
[59] S. Elmitwalli, J. Mehegan, G. Wellock, A. Gallagher, A. Gilmore, Topic prediction
for tobacco control based on COP9 tweets using machine learning techniques,
PLoS One 19 (2) (2024) 0298298, https://doi.org/10.1371/journal.
pone.0298298.
[60] S. Elmitwalli, J. Mehegan, A. Gallagher, R. Alebshehy, Enhancing sentiment and
intent analysis in public health via fine-tuned Large Language Models on tobacco
and e-cigarette-related tweets, Front. Big Data 7 (Nov. 2024), https://doi.org/
10.3389/fdata.2024.1501154.
[61] N. English, et al., Image processing for public health surveillance of tobacco
point-of-sale advertising: machine learning–based methodology, J Med Internet
Res 23 (8) (2021) e24408, https://doi.org/10.2196/24408.
[62] J.M. Faro, et al., Effect of a machine learning recommender system and viral peer
marketing intervention on smoking cessation, JAMA Netw. Open 6 (1) (2023)
2250665, https://doi.org/10.1001/jamanetworkopen.2022.50665.
[63] V.E. Georgakopoulou, A. Diamanti, Artificial intelligence for smoking cessation in
pregnancy, Cureus (2024), https://doi.org/10.7759/cureus.63732.
[64] E. Han, M. Biyani, M. Hrywna, S.I. Donaldson, J.-P. Allem, Identifying topics
around nicotine gum: a machine learning approach with twitter data, Subst. Use
Misuse 60 (3) (2025) 430–435, https://doi.org/10.1080/
10826084.2024.2427164.
[65] S. Huang, A. Wahlquist, J. Dahne, Individual predictors of response to a
behavioral activation-based digital smoking cessation intervention: a machine
learning approach, Subst. Use Misuse 59 (11) (2024) 1620–1628, https://doi.org/
10.1080/10826084.2024.2369155.
[66] E. Kasson, A.K. Singh, M. Huang, D. Wu, P. Cavazos-Rehg, Using a mixed methods
approach to identify public perception of vaping risks and overall health
outcomes on Twitter during the 2019 EVALI outbreak, Int. J. Med. Inf. 155 (2021)
104574, https://doi.org/10.1016/j.ijmedinf.2021.104574.
[67] C. J. Kennedy, J. Vassey, H.-C. H. Chang, J. B. Unger, and E. Ferrara, “Tracking e-
cigarette warning label compliance on Instagram with deep learning,” arXiv.org,
2021. https://arxiv.org/abs/2102.04568.
[68] V. Ketonen, A. Malik, Characterizing vaping posts on Instagram by using
unsupervised machine learning, Int. J. Med. Inf. 141 (2020) 104223, https://doi.
org/10.1016/j.ijmedinf.2020.104223.
[69] K. Kim, S. Kim, Large language models’ accuracy in emulating human experts’
evaluation of public sentiments about heated tobacco products on social media:
evaluation study, J. Med. Internet Res. 27 (2025) e63631, https://doi.org/
10.2196/63631.
[70] G. Kong, A.S. Schott, J. Lee, H. Dashtian, D. Murthy, Understanding e-cigarette
content and promotion on YouTube through machine learning, Tob Control 32 (6)
(2023) 739–746, https://doi.org/10.1136/tobaccocontrol-2021-057243.
[71] G. Kong, R. R. Ouellette, and D. Murthy, “Generative artificial intelligence and
social media: insights for tobacco control,” Tob Control, p. tc-2024-058813, Dec.
2024, doi: 10.1136/tc-2024-058813.
[72] H. Küçükali, M.S. Erdo˘gan, AI for tobacco control: identifying tobacco-promoting
social media content using large language models, Nicotine Tob. Res. (2024), https://
doi.org/10.1093/ntr/ntae276.
[73] R. Lakatos, P. Pollner, A. Hajdu, T. Jo´o, A multimodal deep learning architecture
for smoking detection with a small data approach, Front. Artif. Intell. 7 (2024),
https://doi.org/10.3389/frai.2024.1326050.
[74] J. Lee, R.R. Ouellette, D. Murthy, B. Pretzer, T. Anand, G. Kong, “Identifying e-
cigarette content on tiktok: using a bertopic modeling approach,” nicotine &
tobacco research: official journal of the society for research on nicotine and, Tobacco
27 (1) (2024) 91–96, https://doi.org/10.1093/ntr/ntae171.
[75] J. Lee, D. Murthy, R. Ouellette, T. Anand, G. Kong, Identification and
classification of images in e-cigarette-related content on TikTok: unsupervised
machine learning image clustering approach, Subst. Use Misuse (2024) 1–7,
https://doi.org/10.1080/10826084.2024.2447415.
[76] S.-Y. Lin, et al., Social media data mining of antitobacco campaign messages:
machine learning analysis of facebook posts, J. Med. Internet Res. 25 (2023)
42863, https://doi.org/10.2196/42863.
[77] S.-Y. Lin, et al., Public response to federal electronic cigarette regulations
observed through the lens of social media: natural language processing and topic
modelling, J. Med. Internet Res. 26 (2024) 58919, https://doi.org/10.2196/
58919.
[78] K. Loveys, E. Lloyd, M. Sagar, E. Broadbent, Development of a Virtual human for
supporting tobacco cessation during the COVID-19 pandemic, J. Med. Internet Res.
25 (2023) e42310, https://doi.org/10.2196/42310.
[79] N. Minian, et al., AI conversational agent to improve varenicline adherence:
protocol for a mixed methods feasibility study, JMIR Res. Protocols 12 (2023)
53556, https://doi.org/10.2196/53556.
[80] J.K. Pepper, L.V. Zitney, A. Preiss, T. Bukowski, G. Szczypka, A.E. Kim, Can social
media monitoring help identify the next EVALI? An examination of Reddit posts
about vitamin E acetate and Dank Vapes, Drug Alcohol Depend. 230 (2022)
109193, https://doi.org/10.1016/j.drugalcdep.2021.109193.
[81] Y. Ren, D. Wu, A. Singh, E. Kasson, M. Huang, P. Cavazos-Rehg, Automated
detection of vaping-related tweets on twitter during the 2019 EVALI outbreak
using machine learning classification, Front. Big Data 5 (2022), https://doi.org/
10.3389/fdata.2022.770585.
[82] K. Rijhwani, V.R. Mohanty, A. YB, V. Singh, S. Hashmi, Applicability of data
mining and predictive analysis for tobacco cessation: an exploratory study,
Frontiers Dentistry (2020), https://doi.org/10.18502/fid.v17i24.4624.
[83] N.A. Shah, et al., Identification and Characterization of Synthetic Nicotine
Product Promotion and Sales on Instagram Using Natural Language Processing,
in: Nicotine & Tobacco Research: Official Journal of the Society for Research on
Nicotine and Tobacco, 2023, p. 222, https://doi.org/10.1093/ntr/ntad222.
[84] K. Sharp, et al., Generative artificial intelligence and machine learning methods
to screen social media content, PeerJ Computer Science 11 (2025) 2710, https://
doi.org/10.7717/peerj-cs.2710.
[85] P. Sheeran, et al., Artificial intelligence simulation of adolescents’ responses to
vaping-prevention messages, JAMA Pediatr. (2024), https://doi.org/10.1001/
jamapediatrics.2024.0274.
[86] M. Shete, A. Shete, Applied artificial intelligence for tobacco cessation in the Era
of COVID-19: A Perspective, Asian Pac. J. Cancer Prev. 23 (8) (2022) 2551–2552,
https://doi.org/10.31557/APJCP.2022.23.8.2551.
[87] J. Shi, R. Fu, H. Hamilton, M. Chaiton, A machine learning approach to predict e-
cigarette use and dependence among Ontario youth, Health Promot. Chronic Dis.
Prev. Can. 42 (1) (2022) 21–28, https://doi.org/10.24095/hpcdp.42.1.04.
[88] L.N. Siegel, A.V. Levin, E.C. Kranzler, L.A. Gibson, Do longitudinal trends in
tobacco 21-related media coverage correlate with policy support? an exploratory
analysis using supervised and unsupervised machine learning methods, Health
Commun. 37 (1) (2020) 29–38, https://doi.org/10.1080/
10410236.2020.1816282.
[89] L.N. Siegel, K.P. Wiseman, A. Budenz, Y. Prutzman, Identifying patterns of
smoking cessation app feature use that predict successful quitting: secondary
analysis of experimental data leveraging machine learning, JMIR AI 3 (1) (2024)
e51756, https://doi.org/10.2196/51756.
[90] K. Sinha, N. Ghosh, P.C. Sil, Harnessing machine learning in contemporary
tobacco research, Toxicol. Rep. 14 (2024) 101877, https://doi.org/10.1016/j.
toxrep.2024.101877.
[91] J. Vassey, C. J. Kennedy, H.-C. H. Chang, and J. B. Unger, “Generative AI in a new
era of computer model-informed tobacco research: a short report,” Tob Control, p.
tc-2024-058887, Jan. 2025, doi: 10.1136/tc-2024-058887.
[92] A.L. V´azquez, C.M. Navarro, B.H. Garcia, T.S. Barrett, M.M. Domenech, An
ecological examination of early adolescent e-cigarette use: a machine learning
approach to understanding a health epidemic, PLoS One 19 (2) (2024) 0287878,
https://doi.org/10.1371/journal.pone.0287878.
[93] S. K. R. Vuruma et al., “Utilizing Large Language Models to Identify Reddit Users
Considering Vaping Cessation for Digital Interventions.” 2024. doi: 10.48550/
arXiv.2404.17607.
[94] J. Wu, et al., Protecting historically marginalized groups or targeted marketing? A
computational analysis of individuals engaging with public and protected cigar-
branded tweets, Drug Alcohol Depend. 266 (2025) 112516, https://doi.org/
10.1016/j.drugalcdep.2024.112516.
[95] Y. Zhang, J.-P. Allem, J.B. Unger, T. Boley Cruz, Automated Identification of
Hookahs (Waterpipes) on Instagram: an application in feature extraction using
convolutional neural network and support vector machine classification, J. Med.
Internet Res. 20 (11) (2018) 10513, https://doi.org/10.2196/10513.
[96] A. Deb et al., “Social Bots for Online Public Health Interventions,” 2016 IEEE/
ACM International Conference on Advances in Social Networks Analysis and Mining
(ASONAM), pp. 1–4, Aug. 2018, Doi: 10.1109/asonam.2018.8508382.
[97] M. Braun, D. Klingelh¨ofer, D. Brüggmann, D.A. Groneberg, Activity of the tobacco
industry in research and scientific literature, Tob. Use Insights 17 (2024), https://
doi.org/10.1177/1179173x241271566.
[98] P. A. McDaniel and R. E. Malone, “Tobacco industry and public health responses
to state and local efforts to end tobacco sales from 1969-2020,” PLOS ONE, vol.
15, no. 5, 2020, doi: 10.1371/journal.pone.0233417.
[99] T. Asia, “AI Ignites a Tobacco Industry Revolution.” 2024. Available: https://
www.tobaccoasia.com/features/ai-ignites-a-tobacco-industry-revolution/.
[100] C. Platform, “Leveraging Artificial Intelligence in the Tobacco Industry: A Deep
Dive into Altria’s Innovations.” 2023. Available: https://www.cash-platform.
com/leveraging-artificial-intelligence-in-the-tobacco-industry-a-deep-dive-into-
altrias-innovations/.
[101] Reuters, “British American Tobacco to launch synthetic nicotine
pouches,” Reuters, Oct. 16, 2024. https://www.reuters.com/business/retail-
consumer/british-american-tobacco-launch-synthetic-nicotine-pouches-2024-10-
16/.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
17

[102] T. Tactics, “Heated Tobacco Products.” 2024. [Online]. Available: https://www.
tobaccotactics.org/article/heated-tobacco-products/.
[103] S.A. Bialous, S.A. Glantz, Heated tobacco products: another tobacco industry
global strategy to slow progress in tobacco control, Tob. Control 27 (Suppl 1)
(2018) 111–117, https://doi.org/10.1136/tobaccocontrol-2018-054340.
[104] C. Watts, S. Rose, B. McGill, A. Yazidjoglou, New image, same tactics: global
tobacco and vaping industry strategies to promote youth vaping, Health
Promotion Int. 39 (5) (2024), https://doi.org/10.1093/heapro/daae126.
[105] J. J. Nay, “Large Language Models as Corporate Lobbyists.arXiv.org.” 2023.
Available: https://arxiv.org/abs/2301.01181.
[106] E. Savell, A.B. Gilmore, G. Fooks, How does the tobacco industry attempt to
influence marketing regulations? a systematic review, Plos ONE 9 (2) (2014)
87389, https://doi.org/10.1371/journal.pone.0087389.
D.B. Olawade and C.A. Aienobe-Asekharen                                                                                                                                                                                               International Journal of Medical Informatics 202 (2025) 105987
18
