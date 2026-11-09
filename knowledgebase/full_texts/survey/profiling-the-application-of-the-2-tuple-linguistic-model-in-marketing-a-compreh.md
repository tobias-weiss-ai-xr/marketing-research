---
title: 'Profiling the application of the 2-tuple linguistic model in marketing: a comprehensive analysis
  and future directions'
url: https://doi.org/10.1007/s10700-026-09477-1
category: survey
subcategory: review
date: 2026-03
venue: Fuzzy Optimization and Decision Making
authors:
- Ziwei Shu
- José Javier Galán Hernández
- Álvaro Carrasco-Aguilar
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10700-026-09477-1.pdf
pages: 29
chars: 84787
fetched_at: '2026-11-08T18:39:19+00:00'
kb_version: 1
---

# Profiling the application of the 2-tuple linguistic model in marketing: a comprehensive analysis and future directions

Fuzzy Optimization and Decision Making (2026) 25:285–313
https://doi.org/10.1007/s10700-026-09477-1
Abstract
Customer opinions, preferences, and decision-makers’ insights play a vital role in
marketing by influencing product development, strategy, and customer experience.
Computing with Words (CWW) offers an effective method for processing this quali-
tative information using linguistic terms instead of numerical values. This work
aims to explore the application of one of the most widely used methodologies in
CWW—the 2-tuple linguistic model—in marketing. It employs a combination of
bibliometric analysis and a systematic literature review for a comprehensive analy -
sis. Articles published between 2000 and 2024 on the Web of Science database are
analyzed, incorporating Scopus´s Field-Weighted Citation Impact (FWCI) metrics
to assess the impact of individual studies and the average influence of research in
marketing-related areas. From an initial sample of 165 peer-reviewed articles, 90
were selected for analysis. The findings indicate that the 2-tuple linguistic model
is primarily applied to decision-making problems, with Multiple Attribute Group
Decision Making emerging as the most prominent theme due to its high centrality
and high density in the strategic diagram, as well as its strong connections to vari -
ous marketing-related areas. The 2-tuple linguistic model is widely applied in areas
such as supplier management and product development and innovation, with digital
transformation and consumer behavior representing potential directions for apply -
ing the model to address their respective marketing challenges. Using the FWCI,
this work also identifies marketing-related areas within decision-making themes
where the 2-tuple linguistic model is already applied but has limited influence,
revealing opportunities for development and future research.
Keywords Marketing · 2-tuple linguistic model · Computing with words ·
Decision making · Comprehensive analysis
Received: 6 October 2025 / Accepted: 10 March 2026 / Published online: 27 March 2026
© The Author(s) 2026
Profiling the application of the 2-tuple linguistic model in
marketing: a comprehensive analysis and future directions
Ziwei Shu1  · José Javier Galán Hernández2  · Álvaro Carrasco-Aguilar3
Extended author information available on the last page of the article
1 3

Z. Shu et al.
1 Introduction
Marketing is defined as "the management process responsible for identifying, antici-
pating and satisfying customer requirements profitably," a definition widely adopted
by the Chartered Institute of Marketing ( 2015), emphasizing its core functions:
understanding consumer needs, forecasting future demand, and creating products or
services that fulfill these needs while ensuring profitability. Marketing encompasses a
broad range of activities—from product development and advertising to distribution
and sales—aimed at attracting customers and encouraging them to choose a busi -
ness’s products or services. A careful consideration of multiple factors is essential
in marketing strategies, including consumer needs and preferences, components of
the marketing mix (product, price, place, and promotion), and ongoing competitive
analysis. This can enhance the effectiveness of marketing activities and align with
overarching business goals.
In the modern data-driven era, Marketing Analytics has emerged as a fundamental
discipline, defined as the systematic process of collecting, managing, analyzing, and
interpreting data to bridge customer psychology and managerial decision-making
(Basu et al., 2023). Moving beyond traditional descriptive reporting, it leverages
business intelligence to quantify complex market structures and risk exposures by
exploiting large volumes of quantitative data from Customer Relationship Manage -
ment (CRM) systems—such as sales records, marketing interactions, contact center
metrics—and financial performance indicators (Hye, 2025). However, decision-
makers face a persistent challenge: the inputs are inherently heterogeneous. They
must integrate this "hard" data with "soft" qualitative information (e.g., social media
reviews, expert panel judgments), which is often vague, subjective, and difficult to
process using standard statistical methods (Trung & Thanh, 2022).
This challenge is further intensified by increasingly complex consumer behav -
ior, the growth of omnichannel interactions, and rising expectations for personalized
experiences. As a result, marketers must move beyond purely quantitative metrics to
capture the nuanced and subjective perceptions that shape consumer decision-making
and guide product development and branding strategies (Lemon & Verhoef, 2016;
Rust, 2020). In practice, much of marketing data is expressed in linguistic terms
rather than precise numerical values. For example, customer feedback often includes
subjective descriptors such as "good," "satisfactory," or "terrible," which convey per-
sonal evaluations rather than measurable numbers. Consumer behavior is also fre -
quently described using likelihood-based expressions such as "likely," "unlikely," or
"very likely to purchase." Likewise, product or service ratings are commonly framed
in relative terms like "high," "low," or "average satisfaction." To effectively interpret
and act upon this qualitative information, such as opinions, preferences, and emo -
tional responses, there is a pressing need for methods that can process linguistic and
imprecise data in a structured and meaningful way.
To address this complexity, the paradigm of Computing with Words (CWW),
introduced by Zadeh ( 1996), offers a methodological solution. It enables the use of
words or linguistic variables instead of numbers for computing and reasoning, offer-
ing a more natural representation of human thought processes. It can also handle lin-
guistic information to model imprecise, vague, or qualitative concepts, allowing for
1 3
286

Profiling the application of the 2-tuple linguistic model in marketing: a…
decision-making (DM), inference, and control in situations where traditional quanti-
tative approaches may be inadequate or infeasible. Among CWW methodologies, the
2-tuple linguistic model developed by Herrera and Martínez (2000) stands out for its
ability to manage vague and uncertain information while minimizing information loss
and preserving interpretability. Owing to these properties, the model has experienced
substantial growth and wide applicability in decision analysis and marketing analyt-
ics, with numerous adaptations and extensions building on the original framework (Li
& Yu, 2022; Martínez & Herrera, 2012). Unlike other fuzzy approaches that may lose
information during translation, the 2-tuple model ensures that the linguistic nuances
of consumer feedback are computed without information loss (Martínez & Herrera,
2012; Petrescu & Krishen, 2024). This capability significantly advances Decision
Theory by offering a more granular approach to consensus reaching, and comple -
ments theoretical frameworks like Fuzzy Cognitive Mapping (Borrero-Domínguez &
Escobar-Rodríguez, 2023) by allowing for precise simulation of causal relationships
in uncertain environments. By feeding these processed variables into Multi-Criteria
Decision Making (MCDM) frameworks and AI algorithms, organizations can har -
monize conflicting criteria to generate robust, predictive, and prescriptive insights.
Figure 1 shows the conceptual framework of how CWW and MCDM are integrated
within the Marketing Analytics ecosystem to transform heterogeneous data into stra-
tegic decisions.
This work aims to provide a comprehensive analysis of the application of the 2-tuple
linguistic model within this marketing framework. By combining a systematic litera-
ture review and bibliometric analysis, this work contributes both breadth and depth
to understanding research trends, thematic developments, and knowledge gaps, while
identifying how this methodology bridges the gap between qualitative ambiguity and
quantitative rigor to address complex problems in supplier selection, product inno -
vation, and consumer behavior analysis. Since Scopus and Web of Science (WoS)
exhibit a high degree of overlapping content (Martín-Martín et al., 2021; Visser et
al., 2021), and WoS applies more selective journal coverage (Singh et al., 2021),
this work focuses on analyzing relevant articles from WoS published between 2000
Fig. 1 Conceptual framework of CWW and MCDM integration in marketing analytics

1 3
287

Z. Shu et al.
and 2024, while incorporating Scopus’s Field-Weighted Citation Impact (FWCI) to
evaluate both the impact of individual studies and the average influence of market -
ing-related research. FWCI is included in this work because it is a field-normalized
metric widely used to benchmark research impact fairly, regardless of differences in
entity size, age, disciplinary profile, and publication-type composition (Purkayastha
et al., 2019). Through a comprehensive analysis, the principal themes in which the
2-tuple linguistic model has been applied are used. The analysis also examines how
these themes specifically relate to marketing-related areas. Potential directions for
future research, as well as specific marketing-related areas where the 2-tuple linguis-
tic model can be further developed, are also highlighted.
The remainder of this work is organized as follows. Section 2 provides a brief
overview of concepts related to CWW and presents the fundamentals of the 2-tuple
linguistic model. Section 3 describes the methodology used to search for, identify,
select, and analyze studies on the application of the 2-tuple linguistic model in mar -
keting. Section 4 presents the results of this analysis. Finally, Sect. 5 concludes the
work, highlighting the implications for marketing analytics and potential directions
for applying the 2-tuple linguistic model in future research.
2 Theoretical framework
This section provides a brief overview of concepts related to CWW and presents the
fundamentals of the 2-tuple linguistic model.
2.1 Computing with words
In many DM problems, people often use linguistic information to express their opin-
ions or perspectives, although it is vague, uncertain, or imprecise. Conceptualized
by Zadeh (1996), CWW is a methodology in which words are used in place of num-
bers for computing and reasoning. This methodology aims to impart machines with
a capability so that they can process linguistic information seamlessly as humans do.
Linguistic information is subjective, as words can mean different things to different
people, requiring computational techniques with linguistic operators to solve prob -
lems in the CWW process.
The computational process of CWW involves three steps: translation, manipula -
tion, and retranslation (Yager, 1999), as shown in Fig. 2. The processes of translation
and retranslation play a crucial role in CWW (Yager, 2004). Translation converts
Fig. 2 Computational process of CWW, adapted from Yager (1999)

1 3
288

Profiling the application of the 2-tuple linguistic model in marketing: a…
linguistic inputs into a machine-readable format for computational processing, while
retranslation turns the results back into linguistic information that facilitates human
comprehension.
CWW serves as a computational foundation for addressing DM problems that
involve linguistic information, as it aligns closely with human reasoning, increases
the reliability and adaptability of traditional decision models, and helps resolve
uncertainties in DM processes that rely on linguistic inputs (Martínez et al., 2015).
CWW is based on the use of linguistic variables and fuzzy logic. A linguistic variable
is a variable whose values are words or phrases in a natural language (Zadeh, 1975).
Each linguistic variable can be assigned one or more linguistic terms, which are in
turn connected to numeric values through the mechanism of membership functions
(Ren et al., 2015). A linguistic variable is characterized by (X, T (X) ,U ,G ,M ),
where X is the name of the linguistic variable, T (X) is the set of linguistic terms
of X, U  is the universe of discourse, G is a syntactic rule that generates the terms in
T (X), and M  is a set of semantic rules that link each linguistic value in T (X) to a
fuzzy set. For example, when evaluating the "Restaurant Service," X is "Restaurant
Service," T (X)= {V eryP oor, P oor, Average, Good, V eryGood}, U  represents
customer satisfaction scores or service quality ratings, G defines the syntactic rules
for generating terms like "Good" or "Very Good," and M maps these terms to fuzzy
sets that represent levels of service quality.
CWW has remained a field of interest for many researchers, with applications in
risk assessment (Liu et al., 2010; Tymchuk et al., 2017), medicine (Gupta & Muhuri,
2018; Jain et al., 2017), human–computer interface (Tamir et al., 2019), natural lan-
guage processing (Huseynova, 2020), autonomous unmanned intelligent systems
(Kargin & Petrenko, 2023), industrial applications (Kali et al., 2023), and transporta-
tion problems (Pratihar et al., 2023). Gupta and Andreu-Perez (2022) classify CWW
methodologies into five types based on how they model the semantics of linguistic
information. The first type uses type-1 fuzzy sets, including methodologies like the
Extension Principle-based CWW, Augmented Extension Principle-based CWW, and
Intuitionistic Fuzzy Sets-based CWW. The second type relies on ordinal term sets,
such as Symbolic Method-based CWW and Rough Sets-based CWW methodologies.
The third type combines type-1 fuzzy sets to model the semantics of linguistic infor-
mation with ordinal term sets to perform operations on the linguistic information,
and the classic example is the 2-tuple linguistic model. The fourth type uses inter -
val type-2 fuzzy sets for modeling the semantics of linguistic information and these
semantics are represented as interval type-2 membership functions, for example, Per-
ceptual Computing. Finally, the fifth type uses general type-2 fuzzy sets to model the
semantics of linguistic information, including methodologies such as Linear General
Type-2 Fuzzy Sets-based CWW and General Type-2 Fuzzy Sets-based CWW.
This work focuses on exploring one of the most widely used methodologies in
CWW, the 2-tuple linguistic model, with its fundamentals presented in Sect. 2.2.
2.2 The 2-tuple linguistic model
Among the many CWW methodologies, the 2-tuple linguistic model, developed by
Herrera and Martínez (2000), is widely used because it is easy to implement, captures
1 3
289

Z. Shu et al.
linguistic information continuously within its domain to prevent information loss,
and maintains the interpretability of the results (Martínez et al., 2015; Mi et al., 2014;
Tai & Chen, 2009). The 2-tuple linguistic model preserves the computational process
of CWW (as shown in Fig. 1) and aims to address information loss during the fusion
of linguistic information (Herrera & Martinez, 2000). This model has been widely
used for managing linguistic information in DM problems and is the foundation for
various models in decision analysis (Martínez & Herrera, 2012). Many extensions of
the 2-tuple linguistic model enhance CWW processes in complex DM frameworks,
delivering satisfactory results in linguistic decision problems (Estrella et al., 2014).
The 2-tuple linguistic model, along with its extensions, has been applied to solve var-
ious problems, such as the evaluation of tourist services (Bueno et al., 2021; Cheng
et al., 2019), risk analysis (Wang et al., 2022), consumers’ brand selection (Giráldez-
Cru et al., 2023), customer relationship management (Shu et al., 2023a, 2025), hotel
segmentation (Shu et al., 2023b), and healthcare services (Serrano-Guerrero et al.,
2024).
The 2-tuple linguistic model represents linguistic information using a pair of lin -
guistic values called a 2-tuple value (si,α ), where si ∈ S is a linguistic term with
syntax and semantics, and α ∈ [−0.5,0.5) is a numerical value representing the sym-
bolic translation. The definition of the 2-tuple linguistic model is as follows (Herrera
& Martinez, 2000).
Definition 1 Let S = {s0, ..., sg } be a set of linguistic terms, whose cardinality is
g +1 . β ∈ [0,g ] is a value that represents the result of a symbolic aggregation opera-
tion. The function ∆ : [0 ,g ] →⟨ S⟩ = Sx[−0.5, 0.5) is used to convert β to 2-tuple
value (si,α ) as shown in Eq. (1):

∆( β)=( si,α ) , with
{
i = round(β)
α = β − i, α ∈ [−0.5, 0.5)  (1)
where round(·) is the rounding operation; si has the nearest index label to β; and
α represents a numerical value of the symbolic translation (i.e., the difference of
information between a counting of information β assessed in the interval of granu -
larity [0,g ] obtained after a symbolic aggregation operation and the closest value in
{0, ..., g} that indicates the index of the closest linguistic term in S).
The linguistic terms set may comprise three, five, seven, or more terms. How -
ever, the more terms the set contains, the more challenging it becomes for
experts to use (Wang, 2009). A five-term set is commonly used in practice. For
example, the linguistic terms used by TripAdvisor to evaluate hotel criteria are
T errible = T, P oor = P, Average = A, V eryGood = V G, Excellent = E .
Thus, S = {s0 = T,s 1 = P, s2 = A, s3 = V G, s4 = E} is a set of five linguistic
terms used by TripAdvisor, as shown in Fig. 3.
The 2-tuple linguistic model can perform transformations between 2-tuple
values and numerical values. The function ∆ is bijective; its inverse function
∆−1 : ⟨S⟩ = Sx[−0.5,0.5) → [0,g ] converts the 2-tuple value into its equivalent
numerical value as follows:
1 3
290

Profiling the application of the 2-tuple linguistic model in marketing: a…
 ∆−1 (si,α )= i + α = β (2)
Remark 1 The conversion of a linguistic term into a 2-tuple value consists of adding
a value 0 as symbolic translation, denoted as si ∈ S ⇒ (si, 0).
The comparison of 2-tuple values, the negation operator of a 2-tuple value applied to
handle inverse dimensions, and aggregation operators for 2-tuple linguistic comput -
ing are described as follows (Herrera-Viedma et al., 2004).
Definition 2 The comparison of linguistic information represented by 2-tuple val -
ues is performed according to an ordinary lexicographic order (Herrera & Martinez,
2000). Let (sI ,α 1) and (sJ ,α 2) be two 2-tuple values, the operator is generated to
compare their values as the following:
(i) If I<J , (sI ,α 1) is smaller than (sJ ,α 2).
(ii) If I = J, when:
a. α1 = α2, (sI ,α 1) and (sJ ,α 2) represent the same information.
b. α1 <α 2, (sI ,α 1) is smaller than(sJ ,α 2).
c. α1 >α 2, (sI ,α 1) is larger than (sJ ,α 2).
(iii) IfI>J , (sI ,α 1) is larger than (sJ ,α 2).
Definition 3 The negation operator of a 2-tuple value is defined as follows:
 neg((si,α )) =△ (g − ∆−1(si,α )) = ∆(g − β) (3)
where g +1  is the cardinality of S, S = {s0,...,s g }.
The 2-tuple linguistic aggregation operator involves obtaining a value that sum -
marizes a set of 2-tuple linguistic values (Estrella et al., 2014). As the 2-tuple linguis-
tic model specifies the functions ∆ and ∆−1, which convert numerical values into
2-tuple values and vice versa without any information loss, it is possible to extend
any numerical aggregation operator to handle 2-tuple values, such as the arithmetic
mean operator and the weighted average operator (Herrera-Viedma et al., 2004).
Fig. 3 The linguistic term set S used on TripAdvisor (Shu et al., 2023b)

1 3
291

Z. Shu et al.
3 Review methodology
This section details the methodology for searching, identifying, selecting, and ana -
lyzing studies on the application of the 2-tuple linguistic model in marketing, with an
overview of the process presented in Fig. 4.
Section 3.1 defines specific research objectives that align with the overarching
aim introduced in Sect. 1, ensuring the effective fulfillment of this work. Section 3.2
presents the selection of an appropriate database for the literature search and the
development of a comprehensive search strategy to identify relevant studies for anal-
ysis. Section 3.3 shows the establishment of explicit inclusion and exclusion criteria
to ensure the relevance and validity of the selected papers. These selected studies
then form the basis for the bibliometric analysis and systematic literature review
discussed in Sect. 3.4. Section 3.4 presents two complementary analyses to provide a
comprehensive understanding of the application of the 2-tuple linguistic model in the
field of marketing. A bibliometric analysis is conducted using SciMAT (Cobo et al.,
2012), focusing on keyword co-occurrence to identify thematic clusters. These are
visualized through a strategic diagram that outlines the thematic structure of the field
over the entire study period. Meanwhile, a systematic literature review is performed
through full-text content analysis of the selected papers. By integrating the results
from both methods, the study provides a comprehensive view of the research field.
The detailed analysis and interpretation of the findings are presented in Sect. 4.
Fig. 4 Research methodology, adapted from Cobo et al. (2012) and (Page et al., 2020)

1 3
292

Profiling the application of the 2-tuple linguistic model in marketing: a…
3.1 Definition of research objectives
This step involves defining specific research objectives to ensure alignment with the
overarching aim outlined in Sect. 1: providing a comprehensive understanding of
how the 2-tuple linguistic model is applied in marketing through a combination of
systematic literature review and bibliometric analysis.
To achieve this comprehensive understanding, the following specific research
objectives (ROs) have been defined:
 ● RO1: To identify key research themes in the application of the 2-tuple linguistic
model in marketing and determine their importance through a strategic diagram
analysis.
 ● RO2: To determine the marketing-related areas where the 2-tuple linguistic mod-
el has been predominantly applied.
 ● RO3: To assess the research impact of the 2-tuple linguistic model in these areas,
measured by FWCI.
 ● RO4: To identify emerging or underexplored marketing-related areas where the
2-tuple linguistic model could provide valuable contributions in the future.
3.2 Literature databases selection and search strategy
This step involves selecting an appropriate database for the literature search and
developing a comprehensive search strategy to identify relevant studies for the
analysis.
Commonly accessible data sources include WoS and Scopus. This work selected
WoS as the primary database because of its comprehensive coverage of high-quality,
peer-reviewed journals across a wide range of disciplines. Although Scopus is also
a valuable database, it has a high degree of overlap with WoS (Martín-Martín et
al., 2021; Visser et al., 2021), which would result in numerous duplicate records if
both databases were used for the same topic. To avoid unnecessary duplication of
records, WoS was used to ensure a more streamlined and focused literature search on
articles related to the application of the 2-tuple linguistic model in marketing between
2000 and 2024. Scopus was used solely to complement the article’s FWCI, a field-
normalized metric widely used to benchmark research impact fairly, regardless of
differences in entity size, age, disciplinary profile, or publication-type composition
(Purkayastha et al., 2019). It builds on the field-normalization approaches proposed
by Lundberg (2007) and Waltman et al. (2011) by accounting for differences across
document types, publication years, and research fields. FWCI applies harmonic rather
than arithmetic averaging to calculate the expected number of citations for publica -
tions assigned to multiple fields; the detailed calculation procedure can be consulted
in Purkayastha et al. (2019).
In accordance with the established objectives, a literature search was conducted at
the end of January 2025 using a Topic Search (TS) with the following terms: "2-tuple
linguistic model," "marketing," and their corresponding abbreviations (e.g., "2TL"
for "2-tuple linguistic model"), as well as related synonyms (e.g., "advertising,"
"branding," "commercialization," "merchandising," "sales," "product," "promotion"
1 3
293

Z. Shu et al.
for "marketing"). In WoS, a TS retrieves records where the specified terms appear in
the Title, Abstract, or Author Keywords, providing a broader search than limiting it to
the title or author keywords alone. The query used in WoS combined these terms with
Boolean operators—OR for synonyms and abbreviations, AND for combining con -
cepts—to ensure comprehensive coverage, that is, (TS = ("2-tuple linguistic model"
OR 2TL) AND TS = (marketing OR advertising OR branding OR commercialization
OR merchandising …)), with the full query also including other relevant synonyms
and abbreviations related to marketing.
The publication period was limited to articles published from 2000 to 2024.
The preliminary search resulted in 165 papers. FWCI values for each article were
retrieved manually from Scopus after the articles were collected from WoS. Articles
were matched between WoS and Scopus using the Digital Object Identifier (DOI) to
ensure accurate correspondence. For articles indexed in WoS but not found in Sco -
pus, or for articles whose FWCI was not yet available in Scopus, the FWCI values
were recorded as “NA”.
3.3 Establishment of selection criteria and study filtering
Establishing explicit inclusion and exclusion criteria for selecting studies is impor -
tant. Figure 5 shows the process, adapted from the Preferred Reporting Items for
Systematic reviews and Meta-Analyses (PRISMA) framework (Page et al., 2020),
used to identify relevant and valid papers based on the established inclusion and
exclusion criteria.
Duplicated articles that may appear for various reasons (e.g., corrections or differ-
ent versions) in WoS were removed. Conference papers were also excluded, as they
Fig. 5 Flow diagram of the study selection process, adapted from Page et al. (2020)

1 3
294

Profiling the application of the 2-tuple linguistic model in marketing: a…
are usually not considered peer-reviewed articles. Titles and abstracts were reviewed
to exclude irrelevant papers, such as those unrelated to the 2-tuple linguistic model or
marketing. Only journal articles with full papers available were included to ensure a
comprehensive understanding of the content, resulting in a final sample of 90 articles,
published between 2008 and 2024.
3.4 Analysis of the selected studies
This step consists of two complementary approaches: a bibliometric analysis to iden-
tify thematic clusters based on the co-occurrence of keywords of selected papers (see
Sect.  3.3.1), and a systematic literature review featuring an in-depth full-text analysis
to extract content-driven perspectives (see Sect.  3.3.2).
3.4.1 Bibliometric analysis
Bibliometric analysis is a quantitative method that integrates mathematical and statis-
tical techniques. This work conducts a bibliometric analysis, focusing on construct -
ing strategic diagrams based on the co-occurrence of keywords from the articles
selected in the previous step. This helps identify the principal themes in which the
2-tuple linguistic model has been applied.
SciMAT (Cobo et al., 2012), a useful tool for science mapping analysis, is
employed to generate strategic diagrams. This tool maps the thematic structure of the
research field over the designated study period by identifying thematic clusters based
on the co-occurrence of keywords from the selected publications. These themes are
then visualized through a strategic diagram that highlights the importance of each
cluster in the co-occurrence analysis. In this work, keyword co-occurrence was nor -
malized using the equivalence index in SciMAT. Clustering was performed using
the simple centers algorithm with the default co-occurrence threshold defined in Sci-
MAT, a minimum cluster size of 3 keywords, and a maximum cluster size of 12 key-
words. Keywords were extracted from the author, source, and added terms, and then
filtered according to frequency criteria before analysis. The thematic evolution was
assessed using the inclusion index, while theme overlap was measured using the Jac-
card index. Figure 6 illustrates the strategic diagram, in which themes are positioned
according to their centrality and density, enabling the identification of four thematic
categories.
As shown in Fig. 6, the diagram is based on two measures: centrality and den -
sity. Centrality, represented on the x-axis, indicates the degree to which the different
themes—keyword clusters—are related to each other, while density, shown on the
y-axis, reflects the extent to which the themes are well developed (Muñoz-Leiva et
al., 2022). And the size of the nodes corresponds to the number of publications. The
strategic diagram is divided into four quadrants, each offering a different interpreta -
tion as follows (Cobo et al., 2012):
 ● Motor themes (quadrant I): these themes exhibit both high centrality and high
density, indicating they are well-developed and play a central role in the research
field.
1 3
295

Z. Shu et al.
 ● Highly developed and isolated themes (quadrant II): these themes have high den-
sity but low centrality, indicating they are well-developed internally yet have lim-
ited connections to other themes, making them isolated.
 ● Emerging or declining themes (quadrant III): these themes show low centrality
and low density, indicating they are either emerging or declining in importance
within the field.
 ● Basic and transversal themes (quadrant IV): these themes have high centrality
but low density, suggesting they are important for connecting different areas of
research but are not yet well developed.
Based on the strategic diagram, the principal themes where the 2-tuple linguistic
model has been applied can be identified. The related results are shown and explained
in detail in Sect. 4.1.
3.4.2 Systematic literature review
A systematic literature review is a structured method involving the comprehensive
identification, evaluation, and synthesis of existing studies. As its name suggests, it
is a systematic procedure that includes the following stages: defining clear research
questions, conducting a thorough search across selected literature databases, estab -
lishing explicit inclusion and exclusion criteria, selecting relevant studies based on
predefined criteria, critically appraising the quality of the selected studies, extracting
key data, and synthesizing the findings to draw meaningful conclusions. This struc -
tured approach ensures transparency and provides a reliable overview of the avail -
able evidence on a given topic.
In this work, a systematic literature review is conducted by performing full-text
content analysis on the selected papers to uncover the specific application areas of the
2-tuple linguistic model in marketing. These areas include a wide range of market -
ing topics such as product development and innovation, pricing strategies, supplier
Fig. 6 Strategic diagram (Cobo et al.,
2012; Muñoz-Leiva et al., 2022)

1 3
296

Profiling the application of the 2-tuple linguistic model in marketing: a…
evaluation and management, service quality assessment and improvement, customer
relationship management, brand management, and other critical aspects of marketing
operations and strategic DM. The related results are shown and explained in detail
in Sect. 4.2.
4 Results analysis and interpretation
This section presents the results of the bibliometric analysis (see Sect. 4.1) and sys-
tematic literature review (see Sect. 4.2) on studies related to the application of the
2-tuple linguistic model in marketing. To enhance the visualization of the analysis
results, this work integrates the outcomes of both methods into layered graphs (see
Sect. 4.3). Moreover, the importance of each application area within its respective
theme is evaluated using the FWCI indicator from Scopus, which serves as a more
normalized alternative to mere citation counts.
4.1 Bibliometric analysis
This section presents the results of the bibliometric analysis from the SciMAT report,
with a primary focus on the strategic diagram illustrating the quadrant to which
each theme belongs. Figure 7 presents the strategic diagram for the full study period
(2008–2024) without time slicing, comprising five thematic clusters.
As shown in Fig. 7, alongside the cluster "Multiple Attribute Decision Making
(MADM)", "Multiple Attribute Group Decision Making (MAGDM)" also emerges
as a motor theme due to its high centrality and density. These themes play a central
role in the research field, being both internally cohesive and extensively connected
with the rest of the domain. MAGDM is closely related to MADM, as it extends the
analytical structure of MADM to contexts involving multiple decision-makers by
integrating multi-attribute evaluation with the collaborative processes characteristic
of Group Decision Making (GDM). The prominence of MAGDM can be attributed
to the growing emphasis on collective decision-making in marketing and manage -
ment, where preferences from multiple stakeholders, experts, or consumers must be
aggregated under uncertainty. This trend aligns with the rise of participatory deci -
sion-making environments, consensus-reaching models, and group-based evaluation
mechanisms applied in areas such as supplier management and customer experience
management.
Interestingly, within the articles analyzed, "GDM" itself is classified as a basic
and transversal theme, marked by high centrality but low density. This indicates that,
although the theme "GDM" plays a key role in connecting various research areas
(e.g., with "MADM"), it remains underdeveloped in terms of internal cohesion and
conceptual maturity. Its lower density suggests that it functions more as a set of foun-
dational concepts.
Moreover, the theme "MCDM" is classified as highly developed but isolated, char-
acterized by high density and low centrality. This suggests that, despite its broader
scope compared to MADM, within the articles analyzed in this work, MCDM is well-
developed internally but has less extensive connections to other themes.
1 3
297

Z. Shu et al.
The fifth theme, "Supplier Selection", is categorized as an emerging or declining
theme due to its low centrality and low density. This suggests that, based on the ana-
lyzed literature, it has fewer connections to the core of the research field and a less
consolidated internal development. However, it may still represent an emerging topic
with potential for future growth. Unlike the other four themes, "Supplier Selection"
is better understood as an application area, as it focuses on the practical implementa-
tion of DM methods rather than contributing to the development of core theoretical
frameworks.
Notably, a closer examination of the SciMAT reports for each theme reveals that
some articles are associated with more than one cluster. This overlap underscores
the need for a deeper understanding of the relationships among MCDM, MADM,
MAGDM, and GDM—all of which solve DM problems. Clarifying how these frame-
works differ and interrelate is essential for accurately assigning each article to its
most appropriate thematic cluster. A brief explanation of the relationships among
these concepts is provided below (see also Fig. 8):
Fig. 7 Strategic diagram for the period from 2008 to 2024

1 3
298

Profiling the application of the 2-tuple linguistic model in marketing: a…
 ● MCDM: a discipline that deals with decisions involving the choice of the best
alternative from several potential candidates, subject to several criteria or attrib -
utes that may be concrete or vague (Uzun et al., 2021). It includes both individual
and group DM settings and serves as the foundational field for more specific
approaches.
 ● MADM: a type of MCDM that is applied to solve problems involving discrete
decision variables and limited DM schemes (Feng et al., 2022).
 ● GDM: a process of making decisions within a group setting, utilizing a larger
pool of expertise and viewpoints to reach conclusions (Hogg, 2001). It involves
considering various perspectives and potential biases that may impact the final
decision, and it may or may not involve multiple criteria.
 ● MAGDM: an intersection of MADM and GDM, where a group of decision-mak-
ers evaluates alternatives based on multiple attributes.
 ● Multi-Criteria Group Decision Making (MCGDM): an intersection of MCDM
and GDM, where a group of decision-makers evaluates alternatives based on
multiple criteria. It represents a broader category than MAGDM, as it integrates
the full range of MCDM techniques within group settings, potentially encom -
passing both attribute-based (discrete) and criteria-based (continuous or hybrid)
approaches. Although this type is not shown in Fig. 7, articles that fall under both
MCDM and GDM simultaneously should be considered part of this category.
Based on the previous explanation of different DM themes, if an article falls under
two or more cluster themes simultaneously, it will be reassigned to a more specific
theme. For instance, an article categorized under both MCDM and GDM will be
reclassified as MCGDM; if it belongs to both MADM and GDM, it will be assigned
to MAGDM, and so on. The updated themes for each article can be found in Sect. 4.3.
Fig. 8 Relationship of DM themes
1 3
299

Z. Shu et al.
4.2 Systematic literature review
This section presents the results of the systematic literature review, which comple -
ments the findings of the bibliometric analysis by offering deeper insights into the
specific application areas of the 2-tuple linguistic model in marketing. Table 1 pres-
Table 1 Marketing-related areas and associated articles
Areas related to
marketing
Article IDs [References]
Blockchain 77 (Khan & Ahmad, 2023)
Brand Management 12 (Cid-López et al., 2015a); 13 (Cid-López et al., 2015b); 19 (Li et al.,
2017); 20 (Carrasco et al., 2017); 34 (Zhang et al., 2019); 47 (Giráldez-Cru et
al., 2021); 61 (Zhang et al., 2023); 64 (Li, 2023); 65 (Sun et al., 2023)
Business Intelligence 62 (Chen, 2023a); 63 (Akram et al., 2023a)
Business performance
evaluation
53 (Liu, 2022)
Consumer Behavior 38 (Giráldez-Cru et al., 2020); 44 (Mandal et al., 2021); 59 (Forghani et al.,
2023); 69 (Giráldez-Cru et al., 2023)
Corporate financial
management
76 (Mu, 2024)
Corporate Social Re-
sponsibility assessment
8 (Costa & Menichini, 2013)
Customer Experience
Management
41 (Bueno et al., 2021); 57 (Marín Díaz & Carrasco González, 2023); 58
(Naz et al., 2023a)
Customer segmentation 42 (Martínez et al., 2021); 48 (Marín Díaz et al., 2021); 51 (Shu et al., 2023b)
Digital Marketing 10 (Mi et al., 2014); 49 (Forghani et al., 2022); 52 (Naz et al., 2023b); 67
(Marín Díaz et al., 2023); 72 (Shu et al., 2024); 89 (Wu et al., 2024)
Digital Transformation 60 (Marín Díaz & Galdón Salvador, 2023)
E-commerce 73 (Mao, 2024); 74 (Yang et al., 2024a); 75 (Xu, 2024)
Internal Marketing 3 (Fan et al., 2009a); 18 (Bao et al., 2017)
Knowledge
Management
2 (Fan et al., 2009b); 4 (Tai & Chen, 2009)
Lean Management 15 (Wu et al., 2016)
Product Development
and Innovation
5 (Wang, 2009); 7 (Li, 2012); 9 (Wang, 2013); 16 (Wang et al., 2016); 21
(Liu et al., 2017); 23 (Liu et al., 2018); 24 (Cid-López et al., 2018); 25 (Mi et
al., 2018); 27 (Dursun & Arslan, 2018); 29 (Setti et al., 2019); 36 (Yuan et al.,
2020); 54 (Geng et al., 2023); 55 (Chen et al., 2023); 68 (Zhong et al., 2023);
78 (Alamoodi et al., 2024); 86 (Zhang et al., 2024); 90 (Yang et al., 2024b)
Resource management
and Investment
35 (Wang et al., 2019a); 50 (Wang, 2021)
Risk management 14 (Xing & Xing, 2016); 45 (Choudhary et al., 2021); 81 (Naz et al., 2024);
85 (Chang et al., 2024)
Service Quality 70 (Akram et al., 2023b)
Supplier management 1 (Wang, 2008); 6 (Dhouib & Elloumi, 2011); 11 (Crispim et al., 2015); 17
(Santos et al., 2017); 22 (Wan et al., 2017); 26 (Deng et al., 2018); 28 (Cheng
et al., 2019); 30 (Sohaib et al., 2019); 31 (Wang et al., 2019b); 32 (Wei et al.,
2019); 33 (Wang et al., 2019c); 37 (Wen et al., 2020); 39 (Wei et al., 2020);
40 (Zhang et al., 2020); 43 (Lizarelli et al., 2021); 56 (Chen, 2023b); 66
(Chung et al., 2023); 71 (Büyüközkan et al., 2023); 82 (Alballa et al., 2024);
84 (Galdón Salvador & Marín Díaz, 2024); 87 (Ahmad et al., 2024)
Sustainable Marketing 46 (Fan et al., 2021); 79 (Chen et al., 2024); 80 (Naz et al., 2023c); 83 (Ali et
al., 2024); 88 (Mao et al., 2024)
1 3
300

Profiling the application of the 2-tuple linguistic model in marketing: a…
ents the marketing-related areas identified in this work through a systematic literature
review of 90 articles, along with their corresponding article IDs.
As shown in Table 1, "Supplier management" and "Product Development and
Innovation" are two prominent marketing-related areas where the 2-tuple linguistic
model has been widely applied. Many studies have used this model to support sup -
plier selection and evaluation processes, as well as to optimize supply chain manage-
ment. "Supplier Selection," previously identified as an emerging or declining theme
in the bibliometric analysis, can, through the systematic literature review, be better
understood as an application area that forms part of supplier management. Regarding
product development and innovation, the 2-tuple linguistic model has been employed
to assist in idea evaluation, project selection, and DM under uncertainty, helping
organizations prioritize initiatives and allocate resources more effectively. These
applications demonstrate the model’s utility in various contexts of marketing.
4.3 Integrated findings
This section presents the combined results of the systematic literature review and
bibliometric analysis. Figure 9 shows a layered network graph that integrates three
types of information:
 ● thematic layers (large colored circles): are derived from the bibliometric analysis,
with different colors used to distinguish them. For example, "Other" represents
themes not directly related to DM methodologies identified through the biblio -
metric analysis (see also Fig. 8).
 ● marketing-related areas layers (medium-sized orange circles): are identified
through the systematic literature review (e.g., "Supplier management," "Product
Development and Innovation," "Digital Marketing," "Brand Management"; see
also Table 1). The size of each orange node reflects the number of articles associ-
ated with that application area.
 ● article layer (small numbered nodes): display article IDs (see also Table 1) and
indicate the number of articles linked to each application area within the corre -
sponding theme.
As shown in Fig. 9, MAGDM, one of the high-density clusters identified in Fig. 7,
emerges as the most dominant theme. It exhibits strong connections to several mar -
keting-related areas, including "Supplier management," "Product Development and
Innovation," "Customer Experience Management," and "Risk Management". For
instance, the connection between MAGDM and Customer Experience Manage -
ment research reflects the growing use of group-based preference modeling to cap -
ture heterogeneous consumer perceptions. From a theoretical perspective, MAGDM
provides a structured framework for incorporating multiple criteria and stakeholder
perspectives, with significant implications for consumer behavior modeling, service
design, and strategic marketing decision-making. Methodologically, the integration
of 2-tuple linguistic models within MAGDM further enhances its utility by improv -
ing the aggregation of heterogeneous preferences, capturing nuanced perceptions
of product attributes, and supporting scenario-based decision-making, ultimately
1 3
301

Z. Shu et al.
enabling firms to develop more tailored offerings and refine marketing strategies
under uncertainty.
MCDM also plays an important role, being linked to areas like "Digital Market -
ing," "Corporate Social Responsibility assessment," and "Customer segmentation,"
highlighting and underscoring innovation opportunities in marketing strategy, data-
driven decision-making, and personalized customer experiences. Figure 10 presents
a focused zoom on the MAGDM and MCDM themes to highlight their links with
different marketing application areas. Moreover, GDM, MCGDM, and MADM
exhibit fewer but still noticeable connections to marketing-related areas. In contrast,
the "Other" theme has only a single connection, linking "Supplier management" to
paper ID 11.
This work also investigates the importance of each application area within its
respective themes, as it is evaluated using the FWCI indicator from Scopus, which
serves as a more normalized alternative to mere citation counts. Figure 11 is a bubble
Fig. 9 Layered network graph of the combined results

1 3
302

Profiling the application of the 2-tuple linguistic model in marketing: a…
Fig. 10 Subgraphs of the layered network graph: MAGDM (top) and MCDM (bottom)

1 3
303

Z. Shu et al.
chart where each point represents the FWCI indicator for each marketing-related area
within each theme. The size of each bubble reflects the average FWCI for the papers
related to that area, with larger bubbles indicating higher FWCI values.
As shown in Fig. 11, in both MADM and GDM themes, the marketing-related
area "Supplier management" has higher average FWCI scores, suggesting a well-
established or mature research cluster. In contrast, areas such as "Digital Marketing"
(FWCI = 0.4 in GDM) and "Brand Management" (FWCI = 0.26 in MADM, although
FWCI = 3.75 in GDM) have average FWCI scores below 1 (i.e., less than the average
for similar publications), indicating less developed or emerging areas within these
themes. Within the MAGDM theme, "Knowledge Management" (FWCI = 6.11) and
"Business Intelligence" (FWCI = 4.26) show notably high FWCI scores, reflecting
mature and highly impactful research. Conversely, "Corporate Financial Manage -
ment" has an FWCI of 0, suggesting this area lacks sufficient citation data, suggesting
minimal research influence or visibility in the field.
In the MCDM theme, "Corporate Social Responsibility assessment" (FWCI = 7.28)
and "Digital Marketing" (FWCI = 4.31) exhibit higher citation impact, whereas "Risk
Management" shows a lower score (FWCI = 0.18). For the MCGDM theme, "Knowl-
edge Management" (FWCI = 6.53) and "Supplier Management" (FWCI = 4.3) stand
out with higher average FWCI scores, indicating well-established areas. Especially
compared to the other four DM themes (i.e., excluding the "Other" theme), MCGDM
is the only theme where all marketing-related areas have an average FWCI score
above 1, reflecting a consistently mature research cluster with strong impact.
Finally, the "Other" theme includes only the area of "Supplier management," with
publications in this area cited 22% more than the average for similar works. However,
when considered alongside Fig. 9, it can be concluded that despite having an FWCI
greater than 1, this theme should be viewed more as an application area of marketing
rather than as a standalone theme, as it does not have strong connections with other
areas, especially when compared to more interconnected themes like MAGDM or
MCDM.
Fig. 11 FWCI average of each marketing-related area within each theme

1 3
304

Profiling the application of the 2-tuple linguistic model in marketing: a…
5 Conclusions
This work provides a comprehensive understanding of how the 2-tuple linguistic
model is applied in marketing by combining bibliometric analysis and a systematic
literature review. This comprehensive analysis helps to identify themes that may
be overlooked by bibliometric analysis alone due to keyword limitations or index -
ing inconsistencies. Furthermore, it bridges the marketing-related areas identified
through the systematic literature review with those revealed by bibliometric analy -
sis at the article level. This enhances analytical rigor by leveraging complementary
strengths: bibliometric analysis quantitatively examines large volumes of scholarly
publications to uncover trends and research themes, while the systematic review
allows for a detailed examination of each article to verify and refine thematic clas -
sifications. Another contribution of this work is the use of the FWCI indicator as a
normalized alternative to raw citation counts, allowing for more accurate compari -
sons of research impact in the field.
This work starts with a concise overview of the main CWW concepts and explains
the basics and practical uses of the 2-tuple linguistic model. It then analyzes articles
published between 2000 and 2024 from the WoS database (90 out of 165 publica -
tions) and incorporates Scopus-derived FWCI metrics to evaluate both the impact of
individual articles and the average influence of research in marketing-related areas.
The results of the bibliometric analysis, generated using SciMAT, focus primarily
on the strategic diagram to identify the main themes in which the 2-tuple linguistic
model has been applied. The findings show that the principal themes in which the
2-tuple linguistic model is applied are largely related to DM problems (e.g., MADM,
MAGDM, MCDM, etc.). Among these, MAGDM stands out as the most prominent
theme, not only because it is classified as a motor theme, but also due to its strong
connections with various marketing-related areas.
According to the systematic literature review, the most prominent marketing-
related areas where the 2-tuple linguistic model has been widely applied are "Supplier
management" and "Product Development and Innovation". In terms of the impor -
tance of each application area within its respective theme, measured by the average
FWCI score of each marketing-related area, MCGDM stands out as the only DM
theme where all associated areas have an average FWCI score above 1, indicating a
consistently strong research impact. High-impact marketing-related areas—identi -
fied by an average FWCI score of 4 or higher, include "Supplier management," "Dig-
ital Marketing," "Business Intelligence," "Product Development and Innovation,"
"Knowledge Management," and "Corporate Social Responsibility assessment." This
demonstrates the well-established application of the 2-tuple linguistic model in these
areas, along with a high level of research impact in marketing. Deepening the applica-
tion of the 2-tuple linguistic model in these areas can further enhance DM processes
in marketing contexts. A prime example is supplier management, where the 2-tuple
linguistic model’s integration with MADM or GDM methods has demonstrated a
strong impact and practical utility in handling the linguistic information provided by
decision makers, such as experts. On the other hand, lower-impact marketing-related
areas (e.g., Digital Transformation, Consumer Behavior, etc.) may represent potential
1 3
305

Z. Shu et al.
opportunities where the 2-tuple linguistic model could be applied to solve various
DM problems in marketing.
To sum up, the objectives of this work have been successfully achieved. The
insights presented highlight the current applications of the 2-tuple linguistic model in
marketing and point to valuable opportunities for expanding its use across the field.
However, several limitations should be acknowledged. This work relies primarily
on WoS, which may introduce database bias, as WoS selectively indexes journals
and may underrepresent certain fields or regions. We included only full-text jour -
nal articles, excluding conference papers and other publication types, which may
limit the scope of our analysis. Moreover, the FWCI retrieved from Scopus has some
constraints. FWCI is calculated only for publications indexed in Scopus, so articles
not included in Scopus are excluded. It can also be strongly influenced by outlier
publications, which may skew the interpretation of impact metrics. These limitations
could be addressed in future work by using multiple databases, including additional
publication types, or exploring more metrics less sensitive to outliers, providing a
more comprehensive view of the field.
Acknowledgements The authors gratefully acknowledge the support provided by the project -
PID2024-155289NB-I00 funded by MICIU/AEI/10.13039/501100011033 and ERDF/EU. They also wish
to thank Universidad Complutense de Madrid, ENAE Business School, and Universidad Rey Juan Carlos
for their continued support.
Author contributions Ziwei Shu conducts Conceptualization, Data Curation, Methodology, Software,
Validation, Funding acquisition, Formal analysis, Investigation, Writing (Original Draft, Review and
editing), and Visualization. José Javier Galán Hernández conducts Methodology, Software, Resources,
Writing (Review and editing), Supervision, and Funding acquisition. Álvaro Carrasco-Aguilar conducts
Writing (Review and editing), Investigation, Software, Visualization and Validation. All authors read and
approved the final manuscript.
Funding Open Access funding provided thanks to the CRUE-CSIC agreement with Springer
Nature. This work was supported by the project PID2024-155289NB-I00 funded by MICIU/
AEI/10.13039/501100011033 and ERDF/EU. This work was also supported by ENAE Business School,
Center of Excellence in Digitalization (grant DIGIT–032026–JJGH).
Data availability The dataset supporting the analyses presented in this paper, as well as the corresponding
SciMAT project file, are available from the corresponding author upon request.
Declarations
Competing interests The authors declare no competing interests.
Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative
Commons licence, and indicate if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line
to the material. If material is not included in the article’s Creative Commons licence and your intended use
is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission
directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o n s . o r g / l i c e n
s e s / b y / 4 . 0 /     .
1 3
306

Profiling the application of the 2-tuple linguistic model in marketing: a…
References
Ahmad, U., Khan, A., Shhazadi, S. (2024). Extended ELECTRE I method for decision-making based on
2-tuple linguistic q-rung picture fuzzy sets. Soft Computing.
Akram, M., Bibi, R., & Deveci, M. (2023a). An outranking approach with 2-tuple linguistic fermatean
fuzzy sets for multi-attribute group decision-making. Engineering Applications of Artificial Intel -
ligence, 121, Article 105992.
Akram, M., Naz, S., Edalatpanah, S. A., & Samreen, S. (2023b). A hybrid decision-making framework
under 2-tuple linguistic complex q-rung orthopair fuzzy Hamy mean aggregation operators. Compu-
tational and Applied Mathematics, 42(3), Article 118.
Alamoodi, A. H., Albahri, O. S., Deveci, M., Albahri, A. S., Yussof, S., Dinçer, H., Yüksel, S., & Mohamad
Sharaf, I. (2024). Selection of electric bus models using 2-tuple linguistic T-spherical fuzzy-based
decision-making model. Expert Systems with Applications, 249, Article 123498.
Alballa, T., Alamer, A., Nasir, K., Yousaf, A., Abdualziz Alhabeeb, S., & Abd El-Wahed Khalifa, H.
(2024). A multiple attribute group decision making model based on 2-tuple linguistic pythagorean
fuzzy dombi aggregation operators for optimal selection of potential global suppliers. Heliyon,
10(14), Article e34570.
Ali, Z., Hayat, K., & Pamucar, D. (2024). Analysis of Hamacher power aggregation operators for circular
complex p, q-quasirung orthopair fuzzy 2-tuple linguistic sets and their application in green industry
development. Heliyon, 10(17), Article e36799.
Bao, J., Johansson, J., & Zhang, J. (2017). Comprehensive evaluation on employee satisfaction of mine
occupational health and safety management system based on improved AHP and 2-tuple linguistic
information. Sustainability, 9(1), 133.
Basu, R., Lim, W. M., Kumar, A., & Kumar, S. (2023). Marketing analytics: the bridge between customer
psychology and marketing decision‐making. Psychology & Marketing, 40(12), 2588–2611.
Borrero-Domínguez, C., & Escobar-Rodríguez, T. (2023). Decision support systems in crowdfunding: a
fuzzy cognitive maps (FCM) approach. Decision Support Systems, 173, Article 114000.
Bueno, I., Carrasco, R. A., Porcel, C., Kou, G., & Herrera-Viedma, E. (2021). A linguistic multi-criteria
decision making methodology for the evaluation of tourist services considering customer opinion
value. Applied Soft Computing, 101, Article 107045.
Büyüközkan, G., Uztürk, D., & Maden, A. (2023). Influential factor analysis for cloud computing technol-
ogy service provider. Technological Forecasting and Social Change, 192, Article 122531.
Carrasco, R. A., Sánchez-Fernández, J., Muñoz-Leiva, F., Francisca Blasco, M., & Herrera-Viedma, E.
(2017). Evaluation of the hotels e-services quality under the user’s experience. Soft Computing,
21(4), 995–1011.
Chang, K.-H., Chen, Y .-J., & Liao, C.-C. (2024). A novel improved FMEA method using data envelop-
ment analysis method and 2-tuple fuzzy linguistic model. Annals of Operations Research,  341(1),
485–507.
Chartered Institute of Marketing. (2015). Marketing and the 7Ps: A brief summary of marketing and how
it work. CIM. https://www.cim.co.uk/media/4772/7ps.pdf
Cheng, T.-E., Wang, J., Zhang, D.-J., & Cao, M.-M. (2019). TODIM method for evaluating the service
quality of boutique tourist scenic spot with 2-tuple linguistic information. Journal of Intelligent &
Fuzzy Systems, 37(2), 2075–2083.
Chen, H. (2023a). A multi-attribute decision-making framework for enterprise competitive intelligence
system evaluation with 2-tuple linguistic neutrosophic information. Journal of Intelligent & Fuzzy
Systems, 45(4), 5955–5970.
Chen, S., Zhang, Y ., & Gong, J. (2023). A systematic decision-making approach for quality function
deployment based on hesitant fuzzy linguistic term sets. Applied Sciences, 13(24), 13104.
Chen, X. (2023b). An integrated fuzzy group decision-making model for construction enterprise contractor
selection based on EDAS method and information entropy. Journal of Intelligent & Fuzzy Systems,
45(2), 3233–3245.
Chen, X., Yang, S., Hu, D., & Li, X. (2024). Sustainable mining method selection by a multi-stakeholder
collaborative multi-attribute group decision-making method. Resources Policy, 92, Article 105043.
Choudhary, D., Choudhary, A., Shankar, R., Hicks, C. (2021). Evaluating the risk exposure of sustainable
freight transportation: A two-phase solution approach. Annals of Operations Research.
1 3
307

Z. Shu et al.
Chung, H.-Y ., Chang, K.-H., & Yao, J.-C. (2023). Addressing environmental protection supplier selection
issues in a fuzzy information environment using a novel soft fuzzy AHP–TOPSIS method. Systems,
11(6), Article 293.
Cid-López, A., Hornos, M. J., Carrasco-Gónzález, R. A., & Herrera-Viedma, E. (2018). Prioritization of
the launch of ICT products and services through linguistic multi-criteria decision-making. Techno-
logical and Economic Development of Economy, 24(3), 1231–1257.
Cid-López, A., Hornos, M. J., Carrasco, R. A., & Herrera-Viedma, E. (2015a). SICTQUAL: A fuzzy lin -
guistic multi-criteria model to assess the quality of service in the ICT sector from the user perspec -
tive. Applied Soft Computing, 37, 897–910.
Cid-López, A., Hornos, M. J., Carrasco, R. A., & Herrera-Viedma, E. (2015b). A hybrid model for deci -
sion-making in the information and communications technology sector. Technological and Economic
Development of Economy, 21(5), 720–737.
Cobo, M., López-Herrera, A., Herrera-Viedma, E., & Herrera, F. (2012). SciMAT: a new science mapping
analysis software tool. Journal of the American Society for Information Science and Technology,
63(8), 1609–1630.
Costa, R., & Menichini, T. (2013). A multidimensional approach for CSR assessment: the importance of
the stakeholder perception. Expert Systems with Applications, 40(1), 150–161.
Crispim, J., Rego, N., & Pinho de Sousa, J. (2015). Stochastic partner selection for virtual enterprises: a
chance-constrained approach. International Journal of Production Research, 53(12), 3661–3677.
Deng, X., Wang, J., Wei, G., & Lu, M. (2018). Models for multiple attribute decision making with some
2-tuple linguistic pythagorean fuzzy Hamy mean operators. Mathematics, 6(11), 236.
Dhouib, D., & Elloumi, S. (2011). A new multi-criteria approach dealing with dependent and hetero -
geneous criteria for end-of-life product strategy. Applied Mathematics and Computation,  218(5),
1668–1681.
Dursun, M., & Arslan, Ö. (2018). An integrated decision framework for material selection procedure: a
case study in a detergent manufacturer. Symmetry, 10(11), 657.
Estrella, F. J., Espinilla, M., Herrera, F., & Martínez, L. (2014). FLINTSTONES: A fuzzy linguistic deci-
sion tools enhancement suite based on the 2-tuple linguistic model and extensions. Information Sci-
ences, 280, 152–170.
Fan, J., Yan, F., & Wu, M. (2021). GLDS method for multiple attribute group decision making under 2-tuple
linguistic neutrosophic environment. Journal of Intelligent & Fuzzy Systems, 40(6), 11523–11538.
Fan, Z.-P., Feng, B., Sun, Y .-H., & Ou, W. (2009b). Evaluating knowledge management capability of orga-
nizations: a fuzzy linguistic method. Expert Systems with Applications, 36(2, Part 2), 3346–3354.
Fan, Z.-P., Feng, B., & Suo, W.-L. (2009a). A fuzzy linguistic method for evaluating collaboration sat -
isfaction of NPD team using mutual-evaluation information. International Journal of Production
Economics, 122(2), 547–557.
Feng, J., Yan, Y ., Huang, M., Du, Y ., Lu, Z., & Li, B. (2022). A study on the multi-attribute decision theory
and methods. Procedia Computer Science, 214, 544–551.
Forghani, E., Sheikh, R., Hosseini, S. M. H., & Sana, S. S. (2022). The impact of digital marketing strate-
gies on customer’s buying behavior in online shopping using the rough set theory. International
Journal of System Assurance Engineering and Management, 13(2), 625–640.
Forghani, E., Sheikh, R., & Sana, S. S. (2023). Extraction of rules related to marketing mix on customers’
buying behavior using rough set theory and fuzzy 2-tuple approach. International Journal of Man -
agement Science and Engineering Management, 18(1), 16–25.
Galdón Salvador, J. L., & Marín Díaz, G. (2024). Enhancing business decision making through a new
corporate reputation measurement model: practical application in a supplier selection process. Sus-
tainability, 16(2), Article 523.
Geng, X., Li, Y ., Zhang, H., & He, J. (2023). Configuration optimization of product-service system design
requirements based on hesitant information axiom. Journal of Intelligent & Fuzzy Systems,  45(5),
9007–9028.
Giráldez-Cru, J., Chica, M., & Cordón, O. (2021). A framework of opinion dynamics using fuzzy linguistic
2-tuples. Knowledge-Based Systems, 233, Article 107559.
Giráldez-Cru, J., Chica, M., & Cordón, O. (2023). An integrative decision-making mechanism for con -
sumers’ brand selection using 2-Tuple fuzzy linguistic perceptions and decision heuristics. Interna-
tional Journal of Fuzzy Systems, 25(1), 59–79.
Giráldez-Cru, J., Chica, M., Cordón, O., & Herrera, F. (2020). Modeling agent-based consumers decision-
making with 2-tuple fuzzy linguistic perceptions. International Journal of Intelligent Systems, 35(2),
283–299.
1 3
308

Profiling the application of the 2-tuple linguistic model in marketing: a…
Gupta, P. K., & Andreu-Perez, J. (2022). A gentle introduction and survey on computing with words
(CWW) methodologies. Neurocomputing, 500, 921–937.
Gupta, P. K., & Muhuri, P. K. (2018). A novel approach based on computing with words for monitoring the
heart failure patients. Applied Soft Computing, 72, 457–473.
Herrera, F., Martinez, L. (2000). A 2-tuple fuzzy linguistic representation model for computing with
words. IEEE Transactions on Fuzzy Systems, 8(6), 746–752
Herrera-Viedma, E., Herrera, F., Martı́nez, L., Herrera, J. C., & López, A. G. (2004). Incorporating filtering
techniques in a fuzzy linguistic multi-agent model for information gathering on the web. Fuzzy Sets
and Systems, 148(1), 61–83.
Hogg, M. A. (2001). Group Processes, Social Psychology of. In: N. J. Smelser & P. B. Baltes (Eds.), Inter-
national Encyclopedia of the Social & Behavioral Sciences, pp. 6417–6423.
Huseynova, F. (2020). Computing with Words in Natural Language Processing. In: R. A. Aliev, J.
Kacprzyk, W. Pedrycz, M. Jamshidi, M. B. Babanli, & F. M. Sadikoglu (Eds.), 10th International
Conference on Theory and Application of Soft Computing, Computing with Words and Percep -
tions—ICSCCW-2019, (pp. 621–625). Springer International Publishing.
Hye, A. (2025). Market analytics in the US livestock and poultry industry: using business intelligence for
strategic decision-making. International Journal of Business and Economics Insights, 5(3), 170–204.
Jain, A., Gupta, D., Gupta, G., Aggarwal, S. (2017). Applications of computing with words in medicine:
promises and potential. 2017 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), 1–6.
Kali, A., Shamoi, P., Zhangbyrbayev, Y ., Zhandaulet, A. (2023). Computing with Words for Industrial
Applications. In: K. Arai (Ed.), Intelligent Systems and Applications, (pp. 257–271). Springer Inter-
national Publishing
Kargin, A., Petrenko, T. (2023). Knowledge Distillation for Autonomous Intelligent Unmanned System.
In: W. Pedrycz & S.-M. Chen (Eds.), Advancements in Knowledge Distillation: Towards New Hori-
zons of Intelligent Systems, (pp. 193–230). Springer International Publishing.
Khan, A., & Ahmad, U. (2023). Multi-criteria group decision-making based on 2-tuple linguistic q-rung
picture fuzzy sets. Granular Computing, 9(1), Article 8.
Lemon, K. N., & Verhoef, P. C. (2016). Understanding customer experience throughout the customer
journey. Journal of Marketing, 80(6), 69–96.
Li, C., & Yu, X. (2022). Consensus reaching model for counter-intuitive in D-S evidence theory and appli-
cation under 2-tuple linguistic representation. Engineering Applications of Artificial Intelligence,
112, Article 104832.
Li, M. (2012). The extension of quality function deployment based on 2-tuple linguistic representation
model for product design under multigranularity linguistic environment. Mathematical Problems in
Engineering, 2012(1), Article 989284.
Li, R. (2023). An integrated group decision-making method for brand packaging design effect evaluation
based on the 2-tuple linguistic Pythagorean fuzzy sets. Journal of Intelligent & Fuzzy Systems, 45(2),
2167–2177.
Liu, A., Zhu, Q., Liu, H., Lu, H., & Tsai, S.-B. (2018). A novel approach based on kano model, interval
2-tuple linguistic representation model, and prospect theory for apperceiving key customer require -
ments. Mathematical Problems in Engineering, 2018(1), 8192819.
Liu, H. (2022). Performance evaluation of family business strategic transition based on the 2-tuple linguis-
tic neutrosophic number multiple attribute group decision making. Journal of Intelligent & Fuzzy
Systems, 44, 1–13.
Liu, H.-C., You, X.-Y ., Xue, Y .-X., & Luan, X. (2017). Exploring critical factors influencing the diffusion
of electric vehicles in China: a multi-stakeholder perspective. Research in Transportation Econom-
ics, 66, 46–58.
Liu, J., Martínez, L., Wang, H., Rodríguez, R. M., & Novozhilov, V . (2010). Computing with words in risk
assessment. International Journal of Computational Intelligence Systems, 3(4), 396–419.
Li, W., Yu, S., Pei, H., Zhao, C., & Tian, B. (2017). A hybrid approach based on fuzzy AHP and 2-tuple
fuzzy linguistic method for evaluation in-flight service quality. Journal of Air Transport Manage -
ment, 60, 49–64.
Lizarelli, F. L., Osiro, L., Ganga, G. M. D., Mendes, G. H. S., & Paz, G. R. (2021). Integration of
SERVQUAL, analytical kano, and QFD using fuzzy approaches to support improvement decisions
in an entrepreneurial education service. Applied Soft Computing, 112, Article 107786.
Lundberg, J. (2007). Lifting the crown—citation z-score. Journal of Informetrics, 1(2), 145–154.
Mandal, M., Mohanty, B. K., & Dash, S. (2021). Understanding consumer preference through fuzzy-based
recommendation system. IIMB Management Review, 33(4), 287–298.
1 3
309

Z. Shu et al.
Mao, C. (2024). Enhanced group decision-making through an intelligent algorithmic approach for mul -
tiple-attribute credit evaluation with 2-tuple linguistic neutrosophic sets. International Journal of
Knowledge-Based and Intelligent Engineering Systems, 28(1), 163–177.
Mao, Q., Gao, Y ., & Fan, J. (2024). An integrated MCDM framework for tidal current power plant site
selection based on interval 2-tuple linguistic. Regional Studies in Marine Science, 74, Article 103518.
Marín Díaz, G., Carrasco González, R. A. (2023). Fuzzy logic and decision making applied to customer
service optimization. Axioms, 12(5), 448.
Marín Díaz, G., Carrasco, R. A., & Gómez, D. (2021). RFID: A fuzzy linguistic model to manage custom-
ers from the perspective of their interactions with the contact center. Mathematics, 9(19), Article
2362.
Marín Díaz, G., & Galdón Salvador, J. L. (2023). Group decision-making model based on 2-Tuple fuzzy
linguistic model and AHP applied to measuring digital maturity level of organizations. Systems,
11(7), Article 341.
Marín Díaz, G., Galdón Salvador, J. L., & Galán Hernández, J. J. (2023). Smart cities and citizen adoption:
exploring tourist digital maturity for personalizing recommendations. Electronics, 12(16), Article
3395.
Martínez, L., & Herrera, F. (2012). An overview on the 2-tuple linguistic model for computing with words
in decision making: extensions, applications and challenges. Information Sciences, 207, 1–18.
Martínez, L., Rodriguez, R. M., Herrera, F. (2015). Linguistic Decision Making and Computing with
Words. In: L. Martínez, R. M. Rodriguez, & F. Herrera (Eds.), The 2-tuple Linguistic Model: Com -
puting with Words in Decision Making, (pp. 1–21). Springer International Publishing.
Martínez, R. G., Carrasco, R. A., Sanchez-Figueroa, C., & Gavilan, D. (2021). An RFM model customiz-
able to product catalogues and marketing criteria using fuzzy linguistic models: case study of a retail
business. Mathematics, 9(16), Article 1836.
Martín-Martín, A., Thelwall, M., Orduna-Malea, E., & Delgado López-Cózar, E. (2021). Google scholar,
microsoft academic, scopus, dimensions, web of science, and opencitations’ COCI: a multidisci -
plinary comparison of coverage via citations. Scientometrics, 126(1), 871–906.
Mi, C., Chen, Y ., Zhou, Z., & Lin, C.-T. (2018). Product redesign evaluation: an improved quality function
deployment model based on failure modes and effects analysis and 2-tuple linguistic. Advances in
Mechanical Engineering, 10(11), 1687814018811227.
Mi, C., Shan, X., Qiang, Y ., Stephanie, Y ., & Chen, Y . (2014). A new method for evaluating tour online
review based on grey 2-tuple linguistic. Kybernetes, 43(3/4), 601–613.
Mu, L. (2024). An integrated methodology for enterprise financial management capability evaluation
based on EDAS technique and group decision making. Journal of Intelligent & Fuzzy Systems, 46(1),
2281–2296.
Muñoz-Leiva, F., Maria Eugenia, R., & Martí, B. (2022). Discovering prominent themes of the application
of eye tracking technology in marketing research. Cuadernos De Gestión, 22, 97–113.
Naz, S., Fatima, S. S., Butt, S. A., & Tabassum, N. (2023b). A MAGDM model based on 2-tuple linguistic
variables and power Hamacher aggregation operators for optimal selection of digital marketing strat-
egies. Granular Computing, 8(6), 1955–1990.
Naz, S., Saeed, M. R., & Butt, S. A. (2023c). Multi-attribute group decision-making based on 2-tuple
linguistic cubic q-rung orthopair fuzzy DEMATEL analysis. Granular Computing, 9(1), Article 12.
Naz, S., Shafiq, A., Butt, S. A., & Ijaz, R. (2023a). A new approach to sentiment analysis algorithms:
extended SWARA-MABAC method with 2-tuple linguistic q-rung orthopair fuzzy information.
Engineering Applications of Artificial Intelligence, 126, Article 106943.
Naz, S., Tasawar, A., Butt, S. A., Diaz-Martinez, J., & De-La-Hoz-Franco, E. (2024). An integrated
CRITIC-MABAC model under 2-tuple linguistic cubic q-rung orthopair fuzzy information with
advanced aggregation operators, designed for multiple attribute group decision-making. The Journal
of Supercomputing, 80(19), 27244–27302.
Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L.,
Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson,
A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D. (2021). The
PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ, 372, n71.
Petrescu, M., & Krishen, A. S. (2024). Marketing analytics in 2024 conferences: AI and data-driven deci-
sion-making. Journal of Marketing Analytics, 12(4), 743–745.
Pratihar, J., Dey, A., Khan, A., Banerjee, P., Pal, R. K. (2023). Computing with words for solving the fuzzy
transportation problem. Soft Computing.
1 3
310

Profiling the application of the 2-tuple linguistic model in marketing: a…
Purkayastha, A., Palmaro, E., Falk-Krzesinski, H. J., & Baas, J. (2019). Comparison of two article-level,
field-independent citation metrics: field-weighted citation impact (FWCI) and relative citation ratio
(RCR). Journal of Informetrics, 13(2), 635–642.
Ren, J., Gao, S., Tan, S., Dong, L., Scipioni, A., & Mazzi, A. (2015). Role prioritization of hydrogen pro-
duction technologies for promoting hydrogen economy in the current state of China. Renewable and
Sustainable Energy Reviews, 41, 1217–1229.
Rust, R. T. (2020). The future of marketing. International Journal of Research in Marketing, 37(1), 15–26.
Santos, LFdeOM., Osiro, L., & Lima, R. H. P. (2017). A model based on 2-tuple fuzzy linguistic repre -
sentation and analytic hierarchy process for supplier segmentation using qualitative and quantitative
criteria. Expert Systems with Applications, 79, 53–64.
Serrano-Guerrero, J., Bani-Doumi, M., Romero, F. P., & Olivas, J. A. (2024). A 2-tuple fuzzy linguistic
model for recommending health care services grounded on aspect-based sentiment analysis. Expert
Systems with Applications, 238, Article 122340.
Setti, D., Verona, M. N., Medeiros, B. B., & Restelli, A. (2019). Materials selection using a 2-tuple linguis-
tic multi-criteria method. Materials Research, 22, Article e20180846.
Shu, Z., Carrasco González, R. A., García-Miguel, J. P., & Sánchez-Montañés, M. (2023b). Clustering
using ordered weighted averaging operator and 2-tuple linguistic model for hotel segmentation: the
case of TripAdvisor. Expert Systems with Applications, 213, Article 118922.
Shu, Z., Carrasco, R. A., Sánchez-Montañés, M., & García-Miguel, J. P. (2024). A multi-criteria decision
support model for restaurant selection based on users’ demand level: The case of Dianping.com.
Information Processing & Management, 61(3), Article 103650.
Shu, Z., Llorens-Marin, M., Carrasco, R. A., & Romero, M. S. (2025). Customer electronic word of mouth
management strategies based on computing with words: the case of Spanish luxury hotel reviews on
TripAdvisor. Electronics, 14(2), Article 325.
Shu, Z., Torralba, M. H., Carrasco, R. A., & López, M. F. B. (2023a). Assessing customer satisfaction of
London luxury hotels with the AHP method and the SERVPERF scale: A case study of customer
reviews on TripAdvisor. Procedia Computer Science, 221, 73–80.
Singh, V . K., Singh, P., Karmakar, M., Leta, J., & Mayr, P. (2021). The journal coverage of web of science,
scopus and dimensions: a comparative analysis. Scientometrics, 126(6), 5113–5142.
Sohaib, O., Naderpour, M., Hussain, W., & Martinez, L. (2019). Cloud computing model selection for
e-commerce enterprises using a new 2-tuple fuzzy linguistic decision-making method. Computers &
Industrial Engineering, 132, 47–58.
Sun, P., Cui, T., & Qi, S. (2023). MADM framework based on 2-tuple linguistic neutrosophic sets and its
application to comprehensive evaluation of corporate cultural competitiveness. Journal of Intelligent
& Fuzzy Systems, 45(5), 7921–7937.
Tai, W.-S., & Chen, C.-T. (2009). A new evaluation model for intellectual capital based on computing with
linguistic variable. Expert Systems with Applications, 36(2, Part 2), 3483–3488.
Tamir, D., Neumann, S., Rishe, N., Kandel, A., Zadeh, L. (2019). Computing with Words—A Framework
for Human-Computer Interaction. In: D. D. Schmorrow & C. M. Fidopiastis (Eds.), Augmented Cog-
nition, (pp. 356–372). Springer International Publishing.
Trung, N. Q., & Thanh, N. V . (2022). Evaluation of digital marketing technologies with fuzzy linguistic
MCDM methods. Axioms, 11(5), 230.
Tymchuk, O., Iepik, M., & Sivyakov, A. (2017). Information security risk assessment model based on
computing with words. MENDEL, 23(1), 119–124.
Uzun, B., Ozsahin, I., Agbor, V . O., Uzun Ozsahin, D. (2021). Chapter 2—Theoretical aspects of multi-
criteria decision-making (MCDM) methods. In I. Ozsahin, D. U. Ozsahin, & B. Uzun (Eds.), Appli-
cations of Multi-Criteria Decision-Making Theories in Healthcare and Biomedical Engineering, (pp.
3–40). Academic Press.
Visser, M., van Eck, N. J., & Waltman, L. (2021). Large-scale comparison of bibliographic data sources:
scopus, web of science, dimensions, crossref, and microsoft academic. Quantitative Science Studies,
2(1), 20–41.
Waltman, L., van Eck, N. J., van Leeuwen, T. N., Visser, M. S., & van Raan, A. F. J. (2011). Towards a new
crown indicator: some theoretical considerations. Journal of Informetrics, 5(1), 37–47.
Wang, J., Lu, J., Wei, G., Lin, R., & Wei, C. (2019b). Models for MADM with single-valued neutrosophic
2-tuple linguistic muirhead mean operators. Mathematics, 7(5), 442.
Wang, J., Lu, M., & Wei, G. (2019c). Models for multiple attribute decision making with some interval-
valued 2-tuple linguistic pythagorean fuzzy bonferroni mean operators. International Journal of
Knowledge-Based and Intelligent Engineering Systems, 23(4), 259–294.
1 3
311

Z. Shu et al.
Wang, J.-W. (2021). Multi-criteria decision-making method based on a weighted 2-tuple fuzzy linguistic
representation model. International Journal of Information Technology & Decision Making, 20(02),
619–634.
Wang, P., Wang, J., Wei, G., Wei, C., & Wei, Y . (2019a). The multi-attributive border approximation area
comparison (MABAC) for multiple attribute group decision making under 2-tuple linguistic neutro-
sophic environment. Informatica, 30(4), 799–818.
Wang, S.-Y . (2008). Applying 2-tuple multigranularity linguistic variables to determine the supply per -
formance in dynamic environment based on product-oriented strategy. IEEE Transactions on Fuzzy
Systems, 16(1), 29–39.
Wang, S.-Y . (2013). Applying the superior identification group linguistic variable to construct kano model
oriented quality function deployment. Technological and Economic Development of Economy,
19(sup1), S304–S325.
Wang, W., Ding, L., Liu, X., & Liu, S. (2022). An interval 2-Tuple linguistic fine-kinney model for risk
analysis based on extended ORESTE method with cumulative prospect theory. Information Fusion,
78, 40–56.
Wang, W.-P. (2009). Evaluating new product development performance by fuzzy linguistic computing.
Expert Systems with Applications, 36(6), 9759–9766.
Wang, Z.-L., You, J.-X., & Liu, H.-C. (2016). Uncertain quality function deployment using a hybrid group
decision making model. Symmetry, 8(11), 119.
Wan, S., Xu, G., & Dong, J. (2017). Supplier selection using ANP and ELECTRE II in interval 2-tuple
linguistic environment. Information Sciences, 385–386, 19–38.
Wei, G., Wang, J., Lu, J., Wu, J., Wei, C., Alsaadi, F. E., & Hayat, T. (2020). VIKOR method for mul -
tiple criteria group decision making under 2-tuple linguistic neutrosophic environment. Economic
Research-Ekonomska Istraživanja, 33(1), 3185–3208.
Wei, G., Wu, J., Wei, C., Wang, J., & Lu, J. (2019). Models for MADM with 2-tuple linguistic neutro -
sophic dombi bonferroni mean operators. IEEE Access, 7, 108878–108905.
Wen, T.-C., Chang, K.-H., & Lai, H.-H. (2020). Integrating the 2-tuple linguistic representation and soft
set to solve supplier selection problems with incomplete information. Engineering Applications of
Artificial Intelligence, 87, Article 103248.
Wu, P., Tang, T., Zhou, L., & Martínez, L. (2024). A decision-support model through online reviews:
consumer preference analysis and product ranking. Information Processing & Management,  61(4),
Article 103728.
Wu, Z., Xu, J., & Xu, Z. (2016). A multiple attribute group decision making framework for the evaluation
of lean practices at logistics distribution centers. Annals of Operations Research, 247(2), 735–757.
Xing, Y .-J., & Xing, C. (2016). Model for evaluating the virtual enterprise’s risk with 2-tuple linguistic
information. Journal of Intelligent & Fuzzy Systems, 31(1), 193–200.
Xu, F. (2024). A 2TLNS-based exponential TODIM-EDAS approach for evaluating sustainable devel -
opment of cross-border e-commerce platforms under uncertainty. Journal of Intelligent & Fuzzy
Systems, 46, 1–16.
Yager, R. R. (1999). Approximate Reasoning as a Basis for Computing with Words. In: L. A. Zadeh &
J. Kacprzyk (Eds.), Computing with Words in Information/Intelligent Systems 1: Foundations, pp.
50–77. Physica-Verlag HD.
Yager, R. R. (2004). Generalized OWA aggregation operators. Fuzzy Optimization and Decision Making,
3(1), 93–107.
Yang, Q., Chen, Z.-S., Zhu, J.-H., Martínez, L., Pedrycz, W., & Skibniewski, M. J. (2024b). Concept
design evaluation of sustainable product-service systems: a QFD–TOPSIS integrated framework
with basic uncertain linguistic information. Group Decision and Negotiation, 33(3), 469–511.
Yang, Y ., Xia, D.-X., Pedrycz, W., Deveci, M., & Chen, Z.-S. (2024a). Cross-platform distributed product
online ratings aggregation approach for decision making with basic uncertain linguistic information.
International Journal of Fuzzy Systems, 26(6), 1936–1957.
Yuan, J., Zhang, Z. M., Yüksel, S., & Dinçer, H. (2020). Evaluating recognitive balanced scorecard-based
quality improvement strategies of energy investments with the integrated hesitant 2-tuple interval-
valued Pythagorean fuzzy decision-making approach to QFD. IEEE Access, 8, 171112–171128.
Zadeh, L. A. (1975). The concept of a linguistic variable and its application to approximate reasoning—I.
Information Sciences, 8(3), 199–249.
Zadeh, L. A. (1996). Fuzzy logic = computing with words. IEEE Transactions on Fuzzy Systems, 4(2),
103–111.
1 3
312

Profiling the application of the 2-tuple linguistic model in marketing: a…
Zhang, Q., Jiang, K., Yan, M., & Ma, J. (2019). A competitive multiattribute group decision-making
approach for the game between manufacturers. Computational Intelligence and Neuroscience,
2019(1), 8389035.
Zhang, S., Wei, G., Alsaadi, F. E., Hayat, T., Wei, C., & Zhang, Z. (2020). MABAC method for multiple
attribute group decision making under picture 2-tuple linguistic environment. Soft Computing, 24(8),
5819–5829.
Zhang, S., Zhu, F., Deveci, M., & Liu, X. (2024). Consensus-oriented linguistic multi-criteria group sort-
ing method incorporating dynamic trust management. Information Fusion, 112, Article 102539.
Zhang, Y ., Cai, Q., Wei, G., & Chen, X. (2023). Model for evaluating the airline business operations capa-
bility based on 2TLPF-TOPSIS method and entropy weight. Journal of Intelligent & Fuzzy Systems,
44(4), 5745–5758.
Zhong, Y ., Li, G., Chen, C., Jin, T., & Liu, Y . (2023). Reliability allocation method based on 2-tuple lin-
guistic weighted muirhead mean operator and 2-tuple linguistic best-worst method. IEEE Transac-
tions on Reliability, 72(2), 542–551.
Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps
and institutional affiliations.
Authors and Affiliations
Ziwei Shu1  · José Javier Galán Hernández2  · Álvaro Carrasco-Aguilar3
  Ziwei Shu
ziweishu@ucm.es
1 Department of Marketing, Faculty of Statistics, Complutense University of Madrid,
28040 Madrid, Spain
2 ENAE Business School, 30100 Murcia, Spain
3 Rey Juan Carlos University, 28933 Madrid, Spain
1 3
313
