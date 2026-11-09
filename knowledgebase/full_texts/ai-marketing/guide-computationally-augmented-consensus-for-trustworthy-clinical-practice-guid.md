---
title: 'GUIDE: Computationally Augmented Consensus for Trustworthy Clinical Practice Guidelines'
url: https://arxiv.org/abs/2610.16108
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yuanfan Lin
- Jie Di
- Xujin He
- Zhenzhe Lin
- Jialing Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.16108
pages: 109
chars: 184833
fetched_at: '2026-11-08T13:33:02+00:00'
kb_version: 1
---

# GUIDE: Computationally Augmented Consensus for Trustworthy Clinical Practice Guidelines

1
GUIDE: computationally augmented consensus for trustworthy
clinical practice guidelines
Coauthors: Yuanfan Lin1†; Jie Di1†; Xujin He1†; Zhenzhe Lin1†; Jialing Chen1; Ruiyang Li1;
Changyu Zheng2; Yuanrui Shang1; Weiqin Peng1; Jingxi Qin2; Xiong Wang2; Dongxin Ye2;
YiningHuang1; GuoqiangLi1;AndiXu1;SijiaYu2; RuixinWang1; YahanYang1;Xiaohang Wu1;
DuoruLin1;JingjingChen1;ZhenzhenLiu1;WenbenChen1*;HaotianLin1,3,4,5*
Affiliations:
1ZhongshanOphthalmicCenter,SunYat-senUniversity,WHOCollaboratingCentreforEyeCare
and Vision, State Key Laboratory of Ophthalmology, Guangdong Provincial Key Laboratory of
Ophthalmology and Visual Science, Guangdong Provincial Clinical Research Center for Ocular
Diseases,Guangzhou,China;
2ZhongshanSchoolofMedicine,SunYat-senUniversity,Guangzhou,China;
3HainanEyeHospitalandKeyLaboratoryofOphthalmology,ZhongshanOphthalmicCenter,Sun
Yat-senUniversity,Haikou,Hainan,China;
4Department of Genetics and Biomedical Informatics, Zhongshan School of Medicine, Institute
for Frontier Interdisciplinary Research in Health Sciences and Technology, Sun Yat-sen
University,Guangzhou,China;
5Leadcontact.
†Theseauthorscontributedequallytothiswork.
*Corresponding authors:
Professor Haotian Lin, M.D., Ph.D., Email: linht5@mail.sysu.edu.cn. Zhongshan Ophthalmic
Center, Sun Yat-sen University, 7# Jinsui Road, Guangzhou, China, 510623. Telephone:
+86-20-87330493.Fax:+86-20-87333271.
AssociateProfessor Wenben Chen, M.D.,Ph.D.,Email: chenwb56@mail.sysu.edu.cn.Zhongshan
Ophthalmic Center, Sun Yat-sen University, 7# Jinsui Road, Guangzhou, China, 510623.
Telephone:+86-20-66648760.Fax:+86-20-87333271.

2
Abstract
Maintaining up-to-date clinical practice guidelines (CPGs) is essential for evidence-based
medicine(EBM),yetthecurrentprocessisconstrainedbytherapidexpansionofevidenceandthe
complexity of expert consensus formation. To address this challenge, we developed GUIDE, a
multi-agent copilot system that enables computationally augmented consensus for human-AI
collaborative clinical guideline generation and updating, assigning labor-intensive tasks to
specialized AI agents while preserving critical judgment and final arbitration for human experts.
In a benchmark comprising 12 datasets derived from NICE ophthalmology-specific guidelines,
GUIDE showed strong performance across evidence retrieval, assessment, and synthesis,
achieving88.85%literaturerecall,86.06%alignmentincertainty-of-evidenceratings,and91.67%
agreement on recommendations, only requiring 162.17 minutes per dataset on average (including
28.68% human intervention). Performance remained stable in additional 20 datasets spanning
cardiology, endocrinology, gastroenterology, and respiratory medicine, indicating its
cross-specialtygeneralizability.Wethenconductedanablationanalysistovalidatetheimportance
of human-AI collaboration mechanism, as removing expert intervention reduced performance in
judgment-intensive steps such as Risk-of-Bias assessment. Furthermore, a simulated end-to-end
evaluationusingsixpost-cutoffdatasetsdemonstratedthatGUIDEmaintainedrobustperformance,
supporting its ability to generalize to genuinely unseen evidence within a continuous
guideline-updating workflow. Finally, prospective real-world validation in a live guideline
updating process showed that GUIDE substantially alleviated expert workload across evidence
selection, extraction, and synthesis. The GUIDE-assisted update was judged more clinically
acceptable than the original guideline recommendation issued a decade earlier (mean score, 3.73
vs.1.53;agreement,66.7%vs.13.3%)andachievedoutcomescomparabletothoseofhuman-only
updating (P = 0.588), while requiring substantially less time and expert effort. Together, our
findings support GUIDE as a practical framework for timely, trustworthy, and expert-centric
clinical guideline generation, and validate computationally augmented consensus as a feasible
paradigmforenhancedguidelinedevelopment.

3
Introduction
Clinical practice guidelines (CPGs) constitute central instruments of evidence-based medicine
(EBM), designed to integrate the best available evidence with clinical expertise to support
informed healthcare decision-making [1]. By translating rapidly evolving knowledge into
structured evidence bodies and actionable practice recommendations, CPGs play a critical role in
reducing unwarranted practice variation, improving care delivery quality, and enhancing the
overall efficiency and equity of healthcare systems [2]. Their value, however, depends on their
timeliness. Recommendations that are not updated in line with emerging evidence can weaken
their clinical validity and potentially lead to suboptimal care [3]. Conventional guideline
workflows are increasingly unable to keep pace with the exponential growth of biomedical
knowledge[4]. Withtypical update cycles exceeding two years [5,6],thereis an inherent delayin
translating new evidence into practice recommendations. This strain is exacerbated by the annual
addition of over one million citations and a growing burden of secondary research [7], the scale
andcomplexityofwhichfarexceedcurrentcapacitiesforefficientevidencesynthesis.
Yet the difficulty of guideline generation or updating extends beyond scale alone. More
importantly, it is a consensus-building process that requires experts to collectively interpret
uncertain evidence, weigh methodological limitations, balance benefits and harms, and reconcile
clinical, economic, and societal considerations into accountable consensus. For each clinical
question, experts must determine study eligibility, interpret heterogeneous findings and
conclusionstoestimatecertaintyofevidence,andfinallytranslateevidenceintorecommendations
in broad medical and socioeconomic context [8]. Many of these steps cannot be fully delineated
by deterministic rules but depend on interpretation under uncertainty, contextual trade-offs and
deliberation among domain experts. These tasks are not merely technical operations, but
judgment-intensive processes that rely on time-consuming expert deliberation and consensus
formationtoensurethetrustworthinessofclinicalguidelines.Consequently,continuedrelianceon
traditional updatingworkflows may widenthegap between therapidgrowth ofnew evidenceand
theresponsivenessofexistingguidelinesystems,ultimatelylimitingtheireffectiveness[9].
Recent studies highlight the potential of large language models (LLMs) to streamline
literature screening and evidence extraction in medical guideline development [10,11], with

4
systems like Quicker extending automation to end-to-end recommendation generation [12].
Despite these technical strides, real-world clinical integration remains challenging. Crucial
elements such as transparent evidence scrutiny, the incorporation of expert clinical judgment, and
accountable consensus formation under uncertainty are still inadequately addressed [13]. As
probabilistic models, LLMs remain unreliable in tasks requiring implicit inference and
quantitative reasoning. For example, they may fail to detect methodological bias indicated by
missing information, extract numerical outcomes dispersed across a report, or assess the overall
credibility of a trial [14,15]. Human experts are better equipped to evaluate methodological
nuances and implementation trade-offs, but their capacity is increasingly strained by the rapidly
expanding evidence base. This creates an urgent need for expert-facing AI systems that enable
real-time human-AI collaboration [16]. Such systems should support computationally augmented
consensus: LLMs enhance the speed, breadth, and consistency of evidence processing, while
experts retain responsibility for resolving uncertainty and arbitrating high-stakes decisions,
consistent with the emerging paradigm of AI-integrated medicine [17]. This also necessitates a
well-defined human-AI collaborative framework that clarifies what tasks AI can perform, when
expert judgment is required, and how responsibility should be allocated across both intermediate
stepsandfinalrecommendations[18].
Here,weintroduceGUIDE(Guideline Update Intelligence Decision Engine),anLLM-based
copilot framework for collaborative clinical guideline generation, built upon a human-AI
partnershipmodelderivedfromexistingresearchandDelphi-likeexpertspanelconsultations[19].
The design strategically allocates roles to optimize the strengths of both AI and human experts
throughout the guideline development process. While AI agents execute high-volume, rule-based
tasks such as clinical question decomposition, literature screening, data extraction, and evidence
synthesis, human experts maintain ultimate accountability, overseeing the process and
contributing medical insights to ensure methodological rigor. This human-AI collaboration is
implementedintwokeymodes:expertsinteract reactively,addressingflaggedissuesraisedbyAI
reviewers, and proactively, using their professional judgment to fine-tune system outputs. To
evaluate GUIDE, we first established a benchmark comprising 12 datasets derived from NICE
(NationalInstituteforHealthandCareExcellence)ophthalmology-specificguidelines,confirming

5
thesystem’sfoundational abilityto perform keytasksin guidelinegeneration. Wethen conducted
an ablation study to quantify the impact of human involvement, removing reviewer mechanisms
and expert participation, revealing the critical role of human judgment in enhancing system
performance. To assess the framework’s generalizability, we extended testing across multiple
medical specialties and clinical question complexities on 20 datasets, demonstrating its broad
applicability. Finally, we conducted two critical experiments to assess GUIDE’s real-world
applicability. We performed temporal hold-out simulations, applying GUIDE to six datasets
released after the LLM’s knowledge cutoff, to test the system’s ability to integrate new evidence
into an end-to-end guideline development workflow in real time. Furthermore, in a prospective
real-world validation, we explored how GUIDE integrates emerging evidence into an existing
guideline on intraocular lenses (IOLs) selection for cataract surgery patients. Our findings
demonstratethattrustworthyguidelinegenerationcan befacilitatedthrough GUIDE,aframework
for computationally augmented consensus that systematically couples AI-mediated evidence
processing with expert deliberation, thereby preserving expert oversight, methodological rigor,
andclinicalaccountabilitywhilesubstantiallyreducinghumanworkload.
Results
Development of the GUIDE for clinical guideline generation
GUIDE is a multi-agent copilot system to facilitate clinical guideline generation by integrating
automated efficiency with clinical rigor through a structured human-AI partnership
(Supplementary Video 1). The foundational logic of the system is anchored in a set of
collaboration principles established via a Delphi-like consensus among a multidisciplinary expert
panel.Centeredona“human-in-the-loop”architecture,GUIDEdelegateshigh-volume,rule-based
tasks to AI agents while ensuring that critical professional judgment and final validation remain
firmlyunderhumanoversight.Thiscollaborativedesignisimplementedbyexpertsviatwomodes:
a proactive intervention approach to ensure clinical accountability in critical junctures and a
condition-triggered review mechanism for monitoring automated tasks at predefined checkpoints
(Supplementary Table 1). Throughout the guideline generation workflow, this allocation is
tailored to the demand for professional expertise and risk profiles of each specific step. While AI

6
agents primarily support relatively structured and standardized processes such as search strategy
formulation and data extraction, human experts lead the interpretive and value-sensitive stages:
activities including PICO (Population, Intervention, Comparison, and Outcome) construction,
evidence quality assessment, and the final synthesis of recommendations are reserved for
proactivehumaninterventiontoensureclinicalrigorandconsensus(SupplementaryTable2).
To translate these principles into executable system logic, the system architecture
incorporates specialized agents that operationalize the human-AI interface. Specifically, the
proactive intervention approach is coordinated by an assistant agent that parses natural-language
expert instructions into executable commands for specialized agents. The condition-triggered
review mechanism is implemented through a rule-based reviewer agent that monitors system
outputs to trigger reactive human intervention when suspected anomalies arise. By integrating
these agent-driven functions, GUIDE establishes a dynamic division of labor that balances
computationalpowerwiththerigorousaccountabilityrequiredforreal-worldevidencesynthesis.
The framework operates through a seven-step sequential workflow spanning from question
decomposition to clinical recommendation generation (Fig. 1a, Supplementary Video 1). The
operation process begins with PICO construction, where GUIDE parses the clinical question and
generates a structured PICO draft that can be directly used for evidence mapping. Given that the
decomposed PICO factors determine the recommendation’s clinical scope, experts must verify
them and make necessary amendments at this step. Based on the finalized PICO, GUIDE
generates a structured review protocol detailing the review type, eligibility criteria and synthesis
framework for expert validation and adjustment before retrieval (Supplementary Video 1).
Following protocol confirmation, two search agents driven by different LLMs formulate search
strategies and perform parallel retrieval independently, while the AI reviewer monitors signals of
potentially unreliable retrieval, such as marked discrepancies in literature volume or limited
overlap between two search outcomes and elicits human intervention. The assistant agent
facilitates experts in revising the strategy by translating natural-language instructions into search
strings, obviating the need to directly modify complex syntax (Supplementary Fig. 1).
Subsequently, two screening agents conduct title-and-abstract and full-text eligibility assessments
sequentially, presenting rationales and confidence levels for each inclusion or exclusion decision

7
(Supplementary Fig. 2). At the full-text screening stage, experts may be brought in when the AI
reviewerdetectsany disagreementintwoparallelroundsofscreeningandjudgment. Forincluded
studies, two data extraction agents extract textual and numerical data and generate formats
corresponding to the PICO framework (Supplementary Fig. 3). As previously described, any
discrepancy in two parallel extractions identified by AI Reviewer is referred to experts for
verification against the original text. Comparable outcomes from verified study-level data were
merged into evidence bodies for synthesis and certainty assessment, with pooled effect sizes
calculated by the agent where appropriate. The quality assessment agents then assess these
evidence bodies using the widely adopted Grading of Recommendations Assessment,
Development and Evaluation (GRADE) methods, and experts audit agents’ evaluations where
divergentgradingarises.Expertscaneitherconvey theirinsightsviatheassistantagentordirectly
override automated quality assessment results. Finally, the evidence synthesis and
recommendation module, implemented as a Delphi-like multi-agent module, integrates the
processed evidence into Evidence-to-Recommendation (EtR) materials and draft recommendation
statements, which are then submitted to the expert panel for final deliberation and consensus
decision-making (Supplementary Fig. 4). As a copilot system that extends expert capabilities,
GUIDE synergizes automated efficiency with stringent clinical governance (Fig.1b).Its real-time
interactive interface allows experts to seamlessly integrate their insights into the workflow,
enhancingboththeprecisionandtheclinicalaccountabilityofthefinaloutputs.
GUIDE’s benchmark performance
To evaluate the baseline performance of GUIDE, we conducted a benchmark test using 12
specialized datasets derived from four ophthalmology guidelines published by NICE. NICE was
selected as its guidelines development process is highly transparent and traceable. Each of these
12 datasets encompasses the complete evidence-based workflow, spanning from initial clinical
question formulation to the development of final recommendations (Supplementary Table 3). To
isolate module performance and mitigate error propagation, we tested the framework using a
modular approach, in which each step was independently conducted and evaluated using original
NICEworkflowmaterials(SupplementaryTable4and5).
The collaborative workflow for each dataset involved a senior specialist with over ten years

8
of clinical experience in the respective domain. Under this configuration, GUIDE performed
effectively, enhancing efficiency across the entire process. In the PICO construction phase, the
agent near-instantaneously generated structured drafts in a mean of 0.37 minutes per question. By
havingexpert verifyingitsinterpretation,thesystemachievedamean semanticsimilarity score of
0.83 (ranging from 0.80 to 0.86). Across 12 benchmark tasks, the retrieval module identified
25,744 records in total, which were reduced to 1,369 after title-and-abstract screening and 135
final inclusions after full-text screening. High recall was maintained throughout the pipeline, with
mean recall values of 98.81% (95% Confidence Interval [CI], 97.42%–100.00%), 93.57% (95%
CI, 90.07%–96.96%), and 88.85% (95% CI, 85.22%–92.91%) for retrieval, title-and-abstract
screening, and full-text screening, respectively. Precision improved progressively from 0.47%
(95% CI, 0.33%-0.64%) at retrieval to 8.11% (95% CI, 6.02%–10.70%) after title-and-abstract
screening and 84.60% (95% CI, 78.28%–90.61%) after full-text screening (Fig. 2a). Specificity
and negative predictive value (NPV) were 98.56% (95% CI, 98.09%–99.05%) and 98.81% (95%
CI, 98.27%–99.32%), respectively. In retrieval stage, the AI reviewer correctly triggered human
intervention in 4 of 12 datasets when retrieval count discrepancies were detected. At the full-text
screening stage, discrepant screening decisions were identified for 22 articles (accounting for
16.30% of all full-text articles screened), all of which were referred to experts for arbitration.
Amongthem,21 studieswereconfirmed tohaveinclusion/exclusion decisions consistentwith the
original guidelines. The literature search step required an average of 9.26 minutes per dataset in
total, comprising 7.95 minutes of automated system processing and 1.31 minutes of human
intervention, whereas the literature screening step required 76.20 minutes per dataset in total,
comprising 60.40 minutes of automated system processing and 15.80 minutes of human
intervention.
Thedata extractionprocess demonstrated high efficiencyand precision,requiring an average
of 28.20 minutes per dataset, including 15.89 minutes of automated system processing and 12.31
minutes of human rechecking. Compared with the conventional approach, in which manual
extractionofdatafromasinglearticletypicallyrequiresmorethan40minutes[20],thisworkflow
substantially improved extraction efficiency while maintaining high accuracy of 98.02%.
Although the system handled the majority of the workload, 22.69% of the extraction tasks

9
required expert verification,with numericalvalues accountingfor 88.9%ofthe verifieditems and
textualdata accounting fortheremaining11.1%. Further analysisshowsthat theoverallerror rate
of 1.98% was entirely due to omissions of numerical data. Because the reviewer agent was
designed to flag only mismatches for expert correction, these omissions did not trigger alerts and
thereforeremainedundetected.Subsequentassessmentofthe300profilesaveraged10.24minutes
per dataset, consisting of 5.14 minutes of automated processing and 5.10 minutes of expert
intervention. The framework showed strong agreement with the reference standard, achieving
82.80% (95% CI, 79.57%–86.76%) for risk-of-bias assessment, 90.16% (95% CI,
85.48%–94.33%) for indirectness, 88.84% (95% CI, 83.47%–94.08%) for inconsistency, 92.24%
(95% CI, 87.90%–96.35%) for imprecision, and 86.06% (95% CI, 81.38%–90.96%) for final
certaintygrading.(Fig.2b).Finally,theDelphi-likemulti-agentmoduleintegratedtheseprocessed
findings into draft recommendation statements within 37.90 minutes per question, achieving a
consistency rate of 91.67% with the recommendations reported in the original guidelines (Fig.2c,
SupplementaryTable6).TheaveragetimeexpenditureforbothGUIDEandhumanexpertswithin
each stepis illustratedin Fig.2d. Overall,GUIDE accounted for 71.32% of thetotal time (115.66
minutes), while expert oversight and refinement only comprised the remaining 28.68% (46.51
minutes).
Ablation analysis of expert and multi-agent contributions to performance
To quantify performance gains attributable to expert involvement and the multi-agent system, we
conductedanablationanalysisbyexcludingrecordsfromtheAIreviewer,AIassistantandhuman
expertin thebenchmarktest,retainingonly outputscorrespondingtoafullyautomated workflow.
As the AI reviewer responsible for identifying discrepancies across parallel agents was not
considered, we restricted the analysis to a single GPT-4.1-driven agent at each step to ensure
workflowconsistencyandcomparability.Weobservedthattheautomatedsystemaloneperformed
well on relatively straightforward tasks, achieving a PICO semantic similarity of 0.79 and a mean
literature retrieval recall of 92.58% (Fig. 3a). Across the 12 tasks, the retrieval agent identified
29,121 records in total, 1,645 records after title-and-abstract screening and 155 final inclusions,
reflecting relatively broad eligibility criteria in the absence of expert input. Notably, final-stage
recall decreased from 88.85% (95% CI, 85.22%–92.91%) in the full configuration to 79.80%

10
(95% CI, 74.15%–86.13%) in the ablation analysis (P = 0.008), while final-stage precision fell
even more pronounced from 84.60% (95% CI, 78.28%–90.61%) to 66.09% (95% CI,
58.92%–73.61%)(P =0.010)(Fig.3b).Specificity(96.49%(95%CI,95.36%–97.60%))andNPV
(98.24% (95% CI, 97.43%–98.97%)) were largely preserved at high levels. This sharp decline
indicates that without monitoring provided by the AI reviewer and human expert, single
automated agent struggles to formulate and navigate comprehensive inclusion/exclusion criteria,
leading to an influx of confounding information,especially irrelevant articles, that may ultimately
dilute the quality of evidence synthesis and recommendation value. Data extraction accuracy
dropped from 98.02% to 85.30% (P = 0.046), while the omission rate rose from 1.98% to 14.7%
(P=0.027).Duringtheevidenceassessmentphase,consistencyinriskofbiasjudgmentsdeclined
significantly from 82.80% (95% CI, 79.57%-86.76%) to 69.54% (95% CI, 61.15%-77.92%) (P =
0.002), with a corresponding decline in consistency for overall certainty-of-evidence ratings from
86.06% (95% CI, 81.38%-90.96%) to 68.78% (95% CI, 62.72%-74.83%) (P < 0.001) (Fig. 3c).
Detailed erroneous analysis reveals that agents fell to detect latent methodological flows that
required deductive reasoning to identify the absence of evidence, such as lack randomization
details. In such cases, the agent frequently defaulted to a “low risk” judgment for allocation
concealment based solely on the presence of the term “sealed,” whereas experts correctly
interpreted the absence of these details as indicative of potential bias. In the recommendation
generation step, the proportion of drafted recommendation rated as “exactly consistent” with the
reference standards also decreased from 83.33% to 50.00% (Fig. 3d, Supplementary Table 6).
Taken together, these findings show that LLMs may execute many structured components of
guideline updating efficiently, but the reviewer-guided human-AI collaborative mechanism is
critical for maintaining clinically interpretable recommendation generation in the most
judgment-intensivestages.
Evaluation of GUIDE generalizability across clinical specialties
We further evaluated the generalizability of GUIDE across clinical specialties by testing GUIDE
on 20 datasets derived from NICE guidelines in cardiology, endocrinology, gastroenterology, and
respiratory medicine, with five datasets from each specialty (Supplementary Table 7). A senior
domainspecialistwithovertenyearsofclinicalexperiencewasrecruitedforeachfieldtofunction

11
asacollaborativepartner.Acrossthesespecialties,GUIDEmaintainedrobustperformancedespite
differences in domain-specific terminology and clinical context. The system achieved an average
PICO similarity of 0.85 and literature retrieval recall of 98.88% (95% CI, 97.71%–99.81%) (Fig.
4a). The system’s high-throughput efficiency remained consistent during study selection, where
agents processed a total of 38,317 records and 1,668 full-text literature. Despite the heterogeneity
of cross-disciplinary literature, the collaborative framework sustained high performance, with a
full-textscreeningrecallof88.83%(95%CI,85.45%–92.26%)andprecisionof80.11%(95%CI,
74.33%–85.90%) (Fig. 4a). The final screening yielded a specificity of 97.24% (95% CI,
96.27%–98.14%) and an NPV of 98.61% (95% CI, 98.14%–99.07%). This step involved 51.79
minutesofagentprocessingandonly10.41minutesofhumanreview.Indataextractionfrom177
included studies, the overall data extraction accuracy was 81.13%, with an error rate caused by
omission of 18.87%. Textual data extraction reached an accuracy of 89.91%, whereas numerical
data extraction achieved an accuracy of 78.81%, consistent with previous findings that numerical
data handing remains a challenge for LLMs. For evidence certainty assessment, the system
achieved 82.23% (95% CI, 79.09%-85.55%) agreement in overall quality with the reference
standard, while requiring a mean processing time of 12.47 minutes per article (8.2 minutes of
expertrecheck)(Fig.4b). Finally,themulti-agentmodulesynthesizedthesefindingsand,through
the Delphi-like consensus process, generated draft recommendation statements within 44.0
minutes per dataset, achieving 90.00% agreement in expert evaluations (Fig. 4c, Supplementary
Table 6). Thesefindings indicatethat GUIDE generalizes well acrossmultiple medicalspecialties
and provides a broadly applicable framework for guideline updating. The time expenditure for
bothAIagentsandhumanexpertswithineachstepisillustratedinFig.4d.
End-to-end evaluation of GUIDE performance on post-cutoff datasets
To eliminate data leakage risks and assess the holistic performance of the framework, we curated
six datasets from NICE guidelines published between April 2025 to March 2026 (details in
Methods), simulating an end-to-end prospective experiment within a continuous workflow
(Supplementary Table 8). Unlike modular tests in the benchmark, this end-to-end evaluation
required GUIDE to process raw outputs from previous components, a design wherein the
framework must withstand real-world error propagation to demonstrate its true operational

12
integrity.
The end-to-end pipeline achieved a PICO semantic similarity of 0.84 and maintained strong
performance through literature screening, with a final screening recall of 87.75% (95% CI,
81.05%–94.44%),precisionof82.17%(95%CI,73.49%–91.06%),specificityof97.15%(95%CI,
95.95%–98.49%)andNPVof97.21%(95%CI,94.63%–99.35%)(Fig.5a).Whileminorshiftsin
the evidence pool limited direct comparison of intermediate metrics, such as evidence quality
assessment with original NICE reference, the core clinical reasoning remained consistent.
Subject-matter expert evaluation confirmed a complete (100.00%) directional agreement between
GUIDE’s outputs and recommendations in the original guidelines (Fig. 5b, Supplementary Table
6). By successfully interpreting unseen evidence to generate clinically sound recommendations,
GUIDE proves it moves beyond reproducing embedded content, highlighting its potential as a
resilienttoolforthecontinuousevolutionofclinicalpractices.
Prospective case study of GUIDE for cataract guideline updating
We conducted a prospective validation study of the update of the NICE 2017 guideline Cataracts
inadults:management(NG77),usingitsoriginalreviewquestion,“Whatistheoptimalstrategyto
facilitatesimultaneousdistanceandnearvisionfollowingcataractsurgery?”,asacasestudy.Two
senior cataract specialists, each with over twenty years of clinical expertise, participated in the
entire guideline-updating process. For steps requiring human judgment or intervention, the two
experts independently assessed the issue and resolved disagreements by consensus. A
pre-designatedexpertthenoperatedGUIDEinterface,implementingonlytheagreedactions.
In defining the PICO framework, the “Population” and “Comparator” criteria remained
largely identical to the original version. Notably, the AI system incorporated Extended Depth of
Focus (EDOF) IOLs, a category of growing significance in recent clinical research, into the
“Intervention” criteria. However, consistent with previous observations regarding the limitations
ofautomatedsystemsincapturingsocioeconomicnuances,thesystemomittedresourceutilization
and costs from the “Outcomes” criteria, which were manually added by experts (Supplementary
Information1).
Initial search strategies generated by the system yielded an unmanageable 9,740 records,
indicating an overly broad search scope. Upon experts’ intervention to restrict the inclusion to

13
Randomized Controlled Trials (RCTs) and systematic reviews (following the original guideline’s
methods), the strategies were refined and resulting in 1,111 records (1,107 after de-duplication).
Followingparalleltitle-and-abstractscreening,56articlesunderwentfull-textassessment,yielding
23 new inclusions published after the original guideline’s cutoff date. Furthermore, 28 studies
identified from systematic review searches were subjected to automated full-text screening, from
which four additional studies were included. These processes culminated in a total of 27 eligible
studies comprising the updated body of evidence (Supplementary Information 2 and 3). The AI
reviewer identified only six (6/56, 11%) discrepancies during the second screening phase. These
were resolved through expert review, which confirmed that all six should be excluded based on
minor misalignments with the predefined PICO scope. Remarkably, filtering the 1,107 retrieved
records into the final 27 inclusions studies took only 55 minutes, including 11 minutes of human
adjudication.
Data extraction was complicated by the relative abundance and non-standardized outcome
measures. For example, the outcome “visual function” exhibited substantial heterogeneity across
studies,encompassingmultipleassessmentinstruments,diversetestingconditions,andvarieddata
formats. These included binary outcomes (e.g., spectacle independence), continuous scale scores
(e.g., vision-related quality of life questionnaires), continuous measurements (e.g., contrast
sensitivity), and performance-based metrics (e.g., reading-related tests). Despite significant
variations in narrative phrasing, the data extraction agents robustly captured categorical data,
including study design, intervention details, and complications. Conversely, while numerical data
were often presented in more structured tables, the AI reviewer flagged several omissions and
inconsistencies. For these anomalies, experts verified and corrected them against the original
article. Ultimately, seven IOLs comparisons and 21 distinct outcome categories were successfully
extracted into standardized data tables within 38 minutes, including 15 minutes of expert
involvement. The agent automatically grouped study-level data into comparison- and
outcome-specific evidence bodies, calculated pooled effect sizes using appropriate synthesis
methods,andorganizedtheresultsintostructuredoutputsfordownstreamqualityassessment.
For evidence quality assessment, the system performance revealed distinct patterns across
different Risk-of-Bias domains. Randomization and blinding domains demonstrated high

14
inter-rater consistency between the two assessment agents, with only a single disagreement
identified (3.7% discrepancy rate). In contrast, selection and reporting biases were predominantly
rated as “unclear” due to insufficient reporting in the primary studies; only two studies provided
adequate detail to warrant a “low risk” rating (No discrepancy in these two domains). Attrition
bias emerged as the most contentious domain, with seven inconsistencies (25.9%) flagged by AI
reviewer requiring further adjudication. These discrepancies were resolved by experts viewing
relevant excerpts from source articles. Following this rigorous reconciliation process, the overall
risk of bias for all included study was appraised as serious. The system showed more robust
performance applying GRADE criteria for intervention studies. Out of 291 total quality rating
across evidence bodies, discrepancies occurred only in the indirectness domain (6 cases, 2.1%),
and 100% agreement was observed for imprecision and inconsistency owing to more objective
and quantitatively defined criteria. By contrast, these identified discrepancies in indirectness
typicallyinvolvedsophisticatedPICOinterpretationsthatdemandedcontextualunderstanding.All
discrepancies were carefully reviewed by the experts, who provided the final adjudicated ratings
(Supplementary Information 4). The automated assessment process was completed within 47
minutes,whileexperttookapproximately25minutestofinishjudgement.
Upon completion of the evidence appraisal, a virtual Delphi panel comprising an AI
committee chair, two ophthalmic practice agents, a healthcare provider representative agent, a
commissioneragent,andavirtualpatienttogetherwithtwohumancataractspecialists,deliberated
on thefindings from their respective perspectives toformulate structuredrecommendations. From
PICO formulation to recommendation development, the entire process took 192 minutes,
including 65 minutes of expert involvement. By constructing a comprehensive EtR content, the
virtualpanelintegratedevidencequalityandemergingtrendstobalanceclinicalefficacywithcost
and safety trade-offs (Supplementary Information 5). This evidence review supported a transition
from the original “do not offer” statement to a more supportive recommendation for multifocal
and EDOF IOLs. Notably, the updated recommendation adopted “consider” rather than more
definitive phrasing, reflecting a shift in recommendation strength. This indicates that while these
newer designs show clear clinical promise, the final choice should remain highly individualized
anddependentonthepatient’sspecificvaluesandpreferences(SupplementaryInformation6).

15
In parallel, the human-only group followed the same prespecified guideline-updating
workflow, encompassing PICO refinement, protocol development, literature searching and
screening, data extractionand evidence synthesis,evidencequality assessment,and completion of
the EtR framework. As in the GUIDE-assisted group, the experts incorporated EDOF IOLs into
the intervention framework on the basis of contemporary clinical practice and emerging evidence
(Supplementary Information 7). The literature search retrieved a comparable 1,012 records.
Title-and-abstract screening required a total of 33 hours, followed by 21 hours for full-text
eligibility assessment. Of the retrieved records, 37 articles proceeded to full-text assessment, of
which 25 ultimately met the eligibility criteria (Supplementary Information 8 and 9). Compared
with the GUIDE-assisted group, fewer articles proceeded to full-text assessment, indicating
greaterscreeningspecificityatthisstage.Dataextractionandquantitativesynthesiswasoneofthe
most time-consuming components of the human-only workflow, requiring 76 hours to construct a
structured, long-format data extraction table. The same seven IOL comparison categories and 20
distinct outcome categories were extracted, and pooled effect estimates were subsequently
calculated where appropriate. Evidence quality assessment represented another labor-intensive
step, requiring another eight hours for independent appraisal and consensus resolution of
disagreements.Thedistributionofevidenceratingsandthereasonsfordowngradingwerebroadly
consistent with those observed in the GUIDE-assisted group (Supplementary Information 10). An
eight-member guideline committee then reviewed the GRADE evidence profiles and relevant
benefits,harms,resource use,costs factors toformulate thedraft recommendation over threedays
(Supplementary Information 11). Although phrased slightly differently, the updated
recommendation similarly shifted from a strong recommendation against multifocal IOLs to a
more conditional recommendation to consider their use, consistent with the conclusion of the
GUIDE-assisted group. Overall, updating this review question through the human-only workflow
required 23 days from initiation to completion with a largely consistent practice recommendation
(SupplementaryInformation12).
Afterboth group’scompletionoftheirupdatingprocess,threerecommendations(theoriginal
2017NICEstatement,theGUIDE-assistdraftedversionandhuman-onlydevelopedversion)were
presented to an external panel of 15 ophthalmic experts to evaluate its clinical acceptability.

16
Experts were blinded with recommendation origins and asked to rate their level of agreement
using a five-point Likert scale ranging from “strongly disagree” to “strongly agree”. Agreement
was defined as a rating of either “agree” (4) or “strongly agree” (5) (Supplementary Information
13).
The mean scores were 1.53±1.06 for the original 2017 NICE statement, 3.73±0.96 for the
GUIDE-assist version, and 3.87±1.36 for the human-only version. Both the GUIDE-assist and
human-only versions received significantly higher agreement scores than the original 2017 NICE
statement (adjusted P=0.009 and P=0.015), whereas no significant difference was observed
between the GUIDE-assist and human-only versions (adjusted P=0.588). Agreement was 13.3%,
66.7%,and 73.3% forthe original 2017 NICE,GUIDE-assist, and human-only recommendations,
respectively, with a significant overall difference across groups (Cochran’s Q=11.23, P=0.0036),
although pairwise comparisons did not remain significant after correction, potentially due to
limitedpowerfromthesmallsamplesize.
Discussion
In this study, we developed and validated GUIDE, a human-AI collaborative framework for
clinical guideline generation in realistic settings. The GUIDE framework supports the end-to-end
process from evidence identification to recommendation drafting by leveraging the
complementary strengths of LLM agents and human expert through a stepwise workflow. The
value of GUIDE stems not only from its functional automation but from its principled integration
into the practical workflows of guideline synthesis. Recognizing specific demands of each phase,
a tailored approach to human-AI collaboration was designed. In PICO construction, for instance,
the priority is defining a clinically sharp scope and selecting outcomes that balance benefits with
harms—aprocesswhereproactivehumanoversightisvitaltoensurerelevanceandinterpretability.
Taskslike search formulation,screening, anddata extractionaredefined by theneed fortechnical
precisionandhigh-volumeprocessing.Theseareidealforcondition-triggeredreview,whereLLM
agents manage the heavy lifting of repetitive operations, while experts intervene only when the
system flags uncertainty or inconsistency. Finally, higher-order synthesis and final deliberation
demand holistic judgment such as integrating risk, cost, and patient values, that only experts can

17
provide. This configuration ensures that the workflow achieves maximal operational efficiency
without compromising the rigor of the clinical evidence synthesis. Across benchmark evaluation,
ablationanalysis,temporalhold-outtesting,andprospectivereal-worldvalidation,GUIDEproved
to be a robust collaborative partner,assistingexperts in constructing, appraising, and synthesizing
evidencewithhighfidelityshieldingexpertsfromtheburdenofmanuallabor.
Previous studies have shown that LLMs can support individual components of the process,
such as literature screening, evidence extraction, and quality assessment, and more recent efforts
suchasQuickerhavebeguntointegratethesecomponentsintoend-to-endworkflows[21-25].Yet,
procedural continuity alone does not by itself fulfill the rigorous demands of formal guideline
development [26-28]. The essential challenge extends beyond task execution to the synthesis of
recommendations that possess both clinical interpretability and expert consensus [26]. GUIDE
was designed to address this gap by deeply embedding expert oversight throughout the entire
workflow. Through a reviewer-triggered and copilot-assisted collaboration mechanism, experts
engage both reactively to resolve automated anomalies and proactively to provide guidance at
critical decision junctures. This dual-mode integration preserves computational speed while
ensuring that expert discretion remains central to guidelines’ integrity. These features distinguish
GUIDE from earlier systems and support its role as a practical framework for bringing LLM
capabilitiesintoreal-worldproduction.
Our findings demonstrate that the proposed design performs robustly in module testing, with
its efficacy further validated through ablation studies. In the most labor-intensive stages of
guideline generation such as study selection and data extraction, the system achieved significant
timesavingsbyautomatingpreliminarytasks.Furthermore,fortasksdemandingholisticjudgment
and nuanced interpretation, such as risk of bias assessment and the formulation of final
recommendations, experts leveraged their clinical insights to instruct the AI agents or revise their
generations, ensuring the outputs were finely calibrated with real-world considerations. These
resultspositionGUIDEasmorethanatechnicaltoolforacceleratingguidelineproduction,instead
representing a form of computationally augmented consensus, in which AI-mediated evidence
processing is systematically coupled with expert deliberation. By redistributing labor across the
workflow, GUIDE reduces the amount of expert time required and redirects scarce expert

18
cognitiveresourcesawayfromlow-valuerepetitivetaskstowardcriticaljudgment,arbitration,and
consensus-building. This reframing is particularly important in guideline development, where the
ultimate value of efficiency lies in preserving expert attention for decisions that most directly
shapeclinicalvalidity.
Importantly, we further demonstrate the practical feasibility of this paradigm through
prospective validation in real-world guideline updating scenarios. Unlike retrospective
benchmarks, this setting more closely reflects the complexity, variability, and uncertainty
encounteredinrealguidelinedevelopment.Inthissetting,theindispensableroleofhumanexperts
wasrepeatedlyreinforced.Beyondcorrectinganomaliesanddiscrepanciesarisingfromautomated
processes, experts remained essential for tasks requiring arbitration and contextual judgment,
including defining the research scope, assessing evidence quality, interpreting outcomes, and
considering implementation feasibility in light of both treatment effects and broader practical
concerns. Such tasks require clinical experience, normative reasoning and the ability to balance
competing considerations that remain beyond the reach of current LLM-based automation. At the
same time, the copilot system substantially reduced the burden on experts by supporting
high-volumetaskssuchasevidenceidentification,screening,extraction,andpreliminarysynthesis
[29-31]. The human-only arm further highlighted the substantial time and workforce required for
conventionalguideline updating.Againstthisbenchmark,theGUIDE-assistedworkflow achieved
comparable evidence synthesis and recommendation updating with markedly greater efficiency.
The optimal model, therefore, is not full automation but expert-AI collaboration, in which LLMs
provide scalability and analytical support, while experts ensure methodological rigor, clinical
relevance,andcontextualappropriateness[32-36].
Several limitations of this study warrant consideration. First, while our benchmark covers
multiple specialties, its scale and diversity remain modest. Testing the framework against more
complex or controversial clinical questions is essential to confirm its generalizability. Second, the
current workflow still lacks granular automated processing in evidence synthesis. Specifically, it
cannot yet autonomously extract primary studies from retrieved systematic reviews, leaving the
finalscreeningofthesenestedreferencestohumanexperts.Third,thesystemfocusesprimarilyon
clinicaloutcomesandlacksintegratedmodulesforeconomicevaluationandmodeling.Asaresult,

19
evidence and perspective concerning cost-effectiveness and resource allocation still requires
manual synthesis by expert panels. Furthermore, certain high-level tasks such as risk-of-bias
assessment and final recommendation formulation remain sensitive to the reasoning nuances of
LLMs, occasionally showing variability compared to human consensus. Future iterations should
incorporate more explicit domain-specific criteria to bridge this gap. Additionally, the reviewer
agent’s intervention logic currently relies on static, predefined triggers; transitioning to adaptive,
learning-based strategies could more effectively balance operational efficiency with quality
control. Finally, although prospectively validated, broader multi-center trials are necessary to
evaluate the system’s robustness and long-term clinical impact across diverse organizational
contexts.
In conclusion, this study demonstrates that while LLMs alone are insufficient to fully
automate clinical guideline development, their integration within a structured, human-supervised
workflow can substantially enhance both efficiency and reliability. By shifting the focus from
automation to collaboration, our work provides a practical and scalable framework for
next-generation guideline development. More broadly, this paradigm may represent a
generalizableapproachforintegratingAIintootherhigh-stakes,knowledge-intensiveprocessesin
medicine,wherebothcomputationalefficiencyandexpertjudgmentareindispensable.
Methods
Overall study design and datasets
To evaluate the performance of GUIDE in clinical guideline generation, we constructed datasets
fordifferentevaluationpurposesfrom13publiclyavailableclinicalguidelinespublishedbyNICE
between October 26, 2017, and March 31, 2026 (for details of the dataset contents, see
Supplementary Table 5). NICE guidelines were selected because of their highly transparent
documentation,whichprovidetraceablesearchstrategies,explicitinclusionandexclusioncriteria,
anddetailed evidenceprofiles,with eachdatasetcorrespondingtothefull set oforiginalmaterials
for a single review question. We first established 12 datasets derived from four ophthalmology
guidelines covering different subspecialties for benchmark testing and ablation study
(SupplementaryTable 3).Toassesscross-disciplinarygeneralizability,wefurtherincorporated20

20
datasets derived from 6 guidelines across four clinical specialties: cardiology, endocrinology,
gastroenterology, and respiratory medicine (Supplementary Table 7). To rule out the possibility
that the strong performance of GUIDE was driven by data leakage, we constructed six additional
datasets based on four guidelines published after the training cut-off dates of the LLMs used in
this study and conducted end-to-end simulated prospective evaluations (Supplementary Table 8).
Foreachdataset,thecorrespondingoriginalmaterials,includingPICOelements,searchstrategies,
study selection records, data extraction tables, evidence quality assessments, and final
recommendations,wereextractedasgroundtruthformodularevaluation(SupplementaryTable4).
In addition, a real-world prospective study was designed by identifying a clinical question from a
2017 ophthalmology guideline (NG77: Cataracts in adults: management) in which the
recommendation had been removed for further consideration, thereby enabling a practical
evaluationofthesysteminarealguidelineupdatingscenario.
Development of human-AI collaboration principles
To establish a framework for human-AI collaboration in medical guideline development, a
multidisciplinary panel of 10 experts was convened (four ophthalmologists with expertise in
evidence-based ophthalmic practice and clinical decision-making, three EBM methodologists
specializing in systematic reviews, evidence appraisal, and guideline methodology, and three
specialists with experience in medical AI, LLMs, and clinical decision-support systems). We
balanced the panel settings across clinical, methodological, and technical domains to ensure both
scientific rigor and operational feasibility. We employed a three-round modified Delphi-like
process to define and refine human-AI collaboration principle [19]. In Round one, panelists
independently reviewed the traditional medical guideline development workflow and identified
initial areas of AI involvement regarding efficiency and quality. Round two focused on refining
role boundaries by evaluating anonymized feedback from the previous stage, with specific
emphasis on accountability, and human intervention points. Round three involved a focused
review to resolve remaining contested items and finalize the consensus-based suggestions.
Throughout the process, response anonymization was strictly maintained to mitigate hierarchical
bias and facilitate expert convergence. The resulting suggestions provided valuable guidance for
thedesignofoursystem(SupplementaryTable1and2).

21
Engineering design of GUIDE framework
We developed a user-friendly framework for human-AI collaboration in clinical guideline
generation(SupplementaryVideo1). TheframeworkcomprisesmultipleLLM-basedagents,each
configured to perform a specific step in the guideline development workflow, an AI reviewer
(ChatGPT-4.1) audits outputs and identifies when human intervention is required, an AI assistant
(ChatGPT-4.1) enables experts to interact with the agents through natural-language instructions,
and medical experts who contribute when expert judgment is required. For different task
requirements, we customized standardized prompt templates for each agent, including role
definitions, detailed task instructions, and specifications for output content and format. During
prompt development, the templates were iteratively refined and debugged using five additional
datasets (derived from NG242: Diabetic retinopathy: management and monitoring, NG82:
Age-related macular degeneration: diagnosis and management, NG98: Hearing loss in adults:
assessment and management, NG257: Fertility problems: assessment and treatment and NG250:
Pneumonia: diagnosis and management) that were not included in the subsequent evaluations.
Thesedatasetswereusedformultiple roundsofdevelopmentandsmall-scaletestingtoensurethe
reliabilityoftaskexecution.
The framework was designed to follow the core workflow of guideline development,
spanning evidence retrieval, evidence assessment, and final recommendation formulation. The
process initiates with PICO construction, where a ChatGPT-4.1-driven agent decomposes each
clinical question into structured PICO components. Upon expert validation of these components,
the agent then generates a draft review protocol outlining key methodological parameters,such as
study objectives, review type, eligibility criteria, and the planned evidence synthesis framework
(Supplementary Video 1). This protocol undergoes further expert refinement prior to literature
retrieval. To accommodate complex clinical questions, the system’s interactive interface allows
expertstomanuallyappendadditionalcontextualelementsorbroaderconsiderations.
From literature retrieval to evidence assessment, we adopt a dual-agent parallel design, in
which two independent agents using different LLM models (ChatGPT-4.1 and DeepSeek-R1)
operate concurrently, with human intervention triggered under predefined conditions. In the
literature retrieval stage, two agents independently generate search strings based on the review

22
protocol. These queries are used to search major biomedical literature databases (PubMed via
NCBIE-utilities,andScopusviatheElsevierAPI),forretrievingarticlemetadata,includingtitles,
abstracts, author lists, publication dates, and journal information. The AI reviewer judges the
consistency by previewing and comparing the sets of articles fetched by the different search
strings generated by two agents, and triggers expert intervention when substantial discrepancies
are detected, defined as either a relative difference of more than 30% in the total number of
retrieved records or insufficient overlap between the two retrieval sets (indicated by a Jaccard
similarity coefficient of less than 0.5). When either condition is met, human experts are alerted
and can either directly revise the search strategy or provide natural-language instructions for
optimization. These instructions are then translated by the assistant agent into executable search
syntax, allowing refinement of the retrieval strategy without requiring experts to manually
manipulate complex query logic. To maximize recall, the results from both retrieval rounds are
merged to form the candidate set for downstream screening. To balance recall and screening
efficiency, study selection is conducted in two stages: title-and-abstract screening followed by
full-text screening. In the first stage, the two independent agents evaluate the title and abstract of
eachretrievedrecordagainstinclusionandexclusioncriteriaderivedfromthePICOelements,and
each article is classified as either Include or Exclude. The union of included records retained by
the two agents is then carried forward to full-text screening. For full text acquisition, GUIDE
integrates openaccess repositories, including Semantic Scholar, OpenAlex, and Crossref to locate
freelyavailablePDFlinks.Forcopyright-protectedfulltextsobtainedthroughauthorizedchannels,
GUIDE also supports manual PDF upload. GUIDE supports built-in optical character recognition
(OCR) to extract machine readable text, eliminating manual transcription. Full-text eligibility
assessment is likewise performed independently by the two agents and monitored by the AI
Revieweragent. Whendiscordant decisionsoccur, therevieweragent triggersexpert intervention.
Screening results are displayed in a tabular interface, allowing human experts to inspect the
AI-generated decisions and rationales for each article and, when necessary, revise the
classification.Thefinalsetofincludedstudiesconstitutesthebodyofevidence.
The extracted text was independently analyzed by the dual-agents for data extraction,
including study design, population characteristics, intervention and comparator details, sample

23
size for each comparison group, outcome measures, and corresponding result values. These
extracted fields from each article were organized into structured evidence tables. When
discrepancies arose for the same data element, the AI reviewer initiated expert intervention, and
the experts verified the original text and corrected the extracted information as needed. Under the
GRADE framework, each clinical outcome corresponded to a body of evidence, and its quality
assessment incorporated both effect estimates and certainty of evidence. To estimate effects,
study-level data were automatically categorized into comparison- and outcome-level evidence
bodies. Clinical experts evaluated the extracted data for conceptual and clinical homogeneity to
determine whether quantitative synthesis was appropriate. Where necessary, they refined the
automated collectionsby excludingor segregatingstudies thatinappropriate forpooling. For each
eligible evidence body, the system selected an appropriate pre-specified meta-analytic approach
according to the outcome type, effect measure, review design, and completeness of the available
numerical data. The data required to calculate pooled effect estimates were then transformed into
structuredtabularinputs,includingstudyidentifiers,interventionandcomparatorgroups,outcome
data, and relevant variance information where available. These inputs were passed to R scripts
through a Python-based computational utility, which invoked the execution of the statistical
analyses via system commands. After computation, the pipeline extracted the pooled effect
estimates and associated statistical outputs and reformatted the results into structured evidence
tables suitable for subsequent GRADE assessment. Certainty was evaluated across Risk of bias,
Indirectness,Imprecision, and Inconsistency. Risk of bias was assessed at the study level foreach
outcomeusingmethodologicalassessmenttoolsmatchedtostudydesign.Forincludedstudies,the
correspondinginstrumentswereapplied,includingtheCochraneRiskofBiastool(RoBorRoB2),
ROBINS-I, and the QUADAS-2 checklist [37-40]. Indirectness was assessed according to the
degree of alignment between the study population, intervention, comparator, and outcomes and
the target clinical question defined by the PICO framework. Imprecision was evaluated primarily
on the basis of the width of confidence intervals and sample size. Inconsistency was assessed at
the body-of-evidence level by examining the variability of results across studies reporting the
same outcome. These domain-specific assessments are then synthesized and assign an overall
certainty rating for each outcome according to GRADE upgrading and downgrading rules. When

24
the two parallel agents produced discordant certainty ratings, the AI reviewer triggered expert
adjudication.
The final evidence synthesis was performed by a Delphi-like multi-agent module (all agents
in this module were driven by ChatGPT-4.1 model) that integrated the accumulated evidence and
quality assessment into comprehensive EtR materials and preliminary recommendation draft. To
convene the virtual committee, human experts dynamically selected AI participants from eight
predefined specialist roles: Clinical Practice Expert, Research Methodology Expert, Research
Ethics and Quality Expert, Evidence Synthesis Expert, Health Economics Expert, Patient and
Public Representative, Health Policy and Implementation Expert, and Biostatistician. Beyond
these established roles, experts might introduce novel roles by providing brief professional
backgrounds and role definition, these inputs were subsequently refined by the AI Committee
Chair into optimized system prompts. Once the panel was constituted based on the specific
decisioncontext,theAICommitteeChairprovidedeachpanelistwiththecompleteevidencebase.
Each AI panelist then generated an independent, role-specific assessment. Finally, the AI
Committee Chair synthesized these evaluations, identified points of convergence and divergence,
and determined whether the predefined consensus criteria had been met. Once this consensus
criterionwasmet,thedeliberationprocesswasconcluded.Ifconsensuswasnotreached,theChair
generated targeted feedback for each panelist and initiated a subsequent round of deliberation.
Throughout this process, human experts observed the discussion in real time, reviewed each
panelist’s decision and reasoning, and could provide steering instructions between rounds to
ensurethatthedeliberationremainedmethodologicallyrigorous andclinicallygrounded.Notably,
in our retrospective experimental settings, human experts did not participate in this final
deliberation step to avoid potential bias from their prior knowledge of the original guideline
recommendations.
Implementation of modular test
To assess the system’s performance at each stage and mitigate error propagation, we adopted a
modular testing approach. This approach was applied across the benchmark test, ablation study,
andcross-specialty generalization test.In all threesettings, individualcomponentswereevaluated
inisolationbyinitializingintermediateresultsfromthegold-standardguidelines,enablingadirect

25
comparison between the system’s outputs and the reference material. In the benchmark and
cross-specialty generalization tests, each dataset was paired with a senior domain specialist who
had over ten years of clinical experience in the relevant field and served as the human
collaborativepartner.
Specifically, clinical questions derived from guidelines were provided as inputs for PICO
construction. The expert-verified PICO outputs were compared against the reference using
Bidirectional Encoder Representations from Transformers Score (BERTScore) to evaluate
semantic similarity. For literature retrieval, original PICO elements and eligibility criteria derived
from protocol utilized as search inputs. To ensure arigorous evaluation of the system’s recall, the
temporal upper bound of the literature retrieval period wasmanually set to the publication date of
the source guideline. Following the search strategy reported in the source guideline, a two-stage
screening process (title-and-abstract screening followed by full-text screening) was conducted.
Screening performance was evaluated using precision (positive predictive value [PPV]), recall
(sensitivity), negative predictive value (NPV), and specificity. These metrics were calculated
usingthefollowingformulas:
푃푟푒푐�� 푃푃 = 푇푃
푇푃 + 퐹푃
，�푒푐�(푆푒�����) = 푇푃
푇푃 + 퐹
푒푔���푒 푝푟푒푑�푐��푒 �푒 푃 = 푇
푇 + 퐹
，푆푝푒푐���푐�� = 푇
푇 + 퐹푃
Here,TPdenotesstudiesselectedinagreementwiththereference,FPdenotes studiesselectedbut
not included in the reference, FN denotes studies included in the reference but not selected, and
TN denotes studies excluded in agreement with the reference. For data extraction, full-text PDFs
of the included studies and the corresponding PICO frameworks were provided. The accuracy of
the extraction was validated against the data points specified in the GRADE tables. Quality
assessment was performed based on the extracted outcomes and the effect sizes calculated for
eachPICOelement.FollowingtheGRADEmethodology,riskofbias,inconsistency,indirectness,
and imprecision were assessed individually to determine the overall certainty of the evidence.
Finally, after consensus reached by Delphi-like deliberation, the synthesized recommendations
were evaluated into three levels of consistency (exactly consistent, partially consistent,
inconsistent)relativetotheoriginalguidelines(SupplementaryTable6).
Implementation of end-to-end experiments using post-cutoff datasets

26
Before applying GUIDE in real-world guideline updating practice, to rule out the potential risk
that its strong performance was attributable to data leakage arising from prior LLMs exposure to
guidelines content during training, we constructed datasets from guidelines published after the
release dates of the LLMs used in GUIDE (ChatGPT-4.1 (April 14, 2025) and DeepSeek-R1
(January 20, 2025))and used them for an end-to-end simulated prospective evaluation. As
previously described, each dataset was paired with a senior domain specialist who had over ten
years of clinical experience in the corresponding field and served as the human collaborative
partner.Unlikethemodularevaluationwherestepswereinitializedwithgold-standardinputs,this
simulation required each step to process the direct generations of its predecessor. The process
commenced with the clinical questions as the sole input, from which the determined PICO
frameworks were passed to the retrieval stage. The retrieval literature pool was then fed into a
two-stagescreeningprocess.Allsubsequentstages,includingdataextractionandevidencequality
assessment, were performed based exclusively on the studies selected in the preceding steps, and
thefinalrecommendationsweregeneratedrelyingentirelyontheevidencesynthesizedwithinthis
specificrun.
Design and implementation of the prospective case study
We prospectively evaluated the GUIDE human–AI collaborative framework in a real-world case
study based on the NICE 2017 guideline Cataracts in adults: management (NG77). By targeting
the review question “What is the optimal strategy to facilitate simultaneous distance and near
vision following cataract surgery?” -- a topic that had been officially prioritized for updating on
the NICE website. This case study aimed to demonstrate the system’s ability to integrate modern
clinicaldataintoaformalupdatingprocess.Twoseniorcataractspecialists,eachwithovertwenty
years of clinical expertise, participated in the entire guideline-updating process. For steps
requiring human judgment or intervention, the two experts independently assessed the issue and
discussed any disagreements until a consensus decision was reached. One of the two experts was
pre-designatedbeforetheexperimentasthesystemoperatorandwasresponsibleforalloperations
performedwithinGUIDE,implementingonlytheactionsagreeduponbybothexperts.
In parallel with the GUIDE human-AI collaborative team, we convened an independent
human-only guideline-updating committee. Its evidence review group comprised two additional

27
senior cataract specialists (each with over twenty years of clinical experience) and one technical
analyst.Thisgroupwasresponsibleforevidenceretrieval,qualityassessment,anddataprocessing,
ultimately producing the bodies of evidence and their corresponding quality ratings. Throughout
the process, members were prohibited from using GUIDE system. The core decision-making
committee comprised one committee chair, four cataract specialists (including two experts
participatedintheprecedingevidencesynthesissteps),onehealthcareproviderrepresentative,one
commissioner,andonelaymember.Afterreviewingthebodiesofevidence,thecommitteeuseda
modified three-round Delphi process to complete an EtR table and formulate a draft
recommendationaddressingthesamereviewquestion.
To validate the clinical relevance of the recommendations generated through the two
updating approaches, an external consensus process was initiated with a broader cohort of 15
senior physicians with over 10 years of clinical experience in cataract care. The objective of this
survey was to evaluate the acceptability of three recommendation statements: the original 2017
recommendation, the recommendation drafted through the GUIDE human-AI collaborative
process, and the recommendation developed through the human-only process. The external
reviewers were not involved in any part of either updating process and were fully blinded to the
source of the three recommendation statements. To minimize potential preferential evaluation
based on presentation sequence, thethree statements were presented in a randomizedorder across
reviewers.Usingafive-pointLikertscalerangingfrom“stronglydisagree”(1)to“stronglyagree”
(5), the external reviewers independently assessed each recommendation. These ratting were
dichotomizedasapproval(aratingof4or5)ornon-approval(aratingof1–3).
Statistical analysis
In the benchmark test, ablation analysis, generalization test and end-to-end experiments, system
performancewasevaluatedagainstguideline-derivedgoldstandards.Forclinicalquestionparsing,
semantic similarity between generated and reference PICO elements was assessed using
BERTScore. Retrieval strategy generation and literature screening were evaluated using precision
(PPV), recall (sensitivity), NPV, and specificity. For evidence extraction and quality assessment,
categorical outputs were evaluated using classification accuracy, whereas the accuracy of
quantitative results was assessed by their deviation from reference values. Results are reported as

28
means with 95% CIs, calculated using a non-parametric bootstrap approach with 1,000,000
resamples. Paired t-tests were used for approximately normally distributed differences, and
Wilcoxon signed-rank tests were used otherwise. Approval for three recommendation statements
was reported as the number and proportion of approving reviewers. Overall differences in
approval were assessed using Cochran’s Q test. If the omnibus test was significant, pairwise
comparisons were performed using exact McNemar tests with Holm adjustment. All tests were
two-sided, with P < 0.05 considered statistically significant. All statistical analyses were
performedinR(v.4.2.3).
Data availability
The publicly available guideline documents used in this study include: Diabetic retinopathy:
management and monitoring (NICE guideline Reference number:NG242), Cataracts in adults:
management (NICE guideline Reference number:NG77), Age-related macular degeneration
(NICE guideline Reference number:NG82), Glaucoma: diagnosis and management (NICE
guideline Reference number:NG81), Chronic heart failure in adults (NICE guideline Reference
number: NG106), Adrenal insufficiency: identification and management (NICE guideline
Reference number: NG243), Cirrhosis inover 16s:assessment and management (NICE guideline
Reference number: NG50), Barrett’s oesophagus and stage 1 adenocarcinoma (NICE guideline
Reference number: NG231), Pneumonia: diagnosis and management (NICE guideline Reference
number: NG250), Asthma: diagnosis and monitoring of asthma in adults, children and young
people (NICE guideline Reference number: NG80), Falls: assessment and prevention in older
people and people 50 and over at higher risk (NICE guideline Reference number: NG249),
Fertility problems: assessment and treatment (NICE guideline Reference number: NG257),
Suspectedsepsisinpeopleaged16orover:recognition,assessmentandearlymanagement(NICE
guidelineReferencenumber: NG253),Hearinglossinadults:assessmentandmanagement(NICE
guideline Reference number: NG98). All of these guideline materials can be found in
https://www.nice.org.uk/guidance.
Code availability
GUIDE is an LLM-based copilot system designed to support expert-facing clinical practice
guideline generation and updating. We are not making the source code of GUIDE publicly

29
available at this stage owing to the safety implications of unmonitored use of such a system in
medical guideline workflows. Inappropriate deployment outside expert-supervised settings could
lead to misuse in evidence appraisal, recommendation formulation, or clinical decision-support
contextsbeyondthevalidatedscopeofthisstudy.Intheinterestofresponsibleinnovation,wewill
continue to work with clinical experts, guideline methodologists, institutional partners, and
relevant stakeholders to further validate GUIDE and explore safe onward uses. To facilitate peer
review, we have provided the source code, testing dataset, and demonstration video as
supplementary materials for the editors and expert reviewers in the submission system. The
project overview and deployment instructions are available through GitHub
(https://github.com/KimHe-RGB/GUIDE_INTRO). Additional details may be made available by
the corresponding author upon reasonable request, subject to institutional policies and approval
procedures.
Acknowledgments
We gratefully acknowledge the Guangdong Basic Research Center of Excellence for Major
Blinding Eye Diseases Prevention and Treatment for its support of this study. We also sincerely
thank all participants for their valuable contributions. We gratefully acknowledge Zhenjun, Tu,
Yunyu Lian, Luyu Liu, Kechen Wang, Yulin Zheng, and Qingqing Zhao for their valuable
feedback on the design and use of the GUIDE copilot system. This study was funded by the
National Natural Science Foundation of China (92368205 and 82441003 to H.L.; 82401313 to
R.L.), Guangdong Basic and Applied Basic Research Foundation (2024A1515012001 to W.C.;
2025A1515011616 to R.L.), China Postdoctoral Science Foundation (2023M744033 to R.L.), the
ChinaPostdoctoralScienceFoundationSpecialFund(R.L.),thePostdoctoralFellowshipProgram
of CPSF (GZB20230896 to R.L.), Guangdong Basic Research Center of Excellence for Major
Blinding Eye Diseases Prevention and Treatment (W.C.), the Science and Technology
Development Fund, Macau SAR (File No. 0010/2023/AKP to H.L.), Basic scientific research
projects of Sun Yat-sen University (23ykcxqt002 to H.L.), the Science and Technology Planning
Projects of Guangdong Province (2018B010109008 to H.L.), Hainan Province Clinical Medical
Center (H.L.). “3510” Medical Innovation Leadership Program, Fundamental Research Funds for

30
theCentralUniversities,SunYat-senUniversity(20263510YXON012toW.C.).
Author Contributions
H.L. and W.C. contributed tothe concept of the study and designed the research;Y.L, X.H.,J.D.,
Z.L.,J.C.,R.L.,C.Z.,Y.S.,W.P.,J.Q.,X.W.,D.Y.,G.L.,A.X.,andS.Y.collectedthedata;W.C.,
Y.L,X.H.,J.D.,Z.L.,J.C.,W.P.,andG.L.conductedthestudy;Y.L,X.H.,J.D.,andJ.Q.analyzed
the data; W.C., Y.L, X.H., J.D., Z.L., and C.Z. drafted the manuscript; H.L., W.C., Y.Lin, X.H.,
J.D., Z.L., R.L., C.Z., Y.S., J.Q., and S.Y. critically revised the manuscript; H.L., X.H., Z.L., and
W.P.performedthetechnicalreview;andallauthorsdiscussedtheresultsandprovidedcomments
regardingthemanuscript.
Competing interests
Theauthorsdeclarenoconflictsofinterest.

31
References
1. Committee on Standards for Developing Trustworthy Clinical Practice Guidelines, Board on
Health Care Services, Institute of Medicine. Clinical Practice Guidelines We Can Trust.
(GrahamR,MancherM,WolmanDM,GreenfieldS,SteinbergE,eds.).NationalAcademies
Press;2011:13058.doi:10.17226/13058
2. Lugtenberg M, Burgers JS, Westert GP. Effects of evidence-based clinical practice
guidelines on quality of care: a systematic review. Quality and Safety in Health Care.
2009;18(5):385-392.doi:10.1136/qshc.2008.028043
3. Shekelle PG, Ortiz E, Rhodes S, et al. Validity of the Agency for Healthcare Research and
QualityClinicalPracticeGuidelines:HowQuicklyDoGuidelinesBecomeOutdated?JAMA.
2001;286(12):1461.doi:10.1001/jama.286.12.1461
4. Bastian H, Glasziou P, Chalmers I. Seventy-Five Trials and Eleven Systematic Reviews a
Day: How Will We Ever Keep Up? PLoS Med. 2010;7(9):e1000326.
doi:10.1371/journal.pmed.1000326
5. Yao X, Saha A, Saravanan S, Low A, Sussman J. A Study Protocol for a Comprehensive
EvaluationofTwoArtificialIntelligence-BasedToolsinTitleandAbstractScreeningforthe
Development of Evidence-Based Cancer Guidelines. Cancer Innov. 2025;4(4):e70021.
Published2025Jun29.doi:10.1002/cai2.70021
6. Shekelle PG. Updating practice guidelines. JAMA. 2014;311(20):2072-2073.
doi:10.1001/jama.2014.4950
7. Ioannidis JPA. The Mass Production of Redundant, Misleading, and Conflicted Systematic
Reviews and Meta-analyses. Milbank Quarterly. 2016;94(3):485-514.
doi:10.1111/1468-0009.12210
8. Alonso-Coello P, Schünemann HJ, Moberg J, et al. GRADE Evidence to Decision (EtD)
frameworks: a systematic and transparent approach to making well informed healthcare
choices.1:Introduction.BMJ.PublishedonlineJune28,2016:i2016.doi:10.1136/bmj.i2016
9. Akl EA, Meerpohl JJ, Elliott J, et al. Living systematic reviews: 4. Living guideline
recommendations. Journal of Clinical Epidemiology. 2017;91:47-53.
doi:10.1016/j.jclinepi.2017.08.009

32
10. KohaneIS.GuidelineMachines.NEJMAI.2026;3(7).doi:10.1056/AIe2600680
11. LaiH,LiuJ,BaiC,etal.Languagemodelsfordataextractionandriskofbiasassessmentin
complementarymedicine.npjDigitMed.2025;8(1):74.doi:10.1038/s41746-025-01457-w
12. Li D, Jiang N, Huang K, et al. Streamlining evidence based clinical recommendations with
largelanguagemodels.npjDigitMed.2025;8(1):793.doi:10.1038/s41746-025-02273-y
13. Lieberum JL, Toews M, Metzendorf MI, et al. Large language models for conducting
systematic reviews: on the rise, but not yet ready for use—a scoping review. Journal of
ClinicalEpidemiology.2025;181:111746.doi:10.1016/j.jclinepi.2025.111746
14. Gu B, DesaiRJ, Lin KJ, Yang J. Probabilistic medicalpredictions oflarge languagemodels.
npjDigitMed.2024;7(1):367.doi:10.1038/s41746-024-01366-4
15. Tang L, Sun Z, Idnay B, et al. Evaluating large language models on medical evidence
summarization.npjDigitMed.2023;6(1):158.doi:10.1038/s41746-023-00896-7
16. Christof M, Armoundas AA. Implications of integrating large language models into clinical
decisionmaking.CommunMed.2025;5(1):490.doi:10.1038/s43856-025-01216-8
17. Tudor Car L, Wong TY, Majeed A, Collins GS. Artificial intelligence and the future of
evidence-basedmedicine.Nat.Health.2026;1:268–271.doi:10.1038/s44360-025-00002-z
18. Zheng EL, Jin W, Hamarneh G, Lee SSJ. From Human-in-the-Loop to Human-in-Power.
TheAmericanJournalofBioethics.2024;24(9):84-86.doi:10.1080/15265161.2024.2377139
19. Diamond IR, Grant RC, Feldman BM, et al. Defining consensus: a systematic review
recommends methodologic criteria for reporting of Delphi studies. J Clin Epidemiol.
2014;67(4):401-409.doi:10.1016/j.jclinepi.2013.12.002
20. Nussbaumer-Streit B, Ellen M, Klerings I, et al. Resource use during systematic review
production varies widely: a scoping review. J Clin Epidemiol. 2021;139:287-296.
doi:10.1016/j.jclinepi.2021.05.019
21. Wang Z, Cao L, Danek B, Jin Q, Lu Z, Sun J. Accelerating clinical evidence synthesis with
large language models. NPJ Digit Med. 2025;8(1):509. Published 2025 Aug 8.
doi:10.1038/s41746-025-01840-7
22. Cao C, Sang J, Arora R, et al. Development of Prompt Templates for Large Language
Model-Driven Screening in Systematic Reviews. Ann Intern Med. 2025;178(3):389-401.

33
doi:10.7326/ANNALS-24-02189
23. Homiar A,ThomasJ,OstinelliEG, etal.Development andevaluation ofpromptsforalarge
languagemodeltoscreentitlesandabstractsinalivingsystematicreview.BMJMentHealth.
2025;28(1):e301762.Published2025Jul22.doi:10.1136/bmjment-2025-301762
24. Sanghera R, Thirunavukarasu AJ, El Khoury M, et al. High-performance automated abstract
screening with large language model ensembles. J Am Med Inform Assoc.
2025;32(5):893-904.doi:10.1093/jamia/ocaf050
25. HasanB,SaadiS,RajjoubNS,etal.Integratinglargelanguagemodelsinsystematicreviews:
a framework and case study using ROBINS-I for risk of bias assessment. BMJ Evid Based
Med.2024;29(6):394-398.Published2024Nov22.doi:10.1136/bmjebm-2023-112597
26. National Institute for Health and Care Excellence. Developing NICE Guidelines: The
Manual.London:NationalInstituteforHealthandCareExcellence(NICE);July22,2015.
27. Schünemann HJ, Wiercioch W, Brozek J, et al. GRADE Evidence to Decision (EtD)
frameworks for adoption, adaptation, and de novo development of trustworthy
recommendations: GRADE-ADOLOPMENT. J Clin Epidemiol. 2017;81:101-110.
doi:10.1016/j.jclinepi.2016.09.009
28. Brouwers MC, Kho ME, Browman GP, et al. AGREE II: advancing guideline development,
reporting and evaluation in health care. CMAJ. 2010;182(18):E839-E842.
doi:10.1503/cmaj.090449
29. Martínez García L, Sanabria AJ, García Alvarez E, et al. The validity of recommendations
from clinical guidelines: a survival analysis. CMAJ. 2014;186(16):1211-1219.
doi:10.1503/cmaj.140547
30. Hodder RK, Vogel JP, Wolfenden L, Turner T. Living Systematic Reviews and Living
Guidelines to Maintain the Currency of Public Health Guidelines. Am J Public Health.
2024;114(1):21-26.doi:10.2105/AJPH.2023.307450
31. Tendal B, Vogel JP, McDonald S, et al. Weekly updates of national living evidence-based
guidelines:methodsfortheAustralianlivingguidelinesforcareofpeoplewithCOVID-19.J
ClinEpidemiol.2021;131:11-21.doi:10.1016/j.jclinepi.2020.11.005
32. Hager P, Jungmann F, Holland R, et al. Evaluation and mitigation of the limitations of large

34
language models in clinical decision-making. Nat Med. 2024;30(9):2613-2622.
doi:10.1038/s41591-024-03097-1
33. Williams CYK, Miao BY, Kornblith AE, Butte AJ. Evaluating the use of large language
models to provide clinical recommendations in the Emergency Department. Nat Commun.
2024;15(1):8236.Published2024Oct8.doi:10.1038/s41467-024-52415-1
34. Goh E, Gallo R, HomJ,et al.Large LanguageModel Influence on DiagnosticReasoning:A
Randomized Clinical Trial. JAMA Netw Open. 2024;7(10):e2440969. Published 2024 Oct 1.
doi:10.1001/jamanetworkopen.2024.40969
35. Goh E, Gallo RJ, Strong E, et al. GPT-4 assistance for improvement of physician
performance on patient care tasks: a randomized controlled trial. Nat Med.
2025;31(4):1233-1238.doi:10.1038/s41591-024-03456-y
36. Everett SS, Bunning BJ, Jain P, et al. From Tool to Teammate: A Randomized Controlled
Trial of Clinician-AI Collaborative Workflows for Diagnosis. Preprint. medRxiv.
2025;2025.06.07.25329176.Published2025Jun8.doi:10.1101/2025.06.07.25329176
37. Higgins JP,Altman DG, Gøtzsche PC,et al.TheCochrane Collaboration'stool forassessing
risk of bias in randomised trials. BMJ. 2011;343:d5928. Published 2011 Oct 18.
doi:10.1136/bmj.d5928
38. Sterne JAC, Savović J, Page MJ, et al. RoB 2: a revised tool for assessing risk of bias in
randomisedtrials.BMJ.2019;366:l4898.Published2019Aug28.doi:10.1136/bmj.l4898
39. Sterne JA, Hernán MA, Reeves BC, et al. ROBINS-I: a tool for assessing risk of bias in
non-randomised studies of interventions. BMJ. 2016;355:i4919. Published 2016 Oct 12.
doi:10.1136/bmj.i4919
40. Whiting PF, Rutjes AW, Westwood ME, et al. QUADAS-2: a revised tool for the quality
assessment of diagnostic accuracy studies. Ann Intern Med. 2011;155(8):529-536.
doi:10.7326/0003-4819-155-8-201110180-00009

35

36
Fig.1 | Clinical guideline updating workflow and human-GUIDE collaboration flowchart. a,
OverviewoftheGUIDEworkflowunderahuman-in-the-loopcopilotmodel.Startingfroma
clinicalquestion,GUIDEsupportsPICOconstruction,literatureretrievalandscreening,evidence
assembly,dataextraction,GRADE-basedqualityassessment,evidence-to-recommendation
materialsynthesis,multi-agentconsensus,andgenerationofclinicalrecommendations.
Throughouttheprocess,AIagentsperformstructuredevidence-synthesistasks,whereashuman
expertsretainsupervisoryauthorityandintervenewhenpredefinedconditionsaremet. b,Detailed
workflowshowingthetriggercriterionforexpertinvolvement.GUIDEdecomposesthereview
questionintoPICOelements,coordinatesindependentagentsforsearch,screening,dataextraction
andevidencequalityappraisal,andsynthesizesevidence-to-recommendationmaterialsthrougha
Delphi-likemulti-agentprocess.Ateachkeystage,anAIReviewermonitorspredefinedsignalsof
uncertaintyorinconsistency,suchasdiscordantretrievalresults,screeningdisagreements,
inconsistentextracteddataordivergentcertaintyratings,andtriggersexpertverification,
adjudicationorreassessment.Thiscondition-triggeredoversightenablesGUIDEtocombine
automatedefficiencywithtransparentandaccountablehumangovernance.

37
Fig.2 | Performance of the human-GUIDE collaborative framework in the benchmark
evaluation using 12 ophthalmology datasets. a,RecallandprecisionofGUIDEacrossliterature
retrieval,title-and-abstractscreening,andfull-textscreening.GUIDEachievedhighrecallacross
allstages,whileprecisionprogressivelyincreasedacrossthethreesteps. b,Agreementbetween
GUIDEandhumanreferencestandardsinevidenceassessment,includingriskofbias,indirectness,
imprecision,inconsistency,andoverallcertaintygrading.Ineachboxplot, thetrianglerepresents
themean,thecentrallinedenotesthemedian,theboxindicatestheinterquartilerange,andthe
whiskersextendtovalueswithin1.5×theinterquartilerange. c,ConsistencybetweenGUIDE’s
recommendationoutputsandoriginalrecommendationsassessedbydomainexpert. d,Time
expenditureofGUIDEcopilotsystemandhumanexpertsacrosstheguidelinedevelopment
workflow.GUIDEcontributedthemajorityofprocessingtime,whileexpertinvolvementwas
concentratedonoversight,arbitration,andrefinement.

38

39
Fig. 3 | Ablation tests comparing human-GUIDE collaboration versus GUIDE alone: aThe
recallrateoftheliteraturesearch. bTherecallandaccuracyratesofliteraturescreening. c–dThe
consistencybetweentheGUIDEandtheNICEguidelinesfortheevidenceassessment(RoB,
indirectness,imprecision,inconsistency,andtotalevidencequalityevaluations),and
recommendationgenerationmodules(n=12).Theerrorbarsrepresentthe95%confidence
intervals(CIs).Statisticalsignificanceisindicatedusingpairedcomparisons,withnsdenotingnot
significant,**denotingP<0.01and***denotingP<0.001.

40
Fig.4 | Performance of the human-GUIDE collaborative framework in the generalization test
using 20 datasets derived from four different specialties (cardiology, endocrinology,
gastroenterology, and respiratory medicine). a,RecallandprecisionofGUIDEacrossliterature
retrieval,title-and-abstractscreening,andfull-textscreening. b,ConsistencyofGUIDE-assisted
evidenceassessmentacrossriskofbias,indirectness,imprecision,inconsistency,andevidence
quality. c,ConsistencybetweenGUIDE’srecommendationoutputsandoriginalrecommendations
assessedbydomainexpert.Ineachboxplot,thetrianglerepresentsthemean,thecentralline
denotesthemedian,theboxindicatestheinterquartilerange,andthewhiskersextendtovalues
within1.5×theinterquartilerange. d,Timeexpenditureacrosstheguideline-updatingworkflow,
comparingGUIDEprocessingtimewithhumanexpertinvolvementforPICOconstruction,
literaturesearch,literaturescreening,dataextraction,evidenceassessment,andrecommendation
generation.

41
Fig.5 | human-GUIDE’s end-to-end performance in simulated prospective experiments. a,
Screeningperformanceacrosssixpost-cutoffNICEguidelinedatasets,showingconsistentlyhigh
recallandprecisiondespitepotentialupstreamerrorpropagation.Ineachboxplot,thecentralline
denotesthemedian,theboxindicatestheinterquartilerange,thewhiskersextendtovalueswithin
1.5×theinterquartilerange,andthetrianglerepresentsthemean. b,Assessmentofdrafted
recommendationsinthefinalstep,showing100.00%directionalagreementwiththeoriginal
NICErecommendations.

42
Supplementary Fig. 1 | Example of search strategy revision through expert’s instructions to
the AI assistant.AfterGUIDEconstructsthestructuredPICOframeworkfromtheclinical
question,twoindependentLLM-basedsearchagentsgenerateretrievalstrategiesinparallel.The
AIReviewercomparestheresultingstrategiesandretrievaloutputstoidentifypotential
unreliability,suchaslowoverlapormarkeddiscrepanciesinretrievalvolume.Whenrevisionis
needed,expertsprovidenatural-languageinstructionsthroughtheassistantagent,whichtranslates
theseinstructionsintoupdatedBooleansearchstrings,enablingstrategyrefinementwithoutdirect
manualeditingofcomplexsyntax.

43
Supplementary Fig. 2 | GUIDE-assisted literature screening workflow and rationale display.
Theinterfacesupportssequentialtitle-and-abstractandfull-textscreeningbyparallelscreening
agents.Retrievedrecordsareindependentlyassessedforeligibility,withinclusionorexclusion
labels,confidencelevels,andconciserationalesdisplayedforexpertreview.Whenagentoutputs
areconsistent,thesystempresentsasummarizedscreeningjustification;whendiscrepanciesarise,
detailedagent-specificreasoningisshowntofacilitatehumanadjudicationandcorrection.

44
Supplementary Fig. 3 | Data extraction interface aligned with the PICO framework.
Forstudiesincludedafterfull-textscreening,GUIDEsupportsstructuredextractionofstudy-level
textualdataandoutcome-levelnumericalresults.Expertscaneditorre-extractindividualfieldsto
verifydiscrepanciesagainsttheoriginalfulltextandensureconsistencywiththePICO-defined
evidenceframework.

45
Supplementary Fig. 4 | Delphi-like multi-agent evidence synthesis and recommendation
drafting.ProcessedevidenceissubmittedtoaDelphi-likeconsensusmodule,inwhichhuman
expertscanselectandassembleavirtualpanelwithdifferentrolespecifications.Panelmembers
independentlyreviewtheevidence,providejudgments,andstatefinalrecommendationdecisions
withsupportingrationales.Thecommitteeagentsynthesizestheseinputsintoan
evidence-to-recommendationreportanddraftrecommendation,whichexpertscanfurtherrevise
andfinalizethroughdeliberationandconsensus.

46
Supplementary Table 1. Proposed suggestions for human-AI collaboration
Category Suggestion Description
Core Principles Suggestion1 Thecollaborationshouldfollowa“human-in-the-loop”model:
AI executes rule-based, bulk processing and preliminary
drafting, whereas human experts provide professional
judgement and final decision-making. This collaboration
operates within a dynamic framework that iteratively
optimizes the human-AI division of labor in alignment with
thecharacteristicsandcomplexityoftasks.
Proposed Human-AI
Collaboration Modes
Suggestion2 Proactive human-intervention mode: Applicable to scenarios
where AI capabilities are not yet mature or decision-making is
criticalandrequiresnuancedjudgment.
Suggestion3 Condition-triggered human review mode: Applicable to
scenarios where AI performance is generally robust, but
potential anomalies or uncertainties may arise, triggering
humanreviewaccordingtopredefinedcriteria.

47
Supplementary Table 2. Task characteristics across the guideline generation workflow and
corresponding preferable human-AI collaboration modes
Step Description Challenge Preferable collaboration
mode
PICO Construction Formulatingtheclinical
questionintoPICO
components(Population,
Intervention,Comparison,
Outcome).
Definingafocusedscopeand
selectingclinicaloutcomes
thatreflectbothrisksand
benefits.
Proactive
human-interventionmode
Search Strategy Formulation Developingdatabase-specific
searchstringsbasedonthe
PICOframework.
Mappingandexpandingcore
entitiesintosearchterms,
formulatingsearchstrategies
inaccordancewithspecific
syntaxrules.
Condition-triggeredhuman
reviewmode
Literature Screening Selectingrelevantstudies
fromsearchresultsbasedon
inclusion/exclusioncriteria.
Processinglargevolumesof
literaturefollowing
inclusion/exclusioncriteria.
Condition-triggeredhuman
reviewmode
Data Extraction Collectingkeyvariablesand
statisticaldataforanalysis
andqualityassessment.
Handlinginconsistentdata
formatsandaccurately
extractingfromprimary
studies.
Condition-triggeredhuman
reviewmode
Evidence Quality Assessment Assessingthecertaintyof
evidenceandriskofbias
usingtheGRADEcriteria.
Detectingpotentialbiasin
boththepresenceandabsence
ofinformation,makinga
holisticjudgmenttailoredto
theuniqueconditionsof
studies.
Proactive
human-interventionmode
Evidence-to-Recommendation
(EtR) Synthesis
Synthesizingclinical
evidenceintothe
Evidence-to-Decisionreport.
Accountingforpractical
factorslikecost,feasibility,
andpatientvaluesalongside
Proactive
human-interventionmode

48
clinicaleffects.
Recommendation
Formulation
Reconcilingexpertopinions
toreachafinal,unified
recommendation.
Resolvingexpert
disagreementstoproducea
clearanddeliberateclinical
statement.
Proactive
human-interventionmode

49
Supplementary Table 3. Overview of the benchmark dataset
Specialty NICE Guideline Publication Date Review question
Ophthalmology
NG242:Diabetic
retinopathy:
managementand
monitoring
13-Aug-24
Whatistheeffectivenessofdifferentthresholdsor
criteriaforstartingtreatmentfornon-proliferative
diabeticretinopathy,proliferativediabetic
retinopathy,anddiabeticmacularoedema?
Whatistheeffectofintensivetreatmentstorapidly
lowerbloodglucoselevelsonprogressionof
diabeticretinopathyanddiabeticmacularoedema?
Inpeoplewhoareabouttoundergoorwhohave
undergonecataractsurgery,whatisthe
effectivenessoftreatments(before,duringorafter
surgery)formanaging:
•non-proliferativediabeticretinopathy
•proliferativediabeticretinopathy
•diabeticmacularoedema?
NG77:Cataractsin
adults:management
26-Oct-17
Whatistheoptimalstrategytoaddresspre-existing
regularastigmatisminpeopleundergoingcataract
surgery?
Aretintedlenseseffectiveinpreventingthe
progressionofage-relatedmaculardegeneration
comparedwithcolourlesslensesincataract
surgery?
Whatistheeffectivenessofsedationasanadjunct
tolocalanaesthesiaduringcataractsurgery?
Whatistheeffectivenessofinterventionsto

50
increasepupilsizetoimprovevisualoutcomesand
reducecomplicationsduringphacoemulsification
cataractsurgery?
Whatistheoptimaltypeandadministrationof
anesthesiaforcataractsurgery?
NG82:Age-related
macular
degeneration:
diagnosisand
management
23-Jan-18
Whatistheeffectivenessofpsychologicaltherapies
forAMD?
Whatstrategiesandtoolsareusefulfor
self-monitoringforpeoplewithAMD?
Whatistheeffectivenessofadjunctivetherapiesfor
thetreatmentoflateAMD(wetactive)?
NG81:Glaucoma:
diagnosisand
management
01-Nov-17
Whatistheeffectivenessandcost-effectivenessof
selectivelasertrabeculoplasty(SLT)asafirstline
treatmentcomparedwithintraocularpressure
loweringeyedropsinocularhypertension(OHT)or
chronicopen-angleglaucoma(COAG)adult
patients?

51
Supplementary Table 4. Reference Answers and Evaluation Metrics Used in Module Testing
Step Input GUIDE Output
Reference Answers
(from guideline)
Evaluation Metrics
Clinical Question
Parsing
Naturallanguageclinical
question(fromsource
guidelines)
StructuredPICOelements
PICOdefinitionsfromthereview
protocol
BERTScore
Retrieval Strategy
Generation
PICOrepresentation
Searchstrategy(databases,
filters,studytypes,
keywords)
Searchprotocol Recall
Study Selection Retrievedcandidatestudies Includedstudylist
Includedstudiesreportedinthe
guideline
Recall;Precision
Evidence Extraction Includedstudies,PICO
Structuredstudy-leveldata
(categorical)and
quantitativeresults
Evidencetableswithsummaryof
effectivenessevidence
Typeclassification
accuracy;Numerical
accuracy
Evidence Quality
Assessment
PICO,Synthesizedevidence
table
Qualityratings
Qualityassessmentsreportedin
evidencetablesandmethods
Classification
accuracy
Recommendation
Generation
PICO,Evidenceandquality
assessment
Guideline-style
recommendation
Committeefinalrecommendation
Customized
evaluationrubric

52
Supplementary Table 5. Description of the Dataset Composition
Clinical Question Definition
Data Field Description Example Data Type
Clinical Question Theprimaryclinicalquestionaddressedby
theguideline
“Whatistheeffectivenessofdifferent
thresholdsforinitiatingtreatmentindiabetic
retinopathy?”
String
Population Targetpatientgroupsdefinedinthereview
(PinPICO)
Non-proliferativeDR;proliferativeDR;DMO List[String]
Intervention Interventionsbeingevaluated(IinPICO) Earlylaser;anti-VEGF;vitrectomy List[String]
Comparator Comparatorconditions(CinPICO) Deferredtreatment;standardthreshold List[String]
Outcomes Clinicaloutcomesofinterest(OinPICO) Visualacuity;retinalthickness;qualityoflife List[String]
Literature Retrieval and Screening
Data Field Description Example Data Type
Retrieved Records Bibliographicrecordsidentifiedduringthe
initialliteraturesearch
Alistofcandidatestudiesreturnedby
databasesearch
List[Record]
Retrieved Record
Metadata
Citation-levelmetadataforeachretrieved
record
Title;authors;publicationyear;journal;
databasesource
RecordObject
Screened-in
Records
Recordsretainedaftertitle/abstract
screeningforfull-textassessment
Studiesjudgedpotentiallyeligibleafterinitial
screening
List[Record]
Full-text Assessed
Records
Recordsundergoingfull-texteligibility
assessment
Candidatestudiesreviewedinfulltext List[Record]
Included Studies Finalstudiesincludedinevidencesynthesis Bakeretal.,2019;Elmanetal.,2015 List[Record]
Study-Level Evidence Extraction
Data Field Description Example Data Type
Study Identifier Uniquestudyreference Baker2019 String
Study Design Studymethodology Randomizedcontrolledtrial Categorical
Population
Characteristics
Baselinepatientcharacteristics DMOwithgoodvisualacuity Text
Intervention Descriptionofintervention Promptintravitrealanti-VEGF Text

53
Details
Comparator
Details
Descriptionofcomparator Observationwithdeferredtreatment Text
Outcome Name Specificclinicalendpoint Lossof≥15lettersinBCVA String
Sample Size
(Outcome-Level)
Numberofobservationscontributingtothe
estimate
420eyes Integer
Effect Type Statisticalmeasureused RiskRatio Categorical
Effect Size Estimatedeffectvalue 0.92 Float
Confidence
Interval
Lowerandupperboundsofestimate [0.82,1.03] Tuple
Evidence Quality Assessment
Data Field Description Example Data Type
Risk of Bias
Assessment Tool
Toolusedforqualityassessment RoB2;ROBINS-I Categorical
Risk of Bias Downgradeduetostudylimitations Downgraded(seriouslimitations) Categorical
Inconsistency Variabilityacrossstudyresults Noseriousinconsistency Categorical
Indirectness Applicabilityofevidencetotarget
population
Noseriousindirectness Categorical
Imprecision Uncertaintyineffectestimates Seriousimprecision Categorical
Other
Considerations
Additionalupgrading/downgradingfactors None String
Final Certainty
Rating
Overallinterpretationofeffect Favoursearlytreatment Categorical
Recommendation-Level Extraction
Data Field Description Example Data Type
Evidence
Summary
Narrativesummaryoffindings Earlylaserreducesriskofseverevisualloss Text
Benefit Summary Summaryofbenefits Earlytreatmentreducesprogression Text
Harm Summary Summaryofharmsorrisks Limitedorunclearharms Text

54
Clinical Judgment Expertinterpretationbeyonddata Earlypanretinalphotocoagulationalignswith
clinicalpractice
Text
Resource
Considerations
Costorfeasibilityconsiderations Increasedresourceuseforearlytreatment Text
Recommendation
Statement
Finalsummarizedrecommendation OfferPRPatdiagnosisofproliferativeDR Text

55
Supplementary Table 6. Evaluation criteria for the consistency of recommendations
Consistency Level Description
Exactly Consistent Thesemanticmeaningofcoreelements(e.g.,recommendationdirection,
targetpopulation,andinterventions)completelymatchestheoriginal
guideline,withnosubstantivedifferences.
Partially Consistent Theoverallrecommendationdirectionisconsistent,butthereare
differencesoromissionsregardingthespecificscopeofthetarget
population,interventiondetails,orimplementationconditions.
Inconsistent Therecommendationdirectionsarecontradictory,orthesystemoutputhas
nocorrespondingstatementintheoriginalguideline.
Note:Theoverallagreementrateiscalculatedas:AgreementRate=(ExactlyConsistent
Recommendations+PartiallyConsistentRecommendations)/TotalRecommendations.

56
Supplementary Table 7. Overview of the generalization test dataset
Specialty NICE Guideline Publication Date Review question
Cardiovascular
NG106:Chronicheart
failureinadults
3-Sep-25
Whatistheclinicalandcosteffectivenessof
mineralocorticoidreceptorantagonistsinpeople
withheartfailurewithpreservedejection
fraction?
Whatistheclinicalandcosteffectivenessofsalt
and/orfluidrestrictioninpeoplewithheart
failure?
Whatistheclinicalandcosteffectivenessof
ironsupplementationinpeoplewithchronic
heartfailureandirondeficiency?
Whatistheclinicalandcosteffectivenessof
pharmacologicalinterventionsforheartfailure
inpeoplewithheartfailurewhoalsohave
chronickidneydisease?
Endocrinesystem
NG243:Adrenal
insufficiency:identification
andmanagement
28-Aug-24
Whatistheclinicalandcosteffectivenessof
glucocorticoidsfortheroutinemanagementof
secondaryandtertiaryadrenalinsufficiency?
Whatistheclinicalandcosteffectivenessof
pharmacologicaltreatmentsfortheroutine
managementofprimaryadrenalinsufficiency?
Inpeopleatriskofadrenalinsufficiency

57
becauseofprolongedcorticosteroiduse,whatis
thebestwaytomanagecorticosteroid
withdrawalwhencorticosteroidsarenolonger
neededtocontroldiseaseactivity?
Gastrointestinal
NG50:Cirrhosisinover
16s:assessmentand
management
8-Sep-23
Whatistheclinicalandcost-effectivenessof
non-selectivebeta-blockersfortheprimary
preventionofbleedinginpeoplewith
oesophagealvaricesduetocirrhosis?
Whatistheclinicalandcost-effectivenessof
endoscopicbandligationfortheprimary
preventionofbleedinginpeoplewith
oesophagealvaricesduetocirrhosis?
Whatisthemostclinicalandcost-effective
prophylacticantibioticfortheprimary
preventionofbacterialinfectionsinpeoplewith
cirrhosisanduppergastrointestinalbleeding?
Whatistheclinicalandcost-effectivenessof
antibioticscomparedwithplaceboforthe
primarypreventionofspontaneousbacterial
peritonitis(SBP)inpeoplewithcirrhosisand
ascites?
Whatisthemostclinicallyandcost-effective
interventionforthefirst-linetreatmentofan
episodeofacutehepaticencephalopathyin
peoplewithcirrhosis?
Whatistheclinicalandcost-effectivenessof
transjugularintrahepaticportosystemicshunt
(TIPS)comparedwithlarge-volume

58
paracentesis(LVP)withalbumininthe
managementofdiuretic-resistantascitesdueto
cirrhosis?
NG231:
Barrett’s
oesophagusand
stage1
adenocarcinoma
8-Feb-23
ForadultswithBarrett’soesophagus,whatis
theclinicalandcosteffectivenessof
pharmacologicalinterventions(suchasantacids,
aspirin,H2receptorantagonists,protonpump
inhibitors)inreducingprogressiontodysplasia
orcancer?
Respiratory
system
NG250:Pneumonia:
diagnosisandmanagement
2-Sep-25
Whatistheclinicalandcosteffectivenessof
careoutsideoftheacutehospitalsetting(for
exampleusingintermediatecare,hospitalat
home,orvirtualwards)forpeoplewith
community-acquiredpneumoniawhowould
otherwisebeadmittedtohospital?
Areshorterdurationsofantibiotictreatment
effectiveandcost-effectiveattreatingbabies,
childrenandyoungpeoplewith
community-acquiredpneumoniacomparedto
longertreatmentcourses?
Inadultswithcommunity-acquiredpneumonia,
whatistheclinicalandcosteffectivenessof
corticosteroidtreatmentinadditiontoantibiotic
treatment,comparedwithantibiotictreatment
alone?
Theclinicalandcost-effectivenessof
corticosteroidtreatmentinadditiontoantibiotic
treatmentcomparedwithantibiotictreatment

59
aloneinchildrenwithCAPorHAP?
NG80:Asthma:diagnosis
andmonitoringofasthmain
adults,childrenandyoung
people
29-Nov-17
Inpeoplewithasthma,whatistheclinicaland
cost-effectivenessofusingmeasuresof
pulmonaryfunctionassessingasthmacontrol
(forexample,spirometryandpeakexpiratory
flow)tomonitorasthma?
Inpeoplewithasthma,whatistheclinicaland
cost-effectivenessofusingindirectchallenge
testswithmannitolordirectchallengetestswith
histamineormethacholineformonitoring
asthmacontrol?

60
Supplementary Table 8. Overview of the simulate end-to-end prospective test dataset
NICE Guideline Publication Date Review question
NG249: Falls:assessment
andpreventioninolder
peopleandpeople50and
overathigherrisk
29-Apr-25
What are the most effective methods for
maximising participation, adherence and
continuationoffallspreventioninterventions?
What are the most clinically and cost-effective
methods for falls prevention in older people in
residentialcaresettings?
NG257:Fertility
problems:
assessmentandtreatment
31-Mar-26
Whatistheclinicalandcosteffectivenessoftests
for endometrial receptivity (including gene
expressionanalysisandmicrobiologicalanalysis)
as a treatment add-on for people undergoing
fertilitytreatment?
What is the clinical and cost effectiveness of
treating DNA fragmentation (identified from
screening ejaculated sperm) on reproductive
outcomes for people with male factor fertility
problems?
NG253:Suspectedsepsis
inpeopleaged16or
over:recognition,
assessmentandearly
management
19-Nov-25
What is the most clinical and cost-effective
intravenous fluid for resuscitation ofpeople aged
16oroverwithsuspectedsepsis?
In people aged 16 or over with suspected sepsis,
how safe is the peripheral administration of
intravenous vasopressors compared to central
lineadministration?

61
Supplementary Information 1. PICO criteria (prospective study, GUIDE-assisted group)
Generation by GUIDE Revision by human expert
Population Patientsundergoingcataractsurgery Adults(18yearsandolder)undergoingphacoemulsification
cataractsurgeryandintraocularlens(IOL)implantationinone
orbotheyes
Interventions Anytypeofintraocularlensestofacilitate
simultaneousdistanceandnearvision(e.g.,
multifocalintraocularlenses,monovision
withmonofocallenses,extendeddepthof
focuslenses)
1. Anytypeofnon-accommodatingintraocularlensesto
facilitatesimultaneousdistanceandnearvision(e.g.,
multifocalintraocularlenses,monovisionwithmonofocal
lenses,extendeddepthoffocuslenses)
2. Standardmonofocalintraocularlenses(providingclear
distancevisiononly,requiringreadingglassesfornearvision)
Comparators Standardmonofocalintraocularlenses
(providingcleardistancevisiononly,
requiringreadingglassesfornearvision)
Alllistedinterventionsvs.eachother
Outcomes  Visualacuityatdistanceandnear
 Spectacleindependence
 Contrastsensitivity
 Patientsatisfaction
 Qualityoflife
 Incidenceofvisualdisturbances(e.g.,
glare,halos)
 Needforadditionalcorrective
procedures
 Visualacuityatdistanceandnear
 Spectacleindependence
 Contrastsensitivity
 Patientsatisfaction
 Qualityoflife
 Incidenceofvisualdisturbances(e.g.,glare,halos)
 Needforadditionalcorrectiveprocedures
 Resourceuseandcosts

62
Supplementary Information 2. Summary of included studies (prospective study,
GUIDE-assisted group)
Study & location Sample size Methods
Cochener(2018)
France
120eyes
(60patients)
ProspectiverandomizedcomparativestudyofbilateralAcrySofIQPanOptixand
FineVisionMicroFtrifocalIOLsversustheTECNISSymfonyEDOFIOL.
Vandekerckhove
(2026)
Switzerland
210eyes
(105patients)
Single-centerprospectiverandomizeddouble-blindtrialcomparingbilateral
Isopure,Eyhance,andVivitypresbyopia-correctingIOLswithmini-monovision
(−0.50D).
McCabe(2022)
USA
435eyes
(218patients)
Prospectivemulticenterrandomizedparallelcontrolled,patient-and
assessor-maskedtrialcomparingbilateralDFT015(Vivity)nondiffractiveEDOF
IOLswithSN60WFmonofocalIOLs.
Turhan(2021)/
Sevik(2022)
Turkey
58eyes
(29patients)
ProspectiverandomizedcomparativestudyofbilateralTECNISZKB00low-add
bifocalIOLsversusTECNISSymfonyEDOFIOLs,bothusingmini-monovision
(−0.50D).
Chang(2023)
USA
272patients Prospectivemulticenterbilateralrandomized,three-way-maskedcomparativetrial
ofTECNISSynergyZFR00VhybridIOLsversusTECNISZCB00monofocal
IOLs.
Zeilinger(2025)
Austria
80eyes
(40patients)
Single-centerrandomizeddouble-maskedcontrolledtrialcomparingbilateral
RayOneEMVadvancedmonofocalIOLswithVivitynondiffractiveEDOFIOLs
usingmini-monovision.
Han(2025)
China
100eyes
(100patients)
Prospectiverandomizedcase-controlstudycomparinganasphericmonofocalIOL
withamultifocalIOLinmonocularcataractsurgery.
Li(2023)
China
99eyes
(99patients)
Prospectiverandomizeddouble-maskedcontrolledtrialcomparingunilateralAT
LISAtoric939M/MPtrifocalIOLswithATLISAtoric909MbifocalIOLs.
Webers(2020)
Netherlands
54eyes
(27patients)
ProspectiverandomizedcontrolledtrialcomparingbilateralTECNISSymfony
EDOFIOLswithmicromonovisionversusbilateralATLISAtri839MPtrifocal
IOLs.
Reinhard(2021)
Germany,Belgium,
211patients Prospectivemulticenterrandomizedthree-armtrialcomparingbilateralATLARA
andTECNISSymfonyEDOFIOLswithCTASPHINAmonofocalIOLs.

63
Portugal,Spain,
France,andItaly
Hida(2024)
Brazil
116eyes
(58patients)
ProspectiveinterventionalrandomizedparallelstudycomparingbilateralTECNIS
SynergyZFR00Vimplantationwithablendedstrategy(EyhanceICB00inthe
dominanteyeandSynergyinthenondominanteye).
Sandoval(2020)
USA
76patients ProspectiveunmaskedrandomizedstudyofbilateraltoricTECNISSymfony
EDOFimplantationtargetingemmetropiainbotheyesversus−0.50D
mini-monovisioninthenondominanteye.
Pradeep(2026)
India
70patients ProspectiverandomizedcomparativestudyofbilateralPanOptixtrifocalversus
VivityEDOFIOLimplantation.
Gil(2022)
Spain
152patients Prospectivedouble-maskedcomparativestudyinwhichsixbilateral
presbyopia-correctingIOLgroupswereblock-randomized1:1:1:1:1:1(SV25T0,
ATLISA809M,ATLISAtri839MP,TECNISZKB00,TECNISZLB00,and
TECNISSymfonyZXR00),withanonrandomizedbilateralTECNISZA9003
monofocalcomparatorgroup.
Messias(2021)
Brazil
66eyes
(33patients)
ProspectiverandomizedstudycomparingbilateralSN6AD1diffractivemultifocal
IOLswithSN60WFasphericmonofocalIOLs.
Labiris(2024)
Greece
90patients Prospectiverandomizedcomparativestudyofpremiummonovision(PanOptixin
thenondominanteyeandVivityinthedominanteye)versusbilateralPanOptixor
bilateralVivityimplantation.
Bala(2022)
Australia,Canada,
Spain,andUK
270patients Prospectivemulticenterrandomizedparallelcontrolled,patient-and
assessor-maskedtrialcomparingbilateralDFT015(Vivity)nondiffractiveEDOF
IOLswithSN60WFmonofocalIOLs.
Skov(2026)
Denmark
180patients Single-centerrandomizedcontrolledpilottrialcomparingfourbilateralstrategies:
partial-range-of-focusnarrowIOLstargetingemmetropia,mini-monovision(−1.25
D),monovision(−2.50D),andpartial-range-of-focusextendedIOLs.
Corbett/Black
(2024)
AustraliaandNew
118patients Prospectivemulticenterrandomizedsubject-andevaluator-maskedtrialcomparing
bilateralTECNISPureSeeZEN00VrefractiveEDOFIOLswithEyhanceICB00
enhancedmonofocalIOLs.

64
Zealand
Pantanelli(2023)
USA
51patients Prospectivesingle-centerdouble-armrandomized,patient-andassessor-masked
trialcomparingbilateralVivitynondiffractiveEDOFIOLswithenVistaneutral
asphericmonofocalIOLstargetedforemmetropia.
Gil(2020)
Spain
116patients Prospectiverandomizeddouble-maskedstudycomparingsixbilateral
presbyopia-correctingIOLs(SV25T0,ATLISA809M,ATLISAtri839MP,
TECNISZKB00,TECNISZLB00,andTECNISSymfony).
Guarro(2022)
Spain
88patients Prospectiverandomizeddouble-blindstudycomparingbilateralVivity,AT
LARA,andTECNISSymfonyEDOFIOLswithSN60WFmonofocalIOLs.
Law(2020)
UK
90patients Prospectiverandomizeddouble-maskedstudycomparingbilateralBi-Flex677MY
multifocalIOLswithBi-Flex677ABmonofocalIOLs.
Chang(2022)
USA
299patients Prospectivemulticenterbilateralrandomized,patient-andevaluator-maskedtrial
comparingTECNISSymfonyZXR00EDOFIOLswithTECNISZCB00
monofocalIOLs.
Palkovits(2026)
Austria
35patients Prospectiverandomizedsingle-centerstudycomparingbilateralAcunexVario
AN6VEDOFIOLswithAcunexAN6monofocalIOLs.

65
Supplementary Information 3. Excluded studies and reasons (prospective study,
GUIDE-assisted group)
Study Reason for exclusion
SaviniG,Schiano-LomorielloD,BalducciN,BarboniP.Visual
performanceofanewextendeddepth-of-focusintraocularlenscompared
toadistance-dominantdiffractivemultifocalintraocularlens. Journal of
Refractive Surgery.2018;34(4):228-235.
Retrospectivecomparative
study.
Escandón-GarcíaS,RibeiroFJ,McAlindenC,QueirósA,
González-MéijomeJM.Through-focusvisionperformanceandlight
disturbancesof3newintraocularlensesforpresbyopiacorrection. Journal
of Ophthalmology.2018;2018:6165493.
Nonrandomizedcaseseries.
MencucciR,FavuzzaE,CaporossiO,SavastanoA,RizzoS.Comparative
analysisofvisualoutcomes,readingskills,contrastsensitivity,andpatient
satisfactionwithtwomodelsoftrifocaldiffractiveintraocularlensesand
anextendedrangeofvisionintraocularlens. Graefe's Archive for Clinical
and Experimental Ophthalmology.2018;256(10):1913-1922.
Nonrandomizedcaseseries.
PedrottiE,CaronesF,AielloF,MastropasquaR,BruniE,BonacciE,et
al.Comparativeanalysisofvisualoutcomeswith4intraocularlenses:
monofocal,multifocal,andextendedrangeofvision. Journal of Cataract
& Refractive Surgery.2018;44(2):156-167.
Participantswerenotrandomly
allocatedtotheIOLgroups.*
FernandesMC,NunomuraCY,MessiasA.Visualperformanceandphotic
disturbanceswithdiffractiveandnondiffractiveEDOFintraocularlenses
usingmini-monovision:randomizedtrial.JournalofCataract&Refractive
Surgery.2024;50(2):153–159.
BothgroupsreceivedEDOF
IOLs.
deMedeirosAL,JonesSaraivaF,IgumaCI,KniggendorfDV,AlvesG,
ChavesMAPD,etal.Comparisonofvisualoutcomesafterbilateral
implantationoftwointraocularlenseswithdistinctdiffractiveoptics.
Clinical Ophthalmology.2019;13:1657-1663.
Nonrandomizedcaseseries.
RodovL,ReitblatO,LevyA,AssiaEI,KleinmannG.Visualoutcomes Retrospectivereview.

66
andpatientsatisfactionfortrifocal,extendeddepthoffocusandmonofocal
intraocularlenses. Journal of Refractive Surgery.2019;35(7):434-440.
WantenJC,BauerNJC,BerendschotTTJM,vandenBiggelaarFJHM,
NuijtsRMMA.Twonovelextendeddepth-of-focusintraocularlenses
targetedformini-monovision:Aprospectiverandomizedcontrolledtrial.
AmericanJournalofOphthalmology.2025;276:286–296.
BothgroupsreceivedEDOF
IOLs.*
SinghB,SharmaS,DadiaS,BhartiN,BhartiS.Comparativeevaluation
ofvisualoutcomesafterbilateralimplantationofadiffractivetrifocal
intraocularlensandanextendeddepthoffocusintraocularlens. Eye &
Contact Lens.2020;46(5):314-318.
Nonrandomizedcomparative
study.
PaikDW,ParkJS,YangCM,LimDH,ChungTY.Comparingthevisual
outcome,visualquality,andsatisfactionamongthreetypesofmulti-focal
intraocularlenses. Scientific Reports.2020;10:14832.
Nonrandomizedcomparative
study.
FarvardinM,JohariM,AttarzadeA,RahatF,FarvardinR,FarvardinZ.
Comparisonbetweenbilateralimplantationofatrifocalintraocularlens
(AlconAcrySofIQPanOptix)andextendeddepthoffocuslens(Tecnis
SymfonyZXR00lens). International Ophthalmology.
2021;41(2):567-573.
Nonrandomizedcomparative
study.
HayashiK,YoshidaM,SasakiH,HirataA.Binocularvisualfunctionof
myopicpseudophakicmonovision.JapaneseJournalofOphthalmology.
2018;62:357–364.
Interventiondidnotmeet
predefinedscope.*
ChaoCC,LinHY,LeeCY,MaiELC,LianIB,ChangCK.Differencein
qualityofvisionoutcomeamongextendeddepthoffocus,bifocal,and
monofocalintraocularlensimplantation. Healthcare.2022;10(6):1000.
Retrospectivecomparative
study.
ZhuM,FanW,ZhangG.Stereopsisandvisualacuity:bilateraltrifocal
versusblendedextendeddepthoffocusanddiffractivebifocalintraocular
lenses. Frontiers in Medicine.2022;9:1042101.
Nonrandomizedcomparative
study.
NagyZZ,Popper-SachettiA,KissHJ.Comparisonofvisualandrefractive
outcomesbetweenhydrophilicandhydrophobictrifocalintraocularlenses
BothIOLsweretrifocallenses.

67
sharingthesameopticaldesign. Journal of Cataract & Refractive Surgery.
2019;45(5):553-561.
DickHB,AngRE,CorbettD,HoffmannP,TetzM,VillarrubiaA,
PalominoC,Castillo-GomezA,TsaiL,ThomasEK,JanakiramanP.
Comparisonof3-monthvisualoutcomesofanewmultifocalintraocular
lensvsatrifocalintraocularlens.JournalofCataract&Refractive
Surgery.2022;48(11):1270–1276.
Cataract-onlypatientsoutcome
datawerenotextractable.*
NagyZZ,DormanP,SzalczerS,KissH.ProspectiveComparisonof
ClinicalOutcomesAfterBilateralImplantationofDiffractiveTrifocal
ExtendedDepth-of-FocusandDiffractiveTrifocalHydrophobic
IntraocularLenses.JournalofRefractiveSurgery.2025;41(3):e102–e113.
Cataract-onlypatientsoutcome
datawerenotextractable.*
VasavadaV,VasavadaSA,ShastriL,NathV,VasavadaAR,SrivastavaS.
Visualoutcomescomparingemmetropiavsmini-monovisionafter
bilateralimplantationofanondiffractiveextendedvisionintraocularlens:
randomizedtrial.JournalofCataract&RefractiveSurgery.
2024;50(8):799–804.
Cataract-onlypatientsoutcome
datawerenotextractable.*
MartínezdeCarneros-LlorenteA,MartínezdeCarnerosA,Martínezde
Carneros-LlorenteP,Jiménez-AlfaroI.Comparisonofvisualqualityand
subjectiveoutcomesamong3trifocalintraocularlensesand1bifocal
intraocularlens. Journal of Cataract & Refractive Surgery.
2019;45(5):587-594.
AllIOLsbelongedtothe
multifocalclass.
AsenaBS.Visualandrefractiveoutcomes,spectacleindependence,and
visualdisturbancesaftercataractorrefractivelensexchangesurgery:
comparisonof2trifocalintraocularlenses. Journal of Cataract &
Refractive Surgery.2019;45(11):1539-1546.
Bothstudygroupsreceived
trifocalIOLs.
WendelsteinJA,VallottonK,ZiörjenA,MüllerM,RiazKM,Pantanelli
SM,LangenbucherA,SeilerTG.ReadingSpeedandVisualAcuityin
PhotopicandMesopicConditionsAfterBilateralImplantationof
DiffractiveMultifocalIntraocularLenses.AmericanJournalof
Bothgroupsreceiveddiffractive
multifocalIOLs.

68
Ophthalmology.2026;281:516–525.
SchojaiM,SchultzT,JerkeC,BöckerJ,DickHB.Visualperformance
comparisonof2extendeddepth-of-focusintraocularlenses.Journalof
Cataract&RefractiveSurgery.2020;46(3):388–393.
Bothgroupsevaluated
EDOF-basedIOLs.
FerreiraTB,RibeiroFJ.Prospectivecomparisonofclinicalperformance
andsubjectiveoutcomesbetweentwodiffractivetrifocalintraocularlenses
inbilateralcataractsurgery. Journal of Refractive Surgery.
2019;35(7):418-425.
Bothstudygroupsreceived
trifocalIOLs.
RibeiroFJ,FerreiraTB.Comparisonofvisualandrefractiveoutcomesof
2trifocalintraocularlenses. Journal of Cataract & Refractive Surgery.
2020;46(5):694-699.
Bothstudygroupsreceived
diffractivetrifocalIOLs.
XunY,WanW,JiangL,HuK.Crossedversusconventional
pseudophakicmonovisionforhighmyopiceyes:aprospective,
randomizedpilotstudy.BMCOphthalmology.2020;20:447.
Enrolledhigh-myopiccataract
patients.
AngRE,PicacheGCS,RiveraMCR,LopezLRL,CruzEM.A
comparativeevaluationofvisual,refractive,andpatient-reportedoutcomes
ofthreeextendeddepthoffocus(EDOF)intraocularlenses. Clinical
Ophthalmology.2020;14:2339-2351.
Retrospectivecohortstudy.
HienertJ,StjepanekK,HirnschallN,RuissM,ZwicklH,FindlO.Visual
performanceoftwodiffractivetrifocalintraocularlenses:arandomized
trial. Journal of Refractive Surgery.2021;37(7):460-465.
Bothstudygroupsreceived
diffractivetrifocalIOLs.
KılıçA,ÖzpınarA,TanrıverdiC.Comparisonofvisualoutcomesoftwo
trifocalIOLs. Journal of Refractive Surgery.2023;39(8):524-530.
Bothstudygroupsreceived
diffractivetrifocalIOLs.
DeRojasJO,SandovalHP,PotvinR,SolomonKD.Comparisonofvisual
andsubjectiveoutcomesbetweentwoEDOFintraocularlenses,with
emphasisonmesopicperformance. Journal of Cataract & Refractive
Surgery.2026;52(6):574-581.
Bothstudygroupsreceived
EDOFIOLs.
Note:The6articlesmarkedwithasteriskswereexcludedafterreviewbyhumanexperts.

69
Supplementary Information 4. GRADE tables (prospective study, GUIDE-assisted group)
(1) Multifocal vs Monofocal
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(lowerfavoursmultifocal)
9(Chang2023;elMaghraby
1992;Steinert1992;Percival
1993;Rossetti1994;
Haaskjold1998;Kamlesh
2001;Leyland2002;Sen
2004)
RCT Serious Serious Notserious Serious 953 RR1.09(0.75to
1.58)
Verylow
Uncorrecteddistancevisualacuityworsethan6/6(lowerfavoursmultifocal)
9(Chang2023;elMaghraby
1992;Steinert1992;Percival
1993;Rossetti1994;
Haaskjold1998;Leyland
2002;Sen2004;Jusufovic
2011)
RCT Serious Serious Notserious Notserious 943 RR1.01(0.89to
1.14)
Low
UncorrectednearvisualacuityworsethanJ3/J4oranequivalentthreshold(lowerfavoursmultifocal)
9(Chang2023;elMaghraby
1992;Percival1993;Rossetti
1994;Haaskjold1998;Javitt
2000;Leyland2002;Jusufovic
2011;Ji2013)
RCT Serious Serious Notserious Notserious 1,043 RR0.18(0.08to
0.41)
Low
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
9(Chang2023;Messias2021;
Law2020;Leyland2002;
Nijkamp2004;Harman2008;
Palmer2008;Rasp2012;Peng
2012)
RCT Serious Notserious Notserious Notserious 1,265 MD0.03(0.01to
0.04)
Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
4(Chang2023;Law2020;
Maxwell2017;Peng2012)
RCT Serious Serious Notserious Serious 866 MD−0.12(−0.29to
0.05)
Verylow
Meancorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
9(Chang2023;Law2020;
Javitt2000;Leyland2002;
RCT Serious Veryserious Notserious Serious 1,667 MD−0.15(−0.34to
0.05)
Verylow

70
Palmer2008;Harman2008;
Rasp2012;Peng2012;
Maxwell2017)
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
9(Chang2023;Messias2021;
Law2020;Leyland2002;
Nijkamp2004;Palmer2008;
Harman2008;Peng2012;
Rasp2012)
RCT Serious Notserious Notserious Notserious 1,265 MD0.02(−0.01to
0.05)
Moderate
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
3(Chang2023;Maxwell
2017;Peng2012)
RCT Serious Serious Notserious Serious 776 MD−0.11(−0.27to
0.05)
Verylow
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
9(Chang2023;Messias2021;
Law2020;Javitt2000;
Leyland2002;Harman2008;
Peng2012;Rasp2012;
Maxwell2017)
RCT Serious Serious Notserious Notserious 1,559 MD−0.25(−0.39to
−0.12)
Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Anyspectacledependence(lowerfavoursmultifocal)
15(Chang2023;Han2025;
Law2020;Gil2022;Steinert
1992;Percival1993;Rossetti
1994;Haaskjold1998;Javitt
2000;Leyland2002;Harman
2008;Cillino2008;Zhao
2010;Peng2012;Maxwell
2017)
RCT Serious Serious Notserious Notserious 1,899 RR0.52(0.39to
0.68)
Low
Contrastsensitivity(higherfavoursmultifocal)
4(Harman2008;Leyland
2002;Rossetti1994;Sen
2004)
RCT Serious Notserious Notserious Serious 288 SMD−0.19(−0.57to
0.19)
Low
Visualfunction(higherfavoursmultifocal)
6(Han2025;Law2020;
Cillino2008;Nijkamp2004;
RCT Serious Serious Notserious Serious 663 SMD0.78(−0.09to
1.65)
Verylow

71
Sen2004;Zhao2010)
Patientsatisfaction(numberofsatisfiedparticipants)(higherfavoursmultifocal)
3(Chang2023;Hida2024;
Law2020)
RCT Serious Serious Notserious Serious 403 RR2.41(0.47to
12.46)
Low
Patientsatisfaction(questionnairescore)(higherfavoursmultifocal)
6(Cillino2008;Nijkamp
2004;Peng2012;Sen2004;
Steinert1992;Zhao2010)
RCT Serious Veryserious Notserious Veryserious 643 SMD0.26(−0.37to
0.89)
Verylow
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(lowerfavoursmultifocal)
12(Chang2023;Han2025;
Hida2024;Gil2022;
Percival1993;Rossetti1994;
Haaskjold1998;Kamlesh
2001;Sen2004;Cillino
2008;Harman2008;
Maxwell2017)
RCT Serious Serious Notserious Serious 1,405 RR1.34(0.98to
1.83)
Verylow
Halos(lowerfavoursmultifocal)
13(Chang2023;Han2025;
Hida2024;Gil2022;Law
2020;Cillino2008;
Haaskjold1998;Kamlesh
2001;Maxwell2017;
Percival1993;Rossetti1994;
Sen2004;Zhao2010)
RCT Serious Serious Notserious Notserious 1,614 RR4.06(2.19to
7.55)
Low
Starbursts(lowerfavoursmultifocal)
2(Chang2023;Han2025) RCT Serious Notserious Notserious Very
serious
362 RR6.40(0.00to
33991.66)
Verylow
Nd:YAGposteriorcapsulotomy(lowerfavoursmultifocal)
1(Law2020) RCT Serious N/A Not
serious*
Very
serious
180 RR2.55(0.68to
9.55)
Verylow
(2) EDOF vs Monofocal
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality

72
Correcteddistancevisualacuityworsethan6/6(lowerfavoursEDOF)
2(Black2024;Chang
2022)
RCT Serious Serious Notserious Veryserious 415 RR0.80(0.00,
5055.39)
Verylow
Correctedintermediatevisualacuitymeetingthestudy-definedthreshold(higherfavoursEDOF)
2(McCabe2022;
Pantanelli2023)
RCT Serious Notserious Notserious Notserious 269 RR2.91(0.43,19.82) Moderate
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
5(Reinhard2021;Bala
2022;Corbett2024;
Black2024;Pantanelli
2023)
RCT Serious Notserious Notserious Notserious 764 MD0.02(−0.01,
0.05)
Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
4(Reinhard2021;Bala
2022;Corbett2024;
Pantanelli2023)
RCT Serious Serious Notserious Serious 644 MD−0.15(−0.28,
−0.02)
Verylow
Meancorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
4(Reinhard2021;Bala
2022;Corbett2024;
Pantanelli2023)
RCT Serious Serious Notserious Notserious 644 MD−0.13(−0.24,
−0.01)
Low
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
6(McCabe2022;
Reinhard2021;Bala
2022;Skov2026;Black
2024;Pantanelli2023)
RCT Serious Notserious Notserious Notserious 893 MD0.03(−0.00,
0.07)
Moderate
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
5(McCabe2022;
Reinhard2021;Bala
2022;Skov2026;
Pantanelli2023)
RCT Serious Serious Notserious Serious 833 MD−0.12(−0.21,
−0.02)
Verylow
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
5(McCabe2022;
Reinhard2021;Bala
2022;Skov2026;
Pantanelli2023)
RCT Serious Serious Notserious Serious 833 MD−0.16(−0.24,
−0.08)
Verylow
Uncorrecteddistancevisualacuityworsethan6/6(lowerfavoursEDOF)
2(Black2024;Chang RCT Serious Notserious Notserious Serious 355 RR1.15(0.32,4.12) Low

73
2022)
UncorrectednearvisualacuityworsethanJ3/J4orequivalent(lowerfavoursEDOF)
1(Chang2022) RCT Serious N/A Notserious Notserious 295 RR0.11(0.05,0.25) Moderate
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
BinocularVisualFunctionquestionnairescore(scaledirectionnotreported)(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 92 MD−0.16(−0.41,
0.09)
Low
Contrastsensitivity(higherfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Notserious 92 MD−0.01(−0.06,
0.04)
Moderate
Meanstereoacuity(arcsec)(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Very
Serious
92 MD29.0(−15.4,
73.4)
VeryLow
Lightdistortionindex(lowerfavoursEDOF)
1(Guarro2022) RCT Serious N/A Notserious* Serious 88 MD9.33(3.81,
14.85)
Low
Patientsatisfaction(higherfavoursEDOF)
2(Skov2026;Black
2024)
RCT Serious Serious Notserious Serious 152 RR1.17(0.09,14.57) Verylow
Spectacledependence,any(lowerfavoursEDOF)
8(McCabe2022;Bala
2022;Skov2026;Black
2024;Pantanelli2023;
Chang2022;Palkovits
2026;Gil2022)
RCT Serious Serious Notserious Serious 985 RR0.70(0.59,0.85) Verylow
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Blurredvision(lowerfavoursEDOF)
3(McCabe2022;Pantanelli
2023;Chang2022)
RCT Serious Notserious Notserious Veryserious 565 RR0.50(0.12,2.06) Verylow
Doublevision(lowerfavoursEDOF)
1(McCabe2022) RCT Serious N/A Notserious Veryserious 219 RR2.13(0.20,
23.17)
Verylow
Glare(lowerfavoursEDOF)
9(McCabe2022;Bala2022; RCT Serious Notserious Notserious Serious 1,133 RR0.93(0.73,1.19) Low

74
Skov2026;Corbett2024;
Pantanelli2023;Guarro
2022;Chang2022;Palkovits
2026;Gil2022)
Halos(lowerfavoursEDOF)
10(McCabe2022;Gil2022;
Bala2022;Skov2026;
Corbett2024;Black2024;
Pantanelli2023;Guarro
2022;Chang2022;Palkovits
2026)
RCT Serious Serious Notserious Notserious 1,192 RR2.08(1.16,3.72) Low
Hazyvision(lowerfavoursEDOF)
2(McCabe2022;Pantanelli
2023)
RCT Serious Notserious Not
serious*
Veryserious 270 RR0.78(0.01,
83.56)
Verylow
Negativedysphotopsia(lowerfavoursEDOF)
1(McCabe2022) RCT Serious N/A Notserious Veryserious 219 RR0.68(0.27,1.69) Verylow
Starbursts(lowerfavoursEDOF)
8(McCabe2022;Bala2022;
Skov2026;Corbett2024;
Black2024;Pantanelli2023;
Chang2022;Palkovits
2026)
RCT Serious Serious Notserious Veryserious 1,055 RR0.97(0.59,1.60) Verylow
(3) Monovsion vs Monofocal
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Serious 137 MD0.08(0.04to0.11) Low
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Serious 137 MD−0.07(−0.11to−0.02) Low
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD−0.22(−0.27to−0.16) Moderate
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Contrastsensitivity(Pelli–RobsonlogCS)(higherfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD−0.01(−0.06to0.04) Moderate

75
Patientsatisfaction(higherfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Veryserious 137 RR1.00(0.79to1.26) Verylow
Spectacledependence(any)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 RR0.72(0.62to0.84) Moderate
Visualfunction(Catquest-7SF)(higherfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD−0.01(−0.26to0.23) Moderate
Adverse events
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Veryserious 137 RR0.98(0.74to1.30) Verylow
Halos(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Serious 137 RR1.25(0.78to2.01) Low
Meananiseikonia,%(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious* 137 MD0.66(0.11to1.22) Moderate
*
Starbursts(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Veryserious 137 RR0.97(0.64to1.49) Verylow
(4) Multifocal vs EDOF
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(lowerfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 118 RR0.90(0.28,2.89) Low
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
2(AkkayaTurhan
2021;Gil2020)
RCT Serious Notserious Notserious Notserious 145 MD0.03(-0.22,0.28) Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
2(AkkayaTurhan
2021;Gil2020)
RCT Serious Notserious Notserious Serious 145 MD0.12(-0.09,0.34) Low
Meancorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
2(AkkayaTurhan
2021;Gil2020)
RCT Serious Veryserious Notserious Veryserious 145 MD-0.02(-1.20,1.15) Verylow
Meanuncorrecteddistancevisualacuity(decimal)(higherfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Notserious 118 MD0.02(-0.05,0.10) Moderate
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
3(Sevik2022; RCT Serious Notserious Notserious Notserious 116 MD-0.03(-0.08,0.03) Moderate

76
Webers2020;
Labiris2024)
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
3(Sevik2022;
Webers2020;
Labiris2024)
RCT Serious Notserious Notserious Notserious 116 MD0.03(-0.04,0.10) Moderate
Meanuncorrectedintermediatevisualacuity(decimal)(higherfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Notserious 118 MD-0.05(-0.11,0.02) Moderate
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
3(Sevik2022;
Webers2020;
Labiris2024)
RCT Serious Veryserious Notserious Serious 116 MD-0.03(-0.27,0.20) Verylow
Meanuncorrectednearvisualacuity(decimal)(higherfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 118 MD0.09(0.03,0.16) Low
Uncorrecteddistancevisualacuityworsethan6/6(lowerfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 147 RR1.19(0.76,1.85) Low
UncorrectednearvisualacuityworsethanJ3/J4orequivalent(lowerfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 118 RR0.34(0.15,0.77) Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Maximumreadingspeed,words/min(higherfavoursmultifocal)
1(Akkaya
Turhan2021)
RCT Serious N/A Notserious Veryserious 29 MD-5.00(-26.87,16.87) Verylow
Readingacuity(logMAR)(lowerfavoursmultifocal)
1(Akkaya
Turhan2021)
RCT Serious N/A Notserious* Notserious 29 MD0.01(-0.04,0.06) Moderate
Meanstereoacuity,arcseconds(lowerfavoursmultifocal)
1(Pradeep2026) RCT Serious N/A Notserious* Serious 70 MD29.14(7.27,51.01) Low
Visualfunction(unspecifiedinstruments)(higherfavoursmultifocal)
3(Sevik2022;
Webers2020;
Labiris2024)
RCT Serious Notserious Notserious Veryserious 116 SMD0.00(-0.80,0.80) Verylow
Patientsatisfaction(score,0–100scale)(higherfavoursmultifocal)
1(Sevik2022) RCT Serious N/A Notserious Veryserious 29 MD-1.71(-10.67,7.25) Verylow
Patientsatisfaction(binary)(higherfavoursmultifocal)
1(Webers2020) RCT Serious N/A Notserious Serious 27 RR0.99(0.80,1.23) Low

77
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(lowerfavoursmultifocal)
2(Webers2020;Gil
2022)
RCT Serious Notserious Notserious Serious 137 RR1.16(0.13,10.63) Low
Halos(lowerfavoursmultifocal)
2(Webers2020;Gil
2022)
RCT Serious Serious Notserious Veryserious 138 RR1.05(0.02,64.58) Verylow
Overallphoticphenomena(lowerfavoursmultifocal)
1(Sevik2022) RCT Serious N/A Notserious Veryserious 29 RR4.69(0.24,89.88) Verylow
(5) Multifocal vs Monovision
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
2(Labiris2024；
Wilkins2013)
RCT Serious Notserious Notserious Notserious 246 MD0.04(-0.15,0.23) Moderate
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
2(Labiris2024；
Wilkins2013)
RCT Serious Notserious Notserious Notserious 241 MD0.06(-0.14,0.26) Moderate
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
2(Labiris2024；
Wilkins2013)
RCT Serious Serious Notserious Notserious 246 MD−0.00(−0.57,0.56) Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Visualfunction(lowerfavoursmultifocal)
1(Labiris2024) RCT Serious N/A Serious Serious 60 MD−3.81(−8.64,1.02) Verylow
Visualfunction–VF-14(higherfavoursmultifocal)
1(Labiris2015) RCT Serious N/A Notserious Notserious 75 MD−1.47(−5.51,2.57) Moderate
Spectacledependence–any(lowerfavoursmultifocal)
2(Wilkins2013;
Labiris2015)
RCT Serious Notserious Notserious Notserious 262 RR0.40(0.06,2.59) Moderate
Contrastsensitivity–Pelli-Robsontest(higherfavoursmultifocal)
2(Wilkins2013;
Labiris2015)
RCT Serious Notserious Notserious Notserious 262 MD−0.03(−0.47,0.41) Moderate
Adverse events

78
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(lowerfavoursmultifocal)
1(Wilkins2013) RCT Serious N/A Notserious Notserious 187 RR1.41(1.14,1.73) Moderate
(6) EDOF vs Monovision
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(lowerfavoursEDOF)
1(Vandekerckhove
2026)
RCT Serious N/A Notserious Serious 105 RR5.22(1.07,25.55) Low
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
2(Vandekerckhove
2026;Zeilinger2025)
RCT Serious Notserious Notserious Serious 185 MD0.04(−0.15,0.23) Low
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
2(Vandekerckhove
2026;Zeilinger2025)
RCT Serious Notserious Notserious Serious 185 MD−0.10(−0.33,
0.12)
Low
Meancorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
2(Vandekerckhove
2026;Zeilinger2025)
RCT Serious Serious Notserious Serious 185 MD−0.09(−0.95,
0.77)
Verylow
Meanstereoacuity(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 131 MD10.39(−34.01,
54.78)
Low
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
5(Vandekerckhove
2026;Zeilinger2025;
Sandoval2020;Labiris
2024;Skov2026)
RCT Serious Notserious Notserious Notserious 452 MD0.03(−0.02,0.08) Moderate
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
5(Vandekerckhove
2026;Zeilinger2025;
Sandoval2020;Labiris
2024;Skov2026)
RCT Serious Notserious Notserious Notserious 452 MD−0.01(−0.06,
0.04)
Moderate
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
5(Vandekerckhove
2026;Zeilinger2025;
Sandoval2020;Labiris
RCT Serious Veryserious Notserious Very
serious
452 MD0.01(−0.17,0.19) Verylow

79
2024;Skov2026)
Uncorrecteddistancevisualacuityworsethan6/6(lowerfavoursEDOF)
1(Vandekerckhove
2026)
RCT Serious N/A Notserious Serious 105 RR1.70(0.92,3.11) Low
UncorrectednearvisualacuityworsethanJ3/J4orequivalent(lowerfavoursEDOF)
1(Vandekerckhove
2026)
RCT Serious N/A Notserious Serious 105 RR0.25(0.08,0.77) Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Visualfunction(VF-14)(higherfavoursEDOF)
1(Labiris2024) RCT Serious N/A Notserious Notserious 60 MD−5.59(−10.20,
−0.98)
Moderate
Patientsatisfaction(higherfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 131 RR0.97(0.76,1.25) Low
Spectacledependence(any)(lowerfavoursEDOF)
2(Vandekerckhove
2026;Skov2026)
RCT Serious Notserious Notserious Serious 312 RR1.07(0.40,2.87) Low
Contrastsensitivity(higherfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Notserious 131 MD0.001(−0.044,
0.045)
Moderate
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Veryserious 131 RR1.08(0.82,1.43) Verylow
Halos(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Veryserious 131 RR0.91(0.57,1.44) Verylow
Starbursts(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 131 RR1.29(0.87,1.90) Low
(7) Trifocal multifocal IOL vs Bifocal multifocal IOL
Visual acuity
Noofstudies Design Riskofbias Inconsistency Indirectness Imprecision Noofparticipants Effectsize(95%CI) Quality
Meancorrecteddistancevisualacuity(lowerfavourstrifocal)
3(Li2023,
Gundersen2016,
Jonker2015)
RCT Serious Notserious Notserious Notserious 149 MD0.00(-0.07,0.08) Moderate

80
Meancorrectedintermediatevisualacuity(lowerfavourstrifocal)
2(Li2023,
Jonker2015)
RCT Serious Notserious Notserious Serious 127 MD-0.03(-0.30,
0.24)
Low
Meancorrectednearvisualacuity(lowerfavourstrifocal)
2(Li2023,
Jonker2015)
RCT Serious Notserious Notserious Notserious 127 MD0.01(-0.26,0.29) Moderate
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavourstrifocal)
3(Li2023,
Gundersen2016,
Jonker2015)
RCT Serious Notserious Notserious Notserious 149 MD-0.01(-0.10,
0.07)
Moderate
Meanuncorrectednearvisualacuity(lowerfavourstrifocal)
2(Li2023,
Jonker2015)
RCT Serious Notserious Notserious Serious 127 MD-0.00(-0.41,
0.41)
Low
Visual function
Noofstudies Design Riskofbias Inconsistency Indirectness Imprecision Noofparticipants Effectsize(95%CI) Quality
Spectacledependence–near(lowerfavourstrifocal)
1(Jonker2015) RCT Serious N/A Notserious Veryserious 28 RR0.65(0.18,2.38) Verylow
Note:The6qualityindirectnessgradingandcorrespondingoverallevidencecertaintylevel
markedwithasterisksweredeterminedbyhumanexperts.

81
Supplementary Information 5. Evidence to recommendations (prospective study,
GUIDE-assisted group)
Relative value of
different outcomes
The committee agreed that the choice of intraocular lens should be assessed using outcomes
that reflect the overall experience of vision rather than any single measure of visual acuity.
Patient-reported visual function, quality of life and satisfaction were considered particularly
important because they integrate the ability to perform everyday activities, dependence on
spectacles and the acceptability of unwanted visual symptoms. The need for additional
treatment, serious ocular complications and the financial consequences for patients and
healthcareserviceswerealsoconsideredimportant.
The committee recognised that the relative importance of these outcomes varies between
stakeholders. Patients may place different values on spectacle independence, night-time
visual quality and expenditure; families and caregivers may value the patient’s functional
independence; clinicians may prioritise predictable outcomes and the avoidance of difficult
postoperative adaptation; and healthcare providers must also consider affordability, equity
andtheconsequencesofadditionalfollow-uportreatment.
Trade-off between
benefits and harms
The committee agreed that none of the evaluated options was consistently superior across all
relevant outcomes. Each option represents a different balance between range of vision,
opticalquality,unwantedvisualphenomenaandpredictabilityofthepostoperativeresult.
Monofocallensesgenerally providepredictable distancevisionandareassociated withfewer
concerns about glare, halos and other optical disturbances. Their principal disadvantage is
that patients are more likely to require spectacles for intermediate and near activities.
Multifocal lenses generally offer the greatest potential for near vision and spectacle
independence. These benefits must be balanced against a greater likelihood of halos,
starburstsorotherunwantedvisualphenomenaand,insomepatients,asmallreductioninthe
clarity of distance vision. They may remain troublesome for people who frequently drive at
night, work in low-contrast environments or have particularly high expectations of optical
quality. EDOF lenses may provide a broader and more continuous range of vision than
monofocal lenses, particularly for intermediate activities, while generally retaining useful
distance vision. However, they do not guarantee spectacle independence for near tasks, and

82
theavailabledirectevidencedoesnotconsistentlydemonstratethattheyproducefewervisual
disturbances than multifocal lenses. Monovision may improve functional intermediate and
near vision without using presbyopia-correcting optics. However, it introduces a deliberate
difference between the two eyes and may adversely affect binocular balance, depth
perception or distance visual quality. Tolerance is individual and may be more predictable in
people who have previously used and accepted monovision. The committee considered that
monovisionshouldbeviewedasarefractivestrategyrequiringcarefulpatientselectionrather
thanasadirectequivalentofaparticularlensdesign.
The head-to-head evidence did not identify a clear overall hierarchy among different
strategies.Similarly,theevidencecomparingtrifocalandbifocallensesdidnotdemonstratea
sufficientlyconsistentoveralladvantagetosupportonedesignforallpatients.Thecommittee
emphasised that the absence of a statistically significant difference should not be interpreted
as evidence that the options are equivalent, particularly where studies were small or
imprecise.Thebalanceofbenefitsandharmsisthereforestronglypreferencesensitive.
Overall, the committee considered that the evidence supports individualized selection and
informed shared decision-making rather than routine preference for a single option. Patients
should understand that improved range of vision and reduced spectacle dependence may be
obtainedatthecostofopticaltrade-offs,andthatnooption canguaranteecomplete spectacle
independenceorfreedomfromunwantedvisualsymptoms.
Consideration of
health benefits and
resource use
The committee noted that the acquisition cost of the lens, the amount reimbursed by a payer
and the amount ultimately paid by the patient are different quantities. Nevertheless, they
illustrate that lenses intended to reduce presbyopia and spectacle dependence commonly
remain substantially more expensive than standard monofocal lenses, and that the additional
costmayfallonthehealthcaresystemortheindividualpatientdependingonthecountry.
InChina,nationalvolume-basedprocurementhassubstantiallyreducedtheacquisitionprices
of artificial lenses. The National Healthcare Security Administration reported an average
reduction of approximately 60% in the 2023 national procurement round. The principal
economic benefit of multifocal and other presbyopia-correcting lenses is the potential
reduction in future spectacle use, together with convenience and possible gains in functional

83
independence.Thesebenefits accrueovertime, whereas theadditionallensorprocedurecost
is generally incurred at the time of surgery. The value of the additional expenditure is
therefore likely to be greater for patients who place a high value on spectacle independence,
have a longer expected duration of benefit and are willing to accept the associated visual
trade-offs.
Published economic models illustrate this uncertainty. A United States patient-perspective
model estimated that bilateral trifocal implantation produced 0.67 additional QALYs at an
incremental lifetime patient cost of US$2,783, while reducing lifetime spectacle expenditure
by US$2,593. However, the results were highly sensitive to the assumed burden of wearing
glasses, patient out-of-pocket costs and postoperative spectacle dependence. A South Korean
model estimated an additional 0.60 QALYs at an incremental patient cost of US$4,274, but
the estimated net benefit decreased substantially when assumptions about spectacle use or
willingness to pay were changed. Both studies were sponsored by the manufacturer of the
evaluated lenses and were based on modelling assumptions, their conclusions should
therefore be interpreted cautiously. Where advanced lenses are predominantly self-funded,
routine reliance on ability to pay may increase inequity in access. Procurement-related price
reductions improve affordability but do not, by themselves, establish that the additional
benefitsjustifyroutineuseforallpatients.
The committee therefore considered that the price premium should be assessed against the
benefits that are important to the individual patient and against local opportunity costs. The
present evidence does not support assuming that a more expensive lens necessarily provides
proportionatelygreateroverallhealthbenefit.
Quality of evidence The committee noted that the certainty of the evidence was predominantly low, with
moderate-certainty evidence available for only selected comparisons and outcomes.
Important limitations included risk of bias, imprecision, small studies and limited direct
comparisons between newer lens designs. Evidence on patient-reported quality of life,
dissatisfaction,seriouscomplicationsandtheneedforadditionaltreatmentwaslesscomplete
thanevidenceonvisualacuityorspectacleuse.
The results may also be influenced by differences in lens generation, surgical technique,

84
refractive targets, patient selection and outcome measurement. Consequently, the evidence is
sufficient to describe the main trade-offs but not to establish a robust overall ranking of all
availableoptions.
Other considerations The committee considered that acceptability would depend heavily on the quality of
preoperative counselling and whether the postoperative result matched the patient’s
expectations. Patients should receive balanced information about the likely range of vision,
possible continued need for spectacles, unwanted visual phenomena, uncertainty in the
evidenceandthecompletepersonalcostofeachoption.
Implementation would require appropriate patient selection, access to reliable biometry,
clinicians experienced with the relevant refractive strategies and systems for monitoring
dissatisfaction, additional procedures and lens exchange. Providers should avoid presenting
premium lenses as inherently superior and should ensure that financial incentives do not
replacepreference-sensitiveshareddecision-making.
Further research should prioritise adequately powered direct comparisons using standardised
patient-reported outcomes, longer follow-up and consistent reporting of visual symptoms,
additionaltreatmentandcosts.

85
Supplementary Information 6. Recommendations (prospective study, GUIDE-assisted
group)
Question: What is the optimal strategy to facilitate simultaneous distance and near vision following cataract surgery?
Recommendations in 2017 NICE guideline
(NG77: Cataracts in adults:management)
Recommendations updated by GUIDE
Do not offer multifocal intraocular lenses for people
havingcataractsurgery.
Offer monovision for use after cataract surgery to people
who have either anisometropia or monovision
preoperativelyandwouldliketoremainwithit.
Consider multifocal intraocular lenses for people who want greater
spectacle independence for distance, intermediate and near vision.
Whendiscussingthisoption:
 ensure the person’s ocular health is suitable for multifocal
intraocularlenses
 explain the potential benefits in uncorrected near and
intermediate vision compared with standard monofocal
intraocularlenses
 discuss the increased risk of visual disturbances (such as
halos,glareandstarbursts)
 takeintoaccounttheperson’svisualneedsanddailyactivities
 considercostimplicationsandtheperson’swillingnesstopay

86
Supplementary Information 7. PICO criteria (prospective study, human-only group)
Generation by human expert
Population Adults(18yearsandolder)undergoingphacoemulsificationcataract
surgeryandintraocularlens(IOL)implantationinoneorbotheyes
Interventions  Non-accommodatingintraocularlensdesignedtosupportboth
nearanddistancevision(e.g.,multifocallenses,
extended-depth-of-focuslensesormonovisioncorrectionstrategy)
 Standardmonofocalintraocularlenses
Comparators Alllistedinterventionscomparedwithoneanother
Outcomes  Distance,intermediate,andnearvisualacuity
 Patientsatisfaction
 Spectacleindependence
 Incidenceofvisualdisturbances
 Qualityoflife
 Resourceuseandcosts

87
Supplementary Information 8. Summary of included studies (prospective study, human-only
group)
Study&location Samplesize Methods
Cochener(2018)
France
120eyes
(60patients)
ComparisonofAcrySofIQPanOptixandFineVision
MicroFtrifocalIOLswiththeTECNISSymfony
EDOFIOL.
Gil(2020)
Spain
232eyes
(116patients)
ComparisonofAcrySofReSTORSV25T0,ATLISA
809M,TECNISZKB00andZLB00bifocalIOLsand
theATLISAtri839MPtrifocalIOLwiththeTECNIS
SymfonyZXR00EDOFIOL.
Law(2020)
UnitedKingdom
180eyes
(90patients)
ComparisonoftheBi-Flex677MYapodized
diffractivemultifocalIOLwiththeBi-Flex677AB
asphericaberration-neutralmonofocalIOL.
Sandoval(2020)
USA
152eyes
(76patients)
ComparisonofbilateralTECNISSymfonytoricEDOF
IOLstargetedforbinocularemmetropiaor
mini-monovision.
Webers(2020)
TheNetherlands
54eyes
(27patients)
ComparisonoftheTECNISSymfony(ZXR00)EDOF
IOLusingmicromonovisionwiththeATLISAtri
839MPtrifocalIOL.
Messias(2021)
Brazil
66eyes
(33patients)
ComparisonoftheAcrySofReSTORSN6AD1
apodizeddiffractivemultifocalIOLwiththeAcrySof
IQSN60WFasphericmonofocalIOL.
Reinhard(2021)
Germany,Belgium,
Portugal,Spain,France,
andItaly
422eyes
(211patients)
ComparisonoftheATLARA829MPandTECNIS
SymfonyEDOFIOLswiththeCTASPHINA409MP
monofocalIOL.
Turhan(2021)/Sevik
(2022)
Turkey
58eyes
(29patients)
ComparisonoftheTECNIS+2.75D(ZKB00)low-add
bifocalIOLwiththeTECNISSymfony(ZXR00)
EDOFIOL,bothusingmini-monovision.

88
Bala(2022)
Australia,Canada,Spain,
andtheUnitedKingdom
540eyes
(270patients)
ComparisonoftheAcrySofIQVivity(DFT015)
non-diffractiveEDOFIOLwiththeAcrySofIQ
SN60WFasphericmonofocalIOL.
Chang(2022)
USA
597eyes
(299patients)
ComparisonofbilateralTECNISSymfony(ZXR00)
diffractiveEDOFIOLswithTECNIS1-piece(ZCB00)
asphericmonofocalIOLs,bothtargetedfor
emmetropia.
Guarro(2022)
Spain
176eyes
(88patients)
ComparisonoftheAcrySofIQVivitynon-diffractive
EDOF,ATLARA829MPandTECNISSymfony
ZXR00diffractiveEDOFIOLswiththeAcrySofIQ
SN60WFmonofocalIOL.
McCabe(2022)
USA
435eyes
(218patients)
ComparisonoftheAcrySofIQVivity(DFT015)
non-diffractiveEDOFIOLwiththeAcrySofIQ
SN60WFasphericmonofocalIOL.
Chang(2023)
USA
544eyes
(272patients)
ComparisonoftheTECNISSynergy(ZFR00V)hybrid
multifocal-EDOFIOLwiththeTECNISZCB00
monofocalIOL.
Li(2023)
China
99eyes
(99patients)
ComparisonoftheATLISAtritoric939M/MP
trifocalIOLwiththeATLISAtoric909Mbifocal
IOL.
Pantanelli(2023)
USA
102eyes
(51patients)
ComparisonoftheAcrySofVivity(DFT015)
non-diffractiveEDOFIOLwiththeenVista(MX60E)
neutralasphericmonofocalIOL,bothtargetedfor
emmetropia.
Corbett/Black(2024)
AustraliaandNewZealand
235eyes
(118patients)
ComparisonoftheTECNISPureSee(ZEN00V)fully
refractiveEDOFIOLwiththeTECNISEyhance
(ICB00)enhancedmonofocalIOL.
Hida(2024)
Brazil
116eyes
(58patients)
ComparisonofbilateralTECNISSynergy(ZFR00V)
hybridmultifocal-EDOFIOLswithblendedTECNIS

89
Eyhance(ICB00)enhancedmonofocalandTECNIS
Synergyimplantation.
Labiris(2024)
Greece
180eyes
(90patients)
ComparisonofmixedAcrySofIQPanOptixtrifocal
andAcrySofIQVivitynon-diffractiveEDOF
implantationwithbilateralPanOptixorbilateralVivity
implantation.
Zeilinger(2025)
Austria
80eyes
(40patients)
ComparisonoftheRayOneEMV(RAO200E)
advancedmonofocalIOLwiththeAcrySofIQVivity
(DFT015)non-diffractiveEDOFIOL,bothusing
mini-monovision.
Palkovits(2026)
Austria
70eyes
(35patients)
ComparisonoftheAcunexVarioAN6Vrefractive
EDOFIOLwiththeAcunexAN6monofocalIOL,
bothtargetedat-0.25D.
Pradeep(2026)
India
140eyes
(70patients)
ComparisonofbilateralAcrySofIQPanOptixtrifocal
IOLswithbilateralAcrySofIQVivitynon-diffractive
EDOFIOLs.
Skov(2026)
Denmark
360eyes
(180patients)
Comparisonofemmetropia,mini-monovision,and
monovisionusingbilateralAcrySofACU0T0or
TECNISGCB00/ZCB00monofocalIOLswith
bilateralAcrySofIQVivitynon-diffractiveEDOF
IOLs.
Vandekerckhove(2026)
Switzerland
210eyes
(105patients)
ComparisonofIsopureandTECNISEyhance
enhancedmonofocalIOLswiththeAcrySofIQVivity
EDOFIOLusingmini-monovision.

90
Supplementary Information 9. Excluded studies and reasons (prospective study, human-only
group)
Study Reason for exclusion
HayashiK,YoshidaM,SasakiH,HirataA.Binocularvisualfunction
of myopic pseudophakic monovision. Japanese Journal of
Ophthalmology.2018;62:357–364.
Intervention did not meet the
prespecified pseudophakic monovision
definition.
Schojai M, Schultz T, Jerke C, Böcker J, Dick HB. Visual
performance comparison of 2 extended depth-of-focus intraocular
lenses. Journal of Cataract & Refractive Surgery.
2020;46(3):388–393.
Both groups evaluated EDOF-based
IOLs.
Xun Y, Wan W, Jiang L, Hu K. Crossed versus conventional
pseudophakic monovision for high myopic eyes: a prospective,
randomizedpilotstudy.BMCOphthalmology.2020;20:447.
Included patients with high-myopic
cataract.
Dick HB, Ang RE, Corbett D, Hoffmann P, Tetz M, Villarrubia A,
Palomino C, Castillo-Gomez A, Tsai L, Thomas EK, Janakiraman P.
Comparison of 3-month visual outcomes of a new multifocal
intraocular lens vs a trifocal intraocular lens. Journal of Cataract &
RefractiveSurgery.2022;48(11):1270–1276.
Cataract-only outcome data were not
separatelyextractable.
Gil MÁ, Varón C, Cardona G, Buil JA. Far and Near Contrast
Sensitivity and Quality of Vision with Six Presbyopia Correcting
IntraocularLenses.JournalofClinicalMedicine.2022;11(14):4150.
Participantswerenotrandomlyallocated.
Fernandes MC, Nunomura CY, Messias A. Visual performance and
photic disturbances with diffractive and nondiffractive EDOF
intraocular lenses using mini-monovision: randomized trial. Journal
ofCataract&RefractiveSurgery.2024;50(2):153–159.
BothgroupsreceivedEDOFIOLs.
Vasavada V, Vasavada SA, Shastri L, Nath V, Vasavada AR,
Srivastava S. Visual outcomes comparing emmetropia vs
mini-monovision after bilateral implantation of a nondiffractive
extended vision intraocular lens: randomized trial. Journal of
Cataract-only outcome data were not
separatelyextractable.

91
Cataract&RefractiveSurgery.2024;50(8):799–804.
Han D, Ma X, Gao J, Xu Z, Liu F. Comparison of clinical effects of
aspherical monofocal and Tecnis ZMB00 multifocal intraocular
lenses in patients with age-related cataract. Journal of the Pakistan
MedicalAssociation.2025;75(8):1229–1234.
Intervention could not be reliably
classified:the titleidentifiestheTECNIS
ZMB00, whereas the Methods report the
multifocal IOL as model 52501TW
manufacturedbyOphtec.
Nagy ZZ, Dorman P, Szalczer S, Kiss H. Prospective Comparison of
Clinical Outcomes After Bilateral Implantation of Diffractive
Trifocal Extended Depth-of-Focus and Diffractive Trifocal
Hydrophobic Intraocular Lenses. Journal of Refractive Surgery.
2025;41(2):e102–e113.
Cataract-only outcome data were not
separatelyextractable.
Wanten JC, Bauer NJC, Berendschot TTJM, van den Biggelaar
FJHM, Nuijts RMMA. Two novel extended depth-of-focus
intraocular lenses targeted for mini-monovision: A prospective
randomized controlled trial. American Journal of Ophthalmology.
2025;276:286–296.
BothgroupsreceivedEDOFIOLs.
Wendelstein JA, Vallotton K, Ziörjen A, Müller M, Riaz KM,
Pantanelli SM, Langenbucher A, Seiler TG. Reading Speed and
Visual Acuity in Photopic and Mesopic Conditions After Bilateral
Implantation of Diffractive Multifocal Intraocular Lenses. American
JournalofOphthalmology.2026;281:516–525.
Both groups received diffractive
multifocalIOLs.

92
Supplementary Information 10. GRADE tables (prospective study, human-only group)
(1) Multifocal vs Monofocal
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(RR<1favoursmultifocal)
9(elMaghraby1992;
Steinert1992;Percival
1993;Rossetti1994;
Haaskjold1998;Kamlesh
2001;Leyland2002;Sen
2004;Chang2023)
RCT Serious Serious Notserious Serious 953 RR1.09(0.75to1.58) Verylow
Uncorrecteddistancevisualacuityworsethan6/6(RR<1favoursmultifocal)
9(elMaghraby1992;
Steinert1992;Percival
1993;Rossetti1994;
Haaskjold1998;Leyland
2002;Sen2004;Jusufovic
2011;Chang2023)
RCT Serious Serious Notserious Notserious 943 RR1.01(0.89to1.14) Low
UncorrectednearvisualacuityworsethanJ3/J4oranequivalentthreshold(RR<1favoursmultifocal)
9(elMaghraby1992;
Percival1993;Rossetti
1994;Haaskjold1998;
Javitt2000;Leyland2002;
Jusufovic2011;Ji2013;
Chang2023)
RCT Serious Serious Notserious Notserious 1,043 RR0.18(0.08to0.41) Low
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
8(Leyland2002;Nijkamp
2004;Harman2008;
Palmer2008;Rasp2012;
Peng2012;Law2020;
Messias2021)
RCT Serious Notserious Notserious Notserious 1,062 MD0.03(0.01to0.05) Moderate
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
9(Leyland2002;Nijkamp
2004;Palmer2008;
Harman2008;Peng2012;
Rasp2012;Law2020;
Messias2021;Chang2023)
RCT Serious Notserious Notserious Notserious 1,265 MD0.02(−0.01to
0.05)
Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
4(Peng2012;Maxwell
2017;Law2020;Chang
2023)
RCT Serious Serious Notserious Serious 866 MD−0.12(−0.29to
0.05)
Verylow
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
3(Peng2012;Maxwell RCT Serious Serious Notserious Serious 776 MD−0.11(−0.27to Verylow

93
2017;Chang2023) 0.05)
Meancorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
9(Javitt2000;Leyland
2002;Palmer2008;
Harman2008;Rasp2012;
Peng2012;Maxwell2017;
Law2020;Chang2023)
RCT Serious Serious Notserious Notserious 1,667 MD−0.15(−0.34to
0.05)
Low
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
9(Javitt2000;Leyland
2002;Harman2008;Peng
2012;Rasp2012;Maxwell
2017;Law2020;Messias
2021;Chang2023)
RCT Serious Serious Notserious Notserious 1,559 MD−0.25(−0.39to
−0.12)
Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Contrastsensitivity(higherfavoursmultifocal)
4(Rossetti1994;Leyland
2002;Sen2004;Harman
2008)
RCT Serious Notserious Notserious Serious 288 SMD−0.19(−0.57to
0.19)
Low
Visualfunction(higherfavoursmultifocal)
5(Nijkamp2004;Sen
2004;Cillino2008;Zhao
2010;Law2020)
RCT Serious Serious Notserious Serious 563 SMD0.79(−0.36to
1.94)
Verylow
Spectacledependence(any)(RR<1favoursmultifocal)
13(Steinert1992;
Percival1993;Rossetti
1994;Haaskjold1998;
Javitt2000;Leyland
2002;Harman2008;
Cillino2008;Zhao2010;
Peng2012;Maxwell
2017;Law2020;Chang
2023)
RCT Serious Serious Notserious Notserious 1,647 RR0.54(0.40to0.74) Low
Patientsatisfaction(numberofsatisfiedparticipants)(RR>1favoursmultifocal)
3(Law2020;Chang
2023;Hida2024)
RCT Serious Serious Notserious Serious 403 RR2.41(0.47to12.46) Verylow
Patientsatisfaction(questionnairescore)(higherfavorsmultifocal)
6(Steinert1992;
Nijkamp2004;Sen2004;
RCT Serious Veryserious Notserious Veryserious 643 SMD0.26(−0.37to
0.89)
Verylow

94
Cillino2008;Zhao2010;
Peng2012)
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(RR<1favoursmultifocal)
12(Percival1993;Rossetti
1994;Haaskjold1998;
Kamlesh2001;Sen2004;
Cillino2008;Harman2008;
Maxwell2017;Chang2023;
Hida2024)
RCT Serious Serious Notserious Serious 1,153 RR1.34(1.06to1.83) Verylow
Halos(RR<1favoursmultifocal)
11(Percival1993;Rossetti
1994;Haaskjold1998;
Kamlesh2001;Sen2004;
Cillino2008;Zhao2010;
Maxwell2017;Law2020;
Chang2023;Hida2024)
RCT Serious Serious Notserious Notserious 1,362 RR3.70(1.89to7.23) Low
Nd:YAGposteriorcapsulotomy(RR<1favoursmultifocal)
1(Law2020) RCT Serious N/A Notserious Very
serious
180 RR2.55(0.68to9.55) Verylow
(2) EDOF vs Monofocal
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(RR<1favoursEDOF)
2(Chang2022;
Black2024)
RCT Serious Serious Notserious Very
serious
415 RR0.80(0.21,3.08) Verylow
Uncorrecteddistancevisualacuityworsethan6/6(RR<1favoursEDOF)
2(Chang2022;
Black2024)
RCT Serious Notserious Notserious Serious 355 RR1.15(0.94,1.40) Low
UncorrectednearvisualacuityworsethanJ3/J4orequivalent(RR<1favoursEDOF)
1(Chang2022) RCT Serious N/A Notserious Notserious 295 RR0.11(0.05,0.25) Moderate
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
5(Reinhard2021;
Bala2022;
Pantanelli2023;
Corbett2024;Black
2024)
RCT Serious Notserious Notserious Notserious 764 MD0.02(−0.01,0.05) Moderate
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)

95
6(Reinhard2021;
McCabe2022;Bala
2022;Pantanelli
2023;Black2024;
Skov2026)
RCT Serious Notserious Notserious Notserious 893 MD0.03(−0.00,0.07) Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
4(Reinhard2021;
Bala2022;
Pantanelli2023;
Corbett2024)
RCT Serious Serious Notserious Notserious 644 MD−0.15(−0.28,−0.02) Low
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
5(Reinhard2021;
McCabe2022;Bala
2022;Pantanelli
2023;Skov2026)
RCT Serious Serious Notserious Serious 833 MD−0.12(−0.21,−0.02) Verylow
Meancorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
4(Reinhard2021;
Bala2022;
Pantanelli2023;
Corbett2024)
RCT Serious Serious Notserious Serious 644 MD−0.13(−0.24,−0.01) Verylow
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
5(Reinhard2021;
McCabe2022;Bala
2022;Pantanelli
2023;Skov2026)
RCT Serious Serious Notserious Serious 833 MD−0.16(−0.24,−0.08) Verylow
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Contrastsensitivity(higherfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Notserious 92 MD−0.01(−0.06,0.04) Moderate
Visualfunctionquestionnairescore(scaledirectionnotreported)(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 92 MD−0.16(−0.41,0.09) Low
Spectacledependence(any)(RR<1favoursEDOF)
7(McCabe2022;
Bala2022;Chang
2022;Pantanelli
2023;Black2024;
Skov2026;
Palkovits2026)
RCT Serious Serious Notserious Serious 833 RR0.72(0.60,0.88) Verylow
Patientsatisfaction(RR>1favoursEDOF)
2(Black2024;
Skov2026)
RCT Serious Serious Notserious Serious 152 RR1.17(0.80,1.73) Verylow

96
Meanstereoacuity(arcsec)(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Very
Serious
92 MD29.0(−15.4,73.4) VeryLow
Lightdistortionindex(lowerfavoursEDOF)
1(Guarro2022) RCT Serious N/A Notserious Serious 88 MD9.33(3.81,14.85) Low
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(RR<1favoursEDOF)
8(McCabe2022;
Bala2022;Guarro
2022;Chang2022;
Pantanelli2023;
Corbett2024;Skov
2026;Palkovits2026)
RCT Serious Notserious Notserious Serious 981 RR1.00(0.78,1.28) Low
Halos(RR<1favoursEDOF)
9(McCabe2022;
Bala2022;Guarro
2022;Chang2022;
Pantanelli2023;
Corbett2024;Black
2024;Skov2026;
Palkovits2026)
RCT Serious Serious Notserious Notserious 1,040 RR1.51(1.03,2.20) Low
Blurredvision(RR<1favoursEDOF)
3(McCabe2022;
Chang2022;
Pantanelli2023)
RCT Serious Notserious Notserious Veryserious 565 RR0.50(0.12,2.06) Verylow
Doublevision(RR<1favoursEDOF)
1(McCabe2022) RCT Serious N/A Notserious Veryserious 219 RR2.13(0.20,23.17) Verylow
Hazyvision(RR<1favoursEDOF)
2(McCabe2022;
Pantanelli2023)
RCT Serious Notserious Notserious Veryserious 270 RR0.78(0.38,1.60) Verylow
Negativedysphotopsia(RR<1favoursEDOF)
1(McCabe2022) RCT Serious N/A Notserious Veryserious 219 RR0.68(0.27,1.69) Verylow
Starbursts(RR<1favoursEDOF)
8(McCabe2022;
Bala2022;Chang
2022;Pantanelli
2023;Corbett2024;
Black2024;Skov
2026;Palkovits2026)
RCT Serious Serious Notserious Veryserious 1,055 RR0.97(0.59,1.60) Verylow
(3) Monovsion vs Monofocal
Visual acuity

97
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Serious 137 MD0.08(0.04to0.11) Low
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Serious 137 MD−0.07(−0.11to−0.02) Low
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD−0.22(−0.27to−0.16) Moderate
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Contrastsensitivity(Pelli–RobsonlogCS)(higherfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD−0.01(−0.06to0.04) Moderate
Visualfunction(Catquest-7SF)(higherfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD−0.01(−0.26to0.23) Moderate
Spectacledependence(any)(RR<1favoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 RR0.72(0.62to0.84) Moderate
Patientsatisfaction(RR>1favoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Veryserious 137 RR1.00(0.79to1.26) Verylow
Adverse events
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(RR<1favoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Veryserious 137 RR0.98(0.74to1.30) Verylow
Halos(RR<1favoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Serious 137 RR1.25(0.78to2.01) Low
Meananiseikonia(lowerfavoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Notserious 137 MD0.66(0.11to1.22) Moderate
Starbursts(RR<1favoursmonovision)
1(Skov2026) RCT Serious N/A Notserious Veryserious 137 RR0.97(0.64to1.49) Verylow
(4) Multifocal vs EDOF
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(RR<1favoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 118 RR0.90(0.28,2.89) Low
Uncorrecteddistancevisualacuityworsethan6/6(RR<1favoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 147 RR1.19(0.76,1.85) Low
UncorrectednearvisualacuityworsethanJ3/J4orequivalent(RR<1favoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 118 RR0.34(0.15,0.77) Low
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
2(Gil2020;Akkaya
Turhan2021)
RCT Serious Notserious Notserious Notserious 145 MD0.03(-0.01,0.07) Moderate

98
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
3(Webers2020;
Sevik2022;Labiris
2024)
RCT Serious Notserious Notserious Notserious 116 MD-0.03(-0.08,0.03) Moderate
Meanuncorrecteddistancevisualacuity(decimal)(higherfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Notserious 118 MD0.02(-0.05,0.10) Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
2(Gil2020;Akkaya
Turhan2021)
RCT Serious Notserious Notserious Notserious 145 MD0.12(0.09,0.16) Moderate
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
3(Webers2020;
Sevik2022;Labiris
2024)
RCT Serious Notserious Notserious Notserious 116 MD0.03(-0.04,0.10) Moderate
Meanuncorrectedintermediatevisualacuity(decimal)(higherfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Notserious 118 MD-0.05(-0.11,0.02) Moderate
Meancorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
2(Gil2020;Akkaya
Turhan2021)
RCT Serious Veryserious Notserious Veryserious 145 MD-0.02(-0.20,0.16) Verylow
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
3(Webers2020;
Sevik2022;Labiris
2024)
RCT Serious Veryserious Notserious Serious 116 MD-0.03(-0.27,0.20) Verylow
Meanuncorrectednearvisualacuity(decimal)(higherfavoursmultifocal)
1(Cochener2018) RCT Serious N/A Notserious Serious 118 MD0.09(0.03,0.16) Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Visualfunction(unspecifiedinstruments)(higherfavoursmultifocal)
3(Webers2020;
Sevik2022;Labiris
2024)
RCT Serious Notserious Notserious Veryserious 116 SMD0.00(-0.80,0.80) Verylow
Patientsatisfaction(score,0–100scale)(higherfavoursmultifocal)
1(Sevik2022) RCT Serious N/A Notserious Veryserious 29 MD-1.71(-10.67,7.25) Verylow
Patientsatisfaction(binary)(RR>1favoursmultifocal)
1(Webers2020) RCT Serious N/A Notserious Serious 27 RR0.99(0.80,1.23) Low
Maximumreadingspeed(words/min)(higherfavoursmultifocal)
1(AkkayaTurhan
2021)
RCT Serious N/A Notserious Veryserious 29 MD-5.00(-26.87,16.87) Verylow
Readingacuity(logMAR)(lowerfavoursmultifocal)
1(AkkayaTurhan
2021)
RCT Serious N/A Notserious Notserious 29 MD0.01(-0.04,0.06) Moderate
Meanstereoacuity,arcseconds(lowerfavoursmultifocal)
1(Pradeep2026) RCT Serious N/A Notserious Serious 70 MD29.14(7.27,51.01) Low
Adverse outcomes

99
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(RR<1favoursmultifocal)
1(Webers2020) RCT Serious Notserious Notserious Veryserious 27 RR1.08(0.07–15.51) Verylow
Halos(RR<1favoursmultifocal)
1(Webers2020) RCT Serious N/A Notserious Serious 27 RR1.48(0.89,2.46) Low
Overallphoticphenomena(RR<1favoursmultifocal)
1(Sevik2022) RCT Serious N/A Notserious Veryserious 29 RR4.69(0.24,89.88) Verylow
(5) Multifocal vs Monovision
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursmultifocal)
2(Wilkins2013;
Labiris2024)
RCT Serious Notserious Notserious Notserious 246 MD0.04(0.01,0.07) Moderate
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursmultifocal)
2(Wilkins2013;
Labiris2024)
RCT Serious Notserious Notserious Notserious 241 MD0.06(0.03,0.09) Moderate
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursmultifocal)
2(Wilkins2013;
Labiris2024)
RCT Serious Serious Notserious Notserious 246 MD−0.00(−0.09,0.08) Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Contrastsensitivity(Pelli-Robsontest)(higherfavoursmultifocal)
2(Wilkins2013;
Labiris2015)
RCT Serious Notserious Notserious Notserious 262 MD−0.03(−0.10,0.04) Moderate
Visualfunction(lowerfavoursmultifocal)
1(Labiris2024) RCT Serious N/A Serious Serious 60 MD−3.81(−8.64,1.02) Verylow
Visualfunction(VF-14)(higherfavoursmultifocal)
1(Labiris2015) RCT Serious N/A Notserious Notserious 75 MD−1.47(−5.51,2.57) Moderate
Spectacledependence(any)(RR<1favoursmultifocal)
2(Wilkins2013;
Labiris2015)
RCT Serious Notserious Notserious Notserious 262 RR0.40(0.30,0.53) Moderate
Adverse events
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(RR<1favoursmultifocal)
1(Wilkins2013) RCT Serious N/A Notserious Notserious 187 RR1.41(1.14,1.73) Moderate
(6) EDOF vs Monovision
Visual acuity
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Correcteddistancevisualacuityworsethan6/6(RR<1favoursEDOF)

100
1(Vandekerckhove
2026)
RCT Serious N/A Notserious Serious 105 RR5.22(1.07,25.55) Low
Uncorrecteddistancevisualacuityworsethan6/6(RR<1favoursEDOF)
1(Vandekerckhove
2026)
RCT Serious N/A Notserious Serious 105 RR1.70(0.92,3.11) Low
UncorrectednearvisualacuityworsethanJ3/J4orequivalent(RR<1favoursEDOF)
1(Vandekerckhove
2026)
RCT Serious N/A Notserious Serious 105 RR0.25(0.08,0.77) Low
Meancorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
2(Zeilinger2025;
Vandekerckhove
2026)
RCT Serious Notserious Notserious Notserious 185 MD0.04(0.01,0.07) Moderate
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavoursEDOF)
5(Sandoval2020;
Labiris2024;
Zeilinger2025;
Vandekerckhove
2026;Skov2026)
RCT Serious Notserious Notserious Notserious 452 MD0.03(−0.02,0.08) Moderate
Meancorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
2(Zeilinger2025;
Vandekerckhove
2026)
RCT Serious Notserious Notserious Serious 185 MD−0.10(−0.14,−0.07) Low
Meanuncorrectedintermediatevisualacuity(logMAR)(lowerfavoursEDOF)
5(Sandoval2020;
Labiris2024;
Zeilinger2025;
Vandekerckhove
2026;Skov2026)
RCT Serious Notserious Notserious Notserious 452 MD−0.01(−0.06,0.04) Moderate
Meancorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
2(Zeilinger2025;
Vandekerckhove
2026)
RCT Serious Serious Notserious Serious 185 MD−0.09(−0.22,0.04) Verylow
Meanuncorrectednearvisualacuity(logMAR)(lowerfavoursEDOF)
5(Sandoval2020;
Labiris2024;
Zeilinger2025;
Vandekerckhove
2026;Skov2026)
RCT Serious Veryserious Notserious Very
serious
452 MD0.01(−0.17,0.19) Verylow
Meanstereoacuity(arcsec)(lowerfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 131 MD10.39(−34.01,
54.78)
Low
Visual function
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality

101
Contrastsensitivity(higherfavoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Notserious 131 MD0.001(−0.044,
0.045)
Moderate
Visualfunction(VF-14)(higherfavoursEDOF)
1(Labiris2024) RCT Serious N/A Notserious Notserious 60 MD−5.59(−10.20,
−0.98)
Moderate
Spectacledependence(any)(RR<1favoursEDOF)
2(Vandekerckhove
2026;Skov2026)
RCT Serious Notserious Notserious Serious 312 RR1.07(0.92,1.24) Low
Patientsatisfaction(RR>1favoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Very
serious
131 RR0.97(0.76,1.25) Verylow
Adverse outcomes
No.ofstudies Design Riskofbias Inconsistency Indirectness Imprecision No.ofparticipants Effectsize(95%CI) Quality
Glare(RR<1favoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Veryserious 131 RR1.08(0.82,1.43) Verylow
Halos(RR<1favoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Veryserious 131 RR0.91(0.57,1.44) Verylow
Starbursts(RR<1favoursEDOF)
1(Skov2026) RCT Serious N/A Notserious Serious 131 RR1.29(0.87,1.90) Low
(7) Trifocal multifocal IOL vs Bifocal multifocal IOL
Visual acuity
Noofstudies Design Riskofbias Inconsistency Indirectness Imprecision Noofparticipants Effectsize(95%CI) Quality
Meancorrecteddistancevisualacuity(lowerfavourstrifocal)
3(Jonker2015,
Gundersen2016,
Li2023)
RCT Serious Notserious Notserious Notserious 149 MD0.00(-0.07,0.08) Moderate
Meanuncorrecteddistancevisualacuity(logMAR)(lowerfavourstrifocal)
3(Jonker2015,
Gundersen2016,
Li2023)
RCT Serious Notserious Notserious Notserious 149 MD-0.01(-0.10,0.07) Moderate
Meancorrectedintermediatevisualacuity(lowerfavourstrifocal)
2(Jonker2015,Li
2023)
RCT Serious Notserious Notserious Notserious 127 MD-0.03(-0.07,0.01) Moderate
Meancorrectednearvisualacuity(lowerfavourstrifocal)
2(Jonker2015,Li
2023)
RCT Serious Notserious Notserious Notserious 127 MD0.01(-0.03,0.06) Moderate
Meanuncorrectednearvisualacuity(lowerfavourstrifocal)
2(Jonker2015,Li
2023)
RCT Serious Notserious Notserious Notserious 127 MD0.00(-0.06,0.07) Moderate
Visual function

102
Noofstudies Design Riskofbias Inconsistency Indirectness Imprecision Noofparticipants Effectsize(95%CI) Quality
Spectacledependence(near)(RR<1favourstrifocal)
1(Jonker2015) RCT Serious N/A Notserious Veryserious 28 RR0.65(0.18,2.38) Verylow

103
Supplementary Information 11. Evidence to recommendations (prospective study,
human-only group)
Relative value of
different outcomes
The guideline development group considered distance vision to be an essential safety and
functional outcome. However, the value of visual correcting strategies is determined by
whether they provide meaningful improvements in unaided intermediate or near vision,daily
visual functioning and spectacle independence without imposing unacceptable optical
disturbances. Patient satisfaction, health-related quality of life, ability to perform
occupational tasks, and the effects of optical disturbances on night-time activities were
therefore considered as important as differences in visual-acuity measurements. Clinical
measurementsshouldbeinterpretedinrelationtotheirperceptibleeffectoneverydaylife.
Trade-off between
benefits and harms
The committee agreed that no IOL strategy was consistently preferable for all patients. For
distantvision,therewasevidencethatmonofocallensesprovidedgreaterdistantvisualacuity
and were associated with fewer photic phenomena, maybe because optical performance is
concentrated at a single focal point. However, patients usually required spectacles for near
tasks and sometimes for intermediate activities. Other strategies could also provide good
distance vision and spectacles might still be required for demanding tasks such as night
driving.
For intermediate and near vision, multifocal, especially trifocal lenses generally offered the
widest functional range and the greatest reduction in spectacle dependence. EDOF lenses
offer a range of vision from distance to intermediate, making them suitable for patients who
frequently work on computers. However, they did not reliably provide spectacle
independenceforsmallprintorprolongednearwork.
Improvements in visual range were accompanied by potential reductions in optical quality.
Designs that generated multiple focal ranges could cause halos, glare, starbursts or reduced
contrast sensitivity. These effects might be particularly troublesome for people who drive
frequently atnight orwork inlow illumination.Theevidence didnot support the assumption
that all EDOF lenses produce fewer visual disturbances than multifocal lenses, performance
variedbetweenindividuallensplatforms.
For binocular function, monovision presented a distinct trade-off. Greater anisometropia

104
could improve nearvisionbutimpair binocularcomfort,stereopsis ordistancevisualquality.
Previous successful contact-lens monovision might indicate likely tolerance, caution was
warranted when precise depth perception was important for patients occupational or
recreationalrequirement.
Patient satisfaction depends on whether the postoperative visual profile matched individual
priorities. Some patients might accept halos or reduced contrast in exchange for greater
spectacleindependenceandothersmightprioritizeopticalqualityandreliablenightvision.
The committee did not interpret non-significant findings in small, heterogeneous studies as
evidence of equivalence. Differences in lens generation, refractive targets, follow-up and
outcome measurement prevented a consistent hierarchy among strategies. Lens selection
should therefore be individualized through shared decision-making, addressing the distances
at which unaided vision is most important, night-driving and occupational requirements,
willingness to use spectacles and tolerance of unwanted visual phenomena. Patients should
understand that no current strategy guarantees spectacle independence, optimal vision at
everydistanceorcompletefreedomfromvisualsymptoms.
Consideration of
health benefits and
resource use
The committee agreed that the economic consequences of IOL selection have changed
substantially as procurement systems and the range of available products have developed.
Acquisitionprice,reimbursementbythehealthcaresystemandtheamountultimatelypaidby
anindividualpatientaredifferentquantitiesandshouldnotbeconsideredinterchangeable.
Historically, IOLs with special optical designs were associated with a substantial price
premium over standard monofocal lenses. However, that the absolute price difference has
narrowed in many settings as more domestic and international products have entered the
market and centralized procurement has reduced acquisition prices. In China, the national
volume-based procurement programme for intraocular lenses introduced substantial price
reductions across the category. The National Healthcare Security Administration reported an
average reduction of approximately 60% following the 2023 national centralized
procurement round for intraocular lenses and related high-value medical consumables. The
additional acquisition cost associated with a multifocal, EDOF or other advanced-function
lensmaythereforebeconsiderablysmallerthanpervious.

105
Pervious studies suggest that presbyopia-correcting lenses may provide additional QALYs
and reduce lifetime spectacle expenditure in selected patients. However, these findings are
sensitive to assumptions about postoperative spectacle dependence, lens price premiums and
willingness-to-pay thresholds, and some studies were manufacturer sponsored. Their
applicability to contemporary Chinese practice should therefore be reassessed using current
localprices,reimbursementarrangementsandpatientout-of-pocketcosts.
The committee also noted that affordability may affect equitable access to advanced optical
functions.Althoughcentralizedprocurementandmarketcompetitionmayreducethisbarrier,
higher price should not be interpreted as evidence of greater clinical benefit. Local decisions
should instead consider whether the additional patient-important benefits justify the
incremental cost, with resource-use estimates updated as procurement prices and
reimbursementpolicieschange.
Quality of evidence All included comparisons were based on randomised trials and risk of bias was consistently
judged to be serious. Certainty was frequently reduced further because of inconsistency,
imprecision andsmallsamplesizes. Evidenceformonovision,EDOF versus monovisionand
multifocal versus EDOF was generally derived from relatively few studies, and several
patient-reported or adverse outcomes were informed by a single trial. These limitations
reduce confidence in any conclusion that one presbyopia-correcting strategy is superior
overall.
Other considerations Lens selection should also take account of ocular comorbidity, binocular function, refractive
predictability, previous experience with monovision and the patient’s ability to adapt to
optical phenomena. Counselling should make clear that no strategy guarantees complete
spectacleindependenceorfreedomfromvisualsymptoms.Expectedperformanceatdistance,
intermediate and near should be discussed in functional terms relevant to the individual
patient.

106
Supplementary Information 12. Recommendations (prospective study, human-only group)
Question: What is the optimal strategy to facilitate simultaneous distance and near vision following cataract surgery?
Recommendations in 2017 NICE guideline
(NG77: Cataracts in adults:management)
Recommendations updated by human experts
Do not offer multifocal intraocular lenses for people
havingcataractsurgery.
Offer monovision for use after cataract surgery to people
who have either anisometropia or monovision
preoperativelyandwouldliketoremainwithit.
 Discuss the choice of intraocular lens with the person before
cataract surgery, taking account of their priorities for unaided
distance, intermediate and near vision, willingness to use
spectaclesandtoleranceofunwantedvisualphenomena
 Consideramultifocal intraocularlensforpeoplewhose ocular
health is suitable and who place a high value on unaided
intermediate and near vision and reduced spectacle
dependence
 Explain that no intraocular lens strategy guarantees spectacle
independence, optimal vision at all distances or freedom from
visual symptoms, and that spectacles may still be required for
demandingtasks

107
Supplementary Information 13. External consensus survey (prospective study)
Background
This survey forms part of an expert preference assessment of candidate recommendations on the
useofintraocularlenses(IOLs)inpeopleundergoingcataractsurgery.
Threecandidaterecommendationshavebeendevelopedfortheclinicalquestion:
What is the optimal strategy to facilitate simultaneous distance and near vision following
cataract surgery?
This survey seeks to assess the clinical acceptability and practical applicability of each
recommendationamongabroadergroupofophthalmicexperts.
Instructions for expert reviewers
Please evaluate each recommendation using the five-point Likert scale below. Your rating should
reflect the extent to which you agree that the recommendation is clinically appropriate,
evidence-aligned,andacceptableforimplementationincurrentcataractsurgerypractice.
Score Response option
1 Stronglydisagree
2 Disagree
3 Neutral
4 Agree
5 Stronglyagree
Voting Questions (presented in randomized order)
Question 1: Recommendation A
Pleaseindicateyourlevelofagreementwiththefollowingrecommendation:
 Do not offer multifocal intraocular lenses for people having cataract surgery.
 Offer monovision for use after cataract surgery to people who have either anisometropia
or monovision preoperatively and would like to remain with it.

108
Rating:
☐1Stronglydisagree
☐2Disagree
☐3Neutral
☐4Agree
☐5Stronglyagree
Question 2: Recommendation B
Pleaseindicateyourlevelofagreementwiththefollowingrecommendation:
Consider multifocal intraocular lenses for people who want greater spectacle independence for
distance, intermediate and near vision. When discussing this option:
 ensure the person’s ocular health is suitable for multifocal intraocular lenses
 explain the potential benefits in uncorrected near and intermediate vision compared with
standard monofocal intraocular lenses
 discuss the increased risk of visual disturbances, such as halos, glare and starbursts
 take into account the person’s visual needs and daily activities
 consider cost implications and the person’s willingness to pay.
Rating:
☐1Stronglydisagree
☐2Disagree
☐3Neutral
☐4Agree
☐5Stronglyagree
Question 3: Recommendation C
Pleaseindicateyourlevelofagreementwiththefollowingrecommendation:

109
 Discuss the choice of intraocular lens with the person before cataract surgery, taking
account of their priorities for unaided distance, intermediate and near vision, willingness
to use spectacles and tolerance of unwanted visual phenomena
 Consider a multifocal intraocular lens for people whose ocular health is suitable and
who place a high value on unaided intermediate and near vision and reduced spectacle
dependence
 Explain that no intraocular lens strategy guarantees spectacle independence, optimal
vision at all distances or freedom from visual symptoms, and that spectacles may still be
required for demanding tasks
Rating:
☐1Stronglydisagree
☐2Disagree
☐3Neutral
☐4Agree
☐5Stronglyagree
Consensus Interpretation
Responses will be analyzed descriptively. For each recommendation, the proportion of experts
selecting“agree”or“stronglyagree”willbecalculated.Theresultswillbeusedtoassesswhether
the revised recommendation is aligned with current clinical evidence and acceptable for
implementationinreal-worldophthalmicsurgicalpractice.
