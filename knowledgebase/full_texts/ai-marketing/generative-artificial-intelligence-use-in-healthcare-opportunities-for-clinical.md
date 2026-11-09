---
title: 'Generative Artificial Intelligence Use in Healthcare: Opportunities for Clinical Excellence and
  Administrative Efficiency'
url: https://doi.org/10.1007/s10916-024-02136-1
category: ai-marketing
subcategory: framework
date: 2025-01
venue: Journal of Medical Systems
authors:
- Soumitra S. Bhuyan
- Vidyoth Sateesh
- Naya Meenkashi Mukul
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s10916-024-02136-1.pdf
pages: 11
chars: 67153
fetched_at: '2026-11-08T17:02:51+00:00'
kb_version: 1
---

# Generative Artificial Intelligence Use in Healthcare: Opportunities for Clinical Excellence and Administrative Efficiency

RESEARCH
Journal of Medical Systems           (2025) 49:10
https://doi.org/10.1007/s10916-024-02136-1
Introduction
Artificial Intelligence (AI) is increasingly utilized across
various fields, including healthcare, where it has the poten -
tial to revolutionize clinical decision-making and enhance
operational efficiencies. A significant branch within AI,
Generative AI (Gen AI), has recently attracted attention for
its ability to create precise data through machine learning
algorithms, such as text, images, and music [ 1, 2, 5]. AI
has been defined as “a set of technologies that mimic the
functions and expressions of human intelligence, specifi -
cally cognition, logic, learning, adaptivity, and creativity”
[3]. Gen AI is characterized by its specialized capabilities
to produce new content, data, or solutions based on pat -
terns and information learned from existing datasets [ 4].
This capability arises from powerful foundation models that
utilize advanced machine learning and deep learning tech -
niques [6]. Foundation models are “large, complex models
trained on vast quantities of digital general information
that can later be adapted for more specific uses” [ 7]. These
  Soumitra S. Bhuyan
Soumitra.bhuyan@rutgers.edu
1 Edward J. Bloustein School of Planning and Public Policy,
Rutgers, The State University of New Jersey, 255, Civic
Square Building 33 Livingston Ave #400, New Brunswick,
NJ 08901, USA
2 School of Social Policy, Rice University, Houston, TX, USA
3 Biotechnology High School, Freehold, NJ, USA
4 Center for Health System Improvement, College of
Medicine, The University of Tennessee Health Science
Center, Memphis, TN, USA
5 University of Engineering & Technology, Peshawar, Pakistan
6 Department of Psychology and Counselling, St. Joseph’s
University, Bangalore, India
7 Insight Biopharma, Princeton, NJ, USA
Abstract
Generative Artificial Intelligence (Gen AI) has transformative potential in healthcare to enhance patient care, personal -
ize treatment options, train healthcare professionals, and advance medical research. This paper examines various clini -
cal and non-clinical applications of Gen AI. In clinical settings, Gen AI supports the creation of customized treatment
plans, generation of synthetic data, analysis of medical images, nursing workflow management, risk prediction, pandemic
preparedness, and population health management. By automating administrative tasks such as medical documentations,
Gen AI has the potential to reduce clinician burnout, freeing more time for direct patient care. Furthermore, application
of Gen AI may enhance surgical outcomes by providing real-time feedback and automation of certain tasks in operating
rooms. The generation of synthetic data opens new avenues for model training for diseases and simulation, enhancing
research capabilities and improving predictive accuracy. In non-clinical contexts, Gen AI improves medical education,
public relations, revenue cycle management, healthcare marketing etc. Its capacity for continuous learning and adaptation
enables it to drive ongoing improvements in clinical and operational efficiencies, making healthcare delivery more proac -
tive, predictive, and precise.
Keywords Generative AI · Artificial intelligence · Healthcare · Large language models · Clinical excellence · Ethics ·
Health information technology · AI applications · ChatGPT · Medicine
Received: 27 June 2024 / Accepted: 19 December 2024
© The Author(s) 2024
Generative Artificial Intelligence Use in Healthcare: Opportunities for
Clinical Excellence and Administrative Efficiency
Soumitra S. Bhuyan1 · Vidyoth Sateesh1 · Naya Mukul2 · Alay Galvankar3 · Asos Mahmood4 · Muhammad Nauman5 ·
Akash Rai1 · Kahuwa Bordoloi6 · Urmi Basu7 · Jim Samuel1
1 3

Journal of Medical Systems           (2025) 49:10
models feature two important characteristics: “emergence,”
the propensity to develop new and often unexpected capa -
bilities as they scale, and “homogenization,” the tendency
to serve as a common intelligence base for varied special -
ized functions and AI applications [ 7]. The generative pre-
trained transformer (GPT) model, particularly GPT-3 as a
large language model (LLM) and GPT-4 as a large multi-
modal model (LMM), exemplifies a foundation model
[11, 12]. Other essential AI methods, such as generative
adversarial networks (GANs) and variational autoencoders
(V AEs), also play a critical role.
GANs involve a pair of neural networks—the genera -
tor and the discriminator—that work against each other.
The generator strives to create data as realistically as pos -
sible. At the same time, the discriminator evaluates this data
against real-world examples, iterating until the generated
data is indistinguishable from actual data, at least to the dis-
criminator [ 9, 10]. According to the market research firm
Market.us, the global net value of Gen AI in healthcare was
approximately $800 million in 2022, with projections to
grow to $17.2 billion by 2032 [ 8]. The healthcare industry
has embraced AI-powered solutions, allocating substantial
funding to explore their practical benefits. A recent survey
from the Deloitte Center for Health Solutions reveals that
approximately 75% of large healthcare organizations are
currently using or planning to scale up generative AI in
their operations [ 13]. In 2023, Gen AI technologies made
substantial advancements, as evidenced by a recent study
in which ChatGPT surpassed physicians in both quality
and empathy metrics [14], and Google’s MedPaLM-2 LLM
achieved expert-level scores on the United States Medical
Licensing Examination [ 15]. Furthermore, the first drug
entirely designed with Gen AI entered clinical trials [ 15],
while new GPUs are expected to reduce LLM costs in 2024
[16].
The healthcare industry is grappling with numerous sys -
temic challenges, many of which have been intensified by
the COVID-19 pandemic, affecting both workforce stabil -
ity and patient care delivery. The pandemic has exacerbated
labor shortages in healthcare, making workforce challenges
a top concern for hospital CEOs [ 17]. The Association of
American Medical Colleges predicts a shortfall of 124,000
physicians by 2034 in the US [ 18]. The industry also faces
a shortage of 1.1 million nurses [ 19], resulting in longer
waiting times to see a clinician. In 2019, the average wait
time to see a physician was 26 days, with patients often
making numerous phone calls to schedule visits [ 13]. Pro-
vider burnout is another significant concern, with 81% of
the clinicians reporting high-stress levels primarily due to
increased workloads and administrative burdens [ 20]. Cli-
nicians have low trust in leadership, with fewer than 45%
trusting their organization’s leadership to prioritize patient
care [20]. Financially, the healthcare sector struggles with
rising operational costs, shrinking reimbursement rates, and
low profitability margins [ 21]. Despite increasing national
healthcare expenditures, US life expectancy has declined
recently, and healthcare accessibility remains a significant
issue, especially in underserved communities [ 13]. Gen AI
has the potential to address some of these challenges by
improving healthcare efficiency, reducing administrative
burdens, and enhancing patient care [ 22]. Given that Gen
AI is a relatively new technology, literature is scarce on its
clinical and non-clinical uses. This review article aims to
explore the potential applications of Gen AI for clinical and
non-clinical uses.
Clinical Applications
Tailored Treatment Plans
Generative AI has the potential to improve personalized
medicine by analyzing extensive health datasets and iden -
tifying patterns for tailored treatment plans, thereby signifi-
cantly enhancing patient outcomes. For instance, a research
study demonstrated that deep learning models can predict
cardiovascular risk factors from retinal images and pin -
point biomarkers for complex diseases, thus formulating
precise, personalized treatment plans [ 25]. Using GANs to
simulate virtual patient populations also helps predict treat-
ment outcomes across diverse demographic and genetic
backgrounds. Scientists have successfully utilized GANs
to generate synthetic patient data, facilitating the creation
of personalized treatment plans, especially for rare diseases
where data is scarce or non-existent [26].
The Generative Tensorial Reinforcement Learning
(GENTRL) model is particularly adept at designing drugs
tailored to specific biological mechanisms, ensuring that
drugs interact optimally with biological targets relevant to
an individual patient’s condition [ 27]. This level of speci -
ficity significantly supports the development of personal -
ized treatment plans. It also optimizes resources in genetic
testing by streamlining workflows and automating tasks,
making personalized medicine more accessible. Addition -
ally, Gen AI enhances pharmacogenomic optimization by
analyzing data to predict individual medication responses,
leading to customized prescriptions and improved treatment
outcomes [28]. Gen AI also processes wearable device data
in real-time to monitor vital health indicators, facilitating
early intervention and personalized treatment strategies
[23].
In mental health, Gen AI creates interactive tools for cog-
nitive behavioral therapy (CBT) [ 24]. The TP-GAN (treat -
ment planning with GAN) framework, a cGANs-based
1 3
   10  Page 2 of 11

Journal of Medical Systems           (2025) 49:10
model, represents a significant advancement in the automa-
tion of prostate brachytherapy planning. By reducing the
planning time and potentially the variability associated with
manual planning, this approach can lead to more standard -
ized treatment plans and improve overall treatment efficacy
[29]. AI algorithms also assist in diagnosing dental health
conditions such as caries and periodontal diseases through
image analysis and data interpretation, leading to timely
interventions, personalized treatment plans, and enhanced
treatment outcomes [ 30]. The implications of Gen AI for
personalized medicine are vast, as evidenced by recent
studies exploring its role in improving the diagnosis and
management of rare genetic disorders. These technologies
analyze large datasets for accurate classification and employ
facial recognition to aid in diagnosing genetic conditions
[31].
Surgical Care
Surgical teams are increasingly leveraging AI to enhance
surgical procedures. Before surgery, surgeons must syn -
thesize medical literature with comprehensive patient data,
including imaging, medical history, and relevant labora -
tory results, while adhering to the most recent treatment
guidelines and protocols [32]. Gen AI models can integrate,
analyze, and interpret these complex datasets, expediting
surgical decision-making and improving the timeliness of
treatment [ 33]. Since patients’ understanding of surgical
procedures is crucial, Gen AI can play a vital role in educat-
ing patients about surgical procedures and associated risks,
both pre- and post-surgery [ 34]. Additionally, Gen AI can
be used for quality assurance, to detect errors and suggest
new policies to improve patient care and ultimately improve
health outcomes [35].
A notable collaboration between Johnson & Johnson’s
MedTech unit and Nvidia has been established to enhance
surgical processes by integrating AI from pre- to post-opera-
tive stages. This initiative uses AI to analyze surgical videos
and automate the extensive documentation required after
surgery [36]. Other surgical applications include the intro -
duction of real-time AI annotation in urologic robotic sur -
geries to enhance surgical training and quality metrics. This
technology aims to automatically annotate surgical videos,
providing real-time feedback and support to surgeons and
trainees, thereby increasing the safety, efficiency, and edu -
cational value of surgical procedures [ 37]. AI also has the
potential to augment surgical decision-making through per-
sonalized risk assessments [38]. In recent years, minimally
invasive surgical techniques such as laparoscopic surgery
(LS) and robotic surgery (RS) have become increasingly
prevalent. The ultimate goal of RS development is the cre -
ation of fully autonomous AI-powered surgical instruments.
Although current systems require human supervision, their
success in procedures like prostatectomies (Da Vinci sys -
tem) and bowel suturing (STAR robot) showcases the
potential of AI in enhancing surgical outcomes [39].
Provider Burnout
Provider burnout is one of the major challenges for health -
care systems worldwide. The Association of American
Medical Colleges (AAMC) declared physician burnout a
public health crisis [ 40]. According to a 2019 study, more
than half of US physicians have experienced at least one
common burnout symptom, such as a reduced sense of per-
sonal accomplishment, emotional exhaustion, depersonali -
zation, and the inability to connect with family members.
As the same study reports, burnouts substantially negatively
impact the US economy, costing approximately $4.6 billion
annually [41]. Gen AI tools have shown promise in reducing
physician burnout and enhancing efficiency. Large language
models, such as generative pre-trained transformer 4 (GPT-
4; OpenAI), have shown the ability to draft empathetic
responses to online patient questions [42].
A recent study found that using GPT-4 to generate draft
replies to patient inbox messages improved mental task load
and work exhaustion, reducing burnout scores for medi -
cal professionals. However, no improvements in overall
response time were noted [ 42]. The study also showed that
gastroenterology and hepatology nurses had higher draft
utilization, a trend towards time saved, and positive net pro-
moter scores, suggesting that future Gen AI tools may vary
according to specific practice patterns and workflows [ 43].
These findings underscore the potential positive impact of
Gen AI in healthcare settings to enhance efficiency and
reduce burnout among physicians and other healthcare
professionals.
Another study found that lower satisfaction and higher
frustration with Electronic Health Records (EHRs) were
significantly associated with physician burnout [ 44]. Gen
AI has the potential to not only reduce the documentation
burden but also remove the computer from the physician-
patient interaction and bring the “care” back to healthcare
[45]. This allows the physician to assess the patient’s sit -
uation quickly while the AI summarizes and surfaces the
relevant data. Companies like Axtria are using Gen AI to
improve patient and physician care and advance core infor-
mation management capabilities such as master data and
multi-modal data [46].
Nursing
Gen AI demonstrates the potential to enhance patient care,
optimize workflows, and advance nursing education and
1 3
Page 3 of 11    10

Journal of Medical Systems           (2025) 49:10
and decision support systems, and enables researchers to
conduct large-scale studies and analyses without real patient
data [58]. Synthetic EHR and imaging data, developed using
GANs, aid research and enhance diagnostic algorithms
without compromising patient privacy [59].
A recent study describes how synthetic healthcare
records can be generated using convolutional GANs and
convolutional autoencoders (CorGAN). This architecture
captures correlations between adjacent medical features and
addresses the challenge of generating discrete data outputs
[60]. Synthetic data, when produced using techniques like
Gaussian Copulas (GC), Conditional Generative Adver -
sarial Networks (CGAN), V AEs, and Copula-GAN, can
supplement real datasets, enhancing the performance and
robustness of non-invasive diabetes prediction models [61].
While synthetic data generation is useful in medical tasks,
data is often scarce to train robust predictive models. For
instance, a 2023 study demonstrated that augmenting real
datasets with synthetic chest radiograph images generated
by latent diffusion models can improve classification per -
formance [62].
Additionally, another recent study showed that tailored
prompts provided to ChatGPT can produce task-specific
synthetic data, substantially improving performance in
tasks such as biological named entity recognition and rela -
tion extraction [63]. Synthetic data is invaluable for training
models and analysis and in scenarios where data is miss -
ing from healthcare databases, potentially skewing clini -
cal decisions [ 64]. MDClone, a startup in this field, offers
a platform that provides synthetic health data, eliminating
the need for direct access to patient records while ensuring
regulatory compliance [65].
Medical Image Analysis
Medical image analysis can be defined as the process of
examining medical images for diagnosis, improved treat -
ment planning, and disease monitoring. This analysis plays
a pivotal role in fields such as radiology, neurology, and
oncology, where examining large volumes of images and
data is crucial for extracting significant information [ 66].
Gen AI synthesizes, augments, and interprets heteroge -
neous complex images across various modalities, such as
X-rays, MRIs, and CT scans. AI models such as Generative
Adversarial Networks (GANs) and Variational Autoencod -
ers (V AEs), among several others, facilitate the synthesis
of anatomically precise images for training and education,
addressing the shortage of certain types of images and
the subtleties of ethical and privacy issues [ 67]. GANs
can synthesize MRI brain images specifically to enhance
the detection accuracy of neurological disorders using
training. AI-enhanced simulations are increasingly inte -
grated into nursing education, utilizing AI technologies to
create realistic scenarios that replicate complex medical
situations. This enables nursing students to acquire practical
skills in a controlled environment, mitigating the risks asso-
ciated with real-world scenarios. A recent review under -
scores the potential of AI in medical education, highlighting
its ability to tailor learning experiences and refine clinical
decision-making skills for healthcare professionals [ 47].
Other applications of AI systems include predicting patient
fall risks, generating personalized treatment plans, and auto-
mating routine tasks such as medical documentation, allow-
ing nurses more time for direct patient care [48].
AI-powered tools like voice-to-text transcription, auto -
mated charting, and intelligent data entry could reduce the
time spent on documentation by 21–30%, saving nurses
95–134 h per year. Streamlining administrative processes
like patient admissions, transfers, and discharges with AI
could save nurses 37–46% of the time spent on these tasks,
equating to 32–40 h per year [48]. This workflow optimiza-
tion ensures efficient utilization of human resources, alle -
viating the burden on overburdened staff and potentially
enhancing job satisfaction and retention [49].
Studies have revealed that AI chatbots can provide social
support to patients, serving as a practical and accessible
means of improving patient well-being, particularly in situ-
ations where traditional interventions are limited, such as
during pandemics [ 50]. A recent study explores the trans -
formative potential of Gen AI in nursing practices in Tai -
wan, focusing on the capabilities of the A + Nurse system, a
digital assistant designed to automate routine nursing tasks,
enhance communication within healthcare teams, and inte -
grate current medical information into nursing workflows
[51]. Prompt engineering is critical to effectively interact
with AI, as precise prompts yield desired outputs [52]. Edu-
cators can leverage Gen AI-based models like ChatGPT to
enrich teaching and learning experiences, including creating
virtual simulation scenarios, developing lesson plans, and
designing assessments [53].
Synthetic Data Generation
Synthetic data, as defined by the Royal Society and The
Alan Turing Institute, is data that has been generated using a
purpose-built mathematical model or algorithm to address a
data science task [54]. GANs and V AEs, among other tech-
nologies, can be used to generate synthetic data that safely
replaces sensitive patient information while complying
with strict privacy regulations such as GDPR and HIPAA
[55–57]. Generated through generative models, synthetic
data has numerous applications, including AI model train -
ing, validation, realistic simulations for medical training,
1 3
   10  Page 4 of 11

Journal of Medical Systems           (2025) 49:10
example, AI algorithms can analyze individual health data
alongside socioeconomic factors to predict which popula -
tions are mostly at risk for certain diseases, allowing for tar-
geted interventions and resources. In addition, IoT devices
like wearable fitness trackers can provide continuous health
monitoring for individuals in remote areas, enabling health-
care providers to remotely monitor and treat patients during
emergencies such as disease outbreaks [78].
Gen AI can streamline service delivery and operations for
public health and community health workers by reducing
administrative burdens, optimizing supply chain processes,
and fostering tailored interactions with diverse communi -
ties [79]. AI models excel at analyzing extensive and varied
datasets to forecast outcomes like hospital readmissions and
recommend proactive measures for patient well-being [80].
Further, by categorizing populations based on risk factors,
AI models enhance the effectiveness of interventions by
targeting high-risk groups. In addition, AI can help predict
the population’s health needs, optimizing resource alloca -
tion. Health Catalyst and ClosedLoop.ai also focus on using
the potential of AI for predictive analytics and population
health management, thereby personalizing individual care
plans for members [81]. As Gen AI continues to evolve, it is
poised to pioneer a new population health era by harnessing
a wide range of data sources, including real-time health data
from wearable technology, to deliver increasingly precise
interventions and drive enhanced health outcomes for entire
populations.
Risk Prediction of Pandemic Preparedness
The outbreak of the COVID-19 pandemic, coupled with
rapid advancements in AI and ML algorithms, has paved the
way for significant investments and developments in AI and
ML for pandemic management and surveillance [ 82, 83].
Examples of AI use during the pandemic include disease
forecasting, enhancing outbreak detection, and monitoring
disease progression [ 84]. Gen AI processes real-time data
from diverse sources, including social media, health reports,
and environmental data, to identify early signs of emerging
infectious diseases. Detecting unusual patterns or clusters
can contribute to early warning systems [ 85]. AI has also
supported public health initiatives through public policy
efforts [86].
Additionally, socioeconomic factors have been mod -
eled to gain improved insights into pandemic management
[87]. A recent application of AI during the COVID-19 pan-
demic, spanning from 2020 to as recent as 2023, involves
NERVTAG, a UK Government Advisory Group. They
developed the QCOVID3 risk prediction algorithm to
anticipate potential hospitalizations and deaths among
those infected with COVID-19. Since this algorithm was
machine-learning models without violating patient privacy
regulations [67].
Furthermore, studies have shown that GANs can be used
for data augmentation in liver lesion detection, where syn -
thetic images improve the diagnostic accuracy of the convo-
lutional neural networks (CNNs) that utilize these images
[68]. The CGAN model, enhanced with a 3D discriminator
and adaptive identity loss, significantly improves synthetic
MRI generation, especially in studying Alzheimer’s dis -
ease progression. This addresses the limitations of previous
models that primarily operate in 2D and suffer from spatial
artifacts [69]. Gen AI is also highly effective for anomaly
detection and segmentation, which are crucial for early dis-
ease detection and intervention. For instance, developing
the AnoGAN model for segmenting anomalies in retinal
images aids in early diabetic retinopathy diagnosis [71].
A study investigating the use of GAN to segment MRI
images of the brain showed that the GAN technique outper-
formed traditional methods, achieving an average Dice coef-
ficient of 0.89 [70]. Another study utilizing GAN to generate
synthetic images of the retina found that these images were
as effective as real images in training deep-learning mod -
els for diabetic retinopathy detection [ 71]. GANs are also
employed in image enhancement and reconstruction, such
as enhancing low-dose CT images to promote safer imag -
ing practices with reduced radiation exposure [ 72]. Gen AI
has the potential to not only reduce healthcare disparities
through improved diagnostic accuracy but also to usher in
a new era of personalized medicine, where patient-specific
models will aid in surgical planning and make treatments
more individualized [73].
Population Health Management
Gen AI can play a crucial role in predicting health trends,
personalizing medicine, and optimizing healthcare services
by analyzing vast datasets and tailoring health interventions
to meet service demands. A promising application of deep
learning is to interpret biological data and make predictions
of disease within populations, such as using neural networks
to analyze genetic information for early disease detection.
AI considerably brings value-based care for individual
patients into practice by personalizing treatment plans and
improving patient outcomes, contributing to improved pop-
ulation health [74, 75].
By Integrating individual-level health data with socio-
markers(quantifiable social conditions)— AI enhances dis -
ease surveillance and predicts health risks more accurately
[76]. Using mobile technologies and the Internet of Things
(IoT) allows for real-time health monitoring. It enhances
the ability of health systems to deliver care remotely, which
is crucial during events like the Ebola outbreak [ 77]. For
1 3
Page 5 of 11    10

Journal of Medical Systems           (2025) 49:10
in medical education is its potential to improve machine
translation, fostering knowledge exchange and global col -
laboration. The advent of Gen AI technology has enhanced
the accuracy and sophistication of machine translation. For
instance, eBay’s Machine Translation service demonstrates
a 7% increase in translation accuracy over its previous itera-
tions, highlighting the potential of AI to overcome language
barriers [93].
Additionally, Gen AI models have been utilized in medi-
cal education and surgical training to create dynamic, inter-
active models of patient anatomy, allowing students to gain
theoretical and practical experience without relying on real
patients [94]. Large Language Models (LLMs) are invalu -
able in medical research, literature review, and writing
because they can quickly extract accurate data with appro -
priate usage of terminologies and language [ 95]. LLMs
like GPT-4 can provide personalized learning experiences
through adaptive educational content tailored to learners’
needs. The increase in dermatological datasets with synthetic
images has improved the accuracy of AI model classifica -
tions of skin diseases, making them effective and valuable
tools in medical education [96]. Gen AI has the potential to
personalize education by adapting content according to stu-
dents’ performance and preferences, showcasing AI’s abil -
ity to cater to diverse learning needs [97]. Western Michigan
University has enhanced its medical curriculum with over
100 h of simulation training, providing realistic patient sce-
narios and feedback from professors to prepare students for
real-world medical situations [ 23]. As Gen AI technology
continues to evolve, its application in medical education is
expected to facilitate more advanced simulations and per -
sonalized learning pathways, preparing professionals for the
dynamically changing field of medicine.
Revenue Cycle Management
Gen AI integrated with Health Revenue Cycle Management
(RCM) automates and enhances various sectors in health -
care financial operations, including automated data entry,
patient communication, documentation of lab procedures,
compliance, procurement, contracting, and fraud detection
[98]. Utilizing AI for patient scrutiny and treatment records
facilitates the automatic generation of accurate billing codes
with fewer errors, ensuring compliance with frequently
changing regulations [ 99]. Moreover, Gen AI can predict
personalized patient communication strategies, offer predic-
tive analytics for financial planning, and provide insights
into preventive measures to reduce claim denials. Automat-
ing administrative tasks like coding and billing significantly
reduces the workload for healthcare staff, allowing them to
focus more on patient care [ 100]. Leveraging AI-generated
insights to identify and address the root causes of claim
implemented in Wales, UK, and its results were based on
that area’s demographics, it can only be considered success-
ful within that region [ 88]. Similarly, the Australian gov -
ernment developed a COVID-19 Pandemic Vulnerability
Index (CPVI) to assess vulnerability across different areas
in Australia, thereby helping to delay the pandemic’s expo-
nential growth and mitigate its impact on communities and
the healthcare system. This widespread experiment cov -
ered 563 zones, each with an average population of 45,000,
encompassing the entire country. Australia’s CPVI evaluates
vulnerability across four subsections: socio-demographics,
medical conditions, public works, and land use patterns. By
analyzing these factors, the index provides a more robust
understanding of areas at risk during a pandemic [89]. Both
NERVTAG’s algorithm and Australia’s CPVI have been
successful in their respective regions. However, both relied
on ample data and specific factors differentiating them from
other COVID-19 tools. Researchers have also explored
whether solely comorbidity data, socioeconomic status, age
and race could predict COVID-19 death rates.
To determine how these factors relate to hospitalization,
ICU admission, ventilator use, and mortality, researchers
analyzed a dataset of 1.4 million diagnosed COVID-19
cases [ 90]. During the QCOVID3 risk prediction experi -
ments, scientists found that the predictions closely matched
actual numbers for deaths and admissions up to the fif -
teenth predicted risk level, beyond which the predictions for
deaths were higher and lower for admissions [ 88]. In the
CPVI experiment, the index indicated that vulnerability to
COVID-19 is highest in more populated areas, whereas it
is much lower in rural areas [ 89]. However, graphs based
solely on comorbidity proved insignificant, as the comor -
bidity-predicted death rates were far from actual outcomes
in the experiment in the US and other selected countries.
Non-Clinical Applications
Medical Education and Training
Gen AI has the potential to enhance medical education by
producing realistic medical images and simulating patient
interactions. [91] It allows students to explore a variety of
medical conditions, including rare diseases and complex
clinical cases, through detailed images. Advanced frame -
works such as Generative Adversarial Networks (GANs)
and Variational Autoencoders (V AEs) facilitate synthesiz-
ing these educational tools, thereby expanding the range
of learning materials available to students. GANs, for
example, can generate synthetic medical images for educa -
tional purposes, enriching the pool of diverse and essential
learning materials [ 92]. Another critical benefit of Gen AI
1 3
   10  Page 6 of 11

Journal of Medical Systems           (2025) 49:10
Conclusion
This paper has explored the diverse impacts of Gen AI in
both clinical and non-clinical healthcare domains. Applica -
tions such as personalized treatment plans, medical image
analysis, and synthetic data generation have demonstrated
the transformative capabilities of Gen AI in enhancing diag-
nostic accuracy, streamlining operations, and facilitating
personalized medicine. Furthermore, integrating Gen AI in
medical education, healthcare marketing, and revenue cycle
management illustrates its potential to revolutionize learn -
ing experiences, optimize financial operations, and enhance
patient engagement strategies. It is also critical to recognize
the potential to augment and improve the performance of
human experts in healthcare using personal adaptivity with
generative AI. To ensure the continued advancement of Gen
AI in healthcare, it is imperative to establish robust ethi -
cal guidelines and governance frameworks that address data
privacy, algorithmic bias, transparency, and accountability.
By promoting and strengthening a collaborative environ -
ment among researchers, clinicians, policymakers and pri -
oritizing ethical considerations, Gen AI can continue to be a
significant force for innovation and improvement in health-
care services worldwide.
Author Contributions S.S.B., and V .S. wrote the main manuscript text
with inputs and feedbacks from N.M, A.G., A.M., M.N.,A.R., K.B.,
U.B., J.S. All authors reviewed and approved the final version of the
manuscript.
Funding There was no funding obtained to conduct this research.
Data Availability No datasets were generated or analysed during the
current study.
Declarations
Ethics Approval and Consent to Participate  Not Applicable for the
study.
Competing Interests The authors declare no competing interests.
Open Access   This article is licensed under a Creative Commons
Attribution 4.0 International License, which permits use, sharing,
adaptation, distribution and reproduction in any medium or format,
as long as you give appropriate credit to the original author(s) and the
source, provide a link to the Creative Commons licence, and indicate
if changes were made. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless
indicated otherwise in a credit line to the material. If material is not
included in the article’s Creative Commons licence and your intended
use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright
holder. To view a copy of this licence, visit  h t t  p : / /  c r e  a t i  v e c o m m o n s . o
r g / l i c e n s e s / b y / 4 . 0 /     .
denials can lead to more efficient and accurate RCM pro -
cesses [101].
According to a study by the Deloitte Center for Health
Solutions, Gen AI can save between 41% and 50% of the
time spent by revenue cycle professionals across all revenue
cycle stages, including patient access, clinical revenue cycle,
and patient financial services [48]. For example, Codametrix
and Adonis.io exemplify the application of advanced tech -
nologies in healthcare RCM. Codametrix Inc. uses Natural
Language Processing (NLP) to extract data from unstruc -
tured medical texts. It transforms it into structured data for
medical language interpretation, thus facilitating analysis,
billing, and population health management [ 102]. Adonis.
io integrates revenue intelligence and automation through -
out the process, enhancing efficiency and effectiveness in
healthcare RCM [103].
Healthcare Marketing and Public Relations
Gen AI can assist healthcare organizations with marketing
and public relations (PR) by personalizing content, automat-
ing customer support, and identifying areas for optimization
in marketing campaigns [104]. By analyzing large datasets,
Gen AI can create customized content, such as health tips
and articles, that promote engagement between patients and
healthcare providers [105]. It enhances personalized patient
service by fine-tuning responses based on individual needs,
supporting live agents, and providing real-time feedback,
leading to higher customer satisfaction, faster issue reso -
lution, and lower costs. Additionally, Gen AI can optimize
supply chains by predicting disruptions, enabling scenario
analysis, and assisting in supplier evaluations, allowing
quicker adaptation to market changes and improved opera -
tional efficiency [ 13]. Evidence indicates that one-third of
individuals in the United States first search online for health
information before seeking professional medical advice
[106].
Research shows a rising trend in individuals investigat -
ing mental health symptoms online, with mental health
queries increasing significantly [ 107]. The development of
digital mental health tools, such as AI-driven chatbots,  has
escalated to meet this growing demand. This highlights the
critical importance of enhanced emotional intelligence in
general AI systems, especially in providing empathetic and
personalized user interactions. Generative AI revolutionizes
strategic content analysis in marketing by identifying high-
performing content types and messaging strategies [ 108].
The integrative Gen AI-equipped tools add competitive
advantages to health organizations in patient engagements
and public interactions, underlining its transformational
potential for health marketing and PR [109].
1 3
Page 7 of 11    10

Journal of Medical Systems           (2025) 49:10
18. AAMC Report Reinforces Mounting Physician Shortage. AAMC;
2023. Available from:  h t t  p s : /  / w w  w . a  a m c  . o r  g / n e  w s  / p r  e s s -  r e l  e a s  e s
/ a a m c - r e p o r t - r e i n f o r c e s - m o u n t i n g - p h y s i c i a n - s h o r t a g e     . Accessed
May 31, 2024.
19. Where are all the nurses? Hospitals, advocates disagree on crisis.
Healthcare Dive. Available from:  h t t  p s : /  / w w  w . h  e a l  t h c  a r e d  i v  e . c  o
m / n  e w s  / w h  e r e - a r e - a l l - t h e - n u r s e s - h o s p i t a l s - a d v o c a t e s - d i s a g r e e - o
n - c r i s i s / 6 9 7 8 7 9 /     . Accessed May 31, 2024.
20. Addressing health care’s talent emergency. Deloitte Insights.
Available from:  h t t  p s : /  / w w  w 2 .  d e l  o i t  t e . c  o m  / u s  / e n /  i n s  i g h  t s /  i n d  u s
t r  y /  h e a  l t h -  c a r  e / h  e a l t h c a r e - w o r k f o r c e - s h o r t a g e - s o l u t i o n s . h t m l ? i d
= u s : 2     e l : 3 d p : w s j s p o n : a w a : W S J C M O : 2 0 2 4 : W S J F Y 2 4 . Accessed
May 31, 2024.
21. American Hospital Association. (n.d.). The costs of caring. Avail-
able from: https:/ /www.ah a.org/c ostso fcaring Accessed May 31,
2024
22. TestingXperts. (n.d.). Generative AI in healthcare. Available
from:  h t t  p s : /  / w w  w . t  e s t  i n g  x p e r  t s  . c o m / b l o g / g e n e r a t i v e - a i - i n - h e a l t
h c a r e /     Accessed May 31, 2024
23. Generative AI in Healthcare. N-iX. Available from:  h t t  p s : /  / w w  w .
n  - i x . c o m / g e n e r a t i v e - a i - i n - h e a l t h c a r e /     . Accessed May 31, 2024.
24. Reddy S. Generative AI in healthcare: an implementation science
informed translational path on application, integration and gover-
nance. Implement Sci. 2024;19:27.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 1 8 6 / s 1
3 0 1 2 - 0 2 4 - 0 1 3 5 7 - 9     .
25. Poplin R, Varadarajan A V , Blumer K, et al. Prediction of cardio-
vascular risk factors from retinal fundus photographs via deep
learning. Nat Biomed Eng. 2018;2(3):158–164.  d o i :    h t t p  s : /  / d o  i . o
r g / 1 0 . 1 0 3 8 / s 4 1 5 5 1 - 0 1 8 - 0 1 9 5 - 0     .
26. Yoon J, Jordon J, Schaar M. RadialGAN: Leveraging multiple
datasets to improve target-specific predictive models using Gen -
erative Adversarial Networks. Presented at: International Confer-
ence on Machine Learning; July 2018; pp. 5699–5707. PMLR.
27. Zhavoronkov A, Ivanenkov YA, Aliper A, et al. Deep learning
enables rapid identification of potent DDR1 kinase inhibitors. Nat
Biotechnol. 2019;37(9):1038–1040.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0 3 8 / s
4 1 5 8 7 - 0 1 9 - 0 2 2 4 - x     .
28. MedCity News. (2024). Revolutionizing primary care: The role
of pharmacogenomics and AI in personalized medicine. Available
from:  h t t  p s : /  / m e  d c i  t y n  e w s  . c o m  / 2  0 2 4  / 0 4 /  r e v  o l u  t i o  n i z  i n g -  p r  i m a r y
- c a r e - t h e - r o l e - o f - p h a r m a c o g e n o m i c s - a n d - a i - i n - p e r s o n a l i z e d - m e
d i c i n e /     . Accessed May 31, 2024
29. Aleef TA, Spadinger IT, Peacock MD, Salcudean SE, Mahdavi
SS. Rapid treatment planning for low-dose-rate prostate brachy -
therapy with TP-GAN. Presented at: International Conference on
Medical Image Computing and Computer-Assisted Intervention;
September 2021; Cham: Springer International Publishing; pp.
581–590. doi:https:/ /doi.or g/10.10 07/97 8-3-030-87202-1_56.
30. Dhopte A, Bagde H. Smart smile: revolutionizing dentistry with
artificial intelligence. Cureus. 2023;15(6).  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 .
7 7 5 9 / c u r e u s . 4 1 2 2 7     .
31. Abdallah S, Sharifa M, Almadhoun MKIK, et al. The impact of
artificial intelligence on optimizing diagnosis and treatment plans
for rare genetic disorders. Cureus. 2023;15(10).  d o i :    h t t p  s : /  / d o  i . o r
g / 1 0 . 7 7 5 9 / c u r e u s . 4 6 8 6 0     .
32. Baldwin PJ, Paisley AM, Brown SP. Consultant surgeons’ opin -
ion of the skills required of basic surgical trainees. Br J Surg.
1999;86:1078–1082.
33. Rodler S, Ganjavi C, De Backer P, et al. Generative artificial
intelligence in surgery. Surgery. 2024.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0 1 6
/ j . s u r g . 2 0 2 4 . 0 2 . 0 1 9     .
34. Martin LA, Finlayson SRG, Brooke BS. Patient preparation for
transitions of surgical care: is failing to prepare surgical patients
preparing them to fail? World J Surg. 2017;41:1447–1453.
35. Ali SR, Dobbs TD, Jovic M, et al. Validating a novel natural lan-
guage processing pathway for automated quality assurance in
References
1. Generative AI use cases | Google Cloud. Available from:  h t t  p s : /  /
c l  o u d  . g o o g l e . c o m / u s e - c a s e s / g e n e r a t i v e - a i ? h l = e n     . Accessed May
31, 2024.
2. AI future of healthcare. Available from:  h t t  p s : /  / w w  w . a  s i a  n h h  m . c o
m /  i n f o r m a t i o n - t e c h n o l o g y / a i - f u t u r e - o f - h e a l t h c a r e     Accessed May
31, 2024.
3. Samuel J. A Call for Proactive Policies for Informatics and Artifi-
cial Intelligence Technologies. Scholars Strategy Network; 2021.
Available from:  h t t  p s : /  / s c  h o l  a r s  . o r  g / c o  n t  r i b u t i o n / c a l l - p r o a c t i v e - p
o l i c i e s - i n f o r m a t i c s - a n d     . Accessed May 31, 2024.
4. What is Generative AI? | AWS Amazon. Available from:  h t t  p s : /  / a
w  s . a  m a z o n . c o m / w h a t - i s / g e n e r a t i v e - a i /     .
5. Generative AI vs. Traditional AI: Understand Key Differences. |
Medium. Available from:  h t t  p s : /  / m e  d i u  m . c  o m /  @ b y a  n a  l y t  i x l a  b s /
g e n  e r a t i v e - a i - v s - t r a d i t i o n a l - a i - u n d e r s t a n d - k e y - d i ff  e r e n c e s - c a 2 d 3
e 3 7 c 4 5 d     . Accessed May 31, 2024.
6. Foundation models, generative AI, and large language models in
healthcare: An overview. CIN: Computers, Informatics, Nursing.
2024;42(5). Available from:  h t t  p s : /  / j o  u r n  a l s  . l w  w . c o  m /  c i n  j o u r  n a l
/ f u  l l t e x t / 2 0 2 4 / 0 5 0 0 0 / f o u n d a t i o n _ m o d e l s , _ g e n e r a t i v e _ a i , _ a n d _ l a
r g e . 1 1 . a s p x     . Accessed May 31, 2024.
7. Samuel J. The Critical Need for Transparency and Regulation
amidst the Rise of Powerful Artificial Intelligence Models. Schol-
ars Strategy Network (SSN) Key Findings; 2023. Available from:
h t t  p s : /  / s c  h o l  a r s  . o r  g / c o  n t  r i b u t i o n / c r i t i c a l - n e e d - t r a n s p a r e n c y - a n d - r
e g u l a t i o n     . Accessed May 31, 2024.
8. Generative AI in Healthcare Market News. Market.us. Available
from:  h t t  p s : /  / m e  d i a  . m a  r k e  t . u s  / g  e n e r a t i v e - a i - i n - h e a l t h c a r e - m a r k e
t - n e w s /     . Accessed May 31, 2024.
9. GANs Explained: How Generative Adversarial Networks Work.
Shelf. Available from:  h t t  p s : /  / s h  e l f  . i o  / b l  o g / g  a n  s - e x p l a i n e d - h o w - g
e n e r a t i v e - a d v e r s a r i a l - n e t w o r k s - w o r k /     . Accessed May 31, 2024.
10. What is GAN (Generative Adversarial Network)? Amazon Web
Services. Available from: https:/ /aws.am azon.co m/wha t-is/gan/.
Accessed October 31, 2024
11. What is Multimodal AI? | Zapier. Available from:  h t t  p s : /  / z a  p i e  r . c
o m / b l o g / m u l t i m o d a l - a i /     . Accessed May 31, 2024.
12. What are large language models and how are they used in gen -
erative AI? Computerworld. Available from:  h t t  p s : /  / w w  w . c  o m p  u
t e  r w o r  l d  . c o  m / a r  t i c  l e /  1 6 2  7 1 0  1 / w h  a t  - a r e - l a r g e - l a n g u a g e - m o d e l s - a
n d - h o w - a r e - t h e y - u s e d - i n - g e n e r a t i v e - a i . h t m l     . Accessed May 31,
2024.
13. Generative AI in Healthcare. Deloitte. Available from:  h t t  p s : /  / w
w  w 2 .  d e l  o i t  t e . c  o m  / u s  / e n /  p a g  e s /  l i f e - s c i e n c e s - a n d - h e a l t h - c a r e / a r t i c
l e s / g e n e r a t i v e - a i - i n - h e a l t h c a r e . h t m l     . Accessed May 31, 2024.
14. Study Finds ChatGPT Outperforms Physicians in High-Quality,
Empathetic Answers to Patient Questions. UC San Diego Today.
Available from:  h t t  p s : /  / t o  d a y  . u c  s d .  e d u /  s t  o r y  / s t u  d y -  fi  n  d s -  c h a  t g p t  -
o  u t p e r f o r m s - p h y s i c i a n s - i n - h i g h - q u a l i t y - e m p a t h e t i c - a n s w e r s - t o - p
a t i e n t - q u e s t i o n s     . Accessed May 31, 2024.
15. AI-generated drug begins clinical trials in human patients.
CNBC; 2023. Available from:  h t t  p s : /  / w w  w . c  n b c  . c o  m / 2 0  2 3  / 0 6  / 2
9 /  a i -  g e n  e r a t e d - d r u g - b e g i n s - c l i n i c a l - t r i a l s - i n - h u m a n - p a t i e n t s . h t m
l     . Accessed May 31, 2024.
16. Nvidia announces GH200 Grace Hopper superchip with HBM3E
memory. Nvidia Newsroom. Available from:  h t t  p s : /  / n v  i d i  a n e  w s
.  n v i d  i a  . c o m / n e w s / g h 2 0 0 - g r a c e - h o p p e r - s u p e r c h i p - w i t h - h b m 3 e - m
e m o r y     . Accessed May 31, 2024.
17. Hospital CEOs name staffing, workforce as top concerns for
2023. Healthcare Dive. Available from:  h t t  p s : /  / w w  w . h  e a l  t h c  a r e
d  i v  e . c  o m / n  e w s  / h o  s p i t a l - C E O s - s t a ffi    n g - w o r k f o r c e - t o p - c o n c e r n - 2
0 2 3 / 6 4 2 6 1 5 /     . Accessed May 31, 2024.
1 3
   10  Page 8 of 11

Journal of Medical Systems           (2025) 49:10
52. O’Connor S, Peltonen LM, Topaz M, et al. Prompt engineering
when using generative AI in nursing education. Nurse Educ Pract.
2023. doi: https:/ /doi.or g/10.10 16/j. nepr.2023.103825.
53. Gosak L, Pruinelli L, Topaz M, Štiglic G. The ChatGPT effect
and transforming nursing education with generative AI: Discus -
sion paper. Nurse Educ Pract. 2024;75:103888. doi:  h t t  p s : /  / d o  i . o  r
g / 1 0 . 1 0 1 6 / j . n e p r . 2 0 2 4 . 1 0 3 8 8 8     .
54. Jordon J, Szpruch L, Houssiau F, et al. Synthetic Data–what,
why and how? arXiv preprint arXiv:2205.03257. Available from:
https:/ /doi.or g/10.48 550/a rXiv.2205.03257. Accessed May 31,
2024.
55. Kingma, D.P., & Welling, M. (2013). Auto-Encoding Variational
Bayes. CoRR, abs/1312.6114.
56. Annas GJ. HIPAA regulations: a new era of medical-record pri -
vacy? N Engl J Med. 2003;348:1486.
57. Goodfellow I, Pouget-Abadie J, Mirza M, et al. Generative
adversarial networks. Commun ACM. 2020;63(11):139–144.
doi:https:/ /doi.or g/10.11 45/34 22622.
58. Jadon A, Kumar S. Leveraging generative AI models for syn -
thetic data generation in healthcare: Balancing research and pri -
vacy. In: 2023 International Conference on Smart Applications,
Communications and Networking (SmartNets). IEEE; 2023:1–4.
doi:https:/ /doi.or g/10.11 09/Sm artNets58706.2023.10215825.
59. Frid-Adar M, Diamant I, Klang E, et al. GAN-based synthetic
medical image augmentation for increased CNN performance in
liver lesion classification. Neurocomputing. 2018;321:321–331.
doi:https:/ /doi.or g/10.10 16/j. neucom.2018.09.013.
60. Torfi A, Fox EA. CorGAN: correlation-capturing convolutional
generative adversarial networks for generating synthetic health -
care records. Presented at: The thirty-third international flairs
conference; May 2020.
61. Castañeda WAC, Bertemes Filho P. Synthetic health data genera-
tion for enhancement of non-invasive diabetes AI-based predic -
tion. Available from:  h t t  p s : /  / d o  i . o  r g / 1 0 . 2 0 9 4 4 / p r e p r i n t s 2 0 2 3 0 8 . 1
4 6 4 . v 1     . Accessed May 31, 2024.
62. Packhäuser K, Folle L, Thamm F, Maier A. Generation of Anony-
mous Chest Radiographs Using Latent Diffusion Models for
Training Thoracic Abnormality Classification Systems. In: 2023
IEEE 20th International Symposium on Biomedical Imaging
(ISBI), Cartagena, Colombia, 2023. pp. 1–5.  d o i :    h t t p  s : /  / d o  i . o r g /
1 0 . 1 1 0 9 / I S B I 5 3 7 8 7 . 2 0 2 3 . 1 0 2 3 0 3 4 6     .
63. Tang, R., Han, X., Jiang, X., & Hu, X. (2023). Does Synthetic
Data Generation of LLMs Help Clinical Text Mining? ArXiv,
abs/2303.0460.
64. Eigenschink P, Reutterer T, Vamosi R, et al. Deep Generative Mod-
els for Synthetic Data: A Survey. IEEE Access. 2023;11:47304–
47320. doi:https:/ /doi.or g/10.11 09/AC CESS.2023.3275134.
65. MDClone. Available from: https://www.mdclone.com. Accessed
May 31, 2024.
66. Chola C, Muaad AY , Bin Heyat MB, et al. BCNet: A Deep Learn-
ing Computer-Aided Diagnosis Framework for Human Periph -
eral Blood Cell Identification. Diagnostics. 2022;12(11):2815.
doi:https:/ /doi.or g/10.33 90/di agnostics12112815.
67. Ali H, Biswas MR, Mohsen F, et al. The role of generative adver-
sarial networks in brain MRI: a scoping review. Insights Imaging.
2022;13(1):98. doi: https:/ /doi.or g/10.11 86/s1 3244-022-01237-0.
68. Frid-Adar M, Diamant I, Klang E, et al. GAN-based synthetic
medical image augmentation for increased CNN performance in
liver lesion classification. Neurocomputing. 2018;321:321–331.
doi:https:/ /doi.or g/10.10 16/j. neucom.2018.09.013.
69. Jung E, Luna M, Park SH. Conditional GAN with 3D discrimina-
tor for MRI generation of Alzheimer’s disease progression. Pat -
tern Recognit. 2023;133:109061.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0 1 6 / j . p a
t c o g . 2 0 2 2 . 1 0 9 0 6 1     .
70. Despotović I, Goossens B, Philips W. MRI segmentation of the
human brain: challenges, methods, and applications. Comput
surgical oncology: incomplete excision rates of 34 955 basal cell
carcinomas. Br J Surg. 2023;110:1072–1075.
36. Nvidia and Johnson & Johnson to Build AI Applications for Sur-
gery. CNBC. Available from:  h t t  p s : /  / w w  w . c  n b c  . c o  m / 2 0  2 4  / 0 3  / 1 8
/  n v i  d i a  - a n d - j o h n s o n - j o h n s o n - t o - b u i l d - a i - a p p l i c a t i o n s - f o r - s u r g e r
y - . h t m l     . Accessed May 31, 2024.
37. Zuluaga L, Rich JM, Gupta R, et al. AI-powered real-time annota-
tions during urologic surgery: The future of training and quality
metrics. Urol Oncol. 2024;42(3):57–66.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0
1 6 / j . u r o l o n c . 2 0 2 3 . 1 1 . 0 0 2     .
38. Loftus TJ, Tighe PJ, Filiberto AC, et al. Artificial Intelligence and
Surgical Decision-making. JAMA Surg. 2020;155(2):148–158.
doi:https:/ /doi.or g/10.10 01/ja masurg.2019.4917.
39. Saeidi H, et al. Supervised Autonomous Electrosurgery via Bio -
compatible Near-Infrared Tissue Tracking Techniques. IEEE
Trans Med Robotics Bionics. 2019;1(4):228–236.  d o i :    h t t p  s : /  / d o
i . o r g / 1 0 . 1 1 0 9 / T M R B . 2 0 1 9 . 2 9 4 9 8 7 0     .
40. Physician burnout report 2018 [Internet]. Harvard T.H. Chan
School of Public Health. 2019. Available from:  h t t  p s : /  / w w  w . h  s
p h  . h a  r v a r  d .  e d u  / w p -  c o n  t e n  t / u p l o a d s / s i t e s / 2 1 / 2 0 1 9 / 0 1 / P h y s i c i a n B
u r n o u t R e p o r t 2 0 1 8 F I N A L . p d f     . Accessed May 31, 2024.
41. The economic cost of physician burnout [Internet]. Harvard Busi-
ness School Working Knowledge. 2019. Available from:  h t t  p s :
/  / h b  s w k  . h b  s . e  d u / i  t e  m / t h e - e c o n o m i c - c o s t - o f - p h y s i c i a n - b u r n o u t     .
Accessed May 31, 2024.
42. Ayers JW, Poliak A, Dredze M, Leas EC, Zhu Z, Kelley JB, Faix
DJ, Goodman AM, Longhurst CA, Hogarth M, Smith DM. Com-
paring physician and artificial intelligence chatbot responses to
patient questions posted to a public social media forum. JAMA
Intern Med. 2023;183(6):589–596. doi:  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 0 1 / j a
m a i n t e r n m e d . 2 0 2 3 . 1 8 3 8     .
43. Garcia P, Ma SP, Shah S, et al. Artificial intelligence-generated draft
replies to patient inbox messages. JAMA Netw Open. 2024;7(3).
doi:https:/ /doi.or g/10.10 01/ja manetworkopen.2024.3201.
44. Tajirian T, Stergiopoulos V , Strudwick G, Sequeira L, Sanches
M, Kemp J, Ramamoorthi K, Zhang T, Jankowicz D. The influ -
ence of electronic health record use on physician burnout: cross-
sectional survey. J Med Internet Res. 2020;22(7). doi:  h t t p s : / / d o i .
o r g / 1 0 . 2 1 9 6 / 1 9 2 7 4     .
45. MedCentral. (n.d.). AI scribes: Helpful tools or additional bur -
den? Available from:  h t t  p s : /  / w w  w . m  e d c  e n t  r a l .  c o  m / a i / a i - s c r i b e s - h
e l p f u l - t o o l s - o r - a d d i t i o n a l - b u r d e n     . Accessed May 31, 2024.
46. Generative AI: A game changer for primary care physicians
[Internet]. Medical Economics. 2020. Available from:  h t t  p s : /  / w w
w . m  e d i  c a l  e c o n  o m  i c s  . c o m  / v i  e w /  g e n e r a t i v e - a i - a - g a m e - c h a n g e r - f o
r - p r i m a r y - c a r e - p h y s i c i a n s     . Accessed May 31, 2024.
47. Beam AL, Kohane IS. Big data and machine learning in health
care. JAMA. 2018;319(13):1317–1318. doi:  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0
0 1 / j a m a . 2 0 1 7 . 1 8 3 9 1     .
48. Technology making health care work more meaningful [Internet].
Deloitte. 2020. Available from:  h t t  p s : /  / w w  w 2 .  d e l  o i t  t e . c  o m  / u s  / e n /
i n s  i g h  t s /  i n d  u s t r  y /  h e a l t h - c a r e / t e c h n o l o g y - m a k i n g - h e a l t h - c a r e - w o
r k - m o r e - m e a n i n g f u l . h t m l     . Accessed May 31, 2024.
49. Leung F, Lau YC, Law M, Djeng SK. Artificial intelligence and
end-user tools to develop a nurse duty roster scheduling system.
Int J Nurs Sci. 2022;9(3):373–377. doi:  h t t  p s : /  / d o  i . o  r g / 1 0 . 1 0 1 6 / j .
i j n s s . 2 0 2 2 . 0 6 . 0 1     .
50. Tam W, Huynh T, Tang A, et al. Nursing education in the age
of artificial intelligence powered Chatbots (AI-Chatbots): are we
ready yet? Nurse Educ Today. 2023;129:105917. doi:  h t t  p s : /  / d o  i .
o  r g / 1 0 . 1 0 1 6 / j . n e d t . 2 0 2 3 . 1 0 5 9 1 7     .
51. Liao CT, Tsay SF, Chen HC. Exploring generative AI’s role in alle-
viating nursing workload and burnout in Taiwan. J Formos Med
Assoc. 2024. doi: https:/ /doi.or g/10.10 16/j. jfma.2024.02.003.
1 3
Page 9 of 11    10

Journal of Medical Systems           (2025) 49:10
87. Samuel J, Ali GG, Rahman M, Esawi E, Samuel Y . Covid-19 pub-
lic sentiment insights and machine learning for tweets classifica -
tion. Information. 2020;11(6):314.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 3 3 9 0 / i n f
o 1 1 0 6 0 3 1 4     .
88. Lyons J, Nafilyan V , Akbari A, et al. An external validation of
the QCOVID3 risk prediction algorithm for risk of hospitalisa -
tion and death from COVID-19: An observational, prospective
cohort study of 1.66 m vaccinated adults in Wales, UK. Plos One.
2023;18(5). doi:https:/ /doi.or g/10.13 71/jo urnal.pone.0285979.
89. Saghapour T, Giles-Corti B, Jafari A, et al. Supporting pandemic
disease preparedness: Development of a composite index of area
vulnerability. Health Place. 2021;70:102629.  d o i :    h t t p  s : /  / d o  i . o r g / 1
0 . 1 0 1 6 / j . h e a l t h p l a c e . 2 0 2 1 . 1 0 2 6 2 9     .
90. Cegan JC, Trump BD, Cibulsky SM, et al. Can comorbidity data
explain cross-state and cross-national difference in covid-19
death rates? Risk Manag Healthc Policy. 2021;2877–2885.  d o i :    h t
t p  s : /  / d o  i . o r g / 1 0 . 2 1 4 7 / R M H P . S 3 1 3 3 1 2     .
91. Wolterink JM, Leiner T, Viergever MA, et al. Generative adver -
sarial networks for noise reduction in low-dose CT. IEEE Trans
Med Imaging. 2017;36(12):2536–2545.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 1
0 9 / T M I . 2 0 1 7 . 2 7 0 8 9 8 7     .
92. Eysenbach G. The role of ChatGPT, generative language models,
and artificial intelligence in medical education: a conversation
with ChatGPT and a call for papers. JMIR Med Educ. 2023;9(1).
doi:https://doi.org/10.2196/46885.
93. How machine learning can break down language and trade bar -
riers [Internet]. MIT Sloan; 2020. Available from:  h t t  p s : /  / m i  t s l  o a
n  . m i  t . e d  u /  i d e  a s - m  a d e  - t o  - m a t t e r / h o w - m a c h i n e - l e a r n i n g - c a n - b r e a
k - d o w n - l a n g u a g e - a n d - t r a d e - b a r r i e r s     . Accessed May 31, 2024.
94. Bennett OF, Kanber B, Hoskote C, et al. Learning to see the
invisible: A data-driven approach to finding the underlying pat -
terns of abnormality in visually normal brain magnetic reso -
nance images in patients with temporal lobe epilepsy. Epilepsia.
2019;60(12):2499–2507. doi:https:/ /doi.or g/10.11 11/ep i.16380.
95. Abd-Alrazaq A, AlSaad R, Alhuwail D, et al. Large language
models in medical education: opportunities, challenges, and
future directions. JMIR Med Educ. 2023;9(1).  d o i :   h t t p s : / / d o i . o r
g / 1 0 . 2 1 9 6 / 4 8 2 9 1     .
96. Khan MHM, Sahib-Kaudeer NG, Dayalen M, et al. Multi-class
skin problem classification using deep generative adversarial net-
work (DGAN). Comput Intell Neurosci. 2022.  d o i :    h t t p  s : /  / d o  i . o r g
/ 1 0 . 1 1 5 5 / 2 0 2 2 / 1 7 9 7 4 7 1     .
97. Li H, Xu T, Zhang C, et al. Bringing Generative AI to Adaptive
Learning in Education. arXiv preprint arXiv:2402.14601. Avail -
able from: https:/ /doi.or g/10.48 550/a rXiv.2402.14601. Accessed
May 31, 2024.
98. Optimizing Healthcare Revenue Cycle Management with Gen -
erative AI and Intelligent Automation [Internet]. Automation
Anywhere; 2024. Available from:  h t t  p s : /  / w w  w . a  u t o  m a t  i o n a  n y  w
h e  r e . c  o m /  c o m  p a n  y / b  l o g /  a u  t o m  a t i o  n - a  i / o  p t i m i z i n g - h e a l t h c a r e - r e
v e n u e - c y c l e - m a n a g e m e n t - g e n e r a t i v e - a i - a n d - i n t e l l i g e n t - a u t o m a t i
o n     . Accessed May 31, 2024.
99. Can AI Accurately Perform Medical Billing Coding? [Internet].
Medical Billers and Coders Blog; 2024. Available from:  h t t  p s : /
/ w w  w . m  e d i  c a l  b i l l  e r  s a n  d c o d  e r s  . c o  m / b l o g / c a n - a i - a c c u r a t e l y - p e r f
o r m - m e d i c a l - b i l l i n g - c o d i n g / # : ~ : t e x t = A c c u r a c y % 2 0 o f % 2 0 A I % 2
0     i n % 2 0 M e d i c a l % 2 0 B i l l i n g & t e x t = A I % 2 0 u s e s % 2 0 s m a r t % 2 0 a l g
o r i t h m s % 2 0 t h a t , w i t h % 2 0 A I % 2 0 i s % 2 0 s o % 2 0 p r e c i s e . Accessed
May 31, 2024.
100. Jorie. (n.d.). The benefits of medical billing automation for
healthcare providers. Available from:  h t t  p s : /  / w w  w . j  o r i  e . a  i / p o  s t  / t
h  e - b e  n e fi   t s  - o f - m e d i c a l - b i l l i n g - a u t o m a t i o n - f o r - h e a l t h c a r e - p r o v i d
e r s     . Accessed May 31, 2024.
101. Thoughtful.ai. (n.d.). Leveraging AI for enhanced revenue cycle
management. Available from:  h t t  p s : /  / w w  w . t  h o u  g h t  f u l .  a i  / b l o g / l e
Math Methods Med. 2015;2015:450341.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1
1 5 5 / 2 0 1 5 / 4 5 0 3 4 1     .
71. Kim M, Kim YN, Jang M, et al. Synthesizing realistic high-reso-
lution retina image by style-based generative adversarial network
and its utilization. Sci Rep. 2022;12:17307.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0
. 1 0 3 8 / s 4 1 5 9 8 - 0 2 2 - 2 0 6 9 8 - 3     .
72. Yang Q, Yan P, Zhang Y , Yu H, Shi Y , Mou X, Kalra MK, Zhang
Y , Sun L, Wang G. Low-Dose CT Image Denoising Using a Gen-
erative Adversarial Network With Wasserstein Distance and Per-
ceptual Loss. IEEE Trans Med Imaging. 2018;37(6):1348–1357.
doi: https:/ /doi.or g/10.11 09/TM I.2018.2827462.
73. Ching T, Himmelstein DS, Beaulieu-Jones BK, et al. Opportuni -
ties and obstacles for deep learning in biology and medicine. J R
Soc Interface. 2018;15(141):20170387.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0
9 8 / r s i f . 2 0 1 7 . 0 3 8 7     .
74. Topol EJ. High-performance medicine: the convergence of human
and artificial intelligence. Nat Med. 2019;25(1):44–56. doi:https:/
/doi.or g/10.10 38/s4 1591-018-0300-7.
75. Olawade, D. B., David-Olawade, A. C., Wada, O. Z., Asaolu, A.
J., Adereni, T., & Ling, J. (2024). Artificial intelligence in health-
care delivery: Prospects and pitfalls. Journal of Medicine, Sur -
gery, and Public Health, V olume 3, 100108.
76. Shaban-Nejad A, Michalowski M, Buckeridge DL. Health intel -
ligence: how artificial intelligence transforms population and per-
sonalized health. NPJ Digit Med. 2018;1:53.  d o i :    h t t p  s : /  / d o  i . o r g / 1
0 . 1 0 3 8 / s 4 1 7 4 6 - 0 1 8 - 0 0 5 8 - 9     .
77. Feng S, Grépin KA, Chunara R. Tracking health seeking behavior
during an Ebola outbreak via mobile phones and SMS. NPJ Digit
Med. 2018;1:51. doi:https:/ /doi.or g/10.10 38/s4 1746-018-0055-z.
78. Wu JY , Wang Y , Ching CTS, Wang HMD, Liao LD. IoT-based
wearable health monitoring device and its validation for poten -
tial critical and emergency applications. Front Public Health.
2023;11:1188304. doi:  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 8 9 / f p u b h . 2 0 2 3 . 1 1 8 8
3 0 4
79. Maleki Varnosfaderani, S., & Forouzanfar, M. (2024). The role
of AI in hospitals and clinics: transforming healthcare in the 21st
century. Bioengineering, 11(4), 337.
80. Romero-Brufau S, Wyatt KD, Boyum P, et al. Implementation
of artificial intelligence-based clinical decision support to reduce
hospital readmissions at a regional hospital. Appl Clin Inform.
2020;11(4):570–577.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0 5 5 / s - 0 0 4 0 - 1 7 1 5 8 2
7     .
81. ClosedLoop.ai. Available from: https://www.closedloop.ai.
Accessed May 31, 2024.
82. MacIntyre CR, Chen X, Kunasekaran M, et al. Artificial intel -
ligence in public health: the potential of epidemic early warn -
ing systems. J Int Med Res. 2023;51(3):03000605231159335.
doi:https:/ /doi.or g/10.11 77/03 000605231159335.
83. Rahman MS, Paul KC, Rahman MM, Samuel J, Thill JC, Hos -
sain MA, Ali GMN. Pandemic vulnerability index of US cities: A
hybrid knowledge-based and data-driven approach. Sustainable
Cities Soc. 2023;95:104570.  d o i :    h t t p  s : /  / d o  i . o r g / 1 0 . 1 0 1 6 / j . s c s . 2 0
2 3 . 1 0 4 5 7 0     .
84. Syrowatka A, Kuznetsova M, Alsubai A, et al. Leveraging artifi-
cial intelligence for pandemic preparedness and response: a scop-
ing review to identify key use cases. NPJ Digit Med. 2021;4:96.
doi:https:/ /doi.or g/10.10 38/s4 1746-021-00459-8.
85. Badidi E. Edge AI for early detection of chronic diseases and
the spread of infectious diseases: opportunities, challenges, and
future directions. Future Internet. 2023;15(11):370.  d o i :    h t t p  s : /  / d
o  i . o r g / 1 0 . 3 3 9 0 / fi  1 5 1 1 0 3 7 0     .
86. Ali GMN, Rahman MM, Hossain MA, Rahman MS, Paul KC,
Thill JC, Samuel J. Public perceptions of COVID-19 vaccines:
Policy implications from US spatiotemporal sentiment analytics.
In: Healthcare (2021)(V ol. 9, No. 9, p. 1110)
1 3
   10  Page 10 of 11

Journal of Medical Systems           (2025) 49:10
and Its Prediction during the COVID-19 Pandemic Using Google
Trends. International Journal of Environmental Research and
Public Health. 2021; 18(23):12369.  h t t  p s : /  / d o  i . o  r g / 1 0 . 3 3 9 0 / i j e r p
h 1 8 2 3 1 2 3 6 9
108. Jha, D. K. (n.d.). Revolutionize your marketing campaigns with
generative AI. LinkedIn. Available from:  h t t  p s : /  / w w  w . l  i n k  e d i  n . c
o  m /  p u l  s e / r  e v o  l u t  i o n i z e - y o u r - m a r k e t i n g - c a m p a i g n s - g e n e r a t i v e - a
i - d h r u v - k u m a r - j h a - e 9 3 u c /     . Accessed May 31, 2024.
109. Healthcare Marketing in 2024: Embracing Generative AI and
Machine Learning [Internet]. BPD Healthcare Blog; 2024.
Available from:  h t t    p s : / / b  p d  h  e  a  l t h c   a r e  .  c   o m   / b l  o g  /  h e a  l  t  h  c a r e  - m a r
k e t i n g - i n - 2 0 2 4 - e m b r a c i n g - g e n e r a t i v e - a i - a n d - m a c h i n e - l e a r n i n g     .
Accessed May 31, 2024.
Publisher’s Note Springer Nature remains neutral with regard to juris-
dictional claims in published maps and institutional affiliations.
v e r a g i n g - a i - f o r - e n h a n c e d - r e v e n u e - c y c l e - m a n a g e m e n t     . Accessed
May 31, 2024.
102. Codametrix [Internet]. Available from:  h t t p s : / / w w w . c o d a m e t r i x . c
o m     . Accessed May 31, 2024.
103. Adonis [Internet]. Available from: https://www.adonis.io.
Accessed May 31, 2024.
104. How AI Can Empower Targeted Healthcare Marketing [Internet].
Forbes; 2023. Available from:  h t t  p s : /  / w w  w . f  o r b  e s .  c o m /  s i  t e s  / f o r  b
e s  a g e  n c y  c o u  n c i l  / 2  0 2 3 / 1 2 / 1 8 / h o w - a i - c a n - e m p o w e r - t a r g e t e d - h e a l
t h c a r e - m a r k e t i n g / ? s h = 5 c d 5 1 e 3 b 6 6 e d     . Accessed May 31, 2024.
105. Smith V , Warty RR, Sursas JA, et al. The effectiveness of virtual
reality in managing acute pain and anxiety for medical inpatients:
a systematic review. J Med Internet Res.  2 0 2 0 ; 2 2 ( 1 1 ) . d o i :   h t t p s : / /
d o i . o r g / 1 0 . 2 1 9 6 / 1 7 9 8 0     .
106. Kuehn BM. More Than One-Third of US Individuals Use
the Internet to Self-diagnose. JAMA. 2013;309(8):756–757.
doi:https:/ /doi.or g/10.10 01/ja ma.2013.629
107. Sycińska-Dziarnowska M, Szyszka-Sommerfeld L, Kłoda K,
Simeone M, Woźniak K, Spagnuolo G. Mental Health Interest
1 3
Page 11 of 11    10
