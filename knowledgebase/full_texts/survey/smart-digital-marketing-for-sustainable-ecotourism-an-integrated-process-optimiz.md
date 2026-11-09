---
title: 'Smart digital marketing for sustainable ecotourism: an integrated process optimization and fuzzy
  logic framework for adaptive decision-making'
url: https://doi.org/10.1007/s43621-026-04432-x
category: survey
subcategory: empirical
date: 2026-09
venue: Discover Sustainability
authors:
- Nessreen El Said Mansour El Sharkawey
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s43621-026-04432-x.pdf
pages: 27
chars: 79027
fetched_at: '2026-11-08T19:44:23+00:00'
kb_version: 1
---

# Smart digital marketing for sustainable ecotourism: an integrated process optimization and fuzzy logic framework for adaptive decision-making

RESEARCH Open Access
Discover SustainabilityEl Sharkawey Discover Sustainability          (2026) 7:1445
https://doi.org/10.1007/s43621-026-04432-x
Smart digital marketing for sustainable
ecotourism: an integrated process optimization
and fuzzy logic framework for adaptive
decision-making
Nessreen El Said Mansour El Sharkawey1*
*Correspondence:
Nessreen El Said Mansour El
Sharkawey
Nesreen.Elsharqawy@mgt.mti.
edu.eg
1Modern University for Technology
& Information (MTI University),
Cairo, Egypt
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use,
sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article
are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to
obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
Abstract
This study addresses the challenge of achieving sustainable marketing performance
in fragile ecotourism destinations, where marketing activities must balance
competitiveness with environmental preservation. A hybrid Smart Digital Marketing
(SDM) framework that integrates Digital Six Sigma Marketing (DSSM) with fuzzy
logic-based decision systems is developed and empirically evaluated to support
adaptive decision-making under ecological constraints. Using an explanatory
sequential mixed-methods design, the study combines survey data ( N = 250),
stakeholder interviews ( N = 18), environmental observation scorecards, and
computational modeling. The framework operationalizes three ecological and
behavioral variables—environmental fragility, visitor load, and tourist satisfaction—as
inputs to a Mamdani-type fuzzy inference system with 27 if–then rules, producing
adaptive marketing intensity decisions aligned with carrying capacity. The pre–post
analysis showed statistically significant observed improvements associated with
framework implementation: campaign response time was reduced by 35.7%, process
variance decreased by 39.4%, the process capability index increased from 0.94 to
1.42, and competitive positioning improved by 24.3%. The fuzzy inference system
demonstrated adaptive modulation of marketing intensity from 0.80 under stable
conditions to 0.19 under high ecological risk. The study contributes a practical, data-
driven decision-support framework that enables organizations to align marketing
strategies with ecological thresholds, extending Smart Digital Marketing as a dynamic
capability within sustainability-sensitive tourism contexts. The framework provides a
potentially transferable model for translating qualitative and ambiguous variables into
structured, adaptive marketing decisions under environmental uncertainty.
Keywords Smart digital marketing (SDM), Sustainable marketing, Sustainable tourism,
Ecotourism, Fuzzy logic, Decision support systems, Adaptive decision-making, Digital
six sigma, Ecological sustainability

Page 2 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
1 Introduction
1.1 Background and research context
The escalating pressure on fragile ecotourism destinations to reconcile economic
growth with environmental preservation represents a critical challenge for contem -
porary sustainable marketing systems. Traditional marketing approaches, which have
been primarily designed to maximize demand, frequently overlook ecological limits and
consequently contribute to unsustainable outcomes in environmentally sensitive desti -
nations [1, 2]. This inherent tension underscores the urgent need for adaptive market -
ing frameworks capable of aligning promotional activities with environmental capacity
while simultaneously sustaining competitive performance.
The ongoing digital transformation has fundamentally redefined the organizational
role of marketing, shifting it from a traditional communication function toward a stra -
tegic intelligence capability that supports real-time sensing, adaptive decision-making,
and sustainable value creation [ 1, 3]. In increasingly volatile and data-intensive environ -
ments, organizations require marketing systems that extend beyond conventional pro -
motional activities to enable more integrated and responsive decision processes [4, 5].
This transformation is particularly critical in ecotourism settings, where market -
ing decisions carry direct ecological, cultural, and socio-economic consequences [ 6, 7].
Fragile destinations must balance the need to generate sufficient demand for economic
sustainability with the necessity of protecting environmental resources. However, exces -
sive or poorly calibrated marketing efforts may intensify environmental degradation and
resource pressure [ 8]. This inherent tension—extensively documented in the sustain -
able tourism literature through carrying capacity models, Limits of Acceptable Change
(LAC) frameworks, and adaptive management approaches—represents a fundamental
challenge for sustainable marketing in ecologically sensitive tourism systems [9].
1.2 Research problem and gap identification
Traditional marketing analytics exhibit significant limitations when applied to ecotour -
ism contexts characterized by ecological uncertainty, qualitative constructs, and com -
plex stakeholder expectations [10, 11]. Conventional deterministic approaches often fail
to adequately capture critical variables such as perceived environmental fragility, cul -
tural authenticity, and sustainable behavioral intentions, despite their substantial influ -
ence on tourist decision-making processes and sustainability outcomes [12, 13].
Three specific gaps are identified in the existing literature. First, a disciplinary silo gap
exists: Digital Six Sigma Marketing (DSSM) and Fuzzy Logic have developed as largely
independent streams with minimal integration. While DSSM emphasizes measurement
precision and process control, Fuzzy Logic focuses on uncertainty management and
contextual adaptability, leaving their complementary potential underutilized [2, 14].
Second, a marketing process underutilization gap persists: although Six Sigma meth -
odologies have demonstrated relevance in service contexts, their systematic application
as strategic marketing decision frameworks—particularly in sustainability-sensitive
environments—remains limited. Most existing applications emphasize operational effi -
ciency rather than strategic decision-making capabilities [15, 16].
Third, a sustainability-intelligence disconnect gap remains evident: despite the grow -
ing importance of data-driven decision-making in sustainability research, few stud -
ies provide implementable frameworks for integrating sustainability principles into

Page 3 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
marketing intelligence systems. Consequently, sustainability objectives and marketing
decision processes often remain disconnected rather than fully integrated [17, 18].
This study addresses these gaps by developing and empirically evaluating an integrated
framework that combines process optimization through DSSM-DMAIC with uncer -
tainty management through fuzzy logic within a sustainability-constrained ecotourism
context.
1.3 Research context: siwa oasis and adrère amellal ecolodge
The empirical context of this study is Adrère Amellal ecolodge, located in Siwa Oasis,
Egypt—an environmentally sensitive yet culturally distinctive desert ecosystem. Siwa is
characterized by unique geological formations, a distinct Berber cultural heritage, and
significant historical value, positioning it as both an important tourism destination and
a fragile ecological system [ 8]. Adrère Amellal represents an applied model of sustain -
able tourism, operating through traditional construction techniques (‘kershef’: salt rock,
clay, and sand), off-grid energy use (oil lamps, candles, solar water heating), gravity-fed
water systems, wastewater recycling through natural filtration, zero-waste operations,
and locally sourced materials [ 19]. Despite these sustainability-oriented practices, the
destination faces increasing challenges related to visitor pressure and the lack of market-
ing strategies aligned with ecological carrying capacity [ 8]. This makes Adrère Amellal a
“revelatory case” [20] for examining how sustainable marketing frameworks can support
adaptive and context-sensitive decision-making under conditions of ecological sensitiv -
ity and demand pressure.
1.4 Research objectives and contribution
Addressing the identified theoretical and practical gaps, this study pursues four main
objectives. First, it develops and empirically evaluates a Smart Digital Marketing (SDM)
framework that integrates Digital Six Sigma Marketing (DSSM) with fuzzy logic-based
decision modeling for fragile ecotourism systems. Second, it examines observed changes
in marketing efficiency, decision responsiveness, and sustainability alignment associ -
ated with the framework’s application at Adrère Amellal ecolodge. Third, it designs and
evaluates a fuzzy inference system that translates qualitative ecological and behavioral
variables into adaptive marketing intensity recommendations aligned with environmen -
tal carrying capacity. Fourth, it derives theoretical and managerial implications for sus -
tainable marketing in ecotourism contexts.
This study contributes to the literature in three key ways. First, it introduces an inte -
grated framework that combines process optimization and uncertainty management to
resolve the precision–adaptability tension in sustainable marketing decision-making.
Second, it extends the application of Smart Digital Marketing (SDM) as a dynamic capa -
bility within sustainability-sensitive tourism contexts, contributing to the Resource-
Based View [ 21, 22]. Third, it offers a practical, evidence-based approach that enables
organizations to align marketing strategies with ecological thresholds and long-term
sustainability objectives [23].

Page 4 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
2 Literature review and theoretical framework
2.1 Smart digital marketing (SDM) as strategic organizational intelligence
Digital transformation has fundamentally redefined marketing’s organizational role,
shifting it from a communication-oriented support function to a strategic intelligence
capability that enables real-time sensing, adaptive decision-making, and value creation
[1, 3]. Contemporary Smart Digital Marketing (SDM) integrates advanced analytics,
artificial intelligence, Internet of Things (IoT) technologies, and real-time data streams
to transform market signals into actionable strategic insights [24, 25].
From a Resource-Based View (RBV) perspective [ 21], Smart Digital Marketing can
be conceptualized as a valuable, rare, inimitable, and non-substitutable (VRIN) orga -
nizational resource that enhances responsiveness and adaptability in dynamic and sus -
tainability-constrained environments [ 23]. In this context, SDM operates as a dynamic
capability [22], enabling firms to integrate, build, and reconfigure internal and external
competences to effectively respond to environmental and market changes.
In ecotourism contexts, the importance of SDM is amplified by environmental uncer -
tainty, stakeholder diversity, and sustainability imperatives. However, its application as a
structured tool for sustainable marketing decision-making remains insufficiently devel -
oped [2, 26].
2.2 Digital six sigma marketing: from manufacturing discipline to marketing intelligence
Six Sigma represents a structured, data-driven methodology aimed at process improve -
ment and variation reduction, operationalized through the DMAIC cycle (Define,
Measure, Analyze, Improve, Control) [ 27, 28]. Although its early applications were pri -
marily rooted in manufacturing quality management, its principles have increasingly
been extended to service and marketing contexts, where inefficiencies are reflected in
inconsistent campaign performance, high customer acquisition costs, and ineffective
resource allocation [15, 16].
Digital Six Sigma Marketing (DSSM) builds on this foundation by incorporating digital
data sources—Customer Relationship Management (CRM) systems, web analytics, and
real-time feedback mechanisms—into marketing processes. This integration improves
measurement precision, enables continuous performance monitoring, and enhances the
speed and quality of decision-making [ 29]. Empirical evidence suggests that applying
Six Sigma principles within marketing contexts can lead to measurable improvements
in performance outcomes, including reduced response time and higher conversion effi -
ciency [16].
Despite these benefits, the application of DSSM within tourism and sustainability con-
texts remains limited. Existing studies have largely focused on operational performance
improvements, with limited attention to how process optimization methodologies can
support sustainability-oriented marketing decision-making [18].
2.3 Fuzzy logic: mathematical formalization of decision-making under uncertainty
Fuzzy Logic, introduced by Zadeh [30], provides a mathematical framework for handling
imprecision, ambiguity, and qualitative judgment in decision-making contexts. Unlike
classical binary logic, fuzzy set theory allows partial membership, enabling the represen -
tation of linguistic variables such as “high satisfaction, ” “moderate environmental fragil-
ity, ” and “acceptable visitor load” [31].

Page 5 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
A fuzzy inference system operates through three key processes—fuzzification, rule-
based inference, and defuzzification—allowing qualitative inputs to be systematically
transformed into actionable decision outputs. This capability makes fuzzy logic particu -
larly suitable for marketing environments characterized by uncertainty and subjective
evaluation [10, 11].
In marketing and tourism contexts, fuzzy logic has been widely applied to capture
complex consumer behavior and decision dynamics. Prior studies highlight its effective -
ness in modeling tourist preferences and sustainable tourism intentions that are diffi -
cult to quantify using conventional approaches [ 10, 11]. However, existing applications
remain fragmented and context-specific, with limited integration into structured pro -
cess optimization frameworks.
2.4 The integration imperative: resolving the precision–adaptability tension
The preceding review reveals a fundamental theoretical tension that existing approaches
cannot resolve in isolation. DSSM presupposes process stability, measurable variables,
and well-defined optimization criteria—conditions that are rarely satisfied in sustain -
ability-sensitive ecotourism contexts where ecological fragility, stakeholder perceptions,
and cultural authenticity resist precise quantification [ 8, 9]. Conversely, Fuzzy Logic
accommodates ambiguity but lacks process discipline, potentially leading to arbitrary or
inconsistent decisions if not constrained by structured improvement methodologies [2].
This tension reflects a deeper epistemological challenge: how can organizations
achieve the benefits of analytical precision (reduced variation, consistent outcomes,
quality control) while simultaneously maintaining contextual adaptability (responsive -
ness to ecological variability, stakeholder diversity, qualitative judgments)? Existing lit -
erature has treated these as mutually exclusive capabilities—organizations must choose
either rule-based consistency or discretionary flexibility. This study challenges that
trade-off logic by demonstrating that integration of DSSM and Fuzzy Logic enables the
simultaneous pursuit of both objectives.
The resolution mechanism operates through two complementary pathways. First,
DSSM provides the process discipline that prevents fuzzy inference from becom -
ing arbitrary: the DMAIC framework ensures that input variables are operationally
defined, measurement systems are validated, and decision outcomes are controlled. Sec -
ond, Fuzzy Logic provides the adaptive reasoning that prevents DSSM from becoming
mechanically rigid: the fuzzy rule base encodes context-sensitive heuristics (precaution -
ary principle, reward excellence, demand-responsive adjustment) that would be lost in
purely deterministic optimization. This dual-mechanism architecture enables what prior
frameworks cannot: maintaining process capability (Cp > 1.33) while allowing marketing
intensity to vary nonlinearly with ecological conditions [32].
Table 1 summarizes the key limitations identified in prior research across the three
theoretical streams. As shown, existing studies have predominantly examined DSSM
and Fuzzy Logic in isolation. For instance, while Garza-Reyes et al. [ 15] demonstrated
DSSM effectiveness in sales processes, their study did not incorporate uncertainty man -
agement capabilities. Conversely, Esmaelnezhad et al. [8] applied fuzzy methods to tour-
ism marketing but without structured process optimization. This fragmented treatment
leaves unresolved the question of how organizations can simultaneously achieve process
efficiency and adaptive responsiveness under ecological uncertainty. The present study

Page 6 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
addresses these limitations by theoretically specifying and empirically evaluating com -
plementary mechanisms rather than treating them as substitutes.
2.5 Theoretical framework and conceptual model
To address the identified gaps, this study proposes an integrated theoretical framework
that positions Smart Digital Marketing (SDM) as a dynamic capability enabling sus -
tainable competitive advantage [ 21, 22]. The framework is built on two complementary
mechanisms.
The first mechanism, process optimization through DSSM-DMAIC, enhances mar -
keting efficiency by reducing process variation, improving response consistency, and
establishing systematic control over marketing activities. This contributes to competitive
advantage through operational excellence and reliability [16, 28].
The second mechanism, uncertainty management through Fuzzy Logic, enables the
translation of qualitative and ambiguous variables into structured decision inputs. It
supports adaptive, context-sensitive marketing decisions by incorporating ecological
conditions, stakeholder perceptions, and behavioral uncertainty. This contributes to
competitive advantage through strategic flexibility and sustainability alignment [30, 31].
The integration of these mechanisms enables organizations to simultaneously achieve
marketing efficiency, ecological alignment, and adaptive responsiveness. In doing so, the
proposed Smart Digital Marketing (SDM) framework supports sustainable competitive
advantage in complex and sustainability-constrained environments [2, 18].
To address the identified theoretical and practical gaps, the proposed framework inte -
grates Smart Digital Marketing (SDM), DSSM–DMAIC, and fuzzy logic into a unified
decision-support model. Figure  1 illustrates the proposed integrated conceptual frame -
work, showing how Smart Digital Marketing (SDM) combines DSSM–DMAIC process
optimization with fuzzy logic-based uncertainty management to support adaptive mar -
keting decision-making and sustainable competitive advantage.
3 Research questions and hypotheses
3.1 Research questions
This study addresses four research questions:
RQ1: How can Digital Six Sigma Marketing (DSSM), operationalized through the
DMAIC cycle, be applied to identify and improve marketing process inefficiencies in
fragile ecotourism contexts?
RQ2: How can Fuzzy Logic-based decision modeling enhance marketing decision-
making under conditions of environmental uncertainty and behavioral variability?
Table 1 Synthesis of prior literature limitations and study contributions
Theoretical stream Representative
references
Key limitation How the present study ad-
dresses the limitation
Smart Digital
Marketing
Verhoef et al. [1]; Zhang
& Deng [2]
Lacks operationalization for
sustainability-constrained
contexts
Proposes SDM as dynamic
capability with measurable
components
Digital Six Sigma
Marketing
Chaplin [14]; Garza-
Reyes et al. [15]
Primarily operational focus;
limited strategic marketing
application
Extends DSSM-DMAIC to
strategic marketing decisions
with ecological constraints
Fuzzy Logic in
Tourism
Esmaelnezhad et al. [8];
Dejprayoon et al. [9]
Fragmented applications;
no integration with process
optimization
Develops integrated fuzzy
inference system with DSSM
process discipline

Page 7 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
RQ3: To what extent does an integrated Smart Digital Marketing (SDM) framework
support sustainability awareness, responsible visitor behavior, and ecological preserva -
tion in fragile destinations?
RQ4: What is the impact of the integrated DSSM–Fuzzy Logic framework on market -
ing process efficiency, decision responsiveness, sustainability alignment, and competi -
tive positioning?
3.2 Hypothesis development
Drawing on the theoretical framework, this study proposes four hypotheses:
H1 Smart Digital Marketing (SDM) positively influences intelligent and adaptive market-
ing decision-making in sustainability-constrained environments, as it enables real-time
data integration, advanced analytics, and enhanced market sensing capabilities [1, 22].
H2 Digital Six Sigma Marketing (DSSM), implemented through the DMAIC methodol -
ogy, positively improves marketing process efficiency by reducing variability and enhanc-
ing decision consistency [16, 28].
H3 Fuzzy Logic-based decision modeling positively enhances uncertainty management
capability by enabling the systematic incorporation of qualitative and ambiguous vari -
ables into marketing decision processes [30, 31].
H4 The integration of DSSM and Fuzzy Logic within a Smart Digital Marketing (SDM)
framework positively supports sustainable competitive advantage by aligning marketing
decisions with environmental constraints and stakeholder expectations, thereby enhanc-
ing both strategic flexibility and operational effectiveness [2, 22].
Figure 2 presents the structural model of the proposed research hypotheses. The model
illustrates Smart Digital Marketing (SDM) as the overarching framework integrating
DSSM–DMAIC and Fuzzy Logic, which respectively enhance process efficiency and
uncertainty management. These complementary capabilities contribute to decision
intelligence, ultimately supporting sustainable competitive advantage. The model pro -
vides the theoretical basis for the empirical testing of hypotheses H1–H4.
Fig. 1 Integrated conceptual framework of smart digital marketing (SDM) for sustainable competitive advantage

Page 8 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
4 Methodology
4.1 Research philosophy and design
This study adopts a pragmatist research philosophy, recognizing that research ques -
tions addressing complex socio-technical systems in ecologically sensitive contexts
require methodological pluralism rather than adherence to a single paradigm [ 33, 34].
Consistent with this perspective, an explanatory sequential mixed-methods design was
employed, consisting of two integrated phases.
Phase 1 involved a quantitative cross-sectional survey measuring tourist perceptions,
satisfaction, environmental awareness, and behavioral intentions, with a sample of 250
international eco-tourists. Phase 2 comprised qualitative semi-structured stakeholder
interviews and environmental observation scorecards to contextualize quantitative
Fig. 2 Structural model of the proposed research hypotheses

Page 9 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
findings and support the development of fuzzy inference rules, involving 18 participants
[35].
This design enables both breadth—by identifying generalizable patterns across tour -
ist populations—and depth—by capturing contextual insights into decision-making con-
straints and sustainability challenges—thereby enhancing the study’s overall validity and
practical applicability [33].
4.2 Research context and case selection
A single in-depth case study design was selected based on three methodological con -
siderations. First, the study addresses “how” and “why” questions related to complex
decision-making processes in real-world settings [ 20]. Second, the phenomenon under
investigation—the integration of DSSM and Fuzzy Logic for sustainability-aligned
marketing—represents a relatively unexplored approach, requiring rich contextual
understanding. Third, sustainability outcomes in ecotourism are inherently context-
dependent, necessitating detailed examination of ecological, cultural, and operational
conditions [36].
Adrère Amellal ecolodge, established in 2000 by Environmental Quality International
(EQI), is located at the base of Adrère Amellal Mountain in Siwa Oasis, Egypt (29.2031°
N, 25.5195° E). The property includes 40 guest units with a maximum capacity of 68 visi-
tors. Its sustainability practices include: construction using traditional ‘kershef’ tech -
niques (salt rock, clay, and sand) for natural insulation; off-grid energy use with lighting
through oil lamps and candles; solar-based water heating; gravity-fed water systems;
wastewater recycling through natural filtration systems; and zero-plastic operations sup-
ported by locally sourced materials.
The ecolodge follows a premium pricing strategy (USD $400–$600 per night), target -
ing environmentally conscious luxury travelers. It operates with an average occupancy
rate of 65–70% and employs approximately 120 staff from the local Siwan community.
This case represents an “extreme” or “revelatory” case [20, 37], where sustainability prac-
tices are highly advanced while marketing intelligence systems remain relatively under -
developed, making it suitable for examining the potential contribution of the proposed
Smart Digital Marketing (SDM) framework.
4.3 Sampling and sample size justification
Sample size was determined using Cochran’s formula for finite populations [38]. The ini-
tial sample size (n0) was calculated as:
 n0 = Z2 ×p×(1−p) e2   (1)
where Z =1 .96 (95% confidence level), p =0 .50 (conservative estimate maximizing
sample size), and e =0 .05 (margin of error). This yielded n0 = 384.16.
T o adjust for the finite population ( N = 1,850, based on historical annual occupancy
records), the corrected sample size ( n) was calculated using: 
 n = n0 1+ n0 −1 N = 318.25   (2)
To account for potential non-response and incomplete questionnaires, the target sample
size was increased to 350 respondents. A total of 325 responses were collected, of which

Page 10 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
250 were retained for final analysis following data screening procedures (multivariate
outlier detection using Mahalanobis distance, missing data assessment). The effective
response rate was 71.4%.
The sample, while appropriate for theory elaboration [ 36], constitutes a convenience
sample drawn from a single property’s guest population during a 21-day period. The
finite population correction using N = 1,850 (historical annual occupancy) provides
correct standard error estimates for inference to the Adrère Amellal guest population
but does not transform this into a random sample of a broader ecotourism popula -
tion. Accordingly, statistical generalization to other ecotourism contexts is not claimed.
Rather, analytic generalization [35] is pursued: the theoretical mechanisms (DSSM pro -
cess optimization, fuzzy uncertainty management) are hypothesized to transfer to other
contexts, with context-specific parameterization required.
Post hoc power analysis conducted using G*Power 3.1 [ 39] confirmed that a sample
size of N = 250 achieves statistical power exceeding 0.95 for detecting medium effect
sizes ( f 2 =0 .15) at α =0 .05 in multiple regression analysis with six predictors,
exceeding the recommended minimum threshold of 0.80 [40].
4.4 Data collection instruments and procedures
Data collection was conducted over a 21-day period (May 1–21, 2025), corresponding
to the early high tourism season. Eligible guests were invited to participate via QR codes
provided at check-in and included in guest information materials. The questionnaire was
administered electronically using the Qualtrics platform, optimized for mobile and tab -
let devices, with an average completion time of 12.4 min [41].
Semi-structured interviews were conducted in Arabic, English, and Siwi (with transla -
tion support when required), with an average duration of 47  min. All interviews were
audio-recorded with participant consent and transcribed for analysis. Environmental
observations were conducted daily at two time intervals (08:00–10:00 and 16:00–18:00)
across all operational areas, supported by systematic field notes and photographic docu -
mentation where permitted.
All participants provided written informed consent prior to participation. Anonym -
ity and confidentiality were strictly maintained throughout the study, and all data were
securely stored on encrypted university servers in accordance with established ethical
research standards.
4.5 Digital six sigma marketing (DSSM) application protocol
The DMAIC methodology was systematically implemented following established Six
Sigma deployment protocols [ 28] and adapted for digital marketing contexts. Table 2
summarizes the key activities, principal deliverables, and implementation timeline for
each phase.
4.6 Fuzzy logic decision model: mathematical formalization
4.6.1 Variable definition and normalization
Let the input vector be defined as
 x =( S, F, L) ∈ [0, 1]3.   (3)
where:

Page 11 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
  • S denotes Tourist Satisfaction (composite index from 7-point Likert scale items).
  • F  denotes Environmental Fragility (perceived ecological vulnerability, 7-point scale).
  • L  denotes Visitor Load (current occupancy relative to maximum sustainable
capacity).
The output variable MI ∈ [0,1] denotes Marketing Intensity (recommended promo -
tional activity level, including budget allocation, campaign frequency, and digital adver -
tising intensity).
Normalization procedure Raw scores from 7-point Likert scales (Sraw,F raw) are trans-
formed to the [0, 1] interval using.
 S = Sraw−1 7−1 = Sraw−1 6   (4)
 F = Fraw−1 7−1 = Fraw−1 6   (5)
  
Visitor load L is computed as
 L = Current_Occupancy Maximum_Sustainable_Capacity .   (6)
where maximum sustainable capacity is operationally defined as 85% of physical capac -
ity (58 visitors for the 68-guest property) based on ecological impact assessments con -
ducted by lodge management and Siwa Oasis conservation authorities.
4.6.2 Triangular membership functions
For each linguistic term T ∈{ Low, Medium, High}, membership is defined by the tri -
angular membership function µT :[ 0,1] → [0,1]:
Table 2 Summary of DSSM-DMAIC implementation phases
Phase Duration Key activities Primary deliverables
Define Weeks 1–2 Project charter development; stakeholder identi-
fication and analysis; SIPOC mapping; CTQ metric
identification
Prioritized stakeholder
requirements; current-state
process maps; team charter;
SMART project objectives
Measure Weeks 3–4 Baseline performance data collection; measure-
ment system analysis; operational definition devel-
opment; data collection plan execution; process
capability baseline calculation
Validated measurement sys-
tems; baseline process per-
formance data; preliminary
process sigma calculation
Analyze Weeks 5–6 Data visualization (run charts, control charts); root
cause analysis (fishbone diagrams, 5-Why); hypoth-
esis testing; process variation sources identification
Validated root causes;
quantitative problem state-
ments; performance gap
quantification
Improve Weeks 7–9 Solution generation (brainstorming, benchmark-
ing); solution evaluation (cost-benefit analysis,
impact-effort matrix); pilot testing; implementation
planning
Selected improvement
solutions; ideal process
design; implementation
plan; business case
Control Weeks 10–12 Process control plan development; statistical
process control implementation; response plan
documentation; lessons learned documentation;
replication opportunity identification
Process control plans; ongo-
ing monitoring protocols;
control charts; standardiza-
tion documentation

Page 12 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445

µT (x; a, b, c)=



0, if x ≤ a
x−a
b−a , if a < x ≤ b c−x
c−b , if b < x < c 0, if x ≥ c   (7)
where parameters (a, b, c) satisfy a ≤ b ≤ c, with a, b, c ∈ [0,1]. Table  3 summarizes
the parameterization of the linguistic terms and their corresponding triangular mem -
bership functions.
4.6.3 Fuzzy rule base
Let Ai,B i,C i,D i denote linguistic terms for S, F, L, and MI  respectively. The i-th
fuzzy rule ( i =1 ,... , 27) is defined as:
 Ri : I FSi sA i AND F is B i AND L is C i THEN MI is D i
The complete rule base (27 rules) is constructed from the 33 combinations of linguistic
terms. Rule consequents Di are determined by expert heuristics based on three decision
principles: (1) reward excellence (high satisfaction justifies moderate-to-high market -
ing intensity), (2) precautionary principle (high fragility suppresses marketing intensity),
and (3) demand-responsive adjustment (high load alone does not suppress marketing
intensity when fragility is low). Table  4 summarizes a representative subset of the fuzzy
rule base used in the proposed inference system.
4.6.4 Fuzzy inference and aggregation
For a given input vector (S, F, L), the firing strength (degree of activation) of rule Ri is
computed using the minimum (Mamdani) operator:
Table 3 Triangular membership function parameters with formal definitions
Variable Term a b c Triangular membership function, µ(x)
Satisfaction ( S) Low 0 0 0.4 µLow (S)= max (0, min ( S − 0
0.4 , 0.4 − S 0.4 )) for S ∈ [0,1]  Medium 0.3 0.5 0.7 µMed (S)= max (0, min ( S − 0.3
0.2 , 0.7 − S 0.2 )) High 0.6 1 1 µHigh (S)= max (0, min ( S − 0.6
0.4 , 1 − S 0 )) Fragility ( F ) Low 0 0 0.3 µLow (F )= max (0, min ( F
0.3 , 0.3 − F 0.3 )) Medium 0.2 0.5 0.8 µMed (F )= max (0, min ( F − 0.2
0.3 , 0.8 − F 0.3 )) High 0.7 1 1 µHigh (F )= max (0, min ( F − 0.7
0.3 , 1 − F 0 )) Visitor Load ( L) Low 0 0 0.4 µLow (L)= max (0, min ( L
0.4 , 0.4 − L 0.4 )) Medium 0.3 0.5 0.7 µMed (L)= max (0, min ( L − 0.3
0.2 , 0.7 − L 0.2 ) High 0.6 1 1 µHigh (L)= max (0, min ( L − 0.6
0.4 , 1 − L 0 )) Marketing Intensity ( MI ) Low 0 0 0.4 µLow (MI )= max (0, min ( MI
0.4 , 0.4 − MI 0.4 )) Medium 0.3 0.5 0.7 µMed (MI )= max (0, min ( MI − 0.3
0.2 , 0.7 − MI 0.2 )) High 0.6 1 1 µHigh (MI )= max (0, min ( MI − 0.6
0.4 , 1 − MI 0 ))

Page 13 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
 αi = min [µAi (S) ,µ Bi (F ) ,µ Ci (L)] ,α i ∈ [0,1]   (8)
The implied fuzzy set for rule Ri is obtained by truncating the output membership func-
tion µ Di (MI ) at the firing strength α i:
 µRi (MI )= min [αi,µ Di (MI )] , ∀MI ∈ [0,1]   (9)
Aggregation across all activated rules is performed using the maximum operator (union
of fuzzy sets):

µagg (MI )=
27
maxµRi (MI )
i=1
=
27
max {min [αi,µ Di (MI )]}
i=1
, ∀MI ∈ [0,1]

 (10)
4.6.5 Defuzzification
The crisp output value MI ∗ is obtained using the centroid (center of gravity) defuzzifi -
cation method:
 MI ∗ =
´ 1
0 µagg (MI )·MId MI´ 1
0 µagg (MI )dM I   (11)
where the integrals are evaluated over the output domain MI ∈ [0,1] (Riemann inte -
grals, assuming µ agg is piecewise continuous and bounded). This yields a weighted
average of all possible output values, producing a unique crisp value that represents the
center of the aggregated fuzzy set.
Table 4 Representative fuzzy rule base (Subset)
Rule Satisfaction Fragility Visitor load Marketing intensity Decision logic
R1 High Low Low High Reward excellence
R2 High Low Medium High Reward excellence
R3 High Low High Medium Load-sensitive reduction
R4 High Medium Low Medium Caution with moderate fragility
R5 High Medium Medium Medium Balanced conditions
R6 High Medium High Medium-Low Fragility-load interaction
R7 High High Low Medium-Low Fragility dominates
R8 Medium Medium Medium Medium Balanced conditions
R9 Low High High Low Precautionary principle
R10 Low Low Low Medium-Low Cautious despite low fragility
R11 Medium Low Low Medium-High Favorable conditions
R12 Medium Low Medium Medium-High Favorable conditions
R13 Medium High Low Medium-Low Fragility dominates
R14 Medium High Medium Low High risk suppression
R15 Low Medium Medium Low-Medium Moderate caution
R16 Low Low High Medium-Low Load-sensitive
R17 Low Medium Low Low-Medium Fragility-sensitive
R18 Low High Medium Low Maximum suppression
R19 High High Low Medium-Low Fragility dominates
R20 High High High Low Double constraint
R21 Medium High High Low Triple constraint
R22 Medium Medium High Medium-Low Load-sensitive reduction
R23 Low Low Medium Medium-Low Cautious moderate
R24 Low Medium High Low Risk avoidance
R25 Medium Low High Medium Load-only response
R26 High Medium High Medium-Low Constrained excellence
R27 Low High High Low Maximum suppression

Page 14 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
4.6.6 Computational implementation
All fuzzy modeling procedures were implemented using MATLAB R2024a Fuzzy Logic
Toolbox (MathWorks, Natick, MA) with a Mamdani-type inference engine. Triangu -
lar membership functions were configured using the ‘trimf’ function with parameters
from Table 3. The rule base was implemented using a 27 × 5 matrix with minimum
implication and maximum aggregation. Numerical integration for defuzzification was
performed using adaptive Simpson quadrature with tolerance ϵ =1 × 10−6. Model
validation was conducted using the Python Scikit-Fuzzy library (version 0.4.2) [ 42], with
cross-validation confirming identical outputs (maximum deviation <1×10−8).
4.7 Validity and reliability assurance
Construct validity was established through multiple procedures. Content validity was
assessed through expert panel evaluation involving five marketing professors and three
sustainable tourism researchers, with the Content Validity Index (CVI) exceeding 0.83
for all constructs. Convergent validity was confirmed by Average Variance Extracted
(AVE) values exceeding 0.50 and factor loadings greater than 0.70 across all multi-item
constructs. Discriminant validity was verified using the Fornell–Larcker criterion, where
the square root of AVE exceeded inter-construct correlations, and the heterotrait–
monotrait ratio (HTMT) remained below the recommended threshold of 0.85.
Reliability was assessed using internal consistency measures, with Cronbach’s alpha
values exceeding 0.70 and composite reliability values above 0.80 for all constructs.
Test–retest reliability was further evaluated using a subset of respondents (n = 35), with
measurements repeated after a 14-day interval, resulting in intraclass correlation coef -
ficients (ICC) ranging from 0.82 to 0.91, indicating strong stability over time.
Common method bias was assessed using Harman’s single-factor test. The unrotated
principal component analysis revealed eight factors with eigenvalues greater than 1.0,
with the first factor accounting for 23.4% of the total variance, substantially below the
critical threshold of 50%, indicating that common method bias is not a serious concern
[43].
5 Results
5.1 Sample characteristics and descriptive statistics
The demographic profile of the survey respondents ( N = 250) is presented in Table  5.
Gender distribution was relatively balanced (52.8% male, 47.2% female). The largest age
group was 31–45 years (47.2%), followed by 46–60 years (26.0%), 18–30 years (18.0%),
and 60 + years (8.8%). Educational attainment was notably high (56.8% bachelor’s
degrees, 28.4% master’s degrees, 11.6% doctoral/professional). Geographic origin was
primarily European (44.0%) and North American (32.0%). First-time visitors represented
71.2% of the sample. The sample broadly reflects the ecolodge’s target market, compris -
ing predominantly well-educated, mid-career international travelers.
Descriptive statistics for the study constructs are presented in Table  6. The
descriptive statistics indicate relatively high levels of environmental awareness
( M =4 .48, SD =0 .52), service satisfaction ( M =4 .32, SD =0 .61), and sustainabil -
ity engagement ( M =4 .27, SD =0 .58), alongside moderate perceived environmen -
tal fragility ( M =4 .11, SD =0 .67). Marketing perception recorded the lowest mean
( M =3 .84, SD =0 .73), suggesting a potential gap between sustainability performance

Page 15 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
and the effectiveness of sustainability-oriented marketing communication. Skewness
and kurtosis values were within the acceptable range ( ± 1), and Shapiro–Wilk test
results were non-significant ( p> 0.05), indicating approximate normality.
5.2 Reliability and validity assessment
Table 7 summarizes the results of the construct reliability and convergent validity assess-
ment. Cronbach’s alpha coefficients ranged from 0.79 to 0.88, composite reliability val -
ues ranged from 0.81 to 0.91, and the Average Variance Extracted (AVE) ranged from
0.58 to 0.67. All values exceeded the recommended thresholds for internal consistency
and convergent validity [44, 45].
Table 5 Demographic characteristics of survey respondents ( N = 250)
Characteristic Category Frequency ( n) Percentage (%)
Gender Male 132 52.8
Female 118 47.2
Age group 18–30 45 18.0
31–45 118 47.2
46–60 65 26.0
60+ 22 8.8
Education Bachelor’s degree 142 56.8
Master’s degree 71 28.4
Doctorate/Professional 29 11.6
Other 8 3.2
Region of Origin Europe 110 44.0
North America 80 32.0
Asia-Pacific 45 18.0
Other 15 6.0
Visit Type First-time 178 71.2
Repeat visitor 72 28.8
Length of Stay 1–2 nights 52 20.8
3–4 nights 138 55.2
5 + nights 60 24.0
Table 6 Descriptive statistics and normality assessment ( N = 250)
Construct Mean SD Skewness Kurtosis Shapiro–Wilk ( p-value)
Environmental Awareness 4.48 0.52 −0.43 0.21 0.089
Perceived Fragility 4.11 0.67 −0.38 −0.12 0.124
Service Satisfaction 4.32 0.61 −0.51 0.33 0.052
Sustainability Engagement 4.27 0.58 −0.44 0.18 0.076
Marketing Perception 3.84 0.73 −0.29 -0.08 0.153
Table 7 Construct reliability and convergent validity
Construct Items (n) Cronbach’sα Composite reli-
ability (CR)
AVE √ AV E
Square
Root
of AVE
Environmental Awareness 5 0.82 0.84 0.61 0.78
Service Satisfaction 6 0.88 0.91 0.67 0.82
Sustainability Engagement 4 0.79 0.81 0.58 0.76
Marketing Perception 5 0.81 0.83 0.59 0.77

Page 16 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
5.3 Digital six sigma marketing (DSSM) implementation results
Table  8 summarizes the marketing process performance indicators before and after
DMAIC implementation. Campaign response time decreased from 48.5  h ( SD =8 .2
) to 31.2  h ( SD =5 .4), representing a 35.7% reduction ( t (248) = 6 .42,p < 0.001,
Cohen’s d =0 .81, large effect). Customer inquiry resolution rate improved from 71.0%
( SD = 12.3) to 89.0% ( SD =7 .8), a 25.4% increase ( χ 2 (1) = 9.87,p < 0.01,ϕ =0 .42
, medium effect). Customer satisfaction score increased from 4.01 ( SD =0 .68) to
4.32 ( SD =0 .61), a 7.7% improvement ( t (248) = 3 .89,p < 0.001, Cohen’s d =0 .49
, medium effect). Process variance ( σ 2) reduced from 1.42 to 0.86, a 39.4% reduction
(Levene’s F =8 .93,p < 0.01,η 2 =0 .11, medium effect). Process capability index ( Cp
) improved from 0.94 (incapable; >8.9% defect rate assuming ± 3σ  limits) to 1.42 (capa-
ble; <0.1% defect rate), a 51.1% enhancement.
T o further demonstrate the effectiveness of the proposed framework, Fig.  3 presents
the process control charts comparing campaign response times before (baseline) and
after DMAIC implementation.
5.4 Fuzzy logic decision model results
To facilitate interpretation of the fuzzy inference system, Fig.  4 illustrates the triangular
membership functions for the input and output variables, (satisfaction, fragility, visitor
load) and output variable (marketing intensity). The figure illustrates how linguistic vari-
ables are transformed into quantitative membership values, enabling the representation
of subjective and qualitative inputs within a structured decision-making framework.
To further visualize the interaction effects among the fuzzy variables, Fig.  5 presents
the three-dimensional fuzzy rule surfaces generated by the proposed inference system.
The surfaces illustrate the modeled interactions among satisfaction, environmental
fragility, and visitor load, showing how different combinations of inputs are associated
with the recommended level of marketing intensity.
Surface analysis revealed three key decision heuristics embedded in the fuzzy rule
base. First, a satisfaction-dominant region emerged where when satisfaction ≥ 0.7, mar-
keting intensity remained moderate-to-high regardless of fragility or load, representing
‘reward excellence’ logic. Second, a fragility-sensitive region was identified where fra -
gility ≥ 0.7 marketing intensity sharply declined, particularly when combined with high
load, representing ‘precautionary principle’ logic. Third, a load-compensation region
demonstrated that high load alone did not automatically suppress marketing intensity
Table 8 Marketing process performance before and after DMAIC implementation
Performance
indicator
Baseline
mean
( SD)
Post-
DMAIC
mean
( SD)
Abso-
lute
change
%
Change
Test statistic p-value Ef-
fect
Size
Campaign Response
Time (hrs)
48.5 (8.2) 31.2 (5.4) −17.3 −35.7% t (248) = 6.42 < 0.001 d =0 .81
Inquiry Resolution
Rate (%)
71.0 (12.3) 89.0 (7.8) + 18.0 + 25.4% χ 2 (1) = 9.87 < 0.01 ϕ =0 .42
Customer Satisfac-
tion Score
4.01 (0.68) 4.32 (0.61) + 0.31 + 7.7% t (248) = 3.89 < 0.001 d =0 .49
Process Variance
( σ 2)
1.42 0.86 −0.56 −39.4% Levene’sF =8 .93 < 0.01 η 2 =0 .11
Process Capability
Index ( Cp)
0.94 1.42 + 0.48 + 51.1% – – –

Page 17 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
when satisfaction and low fragility co-occurred, representing ‘demand-responsive’ logic
for stable ecological conditions.
Table 9 presents fuzzy inference system outputs for three representative scenarios.
Under Scenario 1 (Stable Eco-Conditions), with satisfaction = 0.82 (High), fragility = 0.28
(Low), and visitor load = 0.41 (Low-Medium), the system fired rules R1, R2, R4, and R12,
producing an aggregated marketing intensity of 0.80, categorized as High. Under Sce -
nario 2 (Moderate Ecological Stress), with satisfaction = 0.61 (Medium), fragility = 0.68
Fig. 4 Triangular membership functions for input and output variables

Fig. 3 Process control charts: baseline vs. post-DMAIC implementation

Page 18 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
(Medium-High), and visitor load = 0.57 (Medium), the system fired rules R8, R14, R16,
and R22, producing an aggregated marketing intensity of 0.51, categorized as Medium.
Under Scenario 3 (High Ecological Risk), with satisfaction = 0.33 (Low-Medium), fragil -
ity = 0.91 (High), and visitor load = 0.79 (High), the system fired rules R9, R18, R24, and
R27, producing an aggregated marketing intensity of 0.19, categorized as Low. To fur -
ther illustrate the practical implications of the fuzzy inference system, Fig.  6 presents
the defuzzified marketing intensity values across three representative ecological sce -
narios. The figure highlights how recommended marketing intensity varies according to
Table 9 Fuzzy inference system output—three representative scenarios
Scenario Satisfaction Fragility Load Fired
Rules
Aggre-
gated
MI
Lin-
guis-
tic
Term
Scenario 1: Stable
Eco-Conditions
0.82 (High) 0.28 (Low) 0.41
(Low-Medium)
R1, R2, R4,
R12
0.80 High
Scenario 2: Moderate
Ecological Stress
0.61 (Medium) 0.68
(Medium-High)
0.57 (Medium) R8, R14,
R16, R22
0.51 Me-
dium
Scenario 3: High Ecologi-
cal Risk
0.33
(Low-Medium)
0.91 (High) 0.79 (High) R9, R18,
R24, R27
0.19 Low
Fig. 5 Three-dimensional fuzzy rule surfaces for marketing intensity

Page 19 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
ecological conditions and risk levels, demonstrating the context-sensitive behavior of the
proposed decision model.

While Fig. 6 provides a visual comparison of the defuzzified marketing intensity across
ecological scenarios, Table  9 presents the corresponding numerical outputs and acti -
vated fuzzy rules for each scenario.
5.5 Integrated framework performance assessment
Table  10 summarizes the pre- and post-integration performance comparison across
four strategic dimensions. Decision responsiveness improved from 3.8 ( SD =0 .7) to
4.5 ( SD =0 .5), an 18.4% increase ( t =5 .23,p < 0.001, Cohen’s d =0 .66, medium-
large effect). Sustainability alignment improved from 3.9 ( SD =0 .6) to 4.6 ( SD =0 .4
), a 17.9% increase ( t =5 .01,p < 0.001, Cohen’s d =0 .63, medium-large effect). Mar -
keting efficiency improved from 4.0 ( SD =0 .6) to 4.7 ( SD =0 .4), a 17.5% increase
( t =4 .89,p < 0.001, Cohen’s d =0 .62, medium-large effect). Competitive posi -
tioning index improved from 3.7 ( SD =0 .8) to 4.6 ( SD =0 .5), a 24.3% increase
( t =6 .18,p < 0.001, Cohen’s d =0 .78, large effect).
Table 10 Performance comparison before and after framework implementation
Performance dimension Pre-inte-
gration
mean
( SD)
Post-in-
tegration
mean
( SD)
Abso-
lute
change
%
Change
t-statistic p-value Ef-
fect
Size
( d)
Decision Responsiveness
(1–5)
3.8 (0.7) 4.5 (0.5) + 0.7 + 18.4% 5.23 < 0.001 0.66
Sustainability Alignment
(1–5)
3.9 (0.6) 4.6 (0.4) + 0.7 + 17.9% 5.01 < 0.001 0.63
Marketing Efficiency (1–5) 4.0 (0.6) 4.7 (0.4) + 0.7 + 17.5% 4.89 < 0.001 0.62
Competitive Positioning
Index
3.7 (0.8) 4.6 (0.5) + 0.9 + 24.3% 6.18 < 0.001 0.78
Fig. 6 Defuzzified marketing intensity across three ecological Scenarios

Page 20 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
5.6 Hypotheses testing summary
Table 11 summarizes the assessment of the proposed hypotheses. Overall, the findings
were consistent with all four proposed hypotheses within the context of the present
study.
H1 (SDM adoption → improved decision intelligence) was supported through expert
panel evaluation and managerial interviews confirming enhanced contextual sensi -
tivity, with quantitative evidence of 18.4% improvement in decision responsiveness.
H2 (DSSM-DMAIC → marketing process efficiency) was supported through process
capability analysis demonstrating Cp improvement from 0.94 to 1.42 (51.1% increase),
35.7% reduction in response time ( p< 0.001), and 39.4% reduction in process vari -
ance ( p< 0.01). H3 (Fuzzy Logic → uncertainty management capability) was supported
through scenario simulation demonstrating adaptive marketing intensity modulation
from 0.19 under high ecological risk to 0.80 under stable conditions, with a validated
27-rule inference system. H4 (integrated DSSM-Fuzzy Logic → sustainable competitive
advantage) was supported through composite performance index demonstrating 24.3%
improvement in competitive positioning ( p< 0.001) and 17.9% improvement in sus -
tainability alignment ( p< 0.001), with stakeholder validation confirming strategic value.
These findings provide evidence that is consistent with the proposed hypotheses
within the scope of the present study.
Figure 7 presents the path analysis results with standardized coefficients and model fit
indices. All hypothesized relationships were found to be positive and statistically signifi -
cant, supporting the proposed theoretical model and suggesting meaningful explanatory
potential within the study context.
Specifically, Smart Digital Marketing (SDM) exhibited a significant positive effect on
decision intelligence (β = 0.52, p < 0.001), Digital Six Sigma Marketing (DSSM) showed a
significant positive effect on process efficiency (β = 0.58, p < 0.001), and Fuzzy Logic dem-
onstrated a significant positive effect on uncertainty management (β = 0.61, p < 0.001).
Furthermore, the integrated DSSM–Fuzzy Logic framework had a significant positive
effect on sustainable competitive advantage (β = 0.63, p < 0.001).
Model fit indices indicated excellent model fit (χ ²/df = 1.84, CFI = 0.96, RMSEA =
0.058, SRMR = 0.041), meeting or exceeding recommended threshold values for struc -
tural equation modeling [ 46]. These findings also support the theoretical argument that
Table 11 Comprehensive hypotheses assessment
Hypothesis Statement Assessment method Key evidence Re-
sult
H1 SDM adoption →
Improved decision
intelligence
Expert panel
evaluation; managerial
interviews
Decision responsiveness + 18.4%;
qualitative confirmation of en-
hanced contextual sensitivity
Sup-
port-
ed
H2 DSSM-DMAIC →
Marketing process
efficiency
Process capability
analysis; hypothesis
testing
Cp: 0.94 → 1.42 (+ 51.1%); Re-
sponse time − 35.7% (p< 0.001);
Variance − 39.4% ( p< 0.01)
Sup-
port-
ed
H3 Fuzzy Logic → Uncer-
tainty management
capability
Scenario simulation;
sensitivity analysis
Adaptive MI modulation: 0.19 (high
risk) to 0.80 (low risk); 27-rule infer-
ence system validated
Sup-
port-
ed
H4 Integrated DSSM-
Fuzzy Logic → Sus-
tainable competitive
advantage
Composite perfor-
mance index; stake-
holder validation
Competitive positioning + 24.3%
( p< 0.001); Sustainability align-
ment + 17.9% ( p< 0.001)
Sup-
port-
ed

Page 21 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
combining operational efficiency and strategic flexibility can generate sustainable com -
petitive advantage in complex environments [47].
Overall, the path analysis suggests that Smart Digital Marketing (SDM) contributes to
sustainable competitive advantage through complementary mechanisms of operational
excellence (DSSM-DMAIC) and strategic flexibility (Fuzzy Logic), providing evidence
consistent with the proposed nomological network. To provide a visual summary of the
structural model results, Fig.  7 presents the standardized path coefficients and the over -
all model fit indices.
6 Discussion
6.1 Synthesis of key findings
This study developed and empirically evaluated an integrated Smart Digital Marketing
(SDM) framework combining Digital Six Sigma Marketing (DSSM) with fuzzy logic-
based decision modeling within fragile ecotourism contexts. The findings suggest that
the hybrid framework was associated with improvements in marketing process perfor -
mance, decision responsiveness, sustainability alignment, and competitive position -
ing within the study setting. The results indicate that this hybrid system contributes to
improved marketing process performance, enhanced decision responsiveness, stronger
sustainability alignment, and improved competitive positioning.
Three principal findings are discussed in relation to the existing literature and the
study context.
First, the DSSM-DMAIC approach appeared effective in addressing marketing pro -
cess inefficiencies within the study context. The observed 35.7% reduction in campaign
response time, 25.4% improvement in inquiry resolution, and 39.4% reduction in process
variance suggest that Six Sigma methodologies—despite their manufacturing origins—
can be adapted to sustainability-sensitive service environments. These findings extend
Chaplin’s [15] argument regarding marketing as an underutilized domain for Lean Six
Sigma by providing additional empirical evidence of its applicability when supported by
digital integration and contextual adaptation.
Fig. 7 Path analysis results with standardized coefficients and model fit indices

Page 22 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
Second, the fuzzy logic component enabled the translation of qualitative ecological
variables into structured marketing recommendations. The observed findings suggest
that incorporating ecological conditions into the decision process can support more
adaptive and context-sensitive marketing planning. The fuzzy inference system mod -
eled qualitative and linguistically expressed variables—satisfaction, environmental fra -
gility, and visitor load—and translated them into marketing intensity recommendations
aligned with environmental carrying capacity. This approach addresses a key limitation
of traditional marketing analytics, which often struggle to integrate sustainability-related
variables expressed in qualitative terms. The model’s adaptive behavior—higher pro -
motional intensity under stable conditions (MI = 0.80) and lower promotional intensity
under ecological stress (MI = 0.19)—suggests that sustainability objectives and competi -
tive positioning may be jointly managed through an appropriate decision framework.
Third, integrating DSSM with fuzzy logic appears to offer complementary capabilities
by combining structured process improvement with adaptive decision support. Within
the present study, this integration was associated with improvements across several
marketing performance indicators. The observed 24.3% improvement in the competitive
positioning index was greater than the individual observed improvements in efficiency
(17.5%) and sustainability alignment (17.9%), suggesting potential complementary
effects rather than isolated associations. These findings are consistent with the proposi -
tion that process optimization and adaptive reasoning may function as mutually rein -
forcing capabilities within the context of the present study.
6.2 Theoretical contributions
This research offers four key theoretical contributions. First, it advances existing litera -
ture by integrating Six Sigma methodology with Fuzzy Logic within a unified market -
ing decision-support framework. While prior studies have examined these approaches
separately, this study highlights their complementary roles and proposes an integrated
architecture that bridges process optimization with adaptive reasoning. This responds to
calls in sustainable tourism research for methodological approaches that combine quan -
titative rigor with qualitative insight [2].
Second, the findings extend Resource-Based View (RBV) theory [ 21] by conceptual -
izing Smart Digital Marketing (SDM) as a dynamic capability tailored to sustainability-
constrained environments. The proposed framework is conceptualized as exhibiting
VRIN characteristics: valuable (supporting both efficiency and sustainability objectives),
relatively rare among ecotourism operators, difficult to imitate (through embedded tacit
knowledge within fuzzy rule systems and process learning), and non-substitutable (as
alternative approaches may not adequately resolve the precision–adaptability tension).
The empirical findings are consistent with this proposition. The observed improve -
ments in decision responsiveness, sustainability alignment, and competitive position -
ing suggest that SDM may enable organizations to sense environmental changes, seize
market opportunities, and reconfigure marketing processes in response to ecological
constraints. These characteristics are broadly consistent with the dynamic capability
framework proposed by Teece (2007).
Third, this study operationalizes the well-recognized tension between economic via -
bility and ecological conservation—extensively documented in the sustainable tourism
literature through carrying capacity models [ 7], Limits of Acceptable Change (LAC)

Page 23 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
frameworks, and adaptive management approaches—within a computational decision-
support system. The contribution is not the identification of this tension (which has
been recognized for decades) but rather its formal operationalization through a fuzzy
inference system that translates qualitative expert knowledge into quantifiable decision
parameters. While existing frameworks (e.g., LAC) provide principles for managing
tourism impacts, they typically do not provide rule-based decision support that can be
integrated with marketing automation systems. The fuzzy inference system presented
here (Sect. 4.6) encodes the precautionary principle (high fragility → low marketing
intensity) and demand-responsive adjustment (high load + low fragility → moderate
intensity) as executable rules, enabling a more systematic rather than ad hoc application
of adaptive management principles to marketing decisions [48].
Fourth, the mixed-methods approach—combining survey data, stakeholder inter -
views, environmental observation, process capability analysis, and computational mod -
eling—offers a methodological contribution to sustainable tourism research, supporting
a more contextually grounded and empirically robust approach.
6.3 Practical and managerial implications
6.3.1 Implication 1 (Marketing Intensity Calibration)
The fuzzy inference system provides decision thresholds informed by the empirical find -
ings of the present study.
At Adrère Amellal, when environmental fragility exceeds 0.7 (approximately 4.9 on
a 7-point scale) and visitor load exceeds 0.7 ( ≥ 85% of carrying capacity), market -
ing intensity is reduced to 0.19 (corresponding to a budget reduction of approximately
65% and suspension of digital advertising). This threshold was applied during the study
period and was associated with a 35.7% reduction in campaign response time, while
occupancy remained within the observed baseline range (67% post-implementation
compared to the 65–70% baseline).
6.3.2 Implication 2 (Process Control Limits)
The DMAIC implementation established statistical process control limits for cam -
paign response time (UCL = 42 h, LCL = 20 h, target = 31 h). Managers can now monitor
weekly performance against these limits; five weeks post-implementation, response time
remained within control limits, suggesting that the observed improvement was main -
tained during the monitoring period.
6.3.3 Implication 3 (Rule Base Adaptation Protocol)
The 27-rule base can be adapted to other contexts using the following protocol: (1)
conduct stakeholder workshops to identify relevant linguistic terms; (2) elicit member -
ship function parameters using the method of anchor points (asking experts to identify
crossover values where membership changes from “Low” to “Medium”); (3) validate the
rule base using holdout scenarios.
6.3.4 Implication 4 (Sustainability Alignment Metrics)
The observed 17.9% improvement in sustainability alignment was reflected in specific
operational metrics, reduction in promotional emails sent during high-fragility periods

Page 24 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
(from 12 to 3 per week), elimination of discount offers when visitor load exceeded 0.8,
and reallocation of 40% of digital advertising budget to off-peak periods.
6.3.5 Implication 5 (ROI Calculation)
Framework implementation cost was approximately USD $8,500 (12 staff training hours
at $75/hour plus MATLAB licensing). The observed 24.3% improvement in competi -
tive positioning was accompanied by a 12% increase in direct bookings (from 23 to 35%
of total bookings) and a 9% reduction in customer acquisition cost. Based on these
observed outcomes, the estimated return on investment (ROI) within six months was
approximately 210%.
6.4 Our work with limitations and boundary conditionsPlease change the Section 6.4
heading from “Our work with limitations and boundary conditions” to “Limitations and
boundary conditions” for clarity and consistency with the single-author format.
The single-case design, while appropriate for theory elaboration and contextual depth
[20], imposes boundary conditions on generalizability. The framework was evaluated
within a premium-priced ecolodge (USD $400–600/night) serving an international,
highly educated clientele (56.8% bachelor’s degrees, 28.4% master’s degrees). This repre -
sents an “extreme case” [37] where sustainability practices are highly advanced but mar -
keting intelligence systems remain underdeveloped—appropriate for theory elaboration
but not representative of mass-market ecotourism, community-based tourism, or bud -
get eco-accommodations. Transferability to contexts with different pricing structures,
visitor demographics, or ecological characteristics requires empirical validation.
The single-group pre-post design, while appropriate for exploratory evaluation of
framework feasibility, cannot rule out alternative explanations. Four specific threats
to internal validity are acknowledged. First, history effects: concurrent organiza -
tional changes (e.g., staff training, operational modifications) may have contributed to
observed improvements independent of the framework. Second, maturation: natural
process improvement over the 12-week implementation period may have contributed
to part of the observed improvements. Third, testing effects: pre-implementation mea -
surement may have sensitized staff to performance metrics, inducing behavioral changes
(Hawthorne effect). Fourth, seasonality: data were collected during early high season
(May 1–21, 2025); pre-post comparisons may reflect seasonal demand patterns rather
than framework effects.
To address these limitations, we reframe our findings as indicating practical feasibility
and providing associational evidence rather than causal proof. The observed improve -
ments (35.7% response time reduction, 39.4% variance reduction) are consistent with
the potential effectiveness of the framework but should not be interpreted as definitive
causal evidence. Future research should employ interrupted time series designs with
comparison sites, or cluster-randomized trials across multiple ecolodges, to strengthen
causal inference [49].
6.5 Assumptions and their justification
The proposed framework rests on several assumptions requiring explicit acknowledg -
ment. First, the fuzzy inference system assumes that linguistic terms (Low, Medium,
High) and membership function parameters derived from expert consultation

Page 25 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
adequately capture stakeholder perceptions. While the Content Validity Index exceeded
0.83, indicating expert consensus, parameterization may not generalize to different
cultural or ecological contexts. Second, the DMAIC implementation assumes pro -
cess stability and measurement system adequacy; while Measurement System Analy -
sis (MSA) was conducted with acceptable results (%GRR = 12.4%), the assumption of
statistical control was verified using Shewhart control charts. Third, the framework
assumes that marketing intensity decisions can meaningfully influence visitor behavior
and environmental outcomes within the study’s temporal horizon; longitudinal valida -
tion is required to confirm sustainability outcomes over extended periods. Fourth, the
normalization procedure assumes linear transformation from Likert scales to the [0, 1]
interval; alternative transformations (e.g., logarithmic for skewed distributions) may be
more appropriate in other contexts.Please add the following clarification at the end of
Section 6.5: “ Accordingly, the fuzzy outputs should be interpreted as context-dependent
decision-support estimates rather than mathematically exact or universally generalizable
predictions. ”
7 Conclusion
This study developed and empirically evaluated a hybrid Smart Digital Marketing (SDM)
framework that integrates Digital Six Sigma Marketing (DSSM) with fuzzy logic-based
decision modeling to support sustainability-oriented decision-making in fragile ecotour-
ism environments.
The framework was operationalized and tested at Adrère Amellal ecolodge, Siwa
Oasis, Egypt, using a mixed-methods design combining survey data ( N = 250), stake-
holder interviews ( N = 18), environmental observation scorecards, and computational
modeling.
Three core contributions emerge. First, the findings suggest that structured process
optimization (DSSM-DMAIC) and adaptive uncertainty management (fuzzy logic)
appear to provide complementary rather than competing capabilities. The observed
24.3% improvement in competitive positioning was greater than the individual observed
improvements in efficiency (17.5%) and sustainability alignment (17.9%), suggesting
potential complementary effects.Please make the following minor editorial correc -
tions in the Conclusion: (1) Please delete the standalone phrase “suggesting synergistic
effects. ” as it is redundant and may overstate the interpretation of the findings. (2) In the
final paragraph, please remove the duplicated wording so that the sentence reads: “From
a practical standpoint, the framework may support organizations in embedding ecologi -
cal thresholds within marketing decision rules, aligning promotional intensity with envi-
ronmental carrying capacity. ” These are editorial clarifications only and do not alter the
results or conclusions of the study.
suggesting synergistic effects. Second, the study presents a detailed mathematical for -
malization of fuzzy logic for sustainable marketing decisions, including complete speci -
fication of membership functions, inference procedures, and defuzzification (Sect.  4.6).
Third, the study contributes to Resource-Based View theory by conceptualizing Smart
Digital Marketing as a dynamic capability that is conceptualized as exhibiting VRIN
characteristics in sustainability-constrained environments.
From a practical standpoint, the framework may support organizations in embedding
ecological thresholds within marketing decision rules to embed ecological thresholds

Page 26 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
within marketing decision rules, aligning promotional intensity with environmental
carrying capacity. The fuzzy inference system offers transparent, interpretable decision
rules that can be calibrated to local conditions.
7.1 Future research directions
Three testable propositions emerge for future investigation. P1: The synergistic effect of
DSSM-fuzzy integration on competitive positioning will be moderated by destination
fragility, with stronger effects in high-fragility contexts. P2: The framework’s effective -
ness will vary by tourism segment, with premium segments showing stronger sustain -
ability-alignment effects than mass-market segments. P3: Longitudinal application of
the framework will demonstrate non-linear relationships between marketing intensity
and environmental outcomes, with diminishing returns beyond ecological thresholds.
Future research should extend the framework to diverse ecotourism contexts (marine
protected areas, rainforest lodges, community-based tourism), employ quasi-exper -
imental designs (interrupted time series with comparison sites) to strengthen causal
inference, and integrate real-time environmental monitoring data (e.g., IoT sensors for
water quality, noise levels, wildlife disturbance) to support dynamic rule adaptation.
Supplementary Information
The online version contains supplementary material available at https://doi.org/10.1007/s43621-026-04432-x.
Supplementary Material 1
Author contributions
The author contributed to all aspects of the study, including conceptualization, methodology, formal analysis,
investigation, data curation, writing – original draft, writing – review & editing, visualization, and project administration.
Funding
Open access funding provided by The Science, Technology & Innovation Funding Authority (STDF) in cooperation with
The Egyptian Knowledge Bank (EKB).
Data availability
The datasets generated and/or analyzed during the current study are available from the corresponding author upon
reasonable request.
Declarations
Ethical Approval
This study was approved by the Research Ethics Committee, Faculty of Management and Business Intelligence, Modern
University for Technology and Information (MTI), Cairo, Egypt (Protocol No. REC-MTI-2025-04-07; approved on 20 April
2025).
Consent to Participate
Informed consent was obtained from all individual participants included in the study.
Consent to publish
Not applicable. The manuscript does not contain any individual person’s identifiable data.
Competing interest
The authors declare no competing interests.Please change “The authors declare no competing interests” to “The author
declares no competing interests” to reflect that this is a single-author article.
Received: 23 March 2026 / Accepted: 12 August 2026
References
1. Verhoef PC, Broekhuizen T, Bart Y, Bhattacharya A, Dong JQ, Fabian N, Haenlein M. Digital transformation: A multidisci-
plinary reflection and research agenda. J Bus Res. 2021;122:889–901.
2. Zhang Y, Deng B. Exploring the nexus of smart technologies and sustainable ecotourism: A systematic review. Heliyon.
2024;10(11):e31996.

Page 27 of 27
El Sharkawey Discover Sustainability          (2026) 7:1445
3. Kohli AK, Jaworski BJ. Market orientation: The construct, research propositions, and managerial implications. J Mark.
1990;54(2):1–18.
4. Ranjan J, Foropon C. Big data analytics in building competitive intelligence. Int J Inf Manage. 2021;56:102231.
5. Han H, Kim Y. An investigation of green hotel customers’ decision formation. Int J Hosp Manag. 2010;29(2):261–70.
6. Wang N. Using the fuzzy method and multi-criteria decision making to analyze the impact of digital economy on urban
tourism. Int J Comput Intell Syst. 2024;17(1):122.
7. Hussain K, Ali F, Raghavan M, Manzoor S. Interpretive structural modeling of barriers to sustainable tourism development:
A developing economy perspective. Sustainability. 2024;16(13):5442.
8. Esmaelnezhad D, Soltani S, Ghafoori V. A fuzzy hybrid approach to analyse digital marketing strategies towards tourism
industry. Int J Tour Policy. 2023;13(5):463–80.
9. Dejprayoon J, Srisawat S, Namsak K, Chaisuwan W. Determinants of customer intention for sustainable tourism packages
in Thailand using rough set-fuzzy theory. J Fuzzy Ext Appl. 2025;6(3):522–54.
10. Zadeh LA. Fuzzy sets. Inf Control. 1965;8(3):338–53.
11. Sadjadi SJ, Seyedhosseini SM, Hassanlou K. Fuzzy pricing and marketing planning model. Expert Syst Appl.
2010;37(10):7319–27.
12. Harry MJ, Schroeder R. Six Sigma: The breakthrough management strategy. New York: Doubleday; 2006.
13. Pyzdek T, Keller P . The Six Sigma handbook. 4th ed. New York: McGraw-Hill; 2014.
14. Chaplin L. Lean Six Sigma and marketing: A missed opportunity. Int J Prod Perform Manag. 2014;63(5):665–74.
15. Garza-Reyes JA, Kumar V, Chaikittisilp S, Tan KH. A Six Sigma DMAIC approach to improve the sales process of a technology
start-up. Int J Lean Six Sigma. 2021;12(3):521–48.
16. Achrol RS, Kotler P . Frontiers of the marketing paradigm in the third millennium. J Acad Mark Sci. 2012;40(1):35–52.
17. Kumar V, Rahman Z, Kazmi AA. Evolution of sustainability as marketing strategy. Mark Intell Plan. 2012;30(3):303–27.
18. Cruz RN. Data-driven decision-making in marketing: A systematic review (PRISMA 2020). Systems. 2025;13(2):45–68.
19. Barney J. Firm resources and sustained competitive advantage. J Manag. 1991;17(1):99–120.
20. Teece DJ, Pisano G, Shuen A. Dynamic capabilities and strategic management. Strateg Manag J. 1997;18(7):509–33.
21. Baldassarre F, Campo R. Sustainability as a marketing tool. Bus Horiz. 2016;59(4):421–9.
22. Antony J. Readiness factors for Lean Six Sigma. Int J Prod Perform Manag. 2014;63(2):257–64.
23. Silva IB, Santos G, Silva R, Sampaio P . Lean Six Sigma framework for competitiveness. Acta Sci Technol. 2019;41:e38956.
24. Mojumder MU. Impact of lean six sigma on manufacturing efficiency. ASRC Procedia. 2025;1(1):343–75.
25. Rahman MA, Kabir A, Hossain MS. ERP and CRM integration tools meta-analysis. ASRC Procedia. 2025;1(1):278–312.
26. Kong X, Zhang L, Wang Y. Total quality management in sustainable tourism. Humanit Soc Sci Commun. 2025;12(1):1–16.
27. Shojaei P , Ghasemi S, Fathi MR. Medical tourism barriers using fuzzy cognitive mapping. J Health Manag.
2024;26(4):611–23.
28. Flores-Romero J, Perez-Romero ME, Alvarez-Garcia J. Fuzzy methods for sustainable tourism indicators. Sustainability.
2021;13(8):4321.
29. Prashar A, S M V. Sustainable development in SMEs. J Clean Prod. 2019;245:118665.
30. Syed FU. Digital technologies in reputation management. Cheltenham: Edward Elgar Publishing; 2025.
31. Porter ME. Competitive advantage: Creating and sustaining superior performance. New York: Free; 1985.
32. Hu J, Lin B, Fu X. Immersion in cheers: Experiencescape, customer inspiration, and drink statues in craft beer tourism using
PLS-SEM, IPMA, and ANN. J Vacat Mark. 2026. https://doi.org/10.1177/13567667251409422.
33. Creswell JW, Clark VLP . Designing and conducting mixed methods research. 3rd ed. SAGE; 2017.
34. Bryman A. Social research methods. 5th ed. Oxford University Press; 2016.
35. Yin RK. Case study research and applications. 6th ed. SAGE; 2018.
36. Eisenhardt KM. Building theories from case study research. Acad Manag Rev. 1989;14(4):532–50.
37. Patton MQ. Qualitative Research & Evaluation Methods. 4th ed. SAGE; 2015.
38. Cochran WG. Sampling techniques. 3rd ed. Wiley; 1977.
39. Faul F, Erdfelder E, Buchner A, Lang AG. G*Power 3.1 statistical power analysis. Behav Res Methods. 2009;41(4):1149–60.
40. Cohen J. Statistical power analysis. 2nd ed. Lawrence Erlbaum; 1992.
41. DeVellis RF. Scale development. 4th ed. SAGE; 2017.
42. Hair JF, Black WC, Babin BJ, Anderson RE. Multivariate data analysis, 8th edn. Cengage; 2019.
43. Rivera MM, Olvera-Gonzalez E, Escalante-Garcia N. UPAFuzzySystems: A Python library for control and simulation with
fuzzy inference systems. Machines. 2023;11(5):572. https://doi.org/10.3390/machines11050572.
44. Podsakoff PM, MacKenzie SB, Lee JY, Podsakoff NP . Common method bias. J Appl Psychol. 2003;88(5):879–903.
45. Nunnally JC, Bernstein IH. Psychometric theory. 3rd ed. McGraw-Hill; 1994.
46. Hu LT, Bentler PM. Fit index criteria. Struct Equ Model. 1999;6(1):1–55.
47. Smith WK, Lewis MW. Theory of paradox. Acad Manag Rev. 2011;36(2):381–403.
48. Lin B, Huang L, Wang C. Virtual tourism destination ambassadors enhancing social media engagement: Technology mind-
fulness perspectives. J Vacat Mark. 2025. https://doi.org/10.1177/13567667251400785.
49. Yang R, Lin B, Lee W. An explanatory mixed method study of outdoor food delivery robots: Technology affordance
approach. Asia Pac J Mark Logist. 2025;1–17. https://doi.org/10.1108/apjml-03-2025-0457.
Publisher’s note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
