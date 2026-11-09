---
title: 'Skill-Driven Certification Pathways: Measuring Industry Training Impact on Graduate Employability'
url: https://arxiv.org/abs/2506.04588
category: digital-marketing
subcategory: empirical
date: 2025-06
venue: ''
authors:
- Anatoli Kovalev
- Narelle Stefanac
- Marian-Andrei Rizoiu
source: arxiv
pdf_url: https://arxiv.org/pdf/2506.04588
pages: 32
chars: 80235
fetched_at: '2026-11-08T13:18:53+00:00'
kb_version: 1
---

# Skill-Driven Certification Pathways: Measuring Industry Training Impact on Graduate Employability

arXiv:2506.04588v1  [cs.CY]  5 Jun 2025
Skill-Driven Certification Pathways: Measuring
Industry Training Impact on Graduate Employability
Anatoli Kovalev
University of Technology Sydney
Narelle Stefanac
Microsoft
Marian-Andrei Rizoiu
University of Technology Sydney
Abstract
Australia faces a critical technology skills shortage, requiring approximately
52,000 new technology professionals annually by 2030, while confronting a widen-
ing gap between employer requirements and graduate capabilities. With only 1%
of technology graduates considered immediately work-ready, traditional educational
pathways alone prove insufficient to meet industry demands. This research examines
howindustrycertifications, suchasMicrosoft’sAI-900(AzureAIFundamentals), can
bridge this critical skills gap. We propose a novel, data-driven methodology that
quantitatively measures skill alignment between educational offerings and job mar-
ket requirements by analysing over 2.5 million job advertisements from Australia,
the US, and the UK, mapping extracted skills to industry taxonomies using the Vec-
torised Skills Space Method. Our findings reveal that combining university degrees
with targeted industry certifications significantly enhances employability for technol-
ogy roles. The Bachelor of Computer Science with AI major combined with AI-900
certification achieved the highest absolute skill similarity score for Machine Learning
Engineer positions. Surprisingly, the largest improvements when augmented with AI
certifications are experiences by non-technical degrees–such as nursing nursing–with
up to 9, 296% percentage improvements in alignment with Machine Learning Engi-
neer roles. Our results challenge conventional assumptions about technology career
pathways. They can provide actionable insights for educational institutions seeking
evidence-basedcurriculumdesign, studentsrequiringstrategiccertificationguidance,
and employers recognising potential in candidates from non-traditional backgrounds
who have obtained relevant certifications.
1 Introduction
Australia is facing a critical shortage of tech professionals, with The Australian Com-
puter Society reporting that the nation is experiencing a skills shortage not seen in over
six decades [Sadler, 2023]. Based on current business projections, it is anticipated that
by 2030, Australia will require a workforce of 1.3 million technology professionals, conse-
quently, this demand corresponds to an annual need for approximately 52,000 technology
workers [Australian Computer Society, 2024]. The shortage is exacerbated by rapid digi-
tal transformation and the increased adoption of emerging technologies across industries
. In the 2021 report, titled “Technology Council of Australia Roadmap to Deliver One
1

Million Tech Jobs”, it has been suggested that the Australian technology sector stands as
a cornerstone of the nation’s economy, generating an annual contribution of $167 billion
to the Gross Domestic Product (GDP) and employing 861,000 individuals [Technology
Council of Australia, 2021].
The traditional talent source has been evaluated by examining the number of gradu-
ates in technology fields from Australian universities and Vocational Education Training
(VET) institutions. According to the ACS Digital Pulse report [Australian Computer
Society, 2024], only 75,000 ICT students entered the tech workforce in Australia between
2016 and 2021. That is equivalent to 15,000 ICT professionals joining the tech sector per
year. Recently propose caps on the number of international students could potentially
further jeopardise the future influx of technology workers. International students cur-
rently constitute 65% of annual IT program completions [Australian Computer Society,
2024].
Despite the high demand for tech workers, there is a significant mismatch between the
skills required by employers and those possessed by the workforce. This mismatch results
in many tech positions remaining unfilled, which in turn hampers business operations
and growth. Recent research indicates that traditional learning pathways in Australia
are facing challenges in producing job-ready workers. A 2019 study by Think Education
revealed that nearly 40% of young Australians feel their education has not provided them
with the skills required for their current job [Brown, 2019]. This sentiment is echoed in
the Australian Workforce and Productivity Agency’s report, which highlights industry
perceptions that graduates are often “not job ready” [Brown, 2019].
Recent reports from key Australian technology organisations highlight significant chal-
lenges in producing job-ready graduates for the tech sector. The Australian Information
Industry Association’s (AIIA) State of the Nation 2024 report reveals a concerning trend
in graduate work-readiness, with only 1% of technology graduates considered immedi-
ately work-ready, down from 3% in 2023 [Associations Forum, 2024]. The issue is further
compounded by rising youth unemployment rates, reaching up to 20% in some areas, and
data showing that up to 30% of university students are unemployed after completing their
degrees [Brown, 2019].
The Australian Industry and Skills Committee (AISC) has recognised this gap, empha-
sising the need for a more integrated approach to education and workforce development.
Their 2024 VET Workforce study projects that around 44% of new jobs expected to be
created over the next decade will have Vocational Education and Training (VET) as the
primary training pathway [Jobs and Skills Australia, 2024]. This underscores the impor-
tance of vocational skills training in addressing the national skills shortage and preparing
workers for future job markets.
Furthermore, a comprehensive study on educational opportunity in Australia, pub-
lished in 2020, reveals that approximately 29.7% of 24-year-olds were not engaged in
full-time education, training, or work [Lamb et al., 2020]. This statistic suggests that the
education system has not fully delivered on its promise to prepare all students in Aus-
tralia for life, work, and learning. The study also highlights significant disparities based
on socioeconomic status, gender, and geographic location, indicating that the challenges
in producing job-ready workers are not uniformly distributed across the population [Lamb
et al., 2020].
Inresponsetothesechallenges, thereisagrowingrecognitionoftheneedforalternative
pathways and more practical, work-oriented education models. The Australian Technical
and Further Education (TAFE) system and other vocational education providers are in-
2

creasingly seen as crucial in bridging the gap between traditional education and workforce
needs [Jobs and Skills Australia, 2024]. Additionally, initiatives like the National Skills
Agreement (NSA) and fee-free TAFE programs are being implemented to increase access
to vocational education and address specific skill shortages [Jobs and Skills Australia,
2024].
Universities are also increasingly integrating industry-specific training into their tech
programs through various innovative approaches, aiming to produce graduates who are
better prepared for the demands of the rapidly evolving tech sector. This includes imple-
menting work-integrated learning (WIL) experiences, such as internships, placements, and
industry-based projects [Bean and Dawkins, 2021]. The National Priorities Industry Link-
age Fund (NPILF), part of the Job-ready Graduates Package, aims to provide a framework
for stepping up industry engagement in higher education [Bean and Dawkins, 2021]. This
initiative encourages universities to develop innovative WIL arrangements, including re-
mote internships, placements, and industry-based projects. Furthermore, to provide more
flexible and targeted learning options, universities are developing micro-credential offer-
ings, often in collaboration with tech industry partners [Bean and Dawkins, 2021]. These
short courses allow students to acquire specific, in-demand skills quickly and provide a way
for working professionals to upskill or reskill in emerging technologies [Bean and Dawkins,
2021]. The Australian Government’s introduction of the Undergraduate Certificate as a
new qualification type demonstrates this shift towards shorter, more focused credentials
[Bean and Dawkins, 2021].
The VET sector’s approach to creating work-ready graduates offers valuable lessons
for universities, particularly in the tech industry. By adopting and adapting strategies
such as enhanced industry collaboration, flexible credentialing, digital skills integration,
responsive program design, and a focus on employability skills, universities can better
prepare their graduates for the dynamic tech sector. As the lines between vocational and
higher education continue to blur, this cross-sector learning will be crucial in developing
a workforce that can meet the evolving needs of the tech industry and drive innovation
in the Australian economy.
2 Background
The dynamic nature of the technology sector has led to a growing disparity between the
skills taught in traditional educational programs (Universities and TAFE) and those de-
manded by employers. This gap has given rise to the popularity of industry certifications
as a means to bridge this divide. In today’s rapidly evolving job market, the combina-
tion of traditional university degrees and industry-recognised certifications has become
increasingly important for students seeking employment. This section of the paper exam-
ines the value of certifications from major technology companies such as Microsoft, AWS
and Google when paired with a tertiary qualification. We will explore the impact of these
combined credentials on employability, career advancement, and earning potential.
Over the past decade, there has been a significant increase in the popularity and recog-
nition of industry-based certifications. These credentials, offered by technology companies
like Microsoft, Amazon and Google, have become valuable assets for job seekers and pro-
fessionals alike [Certiport]. The growing demand for specialised skills in cloud computing,
data analytics, and cybersecurity has further emphasised the importance of these certifi-
cations.
Research has shown that industry certifications can complement traditional univer-
3

sity degrees by providing practical, job-ready skills that employers value. A study by
the institute of Defence Analysis conducted in 2019 found that while employers generally
preferred academic degrees, they also recognised the importance of certifications in iden-
tifying specific technical skills [Belanich et al., 2019]. This suggests that the combination
of a degree and relevant certifications can be particularly beneficial in the job market.
2.1 Impact on Employability
Several studies have demonstrated the positive impact of industry certifications on em-
ployability. According to a survey conducted by Amazon Web Services, 84% of learners
reported improved on-the-job efficiency after completing AWS training, while 83% re-
ported improved effectiveness [AWS Training and Certification Blog, 2022]. Additionally,
69% of respondents reported higher earnings as a result of AWS training, and 74% re-
ported the same after earning AWS certifications [AWS Training and Certification Blog,
2022].
A survey conducted by Coursera found that 88% of learners believe an industry cer-
tificate will help them stand out with employers in the job market [McAndrew]. This
perception is validated by employer attitudes, as 92% of employers surveyed said a cer-
tificate strengthens a candidate’s application, and 76% reported being more likely to hire
a candidate with a certificate [McAndrew].
Microsoft Technical Certifications are powerful catalysts for employability, offering
industry-recognised validation of job-ready skills. These certifications are tightly aligned
with in-demand job roles and real-world scenarios, enabling individuals to demonstrate
proficiency in critical technical domains. According to a 2024 IDC InfoBrief sponsored
by Microsoft [Smith and Mehta, 2024], 70% of organisations consider industry-recognised
credentials essential or very important for skills training. Furthermore, a 2023 Pearson
VUE Candidate Report [Pearson VUE, 2023] found that 91% of certification holders
felt more confident in their abilities, and 77% reported being better able to innovate
after earning their certification. Microsoft’s credentials not only enhance professional
credibility but also elevate visibility across networks, giving employers full confidence in
the authenticity and relevance of certified skills.
2.2 Existing Methodologies for Researching Certification Impact
Several methodologies have been employed to study the impact of industry certifications
on employment outcomes:
Correlation studiesexamine the relationship between certification and various ed-
ucational outcomes. For example, Cook [2021] investigated the bivariate correlation be-
tween industry credentials earned during high school and post-graduation employment
rates in related job areas. This methodology allows researchers to identify potential asso-
ciationsbetweencertificationanddesiredoutcomes, suchasemploymentratesoracademic
performance. However, it’s important to note that correlation does not imply causation,
and other factors may influence the observed relationships.
Comparative Analysis: Ramamonjiarivelo et al. [2020] used Welch t-tests to com-
pare job satisfaction, and career growth between certified and non-certified individuals.
This approach can be applied to compare outcomes for graduates with and without in-
dustry certifications.
Surveys and Questionnaires:Organisations like Global Knowledge conduct annual
4

surveys to determine the average salaries associated with specific certifications [Global
Knowledge, 2024]. This methodology helps quantify the financial impact of certifications.
While salary surveys provide concrete data on the monetary value of certifications, they
maynotcaptureotherimportantaspectsofcareerdevelopmentandjobsatisfaction. Ano-
table example of this approach is found in the study of Cisco Certified Network Associate
(CCNA) courses. Researchers analysed data from the Waikato Institute of Technology
(Wintec) and the Southern Institute of Technology (SIT) to evaluate how well the CCNA
courses met the needs of the Information and Communications Technology (ICT) indus-
try in Hamilton and Invercargill, New Zealand [Rajendran and Morton, 2011]. The study
compared the effectiveness of embedding CCNA in these regions and highlighted course
topics found to be most useful in the workplace.
These methodologies offer diverse approaches to researching certification impact on
educational programs. Researchers should carefully consider the strengths and limita-
tions of each method when designing studies to evaluate the effectiveness of certification
programs.
3 A Novel Methodology for Assessing the Value of In-
dustry Certifications in Conjunction with University
Degrees
This section introduces our mathematical framework for measuring the impact of industry
certifications on the skill alignment between university degrees and junior AI roles. We
introduce in Section 3.1 the prerequisites for our work, the Skill Space Method. Next,
we present a comprehensive methodology that quantifies skill relationships (Section 3.2),
combines skill sets from different educational components (Section 3.3), and evaluates the
resulting improvement in job market alignment (Section 3.4).
3.1 The Skills Space Method
To quantify skill alignment between degrees, certifications, and job roles, we use the Skills
Space Method [Dawson et al., 2021] as our foundation. This enables us to compute simi-
larity scores between educational offerings and job requirements, specifically to evaluate
certification impact.
The core of this method involves the following components:
1. Skill extraction: Identifying skills from job advertisements, university curricula,
and certification syllabi
2. Revealed Comparative Advantage (RCA):Measuring the relative importance
of skills within each educational or job context
3. Skill similarity matrix:Quantifying relationships between different skills across
educational and employment domains
4. Skill set similarity calculation: Computing overall alignment between educa-
tional offerings and job requirements
5

The Skill Set Similarity (SSS) between two skill sets A and B is calculated as:
SSS (A, B) =
P
i∈A,j∈B w(i, A) · w(j, B) · θ(i, j) pP
i∈A w(i, A)2 · qP j∈B w(j, B)2 (1)
Where:
• w(i, A) is the weight of skill i in skill set A (e.g., a university degree)
• w(j, B) is the weight of skill j in skill set B (e.g., a junior AI role)
• θ(i, j) is the similarity between skills i and j
Temporal complexity and the Vectorised Skills Space Method.Note that the
computation of the Skill Space Similarity in Eq. (1) has a complexity ofO(|A| × |B|) for
each pairwise comparison, where|A| and |B| are the sizes of the skill sets being compared.
When applied to our large-scale analysis involving multiple degree programs, certifica-
tions, and job roles (see Section 4), this results in computationally intensive operations
that do not scale efficiently to real-world scenarios. We contribute an efficient, vectorised
implementation that we denote as the Vectorised Skills Space Method (VSSM) (fully
detailed in Appendix B). Through comprehensive benchmarking, VSSM achieves perfor-
mance improvements of up to143, 876× over naive implementations, enabling practical
application to large datasets containing millions of job advertisements and thousands of
unique skills. This enables us to measure the baseline job alignment of university degrees
and the enhanced alignment when industry certifications are added.
3.2 Skill Alignment with Target Occupations
Beyond overall similarity, we need to identify which specific skills contribute most to
employment readiness. We propose a granular skill alignment measurement function to
determine how individual certification skills enhance job-specific competencies:
L(starget, A, B) =
X
s∈A
w(s, A) · w(starget, B) · θ(s, starget) , (2)
where:
• starget is a specific job skill we want to measure alignment for
• A is the educational skill set (e.g., degree + certification)
• B is the job skill set (e.g., requirements for a Machine Learning Engineer)
• w(starget, B) is the importance of the target skill in the job
• w(s, A) is the importance of a skill in the educational program
• θ(s, starget) is the similarity between an educational skill and the target job skill
This function identifies how well a combined education (university degree plus industry
certification) prepares graduates for specific job requirements. By calculating this for key
AI job skills, we can determine which certification-degree combinations best enhance
employment prospects for specific roles.
6

3.3 Combining Skill Sets from Degrees and Certifications
To model how industry certifications complement university degrees, we formalise the
integration of their respective skill sets.
Let us define:
• S1: University degree skill set (e.g., Bachelor of Computer Science)
• S2: Industry certification skill set (e.g., Microsoft AI-900)
The combined skill setS′ 1 is the union:
S′ 1 = S1 ∪ S2 .
A crucial aspect is appropriately weighting skills in this combined set. Since certi-
fication skills are more recently acquired and often more aligned with current industry
needs, we apply a linear transformation that positions these skills within the topα% of
the degree’s weight range:
wT (s, S2) = a · w(s, S2) + b , (3)
with coefficients:
a = α · (maxS1 − minS1) maxS2 − minS2
b = (1 − α) · (maxS1 − minS1) + minS1 − a · minS2
Note that α is a hyperparamenter of our method, and in our analysis in Section 5
we set it toα = 20%. Where maxS1, minS1, maxS2, and minS2 are the maximum and
minimum values of skill weights in the degree and certification skill sets, respectively:
minS1 = min s∈S1 w(s, S1) (minimum weight in the degree skill set)
maxS1 = max s∈S1 w(s, S1) (maximum weight in the degree skill set)
minS2 = min s∈S2 w(s, S2) (minimum weight in the certification skill set)
maxS2 = max s∈S2 w(s, S2) (maximum weight in the certification skill set)
We compute the weights of each skill in the combined set as
w(s, S′ 1) =



w(s, S1) if s ∈ S1, s /∈ S2
wT (s, S2) if s ∈ S2, s /∈ S1
w(s, S1) + wT (s, S2) if s ∈ S1 ∩ S2
0 otherwise
(4)
This formulation captures how industry certifications enhance university education:
foundational degree skills maintain their importance, certification-specific skills receive
weights reflecting their industry relevance, and overlapping skills gain enhanced impor-
tance—representing both theoretical foundations and practical applications.
7

3.4 Quantifying Certification Impact on Job Alignment
To measure precisely how industry certifications enhance employment readiness, we anal-
yse the transformation in skill set similarity when certification skills are added to univer-
sity degrees:
For a degree skill setS1 and job role skill setT, the baseline similarity is:
Θ(S1, T) = 1 C X s1∈S1 X t∈T w(s1, S1) · w(t, T) · θ(s1, t) (5)
With normalisation constantC = P s1∈S1 P t∈T w(s1, S1) · w(t, T)
For the certification-enhanced skill setS′ 1:
Θ(S′ 1, T) = 1 C ′ X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T) · θ(s′, t) (6)
Through mathematical derivation (see the full derivation in Appendix A), we can
express this relationship as:
Θ(S′ 1, T) = C C ′ · Θ(S1, T) + 1 C ′ X s∈S2 X t∈T wT (s, S2) · w(t, T) · θ(s, t) (7)
Where C ′ = C + P s∈S2 P t∈T wT (s, S2) · w(t, T)
This equation reveals critical insights about certification impact:
• When certification skills align well with job requirements (θ(s, t) is high), the com-
bined similarity Θ(S′ 1, T) significantly exceeds the baseline degree-only similarity
• When certification skills have minimal relevance to target jobs (θ(s, t) ≈ 0), the
combined similarity may actually decrease, asΘ(S′ 1, T) ≈ C C′ Θ(S1, T) < Θ(S1, T)
since C C′ < 1
This mathematical framework explains our empirical findings in Section 5 that non-
technical degrees (like nursing) show dramatic improvement when combined with AI cer-
tifications, while technical degrees show more modest gains. It also explains why irrele-
vant certifications can theoretically reduce job alignment—the denominator (C ′) increases
without a corresponding increase in skill alignment.
This insight emphasises the importance of strategic certification selection aligned with
specific career objectives and provides a theoretical basis for our measured improvements
in degree-job alignment across different educational backgrounds.
4 Analysis Framework and Data Sources
This section introduces the analysis framework and datasets required to quantify skill
alignment between educational offerings and job market requirements. Section 4.1 in-
troduces the overall approach; next we introduce the data sources and their processing.
Section 4.2 introduces the online job ads dataset that captures the market requirements,
and Sections 4.3 and 4.4 introduce, respectively, the industry certifications and university
degrees datasets which capture the educational offers we consider.
8

Analysis Framework for Measuring Certification Impact
University Degree
Programs
Skill sets from curricula
Industry
Certifications
AI-102, AI-900, etc.
Job Advertisements
2.5M job postings
Skill Extraction
SkillNER Named Entity Recognition
Mapping to Lightcast Open Skills Taxonomy
Vectorised Skills Space Method (VSSM)
Revealed Comparative Advantage (RCA)
Skill Similarity Matrix
Skill Set Similarity Calculation
Baseline Similarity Calculation
Degrees to Job Roles
Augmented Similarity Calculation
Degrees + Certifications to Job Roles
Skill Alignment Weakness Analysis
Identifying Specific Skill Contributions
Key Formulas
SSS(A,B) = similarity score
A(s,S,T) = skill alignment
W(s,S,T) = skill weakness
Figure 1: System architecture for skill alignment analysis and decision support.
4.1 Analysis Framework
Fig. 1 shows our methodology to quantify the impact of industry certifications when
combined with university degrees. This approach allows for both theoretical assessment
and real-world application. The input data for the Skill Space Method (see Section 3.1)
comprises skills extracted from online job advertisements (market requirements) and ed-
ucational offerings (industry certifications and university degrees). Our analysis follows a
systematic process:
1. Baseline skill set establishment: We first identify and quantify the skill sets
provided by university degree programs, establishing a foundation for comparison.
2. Certification augmentation:We then calculate the additional skills provided by
industry certifications and modeled how these skills integrate with existing degree-
based skills.
3. Job market alignment:Using the Vector Skill Set Similarity (VSSM) calculation,
we determine the alignment between these combined skill sets and contemporary job
requirements.
4. Skill decomposition: Finally, we identify specific skills contributing to alignment
or misalignment, providing granular insights for curriculum development.
4.2 Data Source: Online Job Ads
We built and analysed a comprehensive dataset of2, 506, 589 job advertisements posted
between June 2023 and June 2024. The dataset spans three economically developed
9

English-speaking countries: Australia (2, 053, 903 listings), the United States (410, 982),
and the United Kingdom (42, 103). This multi-national approach strengthens our analy-
sis by capturing broader skill patterns across culturally and economically similar labour
markets.
SkillExtractionProcess. Weemployedacustomskillextractionpipelinebuiltaround
the open-source SkillNER package to identify skills from job descriptions. SkillNER func-
tions as a specialised rule-based natural language processing module designed specifically
for extracting professional skills and certifications from unstructured text such as job
postings and resumes [Aito, 2022]. SkillNER leverages the SpaCy framework with large
language models for initial named entity recognition, followed by semantic textual simi-
larity techniques to map identified skill phrases to standardised terminology. Extracted
skills are then aligned with the Lightcast Open Skills taxonomy, a comprehensive classi-
fication system containing over33, 000 unique skills organised in hierarchical categories
[Lightcast, 2025]. This structured taxonomy, updated monthly to reflect emerging labour
market trends, provides a standardised vocabulary for workforce analysis and enables
precise comparison between educational offerings and industry requirements. From our
dataset of 2.5 million job advertisements, we identified11, 210 unique skills across var-
ious industries and experience levels. The job descriptions provided sufficient detail for
effective skill extraction, with a median word count of327 (standard deviation =289.65,
interquartile range =142 − 522).
Dataset Profiling. The dataset exhibits diversity across industries and experience lev-
els. Fig. 2 illustrates the distribution across industry sectors, with Information Technology
(381, 877), Staffing and Recruiting (178, 133), and Hospital & Health Care (122, 607) most
prominently represented. The remaining sectors show a more uniform distribution ranging
from approximately 19, 000 to 75, 000 advertisements each.
Experience requirements, presented in Fig. 3, demonstrate a balanced representation
across career stages. Of the 564, 584 listings (22.52% of total) that explicitly specified
minimum experience requirements, most positions clustered around early to mid-career
levels (1-5 years). The distribution is characterised by quartile values of1.0 (Q1), 2.0
(median), and 5.0 (Q3) years, with a mean of3.08 years slightly skewed by senior-level
positions requiring 10+ years of experience.
For each job advertisement, we stored both extracted skills and relevant metadata,
particularly job titles, enabling systematic grouping and comparison of skill sets across
different roles. This structured approach facilitates the application of our skill similar-
ity methodology to compare contemporary job market requirements against educational
offerings detailed in the next sections.
4.3 Data Source: University Degrees Programs
We constructed a comprehensive dataset of degree programs and their constituent courses
and subject from a medium-sized Australian university. Each subject, course and degree
is annotated with the skills that it provides to the students.
10

0k
100k
200k
300k
400k
Number of Jobs
Information Technology and Services
Staffing and RecruitingHospital Health Care
Government Administration
Oil Energy
Retail
Human Resources
Education Management
ConstructionMining Metals
Financial Services
Hospitality
Nonprofit Organization Management
Marketing and Advertising
Internet
Health, Wellness and Fitness
Higher EducationComputer Software
AutomotiveReal Estate
Figure 2: Top 20 Industry Sectors by Number of Job Advertisements
Number of Job Advertisements
Years of Experience Required
0
20K
40K
60K
80K
100K
120K
140K
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16+
30K
125K
135K
103K
23K
90K
8K 10K 10K
~0
17K
2K 1K ~0 ~0 3K 1K
Figure 3: Distribution of Experience Requirements in Job Advertisements
11

4.3.1 Dataset Construction
Educational offering structure. The educational offering follows a hierarchical model
where degrees are composed of courses, and courses comprise individual subjects. Each
subject includes lectures and practical tutorial sessions, with subjects potentially offered
across multiple courses and degrees. For example, the Bachelor of Computing Science
(denoted as BCS) includes core subjects such as Discrete Mathematics, Programming 2,
Data Structures and Algorithms, and Theory of Computing Science, alongside several
specialised majors. The BCS Enterprise Software Development major (denoted as BCS
(ESD))encompassessubjectslikeIntroductiontoSoftwareDevelopment, Fundamentalsof
Interaction Design, Advanced Software Development, and Software Architecture, comple-
mented by optional subjects such as Advanced Algorithms, Advanced Interaction Design,
Advanced Internet Programming, Application Development in the iOS Environment, and
Application Development with .NET.
Data collection and skill extraction. We systematically crawled the university’s
public-facing course handbook website, where each degree, course, and subject is de-
scribed. For each academic offering, we extracted detailed information including: (1)
subject descriptions and learning outcomes, (2) availability schedules (semester offerings),
(3) learning and teaching activities, (4) assessment methodologies, (5) prerequisites and
corequisites, and (6) additional subject-specific details.
We use SkillNER (see Section 4.2) to extract skills from the description of each subject,
interpreting these as the competencies taught within that subject. The complete skill set
for each degree program was constructed as the union of skills present in: (1) core subjects
required for degree completion, (2) core subjects within the chosen major specialisation,
and (3) all available elective subjects.
We note that while students typically select electives up to a specified credit point limit
(24 credit points for BCS (ESD)), we included all elective options in our analysis as we
lack access to enrollment statistics to predict student choices. Our investigation revealed
that elective subjects typically demonstrate high skill overlap, mitigating potential bias
from this methodological choice.
Degree programs. For this work, we selected four representative undergraduate
degree programs:
BCS (AI) Bachelor of Computing Science with Artificial Intelligence and Data An-
alytics major
BCS (ESD) Bachelor of Computing Science with Enterprise Software Development
major
BEng Bachelor of Engineering (Honours) with Mechanical Engineering major
BNur Bachelor of Nursing
We chose these programs to examine certification impact across a diverse educational
spectrum: two programs within information technology, one adjacent STEM discipline
(engineering), and one completely distinct field (nursing).
4.3.2 Dataset Profiling
Our dataset encompasses significant diversity in both scope and specialisation across the
four degree programs, as illustrated in Fig. 4.
12

Dataset Overview. As shown in Fig. 4a, the degree programs demonstrate substantial
variation in skill set sizes. The Bachelor of Engineering contains the largest skill repository
with 491 unique skills across1, 253 total instances, while the Bachelor of Nursing repre-
sents the most focused program with68unique skills distributed across341instances. The
two Computer Science programs occupy an intermediate position, with Enterprise Soft-
ware Development encompassing256 unique skills (504 total instances) and the Artificial
Intelligence specialisation containing135 unique skills (259 total instances).
Aggregate statistics reveal (1)759 total unique skills across all programs, (2)2, 357
total skill instances (including repetitions), (3)589.3 average skills per program, and (4)
145 skills (19.1%) appear in multiple programs (cross-program skill overlap).
Skill Repetition Patterns. The dataset exhibits varying levels of skill duplication
within programs, ranging from 47.9% (CS AI) to 80.1% (Nursing), reflecting curricular
emphasis and structural differences across disciplines. The substantial variation in skill
set sizes shown in Fig. 4a demonstrates how different programs emphasise skill breadth
versus depth. Higher repetition rates in nursing indicate concentrated skill reinforcement
in core competencies, while lower rates in computer science suggest broader skill diversity
across the curriculum.
Domain Distribution. Fig. 4b presents the categorical distribution of skills across
major domains. The analysis reveals that over half of all skills (52.0%, 395 skills) fall
into specialised domains beyond the main technical categories, highlighting the diverse
nature of modern degree programs. The primary technical categories show: Engineering
& Technology leads with154 skills (20.3%), followed by Computer Science with61 skills
(8.0%), Data & Analytics with56 skills (7.4%), Business & Management with56 skills
(7.4%), and Healthcare & Nursing with37 skills (4.9%). This distribution underscores
the multidisciplinary nature of contemporary higher education, where technical skills are
complemented by substantial components from business, communication, and domain-
specific areas.
Technology Specificity The dataset includes only 10 technology-specific skills (1.3%),
referencing particular platforms, tools, or vendors (Microsoft, IBM, iOS, HTML, etc.),
providing granular detail for technical competencies essential in contemporary professional
environments. This low proportion of vendor-specific skills indicates that university pro-
grams maintain a platform-agnostic approach, concentrating on fundamental technologies
and foundational approaches rather than training students on specific commercial tools
or proprietary systems.
Program-Specific Skill Profiles. Each degree program demonstrates distinct skill
emphases aligned with their respective domains:
• BEng: Predominantly technical skills (25.5% engineering-specific, 8.8% business &
management)
• BNur: Highly specialised healthcare focus (50.0% healthcare-specific skills)
• BCS(ESD): Balancedtechnicalprofile( 17.2%engineering/technology, 13.3%com-
puter science)
13

Number of Skills
0
250
500
750
1000
1250
BEng BNur CS (ESD) CS (AI)
Unique Skills
Total Skill Instances
491
1,253
68
341
256
504
135
259
Skills in Bachelor's Degree Program
(a)
Skill Categories
Number of Skills
0
100
200
300
400
Engineering &
T echnology
Computer
Science
Data &
Analytics
Business &
ManagementHealthcare &Nursing
Other
Specialized
154
(20.3%)
61
(8.0%)
56
(7.4%)
56
(7.4%) 37 (4.9%)
395
(52.0%) (b)
Figure 4: Skill analysis across degree programs and categories.(a) Comparison
of skill counts across different bachelor’s degree programs demonstrates the substantial
variation in skill set sizes, with Engineering having the largest and Nursing the smallest
skill sets. (b) Distribution of skills across major categories reveals that over half of all
skills (52.0%) fall into specialised domains beyond the main technical categories.
• BCS (AI):Data-centric specialisation (17.0% data/analytics, 11.9% engineering &
technology)
Cross-Program Skill Overlaps. Our analysis reveals 145 skills shared across mul-
tiple programs, with the most frequent being foundational competencies, such as Prob-
lem Solving (94 instances across programs), Decision Making (85 instances), FourGen
Computer-Aided Software Engineering (CASE) Tools (70 instances), Learning Strategies
(64 instances), and System Requirements (48 instances).
The Jaccard similarity analysis confirms minimal skill overlap between programs, sup-
porting our hypothesis that degrees provide largely distinct skill sets. BCS (AI) and BCS
(ESD) have only15.0% skill overlap. This indicates that even within the same discipline,
different tracks provide largely distinct competencies. While some foundational skills (In-
formation Technology, Computer Science, Problem Solving, and Artificial Intelligence)
are shared, the majority of skills are specialised to each track’s focus area. Other pro-
grams pairs show similar trends: BEng and BCS (ESD) have17.8% overlap, while BEng
and BCS (AI) have9.2% overlap. Finally, BNur is distinct from all other programs with
< 3.2% similarity
4.4 Data Source: Microsoft Industry Certifications
For the purpose of this work, we focus on the Microsoft certification AI-900 (Azure AI
Fundamentals). The Microsoft Azure AI-900 certification is designed to validate an in-
dividual’s skills and knowledge in artificial intelligence (AI) and machine learning (ML)
technologies on the Microsoft Azure platform. This certification caters to foundation level
of expertise and focus on distinct aspects of AI implementation.
The Microsoft Azure AI Fundamentals certification (AI-900) is a foundational-level
coursedesignedtointroducelearnerstoartificialintelligence(AI)conceptsandthevarious
AI services available through Microsoft Azure [K21Academy, 2025]. This certification is
particularly valuable for individuals seeking to enhance their understanding of AI without
14

Aspect AI-900
Level Beginner
Target Audience Technical and non-technical roles
Focus Broad overview of AI concepts
Depth of Technical Knowledge Basic
Hands-on Experience Required Minimal
Table 1: Microsoft Azure AI-900 Certification Overview
requiring extensive technical expertise, making it accessible to a broad audience including
students, business professionals, IT experts, and developers [CertEmpire, 2025].
Accessibility and Prerequisites One significant advantage of the AI-900 certification
is its accessibility; it has no formal prerequisites. However, basic familiarity with cloud
computing concepts can be beneficial for participants [CertEmpire, 2025]. This makes the
course ideal for non-technical professionals who wish to develop foundational knowledge
in AI technologies.
Benefits of the AI-900 CertificationThe Microsoft Azure AI Fundamentals certifi-
cation offers several key benefits:
1. Foundational Knowledge: It provides participants with a solid grounding in
essential AI concepts which can serve as a stepping stone towards more advanced
certifications such as Azure AI Engineer Associate (AI-102) or Azure Data Science
Associate (DP-100)
2. Industry Recognition: Microsoft certifications are widely recognised by employ-
ers globally, enhancing employability by demonstrating verified knowledge in AI
fundamentals
3. Career Opportunities: Even at an entry-level certification stage, it opens op-
portunities in roles such as AI business analysts or cloud consultants where an
understanding of AI principles is beneficial
4. Accessibility for Non-Technical Professionals:The absence of prerequisites
makes it suitable for professionals from diverse backgrounds who aim to incorporate
AI into their business operations or career paths
5. Hands-on Experience with Azure Services: Participants gain practical ex-
posure to Azure’s leading-edge technologies including Machine Learning services,
Cognitive Services for NLP and computer vision tasks, and conversational agents
like chatbots
Relevance to Educational Programs and Employment OutcomesIn the context
of enhancing educational programs and employment outcomes through industry-based
certifications—a primary focus of our research—the Microsoft Azure AI Fundamentals
(AI-900) certification aligns effectively by providing measurable impacts on employability
15

and foundational skill development. According to recent insights from Microsoft Edu-
cation initiatives, incorporating certifications like the AI-900 significantly contributes to-
wards preparing an AI-skilled workforce capable of thriving in an increasingly technology-
driven job market [Microsoft, 2025]. Such credentials not only validate proficiency but
also enhance employment opportunities by equipping learners with industry-recognised
skills that employers value.
5 Results and Analysis
This section presents our empirical findings on the impact of industry certifications when
combined with university degrees. It applies the methodology established in Section 3
to the datasets described in Section 4. We begin by establishing baseline skill alignment
measurements between university degrees and junior AI roles (Section 5.1), providing the
foundation for subsequent impact analysis. We then quantify how industry certifications
enhance these alignments (Section 5.2), revealing both expected improvements and sur-
prising patterns across different educational backgrounds. Finally, we investigate an un-
expected phenomenon whereby non-technical degrees experience dramatic improvements
when augmented with AI certifications (Section 5.3), challenging conventional assump-
tions about technology career pathways and skill development strategies.
5.1 Baseline Skill Set Similarity
This section establishes baseline measurements by computing the Skill Set Similarity
(Eq. (1)) between our four selected university degrees and representative junior AI roles.
To provide context, we also include the skill similarity of the AI-900 certification for direct
comparison. We select six representative roles spanning AI and software engineering that
require minimal prior expertise, as illustrated in Fig. 3. We use our Vectorised Skills Space
Method (VSSM) computation (see Section 3.1), and we present the results in Table 2.
Table 2: The Skill Set Similarity (see Eq. (1)) of Undergraduate Degrees and AI-900 (in
columns) to Junior AI Roles (in lines). The background color indicate the range between
lowest similarity (white background) to highest similarity (blue). All values should be
read multiplied by10−4.
Role BNur BEng BCS (ESD) BCS (AI) AI-900
Software Engineer 1.96 8.50 21.70 13.71 18.61
AI Software Engineer 0.80 4.74 9.69 6.81 11.21
Data Engineer 2.60 5.72 13.07 15.24 36.73
Data Scientist 0.39 4.18 9.63 10.91 39.96
Machine Learning Engineer 0.53 2.21 5.88 48.13 85.87
Data Analyst 2.27 4.14 6.59 10.39 9.03
Our analysis of undergraduate degrees reveals varied alignment with junior AI roles.
TheBachelorofComputerSciencewithAImajor(BCS(AI))producesthehighestskillset
similaritytoanyjuniorAIrole, achievingasimilarityscoreof 48.13withMachineLearning
Engineer positions. This result aligns with expectations, as the AI major specifically
targets data and machine learning competencies that directly correspond to contemporary
industry requirements.
16

The data reveal distinct specialisation patterns across degree programs. For data-
focused and machine learning roles (Data Engineer, Data Scientist, Data Analyst, and
Machine Learning Engineer), BCS (AI) consistently demonstrates the strongest align-
ment. Conversely, formoregeneralisedsoftwaredevelopmentpositions(SoftwareEngineer
and AI Software Engineer), BCS (ESD) exhibits superior skill similarity. This differen-
tiation reflects the targeted nature of university specialisations and their alignment with
specific career pathways.
The Bachelor of Engineering with Mechanical major (BEng) occupies an intermediate
position across all roles, demonstrating moderate skill similarity that reflects the math-
ematical and analytical foundations common to engineering disciplines. As anticipated,
the Bachelor of Nursing shows the lowest overall skill set similarity across all AI roles,
which is intuitive given its primary focus on biological sciences and medical practice rather
than the computational and statistical foundations prevalent in technology roles.
AsurprisingfindingemergeswhenexaminingtheAI-900certificationinisolation. This
industry certification alone demonstrates higher skill similarity to several junior AI roles
than many complete undergraduate degrees. For Machine Learning Engineer positions,
AI-900 achieves a similarity score of 85.87, exceeding even BCS (AI)’s score of 48.13.
Similarly, for Data Scientist roles, AI-900 outperforms all undergraduate degrees with
a score of 39.96, compared to BCS (AI)’s score of10.91. For Data Engineer positions,
AI-900 records a similarity of36.73, surpassing all degrees except the BCS with AI major.
This finding proves particularly significant as it demonstrates that a focused indus-
try certification can potentially provide more relevant skills for specific AI roles than
entire undergraduate degree programmes. The result underscores the value of targeted
certification pathways, especially for professionals seeking to transition into specialised
AI careers. However, it is important to acknowledge that direct comparison between a
targeted industry certification and an entire undergraduate degree programme is not en-
tirely equitable. Bachelor’s degrees, particularly in computing disciplines, must devote
substantial curriculum to fundamental skills such as mathematics, algorithms, and theo-
retical computer science. While these foundational skills may not appear directly in job
requirements for junior roles, they constitute necessary dependencies for more specialised
skills and provide the conceptual groundwork for long-term career development. Industry
certifications, by design, can focus exclusively on immediately applicable skills precisely
because they build upon this foundational knowledge, rather than needing to establish it
from first principles.
5.2 Impact of Industry Certifications
This section measures the impact of adding industry certifications to university degrees
on skill alignment with junior AI roles. We apply our proposed approach for combining
skill sets (see Section 3.3) to quantify the effect of augmenting each of the four university
degrees with the AI-900 certification. The enhanced skill similarities are presented in
Table 3, with percentage improvements detailed in Table 4.
Table 3 quantifies how Microsoft’s AI-900 certification affects skill matching when
added to undergraduate degrees. As expected, BCS (AI) plus AI-900 achieved the highest
absolute score at59.01 × 10−4 for Machine Learning Engineer roles, which is logical given
that adding AI-specific certifications to AI-focused undergraduate training should yield
the strongest alignment with AI-specific positions.
However, Table 4 reveals a more nuanced and intriguing story by examining the per-
17

Table 3: Skill set similarity between roles (in lines) and the Undergraduate Degrees en-
hanced with the AI-900 certification.
Role BNur +
AI-900
BEng +
AI-900
BCS (ESD)
+ AI-900
BCS (AI)
+ AI-900
Software Engineer 10.66 13.06 23.72 20.17
AI Software Engineer 6.27 7.35 11.40 11.07
Data Engineer 20.84 16.52 23.16 27.98
Data Scientist 19.78 13.21 16.80 21.10
Machine Learning Eng. 49.80 31.36 40.51 59.01
Data Analyst 6.09 6.34 8.87 11.37
Table 4: Percentage Increase in Skill Set Similarity with AI-900
Role BNur BEng BCS (ESD) BCS (AI)
Software Engineer 444% 54% 9% 47%
AI Software Engineer 684% 55% 18% 63%
Data Engineer 702% 189% 77% 84%
Data Scientist 4972% 216% 74% 93%
Machine Learning Engineer 9296% 1337% 589% 23%
Data Analyst 168% 53% 35% 9%
centage increase in skill set similarity after adding the AI-900 certification to undergrad-
uate degrees (compared to the baseline similarities shown in Table 2). Nursing graduates
experienced extraordinary improvements: 9296% for Machine Learning Engineer,4972%
for Data Scientist, and702% for Data Engineer roles. We analyse this “nursing anomaly”
in detail in Section 5.3. In contrast, technical degrees showed more modest gains—BCS
(AI) improved by only 23% for Machine Learning Engineer roles despite achieving the
highest absolute score.
A clear pattern emerges across role types. AI-focused positions (Machine Learning
Engineer, Data Scientist) benefited substantially more from AI-900 certification than
traditional software development roles. This observation, combined with the alignment
scores in Table 2, suggests the certification is particularly well-suited to these emerging
technical positions. Software engineering roles showed smaller improvements because
computer science degrees already provide substantial relevant skills, and because AI-900
is less tailored towards these established roles.
5.3 The "Nursing Anomaly"
An unexpected finding emerges from our analysis. The Bachelor of Nursing (BNur) gradu-
ates, when combined with AI-900 certification, demonstrate higher skill similarity to data
and AI roles than BEng or BCS (ESD) graduates. This counterintuitive result challenges
conventional assumptions about technology career pathways and warrants more detailed
investigation.
Several interconnected factors contribute to this phenomenon. The most significant
relates to skill set size differences across degree programmes. The BNur comprises only
68 unique skills, substantially fewer than BEng (491 skills), BCS (ESD) (256 skills), and
18

Table 5: Top Skills by Alignment Score for Bachelor of Nursing + AI-900 by Junior AI
Role
Role Skill Alignment Score
Software Engineer
Application Programming Interface (API) 25.77
C# Programming Language 25.76
Software Development 15.43
Back End Software Engineering 5.69
Systems Integration 4.31
Data Engineer
Azure Machine Learning 28.9
Data Store 7.23
Data Discovery 7.21
Knowledge Graph 6.92
Source Data 6.49
ML Engineer
Azure Machine Learning 222.91
Gradient Boosting 107.23
Natural Language Processing 73.58
Text Mining 46.2
Topic Modeling 41.16
AI Software Engineer
C# Programming Language 16.94
Information Retrieval 7.69
Software Development 6.24
Artificial Intelligence 4.05
Code Review 3.59
Data Analyst
Applied Mathematics 7.53
Extract Transform Load (ETL) 5.3
Power BI 1.72
Cardiac Monitoring 1.55
Data Analysis 1.46
Data Scientist
Machine Learning 19.55
Linear Regression 15.24
Data Science 11.09
Artificial Intelligence 8.94
Algorithmic Trading 6.62
19

BCS (AI) (135 skills). This size disparity creates a proportional impact whereby AI
certification skills represent a much larger proportion of nursing graduates’ total skill set
after augmentation, as described by our skill combination methodology in Section 3.3.
Our mathematical framework (Section 3.4) explains this effect. When certification
skills align well with job requirements, smaller baseline skill sets experience more dramatic
relative improvements. For nursing graduates, the AI-900 certification effectively doubles
their technical skill repertoire, while for engineering or computer science graduates, the
same certification represents a smaller proportional enhancement to an already substantial
skill base.
Unexpectedly, certain nursing skills demonstrate meaningful alignment with data and
AI positions. "FourGen Computer-Aided Software Engineering (CASE) Tools" appears
in 31 times in BNur subjects within our dataset, reflecting the increasing digitalisation
of healthcare systems. Similarly, “Critical Thinking” appears 14 times, representing a
transferable analytical skill highly valued in data science roles. These findings suggest that
modern nursing education incorporates more technological and analytical components
than traditional perceptions might indicate.
To understand the specific contributions of this skill combination, we examine the
latent skill alignment between BNur plus AI-900 and various AI roles. Table 5 presents
the top five skills by alignment score for each role when considering the combined nursing
and AI-900 skill set, using the alignment approach defined in Section 3.2.
The analysis reveals three important insights. First, the highest alignment scores con-
sistently derive from technical skills introduced through the AI-900 certification. “Azure
Machine Learning” achieves an alignment score of222.91 for Machine Learning Engineer
roles, demonstrating how industry certifications can rapidly introduce highly relevant
technical competencies to non-technical degree backgrounds.
Second, healthcare-specificknowledgedemonstratesunexpectedtransferabilitytotech-
nology roles. “Cardiac Monitoring” appears as a relevant skill for Data Analyst positions
with a small, but meaninful alignment score of1.55, illustrating how domain expertise
from nursing can transfer to data-focused positions. This suggests that healthcare profes-
sionals possess valuable analytical and monitoring skills that translate effectively to data
science contexts, particularly in health informatics and medical data analysis.
Third, nursing education’s emphasis on quantitative analysis and precise measurement
provides a solid foundation for data-oriented roles. “Applied Mathematics” achieves an
alignment score of 7.53 for Data Analyst positions, reflecting the statistical and mathe-
matical components inherent in modern nursing education. This quantitative foundation,
combined with critical thinking skills developed through clinical practice, creates an un-
expectedly strong basis for data science competencies.
This finding challenges fundamental assumptions about which degrees benefit most
from industry certifications and suggests promising alternative pathways into AI careers.
Healthcare professionals who combine domain expertise with targeted technical certifi-
cations may represent an untapped talent pool for technology roles, particularly in sec-
tors where healthcare knowledge provides competitive advantage. The results suggest
that universities and industry partners should consider developing specialised technology
tracks within healthcare programmes, while employers should recognise the potential in
candidates from non-traditional backgrounds who have obtained relevant certifications.
20

6 Discussion, Limitations and Future Work
Our analysis reveals fundamental insights about how industry certifications can trans-
form educational pathways and employment outcomes. The findings challenge traditional
assumptions about technology career preparation and suggest concrete strategies for ad-
dressing Australia’s critical skills shortage.
6.1 Transforming Educational Programs
The quantified impact of industry certifications provides compelling evidence for edu-
cational reform. Our results demonstrate that strategic integration of industry-applied
skills can dramatically enhance graduate employability, particularly when implemented
thoughtfully across diverse disciplines.
Curriculum Integration Strategies.Universities could move beyond viewing certi-
fications as supplementary credentials and instead embed them as integral components of
degree programs. The dramatic improvements observed across all degree types—ranging
from 9% to over 9000% increases in job alignment—indicate that certification integration
represents a systematic opportunity rather than a marginal enhancement. This inte-
gration should be particularly prioritised in non-technical disciplines, where our analysis
shows the most substantial relative gains.
Cross-Disciplinary Innovation. The nursing anomaly reveals untapped potential
for technology career pathways from unexpected educational backgrounds. The find-
ing that nursing graduates combined with AI-900 certification outperformed engineering
graduates in several AI roles suggests universities should develop specialised technology
tracks within traditionally non-technical programs. Healthcare informatics, educational
technology, and business analytics represent natural interdisciplinary bridges where do-
main expertise combined with targeted technical certifications can create unique value
propositions.
Data-Driven Curriculum Development. Our skill decomposition methodology
provides educational institutions with precise tools for identifying and addressing skill
gaps. Rather than relying on industry feedback or graduate surveys, institutions can now
quantifyspecificcompetencydeficienciesanddesigntargetedinterventions. Thisapproach
enables continuous curriculum optimisation based on evolving job market requirements,
ensuring graduates remain competitive in rapidly changing technological landscapes.
6.2 Career Development
Our findings reshape how individuals should approach career development and transition
planning in technology sectors.
Evidence-Based Certification Selection. The traditional approach of pursuing
prestigious or popular certifications should be replaced with strategic, data-driven selec-
tion based on quantified skill alignment with target roles. Our analysis demonstrates
that certification value varies dramatically depending on educational background and ca-
reer objectives. For instance, while AI-900 provides modest improvements for computer
science graduates (23% for Machine Learning Engineer roles), it delivers extraordinary
enhancements for nursing graduates (9296% for the same roles).
Alternative Career Pathways.The research validates non-traditional routes into
technology careers, particularly for healthcare and other domain specialists seeking tech-
nology transitions. The discovery that nursing education provides unexpected founda-
21

tions for data analysis roles—through critical thinking, applied mathematics, and sys-
tematic measurement approaches—suggests that career changers should leverage rather
than abandon their domain expertise when entering technology fields.
Targeted Skill Investment.Our granular skill alignment analysis enables individu-
als to identify specific competency gaps and invest learning resources strategically. Rather
than pursuing broad technology education, professionals can focus on targeted certifica-
tions that address precise weaknesses in their skill profiles relative to desired roles.
6.3 Industry Transformation and Talent Acquisition
The implications for employers and industry stakeholders extend beyond traditional hiring
practices to fundamental rethinking of talent identification and development.
Expanding Talent Pipelines.Our findings provide quantitative evidence for recog-
nising potential in candidates from non-traditional educational backgrounds who have
obtained relevant certifications. This is particularly critical given Australia’s projected
need for 52, 000 new technology professionals annually by 2030. By broadening talent
recognition beyond computer science and engineering graduates, organisations can access
previously overlooked candidate pools while addressing diversity and inclusion objectives.
Skills-Based Assessment. The research supports shifting hiring practices from
credential-based screening to skill alignment assessment. Our methodology enables or-
ganisations to evaluate candidates based on quantified competency matches rather than
degree prestige or traditional educational pathways. This approach can improve hiring
effectiveness while reducing bias against non-traditional candidates.
Precision Training Programs. Organisations can leverage our skill decomposi-
tion analysis to design targeted upskilling programs that address specific competency
weaknesses. Rather than implementing broad training initiatives, companies can develop
precise interventions that maximize return on training investment while accelerating em-
ployee transition into high-demand roles.
6.4 Broader Implications for Skills Policy
The research contributes to broader discussions about education policy and workforce
development in Australia’s evolving economy.
Public-Private Collaboration. The demonstrated value of industry certifications
suggests enhanced collaboration opportunities between educational institutions and tech-
nology companies. Government policy could incentivise such partnerships through fund-
ing mechanisms that support certification integration in degree programs, particularly in
universities serving diverse student populations.
Workforce Transition Support.The finding that career changers from healthcare
and other disciplines can successfully transition into technology roles with targeted certi-
fication support suggests opportunities for government-funded reskilling programs. These
programs could specifically target professionals in declining industries or those seeking
career advancement, providing pathways into high-demand technology roles.
Regional Development. The accessibility of industry certifications, particularly
foundational programs like AI-900 that require minimal prerequisites, suggests opportu-
nities for technology workforce development in regional areas where traditional computer
science education may be limited. This could contribute to addressing both regional
economic development and national skills shortage challenges.
22

6.5 Addressing Limitations and Future Considerations
While our findings provide robust evidence for certification value, several methodological
limitations merit consideration for practical implementation and future research direc-
tions.
Methodological Constraints. Our reliance on existing skill taxonomies may not
capture rapidly emerging competencies, and the static nature of our model does not ac-
count for evolving skill relationships over time. Additionally, skill similarity alone repre-
sents one dimension of job readiness—factors such as communication abilities, cultural fit,
and leadership potential remain important considerations that complement quantitative
skill alignment measures.
Geographic and Temporal Scope.This study focuses mainly on the Australian
market. This suggests that findings may require validation in other geographic contexts
before broad generalisation, though our methodology provides a transferable framework
for similar analyses in different labour markets. The mathematical framework also reveals
that irrelevant certifications can theoretically decrease job alignment, emphasizing the
critical importance of strategic selection rather than credential accumulation.
Future Research Priorities.Key extensions include multivariate optimisation in-
corporating variables beyond skill similarity, longitudinal analyses tracking employment
outcomes to validate predictive power, and broader certification analysis encompassing
AWS, Google, and Cisco credentials. We are particularly focused on developing per-
sonalised recommendation systems that leverage predictive analytics and real-time mar-
ket analysis to guide strategic certification selection based on individual academic back-
grounds and career aspirations.
References
Anas Aito. Skillner: A (smart) rule based nlp module to extract job skills from text,
2022. URL https://github.com/AnasAito/SkillNER. Accessed: May 16, 2025.
Associations Forum. Just 1pc of aussie tech graduates ready for work,
2024. URL https://associations.net.au/news/sector-news/2024/
just-1pc-of-aussie-tech-graduates-ready-for-work.html .
AustralianComputerSociety. Digitalpulsereport. Technicalreport, AustralianComputer
Society, 2024. URL https://www.digital.tas.gov.au/__data/assets/pdf_file/
0019/408331/ACS-DigitalPulse-2024_digital.pdf.
AWS Training and Certification Blog. Aws training and cer-
tification provide positive roi to learners, 3 2022. URL
https://aws.amazon.com/blogs/training-and-certification/
aws-training-and-certification-provide-positive-roi-to-learners/ .
M. Bean and P. Dawkins. Review of university-industry collaboration in teach-
ing and learning. Technical report, Department of Education, Skills and Em-
ployment, 12 2021. URL https://www.education.gov.au/download/12973/
university-industry-collaboration-teaching-and-learning-review/24823/
university-industry-collaboration-teaching-and-learning-review/pdf .
23

J. Belanich, E. A. Fedele, C. Dobbins, J. E. Morrison, F. L. Moses, and P. Madha-
van. Impact of professional credentials on employability. Technical report, Institute
for Defense Analyses, 2019. URL https://www.researchgate.net/publication/
334170431_Impact_of_Professional_Credentials_on_Employabili.
L. Brown. New research from think education shows that being ’work-ready’ is what
young australians want from their education, 3 2019. URLhttps://www.think.edu.
au/blog/education-must-make-students-work-ready.
CertEmpire. Everything you need to know about the ai-900 certification exam, 2 2025.
URL https://certempire.com/ai-900-certification-exam-guide/.
Certiport. The value of certification. URLhttps://certiport.pearsonvue.com/About/
The-value-of-certification.aspx.
Kevin R. Cook. Relationship between secondary industry certifications and employment
in the particular credentialed area. Master’s thesis, Eastern Kentucky University, 2021.
URL https://encompass.eku.edu/etd/701.
Nicholas Dawson, Mary-Anne Williams, and Marian-Andrei Rizoiu. Skill-driven rec-
ommendations for job transition pathways. PLOS ONE, 16(8):e0254722, 2021. doi:
10.1371/journal.pone.0254722.
Global Knowledge. Which aws certification should i choose?, 11 2024. URL
https://www.globalknowledge.com/us-en/resources/resource-library/
articles/which-aws-certification-should-i-choose/.
JobsandSkillsAustralia. Vetworkforcestudy2024. Technicalreport, JobsandSkillsAus-
tralia, 10 2024. URL https://www.jobsandskills.gov.au/sites/default/files/
2024-10/vet_workforce_study_2024.pdf.
K21Academy. How to pass azure ai-900 certifica-
tion, 2 2025. URL https://www.linkedin.com/pulse/
how-pass-azure-ai-900-certification-k21academy-g41jf/ .
S. Lamb, S. Huo, A. Walstab, A. Wade, Q. Maire, E. Doecke, J. Jackson, and Z. En-
dekov. Educational opportunity in australia 2020: Who succeeds and who misses out.
Technical report, Centre for International Research on Education Systems, Victoria
University, for the Mitchell Institute, 2020. URLhttps://vuir.vu.edu.au/42362/1/
educational-opportunity-in-australia-2020.pdf.
Lightcast. Open skills library, 2025. URL https://lightcast.io/open-skills. Ac-
cessed: May 16, 2025.
Quinn McAndrew. Leveraging industry content to boost global degree out-
comes: Awarding credit for industry certificates drives recruitment, value, and
employment. URL https://www.coursera.org/partnerships/resources/ebook/
leveraging-industry-content?msockid=2b90681817586317109e7d4e16a262c3.
Microsoft. Advancing education with ai to prepare the workforce of tomor-
row, 1 2025. URL https://www.microsoft.com/en-us/education/blog/2025/01/
advancing-education-with-ai-to-prepare-the-workforce-of-tomorrow/ .
24

Pearson VUE. Pearson vue candidate report, 2023. URLhttps://go.pearsonvue.com/
voc.
Dianne Rajendran and Scott Morton. Industry practitioners’ perceptions of embed-
ded ccna: A comparative study. In Proceedings of the 2nd Annual Conference of
Computing and Information Technology Research and Education New Zealand (CIT-
RENZ), 2011. URL https://researcharchive.wintec.ac.nz/id/eprint/1202/1/
CITRENZ2011Paper_Rajendran&Morton.pdf.
Zo Ramamonjiarivelo, Cristian Lieneck, Clemens Scott Kruse, Lloyd Greene,
and Lawrence Fulton. Assessing the impact of professional certifications
on time-to-hire, job satisfaction, and career growth of health administration
alumni. The Journal of Health Administration Education , 37(2):25–41, 2020.
URL https://www.ingentaconnect.com/contentone/aupha/jhae/2020/00000037/
00000002/art00003?crawler=true&mimetype=application%2Fpdf.
Denham Sadler. Nearly 70pc of aussie it jobs are in shortage. In-
formation Age, ACS , 2023. URL https://ia.acs.org.au/article/2023/
nearly-70--of-aussie-it-jobs-are-in-shortage.html .
G. Smith and A. Mehta. Skilling up! leveraging full and micro-
credentials for optimal skilling solutions. Technical report, 6
2024. URL https://arch-center.azureedge.net/Credentials/
Skilling-Up-Leveraging-Full-and-Micro-Credentials-for-Optimal-Skilling-Solutions.
pdf.
Technology Council of Australia. Technology council of australia roadmap to
deliver one million tech jobs. Technical report, Technology Council of Aus-
tralia, 2021. URL https://techcouncil.com.au/wp-content/uploads/2021/10/
2021-October-Roadmap-to-Deliver-One-Million-Jobs.pdf .
A Mathematical Derivations
This appendix provides detailed mathematical derivations that underpin the methodology
presented in Section 3. These derivations explain the formal relationship between skill set
similarity before and after augmentation with industry certifications.
A.1 Derivation of the Skill Set Similarity Transformation
Here we derive the relationship between the similarity of a degree skill setS1 to a job role
skill set T, and the similarity of the combined degree-certification skill setS′ 1 to the same
job role.
We start with the following expressions for the similarity between skill sets:
Θ(S1, T) = 1 C X s1∈S1 X t∈T w(s1, S1) · w(t, T) · θ(s1, t) (8)
Where C is the normalisation constant:
C =
X
s1∈S1
X
t∈T
w(s1, S1) · w(t, T) (9)
25

Similarly, for the augmented skill setS′ 1:
Θ(S′ 1, T) = 1 C ′ X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T) · θ(s′, t) (10)
With normalisation constant:
C ′ = X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T) (11)
To derive the relationship betweenΘ(S′ 1, T) and Θ(S1, T), we partition the skills in
S′ 1 based on their origin and expand the summation:
X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T) · θ(s′, t) =
X
s∈S1,s /∈S2
X
t∈T
w(s, S1) · w(t, T) · θ(s, t)+
X
s∈S2,s /∈S1
X
t∈T
wT (s, S2) · w(t, T) · θ(s, t)+
X
s∈S1∩S2
X
t∈T
[w(s, S1) + wT (s, S2)] · w(t, T) · θ(s, t) (12)
The last term can be expanded as:
X
s∈S1∩S2
X
t∈T
[w(s, S1) + wT (s, S2)] · w(t, T) · θ(s, t) =
X
s∈S1∩S2
X
t∈T
w(s, S1) · w(t, T) · θ(s, t)+
X
s∈S1∩S2
X
t∈T
wT (s, S2) · w(t, T) · θ(s, t) (13)
Substituting this back and rearranging, we get:
X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T) · θ(s′, t) =
X
s∈S1
X
t∈T
w(s, S1) · w(t, T) · θ(s, t)+
X
s∈S2
X
t∈T
wT (s, S2) · w(t, T) · θ(s, t) (14)
Recognising that the first term is equal toC · Θ(S1, T), we get:
X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T) · θ(s′, t) = C · Θ(S1, T) + X
s∈S2
X
t∈T
wT (s, S2) · w(t, T) · θ(s, t) (15)
Dividing both sides byC ′, we obtain:
Θ(S′ 1, T) = C C ′ · Θ(S1, T) + 1 C ′ X s∈S2 X t∈T wT (s, S2) · w(t, T) · θ(s, t) (16)
26

Similarly, for the normalisation constants, we have:
C ′ = X
s′∈S′ 1
X
t∈T
w(s′, S′ 1) · w(t, T)
=
X
s∈S1
X
t∈T
w(s, S1) · w(t, T) +
X
s∈S2
X
t∈T
wT (s, S2) · w(t, T)
= C +
X
s∈S2
X
t∈T
wT (s, S2) · w(t, T) (17)
Since the second term is non-negative (weights are always non-negative), we have
C ′ ≥ C, which means C C′ ≤ 1.
A.2 Special Cases Analysis
The derived relationship allows us to analyse two important special cases:
1. Case 1: Highly Relevant Certification
When the certification skills are highly relevant to the target job role, the similarity
θ(s, t) is high for many pairs(s, t) where s ∈ S2 and t ∈ T. In this case, the second
term becomes significant:
1
C ′
X
s∈S2
X
t∈T
wT (s, S2) · w(t, T) · θ(s, t) ≫ 0 (18)
Even though the first termC C′ · Θ(S1, T) is scaled down slightly (sinceC C′ < 1), the
large positive contribution from the second term ensures that:
Θ(S′ 1, T) > Θ(S1, T) (19)
This explains why relevant certifications significantly improve skill alignment with
target jobs.
2. Case 2: Irrelevant Certification
When certification skills are completely unrelated to the target job role, the similar-
ity θ(s, t) ≈ 0 for most pairs(s, t) where s ∈ S2 and t ∈ T. In this case, the second
term approaches zero:
1
C ′
X
s∈S2
X
t∈T
wT (s, S2) · w(t, T) · θ(s, t) ≈ 0 (20)
However, the normalisation constantC ′ still increases due to the addition of new
skills, causing the first term to be scaled down:
Θ(S′ 1, T) ≈ C C ′ Θ(S1, T) < Θ(S1, T) (21)
This mathematical result explains the counter-intuitive finding that irrelevant cer-
tifications can actually decrease one’s alignment with target job roles.
27

A.3 Implications for Different Educational Backgrounds
The derivation also explains why non-technical degrees experience larger relative improve-
ments than technical degrees when augmented with the same certification:
1. For a non-technical degree like nursing:
(a) The baseline skill overlap with technical roles is minimal, soΘ(S1, T) is very
small
(b) The certification adds highly relevant skills that directly align with the target
role
(c) The relative increase is large because the starting point is low
2. For a technical degree like Computer Science:
(a) The baseline skill overlap is already substantial, soΘ(S1, T) is relatively high
(b) Many certification skills may already be present in the degree curriculum
(c) The relative increase is smaller because the starting point is higher
This mathematical framework provides the theoretical foundation for our empirical
findings and offers guidance for certification selection based on educational background.
B Vectorised Skills Space Method (VSSM)
The Vectorised Skills Space Method (VSSM) is an optimised implementation of the Skills
Space Method that leverages matrix operations to achieve significant performance im-
provements while maintaining mathematical equivalence to the original formulation. This
section details the implementation approach developed to handle the computational de-
mands of large-scale skill similarity analysis.
B.1 Motivation for Vectorisation
A naive implementation of the Skills Space Method involves constructing a set of jobsJ,
where each job j ∈ J contains a set of skillsSj. Computing Skill Set Similarity using
nested loops and iterative operations results in poor runtime performance that does not
scale with dataset size.
Performance benchmarks of the naive implementation demonstrate polynomial growth
in execution time as the number of occupations and skills increases linearly:
This exponential growth in computation time necessitates an optimised approach suit-
able for large datasets containing millions of job advertisements and thousands of unique
skills.
B.2 Data Representation: Binary Presence Matrix
The foundation of VSSM is transforming the job-skill relationship from an adjacency list
representation to a binary presence matrix. Given a set of jobsJ = {j0, j1, . . . , jn} and
skills S = {s0, s1, . . . , sm}, we construct a skill population matrixP:
28

Unique Occupations Unique Skills Mean Execution Time (ms)
15 5 13.47
30 10 168.04
45 15 2,805.92
60 20 10,544.54
75 25 25,044.62
90 30 68,196.62
Table 6: Performance degradation of naive Skills Space Method implementation
P =


xj0,s0 xj0,s1 · · ·xj0,sm
xj1,s0 xj1,s1 · · ·xj1,sm
... ... ... ...
xjn,s0 xjn,s1 · · ·xjn,sm

 (22)
where:
xj,s =
(
1 if s ∈ j
0 if s /∈ j (23)
This binary matrix representation enables efficient vectorised operations for subse-
quent computations.
B.3 Vectorisation of Revealed Comparative Advantage (RCA)
The RCA function measures skill importance within job advertisements:
RCA(j, s) = x(j, s)/ P s′∈S x(j, s′)P
j′∈J x(j′, s)/ P j′∈J,s′∈S x(j′, s′) (24)
To vectorise RCA computation, we precompute auxiliary vectors and scalars:
Skills per job vector:
b =
P
s∈S x(j0, s) P s∈S x(j1, s) · · ·P s∈S x(jn, s)  (25)
Jobs per skill vector:
c =
P
j∈J x(j, s0) P j∈J x(j, s1) · · ·P j∈J x(j, sm) (26)
Total skill occurrences:
d =
X
j∈J,s∈S
x(j, s) (27)
The RCA matrix is then computed as:
R = P · (b−1)T · c−1 · 1 d (28)
where operations are performed element-wise.
29

B.4 Vectorisation of Skill Similarity
Skill similarity θ(s1, s2) measures the likelihood that two skills appear together in job
advertisements:
θ(s1, s2) =
P
j∈J e(j, s1) · e(j, s2)
max
P
j∈J e(j, s1), P j∈J e(j, s2)  (29)
where:
e(j, s) =
(
1 if RCA(j, s) ≥ 1
0 otherwise (30)
The vectorisation process involves:
Step 1: Effective use matrix
E = where(R ≥ 1, 1, 0) (31)
Step 2: Joint frequency matrix
N = ET E (32)
Step 3: Skill frequency vector
q = diag(N ) (33)
Step 4: Antecedent matrix
A = max(QT , Q) (34)
where Q is the matrix formed by tiling vectorq.
Step 5: Skill similarity matrix
Θ = N · A−1 (35)
B.5 Vectorisation of Skill Set Similarity
For two skill sets represented as subsets of the job population, skill weights are computed
as:
w(s, S) = 1 |J ′| X j∈J ′ RCA(j, s) (36)
where J ′ is the subset of jobs belonging to the skill set.
The vectorised computation proceeds as follows:
Step1: Skillpresencevectors Foreachskillset, createabinaryvector S′ indicating
skill presence:
S′ i =
(
1 if skill i appears in any job inJ ′
0 otherwise (37)
Step 2: Skill weight computation
w = 1 |J ′| X j∈J ′ (S′ · Rj,:) (38)
30

Step 3: Weighted similarity matrix
Θweighted = w2 · wT 1 · Θ (39)
Step 4: Final skill set similarity
SSS(S1, S2) =
P
i,j Θweighted(i, j)P
i,j W (i, j) (40)
where W = wT 1 · w2 is the weight product matrix.
B.6 Performance Results
Benchmarking was conducted on two distinct hardware configurations to evaluate VSSM
performance across different computational architectures:
• Macbook Pro 2021: M1 Pro chip (8-core CPU, 10-core GPU), 16GB RAM, using
MLX acceleration
• PC Workstation: AMD Ryzen 5600X (6-core CPU), 32GB RAM, NVIDIA RTX
3060 12GB, using CuPy acceleration
Comparativebenchmarkingdemonstratessubstantialperformanceimprovementsacross
both platforms:
Test Occupations Skills Baseline (ms) VSSM (ms) Speedup
1 15 5 11.55 0.15 77 ×
2 30 10 141.58 0.14 1,011 ×
3 45 15 2,206.75 0.20 11,034 ×
4 60 20 5,673.70 0.20 28,369 ×
5 75 25 28,927.69 0.30 96,426 ×
6 90 30 34,530.35 0.24 143,876 ×
Table 7: Performance comparison between naive baseline and VSSM implementation on
PC workstation
The performance difference between Apple Silicon and NVIDIA GPU platforms was
negligible for smaller datasets (test iterations 1-5), with the NVIDIA GPU system demon-
strating approximately 5.5× faster execution for the largest dataset (test iteration 6).
Both platforms achieved dramatic improvements over the baseline implementation, with
speed enhancements ranging from 77× to 143,876×, making large-scale skill similarity
analysis computationally feasible for real-world applications.
B.7 Implementation Validation
Mathematical equivalence between the naive and vectorised implementations is verified
through regression testing. Both implementations process identical randomly generated
datasets, and outputs are compared to ensure numerical accuracy within floating-point
precision limits.
31

B.8 Computational Infrastructure
VSSM is implemented using optimised Python libraries:
• NumPy: For CPU-based matrix operations with BLAS optimisation
• CuPy: For GPU-accelerated computations on NVIDIA hardware
• MLX: For Apple Silicon GPU acceleration
• SciPy sparse: For memory-efficient sparse matrix operations
This multi-backend approach ensures optimal performance across different hardware
configurations while maintaining a consistent API for skill similarity computations.
C Implementation Considerations
C.1 Stakeholder-Specific Implementation Guidance
For effective implementation, different stakeholders should consider:
Universities:
• Integrate certification modules within existing degree programs
• Use skill alignment data to inform curriculum updates
• Partner with certification providers for streamlined student pathways
Employers:
• Implement skill similarity assessments in recruitment processes
• Identify internal candidates for role transitions based on skill alignment
• Design targeted training programs addressing specific skill weaknesses
Certification Providers:
• Align certification design with quantified skill gaps
• Develop specialised certification paths for specific degree backgrounds
• Provide integration tools for educational institutions
32
