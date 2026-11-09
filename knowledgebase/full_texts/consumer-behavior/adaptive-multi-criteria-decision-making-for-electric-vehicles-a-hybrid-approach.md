---
title: 'Adaptive multi-criteria decision making for electric vehicles: a hybrid approach based on RANCOM
  and ESP-SPOTIS'
url: https://doi.org/10.1007/s10462-024-10901-4
category: consumer-behavior
subcategory: empirical
date: 2024-08
venue: Artificial Intelligence Review
authors:
- Jakub Więckowski
- Jarosław Wątróbski
- Anna Shkurina
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10462-024-10901-4.pdf
pages: 25
chars: 79072
fetched_at: '2026-11-08T17:09:41+00:00'
kb_version: 1
---

# Adaptive multi-criteria decision making for electric vehicles: a hybrid approach based on RANCOM and ESP-SPOTIS

Vol.:(0123456789)
Artificial Intelligence Review (2024) 57:270
https://doi.org/10.1007/s10462-024-10901-4
Adaptive multi‑criteria decision making for electric vehicles:
a hybrid approach based on RANCOM and ESP‑SPOTIS
Jakub Więckowski1 · Jarosław Wątróbski2 · Anna Shkurina2 · Wojciech Sałabun1,3
Accepted: 6 August 2024 / Published online: 28 August 2024
© The Author(s) 2024
Abstract
In today’s globalized technological area, aligning decisions with customer preferences is
crucial yet challenging due to the complexities and uncertainties involved. Multi-Criteria
Decision Analysis (MCDA) serves as a vital tool for constructing support systems that
cater to customer-centric trends. While existing MCDA methods vary in their calculation
concepts, some prioritize ideal solutions, while others accommodate personalized
preferences within dynamic decision contexts. Moreover, determining the relevance of
criteria based on expert knowledge adds another layer of personalization to the evaluation
process, further individualizing decision-making. However, current decision models often
fail to integrate these concepts, leaving a gap in how recommendations can be enhanced
when both are combined. To address these challenges, this paper introduces an innovative
approach integrating Ranking Comparison and Expected Solution Point Stable Preference
Ordering Towards Ideal Solution methods. This hybrid model incorporates personalization
into multi-criteria evaluation, catering to individual preferences. By representing customer
preferences through two distinct measures, the proposed approach ensures personalized
recommendations aligned with decision-makers’ needs. The efficacy of the hybrid model
was validated through its application to the electric vehicle selection problem. The
verification process highlighted potential disparities compared to other multi-criteria
approaches, establishing a consumer preference-based Decision Support System approach
for more precise and personalized selection recommendations.
Keywords Uncertainty · Fuzzy preferences · Personalized decision · Decision making ·
Electric vehicles · RANCOM
1 Introduction
In the era of global technological advancements, there is a growing emphasis on
empowering customers to make decisions aligned with their preferences Martínez-Torres
et  al. (2015). However, the complexity of individual decision-making is intensified by
conflicting factors, and the multitude of criteria that should be considered in the decision
process often surpasses the analytical capabilities of customers Isen (2001). To navigate
this complexity, Multi-Criteria Decision Analysis (MCDA) emerges as a vital tool, offering
Extended author information available on the last page of the article

 J. Więckowski et al.
270 Page 2 of 25
support systems tailored to address the specific challenges faced by individual customers
Guo et al. (2020). This approach improves clients’ decision-making and contributes to a
more personalized and satisfying customer experience, aligning with the contemporary
trend of customer-centric services in a technology-driven world Zaim et al. (2020).
Multi-Criteria Decision Analysis methods utilize various input data for their evaluations
Sałabun et al. (2020). This includes criteria weights, which are crucial in determining the
relevance of decision criteria Odu (2019). Moreover, different normalization techniques
or distance measures are used Chakraborty and Yeh (2009). In addition, MCDA methods
serve as the foundation for dedicated Decision Support Systems (DSS), aiding in the
comprehensive evaluation of considered decision variants for individual customers Giove
et al. (2009); Razmak and Aouni (2015). In an era where data-driven insights are highly
valued, incorporating criteria weights based on reliable measures enhances the credibility
of the decision support systems Ayan et al. (2023). Furthermore, it ensures a more robust
and transparent decision-making process for customers, integrating their individualized
preferences into the evaluation.
Identifying criteria weights can be approached in three distinct ways Yusop et  al.
(2015). One method employs data information measures derived from the decision
matrix, ensuring objectivity in the criteria weight identification process Paradowski et al.
(2021). Alternatively, criteria weights can be determined based on expert knowledge and
preferences, aligning with individualized priorities Keshavarz-Ghorabaee et al. (2018). This
approach significantly contributes to providing personalized recommendations, facilitating
the identification of the most desired outcome for the decision-maker Şahin (2021). As
decision-making becomes increasingly diversified and contextual, incorporating expert
knowledge allows to model the decision personalization Song et al. (2021). Moreover, it
ensures that decision support systems resonate with individual customers’ preferences and
unique requirements. In addition, another approach combines the objective and subjective
weighting methods and can be used to achieve a compromise regarding the determined
criteria weights Alemi-Ardakani et al. (2016).
Besides the criteria weights, another crucial dimension of multi-criteria decision
analysis involves modeling the personalized decision-making process. Within the MCDA
field, various techniques are developed based on different conceptual foundations Ceballos
et  al. (2016). One prevalent approach utilizes the Ideal Solution Point (ISP), aiming to
create an ideal alternative for assessing considered decision variants Dheena and Mohanraj
(2011). However, achieving a perfect solution in real-world problems remains challenging.
To address this, more suitable measures are needed to model the individualized preferences
of customers. An emerging concept in this area is the Expected Solution Point (ESP), which
enables the evaluation of alternatives based on expected outcomes Dezert et  al. (2020).
This adaptable approach accommodates decision-makers’ personalized needs, enhancing
its relevance in diverse decision contexts Shekhovtsov (2022). In a world characterized by
evolving preferences and dynamic decision areas, the flexibility of the ESP aligns with the
need for adaptive decision-making tools that can satisfy individualized and ever-changing
customer requirements Shekhovtsov et  al. (2023). Despite the significant potential of
subjective weighting methods and the ESP concept for modeling customers’ preferences,
these approaches have traditionally been employed as separate measures. However,
the combination of these measures and the verification of their performance remains
unexplored. Introducing a personalized decision-making process in these two dimensions
has the potential to substantially enhance the effectiveness of supporting customers
in personalized product selection. The current absence of decision models built upon
subjective weighting methods and the ESP concept highlights a noticeable information gap

Adaptive multi‑criteria decision making for electric vehicles:…
Page 3 of 25 270
that should be filled. Exploring the performance of a hybrid decision model built upon
these two approaches could bridge this gap and determine whether their combination leads
to more accurate customer recommendations.
To address the need for more personalized decision support systems, this paper proposes
a new hybrid approach that integrates decision-maker preference-driven requirements.
The model combines a subjective weighting method to determine criteria relevance
based on expert knowledge with the ESP concept, which identifies desired values for the
considered criteria. The Ranking Comparison (RANCOM) method is utilized to establish
criteria weights based on expert opinions Więckowski et al. (2023), while the ESP Stable
Preference Ordering Towards Ideal Solution (ESP-SPOTIS) method evaluates decision
variants based on these expected solutions Dezert et al. (2020). By integrating these two
methods, which consider decision-maker preferences in different dimensions of the multi-
criteria assessment process, the proposed approach aims to develop support systems that
align more closely with customer needs. This hybrid model provides recommendations
supported by the relevance of criteria with the specified expected solutions, making
it a comprehensive tool for customer support. The practical application of this model is
demonstrated through the problem of electric vehicle selection based on personalized
needs. The results are further verified by comparing them with recommendations from
other MCDA methods that incorporate at least one aspect of personalized decision-making.
The goal is to propose a Decision Support System (DSS) approach that leverages consumer
preferences to offer more personalized selection recommendations. The main contributions
of the study are:
• The use of the MCDA concept in a tool for decision support systems significantly
improves clients’ decision-making processes, offering personalized solutions tailored to
individual customer challenges. This contributes to a more satisfying and personalized
customer experience in the context of contemporary customer-centric services and
technological advancements.
• The proposed approach combines the Ranking Comparison (RANCOM) method for
identifying criteria weights based on subjective expert opinions with the Expected
Solution Point Stable Preference Ordering Towards Ideal Solution (ESP-SPOTIS)
method for evaluating decision variants. This innovative integration allows for a more
accurate alignment with decision-makers’ needs, offering a personalized selection of
recommendations and creating the potential to develop decision support systems that
better adapt to individual customer preferences.
• The study proposes a methodology for verifying decision models in the electric vehicle
selection problem. This verification examines the reliability and effectiveness of the
proposed decision support system in aligning with individualized preferences. The
suggested methodology offers a versatile framework applicable to various customer
problems beyond electric vehicle selection, providing a robust approach for selecting
products based on personalized needs in diverse domains.
The rest of the paper is organized as follows. Section 2 presents the review of related works
concerning the subjective and objective weighting techniques and Ideal Solution Point and
Expected Solution Point concepts. Section  3 presents the preliminaries of the RANCOM
method, the ESP-SPOTIS method, and selected correlation coefficients. Section  4 presents
the study case in which the problem of electric vehicle selection is shown, and the results
are included. Then, Sect. 5 shows the verification of the results with the selected sensitivity
analysis approaches. Section  6 presents the discussion about the practical implications of

 J. Więckowski et al.
270 Page 4 of 25
the proposed decision support system. Finally, Sect. 7 presents conclusions drawn from the
research and indicates further directions of the study.
2  Related works
Due to the variety of available methods, developing MCDA models allows for the
application of different techniques. Objective and subjective methods could be used
to model the importance of criteria considered in the decision problem, offering the
possibility to determine more autonomous or expert-dependent support systems. However,
the identification of criteria relevance is only a part of the process of modeling decision
models. The selection of the MCDA method is also significant. Among the various
assessment techniques, multi-criteria methods based on Ideal Solution Point or Expected
Solution Point could be applied depending on the defined objective. To present the
overview of the recent research approaches, which included the mentioned approaches for
modeling decision systems, the application of different weighting approaches and MCDA
methods regarding different reference point assumptions were described below.
2.1  Weighting techniques
To determine criteria weights in decision problems, different approaches can be used,
namely (1) objective methods, which based their calculation on the information measures
extracted from the decision matrix Koksalmis and Kabak (2019), (2) subjective methods,
which rely on expert knowledge and in a structured way allow to establish the relation
between criteria by the expert Pamučar et al. (2018), and (3) mixed approach, including
both objective and subjective approach Liu et al. (2016). The objective techniques allow
for creating more autonomous decision models since domain experts are not required
to participate in the decision process Kumar et  al. (2021). It makes it an interesting
approach when the expert who should be engaged in model development is unavailable.
Moreover, it allows the identification of criteria weights without bias, which could often
appear in the criteria relevance evaluation performed by experts. In this group of methods,
techniques like Equal Marttunen et al. (2018), Entropy Mukhametzyanov (2021), CRiteria
Importance Through Intercriteria Correlation (CRITIC) Krishnan et al. (2021), Integrated
Determination of Objective CRIteria Weight (IDOCRIW) Podvezko et  al. (2020), or
Criterion Impact LOS (CILOS) Tajik et al. (2023) are eagerly applied.
However, it should be noted that in some scenarios, criteria weights determined
with information measures techniques could not include important insights that
could be extracted from the expert and professional experience gained during the
years of handling problems within the given field Koksalmis and Kabak (2019).
Moreover, the objective techniques could not reflect the individualized preferences of
decision-makers, making it an unsuitable solution for a preference-driven approach to
developing personalized decision support systems. Despite the potential bias, expert
hesitance, or inconsistencies in judgments, subjective weighting techniques enable
identifying criteria weights in a more adjustable manner considering the individual
requirements of decision-makers Chou et al. (2008). Moreover, it is worth mentioning
that subjective weighting techniques are consistently improved to offer a more stable
and reliable approach to extracting expert knowledge while limiting the influence of
potential inconsistencies Mahmoudi and Javed (2023). Techniques like the Analytical

Adaptive multi‑criteria decision making for electric vehicles:…
Page 5 of 25 270
Hierarchy Process (AHP) Liu et  al. (2020), Full Consistency Method (FUCOM)
Pamucar and Ecer (2020), Ranking Comparison (RANCOM) Więckowski et  al.
(2023), Step-Wise Weight Assessment Ratio Analysis (SWARA) Hashemkhani Zolfani
et al. (2018), Best-Worst Method (BWM) Liu et al. (2021), or Simple Multi-Attribute
Ratio Technique (SMART) Ezell et  al. (2021), among others, are popular in recent
applications.
A mixed approach could be used to combine the advantages of objective and
subjective methods Paramanik et  al. (2022). It allows the identification of criteria
weights based on the knowledge of domain experts while minimizing potential biases
of judgments by adjusting the established weights with the ones determined with
objective methods Chang (2023). To this end, the obtained criteria’ relevance could
be treated more reliably since the potential biases could be neglected by integrating
the two obtained vectors of criteria weights Sitorus and Brito-Parada (2022). However,
this could also be interference to the criteria weights identification process since even
weights obtained with accurate and consistent expert responses could be slightly
altered by the combination with the objective weights. Moreover, the customer-
driven approach for criteria weight identification should not additionally modify the
importance of criteria determined by the decision-maker to represent the needs as
accurately as possible with compliance to the individualized preference.
2.2  Multi‑criteria decision analysis methods applications
There is a visibly increasing trend of applying MCDA methods within practical decision
problems to propose stable and reliable evaluation tools that aim to support decision-
makers in making more informed choices Więckowski et al. (2023). Dağıstanlı applied
the interval-values intuitionistic fuzzy VIKOR for R &D project selection for defense
industry investments Dağıstanlı (2024). Vahidinia and Hasani directed their research
toward determining a comprehensive evaluation model for smart supply chains based
on the MCDA approach Vahidinia and Hasani (2023). Mahmutagić et  al. covered
the problem of evaluating the efficiency analysis of the forklifts in warehousing
systems Mahmutagić et al. (2021). Kara et al. evaluated the academic performance of
Turkish Universities in 2023 by applying the MEREC-WEBDA hybrid approach Kara
et  al. (2024). Lo et  al. assessed the supplier disruption risks using the Pythagorean
Fuzzy SWARA-TOPSIS method Lo et al. (2024). Sarfraz utilized the interval-valued
T-spherical Fuzzy Dombi Hamy Mean Operators in the antiviral mask selection
against COVID-19 Sarfraz (2024). Tripathi et al. proposed a new intuitionistic fuzzy
parametric divergence measures and score function-based CoCoSo method and applied
it to rank and evaluate the therapies for medical decision-making problems Tripathi
et al. (2023). Biswas et al. assessed the preparedness of small and medium enterprises
for standards of quality management Biswas et  al. (2023). Bairagi proposed a new
framework for green selection of material in fuzzy environment Bairagi (2023). Gökalp
et al. proposed a novel artificial intelligence-based decision model for determining the
priority strategies for improving community health Gökalp et al. (2024). The variety
of problems that are addressed by the developed decision models built upon MCDA
methods highlights the fact, that this field is constantly improving. Moreover, there
is a growing trend in the application of MCDA methods to address practical decision

 J. Więckowski et al.
270 Page 6 of 25
problems, offering stable and reliable tools to aid decision-makers in making more
informed choices.
2.3  Reference point concept in MCDA
Multiple Multi-Criteria Decision Analysis methods use a reference point to compute
alternative rankings Wang and Johnson (2012). This reference point is a concept for
evaluating and ranking alternative options based on predefined criteria, representing a
benchmark or ideal solution that decision-makers aspire to achieve. The reference point
can be presented in various forms, such as an aspiration level, an ideal point, an expected
point, or even a worst-case scenario Dezert et  al. (2020); Nowak (2007), contingent
on the decision context. Reference points assist decision-makers in evaluating and
comparing alternatives and translating criteria into practical assessments Wang et  al.
(2015). They guide decisions toward solutions aligned with predefined objectives and
preferences. Current development directions seek innovative ways to leverage and adapt
reference points to diverse decision contexts, thereby enhancing the applicability and
effectiveness of this approach in real-world decision-making scenarios.
The Ideal Solution Point (ISP) is a commonly used reference point in Multi-Criteria
Decision Analysis, representing the optimal outcome for each criterion when all criteria
are maximized or minimized simultaneously Chen (2015). The ISP is a benchmark for
evaluating alternatives, with those closer to it considered more favorable. In practical
MCDA applications, achieving or closely approximating the ISP can be challenging due
to conflicting criteria or resource constraints Herrera-Viedma et al. (2020). Methods like
Technique for the Order of Prioritisation by Similarity to Ideal Solution (TOPSIS) Uzun
et al. (2021), Measurement Alternatives and Ranking according to COmpromise Solution
(MARCOS) Ulutaş et  al. (2020), Reference Ideal Method (RIM) Cables et  al. (2016),
COmbinative Distance-based ASsessment (CODAS) Keshavarz  Ghorabaee et  al. (2016),
Evaluation based on Distance from Average Solution (EDAS) Akram et  al. (2023), or
VIseKriterijumska Optimizacija I Kompromisno Resenje (VIKOR) Chen (2019) are built
on the different variants of the Ideal Solution concept, assessing alternatives based on their
proximity to the ISP or related points. The ISP plays a crucial role in MCDA by providing a
theoretical reference for evaluating and ranking alternatives in decision-making processes.
The Expected Solution Point (ESP) provides a more flexible and adaptable approach
when decision-makers aim to incorporate subjective preferences into the evaluation
process Shekhovtsov (2022). Contrary to traditional reference points representing
ideal or worst-case scenarios, the ESP acknowledges that decision-makers may not
pursue absolute ideal solutions and are open to selecting outcomes aligning with
their subjective preferences Dezert et  al. (2020). Decision-makers can specify their
expected outcomes for each criterion. This allows for a more personalized decision-
making process where alternatives are assessed based on their proximity to the ESP
Shekhovtsov et al. (2023). It is particularly valuable when decision-makers can express
preferences regarding expected outcomes, enhancing the adaptability of MCDA to
complex and dynamic decision contexts. The ESP-SPOTIS Shekhovtsov (2022) and
ESP-Characteristic Objects Method (COMET) Shekhovtsov et al. (2023) incorporate the
ESP approach to align with decision-makers’ expectations. This approach makes it more
applicable in expert-driven decision problems where absolute ideal solutions may not
always be feasible or desirable. Thus, MCDA methods use diverse calculation concepts
to cater to various decision-making scenarios and preferences, enhancing their overall

Adaptive multi‑criteria decision making for electric vehicles:…
Page 7 of 25 270
applicability. The ISP offers a theoretical benchmark for optimal outcomes, while the
ESP allows for subjective flexibility and practical feasibility. This diversity ensures that
decision-makers have the necessary tools to evaluate and rank alternatives effectively.
3  Preliminaries
The main assumptions of the RANCOM and ESP-SPOTIS methods were described
below to present formal notations of the research methods used to determine the
customer preference-driven decision support system. Moreover, the two selected
correlation measures were presented to show how the results could examined regarding
the occurring differences in rankings.
3.1  The RANCOM method
The Ranking Comparison (RANCOM) method presents an innovative strategy
for extracting expert knowledge while accounting for multiple decision criteria
Więckowski et al. (2023). In a comparative analysis contrasting RANCOM with AHP
methods, it became evident that the former excels in handling inconsistencies within
expert judgments, outperforming the latter. Below, the fundamental principles of the
RANCOM method are described, along with its subsequent procedural steps.
Step 1. Define the criteria ranking.
The expert determines the position of the criteria regarding other factors. The
designated ranking should be defined as lower values assigned to more significant
criteria. Additionally, the criteria may have equal positions in the ranking, meaning
ties are allowed during the expert judgment. The criteria ranking could be defined with
subsequent values (i.e., [1, 2, 3, 4, 5] for five criteria) or could consist of more diverse
values (i.e., [1, 5, 9, 12, 18] for five criteria). However, the differences that occurred in
the ranking vector would not affect the calculated weights unless they include different
criteria hierarchies.
Step 2. Establish the Matrix of Ranking Comparison.
The MAtrix of ranking Comparison (MAC ) is determined by using a pairwise
comparison of the positions from the ranking made by the expert. The comparison result is
determined as 𝛼ij . Based on that, the MAC matrix can be represented as (1):
where n is the number of criteria taken into account in the problem, and 𝛼ij is determined
from (2):
(1)

 J. Więckowski et al.
270 Page 8 of 25
where f (C) is a significance function of criterion C.
Step 3. Calculate the Summed Criteria Weights.
Based on the obtained MAC , the horizontal vector of the Summed Criteria Weights
(SCW) is obtained as follows (3).
Step 4. Calculate the final criteria weights.
Finally, values of preference are approximated for each criterion. As a result, the
horizontal vector W is obtained, where the i − th row contains the approximate preference
value for Ci . The weights for the set of criteria are obtained as (4):
An expert employing the RANCOM method can determine their ranking through
diverse approaches to establish an order relationship among criteria. The potential strat-
egies within this method include: (1) Ranking; (2) Scoring; (3) Sort algorithm; and (4)
Tournament approach. Each option offers the expert a systematic framework for defining
the criteria ranking. Moreover, when dealing with an expanding number of factors in a
problem, creating an order relationship for these criteria becomes challenging, leading
to potential inaccuracies in evaluation. Hence, adopting the proposed approaches aims to
streamline this process, providing a more straightforward task for the expert. The subse-
quent steps of the proposed subjective weighting method are shown in Fig. 1.
(2)𝛼ij =
⎧
⎪
⎨
⎪⎩
IF f �Ci � < f �Cj � THEN 1
IF f �Ci � = f �Cj � THEN 0.5
IF f �Ci � > f �Cj � THEN 0
(3)SCWi =
n/uni2211.s1
j=1
𝛼ij
(4)wi = SCWi ∑n
i=1 SCWi
Step 2
Establish the Matrix of
ranking Comparison
Step 1
Define the criteria order
Step 3
Calculate the Summed
Criteria Weights
Step 4
Calculate
the final weights
Calculate SCW vector
based on Matrix of
Ranking Comparison
Calculate the final
criteria weights using
SCW vector
MAC is built
by expert
MAC could be
inconsistent
Build MAC
automatically
MAC is always
consistent
[Optional]
Use triads consistency
coefficient to ensure
that MAC is consistent
Score the
criteria
Order criteria using
sorting algorithm
Establish the
ranking of criteria
Use the tournament
method
Fig. 1  Flowchart of the subsequent steps in the RANCOM method

Adaptive multi‑criteria decision making for electric vehicles:…
Page 9 of 25 270
3.2  The SPOTIS method
The Stable Preference Ordering Towards Ideal Solution (SPOTIS) method uses the
concept of reference objects Tsakalerou et al. (2022). Unlike other MCDA methods, such
as Technique for the Order of Prioritisation by Similarity to Ideal Solution (TOPSIS)
Chen et al. (2011) and VIseKriterijumska Optimizacija I Kompromisno Resenje (VIKOR)
Chatterjee and Chakraborty (2016), which creates reference objects based on a decision
matrix, the SPOTIS method requires defining the data boundaries. Using this to define
the decision problem domain, it is possible to stabilize ordering alternatives toward Ideal
Solution Point (ISP) to avoid the Rank Reversal (RR) paradox Aires and Ferreira (2018).
Usually, ISP is chosen based on criteria-bound values for the type of criteria (cost or
profit). Data boundaries should be defined to apply this method in the initial phase. For
each criterion Cj , the maximum Smax j  and minimum Smin j  bounds should be selected. The
Ideal Solution Point S∗ j  is defined as S∗ j = Smax j  for profit criterion and S∗ j = Smin j  for cost
criterion.
Furthermore, as demonstrated in Dezert et al. (2020), the SPOTIS method could be used
with any Expected Solution Point (ESP) instead of ISP. When used, ESP creates a ranking
toward this subjectively selected solution. It could be helpful when a decision-maker seeks
a solution that perfectly fits a particular problem instead of a general ideal solution in the
problem domain. Expected Solution Point values S∗ j  must be selected between defined
bounds of the decision problem [Smin j , Smax j ] , then the ESP vector S∗ should be used instead
of ISP in the Eq.  6 in the SPOTIS calculation procedure Shekhovtsov (2022). Below,
subsequent steps of the SPOTIS method are presented.
Step 1. Definition of decision matrix.
The decision matrix describes the characteristics of considered alternatives under
selected criteria. The formal notation of the decision matrix could be defined as (5):
where xij is the attribute value of the i-th alternative for j-th criterion.
Step 2. Calculation of the normalized distances from ISP (6):
Step 3. Calculation of weighted normalized distances d(Ai, S∗)∈[ 0, 1] as (7):
Step 4. Ranking calculation.
The final ranking of alternatives should be determined based on the value of d(Ai, S∗) .
Better evaluated decision variants have smaller values of d(Ai, S∗) , thus should be placed
higher in the ranking.
(5)X =
⎡
⎢
⎢
⎢
⎢
⎢
⎢⎣
x11 x12 ⋯ x1j ⋯ x1m
x21 x22 ⋯ x2j ⋯ x2m
⋮ ⋮⋯⋮⋯ ⋮
xi1 xi2 ⋯ xij ⋯ xim
⋮ ⋮⋯⋮⋯ ⋮
xn1 xn2 ⋯ xnj ⋯ xnm
⎤
⎥
⎥
⎥
⎥
⎥
⎥⎦
(6)d(Ai, S∗ j )= /uni007C.varSij − S∗ j /uni007C.var /uni007C.varSmax j − Smin j /uni007C.var
(7)d(Ai, S∗)=
N/uni2211.s1
j=1
wjdij(Ai, S∗ j )

 J. Więckowski et al.
270 Page 10 of 25
3.3  Correlation coefficients
In numerous cases, researchers conducting studies on decision problems seek to employ
multiple Multi-Criteria Decision Analysis methods to derive the outcome  (Hezer et  al.
2021). This approach enables the comparison of different methods to identify the most
suitable approach for the given problem. However, it is equally important to assess the
coherence of the obtained results (Sennaroglu and Celebi 2018). Consistency among the
selected methods is crucial for establishing a robust final ranking that is both trustworthy
and reliable. To achieve this, correlation coefficients are vital in providing a comparative
analysis of the results and are integral to decision-making (Sałabun et al. 2020).
Most correlation coefficients used in the MCDA domain have a range of values
denoted as x ∈[ 0, 1] (Ganti 2020). Correlation coefficient values close to 1 indicate a high
similarity between the compared rankings, while values lower than this threshold represent
a lower correlation. Conversely, a correlation value of 0 suggests complete opposition
in the results. Generally, rankings are highly correlated when the correlation value is
within the [0.8,  1.0]  (Shekhovtsov et  al. 2021). This study used two selected correlation
coefficients: Weighted Spearman’s correlation coefficient rW and Weighted Similarity WS
rank similarity coefficient. The descriptions of the mentioned coefficients are presented
below.
3.3.1  Weighted Spearman’s correlation coefficient
The Weighted Spearman’s correlation coefficient proposed by  (Dancelli et  al. 2013) is
inspired by the Spearman coefficient. The idea is to add weights that will increase the
influence of the changes in the head of the ranking on the final correlation value. The
correlation value is calculated for two rankings of size N, where xi stands position in the
first ranking and yi is the position in the second ranking (8).
The rW correlation coefficient ranges from − 1 to 1, where one means identical rankings,
minus one means reversed rankings, and zero indicates uncorrelated rankings.
3.3.2  WS rank similarity coefficient
The Weighted Similarity, rank similarity coefficient, is an asymmetrical measure of the
ranking similarities proposed by  (Sałabun and Urbaniak 2020). This approach gives more
weight to the changes in the head of the rankings, and therefore, the correlation drops
significantly when, for example, first and last positions are swapped. The similarity value
between two rankings xi and yi of size N can be calculated as (9):
The WS rank similarity coefficient belongs to domain [0,  1], where zero means
uncorrelated rankings and one means identical rankings.
(8)rW = 1 − 6⋅∑(xi −yi )2 ((n−xi +1)+(n−yi +1)) n⋅(n3 +n2 −n−1)
(9)WS = 1 − ∑ � 2−xi �xi −yi � m ax{�xi −1�,�xi −N�} �

Adaptive multi‑criteria decision making for electric vehicles:…
Page 11 of 25 270
4  Study case
Proposing individualized decision support systems that incorporate the personalized
preferences of decision-makers is essential for providing tailored and effective recom-
mendations aligned with their specific needs. Capturing and understanding individuals’
unique preferences and priorities is crucial for these systems to offer more relevant and
targeted suggestions. This personalized approach enhances user satisfaction and trust
in the decision support system, as it considers the intricacies of each decision-maker’s
objectives and values. Tailored suggestions improve the decision-making process and
increase the likelihood of decisions aligning with individual goals. In complex and
dynamic decision-making environments, where general solutions may be insufficient,
individualized decision support systems empower users with customized insights, fos-
tering more informed and confident decision-making. Integrating personalized prefer -
ences into decision support systems ultimately contributes to a more user-centric and
efficient decision-making experience.
To this end, this paper proposes a new approach for developing personalized
decision support systems based on decision-maker preference-driven requirements. The
RANCOM method is integrated with the ESP-SPOTIS technique to model decision-
makers’ preferences for the relevance of criteria weights and to evaluate options by
indicating the expected solution. This combination allows for creating a decision model
that is closely aligned with individualized preferences, incorporating subjective opinions
and needs in two main steps of multi-criteria evaluation. The aim of integrating the
subjective weighting method with the expected solution point concept is to offer a novel
way of supporting individuals in complex decision problems, addressing their needs in
both dimensions of multi-criteria decision analysis. To verify the proposed approach,
the RANCOM ESP-SPOTIS method was applied to the electric vehicle selection
problem. The individual decision-maker evaluated the importance of various criteria
Initialization of the decision-making process
STEP 1
Identify decision matrix
STEP 2
Assess criteria by
using RANCOM
STEP 3
Determine
expected solution
Perform sensitivity analysis
STEP 4
Assess electric vehicles by using
RANCOM ESP-SPOTIS
STEP 6
Provide the customer with
the final recommendation
STEP 5.1
EQUAL ESP-SPOTIS
STEP 5.2
RANCOM ESP-COMET
STEP 5.3
RANCOM TOPSIS
Fig. 2  Flowchart representing the subsequent research step with determining the preference-driven DSS for
electric vehicle selection

 J. Więckowski et al.
270 Page 12 of 25
using the RANCOM method and then determined the expected solution regarding
specific electric vehicle parameters. These extracted preferences were used to assess
electric vehicles using the RANCOM ESP-SPOTIS approach, which provides results
aligned with the indicated needs. The robustness of the obtained results was examined
using a selected sensitivity analysis approach. This included evaluating the problem
with the equal weights ESP-SPOTIS method, the RANCOM ESP-COMET method,
and the RANCOM TOPSIS method to demonstrate how results vary across different
methods. Based on this assessment, customer recommendations were defined to propose
the most suitable choice aligning with the previously determined preferences. This
comprehensive validation ensures that the proposed hybrid model offers a reliable and
effective decision support system tailored to individual customer needs. The flow of the
study, describing the subsequent steps of analysis, is presented in Fig. 2 .
To evaluate the electric vehicles, 15 criteria were selected, contributing to the significant
dimensionality of the problem. Since the subjective weighting method is engaged in
the assessment process, it was worth selecting the technique that minimizes potential
inaccuracies of the decision-maker judgment. To this end, the RANCOM method was used
for this purpose as it proves to be a reliable tool for determining criteria weights, especially
in decision problems with numerous criteria Więckowski et  al. (2023). The considered
criteria for the problem of personal purpose electric vehicle selection were presented in
Table 1, where the name, unit, and type of criterion were included. Moreover, the ranking
of criteria determined for the RANCOM method was presented, with the criteria weights
calculated with this method. It is worth mentioning that the examined decision-maker was
seeking a compact car to drive mainly in the city center. Based on the defined rankings and
obtained criteria weights, it could be seen that the three most important factors were cost
( C1 : 0.129), charge time from 10% to 80% ( C14 : 0.120), and number of doors ( C10 : 0.111).
On the other hand, the three least important criteria were maximum torque ( C3 : 0.009),
maximum load capacity ( C8 : 0.009), and tire size ( C11 : 0.022).
As the initial set of analyzed decision variants, the publicly available dataset, includ-
ing information about the selected electric vehicles, was used Hadasik and Kubiczek
Table 1  Set of criteria
considered in the electric vehicle
selection problem with ranking
of criteria and calculated weights
Ci Name Unit Type Ranking Weight
C1 Cost PLN Cost 1 0.129
C2 Engine power Hp Profit 7 0.071
C3 Maximum torque Nm Profit 13 0.009
C4 Drive type Unit Profit 11 0.031
C5 Battery capacity kWh Profit 6 0.084
C6 Range Km Profit 7 0.071
C7 Length cm Profit 10 0.040
C8 Maximum load capacity kg Profit 13 0.009
C9 Number of seats Unit Profit 9 0.049
C10 Number of doors Unit Profit 3 0.111
C11 Tire size inches Profit 12 0.022
C12 Maximum speed kph Profit 8 0.058
C13 Boot capacity litres Profit 5 0.093
C14 Charge time 10–80% 50kW minutes Cost 2 0.120
C15 Full charge time 22kW minutes Cost 4 0.102

Adaptive multi‑criteria decision making for electric vehicles:…
Page 13 of 25 270
(2021). This dataset contains 53 electric cars. However, to limit the number of consid-
ered decision variants, the data preprocessing included filtering cars by the length of
the vehicle given in the centimeters, with removal alternatives that had lengths greater
than 420. Since the study was directed to seek a compact car mainly for driving in the
city center, bigger cars were removed from the consideration area. To this end, the final
set of alternatives included 19 electric vehicles. Moreover, the preprocessing included
converting categorical data of drive type ( C4 ) to numerical data. Two categorical values
were in the initial data (2WD (rear) and 2WD (front)). To this end, they were converted
to numerical values as 2WD (rear) was signed as 0, and the 2WD (front) was repre-
sented as 1 in the data. The decision matrix representing the considered alternatives was
presented in Table  2. It is worth mentioning that the values in the decision matrix were
gathered from two sources, from Hadasik and Kubiczek (2021) for criteria C1 − C13 , and
from EV-Database (2023) for criteria C14 − C15 . Moreover, with the data describing the
subsequent alternatives regarding the considered criteria, the expected solution points
determined for each criterion separately by the decision-maker were presented as the
last row of the table. It could be seen that each ESP is placed within the bounds of the
given criterion from the decision matrix, which was the main requirement to indicate
values from the specific range. The presented data were then used in the RANCOM
ESP-SPOTIS decision model to evaluate the alternatives based on the preferences pro-
vided by the decision-maker. Moreover, the ESP-SPOTIS calculations were performed
based on the functionality available in the pymcdm package Kizielewicz et al. (2023);
Shekhovtsov et al. (2023).
Table 2  Decision matrix representing the electric vehicles considered in the customer recommendation
analysis
Ai C1 C2 C3 C4 C5 C6 C7 C8 C9 C10 C11 C12 C13 C14 C15
A1 169700 170 250 0 42.2 359 400.6 440 4 5 19 160 260 36 255
A2 184200 184 270 0 42.2 345 400.6 440 4 5 20 160 260 36 255
A3 159900 136 260 1 50.0 320 411.8 450 5 5 17 150 350 42 450
A4 152900 136 315 0 35.5 222 389.4 342 5 5 16 145 171 39 315
A5 165900 154 315 0 35.5 222 389.4 350 5 5 17 145 171 39 315
A6 154400 136 395 1 39.2 289 418.0 485 5 5 17 155 332 47 390
A7 178400 204 395 1 64.0 449 418.0 485 5 5 17 167 332 63 420
A8 139900 136 395 1 39.2 276 419.5 490 5 5 17 157 315 47 390
A9 160990 204 395 1 64.0 452 419.5 498 5 5 17 167 315 63 630
A10 139900 184 270 1 28.9 234 384.5 480 4 3 16 150 211 54 315
A11 128900 136 260 1 50.0 337 406.0 367 5 5 16 150 267 42 435
A12 139900 136 260 1 50.0 324 415.1 417 5 5 16 150 310 42 450
A13 124900 136 260 1 50.0 340 405.5 463 5 5 16 150 311 42 450
A14 135900 108 225 1 52.0 395 408.5 425 5 5 15 135 338 56 180
A15 142900 135 245 1 52.0 395 408.5 486 5 5 16 140 338 56 180
A16 82050 83 212 1 36.8 260 359.7 367 4 5 14 130 250 48 330
A17 96900 82 160 0 17.6 154 269.5 290 2 3 15 130 185 21 270
A18 98900 82 160 0 17.6 148 349.5 445 4 5 15 130 260 21 270
A19 97990 83 210 1 32.3 258 360.0 370 4 5 14 130 250 48 330
ESP 100000 120 300 1 40.0 300 380.0 400 5 5 16 160 280 25 300

 J. Więckowski et al.
270 Page 14 of 25
Results from the determined MCDA model were presented in Table  3. The calcu-
lated preference scores were indicated, with additional information about the distance
from the evaluated best alternative represented as a difference of preference scores, the
percentage from the best alternative represented as a division of the preference score of
the given alternative by the best preference score, and the ranking position assigned to a
given alternative. It could be seen that the spread of the calculated preference scores is
significant across the analyzed decision variants. The proposed approach for supporting
decisions based on the preference-driven evaluation with the RANCOM ESP-SPOTIS
methods showed that the alternative A11 is the most suitable choice based on the defined
needs. The second most recommended vehicle was A13 , and the third recommendation
was to select alternative A8 . On the other hand, the least recommended electric vehicles
were A17 (19th), A9 (18th), and A7 (17th).
Furthermore, it could be seen that the differences in the top-ranked alternatives regarding
calculated preference scores were minor. The difference between 1st and 3rd position was
0.0105, showing the 6% difference. On the other hand, an even lower difference was noted
between the 2nd and 3rd position, where the preference scores differed by 0.0009, which
represented a 1% difference. It showed that electric vehicles in 2nd and 3rd places were
evaluated as highly similar and could be selected interchangeably. At the same time, the final
decision could rely only on the specific preferences of the decision-maker regarding the brand
or the visual aspect of the car. Moreover, it is worth mentioning that the first 6 alternatives were
evaluated within the 20% difference, while the preference scores of the first 10 alternatives
Table 3  Preference scores and
positional ranking obtained from
RANCOM ESP-SPOTIS model
based on customer’s ESP
Ai Preference score Difference
from best
Percentage
from best (%)
Ranking
A1 0.2546 0.0705 138 9
A2 0.2807 0.0966 152 12
A3 0.2584 0.0742 140 10
A4 0.2628 0.0787 143 11
A5 0.2931 0.1090 159 13
A6 0.2213 0.0371 120 6
A7 0.4214 0.2372 229 17
A8 0.1947 0.0105 106 3
A9 0.4399 0.2557 239 18
A10 0.3943 0.2102 214 16
A11 0.1841 0.0000 100 1
A12 0.2090 0.0249 113 4
A13 0.1937 0.0096 105 2
A14 0.2967 0.1125 161 14
A15 0.2976 0.1135 162 15
A16 0.2283 0.0441 124 7
A17 0.4499 0.2657 244 19
A18 0.2418 0.0577 131 8
A19 0.2167 0.0325 118 5

Adaptive multi‑criteria decision making for electric vehicles:…
Page 15 of 25 270
were placed in the 40% range, showing that many alternatives are evaluated relatively similarly.
The final decision remains to the decision-maker, and the proposed approach for preference-
driven decision support systems should aim to provide accurate recommendations to meet the
individualized demands of the customer in the considered problem. Furthermore, providing
additional information about the percentage differences between the subsequently ranked
alternatives could lead to more informed and rational decisions, showing the advantages of
selecting given decision variants or sacrificing some of the desirability of a given alternative at
the expense of choosing another alternative that is more convincing to the customer.
5  Sensitivity analysis
Utilizing sensitivity analysis in MCDA is crucial as it provides valuable insights into the
robustness and stability of decision outcomes against varying parameters and criteria
relevance. Sensitivity analysis evaluates how changes in input values, criteria weights, or
decision model structures impact final rankings and recommendations. This process gives
decision-makers a deeper understanding of the reliability and consistency of the chosen
MCDA method. By identifying influential factors and potential differences in preferences,
sensitivity analysis enhances decision-making models, increases the credibility of results,
and improves the overall decision-making process. Furthermore, it promotes transparency
by enabling decision-makers to comprehend the implications of uncertainty and change
within the decision-making context, thus supporting more informed and resilient decision-
making strategies.
To compare the results obtained with the RANCOM ESP-SPOTIS methods, three tech-
niques were applied to evaluate the considered problem and verify if the proposed rec-
ommendations will differ. To this end, the equal weights ESP-SPOTIS, RANCOM ESP-
COMET, and RANCOM TOPSIS methods were used. The first approach concerning the
equal weights ESP-SPOTIS method was applied to examine if modeling criteria relevance
equally would cause significant differences in the obtained rankings. Since the subjective
weighting techniques allow for representing the individual preferences of decision-makers,
it was worth comparing the results when criteria would have equal relevance in the prob-
lem. Thus, with this approach, it was possible to omit the subjectivity of the criteria weight-
ing process and focus only on the expected solution determined for the SPOTIS method.
The comparison of the calculated rankings is presented in Fig. 3. It could be seen that from
Fig. 3  Rankings comparison of RANCOM ESP-SPOTIS and equal weights ESP-SPOTIS methods

 J. Więckowski et al.
270 Page 16 of 25
19 considered alternatives, only 4 decision variants were classified in the same positions
in both rankings. However, what should be noted is that the most recommended electric
vehicle is the same within the two examined methods. Other equally ranked alternatives
were placed at 17th, 18th, and 19th positions. Furthermore, the alterations were visible in
the top and middle parts of the ranking. It shows that modeling criteria weights based on
subjective techniques should be included in the decision models determined based on the
ESP concept since it leads to different results than in the case of equal criteria relevance.
The next comparison included using two MCDA methods with ESP concept exten-
sion to verify if those techniques provide similar results. For this purpose, weights
determined from the RANCOM method were used in the evaluation process with the
ESP-COMET method. Since the COMET method bases its calculation on generating a
Matrix of Expert Judgement (MEJ) for which the Characteristic Objects (COs) are gen-
erated and compared, its computational and memory complexity is significant Sałabun
(2014). For the considered problem of electric vehicle evaluation with 19 alternatives
and 15 criteria, the MEJ would have the size of (4251528,  4251528), which exceeds
the capabilities of a standard computational device. To this end, to reduce the problem
dimensionality, the problem was divided into smaller sub-models by splitting the prob-
lem into three parts, each concerning 5 criteria, according to the Structural COMET
approach Shekhovtsov et  al. (2023). The P1 sub-model consisted criteria C1 − C5 ,
sub-model P2 included criteria C6 − C10 , and P3 aggregated criteria C11 − C15 . Each
Fig. 4  Rankings comparison of RANCOM ESP-SPOTIS and RANCOM ESP-COMET methods
Fig. 5  Rankings comparison of RANCOM ESP-SPOTIS and RANCOM TOPSIS methods

Adaptive multi‑criteria decision making for electric vehicles:…
Page 17 of 25 270
sub-model was treated as an input for the final model, for which the equal importance of
the sub-models was used. Thanks to this, the problem dimensionality was significantly
reduced. The rankings comparison was presented in Fig.  4. Only two alternatives were
classified in the same position, namely 1st in the ranking alternative A11 , and 2nd in
the ranking alternative A13 . Other decision variants were classified differently regard-
ing the methods used. The most visible difference could be observed for the alternative
A8 , which by the RANCOM ESP-SPOTIS method was ranked at 4th place, while for
the RANCOM ESP-COMET method, it was placed 17th. However, despite some vis-
ible alterations, selected decision variants were classified similarly in both rankings, for
example, alternatives A4 , A9 , A12 , or A17.
The last comparison included using the RANCOM TOPSIS method. The aim was to
present how the results differ when ESP and ISP concepts are used within the same prob-
lem, having subjective criteria weights as one of the input data elements. The visualization
of the rankings comparison was presented in Fig.  5. In this case, three electric vehicles
were ranked equally, namely alternative A2 in 12th position, A18 in 8th position, and A12
in 4th place. On the other hand, it should be noted that the most recommended decision
variant for the RANCOM TOPSIS method was A13 , which with the RANCOM ESP-SPO-
TIS method, was placed in 2nd position, showing high similarity in this regard. Further -
more, the alternative A11 ranked 1st with the RANCOM ESP-SPOTIS, for the RANCOM
TOPSIS, it was classified in 3rd position. The significant discrepancies could be seen for
alternatives A14 and A15 , which were placed 5th and 2nd, respectively, for the RANCOM
TOPSIS approach, while for the RANCOM ESP-SPOTIS, they were ranked 14th and 15th.
To present the similarities of the results obtained from the examined methods, Weighted
Similarity (WS) and Weighted Spearman ( rW ) coefficients were used. The visualization of
the obtained correlation values was presented in Fig.  6. From the indicated similarities,
it could be noted that the most coherent results were produced by the RANCOM ESP-
SPOTIS and equal weights ESP-SPOTIS methods, with WS  similarity around 0.96, and
rW similarity of 0.89. On the other hand, the least correlated rankings were indicated by
the RANCOM ESP-SPOTIS and RANCOM TOPSIS methods, showing correlation value
of around 0.74 to 0.87 for the WS  coefficient and 0.57 for the rW coefficient. Moreover, it
should be noted that the RANCOM TOPSIS method provided lower similarity values than
Fig. 6  Heatmap correlation of WS and rW similarity coefficients for the examined evaluation approaches

 J. Więckowski et al.
270 Page 18 of 25
other examined methods. Thus, it emphasized the fact that the ESP concept provides sig-
nificantly different results than the ISP within the multi-criteria evaluations.
In addition, since the decision-maker indicated the expected solution point at the ini-
tial phase of the evaluation, it was worth comparing the proposed recommendation with
the actual expectations. For this purpose, the visualization of values distribution for three
best-ranked alternatives with the examined methods was presented in Fig. 7. For the RAN-
COM ESP-SPOTIS recommendations, it could be seen that most values representing the
characteristics of electric vehicles regarding the considered criteria were placed in the
range of 90% and 130% of the expected value. The significantly higher values compared
to defined expectations were observed for the criterion C14 , representing the fast charge
time from 10% to 80%. On the other hand, for the values spread for the three top electric
vehicles determined with the equal weights ESP-SPOTIS method, the spread of values dis-
tribution was mainly placed between 90% and 120%. For the criterion C14 , the maximum
value regarding the expected one was about 170% higher. For the RANCOM ESP-COMET
method, the distribution of the values regarding the ESP was the same as in the case of the
equal weights ESP-SPOTIS since both methods indicated the same alternatives as the top
three recommendations, but the 2nd and 3rd positions were assigned to alternatives in the
reversed order. Furthermore, the most visible spread was observed for the recommended
electric vehicles from the RANCOM TOPSIS method. For criteria C1 − C13 , the distribu-
tion values were similar to those for other examined methods. However, the differences
regarding the indicated ESP were significant for the C14 and C15 . For the former criterion,
the 2nd proposed alternative had 220% of the expected one. Despite the visibly worse per -
formance regarding the fast charge time, the full charge time ( C15 ) was lower than expected
by about 40%, which could compensate for the losses regarding the fast charge time.
Providing decision-makers with insights into the differences between the expected
solution and the recommended variants can offer additional knowledge about potential
choices, enabling more informed and conscious decisions. By analyzing the presented
visualizations, decision-makers can make final decisions based on achieving a compromise
and considering significant differences in expected values. The verification process
demonstrated the necessity of sensitivity analysis in identifying disparities in MCDA
Fig. 7  Comparison of values distribution of three best-ranked alternatives regarding the determined by the
decision-maker the ESP

Adaptive multi‑criteria decision making for electric vehicles:…
Page 19 of 25 270
recommendations, validating the proposed hybrid model’s robustness, and ensuring that
decision-maker preferences are accurately reflected in the final outcomes.
6  Discussion
Incorporating individual preferences of decision-makers in modeling criteria weights and
indicating the ESP in MCDA within personalized decision support systems is essential for
enhancing the relevance and effectiveness of decision outcomes. Decision-makers often
have unique priorities, values, and subjective assessments that significantly influence
their preferences for different criteria. By integrating these individual preferences into
the modeling of criteria weights, the decision process becomes more tailored and aligned
with the specific needs and objectives of the decision-maker. Similarly, indicating the ESP
allows decision-makers to express their preferred outcomes, ensuring that the decision
analysis aligns with their personalized expectations. This personalized approach improves
the accuracy of the decision outcomes and fosters increased user satisfaction and trust in
the decision support system. It acknowledges the inherent subjectivity in decision-making,
providing a more adaptable framework that resonates with the individual decision-maker’s
perspective.
The practical implications of the performed MCDA evaluation involving individualized
decision support systems should be emphasized. By tailoring decision support systems
to incorporate the personalized preferences of decision-makers, the analysis becomes
more aligned with specific needs, leading to more relevant and targeted suggestions. The
personalized approach enhances user satisfaction and trust in the decision support system
and improves the decision-making process by aligning outcomes with individual goals.
In complex decision environments where generic solutions may not fulfill the required
objectives, individualized decision support systems empower users with customized
insights, fostering more informed and confident decision-making. The proposed approach,
integrating the RANCOM method with the ESP-SPOTIS technique, exemplifies this
by allowing decision-makers to express their preferences in two critical dimensions of
MCDA: criteria weights and the expected solution point. The case study involving electric
vehicle selection emphasizes how this personalized approach aids decision-makers in
evaluating alternatives based on their specific needs, leading to well-informed and robust
recommendations.
The proposed approach directed toward a new hybrid approach for personalized
decision support systems has the potential to be used in practical scenarios. Consumers can
be provided with effective tools that enable them to quickly analyze decision options and
select the one that best meets their requirements. As the number of products and services
available to consumers continues to grow, it becomes increasingly challenging for them
to compare options analytically. Decision support systems can address this challenge by
incorporating personalized assessment processes for both criteria weights and reference
points. These systems allow consumers to specify their individual preferences and
priorities, which enhances the efficiency and accuracy of the decision-making process.
By leveraging advanced algorithms and user-friendly interfaces, these tools empower
consumers to make well-informed decisions under uncertainty. This personalized approach
simplifies the comparison of numerous options and ensures that the selected option aligns
closely with the consumer’s specific needs and preferences, ultimately improving their
satisfaction and decision-making experience.

 J. Więckowski et al.
270 Page 20 of 25
Furthermore, the study incorporates sensitivity analysis approaches within multi-
criteria assessment, emphasizing the importance of examining the robustness of results
against changing parameters and criteria relevance. Sensitivity analysis provides decision-
makers with valuable insights into the reliability and consistency of the chosen MCDA
method, helping them understand the impact of variations in input values on final rankings
and recommendations. This approach contributes to more transparent and informed
decision-making strategies, ensuring that decision-makers are aware of the implications of
uncertainty and changes in the decision context. The comparison of results using selected
MCDA methods, including equal weights ESP-SPOTIS, RANCOM ESP-COMET,
and RANCOM TOPSIS, demonstrated the possible variations in recommendations and
highlighted the significance of considering individual preferences. Employing sensitivity
analysis offers a comprehensive understanding of DSS model outcomes, underscoring the
need for personalized and adaptable decision support systems. The study showcases the
practical benefits of a robust MCDA approach in supporting decision-makers in complex
scenarios, demonstrating how personalized decision-making models can enhance the
effectiveness and relevance of recommendations.
To this end, the proposed approach for developing preference-driven decision support
systems showed that integrating subjective weighting techniques with the expected
solution point concept within the MCDA methods could lead to an improved decision-
making process regarding personalized recommendations. The performed analysis of
the robustness of the results showed that it is worth incorporating the criteria weights
determined with the subjective methods since treating criteria equally important while
using the ESP in multi-criteria calculations could lead to different results. Moreover,
it should be mentioned that the developed decision support system for electric vehicle
selection is an illustrative example of how the proposed approach could be utilized in the
practical problem. Furthermore, the determined flow of the DSS application could be used
with other practical problems where customers have their individual and specific needs.
7  Conclusions
Modeling individual preferences of decision-makers regarding criteria weights
and indicating the ESP in MCDA methods is vital for enhancing the relevance and
effectiveness of decision outcomes. Recognizing the unique priorities, values, and
subjective assessments of decision-makers significantly influences the customization
of criteria weights, tailoring the decision process to specific needs. Indicating the ESP
enables decision-makers to express their requirements, aligning the analysis with their
personalized expectations. The study proposed a new approach for determining dedicated
decision support systems based on the decision-maker preference driver requirements.
For this purpose, the RANCOM method was integrated with the ESP-SPOTIS technique
to enable modeling decision-makers preferences for the relevance of criteria weights and
in the evaluation process by indicating the expected solution. The practical implications,
particularly in electric vehicle selection, highlight the benefits of a personalized and robust
MCDA approach, providing users with customized insights in complex decision scenarios.
Furthermore, the incorporation of sensitivity analysis informs decision-makers about the
reliability and consistency of the given MCDA method. The proposed approach presents a
versatile and adaptable framework that can be applied to various decision problems where
individualized preferences play a crucial role.

Adaptive multi‑criteria decision making for electric vehicles:…
Page 21 of 25 270
For further direction, it is worth verifying the proposed approach in other practical
multi-criteria problems engaging the individual preferences of decision-makers. In
addition, the credibility of the obtained results could be examined by applying selected
popular subjective weighting techniques. Since the expected solution point concept proved
to be a significant advancement in personalized decision-making, it is worth extending
existing MCDA methods to handle the ESP modeling within its calculation procedure.
Acknowledgements This research was Co-financed by the Minister of Science under the "Regional Excel-
lence Initiative" Program.
Author contributions Jakub Więckowski was responsible for conceptualization, methodology, software
development, validation, formal analysis, investigation, resource management, data curation, writing
the original draft, reviewing and editing the manuscript, as well as visualization. Jarosław Wątróbski
was responsible for formal analysis, investigation, writing of original draft, and review and editing of
the manuscript. Anna Shkurina was responsible for validation, formal analysis, as well as reviewing and
editing the manuscript Wojciech Sałabun was responsible for conceptualization, methodology, validation,
investigation, writing the original draft, reviewing and editing the manuscript, supervising the project,
handling project administration tasks, and acquiring funding for the project.
Data availability No datasets were generated or analysed during the current study.
Declarations
Competing interests The authors declare no competing interests.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License,
which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long
as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Com-
mons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the
material. If material is not included in the article’s Creative Commons licence and your intended use is not
permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
References
Akram M, Ramzan N, Deveci M (2023) Linguistic pythagorean fuzzy CRITIC-EDAS method for multiple-
attribute group decision analysis. Eng Appl Artif Intell 119:105777
Alemi-Ardakani M, Milani AS, Yannacopoulos S, Shokouhi G (2016) On the effect of subjective, objective
and combinative weighting in multiple criteria decision making: a case study on impact optimization
of composites. Expert Syst Appl 46:426–438
Ayan B, Abacıoğlu S, Basilio MP (2023) A comprehensive review of the novel weighting methods for
multi-criteria decision-making. Information 14(5):285
Bairagi B (2023) A new framework for green selection of material handling equipment under fuzzy environ-
ment. Decis Mak: Appl Manag Eng 6(1):57–69
Biswas S, Božanić D, Pamučar D, Marinković D (2023) A spherical fuzzy based decision making frame-
work with Einstein aggregation for comparing preparedness of SMEs in quality 4.0. Facta Univ, Ser:
Mech Eng 21(3):453–478
Cables E, Lamata MT, Verdegay JL (2016) RIM-reference ideal method in multicriteria decision making.
Inform Sci 337:1–10
Ceballos B, Lamata MT, Pelta DA (2016) A comparative analysis of multi-criteria decision-making meth-
ods. Progress Artif Intell 5:315–322
Chakraborty S, Yeh C-H (2009) A simulation comparison of normalization procedures for TOPSIS. In:
2009 International conference on computers & industrial engineering, pp. 1815–1820. IEEE

 J. Więckowski et al.
270 Page 22 of 25
Chang K-H (2023) Integrating subjective-objective weights consideration and a combined compromise
solution method for handling supplier selection issues. Systems 11(2):74
Chatterjee P, Chakraborty S (2016) A comparative analysis of VIKOR method and its variants. Decis Sci
Lett 5(4):469–486
Chen T-Y (2015) An interval type-2 fuzzy LINMAP method with approximate ideal solutions for multiple
criteria decision analysis. Inform Sci 297:50–79
Chen T-Y (2019) A novel VIKOR method with an application to multiple criteria decision analysis for
hospital-based post-acute care within a highly complex uncertain environment. Neural Comput Appl
31:3969–3999
Chen Y, Li KW, Liu S-F (2011) An OWA-TOPSIS method for multiple criteria decision analysis. Expert
Syst Appl 38(5):5205–5211
Chou S-Y, Chang Y-H, Shen C-Y (2008) A fuzzy simple additive weighting system under group deci-
sion-making for facility location selection with objective/subjective attributes. Eur J Oper Res
189(1):132–145
Dağıstanlı HA (2024) An interval-valued intuitionistic fuzzy VIKOR approach for R &D project selection
in defense industry investment decisions. J Soft Comput Decis Anal 2(1):1–13
Dancelli L, Manisera M, Vezzoli M (2013) On two classes of weighted rank correlation measures deriv -
ing from the spearman’s 𝜌 . Statistical models for data analysis. Springer, Cham, pp 107–114
Dezert J, Tchamova A, Han D, Tacnet J-M (2020) The SPOTIS rank reversal free method for multi-cri-
teria decision-making support. In: 2020 IEEE 23rd International conference on information fusion
(FUSION), pp. 1–8. IEEE
Dheena P, Mohanraj G (2011) Multicriteria decision-making combining fuzzy set theory, ideal and anti-
ideal points for location site selection. Expert Syst Appl 38(10):13260–13265
EV-Database: Electric Vehicle Database. https:// ev- datab ase. org/. [Online; accessed 06-December-2023]
(2023)
Ezell B, Lynch CJ, Hester PT (2021) Methods for weighting decisions to assist modelers and decision
analysts: a review of ratio assignment and approximate techniques. Appl Sci 11(21):10397
Ganti A (2020) Correlation coefficient. Corp. Financ. Account 9:145–152
Giove S, Brancia A, Satterstrom FK, Linkov I (2009) Decision support systems and environment: Role
of MCDA. In: Decision support systems for risk-based management of contaminated sites, 1–21
Gökalp Y, Dinçer H, Eti S, Yüksel S (2024) Generating a novel artificial intelligence-based decision-
making model for determining priority strategies for improving community health. J Oper Intell
2(1):1–13
Guo M, Liao X, Liu J, Zhang Q (2020) Consumer preference analysis: a data-driven multiple criteria
approach integrating online information. Omega 96:102074
Hadasik B, Kubiczek J (2021) Dataset of electric passenger cars with their specifications. Mendeley
Data V2 https:// doi. org/ 10. 17632/ tb9yr ptydn.2
Hashemkhani Zolfani S, Yazdani M, Zavadskas EK (2018) An extended stepwise weight assessment ratio
analysis (SW ARA) method for improving criteria prioritization process. Soft Comput 22:7399–7405
Herrera-Viedma E, Palomares I, Li C-C, Cabrerizo FJ, Dong Y, Chiclana F, Herrera F (2020) Revisiting
fuzzy and linguistic decision making: scenarios and challenges for making wiser decisions in a bet-
ter way. IEEE Trans Syst, Man, Cybern: Syst 51(1):191–208
Hezer S, Gelmez E, Özceylan E (2021) Comparative analysis of topsis, vikor and copras methods for the
covid-19 regional safety assessment. J Infect Public Health 14(6):775–786
Isen AM (2001) An influence of positive affect on decision making in complex situations: theoretical
issues with practical implications. J Consum Psychol 11(2):75–85
Kara K, Yalçın GC, Kaygısız EG, Edinsel S (2024) Assessing the academic performance of Turkish Uni-
versities in 2023: a MEREC-WEDBA hybrid methodology approach. J Oper Intell 2(1):252–272
Keshavarz Ghorabaee M, Zavadskas EK, Turskis Z, Antucheviciene J (2016) A new combinative dis-
tance-based assessment (CODAS) method for multi-criteria decision-making. Econ Comput Econ
Cybern Stud Res 50(3):1
Keshavarz-Ghorabaee M, Amiri M, Zavadskas EK, Turskis Z, Antucheviciene J (2018) An extended step-
wise weight assessment ratio analysis with symmetric interval type-2 fuzzy sets for determining the
subjective weights of criteria in multi-criteria decision-making problems. Symmetry 10(4):91
Kizielewicz B, Shekhovtsov A, Sałabun W (2023) pymcdm-The universal library for solving multi-crite-
ria decision-making problems. SoftwareX 22:101368
Koksalmis E, Kabak Ö (2019) Deriving decision makers’ weights in group decision making: an over -
view of objective methods. Inform Fusion 49:146–160
Krishnan AR, Kasim MM, Hamid R, Ghazali MF (2021) A modified CRITIC method to estimate the
objective weights of decision criteria. Symmetry 13(6):973

Adaptive multi‑criteria decision making for electric vehicles:…
Page 23 of 25 270
Kumar R, Singh S, Bilga PS, Singh J, Singh S, Scutaru M-L, Pruncu CI et al (2021) Revealing the ben-
efits of entropy weights method for multi-objective optimization in machining operations: a critical
review. J Market Res 10:1471–1492
Liu S, Chan FT, Ran W (2016) Decision making for the selection of cloud vendor: an improved approach
under group decision-making with integrated weights and objective/subjective attributes. Expert
Syst Appl 55:37–47
Liu Y, Eckert CM, Earl C (2020) A review of fuzzy AHP methods for decision-making with subjective
judgements. Expert Syst Appl 161:113738
Liu P, Zhu B, Wang P (2021) A weighting model based on best-worst method and its application for
environmental performance evaluation. Appl Soft Comput 103:107168
Lo H-W, Wang L-Y, Weng AK-W, Lin S-W (2024) Assessing supplier disruption risks using a modified
Pythagorean fuzzy SWARA-TOPSIS approach. J Soft Comput Decis Anal 2(1):169–187
Mahmoudi A, Javed SA (2023) Uncertainty analysis in group decisions through interval ordinal priority
approach. Group Decis Negot 32:1–27
Mahmutagić E, Stević Ž, Nunić Z, Chatterjee P, Tanackov I (2021) An integrated decision-making model for
efficiency analysis of the forklifts in warehousing systems. Facta Univ, Ser: Mech Eng 19(3):537–553
Martínez-Torres MDR, Rodriguez-Piñero F, Toral SL (2015) Customer preferences versus managerial
decision-making in open innovation communities: the case of Starbucks. Technol Anal Strat Manag
27(10):1226–1238
Marttunen M, Belton V, Lienert J (2018) Are objectives hierarchy related biases observed in practice? A
meta-analysis of environmental and energy applications of Multi-Criteria Decision Analysis. Eur J
Oper Res 265(1):178–194
Mukhametzyanov I (2021) Specific character of objective methods for determining weights of criteria in
MCDM problems: entropy, CRITIC and SD. Decis Mak: Appl Manag Eng 4(2):76–105
Nowak M (2007) Aspiration level approach in stochastic MCDM problems. Eur J Oper Res
177(3):1626–1640
Odu G (2019) Weighting methods for multi-criteria decision making technique. J Appl Sci Environ Manag
23(8):1449–1457
Pamucar D, Ecer F (2020) Prioritizing the weights of the evaluation criteria under fuzziness: the fuzzy full
consistency method-FUCOM-F. Facta Univ, Ser: Mech Eng 18(3):419–437
Pamučar D, Stević Ž, Sremac S (2018) A new model for determining weight coefficients of criteria in mcdm
models: full consistency method (fucom). Symmetry 10(9):393
Paradowski B, Shekhovtsov A, Bączkiewicz A, Kizielewicz B, Sałabun W (2021) Similarity analysis of
methods for objective determination of weights in multi-criteria decision support systems. Symmetry
13(10):1874
Paramanik AR, Sarkar S, Sarkar B (2022) OSWMI: an objective-subjective weighted method for minimiz-
ing inconsistency in multi-criteria decision making. Comput Ind Eng 169:108138
Podvezko V, Zavadskas EK, Podviezko A (2020) An extension of the new objective weight assessment
methods CILOS and IDOCRIW to fuzzy MCDM. Econ Comput Econ Cybern Stud Res 54(2):1
Razmak J, Aouni B (2015) Decision support system and multi-criteria decision aid: a state of the art and
perspectives. J Multi-Crit Decis Anal 22(1–2):101–117
Şahin M (2021) Location selection by multi-criteria decision-making methods based on objective and sub-
jective weightings. Knowl Inform Syst 63(8):1991–2021
Sałabun W (2014) Reduction in the number of comparisons required to create matrix of expert judgment in
the comet method. Manag Prod Eng Rev 5(3):62–69
Sałabun W, Wątróbski J, Shekhovtsov A (2020) Are MCDA methods benchmarkable? A comparative study
of TOPSIS, VIKOR, COPRAS, and PROMETHEE II methods. Symmetry 12(9):1549
Sałabun W, Urbaniak K (2020) A new coefficient of rankings similarity in decision-making problems. In:
Computational Science–ICCS 2020: 20th International Conference, Amsterdam, The Netherlands,
June 3–5, 2020, Proceedings, Part II 20, pp. 632–645. Springer
Sarfraz M (2024) Application of interval-valued T-spherical fuzzy Dombi Hamy mean operators in the anti-
viral mask selection against COVID-19. J Decis Anal Intell Comput 4(1):67–98
Sennaroglu B, Celebi GV (2018) A military airport location selection by ahp integrated promethee and
vikor methods. Transp Res Part D: Transp Environ 59:160–173
Shekhovtsov A (2022) Decision-making process customization by using expected solution point. Procedia
Comput Sci 207:4556–4564
Shekhovtsov A, Kizielewicz B, Sałabun W (2023) Advancing individual decision-making: an extension of
the characteristic objects method using expected solution point. Inform Sci 647:119456
Shekhovtsov A, Kizielewicz B, Sałabun W (2023) Version [1.1]-[pymcdm–The universal library for solving
multi-criteria decision-making problems]. SoftwareX 24:101519

 J. Więckowski et al.
270 Page 24 of 25
Shekhovtsov A, Więckowski J, Wątróbski J (2021) Toward reliability in the mcda rankings: Comparison of
distance-based methods. In: Intelligent decision technologies: proceedings of the 13th KES-IDT 2021
conference, pp. 321–329. Springer
Sitorus F, Brito-Parada PR (2022) The selection of renewable energy technologies using a hybrid subjective
and objective multiple criteria decision making method. Expert Syst Appl 206:117839
Song Y, Li G, Li T, Li Y (2021) A purchase decision support model considering consumer personalization
about aspirations and risk attitudes. J Retail Consum Serv 63:102728
Tajik M, Makui A, Tosarkani BM (2023) Sustainable cathode material selection in lithium-ion batteries
using a novel hybrid multi-criteria decision-making. J Energy Storage 66:107089
Aires RFDF, Ferreira LA (2018) The rank reversal problem in multi-criteria decision making literature
review. Pesquisa Operacional 38:331–362
Tripathi DK, Nigam SK, Rani P, Shah AR (2023) New intuitionistic fuzzy parametric divergence measures
and score function-based CoCoSo method for decision-making problems. Decis Mak: Appl Manag
Eng 6(1):535–563
Tsakalerou M, Efthymiadis D, Abilez A (2022) An intelligent methodology for the use of multi-criteria deci-
sion analysis in impact assessment: the case of real-world offshore construction. Sci Rep 12(1):15137
Ulutaş A, Karabasevic D, Popovic G, Stanujkic D, Nguyen PT, Karaköy Ç (2020) Development of a novel
integrated CCSD-ITARA-MARCOS decision-making approach for stackers selection in a logistics
system. Mathematics 8(10):1672
Uzun B, Taiwo M, Syidanova A, Uzun Ozsahin D (2021) The technique for order of preference by similar -
ity to ideal solution (TOPSIS). Application of Multi-Criteria Decision Analysis in Environmental and
Civil Engineering, 25–30
Vahidinia A, Hasani A (2023) A comprehensive evaluation model for smart supply chain based on the
hybrid multi-criteria decision-making method. J Soft Comput Decis Anal 1(1):219–237
Wang XT, Johnson JG (2012) A tri-reference point theory of decision making under risk. J Exp Psychol Gen
141(4):743
Wang L, Zhang Z-X, Wang Y-M (2015) A prospect theory-based interval dynamic reference point method
for emergency decision making. Expert Syst Appl 42(23):9379–9388
Więckowski J, Kizielewicz B, Shekhovtsov A, Sałabun W (2023) RANCOM: a novel approach to identify -
ing criteria relevance based on inaccuracy expert judgments. Eng Appl Artif Intell 122:106114
Więckowski J, Sałabun W, Kizielewicz B, Bączkiewicz A, Shekhovtsov A, Paradowski B, Wątróbski J
(2023) Recent advances in multi-criteria decision analysis: a comprehensive review of applications and
trends. Int J Knowl-Based Intell Eng Syst 27(4):367–393
Yusop ZB, Ahmed K, Shirazi SM, Zardari NH (2015) Weighting methods and their effects on multi-criteria
decision making model outcomes in water resources management. Springer, Cham
Zaim H, Ramdani M, Haddi A (2020) Decision tree and MCDA under fuzziness to support e-customer
satisfaction survey. In: Proceedings of the tenth international conference on soft computing and pattern
recognition (SoCPaR 2018) 10, pp. 22–32. Springer
Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and
institutional affiliations.
Authors and Affiliations
Jakub Więckowski1 · Jarosław Wątróbski2 · Anna Shkurina2 · Wojciech Sałabun1,3
 * Wojciech Sałabun
 w.salabun@il-pib.pl
 Jakub Więckowski
 j.wieckowski@il-pib.pl
 Jarosław Wątróbski
 jaroslaw.watrobski@usz.edu.pl

Adaptive multi‑criteria decision making for electric vehicles:…
Page 25 of 25 270
 Anna Shkurina
 anya.shkurina@gmail.com
1 National Institute of Telecommunications, ul. Szachowa 1, Warsaw 04-894, Poland
2 Institute of Management, University of Szczecin, ul. Cukrowa 8, Szczecin 71-004, Poland
3 Department of Artificial Intelligence and Applied Mathematics, West Pomeranian University
of Technology, ul. Żołnierska 49, Szczecin 71-210, Poland
