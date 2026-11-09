---
title: Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
url: https://arxiv.org/abs/2404.01358
category: social-media
subcategory: empirical
date: 2024-04
venue: ''
authors:
- Alon Bartal
- Kathleen M. Jagodnik
- Nava Pliskin
- Abraham Seidmann
source: arxiv
pdf_url: https://arxiv.org/pdf/2404.01358
pages: 19
chars: 64009
fetched_at: '2026-11-08T13:05:24+00:00'
kb_version: 1
---

# Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists

UTILIZING AI AND SOCIAL MEDIA ANALYTICS TO DISCOVER
ADVERSE SIDE EFFECTS OF GLP-1 R ECEPTOR AGONISTS ∗
Alon Bartal, Kathleen M. Jagodnik
The School of Business Administration
Bar-Ilan University
Ramat Gan, Israel
{bartal.alon, kathleen.jagodnik}@biu.ac.ill
Nava Pliskin
Department of Industrial Engineering & Management
Ben-Gurion University of the Negev
Beer-Sheva, Israel
pliskinn@bgu.ac.il
Abraham Seidmann
Questrom School of Business
Boston University
Boston, MA, USA
avis@bu.edu
ABSTRACT
Adverse side effects (ASEs) of drugs, revealed after FDA approval, pose a threat to patient safety. To
promptly detect overlooked ASEs, we developed a digital health methodology capable of analyzing
massive public data from social media, published clinical research, manufacturers’ reports, and
ChatGPT. We uncovered ASEs associated with the glucagon-like peptide 1 receptor agonists (GLP-1
RA), a market expected to grow exponentially to $133.5 billion by 2030. Using a Named Entity
Recognition (NER) model, our method successfully detected 21 potential ASEs overlooked upon FDA
approval, including irritability and numbness. Our data-analytic approach revolutionizes the detection
of unreported ASEs associated with newly deployed drugs, leveraging cutting-edge AI-driven social
media analytics. It can increase the safety of new drugs in the marketplace by unlocking the power of
social media to support regulators and manufacturers in the rapid discovery of hidden ASE risks.
Keywords Adverse Side Effect (ASE) · AI · Data Analytics · Glucagon-Like Peptide 1 Receptor Agonist (GLP-1
RA) · Knowledge Discovery · Social Media
1 Introduction
Over recent decades, obesity has surged as a global health crisis [1], with numbers nearly tripling since 1975, surpassing
650 million individuals globally, among 1.9 billion adults who are overweight [1]. Obesity significantly elevates the
risk of developing an array of health disorders, including type 2 diabetes (T2D), high blood pressure, heart disease,
respiratory problems, joint problems, and gallbladder disease [2, 3, 4]. The consequences of obesity are projected to
consume more than 3% of the gross domestic product in the United States (U.S.) in the coming decades [5].
Glucagon-like peptide 1 receptor agonists (GLP-1 RA), used to treat obesity and T2D, effectively reduce weight,
improve comorbidities, and lower blood sugar levels [6]. Since the U.S. Food and Drug Administration (FDA) approved
the first drug in this class, exenatide, in 2005, the use of GLP-1 RA such as dulaglutide (Trulicity), liraglutide (Victoza),
and semaglutide (Ozempic, Rybelsus) has surged [7]. In 2023, prescriptions spiked, driven by both T2D and obesity
treatments [8]. Semaglutide’s popularity, fueled by celebrity uses for weight loss, led to supply shortages [ 9, 10].
However, GLP-1 RA also have documented Adverse Side Effects (ASEs), including gastrointestinal disorders, metabolic
problems, and eye, renal, urinary, and nutritional disorders [11, 12]. Because some drugs in this class were approved in
recent years (e.g., Ozempic in 2017 [13]), their complete ASE profiles remain under-characterized, since clinical trials,
∗Citation: Bartal et al., Utilizing AI and Social Media Analytics to Discover Side Effects of GLP-1 Receptor Agonists.
Pages.... DOI:000000/11111.
arXiv:2404.01358v1  [q-bio.QM]  1 Apr 2024

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
typically involving only a few thousand human subjects, often cannot detect rare ASEs or those with significant latent
development [14]. Moreover, clinical trials can overlook real-world scenarios, necessitating careful consideration of the
relevance of their findings for larger and more diverse populations. For example, non-obese individuals who use GLP-1
RA for weight loss are not commonly represented in clinical trials. Limited knowledge about ASEs solely from clinical
trials lead physicians to prescribe medications with incomplete information, risking patient safety.
Furthermore, some FDA-approved drugs have been withdrawn from the market when their ASEs became known only
after widespread use [15, 16, 17]. Thalidomide, for example, was prescribed to women during pregnancy to treat nausea,
but led to severe birth defects in infants whose mothers had taken the drug, ultimately resulting in its withdrawal from
the market [15]. Vioxx, which was approved by the FDA for the treatment of pain and inflammation associated with
arthritis, was eventually withdrawn due to its being associated with increased risk of heart attack and stroke [18].
These historical pharmacological precedents motivate the need to add another layer of safety beyond the initial FDA
approval. Our proposed digital health methodology can serve as an effective ‘early warning’ sensor. The approach
should continuously monitor users’ communities following the introduction of any new drug to identify any previously
unreported ASEs that may stem from patients’ biology, unexpected drug interactions, or individual lifestyle choices.
Drug ASEs are already recorded in databases such as the FDA Adverse Event Reporting System (FAERS) [19], the
Side Effect Resource (SIDER) [20], MEDLINE [21], and Embase [22]. However, these databases suffer from improper
indexing [23] and incomplete reporting [ 24], with up to 86% of ASEs unreported [ 24]. Moreover, publishing bias
favoring positive results, as well as practices that may conceal negative data in publications [25, 26, 27], can lead to
incomplete recording of ASEs. Additionally, the diversity of resources providing data about ASEs, the heterogeneous
and incomplete nature of these data [ 24], and failure of patients to report side effects [ 28] make it challenging to
definitively characterize the ASEs of any drug [24, 29].
Social media can supplement these resources by allowing researchers to preemptively detect ASEs before regulatory
intervention [30]. For example, social media analyses have been conducted to identify ASEs of medications for HIV
[31, 32], chemotherapy for cancer [33, 34], and buprenorphine-naloxone treatment for opioid use [35]. Specifically,
Reddit [31, 35, 33, 32] and X (formerly Twitter) [34, 36, 37] have been used to discover pharmacovigilance knowledge.
The Reddit social media platform enables anonymous accounts, encouraging users to share ASE experiences more
honestly compared with other platforms [38], as anonymity often leads individuals to disclose information more freely
[39, 40, 41]. Reddit also permits more substantial exchanges, compared with X, which limits users to brief posts.
However, the briefer X posts can also provide significant information about ASEs reported by users [42, 43, 36, 37, 44]
and about other aspects of drug usage [45, 46].
Using social media analysis, Adjeroh et al. found that ASEs could be detected 3 to 35 months before an FDA alert
was issued, depending on the drug [47]. A scoping review of social media use for pharmacovigilance [30] reported
that social media monitoring can facilitate the detection of labeling changes, black box warnings, or drug withdrawals
3 months to 9 years in advance. Additionally, recent meta-analysis [48] has shown that a higher prevalence of ASE
discussions on social media is associated with a shorter time to drug recall [48].
The rising popularity of GLP-1 RA has led to a surge in online searching [10, 49] and social media posting [50] about
them, offering valuable data to supplement existing pharmacovigilance sources [ 42]. While social media posts do
provide abundant information about GLP-1 RA, previous research has mainly focused on small-scale data [51, 52]. For
instance, recent analysis of the top 100 results of TikTok videos tagged #Ozempic revealed that most videos emphasized
personal experiences and promoted the drug for weight loss, potentially contributing to increased demand [51]. That
study stressed the importance of collaboration among healthcare professionals, regulatory bodies, and social media
platforms to address challenges like drug shortages. Another small-scale study on TikTok compared 16 videos in
total, highlighting how Ozempic users framed obesity as a disease, unlike discussants of traditional diet methods [52].
Researchers have also started to use the abundant information that social media offers about GLP-1 RA for broader
analysis. For example, a recent large-scale study [53] analyzed tens of thousands of posts on Reddit (12,136), YouTube
(14,515), and TikTok (17,059) and uncovered associations between GLP-1 RA and various mental health issues. Our
work responds to the authors’ call for further study to capture subsequent comments after prolonged drugs use.
Training Natural Language Processing (NLP) models, including those utilizing Named Entity Recognition (NER), is
integral to extracting knowledge from unstructured text sources such as social media posts, electronic medical records,
and medical literature [54]. NER plays a crucial role in identifying biomedical entities such as drugs, symptoms, and
diseases mentioned in the text, with potential implications for linking them to ASEs [ 54]. Advanced NER models,
leveraging deep-learning techniques [55], and utilizing contextual information surrounding entities within sentences,
benefit from Large Language Models (LLMs) that are typically pre-trained on massive publicly and freely available text
on the Internet, encompassing books, articles, and webpages [56]. LLMs possess the capability to receive and generate
text queries while adapting to a variety of language-related tasks beyond their primary training objective [57].
2

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
In the medical field, LLMs have been applied to tasks like responding to medical exams and addressing patient queries.
Despite the risk of generating inaccurate outputs, healthcare providers are increasingly integrating LLMs into clinical
applications [58]. Noteworthy examples include LLM use in medical resident training modules and in partnerships of
healthcare providers that incorporate electronic health records [59, 60]. Within the landscape of general LLMs, the
Generative Pre-trained Transformers (GPT) lineage, particularly exemplified by OpenAI’s ChatGPT, emerges as a
frequently used choice, especially in chat applications [57].
ChatGPT is an LLM known for generating informative text and mimicking human-like writing [61, 62]. It has been
widely used in various scientific domains, including mental health research [63, 64], medical research [65, 66], and
detecting drug interactions [67]. However, ChatGPT’s capabilities have not yet been used to study GLP-1 RA, presenting
a valuable opportunity for knowledge discovery through the methods harnessed in the present study.
Computational-based algorithms have already facilitated understanding of drug ASEs, including identifying when they
occur [68, 69]. Accurate assessment of ASE frequencies is crucial for patient care in clinical practice. Drug-related
ASEs persist as a significant cause of morbidity and mortality in healthcare, resulting in substantial economic costs,
amounting to an estimated annual cost of $495-672 billion in the U.S. alone [70]. Moreover, accurate estimation can
help pharmaceutical companies to mitigate the risk of a drug’s withdrawal from the market [71] and avoid the need for
costly reassessment of ASEs through new clinical trials [72].
This study contributes to the understanding of ASEs related to GLP-1 RA through a multifaceted knowledge-discovery
methodology. Our approach mines data from social media, extending beyond existing pharmacovigilance insights
provided by drug manufacturers and clinical trials, to comprehensively identify and analyze the ASEs of GLP-1 RA.
Our construction of an ASE-ASE network, based on co-mentioned ASEs in social media posts, represents a novel
approach to revealing groups of ASEs with similar network patterns. We further contribute by applying network
community detection and classification based on mention frequency, offering a nuanced perspective on ASE prevalence
and interconnections. Overall, our study contributes methodologically and conceptually by offering valuable insights
for drug safety assessment, public health management, and the broader understanding of GLP-1 RA related ASEs.
The rest of this paper is organized as follows: Section 2 elaborates on the research question and hypotheses. Section 3
provides a detailed description of the methodology employed. It also presents the characteristics of the data sources we
used to produce Section 4’s results. Finally, the discussion and conclusions in Section 5 interpret the findings in the
context of the existing literature, explore their implications, and summarize key insights that suggest future research.
2 Research Questions and Hypotheses
RQ1. How can we identify unreported ASEs of GLP-1 RA based on social media discussions?
Health-focused individuals frequently use social media platforms to seek advice and exchange experiences with others,
especially concerning ASEs [73, 74]. These textual posts can be mined using NLP models. Thus, we hypothesize:
H1. A Named Entity Recognition (NER) model applied to social media posts can uncover ASEs of GLP-1 RA that are
not observed by traditional pharmacovigilance methods.
3 Materials and Methods
3.1 Data
We collected five datasets covering biomedical knowledge and social media posts involving the GLP-1 RA that are
included on our 12-item Medication List, including both brand names and generic drug names: dulaglutide (brand
name: Trulicity), exenatide (brand names: Byetta; Bydureon - extended-release), liraglutide (brand name: Victoza),
lixisenatide (brand name: Adlyxin), and semaglutide (brand names: Ozempic - injections; Rybelsus - tablets).
Dataset 1: X – Using the APIfy2 website, we collected the 1,000 most recent posts from 2017 to 2023 that mentioned
each of the 12 items on our Medication List. This produced a dataset that includes 11,185 posted texts, each with
associated data on the posting user, posting time, and GLP-1 receptor agonist mentioned.
Dataset 2: Reddit – Using the Python Reddit API Wrapper (PRAW) package [75], we collected 489,529 posts and
comments from 14 subreddits (Table 1) related to the 12 items on our Medication List. The posts originated in 2022 and
2023. Each collected Reddit post includes the following metadata: ‘Post ID’, ‘Post Author’, ‘Post Content’, ‘Post Date’,
‘Comment ID’, ‘Comment Author’, ‘Comment Content’, ‘Parent ID’, and ‘Parent Author’.
2https://console.apify.com
3

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Table 1: Subreddits that were used to collect social media posts involving GLP-1 RA.
Subreddit # Members ∗
r/diabetes 109K
r/diabetes_t2 29.4K
r/GLP1 1.3K
r/liraglutide 11.7K
r/loseit 3900K
r/MaintenancePhase 25.6K
r/medicine 453K
r/Ozempic 50.1K
r/OzempicForWeightLoss 13.7K
r/semaglutidecompounds 7.2K
r/Semaglutide 45K
r/TheMorningToastSnark 11.6K
r/trulicity 1.1K
r/type2diabetes 8.4K
∗Number of members (in thousands) of each subreddit as of October 2, 2023.
Dataset 3: PubMed. Using the National Center for Biotechnology Information (NCBI) PubMed E-utilities API
(PubMed API) [76] and the Biopython Python library [77], we collected 13,491 articles indexed from 2017 to 2024 in
PubMed that contained at least one item on our Medication List in the title or in the abstract of the article.
Dataset 4: SIDER (Side Effect Resource). We utilized the meddra_all_se.tsv.gz dataset from the SIDER
database version 4.1, which catalogs 5,868 documented ASEs for 1,430 commercially available drugs. SIDER compiles
this information from publicly accessible drug documents and package inserts, providing details on drug names, ASE
frequencies, and classifications.
Dataset 5: Side Effects Reported by Manufacturers and by ChatGPT. We manually searched on the web to
collect ASEs reported by drug manufacturers, whose reports primarily include structured data from clinical trials
and post-marketing surveillance. Table 2 shows the latest update dates for GLP-1 RAs’ ASEs by manufacturers. We
recorded all prominent ASEs reported in the manufacturers’ documents, focusing on data recorded from clinical trials
with human subjects, and omitting side effects reported only in animal models. To address potential gaps in the manually
searched ASE data reported by manufacturers, we integrated them into Dataset 5 with commonly reported ASEs that
we collected from ChatGPT (GPT-3.5) by using the interactive web interface. For this collection, we utilized the
prompt: ‘Please provide a list of adverse side effects for the GLP-1 receptor agonist named S,’ where S corresponds
to an item on our GLP-1 RA Medication List. ChatGPT’s responses may incorporate a broader range of information,
potentially including insights from social media or medical literature, that is not explicitly included in our manual
search of manufacturers’ reports. This approach ensures that Dataset 5 aligns more closely with the timeframes of
Datasets 1 and 2, covering information up to and including 2023, and Dataset 3, which covers information up to and
including January 2024.
3.2 Methods
In Sections 3.2.1 and 3.2.2, we describe the method used to identify ASEs of GLP-1 RA in Datasets 1 to 3, and to
validate the identified ASEs against Dataset 4 in comparison with Dataset 5. In Section 3.2.3, we study the frequency of
ASE mentions on social media. Finally, in Section 3.2.4, we describe the method employed to construct an ASE-ASE
network, which is based on co-mentions of ASEs within the same social media post (Datasets 1 and 2), and detail
our approach to detecting ASEs that tend to co-occur by clustering ASE nodes in an ASE-ASE network based on the
frequency of their mentions in the posts.
Fig. 1 summarizes the steps of our approach to address the two research questions.
3.2.1 Identification of Adverse Side Effects
To identify ASEs of FDA-approved GLP-1 RA, we analyzed the texts in Datasets 1 to 3 and extracted biomedical
entities, which included ASEs. This process used the ScispaCy pre-trained NER model [ 78], specifically employing the
en_ner_bc5cdr_md NER model to identify biological entities. This approach follows the strategy of utilizing ScispaCy
for extracting pharmaceutical-related phrases, including dosage, diseases, and symptoms from electronic medical
4

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Table 2: Last update dates and side effect URLs for GLP-1 RA
Drug Name Brand Name Last Update Side Effects URL
Exenatide Byetta 2009 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2009/
021773s9s11s18s22s25lbl.pdf
Lixisenatide Adlyxin 2016 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2016/
208471orig1s000lbl.pdf
Dulaglutide Trulicity 2017 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2017/
125469s007s008lbl.pdf
Exenatide Bydureon 2017 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2017/
209210s000lbl.pdf
Semaglutide Ozempic 2017 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2017/
209637lbl.pdf
Liraglutide Victoza 2019 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2019/
022341s031lbl.pdf
Semaglutide Rybelsus 2019 https://www.accessdata.fda.gov/
drugsatfda_docs/label/2019/
213051s000lbl.pdf
Data collection
X
Redddit
PubMed
Identify
biomedical
entities
Identify
side
effects
Create a
side effect
network
Classify side effects
by  frequency
Cluster side effects via
community detection
SIDER
PubMedSocial media (Reddit and X)
ChatGPT and manufacturers’
reported side effects
Side effect overlap
Figure 1: Overview of the methodology of this research.
records [54]. To ascertain whether these identified biological entities are potential ASEs of GLP-1 RA, we matched
them against the ASEs catalogued in SIDER [20], which were collected in Dataset 4. This involved normalizing the
potential ASEs and those in SIDER to lowercase and employing NLP stemming to reduce words to their root forms
[79]. Each entity was considered a potential ASE if it existed in SIDER [20]. To the resulting compilation of ASEs, we
added ASEs collected in Dataset 5 from manufacturers’ reports and ChatGPT. Then, we grouped similar ASEs, for
example, combining ‘headache’ and ‘migraines’ and standardized ASEs into their noun forms. Consolidating these
diverse sources facilitated comprehensively identifying ASEs.
3.2.2 Method Evaluation: Identify Unreported ASEs
We examined all ASEs identified in the social media data and classified them into one of two group:
• Established ASEs: ASEs reported by manufacturers and ChatGPT.
• Novel ASEs: ASEs identified by our modeling approach but not reported by manufacturers and ChatGPT.
If our method is able to identify established ASEs, we can confidently explore novel ASEs that we discovered and
hypothesize their novelty. Therefore, we evaluated our method’s performance in identifying established ASEs by
defining the Overlap score (Equation 1):
Overlap (f%) =|Pf% ∩ Id|/|Id| (1)
5

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Pf % - The set of established and novel ASEs identified in social media data located in the top f% of a ranking, based on
the mentioned frequency of ASEs.
Id - The set of established ASEs.
A higher Overlap score indicates greater success identifying established ASEs. A maximum Overlap of 1 indicates that
all established ASEs were captured on social media, whereas a minimum Overlap of 0 indicates that no established
ASEs were captured.
3.2.3 Analysis of Adverse Side Effects Mention Frequency
Addressing RQ1, which focuses on identifying novel ASEs based on social media data, we effectively separate and
detail the frequency of ASE mentions on social media for each specific GLP-1 RA. Additionally, we tracked mentions
of ASEs on social media along intervals of 14 days. To measure ASE frequency over time, we defined two frequency
measures, considering only ASEs with more than ten mentions per interval:
• Pre-mention average frequency (Pre-MAF): average mentions before a selected point in time.
• Post-mention average frequency (Post-MAF): average mentions after a selected point in time.
We define a positive slope in mention frequency as Pre-MAF < Post-MAF, a negative slope as Pre-MAF > Post-MAF,
and no slope otherwise.
Furthermore, we queried Google Trends [80] for each specific GLP-1 RA on our Medication List. This web service
offers insights into how frequently a particular term is searched relative to the total search volume on Google. In Google
Trends the highest score, 100, represents the peak popularity of a particular term during the specified period, and the
scores for other items are relative to this peak.
3.2.4 Analysis of Adverse Side Effects
Using the ASEs identified in the social media posts of Datasets 1 and 2 (Section 3.2.1), we built an ASE-ASE network
denoted by G = (V, E, W). In G, nodes (V ) are identified ASEs. Two nodes mentioned in the same post are connected
by an edge (E). The weights of the edges (W ) represent the frequency of two ASEs being mentioned together in posts.
Identifying the co-occurrence patterns of ASEs, which is crucial in pharmacovigilance drug safety analysis [81], was
accomplished in two steps. We first investigated ASE-ASE clustering inG using a community detection algorithm, as de-
tailed below. Next, to improve risk assessment, inform treatment decisions, and contribute to overall pharmacovigilance
and public health management, we classified ASEs by the frequency with which each was mentioned.
Clustering of ASEs by network community detection. To identify sets of interconnected ASEs, we applied the
cluster_louvain node-clustering algorithm from the igraph R library to ASE-ASE network G. This algorithm
employs a multi-level modularity optimization function, leveraging the modularity measure and adopting a hierarchical
methodology. Clustering nodes into community groups enabled the identification of ASEs that frequently co-occur
beyond a direct 1-hop edge in G.
Classification of ASEs by mention frequency. We also classified ASE nodes by the frequency with which each was
mentioned in the social media posts of Datasets 1 and 2. Specifically, each ASE node was classified into one of the
following groups (as defined in [81]): Very Rare, Rare, Infrequent, Frequent, and Very Frequent. This labeling approach
was used to estimate the ASE frequency.
4 Results
In Section 4.1, we identify ASEs and evaluate our method’s performance in identifying established and novel adverse
side effects (ASEs). Then, In Section 4.2, we analyze the frequency of ASE mentions across social media (Datasets 1
and 2), academic literature (Dataset 3), and manufacturer and ChatGPT reports (Dataset 5), exploring temporal trends
and correlations with external events. Finally, in Section 4.3, we uncover clusters of interconnected ASEs and their
mention frequencies.
4.1 Identify Adverse Side Effects of GLP-1 RA
Using the methods described in Section 3.2, we identified 134 ASEs of GLP-1 RA (Appendix Table A). Fig. 2 presents
a Venn diagram showing the overlaps and distinctions among these ASEs. The bar charts in Fig. 2 indicate ASE mention
frequency in social media (Datasets 1, 2) and academic papers (Dataset 3), as well as ASE percentage frequency as
6

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
5
6
Blurred Vision, Non-Proliferative Retinopathy,
and Diabetic Retinopathy (15) 7
14
32
Figure 2: Venn diagram offering a visual representation of and distinction among ASEs.
reported by drug manufacturers (Dataset 5). There are seven subgroups in the Venn diagram (intersection, union,
and disjoint): Group 1 lists ASEs found in academic papers, social media, and manufacturers’ reports or reported by
ChatGPT. Group 2 lists ASEs reported in academic papers and mentioned on social media. Group 3 lists ASEs reported
exclusively in academic papers. Group 4 lists ASEs reported by ChatGPT and in manufacturers’ reports. Group 5 lists
ASEs mentioned exclusively on social media. Group 6 lists ASEs mentioned on social media, by ChatGPT, and in
manufacturers’ reports. Group 7 lists ASEs mentioned in academic papers, by ChatGPT, and in manufacturers’ reports.
The frequencies of ASEs in Group 7 are summed to 15, as they describe similar ASEs: Blurred Vision, Non-Proliferative
Retinopathy, and Diabetic Retinopathy.
4.1.1 Model Evaluation: Identify Novel ASEs
Following Section 3.2.2, established ASEs are listed in Groups 1, 4, 6, and 7 in Fig. 2, and novel ASEs are listed in
Groups 2 and 5.
Fig. 3 indicates the success of our model’s identification of established ASEs as a function of Pf % ranging between
10% to 100% with increments of 10%. More specifically, it shows that the Overlap score increases with Pf %. For
example, when Pf % = 100%, indicating inclusion of all ASEs identified on social media, Overlap = 53%shows that
our model identified 53% of established ASEs. Similarly, in a recent study [ 82], a model was developed to predict
drug-drug ASEs, with evidence found for 50% of the identified ASEs in the literature.
Next, following the identification of novel ASEs, we analyzed their frequency.
4.2 Analysis of ASE Mention Frequency
Following Section 3.2.3, Fig. 4 shows that Ozempic, which is the most frequently prescribed GLP-1 RA, has the largest
group of associated ASEs.
7

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
0
0.1
0.2
0.3
0.4
0.5
0.6
10 20 30 40 50 60 70 80 90 100
Overlap
Pf%
Figure 3: Overlap score as a function of Pf %.
Tracking mentions of ASEs on social media along intervals of 14 days (Fig. 5), we found that the ASEs mentioned most
frequently over time are constipation, nausea, pain, and vomiting. We observed a sharp spike in these ASEs starting on
September 24, 2023. This date was selected to measure ASE frequency over time. We observe an overall positive slope
(Pre-MAF < Post-MAF) for anxiety, constipation, nausea, pain, and vomiting, an overall negative slope for fatigue, and
no slope for depression (Table 3).
Table 3: Frequency of adverse side effect (ASE) mentions before and after the observed spike in mentions.
Adverse Side Effect Pre-MAF Post-MAF Slope
Anxiety 18.0 20.0 +
Constipation 29.0 35.0 +
Depression 15.5 15.5 0
Fatigue 17.6 14.6 -
Nausea 39.1 57.8 +
Pain (abdominal pain, back pain) 20.5 36.0 +
V omiting 20.5 27.0 +
To better understand the spike, we queried Google Trends [80] for the entries on our Medication List (Fig. 6) with
geographic location, category, and time range specified as ‘Worldwide’, ‘Web Searches’, and ‘Between 9/21/23 and
9/27/23’ (i.e., 3 days before and after the 9/24/23 spike in Fig. 5); we also filtered for ‘health’-related searches. Similar
to Fig. 5, Fig. 6 shows a spike on September 25, 2023, for the search terms ‘Dulaglutide’, ‘Ozempic’, ‘Liraglutide’,
‘Trulicity’, and ‘Rybelsus’. The black dashed line in Fig. 6 represents a spike (Table 3; Pre-MAF < Post-MAF) in
searches for ‘Dulaglutide’, ‘Ozempic’, ‘Liraglutide’, ‘Trulicity’, and ‘Rybelsus’ on September 25, 2023. The Google
Trends delay of one day in the spike observed on September 24 may be attributed to the tendency of social media
discussions to peak before gaining widespread attention through Google searches. This temporal offset could arise
from social media users acting as early adopters of a particular GLP-1 RA or possessing particular interest in a specific
GLP-1 RA, thereby influencing the timing difference between the two spikes.
A further Google search for the analyzed time range helped to explain the spike by revealing that on her September 22,
2023, show, Oprah Winfrey, together with a panel of experts, addressed the growing trend of using weight-loss drugs.
She shared her initial reluctance to use such drugs, emphasizing the societal pressure to rely on personal effort rather
than medication. The panel challenged the notion of weight loss solely relying on willpower and highlighted the roles
of genetics and individual differences.
4.3 Analysis of Adverse Side Effects
Following Section 3.2.4, based on the unprocessed social media data (Datasets 1 and 2), we constructed an ASE-ASE
weighted and non-directed network G = (V, E, W). To emphasize that our method can identify ASEs in raw social
8

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Figure 4: ASE mention frequency (> 1) on X and Reddit for each GLP-1 receptor agonist.
9

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
2023
-10
-22
2023
-07
-16
2023
-07
-02
2023
-07
-30
2023
-08-27
2023
-11
-05
2023
-08-13
2023
-09
-24
2023
-09
-10
2023
-10
-08
2023
-11
-19
Time interval
Pain
Nausea
Constipation
Anxiety
Fatigue
Depression
Vomiting
Figure 5: ASEs mentions > 10 in each of the 14-day intervals on X and Reddit.
0
20
40
60
80
100
120
2023-09-21 2023-09-22 2023-09-23 2023-09-24 2023-09-25 2023-09-26 2023-09-27
Adlyxin Bydureon Byetta Dulaglutide Exenatide Liraglutide
Lixisenatide Ozempic Rybelsus Semaglutide Trulicity Victoza
Figure 6: Google Trends queries for GLP-1 RA on our Medication List.
10

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Anxiety Arthritis Bulimia Choking Constipation Cough Cramps Dehydration Delirium
Depressed Diarrhea Distress Dizziness Drowsiness Fatigue Fibromyalgia Headache Heartburn
Hiccups Hunger pains Hypertension HypomaniaHypothyroidism Hysteria Inflammation Insomnia Irritable
Jaundice Ketosis Labyrinthitis Lethargy Lightheadedness Mania Migraines Nausea Neuropathy
Numb Osteoarthritis Palpitations Paralysis Phobias Pneumonia Puberty Rash Retching
Schizophrenia Shakiness Swelling Tachycardia Thirst Thyroiditis Tinnitus Trauma Vertigo
V omit Worry Anger Anorexia Aches Apathy Burns Gastritis Hyperthyroidism
Ketonemia Auras Acidosis Adenomyosis Chills Endometriosis Dermatitis Encephalitis Hoarseness
Cardiomegaly Hypotension Onycholysis Cold sweats Ileus Overdosed
Figure 7: The ASE-ASE network G based on social media posts.
media discussions (RQ1), unlike in Section 4.1, we neither combined similar ASEs nor standardized ASEs into noun
forms here.
We identified 381 potential ASEs with 1,440 ASE-ASE interactions co-mentioned in the same post. To reduce noise
and focus on ASEs only, we manually removed 52 falsely identified ASEs, ASE-ASE interactions with fewer than 3 co-
mentions, and ASE nodes with no co-mentions in the data (having degree centrality 0). We also used the components
function within the igraph R library [83] to detect graph components. The algorithm detected three components of
sizes 2, 2, and the main component of 78 nodes. We set G as the main component graph with 78 ASE nodes and 253
weighted edges. In Fig. 7, nodes are ASEs and edges represent ASE-ASE co-mentioned relationships identified in X
and Reddit posts.
Clustering of ASE nodes by network community. To identify sets of interconnected ASEs, we applied clustering
analysis to G using the cluster_louvain node-clustering algorithm [ 84]. We discovered four clusters (Fig. 7)
with 34, 23, 19, and 2 ASE nodes, respectively. The node colors in Fig. 7 correspond to membership in each of the
four clusters; node size is proportional to its degree, and edge width is proportional to its weight, representing the
co-mention frequency. In Fig. 7, Cluster 1 (light blue) contains aches, acidosis, adenomyosis, apathy, auras, chills, cold,
constipation, cramps, dehydration, diarrhea, distress, dizziness, drowsiness, endometriosis, fatigue, headache, heartburn,
hiccups, hunger, ileus, labyrinthitis, lethargy, lightheadedness, migraines, nausea, overdosed, phobias, puberty, retching,
tachycardia, thirst, vertigo, and vomiting. Cluster 2 (red) contains anger, anorexia, anxiety, bulimia, cardiomegaly,
choking, cough, delirium, depressed, hypomania, hypotension, hysteria, insomnia, irritable, mania, neuropathy, numb,
onycholysis, palpitations, shakiness, tinnitus, trauma, and worry. Cluster 3 (green) contains arthritis, burns, dermatitis,
fibromyalgia, gastritis, hoarseness, hypertension, hyperthyroidism, hypothyroidism, inflammation, jaundice, ketonemia,
ketosis, osteoarthritis, paralysis, pneumonia, rash, swallowing, and thyroiditis. Cluster 4 (purple) contains encephalitis
and schizophrenia. Additionally, we revealed similar ASEs that affiliate with the same cluster, such as ‘headache’ and
‘migraines’ (Fig. 7).
11

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
5 Discussion and Conclusions
Obesity is a major health concern globally, affecting over 650 million individuals around the world [85]. GLP-1 RA
used to treat obesity and T2D have demonstrated efficacy in reducing excess weight, improving comorbidities, and
lowering blood sugar levels [7]. Because some GLP-1 RA were approved quite recently, their complete ASE profiles
might remain under-reported or be overlooked in conventional studies. Clinical trials involving a few thousand human
subjects are known to have difficulties in detecting ASEs that are rare or have a significant latency of development.
Moreover, GLP-1 RA were originally developed to treat T2D, as opposed to obesity. To address this knowledge gap
about ASEs, which poses risks for patients and physicians, we develop and present in this study a knowledge discovery
approach that incorporates social media data and pharmacovigilance information to identify novel ASEs of GLP-1 RA.
To identify ASEs in texts, we applied a Named Entity Recognition (NER) model to analyze posts from X and Reddit
that discuss GLP-1 RA, as well as academic papers that study GLP-1 RA. We also gathered ASEs along with their
frequency from ChatGPT and manufacturers’ reports. Many ASEs are included in all of our datasets, yet 16 out of
134 (12%) are reported exclusively by academic studies, 14 (10%) solely by manufacturers, and 21 (15%) only on
social media. Social media provides a vast and diverse source of information, as demonstrated here, capturing a broader
spectrum of user perspectives than other data sources, including those that may not be apparent in clinical research. The
ability of our method to identify potentially novel ASEs, validated by academic studies, thereby supporting hypothesis
H1, has been demonstrated by focusing on ASEs present in both social media and academic papers (Group 2 in Fig. 2)
but not reported by manufacturers. Our modeling approach was able to identify 53% of established ASEs reported
by manufacturers and ChatGPT (Fig. 3). The ability to identify established ASEs provides further confidence in our
modeling approach for exploring novel ASEs and supporting their novelty. Notably, established ASEs declared by
manufacturers but not identified on social media have Very Rare frequency, as observed in Groups 4 and 7 (Fig. 2), and
therefore are less likely to be reported on social media.
Furthermore, it is important to note ASEs reported very frequently on social media but not reported by manufacturers
(Groups 2 and 5 in Fig. 2). This discrepancy may stem from individuals using GLP-1 RA for weight loss, diverging
from the drug’s original indication of treating diabetes. Academic studies and manufacturers reporting the frequency of
ASEs often rely on clinical trials, while social media offers much more data. Therefore, comparing the frequency of
ASE mentions on social media to those reported in clinical trials was of great interest in the present study. In Fig. 4,
it is evident that the drug semaglutide (Ozempic) has the highest number of reported ASEs, followed by dulaglutide
and liraglutide, respectively. However, as Ozempic is also the most-prescribed drug among those analyzed in this
study, it is expected to have a higher frequency of reported ASEs. Our drug-ASE matrix analysis (Fig. 4) highlights
numerous prevalent ASEs based exclusively on social media reports. Additionally, comparing mentions of ASEs on
social media in intervals of 14 days (Fig. 5) to data from Google Trends (Fig. 6), we found that the ASEs mentioned
most frequently over time are nausea, pain, vomiting, and constipation. To address RQ1, we identified ASEs solely
based on raw social media discussions and constructed an ASE-ASE network (Fig. 7) G. In G, nodes represent ASEs,
edges signify ASE co-occurrences in the same post, and the weight of an ASE-ASE edge represents the number of
times this ASE co-occurrence pair was co-mentioned in the same post.
Node clustering analysis of the ASE-ASE network revealed four clusters of ASEs, allowing a better understanding of
their relationships: Cluster 1 – gastrointestinal distress; Cluster 2 – emotional and mental strain syndromes; Cluster 3 –
somatic discomfort; and Cluster 4 – neurological disorders. The presence of co-occurring ASEs is apparent (Fig 7),
particularly with respect to Cluster 1 (light blue nodes), with strong and specific associations (thick network links/edges)
among the common ASEs vomiting, nausea, migraines, fatigue, constipation, headache, and heartburn. This network
analysis suggests that pairs of ASEs in Cluster 1 are frequently correlated with each other, and future work should
examine in more detail the co-occurrence of these ASEs and compare these associations as reported by social media
posts against manufacturers’ reports and published literature. Revealing groups of ASEs that commonly co-occur
can highlight potential individual differences among GLP-1 RA users in terms of adverse effects experienced and
provide insights into the interrelationships among different ASEs, potential mechanisms underlying adverse effects, and
opportunities for personalized healthcare approaches that could utilize the complex, and sometimes rare, ASE-related
relationships revealed by our analytical strategy.
Our analytical approach can potentially aid in the timely implementation of regulatory interventions, adjustments in
treatment guidelines, and enhancement of patient safety measures. Moreover, monitoring fluctuations in the frequency
and patterns of reported ASEs on social media need not be limited to GLP-1 RA. The methods we use could enable
detection of emerging issues or safety concerns related to any drug. Our comprehensive data analytics approach applied
to large-scale social media data has substantial implications for drug safety assessment and for public health. The
integration of diverse data sources allows for more holistic discovery of adverse effects than standard pharmacovigilance
strategies provide. Here, the identified clusters contribute to a nuanced understanding of the therapeutic landscape
of GLP-1 RA. Specifically, two important contributions of our study are that only 53% of ASEs reported by drug
12

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
manufacturers have been mentioned on social media, and moreover, 21 ASEs found on social media have not been
reported by manufacturers. These findings call for additional studies. Future work could further examine the association
of drug popularity and awareness in popular culture with the sentiments expressed about the drug on social media.
Additional research could use data from private discussions on social media to compare the sentiments expressed there
with those voiced in public fora. Our data-analytic knowledge discovery approach can be used for any drug to bring to
light currently unidentified or under-reported side effects. Improving our understanding of the adverse effects of drugs
in this way can serve to refine prescription recommendations and accordingly reduce morbidity, thereby increasing
positive outcomes for manufacturer, physician and patient alike. Our approach paves the way for a new era of real-time
pharmacovigilance, leveraging social media data to improve drug safety and public health outcomes.
References
[1] World Health Organization. Obesity and overweight. 2021. Accessed October 5, 2023.
[2] Centers for Disease Control and Prevention. Type 2 diabetes. 2023. Accessed October 5, 2023.
[3] Jonathan Pearson-Stuttard, Sara Holloway, Rosie Polya, Rebecca Sloan, Linxuan Zhang, Edward W Gregg, Katy
Harrison, Jamie Elvidge, Pall Jonsson, and Thomas Porter. Variations in comorbidity burden in people with type 2
diabetes over disease duration: A population-based analysis of real world evidence. EClinicalMedicine, 52, 2022.
[4] Pradeep Khand and Bo Feng. The association of obesity with type 2 diabetes: A review. International Journal of
Science Inventions Today, 9:61–74, 2020.
[5] Adeyemi Okunogbe, Rachel Nugent, Garrison Spencer, Jaynaide Powis, Johanna Ralston, and John Wilding.
Economic impacts of overweight and obesity: Current and future estimates for 161 countries. BMJ Global Health,
7(9):e009773, 2022.
[6] Peyton W Moore, Kevin Malone, Delena VanValkenburg, Lauren L Rando, Brooke C Williams, Hannah G
Matejowsky, Shahab Ahmadzadeh, Sahar Shekoohi, Elyse M Cornett, and Alan D Kaye. GLP-1 agonists for
weight loss: Pharmacology and clinical implications. Advances in Therapy, 40(3):723–742, 2023.
[7] Jennifer M Trujillo, Wesley Nuffer, and Brooke A Smith. GLP-1 receptor agonists: An updated review of
head-to-head clinical studies. Therapeutic Advances in Endocrinology and Metabolism , 12:2042018821997320,
2021.
[8] J. Pritchett. 2022 prescription trends. May 2023. Accessed October 5, 2023.
[9] Patricia J Rodriguez, Samuel Gratzl, Brianna M Goodwin Cartwright, Rajdeep Brar, Ty J Gluckman, and Nicholas
Stucky. First-time prescribing of GLP-1 receptor agonists from 2018-2023: A descriptive analysis. medRxiv,
pages 2023–08, 2023.
[10] Sabrina H Han, Rachel Safeek, Kyle Ockerman, Nicky Trieu, Patricia Mars, Audrey Klenke, Heather Furnas, and
Sarah Sorice-Virk. Public interest in the off-label use of glucagon-like peptide 1 agonists (Ozempic) for cosmetic
weight loss: A Google Trends analysis. Aesthetic Surgery Journal, pages 211–215, 2023.
[11] Ant Cabral Lopes. Gastrointestinal disorders potentially associated with semaglutide: An analysis from the
Eudravigilance Database. Expert Opinion on Drug Safety , pages 1–7, 2023.
[12] Ziqi Zhang, Qiling Zhang, Ying Tan, Yu Chen, Xiqiao Zhou, Su Liu, and Jiangyi Yu. GLP-1RAs caused
gastrointestinal adverse reactions of drug withdrawal: A system review and network meta-analysis. Frontiers in
Endocrinology, 14, 2023.
[13] Novo Nordisk. Ozempic ® (semaglutide) approved in the US. 2017. Accessed October 5, 2023.
[14] Jesse A Berlin, Susan C Glasser, and Susan S Ellenberg. Adverse event detection in drug development: Recom-
mendations and obligations beyond phase 3. American Journal of Public Health , 98(8):1366–1371, 2008.
[15] James E Ridings. The thalidomide disaster, lessons from the past. Teratogenicity Testing: Methods and Protocols,
pages 575–586, 2013.
[16] Skorn Ponrartana, Michael M Moore, Sherwin S Chan, Teresa Victoria, Jonathan R Dillman, and Govind B
Chavhan. Safety issues related to intravenous contrast agent use in magnetic resonance imaging. Pediatric
Radiology, 51:736–747, 2021.
[17] Afaf A El-Malah, Magdy M Gineinah, Pran Kishore Deb, Ahdab N Khayyat, Monika Bansal, Katharigatta N
Venugopala, and Anfal S Aljahdali. Selective COX-2 inhibitors: Road from success to controversy and the quest
for repurposing. Pharmaceuticals, 15(7):827, 2022.
[18] Eduardo Ortiz. Market withdrawal of Vioxx: Is it time to rethink the use of COX-2 inhibitors? Journal of
Managed Care Pharmacy, 10(6):551–554, 2004.
13

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
[19] U.S. Food and Drug Administration. FDA Adverse Event Reporting System (FAERS) Public Dashboard. 2023.
Accessed October 5, 2023.
[20] Michael Kuhn, Ivica Letunic, Lars Juhl Jensen, and Peer Bork. The SIDER database of drugs and side effects.
Nucleic Acids Research, 44(D1):D1075–D1079, 2016.
[21] Jing Ding, Daniel Berleant, Dan Nettleton, and Eve Wurtele. Mining MEDLINE: Abstracts, sentences, or phrases?
In Biocomputing 2002, pages 326–337. World Scientific, 2001.
[22] Elsevier. Embase Database. 2023. Accessed October 6, 2023.
[23] Sheena Derry, Yoon Kong Loke, and Jeffrey K Aronson. Incomplete evidence: The inadequacy of databases in
tracing published adverse drug reactions in clinical trials. BMC Medical Research Methodology, 1:1–6, 2001.
[24] Timothy Nugent, Vassilis Plachouras, and Jochen L Leidner. Computational drug repositioning based on side-
effects mined from social media. PeerJ Computer Science, 2:e46, 2016.
[25] Perihan Elif Ekmekci. An increasing problem in publication ethics: Publication bias and editors’ role in avoiding
it. Medicine, Health Care and Philosophy , 20:171–178, 2017.
[26] Ana Mlinari´c, Martina Horvat, and Vesna Šupak Smolˇci´c. Dealing with the positive publication bias: Why you
should really publish your negative results. Biochemia Medica, 27(3):447–452, 2017.
[27] Kay Dickersin and Iain Chalmers. Recognizing, investigating and dealing with incomplete and biased reporting of
clinical research: From Francis Bacon to the WHO. Journal of the Royal Society of Medicine , 104(12):532–538,
2011.
[28] Juliet M Foster, Thys van der Molen, Manfred Caeser, and Philip Hannaford. The use of questionnaires for measur-
ing patient-reported side effects of drugs: Its importance and methodological challenges. Pharmacoepidemiology
and Drug Safety, 17(3):278–296, 2008.
[29] Ping Zhang, Fei Wang, Jianying Hu, and Robert Sorrentino. Exploring the relationship between drug side-effects
and therapeutic indications. In AMIA annual symposium proceedings, volume 2013, page 1568. American Medical
Informatics Association, 2013.
[30] Jae-Young Lee, Yae-Seul Lee, Dong Hyun Kim, Han Sol Lee, Bo Ram Yang, and Myeong Gyu Kim. The use of
social media in detecting drug safety–related new black box warnings, labeling changes, or withdrawals: Scoping
review. JMIR Public Health and Surveillance , 7(6):e30137, 2021.
[31] Hector Godinez, Qing Xu, Tiana J McMann, Jiawei Li, and Timothy Ken Mackey. Analysis of online user
discussions on Reddit associated with the transition of use between HIV PrEP therapy. Frontiers in Public Health,
11, 2023.
[32] Penny S Loosier, Kaytlin Renfro, Monique Carry, Samantha P Williams, Matthew Hogben, and Sevgi Aral. Reddit
on prep: Posts about pre-exposure prophylaxis for HIV from Reddit users, 2014–2019. AIDS and Behavior, pages
1–11, 2021.
[33] Kristina Jenei, Michael Burgess, Stuart Peacock, and Adam JN Raymakers. Experiences and perspectives of
individuals accessing CAR-T cell therapy: A qualitative analysis of online Reddit discussions. Journal of Cancer
Policy, 30:100303, 2021.
[34] Ling Zhang, Magie Hall, and Dhundy Bastola. Utilizing Twitter data for analysis of chemotherapy. International
Journal of Medical Informatics, 120:92–100, 2018.
[35] Rachel Lynn Graves, Jeanmarie Perrone, Mohammed Ali Al-Garadi, Yuan-Chi Yang, Jennifer S Love, Karen
O’Connor, Graciela Gonzalez-Hernandez, and Abeed Sarker. Thematic analysis of Reddit content about
buprenorphine-naloxone using manual annotation and natural language processing techniques. Journal of
Addiction Medicine, 2022.
[36] Dennis Hsu, Melody Moh, and Teng-Sheng Moh. Mining frequency of drug side effects over a large Twitter
dataset using Apache Spark. In IEEE/ACM, editor, Proceedings of the 2017 IEEE/ACM International Conference
on Advances in Social Networks Analysis and Mining , pages 915–924, 2017.
[37] Keyuan Jiang and Yujing Zheng. Mining twitter data for potential drug effects. In Advanced Data Mining and
Applications: 9th International Conference, ADMA 2013, Hangzhou, China, December 14-16, 2013, Proceedings,
Part I 9, pages 434–443. Springer, 2013.
[38] Katie Elson Anderson. Ask me anything: What is reddit? Library Hi Tech News, 32(5):8–11, 2015.
[39] Mufan Luo and Jeffrey T Hancock. Self-disclosure and social media: Motivations, mechanisms and psychological
well-being. Current Opinion in Psychology, 31:110–115, 2020.
14

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
[40] Ann E Schlosser. Self-disclosure versus self-presentation on social media. Current Opinion in Psychology, 31:1–6,
2020.
[41] John Suler. The online disinhibition effect. Cyberpsychology and Behavior, 7(3):321–326, 2004.
[42] Hyun-Myung Back, Seo-A Choi, and Myeong Gyu Kim. Adverse events of GLP-1 receptor agonists for weight
loss: Twitter and a national pharmacovigilance database. Drug Targets and Therapeutics, 2(1):41–48, 2023.
[43] Keyuan Jiang, Liyuan Huang, Tingyu Chen, Gelareh Karbaschi, Dingkai Zhang, and Gordon R Bernard. Mining
potentially unreported effects from Twitter posts through relational similarity: A case for opioids. In 2020 IEEE
International Conference on Bioinformatics and Biomedicine (BIBM) , pages 2603–2609. IEEE, 2020.
[44] Jiang Bian, Umit Topaloglu, and Fan Yu. Towards large-scale twitter mining for drug-related adverse events. In
Proceedings of the 2012 international workshop on Smart health and wellbeing , pages 25–32, 2012.
[45] Michael P Bremmer and Christian S Hendershot. Social media as pharmacovigilance: The potential for patient
reports to inform clinical research on glucagon-like peptide 1 (GLP-1) receptor agonists for substance use disorders.
Journal of Studies on Alcohol and Drugs , pages 19–23, 2023.
[46] Miguel Angel Alvarez-Mon, Maria Llavero-Valero, Angel Asunsolo del Barco, and Zaragoz. Areas of interest and
attitudes toward antiobesity drugs: Thematic and quantitative analysis using Twitter. Journal of Medical Internet
Research, 23(10):e24336, 2021.
[47] Donald Adjeroh, Richard Beal, Ahmed Abbasi, Wanhong Zheng, Marie Abate, and Arun Ross. Signal fusion for
social media analysis of adverse drug events. IEEE Intelligent Systems, 29(2):74–80, 2014.
[48] Yang Gao, Wenjing Duan, and Huaxia Rui. Does social media accelerate product recalls? Evidence from the
pharmaceutical industry. Information Systems Research, 33(3):954–977, 2022.
[49] Athanasios Tselebis and Ioannis Ilias. Further research on internet searches for on-and off-label use of weight-loss
medications. Aesthetic Surgery Journal, 43(11):NP977–NP978, 2023.
[50] Sabrina K Keating and Cervant Wild. Semaglutide and social media: Implications for young women with
polycystic ovarian syndrome. The Lancet Child and Adolescent Health , 7(5):301–303, 2023.
[51] Corey H Basch, Sandhya Narayanan, Hao Tang, Joseph Fera, and Charles E Basch. Descriptive analysis of TikTok
videos posted under the hashtag# Ozempic. Journal of Medicine, Surgery, and Public Health , 1:100013, 2023.
[52] Jayna Lennon. Can you stomach it? A content analysis of TikTok videos and comments about weight loss with
Ozempic. 2023.
[53] Davide Arillotta, Giuseppe Floresta, Amira Guirguis, John Martin Corkery, Valeria Catalani, Giovanni Martinotti,
Stefano L Sensi, and Fabrizio Schifano. GLP-1 receptor agonists and related mental health issues and insights
from a range of social media platforms using a mixed-methods approach. Brain Sciences, 13(11):1503, 2023.
[54] Amogh Kamat Tarcar, Aashis Tiwari, Vineet Naique Dhaimodker, Penjo Rebelo, Rahul Desai, and Dattaraj Rao.
Healthcare NER models using language model pretraining. arXiv preprint arXiv:1910.11241, 2019.
[55] Jing Li, Aixin Sun, Jianglei Han, and Chenliang Li. A survey on deep learning for named entity recognition. IEEE
Transactions on Knowledge and Data Engineering , 34(1):50–70, 2020.
[56] James Temperton. GPT-3: How does the new language model work? BBC Science F ocus, 2023. Accessed:
February 5, 2024.
[57] Jesutofunmi A Omiye, Haiwen Gui, Shawheen J Rezaei, James Zou, and Roxana Daneshjou. Large language
models in medicine: The potentials and pitfalls: A narrative review. Annals of Internal Medicine , 2024.
[58] Peter Lee, Sebastien Bubeck, and Joseph Petro. Benefits, limits, and risks of GPT-4 as an AI chatbot for medicine.
New England Journal of Medicine , 388(13):1233–1239, 2023.
[59] Andrew Joseph. How ChatGPT 4 is transforming health care and medical education. Stat News, 2023. Accessed:
February 5, 2024.
[60] Mike Miliard. Epic, Microsoft partner to use generative AI for better EHRs. Healthcare IT News, 2023. Accessed:
February 5, 2024.
[61] Qijie Chen, Haotong Sun, Haoyang Liu, Yinghui Jiang, Ting Ran, Xurui Jin, Xianglu Xiao, Zhimin Lin, Hongming
Chen, and Zhangmin Niu. An extensive benchmark study on biomedical text generation and mining with ChatGPT.
Bioinformatics, 39(9):btad557, 2023.
[62] Thomas Lancaster. Artificial intelligence, text generation tools and ChatGPT–Does digital watermarking offer a
solution? International Journal for Educational Integrity , 19(1):10, 2023.
15

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
[63] Alon Bartal, Kathleen M Jagodnik, Sabrina J Chan, Mrithula S Babu, and Sharon Dekel. Identifying women
with postdelivery posttraumatic stress disorder using natural language processing of personal childbirth narratives.
American Journal of Obstetrics and Gynecology MFM , 5(3):100834, 2023.
[64] Bishal Lamichhane. Evaluation of ChatGPT for NLP-based mental health applications. arXiv preprint
arXiv:2303.15727, 2023.
[65] Peter Lee, Carey Goldberg, and Isaac Kohane. The AI Revolution in Medicine: GPT-4 and Beyond . Pearson, 2023.
[66] Suebsarn Ruksakulpiwat, Ayanesh Kumar, and Anuoluwapo Ajibade. Using ChatGPT in medical research:
Current status and future directions. Journal of Multidisciplinary Healthcare, pages 1513–1520, 2023.
[67] Ayesha Juhi, Neha Pipil, Soumya Santra, Shaikat Mondal, Joshil Kumar Behera, Himel Mondal, Neha Pipil Sr,
Soumya Santra Sr, and Joshil K Behera IV . The capability of ChatGPT in predicting and explaining common
drug-drug interactions. Cureus, 15(3), 2023.
[68] Christopher McMaster, Julia Chan, David FL Liew, Elizabeth Su, Albert G Frauman, Wendy W Chapman, and
Douglas EV Pires. Developing a deep learning natural language processing algorithm for automated reporting of
adverse drug reactions. Journal of Biomedical Informatics, 137:104265, 2023.
[69] Dimitar Trajanov, Vangel Trajkovski, Makedonka Dimitrieva, Jovana Dobreva, Milos Jovanovik, and Matej and
Klemen. Review of natural language processing in pharmacology. Pharmacological Reviews, 75(4):714–738,
2023.
[70] Jonathan H Watanabe, Terry McInnis, and Jan D Hirsch. Cost of prescription drug–related morbidity and mortality.
Annals of Pharmacotherapy, 52(9):829–837, 2018.
[71] Igho J Onakpoya, Carl J Heneghan, and Jeffrey K Aronson. Worldwide withdrawal of medicinal products because
of adverse drug reactions: A systematic review and analysis. Critical Reviews in Toxicology, 46(6):477–489, 2016.
[72] Linda Martin, Melissa Hutchens, Conrad Hawkins, and Alaina Radnov. How much do clinical trials cost? Nature
Reviews Drug Discovery, 16(6):381–382, 2017.
[73] LN Ozurumba-Dwight, JO Soyinka, CS Ogbonna, OO Enwere, KO Iyevhobu, OC Iloka, MC Korie, and LN Kevin-
Asogwa. Multi-purposely dynamic use of social media for health purposes: Scooping review of systematic reviews.
International Journal of Advanced Research in Biological Sciences , 9(6):92–108, 2022.
[74] Junhan Chen and Yuan Wang. Social media use for health purposes: Systematic review. Journal of Medical
Internet Research, 23(5):e17917, 2021.
[75] Bryce Boe. PRAW: The Python Reddit API Wrapper. 2023. Accessed January 25, 2024.
[76] Eric Sayers. E-Utilities Quick Start. 2023. Accessed January 25, 2024.
[77] Brad Chapman and Jeffrey Chang. Biopython: Python tools for computational biology. ACM Sigbio Newsletter,
20(2):15–19, 2000.
[78] Mark Neumann, Daniel King, Iz Beltagy, and Waleed Ammar. ScispaCy: Fast and robust models for biomedical
natural language processing. arXiv preprint arXiv:1902.07669, 2019.
[79] Anjali Ganesh Jivani et al. A comparative study of stemming algorithms. International Journal of Computer
Applications in Technology, 2(6):1930–1938, 2011.
[80] Nicolas Woloszko. Tracking activity in real time with Google Trends. OECD iLibrary, 2020.
[81] Diego Galeano, Shantao Li, Mark Gerstein, and Alberto Paccanaro. Predicting the frequencies of drug side effects.
Nature Communications, 11(1):4575, 2020.
[82] Marinka Zitnik, Monica Agrawal, and Jure Leskovec. Modeling polypharmacy side effects with graph convolu-
tional networks. Bioinformatics, 34(13):i457–i466, 2018.
[83] Gabor Csardi and Tamas Nepusz. The igraph software package for complex network research. InterJournal,
Complex Systems, 1695(5):1–9, 2006.
[84] Pascal Held, Benjamin Krause, and Rudolf Kruse. Dynamic clustering in social networks using louvain and
infomap method. In 2016 Third European Network Intelligence Conference (ENIC) , pages 61–68. IEEE, 2016.
[85] Rohana N Haththotuwa, Chandrika N Wijeyaratne, and Upul Senarath. Worldwide Epidemic of Obesity. In
Obesity and obstetrics, pages 3–8. Elsevier, 2020.
16

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Appendix A A list of GLP-1 receptor agonist adverse side effects (ASEs) identified in the
datasets collected for this study.
Table 4: A list of GLP-1 receptor agonist adverse side effects (ASEs) identified in the five datasets collected for this
study.
ASE Frequency Code Legend
Inflammation 1376 1 All
Hypoglycemia 1006 1 All
Depression 981 1 All
Diarrhea 951 1 All
Nausea 820 1 All
Increased Heart Rate 736 1 All
Microalbuminuria 678 1 All
Chills 446 1 All
V omiting 404 1 All
Fatigue 390 1 All
Constipation 333 1 All
Anxiety 320 1 All
Headaches 245 1 All
Cramps 231 1 All
Thyroid Issues 185 1 All
Gastritis 168 1 All
Rash 118 1 All
Dizziness 82 1 All
Hypertrophy 82 1 All
Hypersensitivity 80 1 All
Dyspepsia 79 1 All
Swallowing Difficulty 74 1 All
Thirst 68 1 All
Insomnia 65 1 All
Stress 61 1 All
Thrombosis 44 1 All
Otitis 35 1 All
Jaundice 19 1 All
Cholestasis 10 1 All
Cholelithiasis 8 1 All
Hidradenitis 6 1 All
Thromboembolism 6 1 All
Chest Tightness 5 1 All
Hyperglycemia 5 1 All
Polyuria 5 1 All
Infarction 729 2 PubMed & Social
Ulcerative Wounds 681 2 PubMed & Social
Atherosclerosis 567 2 PubMed & Social
Neuropathy 334 2 PubMed & Social
Dehydration 303 2 PubMed & Social
Hypothyroidism 122 2 PubMed & Social
Hepatic Issues 97 2 PubMed & Social
Trauma 90 2 PubMed & Social
Arthritis 81 2 PubMed & Social
Arrhythmias 77 2 PubMed & Social
Anorexia 69 2 PubMed & Social
Dementia 68 2 PubMed & Social
Ketosis 66 2 PubMed & Social
Allodynia 56 2 PubMed & Social
Ketoacidosis 54 2 PubMed & Social
Osteoarthritis 54 2 PubMed & Social
17

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Table 4: A list of GLP-1 receptor agonist adverse side effects (ASEs) identified in the five datasets collected for this
study.
ASE Frequency Code Legend
Encephalopathy 46 2 PubMed & Social
Mania 42 2 PubMed & Social
Hypotonia 41 2 PubMed & Social
Palpitations 41 2 PubMed & Social
Cholangitis 40 2 PubMed & Social
Urticaria 40 2 PubMed & Social
Cardiomyopathy 38 2 PubMed & Social
Acidosis 36 2 PubMed & Social
Delusion 31 2 PubMed & Social
Erythema 30 2 PubMed & Social
Tachycardia 30 2 PubMed & Social
Compulsive Behavior 25 2 PubMed & Social
Gangrene 23 2 PubMed & Social
Pneumonia 21 2 PubMed & Social
Osteomyelitis 19 2 PubMed & Social
Amnesia 16 2 PubMed & Social
Lethargy 13 2 PubMed & Social
Malnutrition 11 2 PubMed & Social
Fractures 8 2 PubMed & Social
Retching 8 2 PubMed & Social
Bradycardia 7 2 PubMed & Social
Fasciitis 6 2 PubMed & Social
Glycosuria 6 2 PubMed & Social
Hypercholesterolemia 6 2 PubMed & Social
Neurotoxicity 6 2 PubMed & Social
Bezoar 230 3 PubMed
Atheroma 91 3 PubMed
Hypoxia 68 3 PubMed
Nephrotoxicity 67 3 PubMed
Pruritus (Itching) 67 3 PubMed
Stiffness 42 3 PubMed
Hyperphagia 32 3 PubMed
Cardiotoxicity 26 3 PubMed
Ischemia 24 3 PubMed
Polyneuropathies 23 3 PubMed
Paresthesia 20 3 PubMed
Hyperplasia 18 3 PubMed
Arteriosclerosis 8 3 PubMed
Demyelination 8 3 PubMed
Dyskinesia 8 3 PubMed
Hyperemia 8 3 PubMed
Increase in Amylase NA 4 Manufacturers & GPT
Serious Allergic Reaction NA 4 Manufacturers & GPT
Thyroid C-Cell Tumors NA 4 Manufacturers & GPT
Injection Site Nodule 14.5 4 Manufacturers & GPT
Sinus Tachycardia 11.5 4 Manufacturers & GPT
Hair Loss 6 4 Manufacturers & GPT
First-Degree Atrioventricular (A V) Block 4.6 4 Manufacturers & GPT
Elevated Serum Lipase 2.1 4 Manufacturers & GPT
Dysgeusia 1.7 4 Manufacturers & GPT
High Calcitonin 1.2 4 Manufacturers & GPT
Breast Cancer 0.7 4 Manufacturers & GPT
Colorectal Neoplasms 0.6 4 Manufacturers & GPT
Papillary Thyroid Cancer 0.2 4 Manufacturers & GPT
Elevated Serum Amylase 0.1 4 Manufacturers & GPT
18

Utilizing AI and Social Media Analytics to Discover Adverse Side Effects of GLP-1 Receptor Agonists
Table 4: A list of GLP-1 receptor agonist adverse side effects (ASEs) identified in the five datasets collected for this
study.
ASE Frequency Code Legend
Irritability 58 5 Social only
Burns 46 5 Social only
Numbness 45 5 Social only
Hypogonadism 31 5 Social only
Cough 26 5 Social only
Paralysis 24 5 Social only
Anger 22 5 Social only
Hoarseness 22 5 Social only
Bulimia 19 5 Social only
Suicidal 18 5 Social only
Anhedonia 12 5 Social only
Frustration 12 5 Social only
Onycholysis 12 5 Social only
Endometriosis 11 5 Social only
Ketonemia 6 5 Social only
Apathy 4 5 Social only
Aura 4 5 Social only
Hirsutism 4 5 Social only
Infertility 4 5 Social only
Narcolepsy 4 5 Social only
Snoring 4 5 Social only
Eructation 35 6 Manufacturers & Social
Bloating 30 6 Manufacturers & Social
Back Pain 12 6 Manufacturers & Social
Hepatotoxicity 6 6 Manufacturers & Social
Syncope 4.6 6 Manufacturers & Social
Appendicitis 3 6 Manufacturers & Social
Blurred Vision 15 7 Pubmed & manufacturers
19
