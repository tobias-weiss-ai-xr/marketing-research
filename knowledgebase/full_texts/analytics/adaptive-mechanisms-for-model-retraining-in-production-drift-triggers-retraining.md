---
title: 'Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
  and Reduced Data Preparation Time through Automated Orchestration'
url: https://doi.org/10.70315/uloap.ulirs.2026.0301013
category: analytics
subcategory: measurement
date: 2026-02
venue: Universal Library of Innovative Research and Studies
authors:
- Andrei Shcherbinin
source: openalex-oa
pdf_url: https://doi.org/10.70315/uloap.ulirs.2026.0301013
pages: 7
chars: 29658
fetched_at: '2026-11-08T17:01:16+00:00'
kb_version: 1
---

# Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation, and Reduced Data Preparation Time through Automated Orchestration

Page | 94www.ulopenaccess.com
ISSN: 3065-0003 | Volume 3, Issue 1
Open Access | PP: 94-100
DOI: https://doi.org/10.70315/uloap.ulirs.2026.0301013
Universal Library of Innovative Research and Studies Research Article
Adaptive Mechanisms for Model Retraining in Production: Drift
Triggers, Retraining Prioritisation, and Reduced Data Preparation
Time through Automated Orchestration
Andrei Shcherbinin
Social Discovery Group, Team Lead ML Engineer, Tbilisi, Georgia.
Citation: Andrei Shcherbinin, “ Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining
Prioritisation, and Reduced Data Preparation Time through Automated Orchestration” , Universal Library of Innovative
Research and Studies, 2026; 3(1): 94-100. DOI: https://doi.org/10.70315/uloap.ulirs.2026.0301013.
This work provides an analytical and theoretical–practical justification for the effectiveness of deploying adaptive retraining
mechanisms for machine learning models in unstable industrial environments that evolve dynamically over time. The
relevance of the study is driven both by the sharp increase in investment in artificial intelligence in 2025 and by the objective
need to curb losses in model accuracy caused by concept drift and input data drift. The study adopts a comprehensive
methodological approach that combines a systematic review of scientific publications, a comparative analysis of drift-
detection algorithms, and a case study component. The results indicate that introducing automated process orchestration
using Apache Airflow, together with monitoring systems that provide full model coverage, reduces incident detection
time by 60% and lowers the labour intensity of data preparation for subsequent retraining by 40%. An original hybrid
lifecycle governance model for ML systems is proposed, combining statistical activation mechanisms with business-oriented
principles to prioritise computational resources. The conclusions empirically support the hypothesis that a meaningful
increase in model accuracy—up to 11% in marketing attribution tasks—can be achieved while simultaneously reducing
operating costs. The study’s materials carry both practical and scientific value for machine learning practitioners, data
architects, and digital unit leaders responsible for scaling and ensuring the resilient operation of AI solutions in production
environments.
Keywords: Machine Learning, MLOps, Concept Drift, Retraining Automation, Data Orchestration, Model Degradation,
Real-Time Monitoring, Apache Airflow, Retraining Prioritisation, Operational Efficiency.
Abstract
IntroductIon
In 2025, the artificial intelligence domain is characterised
by a transition toward deep operationalisation, where
emphasis shifts from creating experimental prototypes to
ensuring stable model performance in high-load industrial
settings. Current analytical estimates suggest that the global
AI market in 2025 reaches USD 254.5 billion, with a projected
compound annual growth rate of 36.89% through 2031 [1].
At the same time, corporate digital budgets have expanded
markedly: according to Deloitte, in 2025, spending on digital
initiatives amounted to 13.7% of total company revenue,
whereas a year earlier this figure did not exceed 7.5% [2].
Large-scale adoption of ML systems in production processes
has exposed a systemic issue associated with the accelerated
loss of predictive effectiveness under data non-stationarity.
A central challenge for contemporary MLOps practice is
the phenomenon of concept drift and data drift. In dynamic
domains such as e-commerce, financial markets, and Internet
of Things (IoT) ecosystems, the distributions of input features
and the dependencies among them are subject to continuous
evolution [3]. Traditional model maintenance strategies
based on predefined retraining intervals are limited in
applicability: in some cases, they lead to unjustified increases
in computational costs when no meaningful changes occur;
in others, they fail to respond in time to abrupt behavioural
shifts or technological anomalies [4].
A substantial scientific gap in current research is the absence
of end-to-end frameworks that unify statistical methods for
identifying model degradation with automated orchestration
of data preparation processes and mechanisms that account
for business priorities. Most existing work concentrates
either on the algorithmic aspects of drift detection or on
infrastructure solutions at the DevOps level, while the
economic consequences of model “ageing” and its impact
on return on investment (ROI) are often left outside the
analytical scope [5].
Within the present study, the objective is defined as the

Page | 95Universal Library of Innovative Research and Studies
Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
and Reduced Data Preparation Time through Automated Orchestration
development of an adaptive model retraining loop designed
to reduce update time lags and to rationalise the use of
computational resources.
The scientific novelty  lies in substantiating a hybrid
lifecycle management model for ML systems in which end-
to-end monitoring based on AWS Athena and Grafana is
integrated with dynamic orchestration of computational
pipelines in Apache Airflow, producing a synergistic effect
between model accuracy and operational efficiency.
The working hypothesis  is that applying monitoring
solutions with full model coverage, combined with automated
ETL processes (MSSQL → Airflow → Kafka → Athena), makes
it possible to reduce degradation detection time by 60%,
decrease data latency by 35%, and deliver up to an 11% gain
in the accuracy of business-critical models through timely
adaptive retraining.
MaterIals and Methods
To achieve the stated objective, a multi-level methodological
design was employed, combining theoretical and empirical
research methods. A systematic literature review served
as the primary instrument for establishing the theoretical
foundation; relevant scientific publications indexed in Scopus,
Web of Science, IEEE Xplore, and the ACM Digital Library
were analysed. Source selection was performed based on
thematic relevance to MLOps, concept drift mechanisms, and
data orchestration processes in cloud infrastructures.
The empirical component relies on a case-study method
grounded in professional practice. The case demonstrates the
implementation of a comprehensive end-to-end monitoring
system with full model coverage and the automation of Apache
Airflow pipelines in a high-load production environment.
The source base of the study is represented predominantly by
academic publications and conference materials addressing
adaptive management topics, algorithms for detecting data
and concept drift (ADWIN, DDM), as well as Lambda and
Kappa architectural approaches to processing streaming
and batch data [3]. The remaining sources include analytical
reports by leading consulting organisations, including
Deloitte (2025), McKinsey (2024), and Gartner (2025),
used to interpret market trends and evaluate the economic
effectiveness of automation from an ROI perspective [2].
The analytical methodology was based on a comparative
analysis of existing model retraining strategies, including
scheduled, trigger-based, and incremental approaches, as
well as a content analysis of technical documentation for
modern MLOps platforms such as Kubeflow, MLflow, and
AWS SageMaker. In evaluating effectiveness, particular
attention was given to model quality metrics, including
ROC AUC, Precision, and Recall; to operational resilience
indicators expressed via Mean-Time-to-Recovery; and to the
resource intensity of retraining processes under industrial
operating conditions.
results and dIscussIon
Model degradation in production environments is driven
by a breakdown of the core statistical learning assumption
that data-generating distributions remain stationary. In real-
world information systems, the joint distribution of input
features and the target variable is subject to change; such
change may emerge through covariate shift, a transformation
of class prior probabilities, or a modification of the mapping
concept that links features to the target space [10]. These
processes reduce models’ generalisation capacity, making it
necessary to formalise mechanisms for timely adaptation.
The analysis identified four fundamentally distinct
types of concept drift, each implying a specific response
strategy. Sudden drift is characterised by abrupt, stepwise
distributional changes—for example, after sensor hardware
upgrades or a revision of marketing strategy—and it
requires immediate retraining on up-to-date data. Gradual
drift manifests as a slow replacement of an outdated concept
with a new one, where sliding-window methods serve as an
effective adaptation tool. Incremental drift reflects a smooth,
long-term evolution of data without clearly expressed
rupture points, which implies continuous updating of model
parameters. Recurring drift is associated with seasonal or
cyclic patterns, in which previously trained models may
again become highly relevant and can be reactivated without
full retraining [6, 22].
For effective detection of these drift types within an industrial
MLOps architecture, a two-level thresholding system
appears justified, consisting of warning and confirmed drift
states. Implementing such a mechanism through automated
monitoring makes it possible to balance sensitivity to change
against robustness to false alarms, thereby forming a practical
foundation for adaptive lifecycle management of models.
Within Table 1, the results of a comparative analysis of retraining
strategies in dynamic environments are presented.
Table 1. Comparative analysis of retraining strategies in dynamic environments (compiled by the author based on [4, 7, 21])
Strategy Trigger Economic efficiency Risks Recommended stack
Scheduled Calendar interval Low (excess costs) Missing drift between cycles Airflow, Cron
Active (trigger-
based) (Author’s)
Drift/accuracy metrics High (optimal resource
use)
False trigger activations AWS Athena, Grafana
Online
(incremental)
Each new data point/
batch
Medium (high latency) Catastrophic forgetting Kafka, Spark Streaming
Hybrid Drift + business priority Maximum (ROI-oriented) High integration complexity Airflow, SageMaker, Cara

Page | 96Universal Library of Innovative Research and Studies
Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
and Reduced Data Preparation Time through Automated Orchestration
Reducing time costs associated with data preparation is
treated as one of the key factors for increasing the operational
efficiency of ML systems. In traditional architectures, ETL
processes often become a critical—and the most vulnerable—
bottleneck, creating substantial latency between  the moment
concept drift is detected and the point at which the model
is actually ready to be updated. Such delays directly affect
Time-to-Market and reduce the practical value even of
correctly detected changes. The use of automated pipelines
based on Apache Airflow enables a transition to a paradigm
that may be described as “self-healing” data, in which failures
and shifts in upstream sources are handled without manual
intervention.
Empirical results obtained through the author’s professional
practice indicate that automating end-to-end data processing
routes (MSSQL → Airflow → Kafka → Athena) reduces the
volume of manual operations by up to 80%. This effect is
achieved by introducing automated dataset versioning,
standardising transformations, and tightly integrating
with a Feature Store, which substantially lowers the risk
of feature misalignment between training and production
environments. An additional result is a 35% reduction in
data latency, creating conditions for training models on the
most current samples available. This property becomes
critical in domains with high sensitivity to delay, including
fraud detection tasks and high-frequency trading strategies.
The effectiveness of adopting the described MLOps practices
correlates with broader industry trends in which automation
and orchestration tools are becoming key drivers of market
growth and of the shift in focus from experimental analytics
to the industrial operation of models (see Fig. 1).
Fig. 1. Forecast of the MLOps solutions market volume (compiled by the author based on [12]).
Empirical confirmation of the stated hypothesis is provided
by the outcomes of implementing the proposed approaches
in a production loop. Within the executed project, an end-
to-end monitoring system was established that covered
100% of deployed machine learning models, ensuring full
observability of their state across all operational stages. This
approach materially transformed ML system maintenance
practices, shifting the emphasis from fragmented incident
response toward proactive lifecycle governance of models.
Continuous control of key quality and stability metrics
enabled early detection of degradation signals, which in turn
created the conditions for timely and economically justified
activation of adaptive retraining mechanisms.
Table 2 presents a description of the performance metrics
associated with implementing adaptive monitoring and
orchestration.
Table 2. Performance metrics for the implementation of adaptive monitoring and orchestration (compiled from the author’s
data)
Parameter Before implementation After automation Improvement / Effect
Incident detection time Not standardized Reduced by 60% Minimisation of business losses
Data preparation time for retraining Manual ETL pipeline Reduced by 40% Faster update cycle
Data latency in the loop High (batch) Reduced by 35% Higher relevance of predictions
Manual operations in Airflow High share of manual labour Reduced by 80% Lower operational risk
Marketing attribution accuracy Standard models +11% accuracy uplift Advertising budget optimisation
Attribution computation time 6 hours 30 minutes 12× acceleration (12x)

Page | 97Universal Library of Innovative Research and Studies
Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
and Reduced Data Preparation Time through Automated Orchestration
A separate line of analysis is warranted for implementing a
customer support chatbot based on an intent-detection model
comprising 35 semantic classes. During industrial operation,
the model demonstrated strong quality indicators, reaching
ROC AUC = 0.978 and Precision = 0.960. The achieved
accuracy level is directly associated with the functioning of
the adaptive retraining loop, which enables new types of user
requests to be incorporated into the training set promptly,
without compromising the stability of the production
environment. The capacity to update the model quickly on
relevant data made it possible to preserve high generalisation
performance even as user behaviour and the lexical
composition of inquiries shifted over time. A substantial
practical effect of the deployment was the automation of up
to 95% of dialogues without operator involvement, achieved
through resilient process orchestration and continuous
model validation in an automated mode [11, 15].
For the practical implementation of the described approach,
an architectural interaction scheme was developed for
the key components of the MLOps system that form the
adaptive retraining loop. This architecture reflects the
linkage between the monitoring, orchestration, data storage,
and model training subsystems, as visualised in Figure 2,
and demonstrates the logical sequence from degradation
detection to automated model updating within an industrial
production setting.
Fig. 2. Author’s architecture scheme for adaptive retraining with automated orchestration (compiled from the author’s data).
A central element of the proposed architecture is the
Validation Gate node, where the newly trained Challenger
model is compared against the current production Champion
version. Implementing this mechanism makes it possible
to prevent the rollout of models that, despite being trained
on up-to-date data, exhibit degraded generalisation due to
noise effects or overfitting. Comparative validation against
a predefined set of metrics adds a protection layer for the
production loop and supports the preservation of stable
quality under continuous cycles of adaptive updating.
A task of particular importance within adaptive lifecycle
governance is the economically grounded determination of
whenretraining should be initiated. This aspect is formalised
through the CARA algorithm (Cost-Aware Retraining
Algorithm), under which the decision to trigger retraining
is based on optimising a loss function that aggregates
both model error indicators and the cost of consumed
computational resources, including GPU and TPU capacity
[5]. In AWS and GCP cloud infrastructures, which follow
a pay-as-you-go pricing model, uncontrolled or excessive
retraining can produce substantial financial losses without a
commensurate gain in quality.
Synthesising established theoretical and practical approaches
to retraining governance made it possible to formulate a
retraining prioritisation model aimed at balancing accuracy,
operational risk, and economic efficiency. This model,
visualised in Figure 3, reflects the decision logic for launching
adaptive model updates as a function of degradation severity,
the business criticality of the task, and the current cost of
computational resources.

Page | 98Universal Library of Innovative Research and Studies
Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
and Reduced Data Preparation Time through Automated Orchestration
Fig. 3. Author’s algorithm for prioritising retraining processes (compiled from the author’s data).
Implementing the described logic creates the prerequisites
for rational governance of computational resources, making
it possible to concentrate the greatest capacity on those
models whose contribution to achieving key performance
indicators and the organisation’s strategic objectives is
maximal. In practical terms, this alignment ties technical
choices to business metrics and reduces the likelihood of
misallocated spend in scalable ML infrastructures.
At the same time, despite the current level of technological
maturity, the deployment of adaptive retraining systems
is accompanied by a set of substantive limitations and
risks. One systemic barrier is technological fragmentation,
expressed as the absence of end-to-end integration between
the tooling used by data engineers, including streaming
platforms such as Kafka and specialised MLOps solutions
such as Kubeflow. Such infrastructural discontinuity leads
to the accumulation of so-called “automation debt,” reducing
process transparency and complicating ongoing support and
evolution [8, 18].
An additional threat is the risk of cascading error
propagation, in which defects or anomalies in upstream data
are automatically transferred into the training process and,
consequently, into deployed models. Under a high degree of
automation, such errors can scale substantially faster than
in manual workflows, which makes it necessary to introduce
strict data quality validation procedures at the stages that
precede training [14]. A further constraining factor is the
talent gap: McKinsey’s analytical assessments indicate that
in 2025 a shortage of roughly 40% persists for specialists
with competencies in designing complex agent-based
architectures and adaptive retraining loops [20].
Issues of ethical and regulatory compliance require separate
consideration. In domains with heightened requirements for
transparency and responsible decision-making, including
healthcare and the financial sector, automatic model
updates without human participation can conflict with
interpretability and explainability principles formalised
within the Explainable AI concept [13]. These constraints
call for a measured approach to automation, in which
adaptive mechanisms are complemented by elements of
human oversight. Hybrid schemes that incorporate a human-
in-the-loop decision layer for the most critical scenarios are
viewed as an effective instrument for reducing operational,
regulatory, and reputational risks [6, 16].
Table 3 below provides an assessment of how automation
factors influence the total cost of ownership (TCO).
Table 3. Assessment of the impact of automation factors on TCO (compiled by the author based on [6, 16, 17]).
Cost component Manual mode Automated (adaptive) mode Long-term effect
Engineering resources High (continuous support) Medium (one-time investments) 50% reduction after 12 months
Cloud compute Predictable Volatile (drift-dependent) 30% efficiency gain
Cost of errors Critical (prolonged downtime) Minimal (auto-recovery) 60% risk reduction
Infrastructure Low complexity High complexity Requires an MLOps platform

Page | 99Universal Library of Innovative Research and Studies
Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
and Reduced Data Preparation Time through Automated Orchestration
In the medium-term horizon of 2026–2027, an evolutionary
shift is expected from classical MLOps paradigms toward
the concept of Agentic MLOps, in which autonomous AI
agents independently monitor computational pipelines,
conduct A/B testing of alternative model versions, and
adapt ETL processes without direct human involvement.
The analysis of the results indicates that a key prerequisite
for such a transition is the presence of a mature automated
orchestration infrastructure combined with multi-level
mechanisms for detecting concept and statistical drift, which
together form the basis for autonomous decision-making
[19].
A further vector of development is the integration of large
language models (LLMs) into monitoring and analytical
loops. LLM usage can transform low-level statistical
degradation signals into semantically interpretable
explanations of the drivers of change, including the explicit
structuring of business context—for example, by indicating
shifts in the behaviour of specific user segments under the
influence of external market factors [9]. This interpretive
layer substantially increases the transparency of adaptive
ML systems for managerial and business roles, reducing the
gap between technical metrics and strategic decisions and,
as a result, enhancing the practical value of autonomous
MLOps architectures.
conclusIon
This study provided a comprehensive assessment of
adaptive model retraining mechanisms in production loops,
integrating a systematic review of the scientific literature
with an analysis of practical operating experience from high-
load ML systems. The results allow us to highlight several
core contributions.
First, the critical relevance of adaptive retraining is
substantiated: under the conditions of 2025, the capacity
of systems to respond to data drift emerges as a decisive
factor for the resilience of AI initiatives, while investments in
process automation deliver a return on invested resources
within the first year of operation in up to 74% of cases.
Second, the effectiveness of automated orchestration is
demonstrated. Using the Social Discovery Group case as an
illustrative example, it is confirmed that introducing Airflow
pipelines reduces the volume of manual work by 80% and
cuts data preparation time by 40%, enabling up to a twelve-
fold acceleration of key business processes.
Third, an author-developed hybrid architecture and a
retraining prioritisation algorithm are proposed, providing a
balanced relationship between model accuracy and the cost
of consumed cloud resources.
The practical significance of the work lies in establishing
a framework that enables a transition from static machine
learning models to dynamic, self-adapting systems.
Implementing the proposed solutions supports not only the
preservation of high predictive accuracy (ROC AUC 0.978+)
but also a substantial increase in companies’ operational
resilience under unpredictable shifts in the market
environment.
references
Maslej, N., Fattorini, L., Perrault, R., Gil, Y., Parli, V., Kariuki, 1.
N., Capstick, E., Reuel, A., Brynjolfsson, E., Etchemendy,
J., Ligett, K., Lyons, T ., Manyika, J., Niebles, J. C., Shoham,
Y., Wald, R., Walsh, T ., Hamrah, A., Santarlasci, L., … Oak,
S. (2025). Artificial Intelligence Index Report 2025 |
Stanford HAI. Retrieved from: https://hai.stanford.
edu/assets/files/hai_ai_index_report_2025.pdf (date
accessed: October 5, 2025).
Deloitte Insights. (2025, October 16). AI is capturing 2.
the digital dollar. What’s left for the rest of the tech
estate?Retrieved from: https://www.deloitte.com/us/
en/insights/topics/digital-transformation/ai-tech-
investment-roi.html (date accessed: October 17, 2025).
Adaptive machine learning for resource-constrained 3.
environments. (2025). arXiv. https://doi.org/10.48550/
arXiv.2503.18634
On the model update strategies for supervised learning 4.
in AIOps. (2024). ACM Digital Library. https://doi.
org/10.1145/3664599
Cost-effective retraining of machine learning 5.
models. (2023). arXiv. https://doi.org/10.48550/
arXiv.2310.04216
Mahdi, O. A., Pardede, E., Bevinakoppa, S., & Ali, N. (2025). 6.
Federated learning under concept drift: A systematic
survey of foundations, innovations, and future research
directions. Electronics, 14(22), 4480. https://doi.
org/10.3390/electronics14224480
Derzsi, A., Stinner, S., Weber, H., & Huber, M. (2024). 7.
Performance-based drift detection for active machine
learning model adaption: A comparative analysis
across 35 HVAC devices. Journal of Physics: Conference
Series, 3140, 022002. https://doi.org/10.1088/1742-
6596/3140/2/022002
UiPath. (2025). AI and Automation Trends 2025 | UiPath. 8.
Retrieved from: https://assets.ctfassets.net/5965pury2
lcm/54MpJe9ytWk6YhmN2TZwJS/7a96aac2aaad423
c8b06c479a8635f54/ai-and-automation-trends-2025-
ebook.pdf (date accessed: October 18, 2025).
Source Global Research. (2025). Planning for Growth in 9.
2025 | Source Global Research. Retrieved from: https://
www.sourceglobalresearch.com/report/planning-for-
growth-in-2025 (date accessed: October 20, 2025).
Hovakimyan, G., & Bravo, J. M. (2024). Evolving strategies 10.
in machine learning: A systematic review of concept
drift detection. Information, 15(12), 786. https://doi.
org/10.3390/info15120786

Page | 100Universal Library of Innovative Research and Studies
Adaptive Mechanisms for Model Retraining in Production: Drift Triggers, Retraining Prioritisation,
and Reduced Data Preparation Time through Automated Orchestration
Open-source drift detection tools in action: Insights from 11.
two use cases. (2024). arXiv. https://doi.org/10.48550/
arXiv.2404.18673
Grand View Research. (2025). MLOps market size, share 12.
& trends | Industry report, 2030 | Grand View Research.
Retrieved from: https://www.grandviewresearch.com/
industry-analysis/mlops-market-report (date accessed:
October 28, 2025).
Steidl, M., & colleagues. (2023). The pipeline for the 13.
continuous development of artificial intelligence-based
systems. Journal of Systems and Software, 205, 111615.
https://doi.org/10.1016/j.jss.2023.111615
Google Cloud. (2020, January 30). Build a pipeline 14.
for continuous model training | Vertex AI. Retrieved
from: https://docs.cloud.google.com/vertex-ai/docs/
pipelines/continuous-training-tutorial (date accessed:
November 3, 2025).
Forrester. (2024, September 9). Predictions 2025: 15.
Artificial Intelligence | Forrester. Retrieved from: https://
www.forrester.com/report/predictions-2025-artificial-
intelligence/RES181360 (date accessed: November 6,
2025).
GII Research. (2024, October 28). IDC FutureScape: 16.
Worldwide Artificial Intelligence and Automation 2025
Predictions | GII Research. Retrieved from: https://www.
giiresearch.com/report/id1582638-idc-futurescape-
worldwide-artificial-intelligence.html (date accessed:
November 10, 2025).
Google Cloud. (2024, August 28). MLOps: Continuous 17.
delivery and automation pipelines in machine learning
| Google Cloud Architecture Center. Retrieved from:
https://docs.cloud.google.com/architecture/mlops-
continuous-delivery-and-automation-pipelines-in-
machine-learning (date accessed: November 13, 2025).
A systematic literature review of proactive self-healing 18.
techniques for cloud computing. (2024). Concurrency
and Computation: Practice and Experience, e8246.
https://doi.org/10.1002/cpe.8246
Forrester Consulting. (2023). The Total Economic 19.
Impact™ of Google Cloud Vertex AI. Retrieved
from: https://services.google.com/fh/files/
misc/2023forresterteivertexai.pdf (date accessed:
November 19, 2025).
McKinsey & Company. (2025, July 1). Technology Trends 20.
Outlook 2025 | McKinsey & Company. Retrieved from:
https://www.mckinsey.com/~/media/mckinsey/
business%20functions/mckinsey%20digital/our%20
insights/the%20top%20trends%20in%20tech%20
2025/mckinsey-technology-trends-outlook-2025.pd f
(date accessed: November 23, 2025).
Mayeku, B., Hummel, S., & Memarmoshrefi, P . (2025). 21.
Machine unlearning for responsible and adaptive
AI in education. arXiv. https://doi.org/10.48550/
arXiv.2509.10590
Jbari, A., Ezzine, K., & Elghali, H. (2025). Data orchestration 22.
platform for AI workflows execution. SciTePress. https://
doi.org/10.5220/0013140600003892
Copyright: © 2026 The Author(s). This is an open access article distributed under the Creative Commons Attribution License,
which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.
