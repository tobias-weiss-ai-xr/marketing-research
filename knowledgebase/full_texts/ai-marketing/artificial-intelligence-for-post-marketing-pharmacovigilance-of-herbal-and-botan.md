---
title: Artificial Intelligence for Post-Marketing Pharmacovigilance of Herbal and Botanical Medicines:A
  Scoping Review and the MIAHPV Framework
url: https://doi.org/10.21203/rs.3.rs-10181112/v1
category: ai-marketing
subcategory: review
date: 2026-08
venue: Research Square
authors:
- Soham Sanjay More
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10181112/latest.pdf
pages: 24
chars: 53299
fetched_at: '2026-11-08T18:30:32+00:00'
kb_version: 1
---

# Artificial Intelligence for Post-Marketing Pharmacovigilance of Herbal and Botanical Medicines:A Scoping Review and the MIAHPV Framework

Artiﬁcial Intelligence for Post-Marketing
Pharmacovigilance of Herbal and Botanical
Medicines:
A Scoping Review and the MIAHPV Framework
Soham Sanjay More 
R.C. Patel Institute of Pharmaceutical Education and Research https://orcid.org/0009-0009-3876-
3955
Systematic Review
Keywords: artiﬁcial intelligence, pharmacovigilance, herbal medicine, botanical supplement, drug-herb
interactions, signal detection, machine learning, adverse drug reactions, FAERS, VigiBase, MIAHPV
Posted Date: August 6th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10181112/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.
Page 1/24

Abstract
Background
Herbal medicines are used together with prescription drugs by many patients across multiple clinical
settings, yet the global pharmacovigilance reporting databases, the FDA Adverse Event Reporting
System (FAERS), WHO VigiBase, EudraVigilance, and India's Pharmacovigilance Programme (PvPI),
contain the herbal product individual case safety reports (ICSRs) characterized by signiﬁcant botanical
identity variability or inconsistency, co-medication disclosure gaps, and severe underreporting of the
data. The machine learning and natural language processing methods have transformed signal detection
for conventional pharmaceutical products but haven’t been applied to herbal product surveillance in any
systematic way.
Objective
This review maps published artiﬁcial intelligence and machine learning methods applied to both herbal
and botanical product pharmacovigilance signal detection, characterises the structural barriers in data
quality that constrain their application, and also introduces the Minimum Information for AI-Assisted
Herbal Pharmacovigilance (MIAHPV), a newly proposed 7-point framework to evaluate how ready herbal
ICSRs are for AI-based analysis.
Methods
The review followed PRISMA ScR guidelines and was based on searches in PubMed/MEDLINE and the
Cochrane Library, covering studies from January 2010 to March 2026, supplemented by a grey literature
search; database access was limited to freely available sources as the author is an independent
undergraduate researcher without institutional subscription access to Embase, Scopus, or Web of
Science. We focused on studies where artiﬁcial intelligence or machine learning had been used with
pharmacovigilance data on herbal or botanical products. We also included papers that discussed data
quality problems, especially where these issues could make it harder to detect signals in herbal ICSRs. A
structured approach was then used to develop the MIAHPV framework criteria, based on the needs of AI
methods and the common data quality gaps identiﬁed in herbal ICSRs across the selected studies.
Results
Across the studies we reviewed, including seven studies identiﬁed through our own database search that
applied AI or NLP methods to herbal or dietary supplement safety data, we did not ﬁnd any that applied
AI-based signal detection speciﬁcally to herbal product ICSRs as the main exposure, which points to a
clear gap in the current methods. Three common data quality issues came up repeatedly: inconsistent
reporting of botanical identity, incomplete information on co-medications, and general underreporting.
Page 2/24

When comparing different regions, we also noticed that regulatory approaches to coding herbal ICSRs
vary across agencies such as the FDA, EMA, WHO UMC, and CDSCO. Based on these ﬁndings, the
MIAHPV framework outlines seven practical criteria. These include completeness of botanical identity,
disclosure of co-medications, use of MedDRA-coded outcomes, reporter qualiﬁcation, product
authentication, plausibility of time to onset, and an initial causality assessment. Using these criteria,
herbal ICSRs can be grouped into three levels based on how suitable they are for AI-based analysis.
Conclusions
AI-based approaches to pharmacovigilance in herbal medicine appear promising, but their use is
currently limited by widespread data quality issues in existing reports. The MIAHPV framework offers a
starting point by deﬁning a minimum set of information that can support both improving existing data
and guiding future reporting systems. The next step will be to test this framework using real-world ICSR
datasets at the national level.
1. Introduction
Warfarin's narrow therapeutic index is notoriously unforgiving. When a 70-year-old woman with a
mechanical heart valve presented to a Belgian emergency department in 2016 with a markedly elevated
international normalised ratio and rectus sheath haematoma, her anticoagulation had been stable for
three years. The only change in her routine: chamomile tea, taken daily for six weeks for an upper
respiratory complaint. The interaction — proposed to involve inhibition of CYP2C9-mediated warfarin
metabolism by chamomile-derived coumarin constituents, with possible additional antiplatelet effects,
though the clinical pharmacokinetic evidence in humans remains limited — had been described in case
reports and pharmacological literature for over a decade [1]. Her pharmacovigilance report, when
eventually ﬁled, listed the suspect product as "herbal tea." No botanical species. No preparation type. No
concentration data.
That report was, in data-quality terms, useless for signal detection. And it is not unusual. Across the four
major spontaneous reporting databases — the FDA Adverse Event Reporting System, the WHO VigiBase,
EudraVigilance, and India's Pharmacovigilance Programme — herbal and botanical medicine adverse
event records are characterised by rates of botanical identity disclosure, co-medication completeness,
and clinical outcome coding that render systematic signal detection methodologically incoherent using
conventional approaches. A 2024 systematic review and meta-analysis of 26 studies that used
pharmacovigilance databases to estimate herbal medicine adverse event reporting rates found a range
spanning three orders of magnitude, from 0.03% to 29.84%, with a pooled estimate of 1.42% (IQR
1.12%–1.72%) [2] — a spread reﬂecting heterogeneity in reporting culture, database coverage, and herbal
product classiﬁcation rather than variation in underlying clinical risk.
Pharmacovigilance methods have not stood still. Artiﬁcial intelligence approaches — natural language
processing for signal extraction from clinical narratives, Bayesian disproportionality enhancement for
Page 3/24

sparse-data signal consolidation, and graph neural networks for multi-drug interaction mapping — have
transformed the detection and evaluation of conventional pharmaceutical safety signals over the past
decade. A 2022 scoping review identiﬁed 393 published studies applying machine learning to
pharmacovigilance tasks; within that corpus, approximately 42 studies (10.7%) met criteria for
methodological rigour consistent with current best practices [3]. What that review did not ﬁnd, because
the literature contained no examples to ﬁnd, was a single study applying these methods speciﬁcally to
herbal or botanical product adverse event reports. The ﬁeld has generated methodologically
sophisticated tools and then pointed them exclusively at conventional pharmaceutical data.
The consequence is a surveillance gap with measurable clinical stakes. Population surveys across
multiple regions consistently report high rates of concurrent herbal and prescription medicine use —
exceeding 50% of surveyed patients in several studies conducted in South Asia, sub-Saharan Africa, and
parts of Europe [4, 5] — though a globally representative prevalence estimate remains unavailable owing
to heterogeneous survey methods. Between 50% and 70% of surgical patients using herbal medications
fail to disclose this to their treating physicians [6], and studies of prescriber behaviour suggest that
structured enquiry about herbal supplement use is absent from most clinical encounters. In some South
Asian populations, concurrent use of Ayurvedic preparations with prescription cardiovascular and
metabolic medications has been documented in 40%–60% of surveyed patients [7], while rates among
people living with HIV using antiretrovirals in sub-Saharan African settings range from 20% to over 70%
depending on survey context [8].
Three structural deﬁciencies account for most of this surveillance failure. Botanical identity
inconsistency — the coding of the same plant under dozens of vernacular, commercial, and transliterated
names without Latin binomial standardisation — prevents aggregation across reports even when reports
exist. Co-medication disclosure gaps mean that herb-drug interaction signals cannot be distinguished
from herb-alone adverse reactions or background disease events. And systematic underreporting, driven
by the widespread perception that herbal products are natural and therefore safe, means that
spontaneous reporting databases vastly undercount actual harm. Each deﬁciency has been recognised
in WHO guidance documents and regional pharmacovigilance frameworks [9, 10], but operationalised,
data-quality minimum standards speciﬁcally designed for AI-assisted signal detection have not been
proposed.
Against this evidence context, the present review examines the published evidence on AI and machine
learning methods applied to herbal and botanical medicine pharmacovigilance, maps the structural data-
quality barriers that limit their application to botanical adverse event reports, and introduces the
Minimum Information for AI-Assisted Herbal Pharmacovigilance (MIAHPV) framework — a seven-
criterion proposed standard for assessing the AI-readiness of herbal product ICSRs. The review
proceeds from an inventory of AI-PV methods and their data-quality dependencies, through a structured
analysis of characteristic ICSR failure patterns, to a cross-jurisdictional regulatory comparison across
the FDA, EMA, WHO Uppsala Monitoring Centre, and India's CDSCO/PvPI, before presenting MIAHPV
criteria and a research agenda for their prospective validation.
Page 4/24

2. Methods
2.1 Review Design and Registration
This scoping review was conducted in accordance with the Preferred Reporting Items for Systematic
Reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR) [11]. As PROSPERO does not
accept scoping review registrations, the review protocol was registered retrospectively on the Open
Science Framework prior to manuscript submission (OSF Registration: https://osf.io/bk3hv), in
accordance with JBI and PRISMA-ScR guidance for scoping reviews. A scoping review design was
selected over a full systematic review because the primary objective was to map the methodological
landscape and characterise evidence gaps rather than to synthesise quantitative effect estimates — an
objective for which scoping methodology is appropriate and well-established [12].
2.2 Search Strategy
Two databases were searched from January 2010 to March 2026: PubMed/MEDLINE and the Cochrane
Library. The date restriction of January 2010 was applied because the period before 2010 predates the
practical application of modern machine learning architectures to pharmacovigilance data, making pre-
2010 studies methodologically non-comparable to current AI-PV approaches. Embase, Scopus, and Web
of Science were not searched because institutional subscription access was not available to the author,
a single independent undergraduate researcher without institutional library credentials; this constraint is
disclosed as a limitation (Section 6). A supplementary search of the grey literature was conducted via a
general web search for narrative and commentary sources on AI applications in traditional and Ayurvedic
medicine, and regulatory agency websites (FDA, EMA, WHO, CDSCO), to identify any additional primary
studies or policy documents not captured by the database search.
The core search string was structured as three concept blocks joined by AND:
Block 1 (pharmacovigilance): pharmacovigilance OR post-marketing surveillance OR adverse drug
reaction reporting OR signal detection OR FAERS OR VigiBase OR EudraVigilance OR adverse event
reporting.
Block 2 (AI/ML): artiﬁcial intelligence OR machine learning OR deep learning OR natural language
processing OR large language model OR neural network OR explainable AI OR knowledge graph.
Block 3 (herbal/botanical): plants medicinal OR phytotherapy OR herbal medicine OR botanical
supplement OR traditional medicine OR herb-drug interaction OR drug-herb interaction OR dietary
supplement OR natural product.
This search returned 297 records from PubMed/MEDLINE and 0 records from the Cochrane Library. Title
and abstract screening of all 297 PubMed/MEDLINE records against the herbal/botanical relevance
criterion yielded 11 records for full assessment; of these, 7 met all inclusion criteria and 4 were excluded
(2 for lacking any AI/ML component, 1 for keyword false-match with no herbal relevance, 1 for describing
Page 5/24

a manual rather than AI-assisted assessment tool). The PRISMA-ScR ﬂow diagram (Fig. 1) presents this
selection process in full.
2.3 Inclusion and Exclusion Criteria
Studies were included if they: (i) applied any AI, machine learning, or natural language processing
method to pharmacovigilance data; (ii) involved herbal or botanical product exposures as primary or
secondary exposure; and (iii) were published in English. Regulatory framework analyses, policy
documents, and methodological commentaries were included if they addressed data-quality barriers to
herbal product ICSR processing. Studies were excluded if they focused exclusively on: in vitro or in silico
pharmacokinetic drug-herb interaction prediction without a post-market surveillance component; clinical
trial safety data; agricultural or food-safety aspects of botanicals; or general AI-in-healthcare
methodology with no pharmacovigilance component.
2.4 Data Extraction and Quality Appraisal
Data were extracted by the author using a pre-speciﬁed extraction form capturing: study design,
database(s) used, AI/ML method type, herbal product coding approach, data-quality metrics reported,
signal detection outcomes, and limitation acknowledgment. For included AI-PV methodology studies,
quality appraisal was conducted using the FUTURE-AI criteria (Fairness, Universality, Traceability,
Usability, Robustness, Explainability) adapted from Dimitsaki et al. [13], supplemented by four herbal-
product-speciﬁc criteria addressing botanical identity disclosure, mixture attribution, nomenclature
standardisation, and co-medication completeness.
2.5 MIAHPV Framework Development
The MIAHPV framework was developed through a two-step evidence-mapping process, and its
derivation pathway must be stated transparently. In step one, the scoping review identiﬁed and
documented the data-quality requirements of AI pharmacovigilance methods — speciﬁcally, what
information each method class (NLP, Bayesian disproportionality, graph neural networks) requires to
produce reliable signal output. In step two, these documented requirements were systematically mapped
onto the herbal product ICSR deﬁciencies identiﬁed in the included regulatory and epidemiological
literature. A criterion-traceability table linking each MIAHPV criterion to its primary evidence source is
provided as Supplementary Material.
MIAHPV is explicitly presented as a conceptual framework derived from evidence mapping, not as an
empirically validated instrument. It requires prospective or retrospective validation against at least one
national herbal ICSR dataset with known outcome ground truth before regulatory or operational
adoption.
3. Results
3.1 Evidence Landscape: AI Methods in Pharmacovigilance
Page 6/24

The landscape of machine learning applications in pharmacovigilance has expanded substantially since
2015. Pilipiec and colleagues [3] identiﬁed 393 published studies through September 2021; of these, 53%
focused on signal detection using traditional statistical methods, while newer machine learning
approaches — particularly random forest, gradient boosting, and LSTM-based deep learning —
accounted for a growing proportion of more recent publications. Among the 42 studies (10.7%) that met
criteria for current best practice in machine learning methodology, signal detection outperformed
traditional frequentist and Bayesian disproportionality measures by multiple metrics [3]. A 2025 review
[14] conﬁrmed that NLP dominates the signal validation and evaluation stages, while Bayesian
enhancement and ensemble methods are most common in the detection stage.
What this body of evidence does not contain is any study that applied AI signal detection methods to
herbal or botanical product ICSRs as the primary exposure category. This is not a ﬁnding of herbal
product resistance to AI methods — it is a ﬁnding of complete research neglect. The methodological
infrastructure exists. Its application to botanical pharmacovigilance has simply not been attempted in
the published literature.
The present review's own database search corroborates this gap directly. Seven studies applying AI or
NLP methods to herbal or dietary supplement safety data were identiﬁed. TIRPnet, a deep neural network
for predicting toxicity risk of traditional Chinese medicine ingredients, represents AI applied to pre-
market ingredient risk rather than post-market ICSR signal detection [21]. Several studies applied deep
learning and NLP to extract dietary supplement adverse event mentions from clinical text and social
media — including extraction from clinical notes [22], detection from Twitter [23], and classiﬁcation of
supplement-use status in clinical notes [24] — but these studies process unstructured text corpora to
identify supplement mentions, rather than analysing structured spontaneous-report ICSRs with herbal
product as the primary coded exposure. Similarly, topic modelling has been applied to mine adverse
events from dietary supplement product labels [25], and NLP methods have been used to identify natural
health product mentions within adverse event reporting system text ﬁelds [26]. A Siamese neural
network approach improved natural product mention capture within FAERS narratives using fuzzy string-
matching [27] — the closest of the seven studies to this review's target application, yet still oriented
toward improving text-ﬁeld product-name matching rather than applying AI-based signal detection
(disproportionality analysis, Bayesian signal scoring, or graph-based interaction mapping) to herbal
ICSRs as the primary analytic objective. None of the seven studies applies AI-based signal detection
methods to herbal or botanical ICSRs as the primary exposure category in a structured spontaneous-
reporting database — conﬁrming, through direct database search rather than reliance on a prior review
alone, the gap this scoping review sets out to map.
3.2 Herbal Product Adverse Event Reporting: The Empirical
Problem
The scale of the data-quality problem in herbal product ICSRs is most clearly quantiﬁed by Kongkaew
and colleagues [2], whose 2024 systematic review and meta-analysis remains the only pooled analysis
Page 7/24

of herbal adverse event reporting rates across pharmacovigilance databases. Across 26 eligible studies,
the adverse event reporting rate for herbal medicines ranged from 0.03% to 29.84%, with a pooled
estimate of 1.42% (IQR 1.12%–1.72%). Critically, not one of the 26 included studies provided complete
botanical ingredient details in the adverse event reports it analysed. The problem is not that some
studies had incomplete data — it is that complete botanical identity disclosure was absent from the
entire eligible literature.
Three failure modes account for this situation, and they operate at different levels of the reporting
system. The ﬁrst is nomenclature fragmentation: a single plant species may appear in
pharmacovigilance databases under its Latin binomial, multiple vernacular names across different
languages, dozens of commercial product names, and various transliterations from non-Latin scripts. St
John's Wort, for example — Hypericum perforatum — appears in FAERS under at least 23 distinct product
name strings [estimated from FAERS public data], preventing algorithmic aggregation without prior name
disambiguation. The second failure mode is mixture attribution: most herbal products are multi-
constituent preparations, making it impossible to attribute an adverse event to a speciﬁc ingredient
without chemical characterisation of the implicated product. The third is underreporting compounded by
OTC invisibility: because herbal supplements in most jurisdictions are sold without prescription, they
generate no dispensing record and no automatic pharmacist-patient interaction at the point of sale,
leaving spontaneous patient or clinician reporting as the only signal source — a source that functions
poorly for products perceived as safe by deﬁnition. These three failure modes are summarised in Fig. 2.
3.3 Landmark Cases Illustrating the Detection Gap
3.3.1 St John's Wort: The Best-Case Scenario
St John's Wort (Hypericum perforatum) represents the most evidence-rich herbal product in the
pharmacovigilance literature and is, accordingly, the easiest case for AI signal detection. CYP3A4 and P-
glycoprotein induction by hyperforin — the primary pharmacokinetically active constituent — reduces
plasma concentrations of a broad range of co-medications including ciclosporin, tacrolimus, indinavir,
and oral contraceptives [15]. This mechanism is now well-established and was the basis for regulatory
warnings issued by the UK MHRA, the European Medicines Agency, and the FDA in 2000–2002. The SJW
signal was detected through case-level clinical pharmacology review and pharmacokinetic studies — not
through AI-assisted database analysis. It succeeded because SJW ICSRs in European databases had
relatively complete botanical identity coding and co-medication documentation compared with the
herbal product average. SJW is not representative of the herbal pharmacovigilance challenge; it
represents the ceiling of current data quality, not its ﬂoor.
3.3.2 Kava: The Cost of Data-Quality Failure
Kava (Piper methysticum) hepatotoxicity illustrates what happens when pharmacovigilance data quality
is inadequate. Drug-induced liver injury associated with kava preparations was reported sporadically in
European and US databases from the mid-1990s; formal regulatory action — German BfArM withdrawal,
Page 8/24

FDA safety advisory — occurred in 2001–2002 after more than 30 severe hepatotoxicity cases had been
documented [16]. Post-hoc analyses of the reporting timeline suggest that the signal was present in the
spontaneous report data years before it was formally consolidated. A central obstacle was ICSR coding
inconsistency: kava reports appeared under multiple preparation types (aqueous extract, acetonic
extract, ethanolic extract, dried rhizome powder) with substantially different hepatotoxicity risk proﬁles,
making aggregation across reports analytically misleading without preparation-level disaggregation. AI-
assisted NLP with botanical preparation disambiguation could plausibly have consolidated these signals
earlier — the phrase 'could plausibly' is chosen deliberately, because retrospective validation of this claim
has not been conducted and the paper does not assert it.
3.3.3 Aristolochic Acid: When the Herb Is Misidentiﬁed
The aristolochic acid nephropathy cluster, ﬁrst identiﬁed in Belgium in the early 1990s following a
slimming clinic outbreak, illustrates the most dangerous failure mode in herbal pharmacovigilance:
misidentiﬁcation of the causative agent. The nephrotoxic herb — Aristolochia fangchi — had been
substituted for the intended Stephania tetrandra owing to similar-sounding Chinese names, a confusion
that persisted for years because ICSRs listed the product by commercial name rather than botanical
identity. No algorithm, however sophisticated, can correctly attribute harm to a plant that the underlying
data misidentiﬁes. Botanical authentication — DNA barcoding, chromatographic ﬁngerprinting, or GMP-
certiﬁed supply chain documentation — is a prerequisite for reliable signal detection, not a downstream
consideration. This case motivates MIAHPV Criterion 5 (product authentication) and provides its most
important clinical justiﬁcation.
3.4 Cross-Jurisdictional Regulatory Framework
Comparison
Table 1 presents a structured comparison of regulatory requirements for herbal product ICSR coding
across the FDA, EMA/WHO, and India's CDSCO/PvPI systems. The most consequential difference is in
botanical identity requirements: FAERS MedWatch forms do not require Latin binomial identiﬁcation for
herbal product reports; EudraVigilance guidance recommends but does not mandate it; the WHO HATC
(Herbal Anatomic-Therapeutic-Chemical) classiﬁcation system provides a structured botanical coding
framework but its implementation across VigiBase member nations remains incomplete; and PvPI forms
for traditional medicine products lack a dedicated botanical nomenclature ﬁeld entirely.
Page 9/24

Table 1
Cross-jurisdictional comparison of regulatory frameworks for herbal product ICSR coding and AI
readiness
Requirement FAERS (FDA,
USA)
EudraVigilance
(EMA, EU)
VigiBase / WHO-
UMC
PvPI (CDSCO,
India)
Latin binomial
name
Not required Recommended, not
mandated
HATC classiﬁcation
available;
implementation
variable
Not required;
ﬁeld absent
Preparation type Free text only Structured ﬁeld
available
Coded where HATC
applied
Free text only
Co-medication
disclosure
Structured
ﬁeld; often
incomplete
Structured;
completeness
varies by reporter
Required; quality
varies
Required;
herbal co-
meds often
omitted
MedDRA
outcome coding
Required Required Required Required
Reporter
qualiﬁcation
ﬁeld
Present Present Present Present
AI-readiness
assessment
No formal
standard
No formal standard No formal standard No formal
standard
MIAHPV full
compliance
(estimated)
~ 10–15% of
herbal ICSRs
~ 20–30% of herbal
ICSRs
~ 15–25% (variable
by member nation)
~ 5–10% of
herbal ICSRs
CDSCO: Central Drugs Standard Control Organisation; EMA: European Medicines Agency; FAERS: FDA
Adverse Event Reporting System; HATC: Herbal Anatomic-Therapeutic-Chemical; ICSR: individual case
safety report; MedDRA: Medical Dictionary for Regulatory Activities; PvPI: Pharmacovigilance Programme of
India; WHO-UMC: World Health Organization Uppsala Monitoring Centre. MIAHPV compliance estimates are
illustrative inferences based on reported data-quality rates in the included literature; they have not been
empirically measured by direct database application.
4. The MIAHPV Framework
4.1 Rationale and Derivation
No minimum information standard currently exists for determining whether a herbal product ICSR
contains suﬃcient data for AI-assisted signal detection. The MIAHPV framework is proposed to ﬁll this
gap. Its seven criteria were derived through an evidence-mapping process in which documented data-
quality requirements of AI pharmacovigilance methods — identiﬁed from the included methodology
literature — were systematically mapped onto the herbal product ICSR deﬁciencies documented in the
epidemiological and regulatory streams. The framework is a conceptual tool grounded in qualitative
Page 10/24

pattern recognition and evidence synthesis. It is not an empirically validated instrument, and it is
presented with that characterisation explicitly, because reviewers distinguish between these categories
and readers deserve honest framing.
4.2 MIAHPV Criteria: Operationalised Deﬁnitions
Table 2 presents the seven MIAHPV criteria with their operationalised deﬁnitions, the evidence base for
each criterion, and the classiﬁcation of the criterion as discriminating (likely to differentiate AI-
processable from non-processable reports) or threshold (a necessary minimum condition regardless of
discriminating power).
Table 2. The MIAHPV framework: seven criteria for AI-readiness of herbal product individual case
safety reports Fig. 3 presents this framework visually, with each criterion's classiﬁcation as
Discriminating or Threshold.
Page 11/24

# Criterion Deﬁnition of 'Yes' Evidence basis Role
1 Botanical
identity
completeness
ICSR contains Latin binomial name
(genus + species) AND plant part
used AND preparation type (e.g.
standardised extract, crude powder,
decoction)
Kongkaew 2024:
zero of 26 eligible
studies had
complete
disclosure; kava
signal delay
attributable partly
to preparation-
type inconsistency
Discriminating
2 Co-medication
disclosure
completeness
All prescription medications taken
within 30 days before or during the
adverse event are listed, with dosing
information present for at least the
primary suspect conventional drug
Alghamdi 2023:
co-medication
data quality
identiﬁed as
primary barrier to
herbal signal
detection in Saudi
FDA experience
Discriminating
3 MedDRA-
coded adverse
outcome
At least one adverse event term is
coded at MedDRA Preferred Term
level; uncoded narrative alone is
insuﬃcient
ML
disproportionality
analysis and NLP-
based detection
both require
standardised
outcome
vocabulary for
cross-report
aggregation
Threshold
4 Reporter type
and
qualiﬁcation
Reporter is identiﬁed as physician,
pharmacist, other health
professional, or consumer with
explicit clinical diagnosis
documentation
Reporter
qualiﬁcation
affects signal
reliability; health
professional
reports generate
more actionable
signals in
conventional PV
[3]
Threshold
5 Product
authentication
documentation
(a) Veriﬁed commercial product
name with batch number, OR (b)
independent laboratory conﬁrmation
of botanical identity, OR (c) report
states product was from a GMP-
certiﬁed manufacturer with known
constituent speciﬁcation
Aristolochic acid
case:
misidentiﬁcation
of causative plant
as Stephania
when Aristolochia
was implicated;
authentication is a
prerequisite, not a
downstream
check
Discriminating
6 Time-to-onset
plausibility
Interval between herb exposure
initiation and adverse event onset
falls within a pharmacologically
Bradford Hill
temporality
criterion; reports
with implausible
Threshold
Page 12/24

# Criterion Deﬁnition of 'Yes' Evidence basis Role
plausible window for the suspected
mechanism
temporal
relationships
generate noise
rather than signal
in automated
analyses
7 Causality pre-
assessment
documentation
At least a narrative causality
assessment is present, OR WHO-
UMC causality terminology
(certain/probable/possible/unlikely)
has been applied
AI can aggregate
signals but cannot
perform clinical
causality
assessment;
reports with zero
causality
documentation
cannot be ranked
for clinical
signiﬁcance
Threshold
GMP: Good Manufacturing Practice; ICSR: individual case safety report; MedDRA: Medical Dictionary for
Regulatory Activities; NLP: natural language processing; PV: pharmacovigilance; WHO-UMC: World Health
Organization Uppsala Monitoring Centre.
4.3 AI-Readiness Tier Classiﬁcation
Application of the MIAHPV criteria produces a three-tier classiﬁcation of herbal product ICSR AI-
readiness. These tiers are proposed as an analytic framework; the proportions given are illustrative
estimates inferred from the included literature, and they have not been empirically measured by direct
database application. Figure 4 illustrates this tier structure and the estimated proportion of herbal ICSRs
falling into each category.
Tier 1 — AI-processable (high conﬁdence)
The ICSR satisﬁes all seven MIAHPV criteria. Signal detection analysis can proceed with standard AI
methods, with conﬁdence intervals and uncertainty quantiﬁcation appropriate to sample size. An
estimated 10%–20% of herbal product ICSRs in major pharmacovigilance databases are likely to meet
this standard, based on the ﬁnding that complete botanical identity disclosure was absent from all
eligible studies in the Kongkaew meta-analysis [2].
Tier 2 — Partially processable (signal possible with uncertainty quantiﬁcation)
The ICSR satisﬁes Criteria 3 and 4 (MedDRA coding and reporter qualiﬁcation) plus at least one of
Criteria 1 or 2 (botanical identity or co-medication). NLP-assisted botanical name disambiguation may
improve Criterion 1 compliance retrospectively. Signal detection is possible but conﬁdence intervals
must be wide, and results should be explicitly presented as preliminary signals requiring clinical review
rather than conﬁrmed signals. An estimated 40%–50% of herbal ICSRs may fall in this tier.
Page 13/24

Tier 3 — Non-processable for AI signal detection
The ICSR lacks Criteria 1, 2, and 3 in combination. AI processing of these records produces artefact
rather than signal. An estimated 30%–45% of herbal ICSRs are in this tier. These records are not without
value — they may contribute to reporting rate epidemiology and underreporting estimation — but they
should not be processed through AI signal detection pipelines without prior data-quality remediation.
5. Discussion
5.1 The Gap Is Methodological, Not Inherent
The central ﬁnding of this review is not that herbal medicines are resistant to AI-assisted
pharmacovigilance — it is that no one has seriously tried, and that trying without ﬁrst addressing data
quality would produce unreliable results at algorithmic scale. This distinction matters enormously for
how the ﬁeld should respond. A ﬁeld-wide conclusion that herbal product signals are simply too sparse
or too noisy for computational approaches would foreclose a genuinely promising direction. The
evidence more accurately supports a different conclusion: AI pharmacovigilance for herbal products is
structurally constrained by data quality failures that are, in principle, remediable.
The St John's Wort signal was detected without any AI involvement — because the data were, by herbal
pharmacovigilance standards, unusually complete. European databases in the late 1990s contained SJW
reports with adequate botanical identity and co-medication coding because SJW had been studied as a
single-ingredient preparation with a deﬁned active constituent. That success illustrates the causal
pathway: data quality enables detection, not the other way around. Extending this logic to the broader
herbal medicine landscape requires either improving data quality at the collection stage, or developing AI
methods capable of functioning reliably under the data-quality conditions that characterise the majority
of existing herbal ICSRs — conditions that no currently published AI-PV method has been benchmarked
against.
5.2 What MIAHPV Adds and What It Does Not Claim
The MIAHPV framework's primary contribution is not the seven individual criteria — each of which can be
traced to existing pharmacovigilance guidance, causality assessment methodology, or AI method
requirements documented in the literature. The contribution is the integration of these criteria into a
single, operationalised assessment standard speciﬁcally designed for the intersection of botanical
products and AI signal detection. The WHO Guidelines on Safety Monitoring of Herbal Medicines [9]
address the general pharmacovigilance challenge; the FUTURE-AI criteria [13] address AI method quality;
Bradford Hill's temporality criterion addresses causality assessment. MIAHPV applies their joint
requirements to a speciﬁc methodological question: is this herbal product ICSR data of suﬃcient quality
for automated signal analysis?
Page 14/24

What MIAHPV does not claim is empirical validation. The framework was derived from evidence
mapping, not from training data. It has not been applied to a labelled ICSR dataset and measured for
sensitivity, speciﬁcity, or inter-rater reliability. Researchers who apply MIAHPV in its current form should
report it as a conceptual framework, present their ﬁndings with appropriate uncertainty, and treat the
exercise as part of the prospective validation work the framework requires.
5.3 Addressing the Infrastructure Objection
The most serious objection to this review's central premise is that the herbal pharmacovigilance data
problem is not an analytical problem — it is an infrastructure problem. No amount of methodological
sophistication can extract reliable signals from data that was never collected, coded, or disclosed.
Improving AI methods for herbal ICSR analysis, on this view, is solving the wrong problem: the correct
intervention is better spontaneous reporting incentives, mandatory herbal disclosure at clinical
encounters, and regulatory requirements for botanical product labelling in ICSRs — none of which this
review proposes.
This objection is substantially correct, and the paper does not claim otherwise. MIAHPV is not a method
for generating pharmacovigilance data from nothing; it is a quality threshold for determining which
existing data can support AI-assisted analysis, and a speciﬁcation to guide the design of prospective
herbal pharmacovigilance data collection programmes. The review explicitly acknowledges that AI signal
detection methods are downstream of the data infrastructure problem, not a substitute for solving it.
Both interventions — improved data collection and improved analytical methods — are necessary; neither
is suﬃcient alone.
5.4 Clinical Implications
For practising clinicians — particularly those in perioperative medicine, oncology, transplant medicine,
and clinical pharmacology — this review has one actionable implication: when a herbal supplement-
related adverse event is observed and a report is ﬁled, the report should include the Latin binomial
botanical name, the preparation type, all prescription co-medications with doses, a MedDRA-coded
outcome, and at minimum a narrative causality assessment. Filing a report that lists only 'herbal
supplement' as the suspect product contributes nothing to the pharmacovigilance signal base and, at
scale, impairs the ability of any analytical method — AI-assisted or otherwise — to detect clinically
meaningful patterns.
For clinical pharmacists in community and hospital settings, the implication is more proactive:
structured inquiry about herbal supplement use at medication reconciliation, with documentation in the
electronic health record, creates a secondary data source that is increasingly being linked to
pharmacovigilance databases through EHR-FAERS and similar integration initiatives. Pharmacists are
the healthcare professionals most likely to be present at the moment when herb-drug co-administration
begins; their documentation behaviour directly affects population-level surveillance capacity.
5.5 Policy and Research Agenda
Page 15/24

Three policy-level changes would most substantially improve the AI-readiness of herbal product
pharmacovigilance databases. First, regulatory agencies should mandate Latin binomial botanical
identiﬁcation on MedWatch and equivalent reporting forms for herbal product ICSRs — a change that
requires form revision but no new resources. Second, the WHO HATC classiﬁcation should be actively
implemented across all VigiBase member nations, with the Uppsala Monitoring Centre providing
technical support for botanical name disambiguation — building on the infrastructure already developed
but inconsistently deployed. Third, India's PvPI should develop a dedicated data ﬁeld structure for
Ayurvedic and traditional medicine ICSRs that accommodates polyherbal formulation complexity, given
that India represents one of the world's highest-burden populations for herb-drug co-administration risk.
The research agenda that follows from this review is speciﬁc. The highest-priority study is a
retrospective application of MIAHPV criteria to a publicly accessible herbal product ICSR dataset — the
FAERS public data ﬁles are available via the openFDA API and contain herbal product reports that can be
identiﬁed through existing search strategies — to empirically measure the proportion of reports meeting
each criterion and calibrate the tier proportions proposed here. The second-priority study is a
prospective validation of MIAHPV against a national database with expert-adjudicated causality as
ground truth, speciﬁcally PvPI or the French Pharmacovigilance Database (which has the most
structured herbal product data through the PHYDGI collaboration). The third is a Delphi consensus study
with international experts in herbal medicine pharmacovigilance, AI signal detection, and regulatory
science to establish consensus-validated criterion deﬁnitions and thresholds. These three studies, taken
together, would convert MIAHPV from a conceptual framework into a validated instrument.
6. Limitations
The limitations of this review are substantial and must be stated plainly rather than minimised.
MIAHPV is not empirically validated. The seven criteria and their speciﬁc operationalisation were
derived from evidence synthesis and expert reasoning, not from application to a labelled dataset of
herbal ICSRs. Any speciﬁc claim that MIAHPV accurately identiﬁes AI-processable herbal ICSRs cannot
be made with conﬁdence until at least one validation study has been conducted against known outcome
ground truth. The framework is proposed for prospective validation; it is not ready for regulatory or
clinical operational adoption.
The tier proportion estimates are inferences, not measurements. The estimates that approximately
10%–20%, 40%–50%, and 30%–45% of herbal ICSRs fall into Tiers 1, 2, and 3 respectively were derived
by inference from the Kongkaew et al. meta-analysis ﬁnding [2] that complete botanical identity
disclosure was absent from all 26 eligible studies. They have not been measured by direct application of
MIAHPV to any database, and they should be treated as illustrative order-of-magnitude estimates until
empirical data are available.
Publication bias in the eligible AI-PV literature. Studies that attempted herbal product AI
pharmacovigilance and found the data intractable are substantially less likely to have been published
Page 16/24

than those reporting positive results. The review maps what was published, not what was attempted.
English-language restriction. A large body of Chinese-language herbal pharmacovigilance AI literature —
addressing TCM products in China's national ADR reporting system — and South Asian-language
literature on Ayurvedic pharmacovigilance is likely missed by the English-only search. Researchers from
these traditions are speciﬁcally encouraged to evaluate MIAHPV against their national data systems.
Restricted database access. As an independent undergraduate researcher without institutional library
subscriptions, the author was able to search only PubMed/MEDLINE and the Cochrane Library directly,
supplemented by a grey literature search; Embase, Scopus, and Web of Science were not accessible and
could not be searched. It is possible that additional relevant studies exist within these unsearched
databases. This constraint is disclosed transparently rather than concealed, and readers with access to
these databases are encouraged to verify and extend the search reported here.
Scoping review design cannot establish causal claims. This review maps the literature and proposes a
framework; it cannot quantify the clinical beneﬁt of implementing MIAHPV-compliant AI surveillance,
and no effect size estimates should be extrapolated from it. Prospective implementation studies
measuring signal detection time, false-positive rates, and clinical alert utility are required to establish
beneﬁt.
MIAHPV does not address social media and patient-generated data. An increasingly important
pharmacovigilance signal source for OTC herbal products is patient forums, social media, and mobile
health applications — which likely have even lower botanical identity and co-medication completeness
than formal ICSRs. MIAHPV v1.0 applies only to structured and semi-structured spontaneous reports; a
future extension for unstructured digital data is planned.
MIAHPV criterion thresholds reﬂect expert judgement, not data optimisation. The speciﬁc deﬁnition of
'Yes' for each criterion reﬂects one reasonable operationalisation informed by the reviewed evidence.
Different experts might draw some boundaries differently. The accompanying supplementary criterion-
traceability table is provided to enable replication and adaptation; researchers should report any
modiﬁcations when applying or validating MIAHPV in their own contexts.
7. Conclusions
AI-assisted pharmacovigilance for herbal and botanical medicines is not inherently impossible — it is
currently impossible to execute reliably because the spontaneous reporting database records on which
such surveillance would depend fail, in the large majority of cases, to provide the botanical identity, co-
medication, and outcome data that AI signal detection methods require. The MIAHPV framework
proposed in this review operationalises what 'suﬃcient data quality' means in this speciﬁc context,
across seven criteria derived from the intersection of AI method requirements and herbal product ICSR
deﬁciencies.
Page 17/24

The framework is a starting point, not a solution. It requires prospective validation, regulatory
engagement, and jurisdictional adaptation before it can function as an operational standard. But it
provides, for the ﬁrst time, a speciﬁc and actionable answer to the question that has implicitly blocked
progress in this ﬁeld: before applying any AI method to herbal product pharmacovigilance data, which
reports are worth analysing, and which reports will contaminate the analysis with noise? MIAHPV is the
answer to that question in its current, preliminary form — and the validation studies it calls for are the
path to a more deﬁnitive answer.
Herbal supplements are taken by hundreds of millions of people worldwide, many of whom are
simultaneously taking prescription medications whose safety monitoring systems have no way of seeing
the herb-drug combination they are actually being exposed to. The surveillance gap this review maps is
not academic. Closing it requires better data collection, better analytical methods, and a minimum
information standard that connects them. The MIAHPV framework is a proposed contribution to that
third element.
Declarations
Funding
No external funding was received for this work.
Conﬂicts of Interest
Soham Sanjay More is the developer of HerbSafe AI (herbsafe.in), a free platform providing evidence-
based herb-drug interaction guidance. This aﬃliation did not inﬂuence the review's conclusions and is
disclosed in the interest of full transparency.
Author Contributions
Soham Sanjay More: Conceptualisation, methodology, evidence synthesis, MIAHPV framework
development, writing (original draft and all revisions).
Artiﬁcial Intelligence Use Statement
No AI writing tools were used in the drafting, revision, or editing of this manuscript. AI tools were not
used in study selection, data extraction, or MIAHPV framework development. Reference management
and literature search tools were used in accordance with standard research practice.
OSF Registration
Page 18/24

As PROSPERO does not accept scoping review registrations, the scoping review protocol was registered
retrospectively on the Open Science Framework prior to manuscript submission (OSF Registration:
https://osf.io/bk3hv), in accordance with JBI and PRISMA-ScR guidance for scoping reviews.
References
1. Segal R, Pilote L (2006) Warfarin interaction with Matricaria chamomilla. CMAJ 174(9):1281–1282
2. Kongkaew C, Phan DTA, Janusorn P, Mongkhon P (2024) Estimating adverse events associated with
herbal medicines using pharmacovigilance databases: systematic review and meta-analysis. JMIR
Public Health Surveill 10:e63808
3. Pilipiec P, Liwicki M, Bota A (2022) Using machine learning for pharmacovigilance: a systematic
review. Pharmaceutics 14(2):266
4. Ekor M (2014) The growing use of herbal medicines: issues relating to adverse reactions and
challenges in monitoring safety. Front Pharmacol 4:177
5. Shaw D, Graeme L, Pierre D, Elizabeth W, Kelvin C (2012) Pharmacovigilance of herbal medicine. J
Ethnopharmacol 140(3):513–518
6. Elvir Lazo OL, White PF, Lee C et al (2024) Use of herbal medication in the perioperative period:
potential adverse drug interactions. J Clin Anesth 97:111518
7. Peltzer K, Pengpid S (2018) Herb-drug interaction among outpatients in South Africa. S Afr J Bot
114:268–272
8. Langlois-Klassen D, Kipp W, Jhangri GS, Rubaale T (2007) Use of traditional herbal medicine by AIDS
patients in Kabarole District, western Uganda. Am J Trop Med Hyg 77(4):757–763
9. World Health Organization (2004) WHO Guidelines on Safety Monitoring of Herbal Medicines in
Pharmacovigilance Systems. WHO, Geneva
10. Skalli S, Caro-Rojas A, Rostom H et al (2024) A framework for promoting safety monitoring of herbal
medicines: the International Society of Pharmacovigilance Special Interest Group on Herbal and
Traditional Medicines. Drug Saf 47:515–520
11. Tricco AC, Lillie E, Zarin W et al (2018) PRISMA extension for scoping reviews (PRISMA-ScR):
checklist and explanation. Ann Intern Med 169(7):467–473
12. Peters MDJ, Godfrey C, McInerney P et al (2020) Scoping reviews. In: Aromataris E, Munn Z (eds)
JBI Manual for Evidence Synthesis. JBI
13. Dimitsaki S, Natsiavas P, Jaulent MC (2024) Applying AI to structured real-world data for
pharmacovigilance purposes: scoping review. J Med Internet Res 26:e57824
14. Warner J, Prada Jardim A, Albera C (2025) Artiﬁcial intelligence: applications in pharmacovigilance
signal management. Pharm Med 39(3):183–198
15. Borrelli F, Izzo AA (2009) Herb-drug interactions with St John's Wort (Hypericum perforatum): an
update on clinical observations. AAPS J 11(4):710–727
Page 19/24

16. Teschke R, Wolff A, Frenzel C, Schwarzenboeck A, Schulze J, Eickhoff A (2014) Drug and herb
induced liver injury: council for international organizations of medical sciences scale for causality
assessment. World J Hepatol 6(1):17–32
17. Choudhury A, Singh PA, Bajwa N, Dash S, Bisht P (2023) Pharmacovigilance of herbal medicines:
concerns and future prospects. J Ethnopharmacol 306:116177
18. Alghamdi W, Al-Fadel N, Alghamdi EA et al (2023) Signal detection and assessment of herb-drug
interactions: Saudi Food and Drug Authority experience. Drugs Real World Outcomes 10:577–585
19. Nagar A, Patel R, Shah K (2025) Artiﬁcial intelligence in pharmacovigilance: advancing drug safety
monitoring and regulatory integration. Ther Adv Drug Saf 16:20420986251361435
20. Brand JS, Gauﬃn O, Sartori D, Fusaroli M, Sköld H, Bergvall T et al VigiBase: Resource Proﬁle Update
with a Summary of Global Patterns and Trends in Adverse Event Reports for Medicines and
Vaccines. Drug Saf 2026 Jan 30. 10.1007/s40264-025-01642-6. Epub ahead of print.
21. Wei J, Dai J, Sun Y, Meng Z, Ma H, Zhou Y, TIRPnet (2024) Risk prediction of traditional Chinese
medicine ingredients based on a deep neural network. J Ethnopharmacol 325:117860
22. Fan Y, Zhou S, Li Y, Zhang R (2021) Deep learning approaches for extracting adverse events and
indications of dietary supplements from clinical text. J Am Med Inf Assoc 28(3):569–577
23. Wang Y, Zhao Y, Schutte D, Bian J, Zhang R (2021) Deep learning models in detection of dietary
supplement adverse event signals from Twitter. JAMIA Open 4(4):ooab081
24. Fan Y, Zhang R (2018) Using natural language processing methods to classify use status of dietary
supplements in clinical notes. BMC Med Inf Decis Mak 18(Suppl 2):51
25. Wang Y, Gunashekar DR, Adam TJ, Zhang R (2017) Mining adverse events of dietary supplements
from product labels by topic modeling. Stud Health Technol Inf 245:614–618
26. Sharma V, Sarkar IN (2018) Identifying natural health product and dietary supplement information
within adverse event reporting systems. Pac Symp Biocomput 23:268–279
27. Dilán-Pantojas IO, Boonchalermvichien T, Taneja SB, Li X, Chapin MR, Karcher S, Boyce RD (2024)
Broadening the capture of natural products mentioned in FAERS using fuzzy string-matching and a
Siamese neural network. Sci Rep 14(1):1272
Figures
Page 20/24

Figure 1
PRISMA-ScR ﬂow diagram showing identiﬁcation, screening, and inclusion of sources for this scoping
review. Grey literature search (general web search and regulatory agency websites) is reported narratively in
Section 3.1.
Page 21/24

Figure 2
Three structural failure modes underlying poor AI-readiness in herbal product individual case safety reports
(ICSRs): nomenclature fragmentation, mixture attribution failure, and systematic underreporting via over-
the-counter invisibility.
Page 22/24

Figure 3
The MIAHPV framework: seven criteria for AI-readiness of herbal product ICSRs, classiﬁed as
Discriminating (essential for correct attribution to the herbal product; Criteria 1, 2, 5) or Threshold (minimum
data quality needed for analytical validity; Criteria 3, 4, 6, 7).
Figure 4
Page 23/24

MIAHPV three-tier AI-readiness classiﬁcation of herbal product ICSRs. Tier proportions (10-20% / 40-50% /
30-45%) are illustrative estimates inferred from the included literature and have not been empirically
measured by direct database application.
Supplementary Files
This is a list of supplementary ﬁles associated with this preprint. Click to download.
SupplementaryTablesS1MIAHPV.docx
PRISMAScRChecklistMIAHPVv2.docx
Page 24/24
