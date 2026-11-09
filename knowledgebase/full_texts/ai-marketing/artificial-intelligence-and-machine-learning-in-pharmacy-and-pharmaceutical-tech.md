---
title: Artificial intelligence and Machine learning in pharmacy and pharmaceutical technology
url: https://doi.org/10.18231/j.jpbs.14270.1787994979
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: Journal of Pharmaceutical and Biological Sciences
authors:
- Shoheb Shakil Shaikh
source: openalex-oa
pdf_url: https://jpbs.in/archive/volume/14/issue/3/article/27737/pdf
pages: 7
chars: 43002
fetched_at: '2026-11-08T19:57:53+00:00'
kb_version: 1
---

# Artificial intelligence and Machine learning in pharmacy and pharmaceutical technology

Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112
Content available at: https://www.ipinnovative.com/open-access-journals
Journal of Pharmaceutical and Biological Sciences
Journal homepage: https://jpbs.in/
Review Article
Artificial intelligence and Machine learning in pharmacy and pharmaceutical
technology
Shoheb Shakil Shaikh1* iD
1Dept. of Quality Assurance, Dr. Babasaheb Ambedkar Technological University (DBATU), Lonere, Maharashtra, India
Abstract
Artificial intelligence (AI) and Machine learning (ML) are transforming the pharmaceutical lifecycle—from target identification and lead optimization to clinical
development, manufacturing, supply chain orchestration, and real-world pharmacovigilance. This review synthesizes recent advances (2018–2025) across core
methodological families (supervised, unsupervised, reinforcement, and deep learning) and maps them to high-impact use cases in pharmacy and pharmaceutical
technology. We systematically screen academic and industry literature using PRISMA guidelines, extracting evidence on model classes, datasets, performance
metrics, validation strategies, and regulatory considerations. Key progress includes foundation and multimodal models for de novo molecular design, active
learning for assay triage, graph neural networks and transformer architectures for property prediction and ADMET profiling, and digital twins and predictive
control for continuous manufacturing. In clinical and post-marketing contexts, federated learning enhances privacy-preserving trial analytics, while NLP models
accelerate signal detection in safety reports and EHRs. Despite clear gains in speed, cost, and decision quality, translation hurdles persist: data heterogeneity and
bias, limited external validity, explainability gaps in high-stakes decisions, GMP/21 CFR Part 11/GxP-aligned validation, and evolving regulatory expectations
for Software as a Medical Device and AI-as-a-Service. We outline best practices for reproducibility, model risk management, and human-AI governance, and
identify research frontiers in causal ML, uncertainty quantification, hybrid physics-ML models, and responsible deployment. The review provides a consolidated
roadmap for researchers, practitioners, and regulators to harness AI/ML for more efficient, safe, and equitable pharmaceutical innovation.
Keywords: ADMET prediction, Artificial intelligence, Drug discovery and development,
Received: 17-11-2025 Accepted: 29-08-2026 Available Online: 19-09-2026
This is an Open Access (OA) journal, and articles are distributed under the terms of the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License, which
allows others to remix, tweak, and build upon the work non-commercially, as long as appropriate credit is given and the new creations are licensed under the identical
terms.
For reprints contact: reprint@ipinnovative.com
1. Introduction
1.1. Background and significance of the topic
Programs like Logic Theorist, which were created to simulate
human thought processes, marked the beginning of artificial
intelligence in the 1950s. These early systems marked the start
of using computers to support decision-making in medication
design. ML algorithms started supporting molecular docking,
QSAR modeling, and toxicity prediction in the 1990s and
2000s. This made it easier for researchers to search through
enormous chemical libraries. Data Explosion Due to the
abundance of data made possible by new genomes, proteomics,
and imaging technologies, conventional methods were no
longer effective. To recognize and forecast patterns, AI/ML
become essential. The epidemic showed that AI works in the
real world by speeding up its use in remote monitoring, clinical
trials, and drug repurposing.
1.2. Rationale for conducting the review
Drug discovery, formulation design, clinical trials, and
regulatory procedures are all being transformed by AI and
ML in the pharmaceutical sciences. These days, data science,
bioinformatics, nanotechnology, and regulatory politics all
intersect with pharmacy. This review fosters interdisciplinary
understanding and collaboration among pharmacists, data
scientists, and physicians. Critical evaluation is necessary
for ethical concerns and regulatory complexities. In line
with sustainability and therapeutic precision, AI-assisted
modeling is supported by emerging trends including
solvent-free synthesis, personalized medication, and intelligent
nanocarriers.
1.3. Objective and Scope
Although AI has a lot of potential for improving medicine
delivery and drug discovery, it still has several significant
drawbacks that eventually necessitate human intervention or
the assistance of experts to decipher the intricate outcomes.
The datasets serve as the foundation for the majority of
AI forecasts; nevertheless, because of the gray area, human
intervention is necessary to interpret the results and arrive
at the right conclusion. When it comes to processing data
for predictions and evaluating hypotheses, AI may encounter
problems with algorithm bias. The purpose of this study
is to offer practical insights and suggestions for using AI to
develop a more technologically advanced and patient-centered
approach to pharmaceutical care.
2. Discussion
2.1. Historical and theoretical background
2.1.1. Evolution of the field and major milestones
Artificial intelligence was formalized with the Dartmouth
Conference in 1956. The pharmaceutical use of rule-based
expert systems such as MYCIN enabled medical diagnosis.
*Corresponding author: Shoheb Shakil Shaikh
Email: research.publication8891@gmail.com
https://doi.org/10.18231/j.jpbs.14270.1787994979
© 2026 The Author(s), Published by IP Innovative Publication Pvt. Ltd.
106

Shaikh / Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112 107
Drug metabolism and pharmacokinetic predictions were
enabled through statistical modeling. Machine learning
methods such as Random Forests and Support Vector
Machines were applied to QSAR modeling and virtual
screening to enable the prediction of bioactivity and toxicity.
Empirical methods were used to transform pharmacology and
medicine in the 17th century. Merck’s industrial production
of alkaloids in 1827 was a milestone in the industrial origin
of pharma. Beecham built England’s first factory dedicated
to medicines in 1859. 1 In 1876, Eli Lilly founded his
pharmaceutical company. The Pharmacy Council of India was
established in 1949, and Bengal Chemicals in 1901 became the
first pharmaceutical company in the country.2
2.1.2. Foundational theories and principles
2.1.2.1. Artificial Neural Network (ANN)
Machine learning (ML) plays a vital role in AI, and deep
learning utilizes Artificial Neural Networks (ANN). ANNs
are systems inspired by biology that learn from input data
directly, focusing mainly on information analysis. They
are divided into supervised learning (SL) and unsupervised
learning (UL). 3,4 SL entails obtaining direction throughout
the learning process, while SL serves as the leading and
most esteemed network for formulation purposes. Network
architecture, including multilayer perceptron (MLP) networks,
is employed to organize interconnected neurons within a neural
network.5
2.1.2.2. Fuzzy logic
Fuzzy logic, a tool of artificial intelligence, finds extensive
application in addressing problems. Here, ANN plays a role in
comprehending the processes of formulation and optimization.
The traditional sense is based on hypotheses that are either true
or false.6,7,8
2.1.2.3. Neuro-fuzzy logic
Neuro-fuzzy logic combines the learning capabilities of
artificial neural networks (ANNs) with the flexibility of fuzzy
logic, making it particularly suitable for data mining and
integrating learning capacity with fuzzy logic.9
2.1.2.4. Genetic algorithms
In the 1970s, John Holland introduced genetic algorithms
(GA), which are systems inspired by biology that mimic
evolutionary principles across generations. 10 GA offers
an optimization strategy via an iterative process, which
involves creating a starting population and assessing the fitness
of each member. The optimal solution is achieved by
developing potential solutions through an ANN and a genetic
algorithm, and then producing a new solution population via
crossover and mutation methods.11 It has been demonstrated by
researchers that an effective method for creating dosage forms
in pharmaceutical products is the combination of ANN and
GA.
2.1.3. Key terminology and definitions for clarity
Progress in AI and machine learning offers a transformative
opportunity for drug discovery, formulation, and testing of
pharmaceutical dosage forms. Researchers can discover
disease-related targets and forecast their relationships with
possible drug candidates by employing AI algorithms that
examine large biological datasets, such as genomics and
proteomics. Machine intelligence. According to Kaplan and
Haenlein (2019), it is characterized as a system’s capability to
accurately understand external data, derive lessons from that
data, and employ those lessons to accomplish particular aims
and assignments by means of flexible adjustment. According
to Esposito et al. (2017), this area of research enables
machines and computers to learn without the need for explicit
programming, is known as Machine Learning. 12
2.2. Current state of the art
2.2.1. Overview of existing technologies/approaches/models
2.2.1.1. Natural Language Processing [NLP]
One important way that intelligence manifests itself is through
language, which makes Artificial intelligence (AI) an exciting
area.13Applications such as sentiment analysis, automatic text
summarization, topic extraction, stemming, and machine
translation are made possible by the popular field of study
known as natural language processing (NLP), which uses
human language to analyze text. 14
2.2.1.2. Deep learning [DL]
To find tablet flaws, X-ray tomography and deep learning
are used. When employed to treat melanoma, a deep
learning system has demonstrated remarkable accuracy in
patient care and diagnostic support. 15 In order to properly
isolate the particles, the deep learning method is also utilized.
Bubble production, which is typically not dangerous to
patients, is one of the more significant problems related to
parenteral batch defects. However, it is crucial to distinguish
between particles and bubbles. Protein folding patterns
can be predicted by deep learning and molecular dynamics
simulations, which aid in the creation of stable and effective
biologics.16 AI can anticipate how proteins will fold based on
amino acid sequences and apply deep learning and molecular
dynamics modeling to gain a better understanding. Using
generative models and deep learning, scientists can develop
novel molecules with target-binding properties, increasing the
efficacy of medications and reducing side effects.17
2.2.2. Comparison of methodologies and techniques
Drug development, structural analysis, repurposing, and
disease prediction are all done with AI and ML techniques.
In order to anticipate new diseases or identify those who
are at risk, AI/ML models examine patient data, genetic
markers, and environmental factors.18 Designing vaccines and
antivirals is aided by Deep Learning (DL) approaches, which
use imaging and molecular data to comprehend viral structure.
In order to discover novel therapeutic applications for newly
developing illnesses, AI systems search databases of licensed
medications.
2.2.3. Success stories, case studies, or clinical translations
The usefulness of virtual screening in conjunction with
machine learning-based scoring functions in identifying
possible antiviral drug candidates is demonstrated by case
studies where AI-driven molecular docking speeds up lead
compound identification across multiple therapeutic areas,
especially in light of the COVID-19 pandemic.19 In conclusion,
these developments highlight how crucial AI and ML are

108 Shaikh / Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112
to transforming virtual screening and molecular docking,
increasing their effectiveness, precision, and influence in
logical drug design initiatives. Large pharmaceutical
corporations are using AI to detect failure mechanisms,
mitigate risk before commercialization, reduce development
times by up to 50%, identify stable drug candidates early, and
check quality in real-time under QbD frameworks.20
2.3. Mechanisms and underlying science
2.3.1. Biological, chemical, or physical mechanisms
AI and Machine learning (ML) are being used by the
pharmaceutical industry more frequently to optimize drug
development. Machine learning models complex biological
networks, integrates proteomics, metabolomics, and genomic
data, and constructs virtual patient models for personalized
medicine to aid in the discovery of biomarkers and treatment
targets.21 It also assists in predicting cytokine profiles and
immune responses. QSAR modeling, reaction prediction,
molecular docking and binding affinity, and toxicity and
ADMET profiling are additional methods that ML algorithms
use to understand chemical behavior. AI, on the other
hand, mimics physical processes such as rheological behavior
modeling, particle dynamics simulation, and process control
in manufacturing to aid in formulation and production
optimization.22 Physical principles are used to anticipate drug
release from matrices, patches, or nanoparticles, as well as
real-time monitoring of temperature, pressure, and mixing
rates in smart factories.
2.3.2. Molecular pathways, interactions, or system-level functions
With the modeling and deciphering of biological circuits,
Artificial intelligence (AI) and Machine learning (ML)
are revolutionizing drug development and the precision of
therapies.23 These encompass biosynthetic pathway mining,
metabolic route prediction, signal transduction modeling,
and gene regulatory networks. AI is able to predict the
interaction of molecules, for instance, how receptors and
ligands interact, how proteins engage, how drugs interact with
excipients, and how nanoparticles interact with cell surfaces.
Machine learning also facilitates system-level processes such
as formulation optimization, digital twin simulations, real-time
factory control, and systems pharmacology modeling. These
techniques enable scientists to learn more about how drugs
act, make them more effective, and create new drugs and
treatments.24
2.4. Applications and case studies
2.4.1. Pharmaceutical and biomedical applications
There are several important uses for AI and machine learning
in the biomedical and pharmaceutical industries. 25 AI has
applications in pharmaceuticals, including production, process
control, lead optimization, formulation design, drug discovery,
regulatory compliance, and personalized medicine. While
ML-based QSAR models can forecast biological activity,
toxicity, and ADMET profiles, generative AI may produce
new chemical compounds with specified characteristics. 26
AI-guided excipient selection enhances release patterns,
stability, and solubility. AI sensors can be used to
monitor manufacturing and process management, minimizing
downtime and guaranteeing batch uniformity. While
ML models identify irregularities in quality control data,
AI-driven documentation automates audit trails and regulatory
submissions. AI can be used in biomedical applications to
expedite the hiring process, forecast trial results, and facilitate
ongoing vitals and medication response monitoring.27
2.4.2. Clinical relevance and patient outcomes
AI/ML is essential to pharmacy because it enhances precision
dosing, predicts adverse drug reactions, and provides clinical
decision support systems. AI-enhanced CDSS helps physicians
and pharmacists choose the optimum therapies by providing
real-time notifications for drug interactions and dose errors.
Mobile apps and smart pill dispensers utilize Machine learning
(ML) to track and encourage compliance, while AI has
increased medication adherence monitoring in community
pharmacies by 40%. Furthermore, it is becoming more and
more usual to apply machine learning models to predict the
outcomes of patient care. Medical practitioners can adjust
treatment based on patient results by employing the method
of assessing individual risk profiles.28,29
The significant gains in patient outcomes, reduced
healthcare expenses, and improved resource allocation provide
compelling evidence for expanding the use of AI systems
to combat antibiotic resistance. The effectiveness of our
antibiotics depends more and more on these technologies
as they advance. This is particularly true for forecasting
the effectiveness of therapies and identifying novel resistance
patterns before they cause significant issues for patients. Since
referral accuracy helps patients get the proper healthcare
services in a timely way, it must be improved for patient
outcomes.30 Patients were more inclined to use pharmacy
services and their usage increased by 40% after the AI
triage system was implemented. In pharmaceutical supply
chain management, AI-driven methods can improve patient
outcomes and clinical judgment. By anticipating a treatment’s
effectiveness, identifying resistance tendencies before they
become clinical issues, and preserving the efficacy of our
medicinal supplies, it may be able to assist with drug
shortages.31
2.4.3. Industrial and translational applications
Smart manufacturing, supply chain optimization, formulation
automation, regulatory compliance, and translational
applications are just a few of the industrial uses for AI/ML
in pharmaceutical technology. AI sensors preserve batch
uniformity and save downtime by continuously monitoring
temperature, mixing rates, and viscosity. 32 ML models
are used in formulation automation to optimize release
kinetics, particle size distribution, and excipient ratio. AI
lowers waste, predicts demand, and restocks automatically.
Translational applications include tailored nanomedicine,
real-world evidence integration, patient classification and trial
design, and medication repurposing and lead optimization.
Customized therapy for diseases like RA and diabetic
retinopathy are made possible by the application of AI models
to forecast tissue distribution, receptor binding, and cytokine
suppression.33

Shaikh / Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112 109
3. Challenges and Limitations
3.1. Technical challenges in methodology and reproducibility
Despite the previously unheard-of possibilities presented by AI
and ML, there are drawbacks, including issues with scalability,
interpretability, and data quality. Data quality issues are
brought up by the dependence on big, diverse datasets since
AI-driven studies may become less accurate and reliable if the
data is noisy or lacking. Furthermore, it can be difficult for
doctors to comprehend and have faith in algorithmic outputs
due to the opacity of complicated machine learning models. 34
Pharmaceutical businesses must encourage the development of
interpretable machine learning frameworks and give priority
to data cleaning and validation procedures in order to lessen
these difficulties. Furthermore, it is essential to optimize
infrastructure and algorithms to increase scalability in order to
meet the growing demand for AI-driven solutions in healthcare
delivery and pharmaceutical research.35 The reproducibility of
ML-driven research has three primary goals:
1. Identifying the barriers to reproducibility when using
ML in research and classifying the barriers to various
types of reproducibility (description, code, data, and
experiment reproducibility).
2. Talking about potential drivers like tools, practices,
and interventions that support ML reproducibility and
differentiating between procedural, technology-driven,
and awareness and education-related drivers.
3. Mapping the drivers to the barriers. 36
3.2. Safety, ethical, and regulatory barriers
3.2.1. Patient privacy and data security
Healthcare machine learning models present serious privacy
and security issues since they employ vast amounts of
sensitive patient data. 37 Cybercriminals may target this
data, which could result in manipulation, insurance fraud,
and identity theft. Cloud-based AI models expose data
to external parties, and insider threats like hackers reveal
medical information. Additionally, inadequate anonymization
techniques may jeopardize patient data. Global data protection
laws may not be met by ML-driven healthcare apps, posing
regulatory issues.38 Although federated learning, a cooperative
strategy, can aid in safeguarding patient privacy, it has
difficulties preserving data integrity and thwarting hostile
attacks. Modern security mechanisms like multi-factor
authentication, strong encryption, and privacy-preserving
machine learning algorithms are used while adhering to
regulations to guarantee the privacy and security of patient
data.39
3.2.2. Fairness and Bias
Bias in Machine learning (ML) in the healthcare industry
can have discriminatory effects, disproportionately affecting
some groups and resulting in unequal access to care and
treatment. Due to the fact that certain models underdiagnose
Black individuals, historical clinical data may also be
biased. Furthermore, ML models that were trained on
unbalanced datasets would not generalize well across a range
of demographics. 40,41 The quality of care for vulnerable
groups may suffer as a result of algorithmic bias, which is
frequently created to put financial savings ahead of patient care.
Heterogeneous data collection, bias auditing, and regulatory
supervision are all necessary to mitigate bias in healthcare AI.
3.2.3. Transparency and explainability
It can be challenging for physicians to understand Deep
learning (DL) algorithms, also known as ”black boxes,”
which can impact the legitimacy, confidence, and rationale of
AI-assisted medical decisions. This lack of openness, which is
mandated by agencies such as the FDA, GDPR, and HIPAA,
may cause problems with regulatory compliance and impede
the clinical use of AI-based solutions. 42 Interpretable model
design techniques, explainable AI frameworks, and stringent
regulatory criteria can all be used to increase ML explainability
and guarantee transparency in AI systems.
3.3. Limitations in scalability, accessibility, and cost
Pharma data is often fragmented, limiting model
generalizability. Infrastructure demands high-performance
computing and storage for AI training. Model transferability
is limited, and regulatory bottlenecks hinder scalability across
borders. Low-resource regions lack access to AI-powered
tools, and AI systems often lack localization for diverse
patient populations. Clinical integration is limited, and
physical pharmacy closures can reduce access to AI-enabled
services.43,44
4. Emerging Trends and Future Perspectives
4.1. Novel technologies and interdisciplinary integrations
4.1.1. Generative Adversarial Networks (GANS)
A class of machine learning called Generative Adversarial
Networks (GANS) is made up of two neural networks—a
discriminator and a generator—that compete with one another
to learn. In the creation of pharmaceutical products, it is
widely used to create novel chemical structures and optimize
attributes.45 A discriminator network evaluates the quality of
the new molecules created by the generator network, which is
part of GANS. This results in the creation of structurally varied
and functionally optimized therapeutic candidates.46
4.1.2. Recurrent Neural Networks (RNNs)
RNNs are widely used in drug development tasks such as
peptide sequence design, genetic data analysis, and protein
structure prediction. In de novo synthesis, Recurrent Neural
Networks (RNNs) are used to interpret sequential data and
produce new chemical structures. SMILES (Simplified
Molecular Input Line Entry System) strings, a condensed and
understandable method of representing chemical structures,
are used to produce chemical structures. By examining
molecular structures it can aid in the search for new
drugs. Additionally, it can be used to predict medication
adherence.47,48
4.1.3. Convolutional Neural Networks (CNNs)
Neural networks with convolutions A class of deep learning
models called CNNs was created especially for applications
using grid-structured data, such pictures and movies.
Effectiveness is demonstrated in image-based tasks, such
as identifying medication targets and evaluating chemical

110 Shaikh / Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112
characteristics. It has been widely used in the medical sciences
for radiological pictures, which help with well-informed
decision-making and enable accurate disease diagnosis. These
networks are employed to predict receptor structural pictures,
produce precise protein structure predictions, develop medical
robotics, and contribute to genomics. It aids in target
identification as well.49,50
4.1.4. DQNs
Deep learning and reinforcement learning techniques, usually
convolutional neural networks (CNNs), are combined in DQNs
to predict the activity of chemicals and optimize drug discovery
procedures. It makes use of a target network. 51
4.2. Predicted trajectory of research and clinical translation
4.2.1. Hyper-personalized design
Hyper-personalized medicine is a digital tool that focuses on
treating inherited genetic disorders by creating novel drugs
tailored to the patient’s genes. This approach involves gene
replacement, editing, and antisense, which can repair the
patient’s DNA, enabling the design of appropriate regimens,
dose intake, and diets. Genome sequencing and CRISPR
engineering are two main methods used in hyper-personalized
medicine, making it affordable, fast, and applicable in various
hospital environments. While it cannot cure genetic mutations
yet, it can relieve pain and improve disease detection and
treatment.52 The toolkit helps healthcare practitioners stop
the unbearable symptoms of rare diseases and determine the
necessary drug quantity to stabilize the condition in the long
term. This innovation brings hope to hopeless patients and
contributes to the future of the healthcare sector. While ML
models will replicate drug-target interactions with previously
unheard-of accuracy, AI + Omics will allow real-time drug
molecule customization based on genomic, proteomic, and
metabolomic profiles.53
4.2.2. Digital twin technology
A model of an entity that includes all of its parts and
their dynamic interactions is called a digital twin. It entails
simulating the interactions between components.54 Over time,
the term ”digital twin” has changed; some now refer to a design
twin, while others utilize a hybrid model that makes decisions
in real time based on real-time data. These definitions are
beginning to be standardized by the industry. In order to
predict physiological and social tendencies and provide more
individualized treatments and interventions, digital twins are
being utilized in the healthcare industry more and more.
AI-created patient avatars will simulate how drugs work,
enabling more customized treatment regimens. especially
beneficial for long-term diseases with nonlinear progression,
including rheumatoid arthritis or diabetic retinopathy.55
5. Conclusion
5.1. Summary of key insight
Modifications to the Drug Discovery Process Drug
repurposing, lead optimization, and target discovery are
all accelerated by AI. Techniques like generative models,
molecular docking, and QSAR modeling reduce the time and
cost of R&D. Quickening Clinical Trials Machine learning
(ML) speeds up patient recruitment, predicts trial outcomes,
and enables real-time monitoring. Designing adaptive trials
reduces failure rates and boosts efficiency. Enhancing
Production and Supply Chains Predictive maintenance,
process control, and inventory optimization are made
possible by AI, which improves operational effectiveness.
Promoting Customized Medicine To customize patient care,
AI uses genomic data, biomarker detection, and diagnostics.
Increasing Adherence to Regulations AI-based auditing and
automated documentation allow for accurate and timely
regulatory compliance. An increase in pharmacovigilance
NLP and ML improve medication safety monitoring by
detecting adverse occurrences in social media and electronic
health data. Artificial intelligence, which effectively
contributes to pharmacovigilance, clinical decision assistance,
drug discovery, and customized Medicine is meant to take
advantage of the potential to improve patient outcomes, lower
costs, and speed up drug development procedures. Routine
pharmacy procedures like drug dispensing and inventory
management can be automated by AI to significantly lower
human error and improve workflows. However, implementing
AI in pharmacy presents a number of difficulties, including
those related to ethics, data protection, and regulatory
compliance. Since AI is still developing and active, the
pharmacy sector must also take advantage of its full potential
in order to advance the pharmaceutical industry and improve
patient care. The cooperation of AI-driven technologies will
influence the direction of pharmacy in the future.
6. Author Contribution
Shoheb Shakil Shaikh: Formal analysis.
7. Source of Funding
None.
8. Conflict of Interest
None.
References
1. Cova T, Vitorino C, Ferreira M, Nunes S, Rondon-Villarreal P, Pais
A. Artificial intelligence and quantum computing as the next pharma
disruptors. Methods Mol Biol . 2022;2390:321–47. h t t p s : / / d o i . o r g /
10.1007/978-1-0716-1787-8_14
2. Ejeta BM, Das MK, Das S, Bekere FF, Tayeng D. Transformative role
of artificial intelligence in the pharmaceutical sector. J Angiotherapy .
2024;8(9):1–7. https://doi.org/10.25163/angiotherapy.899933
3. Jariwala N, Putta CL, Gatade K, Umarji M, Rahman SNR, Pawde DM,
et al. Intriguing of pharmaceutical product development processes with
the help of artificial intelligence and deep/machine learning or artificial
neural network. J Drug Deliv Sci Technol . 2023;87:104751. h t t p s :
//doi.org/10.1016/j.jddst.2023.104751
4. Duriš J, Kurčubić I, Ibrić S. Review of machine learning algorithms’
application in pharmaceutical technology. Arh Farm. 2021;71(4):302–17.
https://doi.org/10.5937/arhfarm71-32499
5. Das S, Dey R, Nayak AK. Artificial intelligence in pharmacy. Indian J
Pharm Educ Res. 2021;55(2):304–18. https://doi.org/10.5530/ijper.55
.2.68
6. Kalaichelvan K, Ramalingam S, Dhandapani PB, Leiva V, Castro
C. Optimizing the economic order quantity using fuzzy theory and
machine learning applied to a pharmaceutical framework. Mathematics.
2024;12(6):819. https://doi.org/10.3390/math12060819

Shaikh / Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112 111
7. Çelik M. Use of artificial intelligence and expert systems in
pharmaceutical applications. In: Parikh DM, editor. Handbook of
pharmaceutical granulation technology. 4th ed. Boca Raton (FL): CRC
Press; 2021. p. 765–800. https://doi.org/10.1201/9780429320057-26
8. Ashaduzzaman M, Nawar NI, Khan SA, Biswas AA, Islam MM. Strategic
implementation of artificial intelligence and machine learning in the
pharmaceutical sector: a dual hesitant fuzzy group decision making
approach. In: Proceedings of the 7th IEOM Bangladesh International
Conference on Industrial Engineering and Operations Management; 2024;
Dhaka, Bangladesh. Dhaka: IEOM Society International; 2024. p.
1092–102. https://doi.org/10.46254/BA07.20240185
9. Amiri S, Larki E, Esmaile N, Mofavvaz S. The application of fuzzy
inference system and adaptive neuro-fuzzy inference system as artificial
intelligence methods for modeling and prediction of the ceftriaxone
removal percentage using nano zero-valent iron coupled with strontium
hexaferrite. Iran J Chem Chem Eng . 2024;43(3):971–82. h t t p s :
//doi.org/10.30492/ijcce.2023.2006936.6127
10. Vora LK, Gholap AD, Jetha K, Thakur RRS, Solanki HK, Chavda VP.
Artificial Intelligence in pharmaceutical technology and drug delivery
design. Pharmaceutics. 2023;15(7):1916. https://doi.org/10.3390/
pharmaceutics15071916
11. Dey H, Arya N, Mathur H, Chatterjee N, Jadon R. Exploring the role of
artificial intelligence and machine learning in pharmaceutical formulation
design. Int J Newgen Res Pharm Healthc . 2024;2(1):30–41. h t t p s :
//doi.org/10.61554/ijnrph.v2i1.2024.67
12. Allam H. Prescribing the future: the role of artificial intelligence in
pharmacy. Information. 2025;16(2):131. h t t p s : / / d o i . o r g / 1 0 . 3 3 9 0 /
info16020131
13. R N, Khan SB, Kumar AV, T R M, Alojail M, Sangwan SR, et al.
Enhancing drug discovery and patient care through advanced analytics
with the power of NLP and machine learning in pharmaceutical data
interpretation. SLAS Technol. 2025;31:100238. h t t p s : / / d o i . o r g / 1 0
.1016/j.slast.2024.100238
14. Viswanath S, Fennell JW, Balar K, Krishna P. An industrial approach
to using artificial intelligence and natural language processing for
accelerated document preparation in drug development. J Pharm Innov .
2021;16(2):302–16. https://doi.org/10.1007/s12247-020-09449-x
15. Gupta R, Srivastava D, Sahu M, Tiwari S, Ambasta RK, Kumar P.
Artificial intelligence to deep learning: machine intelligence approach for
drug discovery. Mol Divers. 2021;25(3):1315–60. https://doi.org/10.100
7/s11030-021-10217-3
16. Meng Y, Zhang Z, Zhou C, Tang X, Hu X, Tian G, et al. Protein structure
prediction via deep learning: an in-depth review. Front Pharmacol .
2025;16:1498662. https://doi.org/10.3389/fphar.2025.1498662
17. Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O, et
al. Highly accurate protein structure prediction with AlphaFold. Nature.
2021;596(7873):583–9. https://doi.org/10.1038/s41586-021-03819-2
18. Sarkar C, Das B, Rawat VS, Wahlang JB, Nongpiur A, Tiewsoh I, et
al. Artificial intelligence and machine learning technology driven modern
drug discovery and development. Int J Mol Sci . 2023;24(3):2026. https:
//doi.org/10.3390/ijms24032026
19. Bernstam EV, Shireman PK, Meric-Bernstam F, N Zozus M, Jiang X,
Brimhall BB, et al. Artificial intelligence in clinical and translational
science: Successes, challenges and opportunities. Clin Transl Sci .
2022;15(2):309–21. https://doi.org/10.1111/cts.13175
20. Simpson MD, Qasim HS. Clinical and operational applications of artificial
intelligence and machine learning in pharmacy: a narrative review of
real-world applications. Pharmacy. 2025;13(2):41. h t t p s : / / d o i . o r g /
10.3390/pharmacy13020041
21. Bhattamisra SK, Banerjee P, Gupta P, Mayuren J, Patra S, Candasamy
M. Artificial intelligence in pharmaceutical and healthcare research. Big
Data Cogn Comput. 2023;7(1):10. https://doi.org/10.3390/bdcc7010010
22. Karthikeyan A, Priyakumar UD. Artificial intelligence: machine learning
for chemical sciences. J Chem Sci (Bangalore). 2022;134(1):2. h t t p s :
//doi.org/10.1007/s12039-021-01995-2
23. Spanakis M, Tzamali E, Tzedakis G, Koumpouzi C, Pediaditis M,
Tsatsakis A, et al. Artificial intelligence models and tools for
the assessment of drug-herb interactions. Pharmaceuticals (Basel) .
2025;18(3):282. https://doi.org/10.3390/ph18030282
24. Abdelsayed M. AI-driven polypharmacology in small-molecule drug
discovery. Int J Mol Sci . 2025;26(14):6996. h t t p s : / / d o i . o r g / 1 0 . 3
390/ijms26146996
25. Thakur A, Mishra AP, Panda B, Rodríguez DCS, Gaurav I, Majhi B.
Application of Artificial intelligence in pharmaceutical and biomedical
studies. Curr Pharm Des . 2020;26(29):3569–78. https://doi.org/10.217
4/1381612826666200515131245
26. Selvaraj C, Chandra I, Singh SK. Artificial intelligence and machine
learning approaches for drug design: challenges and opportunities for the
pharmaceutical industries. Mol Divers. 2022;26(3):1893–913. h t t p s :
//doi.org/10.1007/s11030-021-10326-z
27. Jessica H, Britney R, Sarira ED, Parisa A, Joe Z, Betty BC. Applications
of artificial intelligence in current pharmacy practice: a scoping review.
Res Social Adm Pharm. 2025;21(3):134–41. https://doi.org/10.1016/j.sa
pharm.2024.12.007
28. Topol EJ. High-performance medicine: the convergence of human and
artificial intelligence. Nat Med. 2019;25(1):44–56. https://doi.org/10.1
038/s41591-018-0300-7
29. Alowais SA, Alghamdi SS, Alsuhebany N, Alqahtani T, Alshaya AI,
Almohareb SN, et al. Revolutionizing healthcare: the role of artificial
intelligence in clinical practice. BMC Med Educ. 2023;23(1):689. https:
//doi.org/10.1186/s12909-023-04698-z
30. Al Meslamani AZ. Applications of AI in pharmacy practice: a look
at hospital and community settings. J Med Econ . 2023;26(1):1081–4.
https://doi.org/10.1080/13696998.2023.2249758
31. Koromina M, Pandi MT, Patrinos GP. Rethinking drug repositioning and
development with artificial intelligence, machine learning, and Omics.
OMICS. 2019;23(11):539–48. https://doi.org/10.1089/omi.2019.0151
32. Rathore AS, Nikita S, Thakur G, Mishra S. Artificial intelligence
and machine learning applications in biopharmaceutical manufacturing.
Trends Biotechnol. 2023;41(4):497–510. https://doi.org/10.1016/j.tibtec
h.2022.08.007
33. Nagaprasad S, Padmaja DL, Qureshi Y, Bangare SL, Mishra M,
Mazumdar BD. Investigating the impact of machine learning in
pharmaceutical industry. J Pharm Res Int. 2021;33(46A):6–14. https:
//doi.org/10.9734/jpri/2021/v33i46A32834
34. Kolluri S, Lin J, Liu R, Zhang Y, Zhang W. Machine learning and
Artificial intelligence in pharmaceutical research and development: a
review. AAPS J. 2022;24(1):19. h t t p s : / / d o i . o r g / 1 0 . 1 2 0 8 / s 1 2 2 4 8
-021-00644-3
35. Al-Hourani S, Weraikat D. A systematic review of Artificial intelligence
(AI) and Machine learning (ML) in Pharmaceutical Supply Chain
(PSC) resilience: current trends and future directions. Sustainability.
2025;17(14):6591. https://doi.org/10.3390/su17146591
36. Kandhare P, Kurlekar M, Deshpande T, Pawar A. A review on
revolutionizing healthcare technologies with AI and ML applications in
pharmaceutical sciences. Drugs Drug Candidates . 2025;4(1):9. h t t p s :
//doi.org/10.3390/ddc4010009
37. Ogbuagu OO, Mbata AO, Balogun OD, Oladapo O, Ojo OO, Muonde
M. Artificial intelligence in clinical pharmacy: Enhancing drug safety,
adherence, and patient-centered care. Int J Multidiscip Res Growth Eval .
2023;4(1):814–22.
38. Roosan D, Wu Y, Tatla V, Li Y, Kugler A, Chok J, et al. Framework
to enable pharmacist access to health care data using Blockchain
technology and Artificial intelligence. J Am Pharm Assoc (2003) .
2022;62(4):1124–32. https://doi.org/10.1016/j.japh.2022.02.018
39. Khatal PA, Goukonde R, Sanap G. Artificial intelligence in pharmacy:
enhancing efficient data processing and healthcare solutions. World J
Pharm Res. 2025;14(1):1486–509. h t t p s : / / d o i . o r g / 1 0 . 2 0 9 5 9 / w j p
r20252-35110
40. Fletcher RR, Nakeshimana A, Olubeko O. Addressing fairness, bias, and
appropriate use of artificial intelligence and machine learning in global
health. Front Artif Intell. 2020;3:561802. https://doi.org/10.3389/frai.2
020.561802
41. Chen RJ, Wang JJ, Williamson DFK, Chen TY, Lipkova J, Lu MY, et al.

112 Shaikh / Journal of Pharmaceutical and Biological Sciences 2026;14(3):106-112
Algorithmic fairness in artificial intelligence for medicine and healthcare.
Nat Biomed Eng. 2023;7(6):719–42. https://doi.org/10.1038/s41551-0
23-01056-8
42. Curia F. Explainable and transparency machine learning approach to
predict diabetes develop. Health Technol. 2023;13(5):769–80. h t t p s :
//doi.org/10.1007/s12553-023-00781-z
43. Bettanti A, Beccari AR, Biccarino M. Exploring the future of
biopharmaceutical drug discovery: can advanced AI platforms overcome
current challenges? Discov Artif Intell. 2024;4:102. https://doi.org/10.1
007/s44163-024-00188-3
44. Agrahari V, Choonara YE, Mosharraf M, Patel SK, Zhang F. The role of
artificial intelligence and machine learning in accelerating the discovery
and development of nanomedicine. Pharm Res . 2024;41(12):2289–97.
https://doi.org/10.1007/s11095-024-03798-9
45. Paladugu PS, Ong J, Nelson N, Kamran SA, Waisberg E, Zaman N, et al.
Generative adversarial networks in medicine: important considerations
for this emerging innovation in artificial intelligence. Ann Biomed Eng .
2023;51(10):2130–42. https://doi.org/10.1007/s10439-023-03304-z
46. Canal-Alonso Á, Jiménez P, Egido N, Prieto Tejedor J, Corchado
Rodríguez JM. Revolutionizing pharmaceuticals: applications and
potential of generative artificial intelligence in drug discovery. Salamanca:
University of Salamanca; 2022. Available from: https://gredos.usal.es/h
andle/10366/153153
47. Teja TB, Sekar M, Pallavi T, Mettu S, Murthy TEG, Mat Rani NNI, et
al. Role of artificial neural networks in pharmaceutical sciences. J Young
Pharm. 2022;14(1):6–14. https://doi.org/10.5530/jyp.2022.14.2
48. Srivastava H, Leel M, Singh P, Rashmi R, Kumar A, Kumar S. The
recurrent neural networks: algorithm driven alchemy of machine learning
into precision therapeutics for today and tomorrow. In: Proceedings of
the 3rd International Conference on Optimization Techniques in the Field
of Engineering (ICOFE-2024); 2024 Nov 15. https://doi.org/10.2139/ss
rn.5091386
49. Yamashita R, Nishio M, Do RKG, Togashi K. Convolutional neural
networks: an overview and application in radiology. Insights Imaging .
2018;9(4):611–29. https://doi.org/10.1007/s13244-018-0639-9
50. Vaz JM, Balaji S. Convolutional neural networks (CNNs): concepts and
applications in pharmacogenomics. Mol Divers . 2021;25(3):1569-84.
https://doi.org/10.1007/s11030-021-10225-3
51. Raut U, Joshi S, Kumar A, Soni S, Behele S. AI-driven failure recovery
in pharma supply chains using deep Q-networks. 2025. https://doi.org/
10.2139/ssrn.5235947
52. Kashyap R, Jain A, Ahamad S, Soni AS, Behar N. Generative AI-driven
hyper personalized wearable healthcare devices: a new paradigm for
adaptive health monitoring. J Inf Technol Manag. 2025;17(Special Issue
on SI: Intelligent Security and Management):130–54. https://doi.org/10
.22059/jitm.2025.102925
53. Yaghmourian SG. The impact of AI-driven hyper-personalization on
online purchasing intention: the mediating role of privacy concerns
[master’s thesis]. Amman (Jordan): Princess Sumaya University for
Technology; 2024. Available from: h t t p s : / / w w w . p r o q u e s t . c o m / o
penview/15c41569cfa91982adcc5e865f521e6c/1?pq-origsite=gschola
r&amp;cbl=2026366&amp;diss=y
54. Davidopoulou C, Ouranidis A. Pharma 4.0-artificially intelligent digital
twins for solidified nanosuspensions. Pharmaceutics. 2022;14(10):2113.
https://doi.org/10.3390/pharmaceutics14102113
55. Mariam Z, Niazi SK, Magoola M. Unlocking the future of
drug development: generative AI, digital twins, and beyond.
BioMedInformatics. 2024;4(2):1441–56. h t t p s : / / d o i . o r g / 1 0 . 3
390/biomedinformatics4020079
Cite this article: Shaikh SS. Artificial intelligence and Machine
learning in pharmacy and pharmaceutical technology. J Pharm Biol Sci .
2026;14(3):106-112.
