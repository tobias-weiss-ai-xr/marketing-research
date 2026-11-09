---
title: 'Machine and deep learning for personality traits detection: a comprehensive survey and open research
  challenges'
url: https://doi.org/10.1007/s10462-025-11245-3
category: survey
subcategory: empirical
date: 2025-05
venue: Artificial Intelligence Review
authors:
- Anam Naz
- Hikmat Ullah Khan
- Amal Bukhari
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10462-025-11245-3.pdf
pages: 57
chars: 178989
fetched_at: '2026-11-08T17:22:54+00:00'
kb_version: 1
---

# Machine and deep learning for personality traits detection: a comprehensive survey and open research challenges

Accepted: 25 April 2025 / Published online: 9 May 2025
© The Author(s) 2025
Extended author information available on the last page of the article
Machine and deep learning for personality traits detection: a
comprehensive survey and open research challenges
Anam Naz1 · Hikmat Ullah Khan2 · Amal Bukhari3 · Bader Alshemaimri4 · Ali Daud5 ·
Muhammad Ramzan6
Artificial Intelligence Review (2025) 58:239
https://doi.org/10.1007/s10462-025-11245-3
Abstract
Natural language processing (NLP), a prominent research domain of Artificial Intelligence
(AI), analyzes users’ generated content on social media for various purposes like sentiment
analysis, text summarization, chatbots, fake news detection, etc. Recent advancements in
NLP have helped for analysis of human behavior analysis and predicting various human
personality traits. Understanding personality traits has long been a fundamental pursuit
in psychology and cognitive sciences due to its vast applications for understanding from
individuals to social dynamics. Due to online social platforms where people express their
views, experiences and comments, NLP is applied for users’ behavior and personality
analysis, which is helpful in defining marketing strategies, consumers’ behavior analysis,
team building, etc. This research study provides a comprehensive overview of existing
methodologies, applications, and challenges in the field of personality traits detection us -
ing shallow machine learning, ensemble learning and deep learning. To conduct this study,
recent research publications relevant to NLP for this new but emerging research domain
are reviewed. The background knowledge of personality models of various nature is dis -
cussed for better domain understanding. The study encompasses machine learning and
deep learning models with thorough analysis of traditional and innovative techniques in -
cluding ensemble learning and transformer-based models in chronological order highlight -
ing the trend analysis showing evolution of application of advanced methods. The review
also presents and compares the widely used datasets which may guide the researchers for
selection of datasets in future studies. Performance evaluation metrics have been discussed
which are used in the relevant literature. Furthermore, it explores the application of re -
search of personality traits detection in various domains highlighting its significance. We
have also carried out extensive empirical analysis using conventional textual to advanced
deep embedding features and applying machine learning, ensemble learning and deep
learning algorithms. Finally, before conclusion, the review highlights the open research
issues and challenges as potential future directions for the researchers.
Keywords Artificial intelligence · Machine learning · Personality traits · Data analytics ·
Psychological analysis · Natural language processing
1 3

A. Naz et al.
Abbreviations
AI  Artificial intelligence
Bi-LSTM  Bi-directional long short-term memory
BERT  Bidirectional encoder representations from transformers
DT  Decision tree
DL  Deep learning
EEG  Electro encephalo gram
GB  Gradient boost
KNN  K-nearest neighbor
LR  Logistic regression
LSTM  Long short-term memory
MBTI  Myers Briggs type indicators
ML  Machine learning
NLP  Natural language processing
NB  Naïve Bayes
RF  Random forest
SVM  Support vector machine
ViT  Vision transformer
XGB  Extreme gradient boosting
1 Introduction
Understanding human personality is quite a complex and complicated task due to its dynamic
nature and it involves an individual’s characteristics including patterns of thoughts, emo -
tions, and behaviors. Such attributes also define how people behave and interact with each
other as the users in a digital environment using various platforms. Moreover, it also plays
a significant role in shaping human interactions, decision-making, and overall psychologi -
cal well-being (Han et al. 2020). Based on psychology, personality theories have evolved
from trait-based models to frameworks that tries to understand and categorize individual
differences in thoughts, emotions, and behaviors (Feher and Vernon 2021). Over time, these
theories have expanded to include different perspectives extending deeper understanding
of how personality shapes behavior, cognition involving reasoning and social engagement
(Kuchhal et al. 2022). Personality models with different traits show the cognitive level of
individual, the widely used traits are agreeableness, conscientiousness, extroversion, open-
ness, and neuroticism (Ahmad et al. 2020). The study of personality traits is a focus in
psychology and leads to the innovation of different frameworks to understand and catego -
rize these traits (Feizi-Derakhshi et al. 2022). Each of these traits represents a spectrum to
understanding personality differences. The big-five framework is a descriptive model that
many psychologists use to assist in understanding and evaluating personality using Machine
Learning (ML) and Deep Learning (DL) detection. The idea of personality refers to an
individual’s emotions and conduct may both influence how they act (Sikström et al. 2025).
Personality model is a theoretical framework, though personality framework data used to
describe, categorize, and understand human personality traits and behaviors (Nisha et al.
2022). Personality datasets do not directly measure emotional stability or neurotic tenden -
cies. Therefore, the two systems are not directly equivalent, and the mapping should be seen
1 3
239 Page 2 of 57

Machine and deep learning for personality traits detection: a…
as a general precise correlation, that are used as dataset to detect personality traits from
online platforms (Ontoum and Chan 2022). The exploration of personality encompasses
various perspectives, including biological, cognitive, and learning theories and trait-based
approaches. Additionally, it includes the psycho-dynamic and humanistic methodologies in
its study. It has had a great deal of interest in current years because of its potential uses in a
variety of sectors such as healthcare (Ramachandran et al. 2020), marketing-leadership style
(Meskelis and Whittington 2020), political and voting intentions (Zarouali et al. 2024) and
human–computer interaction (Sharan and Romano 2020).
The surge in social media usage in recent years has sparked considerable interest in
automatic personality recognition from online social media (Hassanein et al. 2018) by pre-
dicting user profiles to other group to analyze individual’s data such as behaviors detec -
tion, sentiment analysis and many more (Hayat et al. 2019), also observe the affects during
COVID-19 (Zacher and Rudolph 2021)—(Flesia et al. 2020), by analyzing text, images,
and interaction patterns on Facebook, Twitter, and Instagram. Features such as language
use, post frequency, and network characteristics are examined to infer human behavior rely-
ing on personality traits (Naz et al. 2024a). Different models can manage complex social
networks and unstructured data, learning from textual and visual cues to create nuanced
personality profiles (Qin et al. 2022). A web-based framework is also designed to predict
the different models of personality (Iskandar et al. 2021) with Twitter datasets, developed
using the Software Development Life Cycle framework and combines ML techniques with
feature extraction methods to analyze tweets for personality type prediction (William et al.
2023). Psycho-linguistic features use language model embedding for personality predic -
tion, leveraging the based on various available personality datasets. It highlights a learning
model that outperforms existing methods by blending theory-based text features with auto-
mated learning features, offering new insights into language’s role in personality assessment
(Mehta et al. 2020a).
There is significant interest in developing NLP models capable of autonomously identi -
fying a person’s personality traits for the examination of language use, which is a significant
demonstration of personality characteristics (Pradhan et al. 2020). Due to a lack of learning
from experiences, ML classifications in personality psychology, for handling high-dimen -
sional behavioral data, underscores the potential for more objective and automated person -
ality assessment (Khan et al. 2020). Applying DL to larger data sets markedly boosts the
potential of predictive analysis in decision-making (Rahman et al. 2019). Hence, integrating
AI computational models helps to implement more compatible and flexible framework to
explore personality trait, in various fields. This fusion of AI and psychology brings up new
likelihood for perception of human attitude from grounded theory to computational pow -
ered models in an online ecosystem (Bousalem et al. 2025).
2 Research motivation
The motivation to determine and study the characteristics of personality arises from the
merging of theoretical and practical benefits that are used to understand the complications
of human behavior and emotions as well as the study of their cognitive level. This curios -
ity helps in revealing the facts that help in shaping personality discoveries according to
the individual traits and differences involving their personal thoughts and it focuses on the
1 3
Page 3 of 57 239

A. Naz et al.
mechanism that controls human societal interaction. The application of NLP techniques
helps in prediction of various traits of personality traits of individuals. This analysis of
personality helps in finding proper individuals for marketing purposes, finding customers
regarding products and services (Jie et al. 2022), career counselling (Silpa et al. 2024) and
other aspects of personalization (Sarwoko and Nurfarida 2021). The dramatic changes in
personality research are supported with advancements in computational techniques and an
increase in large data. With the inventions and development in ML algorithms, data driven
models and predictive analysis, they all have brought changes in the study of personality
thus offering unparalleled chances and opportunities in revealing hidden patterns, relation -
ships within a vast number of datasets including social media and digital footprints. In this
scenario exploring personality traits limitation are underexplored including LLM, attention
models, language-based dataset based on existing studies, comparatively explore in Sect. 4,
however detailed analysis of research challenges explored in Sect. 8, ensures that it will
enhance our knowledge and understanding of real-world challenges in all fields.
3 Research questions
The following research questions are to be followed to justify the review context for person-
ality trait detection, and their section-wise answers mentioned in Table 1.
RQ1: Which ML Models are more suitable for Personality Traits detection in online
textual content?
RQ2: Which DL Models are more appropriate for Personality Traits detection in online
textual content?
RQ3: How do diverse features and machine learning based models impact the accuracy
of personality trait prediction?
RQ4: What are the features and source of available dataset on personality trait prediction?
RQ5: What are the most potential application areas for AI-based personality trait predic-
tion and how do they impact various fields?
RQ6: What are the main open research challenges and their applicable strategies to be
employed to address these issues?
Research questions Answers
RQ1 Section 4; Heading 4.2: Review of Existing
Studies using Machine Learning Models
RQ2 Section 4; Heading 4.3: Review of Existing
Studies using Deep Learning Algorithms
RQ3 Section 6: Experimental Results
RQ4 Section 7; Datasets
RQ5 Section 8; Applications
RQ6 Section 9; Open Research Issues
Table 1 Relating section for
answers to research questions

1 3
239 Page 4 of 57

Machine and deep learning for personality traits detection: a…
4 Research contributions
The implications of personality traits research need a comprehensive study for future
researchers, and practitioners get to know more about the intersection of personality psy -
chology and computational methodologies. After evaluating the existing studies, the follow-
ing review provides the following contributions including:
 ● Established a novel framework that integrates psychological theories with computa -
tional linguistics, enabling the development of more contextually aware and psycho -
logically informed NLP models for personality detection in textual data.
 ● Discussed a detailed knowledge of personality traits, its model, and relevant background
information of data processing along with features and computational models.
 ● Carried out a brief discussion on identification of methodological trends regarding ML
and DL models along with perspective of state-of-the-art models.
 ● Conducted a comparative analysis of existing studies with our findings based on empiri-
cal analysis to define the contribution of this review.
 ● Provided a comprehensive analysis of key datasets with availability source and learning
models also discusses performance measures.
 ● Examined a brief and quick discussion on potential applications of personality traits in
various fields.
 ● Explored open research challenges can serve as future research directions for the re -
searchers in this new and active domain.
4.1 Comparison with existing relevant review articles
In this literature, comparison presented to show the current literature on personality trait
detection has evolved across multiple dimensions, identifying both advancement and gaps
spanning from 2020 to 2024 based on numerous studies have explored various ML and NLP
to predict traits from textual data, the majority have primarily relied on only ML and DL
approaches with minimal list of multimodal data including text, image, audio, and video.
However, the potential of NLP review focused on textual data, which capture semantic and
contextual information of text, remains a gap in this domain. One significant limitation
observed in the existing literature on personality traits prediction is the dearth of literature
leveraging computational models with background information including analysis of fea -
tures and preprocessing techniques to integrate with psychology lens. Moreover, incorpora-
tion of psychological models also varies. While some studies, one of them from 2020, lack
detailed discussion on personality models, our survey article thoroughly integrates them,
reflecting the growing recognition of psychological theories in computational personality
detection. Therefore, the absence of research integrating represents a notable gap in cur -
rent literature, prominence the need for future investigations to discover this advanced text
representation approach for more accurate personality traits model prediction, we conduct
a systematic literature review by covering all aspect into one article including background
detail of psychological personality model as well as computational models. A key observa-
tion is the count of discussed text datasets, with earlier studies tending to focus on fewer
datasets ranging from 2 to 5, whereas the 2024 survey dataset finds 14 textual datasets
with their source link for accessibility, suggesting more extensive datasets exploration. Fur-
1 3
Page 5 of 57 239

A. Naz et al.
thermore, we discuss research challenges, significance of literature with motivations, and
applications also covered. All studies address minimal exploration of applications and chal-
lenges, in contrast, our 2024 survey provides a comprehensive analysis of complexities in
personality detection research. A detailed analysis with the help of Table 2 shows our work
and research gap by comparing existing studies.
The paper is following the structured as. Section 2 presents experimental setup and data
acquisition. Section 3 discusses personality models. Section 4 investigates the existing stud-
ies with machines and deep learning algorithms that are being used for detecting personality
traits, also highlights the feature engineering strategies in the context. Section 5 provides
analysis of evaluation metrics. Section 6 shares the analysis of experimental results and
discussion using various ML and DL models. Section 7 describes the publicly available
datasets that exist in the personality domain. Section 8 analyses the most relevant real-world
applications. Section 9 highlights the current research issues. Section 10 briefly answers the
research questions, Lastly, Sect. 11 concludes our paper. The mind map diagram of review
article as shown in Fig. 1.
5 Research plan and search strategy
This systematic review article aims to inclusive examine and categorize the most effica -
cious techniques, measures, tools, and classifying methods for predicting personality traits.
Detailed experimental setup and methodology will be used to synthesize existing accom -
plishments in the field of personality trait prediction. By observing primary studies, we
aim to identify and classify the different range of methodologies and approaches used for
predicting traits. The review process will not only merge current understanding but also spot
research challenges, providing intuition for future investigations (MacFarlane et al. 2022).
To orderly gather relevant data samples for the review on personality trait prediction, a thor-
oughly organized search strategy is used. This study conducted based on the last five-year
literature published in well-reputed top journals, shows the exploration encloses a variety
of sources, including academic research papers, case studies, and references from related
publications. Additionally, an examination of related websites specializing in personality
psychology, psychological evaluation and research institutions is obtained. The methodol -
ogy extends to incorporating government reports and statistics, akin to the utilization of
models. The search process is not only confined to academic literature but also involves an
exhaustive review of reference lists from identified publications. The keywords used for the
search are keenly selected to ensure a comprehensive extraction of information related to
personality behavior prediction. By adopting the systematic approach described in Table 3,
the aim is to get meaningful stats from a diverse collection of sources, ensuring the inclusion
of worthy perspectives and methodologies in the detailed review of personality trait predic-
tion studies. The search string for personality trait prediction studies can be constructed as
follows:
 ● (Personality ∗ OR MBTI ∗) AND (Prediction ∗ OR Detection ∗)
 ● (Psychological ∗ OR Psychometric ∗) AND (Personality ∗)
 ● (Behavioral ∗ OR Psychological ∗) AND (Prediction ∗ OR Assessment ∗)
 ● (Trait ∗ OR Sentiment ∗) AND (Machine Learning ∗ OR Predictive Modeling ∗)
1 3
239 Page 6 of 57

Machine and deep learning for personality traits detection: a…
Table 2 Analysis of proposed literature with existing studies
References Year Methodology of existing studies Computational background discussion Person-
ality
models
Datasets Applications RQ Research
challengesML Ensemble DL Transformer Pre-processing Features Models Evalu-
ation
measures
Ahmad et al.
(2020)
2020 ✓ x ✓ x x X x x ✓ 4 x ✓ ✓
Mehta et al.
(2020b)
2020 ✓ x ✓ x x X x x x 5 ✓ x x
Feher and Ver-
non (2021)
2021 x x x x ✓ ✓ x x ✓ 2 x ✓ x
Feizi-Derakhshi
et al. (2022)
2022 ✓ x ✓ x x ✓ x ✓ x 5 x x x
William et al.
(2023)
2023 x x x x ✓ ✓ ✓ x x 2 x ✓ ✓
Singh and
Singh (2024)
2024 x x ✓ x x X ✓ x x 2 ✓ x ✓
This study – ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ 14 ✓ ✓ ✓
1 3
Page 7 of 57 239

A. Naz et al.
 ● (Psychological ∗ OR Personality ∗) AND (Classification*)
 ● (Trait ∗ OR Behavioral ∗) AND (Text Analysis ∗)
Below search string captures a wide range of studies related to personality trait prediction,
including those employing psychological, behavioral, and ML approaches. The use of vari-
ous terms ensures a comprehensive exploration of literature in the domain.
In our preliminary investigation on databases such as IEEE Explore, Springer, DBLP,
ACM, MDPI, and Google Scholar we conducted an exhaustive search for personality trait
prediction studies. The initial search yielded a pool of 305 research papers. Through a metic-
ulous screening process based on duplication and titles, we selected 270 papers deemed
relevant to study. Subsequently, a thorough analysis of the abstracts led to the identification
of an exclusion of 184 research papers. These extracted papers experienced a comprehen -
sive review, resulting in the final of 171 papers as the primary focus of our research. The
entire selection procedure delineated in Fig. 2. The comprehensive analysis of the selected
research papers involves a rigorous assessment of their quality. Quality control questions,
including the research domain and publication in reputable journals or conferences, and
keywords selection (Liu et al. 2021), are employed to examine the credibility of the selected
studies. Systematic research follows a structured approach in assessing the many method -
ologies employed for personality behavior prediction. The inclusive categorization is based
on prediction algorithms, psychological frameworks, and the combination of machine, deep
or hybrid approaches to learning techniques. A tabular summary expresses the characteris -
tics of existing personality trait prediction systems provided. The research strategy guiding
our study is systematically addressed through a diligent review of the selected papers. Addi-
tionally, the potential and limitations of the studies are critically evaluated and suggestions
for future work directions are formulated. The extensive inquiry intends to contribute to
the current body of information on personality trait prediction as well as provide fantastic
insights for both scholars and practitioners in the field.
6 Relevant background: personality models
Personality models present as frameworks to understand and classify human traits, behav -
iors, and tendencies, offering incredible insights into individual differences to psychological
personality measures (Oravecz et al. 2020). Here, we explore some of the personality views
investigated in the relevant literature. The following models are followed in context of psy-
chology encompassing fundamental concepts and methodologies essential for developing
and evaluating the framework. Incorporating these models alongside other well-established
frameworks as illustrated in Table 4, enriches our understanding of the diverse and multifac-
eted nature of human personality by highlighting each trait focus characterized by high level
and low-level score. Each behavior falls into multiple models as mapped in table, plays a
significant role in shaping individual behavior and interactions with others. The high levels
often indicate a more pronounced expression of the trait, leading to specific behavior that
reflects that intensity, while the low-level score typically represents a more subdued or con-
trasting approach. This framework provides a concise overview of how these traits influence
personality, decision-making, and interpersonal dynamics.
1 3
239 Page 8 of 57

Machine and deep learning for personality traits detection: a…
6.1 MBTI model
One broadly useful model is the Myers-Briggs Type Indicator, which distinguishes sixteen
well-defined personality types consisting of four divisions: judging/perceiving, extrover -
sion/introversion, sensing/intuition, and thinking/feeling. Each personality is defined by a
unique four-letter code such as INFJ or ESTP, reflecting these preferences. The widely used
model in various fields, including psychology, counselling, and organizational behavior to
understand and predict the individual differences in behavior, decision-making, and inter -
personal interactions that how they perceived the world and preferences (Butt et al. 2025).
6.2 Big five model
Also familiar as the Five-element Model, shows another dominant model, encompassing
neuroticism, agreeableness, extroversion, conscientiousness, and openness. Each dimension
represents a spectrum, with individuals falling at various points along each continuum. The
model gives an inclusive and widely acquired framework for assessment and categorizing
personality attributes along these five ways (Mayer and Bryan 2024).
6.3 HEXACO model
The model maintains human personality distilled into six dimensions, admits cultural varia-
tions in personality. The model provides a more understanding of personality by incorpo -
rating the dimension of honesty and humility, which influences interpersonal and ethical
concern. This model map to six personality traits such as Honesty-Humility, Emotionality,
Extroversion, Agreeableness, Conscientiousness, Openness. Each of these model traits put
up atomically to the concern of human personality, allowing researchers to find out the rich-
ness and complexity of individual variance in many contexts (Ashton et al. 2024).
Fig. 1 Structure of survey paper

1 3
Page 9 of 57 239

A. Naz et al.
6.4 PEN model
Also called the Psychoticism-Extroversion-Neuroticism model, enlarges the Big Five Per -
sonality behavior by embodying a dimension of Psychoticism traits such as aggression,
impulsiveness, and sensation-seeking. Therefore, in the PEN model, ones are evaluated on
three main perspectives: Psychoticism, Extroversion, and Neuroticism. The model gives
a subtlety understanding of personality by incorporating traits related to risk-taking, and
emotional stability (Netter et al. 2021).
6.5 DISC model
On the contrary, targets observable behavior in various perspectives. DISC represents four
main personality traits: Dominance, Influence, Steadiness, and Conscientiousness. Individ-
Search Set of Keywords
Personality* Personality, personality behavior, personality
behavior techniques, personality model
MBTI* MBTI, MBTI indicators, MBTI classification,
MBTI detection
Prediction* Personality trait prediction, Sentiment
prediction
Big five* Big five personality, big five classification, big
five and social media
Detection* Detect personality traits, personality detection
techniques
Psychological* Psychological parameters, psychological mea-
sures, psychological conditions
Psychometric* Psychometric parameters, psychometric mea-
sures, psychometric conditions
Behavioral
assessment*
Behavioral prediction, behavioral impact
Sentiment* Sentiment analysis, sentiment factors, senti-
ment text prediction
Machine learning* Machine learning techniques for personality
profiles, machine learning methods for detect-
ing traits, Machine learning algorithms for
recognizing sentiment prediction
Predictive
modeling*
Predictive modeling of personality effects,
predictive modeling in psychology, predictive
modeling for trait identifications
Classification* Classification models for psychological traits,
classification techniques for trait identification,
Classification-based personality assessment,
classification frameworks for personality, clas-
sification algorithms for personality
Text analysis* Text and behavioral analysis of personality, text
analysis of personality trends, text analysis:
personality classification, text analysis of
personality insights
Predictive
analytics*
Predictive analytics-driven trait detection, pre-
dictive analytics in psychological profiling, pre-
dictive analytics for personality categorization
Table 3 Search strategy and
formulation

1 3
239 Page 10 of 57

Machine and deep learning for personality traits detection: a…
uals are categorized based on their dominant traits, shown in four basic personality styles:
Dominant, Influential, Steady and Conscientious. The DISC model is often used in organi -
zational and leadership contexts to enhance communication, team dynamics, and personal
development by recognizing and adapting to different behavioral styles (Meliá et al. 2024).
7 Review of existing studies
In this section, a comprehensive review of existing studies on personality detection, focus -
ing on two main domains: firstly, present review of data collection and preprocessing,
feature engineering including textual and word embeddings that directly impact model per-
formance, demonstrating the basic steps of this methodology. Secondly, the application of
ML techniques including ensemble models, and lastly, the exploration of utilizing DL algo-
rithms including state-of-the-art transformer-based models for the detection of personality
traits, as taxonomy of models’ study shown in Fig. 3.
7.1 Pre-processing of data for model application
During data acquisition, preprocessing is a critical step in personality detection studies, as
the quality and diversity of the data directly impact model performance. After data collec -
Fig. 2 Flow of dataset search and selection procedure

1 3
Page 11 of 57 239

A. Naz et al.
Trait Models High score focus Low score
focus
Openness HEXACO,
Big Five,
MBTI
Curious
Imaginative
Open to new ideas
Intuitive
Practical
Prefer
Routine
Conserva-
tive in
Thinking
Sensing
Conscientiousness HEXACO,
Big Five,
DISC,
MBTI
Organized
Responsible
Goal-Oriented
Judging
Flexible
Spontane-
ous
Less
Structured
Perceiving
Extroversion HEXACO,
Big Five,
MBTI, PEN
Energetic
Sociable
Enthusiastic
Extrovert
Reserved
Introspec-
tive
Prefers
Solitude
Introvert
Agreeableness HEXACO,
Big Five,
MBTI
Compassionate
Cooperative
Trustworthy
Thinking
Competitive
Skeptical
More
Critical
Feeling
Neuroticism Big Five,
PEN
Emotionally
Reactive
Prone to stress
Calm
Emotion-
ally Stable
Resilient
Honesty-Humility HEXACO Sincere
Modest
Fair-minded
Self-Cen-
tered
Mislead
Emotionality HEXACO Sensitive
Empathetic
Logical
Detached
Dominant DISC Confidence
Assertive
Takes Charge
Passive
Prefer
Supportive
Role
Influential DISC Persuasive
Motivating
Charismatic
Direct
Factual
Less
Persuasion
Steady DISC Reliable
Patient
Supportive
Adaptable
Less
Routine-
Focus
Prefer
Changes
Psychoticism PEN Impulsivity
Aggressiveness
Less Empathetic
Risk-Taking
Unconventionality
Empathetic
Cooperative
Conven-
tional
Respect
Societal
Norms
Table 4 Personality models and
traits with behavior description

1 3
239 Page 12 of 57

Machine and deep learning for personality traits detection: a…
tion, preprocessing steps have been taken to clean and filter the data, mentioning issues like
mislaid values, and variability. The personality dataset is the base for predicting individuals’
personalities through their posts and comments via extracting from social media. Before
using feature extraction and selection algorithms, the dataset undertakes preprocessing. The
extracted features are then trained using data mining approaches until prime accuracy is
gained (Ishfaq et al. 2025).
Data preprocessing is the process of preparing raw data into a suitable format for pro -
cessing, analysis, and implementation. Data preprocessing aims to improve quality of data,
removal of noise, and make the data more understandable and reusable for other tasks, may
involve techniques to fix noise or misleading values in dataset like often unfairly, filtering
or removing borders. To clean text data from URLs, emojis, emoticons and special symbols
from data (Wang et al. 2021). Splitting text into single units as tokens or words for fur -
ther analysis, could be done using whitespace, punctuation, or more sophisticated methods.
Once the text is tokenized, stop words, which are common words that typically do not carry
significant meaning for analysis (e.g., “the”, “is”, “and”), are removed from the tokenized
text that helps to reduce noise and focus on the more meaningful words in the text (Palo -
mino and Aider 2022).
Converting text to a uniform case (lowercase), and standardizing variations of words to
their base or root form to ensure consistency in representation involving techniques like
stemming or lemmatization. The process involves removing suffixes or prefixes from words
to obtain their root forms, which may not always be lexicographically correct but can be
useful for tasks like search or text analysis where variations of words should be consid -
ered equivalent. Lemmatization to reduce words to their base or dictionary form, known as
the lemma. Unlike stemming, which applies heuristic rules to truncate words to their base
forms, lemmatization uses vocabulary and morphological analysis to obtain the correct base
form of words, making it easier to analyze and interpret text data, especially in tasks related
to sentiment analysis, personality assessment, and behavioral profiling (Nesca et al. 2022).
Fig. 3 Taxonomy of existing studies

1 3
Page 13 of 57 239

A. Naz et al.
7.2 Feature engineering
Personality trait detection using classification techniques further explored using feature
engineering techniques to extract and analyze meaningful data from large volume of dataset
by applying various models of ML and DL. This technique helps to understand the textual
and word-based relationships between sentences and individual text (Ahmed et al. 2022). It
is essential to identify which text features are most important to improve performance with
vectorization for converting text into numeric that algorithms can understand and process.
Features are divided into two parts, text features, and word embeddings.
7.2.1 Text features
The method of representing words as dense vectors in a high dimensional space from NLP,
refers to as text embedding, used to capture the contextual and semantic data about text,
by enabling ML models to process and predict the language words more effectively. The
Bag of Words (BoW) technique takes out unique words from text data. Each word is then
represented as an independent and specific feature. BoW treats words separately. Term Fre-
quency Inverse Document Frequency (TF-IDF) represents the attribute of personality types.
Term Frequency (TF) indicates the repetition of each word in a document, while Inverse
Document Frequency (IDF) manifests the presence of documents containing a specific word
(Alarfaj et al. 2023). An N-gram is a sequence of N contiguous items in a text or speech
sample to analyze the frequency and distribution of words or characters. In N-gram mod -
els,” N” corresponds to the number of items in the sequence, which can be words, or charac-
ters. POS tagging is the process of labeling each word by assigning matching part of speech
such as noun, verb, adjective etc. to words in a text data corpus. This helps in understanding
the grammatical structure of context of the text (Khan et al. 2019).
7.2.2 Word embeddings
Word embeddings capture semantic links between words by replacing them in a space
where similar words are closer together. Embedding approach allows for the finding of
semantic similarities and contextual information within words, converting raw text data into
organized and representations that facilitate more understandable language. Word embed -
dings are generated using algorithms like Word2Vec, GloVe, and Fast Text, which examine
massive amounts of text data to learn meaningful prediction of words (Sandu et al. 2024).
Word2Vec embedding approach that teaches different depiction of words. It is built on
neural networks and is trained to investigate the context of words within a given frame of
text. Word2Vec finds semantic links between words. GloVe is another word embedding
technique. Its aim is to learn word depiction by considering global word repetition stats. It is
based on word vectors by factorizing a matrix of word repetition counts. GloVe embeddings
use both semantic and syntactic information. Fast Text that considers sub word information
represents words as bags of character n-grams and learns embeddings for both words and
sub-words. Fast-Text is particularly useful for processing out-of-vocabulary words (Naqvi
et al. 2023).
1 3
239 Page 14 of 57

Machine and deep learning for personality traits detection: a…
7.3 Literature review using machine learning
Sentiment analysis is increasingly recognized as a cutting-edge area within AI (Babu and
Kanaga 2021). The objective of the field, effective computation, is to revolutionize and
apply emotional reasoning techniques for predicting emotions across different languages
(Escalante et al. 2022). The goal is to develop and predict a system capable of eliciting intui-
tive and emotional reactions by analyzing and converting quantifiable human elements like
emotions, personality characteristics thoughts, and moods into meaningful insights (Talaat
et al. 2023). The text illustrates the meaningful role of ML in presenting a method for pre -
dicting personalities, thereby deepening our understanding of human behavior (Novikov
et al. 2021). Specifically, it points out the superior performance of the Gradient Boost -
ing model, underscoring its practical value in fields like recruitment (Nirmala et al. 2024),
Hate-speech analysis (Canbay 2024), team building, and personalized marketing (Chen et
al. 2023).
Predicting personality traits using ML involves leveraging various algorithms to analyze
patterns and relationships within data illustrated in Fig. 4. Machine learning algorithms
utilize data and algorithms to train the model with the help of data and perform operations
without explicit instruction. Automated personality assessment in areas like cyberbullying
detection, enhanced personal assistants, specialized healthcare, and career counseling have
significant studies that have employed various algorithms and computational techniques
for personality assessment using social media data, including, Support Vector Machines
(SVM), Naïve Bayes (NB), Logistics Regression (LR), Random Forest (RF), Extreme Gra-
dient Boosting (XGBoost) and K-Nearest Neighbor (KNN) (Bruno and Singh 2022).
Here are frequently used ML algorithms for personality trait prediction based on literature:
7.3.1 Shallow machine learning
Shallow ML models refer to traditional ML models that have a small number of layers in
their architecture. These models are often used for simpler classification and regression
tasks and are commonly easier to interpret and understand but more intricate with complex
patterns and high-dimensional data. Table 5 shows the analysis of existing studies used
for personality traits detection using shallow ML. SVM and MNB methods demonstrate
the significant correlation between behavioral tendencies among Twitter data (Cahyani and
Faishal 2020), expanding data sources through Facebook exploring additional personal -
Fig. 4 Basic steps of a typical ML process

1 3
Page 15 of 57 239

A. Naz et al.
ity parameters, and integrating experts at logical insights for deeper analysis (Safari and
Chalechale 2022) utilizing word embeddings and supervised learning models to analyze
tweets and compute personality traits (Carducci et al. 2018). K-Mean clustering on MBTI
(Talasbek et al. 2020), the NB classifier focused on the personality model based on tweet
datasets (Safari and Chalechale 2022) demonstrates the new classifier for traits prediction
of non-playable characters in visual novel games, utilizing the indicator for personality
classification, the study develops text-based classifiers to categorize non-playable character
dialogues (Pretty et al. 2024). The regression model was designed to reduce the value of
personality features (William and Badholia 2021).
Using audio wave to detect the personality pattern from Electro Encephalo Gram (EEG)
signals offers a new direction for research in the fields of neuroscience, psychology, and AI
(Annisa et al. 2020). Another predicting personality perspective features are configured to
evaluate the students’ performance in academic store to detect the traits using decision tree
with notable accuracy rate (El-Keiey et al. 2022). Moreover, the Apache spark platform was
utilized for implementing different ML models training to detect the behavior of user for
perceiving personality from tweets using word embedding techniques (Orynbekova et al.
2021) obtaining inter-dependency degrees of various personality features as trait prediction
based on data dimensions in digital platforms (Choi 2021).
References Year Models Features Platform Dataset
Carducci et
al. (2018)
2018 SVM,
LR,
LASSO
LIWC Facebook My per-
sonality
Cahyani
and Faishal
(2020)
2020 SVM,
NB
TF-IDF Twitter Self-
created
Talasbek et
al. (2020)
2020 k-means
cluster-
ing
Text
features
Google
forms
Question-
naires
Setiawan
and Wafi
(2020)
2020 NB TF-IDF Twitter Self-
created
Annisa et
al. (2020)
2020 EEG-
SVM
Text
features
User’s brain
record
ASCER-
TAIN
Oryn-
bekova et
al. (2021)
2021 SVM,
NB,LR
TF-IDF Twitter MBTI
Safari and
Chalechale
(2022)
2022 DT,
MLP,
KNN
Text
features
Facebook My per-
sonality
El-Keiey et
al. (2022)
2022 SVM,
NB, RF,
LR
Text
features
Twitter MBTI
Sharon et
al. (2023)
2023 SVM,
RF, LR
Text
features
Google
forms
Question-
naires
Kaliap-
pan et al.
(2024)
2024 SVM,
DT
Text
features
Blogs Online
forum
Table 5 Summary of existing
studies of shallow machine
learning

1 3
239 Page 16 of 57

Machine and deep learning for personality traits detection: a…
7.3.2 Ensemble learning
Ensemble Learning is an ML method that combines many models to enhance the overall
performance and predictive accuracy of the system. The main idea at the back of the ensem-
ble studying is to leverage the collective intelligence of more than one model instead of
relying on a single model. Learning algorithms includes bagging (Random Forest, Logistics
regression), stacking, and boosting (Adaboost, XGBoost). Table 6 is the analysis of existing
studies used for personality traits detection.
The boosting ensemble classifier XGBoost (Amirhosseini and Kazemian 2020) is used
to predict personality traits based on MBTI model using textual features such as TF-IDF on
text dataset (Khan et al. 2020) providing a base for potential applications in organizational
environment for recruiting and other domain services (Kamalesh and Bharathi 2022). Per-
sonality traits from social media conversations, employing supervised ML algorithms to
assess traits, utilized feature extraction methods like TFIDF, GloVe, and BoW (Cherukuru
et al. 2022), with TFIDF showing notable accuracy improvements on a dataset that finds that
KNN, RF, and XGBoost algorithm utilized in personality prediction (Garg and Garg 2021).
References Year Models Feature Plat-
form
Dataset
Amirhosseini
and Kazem-
ian (2020)
2020 XGBoosting,
RNN
TF-IDF Twitter MBTI
Mushtaq et
al. (2020)
2020 XGB, SVM,
LSTM
TF-IDF Twitter MBTI
Choi (2021) 2021 NB, RF, XGB TF-IDF Twitter MBTI
Choong and
Varathan
(2021)
2021 LightGBM,
SVM, LR
TF-IDF Social
media
café
forum
Shafi et al.
(2021)
2021 RF, DT, KNN Text
Features
Twitter MBTI
Khan et al.
(2020)
2022 XGB, SVM,
LR, RF, MLP,
KNN
N-Gram,
BoW
Twitter MBTI
Kamalesh
and Bharathi
(2022)
2022 XGB, SVM,
LR, RF
TF-IDF,
BoW
Twitter per-
sonal-
ity
Cherukuru et
al. (2022)
2022 XGBoost, LR,
RF
TF-IDF Twitter Essays
Garg and
Garg (2021)
2022 SVM, DT,
KNN, LR, RF,
XGB
BoW,
GloVe
Twitter MBTI,
Twitter
Zhang et al.
(2023)
2023 BERT + PSYL-
ING, XGB
TF-IDF Social
media
Es-
says,
MBTI
Sai (2023) 2023 LR, SVM,
NB, RF
POS Twitter MBTI
Kishima et al.
(2021)
2023 LightGBM Word2Vec Online
websites
Con-
versa-
tion
Serrano-
Guerrero et
al. (2024)
2024 BERT, XGB,
SVM, LR, RF,
MNB
BoW,
Glove,
TF-IDF
Face-
book
Per-
sonal-
ity
Table 6 Summary of existing
studies of ensemble learning

1 3
Page 17 of 57 239

A. Naz et al.
The ensemble model based on the kernel soft voting system was developed, which inves-
tigated different SVM kernels such as the radial basis function to select the most efficient
point for personality recognition (Kumar et al. 2023). Moreover, judging-perceiving map-
ping in the dataset by utilizing character-level and word-level TF-IDF, along with features
of Linguistic Exploration and Word Count (Choong and Varathan 2021). The data and clas-
sification level fusion and transfer learning from pre-trained language models were used in
automated personality recognition from text integration with ensemble boosting algorithm
GB to distilled version of BERT, for personality detection on Reddit (Julianda and Maharani
2023) discussing the challenges of imbalanced data and the effectiveness of various ML
models, including XGBoost, SVM, and BERT (Bin Tareaf 2022).
Embeddings from Language Models, and Universal Language Model Fine-tuning in per-
sonality classification (Santos and Paraboni 2022) was evaluated on the dataset, and both
annotated the big five personality traits, where bagging algorithm notably excelled in identi-
fying traits like extroversion, conscientiousness, and openness (El-Demerdash et al. 2022).
Psychological analysis (Zhang et al. 2023), the intersection of guidance and AI applying
stacked ensemble techniques of deep learning DNN with boosting models (Serrano-Guer -
rero et al. 2024), highlighting the practical applications of ML in personal development
and career planning (Fatima et al. 2022), curriculum vitae (Singh et al. 2023) analysis,
highlighting the potential of various models in personality type prediction with high accu -
racy and efficiency of the Ensemble Bagged Trees algorithm (Shafi et al. 2021). Ensemble,
unsupervised ML model utilizing models with feature selection PCA technique(Sai 2023)
and others aimed at predicting personality characteristics by analyzing social media subjects
in non-English languages (Alsubhi et al. 2023) with the One-Hot encoding technique focus-
ing on the role of personality traits in guidance (Ryan et al. 2023). Advanced techniques
for classification using LightGBM integrate with word embedding such as Word2Vec and
Sentence BERT for feature extraction (Kishima et al. 2021). Application of ML and DL in
detecting the personalities by applying k-Means Clustering with XG boosting gives better
accuracy than NB (Mushtaq et al. 2020).
7.4 Literature review using deep learning
The subset of ML that handles complex patterns and structure of data with various layers
of neural network to process huge data using multiple feature selection techniques required
high computational training resource. Deep Models include Deep Belief Networks (DBN),
Convolutional Neural Networks (CNN), Long-Short Term Memory (LSTM), Artificial
Neural Networks (ANN), Gated Recurrent Unit (GRU) and Recurrent Neural Networks
(RNN), and have outperformed in various domains (Mehta et al. 2020b). An analysis of how
different ML and DL methods, including supervised, unsupervised, and hybrid approaches
(Rahman and Halim 2022), can effectively categorize the personality traits based on text
multiclass classification by considering part of compound group labels as concerned ele -
ments (Cerkez et al. 2021). For psychological analysis deep learning models such as LSTM,
RNN, GRU and Bi-LSTM utilized to capture users’ profiles from digital platform (Sujatha
et al. 2023) and provides a future direction in text classification to detect different pattern
including personality trait detection (Salminen et al. 2020). Here is a brief overview of exist-
ing studies based on sequential models and state-of-the-art transformer-based model used
for personality detection task.
1 3
239 Page 18 of 57

Machine and deep learning for personality traits detection: a…
7.4.1 Sequential deep learning
The training of DL models using parallel processing techniques to accelerate training time
and improve accuracy refers to the sequential deep learning models, enables large scale
learning models on massive datasets, offering rapid experimentation and model optimiza -
tion. Models include RNN, CNN, LSTM, and Bi-LSTM discussed the existing studies in
Table 7. The psychopathological study was explored to detect the traits from user’s generated
text by applying settings of various hyperparameters including batch size, epochs, embed -
ding sizes integrate with attention-based mechanisms of DL model Bi-LSTM to anticipate
the contextual patterns for improving accuracy. The study compared the Bi-LSTM model’s
performance with ML classifiers like DT, SVM, KNN, MNB, XGBoost, RF, and LR, find-
ing the most effective among them (Asghar et al. 2021). Other DL-based neural network
models including bi-directional models Bi-LSTM, Bi-GRU, and sequential model such as
CNN, LSTM, RNN, and GRU were carried out in literature to detect personality using You
tube dataset by analyzing videos text caption (Teli and Chachoo 2023; Naik et al. 2022;
Ahmad et al. 2021).
Another framework was initiated to detect patterns of personality by applying features
selection to same trait group using embedded deep models (Dutta et al. 2023). An innova-
tive method to detect learners’ personalities through expressions analyzed by CNN (Bahri
References Year Models Features Platform Dataset
Jeremy et al.
(2021)
2020 AttRCNN-
CNNs
Word
and text
embed-
dings
Facebook My
per-
sonal-
ity
Salminen et
al. (2020)
2021 Bi-LSTM Word
embed-
ding
Twit-
ter and
Facebook
Per-
sonal-
ity
Maheswara
Rao et al.
(2023)
2021 DeepLSTM Fast
fourier
Social
media
AS-
CER-
TAIN
Silpa et al.
(2023)
2022 RNN-LSTM SMOTE Social
media
Forum
Asghar et al.
(2021)
2023 RNN, LSTM,
Bi-LSTM
GloVe,
Fast
Text,
Word-
2Vec
YouTube Per-
sonal-
ity
Teli and
Chachoo
(2023)
2023 LSTM, Bi-
LSTM, GRU
Bag of
words
Twitter MBTI
Ahmad et al.
(2021)
2023 LSTM,GRU,
RNN, DEC
Word
embed-
ding
Twitter MBTI
Xue et al.
(2018)
2023 LSTM Word-
2Vec
Twitter MBTI
Ali and
Ahmed
(2023)
2023 RNN-LSTM Word
embed-
ding
Twit-
ter and
facebook
Per-
sonal-
ity
Altaf et al.
(2024)
2024 CNN-EEG Word
embed-
ding
Online
survey
AS-
CER-
TAIN
Table 7 Summary of exist-
ing studies of sequential deep
learning

1 3
Page 19 of 57 239

A. Naz et al.
et al. 2023) combined with text analysis of tweets, can effectively predict personality traits
(Jeremy et al. 2021), these models integrate with word embedding techniques such as word-
2vec with LSTM models (Mohan et al. 2023) was used for personality detection from social
network text postings, utilizing a hierarchical neural network with the ATTRCNN architec-
ture and inception variant to extract deep semantic features evaluated on data my personal-
ity, regression algorithms yielding the lowest prediction error (Xue et al. 2018), also for
recommendation system to predict personality features (Silpa et al. 2023) and CNN models,
enhanced with random search optimization for improved accuracy (Ali and Ahmed 2023).
The RNN-PRS model uses an RNN-LSTM framework to recommend professional careers
by predicting personality types from social media activities, leveraging type indicators for
personalized suggestions (Maheswara Rao et al. 2023). Utilizes a Deep Long Short-Term
Memory network to categorize personality features from EEG signals by creating a new
EEG dataset and comparing the performance of their model with an accuracy of 96.94 per-
cent of ML classifiers, outperforming other models like ANN, LibSVM, KNN, and ensem-
ble genetic programming techniques (Bhardwaj et al. 2021).
7.4.2 Transformer-based learning
DL architecture introduced another class called, Transformer-based models, these models
power the self-attention mechanisms to capture long-range and global dependencies in data,
for tasks like sentiment analysis, text generation, language translation, and understanding.
Transformer based models, include BERT, GPT, Distill BERT. Below Table 8 depicts the
analysis of existing studies used for personality traits detection.
For automatic detection using BERT model was also applied with limited dataset Essays
and mypersonality mapped to personality model of big five founded with DL-based fusion
References Year Models Features Platform Dataset
Chowanda
et al. (2022)
2021 LSTM,
BERT
Word
embedding
Social
media
MBTI,
café
forum
Lucky and
Suhartono
(2021)
2021 BERT,
Indo-BERT
Word
embedding
Twitter Indo-
nesian
tweets
Elourajini
and Aimeur
(2022)
2022 AWS-EP,
ELECTRA
Word
embedding
Social
media
Pandora,
MBTI,
MyPer-
sonality
Sirasapalli
and Malla
(2023)
2023 BERT Elmo,
ULMfit
Social
media
MyPer-
sonality
Rauf et al.
(2023)
2023 BERT Word-
2Vec,
BoW,
TF-IDF
Twitter MBTI
Halimawan
et al. (2022)
2023 BERT ULMfit Twitter Indo-
nesian
tweets
Akber et al.
(2023)
2023 BERT,
SBERT
Word
embedding
Twitter MBTI
Canbay
(2024)
2024 BERT Word
embedding
Social
media
MBTI,
big five
Table 8 Summary of existing
studies of transformer-based
learning

1 3
239 Page 20 of 57

Machine and deep learning for personality traits detection: a…
technique (Sirasapalli and Malla 2023) anticipate text data for extracting emotional expres-
sions into the personality model of MBTI on Twitter data (Stachl et al. 2020), comparing the
results with and without emotional cues in data applying preprocessing stage (Al-Fallooji
and Al-Azawei 2022). AWS-EP and ELECTRA learning models used as encoder that allows
multi-task to predict traits from text posts by setting the weights between two traits of per -
sonality models correlation of MBTI and Big five (Elourajini and Aimeur 2022), handled
scattered data of MBTI personality based on sixteen dimensions with four axes mappings
using Transformer-MD model (Yang et al. 2021).
Computational methods for personality prediction provide the effectiveness of combina-
tions of different DL and ML algorithms in processing and analyzing textual data to deduce
personality types by integrating the agile methodology of the Cross Industry Standardiza -
tion Process for Data Mining will be used to lead the learning process (Ontoum and Chan
2022). The proposed model effectively combines emotion and personality trait detection
tasks, utilizing A model-independent meta-learning framework for efficiency. The learn -
ing process significantly improves the approach, leading to root performance in both emo -
tion and personality detection tasks (Li et al. 2022). Several computational models in NLP
integrate with ML and DL approaches combining selected features for improving the text
patterns (Sahono et al. 2020) using encoder BERT to predict sixteen personality axes by
using online social media collected dataset based on MBTI (Rauf et al. 2023). Another
model proposed with BERT with pre-trained ULMfit model utilizing feature of sentiment,
augmentation, part of speech tagging for grammatical representation for data scaling perfor-
mance (Halimawan et al. 2022) (Cerkez and Vareskic 2021) and aspect analyses for richer
text interpretation, enhancing accuracy in personality classification from text, that shows its
effectiveness through solid baseline models, hyperparameter optimization (Chowanda et al.
2022), and an emphasis on data quality and representativeness of text (Basto 2021) to antici-
pate personality from question–answer session using SBERT model (Akber et al. 2023).
Moreover, XGBoost classifier is used with BERT transformer model to improve the perfor-
mance and reliability of prediction models, particularly analyzing user behavior and traits
based on social media activities (Lucky and Suhartono 2021). A fuzzy logic-based approach
utilized to detect patterns of personality by integrating algorithmic logic with computation
thinking of users’ text for the analysis of MBTI personality recognition to intricate the com-
plexities of personality, give a broader overview of performance as compared to traditional
models (Wang et al. 2024).
7.5 Comparison of existing studies based on MBTI dataset
A detailed comparison of various models and approaches applied to the MBTI datasets,
focusing on key performance metrics such as accuracy, precision, recall and f1-score, as
shown in Table 9. The comparison spans across several approaches including shallow ML,
ensemble learning, Sequential DL and state-of-the-art transformer-based models, providing
a broad overview of model performance on dataset.
In shallow ML model like SVM, NB, LR, are evaluated, showing consistent results with
accuracies ranging from 79 to 85%. The precision, recall, and f1-score indicate that these
models achieve balanced performance, although the combination of NB and LR as in El-
Keiey et al. ( 2022) achieves the highest accuracy at 90%. Moving to the ensemble learn -
ing approach, methods that combine multiple classifiers, such as XGBoosting, RF, GB are
1 3
Page 21 of 57 239

A. Naz et al.
shown to improve results further. The accuracies in this category are notable high, with some
models achieving up to 95% accuracy, precision and recall (Garg and Garg 2021). This sug-
gests that ensemble techniques are highly effective in enhancing performance compared to
individual models in shallow ML approaches. The Sequential DL shows models like LSTM,
Bi-LSTM, CNN and GRU being applied to MBTI dataset. These models exhibit robust
performance, achieving accuracies between 86 and 88%, with high precision and recall as
well. This suggests that deep learning models capture time-dependence and relationships in
the dataset effectively. Finally, Transformer-based models display varied performance using
model AWS-EP and ELECTRA achieve relatively high accuracies of 78% and 75%, BERT
and SBERT showed mixed results with accuracy as high 89%, but some configuration show
lower performance metrics as (Elourajini and Aimeur 2022). This highlights the variabil -
ity in transformer-based models depending on the specific architecture and implementa -
tion. This analysis exhibits that in comparison of all model on same dataset, ensemble and
deep learning approaches tend to outperform shallow machine learning models in terms of
accuracy and general performance across the various evaluation metrics. Transformer-based
models, though powerful, exhibit some variability depending on how they are applied.
Table 9 Comparison of existing studies based on MBTI dataset
MBTI dataset results (%)
Sr. No References Models Accuracy Precision Recall F1-
score
Shallow machine learning approach
1 Orynbekova et al.
(2021)
SVM, NB,LR 85 82 84 82
2 Pretty et al. (2024) SVM, NB, RF, LR 71 70 71 71
3 El-Keiey et al. (2022) NB, LR 90 89 90 89
Ensemble learning approach
4 Amirhosseini and
Kazemian ((2020)
XGBoosting,
RNN
86 85 81 80
5 Choi (2021) NB, RF, XGB 88 86 88 87
6 Shafi et al. (2021) RF, DT, KNN 85 89 83 81
7 Khan et al. (2020) XGB, LR, RF, 89 85 82 84
8 Garg and Garg (2021) SVM, LR, RF,
XGB
90 92 94 94
Sequential deep learning approach
9 Teli and Chachoo
(2023)
LSTM, Bi-LSTM,
GRU, CNN
85 78 85 87
10 Ahmad et al. (2021) LSTM + CNN,
RNN
88 88 88 88
11 Xue et al. (2018) LSTM + DEC 97 92 90 95
Transformer-based models
12 Elourajini and
Aimeur (2022)
AWS-EP,
ELECTRA
78 79 74 86
13 Rauf et al. (2023) BERT 78 75 78 78
14 Akber et al. (2023) BERT, SBERT 90 88 89 90
15 Canbay (2024) BERT 66 67 65 65
1 3
239 Page 22 of 57

Machine and deep learning for personality traits detection: a…
7.5.1 Strength and limitations of models for personality trait detection
The application of ML, and DL based models in personality trait detection presents unique
strengths and limitations. Traditional ML models, such as Support Vector Machines (SVM),
Naïve Bayes (NB), and Logistic Regression (LR), are widely used for text classification
tasks, including personality trait prediction (Safari and Chalechale 2023). Their primary
strength lies in their interpretability and efficiency on small- to medium-sized datasets. How-
ever, their reliance on feature extraction and limited capacity for capturing deep semantic
relationships in text data pose challenges when analyzing complex, context-dependent per-
sonality traits derived from user-generated content (Naithani and Raiwani 2023). Ensemble
learning models, such as Random Forest and Gradient Boosting, improve classification per-
formance by combining multiple weak learners. They are particularly useful for personality
trait detection as they reduce overfitting and enhance generalization across diverse linguistic
styles in social media data. However, they require hyperparameters tuning and may not be
as strong when dealing with highly contextual, long-range dependencies in textual data
(Sivakumar et al. 2023). Deep learning approaches, including Recurrent Neural Networks
(RNNs) and Convolutional Neural Networks (CNNs), offer superior feature learning capa -
bilities, making them highly powerful for extracting latent hidden patterns in social media
text. Sequential models like LSTM networks and GRUs can intricate long-range dependen-
cies, which are crucial when predicting personality-related text spanning multiple posts or
conversational texts. However, these models require huge datasets and high computational
resources, limiting their accessibility for real-time applications (Kelvin and Utomo May
2024). Transformer-based models, such as BERT and GPT, have transformed personality
trait detection by integrating with built-in contextual embeddings. These models can learn
complex language patterns, including false or sarcasm-based text, indirect expressions, and
implicit meanings that are critical aspects of personality inference. Additionally, their abil-
ity to process long-form textual data as whole sentence from multiple sources for enhanc -
ing classification accuracy. Nonetheless, their interpretability remains a challenge, as their
predictions often function as black boxes, making it difficult to explain decision-making
processes. Moreover, fine-tuning transformer models require substantial labeled data and
computational power (Jain et al. 2024a).
Although these models have strengths and weaknesses, the choice depends on the com -
plexity of personality traits to be analyzed, the nature of the dataset, and computational
constraints. A hybrid approach coupling with ML for interpretability, deep learning for fea-
ture extraction, and transformers for contextual understanding may offer the best balance in
advancing personality trait detection research.
8 Performance evaluation measures
Personality traits prediction is measured using a variety of indicators, including precision,
accuracy, and F1 score as discussed for the efficacy of datasets, and prediction models, is
evaluated using these parameters. In evaluating a model’s performance on dataset, key met-
rics are applied including accuracy, precision, recall, f1-score, ROC, and AUC (Ahmad et
al. 2023). In NLP, selecting the appropriate performance metrics is essential for evaluating
1 3
Page 23 of 57 239

A. Naz et al.
classification models effectively, as each metric provides unique insights based on dataset’s
characteristics (Dang and Verma 2024).
8.1 Accuracy
To measure the proportion of correctly classified instances out of total number of instances.
This metric provides a straightforward indicator of model performance; however, in an
imbalanced dataset, relying solely on accuracy may be misleading, can be calculated as
in Eq. 1. For example, in a dataset where one class dominates, a model may achieve high
accuracy simply by predicting the majority class consistently (Saeed et al. 2023). To address
this, it is often used in combination with metrics like precision and recall.

TP + TN
TF + FN + FP + TP  (1)
where TP, TN, FP, FN stands for True Positive, True Negative, False Positive, and False
Negative, respectively.
8.2 Precision
It quantifies the accuracy of true positive prediction out of all positive predictions made by
the model. This metric is particularly valuable in scenarios where false positive carry a high
cost (Akber et al. 2024), computed as in Eq. 2. Task like personality detection and precision
tell us how accurately no. of instances classified as having a specific trait (e.g., introverted)
possess that trait.

TP
TP + FP  (2)
8.3 Recall
Indicates the model’s ability to capture all true positive instances, without missing any out
of all actual positive instances in the dataset (Ahmed et al. 2024), expressed as in Eq. 3. For
example, to detect “Extrovert” trait and there are 100 people who are truly extroverted, but
the model correctly identifies only 70 of them as extroverted, then recall is high for extrovert
trait. However, if 20 extroverted individuals are missed, that means the model has some
space for improvement in capturing all true extroverted.

TP
TP + FN  (3)
8.4 F1-score
The F1-Score is a single metric that combines both precision and recall, providing a balance
between the two. It is useful when need of comprehensive measure of model performance,
especially when there is an uneven class distribution, can be computed as in Eq. 4. If the
1 3
239 Page 24 of 57

Machine and deep learning for personality traits detection: a…
model predicts 50 people as extroverted but only 30 of those predictions are correct and it
successfully identifies 60 out of 100 actual extroverts (recall), the f1-score will help assess
how well the model is performing overall. A high f1-score would indicate that the model
is effectively balancing the trade-off between identifying true extroverts and minimizing
incorrect predictions (Nakib et al. 2024).

2(P recision ∗ Recall)
P recision + Recall  (4)
8.5 AUC-ROC
Quantifies the model’s ability to distinguish between the positive and negative classes
across different threshold values. It reflects the overall model performance in classifying
instances correctly, calculated as in Eq. 5. In a personality detection model that predicts
whether individuals are introverted or extroverted, the AUC-ROC provides an indication
of how well the model can differentiate between the two personality types. An AUC value
closer to 1 means the model is excellent at distinguishing between introvert and extrovert
users, while a value around 0.5 suggests that the model is not much better than random
guessing (Zara et al. 2024).

n−1∑
i=1
(FP i − FP i−1) . (TP i + TP i−1)
2  (5)
By choosing the right metric based on the specific context and goals of NLP task, research
can gain deeper insights into their models’ performance, enabling more informed decision-
making. When evaluating classification models for predicting personality traits, these per -
formance metrics are commonly used, offering a multifaceted view of the model’s ability to
classify personality types accurately from the dataset.
9 Experimental results
The proposed methodology outlines a systematic approach, as shown in Fig. 5 to predict
personality traits from textual data using a combination of preprocessing techniques, feature
engineering methods, and ML as well as DL models as the components of the proposed
methodology to forecast personality traits from textual data. The section is divided into four
subsections that shape the general layout of the recommended methodology; each of these
sections is aimed at tackling different aspects of the process. Data preprocessing helps to
make the text suitable for analysis after eliminating different uninformative features in the
text. In feature engineering, there are significant meaningful patterns and representations
extracted from text followed by applied models for personality traits classification. Finally,
the section of the dataset description gives brief information about the source data utilized
during the research. Thus, this proves a perfect approach that guarantees the right applica -
tion of natural language processing concepts within the personality prediction systems.
1 3
Page 25 of 57 239

A. Naz et al.
9.1 Dataset used for empirical analysis
The data used in this study sourced from online platform Kaggle named as MBTI Dataset.
This corpus consists of text samples belonging to different MBTI personality types includ -
ing INTJ and ENFP types. These annotations point to 16 different personalities of users that
allow supervised learning techniques to predict the patterns of textual data to predict traits,
contributes to the quality of the experiment, therefore, the dataset is useful for examining
the correlation between text and personality trait. For prediction trait using textual dataset,
data preprocessing is an important process since it cleans the raw textual data and prepares
for analysis. The first step is the elimination of stop words, those are words with no particu-
lar importance toward the analysis. URLs and hyperlinks are also removed to quash noise
from unrelated external links. Other symbols including pipes |||, and symbols, and all forms
of punctuation marks are eliminated to reduce the text complexity. Moreover, numbers are
removed from the text as often they are irrelevant to the personality traits description. Pre -
processing is then performed that includes converting all text to lowercase to eliminate cases
where all characters are capitalized in a sentence. In addition, lemmatization and stemming
is used to convert the words to its root form to help category similar words. Last of all the
method splitting the text into individual words which can be referred to as tokens enables
the use of the other text analysis techniques.
Fig. 5 Unified framework of experimental methodology

1 3
239 Page 26 of 57

Machine and deep learning for personality traits detection: a…
9.2 Feature exploration for experimentation
Feature engineering is the process of creating useful representations of text data to feed to the
machine learning and deep learning model. Two main categories of features are considered:
9.2.1 Textual features
Term Frequency Inverse Document Frequency (TF-IDF) is a technique to determine the
importance of particular words used in documents regarding whole texts. This approach
highlights terms that are relevant within a certain category of textual information. To deter-
mine the syntactic structure of the sentences as well syntactic features that may be linked to
a personality, Part-of-Speech (POS) tagging is also used (Grunenberg et al. 2024).
9.2.2 Word embeddings
High level of text extraction is incorporated to capture semantic and contextual features from
the document. The former, which is Word2Vec, assigns high dimension vectors of words
depending on their contextual data while the latter, GloVe consolidates thorough worldwide
coexistence statistic data to create embeddings that portray the relationship between words.
Following the relative vectors, there are the sentence embeddings which aim at encoding
the given sentences into vectors, to display a more general representation of the instances.
9.3 Applied models
The applied models include basic machine learning, ensemble learning, deep learning and
Transformer learning models to deal with textual data for prediction. These models’ purpose
is to make high use of features extraction techniques and embeddings to classify the traits
that given the challenge which always posed by personality prediction models.
9.3.1 Machine learning models
Several basic types of machine learning techniques currently in use are employed. SVM
stands for Support Vector Machine and is a supervised learning algorithm categorized as
being extremely strong in classification. Logistic regression or NB is a probabilistic based
classifier which is suitable for text data based on Bayes theorem, while LR is a linear method
that performs well for classification problems and DT which builds trees where data is split
using feature thresholds. K-Nearest Neighbors is an instance of non-parametric learning
which classifies an instance based on it similarity to close instances.
9.3.2 Ensemble models
Ensemble methods are used to improve performance rates, lift and fuse various learners. GB
creates the weak learner for merging into many so that losses are minimized in an iterative
manner, and XGBoost provides an enhancement for the same by optimizing for missing
values and curb overfitting. RF accumulates the predictions of many decision trees so that
1 3
Page 27 of 57 239

A. Naz et al.
the final determinations are refined, whereas Adaboost different weak learners together in
stages to allow the formation of a stronger model.
9.3.3 Deep learning models
Such patterns are captured using deep learning techniques to predict the data sets accurately.
Text-based dependencies and long-term relations are considered using Long Short-Term
Memory (LSTM) networks. This capability is extended by Bidirectional LSTM (Bi-LSTM)
that treat both past and future context for each token aiding the model’s comprehension of
the text.
9.3.4 Transformer-based models
Transformer models are used at the current level of their higher contextual awareness.
BERT for short Bidirectional Encoder Representations from Transformers is better at cap -
turing both forward and backward relations in the text to create better brackets of contextual
embeddings. Distil BERT is a cheaper version of BERT yet one that is not as computation-
ally intensive while still ranking quite well.
9.4 Results with machine learning models
The analysis of the outcomes of the machine learning suggests that TF IDF features would
be more relevant than the POS based features in all the personality aspects whatsoever, sup-
porting the notion that the choice of features is of paramount importance to high frequency
personality prediction. From the models, the results of which are shown in Table 10 revealed
that SVM emerged superior, due to its efficiency at interpreting high-dimensional data, with
Features Models Extroversion Conscien-
tiousness
Agree-
able-
ness
Open-
ness
TF-IDF SVM 86 80 84 89
NB 78 63 75 86
LR 84 70 84 87
DT 77 70 84 84
KNN 79 70 70 86
GB 86 81 82 90
RF 79 74 79 86
XGB 86 80 83 90
AdaBoost 84 79 81 89
POS SVM 76 61 63 86
NB 70 60 58 70
LR 78 62 62 86
DT 64 53 54 75
KNN 72 56 57 85
GB 78 61 62 86
RF 78 60 61 86
XGB 76 56 58 85
AdaBoost 78 60 61 78
Table 10 Experimental results to
predict personality traits using
textual features (Results in acc
%)

1 3
239 Page 28 of 57

Machine and deep learning for personality traits detection: a…
a measured accuracy of Openness of 89% and Conscientiousness of 80%. The prior per -
formance indicates that SVM adequately tunes the data and retains the semantic density of
textual data in terms of TF-IDF vectors. Consequently, the models such as GB and XGBoost
also had high accuracy bench marked across the traits, including Extroversion and Agree -
ableness. For instance, GB attained 86% for Extroversion and 90% for Openness, suggest -
ing the model’s reliability in managing intricate interactions inherent in the data stream.
On the hand, POS-based features provided lower accuracies as compared to text-based
feature except SVM; the NB and DT provided the lowest accuracies. For instance, accuracy
in only around 53% for Conscientiousness was obtained by the DT and this shows that the
feature-based, syntactic patterns used lack discriminatory power for personality traits. Still,
GB and XGBoost models had a rather decent performance with POS features, proving the
authors’ hypothesis about the ability of such models to fuse less informative features. Fig -
ure 6 and 7 shows the comparative analysis of the results obtained. In general, the results
confirm that TF-IDF representations as the best way of capturing more detailed linguistic
patterns that reflect the subject’s personality when compared to a more basic model like
Nouns, and when combined with powerful models such as SVM and ensemble models. This
comparison strongly shows that when using powerful models, the TF—IDF features are
significant in personality predictions as compared to the other features.
9.5 Results with deep learning algorithms
LSTM and Bi-LSTM models showed an improvement in performance by almost 25% than
traditional machine learning methods. The use of Sentence Embeddings provided the high-
est accuracy results of all the traits with Bi-LSTM with an accuracy level of 92% in Extro -
version and 91% in Agreeableness, as displayed in Table 11. Overall, better performance
can be explained by the fact that deep learning models can explore hierarchical representa-
tions of textual data, thereby detecting both local and global dependencies. This feature is
made even stronger by the bidirectional characteristic of Bi-LSTM because this approach
allows the text sequences to be processed to the forward and backward returns, provid -
Fig. 6 Results analysis of TF-IDF feature based on accuracy measure

1 3
Page 29 of 57 239

A. Naz et al.
ing more accurate information on the contextual interdependencies. The type of embed -
dings used was coupled with a great influence on the performance of such models. Sentence
Embeddings performed better compared to Word2Vec and GloVe for a similar reason that it
can convert entire sentences with vectors and capture semantics and syntactic qualities. For
instance, LSTM we used with the Sentence Embeddings yielded 91% for Agreeableness as
compared to 86% for Word2Vec and 85% for GloVe. This brings out the need for a proper
choice of embeddings that would match with the task at hand. It must also be noted that the
results show that both LSTM and Bi-LSTM are equally good but Bi-LSTM edge is slightly
better which reflects the bidirectional processing gain in personality prediction tasks.
It is clear from this analysis, from Figs. 8 and 9, to further refine deep learning models
for personality prediction tasks, features such as the high-quality Sentence Embeddings are
highly beneficial. Across all the embeddings, Bi-LSTM has maintained top accuracy, mak-
ing it the best structure to capture any subtlety in the underlying language.
Deep learning results further attest to the role of neural architectures for personality
prediction. These models manage to learn sequential dependencies and, by their nature,
Model Embeddings Extroversion Conscien-
tiousness
Agree-
able-
ness
Open-
ness
LSTM Word2Vec 89 87 86 86
GloVe 87 85 89 84
Sentence
Embeddings
91 89 90 88
Bi-
LSTM
Word2Vec 88 86 85 85
GloVe 89 87 91 86
Sentence
Embeddings
92 90 91 89
Table 11 Experimental results to
predict personality traits using
word embeddings (Results in
acc %)

Fig. 7 Results analysis of PoS tagging feature based on accuracy measure

1 3
239 Page 30 of 57

Machine and deep learning for personality traits detection: a…
improve over standard machine learning even for the traits that need more contextual infor-
mation, like Conscientiousness and Openness.
9.6 Results with state-of-the-art transformer-based models
Transformer models especially Distil BERT, did incredibly well and the accuracy score
set a new high for personality prediction. Distil BERT gave the highest accuracy for such
parameters as Conscientiousness: 91% and Openness: 92% of overall accuracy, outperform-
ing even more than ML and DL architectures, as defined in Table 12. This success can be
attributed to the pre-trained nature of transformer models which are fine-tuned in massive
corpora necessary for mastering deep semantic and contextual aspects of the textual data.
Fig. 9 Results analysis of Bi-LSTM model based on accuracy measure

Fig. 8 Results analysis of LSTM model based on accuracy measure

1 3
Page 31 of 57 239

A. Naz et al.
Transformers do not process data word by word as traditional models, and LSTMs do but
then the transformer processes the whole sentence at once, which not only helps to include
all the context but are also much more efficient.
Notably, there is a little difference between the results of Distil BERT and BERT when
analyzing the results Distil BERT obtained 88% while BERT was at 82% in analyzing
Extroversion. This result reinforces the use of Distil BERT, which has 40% of BERT mod-
el’s predictive accuracy while having less computational requirements. The fact that trans -
formers so consistently outperformed the other models on all the traits analyzed shows
that this model is very good for over different aspects of personality detection, as shown in
Fig. 10. Compared to other methods, transformer models demonstrate a significant switch of
states in the experiments’ results. The main advantage for them, which stems from the ratio-
nal use of the training process of contextual embeddings and their consequent fine-tuning
for tasks, is an unmatched measure of accuracy. These models work well when the trait
involves analysis where wide knowledge of the ends of the text is implied where complex
and ambiguous language are used.
9.7 Discussion
In the era of modernization, digitization of human personality becomes buoyant instead
of being futuristic. As the number of users increases at social platforms, personality trait
prediction has emerged to be an interesting research field. Towards this end, this study uses
state-of-the-art approaches including shallow machine learning models, ensemble mod -
els, sequential deep learning models, as well as transformer-based models for predicting
Fig. 10 Results analysis of transformer models based on accuracy measure

Model Embeddings Extroversion Conscien-
tiousness
Agree-
able-
ness
Open-
ness
BERT Bert Encoder 82 77 82 88
Distil
BERT
88 91 89 92
Table 12 Experimental results
to predict personality traits
using transformer-based model
(Results in acc %)

1 3
239 Page 32 of 57

Machine and deep learning for personality traits detection: a…
the desired personality dimensions including extraversion, agreeableness, conscientious -
ness, and openness. The datasets selected, MBTI datasets, offer varied perspective on one’s
behavior, social media activity along with personality traits which serve as the primary
strength of the work.
In our experiments, we have illustrated the advantages of one model over another in
personality trait classification problem. The applications of machine learning with a limited
number of layers include LR and SVM, which act like benchmarks that compare to improve
prediction power, and ensemble models used to boost the prediction’s accuracy include
XGBoost and RF. Most deep learning models for sequential data including the LSTMs
can capture temporal structure within the data. The advanced level progressive model, the
transformer-based model achieved top results with Distil BERT model, accuracy of 92%,
measured using standard performance evaluation such as accuracy, precision, recall, and
f1-score. It is demonstrated that the ability to learn depends on the pattern of personality
trait detection across different models, and this pattern changes the predictive power of
each approach. The experimental results suggest that deep learning architectures (LSTM)
and transformer-based models (DistilBERT) outperform others, as mostly especially using
contextual and sentence embeddings. This shows that transformer models can indeed cap -
ture deep semantic meanings and contextual dependencies, which are well suited for more
intricate patterns of personality inference. Similarly, LSTM yields 91% accuracy in predict-
ing Extrovert from textual patterns which emphasizes the role of sequential information pro-
cessing in modeling any personality related textual patterns. However, the predicate of this
preference is the broad domain of traditional machine learning models such as RF and XGB,
and their ability to utilize these structured text representations (TF-IDF) that are effective
yet not ideal for uncovering more semantic relationships. That is, gradient boosting tech -
niques improve feature selection and model robustness in structured representations, and
moreover, the higher performance of XGBoost (90%) over Random Forest (86%) proves
the ability of Openness prediction. These patterns imply that the prediction of a personal -
ity trait can be more effectively achieved by an intermediate balance of deep contextual
understanding (i.e. transformers and LSTMs) and efficient feature learning (i.e., RF and
XGB). These findings indicate a strong outcome from the fact that while traditional models
are still relevant, advanced embeddings greatly enhance predictive accuracy. Transformers
possess the ability to generalize over complex linguistic patterns, which provides a scalable
solution for personality recognition applications, and fit well for deployment in real world
application domain like HR analytics, targeted marketing, and mental health assessments
(Benjamin 2025). The implementation of such models to actual world solutions has the
potential to transform a wide array of disciplines from Psychology to automatic consumer
targeting—with exponentially richer and more accurate insights into people’s behavior.
10 Data sources and datasets
To work in any domain, it is imperative to have information about dataset being used in
that domain. Table 13 displays some of the real – world datasets utilized for various studies
in related literature to capture comprehensive information about individual behavior traits,
specifically in English language. Datasets often comprise demographic data such as age,
1 3
Page 33 of 57 239

A. Naz et al.
Sr.
No
Dataset Source Attributes No. of
instances
No. of
posts
No. of
participants
Measure Avail-
ability
1 My-Per-
sonality
Safari and
Chalechale
(2022)
User
profiles,
psychomet-
ric, assess-
ment, online
activities
10 10,000 300 Big Five Private
2 Conver-
sation
Kishima et al.
(2021)
daily-life
conversa-
tions
5 15,269 4723 Big Five Private
3 Pandora Elourajini and
Aimeur (2022)
Personal-
ity and
demographic
labels
7 16,000 10,000 MBTI Private
4 ASCER-
TAIN
Subramanian
et al. (2018)
Physiologi-
cal signals,
implicit
personal-
ity, affect
recognition
6 731 58 Big Five Private
5 Face-
book
AI –
Persona
Chat
 h t t p s :  / / w w w  . k a
g g l  e . c o  m / d a t  a s
e t s  / a t h a r  v j a i  r a t
h / p e r s o n a c h a t
Comments,
Conversa-
tion Logs
6 8784 93 PEN Public
6 NeoNyx:
Person-
ality
Profiling
Dataset
 h t t p s :  / / w w w  . k
a g g l  e . c o  m / d a
t  a s e t s  / a b d e l  k a
r i  m b s a l a h / n y
x - 2 - 1
Textual
description,
votes
11 5000 748 MBTI,
Enneagram
Public
7 Essays I  h t t p s :  / / g i t  h u b . c
o  m / S e  n t i c N  e t /
p e  r s o n a l  i t y -  d e t
e c t i o n
The content
of essays
5 2468 132 Big Five Public
8 Essays II Request
granted
Big Five
scores
5 2400 250 Big Five Private
9 Big Five
Person-
ality
 h t t p s :  / / w w w  . k
a g g l  e . c o  m / d a t
a s e t s  / t u n g u  z / b i
g - fi  v e p e r s o n a l i
t y - t e s t
Text, Survey
Responses
5 1,015,342 400 MBTI Public
10 Friends
Persona
 h t t p s :  / / g i t  h u b . c
o  m / e m  o r y n l  p /
p e r  s o n a l i  t y - d  e t
e c t i o n
Dialogues,
character
interactions,
Big Five
labels
5 711 2 Big Five Public
11 MBTI  h t t p s :  / / w w w  . k a
g g l  e . c o  m / d a t  a
s e t s  / d a t a s  n a e k  /
m b t i t y p e / d a t a
tweet texts,
and user
profiles
4 8600 23 MBTI Public
Table 13 Comprehensive analysis of personality prediction datasets
1 3
239 Page 34 of 57

Machine and deep learning for personality traits detection: a…
gender, occupation and a few of them based on sentence behavior where individual’s scores
on various personality dimensions are recorded (Bozyigit et al. 2024).
Additionally, few of them may contain behavioral or situational data, such as responses
to specific scenarios or psychological test, to further contextualize the personality trait. Such
datasets are fully anonymized, ensuring that no personally identifiable information is dis -
closed, thereby eliminating any privacy concerns. Additionally, all labels within the datasets
were assigned by domain experts, specifically psychiatrists, which enhances the reliability
and validity of the tagging process and minimizes potential biased in labels.
10.1 FriendsPersona
The”FriendsPersona” dataset (Chen and Choi 2016), an extension of the original Friends TV
Show Dataset introduces a valuable resource for studying the interplay between dialogue con-
tent and personality traits. Comprising 711 annotated conversations from the iconic “Friends”
television series, each dialogue is meticulously labeled with binary indicators for the Big
Five personality attributes. The dataset is 731 KB in size and available for free download.1
10.2 MBTI
The MBTI personality type dataset stands as a prominent and expansive resource in the
realm of personality analysis, recognized for its distinction as the largest freely available
personality dataset. Specifically sourced from Twitter through the Personality Café forum,
this dataset encompasses a comprehensive collection of fifty tweet texts from 8675 volun -
teers, each associated with their corresponding MBTI personality labels. With a total of
422,845 labeled data points in the format of (post text, MBTI type), this dataset provides a
substantial foundation for research endeavors in the field of personality prediction and NLP.
The dataset is 26 KB in size and is freely available for download2.
1  h t t p s :  / / g i t  h u b . c o  m / e m  o r y n l  p / p e r  s o n a l i  t y - d  e t e c t i o n/Accessed on 16-February-2024.
Sr.
No
Dataset Source Attributes No. of
instances
No. of
posts
No. of
participants
Measure Avail-
ability
12 YouTube  h t t p s :  / / w w w  . k a
g g l  e . c o  m / c o d  e
/ l i s  a a m e l i  e w i t  t
m a n n  / p e r s  o n a l
i t  y - p r  o fi  l i n g - o
f - y o u t u b e - v l o
g g e r s
Video,
speech, and
transcripts
10 10,000 404 Big Five Public
13 Blended
Skill
Talk
 h t t p s :   /  / w w  w . k a
g g l  e . c   o m / d  a t a
s e   t s / t h e  d e v a  s t a
t  o r / u n l   o c k  -  t h e
-  c r e a  t  i v e -  p  o w  e
r -  o f - d   y n a m i c - d
i a l o g u e s
Conversation 8 7000 1500 PEN Public
14 Personae https://
zenodo.org/re-
cords/4643756
Documen-
tary about
Artificial
Life
3 18,000 145 Big Five Public
Table 13 (continued)
1 3
Page 35 of 57 239

A. Naz et al.
10.3 MyPersonality
The MyPersonality dataset stands as a notable and comprehensive resource in the field of
personality psychology, offering valuable insights into the relationships between online
behavior and individual traits that occurred in 2018. Originating from the MyPersonality
Facebook application, this dataset comprises a substantial collection of user profiles, encom-
passing diverse demographic information, psychometric assessments, and online activities
particularly focusing on the Big Five personality dimensions through online interactions,
status updates, and other digital engagements with 10,000 posts from 250 Facebook users,
and another 150 Facebook users to navigate alternative sources and datasets for studying
the connection between online activities and personality attributes. This dataset was cre -
ated by the Cambridge Psychometrics Centre. This dataset seems, however, to be currently
unavailable.
10.4 Essays
The”Essays” dataset, also called essays-I (Pennebaker and King 1999), created by Pen -
nebaker and King in 1999, is a collection of 2,468 anonymous essays, each tagged with the
author’s self-reported Big-Five personality traits. These stream-of-consciousness writings
were written by volunteers in a controlled setting, and the authors were expressly instructed
to name their personality traits using the framework. The size of the dataset is 7.8 MB and
can be downloaded for free. The enhanced version of dataset Essay II dataset (Tausczik and
Pennebaker 2010), comprises 2,400 essays that underwent manual labeling with personality
scores for the same Big-Five traits, not only contains the textual content of the essays but
also incorporates refined and classified personality information. Dataset seems, however, to
be currently unavailable.
10.5 Facebook AI: persona chat
The Facebook AI dataset is a valuable resource to enhance the engagement and specificity
of chit-chat models by conditioning conversations on assigned persona profiles. The dataset
comprises conversations between Turkers, where each participant is given a specific person-
ality. The dataset focuses on two aspects: Conditioning dialogues on the assigned profiles
information of each participant and utilizing information about their conversation partner,
even when the latter is initially unknown. Notably, the data has been sourced from the public
URLs of Kaggle repository having size of 7.99 MB, where new data are openly accessible.2
10.6 ASCERTAIN
The ASCERTAIN dataset (Subramanian et al. 2018), aptly abbreviated as “A multimodal
databaASe for impliCit pERsonaliTy and Affect recognitIoN,” is a specialized collection
tailored for investigating the interrelation between emotions and personality traits. Specifi -
cally designed to explore the domain of personality and affect recognition, ASCERTAIN
integrates multimodal data sources, emphasizing physiological signals. The dataset encom-
passes contributions from 58 users, providing a diverse and comprehensive perspective on
2  h t t p s :  / / w w w  . k a g g l  e . c o  m / d a t  a s e t s  / a t h a r  v j a i  r a t h / p e r s o n a c h a t/Accessed on 25-October-2024.
1 3
239 Page 36 of 57

Machine and deep learning for personality traits detection: a…
the intricate connections between physiological responses and the expression of personality
traits. This dataset is currently no longer available.
10.7 Big five personality
The Big Five textual dataset is based on responses to a questionnaire administered using the
internet platform open psychometric. It contains 1,015,342 tuples organized around the five-
factor model or the OCEAN model for personality characteristics. The dataset is 167 MB in
size and is freely available for download.3
10.8 NeoNyx dataset
The dataset is a comprehensive collection of personality profiles designed for exploration
and analysis of traits. It includes rich textual description and classifications across various
personality typing systems, sourced from reputable databases and thoroughly cleaned for
accuracy. The dataset consists of main file named “combined_data_highest_voted.csv” fea-
turing 18 columns from which 8 columns are unique identifiers, MBTI personality type and
detailed profile description, along with metadata for categorization and voting. The dataset
size is 10.29 MB and is freely available.4
10.9 YouTube
The YouTube dataset comprises personality scores assigned to 404 YouTube vloggers. To
collect this data, Amazon Mechanical Turk, and the Ten-Item Personality Inventory (TIPI)
were used for explaining the recordings where individuals engaged in webcam discussions
on different topics extracting text from captions and posters. The dataset closes a variety of
multimedia objects, including videos, speech recordings, and script converted to text. This
large dataset facilitates the exploration of the relationship between personality behavior and
online content creation on the YouTube platform. The dataset size is 2.68 MB and is freely
available.5
10.10 Blended skill talk
Blended talk is a dataset comprising 7000 conversations designed to explore various
dialogue models, including personality expression, empathy, and knowledge demonstra -
tion. Each record is structured with fields for personas, context, previous utterances, free
messages, guided messages, and suggestions, providing a rich foundation for stimulating
conversations platform, enhancing its relevance for conversational AI research and devel -
opment. The dataset has three folders splitting into test, train and validate.csv file with
16.57 MB in size and is freely available for download.6
3  h t t p s :  / / w w w  . k a g g l  e . c o  m / d a t  a s e t s  / t u n g u  z / b i  g - fi  v  e - p e r  s o n a l i  t y - t  e s t/Accessed on 16-February-2024.
4  h t t p s :  / / w w w  . k a g g l  e . c o  m / d a t  a s e t s  / a b d e l  k a r i  m b s a l a h / n y x - 2 - 1 / A c c e s s e d on 25-October-2024.
5  h t t p s :  / / w w w  . k a g g l  e . c o  m / c o d  e / l i s  a a m e l i  e w i t  t m a n n  / p e r s  o n a l i t  y - p r  o fi  l i n g - o f - y o u t u b e - v l o g g e r s /Accessed on
16-February-2024.
6  h t t p s :  / / w w w  . k a g g l  e . c o  m / d a t  a s e t s  / t h e d e  v a s t  a t o r /  u n l o c  k - t h e -  c r e a  t i v e -  p o w e r  - o f - d y  n a m i  c - d i a l o g u e s/
Accessed on 25-October-2024.
1 3
Page 37 of 57 239

A. Naz et al.
10.11 Personae
The Personae dataset is a collection of essays authored by 145 undergraduate students, each
approximately 1400 words in length. The essays hub on a documentary centered around the
topic of Artificial Life. This collection provides worthy stats into how ones at the bachelor’s
level articulate their ideas and perspectives on the intersection of artificial life and documen-
tary filmmaking. The dataset’s content offers a rich source for exploring diverse viewpoints
and expressions relevant to this context. The dataset is 2.3 MB in size and is freely available
for download.7
10.12 Conversation dataset
The Conversation Dataset consists of junk extracted from daily life meetings obtained
from ninety-six individuals’ attire with an Electronically Activated Recorder (EAR). In this
dataset, there are a total of 118,259 words and 15,269 conversation utterances, providing
a lavish and diverse collection of linguistic data seized in natural, real-life settings. This
dataset serves as a beneficial resource for studying and understanding patterns, dynamics,
and characteristics of spoken language in genuine daily-life interactions. This dataset is no
longer available now.
10.13 Pandora
The Pandora dataset consists of more than seventeen million comments, along with person-
ality and demographic tags, encompassing data from over 10,000 Reddit users. Remarkably,
the dataset includes Big Five personality trait labels for 16,000 users, making it the dedica-
tory Reddit dataset to incorporate such large-scale personality information. Additionally, the
dataset encompasses other personality models, including the MBTI framework. On request
available at.8
11 Applications
The enriching growth of the internet and digital media has significantly heightened the
importance of detecting personality traits from text. This development is gaining attention
from technologists, business leaders, government bodies, and political analysts who see its
potential to enhance decision-making processes in various sectors, including business and
public relations. The proliferation of social media platforms has provided a wealth of data
for analyzing online social behavior either positive or negative (Ahmad et al. 2023), encour-
aging researchers to delve deeper into understanding users’ personalities based on their
digital footprints. Personality trait detection from textual data significantly impacts various
fields by opening and suggesting new research directions and applications with the help of
machine and deep learning model predictions. Personality trait recognition has garnered
7 https://zen odo.org/rec ords/464375 6/Ac cessed on 16-February-2024.
8  h t t p s :  / / p s y  . t a k e l  a b . f  e r . h r  / d a t a  s e t s / a  l l / p  a n d o r a //Accessed on 16-February-2024.
1 3
239 Page 38 of 57

Machine and deep learning for personality traits detection: a…
significant attention across diverse influencing various domains with its potential impact
applications as shown in Fig. 11.
11.1 Machine learning-based approaches
Personality recognition using ML techniques is applied in various areas such as recruit -
ment systems, career counseling, team building where ML models help to predict the best
fit choice based on personality traits using traditional models such as SVM, KNN, NB, LR,
and DT. These techniques widely used due to their simplicity, interpretability, and effec -
tiveness in smaller datasets, which helps in understanding personality for improving users’
interaction in digital environment. Below Few applications are employed to detect personal-
ity with the help of machine learning models.
11.1.1 Personality traits in recruitment and marketing applications
In recruitment systems, understanding candidates’ personality traits aids in predicting job
performance and cultural fit regarding business terms for customers also (Khan et al. 2020).
Online marketing campaigns become more engaging and effective when personalized to
consumers’ personality traits, ensuring targeted advertisements resonate with specific audi-
ences (Yang et al. 2023). The analysis of recommendation systems is enhanced by incor -
porating personality traits, leading to more accurate and satisfying content suggestions.
Deception detection relies on personality cues, enabling the identification of inconsisten -
cies in communication styles (Bucur et al. 2024). Authorship attribution sentiment analysis
and opinion mining based on their research interest give benefit from insights into writers’
personalities, providing a deeper understanding of content distinctions (Urooj et al. 2023).
Fig. 11 Applications of personality traits detection in different domains

1 3
Page 39 of 57 239

A. Naz et al.
Self-report inventories and interviews become more accurate and insightful with personal -
ity trait recognition, aiding in psychological assessments (Asghar et al. 2021). Advertising
agencies tailor campaigns to specific audiences based on personality traits, increasing reso-
nance and impact. Political campaign strategies benefit from understanding voters’ person-
alities, allowing campaigns to tailor messages, advertisements, and outreach efforts for a
more personal connection and influence (Stachl et al. 2020). However, Ethics and risk issues
occur upon integrating AI-driven personality prediction in industrial applications like in
HR system and marketing technologies as well as in social media analysis. In HR systems,
there is a risk of biased hiring decisions if models inadvertently favor certain personality
traits, leading to discrimination (Lee et al. 2023). In marketing, AI in personality profiling
may lead to hyper personalization of ads, credit card frauds and the changing of consumer
behavior issues in this regard regarding privacy and consent (Yang et al. 2022). Misusing
personality insights in social media analysis can help to spread targeted misinformation
or digital surveillance which may attack or violate user autonomy (Pillow et al. 2025). To
mitigate these risks, it is crucial to empower bias mitigation approaches for maintaining
fairness, accountability and regulatory compliance as well as transparent ethical AI models
deployment.
11.1.2 Personality-based educational and counseling systems
Personal consulting systems benefit from tailored advice based on individual traits, enhanc-
ing the effectiveness of guidance. Career counseling benefits from personalized advice tai -
lored to individuals’ traits, guiding informed career decisions (Ahmed et al. 2023). Team
building efforts are optimized by assembling diverse teams with a mix of complementary
personality traits (Choong and Varathan 2021). In conflict resolution and negotiation,
understanding the personality traits of involved parties’ aids mediators in tailoring effective
interventions. In education, adaptive learning platforms leverage personality traits to tailor
teaching styles, content delivery, and assessments, optimizing the educational process for
effective learning outcomes (Nisha et al. 2022).
11.2 Deep learning-based approaches
Deep learning approaches have gained popularity in personality recognition because of their
ability to automatically learn complex patterns from large dataset without need for manual
feature extraction. DL models excel in more dynamic and interactives applications like
chatbots, virtual reality, and gaming where they adapt to users’ personality trait to enhance
engagement and personalization. Below applications are employed to detect personality
using deep learning approaches.
11.2.1 Personality detection in health and lifestyle applications
Personal development strategies become more effective when aligned with individual traits,
fostering meaningful self-improvement (Singh and Singh 2024). In forensic departments,
architectural designs (Schönfelder et al. 2024), personality recognition aids in criminal
profiling and understanding motives (Igwe and Durrheim 2024). Mental health diagnosis
benefits from insights into patients’ unique psychological needs, informing personalized
1 3
239 Page 40 of 57

Machine and deep learning for personality traits detection: a…
treatment plans (Yang et al. 2021). Wellness and lifestyle apps offer personalized health
recommendations by considering users’ traits and suggesting fitness routines, dietary plans,
and stress management techniques aligned with individual preferences (El-Demerdash et
al. 2022).
11.2.2 Personality recognition in interactive and visual system
In human–robot interaction, recognizing user personality enhances the design of robots,
creating more intuitive and responsive interactions. Personalized services, such as chatbots
(Naqvi et al. 2023), provide more engaging interactions in videos instead of traditional-
based interviews (Koutsoumpis et al. 2024) to recognize user personality traits and create
supportive user experience (Sharma et al. 2021). Virtual reality experiences become more
immersive with personality trait recognition, as VR applications adapt scenarios and inter -
actions based on users’ traits. Social influence and trend analysis utilize personality recogni-
tion to identify influential individuals and predict trends and ideas within social networks
for marketers and sociologists (Kumar et al. 2023). In gaming, personality trait recognition
enhances user experiences by personalizing game-play dynamics, challenges, and narratives
(Shah et al. 2021). Smart home automation leverages personality traits to adjust lighting,
temperature, and entertainment systems (Bahri et al. 2023). Language learning platforms
adapt teaching methods, content, and cultural insights based on learners’ personality traits
(Liu et al. 2024), enhancing language acquisition, and making learning more enjoyable
(Basto 2021).
These applications underscore the versatility of personality trait recognition, highlighting
its potential to transform and customize experiences across education, politics, psychology,
human–computer interaction, wellness, entertainment, and technology in various fields. As
research progresses, the integration of personality insights into these applications continues
to evolve, offering new dimensions for customization and personalization.
12 Open challenges and research issues
The domain of personality trait prediction presents lots of challenges and issues that point
out the limitations of existing studies in the relevant literature. In this section, we present
the most updated challenges.
12.1 Utilizing LLM-based models for enhanced predictions
Leveraging LLM including BERT, GPT-3, GPT-4, PaLM and other proprietary and open
source LLMs, presents opportunities for a more enhanced analysis of personality traits
prediction by fine-tuning of these models. However, challenges include ensuring domain
relevance and adapting the model to the intricacies of professional language, by managing
their large computational requirements, and addressing issues of interpretability and ethical
issues (El-Keiey et al. 2022).
1 3
Page 41 of 57 239

A. Naz et al.
12.2 Deeper analysis of word usage and intended meaning
Analyzing word usage requires a deeper understanding of context and meaning. Assigning
weight to word changes and considering the influence of tone, stress points, and enuncia -
tion on the intended meaning are all challenging tasks, especially in sensitive subjects such
as mental health. Expanding the analysis to incorporate tone of voice, captured through
recorded speech data, introduces challenges in accurately interpreting spoken nuances. Dis-
tinguishing between variations in word pronunciation that convey different emotions poses
complexities for mood analysis (Bharadwaj et al. 2018).
12.3 Utilizing deep semantic features for improved accuracy
Integrating deep semantic features into regression algorithms offers potential improvements
in accuracy. They include not actual, frequently occurring words but rather deeper, non-
taxonomic features that are associated with micro and macro aspects of individuals’ per -
sonality traits, including tone of voice and implied meanings. The risk is to create deep
semantic models to grasp the intention, feeling, and reference that often necessitate more
sophisticated practices like latent representations in transformers such as BERT or GPT,
also regression models that successfully use these variables without overfitting or compro -
mising generalizability across many people (Xue et al. 2018). Secondly, human communi-
cation differs significantly between people, space and time, thus few models of personality
description can fully encompass variability of semantic meanings. These limitations call for
the development of more complex and contextualized algorithms, to better match the com-
plexity of the task, as well as the collaboration of experts from natural language processing,
social psychology, and computational cognitive science. (Kusumaningrum et al. 2024).
12.4 Incorporating Facebook reactions for enhanced predictions
Using semantics from Facebook responses shows issues in preserving privacy while gaining
information. Furthermore, including aspects like views, emotions, readability, and formal -
ity entail advanced modeling techniques (Safari and Chalechale 2022). These reactions are
distinct emotions that do not necessarily equal personality characteristics, and depend on
content genre, culture, and user activities (Zhou et al. 2022).
12.5 Multilingual analysis for personality categorization
Enlarging personality prediction to languages such as Urdu and Pashto presents difficul -
ties due to data availability, linguistic complexities, and cultural differences, and how these
variables affect personality prediction across languages. Majorly, English based language
datasets are used to predict as high resource, but low resource data is still unavailable. Creat-
ing strong models that can be generic across several languages and cultural conditions is a
significant task (Cherukuru et al. 2022; Jain et al. 2024b).
1 3
239 Page 42 of 57

Machine and deep learning for personality traits detection: a…
12.6 Personalization vs. generalization
One of the biggest barriers to accurate personality identification is the balance between
personalization (capturing individual-specific traits) and generalization (applying models
across diverse populations). The fact that Models tailored for individual users may fail in
broader contexts while generalized models’ risk lacking complex and unique individual’
characteristics (Liao et al. 2024).
12.7 Dataset availability for advances personality analysis
The absence of publicly available datasets and the lack of significant annotated datasets
pose a significant challenge in advancing research on personality. Without access to numer-
ous and properly annotated datasets, researchers face limitations in training and validating
ML and DL models and algorithms for evaluation. The shortage of such datasets hinders the
development of strong and generalizable strategies for investigating non-textual modalities,
and physiological signals (Ilmini and Fernando 2024).
12.8 Lack of attention models in personality detection
Attention mechanisms, known for improving both model accuracy and interpretability by
analyzing the linguistic patterns, have not yet been fully explored in this domain. Although,
attention mechanisms have demonstrated significant in NLP tasks by dynamically focusing
on the most relevant parts of input, their application to personality detection often reflected
in subtle context-dependent cues within text (Christensen et al. 2020; Saviola et al. 2020).
12.9 Ethical and privacy consideration in AI-based personality recognition
AI-Based Personality detection model face significant ethical challenges, particularly in
terms of bias, privacy, and security. Computational models often rely on sensitive personal
data, such as social media activities, or behavioral patterns, raising privacy concerns about
unauthorized access or misuse of personal data. The collection, storage, and processing
of such data comply with privacy protection laws as GDPR, ensuring user consent and
data anonymity (Islam et al. 2024). Additionally, security vulnerabilities also expose per -
sonal data to breaches, making encryption and secure storage essential which is still under-
explored in existing studies. Techniques such as data anonymization, secure multi-party
computation, and privacy preserving ML are crucial for protecting user data. Furthermore,
addressing bias, fairness constraints and bias removal is still a gap which can be explored
using explainable AI to enhance the transparency and accountability in the deployment of
AI-based models to detect the patterns of personality from digital environment (Jenifa et al.
2024; Manroop et al. 2024).
For the bias mitigation various techniques designed for reducing unfair or discriminatory
outcomes in AI models, so that the outcomes are fair and unbiased. Such as Adversarial
Debiasing is the process by training a personality prediction model as well as an adversarial
network which actively minimizes bias while preserving relevant personality traits. The
analysis of hypothetical scenarios forms the basis on which fairness based on Counterfac-
tuals ensures that personality assessments model predictions do not change considering
1 3
Page 43 of 57 239

A. Naz et al.
changes of sensitive attributes like gender, socioeconomic background, preventing biased
profiling or ethnicity (Jiang et al. 2024). Additionally, reweighting is another method, which
reweights training data to ensure representation (Waris et al. 2024) while fair representation
learning is one which transforms input data to a more neutral state before processing (Shah
et al. 2019). Implementing these techniques in personality recognition enhances fairness,
transparency, and trust, ensuring ethical AI applications in academic, professional, and psy-
chological assessments.
12.10 Addressing ambiguity in personality labels
Personality has an inherently subjective characteristic and shares numerous attributes with
other personality types making it complex in classification. For instance, extraversion and
agreeableness are not only related but also their lexical correlations may also be rather
like each other allowing models to distinguish between them insufficiently. More specific
instructions that define what kind of annotation should be provided are required together
with context-dependent models (Alsini et al. 2024).
12.11 Integrating text with behavioral information
Firstly, personality is shaped not only by language but also the overall interaction, including
online activity, response time, or interaction activity rates. Combining textual information
with behavioral data might enhance the predictions but raises issues and various concerns
about feature extraction, data gathering, and privacy preservation (Fyffe et al. 2024).
12.12 Social engineering attack implication on personality trait detection
Social engineered attack that manipulates the personality of a person using a particular
trick by leveraging psychological insights to deceive individuals. Attackers provide input
to exploit personality estimations or even take advantage of weaknesses inherent in the
acquisition of data sets. To address this challenge strong countermeasures must be taken to
make personality trait detection models less vulnerable to adversarial manipulations as well
as to keep unethical practices in data processing and handling (Huseynov and Kose 2024).
Security can be enhanced by proposing attack mitigation strategies including adversarial
training can be used in personality recognition systems to defend against social engineering
attacks to enhance model robustness by exposing it to deceptive inputs and detection mech-
anisms—such as anomaly detection or behavioral analysis—with which malicious activities
in the real time can be identified (Naz et al. 2024b). Additionally, differential privacy keeps
sensitive user data safe by introducing controlled noise while the access control mecha -
nisms limit the unauthorized data manipulation to ensure that the use of AI in personality
assessments remains secure and ethical (Miller et al. 2020).
12.13 Incorporating multimodal data fusion
Exploring methods to integrate various data sources to predict personality features by ana -
lyzing multi source heterogenous data like personality images, situational cues, and videos
data that can translated into text (Chaurasia et al. 2024). NLP involve text analysis, multi -
1 3
239 Page 44 of 57

Machine and deep learning for personality traits detection: a…
modal data extends NLP focus by extracting text from other data modalities such as video
captions, speech to text transcriptions and text embedding in images (Agastya et al. 2019;
Mahandule et al. 2023). The inclusion of multimodal data fusion provides improved pos -
sibilities for integrating different types of data, including image, video, and text, in problem-
solving situations, for example, in a classification problem of predicting personality traits.
To do this, a Vision Transformer (ViT) will be used for image and video processing since
this approach lends itself well to capturing global contexts efficiently (Vásquez and Ochoa-
Luna 2021). Video datasets are processed using frame sampling or spatiotemporal modeling
to allow dynamic assessment of traits. It was found that images can be preprocessed, and
data augmentation can be applied to increase feature variety. Multimodal fusions like con -
catenation or attention-based fusions can incorporate phenomenon from all these modalities
to output reliable predictions about personality traits encompassing both static and dynamic
characteristics (Agrawal et al. 2021). For images, the deep learning models can be CNNs or
ViTs or others that extract geometric and or color-based features at a high level for the target
task as emotion recognition or personality prediction. For example, an experiment could
include comparing images of faces in different affective states to emotional categories then
combining this database with the text sentiment classification for multimodal perception.
Some format in audio data such as spectrogram representation of the data can then be fed to
models like LSTM or transformer networks to capture temporal aspects in speech such as
tone or pitch for stress or mood prediction. For the practical implementation, feature maps
from text, image, and audio modalities are integrated by using attention mechanisms or
feature concatenation to promote cross-modal integration. For instance, integrating video
frame analysis with audio tone detection enhances the gradient level of accuracy in emotion
recognition systems in human computer interfaces (Guo et al. 2024).
These attempts highlight the difficulties and challenges associated with advancing per -
sonality prediction techniques. Addressing these difficulties is imperative for the effective
integration of advanced technologies and methodologies into the field that ensuring more
accurate and culturally inclusive personality evaluations.
13 Brief answers to research questions
This section provides clear answers to the research questions outlined in Sect. 1.4, establish-
ing a connection between the findings and the overall objectives of the study.
RQ1 Which ML models are more suitable for personality traits detection in online textual
content?
Answer: Based on the analysis of existing studies, traditional ML models such as SVM,
KNN, NB, and LR, have shown promising contribution in personality detection. Leverag -
ing its scope to ensemble learning models including boosting, bagging and stacking models
effectively enhance the linguistic patterns using textual features such as TF-IDF, PoS tag -
ging, BoW and N-Gram to classify the personality traits with reasonable accuracy depend -
ing on the dataset and specific characteristics of the text being analyzed.
1 3
Page 45 of 57 239

A. Naz et al.
RQ2 Which DL models are more appropriate for personality traits detection in online tex -
tual content?
Answer: Advanced deep learning models, particularly those based on transformer archi-
tecture like BERT and GPT, have emerged as the most effective approach for detection of
personality trait. These models excel in capturing complex linguistic and contextual patterns
in data using word embeddings features such as word2vec, GloVe, Fast Text and advanced
sentence embedding rely on word choice and sentence format, significantly improving pre-
dictive accuracy over traditional ML applications. The ability to fine-tune these models on
specific personality datasets enhances their performance.
RQ3 How do diverse features and machine learning based models impact the accuracy of
personality trait prediction?
Answer: By applying advanced deep embeddings, such as Word2Vec, GloVe, and sen -
tence embeddings, along with top-performing models like BERT and Distil BERT, signifi-
cant improvements in personality prediction accuracy can be achieved. These embeddings
effectively capture semantic and contextual nuances in textual data, allowing models to
better understand and classify personality traits. Experimental results demonstrate that
leveraging contextualized embeddings enhances predictive performance, particularly for
the openness trait, which exhibits high accuracy due to its strong linguistic associations in
text. This highlights the crucial role of deep embeddings in refining personality recognition
models, enabling a more precise and reliable assessment of individual personality traits
from textual data.
RQ4 What are the features and source of available dataset on personality trait prediction?
Answer: Key features utilized for personality trait prediction include linguistic indicators
such as sentiment, complexity, and thematic content, derived from text. Available dataset
provides diverse samples along corresponding personality trait labels, that enable robust
training and evaluation of both ML and DL models.
RQ5 What are the most potential application areas for AI-based personality trait prediction
and how do they impact various fields?
Answer: AI-based personality trait prediction has significant applications across various
filed contribute insights that aid in understanding of users’ personality in digital environ -
ment. The integration of insights from diverse areas enhances the accuracy and depth of trait
by analyzing patterns in language, emotional expressions and contextual nuances for indi -
vidual differences. Moreover, drawing on various methodologies and theoretical framework
allows for the development of more predictive models to improve the outcomes. This com-
prehensive approach enriches the understanding of personality and facilitates more precise
modeling technique that help in different areas.
RQ6 What are the main open research challenges and their applicable strategies to be
employed to address these issues?
1 3
239 Page 46 of 57

Machine and deep learning for personality traits detection: a…
Answer: Key challenges ensuring the ethical use of personality data, addressing data
privacy issues, and improving model interpretability. Strategies to mitigate these challenges
involve implementing transparent data handling practices, developing ethical guidelines for
personality assessment, and utilizing explainable AI technologies to clarify how models
derive their predictions. Future research should focus on establishing best practices for the
responsible use of AI in personality predictions.
14 Conclusions and future directions
Personality traits are one of the trending domains of psychology and have the potential
to integrate with the computer science field. In the survey, we have discussed a brief
base knowledge of personality traits and relevant computational data along with tables to
strengthen our arguments. The study has also mentioned the highest count of the latest
and specific datasets with preferred sources and performance evaluation metrics to evalu -
ate them, which will further help the researcher to get all information related to AI traits in
one article. Moreover, the examination of feature engineering techniques highlights the sig-
nificance of text embedding techniques in capturing the language and facilitating accurate
predictions of character trends. Our contribution shows progression in the field by sharing
review of recent studies also describing details of datasets and applications and highlighting
key research gaps which can serve as potential research challenges. This study advances the
application of NLP to improve the detection of personality trait. By addressing gaps in exist-
ing literature such as a limited focus on psychological interpretation of textual data and the
use of advanced NLP models, this study contributes to the grounding and accuracy of per -
sonality detection to highlight the NLP models, how are used to capture language markers
associated with different personality traits, aligning these with personality frameworks. By
addressing research questions, our study highlights the critical factors influencing AI-based
personality trait prediction, identifying promising applications areas, highlighting chal -
lenges, emphasizing the significance of psychology with computational models. In the end,
several future directions and open challenges have been exploring for the investigators to
conduct the computational model in the domain, including leveraging advanced technology
like LLM, GPT-3, and addressing ethical concerns, by providing a holistic overview and
actionable insights. In short, our article aims to look at the massive growth of psychology-
based topics to integrate with ML and DL methods and the power of psychology existing
theoretical based models to enhance the performance of prediction and detection.
The primary focus in this study is to focus on natural language content for personality
trait prediction using NLP features and focusing on applications of ML and DL algorithms.
In the future, we aim to carry out such extensive review analysis of existing studies of
personality trait detection using image and video data as these data types need completely
different set of visual features and latest algorithms and techniques of Digital Image Pro -
cessing and Computer Vision. The latest advancements in digital imaging such as applica -
tion of deep learning like vision transformers will make it comprehensive for multimodal
data such as audio, video, and images. Furthermore, factors such as trust, transparency and
reliability in AI-based personality detection model predictions are dependent on improving
the interpretability of such model for enhancing interpretability. Thus, Explainable AI (XAI)
techniques can also be added to ensure clarity into how models analyze user-generated con-
1 3
Page 47 of 57 239

A. Naz et al.
tent and derive personality traits, making their decision-making process more understand -
able to researchers and end-users, in various fields, like In psychological assessment to help
counselors for understanding AI-generated insights into personalized therapy. Additionally,
In HR management, explainability makes sure that hiring decisions are not biased and are
fair. Social media platforms use XAI to enhance algorithmic transparency in content recom-
mendations for preventing biased profiling (Panfilova and Turdakov 2024). In the educa -
tion domain, explainable models empower personalized learning by offering interpretable
explanations based on the student’s behavior. XAI aids in ethical AI-based profiling and
threat detection in the areas of forensics and security. To measure the understanding of the
model by methods like SHAP (Shapley Additive Explanations) that helps in quantify each
feature’s contribution to predictions, offering a global and local understanding of model
behavior. However, LIME (Local Interpretable Model Agnostic Explanations), generates
interpretable approximations for individual predictions, making complex deep learning
models more understandable, detect bias in model, and ensure the AI is ethically deployed
(Gafarov et al. 2024). Using these techniques helps achieve fairness, reduces bias, and will
also reinforce user trust to spread responsible AI adoption in academic, professional and
psychological assessments.
Author contributions Anam and Hikmat have written a major part of the paper under the supervision of and
Ali. Muhammad and Ali have helped design and improve the methodology and wrote the paper initial draft
with Anam and Hikmat. Amal and Tariq have helped in improving the paper sections, such as, review meth-
odology, datasets, performance evaluation and challenges and future directions. Ali, Amal and Tariq have
improved the technical writing of paper. All authors are involved in revising the manuscript critically and
have approved the final version of the manuscript.
Data availability No datasets were generated or analysed during the current study.
Declarations
Competing interest The authors declare no competing interests.
Ethical approval This is reviewing an article based on different existing studies, Ethical Approval was not
required as no humans were involved in the study. There are no ethical issues or concerns regarding humans
or animals.
Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and
reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it.
The images or other third party material in this article are included in the article’s Creative Commons licence,
unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative
Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use,
you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h
t t p : /  / c r e a  t i v e c o  m m o n  s . o r g  / l i c e  n s e s / b  y - n c  - n d / 4 . 0 /.
References
Agastya IM, Handayani DO, Mantoro T (2019) A systematic literature review of deep learning algorithms
for personality trait recognition
1 3
239 Page 48 of 57

Machine and deep learning for personality traits detection: a…
Agrawal T, Agarwal D, Balazia M, Sinha N, Bremond F (2021) Multimodal personality recognition using
cross-attention transformer and behaviour encoding. https://doi.org/10.5220/0010841400003124
Ahmad H, Asghar MZ, Khan AS, Habib A (2020) A systematic literature review of personality trait classifica-
tion from textual content. Open Comput Sci 10(1):175–193. https://doi.org/10.1515/comp-2020-0188
Ahmad H, Asghar MU, Asghar MZ, Khan A, Mosavi AH (2021) A hybrid deep learning technique for per -
sonality trait classification from text. IEEE Access 9:146214–146232.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / A C C E S
S . 2 0 2 1 . 3 1 2 1 7 9 1
Ahmad W, Khan HU, Iqbal T, Khan MA, Tariq U, Cha JH (2023) Hybrid multichannel-based deep models
using deep features for feature-oriented sentiment analysis. Sustainability (Switzerland).  h t t p s : / / d o i . o r
g / 1 0 . 3 3 9 0 / s u 1 5 0 9 7 2 1 3
Ahmed M, Khan HU, Iqbal S, Althebyan Q (2022) Automated question answering based on improved TF-
IDF and cosine similarity. In: 2022 Ninth international conference on social networks analysis, manage-
ment and security (SNAMS), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / S N  A M S 5 8  0 7 1 . 2 0  2 2 . 1  0 0 6 2 8 3 9
Ahmed M, Khan HU, Khan MA, Tariq U, Kadry S (2023) Context-aware answer selection in community
question answering exploiting spatial temporal bidirectional long short-term memory. ACM Trans
Asian Low-Resour Lang Inf Process. https://doi.org/10.1145/3603398
Ahmed M, Khan HU, Munir EU (2024) Conversational AI: an explication of few-shot learning problem in
transformers-based chatbot systems. IEEE Trans Comput Soc Syst 11(2):1888–1906.  h t t p s : / / d o i . o r g / 1
0 . 1 1 0 9 / T C S S . 2 0 2 3 . 3 2 8 1 4 9 2
Akber MdA, Ferdousi T, Ahmed R, Asfara R, Rab R, Zakia U (2024) Personality and emotion—a compre -
hensive analysis using contextual text embeddings. Natl Lang Process J 9:100105.  h t t p s : / / d o i . o r g / 1 0 . 1
0 1 6 / j . n l p . 2 0 2 4 . 1 0 0 1 0 5
Akber MA, Ferdousi T, Ahmed R, Asfara R, Rab R (2023) Personality prediction based on contextual feature
embedding SBERT. In 2023 IEEE region 10 symposium, TENSYMP 2023, Institute of Electrical and
Electronics Engineers Inc.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / T E  N S Y M P  5 5 8 9 0 .  2 0 2 3  . 1 0 2 2 3 6 0 9
Alarfaj FK, Ahmad H, Khan HU, Alomair AM, Almusallam N, Ahmed M (2023) Twitter bot detection using
diverse content features and applying machine learning algorithms. Sustainability (Switzerland).  h t t p s :
/ / d o i . o r g / 1 0 . 3 3 9 0 / s u 1 5 0 8 6 6 6 2
Al-Fallooji AS, Al-Azawei A (2022) Predicting users’ personality on social media: a comparative study of
different machine learning techniques. Karbala Int J Modern Sci 8(4):617–630.  h t t p s : / / d o i . o r g / 1 0 . 3 3 6
4 0 / 2 4 0 5 - 6 0 9 X . 3 2 6 2
Ali AF, Ahmed AA (2023) Recurrent deep learning to predict personality types from social media posts. In
2023 Second international conference on advanced computer applications (ACA), pp. 63–69.  h t t p s :  / / d o
i  . o r g / 1  0 . 1 1  0 9 / A C  A 5 7 6 1  2 . 2 0 2 3  . 1 0 3  4 6 6 6 8
Alsini R, Naz A, Khan HU, Bukhari A, Daud A, Ramzan M (2024) Using deep learning and word embeddings
for predicting human agreeableness behavior. Sci Rep. https://doi.org/10.1038/s41598-024-81506-8
Alsubhi SM, Alhothali AM, Almansour AA (2023) AraBig5: the big five personality traits prediction using
machine learning algorithm on Arabic tweets. IEEE Access 11:112526–112534.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0
9 / A C C E S S . 2 0 2 3 . 3 2 9 7 9 8 1
Amirhosseini MH, Kazemian H (2020) Machine learning approach to personality type prediction based on
the Myers-Briggs type indicator®. Multimodal Technol Interact. https://doi.org/10.3390/mti4010009
Annisa FQ, Supriyanto E, Taheri S (2020) Personality dimensions classification with EEG analysis using
support vector machine. In 2020 3rd International seminar on research of information technology and
intelligent systems (ISRITI). pp 79–82.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I S  R I T I 5  1 4 3 6 . 2  0 2 0 .  9 3 1 5 5 0 7
Asghar J, Akbar S, Asghar MZ, Ahmad B, Al-Rakhami MS, Gumaei A (2021) Detection and classification of
psychopathic personality trait from social media text using deep learning model. Comput Math Methods
Med. https://doi.org/10.1155/2021/5512241
Ashton MC, Lee K, Anglim J, Bucher MA, Horwood S, Samuel DB (2024) The HEXACO personality space
before and after re-rotation to approximate the big five dimensions. J Pers Assess 106(2):145–155.  h t t p
s :  / / d o i  . o r g / 1  0 . 1 0  8 0 / 0 0  2 2 3 8 9  1 . 2 0 2 3  . 2 2 2  9 4 2 7
Babu NV , Kanaga EGM (2021) Sentiment analysis in social media data for depression detection using artifi-
cial intelligence: a review. SN Comput Sci 3(1):74. https://doi.org/10.1007/s42979-021-00958-1
Basto C (2021) Extending the abstraction of personality types based on MBTI with machine learning and
natural language processing [Online]. Available: https://arxiv.org/abs/2105.11798
Benjamin M (2025) AI-based personality assessments for hiring decisions [Online]. Available:  h t t p s :  / / w w w  .
r e s e a  r c h g  a t e . n  e t / p u  b l i c a t  i o n /  3 8 8 7 2 9 5 9 2
S. Bharadwaj, S. Sridhar, R. Choudhary, and R. Srinath, “Persona Traits Identification based on Myers-
Briggs Type Indicator(MBTI) - A Text Classification Approach,” in 2018 International Conference on
Advances in Computing, Communications and Informatics (ICACCI), 2018, pp. 1076–1082.  h t t p s : / / d o
i . o r g / 1 0 . 1 1 0 9 / I C A C C I . 2 0 1 8 . 8 5 5 4 8 2 8     .
1 3
Page 49 of 57 239

A. Naz et al.
Bhardwaj H, Tomar P, Sakalle A, Ibrahim W (2021) EEG-based personality prediction using fast fourier
transform and DeepLSTM model. Comput Intell Neurosci. https://doi.org/10.1155/2021/6524858
R. Bin Tareaf (2022) MBTI BERT: a transformer-based machine learning approach using MBTI model for
textual inputs. In 2022 IEEE 24th int conf on high performance computing & communications; 8th int
conf on data science & systems; 20th int conf on smart city; 8th int conf on dependability in sensor,
cloud & big data systems & application (HPCC/DSS/SmartCity/DependSys), IEEE, pp 2285–2292.  h t t
p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / H P  C C - D S  S - S m a r  t C i t  y - D e p  e n d S y  s 5 7 0 7 4  . 2 0 2  2 . 0 0 3 3 8
Bousalem S, Benchikha F, Marir N (2025) Personalized learning through MBTI prediction: a deep learning
approach integrated with learner profile ontology. IEEE Access 13:30861–30873.  h t t p s : / / d o i . o r g / 1 0 . 1 1
0 9 / A C C E S S . 2 0 2 5 . 3 5 4 2 7 0 1
Bozyigit F et al (2024) Generating domain models from natural language text using NLP: a benchmark dataset
and experimental comparison of tools. Softw Syst Model. https://doi.org/10.1007/s10270-024-01176-y
Bruno A, Singh G (2022) Personality traits prediction from text via machine learning. IEEE World Conf Appl
Intell Comput (AIC) 2022:588–594.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / A I  C 5 5 0 3  6 . 2 0 2 2  . 9 8 4  8 9 3 7
Bucur AM, Chulvi B, Cosma A, Rosso P (2024) The expression of happiness in social media of individuals
reporting depression. IEEE Trans Affect Comput. https://doi.org/10.1109/TAFFC.2024.3434482
Butt S, Sidorov G, Gelbukh A (2025) Interpretation of Myers-Briggs type indicator personality profiles based
on ambivert continuum scale. Expert Syst Appl 264:125689.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . e s w a . 2 0 2 4 . 1 2 5
6 8 9
Cahyani DE, Faishal AF (2020) Classification of big five personality behavior tendencies based on study field
with twitter analysis using support vector machine. In 2020 7th International conference on information
technology, computer, and electrical engineering (ICITACEE), pp 140–145.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C
I T A C E  E 5 0 1 4 4  . 2 0 2  0 . 9 2 3 9 1 3 0
Canbay P (2024) Predicting discriminative personality profile of haters from digital texts. Knowl Based Syst.
https://doi.org/10.1016/j.knosys.2024.111460
Carducci G, Rizzo G, Monti D, Palumbo E, Morisio M (2018) TwitPersonality: computing personality traits
from tweets using word embeddings and supervised learning. Information (Switzerland).  h t t p s : / / d o i . o r
g / 1 0 . 3 3 9 0 / i n f o 9 0 5 0 1 2 7
Cerkez N, Vrdoljak B, Skansi S (2021) A method for MBTI classification based on impact of class compo -
nents. IEEE Access 9:146550–146567. https://doi.org/10.1109/ACCESS.2021.3121137
Cerkez N, Vareskic V (2021) Machine learning approaches to personality classification on imbalanced MBTI
datasets. In 2021 44th International convention on information, communication and electronic technol-
ogy, MIPRO 2021—proceedings, Institute of Electrical and Electronics Engineers Inc., pp 1259–1264.
h t t p s :  / / d o i  . o r g / 1  0 . 2 3  9 1 9 / M  I P R O 5  2 1 0 1 . 2  0 2 1 .  9 5 9 6 7 4 2
Chaurasia S, Bharti KK, Gupta A (2024) A multi-model attention based CNN-BiLSTM model for personality
traits prediction based on user behavior on social media. Knowl Based Syst.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j .
k n o s y s . 2 0 2 4 . 1 1 2 2 5 2
Chen H, Choi JD (2016) Character identification on multiparty conversation: identifying mentions of charac-
ters in TV shows [Online]. Available: http://www.freebase.com
Chen S, Liu Y , Meng T, Wang S (2023) The enhancement of personality assessment and detection using
machine learning techniques, pp 110–121. https://doi.org/10.2991/978-94-6463-300-9_12
Cherukuru RK, Kumar A, Srivastava S, Verma VK (2022) Prediction of personality trait using machine learn-
ing on online texts. In 2022 International conference for advancement in technology (ICONAT), pp 1–8.
h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  O N A T 5  3 4 2 3 . 2  0 2 2 .  9 7 2 5 9 1 0
Choi S (2021) The interdependency of the diction and MBTI personality type of online users. Am J Appl
Psychol 10(1):21. https://doi.org/10.11648/j.ajap.20211001.14
Choong EJ, Varathan KD (2021) Predicting judging-perceiving of Myers-Briggs Type Indicator (MBTI) in
online social forum. PeerJ. https://doi.org/10.7717/peerj.11382
Chowanda A, Suhartono D, Andangsari EW, Bin-Zamli KZ (2022) Machine learning algorithms exploration
for predicting personality from text. ICIC Express Lett 16(2):117–125.  h t t p s : / / d o i . o r g / 1 0 . 2 4 5 0 7 / i c i c e l
. 1 6 . 0 2 . 1 1 7
Christensen AP, Golino H, Silvia PJ (2020) A psychometric network perspective on the validity and valida-
tion of personality trait questionnaires. Eur J Pers 34(6):1095–1108. https://doi.org/10.1002/per.2265
Dang VM, Verma RM (2024) Data quality in NLP: metrics and a comprehensive taxonomy. In: MiliouIoanna
P, Piatkowski N (eds) Advances in intelligent data analysis XXII. Springer, Cham, pp 217–229
dos Santos VG, Paraboni I (2022) Myers-Briggs personality classification from social media text using pre-
trained language models. J Univ Comput Sci. https://doi.org/10.3897/jucs.70941
Dutta I, Athilakshmi R (2023) Personality Prediction Using Deep Learning. In 2023 Third international con-
ference on advances in electrical, computing, communication and sustainable technologies (ICAECT),
pp 1–5.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  A E C T 5  7 5 7 0 . 2  0 2 3 .  1 0 1 1 7 5 7 3
1 3
239 Page 50 of 57

Machine and deep learning for personality traits detection: a…
El Bahri N, Itahriouan Z, Abtoy A, Brahim Belhaouari S (2023) Using convolutional neural networks to
detect learner’s personality based on the five factor model. Comput Educ: Artif Intell 5:100163.  h t t p s : /
/ d o i . o r g / 1 0 . 1 0 1 6 / j . c a e a i . 2 0 2 3 . 1 0 0 1 6 3
El-Demerdash K, El-Khoribi RA, Ismail Shoman MA, Abdou S (2022) Deep learning based fusion strategies
for personality prediction. Egypt Inf J. https://doi.org/10.1016/j.eij.2021.05.004
El-Keiey S, ElMenshawy D, Hassanein E (2022) Student’s performance prediction based on personality traits
and intelligence quotient using machine learning. Int J Adv Comput Sci Appl 13(9):292–299.  h t t p s : / / d o
i . o r g / 1 0 . 1 4 5 6 9 / I J A C S A . 2 0 2 2 . 0 1 3 0 9 3 4
Elourajini F, Aïmeur E (2022) AWS-EP: a multi-task prediction approach for MBTI/Big5 personality tests.
In IEEE international conference on data mining workshops, ICDMW, IEEE Computer Society, pp
308–315.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  D M W 5 8  0 2 6 . 2 0  2 2 . 0  0 0 4 9
Escalante HJ et al (2022) Modeling, recognizing, and explaining apparent personality from videos. IEEE
Trans Affect Comput 13(2):894–911. https://doi.org/10.1109/TAFFC.2020.2973984
Fatima N, Gul S, Ahmed J, Khand ZH, Mujtaba G (2022) A rule-based machine learning model for career
selection through MBTI personality. Mehran Univ Res J Eng Technol 41(2):185–196.  h t t p s : / / d o i . o r g / 1
0 . 2 2 5 8 1 / m u e t 1 9 8 2 . 2 2 0 2 . 1 8
Feher A, Vernon PA (2021) Looking beyond the Big Five: a selective review of alternatives to the Big Five
model of personality. Pers Individ Dif 169:110002. https://doi.org/10.1016/j.paid.2020.110002
Feizi-Derakhshi AR et al (2022) Text-based automatic personality prediction: a bibliographic review. J Com-
put Soc Sci. https://doi.org/10.1007/s42001-022-00178-4
Flesia L et al (2020) Predicting perceived stress related to the covid-19 outbreak through stable psychological
traits and machine learning models. J Clin Med 9(10):1–17. https://doi.org/10.3390/jcm9103350
Fyffe S, Lee P, Kaplan S (2024) ‘Transforming’ personality scale development: illustrating the potential of
state-of-the-art natural language processing. Organ Res Methods 27(2):265–300.  h t t p s : / / d o i . o r g / 1 0 . 1 1
7 7 / 1 0 9 4 4 2 8 1 2 3 1 1 5 5 7 7 1
Gafarov FM, Gafarova VR, Ustin PN (2024) Explainable artificial intelligence methods in text classification
machine learning models for investigating human behavior in digital environments. In 2024 IEEE 3rd
international conference on problems of informatics, electronics and radio engineering (PIERE), pp
1660–1664.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / P I  E R E 6 2  4 7 0 . 2 0  2 4 . 1  0 8 0 5 0 7 2
Garg S, Garg A (2021) Comparison of machine learning algorithms for content based personality resolution
of tweets. Social Sci Human Open 4(1):100178. https://doi.org/10.1016/j.ssaho.2021.100178
Grunenberg E, Peters H, Francis MJ, Back MD, Matz SC (2024) Machine learning in recruiting: predicting
personality from CVs and short text responses. Front Soc Psychol.  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / f r s p s . 2 0 2 3
. 1 2 9 0 2 9 5
Guo Z, Wang J, Zhang B, Ku Y , Ma F (2024) A dual transfer learning method based on 3D-CNN and vision
transformer for emotion recognition. Appl Intell 55(3):200. https://doi.org/10.1007/s10489-024-05976-z
Halimawan N, Suhartono D, Gema AP, Yunanda R (2022) BERT and ULMFiT ensemble for personality pre-
diction from Indonesian social media text. Int Symp Inf Technol Digit Innov (ISITDI) 2022:156–161.  h
t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I S  I T D I 5  5 7 3 4 . 2  0 2 2 .  9 9 4 4 4 7 6
Han S, Huang H, Tang Y (2020) Knowledge of words: an interpretable approach for personality recognition
from social media. Knowl-Based Syst 194:105550. https://doi.org/10.1016/j.knosys
Hassanein M, Hussein W, Rady S, Gharib TF (2018) Predicting personality traits from social media using
text semantics. In 2018 13th International conference on computer engineering and systems (ICCES),
pp 184–189. https://doi.org/10.1109/ICCES.2018.8639408
Hayat MK et al (2019) Towards deep learning prospects: insights for social media analytics. IEEE Access
7:36958–36979. https://doi.org/10.1109/ACCESS.2019.2905101
Huseynov F, Kose BO (2024) Using machine learning algorithms to predict individuals’ tendency to be vic-
tim of social engineering attacks. Inf Dev 40(2):298–318. https://doi.org/10.1177/02666669221116336
Igwe K, Durrheim K (2024) Analyzing social exchange motives with theory-driven data and machine learn-
ing. IEEE Access 12:2135–2149. https://doi.org/10.1109/ACCESS.2023.3348755
Ilmini W, Fernando TGI (2024) Detection and explanation of apparent personality using deep learning: a
short review of current approaches and future directions. Computing 106(1):275–294.  h t t p s : / / d o i . o r g / 1
0 . 1 0 0 7 / s 0 0 6 0 7 - 0 2 3 - 0 1 2 2 1 - 6
Ishfaq U, Khan HU, Shabbir D (2025) Exploring the role of sentiment analysis with network and temporal
features for finding influential users in social media platforms. Soc Netw Anal Min 14(1):241.  h t t p s : / / d
o i . o r g / 1 0 . 1 0 0 7 / s 1 3 2 7 8 - 0 2 4 - 0 1 3 9 6 - 6
Iskandar AF, Utami E, Hidayat W (2021) A web-based Indonesian MBTI prediction: design, implementation,
and testing. In 2021 IEEE 5th international conference on information technology, information systems
and electrical engineering (ICITISEE), pp 169–174.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  I T I S E  E 5 3 8 2 3  . 2 0 2  1 . 9 6
5 5 9 2 0
1 3
Page 51 of 57 239

A. Naz et al.
Islam A, Noor NF, Rahman SS (2024) Systematic mapping study of tools to identify emotions and personal-
ity traits. https://doi.org/10.21203/rs.3.rs-4356776/v1
Jain D, Beniwal R, Kumar A (2024a) Advancements in personality detection: unleashing the power of trans-
former-based models and deep learning with static embeddings on English personality quotes. Int J Res
Educ Sci Methods 12(4):2235–2251
Jain D, Beniwal R, Kumar A (2024b) Advancements in personality detection: unleashing the power of trans-
former-based models and deep learning with static embeddings on English personality quotes [Online].
Available: www.ijaresm.com
Jenifa G, Sevanthi P, Karthika K, Pandi VS, Arumugam D (2024) An effective personality recognition model
design using generative artificial intelligence based learning principles. In ICCDS 2024—international
conference on computing and data science, Institute of Electrical and Electronics Engineers Inc.  h t t p s :  /
/ d o i  . o r g / 1  0 . 1 1  0 9 / I C  C D S 6 0  7 3 4 . 2 0  2 4 . 1  0 5 6 0 3 6 8
Jeremy NH, Christian G, Kamal MF, Suhartono D (2021) Automatic personality prediction using deep learn-
ing based on social media profile picture and posts. In 2021 4th International seminar on research of
information technology and intelligent systems (ISRITI), pp 166–172.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I S  R I T I
5  4 0 4 3 . 2  0 2 1 .  9 7 0 2 8 7 3
Jiang J, Manoranjan V , Salam H, Celiktutan O (2024) Towards generalised and incremental bias mitigation
in personality computing. IEEE Trans Affect Comput 15(4):2192–2203.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / T A F F
C . 2 0 2 4 . 3 4 0 9 8 3 0
Jie W, Poulova P, Haider SA, Sham RB (2022) Impact of internet usage on consumer impulsive buying
behavior of agriculture products: moderating role of personality traits and emotional intelligence. Front
Psychol. https://doi.org/10.3389/fpsyg.2022.951103
Julianda AR, Maharani W (2023) Personality detection on reddit using DistilBERT. J RESTI (Rekayasa
Sistem Dan Teknologi Informasi) 7(5):1140–1146
Kaliappan S, Paranthaman V , Natrayan L, Kumar BV , Muthukannan M (2024) Leveraging machine learning
algorithm for predicting personality traits on twitter. In Proceedings of the 14th international conference
on cloud computing, data science and engineering, confluence 2024, Institute of Electrical and Electron-
ics Engineers Inc., pp 864–869.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / C o  n fl  u e  n c e 6 0 2  2 3 . 2  0 2 4 . 1 0 4 6 3 4 6 8
Kamalesh MD, Bharathi B (2022) Analysing the personality traits using machine learning techniques. In
2022 International conference on innovative computing, intelligent communication and smart electrical
systems (ICSES), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  S E S 5 5  3 1 7 . 2 0  2 2 . 9  9 1 4 1 1 2
Kelvin K, Utomo Y (2024) Overview of text based personality prediction using deep learning. Eng Math
Comput Sci J (EMACS) 6(2):93–100.  h t t p s :  / / d o i  . o r g / 1  0 . 2 1  5 1 2 / e  m a c s j  o u r n a l  . v 6 i  2 . 1 1 5 5 0
Khan W et al (2019) Part of speech tagging in Urdu: comparison of machine and deep learning approaches.
IEEE Access 7:38918–38936. https://doi.org/10.1109/ACCESS.2019.2897327
Khan AS, Ahmad H, Asghar MZ, Saddozai FK, Arif A, Khalid HA (2020) Personality classification from
online text using machine learning approach. Int J Adv Comput Sci Appl.  h t t p s : / / d o i . o r g / 1 0 . 1 4 5 6 9 / I J A
C S A . 2 0 2 0 . 0 1 1 0 3 5 8
Kishima R, Matsumoto K, Yoshida M, Kita K (2021) Construction of MBTI personality estimation model
considering emotional information. [Online]. Available: https://github.com/ikegami-yukino/
Koutsoumpis A et al (2024) Beyond traditional interviews: psychometric analysis of asynchronous video
interviews for personality and interview performance evaluation using machine learning. Comput
Human Behav 154:108128. https://doi.org/10.1016/j.chb.2023.108128
Kuchhal M, Jangid P, Saini M, Jindal R (2022) Personality prediction and group detection using social media
posts. In 2022 IEEE 7th International conference for convergence in technology, I2CT 2022, Institute of
Electrical and Electronics Engineers Inc.,  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I 2  C T 5 4 2  9 1 . 2 0 2  2 . 9 8  2 5 2 8 0
Kumar A, Beniwal R, Jain D (2023) Personality detection using kernel-based ensemble model for leveraging
social psychology in online networks. ACM Trans Asian Low-Resour Lang Inf Process.  h t t p s : / / d o i . o r
g / 1 0 . 1 1 4 5 / 3 5 7 1 5 8 4
Kusumaningrum R, Khoerunnisa SF, Farikhin BS, Herlambang AA (2024) Comparison of pre-defined auto-
matic machine learning (AutoML) for MBTI personality prediction of twitter users using binary clas -
sification approach. J Adv Res Appl Sci Eng Technol. https://doi.org/10.37934/araset.62.1.106118
Lee P, Fyffe S, Son M, Jia Z, Yao Z (2023) A paradigm shift from ‘human writing’ to ‘machine generation’
in personality test development: an application of state-of-the-art natural language processing. J Bus
Psychol 38(1):163–190. https://doi.org/10.1007/s10869-022-09864-6
Li Y , Kazemeini A, Mehta Y , Cambria E (2022) Multitask learning for emotion and personality traits detec-
tion. Neurocomputing 493:340–350. https://doi.org/10.1016/j.neucom.2022.04.049
Liao R, Song S, Gunes H (2024) An open-source benchmark of deep learning models for audio-visual appar-
ent and self-reported personality recognition. IEEE Trans Affect Comput 15(3):1590–1607.  h t t p s : / / d o i .
o r g / 1 0 . 1 1 0 9 / T A F F C . 2 0 2 4 . 3 3 6 3 7 1 0
1 3
239 Page 52 of 57

Machine and deep learning for personality traits detection: a…
Liu N, Shapira P, Yue X (2021) Tracking developments in artificial intelligence research: constructing and
applying a new search strategy. Scientometrics 126(4):3153–3192.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 1 9 2 - 0 2
1 - 0 3 8 6 8 - 4
Liu W, Sun Z, Wei S, Zhang S, Zhu G, Chen L (2024) PS-GCN: psycholinguistic graph and sentiment seman-
tic fused graph convolutional networks for personality detection. Connec Sci.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  8 0 /
0 9  5 4 0 0 9  1 . 2 0 2 3  . 2 2 9  5 8 2 0
Lucky H, Suhartono D (2021) Towards classification of personality prediction model: a combination of
BERT word embedding and MLSMOTE. In Proceedings of 2021 1st international conference on com-
puter science and artificial intelligence, ICCSAI 2021, Institute of Electrical and Electronics Engineers
Inc., pp 346–350.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  C S A I 5  3 2 7 2 . 2  0 2 1 .  9 6 0 9 7 5 0
MacFarlane A, Russell-Rose T, Shokraneh F (2022) Search strategy formulation for systematic reviews: issues,
challenges and opportunities. Intell Syst Appl 15:200091. https://doi.org/10.1016/j.iswa.2022.200091
Mahandule A, Fiske G, Malusare V , Bhambure O, Shedge R (2023) Personality prediction using ML and
NLP. In 2023 7th International conference on computing, communication, control and automation
(ICCUBEA), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  C U B E A  5 8 9 3 3 .  2 0 2 3  . 1 0 3 9 2 0 8 7
VVR MR, Silpa N, Gadiraju M, Reddy SS, Bonthu S, Kurada RR (2023) A plausible RNN-LSTM based
profession recommendation system by predicting human personality types on social media forums. In
Proceedings—7th international conference on computing methodologies and communication, ICCMC
2023, Institute of Electrical and Electronics Engineers Inc., pp 850–855.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  C M
C 5 6  5 0 7 . 2 0  2 3 . 1  0 0 8 3 5 5 7
Manroop L, Malik A, Milner M (2024) The ethical implications of big data in human resource management.
Hum Resour Manag Rev 34(2):101012. https://doi.org/10.1016/j.hrmr.2024.101012
Mayer JD, Bryan VM (2024) On personality measures and their data: A classification of measurement
approaches and their recommended uses. Pers Soc Psychol Rev 28(3):325–345.  h t t p s : / / d o i . o r g / 1 0 . 1 1
7 7 / 1 0 8 8 8 6 8 3 2 3 1 2 2 2 5 1 9
Mehta Y , Fatehi S, Kazameini A, Stachl C, Cambria E, Eetemadi S (2020a) Bottom-up and top-down: pre-
dicting personality with psycholinguistic and language model features. In Proceedings—IEEE inter -
national conference on data mining, ICDM, Institute of Electrical and Electronics Engineers Inc., pp
1184–1189. https://doi.org/10.1109/ICDM50108.2020.00146
Mehta Y , Majumder N, Gelbukh A, Cambria E (2020b) Recent trends in deep learning based personality
detection. Artif Intell Rev 53(4):2313–2339. https://doi.org/10.1007/s10462-019-09770-z
Meliá S, Reyes R, Cachero C (2024) The impact of personality and self-efficacy on domain modeling pro -
ductivity in graphical and textual notations. Inf Softw Technol 173:107491.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . i
n f s o f . 2 0 2 4 . 1 0 7 4 9 1
Meskelis S, Whittington JL (2020) Driving employee engagement: how personality trait and leadership style
impact the process. J Busin Ind Market 35(10):1457–1473. https://doi.org/10.1108/JBIM-11-2019-0477
Miller DJ, Xiang Z, Kesidis G (2020) Adversarial learning targeting deep neural network classification: a
comprehensive review of defenses against attacks. Proc IEEE 108(3):402–433.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9
/ J P R O C . 2 0 2 0 . 2 9 7 0 6 1 5
Mohan GB, Kumar RP, Gorantla S (2023) Enhancing personality classification through textual analysis:
a deep learning approach utilizing MBTI and social media data. In 2023 International conference on
network, multimedia and information technology (NMITCON), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / N M  I T
C O N  5 8 1 9 6 .  2 0 2 3  . 1 0 2 7 6 1 9 3
Mohsin Altaf M, Ullah Khan S, Majd M, Anwar SM (2024) Personality trait recognition using ECG spectro-
grams and deep learning [Online]. Available: http://arxiv.org/abs/2402.04326
Mushtaq Z, Ashraf S, Sabahat N (2020) Predicting MBTI personality type with K-means clustering and
gradient boosting. In 2020 IEEE 23rd international multitopic conference (INMIC), pp 1–5.  h t t p s :  / / d o i
. o r g / 1  0 . 1 1  0 9 / I N  M I C 5 0  4 8 6 . 2 0  2 0 . 9  3 1 8 0 7 8
Naik H, Dedhia S, Dubbewar A, Joshi M, Patil V (2022) Myers Briggs type indicator (MBTI)—personality
prediction using deep learning. In 2022 2nd Asian conference on innovation in technology (ASIAN -
CON), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / A S  I A N C O  N 5 5 3 1 4  . 2 0 2  2 . 9 9 0 9 0 7 7
Naithani K, Raiwani YP (2023) Realization of natural language processing and machine learning approaches
for text-based sentiment analysis. Expert Syst 40(5):e13114. https://doi.org/10.1111/exsy.13114
Nakib AM, Khan P, Ullah MM, Kawser ML, Jayed AKM, Zim SK (2024) Harnessing advanced NLP tech -
niques for automated personality analysis and future behavior prediction from social media posts. Mid-
dle East Res J Eng Technol 4(04):98–106.  h t t p s :  / / d o i  . o r g / 1  0 . 3 6  3 4 8 / m  e r j e t  . 2 0 2 4 .  v 0 4 i  0 4 . 0 0 1
Naqvi SM, Batool S, Ahmed M, Khan HU, Shahid MA (2023) A novel approach for building domain-specific
chatbots by exploring sentence transformers-based encoding. In 2023 International conference on IT
and industrial technologies, ICIT 2023, Institute of Electrical and Electronics Engineers Inc.  h t t p s :  / / d o i
. o r g / 1  0 . 1 1  0 9 / I C  I T 5 9 2  1 6 . 2 0 2  3 . 1 0  3 3 5 8 8 4
1 3
Page 53 of 57 239

A. Naz et al.
Naz A, Khan HU, Alesawi S, Abouola OI, Daud A, Ramzan M (2024a) AI knows you: deep learning model
for prediction of extroversion personality trait. IEEE Access.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / A C C E S S . 2 0 2 4 . 3
4 8 6 5 7 8
Naz A, Sarwar M, Kaleem M, Mushtaq MA, Rashid S (2024b) A comprehensive survey on social engineer-
ing-based attacks on social networks. Int J Adv Appl Sci 11(4):139–154.  h t t p s : / / d o i . o r g / 1 0 . 2 1 8 3 3 / i j a a
s . 2 0 2 4 . 0 4 . 0 1 6
Nesca M, Katz A, Leung CK, Lix LM (2022) A scoping review of preprocessing methods for unstructured
text data to assess data quality. Int J Popul Data Sci J. https://doi.org/10.23889/ijpds.v6i1.1757
Netter P, Hennig J, Munk AJ (2021) Principles and approaches in Hans Eysenck’s personality theory: their
renaissance and development in current neurochemical research on individual differences. Pers Individ
Dif 169:109975. https://doi.org/10.1016/j.paid.2020.109975
Nirmala M, Rajalakshmi B, Sarvepally SM, Mandava S, Megana M (2024) Personality detection for recruit-
ment using machine learning. In: Kumar A, Mozar S (eds) Proceedings of the 6th international confer-
ence on communications and cyber physical engineering. Springer, Singapore, pp 399–406
Nisha KA, Kulsum U, Rahman S, Hossain MF, Chakraborty P, Choudhury T (2022) A comparative analysis
of machine learning approaches in personality prediction using MBTI. In: Das AK, Nayak J, Naik
B, Dutta S, Pelusi D (eds) Computational intelligence in pattern recognition. Springer, Singapore, pp
13–23
Novikov P, Mararitsa L, and Nozdrachev V (2021) Inferred vs traditional personality assessment: are we
predicting the same thing? [Online]. Available: http://arxiv.org/abs/2103.09632
Ontoum S, Chan JH (2022) Personality type based on myers-briggs type indicator with text posting style by
using traditional and deep learning. [Online]. Available: http://arxiv.org/abs/2201.08717
Oravecz Z, Dirsmith J, Heshmati S, Vandekerckhove J, Brick TR (2020) Psychological well-being and per -
sonality traits are associated with experiencing love in everyday life. Pers Individ Dif 153:109620.
https://doi.org/10.1016/j.paid.2019.109620
Orynbekova K, Talasbek A, Omar A, Bogdanchikov A, Kadyrov S (2021) MBTI personality classification
using Apache Spark. In 2021 16th International conference on electronics computer and computation
(ICECCO), pp 1–4.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  E C C O 5  3 2 0 3 . 2  0 2 1 .  9 6 6 3 8 5 8
Palomino MA, Aider F (2022) Evaluating the effectiveness of text pre-processing in sentiment analysis. Appl
Sci. https://doi.org/10.3390/app12178765
Panfilova AS, Turdakov DYu (2024) Applying explainable artificial intelligence methods to models for diag-
nosing personal traits and cognitive abilities by social network data. Sci Rep 14(1):5369.  h t t p s : / / d o i . o r
g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 4 - 5 6 0 8 0 - 8
Pennebaker JW, King LA (1999) Linguistic styles: language use as an individual difference. J Pers Soc
Psychol 77(6):1296
Pillow DR, Kohler J, Bowers C, Mills S, Crabtree MA (2025) Expressing and negotiating identities in
social media ecosystems: a typology of users and their associated personality profiles. Pers Individ Dif
232:112824. https://doi.org/10.1016/j.paid.2024.112824
Pradhan T, Bhansali R, Chandnani D, Pangaonkar A (2020) Analysis of personality traits using natural lan -
guage processing and deep learning. Second Int Conf Invent Res Comput Appl (ICIRCA) 2020:457–
461.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  I R C A 4  8 9 0 5 . 2  0 2 0 .  9 1 8 3 0 9 0
Pretty EJ, Fayek HM, Zambetta F (2024) A case for personalized non-player character companion design. Int
J Hum Comput Interact 40(12):3051–3070.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  8 0 / 1 0  4 4 7 3 1  8 . 2 0 2 3  . 2 1 8  1 1 2 5
Qin X et al (2022) User OCEAN personality model construction method using a BP neural network. Elec -
tronics (Switzerland). https://doi.org/10.3390/electronics11193022
Rahman AU, Halim Z (2022) Predicting the big five personality traits from hand-written text features through
semi-supervised learning. Multimed Tools Appl 81(23):33671–33687.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1 1 0 4 2 -
0 2 2 - 1 3 1 1 4 - 5
Rahman MA, Al Faisal A, Khanam T, Amjad M, Siddik MS (2019) Personality detection from text using
convolutional neural network. In 2019 1st International conference on advances in science, engineering
and robotics technology (ICASERT), pp 1–6. https://doi.org/10.1109/ICASERT.2019.8934548
Ramachandran V , Loya A, Shah KP, Goyal S, Hansoti EA, Caruso AC (2020) Myers-Briggs type indicator
in medical education: a narrative review and analysis. Health Prof Educ 6(1):31–46.  h t t p s : / / d o i . o r g / 1 0
. 1 0 1 6 / j . h p e . 2 0 1 9 . 0 3 . 0 0 2
Rauf MH, Johan EJ, Abd Aziz Z (2023) A performance comparison of NLP text pre-processing techniques
for analysing personality based on Myers Briggs type indicator (MBTI). In 2023 IEEE international
conference on computing, ICOCO 2023, Institute of Electrical and Electronics Engineers Inc., pp 172–
175.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  O C O 5 9  2 6 2 . 2 0  2 3 . 1  0 3 9 7 6 0 3
Ryan G, Katarina P, Suhartono D (2023) MBTI personality prediction using machine learning and SMOTE
for balancing data based on statement sentences. Information (Switzerland).  h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 / i n
f o 1 4 0 4 0 2 1 7
1 3
239 Page 54 of 57

Machine and deep learning for personality traits detection: a…
Saeed A et al (2023) Topic modeling based text classification regarding islamophobia using word embedding
and transformers techniques. ACM Trans Asian Low-Resour Lang Inf Process.  h t t p s : / / d o i . o r g / 1 0 . 1 1 4
5 / 3 6 2 6 3 1 8
Safari F, Chalechale A (2022) Classification of personality traits on facebook using key phrase extraction,
language models and machine learning. In: 2022 13th International conference on information and
knowledge technology (IKT), 2022, pp. 1–5.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I K  T 5 7 9 6  0 . 2 0 2 2  . 1 0 0  3 9 0 2 0.
Safari F, Chalechale A (2023) Emotion and personality analysis and detection using natural language process-
ing, advances, challenges and future scope. Artif Intell Rev 56:3273–3297.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 1
0 4 6 2 - 0 2 3 - 1 0 6 0 3 - 3
Sahono MN et al (2020) Extrovert and introvert classification based on Myers-Briggs type indicator(MBTI)
using support vector machine (SVM). Int Semin Appl Technol Inf Commun (iSemantic) 2020:572–577.
h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / i S  e m a n t  i c 5 0 1 6  9 . 2 0  2 0 . 9 2 3 4 2 8 8
Sai GD (2023) Ensemble machine learning models in predicting personality traits and insights using Myers-
Briggs dataset. In Proceedings of the 2nd IEEE international conference on advances in computing,
communication and applied informatics, ACCAI 2023, Institute of Electrical and Electronics Engineers
Inc.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / A C  C A I 5 8  2 2 1 . 2 0  2 3 . 1  0 1 9 9 2 9 4
Salminen J, Rao RG, Jung SG, Chowdhury SA, Jansen BJ (2020) Enriching social media personas with
personality traits: a deep learning approach using the big five classes. In: Degen H, Reinerman-Jones L
(eds) Artificial intelligence in HCI. Springer, Cham, pp 101–120
Sandu A, Cotfas L-A, Stănescu A, Delcea C (2024) A bibliometric analysis of text mining: exploring the use
of natural language processing in social media research. Appl Sci. https://doi.org/10.3390/app14083144
Sarwoko E, Nurfarida IN (2021) Entrepreneurial marketing: between entrepreneurial personality traits and
business performance. Entrepreneurial Busin Econ Rev 9(2):105–118.  h t t p s : / / d o i . o r g / 1 0 . 1 5 6 7 8 / E B E R
. 2 0 2 1 . 0 9 0 2 0 7
Saviola F, Pappaianni E, Monti A, Grecucci A, Jovicich J, De Pisapia N (2020) Trait and state anxiety are
mapped differently in the human brain. Sci Rep 10(1):11112.  h t t p s : / / d o i . o r g / 1 0 . 1 0 3 8 / s 4 1 5 9 8 - 0 2 0 - 6 8 0
0 8 - z
Schönfelder P, Stebel F, Andreou N, König M (2024) Deep learning-based text detection and recognition
on architectural floor plans. Autom Constr 157:105156. https://doi.org/10.1016/j.autcon.2023.105156
Serrano-Guerrero J, Alshouha B, Bani-Doumi M, Chiclana F, Romero FP, Olivas JA (2024) Combining
machine learning algorithms for personality trait prediction. Egypt Inf J 25:100439.  h t t p s : / / d o i . o r g / 1 0 .
1 0 1 6 / j . e i j . 2 0 2 4 . 1 0 0 4 3 9
Setiawan H, Wafi AA (2020) Classification of personality type based on twitter data using machine learn -
ing techniques. In 2020 3rd International conference on information and communications technology
(ICOIACT), pp 94–98.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  O I A C T  5 0 3 2 9 .  2 0 2 0  . 9 3 3 2 1 5 2
Shafi H, Sikender A, Jamal IM, Ahmad J, Aboamer MA (2021) A machine learning approach for personality
type identification using MBTI framework. J Indep Stud Res Comput.  h t t p s : / / d o i . o r g / 1 0 . 3 1 6 4 5 / J I S R C
. 4 3 . 1 9 . 2 . 2
Shah V , Modi S (2021) Comparative analysis of psychometric prediction system. In 2021 smart technolo-
gies, communication and robotics (STCR), pp 1–5.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / S T  C R 5 1 6  5 8 . 2 0 2  1 . 9 5  8 8 9 5 0
Shah D, Schwartz HA, Hovy D (2019) Predictive biases in natural language processing models: a conceptual
framework and overview.  h t t p s :  / / d o i  . o r g / 1  0 . 1 8  6 5 3 / v  1 / 2 0 2  0 . a c l -  m a i n  . 4 6 8
Sharan NN, Romano DM (2020) The effects of personality and locus of control on trust in humans versus
artificial intelligence. Heliyon.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  1 6 / j .  h e l i y  o n . 2 0 2  0 . e 0  4 5 7 2
Sharma E, Mahajan R, Mahajan R, Mansotra V (2021) Automated personality prediction of social media
users: a decade review. Turkish J Comput Math Educ 12:5225
Sharon JA, Christinal AH, Chandy DA, Bajaj C (2023) Chapter 11—Application of intelligent edge com -
puting and machine learning algorithms in MBTI personality prediction. In Hemanth DJ, Gupta BB,
Elhoseny M, Shinde SV (Eds) Intelligent edge computing for cyber physical applications, in Intelligent
data-centric systems. Academic Press, pp 187–215.  h t t p s :  / / d o i  . o r g / 1  0 . 1 0  1 6 / B 9  7 8 - 0 -  3 2 3 - 9 9  4 1 2 -  5 . 0 0 0
0 3 - 4
Sikström S, Valavičiūtė I, Kajonius P (2025) Personality in just a few words: assessment using natural lan -
guage processing. Pers Individ Dif 238:113078. https://doi.org/10.1016/j.paid.2025.113078
Silpa N, VVR MR, Subbarao MV , Pradeep M, Grandhi CR, Karunasri A (2023) A robust team building rec-
ommendation system by leveraging personality traits through MBTI and deep learning frameworks. In
2023 International conference on IoT, communication and automation technology (ICICAT), pp. 1–6.  h
t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  I C A T 5  7 7 3 5 . 2  0 2 3 .  1 0 2 6 3 7 1 8
1 3
Page 55 of 57 239

A. Naz et al.
Silpa N, Chandini S, Sravanthi P, Lakshmi PD, VVR MR, Kurada RR (2024) A reliable ensemble machine
learning framework to predict MBTI personality trait for personalized career guidance by integrating
social media data. In 2024 1st International conference on sustainable computing and integrated com -
munication in changing landscape of AI (ICSCAI), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  S C A I 6  1 7 9 0 . 2  0 2
4 .  1 0 8 6 6 5 3 0
Singh S, Singh W (2024) AI-based personality prediction for human well-being from text data: a systematic
review. Multimed Tools Appl 83(15):46325–46368. https://doi.org/10.1007/s11042-023-17282-w
Singh NT, Chanana A, Jain D, Kumar R (2023) Personality prediction through CV analysis using machine
learning techniques. In 2023 Third international conference on advances in electrical, computing, com-
munication and sustainable technologies (ICAECT), pp 1–6.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  A E C T 5  7 5 7 0 . 2
0 2 3 .  1 0 1 1 7 8 8 3
Sirasapalli JJ, Malla RM (2023) A deep learning approach to text-based personality prediction using multiple
data sources mapping. Neural Comput Appl 35(28):20619–20630.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / s 0 0 5 2 1 - 0 2
3 - 0 8 8 4 6 - w
Sivakumar S, Priyanka S, Selvam P (2023) Enhancing personality type prediction with ensemble models:
a robust predictive approach. In 2023 International conference on innovative computing, intelligent
communication and smart electrical systems (ICSES), pp 1–7.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  S E S 6 0  0 3 4 . 2
0  2 3 . 1  0 4 6 5 4 5 2
Stachl C et al (2020) Personality research and assessment in the era of machine learning. Eur J Pers
34(5):613–631. https://doi.org/10.1002/per.2257
Subramanian R, Wache J, Abadi MK, Vieriu RL, Winkler S, Sebe N (2018) ASCERTAIN: emotion and per-
sonality recognition using commercial sensors. IEEE Trans Affect Comput 9(2):147–160.  h t t p s : / / d o i . o
r g / 1 0 . 1 1 0 9 / T A F F C . 2 0 1 6 . 2 6 2 5 2 5 0
Sujatha N, Pramod S, Bhatla S, Thulasimani T, Kant R, Chauhan A (2023) Efficient Method for Personality
Prediction using Hybrid Method of Convolutional Neural Network and LSTM. In 2023 4th Interna -
tional conference on electronics and sustainable communication systems (ICESC), pp 959–964.  h t t p s :  /
/ d o i  . o r g / 1  0 . 1 1  0 9 / I C  E S C 5 7  6 8 6 . 2 0  2 3 . 1  0 1 9 3 0 5 8
Talaat FM, El-Gendy EM, Saafan MM, Gamel SA (2023) Utilizing social media and machine learning for
personality and emotion recognition using PERS. Neural Comput Appl 35(33):23927–23941.  h t t p s : / / d
o i . o r g / 1 0 . 1 0 0 7 / s 0 0 5 2 1 - 0 2 3 - 0 8 9 6 2 - 7
Talasbek A, Serek A, Zhaparov M, Moo-Yoo S, Kim YK, Jeong GH (2020) Personality classification experi-
ment by applying k-means clustering. Int J Emerg Technol Learn 15(16):162–177.  h t t p s : / / d o i . o r g / 1 0 . 3
9 9 1 / i j e t . v 1 5 i 1 6 . 1 5 0 4 9
Tausczik YR, Pennebaker JW (2010) The psychological meaning of words: LIWC and computerized text
analysis methods. J Lang Soc Psychol 29(1):24–54. https://doi.org/10.1177/0261927X09351676
Teli MA, Chachoo MA (2023) Pre-trained word embeddings in deep multi-label personality classification
of YouTube transliterations. In Proceedings of 2023 international conference on intelligent systems,
advanced computing and communication, ISACC 2023, Institute of Electrical and Electronics Engi -
neers Inc..  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I S  A C C 5 6  2 9 8 . 2 0  2 3 . 1  0 0 8 4 0 4 7.
Urooj A, Khan HU, Iqbal S, Alghobiri M (2023) Exploring author, article, and venue feature sets for rising
star prediction in Academic network. J Sch Publ 54(3):445–473
Vásquez RL, Ochoa-Luna J (2021) Transformer-based approaches for personality detection using the MBTI
model. In 2021 XLVII Latin American computing conference (CLEI), pp 1–7.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 /
C L  E I 5 3 2  3 3 . 2 0 2  1 . 9 6  4 0 0 1 2
Wang P et al (2021) Predicting self-reported proactive personality classification with Weibo text and short
answer text. IEEE Access 9:77203–77211. https://doi.org/10.1109/ACCESS.2021.3078052
Wang T, Ye P, Lv H, Gong W, Lu H, Wang FY (2024) Modeling digital personality: a fuzzy-logic-based
Myers-Briggs type indicator for fine-grained analytics of digital human. IEEE Trans Comput Soc Syst
11(1):1096–1107. https://doi.org/10.1109/TCSS.2023.3245127
Waris M, Zaman Fakhar M, Gulsoy M, Yalcin E, Bilge A (2024) A novel pre-processing technique to combat
popularity bias in personality-aware recommender systems. IEEE Access 12:183230–183251.  h t t p s : / / d
o i . o r g / 1 0 . 1 1 0 9 / A C C E S S . 2 0 2 4 . 3 5 1 0 4 7 5
William P, Badholia A (2021) Analysis of personality traits from text based answers using HEXACO model.
In: 2021 International conference on innovative computing, intelligent communication and smart elec-
trical systems (ICSES), pp. 1–10.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I C  S E S 5 2  3 0 5 . 2 0  2 1 . 9  6 3 3 7 9 4.
William P, Yogeesh N, Tidake VM, Gondkar SS, Vengatesan K (2023) Framework for implementation of per-
sonality inventory model on natural language processing with personality traits analysis. In 2023 Inter-
national conference on intelligent data communication technologies and internet of things (IDCIoT). pp
625–628.  h t t p s :  / / d o i  . o r g / 1  0 . 1 1  0 9 / I D  C I o T 5  6 7 9 3 . 2  0 2 3 .  1 0 0 5 3 5 0 1
Xue D et al (2018) Deep learning-based personality recognition from text posts of online social networks.
Appl Intell 48(11):4232–4246. https://doi.org/10.1007/s10489-018-1212-4
1 3
239 Page 56 of 57

Machine and deep learning for personality traits detection: a…
Yang K, Yuan H, Lau RYK (2022) PsyCredit: An interpretable deep learning-based credit assessment
approach facilitated by psychometric natural language processing. Expert Syst Appl 198:116847.
https://doi.org/10.1016/j.eswa.2022.116847
Yang K, Lau RYK, Abbasi A (2023) Getting personal: a deep learning artifact for text-based measurement of
personality. Inf Syst Res 34(1):194–222. https://doi.org/10.1287/isre.2022.1111
Yang F, Quan X, Yang Y , Yu J (2021) multi-document transformer for personality detection. [Online]. Avail-
able: www.aaai.org
Zacher H, Rudolph CW (2021) Big Five traits as predictors of perceived stressfulness of the COVID-19
pandemic. Pers Individ Dif 175:110694. https://doi.org/10.1016/j.paid.2021.110694
Zara U, Ayyub K, Ullah Khan H, Daud A, Alsahfi T, Gulzar Ahmad S (2024) Phishing website detection
using deep learning models. IEEE Access 12:167072–167087.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 9 / A C C E S S . 2 0 2
4 . 3 4 8 6 4 6 2
Zarouali B, Dobber T, Schreuder J (2024) Personality and susceptibility to political microtargeting: a com -
parison between a machine-learning and self-report approach. Comput Human Behav 151:108024.
https://doi.org/10.1016/j.chb.2023.108024
Zhang B, Huang Y , Cui W, Zhang H, Shang J (2023) PsyAttention: psychological attention model for person-
ality detection. [Online]. Available:  h t t p s :  / / w w w  . s i m p l  y p s y  c h o l o  g y . o r  g / t h e -  m y e r  s - b r i g g s
Zhou L, Zhang Z, Zhao L, Yang P (2022) Attention-based BiLSTM models for personality recognition from
user-generated content. Inf Sci (NY) 596:460–471. https://doi.org/10.1016/j.ins.2022.03.038
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Authors and Affiliations
Anam Naz1 · Hikmat Ullah Khan2 · Amal Bukhari3 · Bader Alshemaimri4 · Ali Daud5 ·
Muhammad Ramzan6
  Hikmat Ullah Khan
dr.hikmat.niazi@gmail.com
  Ali Daud
alimsdb@gmail.com
1 Department of Computer Science, University of Sargodha, Punjab, Pakistan
2 Department of Information Technology, University of Sargodha, Punjab, Pakistan
3 Department of Information Systems and Technology, Collage of Computer Science and
Engineering, University of Jeddah, Jeddah, Saudi Arabia
4 Software Engineering Department, College of Computing, and Information Sciences, King
Saud University, Riyadh, Saudi Arabia
5 Faculty of Resilience, Rabdan Academy, Abu Dhabi, United Arab Emirates
6 Department of Software Engineering, University of Sargodha, Punjab, Pakistan
1 3
Page 57 of 57 239
