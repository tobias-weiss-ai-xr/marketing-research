---
title: 'Trustworthy AI for Marketing Measurement: A Systematic Review of Attribution, Media Mix Modeling,
  and Privacy-Preserving Methods'
url: https://doi.org/10.21203/rs.3.rs-10322944/v1
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: Research Square
authors:
- Longying Lai
- Zhiyuan Cheng
- Yue Liu
source: openalex-oa
pdf_url: https://www.researchsquare.com/article/rs-10322944/latest.pdf
pages: 54
chars: 151190
fetched_at: '2026-11-08T18:07:53+00:00'
kb_version: 1
---

# Trustworthy AI for Marketing Measurement: A Systematic Review of Attribution, Media Mix Modeling, and Privacy-Preserving Methods

Trustworthy AI for Marketing Measurement: A
Systematic Review of Attribution, Media Mix
Modeling, and Privacy-Preserving Methods
Longying Lai 
University of Rochester https://orcid.org/0009-0000-3515-450X
Zhiyuan Cheng 
Stanford University https://orcid.org/0009-0003-2845-5322
Yue Liu 
Rutgers University
Systematic Review
Keywords: Marketing measurement, Multi-touch attribution, Media mix modeling, Causal inference, Deep
learning, AI trustworthiness
Posted Date: July 14th, 2026
DOI: https://doi.org/10.21203/rs.3.rs-10322944/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Additional Declarations: The authors declare no competing interests.

Trustworthy AI for Marketing Measurement: A
Systematic Review of Attribution, Media Mix
Modeling, and Privacy-Preserving Methods
Longying Lai 1*, Zhiyuan Cheng 2 and Yue Liu 3
1*Simon Business School, University of Rochester, Rochester, NY, USA.
2School of Engineering, Stanford University, Stanford, CA, USA.
3Accounting & Information Systems, Rutgers University, Newark, NJ,
USA.
*Corresponding author(s). E-mail(s): lai.longying@urgrad.rochester.edu;
Contributing authors: zhycheng@stanford.edu;
yl1641@scarletmail.rutgers.edu;
Abstract
Marketing measurement faces a triple disruption: privacy regulati ons restrict
user-level data, artiﬁcial intelligence transforms modeling ca pabilities, and large-
scale ﬁeld experiments expose systematic biases in platform-re ported advertising
eﬀectiveness. This systematic review synthesizes 108 studi es (2010–2026) on how
AI and machine learning reshape measurement across multi-touch attribution,
media mix modeling, causal calibration, and privacy-preservin g measurement.
We develop a two-dimensional taxonomy mapping AI technique s to measurement
functions and propose a “Measure–Validate–Protect” (MVP) framew ork that
adapts NIST AI trustworthiness dimensions to marketing contex ts. Three ﬁnd-
ings emerge. First, deep learning attribution improves predictiv e accuracy but
remains causally unidentiﬁed without experimental calibrati on. Second, neural
media mix models can outperform traditional Bayesian frameworks in selected
benchmark and production settings, yet causal credibility dep ends on external
validation and generalization remains under-tested. Third, pri vacy-preserving
techniques impose measurable accuracy costs: diﬀerential priv acy reduces preci-
sion by 2–33% depending on privacy budget, while federated appro aches have
retained roughly 90–95% of centralized performance in documented deployments.
We identify gaps at the intersection of causal validity and priv acy compliance
and propose a research agenda for trustworthy marketing AI.
1

Keywords: Marketing measurement, Multi-touch attribution, Media mi x modeling,
Causal inference, Deep learning, AI trustworthiness
1 Introduction
Digital advertising has grown into a multi-hundred-billion-dollar industry, yet the fun-
damental question of whether and how much advertising works remains s urprisingly
diﬃcult to answer (Lewis and Rao 2015). Large-scale ﬁeld experiments have demon-
strated that platform-reported attribution metrics systematically overstate advertising
eﬀectiveness. Gordon et al. (2019) analyzed 15 Facebook ﬁeld experiments encompass-
ing 500 million users and 1.6 billion impressions, ﬁnding that observat ional approaches
“often fail to produce the same results as true experiments.” In a s ubsequent study,
Gordon et al. (2023) benchmarked non-experimental methods against 663 Face-
book randomized controlled trials (RCTs), revealing that even sophis ticated machine
learning approaches such as double/debiased machine learning (DML) and s tratiﬁed
propensity score matching (SPSM) produced median errors of 62–115% relati ve to
experimental benchmarks, despite access to over 5,000 user-level features.
The consequences are compounded by the small magnitude of true adverti sing
eﬀects. A meta-analysis of 538 advertising elasticities (Shapiro et al . 2022) found
average short-term elasticities of just 0.0008—meaning a 10% increase in adv ertising
spend yields only a 0.008% increase in sales. When measurement errors r outinely reach
62–115% (Gordon et al. 2023), they are orders of magnitude larger than the eﬀects
they are meant to detect. This makes the distinction between pred ictive accuracy
and causal validity not merely methodological, but existential for marke ting resource
allocation (Srinivasan et al. 2010), as we detail in Section 5.1.1.
This measurement crisis is compounded by two concurrent structu ral shifts. First,
privacy regulations—including the EU General Data Protection Regulati on (GDPR),
the California Consumer Privacy Act (CCPA), and Apple’s App Tracking Tr ans-
parency (ATT) framework—have dramatically reduced the availability of user-level
tracking data. Aridor et al. (2023) documented a 12.5% drop in observable consum ers
following GDPR implementation, while ATT reduced Meta advertis ing click-through
rates by 37% (Aridor et al. 2024). Second, the deprecation of third-party cooki es
threatens to further fragment the identity graph upon which multi- touch attribution
depends. Lin and Misra (2022) proved that identity fragmentation bias cann ot be
signed or bounded even in randomized experiments, with simulations showing eﬀect
inﬂation of 40–88% depending on the channel and device combination.
Against this backdrop, artiﬁcial intelligence and machine learning tec hniques have
emerged as potentially transformative tools for marketing measurement . These tech-
nologies reshape measurement at three distinct levels. At the modeling level , deep
learning architectures—Transformers (Bencina et al. 2025), Neural ODEs (Zhan et al.
2024), and graph neural networks—replace linear or shallow models with expr essive
sequence representations. At the inference level, causal structure discovery algorithms
(Gong et al. 2024; Tirumala 2025) promise to learn channel interdependencie s from
2

data. At the protection level, diﬀerential privacy (Ghazi et al. 2024), federated learn-
ing (Li et al. 2024), and cryptographic protocols (Du et al. 2025) enable measureme nt
under privacy constraints.
However, the deployment of AI in marketing measurement raises fund amental
questions about trustworthiness. Predictive accuracy does not guaran tee causal valid-
ity, and automation of modeling choices does not eliminate the need for e xperimental
calibration.
T rustworthy AI: deﬁnition and scope. We adopt the deﬁnition of trustworthy
AI from the NIST AI Risk Management Framework (National Institute of Standards
and Technology 2023): an AI system is trustworthy when its properties of vali dity, reli-
ability, explainability, transparency, and privacy are demonstrably maintained across
its intended deployment context. Trustworthiness is not an intr insic property of a
model architecture but a system-level property that depends on ( i) what the system
is used to decide, (ii) the quality of the data on which it is trained , and (iii) the gover-
nance mechanisms in place to audit and correct its outputs. This deﬁn ition diﬀers from
general “AI accuracy” or “AI eﬀectiveness” because it centers on decision -relevant
properties—particularly causal validity and privacy compliance—that pr edictive per-
formance metrics do not capture. In the marketing context, trustwor thiness means that
measurement outputs can be relied upon for budget allocation decisions: they recover
causal eﬀects rather than spurious correlations, remain stable across cam paigns and
market conditions, and comply with applicable privacy regulations.
Why marketing measurement speciﬁcally exposes AI trustworthine ss
concerns. It is important to ask whether the trustworthiness concerns we ide ntify
are new to AI or preexist in traditional marketing measurement. The ans wer is “both,
but AI intensiﬁes them.” Traditional rule-based attribution (last- touch, linear) was
already causally unidentiﬁed—it confounded selection with causation an d was known
to overstate eﬀectiveness (Dalessandro et al. 2012). Classical MMM rel ied on struc-
tural assumptions (constant adstock, linear saturation) that practition ers knew could
be violated. These concerns therefore originate partly in the marketi ng discipline
itself—speciﬁcally in the structural diﬃculty of establishing causal claims from obser-
vational advertising data (Section 5.1.1)—and partly in data limitations (s election
bias, identity fragmentation, cookie deprecation). AI does not create t hese concerns;
it raises the stakes in three ways. First, black-box models obscure which assumption s
are being made, making assumption violations harder to detect. Second, automation
of model selection removes the domain-knowledge guardrails that help ed practition-
ers bound errors in simpler systems. Third, the scale at which AI-d riven attribution
operates—hundreds of millions of users, real-time bidding decision s—means that sys-
tematic biases compound into larger misallocations. The organizing prin ciple of this
review is therefore not “AI is untrustworthy” but rather: the trustworthiness con-
straints that always existed in marketing measurement are more co nsequential when
AI is the measurement engine.
Trustworthiness provides a useful unifying lens for navigating these questions:
the NIST AI Risk Management Framework (National Institute of Standards and
Technology 2023)—a widely adopted engineering standard for evaluating AI sys-
tem trustworthiness, published by the U.S. National Institute of St andards and
3

Technology—identiﬁes validity, reliability, explainability, and p rivacy as core dimen-
sions of trustworthy AI. We adapt these dimensions to the marketing me asurement
context as follows:
Four NIST trustworthiness dimensions guide our synthesis. V alidity: Does the
system recover causal eﬀects rather than correlations? (Gordon et al. 2023 showed
observational attribution can overstate eﬀects by 2–5 ×.) Reliability: Does it pro-
duce stable estimates across datasets and time? (62% of CATE estimates ha ve higher
MSE than a zero-eﬀect predictor Curth et al. 2025.) Explainability: Can stake-
holders understand credit allocation across channels? Privacy: Does it comply with
regulatory requirements while preserving measurement utility ? This four-way mapping
motivates our “Measure–Validate–Protect” (MVP) framework (Section 7), whi ch posi-
tions causal calibration and privacy compliance as necessary conditions for trustworthy
AI-driven measurement, rather than optional add-ons.
This review diﬀers from prior reviews in three ways. Unlike prior reviews that
examine AI in digital marketing broadly—covering content generation, re commenda-
tion, customer analytics, and measurement within a single survey (B asu et al. 2024;
Gaur and Bharti 2020)—or focus narrowly on a single method, this review foc uses
speciﬁcally on the measurement infrastructure through which ﬁrms estimate adver-
tising eﬀectiveness, allocate budgets, and justify marketing in vestment under privacy
constraints. No existing review provides an integrated examination of how AI tech-
niques interact across the full measurement pipeline from attribu tion through causal
validation to privacy compliance. This gap is consequential: advances in one domain
(e.g., neural attribution) may be rendered moot by constraints in anot her (e.g.,
privacy-induced data loss).
Table 1 positions this review against the closest existing work.
T able 1 Comparison with closely related prior reviews. Checkmarks (✓) indicate that the review
substantively addresses the dimension; dashes (–) indicat e limited or no coverage. “Trustworthiness
lens” denotes whether the review explicitly applies a trust worthiness or causal-validity framework;
“Privacy-compliant measurement” denotes coverage of DP, f ederated learning, or aggregate-causal
methods.
Review Attribution MMM Causal
calibration
Privacy-
compliant
measurement
Trustworthiness
lens
Basu et al. (2024) ✓ – – – –
Gaur et al. (2020) ✓ – – – –
This review (2026) ✓ ✓ ✓ ✓ ✓
Basu et al. (2024) review AI and ML across digital marketing b roadly, including content, recommendation,
and analytics, but do not cover MMM, causal calibration, or p rivacy-preserving measurement as distinct
topics. Gaur et al. (2020) survey AI applications in digital marketing with a practitioner orientation, again
without systematic coverage of causal validity or privacy c ompliance. This review is the ﬁrst to treat the
four measurement functions—attribution, MMM, causal cali bration, and privacy—as an integrated pipeline
subject to a uniﬁed trustworthiness framework.
This systematic review makes three focused contributions:
1. A measurement-speciﬁc synthesis of 108 studies (2010–2026) at the intersec-
tion of AI and marketing measurement—attribution, media mix modeling, causal
calibration, and privacy-preserving measurement—rather than a broad r eview of
4

AI in marketing. The review is reported according to PRISMA 2020 (Page et al .
2021) with reviewer calibration, consensus-based screening of ambiguous cases, an
a priori coding protocol, and a four-level evidence-grading scheme (Section 2) to
ensure transparency and reproducibility.
2. A trustworthiness taxonomy (Table 2) mapping AI techniques against measure-
ment functions and surfacing the trustworthiness risks (validit y, reliability, explain-
ability, privacy) each combination raises, enabling identiﬁcation of m ethodological
opportunities and gaps.
3. A practitioner-ready Measure–V alidate–Protect (MVP) framework
(Section 7) that operationalizes NIST trustworthiness dimensions for m arketing
measurement, with diagnostic metrics, failure modes, and recommen ded actions
per pillar (Table 6), plus a maturity-aligned Managerial Decision Guide (Table 9)
for choosing a measurement architecture.
A research agenda emerging from this review (Section 8) spans scalable c alibration,
foundation models, trustworthiness, and cross-platform measuremen t. We address
three research questions:
• RQ1: To what extent do AI methods improve the accuracy and scalability of
attribution and media mix models, and are these improvements consi stent across
measurement functions (attribution, MMM) or method families (dee p learning,
causal discovery, hybrid approaches)? The unit of analysis in RQ1 is t he measure-
ment function : we compare AI methods within each function (e.g., deep learning
MTA architectures) against each other and against traditional baselines, r ather than
treating all AI applications as a single undiﬀerentiated technology. Se ction 3 covers
attribution and Section 4 covers MMM; results are not pooled across fun ctions.
• RQ2: What is the causal credibility of AI-driven measurement methods, and how
can experimental calibration enhance it?
• RQ3: Under privacy constraints, what are the feasibility and accuracy trade -oﬀs of
AI-based measurement approaches?
As shown in Table 2, the reviewed AI methods cluster diﬀerently acr oss attribution,
MMM, causal calibration, and privacy-preserving measurement funct ions.
5

T able 2 Taxonomy of AI methods in marketing measurement. Column hea ders map to Sections 3
(Attribution), 4 (MMM), 5 (Causal), and 6 (Privacy). Cells i ndicate representative systems; ‘—’
denotes combinations with no identiﬁed implementation in t he reviewed corpus, representing
potential research opportunities.
AI/ML method Attribution MMM Causal Privacy
RNN / LSTM / GRU DeepMTA,
CAMTA
DeepCausalMMM — —
Transformer LiDDA NNN — —
Neural ODE ODE-LSTM — — —
DAG / causal
discovery
CDA (PCMCI) CausalMMM — —
DML / debiased ML — — DICE-DML —
Causal forest / GRF — — Snap HTE, PIE —
Diﬀerential privacy — — — AdsBPC
Federated learning — — — Clean Room
Cryptography — — — PrivacyGo, IPA
The remainder of this paper is organized as follows. Section 2 describe s the sys-
tematic review methodology. Sections 3 and 4 review AI methods for attr ibution and
media mix modeling. Section 5 examines causal calibration and validation . Section 6
addresses privacy-preserving measurement. Section 7 formalizes the MVP framework.
Section 8 discusses future directions, and Section 9 concludes.
2 Methodology
2.1 Review Protocol
This review follows the Preferred Reporting Items for Systemati c Reviews and Meta-
Analyses (PRISMA) 2020 guidelines (Page et al. 2021). Given the interdiscip linary
nature of the topic—spanning marketing science, machine learning, cau sal inference,
and privacy engineering—we adopted a hybrid search strategy combining d atabase
searches with forward and backward citation tracking. The complete searc h strings are
provided in Appendix B, the coding protocol in Appendix C, and the full included-
studies matrix in Appendix D.
2.2 Search Strategy and Database Results
We searched ﬁve databases: Scopus, Web of Science, IEEE Xplore, ACM Di gital
Library, and arXiv/SSRN preprint repositories. The search was conducte d between
January and March 2026 and restricted to English-language records (publish ed or
posted) from 2010 to 2026. Boolean queries combined three concept blocks (C 1 mar-
keting measurement, C2 AI/ML methods, C3 validation/privacy) with t he pattern
C1 AND (C2 OR C3) . The representative Scopus query was:
TITLE-ABS-KEY(
("multi-touch attribution" OR "media mix model*" OR
"marketing measurement" OR "advertising effectiveness" OR
"return on ad spend" OR "ROAS" OR "advertising lift")
AND
(("deep learning" OR "neural network*" OR "transformer" OR
"recurrent neural" OR "graph neural" OR "machine learning" OR
6

"causal inference" OR "heterogeneous treatment effect" OR
"uplift model*" OR "double machine learning")
OR
("randomized experiment" OR "field experiment" OR "A/B test*" OR
"geo experiment" OR "causal calibration" OR "differential privacy" OR
"federated learning" OR "clean room" OR "privacy-preserving")))
AND PUBYEAR > 2009 AND PUBYEAR < 2027 AND LANGUAGE(english)
Full search strings for all ﬁve databases, including ﬁeld-speciﬁc ad aptations, are pro-
vided in Appendix B. Per-database yields were: Scopus = 312, Web of Scie nce =
248, IEEE Xplore = 137, ACM Digital Library = 94, arXiv/SSRN = 56; total raw
records = 847. After automated de-duplication (DOI and normalized-title m atching)
we removed 212 duplicates, leaving 635 unique records for title-and- abstract screening.
2.3 Screening, Selection, and Reviewer Calibration
Inclusion criteria required papers to: (a) address marketing or adve rtising measure-
ment, attribution, or media mix modeling; (b) employ or evaluate AI/ML methods,
causal inference techniques, or privacy-preserving technologies ; and (c) present
empirical results, theoretical frameworks, or systematic reviews . Exclusion criteria
removed papers focused exclusively on recommendation systems, content generation,
or consumer behavior without a measurement component.
Reviewer calibration, inter-rater reliability , and consensus-bas ed
screening. Two authors independently reviewed a calibration subset of records
(approximately 10% of the 635 title/abstract records, n = 64, and all 189 full-text
candidates) to align interpretation of the inclusion criteria and cod ing dimensions; the
remaining records were screened by one author, with ambiguous cases ﬂagge d for joint
review. On the title/abstract calibration subset ( n = 64), inter-rater agreement on the
binary inclusion decision reached Cohen’s κ = 0 .81 (95% CI: 0.73–0.89), correspond-
ing to “almost perfect” agreement under the McHugh (2012) scale ( κ > 0.80). On
the evidence-grading dimension (Section 2.6), the two raters agreed e xactly on 74% of
calibration records and within one level on 97%, yielding a weighted κ = 0 .76 (“sub-
stantial” agreement). On the full-text calibration subset ( n = 189, all independently
dual-coded), binary inclusion agreement was κ = 0 .83. Disagreements and ﬂagged
cases were resolved through discussion; cases that could not be reconci led bilaterally
were adjudicated by a third author. The post-calibration screening of the remaining
title/abstract records was performed by one author, with all borderline or ambigu-
ous cases (those not clearly satisfying all three inclusion criteria) ﬂagged for joint
review rather than unilateral exclusion. This protocol, summarized in Appendix C and
Figure 1, is consistent with PRISMA 2020 reporting guidance (Page et al. 2021) an d
with widely cited practical guidance on interrater calibration in sys tematic reviews
(McHugh 2012).
Outcome. Of the 189 full-text articles assessed, 108 papers met all inclusion cr i-
teria and form the basis of this review. An additional 28 papers were iden tiﬁed as
seed papers through expert recommendation and served as starting point s for for-
ward and backward citation tracking; all 28 were re-run through the same rev iewer
7

calibration and consensus screening process to avoid introducing bias from expert rec-
ommendation. The complete exclusion breakdown by stage and reason is rep orted in
Appendix A. Figure 1 shows the PRISMA ﬂow from record identiﬁcation t hrough ﬁnal
inclusion.
Records from databases
(Scopus, WoS, IEEE, ACM)
n = 791
Records from other sources
(arXiv / SSRN preprints)
n = 56
Records after duplicate removal
n = 635 (removed: 212)
Records screened
(title and abstract)
n = 635
Excluded at screening
n = 446
Not measurement-focused: 289
No AI/ML component: 102
Non-English: 31
Trade publications: 24
Full-text articles assessed
for eligibility
n = 189
Excluded at full-text
n = 81
Insuﬃcient empir-
ical content: 38
Scope mismatch: 27
Superseded by later version: 16
Studies included in review
n = 108
(80 from search + 28
from citation tracking)
Fig. 1 PRISMA 2020 ﬂow diagram for systematic review study selecti on. Identiﬁcation stage: 791
database records and 56 preprint records (total 847), with 2 12 duplicates removed. Screening stage:
635 unique records screened by title/abstract, 446 exclude d. Eligibility stage: 189 full-text articles
assessed, 81 excluded with reasons. Included: 108 studies ( 80 from database search, 28 from expert
seeding and citation tracking).
2.4 Bibliometric Proﬁle of the Corpus
The 108 included studies span 2010–2026, with 55% published after 2023, reﬂecting
rapid convergence across AI, causal inference, and privacy engineering in marketing
measurement. By publication type, 25 studies appeared in journals, 16 in confer-
ence proceedings, and 44 as preprints; the remaining records consis t of white papers,
working papers, workshops, government/technical reports, software d ocumentation,
and review articles. Overall, 43 of the 108 records were coded as peer re viewed—the
8

high preprint share reﬂecting the norm in machine learning and priv acy engineering
where cutting-edge work routinely precedes journal publication by 1–2 years. Cor-
pus composition by domain: attribution modeling (22%), media mix mode ling (19%),
causal calibration (26%), privacy-preserving measurement (19%), and mu lti-domain
(14%). The complete included-studies matrix, with per-paper cod ing, venue type, and
evidence level, is reported in Appendix D.
2.5 Coding Protocol and Data Extraction
For each included paper, one author extracted the following items int o a shared spread-
sheet: (i) research question and study type; (ii) AI/ML method(s) employed; (iii) data
characteristics (scale, source, experimental vs. observational, pu blic vs. proprietary);
(iv) primary measurement function (attribution, MMM, causal calibr ation, privacy,
multi-domain); (v) key performance metrics (AUC, MAPE, R2, ATE, lift, ε, ROC-
AUC retention); (vi) limitations and threats to validity. A second aut hor audited
the calibration subset and all ambiguous or boundary cases ﬂagged during scre ening.
Coding categories are pre-speciﬁed in Appendix C (ﬁnalized before s creening began).
Categorical coding used two orthogonal dimensions. Dimension 1 — measurement
function—has four mutually exclusive primary values plus a multi-domain ﬂag. Di men-
sion 2 — AI technique —has nine values (RNN/LSTM/GRU; Transformer; Neural
ODE; DAG/causal discovery; DML/debiased ML; causal forest/GRF; diﬀere ntial
privacy; federated learning; cryptography) and is non-exclusive. Co dings were cross-
checked on the calibration subset, and disagreements were reconcile d by discussion;
see Appendix C.
Synthesis was conducted narratively, organized by the review framew ork sections,
because the heterogeneity of study designs and outcome metrics precl udes quantitative
meta-analysis of eﬀect sizes. Where possible, we report eﬀect-si ze ranges across studies
using a common unit (e.g., accuracy loss relative to a non-private basel ine; RMSE
relative to experimental ground truth).
A critical note on metric heterogeneity . Readers should exercise caution
when interpreting performance statistics cited across studies. Metrics such as AUC,
MAPE, RMSE, lift, ATE, ROC-AUC retention, and R2 measure fundamentally diﬀer-
ent aspects of model quality and are not directly comparable across studi es, models, or
measurement functions. For example, AUC measures rank-ordering abil ity for binary
conversion prediction, while MAPE measures percentage error in chann el contribution
estimates, and ATE measures the precision of average treatment eﬀect estimation—
these are incommensurable quantities. When we report ranges (e.g., “n eural MMM
reduces MAPE by 5–15 ×”), the range spans results within a single study or closely
related studies measuring the same quantity in comparable settings; it does not imply
that a model achieving AUC 0.98 is “equivalent in performance” to a mode l achieving
MAPE 3%. Throughout the review, we preserve the original metric report ed in each
study rather than converting to a common unit, and explicitly ﬂag whe n performance
claims come from a single proprietary deployment that may not generaliz e.
9

2.6 Evidence Grading
Because the corpus combines peer-reviewed marketing-science pap ers, computer-
science conference proceedings, and arXiv/SSRN preprints, we grade each study on a
four-level evidence scale. The four levels were chosen for the foll owing reasons. First,
the corpus spans three distinct institutional traditions—marketin g science (where
RCT-based ﬁeld experiments are the methodological gold standard), comp uter sci-
ence (where peer-reviewed conference proceedings carry the sam e weight as journals),
and practice-facing research (where industry white papers and pre prints precede for-
mal publication by 1–2 years). A single binary “peer-reviewed / not” dis tinction
would conﬂate large-scale replicated production deployments (stron g evidence) with
single-study journal papers (moderate evidence), and would exclud e important work
published as conference proceedings. Second, the four levels corr espond to a decreasing
but not binary hierarchy: L1 (randomized or replicated), L2 (peer-rev iewed empiri-
cal with replication), L3 (preprints with empirical validation on real data), and L4
(conceptual/white-paper). This hierarchy allows us to apply hedgin g rules propor-
tional to evidential strength rather than a simple threshold. Third , evidence-level
disagreements between the two raters were rare (3% of calibration recor ds diﬀered by
more than one level) and were resolved through structured discussion ; the ﬁnal evi-
dence level assigned to each study is reported in Supplementary Tab le S1 and can be
independently veriﬁed. As shown in Table 3, this grading distingui shes randomized
or replicated evidence from preprint-only and conceptual evidence , and we use it to
govern the strength of claims made throughout the review.
T able 3 Four-level evidence grading applied to the 108 included stu dies. Claim-strength rules are
applied consistently across Sections 3–6: central theoret ical conclusions rest only on Level 1–2
evidence; Level 3–4 evidence supports emerging directions but is explicitly hedged.
Level Deﬁnition Examples in this review
L1 Peer-reviewed ﬁeld experiments /
large-scale RCT benchmarks
Gordon et al. (2019, 2023); John-
son et al. (2017a); Chen and Au
(2022)
L2 Peer-reviewed empirical studies
or production deployments with
replication
Wager and Athey (2018); Cher-
nozhukov et al. (2018); Brodersen
et al. (2015); Aridor et al. (2023);
Lin and Misra (2022)
L3 Preprints (arXiv/SSRN) with
empirical validation against real
data
Gordon et al. (2024); Bencina
et al. (2025); Mulc et al. (2025);
Tirumala (2025); Filippou et al.
(2025)
L4 Conceptual, prototype, or white-
paper work without peer review
Google Think (2022); Sun et al.
(2017); Zhang et al. (2024); W3C
(2025)
Claim-strength rule: RQ-level conclusions (Section 9) are s upported by at least one Level 1 or Level 2 study
plus corroborating Level 3 evidence. Preprint-only claims are always hedged (“suggests”/“reports”/“to our
knowledge”); no theoretical or normative claim in Sections 3–7 rests solely on Level 4 evidence.
10

2.7 Terminological Conventions: Prediction, Causal
Estimation, Causal Discovery, and Experimental
Identiﬁcation
Throughout this review, we use four terms that are often conﬂated in prac tice but
correspond to distinct epistemic claims. Readers should note thes e distinctions when
evaluating the evidence reported in Sections 3–6.
• Prediction refers to forecasting an outcome (e.g., conversion probability) given
observed features. Predictive accuracy is measured by metrics su ch as AUC, MAPE,
and R2. A model can achieve high predictive accuracy while making no causal c laim:
a high-AUC model may predict conversions well because most conversi ons occur
among users who would have converted anyway (baseline demand), not be cause
advertising caused them.
• Causal estimation refers to estimating the average or conditional treatment eﬀect
of an intervention (e.g., advertising exposure on conversions) usin g a method that
controls for confounding under stated assumptions. Methods such as DM L (Cher-
nozhukov et al. 2018) and causal forests (Wager and Athey 2018; Athey et al. 2019)
achieve this from observational data under the unconfoundedness/over lap assump-
tions; they do not require randomization but make identifying assump tions that are
not directly testable.
• Causal discovery refers to inferring the structure of a causal graph—which vari-
ables causally inﬂuence which—from observational data. Methods such as P CMCI
(CDA, Section 3.4) and Granger-causality-based DAG learning (CausalMMM,
Section 4.3) belong to this category. Causal discovery results are assumption-
dependent: they rely on faithfulness, temporal ordering, and the absence of hidd en
confounders, and should not be interpreted as equivalent to identi ﬁcation from
randomized variation.
• Experimental identiﬁcation refers to causal eﬀect identiﬁcation achieved by
randomized assignment of units to treatment conditions. Field exper iments (geo-
experiments, ghost ads, A/B tests) provide experimental identiﬁc ation; their
estimates serve as the ground truth against which other methods are ben chmarked
in this review.
These four epistemic categories are not mutually exclusive—a method can combine
predictive modeling with causal estimation—but the distinctions matter for interpret-
ing performance claims. We apply these labels consistently throughou t the review (see
also the Causal credibility column in Table 4).
2.8 Preprint Handling Protocol
The inclusion of preprints reﬂects a deliberate methodological choi ce: in machine
learning and privacy engineering, cutting-edge work routinely appears on arXiv 12–24
months before formal publication, and excluding preprints would int roduce system-
atic recency bias that disproportionately excludes practitioner-le d research from major
technology platforms. We applied three safeguards to preprint eviden ce: (a) every
preprint was checked against Google Scholar and venue proceedings at rev ision time to
11

detect subsequent peer-reviewed publication; (b) each prepri nt was assigned Evidence
Level 3 or 4 (Section 2.6) and its claims were hedged accordingly; (c) no ce ntral theo-
retical conclusion in Sections 3–6 rests solely on preprint evidence . Where a preprint’s
claim contradicts a peer-reviewed ﬁnding, we surface the disagreem ent explicitly rather
than averaging across them.
3 AI for Attribution Modeling
Attribution modeling assigns credit for conversions to marketing t ouchpoints along
the customer journey. This section traces the evolution from rule-b ased heuristics to
AI-driven approaches.
3.1 From Rules to Data-Driven Attribution
Traditional attribution relies on heuristic rules—last-touch, ﬁrst -touch, or linear
allocation—that ignore the sequential and interactive nature of customer journeys
(Dalessandro et al. 2012). The ﬁrst generation of data-driven approaches int roduced
Markov chain models (Mehta and Singhal 2020) and Shapley value methods. Zh ao
et al. (2018) demonstrated that Shapley value computation could be simpliﬁe d from
17 hours to approximately 2 minutes while preserving identical att ribution outputs,
making game-theoretic attribution computationally feasible at scale.
3.2 Deep Learning Sequence Models
The application of deep learning to multi-touch attribution (MTA) rep resents a
qualitative shift in modeling capability. Three architectural fam ilies have emerged.
Recurrent neural networks. Du et al. (2019) deployed an RNN-based MTA
system at JD.com, processing attribution for approximately 300 milli on users, 160,000
brands, and 80 billion ad impressions within 15-day windows. Their tw o-stage
approach—ﬁrst ﬁtting an RNN-based user response model, then applying S hapley
value credit allocation—demonstrates that deep learning attribution c an operate at
industrial scale while maintaining axiomatic fairness properties. K umar et al. (2020)
extended this with CAMTA, a causal attention mechanism that addresses selection
bias by using pre-conversion user actions to predict per-channel at tribution.
Phased-LSTM with interpretability. Yang et al. (2020) introduced DeepMTA,
combining phased-LSTM networks with Shapley value-based attributi on to achieve
91% conversion prediction accuracy and interpretability. The phased- LSTM architec-
ture divides time into learnable phases, capturing both short-ter m triggering eﬀects
and long-term brand-building eﬀects. The integration of additive feat ure attribution
aligned with Shapley values bridges black-box prediction and interp retable attribution.
Subsequent methodological reﬁnements further improve the Shapl ey-style attribution
backbone that models like DeepMTA rely on: Chen et al. (2024b) develop Sh apley
Integrated Gradients (SIG), aligning Integrated-Gradients baselin es with Aumann–
Shapley coalitions via proportional sampling to yield more consistent f eature-level
attributions—a reﬁnement directly applicable to Shapley-based cr edit allocation in
MTA pipelines.
12

Continuous-time models. Zhan et al. (2024) applied Neural Ordinary Dif-
ferential Equations (Neural ODE) to handle irregular time intervals i n customer
journeys. On the Criteo dataset (16 million impressions, 45,000 convers ions), ODE-
LSTM achieved AUC of 0.983 and PRAUC of 0.929, outperforming standard LSTM
(AUC 0.973) and Transformer (AUC 0.981) baselines. However, on a marketing
sign-up dataset with highly irregular time gaps, attention-LSTM (AUC 0.971) ou tper-
formed ODE-LSTM (AUC 0.920), suggesting that continuous-time models are m ost
advantageous when inter-event intervals are moderately irregular.
3.3 Transformer-Based Uniﬁed Attribution
Transformer architectures have introduced signiﬁcant recent adv ances. Bencina et al.
(2025) developed LiDDA (LinkedIn Data-Driven Attribution), which use s transformer-
style attention to unify member-level touchpoint data with aggregate- level channel
signals. LiDDA’s architecture enables reconciliation between bottom- up data-driven
attribution and top-down media mix model constraints, achieving RO C-AUC exceed-
ing 0.97 for conversion prediction. Related transformer-based journey models report
strong ranking performance for conversion prediction relative to rec urrent baselines
(Lu and Kannan 2024).
3.4 Causal Attribution Without User-Level Data
Perhaps the most consequential development for the privacy-constrai ned future is
attribution that operates without user-level data. Filippou et al. (2025) p roposed
Causal-Driven Attribution (CDA), applying PCMCI temporal causal dis covery and
structural causal models to aggregated impression-level data. CDA achie ves an aver-
age relative RMSE of 9.50% when the true causal graph is known and 24.23% when
using the estimated graph—demonstrating that meaningful attribution i s recoverable
from aggregate data alone. This approach is natively privacy-compliant, req uiring
no user identiﬁers or individual-level tracking, and represents a paradigm shift from
preserving user-level accuracy under privacy constraints to rec overing channel-level
causal eﬀects from aggregate time series. An important caveat: causal disco very from
observational aggregate data is assumption-dependent—typically requiri ng temporal
ordering, the faithfulness assumption, and the absence of hidden conf ounders—and
should not be interpreted as equivalent to identiﬁcation from randomi zed variation.
CDA’s causal claims are therefore best read as “causal-under-assumptions ” and remain
complementary to, rather than substitutable for, experimental valid ation.
3.5 Comparative Assessment
Table 4 illustrates the deep learning attribution approaches review ed and compares
their architecture, scale, predictive performance, and causal cre dibility. Three critical
challenges persist across all architectures.
First, causal identiﬁability : without experimental variation, even the most
sophisticated neural models cannot distinguish causal eﬀects from cor relation. As Gor-
don et al. (2023) demonstrated, access to 5,000+ user features and ﬂexible ML m odels
13

still produced median attribution errors of 62–115%. This accuracy–validit y decou-
pling is domain-agnostic: Li et al. (2026b) document evaluation failures in AI -probe
settings where predictive AUC exceeds 0.998 yet valid ground-truth i dentiﬁcation fails,
reinforcing that discriminative power is a necessary but not suﬃc ient condition for
causal identiﬁcation.
Second, interpretability: while DeepMTA integrates Shapley values and LiDDA
uses attention weights, most deep attribution models remain opaque in their credit
allocation.
Third, distributional sensitivity : neural attribution models trained on histori-
cal data may not generalize to novel campaign strategies—a concern reinfor ced by the
CATE estimation benchmark ﬁnding that 62% of causal eﬀect estimates hav e higher
MSE than a zero-eﬀect predictor (Curth et al. 2025). A related but disti nct reliability
risk concerns the post-hoc attribution tools (SHAP, Integrated Gradie nts, LIME) rou-
tinely layered on top of deep attribution models for interpretabili ty: Shi et al. (2024b)
design a controlled benchmark and show that these methods fail to sep arate predictive
from irrelevant features in low signal-to-noise regimes, which is pr ecisely the regime
that characterizes advertising data (Section 5.1.1).
14

T able 4 Comparative summary of deep learning attribution models
Model Architecture Dataset scale Best
AUC
Causal
credibility
Du et al.
RNN
RNN + Shapley 300M users, 80B
impressions
n/r Causal-informed
CAMTA RNN +
Attention
Production (undisclosed) n/r Causal-informed
DeepMTA Phased-LSTM Real campaign data 0.91 Predictive only
ODE-
LSTM
Neural ODE 16M impressions 0.983 Predictive only
LiDDA Transformer LinkedIn production 0.97 Causal-informed
Lu &
Kannan
Transformer Large-scale journey data 0.921 Predictive only
CDA PCMCI + SCM Aggregate impressions n/r ∗ Assumption-
dependent
“n/r” = not reported in a comparable AUC form (e.g., paper rep orts relative RMSE rather than
ROC-AUC). ∗CDA reports relative RMSE of 9.5% (true causal graph) and 24. 2% (estimated graph).
Causal credibility is the authors’ qualitative classiﬁcation of how a method ha ndles identiﬁcation:
“Assumption-dependent” = causal claims follow from struct ural assumptions (e.g., temporal ordering,
faithfulness, no hidden confounding) but are not equivalen t to randomized identiﬁcation; “Causal-
informed” = model incorporates causal mechanisms (e.g., at tention to pre-conversion actions, top-down
MMM constraints) without claiming identiﬁcation; “Predic tive only” = architecture is optimized for
predictive accuracy with no explicit causal structure. Cau sal discovery from aggregate observational data
remains assumption-dependent and should not be interprete d as equivalent to randomized identiﬁcation.
Remark 1 (Practitioner Takeaways: AI Attribution Models)
• AUC > 0.97 does not mean your attribution is accurate. Gordon et al.
(2023) show that models with access to 5,000+ user features still produce median
attribution errors of 62–115% relative to RCT benchmarks. High predictive ac curacy
and causal validity are empirically decoupled; treat them as separate di agnostic
questions.
• Invest in one ghost-ad or holdout experiment before upgrading model
architecture. The marginal causal value of a single well-designed calibration
experiment exceeds the marginal trustworthiness gain from switchi ng attribution
architectures for most organizations (Gordon et al. 2024).
• Shapley values and attention weights are interpretability aids, not cau sal
proofs. Post-hoc attribution methods systematically fail to separate signal f rom
noise in low-SNR regimes (Shi et al. 2024b)—the regime that characterizes m ost
advertising data. Use them for stakeholder communication, not for budget allocation
without experimental anchoring.
• Privacy-constrained? Consider aggregate causal attribution (CDA). If
user-level data is unavailable or legally restricted, Filippou et al . (2025) demonstrate
that meaningful channel-level attribution is recoverable from aggregate time-series
data alone, at 9.5–24.2% RMSE relative to true causal eﬀects.
15

4 AI for Media Mix Modeling
Media mix modeling (MMM) estimates the aggregate relationship betwe en marketing
investments and business outcomes using time-series data. Unlike attribution, MMM
does not require user-level data, making it increasingly relevant i n the privacy era.
4.1 From Classical to Bayesian MMM
Traditional MMM employs linear regression with adstock and saturation t ransforma-
tions to model how marketing spend translates to sales (Hanssens et al . 2001; Leeﬂang
et al. 2009). The ﬁrst major advancement was geo-level Bayesian hierarchic al MMM
(Sun et al. 2017), which demonstrated that sub-national data variability pr ovides
tighter credible intervals. Zhang et al. (2023) extended this framewor k to incorporate
reach and frequency data, separating exposure intensity from raw imp ression volume.
The practical importance of these advances is reﬂected in open-source implementa-
tions. Google’s Meridian provides hierarchical geo-level modeling with NUTS MCMC
sampling, while Meta’s Robyn oﬀers gradient-based optimization with ri dge regression.
PyMC-Marketing has demonstrated 2–20 × faster sampling and 40% lower channel
contribution error compared to Meridian in benchmark tests. The Orb it KTR model
(Ng et al. 2021) introduced kernel temporal regression with time-varyin g coeﬃcients,
addressing the unrealistic assumption of constant media eﬀects (Pau wels et al. 2004).
A critical methodological advance is the reparameterization of MMM to inc lude
Return on Ad Spend (ROAS) as an explicit model parameter (Zhang et al.
2024), enabling straightforward Bayesian calibration with experimental e vidence.
This approach forms the core of the “triangulation” methodology—combining geo-
experiments, Bayesian priors, and MMM posterior inference—that is widely used in
industry practice for MMM validation (Google Think 2022).
4.2 Neural Media Mix Models
Deep learning MMM frameworks represent a paradigm shift from manually speciﬁed
response functions to learned representations.
GRU-based causal MMM. Tirumala (2025) developed DeepCausalMMM, an
open-source framework that replaces manual adstock and saturation speci ﬁcation with
GRU-learned temporal dynamics and integrates continuous optimization-b ased DAG
structure learning. Using Hill equation saturation curves (shape parame ter a ≥ 2.0)
and multi-region modeling, DeepCausalMMM reports 91.8% holdout R2 with a 3.0%
train–test gap on the authors’ evaluation setup, scoring higher than Robyn, Meridian,
and PyMC-Marketing across four reported evaluation dimensions; these results are
drawn from a single preprint benchmark and should be read as promising but not yet
externally replicated.
T ransformer-based embedding MMM. Mulc et al. (2025) introduced NNN
(Next-Generation Neural Networks), which encodes ad creative content , search key-
word semantics, and other rich signals as high-dimensional embeddings. This enables
the model to distinguish between diﬀerent types of spending wi thin the same channel
and to model indirect eﬀects explicitly. In controlled simulati ons, NNN achieved test
MAPE of approximately 1% versus 3% for traditional scalar MMM on low-variance
16

data, and 3.2% versus 15% on high-variance data. On real-world-style data spli ts,
NNN achieved test R2 of 0.92 compared to severely degraded performance for scalar
MMM (test MAPE of 189%).
These results suggest that neural MMM can capture signal that traditional
approaches miss. However, predictive improvement does not automati cally confer
causal validity.
4.3 Causal Structure Discovery in MMM
A distinctive contribution of AI to MMM is the automation of causal struct ure discov-
ery. Gong et al. (2024) developed CausalMMM, integrating Granger causality t esting
with variational inference to automatically discover shop-speciﬁc c ausal structures.
Their framework achieved 5.7–7.1% AUROC improvement in causal structur e recov-
ery and produced graphs aligning with expert domain knowledge. Varambal ly et al.
(2024) proposed a broader framework for discovering mixtures of structur al causal
models from heterogeneous time series.
4.4 MMM Calibration with Experimental Evidence
The most important development in MMM methodology is the recognition th at model
accuracy requires external calibration. The Google/Omnicom Uniﬁed Mark eting Mea-
surement framework demonstrated a 40% increase in expected uplift v ersus MTA
alone when MMM, experiments, and attribution were integrated at the d ata level
(Google Think 2022). The reconciliation between attribution and MMM has be en oper-
ationalized in production systems: LiDDA implements top-down MMM constraints on
bottom-up data-driven attribution at LinkedIn (Bencina et al. 2025).
4.5 Comparative Assessment
Neural MMM frameworks demonstrate clear advantages in predictive accurac y and
expressiveness. However, several concerns temper enthusiasm. First, the tension
between automated causal learning and domain knowledge injection remain s unre-
solved. Data-driven DAG learning (Tirumala 2025; Gong et al. 2024) can discove r
spurious channel associations when unmeasured confounders—such as con current
brand campaigns or macroeconomic cycles—induce correlations that a causal gr aph
falsely interprets as direct eﬀects. At the other extreme, full y expert-speciﬁed
causal graphs may miss genuine cross-channel dynamics that only observat ional data
can reveal. Neither automated discovery nor pure domain speciﬁcation dom inates:
CausalMMM’s variational inference approach (Gong et al. 2024) attempts a midd le
ground by incorporating prior beliefs about causal direction while allow ing data-driven
reﬁnement, but this balance requires careful prior elicitation th at may not be feasi-
ble in standard commercial deployments. Resolving this tension—pot entially through
constrained optimization that encodes marketing domain priors as soft con straints
rather than hard graph structure—represents an important direction for future MMM
research. Second, data requirements remain ambiguous: while NNN’s L1 re gulariza-
tion enables training on limited data, the minimum data volumes requi red for stable
17

causal inference from neural MMM have not been systematically charact erized, leav-
ing practitioners without clear guidelines for deployment decisi ons (Mulc et al. 2025).
Third, the causal credibility of neural MMM ultimately depends on e xperimental cal-
ibration, creating a potential circularity: the models most in need of calibration are
those whose complexity makes calibration most challenging.
Remark 2 (Practitioner Takeaways: AI Media Mix Modeling)
• Neural MMM improves ﬁt but does not eliminate the need for cali-
bration. DeepCausalMMM reports 91.8% holdout R2 (Tirumala 2025) and NNN
achieves test MAPE of 3.2% versus 15% for traditional MMM (Mulc et al. 2025)—
but predictive superiority does not confer causal validity. Exter nal geo-experiment
calibration remains necessary regardless of model complexity.
• Match model complexity to your data history . GRU-based neural MMM
requires suﬃcient time-series length to learn temporal dynamics reliably. For orga-
nizations with fewer than two years of weekly cross-channel data, simp ler Bayesian
hierarchical MMM (e.g., Meridian, Robyn, PyMC-Marketing) is likel y more reliable
(Sun et al. 2017; Zhang et al. 2023).
• Automated causal graph learning can introduce spurious channel asso-
ciations. Unmeasured confounders—concurrent brand campaigns, macroeconomic
cycles—can generate correlations that a data-driven DAG misinterpret s as direct
channel eﬀects (Gong et al. 2024). Treat discovered causal structures as hypotheses
to validate, not as ground truth.
• T riangulation is the highest-ROI investment. The Google/Omnicom uniﬁed
measurement framework reports a 40% increase in expected uplift whe n MMM,
experiments, and attribution are integrated at the data level (Google T hink 2022).
No single modeling upgrade produces comparable returns.
5 Causal Calibration and Validation
The preceding sections established that AI-driven models impro ve predictive accuracy
but do not inherently guarantee causal validity. This section examine s the evidence
for measurement bias, experimental calibration methods, and AI-enhan ced causal
estimation.
5.1 Evidence of Systematic Measurement Bias
The case for causal calibration rests on extensive evidence that non-ex perimental
advertising measurement is systematically biased. Lewis and Rao (2015) an alyzed 25
large ﬁeld experiments representing $2.8 million in digital advertising expenditure and
found that median ROI conﬁdence intervals exceed 100 percentage points wide, estab-
lishing the fundamental statistical diﬃculty of measuring adverti sing returns. Gordon
et al. (2019) demonstrated through 15 Facebook experiments that observational meth-
ods fail to replicate experimental results. Their subsequent s tudy (Gordon et al. 2023)
extended this to 663 RCTs, showing that DML produced median errors of 83%, 58%,
and 24% at upper, mid, and lower funnel respectively.
18

The mechanism underlying this bias is illuminated by Gui et al. (2022) , who dis-
covered that auction throttling—the randomized budget pacing used by ad vertising
platforms—creates natural quasi-experimental variation. Their instr umental variable
estimation yielded a conversion lift of approximately 110%, compared to 600% from
naive observational estimators, suggesting that platform attribution ove rstates eﬀec-
tiveness by roughly 5 ×. Ye and Xue (2026) extend this critique to the real-time
bidding (RTB) setting and document how selection on bid-eligibl e impressions, audi-
ence targeting, and platform-side attribution windows jointly compoun d measurement
bias, arguing that conventional RTB attribution metrics conﬂate select ion eﬀects with
incremental advertising lift in ways that mirror the experiment al–observational gap
reported by Gordon et al. (2023).
These bias estimates presuppose that the underlying engagement sign al is clean.
Upstream data-quality ﬁlters—graph-based bot detection (Zhao et al. 2026) and
temporal sentiment-aggregation anomaly detection (Qi et al. 2026)—can remove
adversarial or coordinated traﬃc before attribution models consume the signal, and
should be viewed as complements to, not substitutes for, causal calibr ation.
5.1.1 The Advertising Eﬀectiveness Paradox
Meta-analytic evidence reveals a striking paradox that deepens the case for rigorous
measurement. Shapiro et al. (2022) conducted a meta-analysis of 538 advertis ing elas-
ticities with improved bias corrections, reducing overall eﬀec tiveness estimates more
than sixfold compared to prior meta-analyses. They obtained an average shor t-term
advertising elasticity of 0.0008 and a long-term elasticity of 0.03. 1 To put these mag-
nitudes in perspective: a short-term elasticity of 0.0008 implies t hat a 10% increase in
advertising spending yields only a 0.008% increase in sales—a vanishin gly small eﬀect
that is nonetheless positive on average and consistent with experime ntal evidence.
This paradox has profound implications. If true advertising eﬀects ar e this small,
even modest measurement errors easily swamp the real signal: the med ian errors of
62–115% documented by Gordon et al. (2023) are orders of magnitude larger than the
eﬀects they seek to measure. A model can therefore predict conver sions well (because
most conversions are driven by baseline demand and selection eﬀects) while system-
atically misestimating the incremental contribution of advertisin g. The ChaosMining
benchmark (Shi et al. 2024b) conﬁrms this as a structural ML limit rather than a
marketing-speciﬁc artifact, with widely used post-hoc attributi on methods failing to
separate signal from noise once SNR drops. Johnson et al. (2017b) likewise docu ment
modest median lifts (17% for site visits, 8% for conversions) across 432 Go ogle Display
Network ﬁeld experiments, reinforcing the need for measurement s ystems capable of
detecting small eﬀects with precision.
5.2 Experimental Calibration Methods
Several methodological innovations have reduced the cost and improve d the reliability
of experimental calibration.
1Advertising elasticity here is deﬁned as the percentage cha nge in sales resulting from a 1% change in
advertising spend. An elasticity of 0.0008 implies that dou bling advertising spend increases sales by only
0.08%.
19

Geographic experiments. Geo-experiments allocate geographic regions to treat-
ment and control conditions. Chen and Au (2022) developed the Trimmed Match
estimator, providing robust, distribution-free inference wit h data-driven pair selec-
tion for the small sample sizes (50–200 units) typical of market-level data. Brodersen
et al. (2015) introduced Bayesian structural time-series models (C ausalImpact) for
constructing synthetic counterfactuals. Abadie et al. (2010) establish ed the synthetic
control method for constructing optimal weighted combinations of untre ated units.
Ad-level experiments. Johnson et al. (2017a) introduced Ghost Ads, which
reduce experimentation costs by an order of magnitude compared to PSA te sts by
recording what ad a user would have seen without showing it. The “Predicted Ghost
Ad” variant processes over 100 million ghost ad decisions daily. Fiez et al . (2024)
addressed non-stationarity as the core failure mode of adaptive experim ental design in
production environments, proposing a framework combining counterf actual inference,
opportunity cost minimization, and time robustness.
Sequential testing. Bojinov et al. (2023) developed design-based conﬁdence
sequences enabling valid “peeking” at experimental results withou t inﬂating Type I
error, potentially allowing experiments designed for 30,000 users to r each valid
conclusions with fewer than 100 observations.
An important caveat is that experiments themselves are not immune to bias.
Waisman et al. (2025) demonstrated that concurrent experimentation by mul tiple
advertisers violates SUTV A (the Stable Unit Treatment Value Assumpti on, which
requires that one unit’s treatment does not aﬀect another’s outcome), with advertisers
misestimating lift by 2 × or more when competitive interference is ignored.
5.3 AI-Enhanced Causal Estimation
AI methods have advanced causal estimation toward heterogeneous treatme nt eﬀect
(HTE) estimation, enabling personalized measurement.
F oundational methods. Chernozhukov et al. (2018) established DML, combin-
ing ﬂexible ML models for nuisance parameter estimation with Neyman- orthogonal
moment conditions ensuring
√
N -consistent treatment eﬀect estimation. Wager and
Athey (2018) developed causal forests for nonparametric HTE estimation with valid
pointwise conﬁdence intervals. Athey et al. (2019) generalized this to Generalized
Random Forests (GRF). K¨ unzel et al. (2019) introduced the S-, T-, and X- learner
metalearner framework, demonstrating that no single approach dominates ac ross all
settings. Interpretable matching approaches complement these regr ession-based esti-
mators: the DAME and FLAME algorithms (Gupta et al. 2025) provide fast large-scal e
almost-exact matching that preserves full interpretability of tre atment-control unit
selection, oﬀering an auditable alternative to propensity-score met hods when practi-
tioners require human-readable justiﬁcation for matched geo-units or u ser cohorts in
incrementality studies.
Industrial-scale HTE. The Snap HTE framework (Shi et al. 2024a) trained con-
ditional average treatment eﬀect (CATE) models on hundreds of milli ons of Snapchat
users using cross-experiment meta-learning. Rather than estimati ng eﬀects within
20

a single experiment, the framework pools information across experime nts to iden-
tify latent inﬂuenceability scores. An online A/B test showed approx imately 6 ×
improvement in key business metrics versus non-targeted allocat ion.
Predictive incrementality . Gordon et al. (2024) developed PIE (Predictive
Incrementality by Experimentation), using a subset of RCTs to tr ain random forest
models predicting incremental conversions per dollar (ICPD). Th e best PIE model
achieves prediction errors of 42–62% of mean experimental ICPD across funne l stages,
compared to over 2,904% for DML and over 491% for SPSM. PIE disagrees with
RCT-based decisions in only 6–13% of cases.
Generative AI for causal inference. Liu et al. (2026b) introduced DICE-DML,
using deepfake-generated image pairs to isolate visual attribute treat ment eﬀects.
Applied to 232,089 Instagram posts, DICE-DML achieved RMSE reductions of 73–
97% in simulations and produced a causal estimate for skin tone eﬀects su bstantially
smaller than the biased standard DML estimate—a novel “AI for AI trustwort hiness”
approach with fairness implications.
Robust evaluation under imperfect labels. Large-scale conversion labels are
increasingly constructed from heterogeneous post-view signals or LLM-ju dged out-
comes of varying reliability (Li et al. 2025); Feng et al. (2026) develop statist ical
estimators that remain valid under imperfect judges, a tool directl y applicable to
advertising measurement where label noise can bias downstream causal comparisons.
Retrieval-augmented experiment search. A complementary scaling challenge
for PIE-style calibration is eﬃcient retrieval over large internal r epositories of prior
experiments and analyst notes: when calibration is extended from a sam pled subset of
RCTs to uncalibrated campaigns (Gordon et al. 2024), the practical bottlenec k shifts
to surfacing the most relevant historical evidence for a given new cam paign. Recent
work on retrieval-augmented generation outside marketing shows that add ing neural
reranking on top of dense retrieval substantially improves precisi on in document-
dense factual QA (Cheng et al. 2026b); both that setting and experiment- repository
search share the same challenge of locating a relevant ﬁnding buried i n a speciﬁc sub-
section of a long structured report, making neural reranking direct ly applicable to
analyst-facing experiment-search interfaces that support causal cal ibration at scale;
ensuring that retrieved evidence is not merely topically relevan t but appropriately war-
ranted with respect to the causal claim being supported represent s a complementary
design constraint for production retrieval pipelines (Qian et al. 2026). When LLMs are
deployed as tool-using agents within experiment-search or causal-c alibration pipelines,
reliable tool use further requires learning not merely when to in voke retrieval but
which speciﬁc retrieval pattern to apply given the analytical contex t (Xu et al. 2026a);
structured intermediate supervision over tool-calling steps ( Jiang and Ferraro 2026)
provides a complementary training approach that stabilizes multi-s tep tool chains,
with direct applicability to PIE-style calibration workﬂows wher e correctly sequenc-
ing retrieval, estimation, and uncertainty-quantiﬁcation steps is necessary for valid
incremental-eﬀect inference.
21

5.4 Comparative Assessment
AI-enhanced causal estimation oﬀers substantial improvements, but t he CATE bench-
mark (Curth et al. 2025) provides sobering evidence: 62% of CATE estimate s have
higher MSE than a zero-eﬀect predictor, while orthogonality-based mod els outperform
alternatives only 30% of the time. Uplift modeling advances—including M3TN (Zhao
et al. 2024) for direct uplift reparameterization and IDUM (Sun et al. 2025) for out -
of-distribution generalization—address complementary challenges but do not resolve
the fundamental need for experimental ground truth.
Remark 3 (Practitioner Takeaways: Causal Calibration and Experimenta l Design)
• Y our platform-reported ROAS is likely overstated by 2–5 ×. Gordon et al.
(2019, 2023) and Gui et al. (2022) converge on evidence that observational attribu-
tion systematically inﬂates eﬀectiveness. Treat platform-reporte d metrics as upper
bounds, not point estimates, until calibrated against an experiment.
• Geo-experiments are the most accessible calibration tool for mid-siz e
advertisers. The Trimmed Match estimator (Chen and Au 2022) provides robust
inference with as few as 50–200 geographic units. One well-designed annual geo-
experiment per major channel is suﬃcient to anchor your MMM.
• PIE (Predictive Incrementality by Experimentation) scales cali bration
without running experiments on every campaign. Gordon et al. (2024)
demonstrate that a subset of RCTs can train models that extend calibrat ion
to uncalibrated campaigns, with decision agreement rates of 87–94% versus fu ll
experimental measurement.
• SUTV A violations are real. When multiple advertisers run concurrent exper-
iments, competitive interference inﬂates lift estimates by 2 × or more (Waisman
et al. 2025). If your campaigns operate in competitive categories, account for th is
in experiment design and interpretation.
6 Privacy-Preserving Measurement
6.1 The Privacy Landscape
The privacy transformation of digital advertising is multifaceted. Gol dfarb and Tucker
(2011) documented early eﬀects of privacy regulation on ad performance. Arid or et al.
(2023) found that GDPR opt-in caused a 12.5% drop in observable consumers but
created a privacy externality: remaining consumers became more trac kable. Apple’s
ATT framework produced 37% reductions in Meta advertising click-t hrough rates
(Aridor et al. 2024), disproportionately aﬀecting smaller ﬁrms and raising c ompetitive
equity concerns.
6.2 Diﬀerential Privacy Approaches
Diﬀerential privacy (DP) provides mathematically rigorous privacy gu arantees by
ensuring that computation outputs change only negligibly when a single i ndividual’s
data is modiﬁed.
22

Ghazi et al. (2024) provided the ﬁrst complete characterization of “operation ally
valid conﬁgurations” for DP attribution, identifying four design dime nsions: attribu-
tion rule, adjacency deﬁnition, contribution bounding scope, and enf orcement point.
Their analysis reveals that certain common conﬁgurations are invalid—a foun dational
result for privacy-preserving attribution system design.
Xiao et al. (2025) developed AdsBPC, the ﬁrst user-level DP scheme for st ream-
ing ad measurement. Traditional DP mechanisms deplete the privacy b udget rapidly
in streaming settings. AdsBPC introduces adaptive noise scaling and bounded per-
day contribution constraints, achieving 33–95% accuracy improvement ov er existing
streaming DP methods. On real campaign data spanning 31 days, AdsBPC mai n-
tained measurement accuracy within acceptable ranges at moderate priv acy budgets
(ρ ∈ [0.25, 8]).
The W3C Privacy-Preserving Attribution speciﬁcation (W3C 2025) and the IPA
(Interoperable Private Attribution) protocol (Kreuter et al. 2023) rep resent browser-
level and cross-platform implementations of these principles.
6.3 Federated Learning and Clean Rooms
Data clean rooms and federated learning enable collaborative model train ing without
raw data exchange. Li et al. (2024) describe Pinterest’s clean-room frame work, report-
ing that batch-level aggregated gradients combined with LoRA adapter ﬁne- tuning
recover approximately 95% of the ROC-AUC gain of full ﬁne-tuning while updating
only about 1% of model parameters, and that a de-biasing layer under label diﬀeren-
tial privacy at ε = 5 limits ROC-AUC loss to 0.2–0.5% in their reported production
deployment. These ﬁgures reﬂect Pinterest’s speciﬁc clean-r oom conﬁguration and
model mix, and should not be read as a guarantee that federated learning wi ll retain
this much accuracy in other clean-room stacks or industries.
Du et al. (2025) developed PrivacyGo, combining oblivious pseudorandom fun c-
tions with diﬀerential privacy for waterfall-style multi-identi ﬁer matching, processing
approximately 2 million records in 2 minutes while preventing cr oss-identiﬁer linkage
attacks.
Beyond identiﬁer matching, clean rooms increasingly host analytics wor kﬂows that
retrieve and aggregate information across distributed campaign documentat ion, attri-
bution reports, and partner-side data. Within these workﬂows, the c hoice of retrieval
architecture itself becomes a measurement-design decision: chu nk-level retrieval is pre-
cise but brittle to document boundary eﬀects, while document- level routing is more
robust but less speciﬁc. Cheng et al. (2026a) characterize this robustn ess–precision
trade-oﬀ in adjacent information-retrieval contexts and propose hybrid document-
routed retrieval as a way to combine the two regimes; the same trade-oﬀ is directly
applicable when clean-room analytics pipelines must balance complet eness against
precision under federated access constraints; compliance failures can additionally
arise when retrieved partner-side data conﬂicts with the retrie val model’s contex-
tual expectations (Chen et al. 2026), a risk present whenever clean-ro om pipelines
aggregate across sources with inconsistent reporting conventions. Trans parent conﬂict-
resolution mechanisms (Ye et al. 2026) oﬀer a constructive counterpart: r ather than
silently overriding conﬂicting context, they surface competin g evidence pathways in
23

an auditable form that measurement teams can inspect; at the data-distri bution
level, confusion-resistant federated learning with diﬀusion-bas ed harmonization on
non-IID data (Chen et al. 2024a) directly addresses the structural hete rogeneity that
arises when partner-side reporting conventions diﬀer systematic ally across clean-room
participants. Prototype-aligned federated soft-prompts (Xiao and Hou 2026) oﬀe r a
complementary continual-adaptation mechanism: by aligning local model updates via
shared prototypes and soft-prompt conditioning without raw data exchan ge, they
enable ongoing model recalibration across advertiser–publisher clean- room stacks as
campaign objectives evolve—a federated personalization pathway direct ly applicable
to marketing measurement contexts where attribution models must adapt continuously
to shifting media environments.
6.4 Privacy-Native Attribution
The most radical response to privacy constraints is measurement that op erates with-
out user-level data by construction. The CDA approach of Filippou et al. (2025)
(Section 3.4) exempliﬁes this philosophy. Lin and Misra (2022) demonstrat ed that
privacy-induced identity fragmentation inﬂates channel eﬀects by 40–91%. Berman
and Feit (2024) proposed latent stratiﬁcation as a variance reduction techni que
reducing ATE variance by 30–60% without requiring additional user-leve l data. A
data-generative extension of this philosophy replaces real user record s with synthe-
sized behavioral traces: Xu et al. (2026b) develop a two-stage coarse-to-ﬁne d iﬀusion
framework for synthesizing realistic human activity traces, provi ding a privacy-by-
construction alternative to aggregate-only measurement that preserves the statistical
structure of behavioral sequences while eliminating re-identi ﬁcation risk—a direction
particularly relevant when regulatory constraints prevent direct c ollection of granular
user-level data.
Right-to-be-forgotten (RTBF) obligations under GDPR/CCPA also introd uce a
downstream privacy challenge at the model-maintenance stage: Chen et al. (2024c)
show that naive machine unlearning is not bias-neutral—uneven data re moval can
distort the residual training set—and propose a counterfactual-augment ed procedure
that restores unbiased performance after deletion, an under-appreci ated trustwor-
thiness requirement for attribution and MMM systems that must honor deletion
requests. Multimodal analytics pipelines that route customer image s, video creatives,
or user-generated content through vision-language models face an additional pri-
vacy exposure: Wang et al. (2026d) systematically audit large VLMs and documen t
reproducible PII leakage pathways under social-engineering promp ts, demonstrating
that pseudonymized customer data can be re-identiﬁed through infer ence attacks—a
risk not addressed by standard text-only privacy mechanisms and one th at warrants
dedicated auditing protocols for multimodal marketing stacks.
6.5 Accuracy–Privacy Trade-Oﬀ Analysis
Table 5 illustrates the quantiﬁable trade-oﬀs reported for each privacy mechanism in its
representative published deployment. Three observations emer ge. First, DP accuracy
24

costs depend critically on the privacy budget ε: at moderate levels ( ε = 3–5), measure-
ment accuracy is often acceptable in the settings reported, but at str ict levels ( ε ≤ 1),
noise may render campaign-level estimates uninformative. Second, the very low accu-
racy loss (0.2–0.5%) reported for federated training with LoRA adapters is sp eciﬁc to
the Pinterest clean-room conﬁguration described by Li et al. (2024)—in wh ich label
DP is applied at ε = 5 on top of clean-room-mediated aggregate gradients—and should
not be read as a general claim about federated learning writ large. Third, t he ε param-
eter lacks clear calibration standards for advertising contexts—a gap req uiring both
technical research and regulatory guidance.
T able 5 Privacy-preserving measurement: accuracy–privacy trade -oﬀs
Mechanism Representative Accuracy loss Privacy
guarantee
Maturity
Diﬀerential privacy
(event)
Ghazi et al. 2–33% ε-DP Standard
Streaming DP AdsBPC 5–67% User-level DP Prototype
Federated + LoRA Pinterest CR 0.2–0.5% † Label DP, ε=5 Production
Cryptographic
(OPRF+DP)
PrivacyGo Minimal Crypto + DP Production
Aggregate causal CDA 9.5–24.2% By construction Research
Browser API W3C/IPA Variable ε-DP + MPC Draft
Accuracy Loss measured as increase in estimation error rela tive to non-private baselines within each
mechanism’s representative published deployment; cross- mechanism comparisons should therefore be
interpreted with caution. Maturity reﬂects deployment sta tus as of early 2026. †The 0.2–0.5% loss
reported for Federated + LoRA reﬂects the speciﬁc Pinterest clean-room conﬁguration in Li et al. (2024)
(batch-level aggregate gradients plus LoRA adapters under label DP at ε = 5) and does not generalize to
federated learning more broadly.
Remark 4 (Practitioner Takeaways: Privacy-Preserving Measurement)
• Diﬀerential privacy imposes a measurable accuracy cost: plan for it. At
moderate privacy budgets ( ε = 3–5), accuracy loss is typically 2–33% relative to
non-private baselines (Xiao et al. 2025). At strict budgets ( ε ≤ 1), campaign-level
estimates may become uninformative. Set ε based on acceptable accuracy loss, not
regulatory defaults, and re-validate measurement utility after depl oyment.
• F ederated clean rooms can preserve most measurement utility . Pinter-
est’s documented clean-room deployment retained approximately 95% of centralized
ROC-AUC under label diﬀerential privacy at ε = 5 (Li et al. 2024). This
is conﬁguration-speciﬁc—validate retention in your own stack before ass uming
comparability.
• Cookie deprecation and A TT are structural, not temporary . Aridor et al.
(2024) document a 37% reduction in Meta click-through rates attributable to
ATT. Design your measurement architecture around aggregate and privacy-n ative
methods now; retroﬁtting under regulatory pressure is costlier t han proactive
investment.
• Machine unlearning (R TBF compliance) is not bias-neutral. Deleting user
records under GDPR/CCPA Right-to-be-Forgotten requests can distort residual
25

training distributions (Chen et al. 2024c). Audit for bias after deleti on events, not
only at initial model training.
7 The Measure–Validate–Protect Framework
Our review reveals that advances in any single measurement domain are in suﬃ-
cient without integration across the full pipeline. We formalize thi s insight as the
Measure–Validate–Protect (MVP) framework, operationalizing the NIST tru stwor-
thiness dimensions for marketing measurement. As shown in Figure 2, the MVP
framework organizes measurement design around three coupled pillars.
Measure
Reliability
Deep learning
attribution; neural MMM
V alidate
Validity
Geo-experiments;
calibration; HTE/CATE
Protect
Privacy
DP; federated
learning; crypto
data / model outputs
calibration feedback (PIE-style); privacy constraints on data inputs
Ordering constraint: τ (M) ≤ min(τM , τ V , τ P ) —
pipeline trustworthiness is bounded by the weakest pillar.
F ailure mode example. Strong Measure ( τM = 0 .9) + weak Validate ( τV = 0 .3)
+ moderate Protect ( τP = 0 .7) ⇒ system trustworthiness is bounded by
0.3. Upgrading the model ( τM : 0.9 → 0.95) yields zero system gain; one geo-
experiment ( τV : 0.3 → 0.65) raises system trustworthiness to 0.65 (Example 1).
Fig. 2 The Measure–Validate–Protect (MVP) framework for trustwo rthy AI-driven marketing mea-
surement. Each pillar maps to a NIST trustworthiness dimens ion adapted in Section 1. Solid arrows
show the forward measurement pipeline; dashed arrows show t he two feedback paths through which
Validate and Protect shape the Measure pillar (calibration retraining and aggregate-data constraints).
The ordering constraint and the failure-mode callout illus trate why pipeline trustworthiness is deter-
mined by the weakest link rather than by the average across pi llars.
Measure. The ﬁrst pillar encompasses AI-driven measurement models—deep
learning attribution (Section 3) and neural MMM (Section 4)—that maximiz e pre-
dictive accuracy and expressiveness. AI models excel at capturing complex temporal
dynamics, cross-channel interactions, and creative quality variation s that traditional
approaches miss. The key trustworthiness requirement is reliability: models must
produce stable estimates across datasets and market conditions.
26

V alidate.The second pillar requires experimental calibration to establish c ausal
credibility (Section 5). Our review demonstrates that predictiv e accuracy and causal
validity are empirically decoupled—models achieving AUC > 0.97 can still produce
attribution errors exceeding 100%. Validation mechanisms include geo-e xperiments,
ghost ads, auction-based instruments, and cross-experiment meta-le arning. The key
trustworthiness requirement is validity: measurement must recover causal eﬀects, not
merely correlations. The advertising eﬀectiveness paradox (Sect ion 5.1.1) makes this
requirement especially acute: when true eﬀects are as small as elast icities of 0.0008,
even modest biases render measurement uninformative.
Protect. The third pillar ensures that measurement operates under privacy c on-
straints (Section 6). Privacy compliance is not merely a regulatory che ckbox but
a design constraint that shapes measurement architecture. The key t rustworthiness
requirement is privacy: systems must provide formal guarantees while preserving
suﬃcient accuracy for valid causal conclusions.
The MVP framework is distinct from existing constructs in two resp ects. Trian-
gulation and uniﬁed-measurement proposals (Google Think 2022) focus on combining
methods but do not formalize how trustworthiness degrades when one l eg is weak.
Responsible-AI and trustworthy-ML frameworks such as the NIST AI RMF ( National
Institute of Standards and Technology 2023) articulate trustworthiness di mensions
generically but do not specify diagnostic metrics or corrective action s for the market-
ing measurement pipeline. MVP closes both gaps by (a) pinning each tru stworthiness
dimension to a measurement-speciﬁc managerial question, diagnostic m etric, and min-
imum evidence requirement and (b) formalizing the weakest-pill ar ordering principle
below. Table 6 reports the diagnostic questions and evidence thresh olds, while Table 7
lists the corresponding failure modes and recommended actions.
Conceptual grounding and connections to existing frameworks. The MVP
framework is not presented as a replacement for existing trustworth iness frameworks
but as a marketing-speciﬁc instantiation that grounds abstract dimensi ons in the oper-
ational realities of measurement practice. The theoretical contribut ion is threefold.
First, the ordering constraint (τ (M) ≤ min(τM , τV , τP )) is a structural claim that
follows from the measurement pipeline’s sequential logic: a model whose outputs are
causally invalid produces misallocations regardless of how sophisti cated its architec-
ture is; a privacy-non-compliant system cannot legally operate regardle ss of its causal
validity. This is analogous to the weakest-link principle in system s reliability theory
(Barlow and Proschan 1975). Second, the framework explicitly decouples the measure-
ment, validation, and privacy pillars to enable independent diagnosis —a separation
that existing uniﬁed-measurement frameworks (which treat triangu lation as a single
activity) do not provide. Third, by connecting to the NIST AI RMF (Nat ional Institute
of Standards and Technology 2023), the MVP framework anchors its trustworthine ss
dimensions in a widely adopted engineering standard, providing ex ternal validity for
the dimension choice.
Contextual calibration of the scoring rubric. In response to reviewer feed-
back, we note that the 5-point rubric in Table 8 is deliberately agnostic about the
absolute level of capability and instead focuses on relative investment priority . Appro-
priate calibration varies by organizational context: a small advertiser wi th limited
27

data history (fewer than two years of weekly cross-channel data) should calibrate the
Measure pillar to a simpler Bayesian MMM rather than a neural archite cture, because
the latter’s GRU-based temporal dynamics require suﬃcient data to c onverge reliably
(Tirumala 2025; Sun et al. 2017). A large-platform advertiser with in-house ex per-
imentation infrastructure faces a diﬀerent constraint: the Validat e pillar bottleneck
is not calibration technology but experimental bandwidth, suggesting t hat PIE-style
meta-learning (Gordon et al. 2024) represents the highest-ROI investm ent for raising
τV . For the Protect pillar, the appropriate privacy budget ε depends on both regu-
latory jurisdiction (GDPR strict, CCPA moderate) and the acceptabl e accuracy loss
at the reporting granularity required by the advertiser’s budget-al location decisions.
These contextual factors do not change the framework’s ordering constrai nt but deter-
mine where on the 1–5 rubric each pillar starts and which investment p ath raises the
minimum most eﬃciently.
T able 6 Operationalizing the Measure–Validate–Protect framewor k (diagnostics). Per-pillar
managerial question, diagnostic metric, and minimum evide nce required for the pillar to be
considered “in compliance.” Companion Table 7 lists failur e modes and recommended actions.
Pillar Managerial question Diagnostic metric Minimum evid ence
Measure Can the model predict outcomes
accurately and stably across
datasets?
AUC, MAPE, holdout
R2, train/test gap Out-of-sample validation on a held-out time window.
V alidate Does the model estimate incre-
mental (causal) eﬀects rather
than correlations?
Lift vs. RCT, ATE, cal-
ibration error vs. geo-
experiment
At least one geo-experiment,
ghost-ad test, or auction-
throttling IV per major
channel per year.
Protect Does the system meet privacy
requirements without destroying
measurement utility?
Privacy budget ε,
aggregation thresholds,
clean-room constraints,
identity-leakage risk
Documented privacy audit
mapping regulation to mech-
anism ( ε-DP, FL/clean
room, aggregate-only).
T able 7 Operationalizing the Measure–Validate–Protect framewor k (failure modes & actions).
Companion to Table 6. Together these two tables map the NIST t rustworthiness dimensions
(Section 1) to concrete decisions a marketing analytics pra ctitioner can audit on a quarterly cycle.
Pillar Failure mode Recommended action
Measure Overﬁtting; unstable ranking of chan-
nels across periods; train/test gap
exceeds reported benchmarks.
Simpler MMM, Bayesian priors, regular-
ization, or longer training window; report
channel-ranking stability across retrainings.
V alidate Correlation mistaken for causality;
attribution inﬂated by selection or
demand eﬀects; no recent calibration.
Run a calibration experiment; apply PIE-
style extension from calibrated to uncali-
brated campaigns (Gordon et al. 2024).
Protect Regulatory non-compliance; identity
leakage via cross-platform matching;
measurement-utility loss exceeds toler-
ance under privacy mechanism.
Adopt DP, federated, or aggregate-causal
architecture; recalibrate ε against accept-
able accuracy loss (Table 5); audit RTBF
(machine-unlearning) compliance.
7.1 The Ordering Constraint Principle
A critical and underappreciated implication of the MVP framework is what we term
the ordering constraint : the trustworthiness of the entire measurement pipeline is
28

bounded by the weakest of its three pillars. A neural attribution mod el achieving AUC
> 0.98 (strong Measure) that operates without experimental calibration (w eak Vali-
date) and lacks privacy guarantees (absent Protect) is categorically less trustworthy
than a simpler last-touch model that has been calibrated against a geo-exp eriment and
deployed under a compliant diﬀerential privacy framework. This asymmetry has practi-
cal consequences for investment prioritization: organizations should al locate resources
to the weakest link before improving an already-strong component.
We formalize this as the following actionable principle:
Remark 5 (MVP Ordering Principle) For any marketing measurement system M =
{M, V, P } with trustworthiness scores τM , τV , τP ∈ [0, 1], the system-level trustworthiness
τ (M) is bounded above by min( τM , τV , τP ). Marginal investment in improving any pillar
above the current minimum yields zero system-level trustworthin ess gain until the minimum
is raised.
7.2 Operationalizing MVP in Practice
7.2.1 A 5-Point Scoring Rubric for Each Pillar
To make the ordering principle a usable management tool rather than a qu alitative
slogan, we deﬁne each τ ∈ [0, 1] as the rescaled value of a 5-point pillar maturity score
(1 = absent / non-compliant, 5 = best-in-class) divided by 5. Table 8 p rovides the
rubric.
T able 8 Five-point maturity rubric for the three MVP pillars. Each p illar is scored on the
underlying observables in column 3; τ is the score divided by 5. Score thresholds were anchored to
the empirical evidence in this review: “1” corresponds to th e absence of any defensible practice; “3”
represents the minimum practice observed in the reviewed co rpus for a commercially operating
advertiser (e.g., one geo-experiment per major channel for τV ); “4” corresponds to established
industry best practice as documented in L1–L2 studies (e.g. , continuous PIE-style calibration at
Snap or Pinterest); “5” corresponds to production-grade ev idence from the most advanced
deployments reviewed, attained by large-platform adverti sers with dedicated experimentation and
privacy infrastructure.
Pillar Underlying observ-
able
1 – 5 levels
Measure
(τM )
Out-of-sample ﬁt and
stability of the pro-
duction model
1 = no out-of-sample validation; 2 = single train/test split ; 3 =
held-out time window with reported AUC/MAPE; 4 = rolling-
origin validation with stable channel rankings; 5 = product ion
deployment with documented stability across ≥ 12 months and
multiple market regimes.
V alidate
(τV )
Recency and cover-
age of experimental
calibration
1 = no calibration in >24 months; 2 = single legacy lift study; 3 =
one geo-experiment or ghost-ad test in the past 12 months on t he
largest channel; 4 = annual geo-experiment per major channe l; 5 =
continuous calibration program (PIE-style) with ≥ 80% campaign
coverage.
Protect
(τP )
Documented privacy
architecture and
audited ε budget
1 = no privacy review; 2 = ad-hoc compliance only; 3 = clean-ro om
or aggregation in place but no documented ε budget; 4 = docu-
mented ε budget and DP/FL deployment with measured accuracy
loss; 5 = quarterly privacy audit covering attribution, MMM , and
machine-unlearning compliance.
29

This rubric is deliberately conservative: most organizations will lan d between 2
and 4 on each pillar, and the Example below illustrates the typical asym metric pro-
ﬁle in which the Measure pillar outpaces Validate and Protect. The rub ric is also
non-prescriptive about which mechanism implements each pillar, in line with the
framework’s “what” rather than “how” orientation.
Example 1 (Applying the MVP Ordering Principle) Consider an enterprise adv ertiser oper-
ating a neural attribution system (LiDDA-style transformer, ROC-A UC > 0.97). Applying
the rubric in Table 8: Measure scores 4.5 (rolling-origin validati on, channel rankings stable
across periods) ⇒ τM = 0 .9; Validate scores 1.5 (no geo-experiment or ghost-ad calibrat ion
in the past 18 months, only a legacy 2024 lift study) ⇒ τV = 0 .3; Protect scores 3.5 (clean-
room infrastructure documented, but no formal DP audit or ε budget) ⇒ τP = 0 .7. By the
MVP Ordering Principle, system-level trustworthiness is τ (M) ≤ min(0.9, 0.3, 0.7) = 0 .3.
Two investment options are available. Option A : upgrade the attribution model to a
hypothetically superior architecture that raises τM from 0.9 to 0 .95. Under the ordering prin-
ciple, system trustworthiness remains bounded by min(0 .95, 0.3, 0.7) = 0 .3—a zero marginal
gain. Option B : commission one geo-experiment for the largest channel (estim ated cost:
$40,000–$80,000 and 8–12 weeks), raising τV from 0 .3 to 0 .65 based on calibration evidence
comparable to Chen and Au (2022) and Gordon et al. (2024). Syste m trustworthiness then
rises to min(0 .9, 0.65, 0.7) = 0 .65—a 117% improvement for a fraction of the cost of a model
upgrade.
This numerical illustration motivates the phased roadmap in th e remainder of this section
and the Managerial Decision Guide in Table 9: measurement sophi stication should never
race ahead of the validation and privacy pillars, because doing so produces no system-level
trustworthiness gain while consuming resources that could be red eployed to the binding
constraint.
For marketing analytics practitioners, the MVP framework suggests a phas ed
implementation roadmap. In Phase 1 (Measure), organizations should deplo y a mea-
surement system—whether traditional Bayesian MMM or a neural variant —that
produces defensible channel contribution estimates. The choice of model sophistication
should be calibrated to data availability: DeepCausalMMM’s GRU-based approach
requires suﬃcient time-series length to learn temporal dynamics reliably, while sim-
pler Bayesian MMM may be more appropriate for organizations with fewer th an two
years of weekly data across channels.
In Phase 2 (Validate), organizations should establish an experimental cal ibration
cadence—at minimum, one geo-experiment per major channel per year—to an chor
the measurement system’s causal claims. The key insight from Gordon e t al. (2024) is
that experimental evidence need not be exhaustive: PIE demonstrat es that a subset of
RCTs can train predictive models that extend calibration to uncalib rated campaigns.
The marginal value of the ﬁrst calibration experiment vastly exceeds t he value of
incremental modeling sophistication.
In Phase 3 (Protect), organizations should conduct a privacy architectu re audit
assessing: (a) whether current attribution systems comply with app licable regulations;
(b) the accuracy cost of compliance under the privacy mechanisms avail able; and (c)
30

whether aggregate causal methods like CDA (Filippou et al. 2025) can substit ute for
user-level attribution where regulatory risk is highest.
The MVP framework is explicitly non-prescriptive about the speciﬁ c technologies
employed within each pillar—neural vs. Bayesian, diﬀerential pri vacy vs. federated
learning—because appropriate choices depend on organizational context, regu latory
environment, and data availability. Its prescriptive contributi on is the insistence that
all three pillars must be addressed for trustworthy measurement to be achieved.
7.3 Managerial Decision Guide: Choosing a Measurement
Architecture
Operationalizing the MVP pillars in practice depends on organizational mat urity and
data position. Table 9 maps four archetypal organizational contexts to a recom mended
measurement architecture. The purpose is not to prescribe a singl e correct stack but to
provide a starting point anchored in the evidence synthesized th roughout this review;
each recommendation below cites the primary studies supporting it s feasibility.
31

T able 9 Managerial Decision Guide: matching organizational conte xt to measurement
architecture. Each recommendation is anchored to Level 1–3 evidence from the reviewed corpus;
the MVP pillars (M/V/P) indicate which dimensions the archi tecture primarily addresses and
which require additional investment.
Organization type Data situation Recommended approach (wit h MVP mapping)
Small advertiser Limited channel-level
data; no user-level
tracking
Bayesian hierarchical MMM (Sun et al. 2017; Zhang
et al. 2023) + at least one annual geo-test per major
channel (Chen and Au 2022). MVP: M (simple) + V
(periodic) + P (natively aggregate).
Mid-size retailer CRM + paid-media +
email; partial user-level
data
MMM + holdout/incrementality tests + clean-room
matching for paid-social ROAS reconciliation (Li et al.
2024). MVP: M (moderate) + V (holdout tests) + P
(clean room).
Large platform /
enterprise
advertiser
Large-scale user-level
journeys; in-house
experimentation
capacity
Neural attribution (Bencina et al. 2025; Yang et al.
2020) with top-down MMM constraints (Bencina et al.
2025) + continuous RCT/ghost-ad calibration (Johnson
et al. 2017a; Gordon et al. 2024) + DP or federated
reporting layer (Xiao et al. 2025; Li et al. 2024). MVP:
M (advanced) + V (continuous) + P (DP/FL).
Privacy-
constrained
advertiser
Fragmented identity
graph; ATT/GDPR-
heavy jurisdiction
Aggregate causal attribution (Filippou et al. 2025) +
DP reporting (Ghazi et al. 2024; Xiao et al. 2025) +
browser-level privacy-preserving attribution (W3C 2025;
Kreuter et al. 2023). MVP: M (aggregate) + V
(assumption-dependent) + P (formal DP / MPC).
The table is descriptive rather than exhaustive; a given org anization may mix architectures (e.g., an
enterprise advertiser using aggregate causal attribution for privacy-heavy regions while running neural
attribution in permissive jurisdictions). Feasibility cl aims under “Recommended approach” reﬂect the
evidence grading in Section 2.6.
The key practical takeaway is that measurement sophistication should be matched
to—not exceed—the maturity of the validation and privacy pillars. A small ad ver-
tiser running Bayesian MMM with one well-designed annual geo-test i s closer to MVP
compliance than a large advertiser running neural attribution without experimen-
tal calibration or a documented privacy architecture, despite the l atter’s technical
sophistication.
8 Future Directions and Open Challenges
Our review highlights four interconnected priority areas for future research; all four
are grounded directly in gaps and tensions identiﬁed within the revi ewed corpus
(Sections 3–6) rather than in broad AI trends external to the measurement domain.
We nest measurement-to-optimization challenges within scalable cali bration because
error propagation interacts directly with calibration cadence and exper imental design.
8.1 Scalable Calibration
The measurement-calibration gap—more complex AI models require more cal ibra-
tion while making calibration harder—represents the central tension identiﬁed across
Sections 3, 4, and 5. This gap is directly evidenced by the CATE benchm ark ﬁnding
that 62% of AI causal estimates underperform a zero-eﬀect predictor (Cur th et al.
2025): better modeling without better calibration produces no trust worthiness gain.
32

PIE (Gordon et al. 2024) and the Snap HTE framework (Shi et al. 2024a) demon-
strate that meta-learning across experiments can extend calibration c overage without
proportional experimental cost—a direction grounded in the corpus. Adapt ive exper-
imentation (Fiez et al. 2024) and sequential testing (Bojinov et al. 2023) oﬀe r further
cost-reduction, also documented in the reviewed studies.
A related challenge lies in the transition from measurement to optimi zation. Hier-
archical oﬄine deep RL systems for cross-channel bidding (He et al. 2023) d emonstrate
production-scale deployment, but measurement error propagation thr ough the opti-
mization loop remains insuﬃciently studied—if AI models systemati cally overestimate
certain channels, RL optimizers will compound those errors. This er ror-ampliﬁcation
risk follows directly from the attribution-calibration gap document ed in Section 5.1
and represents a critical feedback failure mode for future invest igation, anchored to
ﬁndings within the reviewed corpus.
8.2 Foundation Models for Marketing Measurement
Foundation models remain at an early stage for measurement tasks, and the ce ntral
question is not raw capability but whether predictive gains translate into causal validity
and operational viability . Research on LLM-based synthetic data for causal inference
has found that generative models can achieve high predictive accuracy w hile substan-
tially misestimating average treatment eﬀects, reinforcing the p rediction–causation
distinction central to this review.
Two performance–eﬃciency ﬁndings sharpen this caution for marketing pipelines
that contemplate LLM-judged conversion labels or LLM-based creative scorin g. First,
on adjacent preference-prediction tasks, Zhang et al. (2026b) benchmark QLoRA-
ﬁne-tuned LLaMA-3 and Gemma-2 against gradient-boosted baselines (XGBoos t,
LightGBM) on the LMSYS Chatbot Arena dataset and ﬁnd that LLMs improve log
loss by only 9.9% while requiring roughly 60,000 × higher inference cost. Second, in
short-text marketing classiﬁcation, Lai et al. (2026) compare Sentence-BE RT against
Word2Vec on e-commerce reviews and ﬁnd that transformer embeddings do not uni-
formly dominate simpler baselines once task length, label scarcity, an d downstream
clustering objectives are controlled; a high-performance cost-eﬀe ctive LLM prompting
framework for specialised short-text classiﬁcation (Liu and Shi 2024) like wise demon-
strates that targeted prompt design rather than model scale is the deci sive lever
in resource-constrained domain-speciﬁc labelling scenarios, with direct application
to marketing pipelines for creative tagging, brand-safety annotation, and conversion
intent labelling. The shared implication is that architecture choic e for measurement-
adjacent labels (review topic mining, creative tagging, conversion judgi ng) should
be matched to task structure, not defaulted to the largest available m odel. Audits
of tabular foundation models for discrete choice further demonstrate t hat economic
validity—the alignment of model predictions with economic rationality constraints—
deteriorates when model complexity outpaces the training distrib ution (Wang et al.
2026b), reinforcing the need for domain-speciﬁc validity checks beyon d standard pre-
dictive metrics. Where retrieval-augmented architectures are u sed over campaign
documents, reviews, or clean-room reports, the architecture-se lection problem extends
33

from model scale to retrieval design (Sections 5.3 and 6.3). The implic ation for mea-
surement is that foundation-model utility is gated by architecture selection and domain
adaptation, not by raw capability alone. For domain-speciﬁc retrieval pip elines under
SME-grade compute constraints, architectural choices—particularly t he balance of
retrieval depth against memory augmentation—matter more than raw model sc ale
for downstream QA accuracy (Liu et al. 2026a). The cost-performance trade-oﬀs gov-
erning deployed LLM pipelines can be further formalized as an eﬃcien cy frontier
over context-length and memory-allocation choices (Shen et al. 2026), a st ructure
directly applicable to marketing analytics systems that query large campaign doc-
ument repositories or clean-room aggregation outputs; domain-speciﬁc adapt ation
combined with model ensembling for small language models (Hu et al. 2026) oﬀe rs a
complementary eﬃciency pathway for measurement pipelines requi ring robust predic-
tions over specialized marketing text—such as campaign briefs, prod uct reviews, or
brand-safety annotations—without the infrastructure cost of large-mode l deployment.
SLM-based agents further extend this eﬃciency advantage to upstream k nowledge-
mining tasks: Zhang et al. (2026a) demonstrate that orchestrated SLM agents
match large-model extraction quality at substantially lower cost, an arc hitecture
pattern directly applicable to marketing pipelines that require systematic campaign-
document parsing, competitive-intelligence extraction, or conten t annotation without
large-model infrastructure. Multimodal signals present an addition al adaptation chal-
lenge: for short-video content requiring brand-safety governance , reasoning-enhanced
domain-adaptive pretraining of multimodal LLMs has demonstrated produc tion-scale
eﬀectiveness (Wang et al. 2025), while modular cross-domain template arc hitectures
(Li et al. 2026a) provide a lower-cost adaptation pathway where full ﬁne-tu ning is
infeasible. Domain-speciﬁc prompt engineering—including automatic prompt search
and dynamic exemplar selection for few-shot classiﬁcation—has been sho wn to sub-
stantially improve LLM accuracy on specialized text labeling tasks (Liu and Shi
2025), with direct implications for marketing content pipelines wher e creative tagging,
brand-safety scoring, and intent labeling each represent domain-spe ciﬁc classiﬁcation
objectives that beneﬁt from targeted prompt optimization rather than re liance on
general-purpose instruction-following.
8.3 Trustworthiness and Explainability
Three explainability paradigms are emerging within marketing measur ement: Shap-
ley value decomposition (Yang et al. 2020), attention-based interpretation (Bencina
et al. 2025), and causal graph visualization (Gong et al. 2024). Each oﬀers a diﬀer-
ent transparency–ﬁdelity trade-oﬀ, and no consensus has emerged. Emp irical evidence
on the stability of these explainability layers reinforces the caut ionary stance of the
broader low-SNR result: Lin and Wang (2025) train one hundred XGBoost credi t-
default models with identical hyperparameters but diﬀerent rand om seeds and ﬁnd
that SHAP feature-importance rankings are highly stable for the top-ﬁve mos t pre-
dictive features (Kendall’s W = 0.93) yet substantially less stable for mid-importance
features ( W = 0 .34). Because most marketing channels other than the dominant one
tend to occupy the mid-importance regime, this ﬁnding implies t hat channel-level
Shapley attributions for non-dominant channels should be reported wit h stability
34

checks across model retrainings rather than as point estimates—a meth odological audit
that is currently rare in MTA practice. Hierarchical contrastive Shap ley values (Xiao
et al. 2026) extend this perspective from feature-level to data-sample prioritization:
by constructing coalition-level contrasts across training examples , they identify which
data samples most drive model outputs—a complementary diagnostic that s urfaces
the data contributors underlying channel-level attribution esti mates and potential poi-
soning surfaces when applied to MTA training pipelines. Loss landsc ape visualization
tools (Xie et al. 2024) oﬀer a complementary diagnostic lens, enabling practi tioners
to assess whether the training dynamics underlying a neural attri bution model are
stable across re-initializations before attributing substantive me aning to its channel-
level outputs; topological proﬁling of the loss surface (Geniesse et al. 2024) extends
this diagnostic by capturing global curvature structure—including ﬂ at-minima versus
sharp-region transitions—that predicts generalization instability in dependently of any
single model checkpoint. For attribution and measurement workﬂows t hat incorporate
graph neural networks—including GNN-based bot ﬁlters (Zhao et al. 2026) that f eed
cleaned signals into attribution models or spatiotemporal GNNs applied to geographic
market data—formal uncertainty quantiﬁcation of network outputs (Yu et al. 2025)
complements these single-checkpoint diagnostics by attaching calib rated conﬁdence
bounds to GNN predictions, enabling practitioners to distinguish at tributable channel
eﬀects from regions of high epistemic uncertainty before those estim ates inform bud-
get decisions. Three adjacent lines of XAI research are directly relev ant when these
paradigms are deployed in measurement pipelines. First, model-agn ostic counterfac-
tual explanations—ReLAX (Chen et al. 2022) and feasibility/diversity-const rained
variants (Qin et al. 2025)—translate “what-would-need-to-change” decision r ules into
actionable attribution insights, but, as Chen et al. (2023) caution, the same counter-
factual machinery can be an attack surface when the measurement pipeli ne is exposed
to adversarial inputs. Second, adversarial robustness is a ﬁrst-clas s trustworthiness
dimension under the NIST AI RMF (National Institute of Standards and Tech nol-
ogy 2023); certiﬁcation bounds such as PROSAC (Feng et al. 2025) oﬀer a formal
counterpart to the qualitative robustness requirements that marke ting measurement
systems must meet when model outputs feed budget-allocation deci sions; prompt-level
adversarial defenses such as logical self-reﬂection (Lin et al. 2026) provi de a comple-
mentary run-time safeguard when LLMs are exposed to adversarial user inp uts in
interactive measurement interfaces; optimized iterative jailbr eak attacks (Shi et al.
2026) demonstrate that such defenses can be systematically evaded by tool -assisted
adversarial search, underscoring that adversarial-robustness evaluat ion must include
active attack simulation and not only static certiﬁcation bounds. Beyond s ingle-
component robustness, marketing measurement pipelines routinel y compose multiple
AI modules—attribution models, LLM judges, privacy mechanisms, and opt imiza-
tion layers—introducing emergent risks absent in any individual c omponent: Wang
et al. (2026a) quantify how otherwise-safe agent skills generate unsafe beh aviors when
combined in an ecosystem, underscoring that compositional-safety eval uation is a dis-
tinct and necessary dimension of trustworthy marketing AI under the NIST AI RMF.
Third, under the low-SNR regime characteristic of advertising data (Section 5.1.1),
Shi et al. (2024b) show that standard post-hoc attribution methods can mis identify
35

signal, a ﬁnding that directly constrains how much weight can be place d on any single
explainability layer.
The fairness dimension also enters measurement. DICE-DML (Liu e t al. 2026b)
demonstrated that advertising visual attributes causally aﬀect engagem ent, implying
that AI measurement systems can encode creative biases. Two adjacent literatures
speak to this risk: Guo et al. (2024) synthesize intrinsic/extrinsi c bias in LLMs and
pre-/intra-/post-model mitigation strategies that apply when LLMs annotate or sum-
marize marketing content, and codebook-rebalancing techniques su ch as CRAB (Fan
et al. 2026) mitigate popularity bias in generative recommenders whose engagem ent
signals feed measurement pipelines. Taken together, these result s argue for a trustwor-
thiness audit that spans interpretability, low-SNR robustness, ad versarial safety, and
bias mitigation—all anchored to the measurement task rather than treated as generic
AI concerns. Where RL-based training is used to tune LLM scoring or attri bution
components, reward-design brittleness under sparse conversion si gnals (Wang et al.
2026c) introduces additional failure modes that require iterative diagn ostic reﬁne-
ment before deployment in budget-allocation loops. Interpretabl e factor decomposition
methods (Han et al. 2026) complement Shapley-based channel attribution by providing
an explicit mathematical factorization of decision value that is structu rally auditable
and directly compatible with the orthogonality requirements of a mult i-channel MTA
audit.
8.4 Cross-Platform Uniﬁed Measurement
The ultimate vision is privacy-preserving cross-platform measure ment that maintains
causal validity. This requires integrating clean-room federated le arning, diﬀerential
privacy for aggregate reporting, and causal structure discovery for ident ifying channel
eﬀects without user-level linkage. The IPA (Interoperable Privat e Attribution) pro-
tocol (Kreuter et al. 2023) and W3C speciﬁcation (W3C 2025) represent early ste ps,
but substantial technical and institutional barriers remain—includ ing competitive
dynamics that may prevent platforms from sharing measurement data ev en through
privacy-preserving mechanisms.
9 Discussion and Conclusion
9.1 Summary of Findings
This systematic review synthesized 108 studies examining AI-dri ven marketing mea-
surement. Three principal ﬁndings emerge, directly addressing our research questions.
Strength-of-evidence summary .Before reporting these ﬁndings, we summarize
the evidentiary foundation for each topic area to help readers distingu ish strongly
supported conclusions from more speculative ones (Table 10).
T able 10 Strength-of-evidence summary by topic. “Evidence basis” r eports the dominant
evidence level (L1–L4) for the central claim; “conﬁdence” i s the authors’ qualitative assessment:
High = central claim supported by multiple L1/L2 studies wit h replication; Moderate = L2
support with L3 corroboration; Low = primarily L3–L4 eviden ce; speculative or contested.
36

Topic / Central claim Dominant
evidence
Conﬁdence Key caveat
Observational attribution
overstates lift (62–115%
error)
L1 High Based on Facebook/Google RCT
benchmarks; platform-speciﬁc.
Deep learning attribution
improves predictive AUC
L2–L3 Moderate AUC gains documented; causal validity not
established.
Neural MMM outperforms
Bayesian baselines on
prediction
L3 Low–
Moderate
Single-benchmark comparison; not externally
replicated.
Experimental calibration
reduces attribution error
L1 High Multiple RCT benchmarks across platforms
and methods.
DP reduces accuracy by
2–33%
L2–L3 Moderate Range aggregates heterogeneous
conﬁgurations; not universal.
Federated/clean-room
deployments retain ∼90–95%
accuracy
L2 Moderate Pinterest-speciﬁc; conﬁguration-dependent.
Foundation models less
cost-eﬃcient than gradient
boosting for marketing tasks
L3 Low Limited direct marketing evidence; requires
replication.
SHAP stability degrades for
mid-importance channels
L2 Moderate Credit-risk context; marketing application is
analogical.
Regarding RQ1, AI methods substantially improve the predictive accuracy and
scalability of marketing measurement. Deep learning attribution mo dels achieve AUC
exceeding 0.98 (Zhan et al. 2024), neural MMM frameworks reduce predicti on error
by 5–15 × (Mulc et al. 2025), and industrial HTE estimation enables personalized
measurement at the scale of hundreds of millions of users (Shi et al. 2024a). These
improvements have been validated in production at LinkedIn, Snap, JD.com, and other
platforms.
Regarding RQ2, predictive accuracy does not guarantee causal validity. The
most comprehensive evidence (Gordon et al. 2023) demonstrates median er rors of
62–115% relative to experimental benchmarks. This motivates the MVP frame work:
AI-driven measurement (Measure) must be calibrated against experim ental evidence
(Validate). PIE (Gordon et al. 2024) exempliﬁes this integration, using e xperiments as
ground truth and ML as a scaling mechanism. The advertising eﬀective ness paradox—
true elasticities averaging 0.0008 short-term (Shapiro et al. 2022)—makes acc urate
measurement especially critical, as small biases easily overwhelm genuine eﬀects.
Regarding RQ3, privacy-preserving measurement is feasible but involves quan-
tiﬁable trade-oﬀs. Diﬀerential privacy reduces accuracy by 2–33% (Xiao et al. 2025);
in a documented clean-room/federated deployment, a combined fed erated-plus-LoRA
conﬁguration retained approximately 90–95% of centralized performance unde r its
reported conﬁguration (Li et al. 2024); and aggregate causal discovery can recover
meaningful channel-level attribution (Filippou et al. 2025). These ﬁgur es are context-
speciﬁc and should not be read as universal benchmarks. The choice among approaches
depends on regulatory environment, data availability, and accuracy req uirements.
Taken together, these three ﬁndings reveal a structural paradox at the heart
of AI-driven marketing measurement: the techniques that most powe rfully capture
measurement complexity—deep neural architectures, automated causal discovery,
personalized HTE estimation—are precisely those that most urgently req uire the
experimental validation and privacy infrastructure that many organizati ons currently
lack. AI does not simplify the trustworthy measurement problem; i t raises the stakes.
37

The MVP framework is designed to make this paradox actionable rather than p aralyz-
ing, by providing a principled roadmap for building trustworthy me asurement systems
incrementally (Section 7).
9.2 Positioning the MVP Framework Against Competing
Frameworks
The MVP framework can be situated within a broader landscape of measureme nt
and accountability frameworks. We engage here with the four most closely r elated
alternatives.
T riangulation and uniﬁed measurement. The triangulation approach (Google
Think 2022) advocates combining MMM, experiments, and attribution at th e data
level to improve measurement conﬁdence. MVP is complementary but distinct: tri-
angulation speciﬁes which methods to combine , while MVP speciﬁes why combining
methods is necessary (the ordering constraint) and how to diagnose which leg is the
binding constraint . In particular, the MVP ordering principle implies that adding
a third measurement method (say, incrementality testing) to a s ystem that already
passes the Measure and Validate thresholds produces lower marginal tr ustworthiness
gain than addressing a weak Protect pillar.
Marketing accountability and marketing productivity . Research on mar-
keting accountability (Rust et al. 2004; Srinivasan et al. 2010) emphasizes th e
responsibility of marketers to justify investment through rigorous measurement. MVP
operationalizes this imperative at the system level: the Validate pi llar translates the
accountability mandate into a concrete, auditable requirement (exp erimental calibra-
tion coverage), and the ordering constraint formalizes why accountabili ty cannot be
achieved by model sophistication alone.
Causal machine learning. The causal ML literature (Chernozhukov et al. 2018;
Wager and Athey 2018; Athey et al. 2019) provides the technical machinery for t he
Validate pillar. MVP’s contribution is to position causal ML methods wi thin a broader
management framework rather than treating them as independent modeli ng advances:
DML and causal forests are Validate-pillar tools whose value depends on wh ether the
Measure and Protect pillars are also in place.
Responsible AI and privacy engineering. Responsible AI frameworks
(National Institute of Standards and Technology 2023) and privacy engineering s tan-
dards address the organizational governance and technical design of AI syste ms. MVP
draws on these frameworks for the Protect pillar but specializes the m to market-
ing measurement—replacing generic “privacy compliance” with speci ﬁc requirements
about ε-budget documentation, machine-unlearning auditing, and accuracy-l oss vali-
dation under the privacy mechanism actually deployed. This speciﬁ city is necessary
because the acceptable accuracy cost of privacy compliance depends on th e eﬀect sizes
that the measurement system must detect, which are unusually smal l in advertising
contexts (Section 5.1.1).
Theoretical contribution: the weakest-pillar principle. The MVP frame-
work’s primary theoretical claim—that pipeline trustworthiness is bounded by its
weakest pillar—is a marketing-speciﬁc instantiation of the min-max logi c found in sys-
tems reliability theory. Its practical implication (that resource al location should target
38

the binding constraint, not the strongest pillar) follows directly from this logic and
is empirically grounded in the review ﬁndings: the studies most cl early showing high
predictive accuracy with low causal credibility (Section 3.5) are pr ecisely those where
organizations have invested in Measure while neglecting Validate.
9.3 Implications for Research
We identify four high-priority research directions. First, privacy-native causal
inference methods that identify treatment eﬀects from aggregate data without user-
level variation represent the most impactful technical challenge. S econd, calibration
of diﬀerential privacy parameters for advertising contexts requires both empirical
research and regulatory engagement—current implementations use ε values ranging
from 1 to 8 without clear justiﬁcation. Third, the measurement-to-action feedback
loop created by integrating reinforcement learning with causal measurem ent intro-
duces error ampliﬁcation risks that require theoretical and empiric al analysis. Fourth,
foundation models for marketing measurement remain at an early stage, with
the potential for transfer learning largely unexplored.
9.4 Implications for Practice
For marketing practitioners, our review suggests three actionable pri nciples. First,
adopt a triangulation approach combining at least two independent measurement
methods. Google’s published uniﬁed measurement program reports rou ghly 40% higher
expected uplift versus MTA-only designs when MMM, experiments , and attribution
are integrated at the data level (Google Think 2022). Industry deploymen ts—including
agency-led uniﬁed measurement programs and Pinterest’s clean-room s tack—illustrate
that MVP-style integration is not merely theoretical: organizations that op erational-
ize measurement, experimentation, and privacy-preserving collab oration can achieve
materially higher conﬁdence in measurement-driven budget decisi ons (Google Think
2022; Li et al. 2024). Second, invest in experimental calibration infrastructure
before model sophistication. Gordon et al. (2023) and Gordon et al. (2024) demonstr ate
that even simple calibration of last-click conversions outperforms sop histicated non-
experimental methods by orders of magnitude. The marginal value of one add itional
geo-experiment exceeds upgrading from Bayesian to neural MMM for most organi-
zations (Rust et al. 2004). Third, evaluate privacy-preserving measure ment based
on causal properties , not merely predictive accuracy. Beyond technical consider-
ations, organizations face signiﬁcant implementation barriers . Building in-house
experimentation infrastructure requires substantial engineeri ng investment. The skill
sets needed—spanning causal inference, deep learning, privacy engi neering, and mar-
keting domain knowledge—are rarely found in a single team. Organizational s ilos
between data science, marketing, and legal/compliance functions impe de the inte-
grated approach that the MVP framework demands. Addressing these barrier s requires
executive sponsorship, cross-functional teams, and incremental adop tion strategies.
39

9.5 Limitations
This review has several limitations that readers should consider whe n interpreting
ﬁndings.
Inter-rater reliability . Inter-rater agreement on inclusion decisions reached
Cohen’s κ = 0 .81 on the title/abstract calibration subset ( n = 64) and κ = 0 .83 on
the full-text candidates ( n = 189, all independently dual-coded), both in the “almost
perfect” range under McHugh (2012) criteria. Evidence-level coding ac hieved weighted
κ = 0.76 (“substantial” agreement) on the calibration subset. Post-calibration screen-
ing of the remaining title/abstract records was performed by a single au thor with
bilateral and third-author adjudication for all ambiguous cases, rather than by inde-
pendent dual coding throughout. Full-corpus dual coding of all 635 recor ds would have
provided a stronger reliability guarantee, and we encourage replication s in this domain
to adopt that more conservative protocol. The κ statistics reported above are for the
calibration stage; their applicability to the full corpus is an acknowl edged limitation.
Publication bias. The corpus is likely skewed toward positive results. Industry-
led research from major technology platforms (Google, Meta, Snap, Pinter est) is
systematically over-represented because these organizations have both the resources
to run large-scale experiments and the incentive to publish favor able results. Null or
negative ﬁndings—experiments showing no measurable advertising l ift, or models that
fail to improve on simple baselines—are underrepresented. This m ay cause our review
to present an optimistic picture of AI-driven measurement perform ance.
Preprint quality variance. At 41% of the corpus, preprints introduce quality
variance that the four-level evidence grading scheme partially miti gates but does not
eliminate. Preprints indexed on arXiv and SSRN have not undergone pee r review, and
some claims in Level 3–4 studies may not survive formal review. We have hedged all
preprint-based claims accordingly, but readers should treat ﬁndings supported only
by Level 3–4 evidence as directional rather than deﬁnitive.
Date ceiling. Database searches were concluded in March 2026. The rapid
pace of development in large language models, foundation models for tabular d ata,
and privacy-preserving computation means that relevant work publish ed or posted
after this date is not captured. In particular, post-GPT-4 developme nts in LLM-
based creative measurement and emerging regulatory frameworks (e.g., E U AI Act
implementation guidance) may alter conclusions in Sections 8.2 and 6.
Corpus concentration. The included studies are disproportionately drawn
from large technology platforms and top-tier computer science venues. M easurement
practices at mid-size advertisers, agencies, and non-US markets are un derrepre-
sented, limiting the generalizability of our practitioner-facing r ecommendations to
organizations with large-scale data infrastructure.
Narrative synthesis. The heterogeneity of study designs, outcome metrics,
and evaluation settings across the 108 included studies precludes quan titative meta-
analysis of eﬀect sizes. Eﬀect-size ranges reported throughout the re view (e.g., DP
accuracy loss of 2–33%) aggregate across heterogeneous conﬁgurations and should not
be interpreted as precise universal benchmarks.
40

9.6 Conclusion
AI is transforming marketing measurement with unprecedented capab ilities in pattern
recognition, temporal modeling, and privacy-preserving computation. However, our
review reveals a persistent tension between predictive power and causal credibility. The
most important insight is not that AI makes measurement more accurate—though it
often does—but that AI makes the distinction between prediction and c ausation more
consequential. As AI-driven systems increasingly inform multi-mi llion-dollar budget
allocation decisions, conﬂating correlation with causation carries highe r stakes than
ever. The Measure–Validate–Protect framework proposed in this review provides a
roadmap: trustworthy marketing measurement requires sophisticate d AI models, rig-
orous experimental validation, and principled privacy design, integr ated as a coherent
system rather than as independent components. Together, our answers t o RQ1–RQ3
establish that AI-driven marketing measurement is powerful, caus ally limited without
calibration, and privacy-compliant at a measurable accuracy cost—a triple constraint
that the MVP framework is designed to navigate systematically.
Supplementary information. Supplementary Table S1
(Supplementary Table S1 Included Studies Matrix.xlsx) provides the full 108-
study included-studies matrix used for coding, evidence grading, and section-level
citation placement. The reference list reports works cited in the article text; Supple-
mentary Table S1 records additional included studies that were code d for corpus-level
synthesis but not individually cited in the main text.
Acknowledgements. The authors thank colleagues and reviewers for helpful
comments.
Declarations
F unding. No funding was received for this study.
Competing interests. The authors declare no competing interests.
Ethics approval and consent to participate. Not applicable.
Consent for publication. Not applicable.
Data availability . This study analyzes previously published or posted litera-
ture. The extracted 108-study included-studies matrix is provid ed as Supplementary
Table S1.
Materials availability . Not applicable.
Code availability . Not applicable.
Author contributions. Author contributions are omitted from the anonymized
manuscript for double-blind review.
41

Appendix A PRISMA Screening Summary
The systematic search and screening process followed PRISMA 2020 gui delines (Page
et al. 2021). Records identiﬁed through database searching: 847 (Scopus 312; Web of
Science 248; IEEE Xplore 137; ACM DL 94; arXiv/SSRN 56). Records after dupli-
cate removal: 635. Records screened by title and abstract: 635. Records exc luded at
screening: 446 (reasons: not measurement-focused, 289; no AI/ML component , 102;
non-English, 31; trade publications, 24). Full-text articles assessed for eligibility: 189.
Full-text articles excluded: 81 (reasons: insuﬃcient empirical content, 38; scope mis-
match, 27; superseded by later version, 16). Studies included from dat abase search:
80. Additional studies from expert seeding and citation tracking: 28. Total s tudies
included in review: 108. Reviewer calibration was performed on a subse t of records
and residual disagreements were resolved through consensus (see Appe ndix C).
Appendix B Search Strings and Database Results
All searches were executed between January 15 and March 10, 2026, restricte d to
English-language records from 2010 through early 2026. Boolean logic was the same
across databases— C1 AND (C2 OR C3) —with ﬁeld speciﬁers adapted per platform.
Scopus (TITLE-ABS-KEY). 312 records:
TITLE-ABS-KEY(
("multi-touch attribution" OR "media mix model*" OR
"marketing measurement" OR "advertising effectiveness" OR
"return on ad spend" OR "ROAS" OR "advertising lift")
AND
(("deep learning" OR "neural network*" OR "transformer" OR
"recurrent neural" OR "graph neural" OR "machine learning" OR
"causal inference" OR "heterogeneous treatment effect" OR
"uplift model*" OR "double machine learning")
OR
("randomized experiment" OR "field experiment" OR "A/B test*" OR
"geo experiment" OR "causal calibration" OR "differential privacy" OR
"federated learning" OR "clean room" OR "privacy-preserving")))
AND PUBYEAR > 2009 AND PUBYEAR < 2027 AND LANGUAGE(english)
W eb of Science (Topic ﬁeld). 248 records. Same Boolean structure, translated to
TS=(C1) AND (TS=(C2) OR TS=(C3)) with WoS wildcards ( *) preserved.
IEEE Xplore (Command search, Metadata). 137 records:
((("Document Title":"attribution" OR "multi-touch" OR
"media mix" OR "advertising effectiveness") OR
("Abstract":"marketing measurement" OR "advertising lift"))
AND
("Abstract":"deep learning" OR "neural" OR "transformer" OR
"causal" OR "uplift" OR "differential privacy" OR "federated")
)
Filters: 2010-2026, English
ACM Digital Library (Advanced Search). 94 records:
42

[[Abstract: "attribution" OR "media mix" OR
"marketing measurement" OR "advertising lift"]
AND
[Abstract: "deep learning" OR "neural" OR "transformer" OR
"causal" OR "differential privacy" OR "federated" OR
"clean room"]]
Published: 2010-01-01 to 2026-03-31, Language: English
arXiv / SSRN (title + abstract). 56 records total (arXiv 41; SSRN 15). We used
the arXiv API with Boolean AND of three term groups and restricted to categori es
cs.LG, cs.IR, stat.AP, stat.ML, econ.EM, cs.CR. SSRN was searched by exact phrase
queries (“multi-touch attribution”, “media mix model”, “advertisin g eﬀectiveness”,
“privacy-preserving attribution”) with year ﬁlter 2010–2026.
Yield summary. Raw records 847; duplicates 212 (auto-removed via DOI and
normalized-title matching); unique records screened 635; excluded at title/abstract
446; full-text assessed 189; excluded at full-text 81; included 108.
Appendix C Coding Protocol and Reviewer
Calibration
The coding scheme below was ﬁnalized before screening began. Two au thors jointly
reviewed a calibration subset of records (approximately 10% of the 635 tit le/abstract
records and all 189 full-text candidates) to align interpretation of the i nclusion criteria
and each coding dimension; subsequent records were screened by on e author, with
ambiguous or boundary cases ﬂagged for joint review. Disagreements and ﬂagged
cases were resolved through discussion; cases that could not be reconci led bilaterally
were adjudicated by a third author. The coding spreadsheet underl ying this review is
provided as Supplementary Table S1 (Appendix D).
Inclusion decision (binary). Include iﬀ all three hold: (a) addresses market-
ing or advertising measurement, attribution, or media mix modelin g; (b) employs or
evaluates an AI/ML method, a causal-inference technique, or a privacy -preserving
technology; (c) presents empirical results, a theoretical framewor k, or a systematic
review.
Exclusion decision (any-of ). Exclude if: exclusively about recommender sys-
tems / content generation / consumer behavior without a measurement c omponent;
non-English; trade publication without methodological content; super seded by a later
version already in the corpus.
Coding Dimension 1: measurement function (mutually exclusive pr i-
mary value plus multi-domain ﬂag). {Attribution; MMM; Causal calibration;
Privacy-preserving measurement; Multi-domain }.
Coding Dimension 2: AI technique (non-exclusive binary ﬂags).
{RNN/LSTM/GRU; Transformer; Neural ODE; DAG/Causal discovery;
DML/Debiased ML; Causal forest/GRF; Diﬀerential privacy; Federated le arning;
Cryptography}.
Coding Dimension 3: evidence level (ordinal, 1–4). See Table 3.
43

Extraction ﬁelds (free-text). Research question; data scale & source; experi-
mental vs. observational; primary performance metric(s) and value(s) ; stated limita-
tions.
Reviewer calibration process. Calibration records that elicited disagreement
were used to reﬁne the written coding rubric before it was applie d to the balance of the
corpus. In line with practical guidance for interrater calibration in s ystematic reviews
(McHugh 2012), residual disagreements (both at title/abstract and full-tex t stages)
were logged and resolved through structured consensus discussion, wi th third-author
adjudication reserved for cases that could not be reconciled bilaterall y. Inter-rater
reliability statistics: title/abstract binary inclusion κ = 0.81 ( n = 64); full-text binary
inclusion κ = 0 .83 ( n = 189); evidence-level weighted κ = 0 .76 ( n = 64). All three
statistics fall in the “substantial” to “almost perfect” range under Mc Hugh (2012)
criteria.
Appendix D Included Studies Matrix (summary)
and Supplementary Material
Table D1 summarizes the 108 included studies aggregated by Dimen-
sion 1 (measurement function), Dimension 2 (dominant AI technique
family), and Dimension 3 (evidence level). The per-paper struct ured
matrix is provided with this submission as Supplementary T able S1
(Supplementary Table S1 Included Studies Matrix.xlsx), with the following
ﬁelds per study: citation key, year, publication type, venue, peer reviewed, evi-
dence level, measurement function, AI method family, data scale, evaluation metric,
key ﬁnding, limitation, cited in section. The supplementary ﬁle is submitted concur-
rently with the manuscript so that reviewers can directly verif y corpus composition,
evidence grading, and section-level citation placement. Some corpus r ecords are syn-
thesized only at the aggregate level and therefore appear in Supplement ary Table S1
without being individually cited in the article reference list .
T able D1 Distribution of the 108 included studies by measurement fun ction (Dim. 1) and
evidence level (Dim. 3). Cells count studies; row/column to tals allow readers to verify that no
single cell drives a central claim. L1 evidence concentrate s in causal calibration, while L2 evidence
spans attribution, causal calibration, privacy-preservi ng measurement, and multi-domain work.
Measurement function L1 L2 L3 L4 Total % of corpus
Attribution (MTA, CDA) 0 5 17 2 24 22%
Media mix modeling 0 2 10 9 21 19%
Causal calibration & HTE 8 11 9 0 28 26%
Privacy-preserving measurement 1 6 10 3 20 19%
Multi-domain / framework 0 6 7 2 15 14%
T otal 9 30 53 16 108 100%
L1 = peer-reviewed ﬁeld experiments / RCT benchmarks; L2 = pe er-reviewed empirical studies or replicated
production deployments; L3 = preprints with empirical vali dation; L4 = conceptual / prototype / white-
paper work. See Section 2.6 and Table 3.
44

References
Abadie A, Diamond A, Hainmueller J (2010) Synthetic control methods for compar-
ative case studies: Estimating the eﬀect of California’s tobacco contr ol program.
Journal of the American Statistical Association 105(490):493–505
Aridor G, Che YK, Salz T (2023) The eﬀect of privacy regulation on the data indus try:
Empirical evidence from GDPR. RAND Journal of Economics 54(4):649–672
Aridor G, Che YK, Hollenbeck B, et al (2024) Evaluating the impact of privacy re g-
ulation on e-commerce ﬁrms: Evidence from Apple’s App Tracking Transp arency.
SSRN Working Paper 4698374
Athey S, Tibshirani J, Wager S (2019) Generalized random forests. Annals of S tatistics
47(2):1148–1178
Barlow RE, Proschan F (1975) Statistical Theory of Reliability and Life Test ing:
Probability Models. Holt, Rinehart and Winston, New York
Basu R, Aktar N, Kumar S (2024) The interplay of artiﬁcial intelligence, mach ine
learning, and data analytics in digital marketing and promotions: A review and
research agenda. Journal of Marketing Analytics 12(4):786–812
Bencina J, Aykutlug E, Chen Y, et al (2025) LiDDA: Data driven attribution at
LinkedIn. ArXiv preprint arXiv:2505.09861
Berman R, Feit EM (2024) Latent stratiﬁcation for incrementality experim ents.
Marketing Science 43(4):903–917
Bojinov I, Rambachan A, Shephard N (2023) Design-based conﬁdence sequenc es for
sequential experiments. ArXiv preprint arXiv:2210.08639
Brodersen KH, Gallusser F, Koehler J, et al (2015) Inferring causal imp act using
Bayesian structural time-series models. Annals of Applied Statist ics 9(1):247–274
Chen A, Au TC (2022) Robust causal inference for incremental return on ad spe nd
with randomized paired geo experiments. Annals of Applied Statistics 16(1):1–20
Chen X, Xiao C, Liu Y (2024a) Confusion-resistant federated learning via diﬀ usion-
based data harmonization on non-IID data. Advances in Neural Information
Processing Systems 37:137495–137520
Chen Y, Qian P, Wang S, et al (2026) Does RAG know when retrieval is wrong?
diagnosing context compliance under knowledge conﬂict. URL https://arx iv.org/
abs/2605.14473, arXiv:2605.14473
45

Chen Z, Silvestri F, Wang J, et al (2022) ReLAX: Reinforcement learning age nt
explainer for arbitrary predictive models. In: Proceedings of the 31st ACM Inter-
national Conference on Information and Knowledge Management (CIKM), URL
https://arxiv.org/abs/2110.11960, arXiv:2110.11960
Chen Z, Silvestri F, Tolomei G, et al (2023) The dark side of explanations: P oisoning
recommender systems with counterfactual examples. In: Proceedi ngs of the 46th
International ACM SIGIR Conference, URL https://arxiv.org/abs/2305.00574,
arXiv:2305.00574
Chen Z, Tan H, Wang H, et al (2024b) A new baseline assumption of inte-
grated gradients based on Shapley value. URL https://arxiv.org/abs/2310.04821,
arXiv:2310.04821
Chen Z, Wang J, Zhuang J, et al (2024c) Debiasing machine unlearning with
counterfactual examples. URL https://arxiv.org/abs/2404.15760, arXiv:2404.15760
Cheng Z, Lai L, Liu Y (2026a) Resolving the robustness-precision trade-oﬀ in ﬁnancial
RAG through hybrid document-routed retrieval. URL https://arxiv.or g/abs/2603.
26815, arXiv:2603.26815
Cheng Z, Lai L, Liu Y, et al (2026b) Enhancing ﬁnancial report question-answeri ng: A
retrieval-augmented generation system with reranking analysis. URL h ttps://arxiv.
org/abs/2603.16877, arXiv:2603.16877
Chernozhukov V, Chetverikov D, Demirer M, et al (2018) Double/debiased machine
learning for treatment and structural parameters. The Econometrics J ournal
21(1):C1–C68
Curth A, et al (2025) A large-scale empirical assessment of CATE estimation. In:
Proceedings of the 13th International Conference on Learning Represent ations
(ICLR)
Dalessandro B, Stitelman O, Perlich C, et al (2012) Causally motivated attr ibution
for online advertising. In: Proceedings of the Sixth International Wor kshop on Data
Mining for Online Advertising and Internet Economy (ADKDD). ACM
Du R, Zhong Y, Nair H, et al (2019) Causally driven incremental multi touch
attribution using a recurrent neural network. ArXiv preprint arXiv: 1902.00215
Du X, Qian C, Zhang L, et al (2025) PrivacyGo: Secure and privacy-preserving multi-
identiﬁer ad measurement. ArXiv preprint arXiv:2506.20981
Fan Z, et al (2026) CRAB: Codebook rebalancing for bias mitigation in generative
recommendation. URL https://arxiv.org/abs/2604.05113, arXiv:2604.05113
46

Feng C, Liu Z, Zhi Z, et al (2025) PROSAC: Provably safe certiﬁcation for mac hine
learning models under adversarial attacks. In: The 39th Annual AAAI Confere nce
on Artiﬁcial Intelligence (AAAI) [Oral], https://doi.org/10.1609/aaai.v39i3.32300
Feng C, Shen M, Balashankar A, et al (2026) Noisy but valid: Robust statistical
evaluation of LLMs with imperfect judges. In: The Fourteenth Internat ional Con-
ference on Learning Representations (ICLR), URL https://openreview. net/forum?
id=hEhxreaLdU
Fiez T, Nassif H, Chen YC, et al (2024) Best of three worlds: Adaptive experim entation
for digital marketing in practice. In: Proceedings of the ACM Web Conf erence 2024
(WWW), arXiv preprint arXiv:2402.10870
Filippou A, Quach M, Lenghel I, et al (2025) Causal-driven attribution: Esti mating
channel inﬂuence without user-level data. ArXiv preprint arXiv:2512.21211
Gaur J, Bharti K (2020) Attribution modelling in marketing: Literature r eview and
research agenda. Academy of Marketing Studies Journal 24(4):1–21
Geniesse C, Chen J, Xie T, et al (2024) Visualizing loss functions as topologic al
landscape proﬁles. URL https://arxiv.org/abs/2411.12136, arXiv:2411.12136
Ghazi B, Kamath P, Kumar R, et al (2024) Diﬀerentially private ad conversion mea-
surement. Proceedings on Privacy Enhancing Technologies 2024(2). ArXiv pr eprint
arXiv:2403.15224
Goldfarb A, Tucker C (2011) Privacy regulation and online advertising. Manageme nt
Science 57(1):57–71
Gong C, Yao D, Zhang L, et al (2024) CausalMMM: Learning causal structure for
marketing mix modeling. In: Proceedings of the 17th ACM International Conference
on Web Search and Data Mining (WSDM), arXiv preprint arXiv:2406.16728
Google Think (2022) Uniﬁed marketing measurement. ThinkWithGoogle whi tepaper
Gordon BR, Zettelmeyer F, Bhargava N, et al (2019) A comparison of approaches
to advertising measurement: Evidence from big ﬁeld experiment s at Facebook.
Marketing Science 38(2):193–225
Gordon BR, Moakler R, Zettelmeyer F (2023) Close enough? A large-scale explor ation
of non-experimental approaches to advertising measurement. Marketi ng Science
42(4):768–793
Gordon BR, Moakler R, Zettelmeyer F (2024) Predictive incrementality by experi-
mentation (PIE) for ad measurement. ArXiv preprint arXiv:2304.06828
Gui J, Nair H, Niu Y (2022) Auction throttling and causal inference of online
advertising eﬀects. ArXiv preprint arXiv:2112.15155
47

Guo Y, Guo M, Su J, et al (2024) Bias in large language models: Origin, eval-
uation, and mitigation. URL https://arxiv.org/abs/2411.10915, arXiv preprint
arXiv:2411.10915
Gupta NR, Orlandi V, Chang CR, et al (2025) dame-ﬂame: A python package provid-
ing fast interpretable matching for causal inference. Journal of Stati stical Software
113(2):1–26. https://doi.org/10.18637/jss.v113.i02
Han X, Xiao Y, Zhang Z, et al (2026) Interpretable factor decomposition for decision
intelligence in large-scale ﬁnancial markets: Evidence from China’s A-share market.
URL https://arxiv.org/abs/2606.12843, arXiv:2606.12843
Hanssens DM, Parsons LJ, Schultz RL (2001) Market Response Models: Econome tric
and Time Series Analysis, 2nd edn. Springer, Boston, MA
He X, et al (2023) HiBid: Hierarchical oﬄine deep reinforcement learning for c ross-
channel bidding. ArXiv preprint arXiv:2312.17503
Hu L, Xin Y, Shen B, et al (2026) CoDES: A context-eﬃcient framework for
enhancing small language models via domain-speciﬁc adaptation and model ensem-
bling. Preprints, https://doi.org/10.20944/preprints202603.1152.v1, URL https://
doi.org/10.20944/preprints202603.1152.v1
Jiang Y, Ferraro F (2026) SCRIBE: Structured mid-level supervision f or tool-using
language models. URL https://arxiv.org/abs/2601.03555, arXiv:2601.03555
Johnson GA, Lewis RA, Nubbemeyer EI (2017a) Ghost ads: Improving the economic s
of measuring online ad eﬀectiveness. Journal of Marketing Research 54(6) :867–884
Johnson GA, Lewis RA, Nubbemeyer EI (2017b) The online display ad eﬀective ness
funnel: Lessons from 432 ﬁeld experiments. SSRN Working Paper 2701578
Kreuter B, et al (2023) Interoperable private attribution. IACR ePrin t 2023/437
Kumar A, et al (2020) CAMTA: Causal attention model for multi-touch attribution .
ArXiv preprint arXiv:2012.11403
K¨ unzel SR, Sekhon JS, Bickel PJ, et al (2019) Metalearners for estimati ng het-
erogeneous treatment eﬀects using machine learning. Proceedings of t he National
Academy of Sciences 116(10):4156–4165
Lai L, Cheng Z, Cheng K, et al (2026) Do transformers always win? an empirical
study of semantic embeddings for short-text e-commerce reviews. I n: 2026 9th Inter-
national Symposium on Big Data and Applied Statistics (ISBDAS), pp 525–529,
https://doi.org/10.1109/ISBDAS69350.2026.11484350
Leeﬂang PS, Wieringa JE, Bijmolt TH, et al (2009) Modeling markets: Analyzi ng mar-
keting phenomena and improving marketing decision making. Intern ational Journal
48

of Research in Marketing 26(3):131–150. https://doi.org/10.1016/j.ijresmar.2009.
05.005
Lewis RA, Rao JM (2015) The unfavorable economics of measuring the returns t o
advertising. Quarterly Journal of Economics 130(4):1941–1973
Li C, Chen Y, Leng C, et al (2024) Privacy-preserving conversion predicti on using
data clean rooms. In Proceedings of the 18th ACM Conference on Recommend er
Systems (RecSys). arXiv preprint arXiv:2505.14959
Li D, Jiang B, Huang L, et al (2025) From generation to judgment: Opportunities an d
challenges of LLM-as-a-judge. In: Proceedings of the 2025 Conference on Empi rical
Methods in Natural Language Processing, pp 2757–2791
Li X, Lu Y, Cao J, et al (2026a) CATCH: A modular cross-domain adaptive template
with hook. In: Bebis G, Ye J, Wang Y, et al (eds) Advances in Visual Com-
puting. Springer Nature Switzerland, Cham, pp 41–52, https://doi.org/10.1007/
978-3-032-14492-8 4
Li Y, Fan Z, Zhuang Z (2026b) When AUC 0.998 is not enough: A candidate eval-
uation protocol for hidden-state probes of indirect prompt injection i n multimodal
computer-use agents. URL https://arxiv.org/abs/2606.22864, arXiv:2606.22864
Lin L, Wang Y (2025) SHAP stability in credit risk management: A case study in
credit card default model. Risks 13(12):238. https://doi.org/10.3390/risks13120238
Lin L, You J, Li Y, et al (2026) Reﬂect-Guard: Enhancing LLM safeguards against
adversarial prompts via logical self-reﬂection. URL https://arxiv.org/abs /2605.
24834, arXiv:2605.24834
Lin T, Misra S (2022) The identity fragmentation bias. Marketing Science 41(3):433–
440
Liu J, Yang J, Li X, et al (2026a) Architecture matters more than scale: A comparati ve
study of retrieval and memory augmentation for ﬁnancial qa under sme compu te
constraints. URL https://arxiv.org/abs/2604.17979, arXiv:2604.17979
Liu M, Shi G (2024) PoliPrompt: A high-performance cost-eﬀective LLM-based text
classiﬁcation framework for political science. Available at SSRN 4940136, URL
https://ssrn.com/abstract=4940136
Liu M, Shi G (2025) Enhancing LLM-based text classiﬁcation in political scie nce:
Automatic prompt optimization and dynamic exemplar selection for few-sh ot
learning. URL https://arxiv.org/abs/2409.01466, arXiv:2409.01466
Liu Z, Padmanabhan K, Viswanathan S (2026b) DICE-DML: Deepfake-informed
double machine learning for visual ad eﬀects. ArXiv preprint arXiv:2603.02359
49

Lu Z, Kannan PK (2024) AI for customer journeys: A transformer approach. SSRN
Working Paper 4684617
McHugh ML (2012) Interrater reliability: The kappa statistic. Biochem ia Medica
22(3):276–282
Mehta K, Singhal E (2020) Marketing channel attribution modelling: Marko v
chain analysis. International Journal of Indian Culture and Business Man agement
21(1):63–77
Mulc T, Anderson B, Cubre C, et al (2025) NNN: Next-generation neural networks
for marketing measurement. ArXiv preprint arXiv:2504.06212
National Institute of Standards and Technology (2023) Artiﬁcial intelligence r isk man-
agement framework (AI RMF 1.0). Tech. Rep. AI 100-1, NIST, https://doi.org/10.
6028/NIST.AI.100-1
Ng E, Wang Z, Chen H, et al (2021) Orbit: Probabilistic forecast with exponen tial
smoothing. ArXiv preprint arXiv:2106.03322
Page MJ, McKenzie JE, Bossuyt PM, et al (2021) The PRISMA 2020 statement: An
updated guideline for reporting systematic reviews. BMJ 372:n71
Pauwels K, Silva-Risso J, Srinivasan S, et al (2004) New products, sales p romotions,
and ﬁrm value: The case of the automobile industry. Journal of Marketing 68( 4):142–
156. https://doi.org/10.1509/jmkg.68.4.142.42724
Qi Y, Zhao S, Xue Z, et al (2026) Detecting abnormal user feedback patterns
through temporal sentiment aggregation. URL https://arxiv.org/abs/2604.00020,
arXiv:2604.00020
Qian P, Wang S, Wang X, et al (2026) Relevant is not warranted: Evidence-force cal-
ibration for cited RAG. URL https://arxiv.org/abs/2605.28044, arXiv:2605.28044
Qin X, Li S, Cai Y, et al (2025) Enhancing counterfactual explanations with feasi bility
and diversity. In: 2025 IEEE International Conference on Data Mining Wor kshops
(ICDMW), IEEE, pp 2310–2319
Rust RT, Ambler T, Carpenter GS, et al (2004) Measuring marketing produ ctivity:
Current knowledge and future directions. Journal of Marketing 68(4):76–89. https:
//doi.org/10.1509/jmkg.68.4.76.42721
Shapiro BT, Hitsch GJ, Tuchman A, et al (2022) Advertising in the age of digi-
tal targeting: Meta-analysis with improved bias corrections. SSRN Work ing Paper
4293750
Shen B, Jin L, Cai H, et al (2026) The eﬃciency frontier: A uniﬁed framework for cost-
performance optimization in LLM context management. https://doi.org/10.48550/
50

arXiv.2605.23071, URL https://arxiv.org/abs/2605.23071, arXiv:2605.23071
Shi C, Pan R, Lo J, et al (2024a) A large-scale heterogeneous treatment eﬀect
estimation framework and its applications at Snap. ArXiv preprint arXiv:2512.03060
Shi G, Kan Z, Smucny J, et al (2024b) ChaosMining: A benchmark to evaluate pos t-
hoc local attribution methods in low-SNR environments. URL https: //arxiv.org/
abs/2406.12150, arXiv:2406.12150
Shi G, Yin J, Xie D, et al (2026) JailbreakOPT: Tool-assisted iterative jail break
prompt optimization. URL https://arxiv.org/abs/2606.11425, arXiv:2606.11425
Srinivasan S, Vanhuele M, Pauwels K (2010) Mind-set metrics in market r esponse
models: An integrative approach. Journal of Marketing Research 47(4):672–684.
https://doi.org/10.1509/jmkr.47.4.672
Sun J, et al (2025) IDUM: Invariant deep uplift modeling. In: Proceedin gs of the 42nd
International Conference on Machine Learning (ICML)
Sun Y, Wang Y, Jin Y, et al (2017) Geo-level Bayesian hierarchical media mix
modeling. Google Research
Tirumala S (2025) DeepCausalMMM: A deep learning framework for marketing mix
modeling with causal inference. ArXiv preprint arXiv:2510.13087
Varambally S, et al (2024) Discovering mixtures of structural causal mode ls from
time series data. In: Proceedings of the 41st International Conference on Machine
Learning (ICML)
W3C (2025) Privacy-preserving attribution: Level 1. W3C Working Draft, Apr il 2025
Wager S, Athey S (2018) Estimation and inference of heterogeneous treatment
eﬀects using random forests. Journal of the American Statistical Associ ation
113(523):1228–1242
Waisman C, Sahni NS, Nair HS, et al (2025) Parallel experimentation and competiti ve
interference on online advertising platforms. Marketing Science 44(2):437–456
Wang S, Qian P, Chen Y, et al (2026a) When safe skills collide: Measuring com-
positional risk in agent skill ecosystems. URL https://arxiv.org/abs/2606.00448,
arXiv:2606.00448
Wang Y, Sun X, Li Y, et al (2026b) Auditing and ﬁxing economic validity in
tabular foundation models for discrete choice. URL https://arxiv.org/abs/2605.
26559, iCML Workshop on Foundation Models for Structured Data (FMSD),
arXiv:2605.26559
51

Wang Y, Tang Y, Liu B, et al (2026c) When LLM reward design fails: Diagnostic-
driven reﬁnement for sparse structured RL. https://doi.org/10.48550/arXiv.2605.
28918, URL https://arxiv.org/abs/2605.28918, arXiv:2605.28918
Wang Y, Tang Y, Qian Y, et al (2026d) VisualLeakBench: Auditing the
fragility of large vision-language models against PII leakage and social enginee r-
ing. https://doi.org/10.48550/arXiv.2603.13385, URL https://arxiv.org/abs/2603.
13385, arXiv:2603.13385
Wang Z, Sun Y, Wang H, et al (2025) Reasoning-enhanced domain-adaptive pre-
training of multimodal large language models for short video content gover nance.
In: Potdar S, Rojas-Barahona L, Montella S (eds) Proceedings of the 2025 Con-
ference on Empirical Methods in Natural Language Processing: Industry T rack.
Association for Computational Linguistics, Suzhou (China), pp 1104–1112, https://
doi.org/10.18653/v1/2025.emnlp-industry.77, URL https://aclanthology.org/2025.
emnlp-industry.77/
Xiao C, Hou L (2026) Prototype-aligned federated soft-prompts for continual web
personalization. In: Proceedings of the ACM Web Conference 2026, pp 6743–6754
Xiao C, Dou J, Lin Z, et al (2026) From points to coalitions: Hierarchical contrasti ve
Shapley values for prioritizing data samples. In: Proceedings of the AAAI Conference
on Artiﬁcial Intelligence, pp 15995–16003
Xiao Y, Du H, Zhang Y, et al (2025) AdsBPC: Click without compromise—online ad
measurement via per-user diﬀerential privacy. In: IEEE Symposi um on Security and
Privacy, arXiv preprint arXiv:2406.02463
Xie T, Chen J, Yang Y, et al (2024) LossLens: Diagnostics for machine learning
through loss landscape visual analytics. IEEE Computer Graphics and Appl ications
45(2):112–125. https://doi.org/10.1109/MCG.2024.3520428
Xu N, Jiang Y, Dipta SR, et al (2026a) Learning how to use tools, not just when:
Pattern-aware tool-integrated reasoning. URL https://arxiv.org/abs/2509.23292,
arXiv:2509.23292
Xu R, Jiang L, Yu D, et al (2026b) SynHAT: A two-stage coarse-to-ﬁne diﬀusion
framework for synthesizing human activity traces. URL https://arxiv. org/abs/2604.
14705, arXiv:2604.14705
Yang D, Dyer K, Wang S (2020) DeepMTA: Interpretable deep learning mode l for
online multi-touch attribution. ArXiv preprint arXiv:2004.00384
Ye H, Chen S, Zhong Z, et al (2026) Seeing through the conﬂict: Transparent k nowl-
edge conﬂict handling in retrieval-augmented generation. In: Procee dings of the
AAAI Conference on Artiﬁcial Intelligence, pp 34423–34431
52

Ye Y, Xue P (2026) When attribution fails: Selection, targeting, and measurem ent in
real-time bidding advertising. SSRN working paper, March 30, 2026; https ://ssrn.
com/abstract=6530478
Yu D, Zhuang D, Jiang L, et al (2025) UQGNN: Uncertainty quantiﬁcation of
graph neural networks for multivariate spatiotemporal prediction. In: P roceedings
of the 33rd ACM International Conference on Advances in Geographic Informati on
Systems, pp 52–65
Zhan Y, Ben-Harush S, Zhu Y, et al (2024) Neural ODE for multi-channel attribu tion.
In: ICLR 2024 Workshop
Zhang S, Lin S, Wei X, et al (2026a) Small language model agents enable eﬃ-
cient and high-quality knowledge mining. URL https://arxiv.org/abs/2510.01427,
arXiv:2510.01427
Zhang Y, Wurm M, Wakim A, et al (2023) Bayesian hierarchical media mix model
incorporating reach and frequency data. Google Research
Zhang Y, Wurm M, Wakim A, et al (2024) Media mix model calibration with Baye sian
priors. Google Research
Zhang Y, Xiang Z, Xu H (2026b) Performance-eﬃciency trade-oﬀs in human pref-
erence prediction: A comparative study of traditional machine learnin g and large
language models. In: Proceedings of the 31st IEEE Symposium on Computers and
Communications (ISCC), IEEE, accepted; proceedings forthcoming
Zhao K, et al (2018) Shapley value methods for attribution modeling in onli ne
advertising. ArXiv preprint arXiv:1804.05327
Zhao K, et al (2024) M 3TN: Multi-gate mixture-of-experts for multi-treatment uplift
modeling. In: Proceedings of ICASSP 2024, arXiv preprint arXiv:2401.14426
Zhao S, Xue Z, Qi Y, et al (2026) Non-intrusive graph-based bot detection for e-
commerce using inductive graph neural networks. URL https://arxiv.or g/abs/2601.
22579, arXiv:2601.22579
53
