---
title: Association Rules of Author Keywords for Thematic Mapping in Systematic Literature Reviews
url: https://doi.org/10.62036/isd.2026.47
category: consumer-behavior
subcategory: framework
date: 2026-09
venue: Proceedings of the International Conference on Information Systems Development
authors:
- Paweł Karol Frankowski
- Joanna Wiśniewska
- Sebastian Matysik
source: openalex-oa
pdf_url: https://aisel.aisnet.org/cgi/viewcontent.cgi?article=1843&context=isd2014
pages: 8
chars: 22617
fetched_at: '2026-11-08T19:00:47+00:00'
kb_version: 1
---

# Association Rules of Author Keywords for Thematic Mapping in Systematic Literature Reviews

34TH INTERNATIONAL CONFERENCE ON INFORMATION SYSTEMS DEVELOPMENT (ISD2026 PRAGUE, CZECHIA)
Association Rules of Author Keywords for Thematic Mapping in
Systematic Literature Reviews
Paweł Karol Frankowski
Maritime University of Szczecin, Faculty of
Computer Science and Telecommunication
Szczecin, Poland p.frankowski@pm.szczecin.pl

Joanna Wiśniewska
University of Szczecin, Institute of
Management
Szczecin, Poland joanna.wisniewska@usz.edu.pl

Sebastian Matysik
University of Szczecin, Institute of
Management, Doctoral School
Szczecin, Poland sebastian.matysik@usz.edu.pl

Abstract
Systematic literature reviews (SLRs) commonly use keyword co -occurrence analysis for
thematic mapping, but standard tools (e.g., VOSviewer, Bibliometrix) are limited to symmetric
pairwise relationships. The aim of this study is to formalize author keyword association rule
extracting (ARM) as a repeatable, complementary method for thematic mapping in SLR and to
evaluate its analytical value relative to standard co-occurrence methods. We apply the Apriori
algorithm to author keywords from Scopus and demonstrate it on two datasets: a medium one
(597 publications on CSR and consumer behavior) and a large one (14,302 publications on
gamification and marketing). Comparing ARM results with VOSviewer co-occurrence maps,
we find ARM reveals directional dependencies and multi-item themes that symmetric analyses
miss. We propose a three-step framework to incorporate ARM into the PRISMA synthesis stage
and discuss using ARM-derived themes for embedding-based screening in EmbedSLR.
Keywords: association rule mining, systematic literature review, author keywords, thematic
mapping, Apriori algorithm, bibliometrics

1  Introduction
Systematic literature reviews (SLRs) are vital for synthesizing scientific knowledge, with
thematic mapping as a key component that identifies dominant research themes and
relationships among topics using bibliometric tools such as keyword co-occurrence analysis.
While traditional methods face limitations in capturing directional and multi-item relationships,
association rule mining (ARM) offers a promising alternative that has yet to be formally
integrated into SLR methodology or compared with existing co-occurrence tools.
The aim of this study is to formalize the process of extracting association rules from
authors’ keywords as a repeatable, complementary method for thematic mapping in systematic
literature reviews, and to assess its analytical capabilities compared with st andard co-
occurrence-based methods. To achieve this objective, we pose three research questions:
RQ1: To what extent does the exploration of authors’ keyword association rules reveal
thematic relationships, including directional dependencies and multi-element patterns, which
are not apparent in standard symmetric co-occurrence analysis?
RQ2: What differences are observed in the performance and results of the ARM model
depending on the size and thematic structure of the text corpora, and what parameter calibration
is required?
RQ3: How can association rule extraction be integrated into the PRISMA -guided
systematic review workflow to complement existing bibliometric tools?

FRANKOWSKI ET AL.  ASSOCIATION RULES OF AUTHOR KEYWORDS…
We address these questions by: (1) formalizing the ARM pipeline for Scopus-exported
author keywords, (2) demonstrating the method on two contrasting corpora with an explicit
comparison to VOSviewer, and (3) proposing a three-step integration framework. Section 2
reviews related work. Section 3 describes the method. Section 4 presents the demonstration
results. Section 5 discusses implications. Section 6 concludes.

2  Related Work
2.1  Association Rule Extraction in Bibliometrics
Although Association Rule Mining (ARM) [1, 2] and its text-based applications [3] have
been explored, existing studies applying ARM to bibliometric keywords [5] have largely
utilized it as an ad hoc descriptive tool rather than a formalized, reproducible methodological
framework.
A critically important observation, not previously highlighted in the ARM-bibliometrics
literature, is that VOSviewer’s association strength normalization is proportional to the lift
metric in ARM. Both compute the ratio of observed co-occurrence to expected co-occurrence
under independence. This means that existing bibliometric tools already implicitly use one core
ARM metric, but do not exploit the additional analytical capabilities of confidence (directional
conditional probability) and multi-item pattern discovery that the full ARM framework
provides.

2.2  Computational Support for SLR Automation
Automation of SLR processes has progressed unevenly across review stages. Van de Schoot
et al. [10] introduced ASReview, an active learning tool that reduces screening workload.
Marshall and Wallace [6] offer a guide to machine learning tools for research synthesis. Ofori-
Boateng et al. [8] conducted a systematic review of 52 studies on AI for systematic review
automation, identifying the synthesis stage as the main automation gap. Chen, Tsang, and Wu
[4] reviewed text extraction and bibliometric science mapping, identifying research opportunity
associations.
Matysik, Wiśniewska, and Frankowski [7] introduced EmbedSLR, an open-source Python
framework that combines embedding-based semantic similarity with bibliometric validation for
SLR screening. EmbedSLR ranks publications by the cosine distance between user-defined
natural-language problem descriptions and article embeddings, producing reproducible
shortlists. The effectiveness of this approach depends critically on the precision of the problem
description: vague queries retrieve broad, unfocused results, whereas precise, multi-faceted
descriptions yield thematically coherent shortlists. The potential synergy between ARM -
discovered thematic structures and embedding-based query formulation is explored in
Section 5.3.

3  Method
3.1  Data Representation
We model a bibliographic corpus as a transactional database for ARM, where each publication
is a transaction and author keywords are the itemset. Let D = {d₁, d₂, …, dₙ} be N publications
from Scopus. Each publication dᵢ has keywords Kᵢ = {k₁, k₂, …, kₘ}, with variable m. The
complete keyword set is K = ∪ᵢKᵢ. This structure is similar to market basket analysis:
publications as customers, keywords as items, and keyword sets as baskets.

3.2  Preprocessing
Author keywords are extracted from the Scopus CSV 'Author Keywords' column, with multiple
keywords separated by semicolons. They are converted to lowercase, trimmed, and duplicates
within a publication are removed. No stemming or lemmatization is applied. Publications
lacking author keywords are excluded.

ISD2026 PRAGUE, CZECHIA

3.3  Frequent Itemset Generation
We use the Apriori algorithm [2] to find keyword sets that co-occur across publications at or
above a minimum frequency. Implemented with mlxtend (version 0.24.0) in Google Colab,
support of a keyword set S is defined as:
 𝑠𝑢𝑝𝑝𝑜𝑟𝑡(𝑆)=|{#∈%∶	(⊆*(#)}| . ≥𝜎 (1)
Where: S is a candidate keyword set (itemset), K(d) is the set of author keywords for publication
d, N is the total number of publications with author keywords in the corpus, and σ is the
minimum support threshold (a user-defined parameter).
The Apriori property states that all subsets of a frequent itemset are also frequent, enabling
efficient pruning: if a keyword pair {A, B} doesn't meet the support threshold, no superset
containing both needs evaluation.

3.4  Association Rule Generation
From each frequent itemset S of size ≥ 2, we generate all association rules A → B, where A
(antecedent) and B (consequent) are non-empty, disjoint subsets of S whose union equals S.
Confidence measures the conditional probability of B given A.
 𝑐𝑜𝑛𝑓𝑖𝑑𝑒𝑛𝑐𝑒(𝐴→𝐵)=/011234(5∪7) /011234(5)≥𝛾 (2)
Where: A is the antecedent (condition) keyword set, B is the consequent (outcome) keyword
set, with A ∩ B = ∅ and A ∪ B = S, and γ is defined by the user's minimum confidence threshold.
Confidence is inherently directional: confidence(A → B) ≠ confidence(B → A) in general.
This asymmetry is the key distinction from symmetric co-occurrence analysis. The lift metric
quantifies whether co-occurrence exceeds statistical independence:
 𝑙𝑖𝑓𝑡(𝐴→𝐵)=829:;#<98<(5→7) /011234(7)  (3)
Where: lift > 1 indicates positive association (co-occurrence stronger than chance), lift = 1
indicates statistical independence (no association), lift < 1 indicates negative association.

3.5  Parameter Selection
Two parameters are required: minimum support ( σ) and minimum confidence (γ). The
appropriate value of σ depends on the size of the corpus: for small corpora (N < 100), choose σ
between 0.05 and 0.10; for medium-sized corpora (100 < N < 1,000), select σ between 0.005
and 0.02; and for large corpora (N > 1,000), it can be as low as 0.001 to 0.005. Begin with σ set
to 0.05 and reduce it by half until at least 10 keyword pairs surpass this value. The default
confidence γ = 0.3, which is common in ARM [1], is also applied here.

3.6  Integration Framework for SLRs
We suggest integrating ARM into the PRISMA-guided SLR workflow [9] at the synthesis
stage, after article screening. The framework involves three steps: (1) apply the Apriori
algorithm to find frequent itemsets and rules from author keywords, (2) use high-lift rules to
identify thematic clusters and concept dependencies, and (3) organize qualitative synthesis and
develop research questions based on the thematic structure. This complements standard co-
occurrence tools like VOSviewer and Bibliometrix.

4  Demonstration
4.1  Case 1: CSR and Consumer Behavior (Medium Corpus)

FRANKOWSKI ET AL.  ASSOCIATION RULES OF AUTHOR KEYWORDS…
The first corpus was retrieved from Scopus on January 26, 2025, using the query (‘CSR
influence’ OR ‘Corporate Social Responsibility influence’) AND ‘consumer behavior’ on
January 26, 2025, yielding 597 publications. Of these, 555 (93%) contained author keywords
with 1,741 unique terms. The Apriori algorithm (σ=0.005, γ=0.3) generated 278 frequent
itemsets (151 singletons, 115 pairs, 11 triples, 1 quadruple) and 138 rules.
Fig. 1 shows the keyword frequency distribution. “Corporate social responsibility” leads at
42.0%, with “csr” at 14.4% and “corporate social responsibility (csr)” at 6.7%, highlighting the
normalization challenge. Other key keywords include “customer loyal ty” (6.0%),
“sustainability” (5.8%), “customer satisfaction” (4.7%), and “brand image” (4.7%).

Fig. 1. Top 25 author keywords by frequency (CSR corpus, N = 555)
Fig. 2 displays a co-occurrence heatmap, highlighting strong links like "corporate social
responsibility” with “csr” (20), "customer loyalty” (18), and "sustainability” (15). It shows joint
frequency of occurrence but no direction or conditionality.

Fig. 2. Co-occurrence heatmap (CSR corpus)
Table 1 presents selected association rules. The results reveal three types of insights
invisible to standard co-occurrence. First, the multi-item rule {customer loyalty, customer trust}

ISD2026 PRAGUE, CZECHIA
→ {CSR, customer satisfaction} (confidence = 0.80, lift = 31.7) identifies a four -keyword
thematic cluster linking consumer relationship constructs to CSR evaluation a pattern
unreachable by pairwise analysis. Second, the directional rule {customer loyalty} → {CSR}
(confidence = 0.545) reveals that 55% of customer loyalty research addresses CSR, while the
reverse holds for only 7.7% (support of pair/support of CSR = 0.032/0.420). Third, high-lift
rules such as {brand equity, brand loyalty} → {brand awareness} (lift = 52.0) identify tightly
coupled conceptual triads.

Table 1. Selected association rules from CSR corpus (σ = 0.005, γ = 0.3)
Antecedent Consequent Support Confidence Lift
brand equity + brand loyalty brand awareness 0.005 0.750 52.03
Twitter social media 0.005 1.000 42.69
cust. loyalty + cust. Trust CSR + cust. Satisfaction 0.007 0.800 31.71
CSR + cust. Trust cust. loyalty + cust. Satisfaction 0.007 0.444 27.41
CSR + satisfaction Loyalty 0.005 0.600 22.20
customer loyalty CSR 0.032 0.545 1.30
CSR + cust. Satisfaction customer loyalty 0.016 0.643 10.81

Fig. 3 shows the directed network of the top 40 rules, revealing distinct thematic clusters
around customer trust, brand equity-awareness-loyalty, service quality, and organizational
identification.
 Fig. 3. Association rule network, top 40 rules, edge thickness = lift (CSR corpus)

4.2  Comparison with VOSviewer Co-occurrence Map
We analyzed 597 CSR publications with VOSviewer 1.6.20 using author keyword co -
occurrence, a minimum of 5 occurrences, and association strength normalization. Fig. 4 shows
the co-occurrence map.
The VOSviewer map shows thematic clusters, with a central group around “corporate social
responsibility” and satellite clusters on sustainability, trust, banking, and ID. However, some
aspects remain hidden. It shows that “customer loyalty” and “CSR” are connected, but only

FRANKOWSKI ET AL.  ASSOCIATION RULES OF AUTHOR KEYWORDS…
55% of customer loyalty articles address CSR, while 7.7% of CSR articles cover loyalty, shown
only through confidence. The cluster {customer loyalty, trust, CSR, satisfaction} seen in ARM
(Table 1, lift=31.7) isn’t a distinct group in the network. Edge weights encode association
strength but don’t reveal the conditional probabilities that confidence provides.
Importantly, VOSviewer excels at visual exploration and community detection at the macro
level, capabilities that ARM does not replicate. The two methods are complementary:
VOSviewer provides the visual landscape, while ARM reveals the directional micro-structure
within that landscape.

Fig. 4. VOSviewer keyword co-occurrence map (CSR corpus, same dataset as Figs. 1-3)

4.3  Case 2: Gamification and Marketing (Large Corpus)
The second corpus, retrieved using 'gamification' AND 'marketing', included 14,302
publications (12,209 with author keywords, 7,891 unique terms). To address RQ2, we applied
ARM at three support thresholds within the recommended range for large corpora (Table 2).

Table 2. ARM results for the gamification corpus across minimum support thresholds
σ (Threshold) Frequent Itemsets Association Rules Rules without "gamification" as consequent
0.005 82 6 0
0.002 337 30 7
0.001 759 71 23

At σ = 0.005, only 6 star-topology rules emerged, all with "gamification" as the sole
consequent. Lowering σ to 0.001 increased the number of rules to 71, revealing 23 clusters
(e.g., TAM, XR). Notably, 48 of 71 rules (67.6%) still focus on "gamification" as the only
outcome. This confirms the monopolar structure as inherent in the gamification–marketing
literature rather than an artifact. This exercise addresses RQ2, showing how corpus size and
thematic spread influence parameter choice and interpretability.

5  Discussion
5.1  Addressing the Research Questions
Regarding RQ1, the CSR demonstration generated 138 association rules, including 11
triples and 1 quadruple, with no directional asymmetries in the VOSviewer output. Section 4.2

ISD2026 PRAGUE, CZECHIA
shows VOSviewer excels in macro visual exploration and community detection, but ARM
uniquely reveals: (a) directional dependencies via confidence, (b) multi-item clusters from
frequent itemsets of size ≥3, and (c) relationship strength beyond edge thickness in network
visualizations.
Regarding RQ2, identical parameters yielded 138 rules in the CSR corpus but only 6 in the
gamification corpus, showing strong corpus dependence. The star topology in gamification isn't
a method failure but reflects the field's monopolar structure, quantifying what VOSviewer map
inspection suggests qualitatively.
Regarding RQ3, we proposed a three-step integration framework (Section 3.6) placing
ARM at the PRISMA synthesis stage. ARM enhances VOSviewer and Bibliometrix with
directionality, multi-item patterns, and quantifiable thresholds in thematic mapping.

5.2  Iterative Approach for Large Corpora
As shown in Section 4.3 (Table 2), ARM on large, heterogeneous corpora yields limited
results due to keyword dispersion. We propose an iterative approach that combines ARM with
embedding-based screening to address this. Lowering the support threshold on the gamification
corpus reveals satellite clusters while preserving the main star topology, showing that iterative
refinement uncovers finer themes without losing the macro view. The procedure cycle is:
Step 1: Run ARM on the full Scopus export to identify dominant themes and keywords,
along with their confidence values. Step 2: Use these rules to refine the research problem,
adding high-confidence keywords as query terms. Step 3: Use EmbedSLR [7] with this query
to rank and filter the corpus, focusing on the most relevant publications. Step 4: Re-run ARM
on this smaller, more focused set to uncover richer, finer thematic structures.
This cycle repeats: refining the research question, shrinking the corpus, and enabling ARM
to uncover more detailed thematic patterns. It turns ARM's limitation on large corpora into a
strength: the coarse initial ARM output serves as a starting point for iterative problem
definition, eliminating the need for the researcher to formulate a precise query from intuition.
Each iteration is deterministic and reproducible, since both ARM (Apriori algorithm) and
EmbedSLR (cosine distance with fixed embeddings) produce identical outputs with the same
inputs.

5.3  Limitations and Future Work
This study has limitations: it doesn't address keyword normalization, as three synonyms of
“CSR” reduce support and fragment clusters; manual thesaurus creation or automated
deduplication is needed. ARM doesn't directly find research gaps, but negative rules (lift < 1)
between related keywords could show unexplored interdisciplinary links, a promising future
avenue. The minimum support threshold needs corpus-specific calibration; we suggest iterative
halving, but no formal optimality criterion exists.
Future work should: (1) validate the framework on corpora with 200 -500 publications
typical of focused SLRs, (2) benchmark ARM outputs against VOSviewer and Bibliometrix
thematic maps with expert evaluation, (3) explore temporal ARM to track evolving keyword
associations over years, (4) add Index Keywords or MeSH terms with author keywords to enrich
transaction representation, (5) empirically test if ARM-informed problem descriptions lead to
higher-quality shortlists in EmbedSLR versus intuitive queries, and (6) validate the iterative
ARM EmbedSLR cycle in Section 5.4 by measuring thematic coherence improvements.

6  Conclusion
This paper formalized the extraction of association rules from author keywords as a
reproducible, complementary method for thematic mapping in systematic literature reviews.
Demonstrations on two contrasting corpora (a medium CSR corpus with 597 publications and
138 rules, and a large gamification corpus with 14,302 publications and 6 rules), along with a
comparison with VOSviewer, showed that ARM offers three capabilities absent from standard
co-occurrence tools: directional conditional probabilities via confidence, multi-item pattern

FRANKOWSKI ET AL.  ASSOCIATION RULES OF AUTHOR KEYWORDS…
discovery via frequent itemsets, and quantifiable interestingness metrics such as support,
confidence, and lift. We explained weaker performance on large corpora by keyword dispersion
and proposed an iterative refinement cycle that combines ARM with embedd ing-based
screening. The mathematical equivalence between VOSviewer’s association strength and
ARM’s lift further motivates integration. We contributed a three -step PRISMA-aligned
framework to address the SLR synthesis automation gap.
Declaration of generative AI
AI supported this work. Translation content verification was partially performed using
Perplexity and Claude.ai. Linguistic proofreading was performed using Grammarly.
Claude.ai, and NotebookLM supported the review and analysis of the collected scientific
publications.
Acknowledgment

Co-financed by the Minister of Science under the “Regional Excellence Initiative”.
References
1. Agrawal, R., Imielinski, T., Swami, A.: Extracting Association Rules Between Sets of
Items in Large Databases. In: Proc. ACM SIGMOD Record, Volume 22, Issue 2, pp.
207-216. ACM (1993)
2. Agrawal, R., Srikant, R.: Fast Algorithms for Extracting Association Rules in Large
Databases. In: VLDB '94: Proceedings of the 20th International Conference on Very
Large Data Bases, pp. 487-499. Morgan Kaufmann (1994)
3. Cagliero, L., Garza, P., Kavoosifar, M.R., Baralis, E.: Discovering cross-topic
collaborations among researchers by exploiting weighted association rules.
Scientometrics 116 (2), 1273-1301 (2018).
4. Chen, H., Tsang, Y.P., Wu, C.H.: When Text Mining Meets Science Mapping: A
Review and Future Opportunities. International Journal of Engineering Business
Management 15, 18479790231222349 (2023)
5. Kumar, S., Kar, A.K., Ilavarasan, P.V.: Applications of Text Mining in Services
Management: A Systematic Literature Review. International Journal of Information
Management Data Insights 1 (1), 100008 (2021)
6. Marshall, I.J., Wallace, B.C.: Toward systematic review automation: a practical guide to
using machine learning tools in research synthesis. Systematic Reviews 8, 163 (2019)
7. Matysik, S., Wisniewska, J., Frankowski, P.K.: EmbedSLR: an Open-source Python
Framework for Efficient Embedding-based Screening and Bibliometric Validation in
Systematic Literature Review. SoftwareX 32, 102416 (2025)
8. Ofori-Boateng, R., Aceves-Martins, M., Wiratunga, N., Moreno-Garcia, C. F.: Towards
the automation of systematic reviews using natural language processing, machine
learning, and deep learning: a comprehensive review. Artificial Intelligence Review
57(8), 248 (2024)
9. Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C.
D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J.,
Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E.,
McDonald, S., McGuinness, L. A., Stewart, L. A., Thomas, J., Tricco, A. C., Welch, V.
A., Whiting, P., Moher, D.: The PRISMA 2020 Statement: An Updated Guideline for
Reporting Systematic Reviews. Syst. Rev. 10, 89 (2021)
10. van de Schoot, R., de Bruin, J., Schram, R., Zahedi, P., de Boer, J., Weijdema, F.,
Kramer, B., Huijts, M., Hoogerwerf, M., Ferdinands, G., Harkema, A., Willemsen, J.,
Ma, Y., Fang, Q., Hindriks, S., Tummers, L., Oberski, D. L.: An Open Source Machine
Learning Framework for Efficient and Transparent Systematic Reviews. Nat. Mach.
Intell. 3, 125-133 (2021)
