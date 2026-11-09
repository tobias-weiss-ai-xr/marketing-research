---
title: Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models
  with an Application on Semaglutide
url: https://arxiv.org/abs/2504.04346
category: social-media
subcategory: empirical
date: 2025-04
venue: ''
authors:
- Zhijie Duan
- Kai Wei
- Zhaoqian Xue
- Jiayan Zhou
- Shu Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2504.04346
pages: 16
chars: 51097
fetched_at: '2026-11-08T13:01:31+00:00'
kb_version: 1
---

# Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an Application on Semaglutide

Crowdsourcing-Based Knowledge Graph Construction for
Drug Side Effects Using Large Language Models with an
Application on Semaglutide
ZHIJIE DUAN∗ and KAI WEI∗, University of Pennsylvania University of Michigan, USA
ZHAOQIAN XUE, Georgetown University, USA
JIAYAN ZHOU,Stanford University School of Medicine, USA
SHU YANG, University of Pennsylvania, USA
SIYUAN MA, Vanderbilt University, USA
JIN JIN†, University of Pennsylvania, USA
LINGYAO LI†, University of South Florida, USA
Abtract: Social media is a rich source of real-world data that captures valuable patient experience information
for pharmacovigilance. However, mining data from unstructured and noisy social media content remains a
challenging task. We present a systematic framework that leverages large language models (LLMs) to extract
medication side effects from social media and organize them into a knowledge graph (KG). We apply this
framework to semaglutide for weight loss using data from Reddit. Using the constructed knowledge graph, we
perform comprehensive analyses to investigate reported side effects across different semaglutide brands over
time. These findings are further validated through comparison with adverse events reported in the FAERS
database, providing important patient-centered insights into semaglutide’s side effects that complement its
safety profile and current knowledge base of semaglutide for both healthcare professionals and patients.
Our work demonstrates the feasibility of using LLMs to transform social media data into structured KGs for
pharmacovigilance.
Keywords: Pharmacovigilance, Large Language Models, Knowledge Graph, Social Media Mining, FAERS
Database
1 Introduction
When a medicine is approved, it typically undergoes continued monitoring for safety, including the
detection of adverse drug reactions and long-term effects, a process known as pharmacovigilance
[1]. While randomized controlled trials (RCTs) are considered the gold standard for evaluating drug
safety and efficacy, they have limitations due to strict inclusion and exclusion criteria, which could
lead to the underrepresentation of certain patient populations commonly seen in clinical practice
[2]. In contrast, analyzing real-world data (RWD) from a broader and more diverse population over
an extended period after a drug enters the market can help bridge the gap between trial results and
patient outcomes in real-world settings to complement the evidence from RCTs [1–5].
Traditional post-marketing surveillance relies on Phase IV trials and real-world evidence from
electronic health records (EHRs), claims data, or the FDA Adverse Event Reporting System (FAERS)
[6, 7]. In recent years, social media has gathered increasing attention as a potential source of RWD
[8–11]. Unlike the FAERS database, which releases adverse events (AEs) data quarterly [12], social
∗Both authors contributed equally to this research.
†Corresponding author.
Authors’ Contact Information: Zhijie Duan, zhijie.duan@pennmedicine.upenn.edu; Kai Wei, weikai@umich.edu, University
of Pennsylvania, Philadelphia, PA and University of Michigan, Ann Arbor, MI, USA; Zhaoqian Xue, Georgetown University,
Washington DC, USA, zx136@georgetown.edu; Jiayan Zhou, Stanford University School of Medicine, Stanford, CA, USA,
jyzhou@stanford.edu; Shu Yang, University of Pennsylvania, Philadelphia, PA, USA, shu.yang@pennmedicine.upenn.
edu; Siyuan Ma, Vanderbilt University, Nashville, TN, USA, siyuan.ma@vumc.org; Jin Jin, University of Pennsylvania,
Philadelphia, PA, USA, jin.jin@pennmedicine.upenn.edu; Lingyao Li, University of South Florida, Tampa, FL, USA, lingyaol@
usf.edu.
, Vol. , No. , Article . Publication date: .
arXiv:2504.04346v2  [cs.AI]  8 Apr 2025

Duan and Wei, et al.
media is characterized by real-time and dynamic user discussions [13], which could greatly facilitate
the early detection of emerging safety signals. In addition, social media data is publicly accessi-
ble, which contrasts with EHRs that are restricted due to patient privacy and security concerns.
Another important advantage of social media data is its patient-centered nature. Crowdsourcing
this important source of personal experiences can bring valuable patient perspectives into drug
post-marketing monitoring, which is essential to achieving better patient-centered care [8, 10, 11].
However, social media data are inherently unstructured, scattered, and noisy, which poses
challenges for information extraction and analysis. Previous studies have demonstrated the use of
various tools—including natural language processing (NLP), thematic coding, and knowledge graphs
(KGs)—to analyze user discussions on online platforms such as X, Reddit, and other forums [14–17].
The growing body of literature highlights the potential of these tools to identify off-label use and
early signals of adverse effects of medications that are not readily captured in clinical settings
[18, 19]. The mining of social media data can be further enhanced by emerging large language
models (LLMs), which are well-suited for information extraction from large-scale, complex text
content [20, 21].
While studies have utilized social media data to analyze side effects and user experiences, few have
focused on developing a comprehensive pipeline for constructing KGs from user-generated content
to present structured information on real-world drug effects. Moreover, the feasibility of analyzing
large-scale social media content and the potential of LLMs to enhance knowledge graph construction
remain largely underexplored. We address these research gaps by developing a systematic pipeline
for social media-based knowledge graph construction for drug side effects utilizing LLMs. A
knowledge graph is composed of nodes and edges, with the basic unit of observation being a
triple linking two objects through a relationship [22]. It offers the unique advantage of presenting
complex drug-related information in a structured way. In particular, we investigate three research
questions:
• RQ1: How can social media data be transformed into a knowledge graph using LLMs to represent
relationships between the medication and reported side effects?
• RQ2: What are the important messages on the major side effects identified through qualitative
and quantitative analyses of the constructed knowledge graph?
• RQ3: How do the side effects identified from social media compare with the AEs reported in
FAERS?
We select semaglutide as the target medication to demonstrate the utility of our pipeline. Semaglu-
tide, a glucagon-like peptide-1 (GLP-1) receptor agonist, was first approved by the FDA in December
2017 for the treatment of type 2 diabetes mellitus [23]. In 2021, a new formulation received FDA
approval for chronic obesity and overweight management, expanding its use to a broader popu-
lation [24]. According to the Centers for Disease Control and Prevention (CDC), approximately
40.3% of U.S. adults were affected by obesity between August 2021 and August 2023 [25]. Looking
ahead, it is estimated that the total number of adults with overweight and obesity would reach 213
million by 2050 [26]. This growing burdened population corresponds with the rising public interest
in semaglutide, as reflected by the surge of online search queries and increasing off-label use in
recent years [27]. Investigating semaglutide through social media presents a timely opportunity
for us to understand user perspectives and real-world side effects of medications beyond clinical
trial settings.
Our contribution is twofold. First, we demonstrate how LLMs can be used to efficiently extract
side effects information from unstructured social media data and construct an easy-to-use, publicly
accessible knowledge base for downstream analysis and public references. Second, we present
a scalable pipeline designed for LLM-assisted construction of KGs using social media data. We
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
apply the pipeline to semaglutide, showcasing the value of crowdsourced social media data in
complementing traditional pharmacovigilance and facilitating the generation of real-world evidence.
Our case study highlights the applicability, validity, and efficiency of our pipeline for the general
task of developing social media-based side effect KGs for various health conditions.
2 Materials and Methods
The conceptual framework of the proposed pipeline is illustrated in Figure 1 and consists of four
stages. First, posts related to semaglutide and its brand names are retrieved from the Reddit platform,
followed by data-cleaning steps such as the removal of emojis and non-English content. Second, a
LLM, specifically GPT-4o-mini, is used to extract side effect information from the collected posts.
Through prompt design and few-shot in-context learning, the model identifies side effects, their
associated medications, and additional attributes such as severity, duration, and dosage when
mentioned. Third, the extracted information is visualized using D3.js, where nodes represent
drugs and side effects and edges denote the relationships between them. Finally, the Reddit-derived
knowledge graph is compared with the FAERS database to highlight both overlaps and discrepancies,
and a correlation analysis is performed to quantitatively assess the alignment between the two
data sources.
Fig. 1. The conceptualized framework of the pipeline applied to semaglutide.
2.1 Data preparation
We choose Reddit as our primary social media data source. Reddit is a popular platform where
users can share content, which can be voted up or down by other users. Discussions are organized
into user-created communities called subreddits, each focused on specific topics. A typical Reddit
discussion consists of three parts: a post, which serves as a conversation starter; comments, where
users engage with the post by leaving comments; and replies, where users can respond to comments,
forming a hierarchical, tree-like structure. To collect relevant data, we conduct a search on February
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
1, 2025, for Reddit posts containing the keyword “Semaglutide” and its three brands, namely
“Ozempic, ” “Rybelsus, ” and “Wegovy. ” We used the Python-based library PRAW (Python Reddit API
Wrapper) to download user-generated posts published between December 1, 2017, and January 31,
2025 [28, 29]. The start date was chosen to align with Ozempic’s FDA approval on December 5,
2017 [30].
We additionally collect data from FAERS, one of the largest pharmacovigilance databases in the
world, which collects adverse event (AE) reports from pharmaceutical manufacturers, healthcare
providers, patients, and other sources [31, 32]. FAERS uses preferred terms (PTs) from the Medical
Dictionary for Regulatory Activities (MedDRA) to describe AEs [ 33]. These PTs are organized
into 27 system organ classes (SOCs), and each PT may be associated with multiple SOCs [ 34].
We search the FAERS using four product names: “Semaglutide” (i.e., general semaglutide without
brands specified), “Ozempic, ” “Rybelsus, ” and “Wegovy, ” and separately download the data for each
product. This includes all AEs associated with these products reported in FAERS up to the fourth
quarter (Q4) of 2024.
After collection, the Reddit data undergoes several cleaning steps. First, we flatten the scraped
data so that each observation in the transformed dataset represents either a post (conversation
starter), a comment, or a reply. Each observation includes variables such as publication date, score
(upvotes minus downvotes), ID, author, parent ID (linking it to the higher-level conversation), and
text, among others. To further refine the dataset, we filter out observations with non-English text,
bot-generated responses, or content consisting solely of a URL.
2.2 Information extraction
In Stage 2 (Figure 1), we leverage LLM to perform information extraction, aiming to extract drug-
relation-side effect triples related to semaglutide from the given text. We restrict the medication
entity name to only “Wegovy, ” “Ozempic, ” and “Rybelsus, ” as well as “Semaglutide” when no specific
brand name is mentioned. For consistency, “Semaglutide” is later relabeled as “Unspecified Brands”
in the subsequent analysis. Additionally, we instruct GPT to extract the “severity, ” “duration, ”
and “dosage” of side effects if explicitly mentioned in the text and store them as properties of
the relations. We also instruct GPT to provide a concise explanation of each relation within the
properties. A prompt is a set of instructions provided to an LLM to influence its response generation
and customize the output for our specific needs [35, 36]. We employ a few-shot prompting technique
to enhance in-context learning (ICL) by including five examples in the prompt [36]. Among the
five examples, three are “null” examples, which demonstrate cases where no information should
be extracted—either because the text does not align with the guidelines (e.g., discussing other
drugs instead of semaglutide products) or because it lacks meaningful relations [ 37]. For each
observation, the extracted relations are saved into the variable “Relations” in the data. We select
GPT-4o mini because it is a relatively lightweight model that offers a great balance of performance
and cost efficiency [38]. For the rest of the paper, we use “GPT” to refer to the GPT-4o mini model
to maintain consistency and conciseness.
After extracting information, we remove observations with null values, as these posts, comments,
or replies contain no extracted information. Next, we remove duplicates by keeping unique (ID, text)
pairs, resulting in 4,242 rows. These rows contain 7,225 relations and 2,284 unique side-effect entities
(end nodes). To improve the consistency of information extraction, we consolidate highly similar
side effects into standardized terms. For example, “Headaches” and “Headache” are standardized
as “Headache, ” while variations like “Liver Damage, ” “Damaging Liver, ” and “Damage to Liver”
are standardized as “Liver Damage. ” This standardization is conducted in two steps. First, we use
SentenceTransformer’s all-MiniLM-L6-v2 model, a pre-trained model designed for efficient semantic
text similarity computation [ 39], to generate embeddings for each unique side effect. We then
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
construct a similarity matrix and filtered out entities with a similarity score below 0.9. This leaves
us with 605 unique side effects requiring further grouping. Second, we leverage GPT to support
clustering by iteratively grouping similar side effects. If GPT determines that a side effect matches
an existing key, the side effect is added to the group of that key; otherwise, it becomes a new key.
This two-step process results in a total of 96 side effects. Each group is manually reviewed and
adjusted if necessary, with final names standardized using the PTs from MedDRA as the reference.
Next, we evaluate GPT’s performance in extracting side effects and their associated severity. We
do not evaluate dosage or duration due to the high rate of missing data (only a few posts included
that information). We randomly select 213 observations (5% of the sample) for evaluation. Each
relation is independently evaluated by three authors who assign a score of 1 (correct) or 0 (incorrect)
based on the criteria of faithfulness, completeness, and relevance [ 40]. The final annotation is
determined through a majority-voting strategy [41]. The final accuracy of the extracted side effects
and their associated severity, as determined through manual annotation, is 79.34% and 86.85%,
respectively.
Table 1. Representative examples of side effect extraction using GPT-4o mini.
Original Post Extracted Relations Side Effects Severity Dosage
11 weeks in on my Ozempic. Have
had 2 doses at 1mg injected into
thigh which is almost painless. I
alternate thighs each week. At .25
I would have severe cramping in
stomach the day after injection. Eat-
ing carbs made it worse.
["start": "label":
"Medication", "properties":
"name": "Ozempic", "end":
"label": "SideEffect",
"properties": "name":
"Stomach Cramps",
"properties": "severity":
"severe", "duration": "1
day", "dosage": "0.25 mg",
"description": "The user
experienced severe cramping
in the stomach the day after
the 0.25 mg injection."]
Stomach
Cramps
Severe 0.25
mg
I’ve been fine. I have been on a low
dose though as that’s been enough.
I had very mild nausea on 1.2mg, I
think because I didn’t actually eat
enough. It worked too well. My ap-
petite is reduced enough on 0.6mg
so I’ve gone back down to that.
["start": "label":
"Medication", "properties":
"name": "Semaglutide",
"end": "label": "SideEffect",
"properties": "name":
"Nausea", "properties":
"severity": "mild",
"duration": null, "dosage":
"1.2 mg", "description":
"The user experienced mild
nausea from semaglutide at
the 1.2 mg dose."]
Nausea Mild 1.2 mg
I was on saxenda 3.0 for a year, then
went to .25 on ozempic, week two
went to .5, regretted it due to de-
pressed mood, did three more weeks
on .25, three weeks on .5, and am
on week 3 of 1.0. I didn’t really lose
anything until 1.0, but I wasn’t los-
ing on saxenda for the last several
months so it was no skin off my
back to titrate up.
["start": "label":
"Medication", "properties":
"name": "Ozempic", "end":
"label": "SideEffect",
"properties": "name":
"Depression", "properties":
"severity": "severe",
"duration": null, "dosage":
"0.5 mg", "description": "The
user experienced severe side
effects after increasing the
dosage of Ozempic to 0.5
mg."]
Depression Severe 0.5 mg
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
2.3 Knowledge graph construction
Using the cleaned data, we construct a systematic KG structure to represent the relationships
between semaglutide products and their reported side effects, as presented in Figure 1 (Stage 3).
The KG can be formally defined as:
KG =(𝑉,𝐸) (1)
where𝑉 ,𝐸 denote the set of vertices (nodes) and edges (relationships), respectively. In our
semaglutide side effect KG, each node belongs to one of two categories:
𝑉 =𝑀∪𝑆 (2)
where𝑀 ={𝑚1,𝑚 2,...,𝑚 𝑛} represents medication entities (Wegovy, Ozempic, Rybelsus, and
the generic term "Unspecified Brands"), and𝑆 ={𝑠1,𝑠 2,...,𝑠 𝑛} represents the side effects entities.
The relationships between medications and side effects are represented as directed edges, where:
𝑒 =(𝑚,𝑠,𝑃) (3)
Here,𝑚∈𝑀 is a medication entity,𝑠∈𝑆 is a side effect entity, and𝑃 ={𝑝1,𝑝 2,...,𝑝 𝑛} is a set
of properties that capture additional metadata, including:
𝑃 ={severity, duration, dosage, description} (4)
These properties are populated when available in the source content, allowing for rich contextual
information beyond simple links.
To deploy the constructed KG, we utilize D3.js, a JavaScript visualization library that enables
interactive data representation. We employ a force-directed graph layout algorithm that positions
nodes optimally by simulating physical forces, where nodes repel each other while connected nodes
are pulled together, resulting in a visually intuitive arrangement that minimizes edge crossings.
Our visualization assigns distinct visual encodings to medication and side effect nodes. The radius
of each side effect node is proportional to its frequency of mention in the dataset, with node sizes
calculated as:
radius(𝑠) = base_size+ log(frequency(𝑠)) (5)
Similarly, edge thickness is scaled according to the weight of the relationship, reflecting how
frequently a particular medication-side effect pair co-occurred in the Reddit corpus:
thickness(𝑒) = base_thickness· log(weight(𝑒)) (6)
2.4 Comparison between FDA adverse events and Reddit-extracted side effects
In Stage 4, we compare Reddit-derived side effects with FDA-reported AEs. By manually matching
the top 20 side effects extracted from Reddit with the top 20 adverse events reported in the FDA
FAERS database (Figure 4A), we calculate the frequency of each side effect/AE pair in either FDA
reports or Reddit posts. For FDA-reported AEs, the frequency for an AE𝑗 is defined as:
FreqFDA 𝑗 = #Adverse Event𝑗 #Total FAERS Reports (7)
where the number of total reports accounts for all patient reports on AEs related to Semaglutide.
Similarly, for the same side effect𝑗 as reported by Reddit, its frequency is calculated as:
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
FreqReddit 𝑗 = #Side Effect 𝑗 #Total Reddit Posts (8)
where the number of total Reddit posts, by design of our study, represents the number of posts
reporting any side effects of Semaglutide. Thus, while neither metric should be interpreted as the
incidence rate of AEs/side effects in the general population, they do represent similar statistics,
namely, the propensity for a particular AE or side effect for Semaglutide, among all such reports as
collected by the FDA or via Reddit crowdsourcing (Figure 4B).
We conduct a formal binomial regression analysis to test whether the difference between Reddit-
based and FDA-based frequencies is statistically significant. Specifically, for a specific side effect/AE
pair 𝑗, we ran the following regression:
#Side Effect𝑗, #Total Posts𝑗∼𝛽0+𝛽1𝑋 𝑗 (9)
where𝑋 𝑗 is the binary covariate indicating either FDA-reported adverse events (𝑋 𝑗 = 0) or Reddit
side effects (𝑋 𝑗 = 1). The above formulation thus exactly represents the frequency metrics as defined
above but allows for formal statistical tests for whether the difference between Reddit versus FDA
(𝛽1; log odds ratio for side effect propensity in Reddit compared to FDA) is statistically significant,
as reported in Figure 4C. P-values across comparisons for each adverse event are corrected with
the Bonferroni procedure.
Lastly, as the FAERS database reports adverse events as associated with specific Semaglutide
brands (Ozempic/Wegovy/Rybelsus), we further conduct the above analyses but are restricted to
each individual brand (Figure 4D).
3 Results
3.1 RQ1. Knowledge graph for semaglutide side effects
The knowledge graph constructed from GPT-extracted relations visualizes the complex interaction
network between semaglutide products and their associated side effects reported on Reddit (Figure
2). The graph represents 7,225 relations connecting four medication brand entities (Ozempic,
Wegovy, Rybelsus, and unspecified brands) with 1,775 unique side effect entities. To distinguish
entity types, we assign different colors to medication nodes and side effect nodes, with side effect
nodes sized proportionally to their mention frequency. Analysis of the graph reveals that nausea is
the most frequently reported side effect, which is visually represented by its significantly larger
node size than other side effects. The connection between unspecified brands and nausea appears
substantially thicker than connections to less frequently reported side effects, reflecting the weight
of this relationship in user discussions.
The interactive capabilities of our implementation enable a closer look and more detailed exami-
nation of specific elements on the graph. Figure 2B demonstrates this functionality, where selecting
“Nausea” as a single side effect automatically generates a focused knowledge graph displaying the
connections between all four medication brand entities and the nausea node. When hovering over a
side effect node such as “Nausea” (Figure 2B), a tooltip displays comprehensive statistics, including
740 total mentions with severity distributions ranging from “mild” (30 mentions) to “severe” (10
mentions) and various other descriptors. Duration data reveals equal distribution among common
reporting periods (e.g., “1 week, ” “2 weeks, ” and “1 day, ” each with 9 mentions), while dosage informa-
tion indicates variation across medication levels with “1 mg” being the most frequently mentioned
(16 instances). Edge tooltips provide detailed insights into specific medication-side effect relation-
ships (Figure 2B). The Ozempic-nausea relationship displays 483 co-occurrences, along with repre-
sentative examples that contextualize user experiences. For instance, the tooltip shows two patient
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
Fig. 2. Interactive knowledge graph visualization of semaglutide side effect information extracted from
Reddit data. A) The knowledge graph displaying relationships between four medication entities and their
associated side effects, with node sizes proportional to the frequency of Reddit mentions. B) Focused view of
the knowledge graph when selecting nausea as a single side effect, showing detailed statistics on severity,
duration, and dosage, along with representative user experiences across different medication brands.
examples with varying experiences: one user reported nausea for the first couple of weeks at a 0.5
unit dosage, while another experienced nausea for 24 hours at a higher 1.0 unit dose. Our interactive
KG is publicly accessible at https://zx136.georgetown.domains/Semaglutide/knowledge_graph.html.
3.2 RQ2. Qualitative and quantitative analysis of semaglutide side effects
We first examine the GPT-extracted Reddit post information on semaglutide, including side effects
and their severity/dosage information (if available), across different brands and over time (Figure
3). We observe that very few semaglutide-related side effects are discussed on Reddit before 2022,
with only 14 mentions in 2020 and 65 in 2021. However, discussions have increased sharply since
2023, with 1,215 mentions in 2023 and 4,195 mentions in 2024, and monthly mentions peaking in
the most recent month (1,614 relations in Jan. 2025, Figure 3A). This reflects the growing popularity
of all brands of Semaglutide, including Ozempic, Wegovy, Rybelsus, and emerging new brands,
for weight loss, as public interest and media coverage surged in recent years [42]. The decrease in
2025 in Figure 3A is due to our data collection ending on January 31, 2025, resulting in only one
month of data in the first quarter of 2025. The overall upward trends for Ozempic, Wegovy, and
unspecified brands suggest the increasing popularity of these brands in the following years. On the
other hand, the number of mentions per quarter for Rybelsus never exceeds 9 and does not show
a clear increasing or decreasing pattern over the years, suggesting that Rybelsus may not be as
popular and accepted as the other brands over the past five years.
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
Fig. 3. An overview of GPT-extracted Reddit post information on semaglutide. A) Number of Reddit mentions
of semaglutide side effects by brand between January 1st, 2020, and January 31st, 2025. B) Top 10 GPT-
extracted side effects mentioned for each brand of semaglutide. C) Overlapping top side effects extracted
across brands. D) Top 15 GPT-extracted side effects weighted by GPT-extracted severity across brands. The
point size indicates the number of mentions. Rybelsus is not displayed in the figure because none of the top
15 side effects with comments on severity were mentioned for Rybelsus.
The top 10 side effects extracted from Reddit across all brands are nausea (14.3%), decreased
appetite (3.8%), weight gain (3.2%), impaired gastric emptying (3.2%), constipation (2.7%), depression
(2.5%), increased appetite (2.4%), fatigue (2.4%), muscle loss (2.2%), and vomiting (2.2%). The top
side effects overlap considerably but also vary across different brands of Semaglutide (Figure 3B).
Among the top 20 side effects of each brand, the five top side effects shared by all brands are mostly
gastrointestinal symptoms (with one exception, “fatigue”), while other unique and shared side
effects are also gastrointestinal issues mainly, with other symptoms like negative emotion and
depressive symptoms (all but Wegovy) and heartburn (Wegovy and unspecified brands). Finally,
we examine the extracted severity information associated with the top 15 side effects across all
brands and observe that most of the comments on severity levels focus on “severe” followed by
“mild” (Figure 3D). Among the three brands, Ozempic shows the highest frequency of “severe” side
effects, particularly nausea, vomiting, pancreatitis, and allergic reactions. Wegovy’s profile shows
intermediate reporting rates, with nausea and abdominal pain being the most frequent severe
side effects. Unspecified brands demonstrate notably high reports of nausea, constipation, and
pancreatitis, but a large proportion of them only show mild side effects.
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
3.3 RQ3. Validation via comparison with adverse events reported in FAERS
Top side effects as identified by our Reddit-based knowledge graph demonstrate agreement with
FDA-registered top adverse events (AEs) (Figure 4). Most of the top twenty Reddit side effects are
successfully matched against top AEs recorded at the FDA FAERS (Methods, Figure 4A) The only
notable exceptions are (1) Reddit posts fail to cover adversarial procedural complications noted by
the FDA (e.g., off-label use, product use in unapproved indication) and (2) Reddit posts highlight
“minor” side effects—such as muscle loss and the so-called “Ozempic Face”—that the FDA does
not officially classify as adverse events. In addition to nominal matches, the frequencies of these
top events are also positively correlated between the two platforms (Spearman correlation=0.423;
Figure 4B)). Frequency of FDA AEs or Reddit side effects is calculated as the prevalence of an event
among all event reports or Reddit posts and represents the propensity for that event among all cases
under either platform (Methods). Our findings thus support concordance in Semaglutide usage’s
most common side effects, thus validating Reddit crowdsourcing-based results against established
FDA records (RQ3).
Beyond this overall agreement, Reddit crowdsourcing also identifies nuanced differences against
FDA reports (Figure 4B-D). Among AEs that are differentially detected between the two approaches,
crowd-sourcing demonstrates a higher tendency to report rarer AEs under FDA surveillance
(impaired gastric emptying, general gastrointestinal disorders, increased appetite weight increase,
thyroid cancer, and depression; Figure 4B, C). Statistical significance is established with formal
binomial regression and corrected for multiple testing (Methods). These findings, particularly those
related to the treatment’s less expected outcomes (e.g., increased appetite and weight gain), suggest
that Reddit users tend to discuss side effects that are less commonly recorded by the FDA. Lastly,
in medication brand-specific analysis (Methods), the differential pattern of Reddit crowdsourcing
versus FDA surveillance largely remains consistent across medication brands (Figure 4D). Most
prominently, increased appetite is significantly more frequent in Reddit posts compared to FDA
across all brands. Qualitative differences were only observed for two gastrointestinal conditions,
nausea and constipation, which were detected more frequently under Wegovy usage among Reddit
posts than FDA but less frequently under Ozempic usage. Such secondary differences between our
crowdsourcing-identified side effects in comparison to FDA reports highlight the complementary
capacity of crowdsourcing relative to official registrant data, in particular for events less commonly
registered in the latter (RQ3).
4 Discussion and Conclusions
We use semaglutide as a case study to introduce a structured pipeline that utilizes LLMs to extract
and process information on drug side effects from large social media platforms and formulates it
into a comprehensive KG. This framework supports future pharmacovigilance by integrating social
media as a supplementary source of RWD.
To address RQ1 (see Introduction), we develop a multi-stage pipeline that extracts side effect rela-
tions from Reddit posts using LLM and then organizes them into a knowledge graph linking drugs,
side effects, and their associated properties. Compared to earlier NLP methods based on keyword
matching [43] or co-occurrence frequencies [44], our approach captures more nuanced language
and semantic relationships, significantly enhancing recall and contextual relevance. In addition,
this pipeline can process crowdsourcing data from social media, which captures real-world drug use
and user-centered experience that often remain underrepresented in conventional clinical datasets,
such as depression caused by semaglutide in our results. This insight can reveal latent patient
concerns and subtle drug interactions that could be valuable for promoting pharmacovigilance
strategies.
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
Fig. 4. Crowd-sourced side effect surveillance based on Reddit posts for semaglutide demonstrates mostly
consistent findings with FDA-registered AEs, with additional unique discoveries. A) Correspondence between
the top 20 side effects identified by our Reddit-based knowledge graph and top AEs registered by the FDA.
B) Frequency of top events as measured by the FDA compared to Reddit posts largely also agree with
each other (Spearman correlation of per-adverse-event frequencies=0.423). C) Binomial logistic regression
formally established events that Reddit crowdsourcing differentially detected compared to FDA (log odds
ratio; statistical significance determined with p<0.05 post-Bonferroni correction across AEs).D) Brand-specific
analysis of the differential pattern of Reddit crowdsourcing versus FDA surveillance.
Regarding RQ2 and RQ3 (see Introduction), analysis of the knowledge graph shows that the
most common side effects are largely similar across different brands of Semaglutide, but there
are also some differences. All three brands share the same top seven side effects, most of which
are gastrointestinal issues (e.g., nausea and vomiting). This is consistent with reports from the
FAERS database. Among the three brands, Ozempic has the highest number of reports of severe
side effects. We also find that mental health-related symptoms—such as depression, anxiety, and
mood swings—appear more often than FAERS. These symptoms are usually described in user posts
that mention emotional struggles or a lack of motivation, which are often missed or underreported
in traditional adverse event reporting systems. These findings also suggest that psychological
symptoms, though frequently overlooked or underreported in traditional AEs reporting systems,
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
may play a significant role in shaping patient experiences for weight loss drug use. This further
underscores the value of patient-shared experiences in capturing a broader and more nuanced
spectrum of adverse effects. In addition, Reddit posts often appear to surface less common or
emerging concerns, such as thyroid cancer, showing the platform’s potential for identifying side
effects that may be underreported in existing databases.
Our pipeline also has room for growth. First, we make a trade-off in this study by selecting
GPT-4o mini as the backbone model for information extraction to ensure cost-effectiveness. While
the model demonstrates strong performance, it occasionally misinterprets prompts—for instance,
including side effects related to other drugs like Zepbound. Future work could explore alternative
models and refined prompt engineering to improve accuracy.
Second, there is a conceptual challenge in distinguishing AEs from side effects. While AEs
encompass all undesirable experiences during drug use, side effects imply a confirmed causal
link. However, this nuance is often lost in public discourse; users on social media commonly use
“side effect” as a catch-all. To align with user language, we use “side effect” during extraction but
compared results with FDA-reported AEs for rigor. Future research can focus on better integrating
official and user-generated data sources.
Despite these limitations, this work contributes to advancing patient-centered pharmacovigilance
by demonstrating the potential of combining user-generated online content and rapidly evolving
AI tools to capture patient voices.
References
[1] A. Lavertu, B. Vora, K. M. Giacomini, R. Altman, and S. Rensi, “A new era in pharmacovigilance: toward real-world
data and digital monitoring, ”Clinical Pharmacology & Therapeutics , vol. 109, no. 5, pp. 1197–1202, 2021.
[2] L. Blonde, K. Khunti, S. B. Harris, C. Meizinger, and N. S. Skolnik, “Interpretation and impact of real-world clinical data
for the practicing clinician, ”Advances in therapy, vol. 35, pp. 1763–1774, 2018.
[3] B. E. Wilson and C. M. Booth, “Real-world data: bridging the gap between clinical trials and practice, ”EClinicalMedicine,
vol. 78, 2024.
[4] F. Grimberg, P. M. Asprion, B. Schneider, E. Miho, L. Babrak, and A. Habbabeh, “The real-world data challenges radar:
a review on the challenges and risks regarding the use of real-world data, ”Digital Biomarkers, vol. 5, no. 2, pp. 148–157,
2021.
[5] A. Makady, A. de Boer, H. Hillege, O. Klungel, W. Goettschet al., “What is real-world data? a review of definitions
based on literature and stakeholder interviews, ”Value in health, vol. 20, no. 7, pp. 858–865, 2017.
[6] U.S. Food and Drug Administration. (2019) Real-world evidence. Accessed March 2025. [Online]. Available:
https://www.fda.gov/science-research/science-and-research-special-topics/real-world-evidence
[7] ——. (2020) Postmarketing surveillance programs. Accessed March 2025. [Online]. Available: https://www.fda.gov/
drugs/surveillance/postmarketing-surveillance-programs
[8] L. McDonald, B. Malcolm, S. Ramagopalan, and H. Syrad, “Real-world data and the patient perspective: the promise of
social media?” BMC Medicine, vol. 17, no. 1, p. 11, 2019.
[9] D. Wessel and N. Pogrebnyakov, “Using social media as a source of real-world data for pharmaceutical drug development
and regulatory decision making, ”Drug Safety, vol. 47, no. 5, pp. 495–511, 2024.
[10] A. Sarker, R. Ginn, A. Nikfarjam, K. O’Connor, K. Smith, S. Jayaraman, and G. Gonzalez, “Utilizing social media data
for pharmacovigilance: a review, ”Journal of Biomedical Informatics , vol. 54, pp. 202–212, 2015.
[11] D. Pappa and L. K. Stergioulas, “Harnessing social media data for pharmacovigilance: a review of current state of the
art, challenges and future directions, ”International Journal of Data Science and Analytics , vol. 8, no. 2, pp. 113–135,
2019.
[12] National Bureau of Economic Research. (2023) Fda adverse event reporting system. Accessed March 2025. [Online].
Available: https://www.nber.org/research/data/fda-adverse-event-reporting-system
[13] L. Li, J. Zhou, Z. Ma, M. T. Bensi, M. A. Hall, and G. B. Baecher, “Dynamic assessment of the covid-19 vaccine acceptance
leveraging social media data, ”Journal of Biomedical Informatics , vol. 129, p. 104054, 2022.
[14] A. Dirkson, S. Verberne, G. Van Oortmerssen, H. Gelderblom, and W. Kraaij, “How do others cope? extracting coping
strategies for adverse drug events from social media, ”Journal of Biomedical Informatics , vol. 139, p. 104228, 2023.
[15] D. Yu and V. V. Vydiswaran, “An assessment of mentions of adverse drug events on social media with natural language
processing: model development and analysis, ”JMIR Medical Informatics, vol. 10, no. 9, p. e38140, 2022.
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
[16] A. Nikfarjam, A. Sarker, K. O’Connor, R. Ginn, and G. Gonzalez, “Pharmacovigilance from social media: mining adverse
drug reaction mentions using sequence labeling with word embedding cluster features, ” Journal of the American
Medical Informatics Association, vol. 22, no. 3, pp. 671–681, 2015.
[17] Z. Li, Z. Yang, L. Wang, Y. Zhang, H. Lin, and J. Wang, “Lexicon knowledge boosted interaction graph network for
adverse drug reaction recognition from social media, ”IEEE Journal of Biomedical and Health Informatics , vol. 25, no. 7,
pp. 2777–2786, 2020.
[18] Y. Hua, H. Jiang, S. Lin, J. Yang, J. M. Plasek, D. W. Bateset al., “Using twitter data to understand public perceptions of
approved versus off-label use for covid-19-related medications, ”Journal of the American Medical Informatics Association,
vol. 29, no. 10, pp. 1668–1678, 2022.
[19] S. Golder, K. Smith, K. O’Connor, R. Gross, S. Hennessy, and G. Gonzalez-Hernandez, “A comparative view of reported
adverse effects of statins in social media, regulatory data, drug information databases and systematic reviews, ”Drug
Safety, vol. 44, pp. 167–179, 2021.
[20] D. Xu, W. Chen, W. Peng, C. Zhang, T. Xu, X. Zhao et al. , “Large language models for generative
information extraction: a survey, ” arXiv preprint arXiv:2312.17617, 2023, accessed March 2025. [Online]. Available:
https://arxiv.org/abs/2312.17617
[21] X. Xu, Z. Xue, C. Zhang, J. Medri, J. Xiong, J. Zhou, J. Jin, Y. Zhang, S. Ma, and L. Li, “Patients speak, ai listens: Llm-based
analysis of online reviews uncovers key drivers for urgent care satisfaction, ”arXiv preprint arXiv:2503.20981, 2025.
[22] M. Hauben, M. Rafi, I. Abdelaziz, and O. Hassanzadeh, “Knowledge graphs in pharmacovigilance: a scoping review, ”
Clinical Therapeutics, 2024.
[23] S. Dhillon, “Semaglutide: First global approval, ” Drugs, vol. 78, no. 2, pp. 275–284, 2018.
[24] U.S. Food and Drug Administration. (2021) Fda approves new drug treatment for chronic weight management, first
since 2014. Accessed March 2025. [Online]. Available: https://www.fda.gov/news-events/press-announcements/fda-
approves-new-drug-treatment-chronic-weight-management-first-2014
[25] Centers for Disease Control and Prevention. (2024) Obesity and severe obesity prevalence in adults: United states, august
2021–august 2023. Accessed March 2025. [Online]. Available: https://www.cdc.gov/nchs/products/databriefs/db508.htm
[26] M. Ng, X. Dai, R. M. Cogen, M. Abdelmasseh, A. Abdollahi, A. Abdullahiet al., “National-level and state-level prevalence
of overweight and obesity among children, adolescents, and adults in the usa, 1990–2021, and forecasts up to 2050, ”
The Lancet, vol. 404, no. 10469, pp. 2278–2298, 2024.
[27] J. E. Raubenheimer, P. H. Myburgh, and A. S. Bhagavathula, “Sweetening the deal: an infodemiological study of
worldwide interest in semaglutide using google trends extended for health application programming interface, ”BMC
Global Public Health, vol. 2, no. 1, p. 63, 2024.
[28] A. C. Pickett, D. Valdez, K. L. Sinclair, W. J. Kochell, B. Fowler, and N. E. Werner, “Social media discourse related to
caregiving for older adults living with alzheimer disease and related dementias: computational and qualitative study, ”
JMIR Aging, vol. 7, no. 1, p. e59294, 2024.
[29] GoLogin. (2023) Web scraping reddit with python: A complete guide with code. Accessed March 2025. [Online].
Available: https://gologin.com/blog/web-scraping-reddit/
[30] U.S. Food and Drug Administration. (2020) Drug trial snapshot: Ozempic. Accessed March 2025. [Online]. Available:
https://www.fda.gov/drugs/drug-approvals-and-databases/drug-trial-snapshot-ozempic
[31] Y. Yin, Y. Shu, J. Zhu, F. Li, and J. Li, “A real-world pharmacovigilance study of fda adverse event reporting system
(faers) events for osimertinib, ”Scientific Reports, vol. 12, no. 1, p. 19555, 2022.
[32] L. He, Q. Li, Y. Yang, J. Li, W. Luo, Y. Huang et al., “Pharmacovigilance study of glp-1 receptor agonists for metabolic
and nutritional adverse events, ”Frontiers in Pharmacology, vol. 15, p. 1416985, 2024.
[33] N. E. Omar, A. F. Soliman, M. Eshra, T. Saeed, A. Hamad, and A. Abou-Ali, “Postmarketing safety of anaplastic
lymphoma kinase (alk) inhibitors: an analysis of the fda adverse event reporting system (faers), ”ESMO Open, vol. 6,
no. 6, p. 100315, 2021.
[34] MedDRA. (2019) Meddra. Accessed March 2025. [Online]. Available: https://www.meddra.org/
[35] J. White, Q. Fu, S. Hays, M. Sandborn, C. Olea, H. Gilbert et al. , “A prompt pattern catalog to enhance prompt
engineering with chatgpt, ” arXiv preprint arXiv:2302.11382, 2023, accessed March 2025. [Online]. Available:
https://arxiv.org/abs/2302.11382
[36] Z. Gao, L. Li, S. Ma, Q. Wang, L. Hemphill, and R. Xu, “Examining the potential of chatgpt on biomedical information
retrieval: fact-checking drug-disease associations, ”Annals of Biomedical Engineering, vol. 52, no. 8, pp. 1919–1927, 2024.
[37] Z. Wan, F. Cheng, Z. Mao, Q. Liu, H. Song, J. Li et al. , “Gpt-re: In-context learning for relation extraction
using large language models, ” arXiv preprint arXiv:2305.02105, 2023, accessed March 2025. [Online]. Available:
https://arxiv.org/abs/2305.02105
[38] OpenAI. (2024) Gpt-4o mini: advancing cost-efficient intelligence. Accessed March 2025. [Online]. Available:
https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
[39] SBERT Team. (2025) Sentencetransformers documentation — sentence-transformers documentation. Accessed March
2025. [Online]. Available: https://sbert.net/
[40] H. Song, H. Su, I. Shalyminov, J. Cai, and S. Mansour, “Finesure: Fine-grained summarization evaluation using llms, ”
arXiv, 2024, cornell University, June 30, 2024.
[41] J. Wang, Y. Cheng, J. Chen, H. Xu, D. Chen, and J. Wu, “Multi-rater prompting for ambiguous medical
image segmentation, ” arXiv preprint arXiv:2404.07580, 2024, accessed March 25, 2025. [Online]. Available:
https://arxiv.org/abs/2404.07580
[42] J. H. Watanabe, J. Kwon, B. Nan, and A. Reikes, “Trends in glucagon-like peptide 1 receptor agonist use, 2014 to 2022, ”
Journal of the American Pharmacists Association , vol. 64, no. 1, pp. 133–138, 2024.
[43] S. Sellami and N. E. Zarour, “Keyword-based faceted search interface for knowledge graph construction and exploration, ”
International Journal of Web Information Systems , vol. 18, no. 5/6, pp. 453–486, 2022.
[44] A. Onan, S. Korukoğlu, and H. Bulut, “Ensemble of keyword extraction methods and classifiers in text classification, ”
Expert Systems with Applications, vol. 57, pp. 232–247, 2016.
A Prompt design
1 PROMPT = {
2 " Task " : (
3 " Extract relations about the side effects of semaglutide , including Wegovy ,
Ozempic , and Rybelsus , or semaglutide in general , from the given text . "
4 " Here is the given text : { text } "
5 ) ,
6
7 " Instruction " : """
8 Return the extracted relations in the exact format below :
9
10 [
11 {
12 " start ": {
13 " label ": " Medication " ,
14 " properties ": {" name ": ""}} ,
15 " end ": {
16 " label ": " SideEffect " ,
17 " properties ": {" name ": ""}} ,
18 " properties ": {
19 " severity ": null ,
20 " duration ": null ,
21 " dosage ": null ,
22 " description ": ""}
23 } ,
24 ...
25 ]
26
27 ### Guidelines :
28 - ** Only extract side effects that are caused by semaglutide .**
29 - ** Do NOT extract side effects caused by other drugs ( e . g . Mounjaro (
tirzepatide ) ) .**
30 - ** Use standard brand name ** for medications :
31 - " Wegovy " , " Ozempic " , " Rybelsus "
32 - ** If no specific brand name is mentioned ** , use **" Semaglutide "** as the
medication name .
33 - ** If multiple side effects are mentioned ** , extract them all in ** separate
relation entries **.
, Vol. , No. , Article . Publication date: .

Crowdsourcing-Based Knowledge Graph Construction for Drug Side Effects Using Large Language Models with an
Application on Semaglutide
34 - ** The " severity " , " duration " , and " dosage " properties should only be
included if explicitly mentioned in the text .**
35 - If severity , duration , or dosage is not stated , set them to `null `.
36 - ** The " description " property ** should provide a ** concise , factual
explanation ** of the relation .
37 - ** If no relevant relations can be extracted , return `null `.**
38 - ** Do NOT include any explanations or additional information beyond the
specified format .**
39 - ** Return ONLY valid JSON .** Do NOT include `" json " ` or any other prefix in
your response .
40
41
42 ### Example 1:
43 ** Input Text :**
44 " My biggest side effects were fatigue and dizziness , which lasted for three
months while I was on the 0.5 mg dose ."
45 ** Expected Output :**
46 [
47 {
48 " start ": {
49 " label ": " Medication " ,
50 " properties ": {" name ": " Semaglutide "}} ,
51 " end ": {
52 " label ": " SideEffect " ,
53 " properties ": {" name ": " fatigue "}} ,
54 " properties ": {
55 " severity ": null ,
56 " duration ": "3 months " ,
57 " dosage ": "0.5 mg " ,
58 " description ": " The user experienced fatigue from semaglutide , lasting
three months at the 0.5 mg dose ."}} ,
59 {
60 " start ": {
61 " label ": " Medication " ,
62 " properties ": {" name ": " Semaglutide "}} ,
63 " end ": {
64 " label ": " SideEffect " ,
65 " properties ": {" name ": " dizziness "}} ,
66 " properties ": {
67 " severity ": null ,
68 " duration ": "3 months " ,
69 " dosage ": "0.5 mg " ,
70 " description ": " The user experienced dizziness from semaglutide ,
lasting three months at the 0.5 mg dose ."}}
71 ]
72
73 ### Example 2:
74 ** Input Text :**
75 " It also makes you have some severe stomach pain if you overeat anyway ."
76 ** Expected Output :**
77 [
78 {
, Vol. , No. , Article . Publication date: .

Duan and Wei, et al.
79 " start ": {
80 " label ": " Medication " ,
81 " properties ": {" name ": " Semaglutide "}} ,
82 " end ": {
83 " label ": " SideEffect " ,
84 " properties ": {" name ": " stomach pain "}} ,
85 " properties ": {
86 " severity ": " severe " ,
87 " duration ": null ,
88 " dosage ": null ,
89 " description ": " Severe stomach pain occurs if you overeat ."}
90 }
91 ]
92
93 ### Example 3:
94 ** Input Text :**
95 " I've been using sema for months and had no side effects ."
96 ** Expected Output :**
97 null
98 ** Return null if the text states that no side effects were experienced **
99
100 ### Example 4:
101 ** Input Text :**
102 " Ozempic does not cause headaches ."
103 ** Expected Output :**
104 null
105 ** Return null if the text states that semaglutide does NOT cause a side effect
**
106
107 ### Example 5:
108 ** Input Text :**
109 " I experienced headaches after taking Tirzepatide ."
110 ** Expected Output :**
111 null
112 ** Return null if the text is talking about another drug other than semaglutide
**
113 """
114 }
, Vol. , No. , Article . Publication date: .
