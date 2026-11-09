---
title: Fraud Detection in Subsidized LPG Gas Distribution at the Base Level as a Monitoring System Using
  the Mamdani Fuzzy Logic Algorithm
url: https://doi.org/10.69916/jkbti.v5i3.551
category: ai-marketing
subcategory: framework
date: 2026-09
venue: Jurnal Kecerdasan Buatan dan Teknologi Informasi.
authors:
- M.Syahrul
- R Wisnu Prio Pamungkas Pamungkas
- Fried Sinlae
source: openalex-oa
pdf_url: https://ojs.ninetyjournal.com/JKBTI/article/download/551/239
pages: 10
chars: 35545
fetched_at: '2026-11-08T20:04:00+00:00'
kb_version: 1
---

# Fraud Detection in Subsidized LPG Gas Distribution at the Base Level as a Monitoring System Using the Mamdani Fuzzy Logic Algorithm

Jurnal Kecerdasan Buatan dan Teknologi Informasi
Vol. 5, No. 3, September 2026, pp. 475–484
e-ISSN: 2964-2922, p-ISSN: 2963-6191
Original Research
Fraud Detection in Subsidized LPG Gas Distribution at the
Base Level as a Monitoring System Using the Mamdani
Fuzzy Logic Algorithm
M. Syahrul a, R Wisnu Prio Pamungkas b∗, Fried Sinlae c
a,b,c Informatics Department, Faculty of Computer Science, Universitas Bhayangkara Jakarta Raya, Bekasi, Indonesia
*Corresponding Author: wisnu.prio@dsn.ubharajaya.ac.id
ABSTRACT
The distribution of subsidized Liquefied Petroleum Gas (LPG) at pangkalan
levels is still prone to fraud, such as discrepancies between stock and distribu-
tion volumes, sales above the maximum retail price (HET), and undelivered
distributions, all of which are still mostly supervised manually. These con-
ditions make it difficult to quickly and objectively detect the presence of a
fraudulent distribution pattern. This research develops a Mamdani Fuzzy
Logic-based fraud detection engine that functions as a real-time monitoring
system for subsidized LPG gas distribution. The system was developed using
the Waterfall method, which includes requirements analysis, design, imple-
mentation, and testing, and was built with Laravel, React.js, and Inertia.js
as a Single Page Application (SPA) architecture. Fraud-indication analysis
involves three fuzzy input variables — remaining stock, daily distribution
volume, and the Purchase Order (PO) submitted to the agent. They are
processed through fuzzification, a 27-rule rule base, MIN-MAX inference, and
Centroid of Area defuzzification. The output is three categories: safe (aman),
alert (waspada), and irregular/indicative of fraud (menyimpang). Real trans-
action data from Pangkalan Gas Asmalia for May 2026 shows that a daily
distribution of 18 cylinders against a daily quota of 46 cylinders resulted in a
crisp output of 16.20, which falls under the Safe category and is in line with
actual field conditions. This system would enable the pangkalan operators
to identify early fraud signals, have more structured and objective decision-
making, and enhance the accountability of subsidized LPG distribution.
Copyright©2026 by Author(s). This is an open-access article distributed under the
terms of the Creative Commons Attribution 4.0 International License (CC BY 4.0).
How to Cite:
M. Syahrul, R. W. P. Pamungkas, and F. Sinlae, “Fraud Detection in Subsidized LPG
Gas Distribution at the Base Level as a Monitoring System Using the Mamdani Fuzzy
Logic Algorithm,”J. Kecerdasan Buatan dan Teknol. Inf., vol. 5, no. 3, pp. 475–484,
2026.
Doi:https://doi.org/10.69916/jkbti.v5i3.551
KEYWORDS
Subsidized LPG
Fraud Detection
Mamdani Fuzzy Logic
Distribution Monitoring
Single Page Application
ARTICLE INFO
Received: June 22, 2026
Accepted: August 17, 2026
Available Online: September 1, 2026
1. INTRODUCTION
The subsidized Liquefied Petroleum Gas (LPG) distribution is one of the most important components to fulfill
the energy need of the Indonesian people, mainly for households and micro-enterprises. The Government,
through the Ministry of Energy and Mineral Resources, has set the Subsidized LPG quota at 8.3 million metric
tons for 2024 [1]. The large scale at which this is distributed requires an effective and structured monitoring
system to ensure that fraud does not take place during the process. However, the base level of distribution
remains mostly manual, recording simply being stock and distribution, hence no real-time monitoring.
Fraud in the context of subsidized LPG distribution would be any action that causes distribution to deviate from
the regulations, intentional or due to weak controls, including mismatches in stock and sales levels, allocation
irregularities, salesbeyondtheMaximumRetailPrice(MRP),andinflatedpurchaseorderstodealers. According
Page 475

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
to information from the INDEF Policy Brief, nearly 62.3% of 3 kg LPG subsidies are still enjoyed by financially
capable groups of people [2], which means that the distribution of LPG at subsidized rates can be prone to
targeting irregularities and may be considered a kind of fraud in energy subsidies. Research has indicated that
about 40% of 3 kg LPG subsidies are still facing problems with distribution targeting deviations [3], making it
quite an off-target distribution.
Previous research on LPG distribution monitoring has been mainly concerned with the manual monitoring
of price and distribution compliance. A study in Batam City indicated that LPG sales over the HET still
took place, indicating that the distribution monitoring was not running optimally [4]. Another study created
a web-based system for LPG stock and distribution information at Pangkalan Mujitahid. It improved data
recording but did not include automatic analysis for irregularities in distribution [5]. In another field, research
on an early warning system through continuous auditing and monitoring in public-sector procurement showed
that automated early detection could continuously and in real time identify irregularities [6]; however, such an
approach has not been adopted in subsidized energy distribution at the base level.
One of the intelligent computational methods for fraud detection in LPG distribution is the Mamdani Fuzzy
Logic method. It can handle dynamic and uncertain data by using linguistic values such as low, medium, and
high [7]. Based on the identified research gap, which is the absence of an integrated system that combines web-
based LPG distribution monitoring with automatic fraud detection using an AI method at the base level, this
study proposed the construction of a distribution monitoring system for Pangkalan Gas Asmalia with a fraud
detection engine based on Mamdani Fuzzy Logic. The proposed system uses three input variables: remaining
stock, daily distribution volume, and Purchase Order (PO) to the agent. The system was developed using
Laravel, React.js, and Inertia.js applying a Single Page Application (SPA) architecture so that fraud detection
runs automatically and in real time each time distribution data is saved.
Based on these issues, the research objectives are: (1) to design and build a web-based LPG gas distribution
monitoring system using SPA architecture; (2) to build real-time LPG stock and distribution monitoring fea-
tures; (3) to apply the Mamdani Fuzzy Logic method [8–11] as a fraud detection engine to analyze distribution
irregularity levels; and (4) to produce safe, alert, and irregular output categories as the basis for decision-making
in distribution supervision at Pangkalan Gas Asmalia.
2. RESEARCH METHODS
This study applies the Waterfall software development method. The Waterfall model is a type of sequential and
structured development model in software engineering, in which progress is seen as flowing steadily downwards
through the phases of conception, initiation, analysis, design, construction, testing, production/implementation,
and maintenance [12]. This method was chosen because the requirements and scope of the LPG distribution
fraud detection system were well defined at the beginning, so that each stage could be carried out in a focused
and measurable manner. The research stages include problem identification; data collection through observation
and literature study; and system development, which includes analysis, design, implementation, and testing.
The research stages also include the development of the Mamdani Fuzzy fraud detection engine (fuzzification,
rule base formation, MIN inference, MAX aggregation, and Centroid of Area defuzzification) and end with
system results and research conclusions.
2.1. Research Object and Data Sources
The research object is Pangkalan Gas Asmalia as a subsidized LPG distribution case study. Primary data were
collected through direct observation in the form of warehouse stock data, daily distribution summaries, and
monthly Purchase Order (PO) data from the base to the agent for May 2026. These data were used both as
the basis for system requirements analysis and as test data for the Mamdani Fuzzy algorithm.
2.2. Current System Analysis and Proposed System
The Pangkalan Gas Asmalia gas station currently still records inventory and delivery data in a fully manual
mode, and fraud is only identified manually by the station manager, which carries the core defects of delayed
recognition and subjective judgment. In the original system, base specialists are responsible for receiving inven-
tory, maintaining accounting ledgers, delivering LPG, and entering delivery data, while the station manager is
responsible for verifying reports, conducting inspections, tracing delivery histories, and issuing delivery evalua-
Page 476

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
tions. This study puts forward a full-process digital upgrade scheme, under which all business data is entered
into a web-based system. Every time delivery data is saved, the Mamdani Fuzzy fraud detection engine is
triggered automatically.
2.3. Functional and Non-Functional Requirements
Functional requirements include: (a) role-based user authentication for the Base Owner and Base Officer; (b)
automatic execution of Mamdani Fuzzy analysis when distribution data is saved; (c) presentation of distribu-
tion condition analysis results in the Safe, Alert, or Irregular categories; and (d) a real-time LPG distribution
monitoring dashboard. Non-functional requirements include responsive system performance for real-time mon-
itoring, role-based authentication security, compatibility with modern web browsers, ease-of-use interface, and
online accessibility.
2.4. System Architecture Design
The system is designed using a client-server architecture [13] with a Model-View-Controller (MVC) pattern
on the backend. The backend was built using the Laravel framework [14], providing routing, authentication,
database migration, and Eloquent ORM features for interaction with the MySQL database [15]. The user
interface was built using React.js with a component-based approach and Virtual DOM for faster rendering
[16, 17]. Inertia.js serves as the bridge between Laravel and React.js, enabling a Single Page Application
(SPA) without separating frontend and backend into two separate projects [18]. In this architecture, the Model
component manages LPG stock, distribution, and fuzzy analysis result data; the View component renders the
user interface via React.js and Inertia.js; and the Controller component manages application logic, monitoring
processes, and executes the Mamdani Fuzzy fraud detection engine.
2.5. Mamdani Fuzzy Logic as the Fraud Detection Engine
The fraud detection engine in this study is implemented on the backend using the Mamdani Fuzzy method,
selected for its ability to process dynamic and uncertain data using linguistically interpretable rules [7]. The
Mamdani inference process consists of four stages: fuzzification, rule base formation, inference (rule evaluation),
and defuzzification [19].
a. Variable Determination
Variables are determined based on the daily quota of the base, derived by dividing the monthly quota of 1,200
cylinders by 26 effective working days per month to obtain a daily quota of 46 cylinders, as shown in Equation
(1):
Daily Quota= 1200 26 ≈46cylinders/day (1)
Three input variables are used: remaining LPG stock, daily distribution volume, and Purchase Order (PO)
submitted by the base to the agent, with one output variable representing the LPG distribution fraud indication
level. Table 1 presents the complete variable specifications.
Table 1: Input and Output Variables of the Fraud Detection System
No. Variable Value Range Linguistic Category
1 Remaining LPG Stock (Input) 0 – 46 cylinders Low, Medium, High
2 Daily Distribution Volume (Input) 0 – 46 cylinders Low, Medium, High
3 Purchase Order / PO to Agent (Input) 0 – 46 cylinders Low, Medium, High
4 Fraud Indication Level (Output) 0 – 100 Safe, Alert, Irregular
b. Fuzzification
Fuzzification is the process of converting crisp input values into linguistic values using a triangular membership
function. Function parameters are set based on the daily quota of 46 cylinders divided into three proportional
zones with inter-zone overlap following the basic principles of fuzzy logic. For a triangular membership function
with parametersa(lower bound),b(peak), andc(upper bound), the degree of membershipµ(x)is computed
Page 477

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
as Equation (2):
µ(x) =



0, x≤a
x−a
b−a , a < x≤b
c−x
c−b , b < x≤c
0, x > c
(2)
wherea=lower bound,b=peak,c=upper bound, andx=crisp input value. Table 2 presents the member-
ship function parameters for all variables.
Table 2: Membership Function Parameters for Input and Output Variables
Fuzzy Set (Input)a b cFuzzy Set (Output)a b c
Low (Rendah) 0 0 15 Safe (Aman) 0 0 40
Medium (Sedang) 11 23 35 Alert (Waspada) 20 50 80
High (Tinggi) 31 46 46 Irregular (Menyimpang) 60 100 100
c. Rule Base
With three input variables and three fuzzy sets per variable, the number of rule combinations formed is33 = 27
IF-THEN rules. Rules are constructed to represent all possible combinations of remaining stock, distribution
volume, and PO to agent as early indicators of distribution fraud. Table 3 presents the complete rule base.
Table 3: Rule Base for LPG Distribution Fraud Detection
Rule Stock Dist. PO Output Rule Stock Dist. PO Output
1 Low Low Low Alert 15 Medium Medium High Safe
2 Low Low Medium Alert 16 Medium High Low Alert
3 Low Low High Irregular 17 Medium High Medium Irregular
4 Low Medium Low Alert 18 Medium High High Irregular
5 Low Medium Medium Irregular 19 High Low Low Safe
6 Low Medium High Irregular 20 High Low Medium Safe
7 Low High Low Irregular 21 High Low High Alert
8 Low High Medium Irregular 22 High Medium Low Safe
9 Low High High Irregular 23 High Medium Medium Safe
10 Medium Low Low Safe 24 High Medium High Alert
11 Medium Low Medium Alert 25 High High Low Alert
12 Medium Low High Alert 26 High High Medium Alert
13 Medium Medium Low Safe 27 High High High Irregular
14 Medium Medium Medium Alert
As a fraud interpretation example, Rule 17 (Medium Stock, High Distribution, Medium PO→Irregular)
represents a condition where distribution far exceeds what is reasonable relative to available stock, which may
indicate off-target distribution or inflated distribution recording, patterns commonly found in the field.
d. Inference (Rule Evaluation)
The inference stage uses the MIN method as the implication function to determine the truth value of each active
rule, taking the smallest membership value from the three input variables in that rule [19], as formulated in
Equation (3):
µinference = min(µA1 , µA2 , µA3 )(3)
whereµ A1,µ A2, andµ A3 are the membership degrees of the first, second, and third input variables respectively.
Results from all active rules are then combined using the MAX (aggregation) method to obtain the fuzzy output
set, as in Equation (4):
µaggregation = max(µR1 , µR2 , . . . , µRn )(4)
whereµ R1 throughµ Rn are the inference results of each active rule.
e. Defuzzification
Page 478

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
DefuzzificationisperformedusingtheCentroidofArea(CoA)method, whichfindsthecentroidoftheaggregated
fuzzy output area as the crisp output value [4]. Before computing the centroid, a clipping process is applied to
the fuzzy set based on theα-predicate value from inference. For the triangular output fuzzy set with parameters
a, b, cclipped atα, the right-side clipping point is determined by Equation (5):
x1 =c−α(c−a)(5)
The crisp output valuez∗ is then computed by the CoA formula in Equation (6):
z∗ =
R
µ(z)z dzR
µ(z)dz (6)
wherez ∗ is the crisp output,µ(z)is the membership degree of the aggregated output, andzis the value on the
output axis. A higher crisp output value indicates a greater indication of conditions requiring further attention,
including potential distribution fraud.
2.6. Research Tools
Hardware:Intel Core i5-10300H @ 2.50 GHz processor, 16 GB RAM, 477 GB SSD storage, NVIDIA GeForce
GTX 1650 Ti 4 GB.Software:Windows 11 64-bit, Visual Studio Code, PHP 8.2.12, Laravel 11, React.js
19.0.0, Inertia.js 2.0.0, Node.js 22.15.1, Composer 2.8.9, MySQL 8.4, and XAMPP 3.3.0.
2.7. Testing Method
System testing was carried out using the Black Box Testing method, which focuses on system functionality
without examining internal code structure. Testing was performed by providing specific inputs and verifying
whether the resulting outputs — including fraud indication categories, matched expectations. Test coverage
includes role-based authentication, LPG stock and distribution data management, Mamdani Fuzzy analysis
process, distribution category result display, and the real-time monitoring dashboard.
3. RESULTS AND DISCUSSION
3.1. Fraud Detection System Design Results
The design results show that the proposed system successfully integrates LPG stock and distribution recording
functions with the Mamdani Fuzzy fraud detection engine. Each time the Base Officer saves distribution
data, the system automatically runs fuzzy analysis, triggered through an include relationship on the Manage
LPG Stock and Manage LPG Distribution processes, producing a Safe, Alert, or Irregular output category
without requiring additional action from the user. The Base Owner can directly view the analysis results on
the monitoring dashboard and use them as the basis for decision-making and distribution evaluation.
3.2. Fraud Detection Calculation Results Using Real Data from Pangkalan Gas Asmalia
The calculation was tested using real data from Pangkalan Gas Asmalia for the period 22–25 May 2026, with a
daily quota of 46 cylinders (1,200cylinders÷26working days). Input values used were: remaining warehouse
stock = 30 cylinders, daily distribution = 18 cylinders, and PO/demand to agent = 40 cylinders.
Fuzzification results for each input variable were calculated as follows:
µMedium(30) = 35−30 35−23 = 5 12 = 0.417(7)
µMedium(18) = 18−11 23−11 = 7 12 = 0.583(8)
µHigh(40) = 40−31 46−31 = 9 15 = 0.600(9)
Table 4 summarizes the complete fuzzification results.
The active combination is Stock = Medium (0.417), Distribution = Medium (0.583), PO = High (0.600),
corresponding to Rule 15 in Table 3 with output Safe (Aman). Applying the MIN inference method per
Equation (3):
µAman = min(0.417,0.583,0.600) = 0.417(10)
Page 479

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
Table 4: Fuzzification Results for Test Case Data
Variable ValueµLowµMediumµHigh
Remaining LPG Stock 30 0 0.417 0
Daily Distribution Volume 18 0 0.583 0
PO / Demand to Agent 40 0 0 0.600
Since only one rule is active, the MAX aggregation produces:µAman(aggregation) = max(0.417) = 0.417.
Defuzzification using the Centroid of Area method on the Safe fuzzy set (a= 0, b= 0, c= 40) clipped at
µ= 0.417:
x1 = 40−0.417(40−0) = 40−16.68 = 23.32(11)
z∗ = 402 + 40×23.32 + 23.322
3×(40 + 23.32) = 3076.62 189.96 ≈16.20(12)
Table 5: Fraud Detection Output Classification and Case Study Result
Crisp Value Range Category Operational Description
0 – 33 Safe Distribution running normally, no fraud indication
34 – 66 Alert Distribution requires attention / further verification
67 – 100 Irregular Distribution is indicated as fraudulent
16.20 Safe Result for Pangkalan Gas Asmalia (25 May 2026)
These results show that daily distribution of 18 cylinders is well below the daily quota of 46 cylinders and
proportional to available stock, so distribution in this period was assessed as normal and not indicative of fraud.
3.3. System Interpretation of Fraud Indication Scenarios
To illustrate the system’s detection capability, a comparison with other scenarios from Table 3 is instructive. For
example, if remaining stock is Low while daily distribution is High and the PO to agent is also High (Rule 9), the
system produces an Irregular output, indicating a mismatch between physical stock and recorded distribution —
a pattern commonly found in the field as off-target distribution or inflated distribution recording. Conversely,
a combination of stock and distribution that is proportional to demand, as tested with real data on Rule 15,
produces a Safe category. The systematically constructed rule base is thus capable of mapping distribution
variable combination patterns to measurable and consistent fraud risk levels.
3.4. Comparison with Previous Studies
Table 6 presents a comparison of the proposed system with relevant prior research on LPG distribution super-
vision and irregularity detection.
Table 6: Comparison of Fraud Detection Capabilities with Prior Studies
Study Focus Automatic Detection Real-Time
Dewi et al. [20] Subsidized LPG price & distribution supervi-
sion (manual)
No No
Saddami et al. [5] Web-based LPG stock & distribution informa-
tion system
No Yes (recording)
Pamungkas & Khalida [6] Early warning continuous auditing for public
procurement
Yes Yes
This Study LPG distribution monitoring + Mam-
dani F uzzy fraud engine
Y es Y es
The study by Dewi et al. [20] shows that manual LPG distribution supervision was unable to prevent above-
HET sales, while Saddami et al. [5] provided web-based stock and distribution recording but lacked automatic
Page 480

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
irregularity detection. The early warning approach via continuous auditing by Pamungkas & Khalida [6] demon-
strated that automated real-time detection is feasible, but only in the public procurement domain. This study
addresses the gap by adapting early detection to the subsidized energy distribution context at the base level,
combining web-based data recording with an automatically running Mamdani Fuzzy fraud detection engine.
3.5. System Strengths and Limitations
The system’s main strength is its ability to automatically and in real time generate fraud indication categories
each time data is saved, without requiring manual analysis by the Base Owner, using three variables relevant
to real base operations. Limitations include: testing was only performed on one base as a case study so
generalizability requires validation at other bases; only three input variables were used without considering
others such as consumer transaction history; and no comparative performance evaluation against other fuzzy
or machine learning methods for distribution fraud detection was conducted.
3.6. Practical Implications
Practically, this system can help Base Owners and Officers supervise gas distribution more effectively, simplify
stock and distribution data recording, and provide early warnings against fraud indications so they can be
addressed before escalating into larger irregularities. For the broader development of subsidized energy distri-
bution information systems, this study provides an implementation example integrating a web-based system
with an intelligent analysis method to improve the accountability and transparency of distribution.
3.7. Discussion
The evaluation of the proposed fraud detection system using real transaction data from Pangkalan Gas Asmalia
demonstrates the efficacy of the Mamdani Fuzzy Logic algorithm in translating complex, daily operational
variables into actionable intelligence. The test scenario, which recorded a daily distribution of eighteen cylinders
against a maximum daily quota of forty-six, yielded a crisp output of 16.20, categorizing the day’s operations
as safe. This mathematical outcome aligns perfectly with empirical field conditions, as distributing less than
half of the daily quota while maintaining proportional stock and purchase order levels represents normal, non-
fraudulent business activity. By successfully mapping this proportional relationship through fuzzification and
the centroid of area defuzzification, the system proves its capacity to function as a reliable baseline monitor
that avoids generating false alarms during standard operational days, thereby establishing trust in its analytical
capabilities.
Beyond baseline monitoring, the true strength of the system lies in its twenty-seven-rule base, which is specifi-
cally engineered to capture the nuanced, multi-variable patterns of subsidized LPG fraud. Unlike rigid threshold
systems that might only flag a violation if a single metric exceeds a hardcoded limit, the Mamdani inference
engine evaluates the relational dynamics between remaining stock, distribution volume, and purchase orders.
For instance, the rule base is designed to trigger an irregular alert when physical stock is low but recorded
distribution and purchase orders are simultaneously high. This specific linguistic combination effectively iden-
tifies sophisticated fraudulent behaviors, such as inflated distribution records or off-target sales to unauthorized
industries, which are common in the field but easily masked in simple ledger reviews. The ability of the system
to process these dynamic uncertainties using linguistic variables allows it to mimic the intuitive reasoning of an
experienced auditor while maintaining mathematical consistency.
Technologically, the integration of this fuzzy inference engine within a Single Page Application architecture
utilizing Laravel, React.js, and Inertia.js addresses a critical latency issue present in earlier monitoring solutions.
Previous studies focused on basic web-based information systems for LPG stock successfully digitized record-
keeping but failed to provide automated anomaly detection, leaving the analytical burden entirely on the
base manager. Furthermore, traditional manual supervision has repeatedly proven inadequate in preventing
violations like sales above the maximum retail price. By embedding the Mamdani algorithm directly into the
backend logic, the proposed system triggers a comprehensive fraud analysis instantaneously every time a base
officer saves distribution data. This real-time processing paradigm shifts the operational workflow from reactive,
end-of-month auditing to proactive, continuous monitoring, ensuring that irregularities are flagged at the exact
moment of data entry.
The practical implications of this real-time monitoring capability extend significantly toward the broader goal
Page 481

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
of energy subsidy accountability. While continuous auditing and early warning systems have demonstrated
success in public sector procurement, applying these intelligent computational methods to the grassroots level
of subsidized LPG distribution fills a vital gap in current literature and practice. By providing base owners with
an objective, automated dashboard that categorizes daily operations into safe, alert, or irregular statuses, the
system mitigates the subjective biases and delayed recognition inherent in manual oversight. This structured
decision-making support not only empowers local operators to correct operational discrepancies before they
escalate but also provides a scalable technological framework that could assist policymakers in ensuring that
the massive subsidized LPG quota reaches its intended household and micro-enterprise demographics.
Despite these contributions, the study acknowledges several limitations that outline the trajectory for future
research. The current validation was restricted to a single case study at Pangkalan Gas Asmalia, meaning the
generalizability of the rule base and membership functions across bases with different geographical or demo-
graphic characteristics requires further empirical testing. Additionally, the model relies exclusively on three
operational variables, omitting potentially critical indicators such as consumer transaction histories, geographi-
cal distribution anomalies, or historical fraud patterns of specific buyers. Future investigations should focus on
expanding the input variables to capture a more holistic view of the distribution ecosystem, validating the sys-
tem across a diverse network of bases, and benchmarking the Mamdani approach against other computational
intelligence methods, such as Tsukamoto fuzzy logic or advanced machine learning classifiers, to continually
optimize the accuracy and robustness of subsidized energy fraud detection.
4. CONCLUSION
This study successfully designed and built a web-based LPG gas distribution monitoring system for Pangkalan
Gas Asmalia, equipped with a fraud detection engine using the Mamdani Fuzzy Logic method. The system pro-
cesses three input variables, remaining stock, daily distribution volume, and Purchase Order to agent, through
fuzzification, a 27-rule rule base, MIN-MAX inference, and Centroid of Area defuzzification, automatically pro-
ducing Safe, Alert, or Irregular categories in real time each time distribution data is saved. Testing using real
data from Pangkalan Gas Asmalia for May 2026 yielded a crisp output value of 16.20 with a Safe category for a
daily distribution of 18 cylinders against a daily quota of 46 cylinders, consistent with normal field distribution
conditions. The main contribution of this research is the integration of web-based LPG distribution record-
ing and monitoring functions with automatic AI-based fraud detection at the base level, a combination not
previously found in studies on LPG distribution supervision. This system is expected to help base operators
and policymakers detect energy subsidy fraud indications more quickly, in a more structured and objective
manner. This study has limitations in that testing was only performed on one base with three input variables.
Future research is encouraged to validate the system on multiple bases with different characteristics, add ad-
ditional variables relevant to distribution fraud patterns, and compare the performance of the Mamdani Fuzzy
method with other fuzzy approaches or machine learning methods for detecting subsidized LPG distribution
irregularities.
ACKNOWLEDGMENTS
TheauthorsthankR.WisnuPrioPamungkas, S.Kom., M.Kom. forhisguidanceandsupervisionthroughoutthis
research, Pangkalan Gas Asmalia for granting access and data for this research, and Universitas Bhayangkara
Jakarta Raya for facility support throughout the research process.
DECLARATIONS
Author Contributions:
M. Syahrul: Conceptualization, Methodology, Software, Writing – Original Draft.
R. Wisnu Prio Pamungkas: Supervision, Methodology, Writing – Review & Editing.
Fried Sinlae: Manuscript Review, Journal Writing Support, Writing – Review & Editing.
Funding:
The authors received no financial support for the research, authorship, and/or publication of this article.
Conflicts of Interest:
The authors declare no conflict of interest regarding the publication of this paper.
Page 482

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
Data Availability:
The data that support the findings of this study are available from the corresponding author upon reasonable
request.
Additional Information:
No additional information is available for this paper.
REFERENCES
[1] D. J. M. dan Gas Bumi and K. E. dan Sumber Daya Mineral, “Statistik Semester I Minyak dan Gas Bumi,”
2024. [Online]. Available: https://migas.esdm.go.id/cms/uploads/informasi-publik/Stat_tahunan/Statistik-
Migas-Semester-I-2024.pdf
[2] M. R. Taufikurahman, A. Holis, A. J. Mirdad, D. H. Wibowo, and T. Ahmad, “Dampak subsidi BBM dan
LPG 3 kg terhadap kemiskinan nelayan,” 2023.
[3] A. Munandar, “Evaluasi Kebijakan Penyaluran LPG 3 Kg: Efektivitas Subsidi Rumah Tangga Miskin vs
Penggunaan Industri,”J. Ilmu Hukum, Hum. dan Polit., vol. 5, no. 4, 2025, doi: 10.38035/jihhp.v5i4.
[4] S. R. Dewi, Nurlaily, and T. D. Seroja, “Pengawasan pendistribusian gas LPG 3 kg bersubsidi di Kota
Batam,”J. Ilm. Penegakan Hukum, vol. 10, no. 1, pp. 67–78, Jun. 2023, doi: 10.31289/jiph.v10i1.8599.
[5] M. M. Saddami, F. Santoso, and A. Hamdani, “Rancang Bangun Sistem Informasi Stok dan Distribusi
Liquefied Petroleum Gas (LPG) Berbasis Web Pada Pangkalan Mujitahid,”J. TEKNO KOMPAK, vol. 19,
no. 2, pp. 266–278, 2025.
[6] R. W. P. Pamungkas and R. Khalida, “Design and Development of an Early Warning System Through
Continuous Auditing and Continuous Monitoring in Public Sector Procurement,”J. Kecerdasan Buatan
dan Teknol. Inf., vol. 5, no. 2, pp. 2963–6191, 2026, doi: 10.69916/jkbti.v5i2.445.
[7] S. Kusumadewi and H. Purnomo,Aplikasi Logika Fuzzy Untuk Pendukung Keputusan Edisi 2. Yogyakarta:
Graha Ilmu, 2021.
[8] H. Tanaka, “Advanced Fuzzy Clustering for Dynamic Datasets,”IEEE Trans. Fuzzy Syst., vol. 31, no. 6,
pp. 1890–1902, 2023, doi: 10.1109/TFUZZ.2023.3214567.
[9] P. Babu, S. Kumar, and R. Singh, “Customer Segmentation Using Fuzzy Clustering Techniques,”IEEE
Trans. Ind. Informatics, vol. 19, no. 4, pp. 4456–4465, 2024, doi: 10.1109/TII.2024.3456789.
[10] L. Nguyen et al., “Fuzzy Clustering Approach for Consumer Behavior Analysis,”Appl. Soft Comput., vol.
125, p. 109123, 2022, doi: 10.1016/j.asoc.2022.109123.
[11] E. Widodo and S. Santoso, “Clustering-Based Marketing Strategy Using Fuzzy Approach,”Procedia Com-
put. Sci., vol. 216, pp. 350–357, 2023, doi: 10.1016/j.procs.2023.01.045.
[12] A. Yunus, E. N. Wahyudi, and H. C. Kurniawan, “Sistem Peminjaman Barang Menggunakan QR Code
Berbasis Aplikasi Android,”J. Teknol. Dan Sist. Inf. Bisnis, vol. 6, no. 2, pp. 322–328, May 2024, doi:
10.47233/jteksis.v6i2.1350.
[13] Faldi, “Rancang bangun sistem informasi pelayanan administrasi Yayasan Atap Keberagaman Indonesia
berbasis web menggunakan metode RAD,” Universitas Nahdlatul Ulama Indonesia, 2024.
[14] F. Sinlae, E. Irwanda, Z. Maulana, and V. E. Syahputra, “Penggunaan Framework Laravel dalam Mem-
bangun Aplikasi Website Berbasis PHP,”J. Siber Multi Disiplin (JSMD), 2024, doi: 10.38035/jsmd.v2i2.
[15] A.Latifurrahman, Imilda, andA.Salam, “SistemInformasiAkademikmenggunakanPHPdanMySQLpada
Sekolah Tinggi Manajemen Informatika Komputer (STMIK) Indonesia Banda Aceh,”J. Sist. Komput.
(SISKOM), vol. 3, no. 2, pp. 74–83, Aug. 2023, doi: 10.35870/siskom.v3i2.796.
[16] F. Akmal and Nasrul, “Penerapan ReactJS dalam pengembangan front-end aplikasi komunitas Zeromate-
rial,”J. Digit. Bus. and Technol. Innov. (DBESTI), vol. 2, no. 2, pp. 198–205, 2025.
Page 483

M. Syahrul, R. W. P. Pamungkas, & F. SinlaeFraud Detection in Subsidized LPG Gas Distribution at the Base Level...
[17] Nasution and L. Iswari, “Penerapan React JS Pada Pengembangan FrontEnd,”AUTOMATA, vol. 2, no.
2, 2021.
[18] M. F. Aulia and A. Avorizano, “Penerapan Teknologi Single Page Application (SPA) pada Sistem Surat
Disposisi Online (Sudion) di Universitas Muhammadiyah Prof Dr Hamka,” 2022.
[19] D. Prasetya, A. D. R. Putra, W. A. Saksena, and N. Wakhidah, “Penerapan Metode Fuzzy Mamdani dalam
Sistem Pendukung Keputusan untuk Evaluasi Kualitas Game Digital Berbasis Multi-Kriteria,” inSemin.
Nas. Inov. dan Tren Teknol. (SINATTI), 2025.
[20] S. R. Dewi, Nurlaily, and T. D. Seroja, “Pengawasan Pendistribusian Gas LPG 3 Kg Bersubsidi Di Kota
Batam,”J. Ilm. Penegakan Hukum, vol. 10, no. 1, pp. 67–78, May 2023, doi: 10.31289/jiph.v10i1.8599.
Page 484
