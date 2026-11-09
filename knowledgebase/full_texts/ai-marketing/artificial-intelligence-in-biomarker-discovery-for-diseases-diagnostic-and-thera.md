---
title: 'Artificial intelligence in biomarker discovery for diseases: diagnostic and therapeutic prospects.'
url: https://doi.org/10.1038/s41392-026-02946-4
category: ai-marketing
subcategory: empirical
date: 2026-01
venue: MED
authors:
- Dinc R
- Ardic N
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41392-026-02946-4.pdf
pages: 33
chars: 218623
fetched_at: '2026-11-08T20:01:32+00:00'
kb_version: 1
---

# Artificial intelligence in biomarker discovery for diseases: diagnostic and therapeutic prospects.

REVIEW ARTICLE OPEN
Artiﬁcial intelligence in biomarker discovery for diseases:
diagnostic and therapeutic prospects
Rasit Dinc 1 and Nurittin Ardic 2
Biomarkers are central to modern diagnostics and therapeutics, yet traditional discovery approaches suffer from single-modality
analyses, weak mechanistic foundations, and low reproducibility. Arti ﬁcial intelligence (AI) enables the integration of complex
multimodal biomedical data, but the translation of AI-derived biomarkers into clinical applications remains inconsistent. This review
examines how AI reshapes biomarker discovery across diseases, focusing on biological mechanisms, validation requirements, and
therapeutic integration. We synthesize evidence across molecular, cellular, imaging, and digital biomarker approaches, evaluating
AI methodologies including classical machine learning, deep learning, graph-based models, foundation models, and causal
inference. Findings are organized using a pipeline framework encompassing discovery, external validation, robustness testing,
clinical utility, and deployment. AI enables identi ﬁcation of multiscale signatures re ﬂecting cellular programs, tissue remodeling,
and disease trajectories. However, many biomarkers fail external validation. Biologically grounded approaches using network-based
modeling, spatial pro ﬁling, and mechanistic constraints improve interpretability and therapeutic relevance in oncology,
cardiovascular disease, neurodegeneration, and metabolic diseases. Validation frameworks with decision curve analysis and
prospective evaluation are necessary to demonstrate clinical utility beyond predictive accuracy. AI ’s impact will depend on
integration into rigorous validation and therapeutic pathways. By transitioning from correlational pattern recognition to
mechanistically informed, clinically evaluated systems, AI can support next-generation precision diagnostics and targeted
interventions.
Signal Transduction and Targeted Therapy          (2026) 11:407 ; https://doi.org/10.1038/s41392-026-02946-4
INTRODUCTION
Biomarkers form the foundation of precision medicine by de ﬁning
how diseases are detected, classi ﬁed, and treated.1 Yet the transfer
of candidate biomarkers to clinical practice is disproportionately
limited compared to their discovery output. Most biomarkers
show promising performance in initial studies but are not
reproducible in independent cohorts, degrade under real-world
heterogeneity, or prove insuf ﬁcient to change clinical decisions.
This persistent implementation gap re ﬂects weaknesses in
validation processes rather than technological capability. This is
a challenge repeatedly highlighted in translational biomarker
research.2 Reproducibility remains a central challenge in biomar-
ker development, as measured signals are susceptible to cohort-
speciﬁc effects, pre-analytical variability, platform drift, batch
effects, and confounding factors related to concomitant diseases
and treatment. High-dimensional feature domains further increase
the risk of over ﬁtting when sample sizes are modest and analytical
ﬂexibility is high. 3–5 Even when biomarker performance appears
strong, evaluation often relies on discrimination measures such as
the area under the curve (AUC) without demonstrating whether
the biomarker actually improves patient management or out-
comes. This highlights the distinction between statistical perfor-
mance and clinical bene ﬁt.6 Many clinical contexts demonstrate
that incremental gains in statistical performance have a negligible
impact on actual clinical decisions, especially when baseline
performance is strong, or work ﬂow constraints limit
implementation.7,8 These limitations reveal that successful bio-
marker translation requires much more than discovery. It demands
rigorously validated development processes, transparent report-
ing, and documented clinical bene ﬁt. Similar concerns have been
emphasized in previous assessments of biomarker development
and translation. 9 These requirements become even more critical
when arti ﬁcial intelligence (AI) methods are applied to complex,
high-dimensional datasets.
Biomarker discovery now occurs within an exponentially
expanding ecosystem of measurement. Contemporary studies
integrate genomic and epigenomic variation, bulk and unicellular
transcriptomics, proteomics and post-translational modi ﬁcations,
metabolomics, circulating nucleic acids, extracellular vesicle
content, quantitative imaging features, and longitudinal digital
phenotypes derived from wearable sensors and electronic health
records.10–14 This diversity re ﬂects an evolving understanding of
disease biology, as most disorders arise not from isolated
molecular abnormalities but from disruptions distributed across
signaling pathways, cellular states, tissue microenvironments, and
systemic host responses. Consequently, modern biomarker
research faces numerous statistical and biological challenges,
including high dimensionality relative to sample size, complex
confounding relationships, heterogeneity among real-world
populations, inter-regional protocol and device variability, and
temporal changes that can alter biological relationships over time.
Traditional statistical approaches remain indispensable for
Received: 9 February 2026 Accepted: 3 July 2026
1INVAMED Medical Innovation Institute, New York, NY, USA and 2Med-International UK Health Agency Ltd., Warwickshire, UK
Correspondence: Rasit Dinc (rasitdinc@hotmail.com)
www.nature.com/sigtransSignal Transduction and Targeted Therapy
© The Author(s) 2026
1234567890();,:

inference, but they are often inadequate for large-scale repre-
sentation learning and multimodal data integration. AI, particularly
deep learning, has demonstrated the ability to learn hierarchical
representations from complex biomedical inputs and holds great
promise, especially in imaging and multimodal clinical datasets. 15
However, increasingly rich datasets also create new opportunities
for bias and error. Region-speci ﬁc signatures, hidden confounding
factors, and label leakage can produce seemingly accurate models
that fail when evaluated in independent cohorts or real-world
settings.16 Similarly, models can learn super ﬁcial correlations that
provide strong predictive performance during development but
lack biological relevance and robustness. This contrast between
unprecedented opportunities for biomarker discovery and the
increasing risk of erroneous ﬁndings represents a central
challenge in contemporary biomarker science. Accordingly,
successful translation depends not only on predictive perfor-
mance but also on rigorous validation, mechanistic interpretation,
and demonstration of reproducible biological relevance.
AI is reshaping the entire biomarker development lifecycle. In
the discovery phase, machine learning enables scalable feature
screening and multivariate signature generation. 17–19 Whereas
deep neural networks learn direct representations from raw data
such as images, molecular pro ﬁles, and longitudinal measure-
ments, capturing complex distributed biological signals missed by
univariate approaches. 20,21 In the validation phase, the key
challenge is demonstrating robustness, transparency, and general-
izability across diverse cohorts and real-world settings. AI-based
biomarkers require explicit speci ﬁcation of cohort de ﬁnition,
endpoint labeling, preprocessing decisions, handling of missing
data, model development choices, and evaluation protocols. 22,23
The fact that a lack of transparency weakens reproducibility has
led to the development of AI-speci ﬁc reporting frameworks and
bias assessment tools. In the clinical utility phase, biomarkers
should demonstrate incremental decision value according to
established work ﬂows, quanti ﬁed through decision analytics that
translate predictions into actual patient outcomes. This require-
ment is particularly important in settings where modifying existing
tools is impractical and incremental value needs to be precisely
deﬁned by the decision point and patient subgroup. At the
therapeutic stage, an important objective is to move beyond
prediction toward biological interpretation. 24,25 AI-derived bio-
markers are increasingly being used to support pathway analysis,
target identi ﬁcation, patient classi ﬁcation, trial enrichment, and
treatment optimization. Foundation models trained on large-scale
biological data point to more transferable and mechanistically
meaningful representations of molecular function. However,
realizing this promise requires careful separation of correlational
signatures from causal or actionable mechanisms through
biological validation and orthogonal experiments.
This review presents a mechanism-centric, clinically applied
framework for AI-assisted biomarker discovery and adoption in
disease domains. Rather than cataloging studies or algorithms, we
focus on the principles that determine whether AI-derived
biomarkers pass external validation tests, support biological
interpretation, and provide clinical and therapeutic value. We
organize the discussion according to major biomarker data types,
including molecular and cellular measurements, circulating
analytes, imaging phenotypes, and digital biomarkers. These
types differ in terms of sources of variability, susceptibility to
confounding factors, and capacity to support mechanistic inter-
pretation. By mapping AI methods to these biological realities, we
separate prediction performance from biologically grounded
evidence and highlight common modes of failure. We propose
an operational development pipeline (including study design,
harmonization, leakage prevention, robustness testing, and
biological validation) aligned with contemporary reporting stan-
dards and bias assessment frameworks for AI prediction models.
The fundamental contribution of this work is to advance AI-
assisted biomarker discovery toward the ﬁeld of reproducible,
mechanistically based precision medicine by integrating plausi-
bility and therapeutic actionability within a uni ﬁed evidence
framework. We synthesize representative literature encompassing
biomarker validation, AI, systems biology, and translational
medicine, with particular emphasis on studies published in the
last decade and landmark research shaping current practices. The
review is deliberately selective rather than comprehensive,
focusing on conceptual integration between biomarker modal-
ities, AI methodologies, biological interpretation, validation
requirements, and therapeutic relevance.
To provide an overview of how data modalities, AI modeling,
validation, and clinical adoption interact throughout the biomar-
ker lifecycle, Fig. 1 summarizes a generalized AI-enabled
biomarker discovery and deployment pipeline.
BIOMARKER MODELS AND BIOLOGICAL PRINCIPLES (INTER-
DISEASE RELATIONSHIPS)
Molecular biomarkers: genomics/epigenomics, transcriptomics,
proteomics/posttranslational modi ﬁcations, metabolomics/
lipidomics
Molecular biomarkers remain the most mature and widely used
class of biomarkers, providing a mechanistic basis for disease
stratiﬁcation and therapeutic targeting. Genomic variation can ﬁx
disease risk and subtype de ﬁnition, while epigenomic regulation
captures dynamic gene control states shaped by development,
environment, and disease activity. 26–28 In many disorders,
particularly cancer, immune-mediated diseases, cardiometabolic
syndromes, and neurodegeneration, single-layer biomarkers are
increasingly insuf ﬁcient to explain phenotypic heterogeneity. This
situation encourages the development of multi-omics strategies
that integrate molecular layers into coherent biological narratives.
Among molecular modalities, small molecule metabolites and
lipid species provide a sensitive indicator of integrated physiology.
This reﬂects pathway ﬂux, organ crosstalk, in ﬂammatory state, and
exposure history. 29,30 Recent syntheses highlight how metabolite
biomarkers can support diagnosis, prognosis, and therapeutic
target discovery. However, these syntheses also highlight recur-
ring pitfalls such as cohort effects, platform shift, diet/drug-
induced confounding, and limited external validation in clinically
realistic settings. 31–33 Recent multi-omics studies continue to
demonstrate the value of integrated molecular signatures for
biomarker discovery and disease strati ﬁcation.34,35
Transcriptomic biomarkers are increasingly extending beyond
bulk expression pro ﬁles toward spatially resolved and single-cell
readouts, enhancing biological interpretability while preserving
tissue architecture and cell state context. For example, in brain
disorders, recent reviews highlight how single-cell and spatial
transcriptomics can link disease phenotypes to cell-type-speci ﬁc
programs and spatial microenvironments; this approach can be
generalized to oncology, in ﬂammatory diseases, and cardiometa-
bolic organs. 26,27,36
Proteomic biomarkers remain extremely relevant because
proteins and post-translational modi ﬁcations are closer to signal
execution than DNA or RNA. However, they present signi ﬁcant
analytical complexity and reproducibility challenges. 37 Even if
molecular signatures are statistically robust, their real-world
implementation depends on biological plausibility and clinical
utility rather than solely on discrimination metrics. Therefore,
mechanistic ﬁxation (pathways, cell programs) and orthogonal
validation (independent platforms, targeted assays) are essential.
Cellular and immune biomarkers: immune repertoires, single-cell
states, cytokine programs, and NETs
Cellular biomarkers re ﬂect a shift from “single-molecule-derived
causality” to disordered cellular states and tissue ecosystems.
Single-cell pro ﬁling enables the separation of immune activation,
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
2
Signal Transduction and Targeted Therapy          (2026) 11:407

depletion, lineage shifts, and in ﬂammatory programs that often
cut across classical diagnostic categories. 38–40 Spatial technologies
further preserve tissue context, which is critical where pathology is
dependent on cellular neighborhoods, barrier interfaces, micro-
vascular niches, or tumor-immune geography. 36,41,42 As the
technology landscape evolves rapidly, recent studies have focused
on mapping the practical capabilities and limitations of commer-
cial single-cell and spatial platforms, providing a useful basis for
selecting methods that ﬁt the biological question and current
tissue constraints. 43–45 Recent reviews also synthesize spatially
resolved single-cell omics methods, highlighting how computa-
tional integration and standardization gaps shape downstream
biomarker robustness and cross-center generalizability. 42,45–47
Immune repertoires provide quantitative signatures of adaptive
immune dynamics across infection, cancer, autoimmunity, and
transplantation.48 Whereas cytokine programs and innate immune
states serve as integral biomarkers of host response. Neutrophil
extracellular traps (NETs) are a concrete example of the cross-
disease in ﬂammatory biomarker axis: they associate innate
immune activation with vascular injury, thrombosis, and tissue
damage, and carry clear therapeutic implications in the context of
systemic autoimmune and autoin ﬂammatory diseases. 49,50
A recurring principle is that “cellular biomarkers ” are rarely
stable scalar variables. They are compositional, state-dependent,
and context-sensitive. 51 Therefore, translational robustness
requires careful separation of the biological signal from technical
variation (partition effects, dissociation artifacts, antibody panels,
spatial resolution constraints) and explicit linking of biomarker
patterns to cellular programs and mechanisms, rather than
narratives of post hoc interpretation. The diversity of biological
information captured by modern biomarker platforms necessitates
a systematic classi ﬁcation of data modalities.
Because biomarkers are measurements of biological systems at
molecular, cellular, tissue, and behavioral scales, AI discovery
strategies must address the characteristics, constraints, and
dominant noise sources of each data type. Accordingly, Fig. 2
summarizes the major biomarker classes and data sources used
for AI-assisted biomarker discovery, encompassing molecular,
cellular/immune, circulating, imaging, extracellular vesicle, and
digital domains.
CIRCULATING BIOMARKERS: CFDNA/CFRNA, CIRCULATING
PROTEINS/METABOLITES, LIQUID BIOPSY PARADIGMS
Circulating biomarkers provide minimally invasive access to
disease biology and are particularly valuable for longitudinal
monitoring. Cell-free DNA (cfDNA) or RNA (cfRNA) and circulating
tumor DNA (ctDNA) exemplify classes of biomarkers that can
Fig. 1 AI-enabled biomarker discovery pipeline. Schematic overview of an integrated biomarker development work ﬂow encompassing four
interconnected phases: Discovery (data-driven candidate identi ﬁcation through multi-omics scanning, feature extraction, and pattern
recognition), Validation (external cohort testing, TRIPOD + AI compatibility, and systematic bias assessment), Clinical utility (decision curve
analysis, net bene ﬁt quanti ﬁcation, and work ﬂow integration), and Therapeutic integration (accompanying diagnostic development, trial
enrichment strategies, and response monitoring). A central AI core utilizes deep learning, foundation models, and multimodal data integration to
enhance each phase. Data inputs cover six main biomarker methods: genomics/epigenomics, proteomics/metabolomics, single-cell/spatial
proﬁling, imaging/radiomics, extracellular vesicles/liquid biopsy, and digital/wearable sensors. Iterative re ﬁnement cycles (curved arrow) ensure
continuous improvement of the model based on clinical feedback. Figure created by the authors using Adobe Illustrator (Version 29.3.1)
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
3
Signal Transduction and Targeted Therapy          (2026) 11:407

support early detection strategies, residual disease monitoring,
response assessment, and clonal evolution tracking. 52–55 Yet their
clinical value largely depends on pre-analytical processing,
analytical sensitivity, and clinical context (tumor burden, shedding
rates, treatment timing), all of which affect the stability of the
derived biomarkers. Recent syntheses highlight the current status,
advantages, and limitations of liquid biopsy across tumors,
emphasizing both clinical opportunities (early diagnosis, dynamic
monitoring) and translational bottlenecks (standardization, false
positives, access, and evidence quality). 56–58 Emerging studies on
minimal residual disease monitoring further support the clinical
value of liquid biopsy approaches in longitudinal cancer
management.59–61
In non-oncological diseases, circulating proteins and metabo-
lites remain clinically dominant due to assay maturity and
implementation feasibility, but they often re ﬂect downstream
physiology rather than proximate causal mechanisms. 31,62–64 This
creates a predictable mode of failure: biomarker performance
appears promising in selected cohorts, but generalization is poor
when concomitant diseases, drugs, and spectrum effects disrupt
baseline distributions. Cross-mode integration (e.g., pairing
circulating signals with imaging or tissue-derived molecular states)
can improve biological interpretability and stability if validation is
rigorous and leakage is avoided.
Extracellular vesicles/exosomes as biomarker carriers
Extracellular vesicles (EVs), including exosomes and microvesicles,
offer a biologically attractive biomarker model because they carry
a multimolecular payload re ﬂecting cellular status and intercellular
communication. Therefore, EV biomarkers are located at the
intersection of molecular and cellular biomarkers: they can capture
cell-of-origin signals while encoding systemic communication
programs.10,65
Yet the conversion of EVs into biomarkers remains constrained
by heterogeneity in isolation methods, co-isolated contaminants
(including lipoproteins), variable quanti ﬁcation standards, and a
lack of consensus among laboratories. 66 A signi ﬁcant recent
development is the updated consensus guideline MISEV2023 from
the International Society for Extracellular Vesicles (IESV), which
expands minimum information standards from basic to advanced
approaches and explicitly addresses expectations of methodolo-
gical diversity and reproducibility. 67,68
For AI-assisted discovery, EVs are a high-opportunity but high-
risk method: the signal is rich and multilayered, yet the feature
domain is highly sensitive to pre-analytical variation. 69–71 This
makes EV biomarkers a strong test case for the validation ladder,
speciﬁcally external replication, stability analyses, and biologically
grounded validation. Recent AI-assisted studies have further
revealed the diagnostic potential of extracellular vesicle-derived
markers in multiple tumor types. 72
Imaging biomarkers: radiomics, functional imaging, quantitative
imaging processes
Imaging biomarkers enable non-invasive phenotyping of tissue
structure and function at the organ scale. They can encode
clinically relevant heterogeneity (e.g., ﬁbrosis architecture, vascular
Fig. 2 Biomarker modalities and data sources. Overview of six major biomarker domains used in AI-assisted biomarker discovery, including
molecular, cellular/immune, circulating, imaging, extracellular vesicle, and digital biomarkers. Representative analytical methods and biolo gical
information captured by each modality are summarized. Figure created by the authors using Adobe Illustrator (Version 29.3.1). RNA-seq RNA
sequencing, PTM post-translational modi ﬁcation, TCR T cell receptor, BCR B cell receptor, NETs neutrophil extracellular traps, ctDNA circulating
tumor DNA, CT computed tomography, MRI magnetic resonance imaging, PET positron emission tomography, H&E hematoxylin and eosin, EV
extracellular vesicle, MISEV Minimal Information for Studies of Extracellular Vesicles
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
4
Signal Transduction and Targeted Therapy          (2026) 11:407

remodeling, metabolic activity, lesion tissue, and spatial distribu-
tion) and often capture biological variation that correlates with
molecular status and prognosis. Radiomics and computational
imaging methods systematize this quanti ﬁcation, but real-world
implementation requires tight control of scanner variability,
acquisition protocols, segmentation procedures, and inter-site
harmonization.12–14
A signiﬁcant recent development is the emergence of “founda-
tion model-ready ” imaging biomarker discovery: self-supervised
models pre-trained on large imaging datasets can learn transfer-
able feature representations and then be adapted to speci ﬁc
biomarker tasks. Similar advances have been reported in digital
pathology and multimodal imaging foundation models. These
further expand the translational potential of imaging biomar-
kers.73–75 In a representative study, Pai et al. published their work
developing a foundational model for the discovery of cancer
imaging biomarkers. 76 By evaluating this across clinically relevant
applications, they demonstrated how representation learning can
enable more generalizable imaging biomarker processes.
At the same time, recent critical reviews on precision oncology
highlight that large-scale validation remains the limiting step for
radiomic biomarkers, particularly in high-risk contexts such as
immunotherapy response prediction. 77 These analyses reinforce
the core theme of this review: imaging biomarkers are successful
only when supported by biological anchoring and prospective
evidence, not merely retrospective discrimination.
Digital biomarkers: wearable devices, passive sensing, digital
phenotypes and linkage to outcomes
Digital biomarkers are derived from continuous or high-frequency
data streams generated by wearable devices, smartphones, and
ambient sensors. These methods extend biomarker science
beyond molecular analyses to computational physiology and
behavioral phenotyping. Eventually, they enable longitudinal
monitoring of sleep, mobility, autonomic physiology, and symp-
tom dynamics. Their translational appeal lies in their scalability
and temporal resolution, particularly for chronic disease monitor-
ing and early deviation detection. 78–80 Recent wearable device
research continues to expand the scope of digital biomarkers for
physiological monitoring and disease prediction. 81,82
Yet the concept of “digital biomarkers” remains heterogeneous.
A recent systematic mapping of the biomedical literature reveals
signiﬁcant differences in how the term is de ﬁned, with direct
implications for study design, validation, and clinical bene ﬁt
claims.83 This descriptive fragmentation interacts with real-world
technical challenges such as device heterogeneity, incomplete-
ness, behavioral confounding, and socioeconomic bias. This
necessitates careful endpoint alignment and validation. Digital
biomarkers become most defensible when matched with inter-
pretable physiological constructs or functionally meaningful
outcomes, and when their reliability is demonstrated under
realistic application conditions rather than controlled research
settings.
The “Biological plausibility ” framework: distinguishing causal,
mechanistic, and correlational biomarkers
Across all biomarker modalities, biological plausibility is the
gatekeeper of translation. Many biomarkers are predictive correla-
tions that track disease burden without participating in disease
mechanisms. Such biomarkers can still be clinically useful (e.g., risk
stratiﬁcation), but they often fail as therapeutic guidelines or
surrogate endpoints when mechanistic assumptions are overstated.
A practical plausibility framework emphasizes several dimensions:
consistency across cohorts and platforms; temporal alignment with
disease progression; dose-response behavior; speciﬁcity to biologi-
cal processes rather than technical artifacts; and consistency with
known pathways, cell programs, and tissue context. Stronger
mechanistic support comes from genetic linkage, perturbation
evidence, spatial localization of the signal, and longitudinal
dynamics that match causal hypotheses. This framework sets the
groundwork for later sections on mechanistic AI. The aim here is not
only to predict outcomes but also to map biomarker signatures to
pathways and actionable therapeutic hypotheses.
To illustrate how different classes of biomarkers contribute to
AI-assisted discovery and application, Table 1 summarizes the
major types of biomarkers according to their biological scale,
technical characteristics, commonly applied AI methods, and
current application maturity stages.
Collectively, these biomarker classes operate at distinct
biological scales and exhibit signi ﬁcant differences in analytical
Table 1. Biomarker models and translational properties
Biomarker
modality
Typical data sources Biological level Strengths Key limitations AI methods commonly
used
Translation
maturity
Genomics/
epigenomics
WGS, SNP sequences,
methylation pro ﬁles
Germline/
regulatory
Stable, causal
inference, lifetime
risk
Limited dynamic
monitoring, modest
effect sizes
Regularized models,
GNNs, polygenic
modeling
High (risk
prediction)
Transcriptomics
(bulk/scRNA)
Blood, tissue biopsies Cellular
programs
Pathway-level
insight, immune
status
Batch effects, tissue
access, cost
Clustering, VAEs,
graph models
Medium
Proteomics/
metabolomics
Plasma, CSF, tissue Functional
molecular
activity
Proximal to
phenotype,
druggable pathways
Technical variability,
platform dependence
Tree ensembles,
representation
learning
Medium
ctDNA/liquid
biopsy
Plasma cfDNA, RNA Tumor-derived
signals
Minimal residual
disease, mutation
tracking
Low abundancy, test
sensitivity
Deep sequencing ML,
Bayesian models
High
(oncology)
Imaging
radiomics
MRI, CT, PET Organ and tissue
structure/
function
Spatial context,
longitudinal tracking
Scanner heterogeneity,
interpretability
CNNs, vision
transformers
High
Extracellular
vesicles
Plasma, urine, CSF Intercellular
signaling
Mechanistic
signaling insight
Isolation standards, low
throughput
Feature learning,
multi-omics fusion
Low-
medium
Digital
biomarkers
Wearable devices,
smartphones, electronic health
record streams
Behavioral/
physiological
Continuous
monitoring, scalable
Adherence bias, device
variability
Time series models, DL Medium
Key references for this table: refs. 25,67,147,170,278–280
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
5
Signal Transduction and Targeted Therapy          (2026) 11:407

stability, mechanistic interpretability, and clinical scalability. The
comparison also underscores the need for multimodal integration
strategies discussed in Sections “Artiﬁcial intelligence methods for
biomarker discovery” and “Mechanistic AI: mapping biomarkers to
pathways, targets, and therapeutic hypotheses ”, highlighting that
no single biomarker approach is suf ﬁcient to capture complex
disease biology. It also emphasizes that translational readiness
varies considerably among biomarker classes. As will be discussed
in the following section, these modality-speci ﬁc constraints
directly shape the selection and performance of AI methods.
ARTIFICIAL INTELLIGENCE METHODS FOR BIOMARKER
DISCOVERY
Classical machine learning for high-dimensional biomarker data
Many biomarker discovery settings remain fundamentally “small-
n, large-p settings where the number of variables being measured
can far exceed the number of subjects. In this regime, classical
machine learning (ML) methods such as regularized regression,
support vector machines (SVM), tree ensembles, and sparse
feature selection retain their practical value because they provide
strong inductive bias and can be paired with stability analysis. 84,85
Their strengths are most evident when the scienti ﬁc aim is not
only prediction but also generating a suitable shortlist of
candidates for orthogonal validation. However, these same
environments are quite vulnerable to optimistic predictions driven
by leakage, repeated tuning, and selection on outcome. This
means a strict training/validation separation and nested evalua-
tion are essential. 85
A second limitation is interpretability in ﬂation. Feature sig-
niﬁcance or coef ﬁcient magnitude is often treated as biologically
grounded evidence, even if related features are interchangeable
and the learned signature is not unique. In high-dimensional
biology, “explanations” can be unstable unless supported by
stability based on resampling, external replication, and alignment
with path structure.
Deep representation learning and self-supervised learning for
omic and single-cell data
Deep learning (DL) is most advantageous when biomarker signals
are distributed and nonlinear, or when inputs are not naturally
tabular (e.g., arrays, images, graphs). A signi ﬁcant advance is the
shift towards representation learning, where models learn
reusable embedding vectors that capture biological structure
and can be adapted to downstream tasks with limited labels. 86,87
In single-cell genomics, self-supervised learning (SSL) has emerged
as a prime way to leverage large unlabeled datasets, but its
beneﬁts are not homogeneous across tasks. Benchmark-focused
analyses highlight that SSL is most helpful when transfer is
required across batches, tissues, or experimental settings and
downstream task labeling is limited. 88
The practical implication for biomarker discovery is that SSL
should not be framed as a universal upgrade. Its value depends on
whether the pre-training objectives align with biological invar-
iances, whether the batch structure dominates the embedding
space, and whether the learned representations improve general-
ization rather than merely compressing technical variation. 88
When used appropriately, representation learning can support
both prediction and discovery by enabling downstream probe of
latent dimensions and stabilizing models trained on limited
cohorts.
Multimodal learning in omics, imaging, and clinical data
Clinical biomarkers rarely exist in isolation. They are interpreted in
conjunction with imaging, lab values, longitudinal clinical courses,
and often text-derived context. Multimodal ML aims to formalize
this integration, learning complementary information across data
types while avoiding the pitfalls of naïve concatenation. 89–91
Modern multimodal pipelines are often de ﬁned in terms of
merging strategies (early, mid, or late merging), and this choice
greatly in ﬂuences the tolerance for missing data and whether
cross-modal interactions can be learned. 92
A particularly important model in biomarker discovery is
transfer learning across modalities, where large observational
EHR-scale datasets are used to pre-train components that are
then transferred to smaller cohorts with paired omics and
clinical data. 33,93 This approach directly addresses the power
limitation of omics studies and can improve both prediction and
biological insight when implemented with careful cohort
separation and robust evaluation. 94 The broader lesson is that
multimodal models should be designed around realistic clinical
data availability (partial moda lity coverage, asynchronous
sampling, and variable quality) rather than idealized assump-
tions of complete cases. 92
Graph neural networks and knowledge-guided learning
Many biomarker-relevant relationships are naturally relational,
including protein-protein interactions, regulatory networks, cell-
cell communication, pathway graphs, and multimodal linkages
between genes, variants, drugs, and phenotypes. Graph neural
networks (GNNs) enable learning on such non-Euclidean struc-
tures and have rapidly expanded across single-cell tasks, including
imputation, batch correction, cell typing, spatial domain detection,
and network inference. 71,95,96 Their most important advantage for
biomarker discovery is their ability to add structural priors, which
can constrain the hypothesis space and increase robustness in
limited sample sizes. 97
A parallel direction is mechanism-aware architectures that
explicitly encode signal or pathway structure to encourage
biologically plausible computation. Methods such as GNNs have
been proposed to model perturbation biology by constraining
the ﬂow of information through structured interaction graphs
and pairing them with explanatory modules aimed at localizing
the graph substructures responsible for predictions. 98 These
approaches are particularly attractive for target discovery and
therapeutic classi ﬁcation because they can align predictable
features in interpretable ways, but still require rigorous
validation to ensure that interpr etability is not an afterthought
narrative.
Foundation and large-scale pre-training in genomics and
biomedicine
Foundation models trained on large biological datasets are
beginning to reshape biomarker discovery by providing transfer-
able representations across tasks and domains. In genomics, DNA
“language models ” trained with self-supervised targets can learn
sequence representations, improving downstream prediction of
molecular phenotypes and variant effects, and supporting
biomarker processes starting from sequence-level function. 99,100
This class of models is rapidly evolving, and reviews now
categorize foundation models across genomics, transcriptomics,
proteomics, drug discovery, and single-cell analysis. The reviews
also highlight both opportunities and unresolved limitations of
these models in evaluation and interpretability. 46,101 These
developments support the emerging concept of a biological
“language of life ” that can be learned through large-scale
foundational models. 102
In practice, foundation models change biomarker work ﬂows in
two ways. 103–106 First, they can reduce reliance on task-speci ﬁc
labeled datasets by enabling ﬁne-tuning or adaptation with
limited supervision. Secondly, they encourage a shift from
handcrafted features toward learned representations, which can
improve generalization ability but also increase the need for
auditing: pre-training corpora can encode batch, ancestry, or site
signals that later appear as “biomarkers” unless explicitly
controlled.
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
6
Signal Transduction and Targeted Therapy          (2026) 11:407

Generative and simulation-assisted approaches for biomarker
mechanism and target discovery
Beyond prediction, generative modeling offers a pathway
toward biologically grounded hypothesis generation. In biomar-
ker discovery, generative models can be used to simulate
counterfactual molecular states, predict perturbation responses,
or suggest molecular patterns consistent with observed pheno-
types.107 T h em o s tc r e d i b l eu s e sa r et h o s et i e dt op e r t u r b a t i o n
datasets, causal structure, or explicit biological constraints, as
unrestricted generation can produce outputs that seem plau-
s i b l eb u ta r en o ts c i e n t iﬁcally grounded. In perturbation biology,
mechanism-guided graphical models demonstrate how gen-
erative or predictive learning can be anchored to curated
biological structure and experimental perturbations, providing a
more testable bridge between signatures and actionable
pathways. 98
Generative and simulation-assisted outputs should therefore be
interpreted as hypothesis-generating rather than evidentiary by
default. Within the validation ladder proposed in this review, such
models primarily contribute at the discovery stage by proposing
candidate signatures, latent structures, pathway hypotheses, or
putative mechanisms. Moving beyond this stage requires ortho-
gonal conﬁrmation: Level 1 requires internal analytical consistency
and protection against leakage or memorization; Level 2 requires
external replication across independent datasets or sites; Level 3
requires robustness testing under perturbation, subgroup shift, or
alternative preprocessing pipelines; and advancement toward
Levels 4 and 5 requires demonstrating that the generated
hypothesis improves clinically meaningful decisions rather than
merely producing biologically plausible outcomes. Within this
framework, generative AI functions as a discovery engine, whereas
predictive AI more directly supports risk estimation or classi ﬁca-
tion in downstream clinical work ﬂows.98
To highlight which AI approaches have progressed from proof-
of-concept studies to real-world clinical work ﬂows, Table 2
summarizes representative biomarker-driven AI systems with
documented clinical deployment and/or regulatory clearance
across multiple disease domains.
Explainability, uncertainty, and the risk of “false mechanistic
comfort”
Explainability is essential in biomarker discovery because the
output is rarely a ﬁnal decision; it is a candidate hypothesis that
must be subject to biological validation. 108,109 However, explana-
tion methods can create false con ﬁdence if treated as mechanistic
evidence rather than diagnostic tools. Recent domain-focused
reviews highlight that post hoc explainability can be useful for
triage and auditing, but are sensitive to correlated features, model
unidentiﬁability, and dataset shift. These conditions are routinely
encountered in omics. 110,111 Bioinformatics-focused survey further
highlights the diversity of explainability techniques and the
frequent mismatch between explanation outputs and actionable
biological interpretation. 109 A practical principle is to treat
interpretability as evidence that must replicate: do the same
features/pathways appear under resampling, across cohorts,
across platforms, and under perturbation? Wherever possible,
explanations should be tested against orthogonal experiments
(e.g., CRISPR perturbation, proteomic validation, targeted assays)
rather than simply being reported.
Biomarker type and method selection as a translational objective
function
No single AI method is optimal among biomarker modalities.
Classical ML remains strong for small cohort tabular omics,
especially when interpretability and stability are prioritized. DL is
most justi ﬁed when inputs are high-dimensional and structured
(arrays, images, graphs) or when transfer learning and pre-training
are available. Multimodal learning becomes essential when clinical
action depends on the integration of heterogeneous streams of
evidence, and graph/information-guided learning is most valuable
when biological prior information can meaningfully constrain the
hypothesis space.
Table 2. AI methods with demonstrated clinical deployments in biomarker-based applications (representative examples)
Clinical use case (biomarker
function)
Input method/
“biomarker”
Dominant AI method Deployment context Regulatory/clinical
status
Representative
evidence (examples;
not exhaustive)
Autonomous diabetic
retinopathy screening (diagnosis/
triage biomarker)
Retinal fundus
photographs
CNN-based classi ﬁers Primary care/screening
settings (autonomous
operation)
FDA De Novo
clearance (IDx-DR)
281
Atrial ﬁbrillation detection from
wearable ECG (rhythm
biomarker)
Single-lead
wearable or clinical
ECG
Signal
processing + CNN
Consumer devices with
clinician con ﬁrmation
FDA-cleared ECG AF
detection algorithm
80
Large-vessel occlusion stroke
triage (imaging biomarker)
Head/neck CTA CNN-based
detection + workﬂow
prioritization
Emergency stroke
networks (alert routing)
FDA-cleared triage
software (e.g., Viz.ai)
282
Intracranial hemorrhage triage
(imaging biomarker)
Head NCCT CNN-based detection Emergency radiology
triage
FDA-cleared
notiﬁcation system
283
Prostate cancer detection
support (histopathological
biomarker)
Whole slide images
pathology image
(H&E)
CNN/vision
transformer
Pathologist assistive
diagnosis
FDA-cleared
assistive CAD tools
104
Early sepsis deterioration
prediction (physiological/EHR
biomarker)
EHR time-series
(vitals, labs)
Gradient boosting/
RNN
Inpatient clinical decision
support
Clinical deployment;
mixed regulatory
status
284
Low ejection fraction screening
from ECG (functional biomarker)
Standard 12-lead
ECG
CNN-based
phenotype prediction
Opportunistic population
screening
Deployment in
hospital ECG system
194
Pulmonary embolism triage from
CT (imaging biomarker)
Chest CT/CTA CNN-based
detection + workﬂow
prioritization
Radiology work ﬂow
triage
FDA-cleared triage
software
285
CTA CT angiography, NCCT non-contrast CT, CNN convolutional neural network, SaMD software as a medical device, CAD computer-aided detection, EHR electronic
health record
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
7
Signal Transduction and Targeted Therapy          (2026) 11:407

Since different AI architectures are preferentially suited to
distinct biomarker discovery tasks, Fig. 3 maps commonly used ML
paradigms matched with fundamental analytical goals such as
feature selection, multimodal integration, target identi ﬁcation, and
mechanistic inference.
Across all settings, the core requirement is that the method
selection be aligned with the intended claim, including predictive
enrichment, diagnostic discrimination, biologically grounded
pathway nomination, target discovery, or therapeutic response
classiﬁcation. Each claim requires a different standard of evidence,
and each is weakened by different modes of failure. Positioning AI
methods within the logic speci ﬁc to this claim is the most reliable
way to prevent biomarker discovery from drifting toward elegant
models with fragile scienti ﬁc meaning. While the methods in
Section “Artiﬁcial intelligence methods for biomarker discovery ”
provide powerful tools for extracting predictive signatures from
complex biomedical data, prediction alone is insuf ﬁcient when
biomarker claims extend to areas such as biological interpretation,
therapeutic targeting, or surrogate endpoint development. For
biomarkers to inform mechanism and intervention, AI models
must be coupled to biological structure, causal hypotheses, and
perturbation-sensitive validation. Therefore, mechanistic AI repre-
sents a distinct paradigm in biomarker science; one paradigm that
aims not only to predict outcomes but also to map signatures to
pathways, cellular programs, and actionable molecular processes.
The following section examines AI strategies that explicitly
incorporate biological priors, experimental perturbation, and
causal structure to support mechanistically grounded biomarker
discovery.
Since different AI architectures are suited to different biomarker
tasks and data structures, Table 3 maps the major methodological
classes according to their best applications, strengths, and risks in
biomarker development.
MECHANISTIC AI: MAPPING BIOMARKERS TO PATHWAYS,
TARGETS, AND THERAPEUTIC HYPOTHESES
From correlational signatures to mechanistic hypotheses
Most AI-derived biomarkers are correlational by construction. They
identify patterns associated with outcomes, but they do not
specify why these patterns occur. While correlational biomarkers
are clinically useful, they are fragile when used to guide treatment,
predict response mechanisms, or serve as surrogate end-
points.112–115 Mechanistic biomarker discovery requires additional
constraints linking features to biological processes.
Recent reviews emphasize that mechanistic interpretation
should integrate computational evidence with biological plausi-
bility, perturbation consistency, and pathway coherence, rather
than relying solely on pattern explainability techniques. 95 Without
such integration, feature attribution risks generating compelling
narratives not supported by causal biology. Therefore, mechanistic
AI aims to directly encode biological structure into model
architectures or training targets and narrow the hypothesis space
to biologically plausible explanations.
Knowledge-guided and pathway-constrained neural architectures
One approach to mechanistic modeling directly embeds compiled
biological information, such as signaling pathways, transcriptional
Fig. 3 Mapping AI methods to biomarker discovery tasks. Comparative overview of major AI approaches, including classical machine learning,
deep learning, self-supervised learning, graph neural networks, foundation models, and generative/causal AI, across common biomarker discovery
applications. Color indicators represent the relative strength of current evidence and practical applicability. Figure created by the authors usi ng
Adobe Illustrator (Version 29.3.1)
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
8
Signal Transduction and Targeted Therapy          (2026) 11:407

regulatory networks, or metabolic graphs, into neural network
topology. In these architectures, nodes correspond to genes or
proteins, and edges re ﬂect known interactions, thus restricting the
ﬂow of information to biologically meaningful pathways. 95,116
Graphical-structured neural networks have been used to model
perturbation responses, drug sensitivity, and pathway activation
by forcing predictions to traverse interaction networks, enabling
the identi ﬁcation of subnetworks associated with phenotypic
change.98 This design enhances interpretability and stability when
sample sizes are limited, as prior biological information reduces
model ﬂexibility.
Nevertheless, pathway databases are incomplete, context-
dependent, and sometimes contradictory. 117,118 Consequently,
knowledge-guided models should be interpreted as hypothesis
generators rather than de ﬁnitive causal evidence and supported
by data-driven components that allow for the discovery of novel
interactions.
Perturbation-based learning and causal signal identi ﬁcation
Perturbation datasets, such as CRISPR scans, drug response assays,
and cytokine stimulation experiments, provide critical leverage for
separating causal factors from downstream correlations. 119,120 AI
models trained on perturbation responses enable counterfactual
prediction and target prioritization by learning mappings between
molecular states and phenotypic outcomes.
Recent reviews highlight that perturbation-based ML is
particularly powerful when combined with network prioritization
and multimodal measures, supporting the inference of pathway
dependencies and drug mechanisms. These approaches are
increasingly applied in oncology, immunology, and systems
pharmacology, where biologically grounded hypotheses can be
experimentally tested. 121,122 Importantly, perturbation learning
only increases mechanistic reliability when the experimental
design includes adequate controls, replications, and the relevant
biological domain. Sparse or biased perturbation panels can
produce misleading inferences, even in advanced models.
Causal representation learning and counterfactual biomarker
modeling
Causal representation learning aims to identify latent variables
corresponding to underlying causal factors rather than super ﬁcial
correlations. In biomarker discovery, this framework aims to
separate disease-triggering processes from confounding factors
such as technical artifacts, comorbidities, or treatment
effects.112,123
Recent methodological syntheses explain how invariant risk
minimization, instrumental variable approaches, and counter-
factual targets can improve generalization across environments by
prioritizing features that are stable under intervention. 112,124 When
applied in biomarker development, these methods can help
identify signatures that are more likely to re ﬂect causal disease
mechanisms and therefore maintain validity across populations.
However, causal learning in observational biomedical data
remains challenging due to unmeasured confounding factors,
feedback loops, and dynamic disease processes. Causal AI
methods should therefore be viewed as a reinforcing, not a
replacement for, the need for experimental validation.
Linking biomarker signatures to drug response and therapeutic
classiﬁcation
A major objective of mechanistic biomarker discovery is to link
biomarker signatures with biological processes relevant to
treatment response. Unlike purely correlational biomarkers,
mechanistic-based biomarkers can provide information about
pathway activity, cellular states, and molecular interactions that
contribute to disease progression or treatment sensitivity.
Network-based analyses, pathway-level representations, and
causal modeling approaches can help identify biological programs
associated with treatment response. 84,98,116 Knowledge-graph
approaches incorporating perturbation transcriptomic data have
been used to infer compound-protein interactions and connect
molecular perturbations with candidate therapeutic targets.
Therefore, they have improved mechanistic interpretation beyond
conventional predictive modeling. 125 By integrating biomarker
signals with existing biological information, these methods can
generate hypotheses about potential points of intervention,
resistance mechanisms, or patient subgroups with differing
treatment sensitivities. Such analyses can enhance biological
interpretability and facilitate the prioritization of candidate
therapeutic targets for further investigation.
However, identifying mechanistically plausible targets does not
guarantee clinical bene ﬁt. Biological associations need to be
validated through experimental studies, perturbation-based
investigations, and independent clinical datasets to con ﬁrm
therapeutic signiﬁcance. In conclusion, mechanistic AI approaches
should be viewed primarily as tools for hypothesis generation and
Table 3. AI method classes and suitability for biomarker tasks
AI method class Optimal biomarker
tasks
Data types Strengths Major risks Interpretability
Potential
Example use cases
Regularized
regression
Risk scores,
screening
Tabular clinical/omics Stable, transparent,
robust
Limited nonlinear
capture
High Cardiovascular risk,
ﬁbrosis scores.
Tree ensembles Feature selection,
response prediction
Mix tabular data Handles interactions
and missing data
Overﬁtting in small
groups
Medium Treatment response
models
Convolutional
neural networks
(CNNs)
Imaging biomarkers MRI, CT,
histopathology
Spatial feature
learning
Scanner/site shift Low-medium Tumor
segmentation,
plaque analysis
Transformers Multimodal fusion,
arrays
Imaging + omics + EHR Cross-modal
attention
High data demand, non-
transparent structure
Low Survival prediction
Graph neural
networks
Pathway inference,
cell interactions
Molecular networks,
scRNA
Mechanistic
modeling
Complex training Medium Immune network
biomarkers
Foundation models Transfer between
diseases/sites
Imaging, omics,
multimodal
Data ef ﬁciency,
reuse
Bias spread, cost Low Cross-cohort
imaging
Causal machine
learning
Surrogate
validation,
treatment effects
Longitudinal
multimodal
Causal reasoning Strong assumptions High (if
applicable)
Biomarker-outcome
linkage
Key references for this table: refs. 21,112,286,287
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
9
Signal Transduction and Targeted Therapy          (2026) 11:407

biological interpretation, rather than as direct evidence of
treatment ef ﬁcacy.
The translation of biomarker-guided hypotheses into clinical
decision-making frameworks, patient classi ﬁcation strategies,
accompanying diagnostic methods, and drug development
applications is discussed in Section “Translational roles of AI
biomarkers in therapeutic development and clinical decision-
making processes ”.
Limitations of mechanistic AI and the role of experimental
validation
Despite rapid advances, mechanistic AI cannot establish causality
on its own. 112,113 Biological systems exhibit redundancy, compen-
sation, and context speci ﬁcity, limiting inference from static
data.11,126 Especially in immune and neurodegenerative disorders,
even perturbation experiments may not fully re ﬂect in vivo
complexity.127
Therefore, mechanistic AI must be embedded in an iterative
discovery cycle consisting of computational hypothesis genera-
tion, targeted experimentation, model re ﬁnement, and clinical
correlation. This cycle reduces the risk of overinterpreting model
descriptions and aligns biomarker development with experimental
biology.128,129 From a translational perspective, mechanistic
rationality strengthens regulatory and clinical con ﬁdence, but
only when supported by reproducible evidence across platforms
and disease contexts. Therefore, mechanistic AI should be viewed
as a facilitator of biologically based biomarker processes, rather
than a replacement for rigorous validation. 112,130
While mechanistic AI provides the methodological foundation
for moving beyond correlational signatures, the usefulness of
translational biomarkers ultimately depends on whether AI-
generated patterns can be mapped into actionable signal
transduction states that inform therapeutic intervention.
While mechanistic AI provides the methodological foundation
for moving beyond purely correlational biomarker signatures, its
primary contribution lies in the inference of biologically signi ﬁcant
pathway activity states and network relationships. These
approaches enhance the mechanistic understanding of biomarker
signaling by helping to transform high-dimensional molecular
data into interpretable representations of disease biology. There-
fore, the following section focuses on signal transduction
networks and pathway state biomarkers as biological frameworks
within which AI-derived biomarker signatures can be interpreted
and contextualized.
SIGNAL TRANSDUCTION NETWORKS, PATHWAY-STATE
BIOMARKERS, AND THERAPEUTIC TARGETING
Why pathway states outperform static biomarkers
Most conventional biomarkers quantify the abundance of
molecules (gene expression levels, protein concentrations, or
circulating analytes) at a single point in time. While such
measurements can be correlated with disease states, they often
fail to capture the functional activity of underlying biological
systems, particularly in complex and dynamic diseases. In contrast,
signaling pathways represent integrated, dynamic processes that
encode how cells interpret and respond to internal and external
stimuli. Consequently, pathway activity states, rather than static
molecular levels, are often more directly linked to disease
mechanisms and therapeutic response.
For example, activation of the PI3K-AKT-mTOR or MAPK
pathways cannot be reliably inferred from the expression of
individual components alone, due to post-translational regulation,
feedback loops, and compensatory signaling. Similarly, in ﬂamma-
tory signaling pathways such as NF- κB and JAK-STAT exhibit
context-dependent activation patterns in ﬂuenced by cytokine
gradients, cellular composition, and microenvironmental
cues.131,132 Consequently, biomarkers based solely on abundance
measurements can misclassify patients with similar molecular
levels but signi ﬁcantly different pathway activation states.
AI methods can assist in inferring latent pathway states by
integrating transcriptomic, proteomic, imaging, and clinical
information.89,90 Instead of addressing features independently,
these models can learn coordinated patterns across molecular
networks, enabling the identi ﬁcation of pathway-level signatures
that better re ﬂect biological activity. For example, multi-omics
integration approaches using machine learning frameworks have
demonstrated the ability to capture the coordinated activation of
signaling modules associated with disease progression and
treatment response. 11,47
Importantly, pathway-state biomarkers carry greater transla-
tional signiﬁcance by nature, as most therapeutic interventions act
on signaling processes rather than isolated molecules. Targeted
therapies, including kinase inhibitors, immunomodulators, and
pathway-speciﬁc biological drugs, are designed to modulate
pathway activity rather than molecular abundance. Therefore,
biomarkers that measure pathway activation or dysregulation are
more likely to predict treatment response, resistance mechanisms,
and optimal therapeutic combinations, aligning biomarker dis-
covery with mechanisms of action in precision medicine. 133,134
Figure 4 illustrates the hierarchy of biomarker evidence, demon-
strating a progression from purely correlational relationships to
therapeutically applicable biomarkers with robust mechanistic
validation.
Signal transduction complexity and biomarker instability
One of the fundamental challenges in biomarker development is
that signal transduction networks are characterized by redun-
dancy, feedback regulation, and context-dependent crosstalk; all
of which can destabilize biomarker performance across popula-
tions and environments. These characteristics help explain why
many biomarkers that perform well in discovery cohorts fail
during external validation or clinical practice. 5,135
First, redundancy in signaling networks allows multiple path-
ways to produce similar phenotypic outcomes. For example,
tumor proliferation can be driven by MAPK or PI3K-AKT signaling,
and inhibition of one pathway can lead to compensatory
activation of alternative pathways. This redundancy contributes
to therapeutic resistance and limits the generalizability of
biomarkers targeting single molecular traits.
Secondly, both negative and positive feedback loops can
dynamically reshape pathway activity over time, especially under
therapeutic pressure. Targeted inhibition of a signaling node may
initially suppress downstream signaling but subsequently trigger
feedback activation in upstream or parallel pathways. These
adaptive responses reduce the stability of static biomarkers and
make treatment prediction dif ﬁcult, particularly in oncology and
immune-mediated diseases. 98,136
Thirdly, context-dependent cross-talks between pathways
create variability that is dif ﬁcult to capture using unimodal or
linear models. In in ﬂammatory and thrombo-in ﬂammatory
states, signaling interactions between immune cells, endothelial
cells, and circulating mediators create highly context-speci ﬁc
biological states. For example, NET formation demonstrates how
cross-network interactions generate emerging phenotypes that
cannot be reduced to a single marker by integrating
signals from in ﬂammation, coagulation, and endothelial
pathways. 137,138
These features collectively imply that biomarker robustness
depends not only on statistical performance but also on alignment
with the underlying network structure of disease biology. AI
models that ignore these features risk failing to learn dataset-
speciﬁc correlations under distributional shifts; this is a well-
known limitation in biomedical machine learning. 139,140 In
contrast, approaches that incorporate network constraints, path-
way priorities, or learning based on perturbation information are
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
10
Signal Transduction and Targeted Therapy          (2026) 11:407

better positioned to identify features that remain stable across
biological contexts.
From a translational perspective, recognizing signal complexity
clariﬁes why biologically grounding improves generalizability.
Biomarkers that re ﬂect pathway-level processes rather than
isolated molecular relationships are more likely to retain validity
across populations, disease stages, and therapeutic interventions.
This understanding motivates the shift from feature-centric
biomarker design to network-aware biomarker design, where AI
is used not only to detect patterns but also to map those patterns
into biologically interpretable signaling processes and actionable
therapeutic targets.
AI approaches for pathway-state inference and network-
constrained biomarker modeling
A major limitation of traditional biomarker discovery is that
individual molecular measurements often provide only indirect
information about the functional state of biological systems. 11,141
Consequently, there is growing interest in pathway-state biomar-
kers that aim to capture the coordinated activity of signaling
networks rather than isolated molecular features. In this context,
AI primarily serves as an integrative framework for inferring latent
biological states from heterogeneous data, rather than as an end
in itself.
Pathway-state inference typically combines information from
transcriptomic, proteomic, imaging, and clinical datasets to
predict the activity of biological programs that cannot be directly
measured. Recent multimodal interpretable deep learning frame-
works have further demonstrated the ability to integrate
transcriptomic and clinical information, while also providing
insights into drug response mechanisms. 142 Instead of focusing
on single genes or proteins, these approaches identify coordi-
nated patterns re ﬂecting pathway activation, cellular interactions,
or disorganization at the network level. Such representations are
generally more robust than individual biomarkers because they
capture collective biological behavior and are less sensitive to
measurement variability. 143,144
The biological signi ﬁcance of pathway-state biomarkers is
further enhanced by the fact that the inferred activity patterns
remain consistent across multiple data types, independent
cohorts, and experimental disruptions. Evidence from systems
biology and network medicine shows that biomarkers consistent
with coherent biological programs are more likely to remain stable
across populations and disease contexts than signatures derived
solely from statistical association. 145,146 Consequently, pathway-
level inference provides a conceptual bridge between predictive
modeling and mechanistic interpretation.
However, inferred pathway states should be considered
probabilistic representations of biological activity rather than
direct measures of causal mechanisms. Their reliability depends on
the quality of the underlying data, the completeness of the
available biological information, and the extent of external and
Fig. 4 Biomarker evidence hierarchy: from correlation to clinical action. A four-level framework showing the progressive strengthening of the
mechanistic basis and therapeutic signi ﬁcance. Level 1 (Correlational): statistical association without biological context. Level 2 (Pathway-aligned):
consistency with known signaling networks and coordinated pathway organization. Level 3 (Perturbation-validated): functional validation throu gh
CRISPR scans, drug perturbations, or genetic models. Level 4 (Therapeutically actionable): directly guiding treatment selection and therapeutic
response prediction. Arrows show the gradual increase in strength of evidence (left) and clinical impact (right). Higher-level biomarkers require
more extensive validation but provide stronger therapeutic rationale and improved translational probability. Examples are given for each level.
Figure created by the authors using Adobe Illustrator (Version 29.3.1)
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
11
Signal Transduction and Targeted Therapy          (2026) 11:407

experimental validation. Therefore, pathway-state biomarkers are
most valuable when integrated into a broader validation frame-
work that includes mechanistic consistency, evidence of disrup-
tion, and clinical utility assessment. 130,147
Various methodological approaches, including network con-
strained learning, graph-based modeling, perturbation-informed
analysis, and multimodal integration, can contribute to pathway
state inference. 129,148,149 Recently developed graph-based archi-
tectures, including graphical convolutional frameworks developed
for predicting immune checkpoint inhibitor response, have
successfully integrated biological relationships into treatment
response prediction tasks. 150 However, the speci ﬁc algorithm is
often less important than the biological validity of the inferred
pathway activity and its reproducibility across datasets and
experimental settings. From a translational perspective, the main
goal is not the selection of a speci ﬁc AI architecture, but the
identiﬁcation of biologically consistent and clinically relevant
pathway states that can support therapeutic decision-making.
Despite these advances, several limitations remain. Biological
knowledge bases are incomplete and often context-dependent,
which can lead network-constrained models to miss novel
mechanisms while guiding them toward well-characterized path-
ways.112,113 While perturbation datasets are informative, they are
often sparse and may not fully capture in vivo complexity. 128,129
Furthermore, multimodal integration requires careful harmoniza-
tion of data types with varying resolutions, aggregate effects, and
noise structures. Consequently, pathway-state inference should be
interpreted as a probabilistic approximation of biological activity
rather than a precise representation of causal mechanisms.
However, the integration of network constraints, perturbation
data, and multimodal learning represents a signi ﬁcant step toward
mechanistically grounded biomarker modeling. By shifting from
feature-centric prediction to pathway-level inference, these
approaches enhance the stability, interpretability, and transla-
tional signi ﬁcance of AI-derived biomarkers and provide a
foundation for linking biomarker signatures to therapeutic
targeting strategies. 112,145
Neutrophil extracellular traps (NETs) as a pathway-state biomarker
exemplar
Neutrophil extracellular traps (NETs) provide an illustrative
example of how pathway-state biomarkers can capture dynamic
biological processes more effectively than isolated molecular
measurements. NET formation is regulated through coordinated
signaling pathways involving reactive oxygen species production,
PAD4 activation, chromatin decondensation, in ﬂammatory cyto-
kine signaling, and interactions between innate immunity and
coagulation networks. 50,95,151 Consequently, biomarkers re ﬂecting
NET activity can provide information about the functional state of
thrombo-inﬂammatory responses rather than the abundance of
any single molecule.
From a biomarker perspective, NET-associated signatures can
be derived from multiple data sources, including circulating
extracellular DNA, citrullinated histones, myeloperoxidase-DNA
complexes, transcriptomic pro ﬁles, proteomic datasets, and
imaging-based assessments of in ﬂammatory activity. 49,50,151 AI-
powered integration of these heterogeneous data types can
facilitate the identi ﬁcation of latent pathway states associated
with immune activation, vascular damage, tissue remodeling, and
disease progression. 89–91 Importantly, these approaches shift the
biomarker development process from single-marker measure-
ments to network-level representations of biological activity.
The translational signi ﬁcance of NET-associated biomarkers
extends beyond disease detection. Since NET formation is
involved in in ﬂammatory, cardiovascular, autoimmune, thrombo-
tic, and oncological processes, pathway-level NET signatures can
contribute to mechanistic disease strati ﬁcation and the identi ﬁca-
tion of biologically distinct patient subgroups. Although
signiﬁcant experimental and clinical validation is needed, NETs
demonstrate how AI-powered pathway state biomarkers can link
molecular observations to broader disease mechanisms and
support the development of biologically based precision medicine
strategies.49,50,151
Biological relevance of pathway-informed biomarkers
The ultimate translational value of pathway-informed biomarkers
lies in their ability to guide therapeutic decisions, rather than
simply predicting disease presence or prognosis. By capturing the
activation states of signaling networks, these biomarkers provide a
functional output of disease biology that can be directly linked to
drug mechanisms of action, providing biologically meaningful
characterization of disease heterogeneity.
In oncology, pathway-level biomarkers have been widely used
to match patients with targeted therapies. For example, activation
of the PI3K-AKT-mTOR pathway, MAPK signaling, or receptor
tyrosine kinase networks can inform the use of pathway-speci ﬁc
inhibitors, while integrated molecular signatures can identify
resistance mechanisms and compensatory pathway activa-
tion.84,116 Importantly, these approaches are moving beyond
single gene alterations toward network-based patient strati ﬁcation
that better re ﬂects the redundancy and adaptability of signaling
systems.
A similar paradigm is emerging in immune-mediated and
inﬂammatory diseases, where pathway activation states, such as
NF-κB, JAK-STAT, and cytokine signaling networks, can inform
therapeutic targeting with biologics and small molecule inhibitors.
For example, biomarkers re ﬂecting interferon signaling or
cytokine-driven immune activation have been associated with
response to targeted immunomodulatory therapies, supporting
their relevance as indicators of underlying immune activation
states.50,152 In cardiovascular and thrombo-in ﬂammatory condi-
tions, integrated pathway signatures such as NET formation and
coagulation-inﬂammation crosstalk can reveal coordinated
thrombo-inﬂammatory activity patterns associated with disease
progression.
Linking biomarkers to treatment requires not only biological
validity but also a demonstration of clinical bene ﬁt. Predictive
performance alone is insuf ﬁcient; pathway-based biomarkers must
demonstrate that their use improves decision-making, patient
outcomes, or healthcare ef ﬁciency. This requires prospective
validation, decision curve analysis, and evaluation within clinical
workﬂows, as highlighted in recent translational frameworks. 153,154
In this context, pathway-based biomarkers are particularly
valuable because they align diagnostic classi ﬁcation with action-
able points of intervention and strengthen the rationale for their
adoption in clinical practice.
Despite these advances, several challenges remain. Signaling
pathways are highly context-dependent, exhibiting signi ﬁcant
variability across tissues, disease stages, and patient populations.
Redundancy and feedback mechanisms can lead to adaptive
resistance, limiting the effectiveness of therapies guided by single-
pathway biomarkers. Furthermore, many pathway-based models
rely on data from cell lines or controlled experimental systems
that may not fully capture in vivo complexity. Consequently,
robust translation requires the integration of experimental
validation, real-world data, and iterative model re ﬁnement.
Overall, pathway-informed biomarker strategies represent a
critical step toward mechanistically grounded precision medicine,
where diagnostic signals are directly linked to therapeutic
hypotheses and intervention strategies. By combining network-
based modeling, perturbation-informed learning, and clinical
validation, AI-powered biomarker frameworks can facilitate a shift
from descriptive prediction to actionable biological insight,
ultimately enabling more effective and individualized treatment
approaches across disease domains.
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
12
Signal Transduction and Targeted Therapy          (2026) 11:407

Although pathway-based biomarkers provide biologically
meaningful representations of disease activity, their practical
value ultimately depends on their successful integration into
biomarker development work ﬂows, clinical validation frameworks,
and decision support systems. The operational and translational
requirements necessary to facilitate this transition are discussed in
the following sections.
TRANSLATIONAL WORKFLOW FOR AI BIOMARKER
DEVELOPMENT
Unlike Section “Artiﬁcial intelligence methods for biomarker
discovery”, which focuses on methodological approaches to
biomarker discovery, this section describes the operational
workﬂow required to translate AI-derived biomarkers from the
discovery to clinical implementation. The work ﬂow encompasses
study design, data harmonization, model development, biological
validation, clinical utility assessment, reproducibility standards,
and deployment infrastructure. The emphasis is not on speci ﬁc
algorithms, but on the sequential processes necessary to generate
robust, clinically actionable biomarker evidence.
Study design and dataset generation: prospective and
retrospective, endpoints, and spectrum effects
Biomarker processes should begin with a clear de ﬁnition of the
intended clinical task, including screening, diagnosis, prognosis,
treatment selection, or response monitoring. Each task requires
distinct tolerances for false positives, decision timing, and clinical
consequences. Retrospective datasets are valuable for hypothesis
generation, but often overestimate performance when spectrum
bias, convenience sampling, and endpoint ambiguity
present.155,156
Case-control designs with extreme phenotypes in ﬂate separ-
ability and may misrepresent true diagnostic ambiguity. Prog-
nostic biomarkers are particularly susceptible to time-to-event
deﬁnition, censoring, and treatment confounding. For AI models
trained on resting heart rate (RHR)-linked data, temporal
congruence between predictors and outcomes is critical to
prevent accidental inclusion of future information. 15,157
Prospective cohort design remains the gold standard but is
rarely feasible at scale for early discovery. Hybrid designs
(retrospective discovery followed by prospective or pragmatic
validation) represent a realistic translational pathway, provided
that models are locked in before prospective testing and protocol
deviations are minimized.
Data quality control and harmonization across platforms and
centers
The robustness of AI biomarkers is primarily limited by the
consistency of input data. In molecular studies, variations in
sample processing, sequencing chemistry, and library preparation
lead to batch effects that can dominate the biological signal. In
imaging, scanner hardware, acquisition parameters, and recon-
struction algorithms generate region-speci ﬁc signatures. In digital
biomarkers, ﬁrmware updates and sensor drift lead to non-
stationary noise.
While batch-correction and harmonization methods can miti-
gate these effects, overcorrection risks eliminating disease-related
variation. Therefore, harmonization strategies should be modality-
speciﬁc, validated using technical iterations whenever possible,
and implemented with sensitivity analyses demonstrating the
stability of biomarker signals among correction methods. 158–161
Large-scale multicenter studies consistently demonstrate that
harmonization quality and metadata completeness are the
primary determinants of cross-site generalization, often out-
weighing algorithmic differences. 158 In conclusion, data engineer-
ing should be treated as a core scienti ﬁc component of biomarker
pipelines, not as a preprocessing step.
Feature representation, leakage prevention, and evaluation
separation
Classical biomarker pipelines rely on prede ﬁned features such as
gene panels, radiomic measurements, pathway scores, or sum-
mary digital metrics. Although these approaches are often
interpretable and reproducible, they may fail to capture complex
biological patterns. More recent work ﬂows increasingly utilize
data-driven feature representations, which can improve prediction
performance but also increase the risk of leakage and spurious
associations if evaluation procedures are not rigorously separated.
Leakage can occur through repeated patients, shared normal-
ization between training and test sets, feature selection in ﬂuenced
by outcomes, or longitudinal contamination where future
measurements affect previous predictions. In multimodal pro-
cesses, leakage can occur when different modalities share
descriptors or when preprocessing processes inadvertently
transmit label information.
Best practice requires complete process separation between
training and evaluation, including preprocessing, missing data
completion, normalization, and feature selection. Nested cross-
validation is essential when hyperparameter tuning is extensive.
Independent external validation remains the most reliable
indicator that leakage is not in ﬂating performance. 130 Perfor-
mance degradation after implementation has been documented
even in widely adopted clinical prediction systems. 162
Model development: calibration, uncertainty, and subgroup
performance
Beyond discrimination, clinical biomarker models must be well-
calibrated:163 predicted risks or probabilities should correspond to
observed event rates. Incorrect calibration can lead to inappropri-
ate treatment escalation or false reassurance, even if the AUC is
high. Recalibration is often necessary when models are ported
across populations or care settings.
Quantitative uncertainty is particularly important when biomar-
ker outputs guide high-risk decisions or trial enrollments. Bayesian
methods, ensemble variance, and conformal estimation provide
complementary approaches to express predictive con ﬁdence, but
currently, few biomarker studies explicitly report uncertainty. 164,165
Subgroup performance analysis is necessary to identify
differential accuracy rates across strata of sex, ancestry, age,
disease stage, and comorbidity. 166 Apparent global performance
can mask clinically signi ﬁcant modes of failure in speci ﬁc
subpopulations, which can have direct implications for equity
and regulatory approval.
Biomarker selection and stability: reproducibility across cohorts
and resampling
In discovery settings, thousands of associated features may appear
predictive, but only a subset will be stable under perturbation.
Feature stability analysis using bootstrapping resampling, cross-
cohort replication, and perturbation testing helps distinguish
robust biological signals from sampling artifacts. 167
Stability is particularly important when biomarkers are pro-
posed as mechanistic indicators or therapeutic guidelines.
Unstable feature sets weaken biological interpretation and render
subsequent validation inef ﬁcient.168 Ensemble feature selection,
pathway-level aggregation, and consensus modeling can increase
robustness at the expense of lower detail.
From a translational perspective, inter-site generalization is
more important than intra-cohort performance. Therefore, bio-
marker pipelines should prioritize inter-site stability rather than
maximum intra-agency discrimination.
Biological validation cycle: functional evidence and orthogonal
conﬁrmation
Statistical validation does not determine biological relevance.
Functional validation is essential for biomarkers that aim to
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
13
Signal Transduction and Targeted Therapy          (2026) 11:407

provide information about mechanisms or treatments. 169 Strate-
gies include correlation with gene perturbation, pharmacological
modulation, spatial co-positioning with pathology, and orthogonal
molecular assays.
Importantly, validation must be bidirectional: AI-generated
hypotheses should inform experiments, and experimental results
should iteratively improve models. This closed-loop approach
reduces the risk of computational signatures remaining discon-
nected from biological causality.
Functional validation should demonstrate that biomarker-
deﬁned states correspond to reproducible biological processes
and remain consistent across orthogonal experimental systems.
Clinical validation and bene ﬁt: from AUC to decision impact
Even biologically plausible biomarkers can fail clinically if they
don’t improve decisions. Decision curve analysis and net bene ﬁt
frames assess whether biomarker-guided strategies outperform
standard care within plausible threshold ranges. 25 These methods
are particularly important when biomarkers are proposed for risk
stratiﬁcation or treatment enhancement.
Clinical work ﬂow integration should also be considered.
Biomarkers requiring complex testing, long processing times, or
specialized interpretation may not be adopted even if they are
accurate. Human factors, interpretability, and integration into
existing laboratory and IT systems strongly in ﬂuence real-world
efﬁcacy.
Prospective clinical evaluation remains the strongest evidence
of beneﬁt, but pragmatic trials and embedded application studies
may offer scalable alternatives when continuous model updates
are expected. 170
Reporting standards, reproducibility, and auditability
Transparent reporting is essential for independent validation and
regulatory con ﬁdence. TRIPOD-AI speci ﬁes minimum reporting
requirements for predictive model development and validation,
including dataset description, handling of missing data, and
evaluation methodology. 130,147 PROBAST-AI provides a structured
risk-bias assessment with an emphasis on leakage, confounding
factors, and applicability. 147
For imaging biomarkers, modality-speci ﬁc standards such as
CLAIM further specify acquisition and evaluation reporting
requirements. Regulatory bodies expect traceability across data,
model releases, and performance audits, especially when adaptive
or continuously learning systems are proposed.
Historical community-wide benchmarking initiatives, including
Microarray Quality Control (MAQC) and subsequent Sequencing
Quality Control (SEQC), and the more recent SEQC2 programs,
have consistently demonstrated that biomarker signatures derived
from high-dimensional datasets are highly sensitive to analytical
decisions such as preprocessing, feature selection, and model
development.171–173 Importantly, different analytical work ﬂows
applied to the same datasets can produce signi ﬁcantly different
biomarker signatures, even while achieving similar prediction
performance.174 These ﬁndings highlight the importance of
standardized protocols, independent external validation, bench-
mark reference materials, and transparent reporting practices. The
key lesson for AI-based biomarker discovery is that reproducibility
across analytical pipelines, datasets, and study populations is just
as important as prediction accuracy itself. Similar reproducibility
concerns have been demonstrated in microbiome biomarker
studies.175
Data infrastructure and multi-center reproducibility ecosystems
Sustainable biomarker clinical adoption requires an infrastructure
that supports external validation and lifecycle monitoring.
Federated learning, secure data enclaves, and trusted research
environments enable cross-center evaluation while preserving
privacy. Shared benchmark datasets and challenge platforms can
accelerate method comparison, but must re ﬂect realistic clinical
variability rather than idealized curated subsets.
Regulatory-grade biomarker development increasingly relies on
longitudinal performance monitoring, deviation detection, and
recalibration mechanisms. These operational requirements blur
the traditional line between exploratory research and application
engineering, reinforcing the need for biomarker processes to be
designed with the end-use in mind from the outset. 176,177
LEVELS OF EVIDENCE AND VERIFICATION: A UNIFIED
GRADING FRAMEWORK (CROSS DISEASES)
To support a uni ﬁed translation framework for AI-assisted
biomarker development, Fig. 5 summarizes the progressive
evidence requirements needed to advance biomarkers from the
discovery to clinical implementation. The framework emphasizes
internal validation, external replication, robustness testing, clinical
beneﬁt assessment, and real-world deployment readiness.
Levels of evidence for AI-generated biomarkers
AI-powered biomarker studies encompass a wide range of
evidence maturity; however, published claims often fail to make
a clear distinction between exploratory associations and clinically
applicable tools. To support consistent interpretation, biomarker
evidence can be conceptualized through a series of validation
stages re ﬂecting increasing resistance to bias and increasing
suitability for real-world application.
At the exploratory level, biomarkers are derived from a single
cohort or from aggregated retrospective datasets without
independent testing. These studies are essential for hypothesis
generation but are highly vulnerable to over ﬁtting, aggregate
effect, and cohort-speci ﬁc confounding factors. Performance
predictions at this stage re ﬂect primarily intrinsic separability
rather than generalizable disease biology.
External validation requires evaluation in independent cohorts
collected in different locations, time periods, or clinical contexts.
Successful external replication demonstrates that biomarker
signals are not constrained by local technical or demographic
characteristics. However, external validation alone does not
guarantee clinical signi ﬁcance if the patient spectrum, treatment
models, or outcome de ﬁnitions differ from the intended use
cases.155
Prospective validation evaluates biomarkers in prospective
studies where data collection, endpoints, and analysis plans are
determined before outcome observation. Prospective designs
reduce bias from post-model adjustment and allow for the
assessment of operational feasibility, de ﬁciency, and work ﬂow
integration. However, prospective accuracy does not automatically
imply clinical bene ﬁt.66,178,179
Evidence of clinical bene ﬁt addresses whether biomarker-
guided decisions improve patient outcomes or resource allocation
compared to standard care. Decision curve analysis and net utility
frames offer a more direct link between biomarker output and
patient impact by explicitly assessing clinical outcomes at decision
thresholds.25 Beneﬁt can also be assessed through pragmatic trials
or embedded application studies where randomized trials are
impractical.
Finally, regulatory and clinical adoption evidence re ﬂect
sustained performance in real-world conditions, integration into
clinical work ﬂows, and post-market safety and ef ﬁcacy oversight.
For adaptive or continuously learning systems, regulatory frame-
works increasingly emphasize lifecycle oversight rather than one-
off validation. 170
Importantly, progression through this evidence hierarchy is not
guaranteed: many biomarkers demonstrate strong exploratory
performance but fail during external or prospective evaluation
due to biological heterogeneity, dataset shift, or changes in
clinical practice. While validation is generally discussed in general
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
14
Signal Transduction and Targeted Therapy          (2026) 11:407

terms, evidence requirements for AI biomarkers change signi ﬁ-
cantly throughout the development phases. To functionalize the
concept of real-world implementation readiness, Table 4 presents
a uni ﬁed evidence framework for AI biomarkers that links the
study design to the type of clinical claims that can be justi ﬁed at
each validation phase.
This framework is consistent with emerging reporting and bias
assessment standards and provides a practical reference for
interpreting claims in the biomarker literature, particularly when
evaluating whether models have progressed beyond the dis-
covery phase. Most published AI biomarker studies are limited to
early validation phases, contributing to the high loss rate observed
during robustness testing and external replication. In conclusion,
biomarker translation should be viewed as an incremental
evidence-generating process, rather than a one-off model
development effort.
Common failure modes in AI biomarker translation
Across biomarker types and disease domains, translation failures
cluster around a limited number of recurring issues. Recognizing
these failure modes is crucial for designing studies that generate
reliable evidence.
Table 4. Levels of evidence (validation framework) for AI biomarkers
Evidence level Study design Typical dataset What is demonstrated Common pitfalls Suitable publication
claims
Discovery Retrospective Single cohort Signal association Over ﬁtting, leakage Candidate biomarker
External validation Retrospective multi-
center
Independent cohorts Generalizability Dataset shift ignoring Validated biomarker
Prospective validation Prospective observational Real-world work ﬂow Stability in practice Behavior confounding Clinical readiness
Clinical Utility Interventional Decision-guided trials Outcome improvement Poor trial design Clinical bene ﬁt
Regulatory adoption Regulatory submission Audited datasets Safety and effectiveness Limited post-market
data
Approved diagnostic
Key references for this table: refs. 25,130,147,155,170
Fig. 5 Five-level validation framework for AI-based biomarkers. Hierarchical evidence framework illustrating progressive validation requirements,
from internal validation to real-world application. Key methodological requirements, common modes of failure, and alignment with reporting and
bias assessment standards are highlighted. Figure created by the authors using Adobe Illustrator (Version 29.3.1). AI arti ﬁcial intelligence, ML
machine learning, AUC area under the receiver operating characteristic curve, CV cross-validation, TRIPOD + AI Transparent Reporting of a
multivariable prediction model for Individual Prognosis Or Diagnosis with AI extension, PROBAST + AI The prediction model Risk Of Bias
Assessment Tool with AI-extended, NNT number needed to treat, RCT randomized controlled trial
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
15
Signal Transduction and Targeted Therapy          (2026) 11:407

Spectrum bias occurs when discovery cohorts include extreme
phenotypes instead of clinically ambiguous cases, a phenomenon
long recognized in diagnostic test evaluation. 180,181 This in ﬂates
apparent discrimination while underestimating real-world diag-
nostic complexity. In screening and early diagnosis settings,
spectrum bias is particularly harmful because patterns of disease
prevalence and comorbidity differ sharply from compiled datasets.
Dataset shift occurs when relationships between features and
outcomes vary across populations, time periods, or care settings.
Shifts can re ﬂect demographic differences, evolving clinical
guidelines, changes in treatment models, or technology updates.
Models that exploit misleading correlations, such as site identi ﬁers
or acquisition artifacts, may perform well in development cohorts
but degrade rapidly under deployment. 139,182
Confounding factors related to treatment are common in
prognostic and response-predictive biomarkers. 183 When treat-
ment assignment depends on disease severity or physician
assessment, outcome relationships may re ﬂect treatment effects
rather than the intrinsic biology of the disease. Without careful
causal framing, AI models may learn to predict treatment patterns
rather than disease trajectories.
Label noise and endpoint ambiguity are common in datasets
derived from EHRs. Diagnoses may be inconsistently coded,
outcomes may depend to documentation practices, and surrogate
endpoints may not re ﬂect meaningful clinical situations. Models
trained on noisy or surrogate labels may learn institutional
workﬂows rather than pathophysiology. 184
Multicenter generalization failures re ﬂect incomplete harmoni-
zation, unrecognized protocol differences, and demographic
heterogeneity.4,135,185 Even modest changes in imaging para-
meters, sample processing, or ﬁrmware can destabilize biomarker
signals if models are not explicitly trained for robustness. These
failure modes are often driven by biological variability, hetero-
geneity in clinical practice, and data generation processes rather
than algorithmic limitations alone. Consequently, improvements
in model architecture cannot fully compensate for weaknesses in
study design, cohort selection, or validation strategy.
To explain why many AI-based biomarkers fail to progress
beyond the discovery or early validation phase, Table 5
summarizes common failure modes in biomarker methods, their
corresponding mitigation strategies, and proposed validation
practices.
Generating biomarker evidence at the regulatory level
The transition from research-level biomarkers to regulatory-
acceptable tools requires a shift in development culture from
exploratory modeling to controlled evidence generation. There
are several principles that distinguish regulatory-level biomarker
processes from academic discovery studies. 186 Evidentiary require-
ments for biomarker quali ﬁcation continue to evolve across
regulatory jurisdictions. 187 Regulatory agencies are increasingly
promoting collaborative frameworks to accelerate biomarker and
AI validation pathways. 188
First, pre-speci ﬁcation of protocols is essential. Intended use,
endpoints, inclusion criteria, preprocessing processes, and evalua-
tion metrics must be de ﬁned before starting the analysis. Pre-
speciﬁcation limits analytical ﬂexibility and supports the interpret-
ability of results by reducing selective reporting. Second, model
locking is necessary before prospective or pivotal validation.
Continuous tuning during evaluation weakens evidence integrity
and obscures true performance. Locked models enable repeatable
auditing and meaningful performance comparison between
different centers. Third, auditability and traceability must be
integrated into data and model processes. Version control of
Table 5. Common failure modes and proposed mitigation strategies in AI-based biomarker discovery
Failure mode What it looks like Most
affected
methods
Why it matters Practical mitigations Evidence stage
where it must be
addressed
Batch effects/site
effects
Signature tracking points focus on
the center/platform rather than
biology
Omics, EVs,
Imaging
External validation
failure
Harmonized SOPs; batch-aware
modeling; leave-site-out exclusion
testing
External veri ﬁcation
+ robustness
Spectrum bias Trained in “clean” endpoints; fails in
mixed reality clinics
All In ﬂated AUC; poor
calibration
Sequential sampling; spectrum-
aware evaluation; subgroup
reporting
External +
prospective
Tag noise/
endpoint
ambiguity
Misdiagnosis, inconsistent labels,
weak underlying reality
EHR,
Imaging,
Digital
Unstable biomarkers;
low clinical
conﬁdence
Adjudication; multi-rater labels;
sensitivity analyses
Robustness +
prospective
Leakage (temporal
or data leakage)
Future-oriented information in
training; duplicate across splits
EHR, Omics Unrealistic
performance
Patient-level splitting; strict
temporal splits; leakage audits
Discovery → all
stages
Treatment-related
confounding
factors
Biomarkers re ﬂect treatment
exposure, not disease
EHR, Omics Failure in novel
application models
Pre-treatment sampling; causal
adjustment; target trial emulation
Prospective+ utility
Workﬂow
confounding
factors
Model learns care pathways (test
intensity)
EHR Nontransferable
biomarkers
Model input constraint; causal
checks; multi-site validation
External +
prospective
Missingness bias “Missing” severity or reach is
encoded
EHR,
Digital
Biased prediction Model missingness explicitly;
multiple imputation; sensitivity
tests
Robustness
Dataset shift/drift Population or measurement
changes over time
All Performance decay,
safety issues
Monitoring, recalibration, change
control plans
Post-deployment
Lack of biological
integrity
Features are not mapped to
pathways/cell states
Omics, EVs Low therapeutic
signiﬁcance
Pathway priors; network models;
perturbation/replication tests
Mechanistic
validation
Poor portability Works only in one ethnicity/region All Equity harm Diverse cohorts; subgroup
calibration; fairness reporting
External +
prospective
Key references for this table: refs. 140,288–291
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
16
Signal Transduction and Targeted Therapy          (2026) 11:407

datasets, preprocessing scripts, model parameters, and evaluation
code is increasingly expected by regulators and journal reviewers.
Audit trials also support post-deployment monitoring and
deviation detection. Fourth, change management for adaptive
systems must be prede ﬁned. For AI systems that are updated over
time, regulators emphasize prede ﬁned change protocols that
specify what types of updates are permitted, how performance
will be re-evaluated, and when recerti ﬁcation is required. This total
product lifecycle (TPLC) perspective addresses validation con-
tinuously, rather than episodically. Considering the TPLC, regula-
tors expect prede ﬁned update guidelines, traceability, and post-
market performance monitoring plans for AI-powered device
software functions (US Food and Drug Administration, 2021; US
Food and Drug Administration, 2025). 189,190
Finally, clinical integration studies are necessary to demonstrate
that biomarker outputs can be reliably used by clinicians and that
workﬂow, interpretability, and turnaround times are consistent
with application realities. Without such evidence, even analytically
powerful biomarkers may fail to achieve adoption.
Together, these principles shift biomarker development from
retrospective pattern recognition toward structured evidence
generation capable of supporting regulatory evaluation, clinical
decision-making, and real-world implementation.
To distinguish clinically established applications from promising
but still developing approaches, Table 6 summarizes the current
evidence status of major AI-powered biomarker strategies in
translational use cases.
CROSS-DISEASE APPLICATIONS (SYNTHESIS, NOT CATALOG)
Although disease-speciﬁc biology shapes biomarker selection and
clinical goals, the most informative cross-domain comparison is
not simply which biomarkers are used, but which combinations of
methods, AI strategies, and biologically grounded frameworks are
closest to clinical application. Recurring challenges related to
validation, confounding factors, portability, and work ﬂow integra-
tion are evident across all domains, supporting the need for
uniﬁed methodological and regulatory frameworks. To facilitate
cross-disease comparison, Table 7 summarizes the dominant
biomarker methods, dominant AI approaches, major clinical
applications, and key translation barriers across representative
disease categories.
Despite disease-speci ﬁc biological differences, recurring chal-
lenges regarding validation, confounding factors, and clinical
integration are evident across all ﬁelds, supporting the need for
uniﬁed methodological and regulatory frameworks.
Cardiovascular diseases
Cardiovascular biomarker discovery integrates circulating mole-
cular markers, multi-omics pro ﬁling (genomics, proteomics,
metabolomics), immune-in ﬂammatory phenotyping, quantitative
cardiac imaging, and increasingly digital physiological monitoring.
Plasma proteomics and metabolomics capture systemic in ﬂam-
mation, metabolic stress, and extracellular matrix remodeling
associated with the progression of atherosclerosis and heart
failure, while CMR and CCTA provide organ-level phenotypes of
myocardial remodeling, plaque composition, and perivascular
inﬂammation.31,191,192 Imaging-derived In ﬂammatory biomarkers
have also shown prognostic value for residual cardiovascular
risk.193
Wearable and ECG-based biomarkers further expand this
framework by enabling longitudinal detection of arrhythmia,
decompensation, and dynamic cardiometabolic risk. While
ensemble models and regularized regression remain useful for
tabular biomarker panels, deep learning is particularly effective in
ECG and cardiovascular imaging, where spatial and temporal
structure encodes clinically signi ﬁcant phenotypes. 194,195 Large-
scale plasma proteomics studies continue to identify novel
pathways associated with the development and progression of
heart failure. 196 Multimodal learning is increasingly used to
integrate imaging, omics, and clinical data, although performance
gains are largely dependent on harmonization across institutions
and devices.
Mechanistically, most informative cardiovascular biomarker
programs focus on immune-in ﬂammatory activation, endothelial
dysfunction, ﬁbrotic remodeling, thrombosis, and metabolic stress.
Pathway-level analyses correlate circulating and tissue-derived
biomarker with cytokine signaling, extracellular matrix turnover,
lipid processing, and mitochondrial dysfunction, all of which
contribute to plaque instability and myocardial remodeling. 131
Current clinical use includes ECG-based screening for left
ventricular dysfunction and atrial ﬁbrillation, multi-marker risk
stratiﬁcation for adverse cardiovascular outcomes, phenotyping of
heart failure subtypes, and longitudinal monitoring via wearable
or implantable sensors. 80,194 The main translational barrier is not
the lack of a predictive signal, but rather its instability across
scanners, institutions, treatment contexts, and real-world popula-
tions. Many cardiovascular AI biomarkers perform well in carefully
selected cohorts, but experience performance degradation in
situations such as dataset drift, treatment confounding, and
disparities in device access. For meaningful therapeutic integra-
tion, biomarkers need to demonstrate external validity, calibration
stability, and utility at the decision level, especially when used for
trial enrichment and identifying modi ﬁable in ﬂammatory or
ﬁbrotic pathways for targeted intervention.
Oncology (tumor-immune ecosystems, liquid biopsy signatures,
response)
Oncology biomarker discovery is inherently multimodal, integrat-
ing tumor genomics and transcriptomics, immune microenviron-
ment pro ﬁling, circulating tumor DNA (ctDNA), EV content, and
quantitative imaging phenotypes. Tissue-based molecular pro ﬁl-
ing remains fundamental for identifying oncogenic drivers and
resistance mechanisms, while liquid biopsy approaches enable
non-invasive longitudinal monitoring of tumor burden, clonal
evolution, and minimal residual disease (MRD). Accumulation
evidence indicates that ctDNA-based MRD detection is emerging
as a robust biomarker for early recurrence and treatment response
across multiple cancer types, including colorectal, lung, and breast
cancers.56,58,197,198 Recent systematic reviews, meta-analyses, and
comparative assessments of tumor-informed and tumor-agnostic
approaches have further strengthened the evidence base for
ctDNA-guided MRD assessment. 199–202 Genomic MRD strategies
are increasingly being integrated into precision oncology work-
ﬂows.203 Tumor-agonistic MRD approaches have also shown
promising results in non-small cell lung cancer. 204 Individual
clinical reports continue to demonstrate the feasibility of MRD
monitoring in hereditary cancer syndromes. 205
Immune biomarkers, including spatial immune context, T cell
receptor diversity, cytokine schedules, and myeloid polarization,
are central to predicting immunotherapy response. Whereas
imaging and digital pathology provide spatially resolved repre-
sentations of tumor-immune architecture. EV-based biomarkers
offer potential for early detection and resistance monitoring,
although test standardization and interlaboratory reproducibility
remain signi ﬁcant translational barriers. 67
AI methods in oncology re ﬂect the multimodal nature of
modern cancer biology. Deep learning has demonstrated
particular utility in digital pathology and radiological imaging.
On the other hand, multimodal architectures integrating mole-
cular, imaging, and clinical information are increasingly supporting
prognostic assessment and treatment response predic-
tion.103,106,206 However, robust clinical implementation depends
on external validation, standardization, and prospective demon-
stration of clinical utility. Multimodal fusion architectures incor-
porating histological, genomic, and clinical features are
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
17
Signal Transduction and Targeted Therapy          (2026) 11:407

Table 6. Representative evidence status of selective AI-enabled biomarker strategies in translational use cases
Biomarker strategy/
domain
Typical data modality Current evidence
status
Main translational use Main limitation Validation requirement before
broad clinical use
Representative
references
Autonomous diabetic
retinopathy screening
Fundus imaging Proven Screening/Triage Device, population, and work ﬂow
transportability
Prospective deployment studies,
external validation, work ﬂow
integration
281
AI-assisted ECG
phenotyping (e.g., AF, low
EF, diabetes risk)
ECG + clinical metadata Proven to
emerging
Screening, early diagnosis, risk
stratiﬁcation
Calibration drift, prevalence
dependence, implementation
variability
External validation, calibration,
decision curve or work ﬂow
beneﬁt analyses
80,194,292
Imaging radiomics for
oncological risk
stratiﬁcation
CT/MR/PET imaging Emerging Prognosis, response
prediction, trial enrichment
Limited reproducibility, site/
scanner variability, weak external
validation
Multicenter harmonization,
external validation, prospective
utility studies
12,14,77
ctDNA minimal residual
disease monitoring
Liquid biopsy Emerging to
proven (context-
dependent)
Recurrence detection,
treatment monitoring, trial
adaptation
Tumor type dependence, assay
sensitivity, false positive/negative
results, context-of-use constrained
Analytical validation, prospective
clinical utility, disease-speci ﬁc
implementation studies
58,197,210,211
Multi-omics pathway-state
biomarkers
Genomics/
transcriptomics/
proteomics/
metabolomics
Emerging Patient strati ﬁcation,
mechanism inference, therapy
selection
Batch effects, over ﬁtting,
incomplete pathway knowledge
External validation, robustness
testing, perturbation/
mechanistic support
11,47,89
Digital pathology/
computational histology
biomarkers
Whole slide histology Emerging Diagnostic support, subtype
classiﬁcation, biomarker
discovery
Staining/site shift, annotation
dependence, pathologist work ﬂow
integration
Multi-site validation, reader-
assisted studies, deployment
evaluation
87,104,206
Spatial omics and single-
cell AI biomarkers
Single-cell and spatial
transcriptomics/
proteomics
Emerging Cellular state mapping, tissue
programming, target discovery
Cost, sparsity, technical
heterogeneity, limited clinical
standardization
Cohort replication, orthogonal
biological validation, clinical
relevance testing
36,41,42
Wearable/digital
biomarkers
Continuous sensor data,
smartphones
Emerging Monitoring, ﬂare prediction,
risk estimation
Signal noise, adherence, device
heterogeneity, behavioral
dependence
Longitudinal prospective
validation, addressing missing
data, implementation studies
79,262,293
Perturbation informed
pathway biomarkers
CRISPR, drug
degradation, stimulation
assays
Emerging Target prioritization, resistance
mapping, therapeutic
hypothesis generation
Experimental context mismatch,
sparse perturbation coverage
Orthogonal validation, in vivo
translation, pathway consistency
testing
116,152,207
Foundational model/
simulation-guided
biomarkers
Multimodal large-scale
data, virtual
representations
Speculative General purpose biomarker
discovery, virtual clinical trial
support, adaptive modeling
Limited prospective validation,
opaque failure modes, uncertain
clinical utility
Benchmarking, external
validation, prospective decision
studies
101,107,276
Proven = supported by prospective validation through regulatory approval and/or clinical practice in de ﬁned contexts; Emerging = supported by external validation and increasing translational evidence, but
prospective bene ﬁt and work ﬂow integration are under evaluation; Speculative = proof-of-concept or early translational stage, requiring signi ﬁcant experimental and clinical validation before routine use
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
18
Signal Transduction and Targeted Therapy          (2026) 11:407

continuously improving treatment response and survival predic-
tion by re ﬂecting the hierarchical organization of tumor biology.
Mechanistically, the most informative oncology biomarkers
capture tumor-immune ecosystem states rather than isolated
tumor-intrinsic changes. Single-cell and spatial analysis reveal
coordinated programs of immune exclusion, T-cell depletion,
stromal activation, angiogenesis, and metabolic adaptation
shaping treatment response. AI-enabled network and perturbation
models facilitate mapping of biomarker signatures to pathways
governing DNA repair, immune evasion, epigenetic plasticity, and
drug tolerance. 207,208 Mechanistic relevance is stronger than
relying solely on post-exposure feature attribution when biomar-
ker signals are consistent across molecular, cellular, and tissue
scales and align with experimentally validated resistance
mechanisms.
Clinically, AI-derived oncology biomarkers support diagnosis,
prognosis, treatment selection, and disease monitoring. Digital
pathology models can aid tumor classi ﬁcation by extracting
molecular subtypes from routine slides and enable prioritization of
molecular testing. 206 Integrated multimodal signatures improve
prognostic classiﬁcation beyond traditional staging, while immune
and pathway-level biomarkers guide the selection of checkpoint
inhibitors and targeted therapies. Elevated systemic in ﬂammatory
markers have also been shown to be associated with reduced
beneﬁt obtained from immune checkpoint blockade. 209 ctDNA
dynamics enable early detection of relapse and emerging
resistance, often preceding radiographic progression, and are
increasingly being considered as surrogate endpoints in clinical
trials.136,210,211 However, the regulatory characterization of such
endpoints, particularly for MRD-based decision-making, remains.
Despite rapid progress, signi ﬁcant clinical adoption barriers
persist. The integration of biomarkers into routine clinical practice
remains an ongoing challenge across all specialties. 212 These
include interlaboratory variability in pathology processing and
imaging, differences in scanners and staining, the effects of tumor
purity on molecular measurements, and the evolution of tumor
biology due to treatment, which limits the validity of static
biomarkers. Liquid biopsy sensitivity is in ﬂuenced by tumor
burden, vascularization, and anatomical context, which restricts
its use for universal early diagnosis. More generally, many AI
biomarkers demonstrate strong retrospective performance but fail
to prospectively improve clinical outcomes due to treatment
confounding, biological heterogeneity, and inadequate integra-
tion into clinical work ﬂows. Therefore, reliable clinical practice
requires standardized tests, externally validated models,
predeﬁned analytical processes, and a clear demonstration of
added value compared to existing molecular diagnostic methods.
Biomarker-driven strategies should ultimately be compatible with
viable therapeutic pathways and evaluated within prospective,
decision-driven study designs.
Neurodegenerative disorders (early diagnosis, progression, and
multimodal integration)
Neurodegenerative biomarker discovery increasingly integrates
liquid biomarkers, neuroimaging phenotypes, genetic risk pro ﬁl-
ing, EV content, and digital behavioral measurements. Key
biomarker modalities include plasma biomarkers, advanced
neuroimaging, extracellular vesicle cargo, and digital behavioral
measurements. All of which together support earlier diagnosis and
long-term disease monitoring. 67,213–217 Digital biomarkers derived
from speech, gait, and cognitive testing further extend this
framework by enabling high-frequency monitoring of functional
decline, albeit with limited cross-platform validation.
AI approaches re ﬂect this multimodal structure. DL models are
particularly effective for neuroimaging, capturing spatial patterns
of atrophy, connectivity disruption, and ligand distribution across
disease stages. They often outperform traditional morphometric
methods in classi ﬁcation and progression. 218
For molecular and clinical data, ensemble and Bayesian
approaches enable calibrated integration of plasma, cerebrospinal
ﬂuid, genetic, and demographic characteristics. Multimodal fusion
models combining imaging and molecular data improve the
prediction of transition from mild cognitive impairment to
dementia and support disease subtyping; however, generalization
is sensitive to scanner protocols, cohort composition, and real-
world variability. 67
Mechanistically, the most informative neurodegenerative
biomarkers capture interactions among protein aggregation,
synaptic insuf ﬁciency, neuroin ﬂammation, vascular dysfunction,
and glial activation. Growing evidence supports the central role
of neuroin ﬂammation in the progression of neurodegenerative
disease.219 Single-cell and spatial transcriptomic studies high-
light microglial activation programs, astrocytic in ﬂammatory
states, and complement-mediated synaptic pruning as factors
contributing to regional vulnerability and disease progres-
sion.220,221 AI-assisted network analyses offer a more integrated
perspective on disease biology by correlating circulating and
imaging-derived biomarkers wit h pathways governing proteos-
tasis, mitochondrial stress, lip id metabolism, and blood-brain
barrier (BBB) integrity. Importantly, biomarkers re ﬂecting
Table 7. Cross-disease comparison of AI biomarker translation
Disease domain Dominant biomarker
modalities
Predominant AI
approaches
Principal mechanistic
insight
Key clinical applications Major translation
barriers
Cardiovascular Imaging, plasma
proteomics,
inﬂammation
CNNs, ensembles,
multimodal fusion
Plaque instability, ﬁbrosis,
thrombosis pathways
Risk classi ﬁcation, heart failure
phenotyping
Dataset shift,
treatment
confounding
Oncology ctDNA, pathology,
immune pro ﬁling
Transformers,
foundation models
Tumor-immune
ecosystems, resistance
Treatment selection, monitoring
of minimal residual disease
Biological
heterogeneity
Neurodegenerative PET/MRI, plasma p-tau,
EVs
CNNs, Bayesian
fusion
Glial activation, synaptic
loss
Early diagnosis, progression
monitoring
Mixed pathology
Autoimmune scRNA, cytokines,
imaging
Graph models,
clustering
Immune cell programs,
cytokine circuits
Treatment response,
exacerbation prediction
Tissue and blood
incompatibility
Metabolic Multi-omics, imaging,
digital
Ensembles,
representation
learning
Lipotoxicity, ﬁbrogenesis Fibrosis risk, lifestyle response Behavioral
confounding
Infection Host transcriptomics,
EHR time series
Time series DL,
sparse ML
Immune dysregulation
and hyperin ﬂammation
Worsening prediction Rapid dataset shift
Key references for this table: refs. 11,21,213,294
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
19
Signal Transduction and Targeted Therapy          (2026) 11:407

neuroinﬂammatory and vascular processes can capture modi ﬁ-
able disease processes beyond amyloid and tau load, particularly
in mixed and vascular dementia phenotypes.
Clinically, AI-powered biomarkers support early diagnosis,
prognostic strati ﬁcation, disease classi ﬁcation and longitudinal
monitoring. Plasma and imaging markers enable the identi ﬁcation
of preclinical or prodromal disease states, while multimodal
models improve differentiation between Alzheimer ’s disease,
Lewy body disease, frontotemporal dementia, and mixed pathol-
ogies. Biomarkers are increasingly used in clinical trials for
participant selection, disease staging, and pharmacodynamic
assessment. However, characterizing them as surrogate endpoints
is insuf ﬁcient and limits their role in regulatory decision-making
processes. One of the biggest obstacles to the widespread
adoption of blood-based Alzheimer ’s biomarkers remains the
practical application challenges. 222 The fundamental clinical
adoption barrier is biological and clinical heterogeneity: mixed
pathologies, comorbidities, and population diversity complicate
biomarker speciﬁcity and generalizability. Many AI models trained
on select datasets fail to consistently perform in community
settings where diagnostic uncertainty and multiple diseases are
prevalent. Therefore, reliable clinical practice requires consistent
testing and imaging protocols, representative validation cohorts,
and demonstration that biomarker-driven strategies improve not
only diagnostic accuracy but also clinical decision-making
processes.
Autoimmune and in ﬂammatory diseases (immune-state
biomarkers, therapeutic strati ﬁcation)
Autoimmune and in ﬂammatory diseases are characterized by
dysregulated immune activation across innate and adaptive
compartments; this makes immune cell phenotyping, cytokine
proﬁling, autoantibody repertoires, transcriptomic signatures cen-
tral biomarker modalities. Single-cell and bulk RNA sequencing
captures heterogeneity in interferon signaling, T and B cell
activation, and myeloid polarization, revealing disease- and tissue-
speciﬁc immune programs in conditions such as rheumatoid
arthritis, systemic lupus erythematosus, in ﬂammatory bowel
disease, and multiple sclerosis.132,223,224 AI methods are increasingly
used to integrate heterogeneous metabolic, imaging, and beha-
vioral data for risk strati ﬁcation and treatment response assess-
ment.225,226 Nevertheless, performance often remains sensitive to
cohort composition, reference standards, and healthcare system-
speciﬁc factors. Therefore, effective clinical adoption requires
standardized testing, consistent single-cell pipelines, and prospec-
tive validation demonstrating that biomarker-guided treatment
selection improves outcomes compared to empirical treatment
strategies.
Metabolic disorders (multimodal metabolic phenotyping and
ﬁbrosis-risk strati ﬁcation)
Metabolic disorders, including type 2 diabetes and MASLD/MASH
(Metabolic Dysfunction-Associated Steatotic Liver Disease) are
systemic conditions. These conditions include cardiometabolic
comorbidities such as adipose tissue dysfunction, insulin resis-
tance, hepatic steatosis, and ﬁbrogenesis, and therefore multi-
modal biomarker integration is essential. Informative biomarker
frameworks combine routine clinical chemistry, multi-omics
(genomics, proteomics, metabolomics), in ﬂammatory and immune
markers, non-invasive imaging or ﬁbrosis scores, and increasingly
digital physiological and behavioral data. In MASLD/MASH,
biomarker development focuses on identifying clinically signi ﬁ-
cant ﬁbrosis risk and treatment-responsive disease states using
non-invasive tools supported by omics and imaging. 227–229
Advanced metabolomic signatures have recently improved the
identiﬁcation of patients at risk of progressive MASH. 230,231
Updated disease terminology and diagnostic frameworks continue
to reshape biomarker development studies in steatotic liver
disease.232 Machine learning analysis of gut microbiota signatures
may further support the diagnosis of MASLD. 233
Mechanistically, metabolic biomarkers re ﬂect the interaction of
adipose tissue in ﬂammation, hepatic lipotoxicity, insulin signaling
disruption, mitochondrial stress, and ﬁbrogenesis remodeling, and
multi-omics studies reveal coordinated pathway-level changes
that capture disease heterogeneity better than single mar-
kers.234,235 Recent multi-omics studies have identi ﬁed the under-
lying biological pathways of childhood obesity and metabolic
dysfunction.236 Adipose tissue-microbiome interactions appear to
play a central role in de ﬁning metabolic obesity phenotypes. 237
Obesity-related in ﬂammation and its resolution pathways con-
tinue to emerge as promising biomarker targets. 238
AI approaches, including ensemble models and representative
learning, are used to integrate heterogeneous data sources and
improve the prediction of metabolic risk, disease progression, and
treatment response; however, performance gains are often
cohort-dependent and sensitive to reference standard variabil-
ity.32,239,240 Digital biomarkers derived from wearable devices,
including activity, sleep, and glucose dynamics, extend metabolic
phenotyping to longitudinal tracking, but are still affected by
adherence, device variability, and behavioral confounding factors.
Clinically, AI-derived metabolic biomarkers are used in risk
stratiﬁcation, complication prediction, ﬁbrosis assessment, and
treatment monitoring, and are increasingly being investigated for
trial enrichment by identifying patients with active target path-
ways. However, translation is limited by dataset shifts across
health systems, treatment and lifestyle confounding factors,
variability in reference standards such as liver histology, and poor
portability from speci ﬁc cohorts to larger populations. 241 There-
fore, reliable clinical practice requires standardized processes,
external validation across care settings, calibration reporting, and
demonstration that biomarker-guided decisions improve out-
comes in real-world metabolic care pathways.
Infectious diseases and host-response states (dynamic biomarkers
and stress testing of translation)
Infection and sepsis present a challenging test case for biomarker
translation due to rapidly evolving biological and clinical
conditions, including pathogen variability, treatment timing, and
changing care practices. Recent reviews continue to identify
signiﬁcant unmet needs in the discovery and validation of sepsis
biomarkers.242 The most informative biomarkers re ﬂect host
response states, including cytokine and chemokine pro ﬁles,
immune cell activation markers, and transcriptomic signatures
that capture the balance between hyperin ﬂammation and
immunosuppression.243,244 AI approaches often integrate electro-
nic health record time series with host response data to predict
clinical deterioration and course changes rather than static
diagnosis. Machine learning approaches have identi ﬁed additional
candidate biomarkers associated with immune dysregulation at
various stages of sepsis. 245 Mechanistically, these biomarkers
capture coordinated immune programs involving interferon
signaling, myeloid activation, lymphocyte dysfunction, and
endothelial damage, but interpretation is complex due to strong
treatment and timing confounding factors. In clinical use, the
focus is on early risk strati ﬁcation, immunophenotype classi ﬁca-
tion, and monitoring of treatment response. However, infectious
diseases consistently reveal fundamental failure modes of AI
biomarkers, such as rapid dataset drift, label instability, and poor
cross-reproducibility. Therefore, robust real-world implementation
requires time-sensitive validation, standardized processes, and
explicit handling of treatment effects, highlighting that the
biomarker utility depends on stability in evolving clinical settings
rather than performance on static datasets.
While speci ﬁc biomarkers and data modalities differ substan-
tially across disease domains, the determinants of successful
translation are remarkably consistent. Biomarkers with the
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
20
Signal Transduction and Targeted Therapy          (2026) 11:407

greatest clinical impact are those that are biologically plausible,
have external validation, are reproducibly measurable, and
provide a clear level of bene ﬁt at the decision-making level.
Conversely, common causes of failure include dataset drift,
treatment confusion, biological heterogeneity, and inadequate
integration into clinical work ﬂows. These recurring patterns
demonstrate that disease-speci ﬁc innovation alone is insuf ﬁcient
and that progress toward clinical implementation depends on
shared methodological and regulatory principles applicable across
biomarker domains (Fig. 6).
TRANSLATIONAL ROLES OF AI BIOMARKERS IN THERAPEUTIC
DEVELOPMENT AND CLINICAL DECISION-MAKING PROCESSES
Moving from purely predictive markers to biologically based and
therapeutically applicable biomarkers requires the explicit inte-
gration of mechanistic modeling and validation, as conceptually
shown in Fig. 7.
Biomarkers for study enrichment, adaptive designs, and outcome
selection
AI-derived biomarkers are increasingly being used to enrich
clinical trials by selecting patient subgroups that are more likely to
express targetable disease biology or demonstrate measurable
progression within feasible follow-up periods. In oncology, ctDNA
dynamics, immune phenotypes, and tumor microenvironment
signatures are used to identify biologically responsive subgroups,
increase statistical power, and reduce sample size require-
ments.246,247 A key example is the TIDE framework, which predicts
response to immune checkpoint blockade by integrating signa-
tures of T cell dysfunction and exclusion, demonstrating how
biologically informed computational biomarkers can support
patient enrichment and treatment strati ﬁcation.248 Similarly, the
IMPRES framework further supports the value of mechanistically
informed biomarker signatures in therapeutic decision-making by
showing that immune interaction patterns can strongly predict
response to checkpoint inhibitor therapy in melanoma cohorts. 249
In neurodegenerative and metabolic diseases, enrichment
strategies often address the dilution of treatment effects in
heterogeneous populations by focusing on selecting individuals
with biomarker-validated pathology or rapid progression
trajectories.214,228
Figure 8 illustrates how AI-enabled biomarkers can support
enrichment, strati ﬁcation, longitudinal tracking, and adaptive
treatment modi ﬁcation in modern clinical trial designs.
Adaptive clinical trial designs are increasingly integrating
biomarker feedback to modify enrollment criteria, randomization
ratios, or treatment arms during trial execution. AI models
predicting early response or toxicity can support response
adaptive randomization and Bayesian borrowing among sub-
groups, but operational complexity and regulatory acceptance
remain limiting factors. 250 Importantly, to avoid bias in treatment
effect prediction, biomarker-driven enrichment should avoid
selection based on post-randomization variables.
Fig. 6 Cross-disease AI biomarker applications. Examples of biomarker-driven applications across cardiovascular, oncology, neurodegenerative,
autoimmune, metabolic, and infectious diseases. Despite disease-speci ﬁc objectives, all applications rely on shared methodological foundations,
including multimodal integration, baseline models, external validation, and clinical bene ﬁt assessment. Figure created by the authors using Adobe
Illustrator (Version 29.3.1). AI arti ﬁcial intelligence, ECG electrocardiogram, NETs neutrophil extracellular traps, ctDNA circulating tumor DNA, NfL
neuroﬁlament light chain, p-tau phosphorylated tau, TRIPOD + AI Transparent Reporting of a multivariable prediction model for Individual
Prognosis or Diagnosis with AI extension, PROBAST + AI The prediction model Risk Of Bias ASsessment Tool with AI-extended
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
21
Signal Transduction and Targeted Therapy          (2026) 11:407

Endpoint selection represents another crucial translational
role for AI biomarkers. Imagi ng-derived radiomic features,
molecular response scores, and d igital functional endpoints are
being considered as intermediate or surrogate endpoints to
accelerate drug development. However, regulatory acceptance
requires evidence that biomarker modi ﬁcations reliably predict
clinical bene ﬁtr a t h e rt h a nm e r e l yr eﬂecting pharmacodynamic
activity. While predictive biomarkers can improve enrichment
and risk strati ﬁcation, mechanistically grounded biomarkers are
more likely to provide informat ion about drug targeting and
adaptive therapy strategies. Table 8 compares these paradigms
in terms of interpretability, validation requirements, and
therapeutic bene ﬁt.
Accompanying diagnosis: linking AI biomarkers to treatment
selection
Beyond trial enrichment, AI biomarkers are increasingly function-
ing as complementary or accompanying diagnostic tools, linking
patients to targeted therapies or combination strategies. In
oncology, predictive biomarkers derived from tumor genomics,
immune context, and ctDNA dynamics inform the selection of
targeted agents, immunotherapies, and rational combina-
tions.248,249,251,252 AI models integrating these layers can identify
resistance mechanisms and suggest adaptive treatment strategies
during therapy. Recently, graph-based and multimodal learning
approaches have further improved treatment response prediction
by integrating molecular features with biological relationships and
clinical context, thereby enhancing both prediction performance
and biological interpretability. 142,224
In autoimmune and in ﬂammatory diseases, immune status
biomarkers can guide the selection between biological drugs and
small molecule inhibitors by identifying dominant cytokine or cell
type pathways, potentially reducing the empirical treatment
cycle.225 In cardiovascular and metabolic diseases, phenotypic
clusters arising from in ﬂammatory, ﬁbrotic, or metabolic signa-
tures may shed light on the use of anti-in ﬂammatory, anti ﬁbrotic,
or metabolic modulating therapies, but clinical implementation is
still in its early stages.
Dose optimization and treatment sequencing offer additional
opportunities for biomarker-guided therapy. 253 Longitudinal
biomarker trajectories may reveal inadequate target interaction
or the risk of early relapse and may support proactive dose
adjustment or treatment escalation. However, most AI-assisted
treatment selection frameworks are observational and require
prospective validation to demonstrate clinical bene ﬁt.
Biomarkers as surrogate endpoints: when do they succeed and
why do they fail?
The use of biomarkers as surrogate endpoints remains contro-
versial, particularly in chronic and heterogeneous diseases.
Successful surrogate endpoints should lie on the causal pathway
between intervention and clinical outcome and capture the
dominant mechanism of therapeutic effect. 115,254,255 Classic
examples include viral load suppression in HIV and blood pressure
Fig. 7 Conceptual transition from predictive to mechanistically grounded AI biomarkers. Correlation-based biomarkers provide predictive
signatures but are often lack biological interpretability. Mechanistically informed biomarkers may better support therapeutic decision-making and
clinical application by integrating biological context, causal reasoning, and pathway-level understanding. Figure created by the authors using
Adobe Illustrator (Version 29.3.1)
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
22
Signal Transduction and Targeted Therapy          (2026) 11:407

reduction in cardiovascular disease, where strong causal links exist
between biomarker change and clinical events.
Historical experience in therapeutic ﬁelds shows that only a
small subset of biomarkers reliably functions as surrogate
endpoints. Table 9 summarizes representative examples, high-
lighting the biological conditions under which surrogate strategies
succeed or fail.
These examples demonstrate that biomarker performance as a
surrogate endpoint depends primarily on biological causality
rather than measurement precision. Biomarkers that directly
capture dominant disease mechanisms are more likely to predict
clinical bene ﬁt. Otherwise, markers that re ﬂect only partial or
downstream aspects of disease biology often fail despite strong
statistical associations. AI can improve biomarker sensitivity,
Fig. 8 Biomarker-guided adaptive clinical trial design: AI-enabled biomarker enrichment is used to identify high-probability responders, stratify
enrollments, and guide treatment allocation. Longitudinal biomarker monitoring supports adaptive decisions, including sample size re-estimati on,
arm modi ﬁcation, dose adjustment, and endpoint re ﬁnement. Continuous feedback improves trial ef ﬁciency and therapeutic accuracy. Figure
created by the authors using Adobe Illustrator (Version 29.3.1)
Table 8. Predictive and mechanistically grounded AI biomarkers: Translative implications
Dimension Predictive biomarkers Mechanistically grounded biomarkers
Primary goal Outcome prediction Biological program/pathway inference
Typical outputs Risk score, classi ﬁer, latent signature Pathway activity, cell state program, network module
Dependence type Correlational association Causal/structural relationships (explicit or restricted)
Interpretability Often post hoc Direct biological interpretability (when validated)
Stability across therapies Often unstable More robust to treatment perturbations (if causal)
Trial enrichment Common, pragmatic Especially strong for especially mechanism-matched therapies
Treatment selection Limited Directly informative (companion/complementary role)
Potential surrogate endpoints Often weak Higher if tied to causal pathway
Emphasis on validation Discrimination/calibration Biological coherence + perturbation evidence + clinical utility
Key risk Spurious association leakage Over-claiming mechanism without experimental support
Best use case Screening/prognosis Drug development, strati ﬁcation, adaptive monitoring
Key references for this table: refs. 4,112,268,289
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
23
Signal Transduction and Targeted Therapy          (2026) 11:407

integration, and temporal resolution, but it cannot overcome the
weak causal relationships between biomarker modulation and
patient-relevant outcomes. Therefore, AI-derived surrogate bio-
markers should be evaluated within causal frameworks and
validated across interventions operating through diverse biologi-
cal mechanisms.
Longitudinal monitoring and dynamic treatment adaptation
AI-enabled longitudinal biomarker monitoring enables dynamic
assessment of disease course, treatment response, and relapse
risk. Time series models integrating molecular, imaging, and
digital biomarkers can detect early deviations from expected
response patterns and potentially enable preventive treatment
modiﬁcation.15 In oncology, serial ctDNA monitoring can identify
molecular relapse before radiographic progression, while in
metabolic diseases, continuous glucose and activity monitoring
support adaptive lifestyle and pharmacological interventions.
Longitudinal validation is still an underdeveloped area. Similar
challenges have recently been highlighted in the validation of
biomarkers of biological aging. 256
Longitudinal monitoring, especially when digital biomarkers are
included, also carries risks of overdiagnosis, alert fatigue, and
behavioral confounding. Therefore, effective clinical practice
requires careful calibration of alert thresholds, integration with
clinical work ﬂows, and continuous performance monitoring.
Real-world evidence (RWE) and post-implementation monitoring
After transitioning to clinical practice, AI biomarkers must be
evaluated under real-world conditions characterized by hetero-
geneous populations, evolving clinical practices, and variable
data quality. Real-world evidence (RWE) studies can assess
whether biomarker-guided decis ions improve outcomes, reduce
costs, or change treatment models compared to standard
care.257–259
Post-application monitoring should evaluate not only prediction
performance but also clinical impact, adverse events, and equity
among subpopulations. Model drift, test changes, and shifts in disease
epidemiology can degrade performance over time and may require
recalibration or retraining strategies under regulatory oversight.
More importantly, RWE can contribute to the improvement of
biomarker thresholds, decision rules, and patient selection criteria
by revealing discrepancies between controlled clinical trial
performance and real-world ef ﬁcacy. Continuously learning health
systems offer a framework for iterative improvement but require
governance structures that balance innovation with patient safety
and transparency.
Taken collectively, these applications demonstrate the transition
of AI biomarkers from discovery tools to clinical decision support
instruments. Their greatest value emerges when biological
interpretation, rigorous validation, therapeutic suitability, and
real-world performance are considered together, rather than as
separate objectives. Ultimately, successful implementation will
depend not only on predictive accuracy but also on demonstrable
improvements in patient outcomes, treatment selection, and
healthcare delivery.
REGULATORY, ETHICAL, AND IMPLEMENTATION
CONSIDERATIONS FOR AI-BASED BIOMARKERS (BIOMARKER-
FOCUSED; ALGORITHM + ANALYSIS COMBINED SYSTEM)
Biomarker characterization and algorithm validation: crossroads
and interaction
Since regulatory requirements depend on intended use, clinical
risk, and model adaptability, Fig. 9 summarizes a simpli ﬁed
decision tree regarding the FDA and EMA classi ﬁcation pathways
applicable to AI-based biomarker software and devices.
Regulatory evaluation of AI-based biomarkers requires char-
acterization of both the biological signal and the algorithmic
transformation applied to that signal. 187,260 Unlike traditional
biomarkers, AI biomarkers can integrate hundreds to thousands of
features across various methods, complicating biological inter-
pretability and analytical validation. Therefore, regulators are
increasingly emphasizing the need to de ﬁne intended use,
biological plausibility, and pathway relevance, especially when
biomarkers guide therapeutic decisions or serve as trial enrich-
ment tools. Algorithm validation must demonstrate stability across
clinically relevant subgroups, testing platforms, and disease
spectra. When biomarkers integrate multi-omics or imaging data,
analytical variability arising from upstream testing propagates into
model uncertainty, requiring joint validation of laboratory
procedures and algorithm performance. Interaction effects
between biomarkers and treatments (e.g., predictive and prog-
nostic roles) should also be clearly characterized to prevent
misapplication of biomarkers beyond their validated contexts.
Biomarker characterization also requires a clear de ﬁnition of the
Context of Use (COU), including the purpose for which the
biomarker will be applied, the patient population, and the clinical
decision-making context. Regulatory pathways for biomarkers
developed as drug development tools rather than diagnostic
devices differ from the SaMD or IVD/CDx frameworks; in this case,
the FDA Biomarker Quali ﬁcation Program (BQP) provides a
mechanism for formally qualifying biomarkers for speci ﬁc use
contexts in clinical trials and therapeutic development. 261
SaMD and AI governance for biomarker tools: locked versus
adaptive models
Many AI-enabled biomarker systems are classi ﬁed as SaMD when
used for clinical decision-making purposes. Since many AI
biomarker tools ﬁt the Software as a Medical Device (SaMD)
deﬁnition, regulatory expectations are increasingly emphasizing
lifecycle management, transparency of intended use, and
structured oversight of model updates. 189 Regulatory frameworks
distinguish between locked algorithms (which remain unchanged
after deployment) and adaptive or continuously learning systems
(which can be updated based on new data). While adaptive
models offer potential performance improvements, they also
present challenges related to version control, traceability, and
post-market surveillance.186,189 For adaptive biomarker algorithms,
the FDA has proposed the concept of a PCCP to de ﬁne permitted
updates, relevant validation/veri ﬁcation evidence, and post-
update monitoring expectations. 190 Since AI-powered biomarkers
are implemented through different regulatory and translational
Table 9. When do biomarkers succeed or fail as surrogate endpoints
Disease era Biomarker surrogate Biological rationale Outcome correlation Trial success? Reasons for success/failure.
HIV Viral load Direct causal driver Strong Yes Capture mechanism
Hypertension Blood pressure Mediator of vascular damage Strong Yes Linear causal pathway
Oncology Tumor shrinkage Tumor burden proxy Variable Mixed Resistance pathways
Alzheimer’s diseases Amyloid load Plaque hypothesis Weak Mostly no Downstream neurodegeneration
MASH Fibrosis scores Predicts mortality rate Moderate Emerging Slow biological response
Key references for this table: refs. 115,254,255,295,296
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
24
Signal Transduction and Targeted Therapy          (2026) 11:407

pathways depending on their intended use, Table 10 summarizes
the main categories related to clinical implementation, the
relevant evidence requirements, and representative application
contexts.
For biomarker applications, regulatory expectations generally
favor locked models for diagnostic and therapeutic decision
support, with prede ﬁned retraining and recerti ﬁcation pathways
for updates.187 While continuous learning may be more feasible in
low-risk monitoring contexts, reconciling it with traditional
validation paradigms remains challenging when biomarker thresh-
olds directly impact patient management. Navigating the
regulatory landscape for AI-based biomarkers requires systematic
assessment of the intended use, clinical risk level, and information
signiﬁcance.262
Data privacy, fairness, consent, and population equity in
multimodal biomarkers
AI biomarker development often relies on large-scale, multi-
modal datasets derived from vulnerable patient populations. 263
Genomic and imaging data increase the risks of re-identi ﬁcation,
while wearable and behavioral data raise concerns about
ongoing surveillance. Therefore, ethical practice requires robust
consent frameworks, transparency regarding secondary data
use, and safeguards against misuse beyond clinical intent.
Fairness is a critical regulatory and ethical issue, as biomarker
performance can differ signi ﬁcantly across ancestry groups,
socioeconomic strata, and contexts of access to healthcare.
Failure to assess and correct such disparities risks exacerbating
health inequalities, particularly when biomarkers determine
eligibility for expensive targeted therapies. Multiple ancestry
polygenic approaches can partially reduce ancestry differences
in biomarker performance. 264 Regulators expect subgroup
performance reporting and mitigation strategies when clinically
signiﬁcant disparities are observed. 265
Clinical work ﬂow integration, interpretability thresholds, and trust
Even analytically validated biomarkers can fail clinically if they
cannot be integrated into routine work ﬂows. Practical application
requires compatibility with laboratory information systems,
imaging platforms, and electronic health records, as well as
clearly deﬁned clinical action thresholds. For AI-enabled biomarker
systems that generate continuous risk scores, translating them
into actionable categories remains one of the biggest barriers to
adoption. Interpretability requirements are context-dependent:
mechanistic transparency may not be necessary for low-risk
screening tools, while therapeutic decision support often requires
the description of contributing features or biological pathways. 108
Importantly, over-reliance on post-annotations lacking a biological
basis can create false reassurance instead of true understanding.
Clinician trust is shaped not only by model performance but also
by perceived alignment with standards of clinical reasoning and
evidence.
Fig. 9 Regulatory pathway decision tree for AI-based biomarkers: the framework illustrates how the context of use determines FDA and EMA
regulatory classi ﬁcation pathways. Products for research-only use are separated from clinical decision support applications and are further
classiﬁed according to risk level and regulatory requirements. These include Class I –III pathways and biomarker quali ﬁcation programs. Figure
created by the authors using Adobe Illustrator (Version 29.3.1). FDA Food and Drug Administration, EMA European Medicines Agency, SaMD
Software as a Medical Device, RUO Research Use Only, PMA Pre-market Approval, CADe Computer-Aided Detection, CDx Companion Diagnostics,
PCCP Pre-determined Change Control Plan
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
25
Signal Transduction and Targeted Therapy          (2026) 11:407

Accountability and responsibility in biomarker-driven decisions
AI biomarkers complicate traditional medical accountability
concepts by involving algorithm developers, data providers, and
healthcare institutions in decision-making paths historically driven
by clinician judgment. When biomarker outputs in ﬂuence
diagnosis, treatment selection, or clinical trial appropriateness,
responsibility for errors is distributed among technical and clinical
actors.
Regulatory and legal frameworks are increasingly emphasizing
common accountability models that require documentation of
intended use, decision support limitations, and clinician override
mechanisms. Ethically, clinicians should retain ultimate responsi-
bility for patient care decisions, while institutions must ensure that
the biomarker systems used meet comparable standards of
evidence and safety to other diagnostic technologies.
Effective use of AI biomarkers requires coordinated validation of
analytical tests, algorithms, and clinical work ﬂows. Table 11
summarizes regulatory and implementation requirements
throughout the development phases and highlights common
failure points that prevent real-world deployment.
Meeting these requirements is vital not only for regulatory
approval but also for sustainable clinical reliability, particularly in
environments where adaptive models and evolving data distribu-
tions are expected.
CHALLENGES AND DEBATES IN AI BIOMARKER DISCOVERY
AND TRANSLATION
Spurious biomarker phenomenon: confounding effects, leakage,
and batch effects
A signi ﬁcant limitation in AI-powered biomarker discovery is the
frequent identi ﬁcation of signals in discovery datasets that
correlate with outcomes but do not re ﬂect true disease biology.
Such spurious biomarkers arise from technical batch effects,
confounding effects stemming from treatment or care pathways,
and information leakage across training and testing sets. 266 In
multi-omics studies, differences in sample processing, sequencing
platforms, or laboratory protocols can dominate biological
variation, leading to signatures that re ﬂect study design rather
than disease mechanisms. 159
Clinical confounding effects are particularly problematic when
biomarkers represent healthcare utilization, disease severity at
presentation, or therapeutic interventions rather than intrinsic
disease processes. For example, laboratory tests requested only in
critically ill patients may appear predictive simply because they
encode clinician behavior. Without careful causal framing and data
source analysis, AI models can inadvertently learn such non-
biological relationships and produce biomarkers that collapse
under external validation.
Interpretability discussions: post hoc explanations versus
mechanistic evidence
Interpretability remains one of the most controversial aspects of AI
biomarker research. Post hoc explanation techniques, such as
feature attribution maps, SHAP values, and saliency methods, aim
to identify effective inputs but do not establish causal relation-
ships or biological relevance. 267 In biomarker discovery, such
explanations can give a false impression of biological insight by
highlighting associated but mechanistically irrelevant features.
Mechanistic interpretability requires alignment between
learned representations and known biological pathways, cellular
states, or molecular interactions. Approaches involving pathway
prioritization, graph-based biological networks, or causal discovery
frameworks offer greater potential for biologically grounded
inference but remain computationally and data-intensive.
Generalizability and population bias: multi-ethnic and multi-
regional performance gaps
Many AI-enabled biomarker studies rely on datasets that
incompletely represent minority populations and low-resource
healthcare settings, raising concerns about unequal performance
across demographic groups. Differences in genetic origin,
comorbidities, environmental exposures, and access to healthcare
can signi ﬁcantly alter biomarker distributions, weakening model
calibration and clinical reliability. 185,268
Therefore, external validation across geographic regions,
healthcare systems, and origin groups is essential but is often
neglected due to data access barriers and logistical constraints.
When performance disparities are identi ﬁed, mitigation strategies
such as reweighting, subgroup-speci ﬁc thresholds, or transfer
learning can partially address disparities but cannot completely
replace inclusive data collection strategies. Failure to address
these issues risks embedding structural disparities into diagnostic
and treatment pathways.
Table 10. Regulatory and translational pathways for AI-powered biomarker tools
Translational
category
Typical intended use Regulatory/translational
pathway
Main evidence expectations Example context Representative
references
Software as a
Medical Device
(SaMD)
Risk prediction, triage,
assistive clinical decision
support
device-software pathway
with lifecycle oversight
Technical veri ﬁcation, clinical
validation, workﬂow integration,
post-deployment monitoring
AI-powered ECG, stroke
triage, autonomous
screening systems
186,260,297
In vitro
diagnostics/
companion
diagnostics (IVD/
CDx)
Patient selection for
treatment, assay-related
treatment decisions
Assay-speciﬁc diagnostic
pathway; often linked-
targeted therapy
approval
Analytical validation, clinical
validation, intended-use
deﬁnition, context-speci ﬁc
performance
PD-L1 type selection
paradigms, biomarker-
linked oncology treatment
decisions
134,253
Biomarker
qualiﬁcation/drug
development tool
Trial enrichment,
pharmacodynamic
biomarkers, surrogate
development
Context-of-use
qualiﬁcation framework
Reproducibility, context-of-use
deﬁnition, evidentiary package,
trial-level utility
Enriching biomarkers in
targeted therapy
development
115,255,295
Research use only
(RUO) biomarker
models
Discovery-stage
signatures, exploratory
mechanism studies
Preclinical/exploratory
pathway
Internal rigor, transparent
methods, replication where
possible, no clinical claims
Early multi-omics discovery
models
5,85,178
Adaptive/
continuously
updated AI
biomarker systems
Recalibrated or learning
systems for longitudinal
prediction or support
Lifecycle governance
with update control and
monitoring
Change management,
traceability, prede ﬁned update
rules, post-market oversight
Adaptive clinical decision
support tools
260,298–300
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
26
Signal Transduction and Targeted Therapy          (2026) 11:407

Reproducibility and evidentiary standards
Reproducibility remains one of the most signi ﬁcant unsolved
challenges in AI-powered biomarker research. Biomarkers that
perform well in discovery datasets often show declines in
accuracy, calibration, or clinical utility when evaluated across
independent cohorts, health systems, or measurement platforms.
Large collaborative consortia, benchmark datasets, and multi-
center validation initiatives offer valuable opportunities to assess
robustness, but they often fail to fully re ﬂect the diversity and
complexity of real-world clinical settings. 269
An ongoing debate concerns the level of evidence required for
AI-derived biomarkers to support clinical decision-making. Pre-
dictive performance alone is increasingly seen as insuf ﬁcient.
Instead, reproducibility should encompass stability across popula-
tions, consistency across technical platforms, and the preservation
of clinical utility in independent settings. These challenges
highlight the need for evidence frameworks that balance
methodological rigor with practical clinical application and
acknowledge that acceptable thresholds of evidence may differ
depending on the intended biomarker application.
EMERGING TRENDS AND FUTURE DIRECTIONS IN AI
BIOMARKER DISCOVERY
Foundation and self-supervised learning for biomarkers: promises
and exaggerations
Foundation models trained on large-scale unlabeled biomedical
data offer a pathway for transferable representations across
diseases, modalities, and institutions. In imaging, self-supervised
pretraining improves performance in low-label regimens and
enhances the ability to generalize across scanners and popula-
tions. In molecular biology, protein, transcriptomic, and multi-
modal foundation models capture structural and regulatory
patterns adaptable to biomarker discovery tasks. 101,107 Precision
oncology represents one of the clearest examples of this
convergence between biomarkers, machine learning, and clinical
decision support.270 Future integration of electronic health records
with post-genome datasets could further accelerate precision
medicine initiatives. 271
However, foundation models inherently do not address issues
of cohort bias, confounding factors, or clinical utility. Without
careful ﬁne-tuning and external validation, pre-trained representa-
tions may encode large-scale correlations rather than disease-
related mechanisms. Furthermore, the computational and envir-
onmental costs of training such models raise questions about
sustainability and accessibility. Therefore, future assessment
frameworks should evaluate not only predictive gains but also
robustness, interpretability, and clinical impact.
Multiscale systems medicine: linking molecules, cells, organs, and
phenotypes
A signi ﬁcant frontier in biomarker science is the integration of
molecular, cellular, tissue-level, and organism-level phenotypes
into coherent disease models. Advances in single-cell and spatial
technologies enable mapping of cellular state programs in
anatomical and microenvironmental contexts, while imaging
and digital biomarkers capture organ-level and functional
manifestations. 272,273 Single-cell technologies are expected to
play an increasingly important role in therapeutic target
discovery and drug development. 274 Interpretable frameworks
for integrating single-cell and spatial omics data are likely to
become increasingly important in future biomarker
processes. 45,273
AI architectures with hierarchical and graph-based reasoning
capabilities offer tools to connect these scales, making it possible
to infer how molecular perturbations propagate through cellular
networks and produce clinical phenotypes. Such multiscale
models can support the identi ﬁcation of causal pathways, cross-
tissue interactions, and emerging disease programs that are not
visible in unimodal analyses. However, bringing together suf ﬁ-
ciently large, well-explained multiscale datasets remains a
signiﬁcant bottleneck, and experimental validation of the inferred
mechanisms will remain essential.
Joint learning and privacy-preserving analytics for multicenter
validation
Data sharing barriers remain a fundamental obstacle to robust
biomarker validation. Federated learning, secure multi-party
computation, and differential privacy frameworks enable colla-
borative model development without centralizing sensitive
patient data, thereby supporting multicenter validation while
respecting regulatory and ethical constraints. By exposing models
to more diverse populations and health systems, these
approaches can increase generalizability and reduce center-
speciﬁc biases.
However, distributed learning frameworks introduce additional
challenges, including heterogeneous data distributions, variable
local data quality, and evolving regulatory requirements for
certiﬁcation and auditing. 275 Future efforts should focus on
establishing practical standards for governance, validation, and
interoperability across participating institutions.
Digital twins and in silico trials: realistic short-term use cases
Digital twins, computational representations of individual patients
or disease trajectories, have been proposed as tools to simulate
treatment response and optimize trial design. 276 In the near term,
realistic applications are likely to focus on population-level or
cohort-level simulations rather than fully individualized physiolo-
gical replicates.
In silico trials can support hypothesis generation, dose- ﬁnding
studies, and the exploration of trial design alternatives, potentially
reducing costs and accelerating development cycles. 277 However,
digital twins are critically dependent on the validity of the
underlying mechanistic and statistical models; without strong
empirical grounding, simulations risk reinforcing existing assump-
tions rather than revealing new insights. Therefore, digital twin
approaches should complement rather than replace experimental
validation strategies, serving as hypothesis-generating and trial-
Table 11. Regulatory and implementation requirements for AI biomarkers
Requirements What needs to be validated Who is responsible Typical evidence Common failure points
Analytical validity Analysis + preprocessing Laboratory + vendor Accuracy, reproducibility Batch effects
Clinical validity Biomarker-outcome correlation Developers External cohorts Spectrum bias
Clinical utility Decision bene ﬁt Trial Sponsors Interventional trials No impact on work ﬂow
Algorithm governance Model stability Manufacturers Version control audits Drift post-distribution
Post-marketing surveillance Safety and bias Institutions Real-world monitoring Recalibration neglected
Key references for this table: refs. 170,189,298,301,302
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
27
Signal Transduction and Targeted Therapy          (2026) 11:407

optimization tools while maintaining reliance on prospective
biological and clinical validation.
A pragmatic roadmap for the next 5 years
Over the next 5 years, progress in the implementation of AI-enabled
biomarker systems will depend less on algorithmic innovation and
more on infrastructure, standards, and collaborative frameworks. Key
priorities include92: (1) data foundations (large, diverse, longitudinal,
and multimodal cohorts with standa rdized acquisition and annota-
tion); (2) methodological rigor (routine external validation, subgroup
performance reporting, and decis ion curve-based assessment of
clinical beneﬁt); (3) biologically grounded integration (embedding
biological information into mod el architectures and validation
strategies to support causal infere nce); (4) regulatory alignment
(early engagement with regulators to de ﬁne acceptable evidence
pathways for AI biomarkers); (5) implementation science (prospective
studies evaluating how biomarker -guided decisions impact work-
ﬂows, outcomes, and equity).
Therefore, investment strategies should prioritize interoperable
data ecosystems, cross-industry consortia, and reproducibility
infrastructure, rather than isolated model development efforts.
Success will be measured not by benchmark performance, but by
demonstrable improvements in patient outcomes and treatment
development ef ﬁciency.
CONCLUSION AND STRATEGIC PERSPECTIVE
Across disease domains and biomarker modalities, several consistent
principles distinguish robust, tr anslatable AI-powered biomarkers
from that remain con ﬁned to discovery settings. First, biological
validity and mechanistic grounding are central when biomarkers are
intended to provide information on therapeutic development,
patient stratiﬁcation, or treatment selection. Biomarkers re ﬂecting
causal disease processes are more likely to generalize across
populations and remain stable under clinical intervention than those
derived solely from correlational signatures. Second, multimodal
integration offers clear advantages when pathological processes
span molecular, cellular, tissue, a nd organ-level scales. However,
integration should be driven by biological hypotheses and empirical
probability, rather than the indiscr iminate aggregation of hetero-
geneous features, risking increasing noise and confusion instead of
revealing disease mechanisms. Thi rd, external validation across
independent cohorts and clinically relevant subgroups is indispen-
sable, as predicted performance in discovery datasets routinely
overestimates real-world efﬁcacy. Finally, success should be de ﬁned
not only by prediction accuracy bu t also by demonstrable clinical
beneﬁt. Evaluation frameworks inco rporating decision analysis
metrics, workﬂow integration, and patient-relevant outcomes are
necessary to differentiate biomarkers that meaningfully improve care
from those that merely improve risk strati ﬁcation without altering
management.
Evidence across multiple disease domains indicates that
translational success depends as much on study design, validation
strategy, and clinical integration as on algorithmic performance.
Biomarker development studies are most effective when aligned
with explicitly stated diagnostic or therapeutic decisions and
when model building incorporates biological information support-
ing reasonable biologically grounded interpretation. Evaluation
strategies should extend beyond retrospective accuracy estima-
tions to include prospective assessments of biomarker-guided
decision paths, particularly in settings where treatment selection,
dosing strategies, or trial enrichment are intended applications.
On the other hand, common pitfalls include assuming statistical
association has therapeutic signi ﬁcance, relying solely on endo-
genous cross-validation, and neglecting population diversity and
health system variability during development. Similarly, while
interpretability techniques are valuable for transparency, they
cannot replace biological validation or experimental veri ﬁcation of
disease mechanisms. These considerations are equally valid for
molecular, imaging, and digital biomarkers, highlighting that
translation barriers are often methodological and organizational
rather than purely technical.
Despite substantial methodological advances, several barriers
remain that limit the transfer of AI-derived biomarkers to clinical
practice. Data heterogeneity, limited cohort diversity, incomplete
biological annotation, and inconsistencies in reporting standards
continue to be major challenges across disease domains.
Addressing these limitations will require harmonized data
collection frameworks, prospective multicenter validation studies,
transparent model reporting, and closer integration of computa-
tional scientists with clinicians and experimental researchers.
Equally important is the adoption of standardized evaluation
frameworks that assess not only predictive performance but also
robustness, calibration, fairness, and clinical utility. Such measures
can mitigate the risk of over ﬁtting, improve reproducibility, and
facilitate regulatory acceptance.
Future progress will likely be driven by the convergence of
foundation models, multimodal learning architectures, causal
inference approaches, and systems biology frameworks. These
technologies have the potential to move biomarker discovery
beyond pattern recognition to the identi ﬁcation of biologically
coherent disease programs that can inform therapeutic interven-
tion. However, successful implementation will depend on rigorous
external validation, continuous post-deployment monitoring, and
prospective demonstration of patient bene ﬁt. Consequently, the
most valuable AI-powered biomarkers will be those that not only
accurately predict outcomes but also improve clinical decision-
making, support therapeutic development, and contribute to
more effective and personalized healthcare.
Despite substantial methodological progress, important barriers
continue to limit the clinical translation of AI-derived biomarkers. If
these conditions are met, AI-pow ered biomarkers can evolve from
exploratory research outputs into reliable components of therapeutic
development and routine clinical decision-making. Their greatest
value will stem not only from increasingly sophisticated predictions
but also from their ability to gener ate reproducible, biologically
based, and clinically applicable knowledge. Consequently, the future
success of AI-driven biomarker science will depend on integrating
methodological innovation with ri gorous validation, mechanistic
understanding, and demonstrable patient beneﬁt.
DATA AVAILABILITY
All supporting data are included in the article.
AUTHOR CONTRIBUTIONS
R.D. and N.A. designed the study, drafted the manuscript, and supervised and edited
it. N.A. wrote the manuscript. All authors read and approved the review article.
ADDITIONAL INFORMATION
Competing interests: R.D. is the president of the INVAMED Institute for Medical
Innovation. N.A. is retired and works as a volunteer consultant for Med-International
UK Health Agency Ltd.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims
in published maps and institutional af ﬁliations.
REFERENCES
1. Ahmad, A., Imran, M. & Ahsan, H. Biomarkers as biomedical bioindicators:
approaches and techniques for the detection, analysis, and validation of novel
biomarkers of diseases. Pharmaceutics 15, 1630 (2023).
2. Drucker, E. & Krapfenbauer, K. Pitfalls and limitations in translation from bio-
marker discovery to clinical utility in predictive and personalised medicine.
EPMA J. 4, 7 (2013).
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
28
Signal Transduction and Targeted Therapy          (2026) 11:407

3. Zhao, Q. et al. Applications and challenges of biomarker-based predictive
models in proactive health management. Front. Public Health 13, 1633487
(2025).
4. Ioannidis, J. P. Why most published research ﬁndings are false. PLoS Med. 2,
e124 (2005).
5. Rifai, N., Gillette, M. A. & Carr, S. A. Protein biomarker discovery and validation: the
long and uncertain path to clinical utility. Nat. Biotechnol. 24,9 7 1–983 (2006).
6. AbdulRaheem, Y. Statistical signi ﬁcance versus clinical relevance: key con-
siderations in interpretation medical research data. Indian J. Community Med. 49,
791–795 (2024).
7. Parikh, C. R. & Thiessen-Philbrook, H. Key concepts and limitations of statistical
methods for evaluating biomarkers of kidney disease. J. Am. Soc. Nephrol. 25,
1621–1629 (2014).
8. Cook, N. R. Methods for evaluating novel biomarkers: a new paradigm. Int. J.
Clin. Pract. 64, 1723 –1727 (2010).
9. Poste, G. Bring on the biomarkers. Nature 469, 156 –157 (2011).
10. Kalluri, R. & LeBleu, V. S. The biology, function, and biomedical applications of
exosomes. Science 367, eaau6977 (2020).
11. Hasin, Y., Seldin, M. & Lusis, A. Multi-omics approaches to disease. Genome Biol.
18, 83 (2017).
12. Gillies, R. J., Kinahan, P. E. & Hricak, H. Radiomics: images are more than pictures,
they are data. Radiology 278, 563 –577 (2016).
13. Lambin, P. et al. Radiomics: extracting more information from medical images
using advanced feature analysis. Eur. J. Cancer 48, 441 –446 (2012).
14. Aerts, H. J. et al. Decoding tumour phenotype by noninvasive imaging using a
quantitative radiomics approach. Nat. Commun. 5, 4006 (2014).
15. Fu, W., Ding, J., Gao, K., Ma, S. & Tian, L. A likelihood ratio test on temporal trends
in age-period-cohort models with applications to the disparities of heart disease
mortality among US populations and comparison with Japan. Stat. Med. 40,
668–689 (2021).
16. Bu, K. et al. Identifying correlations driven by in ﬂuential observations in large
datasets. Brief. Bioinform. 23, bbab482 (2022).
17. Al-Ewaidat, O. A. & Naffaa, M. M. Emerging AI- and biomarker-driven precision
medicine in autoimmune rheumatic diseases: from diagnostics to therapeutic
decision-making. Rheumato 5, 17 (2025).
18. Awari, A. et al. Obesity biomarkers: exploring factors, ramiﬁcation, machine learning,
and AI-unveiling insights in health research. MedComm 6, e70169 (2025).
19. Carletti, M. et al. Multimodal AI correlates of glucose spikes in people with
normal glucose regulation, pre-diabetes and type 2 diabetes. Nat. Med. 31,
3121–3127 (2025).
20. Rajpurkar, P., Chen, E., Banerjee, O. & Topol, E. J. AI in health and medicine. Nat.
Med. 28,3 1 –38 (2022).
21. Topol, E. J. High-performance medicine: the convergence of human and arti ﬁcial
intelligence. Nat. Med. 25,4 4 –56 (2019).
22. Norgeot, B. et al. Minimum information about clinical arti ﬁcial intelligence
modeling: the MI-CLAIM checklist. Nat. Med. 26, 1320 –1324 (2020).
23. Haibe-Kains, B. et al. Transparency and reproducibility in arti ﬁcial intelligence.
Nature 586, E14 –E16 (2020).
24. Diniz, M. A. Statistical methods for validation of predictive models. J. Nucl.
Cardiol. 29, 3248 –3255 (2022).
25. Vickers, A. J. & Elkin, E. B. Decision curve analysis: a novel method for evaluating
prediction models. Med. Decis. Mak. 26, 565 –574 (2006).
26. Manolio, T. A. et al. Finding the missing heritability of complex diseases. Nature
461, 747 –753 (2009).
27. Klarin, D. & Natarajan, P. Clinical utility of polygenic risk scores for coronary
artery disease. Nat. Rev. Cardiol. 19, 291 –301 (2022).
28. Roadmap Epigenomics Consortium et al. Integrative analysis of 111 reference
human epigenomes. Nature 518, 317 –330 (2015).
29. Nicholson, J. K. et al. Metabolic phenotyping in clinical and surgical environ-
ments. Nature 491, 384 –392 (2012).
30. Lin, C. et al. Metabolomics for clinical biomarker discovery and therapeutic
target identi ﬁcation. Molecules 29, 2198 (2024).
31. Qiu, S. et al. Small molecule metabolites: discovery of biomarkers and ther-
apeutic targets. Signal Transduct. Target. Ther. 8, 132 (2023).
32. Ghosh, S., Zhao, X., Alim, M., Brudno, M. & Bhat, M. Arti ﬁcial intelligence applied
to ‘omics data in liver disease: towards a personalised approach for diagnosis,
prognosis and treatment. Gut 74, 295 –311 (2025).
33. Cheerla, A. & Gevaert, O. Deep learning with multimodal representation for
pancancer prognosis prediction. Bioinformatics 35, i446 –i454 (2019).
34. Ahmed, I. et al. Plasma multi-omics and machine learning reveal predictive
biomarkers for type 2 diabetes and retinopathy in Qatar Biobank Cohort. J.
Transl. Med. 23, 1159 (2025).
35. Liu, J. et al. The role of multi-omics in biomarker discovery, diagnosis, prognosis,
and therapeutic monitoring of tissue repair and regeneration processes. J.
Orthop. Transl. 54, 131 –151 (2025).
36. Piwecka, M., Rajewsky, N. & Rybak-Wolf, A. Single-cell and spatial tran-
scriptomics: deciphering brain complexity in health and disease. Nat. Rev.
Neurol. 19, 346 –362 (2023).
37. Aebersold, R. & Mann, M. Mass-spectrometric exploration of proteome structure
and function. Nature 537, 347 –355 (2016).
38. Stuart, T. & Satija, R. Integrative single-cell analysis. Nat. Rev. Genet. 20,2 5 7–272
(2019).
39. Boxer, E. et al. Emerging clinical applications of single-cell RNA sequencing in
oncology. Nat. Rev. Clin. Oncol. 22, 315 –326 (2025).
40. Tirosh, I. & Suvà, M. L. Cancer cell states: lessons from ten years of single-cell
RNA-sequencing of human tumors. Cancer Cell 42, 1497 –1506 (2024).
41. Kleshchevnikov, V. et al. Cell2location maps ﬁne-grained cell types in spatial
transcriptomics. Nat. Biotechnol. 40, 661 –671 (2022).
42. Dezem, F. S., Arjumand, W., DuBose, H., Morosini, N. S. & Plummer, J. Spatially
resolved single-cell omics: methods, challenges, and future perspectives. Annu.
Rev. Biomed. Data Sci. 7, 131 –153 (2024).
43. De Jonghe, J. et al. scTrends: a living review of commercial single-cell and spatial
‘omic technologies. Cell Genom. 4, 100723 (2024).
44. Si, Y., Lee, J. S., Jun, G., Kang, H. M. & Lee, J. H. Spatial omics enters the microscopic
arena: opportunities and challenges. Trends Genet. 41,7 7 4–787 (2025).
45. Dinc, R. & Ardic, N. Mapping the immune environment: spatiotemporal
dynamics in cardiovascular events. Front. Immunol. 17, 1809941 (2026).
46. Yiu, T. et al. Transformative advances in single-cell omics: a comprehensive
review of foundation models, multimodal integration and computational eco-
systems. J. Transl. Med. 23, 1176 (2025).
47. Baião, A. R. et al. A technical review of multi-omics data integration methods:
from classical statistical to deep generative approaches. Brief. Bioinform. 26,
bbaf355 (2025).
48. Robins, H. S. et al. Comprehensive assessment of T-cell receptor beta-chain
diversity in alphabeta T cells. Blood 114, 4099 –4107 (2009).
49. Wigerblad, G. & Kaplan, M. J. Neutrophil extracellular traps in systemic auto-
immune and autoin ﬂammatory diseases. Nat. Rev. Immunol. 23, 274–288 (2023).
50. Ardic, N. & Dinc, R. Relationship between neutrophil extracellular traps and
venous thromboembolism: pathophysiological and therapeutic role. Br. J. Hosp.
Med. 86,1 –15 (2025).
51. Busarello, E. et al. Cell Marker Accordion: interpretable single-cell and spatial
omics annotation in health and disease. Nat. Commun. 16, 5399 (2025).
52. Corcoran, R. B. & Chabner, B. A. Application of cell-free DNA analysis to cancer
treatment. N. Engl. J. Med. 379, 1754 –1765 (2018).
53. Wan, J. C. M. et al. Liquid biopsies come of age: towards implementation of
circulating tumour DNA. Nat. Rev. Cancer 17, 223 –238 (2017).
54. Crosby, D. et al. Early detection of cancer. Science 375, eaay9040 (2022).
55. Li, F. Q. & Cui, J. W. Circulating tumor DNA-minimal residual disease: an up-and-
coming nova in resectable non-small-cell lung cancer. Crit. Rev. Oncol. Hematol.
179, 103800 (2022).
56. Ma, L. et al. Liquid biopsy in cancer current: status, challenges and future pro-
spects. Signal Transduct. Target. Ther. 9, 336 (2024).
57. Qureshi, Z. et al. Liquid biopsies for early detection and monitoring of cancer:
advances, challenges, and future directions. Ann. Med. Surg. 87, 3244 –3253
(2025).
58. Pantel, K. & Alix-Panabières, C. Minimal residual disease as a target for liquid
biopsy in patients with solid tumours. Nat. Rev. Clin. Oncol. 22,6 5 –77 (2025).
59. Boukouris, A. E. et al. A comprehensive overview of minimal residual disease in
the management of early-stage and locally advanced non-small cell lung can-
cer. NPJ Precis. Oncol. 9, 178 (2025).
60. Hoang, T., Choi, M. K., Oh, J. H. & Kim, J. Utility of circulating tumor DNA to detect
minimal residual disease in colorectal cancer: a systematic review and network
meta-analysis. Int. J. Cancer 157, 722 –740 (2025).
61. Negro, S. et al. Circulating tumor DNA as a real-time biomarker for minimal
residual disease and recurrence prediction in stage II colorectal cancer: a sys-
tematic review and meta-analysis. Int. J. Mol. Sci. 26, 2486 (2025).
62. Geyer, P. E., Holdt, L. M., Teupser, D. & Mann, M. Revisiting biomarker discovery
by plasma proteomics. Mol. Syst. Biol. 13, 942 (2017).
63. Ek, W. E., Karlsson, T., Höglund, J., Rask-Andersen, M. & Johansson, Å Causal
effects of in ﬂammatory protein biomarkers on in ﬂammatory diseases. Sci. Adv.
7, eabl4359 (2021).
64. Moreno-Torres, M. et al. Factors that in ﬂuence the quality of metabolomics data
in in vitro cell toxicity studies: a systematic survey. Sci. Rep. 11, 22119 (2021).
65. Kumar, M. A. et al. Extracellular vesicles as tools and targets in therapy for
diseases. Signal Transduct. Target. Ther. 9, 27 (2024).
66. Dinc, R. & Ardic, N. Arti ﬁcial intelligence for exosomal biomarker discovery for
cardiovascular diseases: multi-omics integration, reproducibility, and transla-
tional prospects. Cells 15, 304 (2026).
67. Welsh, J. A. et al. Minimal information for studies of extracellular vesicles (MISEV2023):
from basic to advanced approaches.J. Extracell. Vesicles13, e12404 (2024).
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
29
Signal Transduction and Targeted Therapy          (2026) 11:407

68. Théry, C. et al. Minimal information for studies of extracellular vesicles 2018
(MISEV2018): a position statement of the International Society for Extracellular
Vesicles and update of the MISEV2014 guidelines. J. Extracell. Vesicles 7, 1535750
(2018).
69. Mateescu, B. et al. Obstacles and opportunities in the functional analysis of
extracellular vesicle RNA: an ISEV position paper. J. Extracell. Vesicles 6, 1286095
(2017).
70. Darci-Maher, N. et al. Cross-tissue omics analysis discovers ten adipose genes
encoding secreted proteins in obesity-related non-alcoholic fatty liver disease.
EBioMedicine 92, 104620 (2023).
71. Li, H. et al. Identi ﬁcation and validation of core biomarkers for sepsis: a com-
prehensive analysis using bioinformatics and machine learning. Front. Immunol.
16, 1700704 (2025).
72. Xu, L., Li, J. & Gong, W. Applications of machine learning-assisted extracellular
vesicles analysis technology in tumor diagnosis. Comput. Struct. Biotechnol. J. 27,
2460–2472 (2025).
73. Campanella, G. et al. Real-world deployment of a ﬁne-tuned pathology foun-
dation model for lung cancer biomarker detection. Nat. Med. 31, 3002 –3010
(2025).
74. Nicke, T. et al. Tissue concepts: supervised foundation models in computational
pathology. Comput. Biol. Med. 186, 109621 (2025).
75. Li, Z. et al. AI-enabled virtual spatial proteomics from histopathology for inter-
pretable biomarker discovery in lung cancer. Nat. Med. 32, 231 –244 (2026).
76. Pai, S. et al. Foundation model for cancer imaging biomarkers. Nat. Mach. Intell.
6, 354 –367 (2024).
77. Ligero, M. et al. A whirl of radiomics-based biomarkers in cancer immunother-
apy, why is large scale validation still lacking? NPJ Precis. Oncol. 8, 42 (2024).
78. Coravos, A. et al. Digital medicine: a primer on measurement. Digit. Biomark. 3,
31–71 (2019).
79. Bent, B. et al. Engineering digital biomarkers of interstitial glucose from non-
invasive smartwatches. NPJ Digit. Med. 4, 89 (2021).
80. Perez, M. V. et al. Large-scale assessment of a smartwatch to identify atrial
ﬁbrillation. N. Engl. J. Med. 381, 1909 –1917 (2019).
81. Zahedani, A. D. et al. Digital health application integrating wearable data and
behavioral patterns improves metabolic health. NPJ Digit. Med. 6, 216 (2023).
82. Huang, X. et al. Digital biomarkers for interstitial glucose prediction in healthy
individuals using wearables and machine learning. Sci. Rep. 15, 30164 (2025).
83. Macias Alonso, A. K., Hirt, J., Woel ﬂe, T., Janiaud, P. & Hemkens, L. G. De ﬁnitions
of digital biomarkers: a systematic mapping of the biomedical literature. BMJ
Health Care Inf. 31, e100914 (2024).
84. Menden, M. P. et al. Machine learning prediction of cancer cell sensitivity to
drugs based on genomic and chemical properties. PLoS ONE 8, e61318 (2013).
85. Ng, S., Masarone, S., Watson, D. & Barnes, M. R. The bene ﬁts and pitfalls of
machine learning for biomarker discovery. Cell Tissue Res. 394,1 7 –31 (2023).
86. Esteva, A. et al. Dermatologist-level classi ﬁcation of skin cancer with deep neural
networks. Nature 542, 115 –118 (2017).
87. Bera, K., Schalper, K. A., Rimm, D. L., Velcheti, V. & Madabhushi, A. Arti ﬁcial
intelligence in digital pathology: new tools for diagnosis and precision oncol-
ogy. Nat. Rev. Clin. Oncol. 16, 703 –715 (2019).
88. Richter, T., Bahrami, M., Xia, Y., Fischer, D. S. & Theis, F. J. Delineating the
effective use of self-supervised learning in single-cell genomics. Nat. Mach. Intell.
7,6 8 –78 (2025).
89. Acosta, J. N., Falcone, G. J., Rajpurkar, P. & Topol, E. J. Multimodal biomedical AI.
Nat. Med. 28, 1773 –1784 (2022).
90. Lipkova, J. et al. Arti ﬁcial intelligence for multimodal data integration in
oncology. Cancer Cell 40, 1095 –1110 (2022).
91. Steyaert, S. et al. Multimodal data fusion for cancer biomarker discovery with
deep learning. Nat. Mach. Intell. 5, 351 –362 (2023).
92. Krones, F., Marikkar, U., Parsons, G., Szmul, A. & Mahdi, A. Review of multimodal
machine learning approaches in healthcare. Inf. Fusion 114, 102690 (2025).
93. Chen, R. J. et al. Pan-cancer integrative histology-genomic analysis via multi-
modal deep learning. Cancer Cell 40, 865 –878.e6 (2022).
94. Mataraso, S. J. et al. A machine learning approach to leveraging electronic
health records for enhanced omics analysis. Nat. Mach. Intell. 7, 293–306 (2025).
95. Camacho, D. M., Collins, K. M., Powers, R. K., Costello, J. C. & Collins, J. J. Next-
generation machine learning for biological networks. Cell 173, 1581 –1592
(2018).
96. Lin, J. et al. Chemokine-like factor-like MARVEL transmembrane domain-
containing 1 identi ﬁed as a novel target protein for immune dysregulation in
sepsis: a machine learning and molecular dynamics framework for diagnostic
biomarkers and therapeutic exploration. Int. J. Biol. Macromol. 319, 145276
(2025).
97. Xie, W. et al. A novel biomarker selection method combining graph neural
network and gene relationships applied to microarray data. BMC Bioinforma. 23,
303 (2022).
98. Dharanipragada, P. et al. Blocking genomic instability prevents acquired resis-
tance to MAPK inhibitor therapy in melanoma. Cancer Discov. 13, 880 –909
(2023).
99. Dalla-Torre, H. et al. Nucleotide Transformer: building and evaluating robust
foundation models for human genomics. Nat. Methods 22, 287 –297 (2025).
100. de Almeida, B., Lopez, M. & Pierrot, T. Generalized AI models for genomics
applications. Nat. Methods 22, 231 –232 (2025).
101. Guo, F. et al. Foundation models in bioinformatics. Natl. Sci. Rev. 12, nwaf028
(2025).
102. Topol, E. J. Learning the language of life with AI. Science 387, eadv4414 (2025).
103. Vorontsov, E. et al. A foundation model for clinical-grade computational
pathology and rare cancers detection. Nat. Med. 30, 2924 –2935 (2024).
104. Campanella, G. et al. Clinical-grade computational pathology using weakly
supervised deep learning on whole slide images. Nat. Med. 25, 1301 –1309
(2019).
105. Ding, T. et al. A multimodal whole-slide foundation model for pathology. Nat.
Med. 31, 3749 –3761 (2025).
106. Xu, H. et al. A whole-slide foundation model for digital pathology from real-
world data. Nature 630, 181 –188 (2024).
107. Moor, M. et al. Foundation models for generalist medical arti ﬁcial intelligence.
Nature 616, 259 –265 (2023).
108. Rudin, C. Stop explaining black box machine learning models for high stakes
decisions and use interpretable models instead. Nat. Mach. Intell. 1, 206 –215
(2019).
109. Budhkar, A., Song, Q., Su, J. & Zhang, X. Demystifying the black box: a survey on
explainable arti ﬁcial intelligence (XAI) in bioinformatics. Comput. Struct. Bio-
technol. J. 27, 346 –359 (2025).
110. Zhang, K., Wang, D., Lin, F., Xie, J. & Zhou, W. A comprehensive review of
explainable arti ﬁcial intelligence in healthcare methods, evaluation, and clinical
integration. iScience 29, 115026 (2026).
111. Toussaint, P. A. et al. Explainable arti ﬁcial intelligence for omics data: a sys-
tematic mapping study. Brief. Bioinform. 25, bbad453 (2024).
112. Schölkopf, B. et al. Toward causal representation learning. Proc. IEEE 109,
612–634 (2021).
113. Pearl, J. An introduction to causal inference. Int. J. Biostat. 6, 7 (2010).
114. Javaid, H. et al. The impact of arti ﬁcial intelligence on biomarker discovery.
Emerg. Top. Life Sci. 8,8 9 –105 (2025).
115. Prentice, R. L. Surrogate endpoints in clinical trials: de ﬁnition and operational
criteria. Stat. Med. 8, 431 –440 (1989).
116. Gao, S. et al. Modeling drug mechanism of action with large scale gene-
expression pro ﬁles using GPAR, an arti ﬁcial intelligence platform. BMC Bioin-
forma. 22, 17 (2021).
117. García-Campos, M. A., Espinal-Enríquez, J. & Hernández-Lemus, E. Pathway
analysis: state of the art. Front. Physiol. 6, 383 (2015).
118. Mubeen, S. et al. The impact of pathway database choice on statistical enrich-
ment analysis and predictive modeling. Front. Genet. 10, 1203 (2019).
119. Zhou, J. L. et al. Analysis of single-cell CRISPR perturbations indicates that
enhancers predominantly act multiplicatively. Cell Genom. 4, 100672 (2024).
120. Bjerregaard, A., Prada-Luengo, I., Das, V. & Krogh, A. What do single-cell models
already know about perturbations? Genes 16, 1439 (2025).
121. Egbon, O. A., Hickey, J. W. & Anchang, B. Fusion of spatiotemporal and network
models to prioritize multiscale effects in single-cell perturbations. Brief. Bioin-
form. 26, bbaf277 (2025).
122. Kleandrova, V. V., Cordeiro, M. N. D. S. & Speck-Planche, A. Perturbation-theory
machine learning for multi-target drug discovery in modern anticancer
research. Curr. Issues Mol. Biol. 47, 301 (2025).
123. Davey Smith, G. & Hemani, G. Mendelian randomization: genetic anchors for causal
inference in epidemiological studies.Hum. Mol. Genet. 23,R 8 9–R98 (2014).
124. Mo, Z., Zhang, Z., Miao, Q. & Tsui, K. L. Sparsity-constrained invariant risk
minimization for domain generalization with application to machinery fault
diagnosis modeling. IEEE Trans. Cybern. 54, 1547 –1559 (2024).
125. Ni, S. et al. Identifying compound-protein interactions with knowledge graph
embedding of perturbation transcriptomics. Cell Genom. 4, 100655 (2024).
126. Crespi, E. et al. Resolving the rules of robustness and resilience in biology across
scales. Integr. Comp. Biol. 61, 2163 –2179 (2022).
127. Wood, L. B., Winslow, A. R. & Strasser, S. D. Systems biology of neurodegen-
erative diseases. Integr. Biol. 7, 758 –775 (2015).
128. Ocana, A. Integrating arti ﬁcial intelligence in drug discovery and early drug
development: a transformative approach. Biomark. Res. 13, 45 (2025).
129. Arango-Argoty, G. et al. AI-driven predictive biomarker discovery with con-
trastive learning to improve clinical trial outcomes. Cancer Cell 43, 875 –890.e8
(2025).
130. Collins, G. S. et al. TRIPOD+AI statement: updated guidance for reporting clinical
prediction models that use regression or machine learning methods. BMJ 385,
e078378 (2024).
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
30
Signal Transduction and Targeted Therapy          (2026) 11:407

131. Libby, P., Ridker, P. M. & Hansson, G. K. In ﬂammation in atherosclerosis: from
pathophysiology to practice. J. Am. Coll. Cardiol. 54, 2129 –2138 (2009).
132. Firestein, G. S. & McInnes, I. B. Immunopathogenesis of rheumatoid arthritis.
Immunity 46, 183 –196 (2017).
133. Fountzilas, E., Tsimberidou, A. M., Vo, H. H. & Kurzrock, R. Clinical trial design in
the era of precision medicine. Genome Med. 14, 101 (2022).
134. Jørgensen, J. T. Companion and complementary diagnostics: clinical and reg-
ulatory perspectives. Trends Cancer 2, 706 –712 (2016).
135. Kern, S. E. Why your new cancer biomarker may never work: recurrent patterns
and remarkable diversity in biomarker failures. Cancer Res. 72, 6097 –6101
(2012).
136. Ernst, S. M. et al. Utilizing ctDNA to discover mechanisms of resistance to tar-
geted therapies in patients with metastatic NSCLC: towards more informative
trials. Nat. Rev. Clin. Oncol. 22, 371 –378 (2025).
137. Papayannopoulos, V. Neutrophil extracellular traps in immunity and disease.
Nat. Rev. Immunol. 18, 134 –147 (2018).
138. Bonaventura, A. et al. Endothelial dysfunction and immunothrombosis as
key pathogenic mechanisms in COVID-19. Nat. Rev. Immunol. 21, 319 –329
(2021).
139. Finlayson, S. G. et al. The clinician and dataset shift in arti ﬁcial intelligence. N.
Engl. J. Med. 385, 283 –286 (2021).
140. Roberts, M. et al. Common pitfalls and recommendations for using machine
learning to detect and prognosticate for COVID-19 using chest radiographs and
CT scans. Nat. Mach. Intell. 3, 199 –217 (2021).
141. Tang, S., Yuan, K. & Chen, L. Molecular biomarkers, network biomarkers, and
dynamic network biomarkers for diagnosis and prediction of rare diseases.
Fundam. Res. 2, 894 –902 (2022).
142. Qu, N. et al. Multimodal interpretable deep learning for transcriptome-informed
precision oncology and drug mechanism analysis. NPJ Digit. Med . https://
doi.org/10.1038/s41746-026-02735-x (2026).
143. Subramanian, I., Verma, S., Kumar, S., Jere, A. & Anamika, K. Multi-omics data
integration, interpretation, and its application. Bioinform. Biol. Insights 14,
1177932219899051 (2020).
144. Galindez, G., Sadegh, S., Baumbach, J., Kacprowski, T. & List, M. Network-based
approaches for modeling disease regulation and progression. Comput. Struct.
Biotechnol. J. 21, 780 –795 (2022).
145. Liu, Y., Zhu, K., Peng, W., Liu, Z. & Mao, X. Multi-omics and arti ﬁcial intelligence
for precision drug discovery and potential clinical applications. Signal Transduct.
Target. Ther. 11, 210 (2026).
146. Ben-Jaafar, A. et al. Arti ﬁcial intelligence-based biomarkers for the diagnosis and
treatment of neurological conditions: a narrative review. Mol. Brain 19,2 6
(2026).
147. Moons, K. G. M. et al. PROBAST+AI: an updated quality, risk of bias, and
applicability assessment tool for prediction models using regression or arti ﬁcial
intelligence methods. BMJ 388, e082505 (2025).
148. Valous, N. A. et al. Graph machine learning for integrated multi-omics analysis.
Br. J. Cancer 131, 205 –211 (2024).
149. Rodriguez-Mier, P. et al. Unifying multi-sample network inference from prior
knowledge and omics data with CORNETO. Nat. Mach. Intell. 7, 1168 –1186
(2025).
150. Wang, K. et al. TG468: a text graph convolutional network for predicting clinical
response to immune checkpoint inhibitor therapy. Brief. Bioinform. 25, bbae017
(2024).
151. Bonaventura, A. et al. The pathophysiological role of neutrophil extracellular
traps in in ﬂammatory diseases. Thromb. Haemost. 118,6 –27 (2018).
152. Marsiglia, J. Computationally guided high-throughput engineering of an anti-
CRISPR protein for precise genome editing in human cells. Cell Rep. Methods 4,
100882 (2024).
153. Van Calster, B., McLernon, D. J., van Smeden, M., Wynants, L. & Steyerberg, E. W.
Calibration: the Achilles heel of predictive analytics. BMC Med. 17, 230 (2019).
154. Piovani, D., Sokou, R., Tsantes, A. G., Vitello, A. S., & Bonovas, S. Optimizing
clinical decision making with decision curve analysis: insights for clinical
investigators. Healthcare 11, 2244 (2023).
155. Riley, R. D. et al. Minimum sample size for developing a multivariable prediction
model: PART II —binary and time-to-event outcomes. Stat. Med. 38, 1276 –1296
(2019).
156. Collins, G. S. et al. Protocol for development of a reporting guideline (TRIPOD-AI)
and risk of bias tool (PROBAST-AI) for diagnostic and prognostic prediction
model studies based on arti ﬁcial intelligence. BMJ Open 11, e048008 (2021).
157. van de Vegte, Y. J. et al. Genetic insights into resting heart rate and its role in
cardiovascular disease. Nat. Commun. 14, 4646 (2023).
158. Johnson, W. E., Li, C. & Rabinovic, A. Adjusting batch effects in microarray
expression data using empirical Bayes methods. Biostatistics 8, 118 –127 (2007).
159. Leek, J. T. et al. Tackling the widespread and critical impact of batch effects in
high-throughput data. Nat. Rev. Genet. 11, 733 –739 (2010).
160. Hu, F. et al. DeepComBat: a statistically motivated, hyperparameter-robust, deep
learning approach to harmonization of neuroimaging data. Hum. Brain Mapp.
45, e26708 (2024).
161. Fortin, J. P. et al. Harmonization of cortical thickness measurements across
scanners and sites. Neuroimage 167, 104 –120 (2018).
162. Wong, A. et al. External validation of a widely implemented proprietary sepsis
prediction model in hospitalized patients. JAMA Intern. Med. 181, 1065 –1070
(2021).
163. Dhiman, P. et al. Risk of bias of prognostic models developed using machine
learning: a systematic review in oncology. Diagn. Progn. Res. 6, 13 (2022).
164. Hernández, B., Pennington, S. R. & Parnell, A. C. Bayesian methods for proteomic
biomarker development. EuPA Open Proteom. 9,5 4 –64 (2015).
165. Olsson, H. et al. Estimating diagnostic uncertainty in arti ﬁcial intelligence
assisted pathology using conformal prediction. Nat. Commun. 13, 7761 (2022).
166. Seabroke, S. et al. Performance of strati ﬁed and subgrouped disproportionality
analyses in spontaneous databases. Drug Saf. 39, 355 –364 (2016).
167. Russo, C. A. M. & Selvatti, A. P. Bootstrap and rogue identi ﬁcation tests for
phylogenetic analyses. Mol. Biol. Evol. 35, 2327 –2333 (2018).
168. Hayes, D. F. Biomarker validation and testing. Mol. Oncol. 9, 960 –966 (2015).
169. Ou, F. S., Michiels, S., Shyr, Y., Adjei, A. A. & Oberg, A. L. Biomarker discovery and
validation: statistical considerations. J. Thorac. Oncol. 16, 537 –545 (2021).
170. Vasey, B. et al. Reporting guideline for the early stage clinical evaluation of
decision support systems driven by arti ﬁcial intelligence: DECIDE-AI. BMJ 377,
e070904 (2022).
171. Shi, L. et al. The MicroArray Quality Control (MAQC)-II study of common prac-
tices for the development and validation of microarray-based predictive mod-
els. Nat. Biotechnol. 28, 827 –838 (2010).
172. MAQC Consortium The MicroArray Quality Control (MAQC) project shows inter-
and intraplatform reproducibility of gene expression measurements. Nat. Bio-
technol. 24, 1151 –1161 (2006).
173. SEQC/MAQC-III Consortium A comprehensive assessment of RNA-seq accuracy,
reproducibility and information content by the Sequencing Quality Control
Consortium. Nat. Biotechnol. 32, 903 –914 (2014).
174. Balikci, M. A., Njume, C. M. & Cakmak, A. BioMark: biomarker analysis tool. BMC
Bioinform. 27, 42 (2026).
175. Jiang, L. et al. Utilizing stability criteria in choosing feature selection methods
yields reproducible results in microbiome data. Biometrics 78, 1155–1167 (2022).
176. Traverso, A. et al. Powering responsible arti ﬁcial intelligence with high-quality
real-world data: the S-RACE platform for scalable, multi-specialty clinical
research. NPJ Digit. Med. 9, 6 (2026).
177. Davatzikos, C. et al. AI-based prognostic imaging biomarkers for precision
neuro-oncology: the ReSPOND consortium. Neuro. Oncol. 22, 886 –888 (2020).
178. Ransohoff, D. F. Rules of evidence for cancer molecular-marker discovery and
validation. Nat. Rev. Cancer 4, 309 –314 (2004).
179. Pepe, M. S., Janes, H., Longton, G., Leisenring, W. & Newcomb, P. Limitations of
the odds ratio in gauging the performance of a diagnostic, prognostic, or
screening marker. Am. J. Epidemiol. 159, 882 –890 (2004).
180. Obermeyer, Z., Powers, B., Vogeli, C. & Mullainathan, S. Dissecting racial bias in
an algorithm used to manage the health of populations. Science 366, 447 –453
(2019).
181. Mulherin, S. A. & Miller, W. C. Spectrum bias or spectrum effect? Subgroup
variation in diagnostic test evaluation. Ann. Intern. Med. 137, 598 –602 (2002).
182. Hatherley, J. A moving target in AI-assisted decision-making: dataset shift,
model updating, and the problem of update opacity. Ethics Inf. Technol. 27,2 0
(2025).
183. Cagney, D. N. et al. The FDA NIH Biomarkers, EndpointS, and other Tools (BEST)
resource in neuro-oncology. Neuro. Oncol. 20, 1162 –1172 (2018).
184. Agarwal, V. et al. Learning statistical models of phenotypes using noisy labeled
training data. J. Am. Med. Inform. Assoc. 23, 1166 –1173 (2016).
185. Ioannidis, J. P. Why most discovered true associations are in ﬂated. Epidemiology
19, 640 –648 (2008).
186. Benjamens, S., Dhunnoo, P. & Meskó, B. The state of arti ﬁcial intelligence-based
FDA-approved medical devices and algorithms: an online database. NPJ Digit.
Med. 3, 118 (2020).
187. Mattes, W. B. & Goodsaid, F. Regulatory landscapes for biomarkers and diag-
nostic tests: Quali ﬁcation, approval, and role in clinical practice. Exp. Biol. Med.
243, 256 –261 (2018).
188. Gallas, B. D. et al. FDA fosters innovative approaches in research, resources, and
collaboration. Nat. Mach. Intell. 4,9 7 –98 (2022).
189. U.S. Food and Drug Administration. Arti ﬁcial Intelligence/Machine Learning (AI/
ML)-Based Software as a Medical Device (SaMD) Action Plan. https://
www.fda.gov/media/145022/download (2021).
190. U.S. Food and Drug Administration. Marketing submission recommendations for
a predetermined change control plan for arti ﬁcial intelligence-enabled device
software functions. https://www.fda.gov/regulatory-information/search-fda-
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
31
Signal Transduction and Targeted Therapy          (2026) 11:407

guidance-documents/marketing-submission-recommendations-predetermined-
change-control-plan-artiﬁcial-intelligence (2025).
191. Hu, Y., Zou, Y., Qiao, L. & Lin, L. Integrative proteomic and metabolomic eluci-
dation of cardiomyopathy with in vivo and in vitro models and clinical samples.
Mol. Ther. 32, 3288 –3312 (2024).
192. Babu, M. & Snyder, M. Multi-omics pro ﬁling for health. Mol. Cell. Proteom. 22,
100561 (2023).
193. Oikonomou, E. K. et al. Non-invasive detection of coronary in ﬂammation using
computed tomography and prediction of residual cardiovascular risk (the CRISP
CT study): a post-hoc analysis of prospective outcome data. Lancet 392,
929–939 (2018).
194. Attia, Z. I. et al. Screening for cardiac contractile dysfunction using an arti ﬁcial
intelligence-enabled electrocardiogram. Nat. Med. 25,7 0 –74 (2019).
195. Bai, W. et al. Automated cardiovascular magnetic resonance image analysis with
fully convolutional networks. J. Cardiovasc. Magn. Reson. 20, 65 (2018).
196. Shah, A. M. et al. Large scale plasma proteomics identi ﬁes novel proteins and
protein networks associated with heart failure development. Nat. Commun. 15,
528 (2024).
197. Faulkner, L. G., Howells, L. M., Pepper, C., Shaw, J. A. & Thomas, A. L. The utility of
ctDNA in detecting minimal residual disease following curative surgery in col-
orectal cancer: a systematic review and meta-analysis. Br. J. Cancer 128, 297–309
(2023).
198. Chidharla, A. et al. Circulating tumor DNA as a minimal residual disease
assessment and recurrence risk in patients undergoing curative-intent resection
with or without adjuvant chemotherapy in colorectal cancer: a systematic
review and meta-analysis. Int. J. Mol. Sci. 24, 10230 (2023).
199. Zheng, J., Qin, C., Wang, Q., Tian, D. & Chen, Z. Circulating tumour DNA-based
molecular residual disease detection in resectable cancers: a systematic review
and meta-analysis. EBioMedicine 103, 105109 (2024).
200. Zhu, L. et al. Minimal residual disease (MRD) detection in solid tumors
using circulating tumor DNA: a systematic review. Front. Genet. 14, 1172108
(2023).
201. Martín-Arana, J. et al. Whole-exome tumor-agnostic ctDNA analysis enhances
minimal residual disease detection and reveals relapse mechanisms in localized
colon cancer. Nat. Cancer 6, 1000 –1016 (2025).
202. Martínez-Castedo, B. et al. Minimal residual disease in colorectal cancer. Tumor-
informed versus tumor-agnostic approaches: unraveling the optimal strategy.
Ann. Oncol. 36, 263 –276 (2025).
203. Semenkovich, N. P., Szymanski, J. J., Earland, N., Chauhan, P. S. & Chaudhuri, A. A.
Genomic approaches to cancer and minimal residual disease detection using
circulating tumor DNA. J. Immunother. Cancer 11, e006284 (2023).
204. Rosenlund, L. et al. ctDNA can detect minimal residual disease in curative
treated non-small cell lung cancer patients using a tumor agnostic approach.
Lung Cancer 203, 108528 (2025).
205. Eslinger, C., Wu, C. & Ahn, D. H. Minimal residual disease monitoring via ctDNA: a
case report of Lynch syndrome with synchronous colorectal cancer and review
of literature. J. Gastrointest. Oncol. 15, 1341 –1347 (2024).
206. Kather, J. N. et al. Deep learning can predict microsatellite instability directly
from histology in gastrointestinal cancer. Nat. Med. 25, 1054 –1056 (2019).
207. Qian, L. et al. AI-empowered perturbation proteomics for complex biological
systems. Cell Genom. 4, 100691 (2024).
208. Sekar, P. K. & Veerabathiran, R. Systems immunology meets clinical translation:
multi-omic approaches to predict therapy response in cancer and autoimmune
disease. Clin. Immunol. Commun. 9, 22 (2025).
209. Yuen, K. C. et al. High systemic and tumor-associated IL-8 correlates with
reduced clinical bene ﬁt of PD-L1 blockade. Nat. Med. 26, 693 –698 (2020).
210. Kasi, P. M. et al. Impact of circulating tumor DNA-based detection of molecular
residual disease on the conduct and design of clinical trials for solid tumors. JCO
Precis. Oncol. 6, e2100181 (2022).
211. Bartolomucci, A. et al. Circulating tumor DNA to monitor treatment response in
solid tumors and advance precision oncology. NPJ Precis. Oncol. 9, 84 (2025).
212. García de Yébenes Prous, M. J. & Carmona Ortells, L. Biomarkers: how to con-
solidate them in clinical practice. Reumatol. Clin. 20, 386 –391 (2024).
213. Mattsson-Carlgren, N. et al. Longitudinal plasma p-tau217 is increased in early
stages of Alzheimer ’s disease. Brain 143, 3234 –3241 (2020).
214. Hansson, O., Blennow, K., Zetterberg, H. & Dage, J. Blood biomarkers for Alz-
heimer’s disease in clinical practice and trials. Nat. Aging 3, 506 –519 (2023).
215. Jack, C. R. et al. NIA-AA Research Framework: toward a biological de ﬁnition of
Alzheimer’s disease. Alzheimers Dement. 14, 535 –562 (2018).
216. Leuzy, A. et al. Tau PET imaging in neurodegenerative tauopathies —still a
challenge. Mol. Psychiatry 24, 1112 –1134 (2019).
217. Mormino, E. C. et al. Tau PET imaging with 18F-PI-2620 in aging and neurode-
generative diseases. Eur. J. Nucl. Med. Mol. Imaging 48, 2233 –2244 (2021).
218. Ravi, D. et al. Deep learning for health informatics. IEEE J. Biomed. Health Inform.
21,4 –21 (2017).
219. Zhang, W., Xiao, D., Mao, Q. & Xia, H. Role of neuroin ﬂammation in neurode-
generation development. Signal Transduct. Target. Ther. 8, 267 (2023).
220. van der Kant, R., Goldstein, L. S. B. & Ossenkoppele, R. Amyloid- β-independent
regulators of tau pathology in Alzheimer disease. Nat. Rev. Neurosci. 21,2 1 –35
(2020).
221. Serrano-Pozo, A., Frosch, M. P., Masliah, E. & Hyman, B. T. Neuropathological
alterations in Alzheimer disease. Cold Spring Harb. Perspect. Med. 1, a006189
(2011).
222. Schöll, M. et al. Challenges in the practical implementation of blood biomarkers
for Alzheimer ’s disease. Lancet Healthy Longev. 5, 100630 (2024).
223. Smillie, C. S. et al. Intra- and inter-cellular rewiring of the human colon during
ulcerative colitis. Cell 178, 714 –730.e22 (2019).
224. Wang, L. et al. An atlas of single-cell eQTLs dissects autoimmune disease genes
and identi ﬁes novel drug classes for treatment. Cell Genom. 5, 100820 (2025).
225. Smolen, J. S. et al. Treating rheumatoid arthritis to target: recommendations of
an international task force. Ann. Rheum. Dis. 69, 631 –637 (2010).
226. Hauser, S. L. & Cree, B. A. C. Treatment of multiple sclerosis: a review. Am. J. Med.
133, 1380 –1390.e2 (2020).
227. Tilg, H., Byrne, C. D. & Targher, G. NASH drug treatment development: chal-
lenges and lessons. Lancet Gastroenterol. Hepatol. 8, 943 –954 (2023).
228. Thiele, M. et al. Opportunities and barriers in omics-based biomarker discovery
for steatotic liver diseases. J. Hepatol. 81, 345 –359 (2024).
229. Lazarus, J. V. et al. A call for doubling the diagnostic rate of at-risk metabolic
dysfunction-associated steatohepatitis. Lancet Reg. Health Eur. 54, 101320
(2025).
230. Noureddin, M. et al. Serum identi ﬁcation of at-risk MASH: the metabolomics-
advanced steatohepatitis ﬁbrosis score (MASEF). Hepatology 79, 135–148 (2024).
231. Rinella, M. E. & Sookoian, S. From NAFLD to MASLD: updated naming and
diagnosis criteria for fatty liver disease. J. Lipid Res. 65, 100485 (2024).
232. Sergi, C. M. NAFLD (MASLD)/NASH (MASH): does it bother to label at all? A
comprehensive narrative review. Int. J. Mol. Sci. 25, 8462 (2024).
233. Park, I. G. et al. Gut microbiota-based machine-learning signature for the
diagnosis of alcohol-associated and metabolic dysfunction-associated steatotic
liver disease. Sci. Rep. 14, 16122 (2024).
234. Sveinbjornsson, G. et al. A multi-omics study of non-alcoholic fatty liver disease.
Nat. Genet. 54, 1652 –1663 (2022).
235. Verschuren, L. et al. Development of a novel non-invasive biomarker panel for
hepatic ﬁbrosis in MASLD. Nat. Commun. 15, 4564 (2024).
236. Stratakis, N. et al. Multi-omic architecture, biological pathways, and prenatal
determinants of childhood obesity and metabolic dysfunction. Nat. Commun.
16, 654 (2025).
237. Chakaroun, R. M. et al. Multi-omic de ﬁnition of metabolic obesity through adi-
pose tissue-microbiome interactions. Nat. Med. 32, 113 –125 (2026).
238. Soták, M., Clark, M., Suur, B. E. & Börgeson, E. In ﬂammation and resolution in
obesity. Nat. Rev. Endocrinol. 21,4 5 –61 (2025).
239. Rönn, T., Per ﬁlyev, A., Oskolkov, N. & Ling, C. Predicting type 2 diabetes via
machine learning integration of multiple omics from human pancreatic islets.
Sci. Rep. 14, 14637 (2024).
240. Dai, L. et al. A deep learning system for predicting time to progression of
diabetic retinopathy. Nat. Med. 30, 584 –594 (2024).
241. Ratziu, V. et al. Con ﬁrmatory biomarker diagnostic studies are not needed when
transitioning from NAFLD to MASLD. J. Hepatol. 80, e51 –e52 (2024).
242. Chen, L., Zhang, X. & Shi, P. Recent advances in biomarkers for detection and
diagnosis of sepsis and organ dysfunction: a comprehensive review. Eur. J. Med.
Res. 30, 1081 (2025).
243. de Nooijer, A. H., Pickkers, P., Netea, M. G. & Kox, M. In ﬂammatory biomarkers to
predict the prognosis of acute bacterial and viral infections. J. Crit. Care 78,
154360 (2023).
244. Xiong, W., Zhan, Y., Xiao, R. & Liu, F. Advancing sepsis diagnosis and immu-
notherapy: machine learning-driven identi ﬁcation of stable molecular bio-
markers and therapeutic targets. Sci. Rep. 15, 8333 (2025).
245. Yang, J. et al. Machine learning based screening of biomarkers associated with
cell death and immunosuppression of multiple life stages sepsis populations.
Sci. Rep. 15, 30302 (2025).
246. Rolfo, C. et al. Liquid biopsy for advanced NSCLC: a consensus statement from
the International Association for the Study of Lung Cancer. J. Thorac. Oncol. 16,
1647–1662 (2021).
247. Sabari, J. K. et al. A prospective study of circulating tumor DNA to guide mat-
ched targeted therapy in lung cancers. J. Natl. Cancer Inst. 111, 575–583 (2019).
248. Jiang, P. et al. Signatures of T cell dysfunction and exclusion predict cancer
immunotherapy response. Nat. Med. 24, 1550 –1558 (2018).
249. Auslander, N. et al. Robust prediction of response to immune checkpoint
blockade therapy in metastatic melanoma. Nat. Med. 24, 1545 –1549 (2018).
250. Berry, S. M., Carlin, B. P., Lee, J. J. & Muller, P. Bayesian Adaptive Methods for
Clinical Trials (CRC Press, 2010).
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
32
Signal Transduction and Targeted Therapy          (2026) 11:407

251. Topalian, S. L., Taube, J. M., Anders, R. A. & Pardoll, D. M. Mechanism-driven
biomarkers to guide immune checkpoint blockade in cancer therapy. Nat. Rev.
Cancer 16, 275 –287 (2016).
252. Subbiah, V. & Kurzrock, R. Challenging standard-of-care paradigms in the pre-
cision oncology era. Trends Cancer 4, 101 –109 (2018).
253. Okusanya, O. O. et al. FDA-AACR strategies for optimizing dosages for oncology
drug products: early-phase trials using innovative trial designs and biomarkers.
Clin. Cancer Res. 31, 4882 –4890 (2025).
254. Fleming, T. R. & DeMets, D. L. Surrogate end points in clinical trials: are we being
misled? Ann. Intern. Med. 125, 605 –613 (1996).
255. Fleming, T. R. & Powers, J. H. Biomarkers and surrogate endpoints in clinical
trials. Stat. Med. 31, 2973 –2984 (2012).
256. Moqri, M. et al. Validation of biomarkers of aging. Nat. Med. 30, 360–372 (2024).
257. Sherman, R. E. et al. Real-world evidence —what is it and what can it tell us? N.
Engl. J. Med. 375, 2293 –2297 (2016).
258. Ohtsu, H., Shimomura, A. & Sase, K. Real-world evidence in cardio-oncology:
what is it and what can it tell us? JACC CardioOncol. 4,9 5 –97 (2022).
259. Griesinger, F., Cox, O., Sammon, C., Ramagopalan, S. V. & Popat, S. Health
technology assessments and real-world evidence: tell us what you want, what
you really, really want. J. Comp. Eff. Res. 11, 297 –299 (2022).
260. Ardic, N. & Dinc, R. Arti ﬁcial intelligence in healthcare: current regulatory
landscape and future directions. Br. J. Hosp. Med. 86,1 –21 (2025).
261. U.S. Food and Drug Administration. Biomarker quali ﬁcation: evidentiary fra-
mework. https://www.fda.gov/regulatory-information/search-fda-guidance-
documents/biomarker-qualiﬁcation-evidentiary-framework (2018).
262. Coravos, A., Khozin, S. & Mandl, K. D. Developing and adopting safe and
effective digital biomarkers to improve patient outcomes. NPJ Digit. Med. 2,1 4
(2019).
263. Price, W. N. II. & Cohen, I. G. Privacy in the age of medical big data. Nat. Med. 25,
37–43 (2019).
264. Patel, A. P. et al. A multi-ancestry polygenic risk score improves risk prediction
for coronary artery disease. Nat. Med. 29, 1793 –1803 (2023).
265. GBD 2023 Causes of Death Collaborators Global burden of 292 causes of death
in 204 countries and territories and 660 subnational locations, 1990 –2023: a
systematic analysis for the Global Burden of Disease Study 2023. Lancet 406,
1811–1872 (2025).
266. Alum, E. U. AI-driven biomarker discovery: enhancing precision in cancer
diagnosis and prognosis. Discov. Oncol. 16, 313 (2025).
267. Singh, Y. et al. Beyond post hoc explanations: a comprehensive framework for
responsible arti ﬁcial intelligence in medical imaging through transparency,
interpretability, and explainability. Bioengineering12, 879 (2025).
268. Begley, C. G. & Ellis, L. M. Drug development: raise standards for preclinical
cancer research. Nature 483, 531 –533 (2012).
269. Laird, A. R. Large, open datasets for human connectomics research: considera-
tions for reproducible and responsible data use. Neuroimage 244, 118579
(2021).
270. Fountzilas, E., Pearce, T., Baysal, M. A., Chakraborty, A. & Tsimberidou, A. M.
Convergence of evolving arti ﬁcial intelligence and machine learning techniques
in precision oncology. NPJ Digit. Med. 8, 75 (2025).
271. Mendez, K. M. et al. A roadmap to precision medicine through post-genomic
electronic medical records. Nat. Commun. 16, 1700 (2025).
272. Liu, Y., Dai, Y. & Wang, L. Spatial omics at the forefront: emerging technologies,
analytical innovations, and clinical applications. Cancer Cell 44,2 4 –49 (2026).
273. Zhang, Y. et al. Robust integration and annotation of single-cell and spatial
omics data using interpretable gene programs. Cell Genom. 6, 101105 (2025).
274. Van de Sande, B. et al. Applications of single-cell RNA sequencing in drug
discovery and development. Nat. Rev. Drug Discov. 22, 496 –520 (2023).
275. Dasaradharami Reddy, K. & Gadekallu, T. R. A comprehensive survey on feder-
ated learning techniques for healthcare informatics. Comput. Intell. Neurosci.
2023, 8393990 (2023).
276. Olawade, D. B. et al. Digital twin paradigm in diabetes prediction and man-
agement. Diab. Res. Clin. Pract. 231, 113075 (2026).
277. Viceconti, M. et al. In silico trials: veri ﬁcation, validation and uncertainty quan-
tiﬁcation of predictive models used in the regulatory evaluation of biomedical
products. Methods 185, 120 –127 (2021).
278. Strimbu, K. & Tavel, J. A. What are biomarkers? Curr. Opin. HIV AIDS 5, 463 –466
(2010).
279. Chenchula, S., Paraskar, G., Krishna, S. & Chavan, M. Liquid biopsy in clinical
practice: current evidence and future directions. In Liquid Biopsy in Cancer
Management (eds Bhatt, S., Anitha, A., Chenchula, S. & Mishra, N.) 405 –438
(Academic Press, 2026).
280. Ohara, S. & Suda, K. Current status and future challenges of liquid biopsy. Cells
14, 2000 (2025).
281. Abràmoff, M. D., Lavin, P. T., Birch, M., Shah, N. & Folk, J. C. Pivotal trial of an
autonomous AI-based diagnostic system for detection of diabetic retinopathy in
primary care of ﬁces. NPJ Digit. Med. 1, 39 (2018).
282. Elijovich, L. et al. Automated emergent large vessel occlusion detection by
artiﬁcial intelligence improves stroke work ﬂow in a hub and spoke stroke sys-
tem of care. J. Neurointerv. Surg. 14, 704 –708 (2022).
283. Chilamkurthy, S. et al. Deep learning algorithms for detection of critical ﬁndings
in head CT scans: a retrospective study. Lancet 392, 2388 –2396 (2018).
284. Komorowski, M., Celi, L. A., Badawi, O., Gordon, A. C. & Faisal, A. A. The Arti ﬁcial
Intelligence Clinician learns optimal treatment strategies for sepsis in intensive
care. Nat. Med. 24, 1716 –1720 (2018).
285. Weikert, T. et al. Automated detection of pulmonary embolism in CT pulmonary
angiograms using an AI-powered algorithm. Eur. Radiol. 30, 6545 –6553 (2020).
286. Beam, A. L. & Kohane, I. S. Big data and machine learning in health care. JAMA
319, 1317 –1318 (2018).
287. Esteva, A. et al. A guide to deep learning in healthcare. Nat. Med. 25,2 4–29 (2019).
288. Willis, B. H. Spectrum bias —why clinicians need to be cautious when applying
diagnostic test studies. Fam. Pract. 25, 390 –396 (2008).
289. Hernán, M. A. & Robins, J. M. Using big data to emulate a target trial when a
randomized trial is not available. Am. J. Epidemiol. 183, 758 –764 (2016).
290. Poldrack, R. A. et al. Scanning the horizon: towards transparent and reproducible
neuroimaging research. Nat. Rev. Neurosci. 18, 115 –126 (2017).
291. Wiens, J. et al. Do no harm: a roadmap for responsible machine learning for
health care. Nat. Med. 25, 1337 –1340 (2019).
292. Kim, J. et al. Deep learning-based long-term risk evaluation of incident type 2
diabetes using electrocardiogram in a non-diabetic population: a retrospective,
multicentre study. EClinicalMedicine 68, 102445 (2024).
293. Fraser, R. A., Walker, R. J., Campbell, J. A., Ekwunife, O. & Egede, L. E. Integration
of arti ﬁcial intelligence and wearable technology in the management of dia-
betes and prediabetes. NPJ Digit. Med. 8, 687 (2025).
294. Lee, H. et al. External validation of ECG arti ﬁcial intelligence for emergency and
cardiac assessment across a large-scale U.S. healthcare system. NPJ Digit. Med .
https://doi.org/10.1038/s41746-026-02682-7 (2026).
295. FDA-NIH Biomarker Working Group. BEST (Biomarkers, EndpointS, and other
Tools) Resource (Food and Drug Administration (US); FDA-NIH Biomarker
Working Group, 2016).
296. Ciani, O. et al. Time to review the role of surrogate end points in health policy:
state of the art and the way forward. Value Health 20, 487 –495 (2017).
297. Chandrabhatla, A. S. et al. Arti ﬁcial intelligence and machine learning in the
diagnosis and management of stroke: a narrative review of United States Food
and Drug Administration-approved technologies. J. Clin. Med. 12, 3755 (2023).
298. Carvalho, E. et al. Predetermined change control plans: guiding principles for
advancing safe, effective, and high-quality AI-ML technologies. JMIR AI 4,
e76854 (2025).
299. Liu, X., Cruz Rivera, S., Moher, D. & Calvert, M. J. Reporting guidelines for clinical
trial reports for interventions involving arti ﬁcial intelligence: the CONSORT-AI
extension. Lancet Digit. Health 2, e537 –e548 (2020).
300. Rivera, S. C., Liu, X., Chan, A. W., Denniston, A. K. & Calvert, M. J. Guidelines for
clinical trial protocols for interventions involving arti ﬁcial intelligence: the
SPIRIT-AI Extension. BMJ 370, m3210 (2020).
301. Aboy, M., Minssen, T. & Vayena, E. Navigating the EU AI Act: implications for
regulated digital medical products. NPJ Digit. Med. 7, 237 (2024).
302. Yuan, H. Toward real-world deployment of machine learning for health care:
external validation, continual monitoring, and randomized clinical trials. Health
Care Sci. 3, 360 –364 (2024).
Open Access This article is licensed under a Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License,
which permits any non-commercial use, sharing, distribution and reproduction in any
medium or format, as long as you give appropriate credit to the original author(s) and
the source, provide a link to the Creative Commons licence, and indicate if you modiﬁed
the licensed material. You do not have permission under this licence to share adapted
material derived from this article or parts of it. The images or other third party material in
this article are included in the article ’s Creative Commons licence, unless indicated
otherwise in a credit line to the material. If material is not included in the article ’s
Creative Commons licence and your intended use is not permitted by statutory
regulation or exceeds the permitted use, you will need to obtain permission directly
from the copyright holder. To view a copy of this licence, visit http://
creativecommons.org/licenses/by-nc-nd/4.0/.
© The Author(s) 2026
Artiﬁcial intelligence in biomarker discovery for diseases: diagnostic. . .
Dinc and Ardic
33
Signal Transduction and Targeted Therapy          (2026) 11:407
