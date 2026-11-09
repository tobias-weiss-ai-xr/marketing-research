---
title: On the security and privacy of LLMs in Mobility
url: https://arxiv.org/abs/2609.26295
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Mauro Conti
- Lorenzo Perinello
- Umberto Salviati
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.26295
pages: 9
chars: 57448
fetched_at: '2026-11-08T13:24:31+00:00'
kb_version: 1
---

# On the security and privacy of LLMs in Mobility

On the security and privacy of LLMs in Mobility
Mauro Conti
mauro.conti@unipd.it
University of Padova
Italy
Örebro University
Örebro, Sweden
Lorenzo Perinello
lorenzo.perinello@phd.unipd.it
University of Padova
Italy
Umberto Salviati
umberto.salviati@phd.unipd.it
University of Padova
Italy
Fondazione Bruno Kessler
Italy
Abstract
The mobility sector is undergoing a paradigm shift driven by ad-
vances in Generative Artificial Intelligence. With a global market
valued at approximately 2.9 trillion dollars annually, considering
only cars, the integration of these technologies has the potential
to impact more than 1.5 billion vehicles worldwide. As Large Lan-
guage Models (LLMs) are increasingly adopted in mobility, concerns
about cybersecurity, privacy, and reliability emerge. Accordingly,
this paper surveys current applications and assesses these chal-
lenges. Since the European AI Act classifies transportation AI as
high risk, we derive nine technical classes from its requirements
to assess current research and future deployments. Our findings
show that research mainly studies GPT and Llama models (over
50% of reviewed works) and traffic applications while largely ne-
glecting security, privacy, and reliability. This gap extends to AI Act
compliance: among 35 reviewed works, only one includes a partial
vulnerability assessment and one a partial risk management system.
We identify a clear gap between strong optimization performance
and regulatory adherence, suggesting compliance is limited less by
technology than by a focus on static performance over lifecycle
safety, and underscoring an urgent need for security-by-design in
safety-critical intelligent transportation systems.
CCS Concepts
•General and reference → Surveys and overviews;•Security
and privacy→ Human and societal aspects of security and
privacy;•Applied computing→Transportation; Law.
Keywords
Security Survey, LLMs, Large Language Models, Transportation, AI
Act, Artificial Intelligence
ACM Reference Format:
Mauro Conti, Lorenzo Perinello, and Umberto Salviati. 2026. On the security
and privacy of LLMs in Mobility. InInternational Conference on Information
Technology for Social Good (GoodIT ’26), September 02–04, 2026, Pisa, Italy.
ACM, New York, NY, USA, 9 pages. https://doi.org/10.1145/3794786.3830783
This work is licensed under a Creative Commons Attribution 4.0 International License.
GoodIT ’26, Pisa, Italy
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2483-1/2026/09
https://doi.org/10.1145/3794786.3830783
1 Introduction
Mobility is a ubiquitous concept related to a multitude of social and
economic aspects: thereby, it represents an umbrella term encom-
passing multiple stakeholders and sectors and, today more than
ever, raises questions and opportunities [3].
Focusing on urban mobility, defined as the movement of indi-
viduals within urban areas, which currently host nearly 5 billion
people worldwide, issues and challenges concerning the efficiency
and effectiveness of mobility management are becoming increas-
ingly significant [ 66]. The importance of urban mobility is also
reflected in the growing body of scientific literature on the topic,
which explores the broader sector, investigates its limitations and
challenges, and focuses on its various dimensions [50]. One of these
dimensions concerns Intelligent Transport Systems (ITS), also re-
ferred to as smart mobility: a framework that integrates information
and communication technologies, and applies them to the trans-
port sector [ 58]. However, such integration has also introduced
new security and privacy challenges, including cyber threats, data
protection issues, and risks associated with the reliability and trust-
worthiness of these systems. Consequently, security has become a
fundamental aspect in the design, deployment, and management of
modern mobility systems [1].
At the same time, artificial intelligence (AI) has emerged as a
novel and important technology within the mobility sector and
has been widely exploited for optimization, simulation, and predic-
tion tasks within ITS. More recently, generative AI technologies,
such as LLMs, have emerged as key enabling technologies for these
tasks [45]. Furthermore, autonomous AI systems (Agentic AI) have
also been integrated into the mobility domain to boost the effec-
tiveness of simulations, management processes, and other mobility-
related tasks [19]. While researchers and industry drivers focus
almost exclusively on enhancing the performance [57], accuracy,
and operational capabilities of Generative Artificial Intelligence in
transport, they systematically overlook the foundational principle
of security-by-design [65]. As a consequence, the rapid deployment
of LLMs and autonomous agents effectively creates an entirely new
threat surface that can be readily exploited by malicious actors [20].
Recognizing the severity of these emerging vulnerabilities, reg-
ulatory bodies [25, 52] have increasingly expressed deep concern
about the rapid deployment of generative models in critical sec-
tors. This institutional awareness of the threat is manifested in
the enforcement of the European AI Act [25], which will become
fully applicable by August 2026, with specific compliance dead-
lines for embedded high-risk mobility systems extending to August
2027. Under this framework, regulatory entities explicitly acknowl-
edge that AI applications integrated into critical infrastructure (i.e.,
arXiv:2609.26295v1  [cs.CR]  22 Sep 2026

GoodIT ’26, September 02–04, 2026, Pisa, Italy Conti et al.
urban transportation and traffic management systems) pose sub-
stantial systemic risks, frequently classifying them as “high-risk”
systems. The AI Act mandates strict compliance regarding tech-
nical robustness, cybersecurity, and continuous human oversight.
Consequently, understanding the intersection of generative AI vul-
nerabilities and regulatory mandates is no longer just a technical
precaution but a legal requirement.
To the best of our knowledge, no study has yet systematically
investigated the current trends and trajectories of LLMs within
the mobility context through a security-focused lens. This paper
aims to bridge this gap. We provide a comprehensive security anal-
ysis of LLMs deployment in mobility systems, identifying current
gaps, mapping the expanding threat landscape, and aligning these
technical risks with the compliance requirements set by the AI Act.
Therefore, the contributions of this paper are to provide a tar-
geted survey of the topic and to investigate specific security, privacy
and reliability aspects of the works taken into account. Additionally,
the work presents a translation of the EU AI Act provisions into 9
technical evaluation criteria for AI transportation systems, which
are then systematically assessed against the investigated works.
This work is organized as follows: Section 2 provides an overview
of related work, while Section 3 describes the survey, the adopted
methodology, and the findings. Section 4 describes our AI Act re-
lated contribution. Finally, 5 outlines the conclusion and directions
for future works.
2 Related Work
This section gives a brief overview of security in AI and summarizes
recent surveys on AI in transportation.
Security on AI.A June 2026 Google Scholar search for(“large
language model” OR “llm”) AND (“security” OR “vulnerability” OR
“attack”)returned over 32,000 results. Since 2022 (before the rollout
of ChatGPT), more than 420 LLM security papers have appeared
in top venues (NDSS, IEEE S&P, ACM CCS, USENIX Security),
indicating rapid progress in LLM security research. AI security
has traditionally been studied as Adversarial Machine Learning
(AML), which examines the security, vulnerabilities, and robust-
ness of AI systems across their lifecycle, including both AI-level
and system-level exploits [10, 56]. Focusing specifically on LLMs,
since it is the goal of our work, introduces risks unique to gener-
ative models. The main threats are jailbreaking [70] and prompt
injection [39]. Jailbreaking bypasses alignment guardrails to elicit
prohibited content, while prompt injection uses text-based adver-
sarial examples to override system constraints. Indirect prompt
injection is especially dangerous, as malicious payloads are silently
ingested from untrusted external sources such as parsed documents
or web pages [16].
AI in transportation.Recent years have witnessed growing in-
terest in the integration of Generative AI and LLMs into mobility
systems, resulting in numerous studies investigating their applica-
tions. While a few works examine broader contexts, such as the role
of Generative AI in smart cities [60] and digital twins [21], which
may also encompass mobility-related applications and consider-
ations, most studies focus specifically on transportation-related
domains. For example, Mahmud et al. [45] provide a comprehensive
review of LLM integration in ITS, covering applications such as
traffic prediction, traffic signal optimization, autonomous driving,
and vehicle and pedestrian detection. The survey highlights the
potential of LLMs to improve transportation efficiency and decision-
making while also discussing technical and deployment challenges.
Other works survey the application of LLMs in ITS: Kaur et al. [37]
synthesize the LLM models, methods, and datasets used in the litera-
ture, while Hassija et al. [32] present a broader, application-oriented
survey of LLMs in ITS, discussing their adoption in traffic man-
agement, autonomous driving, predictive maintenance, vehicular
communications, and the challenges associated with integrating
multimodal data. Further studies focus on specific aspects of LLMs
in mobility: Jin et al. [ 34] examine LLMs from a transportation
planning perspective, covering transportation analysis, modeling,
and prediction, while Zhang and Dingkai [72] focus specifically on
transportation management and safety.
Overall, existing papers provide valuable insights into the usage
of LLMs for mobility applications, however, none of the previously
cited works systematically addresses security (or related fields) con-
siderations or analyzes the security challenges arising from their
adoption. As a result, despite its importance, security remains a
largely overlooked research area within the current body of litera-
ture.
3 Survey
This section presents a preliminary survey of the literature on
the application of LLMs in urban mobility, with a twofold goal: to
analyze the models used and the tasks addressed, and to examine
security, privacy, reliability and reproducibility aspects of these
systems. Finally the findings, which are discussed in Section 3.3,
provide an overview of the current landscape and identify research
gaps that motivate further investigation into secure and trustworthy
generative AI solutions for urban mobility.
3.1 Methodology
We conducted a targeted literature search in Web of Science using
a boolean query that combined mobility terms with LLM-related
terms. Guided by Google Trends data for the first half of 2026, we
compared major generative AI platforms: ChatGPT, Google Gemini,
Claude AI, Microsoft Copilot, Grok AI, Llama, Qwen, Microsoft Phi,
Mistral AI, and DeepSeek. ChatGPT [2] showed the highest relative
search interest (average interest index 1: 92), while Llama and Gem-
ini ranked much lower, 8 and 6, respectively, and the others showed
negligible interest. Although Google Trends does not reflect actual
usage, we used relative search interest as proxy data for public
attention and visibility, motivating our focus on GPT-based archi-
tectures. Our mobility query included: urban mobility, intelligent
transport system(s), smart mobility, traffic management, spatio-
temporal, urban computing, urban sensing, smart city, and urban
prediction, combined with OR. This block was then linked with
AND to at least one generative AI term: large language model(s),
generative artificial intelligence, agentic AI, autonomous agent(s),
LLM, or GPT. The search returned 125 publications. After removing
duplicates, review papers (see Section 2), and out-of-scope studies,
we obtained 35 papers for full-text analysis.
1For the average interest definition, see trends.google.com/trends

On the security and privacy of LLMs in Mobility GoodIT ’26, September 02–04, 2026, Pisa, Italy
3.2 Key elements inspected
Table 1 summarizes the studies included in the review, reporting
the functionality of the models utilized, classified according to the
taxonomy provided in [53]: Information Processor (A), Knowledge
Encoders (B), component generators (C) and decision facilitators
(D). A includes papers that use AI as context encoder, data analyzer
or a multimodal fuser; B includes knowledge extractor and repre-
sentation embedder; C includes simulator, evaluator and interpreter,
or data synthesizer; finally D includes Decision maker or guider and
spatio-temporal predictors. A more detailed description of these
categories is provided in [53]. Moreover, we reported the task ad-
dressed, and the extent to which security, privacy, and reliability
aspects are considered. These aspects are categorized as follows:
• discussed(◦): the topic is mentioned or discussed in the
paper, either briefly or in detail, but no concrete implemen-
tation is provided;
• implemented(•): the paper not only discusses the topic
but also describes and incorporates specific mechanisms,
methods, or procedures addressing it;
• not addressed( –): the topic is neither discussed nor imple-
mented within the study.
3.3 Findings
This section provides an overview of the findings derived from
the preliminary survey, highlighting the most commonly adopted
models and application tasks, as well as the extent to which security,
privacy, reliability, and reproducibility aspects are considered in
current research.
3.3.1 Models.Figure 1 summarizes the distribution of model fami-
lies employed across the reviewed studies: the GPT family appears
in 19 papers, accounting for more than half of the reviewed papers;
the Llama family is the second-most-frequently used category, ap-
pearing in 11 studies. In contrast, language models such as BERT are
less common, appearing in only four papers. Other large language
models are represented only marginally in the literature: Mistral
family appears in three papers, and Gemini, Qwen, Gemma, and
Vicuna occur in two, and Vicuna appears in one. Other models,
which represent the remaining seven paper, include other LLMs
such as DeepSeek or Chronos.
Figure 1: Distribution of Model Families Across the Reviewed
Papers
3.3.2 Functionality.Decision facilitators emerged as the dominant
functionality category, appearing in 25 of the 35 reviewed studies
(71.4%). Then, Information Processor was the second most common,
occurring in 18 studies (51.4%), while Knowledge Encoders appeared
in 11 studies (31.4%). In contrast, we identify Functionality C in only
one publication. Notably, functionalities frequently co-occurred,
particularly A and D, which appeared together in 10 studies.
3.3.3 Security, Privacy, Reliability.Regarding the acknowledgment
of security aspects in the scrutinized papers, only two studies imple-
mented security measures at least partially within their proposed
methodologies, while an additional four papers merely discussed
security-related concerns without providing concrete implemen-
tation details. Among the measures implemented, [73] maintains
data security and integrity, and [35] prevents the use of invalid or
harmful prompts [51]. Other works, [14, 31, 36, 51, 67], only discuss
security-related problems without any explicit implementation.
With respect to privacy, only [26] explicitly addresses privacy
preservation by explicitly taking into account data privacy in the
selection of the datasets used; six additional studies ([7, 8, 14, 46,
51, 67, 73]) discuss only privacy at high level: [14, 73] state privacy
without giving any implementation details, others ( [ 9, 38, 67])
declare privacy as future work trajectory and only [46] specifies
clearly privacy as a limitation of the work.
Regarding reliability, six studies incorporate mechanisms to im-
prove the robustness and dependability of their proposed systems.
In [73], the LLM-based system is equipped with mechanisms to en-
sure data authenticity, and incorporate a human-in-the-loop inter-
vention protocol by design. Furthermore, [64] improves reliability
by implementing output validation procedures. In [ 13] and [41],
reliability is assessed by evaluating the proposed frameworks with
different LLM backbones, demonstrating consistent performance
across models. Furthermore, [35] explicitly states the evaluation of
the robustness as an objective of the paper. Finally, [43] enhances
robustness by employing output comparison, consistency checks,
and selective re-extraction mechanisms to mitigate bias and im-
prove the reliability of generated predictions. All the other papers
that discuss reliability address it as a limitation or future work.
3.3.4 Code A vailability.Regarding the open-source aspect, which
is crucial for reproducibility of results and for conducting security
and related research, among the investigated papers, 13 out of 35
made the code available through a repository.
4 AI Act in Transportation Reserach
This section contextualizes the current trajectories of LLMs in urban
mobility within the newly established European regulatory frame-
work [25]. By mapping the technical vulnerabilities discovered in
literature to explicit legal obligations, we evaluate the systemic
readiness of the intelligent transportation research domain.
4.1 Risk Classification in Transportation
Systems
The AI Act introduces a strict risk-based paradigm [24] that cate-
gorizes artificial intelligence systems into four distinct levels based
on their potential to cause harm, establish systemic vulnerabilities,
or infringe upon fundamental rights:

GoodIT ’26, September 02–04, 2026, Pisa, Italy Conti et al.
Paper Model(s) Funct. Task
Security
Privacy
Reliability
Code Avail.
Accuracy & Robustness
Risk Mgmt. System
Transparency & Copy.
Vulnerability Eval.
[17] GPT-3.5-turbo A Route risk assessment for urban cyclists – – ◦ ✓ 1.50±0.71 1.00 † 1.00† 1.00†
[73] GPT-3.5-turbo A Traffic management • ◦ • ✓ 3.50±0.711.00 † 1.00† 1.33±0.58
[33] LLaMA 3 8B, Mistral 8x7B B Location representation – – – ✓ 2.00±1.41 1.00 † 1.00† 1.00†
[51] LSTM, GAN, RL A,D Traffic management ◦ ◦ ◦ ✗ 1.00† 1.00† 1.00† 1.00†
[38] BERT, TrajC-BERT variants D Trajectory prediction for carpooling &
taxi routing
– – ◦ ✓ 2.00±1.41 1.00 † 1.00† 1.00†
[63] GPT-3 A,D Traffic management – – – ✗ 2.50±0.71 1.00 † 1.00† 1.33±0.58
[61] GPT-5 Thinking, GPT-4o,
Gemini 2.5 Pro, DeepSeek
V3
C,D Traffic light optimization – – – ✗ 3.00±2.83 1.00 † 1.00† 1.00†
[4] Gemma 2, Qwen 2.5,
GPT-4o, Llama 3.2,
Aya-Expanse
A,D Traffic prediction – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[29] BERT-family models A Traffic incident severity classification – – – ✓ 2.00±1.41 1.00 † 1.00† 1.00†
[64] GPT-3.5-turbo A Real-time traffic insights – – • ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[67] GPT-2 D Traffic prediction ◦ ◦ ◦ ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[42] GPT-2 A,B Traffic prediction – – – ✓ 2.00±1.41 1.00 † 1.00† 1.00†
[13] Llama 3.2-1B-Instruct B – – • ✓ 2.50±2.12 1.00 † 1.00† 1.00†
[62] Meta-Llama A,D Electric vehicles charging demand
prediction
– – – ✗ 2.50±2.12 1.00 † 1.00† 1.00†
[9] Qwen2.5-7B D Multimodal transportation simulation – – ◦ ✓ 3.50±0.711.00 † 1.00† 1.00†
[35] Llama 3 A,D Fleet dispatching • – • ✗ 3.50±2.123.00 † 1.00† 3.67±0.58
[36] GPT-4o, Mistral-8x22B,
Llama 3.1
D Urban planning and smart-city
management
◦ ◦ – ✓ 2.50±2.12 1.00 † 1.00† 1.00†
[26] GPT-2 A,D Electric Vehicle Charging Forecasting – • – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[12] GPT-3.5, GPT-4 D Autonomous vehicle coordination – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[69] GPT-2 A,D Traffic flow prediction – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[41] Vicuna-7B A,B Urban forecasting – – • ✗ 2.50±2.12 1.00 † 1.00† 1.00†
[71] LLaMA2-7B D Origin-Destination flow prediction – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[15] BERT B,D Traffic flow prediction framework – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[40] Vicuna-7B, Vicuna-13B D Traffic forecasting – – – ✓ 2.00±1.41 1.00 † 1.00† 1.00†
[43] GPT-4o A,B Urban forecasting – – • ✓ 3.50±0.711.00 † 1.50±0.711.00 †
[68] Unknown B,D Point-of-interest recommendation – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[14] GPT-4, Llama3-8B A,D Mobility perspective framework ◦ ◦ ◦ ✗ 2.50±0.71 1.00 † 1.00† 1.67±1.15
[8] GPT-4-turbo, Gemini-Pro,
Llama-2
B Urban mobility assessment – ◦ – ✓ 2.00±1.41 1.00 † 1.00† 1.00†
[46] GPT-4o-mini D Traffic management – ◦ ◦ ✗ 1.50±0.71 1.00 † 1.00† 1.00†
[7] GPT-4o, GPT-4, GPT-3.5,
Llama, Mistral families
D Zero-shot next-location prediction
benchmark
– – – ✓ 3.50±0.712.00 † 1.00† 1.00†
[11] GPT-2 D Taxi demand forecasting – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[27] BGE-Large, GLM4-9B, BERT B,D Traffic management regulations – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[30] Meta-Llama-3.1-8B B,D POI prediction – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
[31] GAN A,D Traffic management ◦ – – ✗ 3.00±1.41 1.00 † 1.00† 1.00†
[44] ST-LLM, GCN-GPT,
GAT-GPT, Chronos
D Traffic prediction – – – ✗ 2.00±1.41 1.00 † 1.00† 1.00†
† indicates that the standard deviation value is equal to zero (std=0.00).
Table 1: Review of Model(s) used, Functionality (Funct.), Task, Security, Privacy, Reliability, Code Availability, Accuracy &
Robustness, Risk Management System, Transparency & Copyright, and Vulnerability Evaluation in surveyed papers.
(i)Unacceptable Risk:AI systems that pose a clear threat to the
safety, livelihoods, and rights of individuals are strictly prohibited.
This category includes practices such as social scoring, harmful
AI-based manipulation, and real-time remote biometric identifica-
tion in publicly accessible spaces. (ii)High Risk:Use cases that can
pose serious risks to human health, safety, or fundamental rights
are classified under this tier. These systems are subject to strict
legal and technical obligations before they can be deployed on the
market. (iii)Limited (Transparency) Risk:This category applies to
AI systems with a specific need for disclosure, such as chatbots
[5, 18, 28, 47, 48, 54, 59] or generative AI tools [49, 55]. Providers

On the security and privacy of LLMs in Mobility GoodIT ’26, September 02–04, 2026, Pisa, Italy
must ensure that humans are explicitly informed they are interact-
ing with an automated system and that AI-generated content or
deep fakes are clearly identifiable. (iv)Minimal or No Risk:The vast
majority of AI applications currently utilized within the EU (e.g.,
spam filters or AI-enabled video games) fall into this category and
face no regulatory restrictions under the Act.
Under this risk-based paradigm, AI safety components in criti-
cal transportation infrastructure, such as road traffic management
and transport operations, are classified as high-risk under Article
6(2)[6] and Annex III [22, 25], as their failure could endanger public
health and safety [25]. As discussed in our literature survey (Sec-
tion 3), recent research increasingly uses LLMs and autonomous
agentic architectures for core mobility tasks such as real-time traffic
management, traffic light optimization, and vehicle dispatching.
4.2 Compliance Framework Evaluation Criteria
While these top-down institutional tools offer a generalized base-
line, mobility systems present highly interconnected threat surfaces
bridging General Purpose AI (GPAI) [23] and embedded safety com-
ponents. To address this domain-specific complexity, we translate
the high-level legal articles of the AI Act into actionable develop-
ment and evaluation requirements tailored for the transportation
sector, as structured in Table 2.
To systematically assess the selected state-of-the-art mobility lit-
erature against the technical mandates of Regulation (EU) 2024/1689
(the AI Act), this section examines each requirement presented in
Table 2 item by item. Specifically, we detail the underlying opera-
tional objectives for each criterion, defining the baseline compliance
scope used to evaluate the reviewed works:
Vulnerability evaluation.
• Adversarial Testing:The execution and documentation of
standardized adversarial testing protocols to proactively
identify vulnerabilities, safety weaknesses, and potential
systemic risks within the AI model.
• Risk Mitigation Measures:The strategic assessment of sys-
temic risks at the Union level, coupled with the implementa-
tion of mitigation measures and the procedural management
of serious incidents and corrective actions.
• Cybersecurity Protection:The assurance of an adequate level
of security for both the AI model and its underlying physical
infrastructure to prevent unauthorized access, manipulation,
or compromise.
Risk management system.
• Lifecycle Risk Identification & Analysis:Continuous, iterative
management of risks across the AI system’s entire lifecy-
cle, including initial analysis and post-market monitoring
feedback loops.
• Misuse Scenario Evaluation:Evaluation of risks arising from
reasonably foreseeable misuse, including impacts on funda-
mental rights and specific safeguards for vulnerable groups
or minors.
• Residual Risk Acceptability:Formal application of the mitiga-
tion hierarchy (design, controls, information and training) to
reduce risks, followed by a documented judgment of residual
risk acceptability.
• Real-World / Pipeline Attack Testing:Technical validation
through predefined metrics or thresholds and, if applicable,
Art. 60-compliant [25] real-world testing plans, informed
consent, and regulatory oversight.
Quality management system.
• Design Controls & Test Plans:The implementation of system-
atic actions, technical procedures, and validation processes
used for the design, development, and verification of the
high-risk AI system.
• Data Governance:Management practices for data acquisition,
collection, labelling, storage, and bias mitigation, ensuring
data sets are representative and of high quality.
• Logging by Design:Technical capabilities allowing for the
automatic, continuous recording of events throughout the
AI system’s lifetime to ensure traceability and operational
accountability.
• Post-Market Monitoring:A systematic process to actively
collect, document, and analyze data on the system’s perfor-
mance after it has been placed on the market.
• Incident Reporting:Procedures for the identification, inves-
tigation, and timely notification of serious incidents to na-
tional competent authorities.
Transparency & copyright.
• Interaction Disclosure:The implementation of clear, distin-
guishable mechanisms to inform natural persons that they
are interacting with an AI system rather than a human, un-
less it is obvious from the context.
• AI-Generated Content Watermarking:The technical imple-
mentation of machine-readable, robust, and interoperable
markings on synthetic audio, image, video, or text outputs
to ensure they are detectable as artificially generated.
• Deep Fake Labelling:Obligations for deployers to disclose
when content constitutes a deep fake (artificially generated
or manipulated imagery, audio, or video) or to disclose the
use of AI-generated text in public interest publications.
• Training Data Summary:The creation and public disclosure
of a sufficiently detailed summary of the training content
used for General-Purpose AI models, following the template
provided by the AI Office.
• Copyright Compliance Policy:The establishment and execu-
tion of an internal policy to respect Union copyright law,
specifically identifying and adhering to the “reservation of
rights” (opt-outs) expressed by rightsholders.
Technical documentation.
• Compliance for Regulators:The comprehensive collection
of technical documentation regarding the model’s devel-
opment, training, testing processes, and evaluation results,
maintained for the AI Office and national competent author-
ities.
• Transparency for Downstream Users:The documentation pro-
vided to downstream AI system providers, detailing the
model’s capabilities and limitations to ensure safe integra-
tion and compliance with regulatory obligations.

GoodIT ’26, September 02–04, 2026, Pisa, Italy Conti et al.
Category Requirement Article Reference Mean±SD
Vulnerability Evaluation
(GPAI w/ Systemic Risk)
Adversarial testing (assessment) Art. 55(1)(a)1.11±0.53
Risk mitigation measures (implementation) Art. 55(1)(b),(c)1.06±0.34
Cybersecurity protection Art. 55(1)(d)1.17±0.62
Risk Management System
(High-Risk)
Lifecycle risk identification & analysis Art. 9(1), Art. 9(2)(a), Art. 9(2)(c) -
Misuse scenario evaluation Art. 9(2)(b), Art. 9(9) -
Residual risk acceptability Art. 9(5) -
Real-world/pipeline attack testing Art. 9(6), Art. 9(7), Art. 9(8), Art. 601.09±0.37
Quality Management System
(High-Risk)
Design controls, test plans Art. 17(1)(b–d) -
Data governance Art. 17(1)(f), Art. 10 -
Logging by design Art. 12, Art. 19(1) -
Post-market monitoring Art. 17(1)(h), Art. 72 -
Incident reporting Art. 17(1)(i), Art. 73(1) -
Transparency & Copyright
Interaction disclosure (chatbot) Art. 50(1) -
AI-generated content watermarking Art. 50(2)1.03±0.17
Deep fake labelling Art. 50(4) -
Training data summary (GPAI) Art. 53(1)(d)1.00 †
Copyright compliance policy (GPAI) Art. 53(1)(c) -
Technical Documentation Compliance for Regulators Art. 53(1)(a), Annex XI - Transparency for Downstream Users Art. 53(1)(b), Annex XII -
Human Oversight
(High-Risk)
Override/interrupt mechanism Art. 14(3), Art. 14(4)(d–e) -
Automation bias & cognitive safeguards Art. 14(1–3); Art. 14(4)(a–c); Art. 14(5) -
Accuracy & Robustness
(High-Risk)
Defined accuracy metrics Art. 15(1), 15(2), 15(3)3.03±0.79
Robustness and adversarial resilience Art. 15(1), 15(4), Art. 15(5)1.57±1.12
Fundamental Rights &
Deployment
FRIA conducted before deployment Art. 27 -
Informing workers of AI deployment Art. 26 -
Compliance & Administrative
(High-Risk)
Conformity assessment procedure Art. 43 -
Registration in the EU database Art. 49 -
EU Declaration of Conformity & CE marking Art. 47, Art. 48 -
† indicates that the standard deviation value is equal to zero (std=0.00).
Table 2: EU AI Act Compliance Requirements with paper evaluation means and standard deviations.
Human oversight.
• Override / Interrupt Mechanism:The implementation of de-
sign features and procedures that allow natural persons to
effectively monitor the system, intervene in its operation,
and safely halt or override its output or functioning when
necessary.
• Automation Bias & Cognitive Safeguards:The implementation
of tools, training, and processes (including dual-verification
where required) that enable natural persons to understand
system limitations, avoid over-reliance on AI outputs, inter-
pret results correctly, and perform independent validation.
Accuracy & robustness.
• Defined Accuracy Metrics:The systematic process for defin-
ing, measuring, and documenting the accuracy performance
of the AI system, including the selection of appropriate met-
rics and their communication in user instructions.
• Robustness and Adversarial Resilience:The implementation of
technical and organizational measures to ensure the system
performs consistently under stress, handles errors gracefully,
and remains secure against malicious attempts to manipulate
performance or exploit vulnerabilities (e.g., data poisoning,
evasion).
Fundamental rights.
• Fundamental Rights Impact Assessment (FRIA) Conducted Be-
fore Deployment:The process of identifying, assessing, and
documenting the potential impact of a high-risk AI system
on fundamental rights, including the mitigation of identified
risks and the implementation of human oversight measures.
• Informing Workers of AI Deployment:The transparency and
communication protocol established to inform workers and
their representatives about the deployment of high-risk AI
systems in the workplace, ensuring compliance with Article
26(7).
Compliance & administrative.
• Conformity Assessment Procedure:The process of verifying
that the high-risk AI system complies with the requirements
set out in the AI Act, utilizing either internal control or a
third-party notified body assessment as mandated by Article
43.
• Registration in the EU Database:The mandatory registration
of the high-risk AI system (and in some cases, the deployer)
in the EU database pursuant to Article 49 before the system
is placed on the market or put into service.

On the security and privacy of LLMs in Mobility GoodIT ’26, September 02–04, 2026, Pisa, Italy
• EU Declaration of Conformity & CE Marking:The creation of
the written EU Declaration of Conformity (Art. 47) and the af-
fixing of the CE marking (Art. 48) to indicate the AI system’s
adherence to all relevant Union harmonization legislation.
4.3 Compliance Assessment of the Reviewed
Work
While the previous section defines the regulatory framework of
the EU AI Act for high-risk AI systems, analyzing the exploratory
literature requires a more focused and quantifiable methodological
scope. To establish a rigorous empirical baseline, the corpus of35
selected papers has been systematically evaluated across nine dis-
tinct technical criteria derived from the regulatory mandates. This
cross-sectional analysis yields a total dataset of280individual eval-
uation points (35 papers× 8 criteria), providing a comprehensive
mapping of the current research landscape against the European
framework.
4.3.1 Scope Selection.Assessing academic research under the EU
AI Act requires separating technical design from deployment. Since
this study analyzes algorithmic architectures rather than commer-
cial systems, applying the full regulatory spectrum is inappropriate.
Our scope isolates eight requirements within the researcher’s
sphere of influence, mapping to theSecurity and Compliance by
Designparadigm across four framework categories:
(i) Vulnerability Evaluation (GPAI with Systemic Risk):Adver-
sarial testing,Risk mitigation, andCybersecurity protection,
addressing model flaws and execution security.
(ii) Risk Management System (High-Risk):Real-world/pipeline
attack testingto evaluate pipeline resilience before industri-
alization.
(iii) Transparency & Copyright:AI content watermarkingand
Training data summary, embedding traceability into gen-
eration routines.
(iv) Accuracy & Robustness (High-Risk):Defined accuracy met-
ricsandAdversarial resilience, forming the core of empirical
benchmark testing.
Conversely, downstream operational and administrative duties,
such as Quality Management Systems (QMS), Technical Documenta-
tion with compliance documentation, Human Oversight, Fundamen-
tal Rights and Deployment, and Compliance and Administrative
categories are excluded. These represent institutional governance
belonging strictly to commercial deployment.
4.3.2 Evaluation Metric and Likert Scale.To evaluate the depth
to which each reviewed work addresses these fundamental legal
mandates, we apply a standardized 5-point Likert scale. This metric
measures the progression from total regulatory omission to full
pipeline integration for each requirement:
1. Not Mentioned:There is no evidence, acknowledgment,
or discussion of the requirement or its underlying safety
implications.
2. Identified:The requirement or threat surface is explicitly
acknowledged as a theoretical necessity, but no actionable
technical methodology or concrete test cases are provided.
3. Assessed:The requirement is actively evaluated or tested as
a static, one-time baseline activity (e.g., standard static test-
ing), but lacks a formalized protocol or structured lifecycle
integration.
4. Planned / Implemented:Structured technical mechanisms,
defensive policies, or compliant testing plans are formally
implemented and fully documented within the proposed
architecture.
5. Fully Assessed & Integrated:Advanced, automated com-
pliance workflows are seamlessly integrated into the devel-
opment framework.
4.3.3 Empirical Evaluation.The empirical mapping of the reviewed
papers reveals a pronounced empirical divergence between high
functional performance and near-absent real security compliance
(see Table 2). Academic research focuses almost exclusively on the
applications themselves, systematically omitting the technical and
procedural safeguards mandated by Regulation (EU) 2024/1689.
• Accuracy & Robustness [ 𝜇= 2.30, 𝜎= 1.21, 𝑁= 70]:
This category features the highest macro average but re-
mains heavily polarized. While researchers meticulously
track standard performance parameters (𝜇= 3.03, 𝜎= 0.79),
actual resilience against cyberattacks drops sharply (𝜇= 1.57,
𝜎= 1.12). This observation highlights a clear tendency to
conflate statistical precision with structural safety. How-
ever, the high variance points to rare, virtuous exceptions
(max= 5) capable of embedding effective defensive barriers,
proving that the current bottleneck is a matter of research
priorities rather than technical feasibility.
• Vulnerability Evaluation [ 𝜇= 1.11, 𝜎= 0.51, 𝑁= 105]:
A critical blind spot for the domain. Near-zero scores in
cybersecurity protection (𝜇= 1.17, 𝜎= 0.62) and vulnera-
bility testing (𝜇= 1.11, 𝜎= 0.53) confirm a widespread lack
of proactive controls against malicious exploitation. Only
isolated exceptions (max= 5) demonstrate that subjecting
models to stress tests and attack simulations prior to publi-
cation is entirely achievable.
• Risk Management System [ 𝜇= 1.09, 𝜎= 0.37, 𝑁=
35]:Risk governance is virtually non-existent. Real-world
pipeline attack testing and risk mitigation measures share an
identical low rating (𝜇= 1.09, 𝜎= 0.37and 𝜇= 1.06, 𝜎= 0.34,
respectively). Even the top-scoring studies (max= 5) limit
security to basic technical bug-tracking, completely omitting
organizational governance, contingency fallback plans, and
the regulatory notification channels required by law.
• Transparency & Copyright [ 𝜇= 1.01, 𝜎= 0.12, 𝑁= 70]:
Total stagnation across the entire sector. The inclusion of dig-
ital watermarking in synthetic content is nominal (𝜇= 1.03,
𝜎= 0.17). The most critical metric is training data trans-
parency, which registers absolute zero variance ( 𝜇= 1.00,
𝜎= 0.00, max= 5): none of the evaluated papers provide or
plan copyright-compliant dataset documentation, marking a
collective failure regarding transparency obligations.
5 Conclusion and Future Directions
This paper investigated the integration of Large Language Mod-
els within the mobility domain by analyzing 35 studies through

GoodIT ’26, September 02–04, 2026, Pisa, Italy Conti et al.
a security lens and evaluating their compliance readiness against
the European AI Act. Findings indicate a technological landscape
dominated by the GPT and Llama model families, which together
account for more than half of the surveyed papers. Such concen-
tration not only reflects the popularity of these models in current
research but also raises concerns that vulnerabilities affecting them
could propagate across a large portion of mobility applications. Fur-
thermore, only five papers discuss security-related aspects, and only
two incorporate security mechanisms into their proposed solutions.
This trend suggests that security remains largely overlooked by
the research community, despite its critical importance for mobility
applications. Consequently, the real-world deployment of many
proposed approaches could be premature without a comprehensive
security assessment and validation. This also applies to security
as well: only one paper implements countermeasures, and seven
discuss this aspect mainly as future work, limitations, or without
providing any real details. The very limited attention devoted to
privacy suggests that the design of LLM-based mobility solutions
often lacks concrete privacy-preserving principles and mechanisms.
Although reliability is the most widely implemented element in the
works (six papers out of 35 implement reliability-related mecha-
nisms), hallucination prevention, output validation, human-in-the-
loop, and other mitigation methods are clearly underinvestigated
and underimplemented in a critical sector such as mobility. Over-
all, the survey highlights systematic vulnerabilities in the mobility
domain, providing fertile ground for potential attacks and threats.
These findings align with the compliance categories of the EU Reg-
ulation 2024/1689 discussed in Section 4. The Act strictly regulates
AI-based transportation systems, classifying the mobility sector
as a high-risk AI application area. Quantitative analysis shows a
statistically significant gap between high functional performance
and regulatory alignment, indicating that current literature priori-
tizes capabilities over required technical and procedural safeguards.
Although isolated peak scores (max= 5) prove that compliance is
technically feasible, they are rare: this suggests the main barrier is
not technical capability, but the research community’s treatment
of safety and security beyond deployability. Proactive vulnerability
testing, lifecycle risk governance, and copyright-compliant training
data transparency are largely absent from most worsk.
With this work, which underlines a clear gap between the adop-
tion of LLMs in mobility and the treatment of security and privacy.
First, developing interdisciplinary frameworks at the intersection
of legal compliance and transportation AI is critical to translate reg-
ulatory mandates into quantifiable operational constraints. Second,
establishing robust deployability paradigms will ensure that LLMs
can handle real-time, large-scale mobility data safely at the edge.
Third, future work must embed advanced cybersecurity mecha-
nisms directly into Intelligent Transportation Systems to secure the
entire AI lifecycle against data manipulation. Finally, achieving full
compliance with overarching frameworks like the AI Act requires
strict adherence to copyright laws for transit datasets, alongside
rigorous, real-world stress testing. This demands continuous adver-
sarial risk assessment measures to guarantee systemic resilience
against prompt injections, data poisoning, and cyber threats in
physical deployment.
Acknowledgments
This work is funded by the MUR (Italian Ministry of Universities and Research) under
the MOST—Sustainable Mobility National Research Center initiative within the Euro-
pean Union Next-Generation EU (PIANO NAZIONALE DI RIPRESA E RESILIENZA
(PNRR)—MISSIONE 4 COMPONENTE 2, INVESTIMENTO 1.4—D.D. 1033 17 June 2022,
CN00000023), as well as from the Department of Mathematics of the University of
Padua.
References
[1] Abdo, A., Chen, H., Zhao, X., Wu, G., and Feng, Y.Cybersecurity on connected
and automated transportation systems: A survey.IEEE Transactions on Intelligent
Vehicles 9, 1 (2024), 1382–1401.
[2] Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. L.,
Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al.Gpt-4 technical
report.arXiv preprint arXiv:2303.08774(2023).
[3]Adey, P.Mobility. Routledge, 2017.
[4] Alsahfi, T., and Qasim, K. U.Trafficot-r: A framework for advanced spatio-
temporal reasoning in large language models.Alexandria Engineering Journal
128(2025), 464–475.
[5]Anthropic. Claude. https://claude.ai, 2026. Accessed: 2026-06-04.
[6] Artificial Intelligence Act EU. Article 6: Classification rules for high-risk ai
systems, 2026. Accessed: 2026-06-04.
[7] Beneduce, C., Lepri, B., and Luca, M.Large language models are zero-shot next
location predictors.IEEE Access 13(2025), 77456–77467.
[8] Bhandari, P., Anastasopoulos, A., and Pfoser, D.Urban mobility assessment
using llms. InProceedings of the 32nd ACM International Conference on Advances
in Geographic Information Systems(New York, NY, USA, 2024), SIGSPATIAL ’24,
Association for Computing Machinery, p. 67–79.
[9] Calderón, C., Martí, P., Jordán, J., Palanca, J., and Julian, V.Cognitive
agents in urban mobility: Integrating llm reasoning into multi-agent simulations.
Sensors 25, 18 (2025).
[10] Castagnaro, A., Salviati, U., Conti, M., Pajola, L., and Pizzi, S.The hidden
threat in plain text: Attacking rag data loaders. InProceedings of the 18th ACM
Workshop on Artificial Intelligence and Security(New York, NY, USA, 2026), AISec
’25, Association for Computing Machinery, p. 170–181.
[11] Chen, J., W ang, Y., Li, R., Yuan, C., Zong, C., Zhang, M., and Chen, Z.Enhancing
taxi demand prediction with limited data using a spatial-temporal large language
model.Transportation Research Record 2680(2025), 336 – 352.
[12] Chen, R., Song, W., Zu, W., Dong, Z., Guo, Z., Sun, F., Tian, Z., and W ang,
J.An llm-driven framework for multiple-vehicle dispatching and navigation
in smart city landscapes. In2024 IEEE International Conference on Robotics and
Automation (ICRA)(05 2024), pp. 2147–2153.
[13] Chen, Y., Tao, Y., Jiang, Y., Liu, S., Yu, H., and Cong, G.Enhancing large
language models for mobility analytics with semantic location tokenization. In
Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and
Data Mining V.2(New York, NY, USA, 2025), KDD ’25, Association for Computing
Machinery, p. 262–273.
[14] Chen, Y., Zhang, H., Li, C., Chi, B., Chen, X. M., and Wu, J.Large language
model empowered smart city mobility.Frontiers of Engineering Management 12,
1 (Mar 2025), 201–207.
[15] Cheng, H., Gong, Z., and W ang, C.Llm-tfp: Integrating large language models
with spatio-temporal features for urban traffic flow prediction.Applied Soft
Computing 177(2025), 113174.
[16] Collu, M. G., Salviati, U., Confalonieri, R., Conti, M., and Apruzzese, G.
Misleading large language models used (or misused) in scientific peer-reviewing
via hidden prompt-injection attacks.ACM Trans. AI Secur. Priv.(Mar. 2026). Just
Accepted.
[17] Costa, D. G., Silva, I., Medeiros, M., Bittencourt, J. C. N., and Andrade, M.
A method to promote safe cycling powered by large language models and ai
agents.MethodsX 13(2024), 102880.
[18]DeepSeek. Deepseek. https://www.deepseek.com, 2026. Accessed: 2026-06-04.
[19] Dokuchaev, V. A., and Maklachkova, V. V.Cybersecurity impact on the
transport security. In2023 International Conference on Engineering Management
of Communication and Technology (EMCTECH)(2023), pp. 1–6.
[20] Dong, Z., Zhou, Z., Y ang, C., Shao, J., and Qiao, Y.Attacks, defenses and evalu-
ations for llm conversation safety: A survey. InProceedings of the 2024 Conference
of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers)(2024), pp. 6734–6747.
[21] Duran, K., Cakir, L. V., Ozdem, M., Gursu, K., and Canberk, B.Generative
ai-enabled digital twins for 6g-enhanced smart cities. In2024 IEEE Globecom
Workshops (GC Wkshps)(2024), pp. 1–6.
[22]EU AI Act. Annex iii: High-risk ai systems under the eu ai act, 2026. Accessed:
2026-06-04.
[23] European Commission. The general-purpose AI code of practice. https://digital-
strategy.ec.europa.eu/en/policies/contents-code-gpai, 2026. Accessed: 2026-06-
04.

On the security and privacy of LLMs in Mobility GoodIT ’26, September 02–04, 2026, Pisa, Italy
[24] European Commission. Regulatory framework for artificial intelligence (ai act),
2026. Accessed: 2026-06-04.
[25] European Parliament and Council of the European Union. Regulation (eu)
2024/1689 of the european parliament and of the council of 13 june 2024 laying
down harmonised rules on artificial intelligence (artificial intelligence act), 2024.
OJ L 2024/1689, 12 July 2024.
[26] Fan, H., Chai, Y., Liu, C., Liu, W., Zhang, Z., Run, W., and Liu, D.Ev-stllm:
Electric vehicle charging forecasting based on spatio-temporal large language
models with multi-frequency and multi-scale information fusion.Expert Systems
with Applications 313(2026), 131620.
[27] Gan, L., Y an, C., W ang, T., and Zhang, W.Tfmr-rag: a knowledge base for
traffic facility management regulations.Transportmetrica A: Transport Science 0,
0 (2025), 1–29.
[28]Google. Gemini. https://gemini.google.com, 2026. Accessed: 2026-06-04.
[29] Grigorev, A., Saleh, K., Ou, Y., and Mihaita, A.-S.Enhancing traffic incident
management with large language models: A hybrid machine learning approach
for severity classification.International Journal of Intelligent Transportation
Systems Research 23(12 2024).
[30] Han, Q., Yoshikawa, A., and Y amamura, M.Adapting large language model for
spatio-temporal understanding in next point-of-interest prediction. InICASSP
2025 - 2025 IEEE International Conference on Acoustics, Speech and Signal Processing
(ICASSP)(2025), pp. 1–5.
[31] Hao, X., Zhang, Q., Xue, T., Bai, Y., and Y ang, A.Green transportation develop-
ment optimization based on g2-hgnn multiple traffic states.IEEE Transactions on
Intelligent Transportation Systems(2025), 1–14.
[32] Hassija, V., Majumder, T., Roy, D., Piyush, R., and Chamola, V.The role of
large language models (llms) in enhancing intelligent transportation systems: A
survey.Vehicular Communications 58(2026), 100996.
[33] He, J., Nie, T., and Ma, W.Geolocation representation from large language
models are generic enhancers for spatio-temporal learning.Proceedings of the
AAAI Conference on Artificial Intelligence 39, 16 (Apr. 2025), 17094–17104.
[34] Jin, Y., and Ma, J.A survey of large language models in transportation planning:
modelling, design and decision-making.Transportmetrica A: Transport Science
(2026), 1–46.
[35] Kalantari, S., W ang, Y., Sun, S., and W ang, X.Fleetwiz: An intelligent platform
for spatio-temporal multi-resource truckload fleet dispatching. InProceedings of
the 32nd ACM International Conference on Advances in Geographic Information
Systems(New York, NY, USA, 2024), SIGSPATIAL ’24, Association for Computing
Machinery, p. 665–668.
[36] Kalyuzhnaya, A., Mityagin, S., Lutsenko, E., Getmanov, A., Aksenkin, Y.,
Fatkhiev, K., Fedorin, K., Nikitin, N. O., Chichkova, N., Vorona, V., and
Boukhanovsky, A.Llm agents for smart city management: Enhancing decision
support through multi-agent ai systems.Smart Cities 8, 1 (2025).
[37] Kaur, S., Sehra, S. S., Ebrahimi, D., W ang, X., Singh, J., and Sehra, S. K.
Harnessing large language models for intelligent transportation systems: A
systematic review.Multimodal Transportation 5, 3 (2026), 100308.
[38] Kengne, D., Nkambou, R., Tato, A., and Lacourarie, C.Towards predicting
complex carpooling trajectories with context-augmented bert-llm in chaotic
environments. InAdvances and Trends in Artificial Intelligence. Theory and
Applications(Berlin, Heidelberg, 2025), Springer-Verlag, p. 419–431.
[39]Kumar, S. S., Cummings, M., and Stimpson, A.Strengthening llm trust bound-
aries: A survey of prompt injection attacks. In2024 IEEE 4th International Con-
ference on Human-Machine Systems (ICHMS)(2024), pp. 1–6.
[40] Li, S., Li, H., Li, X., Xu, Y., Lin, Z., and Jiang, H.Causal intervention is what
large language models need for spatio-temporal forecasting.IEEE Transactions
on Cybernetics 55(2025), 3825–3837.
[41] Li, Z., Xia, L., Tang, J., Xu, Y., Shi, L., Xia, L., Yin, D., and Huang, C.Urbangpt:
Spatio-temporal large language models. InProceedings of the 30th ACM SIGKDD
Conference on Knowledge Discovery and Data Mining(New York, NY, USA, 2024),
KDD ’24, Association for Computing Machinery, p. 5351–5362.
[42] Liu, C., Hettige, K. H., Xu, Q., Long, C., Xiang, S., Cong, G., Li, Z., and Zhao,
R.ST-LLM+: Graph Enhanced Spatio-Temporal Large Language Models for
Traffic Prediction .IEEE Transactions on Knowledge & Data Engineering 37, 08
(Aug. 2025), 4846–4859.
[43] Lou, S.Urban-mas: Human-centered urban prediction with llm-based multi
agent system. InProceedings of the 3rd ACM SIGSPATIAL International Workshop
on Advances in Urban-AI(New York, NY, USA, 2025), UrbanAI ’25, Association
for Computing Machinery, p. 37–40.
[44] Madi, R., Elayoubi, S.-E., do Lago, R. C., and Estanislau, V. O.Large language
models for spatio-temporal mobile traffic predictions. In2025 IEEE International
Mediterranean Conference on Communications and Networking (MeditCom)(2025),
pp. 1–6.
[45] Mahmud, D., Hajmohamed, H., Almentheri, S., Alqaydi, S., Aldhaheri, L.,
Khalil, R. A., and Saeed, N.Integrating llms with its: Recent advances, potentials,
challenges, and future directions.IEEE Transactions on Intelligent Transportation
Systems 26, 5 (2025), 5674–5709.
[46] Masri, S., Ashqar, H. I., and Elhenawy, M.Leveraging large language models
(llms) for traffic management at urban intersections.2025 Sixteenth International
Conference on Ubiquitous and Future Networks (ICUFN)(2024), 347–351.
[47]Meta. Meta ai. https://meta.ai, 2026. Accessed: 2026-06-04.
[48] Microsoft. Copilot. https://copilot.microsoft.com, 2026. Accessed: 2026-06-04.
[49] Midjourney Inc.Midjourney. https://www.midjourney.com, 2026. Accessed:
2026-06-04.
[50] Miskolczi, M., Földes, D., Munkácsy, A., and Jászberényi, M.Urban mobility
scenarios until the 2030s.Sustainable Cities and Society 72(2021), 103029.
[51] Muriuki, K. P., Okello, J. O., and Chepkoech, J.Advanced intelligent traffic
management system(aitms): A generative ai-enhanced model.2024 IEEE PES/IAS
PowerAfrica(2024), 1–3.
[52] National Institute of Standards and Technology. Ai risk management
framework. https://www.nist.gov/itl/ai-risk-management-framework, 2023. Ac-
cessed: 2026-06-04.
[53] Nie, T., Sun, J., and Ma, W.Exploring the roles of large language models in
reshaping transportation systems: A survey, framework, and roadmap.Artificial
Intelligence for Transportation 1(2025), 100003.
[54]OpenAI. Chatgpt. https://chat.openai.com, 2026. Accessed: 2026-06-04.
[55]OpenAI. Dall-e 3. https://openai.com/dall-e-3, 2026. Accessed: 2026-06-04.
[56] Pajola, L., and Conti, M.Lights Toward Adversarial Machine Learning: The
Achilles Heel of Artificial Intelligence .IEEE Intelligent Systems 39, 05 (Sept. 2024),
20–24.
[57] Pati, A. K.Agentic ai: a comprehensive survey of technologies, applications, and
societal implications.IEEE Access(2025).
[58] Perallos, A., Hernandez-Jayo, U., Onieva, E., and Zuazola, I. J. G.Intelligent
transport systems: technologies and applications. John Wiley & Sons, 2015.
[59] Perplexity AI. Perplexity ai. https://www.perplexity.ai, 2026. Accessed: 2026-
06-04.
[60] Pradhan, D., Arora, L., Shetgaonkar, A., Girija, S. S., Kapoor, S., and Raj, A.
Opportunities and applications of genai in smart cities: A user-centric survey.
In2025 IEEE International Conference on Omni-layer Intelligent Systems (COINS)
(2025), pp. 1–7.
[61] Santana-Mancilla, P. C., Guerrero-Ibáñez, A., Contreras-Castillo, J.,
García-Mancilla, J., and Anido-Rifón, L.Sustainable urban mobility: Lever-
aging generative ai for symmetry-aware traffic light optimization.Symmetry 17,
12 (2025).
[62] Shang, Y., Shang, W.-L., Cui, D., Liu, P., Chen, H., Zhang, D., Zhang, R., Xu, C.,
Liu, Y., W ang, C., and Alhazmi, M.Spatio-temporal data fusion framework based
on large language model for enhanced prediction of electric vehicle charging
demand in smart grid management.Inf. Fusion 126, PB (Feb. 2026).
[63] Singh, A., Ashraf, M., Rathore, R., Li, B., and Sujatha, M.Real-time traffic flow
optimization using large language models and reinforcement learning for smart
urban mobility.Applied Soft Computing 185(Sept. 2025). Publisher Copyright:©
2025 Elsevier B.V.
[64] Syum Gebre, T., Endale Ashebir, S., Blay, J., Anokye, M., Pandey, V., and
Hashemi-Beni, L.Real-time traffic insights with physics-informed neural net-
works: Integrating the aw-rascle model and llms.IEEE Access 13(2025), 181246–
181266.
[65] Tallam, K.Engineering risk-aware, security-by-design frameworks for assurance
of large-scale autonomous ai models. InProceedings of the Future Technologies
Conference(2025), Springer, pp. 209–227.
[66] United Nations Department of Economic and Social Affairs. World ur-
banization prospects 2025, 2025. Accessed: 2026-06-03.
[67] W ang, H., Li, Y., Zhao, W., Zhu, H., Zhang, J., and Wu, X.Gsf-llm: Graph-
enhanced spatio-temporal fusion-based large language model for traffic predic-
tion.Sensors 25, 21 (2025).
[68] W ang, J., W ang, Z., Lu, T., and Y an, C.Llm-augmented spatio-temporal graph
learning for poi recommendation. InAdvanced Data Mining and Applications
(Berlin, Heidelberg, 2025), Springer-Verlag, p. 444–451.
[69] Xu, Y., and Liu, M.Gpt4tfp: Spatio-temporal fusion large language model for
traffic flow prediction.Neurocomputing 625(2025), 129562.
[70] Yi, S., Liu, Y., Sun, Z., Cong, T., He, X., Song, J., Xu, K., and Li, Q.Jailbreak
attacks and defenses against large language models: A survey.arXiv preprint
arXiv:2407.04295(2024).
[71] Yu, C., Xie, X., Huang, Y., and Qiu, C.Harnessing llms for cross-city od flow
prediction. InProceedings of the 32nd ACM International Conference on Advances
in Geographic Information Systems(New York, NY, USA, 2024), SIGSPATIAL ’24,
Association for Computing Machinery, p. 384–395.
[72] Zhang, D., Zheng, H., Yue, W., and W ang, X.Advancing its applications with
llms: A survey on traffic management, transportation safety, and autonomous
driving. InRough Sets(Cham, 2024), M. Hu, C. Cornelis, Y. Zhang, P. Lingras,
D. Ślęzak, and J. Yao, Eds., Springer Nature Switzerland, pp. 295–309.
[73] Zhang, S., Fu, D., Liang, W., Zhang, Z., Yu, B., Cai, P., and Y ao, B.Trafficgpt:
Viewing, processing and interacting with traffic foundation models.Transport
Policy 150(2024), 95–105.
