---
title: Artificial intelligence embeddedness in marketing
url: https://doi.org/10.1007/s44362-025-00020-7
category: ai-marketing
subcategory: theory
date: 2025-12
venue: Journal of Digital Management
authors:
- Shanji Yao
- Zi-yi Wei
- Zhuang Wan
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44362-025-00020-7.pdf
pages: 17
chars: 85776
fetched_at: '2026-11-08T17:56:16+00:00'
kb_version: 1
---

# Artificial intelligence embeddedness in marketing

REVIEW Open Access
Journal of Digital
Management
© The Author(s) 2025. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and
the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included
in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will
need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p  : / /  c r e a  t i  v e c  o m m  o n s .  o r  g / l i c e n s e s / b y / 4 . 0 /.
Yao et al. Journal of Digital Management            (2025) 1:17
https://doi.org/10.1007/s44362-025-00020-7
From a strategic standpoint, the application of AI in
marketing is gaining increasing significance. Leading cor-
porations such as Google, Amazon, Microsoft, and Intel
are harnessing AI technologies to enhance their perfor -
mance (Ramadan, 2021; Choudrie et al., 2023). Conse -
quently, AI is recognized as a pivotal technology in the
business world, with its market projected to expand from
$10.1  billion in 2018 to $126  billion by 2025. Although
the study of the synergy between employees and AI is
necessary and practical, and many scholars have con -
ducted in-depth explorations of AI in marketing using
bibliometrics (Mustak et al., 2021), meta-analysis (Shukla
et al., 2024), and content analysis (Vlačić et al., 2021),
these studies lack a solid theoretical foundation. They fail
to analyze the degree of employee-AI alignment in the
marketing field from a comprehensive perspective.
Mitchell et al. ( 2001)’s systematic elaboration on job
embeddedness refers to the degree of fit between an
organization and its employees. With the advent of
new-generation AI technologies such as mobile facto -
ries (Won & Park, 2020), smart warehousing (Tiwari,
2023), and digital twins (Maheshwari & Devi, 2024), the
1 Introduction
The rapid advancement of artificial intelligence (AI) tech-
nology, exemplified by ChatGPT, has integrated AI into
various facets of human life. AI has gradually become
indispensable for employees in performing management
functions such as planning, organizing, leading, and con -
trolling (Davenport et al.,2020; Huang & Rust, 2021). This
phenomenon is particularly pronounced in the market -
ing field. Numerous practices, including service robots
(Sjödin et al., 2020; Liu et al., 2023), metaverse market -
ing (Pamucar et al., 2022; Thakral et al., 2023), digital
human brand building (Dalman et al., 2019; Zhen et al.,
2023), and AI customer relationship management (Li
& Xu, 2022; Ledro et al., 2023) have demonstrated that
the degree of alignment between employees and AI has
become a core research topic.
*Correspondence:
Zi-yi Wei
weiziyi0429@163.com
1Nanjing Tech University, Nanjing, China
2Capital University of Economics and Business, Beijing, China
Abstract
Disruptive innovations, particularly artificial intelligence (AI), are revolutionizing marketing. The alignment between
employees and AI is a critical issue in current marketing research. This study uses job embeddedness theory to
explore this alignment. By employing the BERTopic model and comparing different clustering algorithms through
topic coherence, we model themes in existing AI marketing research. Analysis through the dimensions of job
embeddedness—links, fit, and sacrifice—reveals that hierarchical clustering in BERTopic provides superior data
fitting. Intertopic visualization identifies three themes: “financial and marketing operations” , “marketing tactics and
innovations” , and “data analytics and VR innovations” . This study extends job embeddedness theory, defining its
dimensions in the AI era and guiding future research directions.
Keywords Artificial intelligence, Marketing, Job embeddedness theory, BERTopic, Clustering algorithms
Artificial intelligence embeddedness
in marketing
Shan-ji Yao1, Zi-yi Wei1* and Zhuang Wan2

Page 2 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
extensive application of AI has further improved deci -
sion-making efficiency in employees’ managerial func -
tions, gradually positioning AI as a pivotal role within
organizations. Consequently, analogous to the research
paradigm of sales personnel job embeddedness, we can
use the concept of AI embeddedness to comprehensively
describe the degree of fit between employees and AI
(Cheng, 2014; Elliott et al., 2020; Berry et al., 2024). To
delve into the conceptual structure of AI embeddedness,
our research questions (RQs) are as follows:
RQ.1 What are the research themes about AI
embeddedness?
RQ.2 What is the concept of AI embeddedness?
Our study employs job embeddedness as its theoretical
foundation and utilizes research methods such as biblio -
metrics, topic modeling, and social network analysis to
address the research questions. By integrating qualitative
and quantitative research paradigms, this study conducts
an in-depth exploration of the fit between employees and
AI, providing a theoretical perspective for AI embedded -
ness in marketing and suggesting directions for future
research.
The structure of this paper is as follows: In the subse -
quent sections, we provide a literature review of previ -
ous research on AI in marketing and the theory of job
embeddedness, theoretically demonstrating the neces -
sity of proposing AI embeddedness. In Sect.  3, we strictly
follow the SPAR-4-SLR data collection and data refine -
ment method, systematically reporting the data sources,
cleaning process, and the software and methods used in
this study. Section 4 and Sect. 5 are dedicated to present-
ing the research findings. Finally, in Sect.  6, we summa -
rize the conclusions, theoretical contributions, practical
implications, and limitations of this research.
2 Literature review
2.1 AI in marketing
The extensive application of AI in marketing strategies
and consumer behavior indicates that AI in marketing
is multidimensional on a technical level (Mustak et al.,
2021). This encompasses a range of digital technologies,
including machine learning, automated robots, big data,
neural networks, text mining, natural language process -
ing, data mining, software computing, and complex logic
(Tirunillai & Tellis, 2014; Salminen et al., 2019; Van Pinx-
teren et al., 2019). Referring to Vlačić et al. ( 2021) on the
concept of AI in marketing, which pertains to the devel -
opment of “ AI agents that recommend or take marketing
actions to achieve optimal marketing outcomes based
on information about consumers, competitors, and the
focal company they possess” , the research on AI in mar -
keting is already quite extensive, with studies employing
qualitative methods to analyze how AI in marketing can
promote social and environmental well-being (Hermann,
2022), and using fsQCA to analyze the effect of supply
chain finance on sustainability performance (Wang et al.,
2023b).
A substantial body of research on AI in marketing indi-
cates that the alignment between employees and AI has
become a shared concern for both academia and indus -
try, with numerous studies employing various research
methods to delve deeply into this issue. However, most
of these studies focus on specific areas, such as AI-CRM.
Few have examined the alignment between employees
and AI in the marketing field from a theoretical perspec -
tive, revealing a lack of top-level design.
2.2 Job embeddedness theory
Mitchell et al. ( 2001) pioneered the concept of job
embeddedness, which is the networks and connections
that employees can immerse themselves in, and com -
prises three dimensions: the employee’s connection to
the job or community, the match between the employee
and the job or community, and what the employee is
going to give up once he or she leaves the job or the com-
munity, and thus includes the dimensions of 6 Organiza -
tional-Community Connection, Match, and Sacrifice. Lee
et al. (2004), however, categorized it into two dimensions
of job embeddedness and non-job embeddedness. Job
embeddedness consists of work-based embeddedness,
which includes in-work, organizational and occupational
embeddedness dimensions; and non-work embedded -
ness, which includes family embeddedness and com -
munity embeddedness dimensions in the community
(Kiazad et al., 2015). A large number of job embedded -
ness studies in marketing synthesize theoretical perspec -
tives such as organizational strategy and focus on both
predicting employee performance and employee turn -
over (Sender et al., 2018; Martadiani et al., 2022; Pelto-
korpi & Allen, 2024). Overall, the research represented
by Mitchell et al. (2001) identifies the theoretical basis for
this paper’s definition of AI embeddedness and serves as
a screening mechanism for screening relevant literature
that fits the concept of AI embeddedness in subsequent
studies. Notably, alternative theories explaining “human-
AI interaction” such as human-AI collaboration theory
and AI readiness theory can’t fully address core needs.
Specifically, Human-AI Collaboration Theory focuses
on the efficiency of short-term task-based interactions
between employees and AI, with core dimensions includ-
ing “task division, interaction trust, and communication
mechanisms” . For example, this theory explores role allo-
cation in AI-assisted customer service. However, it lacks
attention to long-term alignment and potential costs (Wu
et al., 2024); AI Readiness Theory emphasizes the pre-
implementation preparation status of organizations or

Page 3 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
individuals for AI, with dimensions centered on techni -
cal capabilities, resource support, and attitudinal will -
ingness. For example, it usually assesses an enterprise’s
readiness for AI deployment. However, AI Readiness
Theory does not address the dynamic alignment process
between employees and AI post-implementation (Chow -
dhury et al., 2023).
In contrast, as shown in the Table  1, “Links-Fit-Sacri-
fice” conception of job embeddedness simultaneously
covers three critical aspects of employee-AI long-term
alignment: the connection between employees and
AI (Links), the alignment between AI capabilities and
employee/organizational needs (Fit), and the potential
costs of AI adoption (Sacrifice), forming a comprehensive
explanatory framework for relationship.
As AI is gradually embedded in all aspects of human
life, the use of job embeddedness theory can effectively
explain the degree of fit between employees and AI.
Specifically, connection refers to the formal or informal
relationship between employees and AI, match refers
to the degree of fit between employee growth paths and
the level of AI development and AI ethics, and sacrifice
refers to the tangible or intangible losses that AI may
bring to employees, such as service failure and customer
retention.
3 Methodology
3.1 Data collection
In this section, we provide a detailed explanation of the
data acquisition and data cleaning methods used in this
study, following the SPAR-4-SLR protocol proposed by
Paul et al. ( 2021). For the data assembling part, we uti -
lized the SCI and SSCI databases from the Web of Sci -
ence Core Collection as the sole data source, with three
critical justifications to guarantee the robustness of data -
base selection:
First, Web of Science ensures precise coverage of core
marketing journals, which is essential for our focus on
“ AI embeddedness in marketing” . Unlike Scopus, a widely
used alternative, The “Business, Economics & Manage -
ment” category of Web of Science prioritizes top-tier
marketing journals, such as Journal of Marketing , Jour-
nal of Marketing Research, Journal of Consumer Research,
that are directly relevant to our topic (Mustak et al., 2021;
Vlačić et al., 2021). Scopus, by contrast, includes a higher
proportion of computer science or engineering-focused
AI papers which contain plenty studies on pure LSTM
algorithm optimization without any marketing context.
This would introduce irrelevant samples and increase
data cleaning complexity, conflicting with our goal of
building a focused and specific area in marketing context.
Second, Web of Science’s comprehensive citation data
supports our qualitative analysis of highly cited papers,
that is a core step in defining AI embeddedness. As
noted, Web of Science manages citation data for every
bibliographic record, allowing us to reliably identify influ-
ential studies by filtering for papers with ≥ 100 citations
(Fischer & Krauss, 2018; Mikalef et al., 2020). Scopus
lacks such consistency in citation indexing for pre-2018
marketing papers, which would undermine the validity of
our high-citation sample and weaken the conceptualiza -
tion of AI embeddedness.
Third, using Web of Science avoids unnecessary sam -
ple redundancy while guaranteeing quality. Our study
focuses on papers from high level which contains ABDC-
A and A*. Web of Science already covers over 90% of
these journals. Adding Scopus would only introduce
30% redundant samples which contain the same paper
indexed in both databases, without expanding the pool of
high-quality, marketing-relevant studies. This would not
improve our analysis but rather increase computational
burden and the risk of data duplication errors.
Referring to the studies on AI in marketing by Mustak
et al. ( 2021) and Vlačić et al. ( 2021), we used the Title
as the search method, with specific search terms listed
in Table  2. Additionally, we limited the search topics to
marketing and the research domains to business, eco -
nomics and management. We restricted the document
types to articles or review articles, resulting in a total of
1289 documents.
3.2 Data refinement
To ensure the rigor of data refinement, our study consists
with the SPAR-4-SLR (Scientific Procedures and Ratio -
nales for Systematic Literature Reviews) protocol which
is proposed by Paul et al. ( 2021) for business, economics,
and management research. We first clarify how this pro -
tocol guides our data cleaning process, before detailing
specific steps.
Table 1 Comparison of job embeddedness theory and adjacent constructs
Theory Core Focus Key Dimensions Explanatory Power for Our Study
Job Embeddedness
Theory
Long-term alignment between employ-
ees and organizations/communities
Links, Fit, Sacrifice ★★★★★ (Fully covers “connection–fit–
cost” of employee-AI alignment)
Human-AI Collabora-
tion Theory
Short-term interaction efficiency between
employees and AI
Task Division, Interaction Trust,
Communication Mechanisms
★★★☆☆ (Focuses only on interaction
processes; lacks long-term alignment and
cost dimensions)
AI Readiness Theory Pre-implementation preparation for AI
(organization/individual)
Technical Capability, Resource
Support, Attitudinal Willingness
★★☆☆☆ (Focuses only on preparation;
lacks post-implementation alignment depth)

Page 4 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
SPAR-4-SLR is particularly suitable for our data refine -
ment because it addresses the unique challenges of mar -
keting research. For example, it does well in filtering
interdisciplinary AI studies to retain only marketing-
relevant content, which focus on the general systematic
review frameworks like PRISMA (Preferred Reporting
Items for Systematic Reviews and Meta-Analyses) lack,
for reason that PRISMA is tailored for medical sciences
(Rethlefsen, 2021). Specifically, there are two core pil -
lars of SPAR-4-SLR directly inform our approach. On the
one hand, it requires prioritizing high-quality, domain-
specific literature. For our study, this translates to filter -
ing for papers from ABDC A or A* journals, ensuring our
corpus reflects impactful Artificial intelligence in market-
ing. On the other hand, it also mandates explicit docu -
mentation of screening criteria and inter-coder reliability
which are critical for reproducibility. We operationalize
this through independent manual screening, detailed
below in Fig.  1, and report clear exclusion or inclusion
rules.
Therefore, we apply the SPAR-4-SLR for refining our
data. First, we merged articles with consistent themes
and conclusions, eventually obtained 1258 articles. Sec -
ond, to ensure the high quality of the literature, we
conducted data cleaning on the 1258 target papers by
retaining only those published in journals rated as A and
A* on the ABDC Journal Quality List, resulting in 682
documents. Next, although we limited the research area
and topics to marketing-related fields such as economics,
management, and business, due to the interdisciplinary
nature of marketing with fields like organizational strat -
egy, e-commerce, and international business, and con -
sidering our research theme focuses on the alignment of
employees and artificial intelligence within the marketing
domain, we manually screened the 682 documents from
the previous step. Each author independently reviewed
the abstracts of these documents, excluding those not
belonging to the marketing field. Finally, we obtained 640
documents for subsequent data analysis.
3.3 Data analysis
To elucidate the research themes surrounding the issue
of employee alignment with artificial intelligence, we
employed BERTopic for topic modeling. The raw data
consisted of the titles and abstracts from 640 cleaned
scientific articles, as titles and abstracts typically encap -
sulate the core viewpoints of the papers. Initially, fol -
lowing the data processing approach used by Sánchez
and Rey ( 2022) for Airbnb customer reviews, we under -
took data preprocessing: converting all text to lower -
case, part-of-speech tagging (retaining nouns, verbs, and
adjectives to focus on meaningful content), lemmati -
zation, and removing stop words, which used a custom
Table 2 Database search details of the study
Search Terms
Field Tag: Title (TI) TI=(“AI” OR “artificial intelligence” OR “machine learn-
ing” OR “deep learning” OR “robot” OR “automation”
OR “Big data” OR “neural network*” OR “natural lan-
guage processing” OR “NLP” OR “AR” OR “augmented
reality” OR “VR” OR “virtual reality” OR “data mining”
OR “soft computing” OR “fuzzy logic” OR “ChatGPT”
OR “LLM” OR “large language model” OR “biometrics”
OR “geotagging” OR “wearable*” OR “IoT” OR “internet
of things” OR “blockchains” OR “cloud computing”)
Boolean: AND
Field Tag: Topics (TS) TS=(Marketing)
Boolean: AND
Field Tag: Research Area (SU) SU = (“Business and Economics” OR “Management”)
Boolean: AND
Field Tag: Document Type (DT) DT=(Article OR Review)
Note: Asterisks (*) are used to capture plural forms
Fig. 1 Data Refinement with SPAR-4-SLR

Page 5 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
marketing-domain list to exclude non-informative terms
like “method” or “study” .
Next, adhering to the BERTopic procedure, we used
the scibert-scivocab-uncased pre-trained model (Amba -
lavanan & Devarakonda, 2020) for word embedding. For
dimensionality reduction, we opted for UMAP (BERTop-
ic’s default) with fixed key parameters: n_neighbors = 15,
n_components = 10, and random_state = 42—ensuring
result replicability while preserving global data structure
(Sainburg et al., 2021).
For the clustering step, we determined the number of
topics via topic coherence (Röder et al., 2015) and com -
pared three algorithms: HDBSCAN, K-means, and hier -
archical clustering. Each used standard configurations,
for example, K-means with random_state = 42; hierar -
chical clustering with ward linkage, to maintain consis -
tency. Despite HDBSCAN’s strength in variable-density
datasets, its results were prone to noise (Kim & Kang,
2022). K-means offered efficiency but lacked hierarchi -
cal insight, while hierarchical clustering better captured
nested thematic relationships—critical for “embedded -
ness” as a multi-layered concept. Thus, we selected hier -
archical clustering.
To ensure rigor in literature screening, two research -
ers independently assessed marketing relevance, with
inter-coder agreement measured via Cohen’s kappa = 0.87
(p < 0.001)—meeting the threshold for substantial reli -
ability (Landis & Koch, 1977). Discrepancies were
resolved via third-researcher arbitration.
To address the concept of AI embeddedness, we sys -
tematically analyzed highly cited papers (≥ 100 citations;
Fischer & Krauss, 2018) from hierarchical clustering
results. From 640 articles, 52 met this criterion (18 in
Cluster 1, 21 in Cluster 2, 13 in Cluster 3), ensuring the -
matic coverage. Two researchers independently reviewed
full texts to extract employee-AI alignment content, with
89% inter-coder agreement; discrepancies were resolved
via discussion. Drawing on job embeddedness’ link, fit,
and sacrifice dimensions (Mitchell et al., 2001), we analo-
gized AI as a novel organizational resource. Integrating
findings from highly cited papers, we derived AI embed -
dedness’ sub-dimensions.
4 Topic modelling algorithm
To ensure the reliability of topic modeling results, we first
verified the representativeness of the 640 cleaned papers
by extracting key metadata, in order to be consistent with
text-mining data preprocessing logic:
Publication timeline  72% of papers were published
between 2019 and 2024, with only 28% before 2019,
reflecting the latest research trends of AI in marketing,
which is critical for capturing current “ AI embeddedness”
practices.
Journal quality  All papers come from ABDC A/A*
journals, with the top 3 sources being Journal of Busi -
ness Research  (35 papers), Industrial Marketing Man -
agement (29 papers), and Journal of Consumer Research
(22 papers)—ensuring the academic rigor of text data for
topic modeling.
Highly cited paper distribution  The 52 highly cited
papers (≥ 100 citations) used for conceptual deriva -
tion (Sect.  3.3) are evenly spread across the 3 clusters
(18/21/13), confirming that no core theme is overrepre -
sented, which guarantees the balance of topic modeling
results” .
4.1 BERTopic with HDBSCAN
In practice, we used the PyCharm environment for data
analysis in the topic modeling process. First, following
the standard BERTopic algorithm, we used the optimized
pre-trained sentence transformer model scivocab to con -
vert the corpus into 768-dimensional vectors. Second,
following the UMAP dimensionality reduction method
by McInnes et al. ( 2020), we set the n_neighbors param -
eter to 15; n_components to 10; min_dist to 0.0; metric
to cosine; and random_state to 42 to ensure reproducibil-
ity and facilitate result validation and comparison. Third,
using the HDBSCAN clustering algorithm encapsulated
in BERTopic, we clustered the dimensionally reduced
text vectors and obtained 21 clusters. We calculated the
proportion of documents in each category out of the 640
documents and found a significant number of discrete
items, with the proportion exceeding 25%, significantly
affecting the analysis of AI embedding. Finally, we used
the Topic-documents visualization in BERTopic to visual-
ize the extracted 21 topics and found that the similarity
between different clusters was relatively high. Therefore,
we referred to the research by Farea et al. (2024) and used
hierarchical clustering and K-means to optimize the BER-
Topic model for more robust results Figs. 2 and 3.
4.2 BERTopic with hierarchical clustering
First, we replaced the HDBSCAN clustering algorithm
in BERTopic with hierarchical clustering. Hierarchical
clustering merges or splits data points into different lev -
els of clusters by constructing a dendrogram, showing
the nested relationships and clustering process between
data points (Murtagh & Legendre, 2014). Secondly, by
referring to O’Callaghan’s (2015) research, we used topic
coherence to calculate the number of topics in the clus -
ters. Higher topic coherence indicates a better fit of the
topic model. Thus, we determined the optimal number
of topics in the topic model by selecting the point with
the highest topic coherence. As shown in Fig. 4, we deter-
mined the optimal number of topics to be 9.

Page 6 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
To further justify the selection of hierarchical cluster -
ing, we supplemented two key validations: (1) Quantified
coherence comparison: Hierarchical clustering achieved
a u_mass score of -2.209 and c_v score of 0.409, which
is not a “marginal difference” , compared to K-means
(-5.649 for u_mass, 0.405 for c_v), u_mass (a measure of
topic coherence) was 61% closer to 0 (Röder et al., 2015);
(2) Thematic interpretability validation: Three market -
ing scholars with 5 + years of AI marketing research
experience independently rated the “thematic clar -
ity” of the three algorithms’ results (1 = uninterpretable,
5 = highly interpretable). Hierarchical clustering scored
an average of 4.3, significantly higher than HDBSCAN
(2.7) and K-means (3.1), confirming it aligns better with
domain.
In the hierarchical clustering model algorithm, we
chose Agglomerative Hierarchical Clustering, which
starts with each data point as a single cluster and
Fig. 3 Topic-documents Visualization of BERTopic-HDBSCAN

Fig. 2 BERTopic-HDBSCAN Topic-document Percentage

Page 7 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
continuously merges the most similar clusters. We used
the topic-document and topic-visualization methods
in BERTopic to make assessments. According to the
visualization results, after modeling the AI embedded -
ness topic with this algorithm, we found that the 9 clus -
ters were distinctly divided into 3 classes, as shown in
Figs. 5 and 6. This aligns with the three dimensions of job
embeddedness. Therefore, as shown in Table  3; Fig. 7, we
identified the representative articles within each topic
and listed the top 5 keywords for each topic for further
analysis.
Class 1 encompasses two topics: topic 1 and topic
2. Topic 1 centers on predicting stock market price
trends using machine learning algorithms, while topic
2 explores the application of neural networks and deep
learning models in direct sales and market segmentation.
Fig. 5 Topic-document of BERTopic-hierarchical

Fig. 4 Topic coherence distribution of hierarchical clustering

Page 8 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
Class 2 comprises four topics: topic 3, topic 4, topic 6,
and topic 8. These topics discuss the extensive use of data
in customer relationship management, product design,
price forecasting, and platform companies, reflecting the
close relationship between employees and artificial intel -
ligence in marketing. Class 3 includes three topics: topic
0, topic 5, and topic 7. Topic 0 details the application of
big data analysis in business models and supply chains,
Table 3 Classification of topics and representative documents in hierarchical clustering
Class Topic BERTopic name Representative documents
1 1 market_price_model_machine Thomas and Christopher, 2017
2 model_network_neural_data Huang et al., 2004
2 3 data_product_customer_system Paulo et al., 2009
4 model_data_product_social Liu & Shih, 2005
6 model_base_data_market Zhu et al., 2019
8 platform_firm_service_market Joe, 1995
3 0 data_study_business_marketing Wang et al., 2016
5 performance_firm_data_capability Mikalef et al., 2020
7 intention_experience_consumer_reality Tussyadiah et al., 2018
Fig. 6 Topic-visualization of BERTopic-hierarchical

Page 9 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
topic 5 investigates the impact of data analysis and inno -
vation capabilities on company performance, and topic 7
focuses on research related to virtual reality technology
in consumer experiences.
4.3 BERTopic with K-means
While we had modeled the research themes of the AI
embeddedness concept using both HDBSCAN and hier -
archical clustering methods, we observed that HDB -
SCAN, due to the inherent objectivity of textual data,
resulted in a substantial number of discrete items. Con -
versely, the hierarchical clustering algorithm yielded only
three classes in practice. To validate the effectiveness
of the hierarchical clustering algorithm, we employed
the K-means clustering algorithm, known for providing
clearer and more consistent class divisions, for cross-
validation with hierarchical clustering. This approach
ensures the robustness of the topic model results (Jain,
2010). During the implementation, we meticulously con -
trolled the BERTopic data preprocessing, Scivocab pre-
trained model, UMAP dimensionality reduction, and the
process for determining the optimal number of topics to
ensure the efficacy of the topic extraction algorithm. As
illustrated in Fig.  8, the coherence curve peaks when the
number of topics is set to 30. Consequently, we fixed the
number of K-means clustering topics at 30, resulting in
the topic distribution depicted in Fig. 9.
Next, referring to Röder et al. ( 2015) for the measure -
ment of coherence, we calculated the consistency of top -
ics using both “u_mass” and “c_v” to compare K-means
and hierarchical clustering. We then determined our
topic extraction model based on these two clustering
algorithms. The specific results are detailed in Table  4.
Table 4 shows that the BERTopic model with hierarchi -
cal clustering has the highest “u_mass” and “c_v” values,
indicating it is the most effective for this study’s data.
Consequently, we used this model for the abstract por -
tion of 640 documents for subsequent in-depth analysis
of AI embeddedness’s conceptual structure.
5 Conceptual formation of AI embeddedness
5.1 Thematic analysis of clustering result
Based on a comparison of three clustering algorithms,
we ultimately selected hierarchical clustering for our
subsequent analysis. While the section on topic model -
ing algorithm selection has already provided an initial
explanation of the BERTopic results based on hierarchi -
cal clustering, this section delves deeper into the concep -
tual structure of AI embeddedness. To achieve this, we
used a literature review approach to examine papers with
Fig. 7 Topic-word of Hierarchical Clustering

Page 10 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
more than 100 citations within each topic, thereby laying
a solid foundation for the formation of the AI embedded-
ness concept. To clarify the mapping logic between the
9 topics and the three dimensions of AI embeddedness
(Link, Fit, Sacrifice), we constructed a transparent cod -
ing scheme and validated its reliability, as shown in the
Table 5. An independent marketing scholar who is unre -
lated to the research team, re-mapped the 9 topics using
the above scheme, with Cohen’s kappa = 0.82 (p < 0.001),
Table 4 Comparative experiments on thematic coherence and
number of themes
Coherence u_mass c_v Topic-number
Hierarchical clustering -2.209 0.409 9
K-means -5.649 0.405 30
Fig. 9 Topic-documents distribution of K-means algorithm

Fig. 8 Topic-coherence of K-means algorithm

Page 11 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
meeting the standard for substantial reliability and ensur-
ing the mapping is auditable.
5.1.1 Class 1: AI-Integrated in financial and marketing
operations
Topic 1 primarily describes the impact of deep learn -
ing algorithms on financial marketing and stock market
prediction. Fischer and Krauss ( 2018) applied long-short
term memory (LSTM) networks to a large-scale finan -
cial market prediction task, successfully demonstrating
that LSTM networks can effectively extract meaningful
information from noisy time series data to predict price
trends. Similar studies have used neural networks and
other intelligent technologies for stock market predic -
tion, indicating a close relationship between employees,
consumers, and digital technology. Consequently, artifi -
cial intelligence and similar technologies have been long-
term applications in investor behavior research (Chen et
al., 2003; Cao et al., 2005; Leippold et al., 2022). Addition-
ally, by applying large-scale deep learning methods to
stock market research, it is possible to more accurately
predict market price changes and make timely adjust -
ments to company marketing strategies (Tambe, 2014;
Cont and Sirignano, 2019).
Topic 2 primarily describes the application of neural
networks in marketing. As early as 2004, Huang et al.
conducted a market comparative study on credit rating
analysis using neural networks, finding that neural net -
work algorithm models provide better interpretability for
credit ratings, a conclusion also supported by Leigh et al.
(2002). Subsequently, researchers built comprehensive
bankruptcy databases by extracting features from tex -
tual data using neural network layers, demonstrating that
deep learning models based on neural networks excel
in predicting bankruptcy through textual disclosures,
thereby offering more intelligent models for investors,
regulators, and researchers (Mai et al., 2019). Moreover,
neural network models have been widely applied in direct
marketing. For example, Cui et al. ( 2006) used Bayesian
networks to model consumer responses, aiding in man -
agement decision-making, and He et al. ( 2021) employed
neural network algorithms to delve into consumer
neuroscience. These studies collectively highlight that
neural networks play a crucial role in direct marketing by
enhancing the accuracy of customer targeting, predicting
consumer behavior, and optimizing marketing strategies
through advanced data analysis and pattern recognition.
Following a comprehensive literature review of the top-
ics encompassed in class 1, we have designated this class
as “ AI Integration in Financial and Marketing Opera -
tions. ” This category captures the application of deep
learning and neural networks within the financial and
marketing sectors, highlighting the integration of artifi -
cial intelligence in these domains and the pivotal role of
employees in leveraging these technologies.
5.1.2 Class 2: AI-Enhanced marketing tactics and
innovations
Topic 3 primarily explores the application of data min -
ing in marketing contexts such as product recommenda -
tion and sales forecasting. Cortez et al. ( 2009) introduced
a data mining approach to predict human wine taste
preferences using various algorithms, including support
vector machines, neural networks, and multiple regres -
sion. This method aids targeted marketing by simulat -
ing consumer tastes in niche markets. Researchers have
employed data mining techniques to extract customer
knowledge for product development across different
market segments, thereby aligning customer needs with
product development processes to reduce trial-and-
error costs and enhance sales performance (Agard and
Kusiak, 2004; Su et al., 2006; Yu et al., 2020). By lever -
aging data mining, companies can better understand
and predict online consumer product demands. Previ -
ous studies have utilized online promotional marketing
and online reviews as predictive factors, employing deep
learning algorithms such as neural networks to analyze
online data comprehensively. This approach yields valu -
able insights to inform corporate marketing strategies
(Chong et al., 2017; Loureiro et al., 2018). The extensive
application of data mining in marketing has significantly
strengthened the integration of companies, consumers,
and their stakeholders with digital technologies, includ -
ing artificial intelligence, in the digital age.
Table 5 Coding scheme for Topic-Dimension mapping
Class Topic ID BERTopic Name Core Content Corresponding Dimension
1 1 market_price_model_machine ML predicts stock price trends Link
1 2 model_network_neural_data Neural networks for direct marketing Link
2 3 data_product_customer_system Data mining for product recommendations Fit
2 4 model_data_product_social Digital tech for social media marketing Fit
2 6 model_base_data_market Deep learning for price forecasting Fit
2 8 platform_firm_service_market Tech innovation for platform services Fit
3 0 data_study_business_marketing Big data for operations Sacrifice
3 5 performance_firm_data_capability Data analytics impacts performance Sacrifice
3 7 intention_experience_consumer_reality VR for consumer experience Sacrifice

Page 12 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
Topic 4 primarily delves into the application of digi -
tal technologies in social media marketing. Liu and
Shih ( 2005) pioneered a marketing model that inte -
grates hierarchical analysis and data mining techniques
to deliver precise product recommendations tailored to
each customer segment. This seminal study has exerted
considerable influence in this domain. Building on their
foundation, subsequent researchers have leveraged senti -
ment analysis, big data architectures, and advanced deep
learning algorithms to investigate how online reviews
and online promotional marketing strategies can pre -
dict sales performance. They discovered that sentiment
significantly interacts with both the volume and valence
of online reviews, thereby substantially influencing and
forecasting product sales (Chong et al., 2016; Kauffmann
et al., 2020). Furthermore, contemporary scholars have
enhanced social media marketing through the implemen-
tation of a visual data analytics framework. By employ -
ing deep learning algorithms, they have explored various
contexts, including the study of CEO oral communica -
tion, to strengthen the impact of social media marketing
efforts (Choudhury et al., 2019; Shin et al., 2020).
Topic 6 focuses on data-driven marketing models uti -
lizing deep learning algorithms, such as neural networks,
for predictive analysis. Researchers have employed
enhanced hybrid ensemble machine learning approaches
and text-based deep learning methods to forecast crude
oil prices and assess the credit risk of SMEs in supply
chain finance, thereby offering scientific guidance for
developing corporate marketing strategies (Li et al., 2019;
Zhu et al., 2019). Currently, marketing models based on
deep learning algorithms are extensively applied in stud -
ies on customer demand analysis, product innovation,
and green technology innovation. These applications
highlight the effective integration of human resources
and artificial intelligence in marketing, providing a
robust theoretical foundation for business performance
improvement (Li et al., 2018; Zhang et al., 2018; Yaoteng
& Xin, 2022). Moreover, recent research has explored
financial performance and marketing innovation through
deep learning algorithms in various contexts, such as
supply chain strategy and intercity connections, contrib -
uting to a deeper understanding of these domains (Luo et
al., 2023; Wang et al., 2023a, b).
Topic 8 primarily explores how platform companies
develop service marketing strategies through product
and technological innovation. Current research on plat -
form companies focuses on the impact of two major
digital technologies, the Internet of Things (IoT) and
blockchain, on the platform ecosystem (Liu et al., 2021).
Basaure et al. ( 2020) used agent-based modeling to ana -
lyze the effects of consumer switching costs and provider
multi-homing on market structure and competition.
Simulation results indicate that when switching costs
decrease due to factors such as consumer data portability,
provider multi-homing plays a critical role in enhancing
market competition. Additionally, cloud computing has
also played a significant role in the formulation of ser -
vice marketing strategies for platform companies. Stud -
ies have shown that cloud computing can effectively help
companies track consumer adoption behavior in strategic
management, make timely adjustments in service failure
scenarios to retain customers, and improve user satisfac -
tion and trust (Shin et al., 2014; Huang et al., 2015; Chen
et al., 2019).
Following an extensive literature review of the four
topics within class 2, we have named this category “ AI-
Enhanced Marketing Tactics and Innovations” . This
designation underscores the application of artificial intel-
ligence in data mining, social media marketing, predic -
tive analysis, and the innovation of service marketing
strategies, specifically illustrating AI in enhancing mar -
keting strategies and driving innovation.
5.1.3 Class 3: AI-Driven data analytics and VR innovations
Topic 0 primarily describes the widespread application of
big data in marketing, encompassing areas such as opera-
tions management, e-commerce, and strategic manage -
ment. Grover et al. ( 2018), based on the resource-based
view, proposed a big data value creation framework,
arguing that the better the alignment between employ -
ees and consumers with big data analytics, the more sig -
nificant the improvements in company performance and
consumer well-being. Existing research indicates that
big data can provide unique insights into market trends,
customer purchasing patterns, and maintenance cycles,
as well as methods to reduce costs and make more tar -
geted business decisions. Therefore, employees or con -
sumers with big data analytical capabilities can overcome
computational and data challenges, further enhancing
job performance and consumer well-being (Wang et al.,
2016; Choi et al., 2018). The operational performance
improvements brought about by big data have been fur -
ther confirmed in studies targeting manufacturing orga -
nizations and e-commerce scenarios (Akter & Wamba,
2016; Dubey et al., 2020).
Topic 5 primarily examines the impact of data analytics
capabilities on corporate performance and market inno -
vation. Research indicates that big data analytics capabili-
ties enable firms to generate insights that enhance their
dynamic capabilities, thereby positively influencing both
marketing and technological competencies (Mikalef et
al., 2020). With advances in artificial intelligence and the
growing availability of data, data network effects manifest
in the positive direct relationship between a platform’s AI
capabilities and users’ perceived value of the platform.
When data network effects are activated, customers per -
ceive the value brought by AI, further strengthening the

Page 13 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
company’s competitive advantage (Gregory et al., 2021).
Existing studies, based on the knowledge-based view the -
ory, demonstrate that the business value realized through
investments in big data analytics can provide financial
performance advantages to companies. AI technologies
enabled by big data enhance firm performance through
knowledge creation processes involving customers, users,
and the external market (Raguseo & Vitari, 2018; Bag et
al., 2021).
Topic 7 mainly discusses the application of virtual
reality technology in tourism services and its impact on
consumer experience and purchase intentions. The rapid
development of virtual reality technology offers opportu -
nities for widespread consumption of tourism content. It
also presents challenges in understanding the effective -
ness of virtual experiences in fostering more favorable
attitudes towards tourist destinations and shaping visi -
tation intentions (Tussyadiah et al., 2018). Bogicevic et
al. (2019) found that virtual reality previews can provide
more detailed explanations of experiential mental imag -
ery and generate a stronger sense of presence, thereby
enhancing brand experience. Through digital technolo -
gies like virtual reality, consumers resonate with tourism
brands, which benefits companies in adjusting marketing
strategies and choosing strategic directions. Additionally,
applying augmented reality technology in scenarios such
as museums and cultural heritage sites enables consum -
ers to have immersive experiences, thereby influencing
their purchase motivations, stimulating purchase inter -
est, and driving consumption behavior (Javornik, 2016;
He et al., 2018; Jung et al., 2018).
Following a thorough literature review of the topics
within class 1, we have designated this category as “ AI-
Driven Data Analytics and VR Innovations. ” This title
reflects the integration of AI-driven data analytics and
virtual reality technology in marketing, highlighting the
significant impact these innovations have on corporate
performance and consumer experience.
5.2 Definition of AI embeddedness
Through thematic clustering analysis of 640 cleaned
documents and systematic extraction from 52 highly
cited papers (≥ 100 citations; see Sect. 3.3 for details), it is
evident that with the rapid advancement of digital tech -
nology, the integration between employees and artificial
intelligence in the marketing sector has become increas -
ingly seamless. Management practices such as Gener -
ated-AI, advanced chatbots, and customer customization
have given rise to the concept of AI embeddedness.
Drawing on Zhang et al. ( 2012)’s review of job embed -
dedness, this section uses the three dimensions of job
embeddedness theory—link, fit, and sacrifice—combined
with clustering results and findings from the analysis of
highly cited papers, to comprehensively explain the con -
cept of AI embeddedness.
5.2.1 Link dimension of AI embeddedness
The link dimension in job embeddedness refers to the for-
mal and informal relationships between employees and
the organization and its members. For AI embeddedness,
this dimension is derived from the analysis of 52 highly
cited papers: As data becomes a crucial production fac -
tor, AI has deeply penetrated domains such as consumer
behavior, customer relationship management, service
marketing, and brand management through extensive
data training sets (76% of the 21 highly cited papers in
Cluster 2 mention such penetration). These penetrations
result in two types of links: formal relationships where
enterprises utilize AI for marketing purposes, and infor -
mal relationships where employees use AI to enhance
their job performance. Therefore, the link dimension
of AI embeddedness refers to the degree of connec -
tion between AI systems and various organizational
processes, employees, and external stakeholders. This
includes how AI technology is integrated into workflows
to enhance collaboration and communication within the
organization, as well as the depth of connection between
AI tools and other systems, such as Customer Relation -
ship Management platforms, marketing automation tools
and employee communication channels.
5.2.2 Fit dimension of AI embeddedness
The fit dimension in job embeddedness refers to the
alignment between employees’ growth paths and orga -
nizational development plans, as well as the congruence
between personal values and organizational beliefs. For
AI embeddedness, core findings of this dimension come
from systematic extraction from highly cited papers:
Amazon employs AI algorithms to analyze users’ brows -
ing and purchase histories, offering personalized prod -
uct recommendations; Salesforce leverages AI to analyze
customer data, providing insights into customer behav -
ior and sales forecasts to help marketing teams develop
more effective customer engagement strategies (Acha -
rya et al., 2018; Chen & Guo, 2022), these cases are all
from the top 10 most cited papers in Clusters 1 and 2.
This alignment between employees and AI in marketing
not only enhances user satisfaction and purchase rates
but also reflects corporate values and promotes brand
culture. Therefore, in the concept of AI embeddedness,
the fit dimension refers to the degree to which AI tech -
nology aligns with business needs, employee work styles,
and organizational culture in the marketing field. By
improving the efficiency and effectiveness of personal -
ized recommendations, dynamic ad generation, customer
relationship management, and content creation, AI appli-
cations ensure that they meet and support the company’s

Page 14 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
strategic goals and operational processes. This conclusion
is consistent with 83% of findings in the 52 highly cited
papers.
5.2.3 Sacrifice dimension of AI embeddedness
The sacrifice dimension in job embeddedness refers to
the tangible or intangible losses employees might face
upon leaving, such as loss of salary, career advancement
opportunities, and personal relationships. For AI embed -
dedness, the connotation of this dimension is based on
the focused discussion of risks in highly cited papers.
Algorithmic black boxes (Basukie et al., 2020), AI-related
errors (Falk, 2021), and big data price discrimination
(Valletti & Wu, 2020) have emerged as critical issues,
making it crucial to address the welfare dilemmas posed
by AI embeddedness. These studies all come from the 13
highly cited papers in Cluster 3, with 92% emphasizing
the inevitability of such risks. Beyond technical and eco -
nomic risks, there are also socio-technical costs that have
been under-addressed in prior discussions.
One key socio-technical cost is deskilling among mar -
keting employees. As AI automates repetitive yet skill-
dependent marketing tasks—like manual customer
segmentation and heuristic market analysis. employees
may gradually lose proficiency in these core competen -
cies. This weakens their career resilience and increases
organizational dependence on AI systems, creating hid -
den operational risks if AI fails (Puntoni et al., 2021).
Another is algorithmic bias in AI marketing systems. AI
recommendation or pricing systems often inherit biases
from historical training data; for example, overrepre -
senting high-income consumer preferences may lead to
discriminatory recommendations or worsened big data
price discrimination (Valletti & Wu, 2020). Such bias
violates marketing fairness, triggers regulatory scrutiny,
and erodes consumer trust, resulting in intangible losses
like brand image damage that are harder to mitigate than
direct financial costs.
Therefore, in the concept of AI embeddedness, the sac -
rifice dimension involves potential losses or costs from
adopting and implementing AI technology. This includes
financial investments, time for training and integration,
risk of certain job roles being displaced, data privacy and
security issues, employee skill degradation, and reputa -
tional or regulatory costs from algorithmic bias. Under -
standing these sacrifices helps organizations balance
benefits and costs. For instance, by designing AI-human
collaboration training programs to mitigate deskilling
or conducting regular algorithmic audits to reduce bias,
leading to informed decisions about AI integration.
6 Conclusion
This study utilizes literature data from the Web of Sci -
ence Core Collection to explore AI research topics in the
field of marketing. By integrating the theoretical perspec-
tive of job embeddedness, we define the variable repre -
senting the degree of fit between employees and AI as
AI embeddedness. Our findings reveal that AI embed -
dedness encompasses three primary research themes:
AI-Integrated Financial and Marketing Operations, AI-
Enhanced Marketing Tactics and Innovations, and AI-
Driven Data Analytics and VR Innovations. The three
dimensions of AI embeddedness are further explained
using established theories of job embeddedness. The
‘link’ dimension refers to the formal or informal relation -
ships between AI systems and various organizational
processes, employees, and external stakeholders. The ‘fit’
dimension denotes the degree to which AI capabilities
align with organizational needs and culture. Lastly, the
‘sacrifice’ dimension pertains to the potential losses or
costs associated with the adoption and implementation
of AI technologies.
6.1 Contributions
6.1.1 Theoretical contributions
Firstly, this study creatively defines the degree of fit
between employees and AI as AI embeddedness, and
proposes the concept of AI embeddedness. And with
the help of the established theory of job embeddedness,
the subdivision dimension of the concept of AI embed -
dedness is specifically elaborated. Secondly, this study
optimizes the BERTopic theme model by combining the
characteristics of text data in the process of theme extrac-
tion. Among the clustering algorithms adopted by BER -
Topic, we compare the traditional HDBSCAN, K-means
and hierarchical clustering algorithms, and found that
BERTopic with hierarchical clustering algorithm has bet -
ter interpretability for the dataset of this study. Thirdly,
this study expands the study of AI in the field of market -
ing, and creatively introduces the existing theory of job
embedding into the study of AI, which provides theoreti -
cal perspectives for the subsequent scholars to carry out
the relevant research.
6.1.2 Practical implications
Given the widespread use of AI in marketing and the fact
that it has become a public resource, it is imperative to
investigate the extent of employee-AI fit in marketing.
At the practical level, companies further enable con -
sumers to have an immersive experience through digital
technologies such as virtual reality, big data, and block -
chain, which enhances consumers’ interest in their prod -
ucts and leads to purchasing behavior. By applying the
AI embeddedness theory proposed in this study, firms
can reasonably avoid the risks of big data killing, privacy

Page 15 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
infringement, and algorithmic ethics brought about by
AI, fully release the technological benefits brought about
by AI, and take advantage of the positive externalities of
AI to continuously improve firm performance. For con -
sumers, AI embeddedness can make theoretical guid -
ance for their use of AI, and through the measurement
of sacrifice, consumers can reasonably narrow the sunk
costs, and utilize the digital technology represented by AI
to improve their consumer happiness. In addition, when
scholars apply the BERTopic algorithm model in the
future, they can refer to the optimization of the cluster -
ing algorithm in this study, and use the BERTopic model
based on the hierarchical clustering algorithm to carry
out in-depth research on the literature data.
6.2 Limitations
Although this paper has included as much AI research
in the field of marketing as possible, along with the rapid
development of AI technology, there are still some frag -
mented articles that could not be included due to the
limitations of the database. Although this study has made
an in-depth exploration of the concept of the degree of
fit between employees and AI in the field of marketing, it
has not conducted a large sample of empirical research,
and future scholars can make a more in-depth explora -
tion of the path of governance of AI in marketing, and
the mechanism of influence based on the concept of AI
embeddedness proposed in this study.
Author contributions
Yao Shan-ji: put forward ideas and revise papers Wei Zi-yi: writing papers, data
analysis Wan Zhuang: revise the paper.
Funding
This study is a phased research achievement of the National Natural Science
Foundation of China 71772086, the National Social Science Foundation of
China 22AGL022, and Outstanding Teaching Team of Jiangsu Colleges and
Universities “Qing Lan Project” .
Data availability
No datasets were generated or analysed during the current study.
Declarations
Competing interests
The authors declare no competing interests.
Received: 24 March 2025 / Revised: 20 October 2025 / Accepted: 21 Octo-
ber 2025
References
Acharya, A., Singh, S. K., Pereira, V., & Singh, P . (2018). Big data, knowledge co-
creation and decision making in fashion industry. International Journal of
Information Management, 42, 90–101.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i j  i n f  o m g t  . 2  0
1 8 . 0 6 . 0 0 8
Agard, B., & Kusiak *, A. (2004). Data-mining-based methodology for the design
of product families. International Journal of Production Research, 42(15),
2955–2969.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 8 0  / 0  0 2 0  7 5 4  0 4 1 0  0 0  1 6 9 1 9 2 9
Akter, S., & Wamba, S. F. (2016). Big data analytics in E-commerce: A systematic
review and agenda for future research. Electronic Markets, 26(2), 173–194.  h t t p
s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 2 5 2 5 - 0 1 6 - 0 2 1 9 - 0
Ambalavanan, A. K., & Devarakonda, M. V. (2020). Using the contextual Language
model BERT for multi-criteria classification of scientific articles. Journal of
Biomedical Informatics, 112, 103578.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j b i . 2 0 2 0 . 1 0 3 5 7 8
Bag, S., Gupta, S., Kumar, A., & Sivarajah, U. (2021). An integrated artificial intel-
ligence framework for knowledge creation and B2B marketing rational
decision making for improving firm performance. Industrial Marketing Man-
agement, 92, 178–189.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i n  d m a  r m a n  . 2  0 2 0 . 1 2 . 0 0 1
Basaure, A., Vesselkov, A., & Töyli, J. (2020). Internet of things (IoT) platform com-
petition: Consumer switching versus provider multihoming. Technovation,
90–91.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t e  c h n  o v a t  i o  n . 2 0 1 9 . 1 0 2 1 0 1
Basukie, J., Wang, Y., & Li, S. (2020). Big data governance and algorithmic manage-
ment in sharing economy platforms: A case of ridesharing in emerging
markets. Technological Forecasting and Social Change, 161, 120310.  h t t p  s : /  / d o i  .
o  r g /  1 0 .  1 0 1 6  / j  . t e  c h f  o r e .  2 0  2 0 . 1 2 0 3 1 0
Berry, L. L., Danaher, T. S., Keiningham, T., Aksoy, L., & Andreassen, T. W. (2024).
EXPRESS: Social profit orientation: lessons from organizations committed to
building a better world. Journal of Marketing, 00222429241258495.  h t t p  s : /  / d o
i  . o  r g /  1 0 .  1 1 7 7  / 0  0 2 2 2 4 2 9 2 4 1 2 5 8 4 9 5
Bogicevic, V., Seo, S., Kandampully, J. A., Liu, S. Q., & Rudd, N. A. (2019). Virtual reality
presence as a preamble of tourism experience: The role of mental imagery.
Tourism Management, 74, 55–64.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t o  u r m  a n . 2  0 1  9 . 0 2
. 0 0 9
Cao, Q., Leggio, K. B., & Schniederjans, M. J. (2005). A comparison between Fama
and french’s model and artificial neural networks in predicting the Chinese
stock market. Computers & Operations Research, 32(10), 2499–2512.  h t t p  s : /  / d o i
. o  r g /  1 0 .  1 0 1 6  / j  . c o r . 2 0 0 4 . 0 3 . 0 1 5
Chen, A. S., Leung, M. T., & Daouk, H. (2003). Application of neural networks to an
emerging financial market: Forecasting and trading the Taiwan stock index.
Computers & Operations Research, 30(6), 901–923.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / S  0 3
0 5 - 0 5 4 8 ( 0 2 ) 0 0 0 3 7 - 0
Cheng, C. Y. (2014). A longitudinal study of newcomer job embeddedness and
sales outcomes for life insurance salespersons. Journal of Business Research,
67(7), 1430–1438.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j b  u s r  e s . 2  0 1  3 . 0 7 . 0 2 4
Chen, J., & Guo, Z. (2022). New-Media advertising and retail platform openness. MIS
Quarterly, 46(1), 431–456.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 5 3 0  0 /  M I S Q / 2 0 2 2 / 1 5 4 2 0
Chen, S., Lee, H., & Moinzadeh, K. (2019). Pricing schemes in cloud computing:
Utilization-Based vs. Reservation‐Based Production and Operations Manage-
ment, 28(1), 82–102.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 1 1  / p  o m s . 1 2 8 9 3
Choi, T., Wallace, S. W., & Wang, Y. (2018). Big data analytics in operations manage-
ment. Production and Operations Management, 27(10), 1868–1883.  h t t p  s : /  / d o i
. o  r g /  1 0 .  1 1 1 1  / p  o m s . 1 2 8 3 8
Chong, A. Y. L., Ch’ng, E., Liu, M. J., & Li, B. (2017). Predicting consumer product
demands via big data: The roles of online promotional marketing and online
reviews. International Journal of Production Research, 55(17), 5142–5156.  h t t p  s :
/  / d o i  . o  r g /  1 0 .  1 0 8 0  / 0  0 2 0  7 5 4  3 . 2 0  1 5  . 1 0 6 6 5 1 9
Chong, A. Y. L., Li, B., Ngai, E. W. T., Ch’ng, E., & Lee, F. (2016). Predicting online prod-
uct sales via online reviews, sentiments, and promotion strategies: A big data
architecture and neural network approach. International Journal of Operations
& Production Management, 36(4), 358–383.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 0 8  / I  J O P M - 0
3 - 2 0 1 5 - 0 1 5 1
Choudhury, P ., Wang, D., Carlson, N. A., & Khanna, T. (2019). Machine learning
approaches to facial and text analysis: Discovering CEO oral communication
styles. Strategic Management Journal, 40(11), 1705–1732.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1
0 0 2  / s  m j . 3 0 6 7
Choudrie, J., Manandhar, N., Castro, C., & Obuekwe, C. (2023). Hey Siri, Google! Can
you help me? A qualitative case study of smartphones AI functions in SMEs.
Technological Forecasting and Social Change, 189, 122375.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1
0 1 6  / j  . t e  c h f  o r e .  2 0  2 3 . 1 2 2 3 7 5
Chowdhury, S., Dey, P ., Joel-Edgar, S., Bhattacharya, S., Rodriguez-Espindola, O.,
Abadie, A., & Truong, L. (2023). Unlocking the value of artificial intelligence
in human resource management through AI capability framework. Human
Resource Management Review, 33(1), 100899.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . h r m r .
2 0 2 2 . 1 0 0 8 9 9
Cortez, P ., Cerdeira, A., Almeida, F., Matos, T., & Reis, J. (2009). Modeling wine prefer-
ences by data mining from physicochemical properties. Decision Support
Systems, 47(4), 547–553.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . d s s . 2 0 0 9 . 0 5 . 0 1 6
Cui, G., Wong, M. L., & Lui, H. K. (2006). Machine learning for direct marketing
response models: Bayesian networks with evolutionary programming. Man-
agement Science, 52(4), 597–612.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 2 8 7  / m  n s c . 1 0 6 0 . 0 5 1 4

Page 16 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
Dalman, M. D., Buche, M. W., & Min, J. (2019). The differential influence of identifica-
tion on ethical judgment: The role of brand love. Journal of Business Ethics,
158(3), 875–891.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 0 5 5 1 - 0 1 7 - 3 7 7 4 - 1
Davenport, T., Guha, A., Grewal, D., & Bressgott, T. (2020). How artificial intelligence
will change the future of marketing. Journal of the Academy of Marketing Sci-
ence, 48(1), 24–42.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 1 7 4 7 - 0 1 9 - 0 0 6 9 6 - 0
Dubey, R., Gunasekaran, A., Childe, S. J., Bryde, D. J., Giannakis, M., Foropon, C.,
Roubaud, D., & Hazen, B. T. (2020). Big data analytics and artificial intelligence
pathway to operational performance under the effects of entrepreneurial
orientation and environmental dynamism: A study of manufacturing organ-
isations. International Journal of Production Economics, 226, 107599.  h t t p  s : /  / d o i
. o  r g /  1 0 .  1 0 1 6  / j  . i j p e . 2 0 1 9 . 1 0 7 5 9 9
Elliott, C., Mavriplis, C., & Anis, H. (2020). An entrepreneurship education and peer
mentoring program for women in STEM: Mentors’ experiences and percep-
tions of entrepreneurial self-efficacy and intent. International Entrepreneurship
and Management Journal, 16(1), 43–67.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 1 3 6 5 - 0 1
9 - 0 0 6 2 4 - 2
Falk, M. (2021). Artificial stupidity. Interdisciplinary Science Reviews, 46(1–2), 36–52.  h
t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 8 0  / 0  3 0 8  0 1 8  8 . 2 0  2 0  . 1 8 4 0 2 1 9
Farea, A., Tripathi, S., Glazko, G., & Emmert-Streib, F. (2024). Investigating the
optimal number of topics by advanced text-mining techniques: Sustainable
energy research. Engineering Applications of Artificial Intelligence, 136, 108877.
h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . e n  g a p  p a i .  2 0  2 4 . 1 0 8 8 7 7
Fischer, T., & Krauss, C. (2018). Deep learning with long short-term memory
networks for financial market predictions. European Journal of Operational
Research, 270(2), 654–669.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . e j o r . 2 0 1 7 . 1 1 . 0 5 4
Gregory, R. W., Henfridsson, O., Kaganer, E., & Kyriakou, H. (2021). The Role of Artifi-
cial Intelligence and Data Network Effects for Creating User Value. Academy of
Management Review, 46(3), 534–551.  h t t p  s : /  / d o i  . o  r g /  1 0 .  5 4 6 5  / a  m r . 2 0 1 9 . 0 1 7 8.
Grover, V., Chiang, R. H. L., Liang, T. P ., & Zhang, D. (2018). Creating Strategic Business
Value from Big Data Analytics: A Research Framework. Journal of Management
Information Systems, 35(2), 388–423.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 8 0  / 0  7 4 2  1 2 2  2 . 2 0  1 8
. 1 4 5 1 9 5 1.
He, L., Freudenreich, T., Yu, W., Pelowski, M., & Liu, T. (2021). Methodological
structure for future consumer neuroscience research. Psychology & Marketing,
38(8), 1161–1181.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 2  / m  a r . 2 1 4 7 8
Hermann, E. (2022). Leveraging artificial intelligence in marketing for social
Good—An ethical perspective. Journal of Business Ethics, 179(1), 43–61.  h t t p  s : /
/ d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 0 5 5 1 - 0 2 1 - 0 4 8 4 3 - y
He, Z., Wu, L., & Li, X. (2018). (Robert). When art meets tech: the role of augmented
reality in enhancing museum experiences and purchase intentions. Tourism
Management, 68, 127–139.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t o  u r m  a n . 2  0 1  8 . 0 3 . 0 0 3
Huang, J., Kauffman, R. J., & Ma, D. (2015). Pricing strategy for cloud computing: A
damaged services perspective. Decision Support Systems, 78, 80–92.  h t t p  s : /  / d
o i  . o  r g /  1 0 .  1 0 1 6  / j  . d s s . 2 0 1 4 . 1 1 . 0 0 1
Huang, M. H., & Rust, R. T. (2021). A strategic framework for artificial intelligence in
marketing. Journal of the Academy of Marketing Science, 49(1), 30–50.  h t t p  s : /  / d
o i  . o  r g /  1 0 .  1 0 0 7  / s  1 1 7 4 7 - 0 2 0 - 0 0 7 4 9 - 9
Huang, Z., Chen, H., Hsu, C. J., Chen, W. H., & Wu, S. (2004). Credit rating analysis
with support vector machines and neural networks: A market comparative
study. Decision Support Systems, 37(4), 543–558.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / S  0 1 6
7 - 9 2 3 6 ( 0 3 ) 0 0 0 8 6 - 1
Jain, A. K. (2010). Data clustering: 50 years beyond K-means. Pattern Recognition
Letters, 31(8), 651–666.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . p a  t r e  c . 2 0  0 9  . 0 9 . 0 1 1.
Javornik, A. (2016). It’s an illusion, but it looks real!’ consumer affective, cognitive
and behavioural responses to augmented reality applications. Journal of
Marketing Management, 32(9–10), 987–1011.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 8 0  / 0  2 6 7  2 5
7  X . 2 0  1 6  . 1 1 7 4 7 2 6
Jung, T. H., Lee, H., Chung, N., & Tom Dieck, M. C. (2018). Cross-cultural differences
in adopting mobile augmented reality at cultural heritage tourism sites. Inter-
national Journal of Contemporary Hospitality Management, 30(3), 1621–1645.  h
t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 0 8  / I  J C H M - 0 2 - 2 0 1 7 - 0 0 8 4
Kauffmann, E., Peral, J., Gil, D., Ferrández, A., Sellers, R., & Mora, H. (2020). A frame-
work for big data analytics in commercial social networks: A case study on
sentiment analysis and fake review detection for marketing decision-making.
Industrial Marketing Management, 90, 523–537.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i n  d m
a  r m a n  . 2  0 1 9 . 0 8 . 0 0 3
Kiazad, K., Holtom, B. C., Hom, P . W., & Newman, A. (2015). Job embeddedness: A
multifoci theoretical extension. Journal of Applied Psychology, 100(3), 641–659.
h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 3 7  / a  0 0 3 8 9 1 9
Kim, J., & Kang, Y. (2022). Automatic classification of photos by tourist attractions
using deep learning model and image feature vector clustering. ISPRS
International Journal of Geo-Information, 11(4), 245.  h t t p  s : /  / d o i  . o  r g /  1 0 .  3 3 9 0  / i
j g i 1 1 0 4 0 2 4 5
Landis, J. R. & Koch, G. G. (1977). An application of hierarchical kappa-type statistics
in the assessment of majority agreement among multiple observers. Biomet-
rics, 33, 363–374.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 3 0 7  / 2  5 2 9 7 8 6
Ledro, C., Nosella, A., & Dalla Pozza, I. (2023). Integration of AI in CRM: Challenges
and guidelines. Journal of Open Innovation: Technology Market and Complexity,
9(4), 100151.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j o  i t m  c . 2 0  2 3  . 1 0 0 1 5 1
Lee, T. W., Mitchell, T. R., Sablynski, C. J., Burton, J. P ., & Holtom, B. C. (2004). THE
EFFECTS OF JOB EMBEDDEDNESS ON ORGANIZATIONAL CITIZENSHIP , JOB
PERFORMANCE, VOLITIONAL ABSENCES, AND VOLUNTARY TURNOVER.
Academy of Management Journal, 47(5), 711–722.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 3 0 7  / 2
0 1 5 9 6 1 3
Leigh, W., Purvis, R., & Ragusa, J. M. (2002). Forecasting the NYSE composite index
with technical analysis, pattern recognizer, neural network, and genetic algo-
rithm: A case study in romantic decision support. Decision Support Systems,
32(4), 361–377.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / S  0 1 6 7 - 9 2 3 6 ( 0 1 ) 0 0 1 2 1 - X
Leippold, M., Wang, Q., & Zhou, W. (2022). Machine learning in the Chinese stock
market. Journal of Financial Economics, 145(2), 64–82.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6
/ j  . j fi    n e  c o . 2  0 2  1 . 0 8 . 0 1 7
Li, F., & Xu, G. (2022). AI-driven customer relationship management for sustainable
enterprise performance. Sustainable Energy Technologies and Assessments, 52,
102103.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . s e t a . 2 0 2 2 . 1 0 2 1 0 3
Liu, D. R., & Shih, Y. Y. (2005). Integrating AHP and data mining for product recom-
mendation based on customer lifetime value. Information & Management,
42(3), 387–400.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i m . 2 0 0 4 . 0 1 . 0 0 8.
Liu, D., Li, C., Zhang, J., & Huang, W. (2023). Robot service failure and recovery:
Literature review and future directions. International Journal of Advanced
Robotic Systems, 20(4), 17298806231191606.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 7 7  / 1  7 2 9 8 8
0 6 2 3 1 1 9 1 6 0 6
Liu, L., Zhang, J. Z., He, W., & Li, W. (2021). Mitigating information asymmetry in
inventory pledge financing through the internet of things and blockchain.
Journal of Enterprise Information Management, 34(5), 1429–1451.  h t t p  s : /  / d o i  . o  r
g /  1 0 .  1 1 0 8  / J  E I M - 1 2 - 2 0 2 0 - 0 5 1 0
Li, X., Shang, W., & Wang, S. (2019). Text-based crude oil price forecasting: A deep
learning approach. International Journal of Forecasting, 35(4), 1548–1560.  h t t p
s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i j  f o r  e c a s  t .  2 0 1 8 . 0 7 . 0 0 6
Li, L., Chi, T., Hao, T., & Yu, T. (2018). Customer demand analysis of the electronic
commerce supply chain using Big Data. Annals of Operations Research,
268(1–2), 113–128.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 0 4 7 9 - 0 1 6 - 2 3 4 2 - x.
Loureiro, A. L. D., Miguéis, V. L., & Da Silva, L. F. M. (2018). Exploring the use of
deep neural networks for sales forecasting in fashion retail. Decision Support
Systems, 114, 81–93.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . d s s . 2 0 1 8 . 0 8 . 0 1 0
Luo, J., Wang, Y., & Li, G. (2023). The innovation effect of administrative hierarchy on
intercity connection: The machine learning of twin cities. Journal of Innova-
tion & Knowledge, 8(1), 100293.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j i k . 2 0 2 2 . 1 0 0 2 9 3
Mai, F., Tian, S., Lee, C., & Ma, L. (2019). Deep learning models for bankruptcy
prediction using textual disclosures. European Journal of Operational Research,
274(2), 743–758.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . e j o r . 2 0 1 8 . 1 0 . 0 2 4
Maheshwari, P ., & Devi, Y. (2024). Investigating the relationship between lean six
Sigma performance strategy with digital twin modeling: Practices and fac-
tors. Journal of Cleaner Production, 436, 140449.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j c  l e
p  r o . 2  0 2  3 . 1 4 0 4 4 9
Martadiani, A. A. M., Supartha, I. W. G., Dewi, M., I. G. A., Riana, I. G., & ROLE OF JOB
SATISFACTION AND EMBEDDEDNESS IN MANAGING TURNOVER INTENTION
IN HEALTHCARE INDUSTRIES. (2022). THE Polish Journal of Management Stud-
ies, 25(1), 228–241.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 7 5 1  2 /  p j m s . 2 0 2 2 . 2 5 . 1 . 1 4.
McInnes, L., Healy, J., & Melville, J. (2020). UMAP: Uniform Manifold Approximation
and Projection for Dimension Reduction (No. arXiv:1802.03426). arXiv.  h t t p  : / /
a r x i  v .  o r g  / a b  s / 1 8  0 2  . 0 3 4 2 6
Mikalef, P ., Krogstie, J., Pappas, I. O., & Pavlou, P . (2020). Exploring the relationship
between big data analytics capability and competitive performance: The
mediating roles of dynamic and operational capabilities. Information & Man-
agement, 57(2), 103169.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i m . 2 0 1 9 . 0 5 . 0 0 4.
Mitchell, T. R., Holtom, B. C., Lee, T. W., Sablynski, C. J., & Erez, M. (2001). Why people
stay: using job embeddedness to predict voluntary turnover. Academy of
Management Journal, 44(6), 1102–1121.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 3 0 7  / 3  0 6 9 3 9 1
Murtagh, F., & Legendre, P . (2014). Ward’s hierarchical agglomerative clustering
method: Which algorithms implement ward’s criterion? Journal of Classifica-
tion, 31(3), 274–295.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  0 0 3 5 7 - 0 1 4 - 9 1 6 1 - z

Page 17 of 17
Yao et al. Journal of Digital Management             (2025) 1:17
Mustak, M., Salminen, J., Plé, L., & Wirtz, J. (2021). Artificial intelligence in marketing:
Topic modeling, scientometric analysis, and research agenda. Journal of Busi-
ness Research, 124, 389–404.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j b  u s r  e s . 2  0 2  0 . 1 0 . 0 4 4
O’Callaghan, D., Greene, D., Carthy, J., & Cunningham, P . (2015). An analysis of the
coherence of descriptors in topic modeling. Expert Systems with Applications,
42(13), 5645–5657.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . e s w a . 2 0 1 5 . 0 2 . 0 5 5
Pamucar, D., Deveci, M., Gokasar, I., Tavana, M., & Köppen, M. (2022). A metaverse
assessment model for sustainable transportation using ordinal priority
approach and Aczel-Alsina norms. Technological Forecasting and Social
Change, 182, 121778.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t e  c h f  o r e .  2 0  2 2 . 1 2 1 7 7 8
Paul, J., Lim, W. M., O’Cass, A., Hao, A. W., & Bresciani, S. (2021). Scientific procedures
and rationales for systematic literature reviews (SPAR-4‐SLR). International
Journal of Consumer Studies, 45(4).  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 1 1  / i  j c s . 1 2 6 9 5
Peltokorpi, V., & Allen, D. G. (2024). Job embeddedness and voluntary turnover in
the face of job insecurity. Journal of Organizational Behavior, 45(3), 416–433.  h
t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 2  / j  o b . 2 7 2 8
Puntoni, S., Reczek, R. W., Giesler, M., & Botti, S. (2021). Consumers and artificial
intelligence: An experiential perspective. Journal of Marketing, 85(1), 131–151.
h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 7 7  / 0  0 2 2 2 4 2 9 2 0 9 5 3 8 4 7
Raguseo, E., & Vitari, C. (2018). Investments in big data analytics and firm perfor-
mance: An empirical investigation of direct and mediating effects. Interna-
tional Journal of Production Research, 56(15), 5206–5221.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0
8 0  / 0  0 2 0  7 5 4  3 . 2 0  1 8  . 1 4 2 7 9 0 0
Ramadan, Z. B. (2021). Alexafying shoppers: The examination of amazon’s captive
relationship strategy. Journal of Retailing and Consumer Services, 62, 102610.  h t
t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j r  e t c  o n s e  r .  2 0 2 1 . 1 0 2 6 1 0
Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence
measures. Proceedings of the Eighth ACM International Conference on Web
Search and Data Mining, 399–408.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 4 5  / 2  6 8 4 8 2 2 . 2 6 8 5 3 2 4
Rethlefsen, M. L., & Page, M. J. (2021). PRISMA 2020 and PRISMA-S: common ques-
tions on tracking records and the flow diagram. Journal of the Medical Library
Association, 110(2).  h t t p  s : /  / d o i  . o  r g /  1 0 .  5 1 9 5  / j  m l a . 2 0 2 2 . 1 4 4 9
Sainburg, T., McInnes, L., Gentner, T. Q. (2021). Parametric UMAP Embeddings for
representation and semisupervised learning. Neural, & Computation, 1–27.  h t t
p  s : /  / d o i  . o  r g /  1 0 .  1 1 6 2  / n  e c o _ a _ 0 1 4 3 4
Salminen, J., Yoganathan, V., Corporan, J., Jansen, B. J., & Jung, S. G. (2019). Machine
learning approach to auto-tagging online content for content marketing
efficiency: A comparative analysis between methods and content type.
Journal of Business Research, 101, 203–217.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j b  u s r  e s . 2
0 1  9 . 0 4 . 0 1 8
Sender, A., Rutishauser, L., & Staffelbach, B. (2018). Embeddedness across contexts:
A two-country study on the additive and buffering effects of job embed-
dedness on employee turnover. Human Resource Management Journal, 28(2),
340–356.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 1 1  / 1  7 4 8 - 8 5 8 3 . 1 2 1 8 3
Shin, J., Jo, M., Lee, J., & Lee, D. (2014). Strategic management of cloud comput-
ing services: Focusing on consumer adoption behavior. IEEE Transactions on
Engineering Management, 61(3), 419–427.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 0 9  / T  E M . 2 0 1 3
. 2 2 9 5 8 2 9
Shin, D., He, S., Lee, G. M., Whinston, A. B., Cetintas, S., & Lee, K. C. (2020). Enhancing
Social Media Analysis with Visual Data Analytics: A Deep Learning Approach.
MIS Quarterly, 44(4), 1459–1492.  h t t p  s : /  / d o i  . o  r g /  1 0 .  2 5 3 0  0 /  M I S Q / 2 0 2 0 / 1 4 8 7 0.
Shukla, A., Varshney, J., & Raj, A. (2024). Examining the linkage between managerial
ties and firm performance: The mediating role of marketing capabilities and
moderation role of industry - A meta-analytic approach. Industrial Marketing
Management, 119, 122–134.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i n  d m a  r m a n  . 2  0 2 4 . 0 4 . 0
1 0
Sirignano, J., & Cont, R. (2019). Universal features of price formation in financial
markets: Perspectives from deep learning. Quantitative Finance, 19(9),
1449–1459.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 8 0  / 1  4 6 9  7 6 8  8 . 2 0  1 9  . 1 6 2 2 2 9 5
Sjödin, D., Parida, V., Kohtamäki, M., & Wincent, J. (2020). An agile co-creation pro-
cess for digital servitization: A micro-service innovation approach. Journal of
Business Research, 112, 478–491.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j b  u s r  e s . 2  0 2  0 . 0 1 . 0 0 9
Sánchez-Franco, M. J., & Rey‐Moreno, M. (2022). Do travelers’ reviews depend on
the destination? An analysis in coastal and urban peer‐to‐peer lodgings.
Psychology & Marketing, 39(2), 441–459.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 2  / m  a r . 2 1 6 0 8
Su, C. T., Chen, Y. H., & Sha, D. Y. (2006). Linking innovative product development
with customer knowledge: A data-mining approach. Technovation, 26(7),
784–795.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t e  c h n  o v a t  i o  n . 2 0 0 5 . 0 5 . 0 0 5
Tambe, P . (2014). Big data Investment, Skills, and firm value. Management Science,
60(6), 1452–1469.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 2 8 7  / m  n s c . 2 0 1 4 . 1 8 9 9
Thakral, P ., Srivastava, P . R., Dash, S. S., Jasimuddin, S. M., Zhang, Z., & Justin (2023).
Trends in the thematic landscape of HR analytics research: A structural topic
modeling approach. Management Decision, 61(12), 3665–3690.  h t t p  s : /  / d o i  . o  r
g /  1 0 .  1 1 0 8  / M  D - 0 1 - 2 0 2 3 - 0 0 8 0
Tirunillai, S., & Tellis, G. J. (2014). Mining Marketing Meaning from Online Chatter:
Strategic Brand Analysis of Big Data Using Latent Dirichlet Allocation. Journal
of Marketing Research, 51(4), 463–479.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 5 0 9  / j  m r . 1 2 . 0 1 0 6.
Tiwari, S. (2023). Smart warehouse: A bibliometric analysis and future research
direction. Sustainable Manufacturing and Service Economics, 2, 100014.  h t t p  s : /  /
d o i  . o  r g /  1 0 .  1 0 1 6  / j  . s m s e . 2 0 2 3 . 1 0 0 0 1 4
Tussyadiah, I. P ., Wang, D., Jung, T. H., & Tom Dieck, M. C. (2018). Virtual reality,
presence, and attitude change: Empirical evidence from tourism. Tourism
Management, 66, 140–154.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t o  u r m  a n . 2  0 1  7 . 1 2 . 0 0 3
Valletti, T., & Wu, J. (2020). Consumer profiling with data requirements: Structure
and policy implications. Production and Operations Management, 29(2),
309–329.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 1 1  / p  o m s . 1 3 1 0 8
Van Pinxteren, M. M. E., Wetzels, R. W. H., Rüger, J., Pluymaekers, M., & Wetzels, M.
(2019). Trust in humanoid robots: Implications for services marketing. Journal
of Services Marketing, 33(4), 507–518.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 0 8  / J  S M - 0 1 - 2 0 1 8 - 0
0 4 5
Vlačić, B., Corbo, L., Costa, E., Silva, S., & Dabić, M. (2021). The evolving role of
artificial intelligence in marketing: A review and research agenda. Journal of
Business Research, 128, 187–203.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . j b  u s r  e s . 2  0 2  1 . 0 1 . 0 5 5
Wang, G., Gunasekaran, A., Ngai, E. W. T., & Papadopoulos, T. (2016). Big data analyt-
ics in logistics and supply chain management: Certain investigations for
research and applications. International Journal of Production Economics, 176,
98–110.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . i j p e . 2 0 1 6 . 0 3 . 0 1 4
Wang, L., Jia, F., Chen, L., & Xu, Q. (2023a). Forecasting smes’ credit risk in supply
chain finance with a sampling strategy based on machine learning tech-
niques. Annals of Operations Research, 331(1), 1–33.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s
1 0 4 7 9 - 0 2 2 - 0 4 5 1 8 - 5
Wang, S., Yu, H., & Wei, M. (2023b). The effect of supply chain finance on sustain-
ability performance: Empirical analysis and FsQCA. Journal of Business &
Industrial Marketing, 38(11), 2294–2309.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1 0 8  / J  B I M - 0 3 - 2 0
2 2 - 0 1 5 4
Won, J. Y., & Park, M. J. (2020). Smart factory adoption in small and medium-sized
enterprises: Empirical evidence of manufacturing industry in Korea. Techno-
logical Forecasting and Social Change, 157, 120117.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . t
e  c h f  o r e .  2 0  2 0 . 1 2 0 1 1 7
Wu, T. J., Liang, Y., & Wang, Y. (2024). The buffering role of workplace mindfulness:
How job insecurity of human-artificial intelligence collaboration impacts
employees’ work–life-related outcomes. Journal of Business and Psychology,
39(6), 1395–1411.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 0 8 6 9 - 0 2 4 - 0 9 9 6 3 - 6
Yaoteng, Z., & Xin, L. (2022). Research on green innovation countermeasures of
supporting the circular economy to green finance under big data. Journal of
Enterprise Information Management, 35(4/5), 1305–1322.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 1
0 8  / J  E I M - 0 1 - 2 0 2 1 - 0 0 3 9
Yu, C. E., Xie, S. Y., & Wen, J. (2020). Coloring the destination: The role of color
psychology on Instagram. Tourism Management, 80, 104110.  h t t p  s : /  / d o i  . o  r g /  1
0 .  1 0 1 6  / j  . t o  u r m  a n . 2  0 2  0 . 1 0 4 1 1 0
Zhang, H., Rao, H., & Feng, J. (2018). Product innovation based on online review
data mining: A case study of Huawei phones. Electronic Commerce Research,
18(1), 3–22.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 0 7  / s  1 0 6 6 0 - 0 1 7 - 9 2 7 9 - 2
Zhang, M., Fried, D. D., & Griffeth, R. W. (2012). A review of job embeddedness:
Conceptual, measurement issues, and directions for future research. Human
Resource Management Review, 22(3), 220–231.  h t t p  s : /  / d o i  . o  r g /  1 0 .  1 0 1 6  / j  . h r m r
. 2 0 1 2 . 0 2 . 0 0 4
Zhen, R., Song, W., He, Q., Cao, J., Shi, L., & Luo, J. (2023). Human-Computer interac-
tion system: A survey of Talking-Head generation. Electronics, 12(1), 218.  h t t p  s :
/  / d o i  . o  r g /  1 0 .  3 3 9 0  / e  l e c  t r o  n i c s  1 2  0 1 0 2 1 8
Zhu, Y., Zhou, L., Xie, C., Wang, G. J., & Nguyen, T. V. (2019). Forecasting smes’ credit
risk in supply chain finance with an enhanced hybrid ensemble machine
learning approach. International Journal of Production Economics, 211, 22–33.
h t t p s :   /  / d o  i .  o r  g  /  1 0  . 1 0   1   6 / j . i  j p e .  2 0 1  9 . 0 1 . 0 3 2
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in
published maps and institutional affiliations.
