---
title: Scalable and Data-Driven Decision Support in the Maintenance, Repair, and Overhaul Process
url: https://arxiv.org/abs/2609.33641
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Houkun Zhu
- Helena Ebel
- Dominik Scheinert
- Florian Schmidt
- Jens Altenkirch
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.33641
pages: 5
chars: 26636
fetched_at: '2026-11-08T13:25:02+00:00'
kb_version: 1
---

# Scalable and Data-Driven Decision Support in the Maintenance, Repair, and Overhaul Process

Scalable and Data-Driven Decision Support in the
Maintenance, Repair, and Overhaul Process
Houkun Zhu 1, Helena Ebel 1, Dominik Scheinert 1, Florian Schmidt 1, Jens Altenkirch 2, and Odej Kao 1
1Technische Universit¨at Berlin, Berlin, Germany
2Siemens Energy Global GmbH & Co. KG, Berlin, Germany
Emails:{h.zhu, firstname.lastname}@tu-berlin.de, jens.altenkirch@siemens-energy.com
Abstract—Several businesses apply maintenance, repair, and
overhaul (MRO) principles to the life-cycle of their existing
products. In cases like casted gas turbine component Product
Lifecycle Management (PLM), repairing components in frequent
intervals can extend the lifetime expectation of the product,
provide higher cost efficiency compared to newly produced
components, and even improve the part design during the
repair cycle. Another aspect of repair concerns sustainability, as
products often contain rare materials. The emissions produced
by the repair process are usually smaller than mining materials
and casting new components.
To optimize the repair process further, we propose the Smart
Expert System (SES), which assists engineering experts with
machine learning-based decision support throughout the repair
process. We elaborate on its IT architecture and present machine
learning models employed for representative MRO use cases. The
SES is evaluated using actual industry data from a leading gas
turbine company and demonstrably fulfills formulated require-
ments concerning the suitability of the overall decision support
and the stability of the enclosing IT architecture.
Keywords—Smart Factory, MRO, Digital Assistance, Machine
Learning, Industry 4.0
I. INTRODUCTION
The fourth industrial revolution, also called Industry 4.0, is
progressing exponentially, integrating horizontal and vertical
manufacturing processes and linking products to improve
industry performance and sustainability [1], [2]. Many com-
panies start with maintenance management in the Industry 4.0
practice because the transition from responsive and periodic
maintenance to predictive and proactive maintenance is critical
for companies to obtain technical and economical benefits [3].
Maintenance management is often referred to as Maintenance,
Repair, and Overhaul (MRO) to describe the diverse cost-
effective practice better. The MRO process is typically used
in the context of gas turbine refurbishment to minimize life
cycle costs and optimize the performance of the part.
Availability and efficiency of gas turbine units are two
main concerns for gas turbine operators regarding performance
optimization [4], [5]. Many components have limited life ex-
pectations compared to the gas turbine unit’s operational life-
time [5]. Consequently, maintenance and repair have always
been in the interest of operators. The traditional procedure is
usually executed by static repair process chains in which the
same value-added steps are carried out continuously.
However, the manual and static procedure is often ineffi-
cient. Typically, engineers refer to the Repair Specification
Manual (RSM) to locate the corresponding repair actions
or follow-up investigation process for an observed material
defect. This procedure is monotonous, error-prone, and breaks
the real-time capacity principle of documentation management
in Industry 4.0 [6] due to manual search through the RSM
documentation and infrequent RSM updates.
Additionally, component-specific knowledge—how to solve
novel issues and execute unique or complex repair patterns—
is built up continuously by individual engineering experts. In
order to ensure a standardized and high-quality knowledge
base, this knowledge needs to be documented and made
available to all experts by the RSM.
To address the aforementioned challenges, a data-driven
approach is effective because it can help automate the gas
turbine repair process and boost efficiency in extracting and
integrating new engineering expertise from unseen repair-
ing operations data. Therefore, we introduce a scalable and
data-driven assistant, Smart Expert System (SES), to support
decision-making in the MRO process. Specifically, SES is
applied in the following use cases we identified: (1) Automa-
tion of the repair decision process through digitalization and
rule-based application of RSMs (Digital RSM), (2) Inference
of dispositions for defects not defined in RSMs through
data-driven modeling of historical expert decisions (Quality
Inspection), (3) Estimation of the repair cost and overall
feasibility of repair actions (Repair Scope).
In this paper, we make the following contributions:
1) We provide a machine learning-based decision support
solution for the MRO process.
2) Our architecture can effectively handle varying demands
through fine-granular system component scaling.
3) Empirical results show that our solution can achieve high
performance for repair operation predictions and effec-
tively and reliably handle varying loads on the system
via horizontal scaling.
The rest of this paper is organized as follows. Section II
describes the problem statement and requirements for a digital
assistant system. Section III presents the general architecture
design as well as solutions to each use case. Section IV
evaluates the prediction accuracy of machine learning (ML)
models in SES and scalability of SES. Section V introduces
arXiv:2609.33641v1  [cs.AI]  27 Sep 2026

other intelligent assistant systems for Industry 4.0. In the
end, Section VI concludes the paper and outlines future work.
II. PROBLEMSTATEMENT
We first present the conventional MRO process and its as-
sociated manual decision-making steps. From this description,
we then derive the concrete problems to be solved by SES
and formulate further key requirements to be considered by
the envisioned system.
A. Conventional Engineering Process
MRO Process
Repair
Process
Inspection
Process
Smart Expert System
RSM
Decision
Process
Quality
Inspection
Process
Repair
Scope
Process
RSM Revision Process
Fig. 1. MRO process and the corresponding use cases for the SES.
The conventional MRO process (see Figure 1) typically
starts with the handover of a used machine component (e.g.,
a gas turbine blade) by a customer. The given component
is inspected using different methods to detect all sorts of
damages. Generally, the first step concentrates on an inspec-
tion phase, where all damages are documented to check the
product’s surface and material consistency by various tests,
e.g., 3D scans. Based on the inspection results and decision
rules defined in the RSM, an engineering expert decides on
the severity of damage and possible repair options, including
keeping or scraping the component.
As RSMs often focus on standardized damage patterns,
rare defect types and complex defect patterns can be missed.
Therefore, such defects require further inspection to determine
a concrete repair process, i.e., a Quality Inspection (QI)
process is started. Engineering experts manually inspect the
component within the QI process and decide on a repair
process based on their own experiences and expertise.
In order to learn and generalize from the cases handled
via the QI process, the associated final repair decisions are
documented within a Product Lifecycle Management (PLM)
software. Based on this knowledge, the engineering experts
periodically adapt RSMs to keep the decision process docu-
mented. This standardization process usually occurs in longer
intervals, commonly one or two years.
The outlined conventional engineering process bears poten-
tial for automation in various places, e.g., rule-based applica-
tion of digital RSMs or inference of repair process decisions
based on historical data. Hence, a digital assistant system is
demanded.
B. Requirements for an Assistant System
In order to design and develop a valuable assistant system,
we interviewed practitioners and collected user stories from the
roles involved in the MRO Process. The gathered user stories
indicate four core requirements for an assistant system.
(i) The system provides suggestions instead of automated
decisions. The main focus here is on using AI to assist the
decision-making process. Engineers want to revise system
results before passing on in the process. On the other hand,
the system should support the incorporation of engineers’
feedback on the prediction results to improve ML models.
(ii) The system has access to all decision-relevant data
points and extensively incorporates them to assist in the
MRO process. The system should be based on the MRO
process’s existing information and expert knowledge. For the
training of ML models, it is necessary to process data, confirm
intermediate results from experts, and create final results in a
form that can be further applied in the MRO process and to
link expert knowledge with the data sources.
(iii) ML models can adapt to new conditions. Constantly
emerging unseen conditions disqualify a static model. For
example, it is conceivable that rare and previously unknown
defect types arise or the data input changes due to techno-
logical advances, as a consequence exceeding defined limits.
In order to continuously adapt to new conditions, the system
should regularly retrain its models.
(iv) The reasoning behind system results is human-
understandable. To increase the acceptance of ML models, the
system should provide engineers with sufficient explanations,
e.g., regarding the decision-making process and the confidence
of a particular model about generated predictions.
III. ANALYSISPIPELINES
This section describes the design and analysis pipeline of
SES, which takes the problem statement described in Section II
into account.
A. Architecture Design
Distribution Layer
Transportation Layer
Prediction Layer
Ingestion Layer
Storage Layer
MLOps Layer
Request Response
Fig. 2. The architecture of SES. The layers can be categorized with respect to
1) request handling and 2) modeling, with the transportation layer in between.
The SES attempts to support engineers in various phases
of the engineering process via intelligent and data-driven
suggestions. Consequently, for its realization, we choose a
distributed system, i.e., loosely coupled system components

interacting with each other, which allows for scalability and
maintenance of individual components. As shown in Figure 2,
our architecture can be decomposed into six application layers:
1) Ingestion Layer: The SES utilizes Restful APIs so that
other systems can effortlessly integrate with the SES
and provide data related to the engineering process. If
required, the received data is further processed before
being sent to the transportation layer.
2) Transportation Layer: In order to facilitate communica-
tion among individual components and allow for asyn-
chronous request handling and data processing, we em-
ploy a scalable message broker 1. This distributed mid-
dleware component enables the publication and retrieval
of data from message queues. To ensure a high level
of performance, all data should be routed through this
platform as it decouples components where slow sinks
are regularly a limiting factor.
3) Prediction Layer: The various prediction services are
organized in this layer. They consume data from message
queues of interest, enrich it with respective predictions,
and publish the transformed data again to suitable mes-
sage queues.
4) Persistence Layer: In order to retrain models when needed
and keep track of provided user feedback, we persist re-
quests, predictions, and potential correction of predictions
reported by users.
5) MLOps Layer: All ML operations are encapsulated by
this layer. This encompasses the training, updating, ver-
sioning, and serving of models.
6) Distribution Layer: Once a user request has been pro-
cessed and enriched by a model covering the respective
use case, the transformed data is either 1) ready for
retrieval by the initially requesting service, or 2) directly
send there.
The individual system components of this architecture are
realized as containerized applications. This allows for individ-
ual scaling of system components and thus efficiently adapting
the SES to different demands, e.g. adapting to increased user
requests or extending further ML models. Using a container
orchestration system such as Kubernetes 2, the deployment and
management of our distributed system are further simplified.
B. Use Cases
To boost the conventional engineering process detailed
in Subsection II-A, we identify and provide solutions for the
following use cases:
1) Digital Repair Specification Manual:The SES digitizes
RSM to automate the defect evaluation and repair process.
Specifically, the SES converts the existing RSM to a machine-
readable form. Therefore, once the defect measurement data
is available, engineers do not need to refer to the RSM,
but acquire the appropriate repair operation recommendation
directly.
1https://www.rabbitmq.com/, Accessed: May 2022
2https://kubernetes.io/, Accessed: May 2022
2) Quality Inspection:In some cases, the defect situation
is not defined in RSM. Engineering experts then need to
investigate those defects and make repair decisions case by
case. The expertise is generalized every one to two years and
then integrated into the RSM. In order to boost the QI process,
we employ ML to generalize previous experts’ decisions and
automate the QI. Specifically, we choose decision tree models
to learn the insights because they foster model explainability
and thus enable trust in model predictions.
3) Repair Scope:Repair scope condenses information
about all required repair operations assigned to a single part.
It defines the severity level of defects and the complexity
level of associated repair operations. It is used to calculate
the repair cost and decide whether a component is worthwhile
to repair. This is oftentimes rule-based but varies nonetheless,
for instance across repair shop floors (technical equipment)
or customers (financial budget and expectations). Therefore,
our system digitizes the repair scope logic per shop floor and
customer to automate this process.
C. Fulfillment of Requirements
Our proposed realization of the SES takes into consideration
the requirements defined in Subsection II-B.
With regards to requirement (i), the predictions produced by
the SES can be visualized in a user interface and thus leave the
final decision to the engineer in charge. In case of unsuitable
recommendations, an engineer can apply a correction, which
in turn is sent to the SES using dedicated endpoints and used
for fine-tuning the internally utilized machine learning models.
The second requirement (ii) is demanding data completeness
and data interpretability. On the one hand, the SES is making
use of existing documents such as the RSM for rule-based
predictions, thereby making use of available expert knowledge.
On the other hand, the general problem modeling and close
development of the SES together with engineers in the field
assured that 1) the process is sufficiently incorporated and
reflected, and 2) the utilized modeling techniques comply with
the requirements of engineers regarding interpretability.
Quickly adapting ML models are required following re-
quirement (iii), and with our use of decision trees, the SES
can adapt to new conditions through periodic retraining from
scratch and fine-tuning of a warm-started model.
After the previous discussions, the last requirement (iv)
regarding human-understandable results is considered fulfilled
as well by the design of the ML model. In this context, it
is advisable to enrich an incoming request not only with the
respective model prediction, but also with an indication of the
certainty of the prediction produced.
Besides the general fulfillment of requirements by design
choices, we next look into the quantitative analysis of SES.
IV. EVALUATION
In this section, we demonstrate experiment results of SES
performance. Both the prediction performance and end-to-end
latency are evaluated.

A. Prediction Performance
To predict the disposition of a defect component in QI,
we employ the decision tree model to provide a transparent
and explainable model. There are three types of disposition
decisions, (1) Use as is: the component is good enough
and demands no repair. (2) Rework: the additional repair
operations need to be conducted. (3) Scrap: the component is
beyond repair or worthless to repair. As depicted in Figure 3,
the training data is imbalanced, where half of the data are use
as is.
Rework
21.9%
Scrap
28.8%
Use as is
49.3%
Fig. 3. Imbalanced distribution in Quality Inspection training data.
It is critical to predict gas turbine component disposition
conservatively in the industry because if the prediction is
more optimistic than reality, it may bring potential risk to
consumers’ products, e.g., complete damage to a gas turbine.
Therefore, it is more favorable to dispose components cau-
tiously.
In order to handle skewed disposition distribution and
conservative prediction, SES considers conservative preference
ranks while making a decision, i.e., SES tends to make a
more serious disposition prediction (overestimation) when the
probability of that disposition is above a certain threshold. For
example, if the threshold is 30%, and the model outputs the
probability of 40% use as is, 22% rework and 38% scrap,
conservative prediction will then select scrap as the prediction
result because it ranks first and is greater than 30%.
Proper evaluation metrics are essential to handle imbalanced
data. SES uses F1 score to evaluate the prediction as it
combines both recall and precision score. Furthermore, to
quantify the cautiousness of our prediction, we define another
metric, underestimation ratio, as,
# of underestimated prediction
total predictions .
Underestimation is to predict use as is or rework for scrap, or
to predict use as is for rework.
The evaluation data is based on real industry data from a
leading gas turbine company, and the empirical results show
a decrease of the underestimation ratio from 8.0% to 5.0% at
the cost of 0.5% drop in F1 score by utilizing the conservative
prediction, i.e., SES can achieve 88.5% F1 score with a 5.0%
underestimation ratio.
B. End-to-End Latency
We evaluate the end-to-end latency of SES in two set-
tings. Firstly, all components in SES are running with two
instances. Different pressure levels of requests are sent to
simulate various loads. Secondly, we run 50 request threads
and test the latency under a different number of scale-out,
i.e., all components in our architecture are deployed with the
same number of instances except the message broker. In both
experiments, we measure the latency of requests in the first 60
seconds and run each setting 5 times. The experiments assess
the processing speed and scalability of SES.
1) Same Scale-out Under Different Loads:In this experi-
ment, we measure the latency of SES under different loads,
i.e., we use a different number of request threads to simulate
various loads. As presented in Figure 4, the latency rises
significantly after increasing the pressure, i.e., latency surges
from around 20 seconds to almost 80 seconds when we grow
the number of request threads from 10 to 200.
0 25 50 75 100 125 150 175 200
Number of Threads
0
10
20
30
40
50
60
70
80Latency (second)
Use Case
Digital RSM
Quality Inspection
Repair Scope
Fig. 4. Latency under pressure test with the same scale-out (# of instance is
2). The bigger the number of threads is, the greater load we generate.
2 3 4 5 6 7 8 9
Number of Instances
0
10
20
30
40
50
60
70Latency (second)
Use Case
Digital RSM
Quality Inspection
Repair Scope
Fig. 5. Scale out test under same load (# of threads is 50). The higher number
of instance we scale out, the lower latency we get.

2) Different Scale-out Under Same Loads:In this experi-
ment, we measure the latency of SES under a different number
of scale-out, i.e., we use different numbers of SES instances.
As illustrated in Figure 5, scaling out of SES can noticeably
decrease the latency.
Both experiments showed that the SES can effectively adapt
to a surge in demand by scaling to ensure process efficiency.
V. RELATEDWORK
This section presents related work from the general field of
intelligent assistance solutions for Industry 4.0.
There exist related work for envisioned holistic solutions for
intelligent, digital assistants. For instance, it is motivated in [7]
that process-related assistance systems could be used both lo-
cally and globally, with the global assistance system evaluating
individual results and thus having a central overview, whereas
the local assistants are specialized on concrete machines or
production processes. An agent-based manufacturing system
is proposed in [8], with a cloud-assisted self-organized archi-
tecture designed for smart agents in the field, which makes it
feasible for industry 4.0 and its typical edge environments.
In order to increase the acceptance and lifespan of to-be-
employed digital assistance, it is also important to follow a
systematic approach to reconfiguration of such systems, which
has been proposed in [9] and attempts to act as a concept for
various common challenges.
Notably, a majority of works focuses on the usage of
Augmented Reality (AR) to support various engineering
tasks [10]. One example is Sophos-MS [11], a human-centered
and modular solution which relies on AR contents and on
a personal digital assistant with vocal interaction support.
Another example is presented in [12], an AR inspection
tool that allows detection of discrepancies on 3D models
and subsequent annotation of those, effectively improving
problem identification and digital documentation. Similarly, a
methodology is proposed in [6] for the conversion of analog
documentation manuals and for the authoring of new AR-
based manuals in accordance with Industry 4.0 principles.
On a meta-level, the authors of [13] generally review the
state of the art for AR in industry, and work out architecture
considerations and user experience recommendations based on
use cases provided by cooperating Industry 4.0 companies.
More recently, researchers started to review existing ap-
proaches in this field to derive general recommendations and
reveal current limitations. For instance, a systematic literature
review of worker assistance systems in production has been
conducted by the authors in [14], aiming at classification of
existing systems, discussion of the associated user groups and
their individual requirements, as well as motivation of future
research directions. Similarly, the general benefits of using dig-
ital assistance systems in manufacturing are discussed in [15],
thereby among other things touching upon considerations of
accessibility, speed, customization, and interaction capabilities.
Evidently, the aforementioned works mainly attempt to
reinvent the interaction process of various manufacturing tasks,
consequently demanding for a holistic approach. With the SES
solution and architecture proposed in this paper, we focus more
on supporting engineers in the decision-making process in a
data-driven manner through interactive suggestion of options.
VI. CONCLUSION
In this paper, we presented SES, a scalable and data-driven
system to assist gas turbine repairing process. It automates
the conventional engineering process in MRO. Furthermore,
it assists engineering experts with ML-based decision support
in defects undefined in the RSM. Lastly, SES can effectively
adapt to different demand and meet latency requirements due
to its scalable architecture. In our experiments, we evaluated
the performance of SES. Empirical results showed that SES
can achieve 88.5% F1 score and 5.0% under-estimation ratio.
Additionally, the SES is able to mitigate and even prevent
latencies from increasing by scaling out.
In the future, we want to evaluate and strengthen the
transferability of our model on different repair objects.
ACKNOWLEDGMENT
This work has been supported through grants by the German
Federal Ministry of Education and Research (BMBF) as MRO
2.0 which is co-financed by the European Regional Develop-
ment Fund (ERDF).
REFERENCES
[1] L. S. Dalenogare, G. B. Benitez, N. F. Ayala, and A. G. Frank,
“The expected contribution of industry 4.0 technologies for industrial
performance,”International Journal of production economics, 2018.
[2] M. Ghobakhloo, “Industry 4.0, digitization, and opportunities for sus-
tainability,”Journal of cleaner production, 2020.
[3] A. Mosyurchak, V . Veselkov, A. Turygin, and M. Hammer, “Prognosis of
behaviour of machine tool spindles, their diagnostics and maintenance,”
MM Science Journal, 2017.
[4] R. Anton, B. Heinecke, M. Ott, and R. Wilkenhoener, “Repair of
advanced gas turbine blades,” inTurbo Expo: Power for Land, Sea,
and Air, 2007.
[5] K. Pallos, “Gas turbine repair technology,”Atlanta, GA, USA, GE Energy
Services Technology, GE Power Systems, 2001.
[6] M. Gattullo, G. W. Scurati, M. Fiorentino, A. E. Uva, F. Ferrise, and
M. Bordegoni, “Towards augmented reality manuals for industry 4.0: A
methodology,”Robotics and Computer-Integrated Manufacturing, 2019.
[7] B. Barig and K. Balzereit, “Assistance systems for industry 4.0 environ-
ments,” in17th embedded world Conference, 2019.
[8] H. Tang, D. Li, S. Wang, and Z. Dong, “CASOA: an architecture for
agent-based manufacturing system in the context of industry 4.0,”IEEE,
2018.
[9] G. Reisinger, T. Komenda, P. Hold, and W. Sihn, “A concept towards
automated data-driven reconfiguration of digital assistance systems,”
Procedia Manufacturing, vol. 23, pp. 99–104, 2018.
[10] A. Gallala, B. Hichri, and P. Plapper, “Survey: The evolution of the
usage of augmented reality in industry 4.0,”IOP Conference Series:
Materials Science and Engineering, 2019.
[11] F. Longo, L. Nicoletti, and A. Padovano, “Smart operators in industry
4.0: A human-centered approach to enhance operators’ capabilities and
competencies within the new smart factory context,”Computers &
industrial engineering, 2017.
[12] E. Marino, L. Barbieri, B. Colacino, A. K. Fleri, and F. Bruno, “An
augmented reality inspection tool to support workers in industry 4.0
environments,”Computers in Industry, 2021.
[13] A. Jakl, L. Sch ¨offer, M. Husinsky, and M. Wagner, “Augmented reality
for industry 4.0: Architecture and user experience,” inFMT, 2018.
[14] B. G. Mark, E. Rauch, and D. T. Matt, “Worker assistance systems in
manufacturing: A review of the state of the art and future directions,”
Journal of Manufacturing Systems, 2021.
[15] S. Wellsandt, K. Hribernik, and K. Thoben, “Anatomy of a digital
assistant,” inAPMS. Springer, 2021.
