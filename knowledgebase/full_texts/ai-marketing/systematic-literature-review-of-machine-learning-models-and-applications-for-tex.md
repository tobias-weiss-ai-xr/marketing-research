---
title: Systematic Literature Review of Machine Learning Models and Applications for Text Recognition
url: https://arxiv.org/abs/2608.26500
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Nuzhat Khan
- Ab Al-Hadi Ab Rahman
- Shahriyar Masud Rizvi
- Ibrahim Yousef Alshareef
- Muhammad Nadzir Marsono
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.26500
pages: 24
chars: 134246
fetched_at: '2026-11-08T13:29:32+00:00'
kb_version: 1
---

# Systematic Literature Review of Machine Learning Models and Applications for Text Recognition

Date of publication October 6, 2025.
Digital Object Identifier 10.1109/ACCESS.2025.3618109
Systematic Literature Review of Machine
Learning Models and Applications for
Text Recognition
NUZHAT KHAN1, AB AL-HADI AB RAHMAN 1 (Senior Member, IEEE), SHAHRIY AR MASUD
RIZVI3, IBRAHIM YOUSEF ALSHAREEF 1, MUHAMMAD NADZIR MARSONO 1, MUHAMMAD
P AEND BAKHT4 (Member, IEEE), MOHD SHAHRIZAL RUSLI 2, and SHAHIDATUL SADIAH 1
1Faculty of Electrical Engineering, Universiti Teknologi Malaysia, Johor Bahru 81310, Malaysia (khan.nuzhat@utm.my), (hadi@utm.my),
(Yousefm@graduate.utm.my), (shahidatulsadiah@utm.my), (mnadzir@utm.my)
2Faculty of Artificial Intelligence, Universiti Teknologi Malaysia, Kuala Lumpur 54100, Malaysia (shahrizalr@utm.my)
3Department of Electrical and Electronic Engineering, American International University-Bangladesh, 408/1, Kuratoli 1229, Bangladesh (shahriyar@aiub.edu)
4Department of Electrical Engineering, Balochistan University of Information Technology, Engineering and Management Sciences, Quetta 87300, Pakistan
(paend.bakht@gmail.com)
Corresponding author: Ab Al-Hadi Ab Rahman (hadi@utm.my).
This work was supported in part by Universiti Teknologi Malaysia with the Flagship CoE/RG research grant number
Q.J130000.5023.10G05 and Q.J130000.5023.10G09, and the Professional Development grant number R.J130000.7113.07E51. This work
is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/.
ABSTRACTOptical Character Recognition (OCR) for text recognition using machine vision has
significantly improved, particularly when handling heterogeneous textual data. Traditional OCR models
struggle with script variations, writing styles, and degraded documents. Advancements in technology
are leading to new AI models with improved architecture for handling multiple languages and complex
data formats. Despite this progress, a comprehensive evaluation of OCR advancements remains limited.
Based on the established preferred reporting items for systematic reviews and meta-analysis (PRISMA)
guidelines, this literature review presents an extensive assessment of OCR research to trace the evolution
of AI models over the past decade. It explores the transition in AI models, application domains, data
types, linguistic coverage, and challenges. Through a detailed analysis of 97 selected studies published
during January 2015 - January 2025, key OCR models are identified, and their performance, strengths, and
limitations are analyzed. The findings highlight how OCR technologies have evolved to address structured
and unstructured text, scene text recognition, and multilingual processing. Unresolved challenges include
limited resources for underrepresented languages, high variability in handwritten text, visual similarity
among characters, and constraints in real-time OCR applications. To address these issues, several promising
approaches are proposed. Key suggestions include self-supervised learning, multimodal AI, automated
machine learning (AutoML), AI-assisted postprocessing, tiny machine learning (TinyML), and the creation
of joint corpora for script matching. The future recommendations aim to enhance OCR accuracy and tackle
the challenges identified for real-time industrial applications. This study will guide future research and
establish a foundation for OCR field.
INDEX TERMSOptical Character Recognition, OCR, Machine Vision, Deep Learning, Text Recognition,
Literature Review.
I. INTRODUCTION
O
PTICAL character recognition (OCR) systems have
transformed the way we interact with textual informa-
tion [1]. Recent advancements in artificial intelligence (AI)
and machine vision have significantly enhanced the ability of
computers to interpret and process visual information. Now,
AI models analyze their surroundings through image pro-
cessing to extract meaningful insights. One key application
of image processing is text extraction, where AI models use
OCR to convert printed or handwritten text into a machine-
readable format [2]. See a simplified illustration of an end-
to-end OCR system for a car license plate recognition in
VOLUME 13, 2025 177647
arXiv:2608.26500v1  [cs.CV]  27 Aug 2026

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
Figure 1. The process begins with text detection, followed
by text segmentation, and concludes with text recognition.
Associated techniques, such as text localization and text
verification, complement the main process. These dynamic
and problem-specific techniques may include multiple steps
of image processing, classification, and natural language pro-
cessing [3]. Initially developed to digitize printed and hand-
written documents, OCR has evolved into a standard tool for
modern data management and the digital preservation of cul-
tural heritage [4]. Today, OCR technology is widely adopted
across various industries for seamless human-computer in-
teraction [5]. In the finance sector, OCR streamlines check
processing and fraud detection [6]. In healthcare, it facilitates
the digitization of patient records and the automation of
medical billing [7]. The education sector benefits from the
digitization of books and research papers, which increases
access to academic resources [8]. In the legal field, OCR
supports contract analysis and digitization of case files [9]
while government agencies use it to digitize public records
for efficient services [10]–[12]. In logistics, OCR automates
data extraction from shipping labels and packaging for rapid
inventory management. Retailers implement OCR for receipt
scanning and product cataloging. In manufacturing, it as-
sists with quality control and information extraction from
documents. The publishing industry utilizes OCR to digitize
newspapers and archives for online accessibility [13]. The
automotive sector uses it for license plate recognition and ve-
hicle registration [14]. Additionally, OCR aids law enforce-
ment in forensic analysis and identity verification, besides
enhancing assistive technologies for visually impaired users
and facilitating real-time text translation in augmented reality
(AR) and virtual reality (VR) environments [15].
Considering their widespread adoption, modern intelligent
systems require fast and accurate OCR models for real-
time text recognition. The core of these systems is OCR
technology supported by pre-trained AI models to trans-
form analog text into a machine-encoded format [16]. AI-
based OCR models use classification techniques to recognize
and extract text from images. These models have evolved
significantly since their inception [17]. Early OCR systems
were built on handcrafted feature extraction, where models
identified textual patterns using predefined rules and statisti-
cal methods. These approaches, including template matching
and optical feature detection, performed well for structured
printed text but faced difficulty with font, style, and layout
variations. The advent of machine learning improved the
capabilities of OCR models to learn representations from
labeled data. For instance, techniques such as support vector
machines (SVMs) and artificial neural networks (ANNs)
enhanced OCR. However, these models required extensive
feature engineering and often lacked adaptability for different
languages and scripts [18].
The shift towards deep learning has revolutionized OCR
and empowered models to learn hierarchical features auto-
matically. Convolutional neural networks (CNNs) became
the foundation for printed OCR with convolutional layers to
Text detection
Text verification
Text localization
Text recognition
Input image
Text
segmentation
Classifier
TBH 5019
Digital text
Output text
Cropped characters
Text region
Character images
FIGURE 1: Example of end-to-end car plate OCR.
extract spatial features and classify characters [19]. Similarly,
different types of recurrent neural networks (RNNs), particu-
larly long short-term memory networks (LSTMs) addressed
sequential dependencies in handwritten and cursive text [20].
These methods led to enhanced recognition of connected
characters. Transformer-based architectures have recently
dominated OCR applications. Models such as TrOCR [21],
ViT [22], and CharFormer [23] have achieved state-of-the-
art results using self-attention mechanisms for contextual
text interpretation. They are characterized by the ability to
process multilingual content, recognize handwritten scripts,
and navigate complex document layouts [24]. Despite these
breakthroughs, OCR systems still fall short of human-level
reading. While research in this area is expanding, the ab-
sence of a unified review has resulted in a lack of clarity
regarding dominant OCR architectures. Moreover, several
persistent challenges in OCR applications have not been
explored. Many existing literature reviews related to OCR
are fragmented due to focusing on individual languages [25],
datasets [26], particular scenarios [27] or specific model
architectures [28]. Given the growing demand for efficient
real-world OCR solutions, a systematic evaluation of current
AI-based OCR models is necessary. This review bridges ex-
isting gaps by examining the evolution of OCR technologies,
their multilingual capabilities, and the primary challenges. It
presents a comprehensive and up-to-date synthesis of OCR-
based information extraction (IE), extending beyond previ-
ous surveys that focused on narrower aspects [2], [29]. By
consolidating recent model developments, real-world appli-
cations, and multilingual advancements, the review provides
a structured meta-analysis of the field. It critically assesses
leading architectures, outlines their strengths and limitations,
and proposes future research directions to advance the state
of OCR systems. The key objectives of this work are as
follows:
•A systematic review of existing OCR research to examine
state-of-the-art models and supported languages.
•To assess the temporal trends in OCR models from a
multilingual recognition and overall accuracy perspective.
•To explore the fundamental challenges encountered by
177648 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
existing OCR systems.
•To identify the gaps in ongoing OCR research.
•To propose future directions for improved cross-lingual
OCR, robust error correction, and better recognition of
underrepresented languages.
The remainder of this paper is organized as follows: Sec-
tion II explains the review methodology. The results and a de-
tailed discussion are presented in Section III, and Section IV
concludes the paper.
II. REVIEW METHODOLOGY
A. PROBLEM FORMULATION
Advancements in AI [30] have led to major improvements
in computer vision techniques for automatically recogniz-
ing text from images using OCR [9]. This progress has
introduced many OCR systems, each using unique machine-
learning and deep-learning models [2]. Several studies focus
on evaluating specific models [31] or testing them on indi-
vidual languages [32], [33] and datasets [34], [35]. How-
ever, no structured review explores the core OCR models.
Despite extensive research, a clear gap remains because
no comprehensive study identifies the main OCR models,
their strengths, and their limitations. A broader analysis is
needed to understand the barriers to accurate OCR and to
determine which models work best for different problems.
This review addresses that gap by examining existing OCR
models and their performance for several languages and ap-
plication domains. Furthermore, it highlights underexplored
areas that require additional investigation. These findings will
assist researchers in making informed decisions about model
selection and advance OCR technology.
B. REVIEW SCOPE
The scope of this review is defined according to the PICOC
(population, intervention, comparator, outcomes, context)
framework, which supports a well-structured and unbiased
analysis [36]. The review focuses on the development and
transition of OCR models from January 2015 to January
2025. It is important to note that AI models used in OCR
have been extensively studied in other fields, for example
[37]. Therefore, this review does not explain the working
mechanisms or architectural designs of OCR models. In-
stead, it examines their application in OCR, performance in
different languages and scripts, and the challenges they face.
In response to these challenges, the review proposes alter-
native methods to mitigate the limitations. It includes peer-
reviewed journal articles and conference papers published
in the last ten years and excludes gray literature, extended
abstracts, literature reviews, and non-English studies. The
review also omits general computer vision applications (such
as self-driving cars reading signboards), non-text image anal-
ysis (e.g., satellite imagery with partial textual content), and
commercial software evaluations.
C. REVIEW PROTOCOL
Unlike previous systematic reviews that have focused on
specific aspects of OCR such as [8], [38], this work com-
prehensively covers OCR research. We conducted a sys-
tematic search across seven major academic databases: Sci-
enceDirect, IEEE Xplore, Scopus, Web of Science, ACM
Digital Library, SpringerLink, and Google Scholar. These
databases were selected for their broad coverage of AI,
machine learning, and computer vision research. Predefined
inclusion and exclusion criteria were applied to filter and
select relevant studies to ensure a thorough and focused
analysis. The primary search strategy involved a combination
of Boolean operators and keyword variations to maximize
retrieval efficiency. The core search terms in the search string
were related to OCR and AI. Figure 2 shows the step-by-step
review protocol.
Need
Research
questions
Scope Search
Screen
Extract Analyze
Synthesize
Report
FIGURE 2: Review protocol.
This review protocol was designed to extract, synthesize,
and evaluate studies that align with the predefined research
objectives. For each database, the search string was modified
to refine the search outcomes. We applied additional filters
based on publication type, accessibility, and relevance to
OCR model development. By applying the inclusion and ex-
clusion criteria, only papers that met the predefined selection
parameters were retained for further analysis. While some
papers may have indirectly addressed OCR models without
explicitly mentioning key terms in their titles, abstracts, or
keywords, they were omitted as they fell outside the search
scope. The inclusion and exclusion criteria are outlined in
Table 1.
Initially, a total of 45959 records were retrieved from var-
ious databases (including 1923 from Web of Science, 9039
from Scopus, 21100 from Google Scholar, 10149 from IEEE
Xplore, 2480 from SpringerLink, 3121 from ScienceDirect
and 689 from ACM Digital Library). After removing irrel-
evant and inaccessible articles, the database was reduced to
497 articles for title screening. Following this, 310 papers
met the eligibility criteria for abstract review. Upon further
assessment, only 182 papers proceeded to full-text evaluation
due to the inaccessibility of 128 articles. During this phase,
we manually excluded duplicate entries and studies that
lacked transparent OCR models or evaluation methodologies.
VOLUME 13, 2025 177649

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
TABLE 1: Inclusion and exclusion criteria
Criteria Type Description
Period Focus on recent advancements in OCR.
Inclusion: Publications from January 2015 to January 2025.
Exclusion: Articles published before 2015.
Language Only English language articles are included.
Exclusion: The articles published in languages other than English.
Type of literature Only high-quality, peer-reviewed sources are considered.
Exclusion: Grey literature such as reports, government documents, working papers, and
non-peer-reviewed sources.
Type of source Only peer-reviewed journal and conference papers are included.
Exclusion: Books, preprints, and non-peer-reviewed articles.
Accessibility Studies must be accessible from major academic databases (IEEE Xplore, Scopus, Web
of Science, SpringerLink, ScienceDirect, ACM Digital Library).
Exclusion: Articles behind paywalls without institutional access.
Relevance to RQs Articles must contribute to at least two predefined research questions.
Exclusion: Articles that do not address at least two research questions.
D. SEARCH STRATEGY AND DATABASE SELECTION
To retrieve relevant high-quality articles, the search involved
multiple iterations in refining keyword combinations. The
primary search string included variations of following terms:
("optical character recognition" OR "OCR" OR "text recog-
nition" OR "document digitization" OR "document digiti-
sation" OR "image text extraction" OR "character recog-
nition") AND ("deep learning" OR "machine vision" OR
"machine learning" OR Model). Searches were performed
between 15–26 January 2025, applying language, date, and
article type filters specific to each database. Following the
inclusion and exclusion criteria, initial search results were
filtered using a full-text screening process. The final dataset
selection process is summarized in Table 2. After duplicate
removal and full-text analysis, the final dataset comprised
97 articles that met the predefined inclusion criteria. The
PRISMA flow diagram in Figure 3 illustrates the step-by-
step article selection process. Additionally, distribution of
the final database of 97 article with percentages is given in
Figure 4.
TABLE 2: Studies retrieved from each database in automated
search
Source Initial Results Retrieved Articles
Web of Science 1923 870
Scopus 9039 685
Google Scholar 21100 40
IEEE Xplore 10149 689
SpringerLink 2480 509
ScienceDirect 3121 88
ACM Digital Library 627 21
Records identified from
Databases (n = 7)
Registers (n =2902)
Records removed before screening:
Duplicate records removed (n = 870)
Records removed after reading titles (n = 1562)
Records screened
(n = 497)
Records excluded after reading abstract
(n = 187)
Records sought for
retrieval (n = 310)
Records not retrieved
(n = 128)
Records assessed for
Eligibility (n = 182)
Records excluded:
Beyond review scope (n = 34)
Phase 2 criteria (n = 51)
Ethical reason (n = 1)
Studies included in the
review (n = 97)
Identification of studies via databases and registers
IdentificationScreeningIncluded
FIGURE 3: PRISMA flow diagram of reviewed literature.
E. RESEARCH QUESTIONS AND MOTIVATION
For this systematic review, we defined three research ques-
tions (RQs) that align with the study’s primary objectives.
These RQs are given below:
•RQ1: What are the dominant AI-based models used in
OCR, and how do they compare in terms of accuracy,
efficiency, and multilingual performance?
•RQ2: Which writing scripts are well-supported in OCR
research, and what gaps exist?
•RQ3: What are the significant challenges in current OCR
systems, and what future research directions can address
these issues?
Addressing these questions comes with individual and
collective benefits. Individually, each question targets a crit-
ical dimension of OCR: RQ1 enhances understanding of
AI-driven OCR models, RQ2 evaluates script coverage to
identify inclusivity gaps, and RQ3 uncovers existing chal-
lenges to inform future advancements. Collectively, these
inquiries form a comprehensive framework for an improved
OCR technology. The combined outcomes will contribute
177650 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
54%
18%
12%
5%
5% 4% 2%
 IEEE
Web of Science
Springer
ScienceDirect
ACM Digital Library
Scopus
GoogleScholar
FIGURE 4: Database distribution of the final 97 retrieved
articles after systematic screening.
to improving OCR accuracy and efficiency by addressing
current limitations.
F . THREATS TO VALIDITY
The quality of a systematic review relies on thoroughly
addressing potential threats to validity [39]. In this study, key
threats included selection bias, information bias, and biases
in the data extraction process. To minimize selection bias,
we employed a broad search string followed by a selection
strategy based on the method adopted in [40]. During the
literature search, no keywords related to a certain model,
method, or language were included in the search string.
OCR research is captured equally, with statistics analyzed
afterward from the final results to show a true research dis-
tribution. A second phase of selection criteria was introduced
to address information bias, in which studies with ambigu-
ous or missing information were excluded after a full-text
review. Additionally, both manual and automated searches
were conducted collectively on multiple databases, focusing
on publication titles, abstracts, and keywords for thorough
coverage of relevant studies.
While the search was restricted to English-language pub-
lications within a specific time frame, the large number
of identified studies reflects the thoroughness of our ap-
proach. A data template was developed to guide informa-
tion collection and reduce extraction bias. Furthermore, two
researchers independently extracted the data, adhering to
PRISMA guidelines to ensure consistency throughout the
process and prevent disagreements.
III. RESULTS AND DISCUSSION
The overview of the initially retrieved database returned
prominent OCR application domains, which are broadly clas-
sified into printed and handwritten OCR. Given the multidis-
ciplinary nature of machine vision, it is clear that machines
encounter various types of text in different languages and
scripts for digitization [41]. OCR research is driven by the
growing demand in fields including automatic data entry
[42], license plate recognition [43], passport verification [35],
reading traffic signs for automated systems [44], managing
traffic flow [45], converting handwriting in pen computing
[46] and text to speech conversion to assist individuals with
vision impairments [47]. The research published throughout
the study period initially focused on OCR model devel-
opment and data preprocessing methods [12]. From 2016
onward, the OCR applications spectrum expanded in hand-
written text recognition [48] and vehicle plate identification
[43]. The subsequent research in OCR focuses on complex
data types and new application domains, as shown in Figure
Figure 5.
Form
Script
Generation
Printed
Handwritten
Latin
Chinese
Arabic…
Graphic
Scene text
Text in images
FIGURE 5: Classification of text types in OCR.
A. AI MODELS IN OCR (RQ1)
Classification models form the core of most OCR systems
[49], with text recognition typically handled using multi-
class classifiers [50]. To analyze the evolution of OCR
models over time, a manual review of the final 97 selected
studies was conducted. Figure 6 presents the temporal trend
analysis of individual models, while Figure 7 illustrates
broader classification trends, grouping OCR models into four
main categories: conventional machine learning models, deep
learning models, transformers, and hybrid models.
1) DOMINANT AND EMERGING DEEP LEARNING
MODELS (CNN, LSTM, GAN, TRANSFORMERS)
Since 2015, CNNs have been widely used in image-based
recognition tasks [31]. Different CNN architectures experi-
enced steady growth and remained dominant until a surge of
handwritten text. LSTM networks gained prominence after
2017 [51] for sequential and bidirectional text. However,
their popularity has slightly declined in recent years, likely
due to the rise of more advanced alternatives. Since 2020,
GANs have attracted increasing attention in OCR research
primarily for their ability to generate realistic synthetic data,
enhance low-quality images, and refine recognition outputs.
Although GANs do not directly perform OCR classification,
they are valuable auxiliary techniques to support other OCR
models [52]. More recently, OCR has been dominated by
Transformer-based deep learning architectures. Since 2020,
Transformers have seen significant growth and have largely
replaced LSTMs in many OCR-related applications [53].
With dynamic feature selection, Transformers are a superior
VOLUME 13, 2025 177651

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
0%
10%
20%
30%
40%
50%
60%
70%
80%
90%
100% 2025
2024
2023
2022
2021
2020
2019
2018
2017
2016
2015
FIGURE 6: Prominent AI models applied to Optical Character Recognition (OCR) over the past decade.
Machine Learning Models
Deep Learning Models
Hybrid Models
----- Hybrid models (can combine and incorporate elements from any layers)
Nested structure: Transformers ⊂ Deep learning ⊂ Machine learning
Autoencoders
Logistic regression
Naïve
Bayes
Decision
trees
Vision Transformer
CharFormer
TrOCR
Transformers
FIGURE 7: Evolution of OCR models architectures in a
decade.
alternative to LSTMs for efficiently recognizing sequential
data like handwritten text.
2) ADAPTIVE AND EVOL VING HYBRID MODELS AND
NEURAL FUZZY SYSTEMS
Hybrid OCR models are important when standalone mod-
els deliver suboptimal results. These models enhance text
recognition by combining different approaches, especially in
cases where a single method is inadequate due to limited
training data or interpretation challenges. When dealing with
distorted or ambiguous text, rule-based techniques refine
predictions. A great example is Neural Fuzzy Systems, which
have gained attention since 2020 for their ability to handle
uncertainty and improve decision-making in complex recog-
nition tasks. By integrating fuzzy logic with other learning
models, these models efficiently process noisy or highly vari-
able text [54]. Hybrid models are prioritized for recognizing
text in languages and scripts with limited training data where
characters can appear in different forms.
3) DECLINING TRADITIONAL MACHINE LEARNING
MODELS
Before 2019, machine learning models like KNN, SVM,
Naïve Bayes, Logistic regression, and statistical models were
widely used in OCR [1], [55]. Their appeal came from their
ability to recognize text even with limited training data.
These models were ideal for early OCR systems when com-
putational resources were scarce and large labeled datasets
were hard to obtain. KNN and SVM are commonly applied
to character recognition due to their strong classification
capabilities, while Naïve Bayes is practical for text-based
OCR. At that time, ANN and MLP, as early neural network-
based models, helped with pattern recognition [1]. At the
same time, logistic regression and statistical models were
also used in rule-based approaches to text segmentation and
classification. These models excelled in OCR on structured,
small-scale datasets where handcrafted features were engi-
neered for specific tasks [56].
However, as OCR tasks grew more complex and the avail-
ability of big data increased, the limitations of traditional ma-
chine learning became evident. These models require exten-
177652 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
sive manual feature engineering, which demands domain ex-
pertise. While they worked well on simple datasets, they en-
countered obstacles with large-scale, high-dimensional data,
when variations in fonts, handwriting styles, and document
layouts introduced complexity beyond their capabilities. As
a result, the reliance on traditional machine learning models
has steadily declined.
B. TRANSITION IN OCR APPLICATIONS SPECTRUM
The applications of OCR reflect the extensive research and
growing popularity of modern OCR systems. Recent research
has oriented towards integrating OCR with advanced AI-
driven applications shown in Figure 8. OCR, which started
with basic document digitization has moved toward a deeper
understanding of documents in healthcare and banking [57].
Now, autonomous systems extract text from real-world
scenes with higher accuracy. On the other hand, multilingual
recognition improves translation for low-resource languages
[58]. Assistive technologies use OCR to support visually im-
paired individuals in reading and navigation [59]. Recently,
multi-modal learning in augmented reality (AR)/virtual real-
ity (VR) has been used for user engagement in an immersive
environment [60]. Advanced research beyond applied models
now addresses complex challenges, broader applications, and
the need for stronger, more adaptable systems [61]. Recent
publications have mainly focused on multilingual, multi-
modal, and high-performance OCR solutions [62].
OCR application
domains
Healthcare
Banking
Autonomous
systems
Assistive
technology
AR/VR recognition
Document
digitization
FIGURE 8: Popular OCR application domains. General do-
mains (blue box) initially focused on document digitization
(green box) and expanded to other domains (orange boxes).
The AI models in OCR research have evolved from tra-
ditional statistical methods to deep learning techniques for
higher performance. The performance of OCR is typically
evaluated using a variety of metrics including accuracy,
precision, recall, F1-score, speed, and specialized metrics
like character error rate (CER) and word error rate (WER).
However, due to the variations in text formats ranging from
individual digits and characters to complete words and sen-
tences, accuracy remains the most consistently reported and
broadly applicable evaluation metric in OCR research. Table
3 presents the reported accuracy values of each model on
different datasets. The minimum and maximum accuracy
values reflect the performance range observed across separate
studies using the same model architecture. These results were
extracted directly from the original papers, without averaging
or statistical aggregation. It is important to note that studies
use various types and amounts of data for training and testing
their methods, pre-process and split datasets in different
ways. Therefore, it is impractical to suggest the best perform-
ing model based on direct comparison. As such, the table
describes the reported performance of each model. Early
models like logistic regression and KNN faced complex
scripts and handwriting challenges [63]. The low accuracy of
conventional machine learning led to the adoption of CNNs
and LSTMs for OCR tasks. Deep learning significantly im-
proved feature extraction and sequence modeling. Hybrid
architectures (CNN-LSTM, CNN-RNN, CNN-YOLO) have
been explored to combine feature extraction and sequence
learning capabilities. It resulted in higher accuracy than
standalone models [64]. However, complexity often increases
training time and computational costs. Hence, it makes them
less feasible for large-scale OCR applications. Hybrid mod-
els combining statistical and deep learning techniques are
proposed in noisy document scenarios [65]. Despite improve-
ments, challenges persist for low-resource languages and
complex scripts because of the limited availability of training
data.
In 2019, CNNs transformed OCR with high accuracy,
while hybrid models like RF-CNN improved flexibility. By
2020, CNNs dominated printed text recognition, with LSTMs
and CNN-LSTM hybrids excelling in sequential data recog-
nition. Lightweight machine learning models still play an
important role in resource-constrained applications. Initially
developed for synthetic data generation, GANs found success
for OCR in low-resource or degraded text scenarios. Their
exceptional data generation feature is beneficial in OCR
when handling incomplete, noisy, or distorted text data [66].
Deep learning-based transformer models have recently
gained prominence for their superior contextual understand-
ing and multilingual capabilities despite their high computa-
tional requirements [67]. Transformers use attention mecha-
nisms to understand character and word relationships. These
models, such as Vision Transformers (ViT) and TrOCR,
have already improved efficiency through direct image-to-
text conversion. AI models using these mechanisms have
achieved an impressive 99.89% accuracy in character recog-
nition [68].
The main difference between conventional machine learn-
ing, conventional deep learning, and transformers is how
they handle data, feature extraction, context, and scalability.
Traditional machine learning models rely on handcrafted fea-
tures and do not inherently capture sequential dependencies
[69]. They perform well on structured data but underperform
with complex patterns in large-scale unstructured data. Con-
ventional deep learning models learn features automatically
but have limitations in processing long-range dependencies.
RNN-based deep learning models like LSTMs handle se-
VOLUME 13, 2025 177653

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
quential data but suffer from vanishing gradients, sequential
bottlenecks, and inefficient scalability [70].
Transformers, in contrast, overcome these challenges with
self-attention, parallel processing, and better long-range de-
pendency capture [71]. Unlike conventional deep learning,
transformers do not rely on recurrence. Hence, they are faster
for OCR tasks that require contextual understanding. How-
ever, this comes at the cost of higher memory consumption
and the need for large datasets for optimal performance [72].
C. PERFORMANCE OF OCR MODELS ON
HETEROGENEOUS DATASETS
When the data is complicated, OCR models evolved from
rule-based and statistical models to deep learning archi-
tectures. As the architectures of AI models contrast, their
accuracy on various datasets differs; therefore, instead of a
direct comparison, a comprehensive assessment of all models
is tabulated in Table 3 for better understanding. Accuracy was
chosen as the primary evaluation metric due to its consistent
reporting in 72% of studies. In contrast, key OCR metrics
such as WER and CER appeared in only 5% and 4% of
studies, respectively. The limited reporting of other metrics
prevented their use in cross-study analysis. In the same way,
presenting an in-depth analysis of popular datasets and data
processing methods merits writing another comprehensive
literature review. From current analysis, it is found that
OCR models are capable of recognizing printed and hand-
written text containing symbols, digits, and characters in
many languages. The performance gap between traditional
and deep learning-based OCR models is evident from the
accuracy range of each model. In SVM model a significant
performance significant performance variation was observed.
The accuracy ranged from 60% to 94% depending on script
complexity, model architecture, hyperparameters, and dataset
characteristics. Overall variation in accuracy indicates SVM
can handle simpler OCR tasks, but its performance de-
grades for complex scripts, handwritten text, or degraded
image quality. Similarly, CNN-based models like VGG16
and CRNN demonstrate consistent performance on printed
text datasets but show notable accuracy drops on handwritten
text due to their inherent limitations in processing sequen-
tial information and character dependencies. Compared to
SVM and ANN-based models, deep learning-based trans-
former models, Vision Transformer (ViT), TrOCR, and Char-
Forme maintain higher accuracy above 77% regardless of the
datasets.
More recent Transformer-based OCR models outperform
CNNs and LSTMs for multilingual and complex-script OCR
due to their self-attention mechanisms. Transformer-based
models achieved high accuracy and demonstrated state-of-
the-art performance for languages with complex diacritics.
Multi-head attention, parallel processing, bidirectional rep-
resentation and self-supervised learning are distinguishing
characteristics of Transformers [97]. However, these models
are computationally expensive as compared to traditional
CNN architectures. For instance, TrOCR [24] uses pre-
trained Vision Transformers for both image encoding and
autoregressive decoding. The base and large versions of
this model contain 334 million and 558 million parameters,
respectively. These sizes are up to 20 times larger than those
of traditional CNN-based models, which typically contain
between 10 million and 50 million parameters. As a result,
memory demand of TrOCR is high with usage ranging from
4 to 16 gigabytes, compared to the 500 megabytes to 2
gigabytes required by CNN-based models. This also leads
to longer inference times, which can range from 100 to
500 milliseconds, whereas CNNs typically perform inference
within 10 to 50 milliseconds. Additionally, the training costs
are considerably higher for TrOCR. Similarly, Donut [98]
avoids traditional OCR pipelines by relying on Transformer-
based architectures. However, it requires over 200 million
parameters and encounters similar computational and mem-
ory challenges. The self-attention mechanism with quadratic
memory complexity necessitates the use of GPUs with at
least 16 gigabytes of VRAM. It also requires a substantially
higher number of floating-point operations per image, rang-
ing from 10 to over 100 gigaflops, compared to the 1 to 10
gigaflops typically required by CNNs. Therefore, the feasi-
bility of transformers in real-time and mobile applications is
limited. For an in-depth comparison between Transformers
and CNNs, along with a detailed exposition of the technical
foundations of Transformer architectures, refer to study [97].
1) CORRELA TION BETWEEN INPUT DA T A AND
GENERALIZA TION OF OCR MODELS
The overall OCR accuracy is driven by several fundamental,
architectural, and universal factors. Apart from the archi-
tecture of the classification model, hybridization, hyperpa-
rameter tuning, data preprocessing steps, training strategies,
and post-processing methods, the ultimate performance of
an OCR system is determined by the dataset complexities.
Existing OCR models underperform in complex dynamic
environments due to the complexity of the background in-
formation of the input data [99]. Pretraining data coverage
is another major factor due to the limited transferability of
pretrained models. Models trained primarily on Latin scripts
may underperform on Arabic, Chinese, or Devanagari scripts
due to differences in text direction (left-to-right vs. right-to-
left), character complexity (e.g., dots, diacritics, and strokes),
and word structure (spaced vs. compound). The reverse is
also true for models trained on non-Latin scripts. Models
trained on varied datasets, including multilingual, handwrit-
ten, or historical documents, tend to generalize better in real-
world scenarios.
Real scene images contain text along with background,
foreground information, and noise. It is challenging to de-
tect, segment, and extract text from low-contrast real scene
images with partial visibility. In addition to degraded images
and noisy backgrounds, real-world OCR tasks frequently
involve more complex visual conditions such as skewed
perspectives, motion blur, occlusion, and multilingual text
appearing within the same scene [67]. These adversarial
177654 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
TABLE 3: Reported accuracy of each OCR model on various datasets from selected studies
Model Type Architecture Datasets Used Text Type / Lan-
guage(s)
Performance (Ac-
curacy)
Strength / Limitation
SVM [73], [1],
[74], [75],
SVM-MLP-ETC, NCC,
HOG-SVM
286 Font Packs, Bangla
Handwritten Dataset
Printed / Handwritten
(English, Bangla)
60.6% - 94.53% Works well for structured fonts
but struggles with handwritten
text and complex scripts
ANN [76], [77],
[78], [79]
Feedforward NN,
Backpropagation NN,
Hopfield-ANN
MNIST, CROHME,
EMNIST, Picture Editor
Dataset
Printed / Handwritten
(English, Arabic)
92% - 100% Effective in basic OCR but
lacks generalization for large-
scale real-world datasets
Neural Fuzzy Sys-
tem [80], [81]
IT2NFS-SPSA, ANFIS Alphabetic and Numeric
Datasets, Burmese OCR
Printed (English,
Burmese)
7.25% - 98.20% Reduces computational cost
compared to traditional fuzzy
systems but limited in scalabil-
ity
CNN [31], [50],
[82]–[85]
VGG16, CRNN, Incep-
tion V3, ResNet50, Multi-
CNN
MJSynth, Kaggle, IAM,
BanglaLekha-Isolated,
CMATERdb, EMNIST
Printed/Handwritten
(English, Arabic,
Tamil, Bangla,
Gujarati, Devanagari)
57.2% - 99.76% Strong for printed OCR, but
struggles with handwritten cur-
sive text and script complexity
LSTM/BLSTM
[51], [14], [86],
[87], [88], [89],
[90], [91], [92],
[93]
Bi-LSTM, Gated-CNN-
BLSTM, Tesseract LSTM
Medical Records,
EMNIST, IAM, BCSD
Long-Sequenced Text
(English, Arabic, Ger-
man, Indonesian)
91% - 99.94% Worked well for long-sequence
text, but require high computa-
tional resources
Transformer [23],
[53], [84], [94]
Vision Transformer (ViT),
TrOCR, CharFormer
Shotor, Sadri, Born-
Digital, LicenseNet
Multilingual
(Chinese, English,
Persian)
77.25% - 99.98% Outperforms CNNs/LSTMs in
multilingual OCR, but compu-
tationally expensive
GAN [65], [66] CycleGAN, SRGAN,
DESRGAN
CASIA HWDB, Synthetic
Data
Noise-Resistant OCR
(Chinese, English)
87.4% - 99.89% Effective for enhancing resolu-
tion of noisy images but prior-
itizes realism over textual cor-
rectness.
Hybrid Models
[19], [95], [96]
CNN-LSTM, CNN-RNN,
CNN-YOLO, Faster R-
CNN
IIIT-HW-Telugu,
CMATERdb, LicenseNet,
CCPD
Printed/Handwritten
(English, Arabic,
Telugu, Chinese)
94.5% - 99.75% Combining different models
improves accuracy. However,
training complexity increases
conditions challenge OCR models when the training data
does not reflect such variability. Several real-scene datasets
like ICDAR robust reading challenge, ICDAR incidental
scene text, Street View Text (SVT), COCO-Text, SynthText,
MJSynth, and TextOCR have been developed to capture the
complexities of multilingual scripts, varied lighting condi-
tions, handwriting variability and natural image distortions.
However, a major limitation of these datasets is the absence
of associated lexicons, which restricts the development and
evaluation of OCR models that rely on language constraints
or post-processing for improved accuracy [27]. The scale
and script diversity in these datasets is limited compared to
the complexity in real unconstrained environments. In such
contexts, OCR accuracy is enhanced by combining domain-
specific data augmentation, advanced feature learning, and
semi-supervised techniques to bridge the gap between con-
trolled training data and uncontrolled real-world inputs [100].
2) CONTEXTUAL SENSITIVITY OF OCR MODELS
The accuracy variations of the same model in different stud-
ies indicate that OCR performance depends on architecture,
training strategy, data coverage, and decoding method. This
includes how well a model’s architecture aligns with the
training design [101]. Earlier OCR systems, based on ma-
chine learning techniques, lacked the flexibility needed for
complex or noisy layouts. While Transformer-based models
show consistent advantages over traditional machine learning
methods and CNN-based architecture for complex images
[102]. The ability to model contextual relationships and long-
range dependencies between characters leads to higher recog-
nition accuracy on multi-column and irregularly formatted
documents [24]. Transformer-based models are suitable for
visually complex or noisy inputs, while CNNs are preferred
in resource-limited environments with high-quality inputs
[103]. Hybrid systems, which combine pretraining, flexible
decoding, and language-aware components, are well-suited
for multilingual or high-accuracy applications such as text
script identification [104]. Data augmentation with geometric
transformations like rotation and perspective changes im-
proves generalization on distorted inputs. Besides geomet-
ric transformations, augmentation strategies such as color
space transformations, kernel filters, mixing images, random
erasing, feature space augmentation, adversarial training,
GAN-based augmentation, neural style transfer, and meta-
learning schemes are good solutions for positional biases
present in the training data [105]. Research suggests that
different models respond differently to different preprocess-
ing steps [106]. Traditional machine learning approaches are
comparatively more reliant on binarization, denoising, skew
correction, feature extraction, and segmentation. Preprocess-
ing reduces input complexity and enhances feature clarity.
Classical models require clean, well-aligned inputs and hand-
crafted features. The performance of these models is strongly
influenced by preprocessing quality, and their generalization
is limited when inputs are noisy or documents deviate from
VOLUME 13, 2025 177655

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
the expected layout. In addition, hyperparameters such as
kernel functions in SVM, the number of neighbors in k-
NN, and decision criteria in tree-based models are manu-
ally selected or externally tuned using techniques like grid
search or cross-validation. These models are also sensitive to
overfitting when trained on very large, very small, or imbal-
anced datasets [107]. In contrast, deep learning models learn
hierarchical feature representations directly from raw input
pixels. Their dependency on manual feature engineering is
limited. However, their performance relies on the availability
of large, well-labeled datasets [100]. Without sufficient data,
deep learning models are prone to overfitting when trained
from scratch. In such cases, data augmentation becomes an
important strategy with techniques such as random rotation,
scaling, contrast shifts, and synthetic noise, etc, to simulate
variability found in real-world documents. Performance of
deep learning models varies with changing training config-
urations. Hyperparameters such as learning rate, optimizer
type, batch size, network depth, and regularization strategies,
for instance, dropout, batch normalization, weight decay, etc.,
influence OCR accuracy [19]. To improve convergence and
generalization in deep learning models, different techniques
such as early stopping, learning rate scheduling, and data
normalization are used. Hybrid models are generally more
robust than a model alone, especially in recognizing text lines
with varying lengths and orientations. However, additional
complexities are introduced during training, including hyper-
parameter choices [108] and sequence length management.
Stabilizing training may require techniques such as gradient
clipping and careful weight initialization. In contrast, the
end-to-end architectures in transformers can model entire
sequences or documents using self-attention mechanisms.
These models learn long-range dependencies and attend to
relevant regions without explicit segmentation or handcrafted
features. They perform well even on inputs with irregular
layouts, noise, or partial occlusions. However, they are highly
dependent on large-scale pretraining, typically on multi-
modal datasets, and fine-tuning on task-specific data. Factors
such as input resolution, tokenization strategy, positional
encoding, and optimizer configurations have a substantial
influence on Transformers [24]. The relative impact of differ-
ent factors on OCR varies, depending on the model family.
Understanding these distinctions is critical when designing
OCR systems for specific tasks or document domains.
D. TEXT SCRIPTS IN OCR RESEARCH (RQ2)
Language is a complex vocabulary, grammar, and phonetics
system while its written counterpart, script is a structured
visual representation. Scripts consist of symbols, letters, or
characters that transcribe spoken language into a readable
format. Interestingly, a single language can be represented
in multiple scripts, just as a single script can be adapted
for different languages. Based on their approach to encoding
linguistic units, scripts are generally classified into three
main categories: alphabetic, syllabic, and logographic [109].
Multilingual OCR research still has a long way to go,
especially compared to how well English is doing. Since
English is resource-rich and works smoothly with most ex-
isting OCR tools, it has been the most used and researched
language. English is one of the most spoken languages in
the world. It is the official language in 53 countries and the
first language for about 400 million people. Many bilingual
speakers also use it to communicate globally. Over the years,
researchers have studied OCR for English more than for
any other language, leading to many published studies [38].
Because of this extensive research, English OCR systems
have greatly improved and are widely used. Today, English
OCR is mature, and its accuracy is high due to extensive
training data, simple character sets, consistent spacing, and
limited diacritics. After English, Arabic is the second most
researched language in OCR. Written right to left, Arabic
features letters that change shape based on position and
diacritics that alter meaning. Complex Arabic script compris-
ing connected characters is challenging for OCR. Similar-
looking letters and variations in handwriting further com-
plicate text recognition. These factors demand specialized
OCR models for accurate processing, and research is being
carried out, too. Although the demand for multilingual OCR
continues to rise, languages with complex scripts have not
advanced at the same pace as those with more straightforward
writing systems. Primarily, it is due to the scarcity of high-
quality datasets and the inherent complexity of the scripts
themselves. The less explored languages, such as Bangla,
Tamil, Telugu, Oriya, Devanagari, Chinese, Gujarati, Ko-
rean, Finnish, Indonesian, Javanese, Uighur, Myanmar, and
Nepali and more lack quality datasets and advanced OCR
solutions. As shown in Figure 9, these languages lag be-
hind English due to limited resources and lower recognition
accuracy. Moreover, their harder-to-process scripts result in
less accurate OCR. There is an apparent necessity to bridge
the gap for the global adoption of OCR by achieving high
accuracy in languages other than English. Further research is
needed to develop more inclusive multilingual OCR models
with enhanced recognition capabilities for underrepresented
languages.
Current research in OCR focuses on improving multilin-
gual script recognition. However, a one-size-fits-all OCR
model is ineffective due to the vast differences in writing
systems. Current script-specific OCR systems are designed
for the unique structural, linguistic, and typographical char-
acteristics of individual scripts. This review explored promi-
nent scripts adopted in OCR research, their unique char-
acteristics, and the languages they support. Representative
samples of the most commonly reported scripts are illustrated
in Figure 10 followed by a brief discussion on prominent
characteristics of each script. The identified features in dif-
ferent scripts sharing some common characteristics can be
used in grouping similar script patterns to apply the same
recognition approaches. This will improve the generalization
performance of OCR models.
177656 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
0
2
4
6
8
10
12
14
16
18
20
2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025
Articles
Year
English
Arabic
Persian
Bangla
Chinese
German
Tamil
Telugu
Nepali
Urdu
Others
FIGURE 9: Trends in language-specific OCR models.
(a) (b)
(c) (d)
FIGURE 10: Sample of printed scripts: (a) Latin, (b) Devanagari, (c) Chinese, and (d) Arabic.
1) LA TIN SCRIPT
The Latin script, also known as the Roman alphabet, has its
roots in the old Italic scripts, which were influenced by the
Greek alphabet and ultimately derived from the Phoenician
script [110]. The Romans standardized it, and it has since
evolved into the world’s most widely used writing system
[111]. It is the foundation for hundreds of languages, includ-
ing English, Spanish, French, German, Italian, Portuguese,
Dutch, Turkish, Vietnamese, and many more [112]. It is the
dominant writing system in Europe, the Americas, parts of
Africa, and certain regions of Asia and Oceania [113]. It
is one of the most versatile and enduring writing systems
in history. Over time, the Latin script has evolved into nu-
merous typographic styles, from simple print fonts to artistic
calligraphy. It consists of a finite set of characters (letters,
numbers, and punctuation) with consistent shapes. Some of
the defining features of the Latin script include its left-to-
right writing direction, the presence of both uppercase (cap-
ital) and lowercase letters, and the explicit representation of
vowels as essential characters. Latin characters have only two
VOLUME 13, 2025 177657

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
forms, uppercase and lowercase, that maintain shape within
a word [71]. Due to these characteristics, the Latin script
is highly compatible with digital processing. Individually
spaced letters are easy to segment and recognize for OCR
models. The Latin script has also been widely standardized
through Unicode encoding for seamless digital representa-
tion.
2) ARABIC SCRIPT
The Arabic alphabetic script, known as the Arabic abjad,
originates from the Nabataean script, which evolved from
Aramaic around the 4th century CE [114]. Over time, it
developed into a highly cursive and adaptable writing system.
It is used for many languages, either as their primary writing
system or as an alternative, including Arabic, Persian, Urdu,
Pashto, Kurdish, Sindhi, Punjabi, Malay (Jawi), Uyghur, and
Hausa. Various languages in the Middle East, North Africa,
South Asia, Central Asia, Southeast Asia, and parts of Africa
are expressed in the Arabic script. Some exceptional charac-
teristics of Arabic script are right-to-left direction, diacritics,
dots, the absence of vowels and capital letters, connected
letters without spacing between them, and a slanted calli-
graphic style. Another distinction of Arabic script is its use
of contextual characters, also called positional variants. In
the Arabic script, letters have four shapes depending on their
position in the word: isolated (complete) form, initial form,
medial form, and final form [115]. Accuracy of Arabic OCR
models is negatively influenced by segmentation errors. To
address the segmentation complexities and shape variations
in Arabic, many systems adopt word-level OCR. Arabic
script-specific preprocessing steps typically involve diacritic
removal, dot normalization, and segmentation into words or
characters. Models such as CNN, RNN, and LSTM have been
used for Arabic OCR on a labeled Quranic text database [50].
Among these, GRU and LSTM-based models have shown
high performance due to the sequential nature of the Arabic
script. To improve the Arabic OCR, postprocessing methods
such as Word Beam Search decoding with dictionaries and
auto-correction using BERT have been proposed [116].
3) CHINESE SCRIPT
The Chinese script, one of the world’s oldest continuously
used writing systems, dates back over 3,000 years to ancient
oracle bone inscriptions [117]. Unlike alphabetic scripts, it is
a logographic writing system where each character represents
a word or a meaningful unit rather than individual sounds.
The script is used primarily for Mandarin, Cantonese, and
other Chinese dialects and has also historically influenced
Japanese, Korean, and Vietnamese writing systems [118].
Today, it is the official script of China, Taiwan, and Singa-
pore, with variations in Simplified Chinese, which is used
in mainland China and Singapore, and Traditional Chinese,
which is used in Taiwan and Hong Kong. Key features
of the Chinese script include its top-to-bottom and left-
to-right writing orientations, the absence of uppercase and
lowercase distinctions, and diacritics. It consists of thou-
sands of unique words made up of strokes and radicals,
which provide clues for meaning and pronunciation. [119].
Although complex, the Chinese script is one of the most
visually attractive and historically significant writing sys-
tems globally. The massive Chinese character set, potentially
containing over 50,000 characters in comprehensive dictio-
naries, is addressed through hierarchical encoding schemes
and transformer architectures with attention mechanisms.
To reduce computational complexity, OCR models employ
multi-stage pipelines. A large number of visually similar ele-
ments and stroke variations (1-30 strokes per character) also
create computational challenges, tackled through multi-scale
feature extraction, attention-based discriminative learning for
subtle stroke differences, and synthetic data augmentation to
improve character distinction. The dual directionality with
horizontal (left-to-right) or vertical (top-to-bottom, right-to-
left) in Chinese text requires adaptive OCR systems. In
literature, it is addressed through orientation-aware detection
algorithms, bidirectional LSTMs for sequence modeling, and
adaptive layout analysis modules in frameworks like Easy-
OCR and PaddleOCR [5].
4) DEVANAGARI SCRIPT
In South Asia, the Devanagari script is one of the most widely
used writing systems. It originates from the Brahmi script and
has been used for over 1,500 years. It is the primary script for
Hindi, Marathi, Nepali, and Sanskrit, among other languages
[63]. The Devanagari script is an abugida, a writing system
that differs from purely alphabetic, logographic, or syllabic
scripts. In Devanagari, each consonant inherently carries a
vowel sound, which can be modified or muted using dia-
critical marks. Unlike alphabetic scripts, where vowels and
consonants are written separately, Devanagari combines them
into a single unit [120]. This script is more structured, but it
is also more complex than a simple alphabet. A distinctive
feature of Devanagari is the horizontal line running along
the top of the characters, which visually connects letters in
a word. The script follows a left-to-right writing direction. It
consists of vowel and consonant characters, diacritical marks,
ligatures, and conjunct forms, where multiple consonants
merge into a single shape. Digital text processing of Devana-
gari script is complicated since characters change form when
combined, and words are written without explicit spacing
between them [121].
Consequently, segmentation of words, characters, and dia-
critical marks is a challenge for OCR on this script. Segmen-
tation methods are broadly divided into implicit (pure seg-
mentation), explicit (recognition-based segmentation), and
holistic (segmentation-free) methods. In Devanagari charac-
ter segmentation, the header line is removed, and characters
in words are divided into three zones: the upper zone, the
middle zone, and the lower zone. However, the performance
of OCR models is significantly reduced due to incorrect
segmentation. Therefore, for the Devanagari script, custom
segmentation algorithms for conjunct handling are proposed.
For accurate Devanagari OCR hybrid models for OCR and
177658 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
post-processing for error correction are recommended [122].
Given the inherently sequential and interconnected structure
of Devanagari characters, Bidirectional LSTM (BiLSTM) is
a more appropriate choice for accurately recognizing this
script [63].
E. KEY CHALLENGES IN ACCURATE OCR SYSTEMS
(RQ3)
A word cloud analysis was performed to identify key ter-
minologies associated with the challenges and limitations
reported in OCR research. Unlike conventional systematic
reviews that primarily rely on titles, abstracts, and keyword-
based filtering, this study adopted a full-text analysis. Con-
sequently, more profound insights into the specific obstacles
encountered in the field are provided as illustrated in Fig-
ure 11.
FIGURE 11: A word cloud of keywords extracted from
literature phrases describing challenges.
The most frequently reported challenges in OCR research
emphasize the ongoing efforts to extract meaningful tex-
tual and visual features from complex, real-world images.
Classification models, background noise, character shape and
size variations, diacritics, low contrast, resolution limita-
tions, and dataset scarcity are commonly discussed issues
that cause persistent accuracy constraints. However, beyond
these well-documented challenges, several less-explored but
equally significant obstacles include glyph variations, dis-
tortion sensitivity, overlapping characters, skewed and tilted
text, shading effects, data imbalance, positioning errors, short
strokes, fragmented text segments, computational inefficien-
cies, overfitting, and punctuation mark recognition. These
challenges bring up gaps in current OCR methodologies and
point to deeper issues in script-specific complexities, lan-
guage adaptability, and model generalization. The presence
of these terms in word cloud feature the urgency to address
these limitations with innovative solutions for advancing
OCR technologies.
As observed, the studies on multi-disciplinary text extrac-
tion exhibited a variety of challenges and limitations that
modern OCR models still face. The challenges reported in
various contexts are broadly categorized into data quality
issues, limitations of AI models (algorithmic challenges),
and resource constraints. Explicitly mentioned limitations are
outlined in Figure 12.
52%
17%
31%
Data
Resources
Models
FIGURE 12: Main sources of challenges in OCR.
Challenges reported in the literature are often problem-
specific and closely linked to individual system designs.
However, these challenges can be broadly categorized into
key problem areas, as illustrated in Figure 13. The identified
challenges are grouped into data, model, and resource con-
straints. Since all main categories are interconnected while
each category is wrapped around multiple subcategories.
Therefore, the primary classification of challenges disregards
their interconnected and multilayered nature. To dig deeper,
the prominent subcategories of challenges associated with
the primary categories are shown in Figure 14. Here, data-
related issues focus on the quality, quantity, and availability
of training data, directly impacting model performance. The
complexity and variability of text, such as different fonts,
handwriting styles, and distortions, add another layer of dif-
ficulty. Model limitations represent the technical constraints
of OCR systems, including accuracy, speed, and complexity.
Besides, latency, adaptability to different text styles, and
the ability to generalize through datasets and languages are
significant hurdles, especially when dealing with noisy real-
world text. Finally, resource constraints are the practical
barriers to deploying OCR systems. Hardware limitations
include energy consumption, memory requirements, band-
width, and connectivity issues. Resource constraints are par-
ticularly critical in edge computing or mobile applications,
where processing power is limited. Collectively, these cat-
egories illustrate the persistent challenges faced by OCR.
Addressing these challenges requires identifying research
gaps for continuous advancements in data processing, model
efficiency, and resource optimization [8]. Since the chal-
lenges identified are potential avenues for future research, a
thorough discussion of these challenges and solutions will be
provided in a subsequent section.
The discussion is followed by targeted solutions for each
challenge and general guidelines for enhancing OCR system
performance in future research. Data quality challenges in-
clude small sample sizes in datasets, insufficient for practical
model training, and low-quality inputs, such as blurriness,
noise, and low contrast. Complex scripts with diacritics and
VOLUME 13, 2025 177659

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
joint characters add to the difficulties, as do fonts, sizes, and
shape variations that affect recognition accuracy. Moreover,
structural problems such as overlapping text and connected
characters make OCR tasks more challenging. Environmen-
tal factors such as changes in lighting and background com-
plexity negatively affect text recognition in natural scenes.
Selecting and optimizing suitable classification algorithms
requires domain-specific knowledge. The architecture of the
model determines accuracy, speed, and adaptability. Com-
plex models can enhance recognition but may increase com-
putational costs and latency, which limit their real-time
performance. A lack of optimal training data required by
the model raises the risk of overfitting and the inability to
generalize to new scripts and fonts. Moreover, similar shapes,
distortions, or noise also complicate feature extraction.
Resource constraints inhibit the evolution of real-time and
embedded OCR applications. Limitations in hardware, such
as processing speed and memory, restrict model deployment
in resource-constrained environments. High energy con-
sumption and optimization issues arise from power efficiency
constraints. The lack of publicly available OCR datasets
limits training samples and reduces model generalization.
Additionally, deep learning model complexity contributes to
high latency and impacts real-time performance.
Multilingual complexity is a growing challenge in OCR
systems where script variations cause misclassifications and
recognition errors. Addressing these challenges requires
high-level data preprocessing techniques, optimized algo-
rithmic strategies, and efficient resource management. The
following sections propose targeted solutions for identified
challenges and present general guidelines for developing
robust OCR systems in the future.
Data Related
Issues
Quality
Quantity
Availability
Complexity
Variability
Algorithmic
Limitations
Accuracy
Speed
Complexity
Latency
Adaptability
Generalization
Resources
Constraints
Hardware
Energy
Memory
Bandwidth
Connectivity
FIGURE 13: Key challenges and limitations in OCR.
The reviewed studies demonstrate substantial progress in
OCR performance in several domains and uncover consistent
shortcomings that limit the broader applicability and relia-
bility of OCR technology. These limitations point to unad-
dressed critical gaps caused by script variability, domain-
specific noise, and generalization on different databases. The
following sections detail these research gaps obtained from
empirical trends and common challenges observed in recent
work.
1) DA T A-RELA TED CHALLENGES
OCR models use supervised learning and primarily depend
on extensive, high-quality labeled training data. A compre-
hensive, well-annotated, and balanced dataset with a suf-
ficient number of examples is vital for achieving optimal
training results. Many existing datasets today are limited in
both size and scope [99]. Uniform datasets are not available
for different languages to equally train OCR models. Training
OCR models on imbalanced datasets does not yield the nec-
essary understanding for adequate generalization. Underfit-
ting OCR models frequently fail when applied to real-world
scenarios. Besides quantity, the quality of training datasets
is an important element of OCR performance. Low-quality
datasets propagate errors, resulting in poor performance even
for strong models [52]. Text data can be quite challeng-
ing for OCR systems to recognize accurately. Unlike typed
English text in clean environments, real-world OCR tasks
involve complex scripts with multiple strokes, diacritics,
connected characters, and glyph structures that are difficult
for models to learn without specialized data. Moreover, many
datasets do not account for challenging conditions like noisy,
low-resolution, or degraded documents. OCR models must
contend with variations in illumination, low contrast, back-
ground clutter, and geometric distortions such as rotated,
tilted, or skewed text. Factors reducing recognition accuracy
are not universal for models to learn from datasets. Similarly,
different scripts have unique annotation practices when it
comes to segmentation. The absence of standardized anno-
tations makes it difficult to train models, compare results,
reproduce findings, and generalize to multilingual datasets.
Continuous retraining is required to enhance performance
and ensure reproducibility. Furthermore, there has been lim-
ited attention given to documents with faded ink, worn-out
characters, or overlapping and slanted text common in histor-
ical archives, handwritten records, and real-world imagery.
Another limitation arises from domain-specific issues present
in each dataset; for example, quality concerns differ between
medical images and banking documents. Moreover, despite
the increasing demand for multilingual OCR systems, there is
a noticeable lack of high-quality datasets containing multiple
scripts or mixed languages [8]. The common data-related
issues, including availability, complexity, image condition,
and text quality, are listed in Figure 14.
2) MODEL-SPECIFIC LIMIT A TIONS AND
COMPUT A TIONAL CONSTRAINTS
Despite significant advancements in OCR technology, there
are several limitations in recognizing complex text structures
and scripts. Challenges associated with adopted models ex-
plicitly reported in the literature are provided in the Table 4
and described in the subsequent section. Key challenges
existing OCR models face include the following:
•Difficulty in handling overlapping, connected handwritten
and cursive scripts.
•High misclassification rates for visually similar characters,
177660 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
TABLE 4: Challenges associated with OCR models
Model Application Challenges Reported References
CNN Multiple studies on various languages
(e.g., Arabic, Bangla, Telugu, Tamil,
Persian, Urdu, Gujarati, Devanagari, Ja-
vanese and Swedish)
Small text size, blurry images, non-horizontal text,
complex character shapes, compound characters, di-
acritics, connected characters, font variations, low-
quality images, and overlapping text.
[4], [16], [82], [85],
[123]–[125]
DNN Studies on OCR for different languages
and document types
High computational cost, large feature matrices,
memory inefficiency, data imbalance, and difficulty in
recognizing handwritten text.
[17], [126], [127]
LSTM Studies on handwritten OCR, license
plate recognition, and document pro-
cessing
Similar character shapes, joint characters, varying
orientations, illumination conditions, font and back-
ground variations, and computational resource limita-
tions.
[51], [88]–[90],
[128]–[135]
SVM Printed Arabic OCR and Bangla OCR
studies
Feature extraction challenges, low contrast images,
and difficulty handling multiple font types.
[73], [136], [137]
ANN Language-oriented OCR implementa-
tions for Arabic, Persian, and Nepali
scripts
Image quality issues, font variations, low resolution,
and complex background interference.
[77], [138]–[142]
Hybrid Models (CNN +
LSTM, SVM + MLP, etc.)
Studies assessed ensemble approaches
for OCR
Overfitting, increased training time, high memory re-
quirements, and difficulty optimizing network layers.
[23], [54], [84], [96],
[125], [143]–[145]
GAN-based Models Studies on OCR for character separation
and text denoising
Complex backgrounds, overlapping text, and varia-
tions in stroke thickness.
[65], [146]
Transformer-based Models
(TrOCR, ViT-OCR, etc.)
Studies on printed and handwritten
OCR
Poor generalization for different languages, computa-
tional complexity, and model fine-tuning challenges.
[53], [147], [148]
Data-related challenges
Script complexity
Image condition Text quality
Dataset availability
Dotted or slanted scripts
Diacritics
Glyphs structure
Connected characters
Overlapping text
Pixelated characters
Noisy text
Faded text
Lighting
Occlusions/obstructions
Complex natural scenes
Tilt/ rotation/ skew
Low contrast
Limited benchmark  data
Limited multilingual data
Underrepresented scripts
Annotation limitations
FIGURE 14: Data related challenges in OCR.
such as ’O’ and ’0’ or ’2’ and ’z’ lead to reduced recogni-
tion accuracy.
•Ineffective segmentation techniques for complex layouts,
handwritten scripts, and multi-column documents, result-
ing in fragmented or incorrect text extraction.
•Deep learning models suffer from overfitting and ineffi-
ciencies when trained on small or unbalanced datasets.
•Lack of adaptive OCR architectures to handle script, font,
and language variations.
Deploying OCR systems on mobile, edge, and embedded
devices often encounters computational challenges. A few
frequently reported computational challenges are listed be-
low:
•Real-time OCR is impractical for resource-limited embed-
ded systems due to high power consumption and process-
ing overhead.
•Limited lightweight and optimized models are available for
mobile and edge computing environments.
•Balancing accuracy, speed, and computational efficiency
are challenging when optimizing deep learning architec-
tures.
Understanding these collective challenges is essential for
identifying research gaps. These gaps reveal where current
models are deficient and what issues are holding back further
progress. Tackling these issues is about making real advance-
ments that push OCR models forward. The following section
explores possible solutions and future directions to develop
more adaptable and powerful OCR systems.
F . OCR ENHANCEMENT STRATEGIES (RQ3)
Advanced strategies such as transformer-based architectures,
self-supervised learning, and adaptive preprocessing methods
are recommended for handling handwritten, complex, and
cursive text recognition to enhance OCR performance fur-
ther. Additionally, multi-modal learning, data augmentation,
and GAN-based de-noising techniques should be integrated
to mitigate challenges related to low resolution, distortions,
and background interference [149]. Identified issues, existing
solutions, the limitations associated with the existing meth-
ods, and future directions to overcome the challenges are in
Figure 15.
For specialized applications such as license plate and
scene text recognition, domain-adaptive learning, improved
segmentation, and multi-frame fusion methods can be ex-
plicitly applied to handle variations in lighting conditions
and motion blur. Post-processing techniques, including NLP-
driven context-aware correction, hybrid dictionary-based re-
finement, and ensemble OCR models, are suggested to en-
VOLUME 13, 2025 177661

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
Challenges
Multilingual
complexity
Handwriting
issues
Noisy images
Limited dataset
Existing solutions
(Limitations)
Transformer
models (high
cost)
CNN-BLSTM
(struggles with
cursive)
GAN-based
enhancement
(unreliable)
Synthetic data
(poor
generalization)
Future directions
Lightweight
Transformers
Hybrid CNN-
Transformers
Improved GAN
architectures
Self supervised
learning
FIGURE 15: Frequently reported challenges, existing solutions, their limitations, and future directions to overcome these issues.
hance recognition accuracy. Furthermore, AutoML frame-
works, hybrid deep learning models, and continual learning
strategies should be explored for dynamic model adaptation
without extensive manual tuning. OCR is a multi-stage pro-
cess involving data preprocessing, character recognition, and
post-recognition refinement. Accuracy enhancement tech-
niques are systematically integrated during all stages of OCR
development. These techniques can be broadly categorized
into three key strategies: data-centric, model-oriented, and
output refinement.
1) DA T A-CENTRIC STRA TEGIES
A significant portion of OCR research focuses on improving
input data quality to enhance recognition accuracy. Prepro-
cessing techniques are widely employed to mitigate varia-
tions in lighting, resolution, and geometric distortions [126].
Data-centric strategies in OCR are developed to improve
input image quality with preprocessing. It ultimately con-
tributes to the accuracy and processing speed of OCR mod-
els. Unlike traditional model-centric approaches that refine
OCR architectures, data-centric methods emphasize intelli-
gent preprocessing, adaptive data augmentation, and efficient
dataset curation to optimize recognition performance. Ex-
isting preprocessing techniques, such as binarization, noise
reduction, contrast enhancement, and geometric correction
[126], have been widely used to address common challenges
like poor lighting, distortions, and low resolution. However,
preprocessing techniques are image- and case-specific and do
not benefit images uniformly.
In the future, automated and flexible preprocessing
pipelines can be developed to adjust data dynamically ac-
cording to the characteristics of each image. Moreover,
deep learning-based enhancement techniques, such as super-
resolution reconstruction and adaptive denoising, can im-
prove text clarity without relying on fixed parameters [146].
Additionally, self-learning preprocessing frameworks, where
models iteratively refine image quality based on OCR confi-
dence scores, could enhance accuracy.
2) MODEL-ORIENTED STRA TEGIES
Apart from input quality, OCR accuracy is ultimately deter-
mined by the ability of the recognition model to classify char-
acters and words correctly. Model-oriented strategies focus
on enhancing OCR systems through two primary approaches,
model selection and optimization. first, the most suitable
model is identified considering accuracy and computational
efficiency. Then OCR models are fine-tuned by adjusting
hyper-parameters, and employing suitable feature extraction
techniques.
Model-oriented strategies in the literature still use do-
main knowledge for model selection and conventional opti-
mization techniques for hyper-parameters tuning [108]. We
suggest automating these model selection and optimization
strategies simultaneously using AutoML. It can streamline
the selection of the most efficient OCR architectures and
hyperparameters using AI.
3) OUTPUT REFINEMENT STRA TEGIES
Despite improvements in preprocessing and model archi-
tecture, OCR outputs contain residual errors, commonly
in complex text environments. Post-recognition refinement
strategies correct misclassified characters and contextual in-
177662 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
consistencies to improve the reliability of the extracted text.
Primary types of post-processing techniques include lexi-
con driven methods that correct OCR errors by referenc-
ing domain-specific dictionaries. Algorithm-based methods
refine OCR predictions based on contextual understanding.
Several computational models such as sequence-to-sequence
(Seq2Seq) networks, topic-based language models, and prob-
abilistic error correction algorithms are utilized. Besides,
integrating domain-aware lexicons and language modeling
techniques improve text recognition accuracy [7].
4) AI INTEGRA TED SYSTEMS
In recent years, OCR technology has moved from traditional
image processing pipelines to more advanced, integrated
systems that combine multiple areas of machine intelligence.
Figure 16 shows the main stages of this development. The
years indicate when each approach saw the most attention in
literature and broad use, not necessarily when it was first in-
troduced. Early OCR systems focused on low-level pixel op-
erations, but over time, they grew into more capable systems
that can interpret both visual and textual information. Their
performance improved further as methods from computer
vision, natural language processing (NLP), large language
models (LLMs), and contextual reasoning were brought to-
gether. Introduced by Google, PaLM-E demonstrated mul-
timodal characteristics beyond conventional pipelines with
embodied AI to interpret text within broader visual and
semantic contexts [150]. Along similar lines, transformer-
based design of TrOCR established a standard approach
of end-to-end learning, which mitigated the dependence on
separate text detection and recognition. The same trend
continued in LayoutLMv3, which combines visual, textual,
and structural features through cross-modal attention. This
combined OCR model is efficient for complex layouts like
tables, forms, and mixed-content documents [24]. A few new
scene-text detection models, such as CLIP4STR, PARSeq,
and ABINet, apply vision-language pretraining and iterative
correction for more reliable OCR in real-world conditions.
Outside the main timeline, other important developments
include DONUT, an image encode-text-decoder, which skips
OCR entirely for document parsing [151]; Nougat, designed
specifically for scientific documents; and BERT-based sys-
tems that extend document understanding through language
modeling [152]. Most recently, systems like GPT-4 Vision,
Claude 3 Opus, and Gemini Pro Vision bring OCR into the
zero-shot era for recognizing and interpreting text in unfa-
miliar domains and languages without task-specific training
[153]. These models blur the line between OCR and general
AI, and appear to be moving toward systems that not only
extract text but also understand its visual, linguistic, and
contextual framework. While recent OCR models exhibit
broader language understanding and some level of cross-
domain capability, several improvements are needed in real-
world applications. There is still no unified system that
performs consistently well on heterogeneous document types
and languages. Contextual understanding is limited for long
Multimodal language models
PaLM-E
• Multimodal capabilities
• Language understanding
• Vision
TrOCR
• End-to-end learning
• Vision transformer
• Pretrained models
Transformer-based OCR systems
LayoutLMv3
• Layout understanding
• Cross-modal attention
• Document intelligence
Unified document understanding
MuLTI
• Self-supervision
• Cross-lingual transfer
• Script diversity
Multilingual support
Scene text recognition
CLIP4STR
• Robustness
• Attention mechanisms
• Context understanding
GPT-4
• Integrated language models
• Generalization
• Cross-domain adaptation
Zero-shot  and few-shot OCR
2023 2023-
2024
2024 2024
2024-
2025 2025
FIGURE 16: Recent advancements in integrated systems for
OCR.
documents. Most models also lack support for incremental
learning and on-device adaptability. Future research should
explore building multimodal OCR systems that can jointly
process text, layout, and visual features. Addressing script
diversity will require developing multilingual and multiscript
models using self-supervised and cross-lingual learning. Fur-
ther progress is needed in context-aware OCR using memory-
augmented transformers. Models should be designed to gen-
eralize well in zero-shot settings while adapting to new do-
mains and tasks. As OCR systems are widely adopted, protect
user privacy with federated learning needs to be prioritized.
G. FUTURE RESEARCH DIRECTIONS (RQ3)
1) ADVANCED LEARNING APPROACHES FOR
L0W-RESOURCE LANGUAGES
OCR on low-resource scripts is due to insufficient training
data, which limits the ability of OCR models to general-
ize well. To address the dataset limitations, self-supervised
learning (SSL) [20] and few-shot learning (FSL) [154] can
be promising alternatives for extracting meaningful patterns
from unlabeled text data. These techniques enhance recogni-
tion accuracy with minimal reliance on annotated datasets.
Consequently, they reduce the need for extensive manual
labeling. By integrating SSL and FSL, OCR systems can
become more adaptable and resilient. In this way, text recog-
nition can be more accessible to languages with scarce digital
resources.
2) OPTIMIZED ARCHITECTURES FOR REAL-TIME
APPLICA TIONS
While transformers have significantly advanced OCR perfor-
mance, their computational cost is a key limitation for real-
time deployment. Research on efficient transformer variants
such as MobileViT and TinyBERT can improve model scal-
ability without compromising accuracy [53]. Quantization,
knowledge distillation, and pruning techniques can further
reduce model size and inference time [155], making OCR
viable for mobile and embedded systems.
VOLUME 13, 2025 177663

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
3) ADVANCED IMAGE ENHANCEMENT TECHNIQUES
Noisy and low-resolution images are one of the key obstacles
to OCR accuracy. Future research should focus on GANs for
document enhancement. Super-resolution GANs (SRGAN,
DESRGAN) can reconstruct degraded text, mitigate back-
ground noise, and enhance text clarity to improve recognition
performance in challenging real-world environments.
An important prerequisite for achieving high OCR accu-
racy is the completeness and legibility of both training and
inference data [156]. In many real-world scenarios, parts of
the textual information may be missing or corrupted. Unlike
traditional enhancement filters that only modify existing pix-
els, GANs can generate entirely new image content based on
learned patterns [66]. Through adversarial training, GANs
produce high-quality reconstructions with lifelike features
that are sufficiently realistic to fool the discriminator network
[5].
With semantic understanding, GANs are capable of recon-
structing contextually appropriate character structures. They
address both local character-level missing information and
global document-level quality issues simultaneously [157].
In contrast to conventional methods, GANs learn the data
distribution and hallucinate plausible structures in place
of missing or degraded regions. Consequently, GAN-based
methods can restore broken license plates [149] obscured by
dirt or weathering [158], reconnect incomplete pen strokes in
handwritten text [159], recover damaged or faded characters
in historical documents [160], [161], infer obscured portions
of text hidden by ink smearing (ink blots) [162], [163] and
overlapping objects in scene text images [164]. For challeng-
ing images with noise or missing information, GAN-based
preprocessing for simultaneous data cleaning, repairing, fill-
ing, and reconstruction instead of simple image enhancement
is expected to overcome the limitations of traditional prepro-
cessing techniques. A comprehensive comparison of GAN
with traditional popular data-centric approaches, including
Bilateral filter, Contrast-limited adaptive histogram equal-
ization (CLAHE) [165], Otsu thresholding [106], Gaussian
blur [166], Unsharp mask [167], Morphological operations
(Morphological Ops), and Wavelet transform is provided in
Table 5.
IV . CONCLUSION
The evolution of AI models for Optical Character Recog-
nition (OCR) has led to remarkable improvements in text
recognition accuracy. Yet, significant challenges persist in
handling complex scripts, handwritten text, and real-world
noisy environments. This systematic review analyzed 97
research articles from seven major scholarly databases to
present a structured examination of OCR progress over the
past decade. It investigated the evolution of OCR models,
the expansion of application domains, the increasing com-
plexity of dataset types, and the continuous improvements in
accuracy. Through a PRISMA-based methodology, this study
examined the transition from traditional machine learning
techniques (KNN, RF, SVM) to deep learning-based archi-
tectures, including CNNs, LSTMs, GANs, and Transformers,
which have significantly enhanced OCR performance. This
review explores advancements and highlights critical gaps
in OCR research. The main challenges fall into three areas:
data limitations, algorithmic constraints, and computational
demands.
To address these issues, we propose targeted solutions.
Techniques such as transfer learning and self-supervised
learning can enhance model generalization, while multi-
modal AI and integrated data sources help mitigate data
scarcity. For improved accuracy, the use of advanced pre-
trained models is recommended to refine OCR outputs at
the character level. This survey provides valuable insights
for both industry and academia. The identified research gaps
and suggested solutions are expected to accelerate the de-
velopment of fast, reliable, and multilingual AI-driven OCR
systems.
ACKNOWLEDGMENT
The authors extend their gratitude to UTM for providing
invaluable support.
TABLE 5: Comparison of traditional image enhancement techniques and GAN-based methods. (✓= Supported,✗= Not
supported,◦= Limited support)
Enhancement Capability Bilateral
Filter
CLAHE Otsu
Thresh-
olding
Gaussian
Blur
Unsharp
Mask
Morph.
Ops
Wavelet
Transf.
GAN
Methods
Noise Reduction✓✗ ✗◦✗ ✗✓ ✓
Contrast Enhancement✗✓✗◦✗ ✗ ✗✓
Resolution Enhancement✗ ✗ ✗ ✗ ✗ ✗ ✗✓
Blur Removal✗ ✗ ✗◦✓✗ ✗✓
Artifact Removal✗ ✗ ✗ ✗ ✗ ✗ ✗✓
Illumination Correction✗✓✗ ✗ ✗ ✗ ✗✓
Data Generation✗ ✗ ✗ ✗ ✗ ✗ ✗✓
Multi-degradation
Handling
✗ ✗ ✗ ✗ ✗ ✗ ✗✓
Semantic Understanding✗ ✗ ✗ ✗ ✗ ✗ ✗✓
Adaptive Processing✗ ✗ ✗ ✗ ✗ ✗ ✗✓
177664 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
REFERENCES
[1] L. Abhishek, “Optical character recognition using ensemble of svm, mlp
and extra trees classifier,” in 2020 International Conference for Emerging
Technology (INCET). IEEE, 2020, pp. 1–4.
[2] M. H. A. Abdullah, N. Aziz, S. J. Abdulkadir, H. S. A. Alhussian, and
N. Talpur, “Systematic literature review of information extraction from
textual data: recent methods, applications, trends, and challenges,” IEEE
Access, vol. 11, pp. 10 535–10 562, 2023.
[3] C. Thorat, A. Bhat, P. Sawant, I. Bartakke, and S. Shirsath, “A detailed re-
view on text extraction using optical character recognition,” ICT Analysis
and Applications, pp. 719–728, 2022.
[4] S. Drobac and K. Lindén, “Optical character recognition with neural
networks and post-correction with finite state methods,” International
Journal on Document Analysis and Recognition (IJDAR), vol. 23, no. 4,
pp. 279–295, 2020.
[5] L. Kopitar, P. Kocbek, L. Gosak, and G. Stiglic, “Review of data-driven
generative ai models for knowledge extraction from scientific literature in
healthcare,” in Next Generation eHealth. Elsevier, 2025, pp. 127–146.
[6] I. A. Khandokar and P. Deshpande, “Computer vision-based framework
for data extraction from heterogeneous financial tables: A comprehensive
approach to unlocking financial insights,” IEEE Access, 2024.
[7] S. Karthikeyan, A. G. S. de Herrera, F. Doctor, and A. Mirza, “An ocr
post-correction approach using deep learning for processing medical re-
ports,” IEEE Transactions on Circuits and Systems for Video Technology,
vol. 32, no. 5, pp. 2574–2581, 2021.
[8] A. Naseer, M. Tamoor, N. Allheeib, and S. Kanwal, “Investigating
the taxonomy of character recognition systems: A systematic literature
review,” IEEE Access, 2024.
[9] D. Baviskar, S. Ahirrao, V . Potdar, and K. Kotecha, “Efficient automated
processing of the unstructured documents using artificial intelligence: A
systematic literature review and future directions,” IEEE Access, vol. 9,
pp. 72 894–72 936, 2021.
[10] P. Ruangraweenukit, P. Khambun, T. Nupim, P. Chophuk, A. Onuean,
and A. Saengsai, “Autonomous drive-through system using easyocr and
dobot,” in 2024 IEEE International Symposium on Consumer Technol-
ogy (ISCT). IEEE, 2024, pp. 497–502.
[11] R. K. Singh, A. K. Saxena, A. Jhapate, R. Shrivastava, and R. Srivastava,
“Review on advanced vehicle recognition system: Ocr and rest api inte-
gration for efficient results,” in 2024 IEEE International Conference on
Computing, Power and Communication Technologies (IC2PCT), vol. 5.
IEEE, 2024, pp. 95–100.
[12] N. H. Imam, V . G. Vassilakis, and D. Kolovos, “Ocr post-correction for
detecting adversarial text images,” Journal of Information Security and
Applications, vol. 66, p. 103170, 2022.
[13] A. Almutairi, “Newspaper elements detection and newspaper pages
categorization using cnns and transformers,” International Journal on
Document Analysis and Recognition (IJDAR), pp. 1–13, 2024.
[14] M. S. H. Onim, H. Nyeem, K. Roy, M. Hasan, A. Ishmam, M. A. H.
Akif, and T. B. Ovi, “Blpnet: A new dnn model and bengali ocr engine
for automatic licence plate recognition,” Array, vol. 15, p. 100244, 2022.
[15] T. T. H. Nguyen, A. Jatowt, M. Coustaty, and A. Doucet, “Survey of post-
ocr processing approaches,” ACM Computing Surveys (CSUR), vol. 54,
no. 6, pp. 1–37, 2021.
[16] S. Ahlawat, A. Choudhary, A. Nayyar, S. Singh, and B. Yoon, “Improved
handwritten digit recognition using convolutional neural networks (cnn),”
Sensors, vol. 20, no. 12, p. 3344, 2020.
[17] H. Chaitanyaswami and A. Dobariya, “Deep learning recurrent attention
optical character recognition network with data augmentation for cheque
data extraction,” in 2023 International Conference on Computer, Elec-
tronics & Electrical Engineering & their Applications (IC2E3). IEEE,
2023, pp. 1–6.
[18] H. Wang, C. Pan, X. Guo, C. Ji, and K. Deng, “From object detection
to text detection and recognition: A brief evolution history of optical
character recognition,” Wiley Interdisciplinary Reviews: Computational
Statistics, vol. 13, no. 5, p. e1547, 2021.
[19] A. Choudhury and K. K. Sarma, “A cnn-lstm based ensemble framework
for in-air handwritten assamese character recognition,” Multimedia Tools
and Applications, vol. 80, no. 28, pp. 35 649–35 684, 2021.
[20] J. Gui, T. Chen, J. Zhang, Q. Cao, Z. Sun, H. Luo, and D. Tao, “A survey
on self-supervised learning: Algorithms, applications, and future trends,”
IEEE Transactions on Pattern Analysis and Machine Intelligence, 2024.
[21] H. Zhang, E. Whittaker, and I. Kitagishi, “Extending trocr for text
localization-free ocr of full-page scanned receipt images,” in Proceedings
of the IEEE/CVF International Conference on Computer Vision, 2023,
pp. 1479–1485.
[22] F. Xue, J. Sun, Y . Xue, Q. Wu, L. Zhu, X. Chang, and S.-c. Cheung,
“Attention guidance by cross-domain supervision signals for scene text
recognition,” IEEE Transactions on Image Processing, 2025.
[23] D. Shi, X. Diao, L. Shi, H. Tang, Y . Chi, C. Li, and H. Xu, “Charformer:
A glyph fusion based attentive framework for high-precision character
image denoising,” in Proceedings of the 30th ACM international confer-
ence on multimedia, 2022, pp. 1147–1155.
[24] M. Li, T. Lv, J. Chen, L. Cui, Y . Lu, D. Florencio, C. Zhang, Z. Li,
and F. Wei, “Trocr: Transformer-based optical character recognition with
pre-trained models,” in Proceedings of the AAAI conference on artificial
intelligence, vol. 37, no. 11, 2023, pp. 13 094–13 102.
[25] H. M. Balaha, H. A. Ali, and M. Badawy, “Automatic recognition of
handwritten arabic characters: a comprehensive review,” Neural Comput-
ing and Applications, vol. 33, pp. 3011–3034, 2021.
[26] K. Nikolaidou, M. Seuret, H. Mokayed, and M. Liwicki, “A survey of
historical document image datasets,” International Journal on Document
Analysis and Recognition (IJDAR), vol. 25, no. 4, pp. 305–338, 2022.
[27] X. Chen, L. Jin, Y . Zhu, C. Luo, and T. Wang, “Text recognition in the
wild: A survey,” ACM Computing Surveys (CSUR), vol. 54, no. 2, pp.
1–35, 2021.
[28] S. Saeed, S. Naz, and M. I. Razzak, “An application of deep learning
in character recognition: an overview,” Handbook of Deep Learning
Applications, pp. 53–81, 2019.
[29] J. Fields, K. Chovanec, and P. Madiraju, “A survey of text classification
with transformers: How wide? how large? how long? how accurate? how
expensive? how safe?” IEEE Access, vol. 12, pp. 6518–6531, 2024.
[30] M. Pandey, M. Arora, S. Arora, C. Goyal, V . K. Gera, and H. Yadav, “Ai-
based integrated approach for the development of intelligent document
management system (idms),” Procedia Computer Science, vol. 230, pp.
725–736, 2023.
[31] S. B. Suthar and A. R. Thakkar, “Cnn-based optical character recogni-
tion for isolated printed gujarati characters and handwritten numerals,”
International Journal of Mathematical, Engineering and Management
Sciences, vol. 7, no. 5, p. 643, 2022.
[32] M. Sobhi, Y . Hifny, and S. Mesbah Elkaffas, “Arabic optical character
recognition using attention based encoder-decoder architecture,” in 2020
2nd International Conference on Artificial Intelligence, Robotics and
Control, 2020, pp. 1–5.
[33] C. Ziyan and L. Shiguo, “China’s self-driving car legislation study,”
Computer Law & Security Review, vol. 41, p. 105555, 2021.
[34] A. Alaei, V . Bui, D. Doermann, and U. Pal, “Document image quality
assessment: A survey,” ACM computing surveys, vol. 56, no. 2, pp. 1–
36, 2023.
[35] S. Chakrabarti, H. Singh, D. Yadav, and P. Rana, “Authentication system
combining optical character recognition and error level analysis,” in 2024
Asia Pacific Conference on Innovation in Technology (APCIT). IEEE,
2024, pp. 1–8.
[36] M. Petticrew and H. Roberts, Systematic reviews in the social sciences:
A practical guide. John Wiley & Sons, 2008.
[37] D. Peral-García, J. Cruz-Benito, and F. J. García-Peñalvo, “Systematic
literature review: Quantum machine learning and its applications,” Com-
puter Science Review, vol. 51, p. 100619, 2024.
[38] J. Memon, M. Sami, R. A. Khan, and M. Uddin, “Handwritten optical
character recognition (ocr): A comprehensive systematic literature review
(slr),” IEEE access, vol. 8, pp. 142 642–142 668, 2020.
[39] A. Ampatzoglou, S. Bibi, P. Avgeriou, M. Verbeek, and A. Chatzi-
georgiou, “Identifying, categorizing and mitigating threats to validity
in software engineering secondary studies,” Information and Software
Technology, vol. 106, pp. 201–230, 2019.
[40] X. Zhou, Y . Jin, H. Zhang, S. Li, and X. Huang, “A map of threats to
validity of systematic literature reviews in software engineering,” in 2016
23rd Asia-Pacific Software Engineering Conference (APSEC). IEEE,
2016, pp. 153–160.
[41] M. A. K. Raiaan, M. S. H. Mukta, K. Fatema, N. M. Fahad, S. Sakib,
M. M. J. Mim, J. Ahmad, M. E. Ali, and S. Azam, “A review on large
language models: Architectures, applications, taxonomies, open issues
and challenges,” IEEE access, vol. 12, pp. 26 839–26 874, 2024.
[42] H. T. Ha and A. Horák, “Information extraction from scanned invoice
images using text analysis and layout features,” Signal Processing: Image
Communication, vol. 102, p. 116601, 2022.
VOLUME 13, 2025 177665

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
[43] S. M. Silva and C. R. Jung, “Real-time license plate detection and
recognition using deep convolutional neural networks,” Journal of Visual
Communication and Image Representation, vol. 71, p. 102773, 2020.
[44] D. Sirohi, N. Kumar, and P. S. Rana, “Convolutional neural networks
for 5g-enabled intelligent transportation system: A systematic review,”
Computer Communications, vol. 153, pp. 459–498, 2020.
[45] M. Anedda, M. Fadda, R. Girau, G. Pau, and D. Giusto, “A social
smart city for public and private mobility: A real case study,” Computer
Networks, vol. 220, p. 109464, 2023.
[46] M. A. Alzubaidi, M. Otoom, and N. S. Ahmad, “Real-time assistive
reader pen for arabic language,” ACM Transactions on Asian and Low-
Resource Language Information Processing (TALLIP), vol. 20, no. 1, pp.
1–30, 2021.
[47] V . P. Revelli, G. Sharma et al., “Automate extraction of braille text to
speech from an image,” Advances in Engineering Software, vol. 172, p.
103180, 2022.
[48] R. Najam and S. Faizullah, “A scarce dataset for ancient arabic handwrit-
ten text recognition,” Data in Brief, vol. 56, p. 110813, 2024.
[49] D. Das, D. R. Nayak, R. Dash, and B. Majhi, “Mjcn: Multi-objective jaya
convolutional network for handwritten optical character recognition,”
Multimedia Tools and Applications, vol. 79, no. 43, pp. 33 023–33 042,
2020.
[50] M. Mohd, F. Qamar, I. Al-Sheikh, and R. Salah, “Quranic optical text
recognition using deep learning models,” IEEE Access, vol. 9, pp.
38 318–38 330, 2021.
[51] Y . Zou, Y . Zhang, J. Yan, X. Jiang, T. Huang, H. Fan, and Z. Cui, “A
robust license plate recognition model based on bi-lstm,” IEEE Access,
vol. 8, pp. 211 630–211 641, 2020.
[52] V . Agrawal, J. Jagtap, and M. P. Kantipudi, “Exploration of advancements
in handwritten document recognition techniques,” Intelligent Systems
with Applications, p. 200358, 2024.
[53] A. Azadbakht, S. R. Kheradpisheh, and H. Farahani, “Multipath vit ocr:
A lightweight visual transformer-based license plate optical character
recognition,” in 2022 12th International Conference on Computer and
Knowledge Engineering (ICCKE). IEEE, 2022, pp. 092–095.
[54] A. T. Sahlol, M. Abd Elaziz, M. A. Al-Qaness, and S. Kim, “Handwritten
arabic optical character recognition approach based on hybrid whale
optimization algorithm with neighborhood rough set,” IEEE Access,
vol. 8, pp. 23 011–23 021, 2020.
[55] A. Raj, “An optical character recognition of machine printed oriya script,”
in 2015 Third International Conference on Image Information Processing
(ICIIP). IEEE, 2015, pp. 543–547.
[56] A. W. Mahastama and L. D. Krisnawati, “Optical character recognition
for printed javanese script using projection profile segmentation and
nearest centroid classifier,” in 2020 Asia Conference on Computers and
Communications (ACCC). IEEE, 2020, pp. 52–56.
[57] S. A. Francis and M. Sangeetha, “A comparison study on optical character
recognition models in mathematical equations and in any language,”
Results in Control and Optimization, p. 100532, 2025.
[58] A. Ghafoor, A. S. Imran, S. M. Daudpota, Z. Kastrati, R. Batra, M. A.
Wani et al., “The impact of translating resource-rich datasets to low-
resource languages through multi-lingual text processing,” IEEE Access,
vol. 9, pp. 124 478–124 490, 2021.
[59] M. P. Arakeri, N. Keerthana, M. Madhura, A. Sankar, and T. Munnavar,
“Assistive technology for the visually impaired using computer vision,”
in 2018 International Conference on Advances in Computing, Communi-
cations and Informatics (ICACCI). IEEE, 2018, pp. 1725–1730.
[60] J. Cao, K.-Y . Lam, L.-H. Lee, X. Liu, P. Hui, and X. Su, “Mobile
augmented reality: User interfaces, frameworks, and intelligence,” ACM
Computing Surveys, vol. 55, no. 9, pp. 1–36, 2023.
[61] S. V . Mahadevkar, S. Patil, K. Kotecha, L. W. Soong, and T. Choudhury,
“Exploring ai-driven approaches for unstructured document analysis and
future horizons,” Journal of Big Data, vol. 11, no. 1, p. 92, 2024.
[62] F. Sanfilippo, T. Blažauskas, M. Girdži ¯una, A. Janonis, E. Kiudys, and
G. Salvietti, “A multi-modal auditory-visual-tactile e-learning frame-
work,” in International conference on intelligent technologies and appli-
cations. Springer, 2021, pp. 119–131.
[63] S. Arora, L. Malik, S. Goyal, D. Bhattacharjee, M. Nasipuri, and O. Kre-
jcar, “Devanagari character recognition: A comprehensive literature re-
view,” IEEE Access, 2024.
[64] S. Hangaragi, P. B. Pati, and N. Neelima, “Accuracy comparison of neural
models for spelling correction in handwriting ocr data,” in Proceedings
of Fourth International Conference on Communication, Computing and
Electronics Systems: ICCCES 2022. Springer, 2023, pp. 229–239.
[65] B. Huang, J. Lin, J. Liu, J. Chen, J. Zhang, Y . Hu, E. Chen, and
J. Yan, “Separating chinese character from noisy background using gan,”
Wireless Communications and Mobile Computing, vol. 2021, no. 1, p.
9922017, 2021.
[66] H. Ibrahim, O. M. Fahmy, and M. A. Elattar, “License plate image
analysis empowered by generative adversarial neural networks (gans),”
IEEE Access, vol. 10, pp. 30 846–30 857, 2022.
[67] P. Xu, X. Zhu, and D. A. Clifton, “Multimodal learning with trans-
formers: A survey,” IEEE Transactions on Pattern Analysis and Machine
Intelligence, vol. 45, no. 10, pp. 12 113–12 132, 2023.
[68] P. Kumar, R. L. Babu, G. Sunil, J. Sampathkumar, and S. Chakraborty,
“Attention-based deep learning algorithm in natural language processing
for optical character recognition,” in 2023 International Conference on
Evolutionary Algorithms and Soft Computing Techniques (EASCT).
IEEE, 2023, pp. 1–5.
[69] Z. Azam, M. M. Islam, and M. N. Huda, “Comparative analysis of
intrusion detection systems and machine learning-based model analysis
through decision tree,” IEEE Access, vol. 11, pp. 80 348–80 391, 2023.
[70] S. F. Ahmed, M. S. B. Alam, M. Hassan, M. R. Rozbu, T. Ishtiak,
N. Rafa, M. Mofijur, A. Shawkat Ali, and A. H. Gandomi, “Deep learning
modelling techniques: current progress, applications, advantages, and
challenges,” Artificial Intelligence Review, vol. 56, no. 11, pp. 13 521–
13 617, 2023.
[71] C. Gu and S. A. Manan, “Transliterated multilingualism/globalisation:
English disguised in non-latin linguistic landscapes as new type of world
englishes?” International Journal of Applied Linguistics, vol. 34, no. 3,
pp. 1183–1204, 2024.
[72] A. Mortadi, A. Mohamed, A. Talima, A. Alkhattip, A. Ibrahim, A. Os-
man, and Y . Hifny, “Alnasikh: an arabic ocr system based on transform-
ers,” in 2023 International Mobile, Intelligent, and Ubiquitous Comput-
ing Conference (MIUCC). IEEE, 2023, pp. 74–81.
[73] O. J. Yamina, M. El Mamoun, and S. Kaddour, “Printed arabic optical
character recognition using support vector machine,” in 2017 Interna-
tional Conference on Mathematics and Information Technology (ICMIT).
IEEE, 2017, pp. 134–140.
[74] M. Das and M. Panda, “An ensemble method of feature selection and
classification of odia characters,” in 2021 1st Odisha international con-
ference on electrical power engineering, communication and computing
technology (ODICON). IEEE, 2021, pp. 1–6.
[75] M. R. Phangtriastu, J. Harefa, and D. F. Tanoto, “Comparison between
neural network and support vector machine in optical character recogni-
tion,” Procedia computer science, vol. 116, pp. 351–357, 2017.
[76] Y . Jing, B. Youssefi, M. Mirhassani, and R. Muscedere, “An efficient
fpga implementation of optical character recognition for license plate
recognition,” in 2017 IEEE 30th Canadian Conference on Electrical and
Computer Engineering (CCECE). IEEE, 2017, pp. 1–4.
[77] S. Afroge, B. Ahmed, and F. Mahmud, “Optical character recognition
using back propagation neural network,” in 2016 2nd International
Conference on Electrical, Computer & Telecommunication Engineering
(ICECTE). IEEE, 2016, pp. 1–4.
[78] R. S. Hussien, A. A. Elkhidir, and M. G. Elnourani, “Optical charac-
ter recognition of arabic handwritten characters using neural network,”
in 2015 International Conference on Computing, Control, Networking,
Electronics and Embedded Systems Engineering (ICCNEEE). IEEE,
2015, pp. 456–461.
[79] J. Lee, B. W. Yogatama, and H. Christian, “Optical character recogni-
tion for handwritten mathematical expressions in educational humanoid
robots,” in 2018 IEEE 8th International Conference on System Engineer-
ing and Technology (ICSET). IEEE, 2018, pp. 178–183.
[80] S. Bhyrapuneni and A. Rajendran, “A comparative analysis for optical
character recognition for text extraction from images using artificial
neural network fuzzy inference system.” Traitement du Signal, vol. 39,
no. 1, 2022.
[81] C. M. M. Maung et al., “Myanmar optical character recognition using
block definition and featured approach,” in 2017 3rd International Con-
ference on Science in Information Technology (ICSITech). IEEE, 2017,
pp. 313–318.
[82] R. Busa, K. Shahira, and A. Lijiya, “Small text extraction from docu-
ments and chart images,” in 2022 IEEE 19th India Council International
Conference (INDICON). IEEE, 2022, pp. 1–5.
[83] A. Shukla, A. Sharma, A. Aggarwal, and S. Jain, “Devnagari char-
acter recognition using optical character recognition (ocr),” in 2023
International Conference on Computational Intelligence, Communication
Technology and Networking (CICTN). IEEE, 2023, pp. 373–379.
177666 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
[84] M. A. Zaryab and C. R. Ng, “Optical character recognition for medical
records digitization with deep learning,” in 2023 IEEE International
Conference on Image Processing (ICIP). IEEE, 2023, pp. 3260–3263.
[85] B. Dessai and A. Patil, “A deep learning approach for optical character
recognition of handwritten devanagari script,” in 2019 2nd international
conference on intelligent computing, instrumentation and control tech-
nologies (ICICICT), vol. 1. IEEE, 2019, pp. 1160–1165.
[86] J. Singh and B. Bhushan, “Real time indian license plate detection using
deep neural networks and optical character recognition using lstm tesser-
act,” in 2019 international conference on computing, communication, and
intelligent systems (ICCCIS). IEEE, 2019, pp. 347–352.
[87] G. Serhan, D. Parker, G. Dhruv, F. Alexander, and A. Ali, “Gpu-based
and streaming-enabled implementation of pre-processing flow towards
enhancing optical character recognition accuracy and efficiency,” Cluster
Computing, vol. 26, no. 6, pp. 3407–3419, 2023.
[88] M. Wasan et al., “Development of text extraction technique using optical
character recognition and morphological reconstruction to eliminate ar-
tifacts of image’s background,” Eastern-European Journal of Enterprise
Technologies, vol. 1, no. 2, p. 115, 2022.
[89] S. Gener, P. Dattilo, D. Gajaria, A. Fusco, and A. Akoglu, “Gpgpu-
based high throughput image pre-processing towards large-scale optical
character recognition,” in 2022 IEEE/ACS 19th International Conference
on Computer Systems and Applications (AICCSA). IEEE, 2022, pp.
1–7.
[90] N. Alamsyah, M. N. Fauzan, A. G. Putrada, and S. F. Pane, “Autoencoder
image denoising to increase optical character recognition performance in
text conversion,” in 2022 International Conference on Advanced Creative
Networks and Intelligent Systems (ICACNIS). IEEE, 2022, pp. 1–6.
[91] D. Scazzoli, G. Bartezzaghi, D. Uysal, M. Magarini, M. Melacini, and
M. Marcon, “Usage of hough transform for expiry date extraction via
optical character recognition,” in 2019 Advances in Science and Engi-
neering Technology International Conferences (ASET). IEEE, 2019,
pp. 1–6.
[92] D. Akinbade, A. O. Ogunde, M. O. Odim, and B. O. Oguntunde, “An
adaptive thresholding algorithm-based optical character recognition sys-
tem for information extraction in complex images,” Journal of Computer
Science, vol. 16, no. 6, pp. 784–801, 2020.
[93] Y . Yanfi, H. Soeparno, R. Setiawan, and W. Budiharto, “Multi-head
attention based bidirectional lstm for spelling error detection in the
indonesian language,” IEEE Access, 2024.
[94] A. Rakshit, S. Mehta, and A. Dasgupta, “A novel pipeline for improv-
ing optical character recognition through post-processing using natural
language processing,” in 2023 IEEE Guwahati Subsection Conference
(GCON). IEEE, 2023, pp. 01–06.
[95] S. R. Dhanikonda, P. Sowjanya, M. L. Ramanaiah, R. Joshi, B. Kr-
ishna Mohan, D. Dhabliya, and N. K. Raja, “An efficient deep learning
model with interrelated tagging prototype with segmentation for telugu
optical character recognition,” Scientific Programming, vol. 2022, no. 1,
p. 1059004, 2022.
[96] Z. Zhao, M. Jiang, S. Guo, Z. Wang, F. Chao, and K. C. Tan, “Improving
deep learning based optical character recognition via neural architecture
search,” in 2020 IEEE Congress on Evolutionary Computation (CEC).
IEEE, 2020, pp. 1–7.
[97] S. Khan, M. Naseer, M. Hayat, S. W. Zamir, F. S. Khan, and M. Shah,
“Transformers in vision: A survey,” ACM computing surveys (CSUR),
vol. 54, no. 10s, pp. 1–41, 2022.
[98] G. Kim, T. Hong, M. Yim, J. Nam, J. Park, J. Yim, W. Hwang, S. Yun,
D. Han, and S. Park, “Ocr-free document understanding transformer,” in
European Conference on Computer Vision. Springer, 2022, pp. 498–
517.
[99] K. Tzoumpas, A. Estrada, P. Miraglio, and P. Zambelli, “A data filling
methodology for time series based on cnn and (bi) lstm neural networks,”
IEEE Access, vol. 12, pp. 31 443–31 460, 2024.
[100] H. Gbada, K. Kalti, and M. A. Mahjoub, “Deep learning approaches
for information extraction from visually rich documents: Datasets, chal-
lenges and methods,” International Journal on Document Analysis and
Recognition (IJDAR), vol. 28, no. 1, pp. 121–142, 2025.
[101] J. Martínek, L. Lenc, and P. Král, “Building an efficient ocr system for
historical documents with little training data,” Neural Computing and
Applications, vol. 32, no. 23, pp. 17 209–17 227, 2020.
[102] R. Anand, A. Rath, P. K. Sahoo, P. Jain, G. Panda, X. Wang, and H. Liu,
“Winograd transform based fast detection of heart disease using ecg
signals and chest x-ray images,” IEEE Access, 2025.
[103] Y . Aliyu, A. Sarlan, K. U. Danyaro, A. S. B. Rahman, and M. Abdullahi,
“Sentiment analysis in low-resource settings: a comprehensive review
of approaches, languages, and data sources,” IEEE Access, vol. 12, pp.
66 883–66 909, 2024.
[104] Y . Yang, E. Eli, A. Aysa, and K. Ubul, “Script identification in mul-
tilingual environment: a survey in recent years,” Artificial Intelligence
Review, vol. 58, no. 10, p. 294, 2025.
[105] C. Shorten and T. M. Khoshgoftaar, “A survey on image data augmenta-
tion for deep learning,” Journal of big data, vol. 6, no. 1, pp. 1–48, 2019.
[106] M. Amiriebrahimabadi, Z. Rouhi, and N. Mansouri, “A comprehensive
survey of multi-level thresholding segmentation methods for image pro-
cessing,” Archives of Computational Methods in Engineering, vol. 31,
no. 6, pp. 3647–3697, 2024.
[107] K. Sharifani and M. Amini, “Machine learning and deep learning: A
review of methods and applications,” World Information Technology and
Engineering Journal, vol. 10, no. 07, pp. 3897–3904, 2023.
[108] L. Liao, H. Li, W. Shang, and L. Ma, “An empirical study of the impact
of hyperparameter tuning and model optimization on the performance
properties of deep neural networks,” ACM Transactions on Software
Engineering and Methodology (TOSEM), vol. 31, no. 3, pp. 1–40, 2022.
[109] S. Kuester-Gruber, T. Faisst, V . Schick, G. Righetti, C. Braun, A. Cordey-
Henke, M. Klosinski, C.-C. Sun, and S. Trauzettel-Klosinski, “Is learning
a logographic script easier than reading an alphabetic script for german
children with dyslexia?” Plos one, vol. 18, no. 2, p. e0282200, 2023.
[110] C. Burlacu and A. Rabus, “Digitising (romanian) cyrillic using tran-
skribus: new perspectives.” Diacronia, no. 14, 2021.
[111] T. Asselborn, W. Johal, B. Tleubayev, Z. Zhexenova, P. Dillenbourg,
C. McBride, and A. Sandygulova, “The transferability of handwriting
skills: from the cyrillic to the latin alphabet,” npj Science of Learning,
vol. 6, no. 1, p. 6, 2021.
[112] Z. Byambadorj, R. Nishimura, A. Ayush, and N. Kitaoka, “Normalization
of transliterated mongolian words using seq2seq model with limited
data,” Transactions on Asian and Low-Resource Language Information
Processing, vol. 20, no. 6, pp. 1–19, 2021.
[113] F. Lebsanft and F. Tacke, Manual of standardization in the Romance
languages. Walter de Gruyter GmbH & Co KG, 2020, vol. 24.
[114] B. Gruendler, The development of the Arabic scripts: From the Nabatean
era to the first Islamic century. Brill, 2019, vol. 43.
[115] E. F. Bilgin Tasdemir, “Printed ottoman text recognition using synthetic
data and data augmentation,” International Journal on Document Analy-
sis and Recognition (IJDAR), vol. 26, no. 3, pp. 273–287, 2023.
[116] R. Krithiga, S. Varsini, R. G. Joshua, and C. O. Kumar, “Ancient character
recognition: a comprehensive review,” IEEE Access, 2023.
[117] Z. Liu, “Optical character recognition and the smart ancient script
database,” Journal of Chinese Writing Systems, vol. 4, no. 4, pp. 255–
269, 2020.
[118] Y . Liang and Z. Li, Diversity and Inclusiveness in Chinese as a Second
Language Education. Taylor & Francis, 2025.
[119] Z. Handel, Sinography: The borrowing and adaptation of the Chinese
script. Brill, 2019, vol. 1.
[120] N. Gautam, S. S. Chai, and M. Gautam, “The dataset for printed brahmi
word recognition,” in Micro-Electronics and Telecommunication Engi-
neering: Proceedings of 3rd ICMETE 2019. Springer, 2020, pp. 125–
133.
[121] S. Singh, N. K. Garg, and M. Kumar, “Feature extraction and classifi-
cation techniques for handwritten devanagari text recognition: a survey,”
Multimedia Tools and Applications, vol. 82, no. 1, pp. 747–775, 2023.
[122] S. K. Manocha and P. Tewari, “Comparative study of deep learning mod-
els for devanagari ocr,” in 2021 International Conference on Smart Gener-
ation Computing, Communication and Networking (SMART GENCON).
IEEE, 2021, pp. 1–7.
[123] S. M. Darwish and K. O. Elzoghaly, “An enhanced offline printed arabic
ocr model based on bio-inspired fuzzy classifier,” IEEE Access, vol. 8,
pp. 117 770–117 781, 2020.
[124] N. M. Dipu, S. A. Shohan, and K. Salam, “Bangla optical character recog-
nition (ocr) using deep learning based image classification algorithms,”
in 2021 24th International Conference on Computer and Information
Technology (ICCIT). IEEE, 2021, pp. 1–5.
[125] Z. Khosrobeigi, H. Veisi, E. Hoseinzade, and H. Shabanian, “Persian
optical character recognition using deep bidirectional long short-term
memory,” Applied Sciences, vol. 12, no. 22, p. 11760, 2022.
[126] T. C. Wei, U. Sheikh, and A. A.-H. Ab Rahman, “Improved optical
character recognition with deep neural network,” in 2018 IEEE 14th
VOLUME 13, 2025 177667

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
international colloquium on signal processing & its applications (CSPA).
IEEE, 2018, pp. 245–249.
[127] X. Zhang, H. Ma, H. Zhao, and R. Wang, “Optical character recognition
of electrical equipment nameplate with contrast enhancement,” in 2022
Power System and Green Energy Conference (PSGEC). IEEE, 2022,
pp. 1062–1066.
[128] M. Brisinello, R. Grbi ´c, M. Pul, and T. An ¯deli´c, “Improving optical
character recognition performance for low quality images,” in 2017
International Symposium ELMAR. IEEE, 2017, pp. 167–171.
[129] K. Charan and T. Pramod, “Optical character recognition system of
telugu language characters using convolutional neural networks,” in
Emerging Research in Computing, Information, Communication and
Applications: Proceedings of ERCICA 2022. Springer, 2022, pp. 615–
623.
[130] A. Arora and A. Chandratre, “Optical character recognition for handwrit-
ten forms with dynamic layout,” in 2018 4th International Conference
on Applied and Theoretical Computing and Communication Technology
(iCATccT). IEEE, 2018, pp. 299–303.
[131] M. Andersson, S. Kanwal, and F. Khan, “Cognitive-inspired post-
processing of optical character recognition for swedish addresses,” in
2022 IEEE 21st International Conference on Cognitive Informatics &
Cognitive Computing (ICCI* CC). IEEE, 2022, pp. 248–257.
[132] F. M. Rusli, K. A. Adhiguna, and H. Irawan, “Indonesian id card
extractor using optical character recognition and natural language post-
processing,” in 2021 9th International Conference on Information and
Communication Technology (ICoICT). IEEE, 2021, pp. 621–626.
[133] U. Kumaran, D. Biswas, B. Sneha, S. Nadipalli, S. Raja et al., “Text post-
processing on optical character recognition output using natural language
processing methods,” in 2023 IEEE 3rd Mysore Sub Section International
Conference (MysuruCon). IEEE, 2023, pp. 1–6.
[134] D. G. Vidakis and D. I. Kosmopoulos, “Facilitation of air traffic control
via optical character recognition-based aircraft registration number ex-
traction,” IET intelligent transport systems, vol. 12, no. 8, pp. 965–975,
2018.
[135] P. Ramya, T. H. Chowdary, P. K. Teja, and T. Hrushikesh, “Number
plate recognition using optical character recognition (oca) and connected
component analysis (cca),” in Smart Technologies in Data Science and
Communication: Proceedings of SMART-DSC 2022. Springer, 2023,
pp. 29–40.
[136] S. L. Gomes, E. d. S. Rebouças, E. C. Neto, J. P. Papa, V . H. d. Albu-
querque, P. P. Rebouças Filho, and J. M. R. Tavares, “Embedded real-
time speed limit sign recognition using image processing and machine
learning techniques,” Neural Computing and Applications, vol. 28, no.
Suppl 1, pp. 573–584, 2017.
[137] M. T. Pervin, S. Afroge, and A. Huq, “A feature fusion based optical
character recognition of bangla characters using support vector machine,”
in 2017 3rd international conference on electrical information and com-
munication technology (EICT). IEEE, 2017, pp. 1–6.
[138] M. Rajkumar, I. Chandra, S. J. Ganesh, K. Dhivya, and K. Sangeetha-
lakshmi, “Smart vehicle number plate scanning system using optical
character recognition strategy,” in 2022 6th International Conference on
Computing Methodologies and Communication (ICCMC). IEEE, 2022,
pp. 1328–1334.
[139] A. Singh and S. Desai, “Optical character recognition using template
matching and back propagation algorithm,” in 2016 International Con-
ference on Inventive Computation Technologies (ICICT), vol. 3. IEEE,
2016, pp. 1–6.
[140] M. I. Yap, K. Moorthy, K. M. Daud, and F. Ernawan, “Optical character
recognition using backpropagation neural network for handwritten digit
characters,” in 2021 International Conference on Software Engineering &
Computer Systems and 4th International Conference on Computational
Science and Information Management (ICSECS-ICOCSIM). IEEE,
2021, pp. 167–171.
[141] M. K. Sharma and B. Bhattarai, “Optical character recognition system for
nepali language using convnet,” in Proceedings of the 9th International
Conference on Machine Learning and Computing, 2017, pp. 184–189.
[142] C.-C. Chang, A. Arora, L. P. G. Perera, D. Etter, D. Povey, and S. Khu-
danpur, “Optical character recognition with chinese and korean character
decomposition,” in 2019 International Conference on Document Analysis
and Recognition Workshops (ICDARW), vol. 5. IEEE, 2019, pp. 134–
139.
[143] P. Georgieva and P. Zhang, “Optical character recognition for au-
tonomous stores,” in 2020 IEEE 10th International Conference on In-
telligent Systems (IS). IEEE, 2020, pp. 69–75.
[144] A. Chandra and R. Stefanus, “An end-to-end optical character recognition
pipeline for indonesian identity card,” in 2021 9th International Confer-
ence on Information and Communication Technology (ICoICT). IEEE,
2021, pp. 307–312.
[145] K. Eghbali, H. Veisi, M. Mirzaie, and Y . M. Behbahani, “Font recognition
for persian optical character recognition system,” in 2017 10th Iranian
Conference on Machine Vision and Image Processing (MVIP). IEEE,
2017, pp. 252–257.
[146] A. C. Luna, C. Trajano, J. P. So, N. J. Pascua, A. Magpantay, and
S. Ambat, “License plate recognition for stolen vehicles using optical
character recognition,” in ICT Analysis and Applications. Springer,
2022, pp. 575–583.
[147] F. Asadi-Zeydabadi, E. Shabaninia, H. Nezamabadi-Pour, and M. Sho-
jaee, “Farsi optical character recognition using a transformer-based
model,” in 2023 13th International Conference on Computer and Knowl-
edge Engineering (ICCKE). IEEE, 2023, pp. 293–299.
[148] W. Zou, X. Sun, W. Wu, Q. Lu, X. Zhao, Q. Bo, and J. Yan, “Tcmt:
Target-oriented cross modal transformer for multimodal aspect-based
sentiment analysis,” Expert Systems with Applications, vol. 264, p.
125818, 2025.
[149] Y . Pan, J. Tang, and T. Tjahjadi, “Lpsrgan: Generative adversarial net-
works for super-resolution of license plate image,” Neurocomputing, vol.
580, p. 127426, 2024.
[150] W. Gao and G. Li, “Point cloud-language multi-modal learning,” in Deep
Learning for 3D Point Clouds. Springer, 2024, pp. 227–254.
[151] A. Sassioui, R. Benouini, Y . El Ouargui, M. El Kamili, M. Chergui, and
M. Ouzzif, “Visually-rich document understanding: concepts, taxonomy
and challenges,” in 2023 10th International Conference on Wireless
Networks and Mobile Communications (WINCOM). IEEE, 2023, pp.
1–7.
[152] Q. Zhang, F. Liu, and W. Song, “Imtlm-net: improved multi-task trans-
former based on localization mechanism network for handwritten english
text recognition,” Complex & Intelligent Systems, vol. 11, no. 1, p. 125,
2025.
[153] J. Wang, Y . Ming, Z. Shi, V . Vineet, X. Wang, S. Li, and N. Joshi, “Is a
picture worth a thousand words? delving into spatial reasoning for vision
language models,” Advances in Neural Information Processing Systems,
vol. 37, pp. 75 392–75 421, 2024.
[154] H. Gharoun, F. Momenifar, F. Chen, and A. H. Gandomi, “Meta-learning
approaches for few-shot learning: A survey of recent advances,” ACM
Computing Surveys, vol. 56, no. 12, pp. 1–41, 2024.
[155] J. Kim, “Quantization robust pruning with knowledge distillation,” IEEE
Access, vol. 11, pp. 26 419–26 426, 2023.
[156] C. Neudecker, K. Baierer, M. Gerber, C. Clausner, A. Antonacopoulos,
and S. Pletschacher, “A survey of ocr evaluation tools and metrics,” in
Proceedings of the 6th International Workshop on Historical Document
Imaging and Processing, 2021, pp. 13–18.
[157] X. Li, J. Jin, Y . Zhou, Y . Zhang, P. Zhang, Y . Zhu, and Z. Dou, “From
matching to generation: A survey on generative information retrieval,”
ACM Transactions on Information Systems, vol. 43, no. 3, pp. 1–62,
2025.
[158] A. Pattanaik and R. C. Balabantaray, “Enhancement of license plate
recognition performance using xception with mish activation function,”
Multimedia tools and applications, vol. 82, no. 11, pp. 16 793–16 815,
2023.
[159] M. Ayyoob and P. M. Ilyas, “Stroke-based data augmentation for enhanc-
ing optical character recognition of ancient handwritten scripts,” IEEE
Access, 2024.
[160] M. A. Souibgui and Y . Kessentini, “De-gan: A conditional generative
adversarial network for document enhancement,” IEEE Transactions on
Pattern Analysis and Machine Intelligence, vol. 44, no. 3, pp. 1180–1191,
2020.
[161] U. Saha, S. Saha, S. A. Fattah, and M. Saquib, “Npix2cpix: A gan-
based image-to-image translation network with retrieval-classification
integration for watermark retrieval from historical document images,”
IEEE Access, 2024.
[162] W. Alkendi, F. Gechter, L. Heyberger, and C. Guyeux, “Unsupervised
approach to text line extraction in belfort civil registers of births,”
International Journal on Document Analysis and Recognition (IJDAR),
pp. 1–22, 2024.
[163] O. Kodym and M. Hradiš, “Tg 2: text-guided transformer gan for restor-
ing document readability and perceived quality,” International Journal on
Document Analysis and Recognition (IJDAR), vol. 25, no. 1, pp. 15–28,
2022.
177668 VOLUME 13, 2025

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
[164] Y . Cheema, M. N. Cheema, A. Nazir, F. A. Khokhar, P. Li, and A. Ahmed,
“A novel approach for improving open scene text translation with modi-
fied gan,” The Visual Computer, pp. 1–13, 2024.
[165] P. Musa, F. Al Rafi, and M. Lamsani, “A review: Contrast-limited
adaptive histogram equalization (clahe) methods to help the application
of face recognition,” in 2018 third international conference on informatics
and computing (ICIC). IEEE, 2018, pp. 1–6.
[166] Y .-Q. Liu, X. Du, H.-L. Shen, and S.-J. Chen, “Estimating generalized
gaussian blur kernels for out-of-focus image deblurring,” IEEE Transac-
tions on circuits and systems for video technology, vol. 31, no. 3, pp.
829–843, 2020.
[167] N. K. Shine, G. Bhutani, T. S. Keerthana, and G. Rohith, “An approach
for improving optical character recognition using contrast enhancement
technique,” in Journal of Physics: Conference Series, vol. 2466, no. 1.
IOP Publishing, 2023, p. 012009.
NUZHA T KHANis a Postdoctoral Research Fel-
low at the VLSI and Embedded Computing Ar-
chitecture Design Laboratory (VeCAD Lab), Uni-
versiti Teknologi Malaysia (UTM). She completed
her Ph.D. in Environmental Technology at Univer-
siti Sains Malaysia (USM) in 2023. She earned her
M.S. in Information Technology from Balochis-
tan University of Information Technology, Engi-
neering, and Management Sciences (BUITEMS),
Pakistan, in 2019 under the Higher Education
Commission (HEC) Scholarship. Her research focuses on optical character
recognition (OCR), image processing, natural language processing (NLP),
artificial intelligence (AI), machine learning, deep learning, applied and
statistical linguistics, and precision agriculture. She has authored multiple
research papers, completed projects, and holds patents in these domains.
She is a technical committee member for the ICEST 2025 conference.
She serves as a reviewer for several reputed journals, including Pattern
Recognition, Genetic Resources and Crop Evolution, Artificial Intelligence
Review, Scientific Reports, Theoretical and Applied Climatology, Journal of
Oil Palm Research, Discover Applied Sciences, Cluster Computing, and the
Journal of Big Data, among others.
AB AL-HADI AB RAHMANPhD, SMIEEE,
MIET, CEng, PEng, is the Head of the Research
Group at the VLSI and Embedded Computing Ar-
chitecture Design (VeCAD) Laboratory, Faculty
of Electrical Engineering, Universiti Teknologi
Malaysia (UTM). He is also an Associate Profes-
sor in the Department of Electronic and Computer
Engineering at UTM. Dr. Ab Al-Hadi holds pro-
fessional affiliations as a Senior Member of the
IEEE (SMIEEE), a Member of the Institution of
Engineering and Technology (MIET), a Chartered Engineer (CEng), and a
Professional Engineer (PEng). His research interests include VLSI design,
embedded systems, computer architecture, and high-performance comput-
ing. He has published extensively in high-impact journals and conferences.
He leads several research projects focused on advanced computing and
embedded system technologies. He also holds two patents in the related area.
IBRAHIM YOUSEF ALSHAREEFis pursuing
his Ph.D. in Artificial Intelligence at Universiti
Teknologi Malaysia (UTM). He holds a bachelor’s
degree in industrial electronics and automatic con-
trol from the College of Electronics and Commu-
nications and a Master’s in Embedded Software
Engineering from Gannon University, USA. His
research interests include deep neural networks,
electronics, and embedded systems, focusing on
optimizing computational efficiency and perfor-
mance in artificial intelligence applications.
SHAHRIY AR MASUD RIZVIis an Associate
Professor in the Department of Electrical and
Electronic Engineering and a Deputy Director
at the Center for VLSI and Embedded Systems,
Dr. Anwarul Abedin Institute of Innovation at
the American International University-Bangladesh
(AIUB). He received his BS and MS degrees in
Electrical Engineering (EE) in 2000 and 2002,
respectively, from the University of Wyoming,
WY , USA. He obtained his Ph.D. in EE in 2023
from the Universiti Teknologi Malaysia (UTM), Johor Bahru, Malaysia.
His research interests include low-complexity and energy-efficient deep
learning, optical character recognition (OCR), synthesis methodologies for
behavioral FSMs modeled in SystemVerilog/VHDL, and hardware/software
co-simulation for FPGA-based image processing. He also serves as a re-
viewer for the Scopus-indexed AIUB Journal of Science and Engineering
(AJSE) and numerous international conferences.
MUHAMMAD NADZIR MARSONOis an Elec-
tronics and Computer Engineering Professor at
Universiti Teknologi Malaysia (UTM). He serves
as Deputy Dean (Academic and Student Affairs)
at the Faculty of Electrical Engineering. He is
also a member of the VeCAD research group.
His research focuses on domain-specific comput-
ing architecture, VLSI/SoC design, and embedded
systems. His interests span digital system design,
computer architecture, reconfigurable computing,
multicore/manycore SoCs, NoCs, network algorithmics, network process-
ing, and software-defined networks. He holds a PhD from the University of
Victoria, Canada, and an MEng degree from UTM.
MUHAMMAD P AEND BAKHTreceived the
Ph.D. degree in electrical engineering from the
Universiti Teknologi Malaysia (UTM). He is cur-
rently an Assistant Professor in the Department of
Electrical Engineering at Balochistan University
of Information Technology, Engineering and Man-
agement Sciences (BUITEMS), Quetta, Pakistan.
He has also gained postdoctoral research expe-
rience at Universiti Tun Hussein Onn Malaysia
(UTHM). He has authored several research articles
in reputable journals and presented his research ideas at international confer-
ences. His research interests include optimization and energy management
of grid-connected renewable energy systems, Artificial Intelligence, and
predictive modeling. His current research at Teagasc, Ireland, focuses on
the integration of renewable energy technologies in agriculture.
VOLUME 13, 2025 177669

Khanet al.: Systematic Literature Review of Machine Learning Models and Applications for T ext Recognition
MOHD SHAHRIZAL RUSLIreceived his PhD,
MEng. and BEng. in electrical engineering from
Universiti Teknologi Malaysia (UTM), Malaysia.
During his doctoral study, he attended the Uni-
versity of California Irvine, USA, and the Uni-
versity of Catania, Italy, as a research scholar.
His research interests are network-on-chip, com-
puter architecture, machine learning accelerators
and power management. He has published in nu-
merous journals, proceedings, and book chapters.
From 2021 to 2022, he was a SoC design engineer at Mediatek Singapore,
working on interconnect design and timing closure. He is a senior lecturer
of Electronic and Computer Engineering, UTM, and a researcher for VLSI
and Embedded Computing Architecture Design (VeCAD) Research Group.
SHAHIDA TUL SADIAH(Member, IEEE) re-
ceived a B.Eng. degree in communication net-
work engineering and an M.Eng. degree in elec-
tronic and information system engineering from
Okayama University, Japan, in 2013 and 2015,
respectively, and a Ph.D. degree in information
engineering from Hiroshima University, Japan, in
2018. She has been a senior lecturer with the De-
partment of Electronics and Computer Engineer-
ing, Universiti Teknologi Malaysia, since January
2019. Her research interests include cryptography, information security,
digital system design, and computer architecture.
177670 VOLUME 13, 2025
