---
title: Measuring Curriculum-Labor Market Alignment at the Scale of a Program Portfolio
url: https://arxiv.org/abs/2608.12356
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Sherzod Turaev
- Saja Aldabet
- Mary John
- Namya Musthafa
- Mamoun Awad
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.12356
pages: 21
chars: 83516
fetched_at: '2026-11-08T13:05:11+00:00'
kb_version: 1
---

# Measuring Curriculum-Labor Market Alignment at the Scale of a Program Portfolio

MEASURINGCURRICULUM–LABORMARKETALIGNMENT AT
THESCALE OF APROGRAMPORTFOLIO
Sherzod Turaev1,∗ Saja Aldabet 1 Mary John 2 Namya Musthafa 3
Mamoun Awad 1 Nazar Zaki 1 Khaled Shuaib 4
1Department of Computer Science & Software Engineering, College of Information Technology,
United Arab Emirates University, Al Ain, United Arab Emirates
2Academic Support Department, Abu Dhabi Polytechnic, Abu Dhabi, United Arab Emirates
3Department of Electrical and Communication Engineering, College of Engineering,
United Arab Emirates University, Al Ain, United Arab Emirates
4Department of Information Systems and Security, College of Information Technology,
United Arab Emirates University, Al Ain, United Arab Emirates
∗Corresponding author:sherzod@uaeu.ac.ae
August 14, 2026
ABSTRACT
A college that offers several overlapping computing degrees implicitly assumes that its programs
are differentiated in line with the way the labor market segments computing work and that, taken
together, they prepare graduates for that market. Testing such an assumption is difficult, because the
instruments available to curriculum committees, namely advisory boards, graduate tracer studies,
and employer surveys, are slow, narrow, and hard to reproduce. In the current work, we apply
one uniform, taxonomy-anchored alignment analysis across all five undergraduate programs of a
College of Information Technology, comparing 1,922 course learning outcomes against 103,349
competencies extracted from a unified corpus of 5,186 deduplicated job openings drawn from four
boards. Every competency, on both sides, is obtained by agroundedsingle-language-model procedure
that copies it verbatim from the source and verifies it against the source, then assigned to one of
eleven ESCO-aligned domains and a Bloom cognitive level, and the curricular supply is read not as a
catalog but on arealized-attainmentbasis that respects the credit-hour and elective constraints under
which a student completes a degree. The extraction is validated blind by two independent faculty
raters (domain κ= 0.91 , Bloom level κ= 0.86 ) and the ESCO matching by a human-adjudicated
gold set (κ= 0.72 ). The analysis yields four findings. The content gaps are systemic rather than
program-specific, concentrated in systems, software engineering, security, and web development; the
shared college core satisfies only about a third of the demanded competencies; the programs are well
differentiated in disciplinary content yet homogeneous in where they fall short; and the curriculum is
aligned roughly a full Bloom level below the market across the portfolio, most acutely in systems.
We discuss the implications for program design, for curriculum governance, and for the practice of
curriculum analytics.
Keywords:computing education; curriculum analysis; curriculum–labor market alignment; program design; skills
taxonomy; large language models; ESCO; Bloom’s taxonomy.
1 Introduction
The relationship between what universities teach and what the labor market requires has long been a concern of
higher-education policy, and within computing it has become acute, because the field’s occupational categories multiply
arXiv:2608.12356v1  [cs.CY]  4 Jul 2026

APREPRINT- AUGUST14, 2026
and its tools turn over faster than the multi-year cycles on which curricula are revised (ACM/IEEE-CS/AAAI, 2020). A
computing program is, in effect, a standing premise that the competencies it cultivates will still command value by
the time its graduates enter the workforce. Where a college offers several computing degrees at once, the premise is
compounded by a second one, namely that the programs are differentiated from one another in a way that mirrors how
the labor market itself segments computing roles, so that a graduate of each program is prepared for a distinct slice of
the market rather than for an undifferentiated average of it.
The instruments on which institutions traditionally rely to examine these wagers, namely industry advisory boards,
graduate tracer studies, and employer satisfaction surveys, are valuable but inherently slow, narrow in coverage, and
difficult to reproduce across programs or over time. A decade of computational work has sought to supplement them by
mining curricular and labor-market text directly, and recent advances in large language models have made it possible
to extract structured competency records, anchored to standardized skill taxonomies, with a reliability that the earlier
lexical and shallow-semantic methods could not attain. A reference framework for such analysis, together with a
single-program proof of concept, has been established in prior work (Turaev et al., 2026a,b); that work, however,
diagnoses one program in isolation.
What has not been examined is theportfolio, that is, the full set of programs a college offers, analyzed as a system
against a common labor market with one uniform instrument. The portfolio is the level at which the governance
questions actually arise, because it is the college, and not the individual course, that decides which competencies
are guaranteed to every graduate through a shared core, which are reserved to program-specific majors, and how the
programs are meant to differ from one another. A study confined to a single program cannot speak to whether a gap
is peculiar to that program or shared across all of them, whether the common core carries its weight, or whether the
programs are differentiated in line with the market they collectively serve.
These governance choices are neither incidental nor easily reversed. A college must decide which competencies every
graduate will be guaranteed through the shared core and which will be localized in a particular major, how far the
sibling programs may overlap before differentiation collapses into redundancy, and how to weigh the breadth that
prepares a graduate for several adjacent roles against the depth that genuine specialization requires. Each such decision
is taken once and then binds a cohort for the several years of a degree, and each is made, in current practice, largely on
the basis of disciplinary tradition, accreditation requirements, and the periodic judgment of advisory boards, rather than
on a measured reading of how the programs together meet the market they serve. The portfolio is, in this sense, the
natural unit of curricular governance, and yet it is precisely the unit at which systematic evidence is scarcest.
A second consideration concerns what a curriculum delivers as opposed to what it lists. A published plan of study is an
inventory of opportunities rather than a record of attainment, because the general-education and elective requirements
that bulk out a catalog are satisfied by selecting a few courses from a much larger menu, so that no single graduate
encounters more than a fraction of what the catalog displays. A supply-versus-demand comparison that counts
every cataloged course equally therefore measures an idealized program that no student actually completes, and it
systematically overstates the breadth a degree can guarantee. Separating what a program offers from what a graduate is
assured of receiving is, we argue, a precondition for an honest alignment analysis, and it is the second thread the present
study develops.
In the current research, we take the college as the unit of analysis and apply one uniform, taxonomy-anchored alignment
instrument across all five undergraduate programs of a College of Information Technology, namely Computer Science,
Computer Engineering, Data Science and Artificial Intelligence, Information Security, and Information Technology. We
compare the competencies these programs develop against those demanded by a contemporaneous corpus of regional job
advertisements, on a common frame of eleven domains aligned to the European Skills, Competences, Qualifications and
Occupations (ESCO) taxonomy and five Bloom cognitive levels. One methodological choice distinguishes the analysis:
rather than counting every course in the catalog equally, we read the curricular supply on arealized-attainmentbasis
that respects the credit-hour and elective constraints under which a student completes a degree, so that the comparison
reflects what graduates actually attain rather than what the catalog nominally offers. We organize the study around four
questions: whether the curriculum–market gaps are systemic across the portfolio or specific to particular programs
(RQ1); how much of the market’s demand the shared college core satisfies on its own (RQ2); whether the programs are
differentiated in line with the market’s segmentation of computing roles (RQ3); and whether the curriculum is pitched
at the cognitive depth the market expects (RQ4).
The paper makes four contributions:
1. the first portfolio-scale alignment analysis of an entire college of computing programs, conducted with a single
uniform instrument so that programs are directly comparable rather than studied in isolation, and built on a
groundedextraction whose every competency is copied verbatim from its source and verified against it, with
the extraction and the ESCO matching independently validated;
2

APREPRINT- AUGUST14, 2026
2. arealized-attainmentscope model that weights the curricular supply by the credit-hour and elective constraints
of each program, correcting the catalog-level over-counting that would otherwise distort the supply–demand
comparison;
3. an empirical diagnosis of the College of Information Technology that establishes the gaps as systemic rather
than program-specific, quantifies the limited reach of the shared core, distinguishes content differentiation
from gap homogeneity across the programs, and measures a portfolio-wide cognitive-depth deficit; and
4. a reading of these results for curriculum governance, identifying where in the plan, and at what cognitive level,
each gap could be closed.
The remainder of the paper is organized as follows. The next section reviews related work in computing-education
curriculum design and computational curriculum–labor alignment and situates the present study. We then recap the
alignment framework and the competency formalism on which the analysis rests, before detailing the study design and
method, including the corpora, the grounded extraction, the taxonomic and cognitive anchoring, and the scope model.
The reliability of the extraction and of the ESCO matching is established next, after which the results are reported
around the four research questions, followed by a discussion of the implications for program design and governance,
the limitations of the study, and conclusions.
2 Background and Related Work
That graduate competencies and employer expectations diverge is among the more persistently documented concerns in
higher education, and the divergence is sharpest in computing. Labor-market analyses report that a substantial fraction
of workers’ core skills will change within a few years and that employers identify the skills gap as a leading barrier to
growth (World Economic Forum, 2025), while the automation of routine cognitive work continues to reshape which
competencies retain value (Frey and Osborne, 2017). Within computing and software engineering specifically, studies
have repeatedly documented a gap between what programs cultivate and what industry expects, in both technical and
professional competencies (Garousi et al., 2020; Radermacher and Walia, 2013). The difficulty is structural rather
than incidental: universities revise curricula on multi-year cycles, whereas the competencies the market rewards shift
continuously, so that even a well-designed program drifts out of alignment between revisions.
Computing-education practice has long sought to manage this through outcome- and competency-oriented curriculum
design. The ACM and IEEE Computer Society curricular guidelines, culminating in the competency-based CC2020
framework (ACM/IEEE-CS/AAAI, 2020), define what graduates should know and be able to do, and accreditation
regimes require programs to specify measurable student outcomes and to demonstrate their attainment (ABET, 2024),
with national qualifications frameworks situating each degree at a defined level of competence. These practices rest
on a longer tradition of outcome-based education (Spady, 1994) and of constructive alignment between intended
outcomes, learning activities, and assessment (Biggs and Tang, 2011), in which the cognitive demand of an outcome is
conventionally expressed on the revised Bloom taxonomy (Anderson and Krathwohl, 2001). Valuable as they are for
internal coherence and disciplinary conformance, these instruments specify what a program intends; they do not, on
their own, measure or track how well those intentions match a labor market that changes faster than the curricular cycle.
The discipline does not, moreover, present itself as a single curriculum. The ACM and IEEE Computer Society overview
frames computing as a family of related but distinct disciplines, each governed by its own curricular volume, so that
separate guidelines now exist for computer science (ACM/IEEE-CS/AAAI, 2024), computer engineering (ACM/IEEE-
CS, 2016), information technology (ACM/IEEE-CS, 2017), cybersecurity (Joint Task Force on Cybersecurity Education,
2017), and, most recently, the computing competencies of data science (ACM Data Science Task Force, 2021), under
the common umbrella of CC2020 (ACM/IEEE-CS/AAAI, 2020). A college that offers degrees across this family is
therefore not replicating one program under several names but instantiating several disciplinary specifications that
overlap by design in a shared computing core and diverge in their majors. This disciplinary differentiation is the
curricular counterpart of the labor market’s own segmentation of computing roles, and it is what renders the question of
whether a portfolio’s programs are differentiated in line with the market both well posed and answerable, since the
guidelines establish what each program is meant to emphasize while the market establishes what each corresponding
family of roles demands.
A separate body of work, drawn from the measurement tradition in education rather than from computing, bears directly
on how the curricular side of such a comparison ought to be read. Research on theopportunity to learn, originating in
Carroll’s model of school learning (Carroll, 1963) and developed through the large international curriculum studies,
distinguishes theintendedcurriculum that appears in official documents from theimplementedcurriculum that is actually
taught and theattainedcurriculum that students ultimately acquire (Travers and Westbury, 1989). The distinction is
consequential because the three rarely coincide, and treating the intended curriculum as though it were the attained
one inflates any estimate of what graduates know (McDonnell, 1995); the same concern animates the methodological
3

APREPRINT- AUGUST14, 2026
literature on measuring the content actually delivered rather than its nominal description (Porter, 2002), in content and
in the cognitive depth at which it is pitched, the latter conventionally expressed on the revised Bloom taxonomy and
central to the constructive-alignment tradition (Anderson and Krathwohl, 2001; Biggs and Tang, 2011). A program’s
published plan of study is an intended curriculum in exactly this sense, and the elective and general-education structures
that pad a catalog widen the gap between what is offered and what any one graduate attains. We take this distinction as
the conceptual basis for the opportunity–attainment scope model developed below, which reads the curricular supply
not as a catalog but on the realized-attainment basis that the opportunity-to-learn tradition prescribes.
A complementary, computational line of work measures that match directly by mining curricular and labor-market text.
Early efforts applied keyword and topic-model comparisons to job postings and course catalogs (Piróg and Hibszer,
2024; Almgerbi et al., 2022; Gürcan and Cagiltay, 2019); a second wave added supervised classification, named-entity
recognition, and taxonomy grounding to extract skills more precisely (Karakolis et al., 2022; Spada et al., 2022;
Gnehm et al., 2022; Zhang et al., 2022; Decorte et al., 2023); and a third has begun to apply large language models to
schema-constrained competency extraction (Jaiswal et al., 2025; Zamecnik et al., 2024; Xu et al., 2025). A smaller set
of studies turns the analysis explicitly toward curriculum design, contrasting the skills taught with the skills sought
(Föll et al., 2018; Ahadi et al., 2022; Aljohani et al., 2022). The full trajectory, and the methodological limitations
that motivated the reference framework adopted here, are surveyed in Turaev et al. (2026a), whose single-program
instantiation is reported by Turaev et al. (2026b). What this body of work shares, with few exceptions, is its unit of
analysis: it diagnoses one program, or one occupational slice, in isolation.
Common to the more reliable of these efforts is a standardized skills taxonomy that renders the heterogeneous vocabulary
of curricula and the market commensurable. The European ESCO classification (European Commission, 2021), the
United States O*NET system (National Center for O*NET Development, 2026), and the Skills Framework for the
Information Age (SFIA Foundation, 2026) each supply such a reference vocabulary; we adopt ESCO, for the reasons
set out in the framework, as the normalization anchor against which both sides of the comparison are mapped.
The portfolio scale has accordingly remained unexamined. A college of computing offers not a single degree but a
family of related programs that share a common core, partition the discipline among their majors, and are intended,
collectively, to span the computing labor market; the decisions that govern this arrangement, namely which competencies
to guarantee to every graduate, which to localize in a particular program, and how the programs should differ from
one another, are made at the level of the portfolio rather than the individual course. A single-program study, however
carefully conducted, cannot determine whether a diagnosed gap is idiosyncratic to one program or common to all,
whether the shared core carries its weight, or whether the programs are differentiated in a manner that matches the
market’s own segmentation of computing roles. Answering these questions requires that every program be measured
with one and the same instrument, against one and the same labor market, and on a basis that reflects what graduates
actually attain rather than what each catalog nominally lists. In the current research, we supply such an analysis,
applying a uniform, taxonomy-anchored instrument across an entire undergraduate computing portfolio and reading the
curricular supply through the realized-attainment scope model developed in the next sections.
3 The Alignment Framework
This study operationalizes the reference framework introduced in Turaev et al. (2026a) and first instantiated, for a single
program, by Turaev et al. (2026b); we recapitulate here only what is needed to make the present portfolio-scale analysis
self-contained, and we refer the reader to those works for the full formal development. The framework represents
every curricular and labor-market requirement as a structured competency record carrying adomain, drawn from ten
ESCO-aligned computing domains augmented by a transversal-skills category; alevel, encoding cognitive depth on
a five-point ordinal scale derived from the revised Bloom taxonomy (Anderson and Krathwohl, 2001); andevidence,
tying the record to the source passage that produced it, so that every downstream finding remains traceable to the text.
Where the pilot populated a seven-slot record by a two-model ensemble, the present work obtains the record by the
groundedsingle-model extraction detailed in Section 4, which copies each competency verbatim from the source and
verifies it against the source, so that the evidence is a grounding guarantee rather than a post-hoc confidence score and
the analysis turns on thedomainandlevelthe record carries. Curricular competencies constitute thesupplyinventory
and labor-market competencies thedemandinventory, and the relationship between them is quantified along three
dimensions, namelycoverage, the proportion of demanded competencies for which the curriculum offers a sufficiently
similar counterpart; thecognitive-depth differential, the signed difference between the level at which a competency is
taught and the level at which it is demanded; andtemporal lag, the delay between a competency’s first appearance in the
labor market and its subsequent incorporation into the curriculum. The ESCO taxonomy (European Commission, 2021)
serves throughout as thenormalization anchoragainst which both inventories are mapped before they are compared,
which renders competencies expressed in different registers and institutional conventions commensurable. Whereas the
pilot established the feasibility of this machinery on a single program, the contribution of the present work is to apply it
4

APREPRINT- AUGUST14, 2026
uniformly across an entire college, on a grounded and independently validated extraction, and to add the cognitive and
curricular instrumentation that a portfolio-scale, governance-oriented analysis requires.
4 Study Design and Method
As a case study that applies the portfolio-alignment framework to one institution, the study extends the single-program
pilot to the complete undergraduate portfolio of a College of Information Technology at a public research university,
comprising five accredited Bachelor of Science programs, namely Computer Science, Computer Engineering, Data
Science and Artificial Intelligence, Information Security, and Information Technology. The method proceeds in five
stages (Figure 1), namely the construction of a curricular supply inventory and a unified labor-market demand inventory;
thegroundedextraction of competencies from each inventory; the anchoring of every competency to an ESCO domain
and to a cognitive level on the revised Bloom taxonomy; an opportunity–attainment scope model that reconciles the
catalog breadth of each program with the credit-hour and elective constraints under which a graduate realizes it; and the
taxonomy-anchored alignment computation that compares the two sides. We describe each stage in turn, and we make
the extraction stage, which departs most from the pilot, the subject of the most detailed treatment.
4.1 The Curricular Supply and the Labor-Market Demand
The supply inventory is assembled from the complete curricular record of the five programs, rather than from the
computing core alone, so that the portfolio is represented as students actually encounter it. Each program organizes its
courses into curricular blocks, namely general education, college (computing) requirements, major requirements, major
or specialization electives, supporting-requirement groups, and an internship, and the programs share a substantial
college-requirement core while differing in their major requirements and electives. Every course contributes its intended
learning outcomes, and eachcourse learning outcome(CLO) becomes the atomic unit of the supply side, which
preserves the granularity at which a curriculum committee actually acts and yields a supply inventory of 1,922 CLOs
across the five programs. The decision to treat the CLO as the unit is consequential for what follows: a single outcome
corresponds to a single competency, so that the supply inventory neither fragments an outcome into disconnected
phrases nor merges several outcomes into one.
The demand inventory is assembled from contemporaneous online job advertisements within the national and regional
labor market, filtered by occupation family, namely the group of advertised roles whose discipline corresponds to one
of the five programs. Because no single job board offers either complete or unbiased coverage of a regional market,
we draw postings from four sources, namely a general aggregator and three regional boards, and we combine them
into one corpus. A naive union, however, would overstate demand, since a single opening is frequently cross-posted
to several boards and the same role is re-advertised over time, and counting such duplicates would inflate precisely
the applied-skill domains that the high-volume boards favor. We thereforededuplicatethe union to unique openings,
collapsing postings that share an employer and a job title (with a description guard for the rare case of an empty
employer field) and retaining a single representative per opening together with the list of boards on which it appeared.
The union of 6,563 postings reduces in this way to 5,186 unique openings, of which 865 had been posted more than
once, and it is this deduplicated corpus, rather than any single source, that constitutes the demand side of the analysis.
4.2 Grounded Competency Extraction
Extracting a structured competency from a course outcome or a job advertisement with a large language model is
reliable only to the extent that the model reports what the source says rather than what it expects a plausible source to
say. A model asked to summarize the competencies in a passage may paraphrase a requirement into a skill the text does
not contain, may supply a governing verb the source omits, or may import competencies that are conventional for the
role but absent from the posting, and each such liberty contaminates a downstream coverage or depth measurement
in a way that is difficult to detect after the fact. The pilot bounded these risks with a two-model ensemble whose
disagreements were flagged for adjudication. To overcome the residual fabrication risk and the cost and complexity that
a second extractor entails, the present work adopts agroundedextraction procedure built on a single large language
model (Claude Opus 4.8) whose every output is verified against the source by deterministic, model-free machinery.
The procedure proceeds in three steps. In theidentifystep, one call to the language model reads the source and returns
each competency as a span copiedverbatimfrom it, under an instruction to copy character-for-character and to add
neither a verb nor an object that the source lacks; in parallel, a deterministic gazetteer tagger marks every occurrence of
a curricular-topic or labor-market skill term, supplying a model-independent anchor. In thegroundstep, a grounding
gate rejects any returned span that cannot be located in the source, so that a competency that survives is, by construction,
present in the text that produced it; across the corpus the gate admits the extractions at full grounding, and no action
5

APREPRINT- AUGUST14, 2026
Curricular supply
1,922 CLOs · 5 programs
Labor-market demand
5,186 openings · 4 boards
Grounded extraction
Identify→Ground→Label · verbatim spans
ESCO domain
11 ESCO domains
Bloom cognitive level
5-point scale · verb table
Opportunity–attainment scope model
floor · expected · ceiling weights
Alignment computation
coverage · cognitive-depth differential · pillar-aware matching
Four findings (RQ1–RQ4)
systemic gaps · shared-core reach · differentiation · depth deficit
Stage 1
Stage 2
Stage 3
Stage 4
Stage 5
Validation
Blind IRR
domainκ= 0.91
levelκ= 0.86
ESCO gold
matchingκ= 0.72
Grounding gate
verbatim spans only
Figure 1: Overview of the portfolio-scale alignment method. The pipeline proceeds in five stages, from the curricular
supply and the unified labor-market demand inventories (Stage 1), through the grounded extraction of verbatim
competencies (Stage 2) and their anchoring to an ESCO domain and a Bloom cognitive level (Stage 3), to the
opportunity–attainment scope model (Stage 4) and the taxonomy-anchored alignment computation (Stage 5), which
together yield the four findings. The dashed panel summarizes the independent validation that underwrites the
records, namely the blind inter-rater reliability of the extraction, the human-adjudicated ESCO matching gold, and the
deterministic grounding gate.
verb is ever introduced that the source did not contain. In thelabelstep, the grammaticalflavorof each competency,
namely whether it states an action the graduate performs or a possession such as knowledge or a credential, and the
governing source verb where one exists, are read deterministically from the span. A course learning outcome, being
a single self-contained statement, yields exactly one competency, whereas a job advertisement yields several; on the
demand side, where postings rarely state a performance verb, the majority of competencies are possessions for which
no cognitive level can be honestly assigned, a property we record rather than impute.
4.3 Taxonomic and Cognitive Anchoring
Two reference spaces anchor every competency, one for what it concerns and one for the cognitive depth at which
it is taught or demanded. For the semantic dimension, each competency is assigned to one of ten ESCO-aligned
computing domains augmented by a transversal-skills category. The language model proposes the domain from the
6

APREPRINT- AUGUST14, 2026
Table 1: Per-program elective model used by the expected scope: the number of mandatory (guaranteed) general-
education courses, the general-education elective selection (sg slots from a pool of |Mg| courses), and the major or
specialization elective baskets (sg of |Mg|). Each elective course carries expected weight π=s g/|Mg|; mandatory
courses carry one.
Program Mandatory gen-ed Gen-ed electives g/|Mg|Major/spec. electives g/|Mg|
Computer Science 4 3/41 major 4/10
Computer Engineering 5 2/39 major 4/12
Data Science & AI 4 3/41 specialization 3/5, supporting 3/5
Information Security 4 † 2/40 major 2/5
Information Technology 4 3/40 major 3/6
†Plus one mandatory theme satisfied by a choice of one of two equivalent courses, guaranteed at the theme level.
competency in context, and a set of deterministic, re-runnable conventions then reconciles the proposal so that boundary
cases are treated uniformly across the whole corpus rather than left to the model’s case-by-case judgment: foundation
mathematics and statistics courses are fixed by course-code rule; outcomes namingdata structuresare placed in
Programming and Software Development while those naming analgorithmorrecursionare placed in Algorithms and
Computational Theory; cryptographic content remains in Cybersecurity and Ethics even when it names an algorithm;
and an outcome concerning the societal or ethical dimension of artificial intelligence is routed to Artificial Intelligence
and Data Science when it belongs to an AI course and to Cybersecurity and Ethics otherwise. Separating the extraction
of a competency from its typing in this way allows a convention to be revised and the entire inventory re-typed in
seconds, without any further call to the model.
For the cognitive dimension, each competency is leveled by its governing verb against a verb-to-level table on the
five-point scale of the revised Bloom taxonomy, in which Analyze and Evaluate are collapsed into a single level. The
table is a faithful transcription of the computing-specific verb lists published by the ACM Committee for Computing
Education in Community Colleges (Bamkole et al., 2023), supplemented by the canonical action verbs of Anderson
and Krathwohl (2001), and where the two sources place a verb at different levels we follow the computing-specific
assignment, so that, for example,buildandproduceare treated as application rather than creation whiledesignand
developremain creation. A small number of verbs are genuinely polysemous in a way the object resolves:buildand
produceare leveled as creation when their object is a whole, novel artifact such as a system, a model, or a program,
and as application otherwise. Competencies whose verb falls outside the cognitive taxonomy, principally the affective
and dispositional verbs that Bloom’s cognitive domain does not cover, and possession competencies that state no verb
at all, are recorded as having no assigned level rather than forced onto the scale. The ESCO taxonomy (European
Commission, 2021), rebuilt for this study from its official release and partitioned into its knowledge and skill pillars,
serves throughout as the normalization anchor against which both inventories are mapped before they are compared.
4.4 The Opportunity–Attainment Scope Model
A portfolio analysis that counted every catalog course equally would misrepresent what a graduate attains, because the
general-education and elective requirements are satisfied by selecting a small number of courses from a much larger
menu. We therefore characterize the supply inventory under three scopes: thefloorcounts only the courses every
graduate is required to take; theceilingcounts the entire catalog; and theexpectedscope weights each elective course
by the probability that a graduate completes it under the program’s own elective model, namely the number of slots
divided by the size of the menu from which they are drawn. The difference between floor and ceiling, which we term
theopportunity–attainment gap, measures how much of a program’s apparent coverage is guaranteed to its graduates
rather than left contingent on elective choice. The formal development of the weighting, its normalization, and its
verification against each program’s prescribed credit-hour load generalize the single-program derivation of the pilot
and are recapitulated in Appendix A; Table 1 lists the slot counts and menu sizes for the five programs. The effect
is substantial: across the portfolio the transversal-skills share of the supply falls from 58.8% at the catalog ceiling to
27.8% at the guaranteed floor, so that nearly half of the apparent general-education breadth is contingent on elective
choice rather than assured (Figure 2).
4.5 The Alignment Computation
With both inventories anchored to ESCO, the alignment is computed as apillar-awarematch: the object of a competency
is matched against ESCO knowledge concepts and the full action clause against ESCO skill and competence concepts,
which respects the taxonomy’s own division of labor between what is known and what is done. A competency is
7

APREPRINT- AUGUST14, 2026
floor (guaranteed) expected (graduate) ceiling (catalog)
0%
10%
20%
30%
40%
50%
60%
70%
CE CS DSAI IS IT College
Figure 2: Transversal-skills share of the curricular supply under the floor (guaranteed), expected (graduate), and ceiling
(catalog) scopes, by program and pooled. The catalog roughly doubles the transversal share relative to what a graduate
is guaranteed (College: 58.8% ceiling against 27.8% floor). Programs: CE (Computer Engineering), CS (Computer
Science), DSAI (Data Science and Artificial Intelligence), IS (Information Security), IT (Information Technology).
counted as covering an ESCO concept when their similarity attains a threshold, and per domain we report the supply
coverage, the demand coverage, and the demand-minus-supply gap. Because the similarity function and the operating
threshold are themselves methodological choices, we do not assume them: the embedding model used for matching,
and the distinct model used to refine the domain assignment, were each selected by a task-grounded comparison rather
than by reputation, and the coverage threshold is calibrated so that supply coverage attains a reference operating point,
with the gap then read at that matched coverage and its sensitivity reported. Matching against the concept label, rather
than its longer description, keeps the coverage measure discriminative, since a competency clause embedded against a
verbose description saturates the similarity at a low threshold.
4.6 Reliability and Validation
The reliability of the analysis is established on the extraction and the matching independently of the demand corpus.
The grounded extraction isfaithfulby construction, in that every competency is verified against its source and no
governing verb is invented; this is a property of the procedure rather than an estimate. Itsaccuracy, namely whether the
assigned domain and level are correct, is assessed by a blind validation in which two independent raters are shown only
a competency and its highlighted source and assign the domain and the level themselves, without sighting the model’s
answer, so that the agreement between raters and the agreement between each rater and the model are both free of the
anchoring that a confirmatory “is this correct” design would introduce; reliability is reported as Krippendorff’s alpha
and chance-corrected κ coefficients, and the sample deliberately oversamples the hard cases, namely boundary and
multi-domain outcomes, multi-verb outcomes, and the verbless possessions, so that accuracy is reported separately
for clear and for hard items rather than dominated by trivial ones. The matching is validated by a separate technique-
selection gold set of human-adjudicated competency-to-ESCO pairs, against which the candidate matchers are scored,
so that the matcher adopted for the analysis is the one that best reproduces human judgment on this task. The agreement,
effect-size, multiplicity, and uncertainty measures used throughout are defined in Appendix B.
4.7 Ethics and Research Integrity
The blind validation reported in Section 5 involved human raters, who coded competency records under a voluntary and
informed protocol, with their responses anonymized before analysis. The labor-market corpus comprises publicly posted
job advertisements, which contain no personal data of identifiable individuals, and no posting is reproduced in a form
8

APREPRINT- AUGUST14, 2026
Table 2: Inter-rater reliability between two independent, blind raters over 300 competencies. Confidence intervals are
3,000-sample bootstrap. Validity is reported with prevalence-robust coefficients owing to the skewed marginal.
Attribute % agree CohenκWeightedκPABAK /AC 1 95%CI (κ)
Validity (genuine competency) 0.953 0.444 — 0.907 / 0.949[0.18,0.67]
Domain (11 ESCO categories) 0.930 0.912 — 0.924 (AC 1)[0.88,0.95]
Bloom level (1–5 + no-level) 0.887 0.858 — 0.865 (AC 1)[0.81,0.90]
Bloom level (numeric 1–5) 0.939 0.919 0.877 (quad.) —[0.79,0.95]
Table 3: Accuracy of the extraction against the blind human consensus (the cards on which both raters agree), with
Wilson 95% intervals reported in the supplementary analysis. Domain and level accuracy are computed on the
agreed-domain and agreed-level subsets respectively.
SubsetnValidity Domain Bloom level
Random (representative) 150 1.00 1.00 1.00
Hard (stress test) 150 0.96 0.98 0.96
Supply (curriculum) 150 1.00 0.99 1.00
Demand (labor market) 150 0.96 0.99 0.96
Overall 300 0.98 0.99 0.99
that could identify an employer or applicant. A generative language model was employed as an analytical instrument
for theidentifystep of the extraction only, and its every output was verified against the source by the deterministic
grounding gate and further subjected to the blind human validation, so that no finding rests on an unverified model
assertion, consistent with ACM’s policy on the use of generative artificial intelligence in scholarly work.
5 Reliability of the Extraction
The reliability of the structured extraction was established along two complementary axes, namely the agreement
between independent human raters on how a competency should be coded and the agreement between the automated
extraction and the human consensus, both assessed under ablindprotocol designed to remove the confirmation bias that
a verify-the-system’s-answer design would introduce. Two faculty raters independently coded a stratified sample of
three hundred competencies, one hundred fifty drawn at random and one hundred fifty drawn deliberately from the
hard cases, namely boundary and multi-domain outcomes, outcomes governed by more than one verb, and the verbless
possessions that dominate job advertisements, with each rater assigning the ESCO domain and the Bloom level from
the competency and its highlighted source alone, without sight of the model’s assignment or of the other rater’s coding.
Table 2 reports the inter-rater reliability. The raters agree on the eleven-way domain assignment at a Cohen’s κ of
0.912 and on the cognitive level at a κ of 0.858, both of which fall in the range conventionally read as almost-perfect
agreement, and on the numeric Bloom levels alone the agreement is 93.9% exact with a quadratic-weighted κ of 0.877.
The validity judgment returns a high raw agreement of 0.953 but a modest κ of 0.444, a discrepancy that reflects the
well-documented behavior of the κ statistic under a skewed marginal rather than unreliable coding: because nearly
every extracted unit is in fact a genuine competency, the chance correction thatκ applies is large, so the prevalence-
and bias-adjusted coefficient (PABAK = 0.907) and Gwet’s AC1 (0.949), both robust to such skew, give the faithful
picture of near-perfect agreement on validity (Feinstein and Cicchetti, 1990; Gwet, 2008).
Table 3 reports the accuracy of the extraction against the human consensus, computed on the cards for which the two
raters agree and therefore furnish a defensible ground truth. The extraction is correct on 98% of validity judgments,
99% of domain assignments, and 99% of cognitive levels overall; it is essentially perfect on the random stratum and
holds between 96% and 99% on the deliberately hard stratum and on the demand side, where the residual error is
concentrated in a small number of boilerplate advertisement phrases that the raters jointly declined to treat as discrete
competencies. Because the raters coded blind to the model, this accuracy is free of the anchoring that a confirmatory
design would introduce, and the hard-case stratum, on which the accuracy barely declines, furnishes a conservative
stress test rather than a best-case estimate.
Figure 3 summarizes the two together, the blind inter-rater reliability and the model’s accuracy across the random and
hard strata.
The residual disagreement, modest as it is, was not diffuse but concentrated on two interpretable boundaries. On
the domain, the divergences fell almost entirely on the line between the transversal and the technical reading of a
9

APREPRINT- AUGUST14, 2026
validity domain level (groups in (b): Random / Hard strata)
0.0
0.2
0.4
0.6
0.8
1.0
0.91
Validity (PABAK)
0.91
Domain (κ)
0.86
Bloom level (κ)
(a) inter-rater reliability (n=300)
0.0
0.2
0.4
0.6
0.8
1.0 1.00 1.00 1.00
Random
0.96 0.98 0.96
Hard
(b) accuracy vs. consensus
Figure 3: Blind extraction validation. Left: inter-rater reliability on validity (PABAK), domain (Cohen’s κ), and Bloom
level (Cohen’s κ); the dashed line marks the almost-perfect threshold. Right: extraction accuracy against the human
consensus on the random and hard strata.
competency, and in particular on foundational mathematics courses and on outcomes framed by a communication
verb, where one rater coded an outcome such ascommunicate the results of an applied linear-algebra computation
by its framing and the other, with the model, by its subject matter. On the cognitive level, the few large gaps arose on
multi-verb outcomes, where leveling by the leading verb, the convention the extraction adopts, parts company with
leveling by the highest-order verb that the same outcome also contains, as indefine and formulateoridentify and
implement. In both cases the automated assignment fell within the range of competent human variation rather than
outside it, which is the property a reliability analysis seeks to establish; we note the leading-verb convention as a
deliberate and reproducible choice rather than a neutral one, and return to its consequences among the limitations.
Together with the procedural faithfulness of the grounded extractor, which admits no span absent from the source and
invents no governing verb, these results establish that the competency records on which the portfolio analysis rests are
both reliably coded and accurately typed. The validation of the supply-to-demandmatching, by which competencies
are aligned to ESCO concepts, was conducted on the same blind, independent basis. From a matcher-neutral pool
of candidate skill-to-concept pairs, the union of the top candidates proposed by every matching technique under
consideration, two raters independently judged three hundred pairs as matching or not, agreeing at a Cohen’s κ of
0.718, the substantial agreement expected of a semantic-equivalence judgment that is inherently more interpretive
than a domain or level assignment; the residual disagreement was itself principled, turning on how much credit a
broad, transversal ESCO concept should receive for a specific technical skill. Against the resulting consensus gold
of two hundred fifty-eight pairs, the candidate techniques were scored on a held-out split, and a general-purpose
sentence embedder (GTE-large) attained the highest F1 of 0.718, narrowly ahead of a cross-encoder reranker and of
the multilingual embedder used by the pilot (BGE-M3); this embedder, which also serves the domain refinement, is
therefore adopted for the alignment, and we report the coverage analysis under it with the next-best embedder as a
robustness comparison.
6 Results
The demand side of the analysis is the unified labor-market corpus, in which the postings collected from a general
aggregator and three regional boards are merged and reduced to 5,186 unique openings, from which 103,349 compe-
tencies are extracted; the supply side is the curricular census of 1,922 course learning outcomes. We report the four
research questions in turn.
10

APREPRINT- AUGUST14, 2026
Table 4: Domain composition of supply and demand and the demand-to-supply representation ratio (a ratio above one
marks under-supply). Cramér’sV= 0.213.
Domain Supply % Demand % D:S Status
Software Engineering & Project Mgmt 3.1 12.5 4.00 under-supplied
Systems & Infrastructure 4.9 15.3 3.11 under-supplied
Web & Mobile Development 1.4 3.6 2.69 under-supplied
Cybersecurity & Ethics 6.6 9.9 1.50 under-supplied
HCI & Design 0.9 0.9 1.01 aligned
Emerging Technologies 0.8 0.8 1.01 aligned
Artificial Intelligence & Data Science 9.3 8.9 0.95 aligned
Programming & Software Development 3.5 3.3 0.95 aligned
Computer Architecture & Hardware 2.0 1.5 0.76 over-supplied
General & Transversal Skills 58.8 43.1 0.73 over-supplied
Algorithms & Computational Theory 8.7 0.2 0.02 over-supplied
supply share demand share
0% 10% 20% 30% 40% 50% 60%
Software Eng. & PM
Systems & Infrastructure
Web & Mobile
Cybersecurity & Ethics
HCI & Design
Emerging Technologies
AI & Data Science
Programming & Software
Computer Arch. & HW
General & Transversal
Algorithms & Theory
Figure 4: Supply and demand domain composition: each domain’s share of the curricular supply against its share of
labor-market demand, ordered by the demand-to-supply gap. The applied domains (systems, software engineering, web,
security) are demanded far more than supplied; Algorithms and general-education breadth are over-represented.
6.1 The content gaps are systemic, not program-specific (RQ1)
Projecting both inventories onto the eleven ESCO domains and comparing their compositional shares locates where
the portfolio’s attention diverges from the market’s. The two compositions differ substantially (Cramér’sV= 0.213 ),
and the divergence is not uniform but concentrated, as Table 4 shows. The market demands competencies in Software
Engineering and Project Management at four times the rate at which the curriculum supplies them, in Systems and
Infrastructure at three times, and in Web and Mobile Development and in Cybersecurity at roughly two-and-a-half and
one-and-a-half times. The curriculum, conversely, over-invests relative to demand in General and Transversal skills and,
most strikingly, in Algorithms and Computational Theory, which accounts for8.7% of the curricular supply against
0.2% of market demand, a representation ratio (a domain’s share of demand divided by its share of supply) of0.02. The
under-supplied domains are precisely the applied and professional ones rather than the foundational ones, and because
they are thin in the shared structure that every program inherits, the shortfall is systemic across the portfolio rather than
peculiar to any single program, a reading that the program-level analysis of RQ3 makes precise.
11

APREPRINT- AUGUST14, 2026
supply coverage demand coverage
0% 25% 50% 75% 100%
General & Transversal
AI & Data Science
Software Eng. & PM
Cybersecurity & Ethics
HCI & Design
Computer Arch. & HW
Systems & Infrastructure
Programming & Software
Web & Mobile
Algorithms & Theory
Emerging Technologies
full portfolio (mean gap 0.44)
0% 25% 50% 75% 100%
General & Transversal
Software Eng. & PM
AI & Data Science
Computer Arch. & HW
Algorithms & Theory
Programming & Software
HCI & Design
Systems & Infrastructure
Cybersecurity & Ethics
Web & Mobile
Emerging Technologies
shared core (mean gap 0.63)
Figure 5: ESCO-concept coverage per domain, supply versus demand, for the full portfolio (left) and the shared college
core (right), under the validated matcher. Demand coverage is near-complete; the deficit is the unfilled supply coverage,
concentrated in the applied and theory domains and most severe in the shared core.
6.2 The shared core is necessary but far from sufficient (RQ2)
Aligning each side to ESCO and measuring, per domain, the share of demanded concepts the curriculum covers,
the full portfolio covers 46% of the demanded competency breadth, leaving a mean content-gap of 0.44; the deficit
is widest in Emerging Technologies ( 0.74), Programming, Algorithms, and Web ( 0.57 each), and Systems ( 0.51),
and narrowest in General (0.18) and Artificial Intelligence (0.20). Restricted to the shared college-requirement core,
namely the college-requirement courses common to all five programs that every graduate completes, coverage falls
to 0.31 and the gap widens to 0.63, with the applied domains all but absent, Emerging Technologies ( 0.88), Web
(0.86), Cybersecurity ( 0.83), Systems ( 0.72), HCI ( 0.71), and Programming ( 0.70). The shared core thus delivers
the foundational and transversal competencies it is designed to guarantee while leaving the applied, market-facing
breadth to the program-specific majors. These figures are read at the operating point where supply coverage matches
the reference value, and they are stable under the alternative embedder (full-portfolio mean gap 0.48, shared-core gap
0.64), so the finding does not depend on the matcher even though the finer per-domain ordering does. Figure 5 shows
the per-domain supply and demand coverage for the full portfolio and the shared core.
6.3 Differentiation in content, homogeneity in shortfall (RQ3)
The five programs are genuinely differentiated where differentiation is meant to live. On the full realized curriculum
their pairwise domain-profile similarity is high (cos = 0.835), reflecting the large shared core, but on the major blocks
alone it falls to 0.535, confirming that the programs diverge in their specializations. Each program’s supply profile is,
moreover, closest to its own occupation family’s demand profile more often than not (own-family cosine0.88 against
0.722 off-diagonal), though two of the five, Computer Science and Information Technology, sit nearest the Computer
Engineering family, an artifact of the heavily shared computing core. The programs are therefore differentiated in
disciplinary content while remaining homogeneous in where they fall short of the market, which is what makes the
RQ1 gaps systemic: the under-supplied applied domains are missing from all five programs alike, not localized to
one. Figure 6 shows the program-by-family alignment and the drop in program-to-program similarity from the full
curriculum to the majors.
6.4 A portfolio-wide cognitive-depth deficit (RQ4)
Beyond which competencies are taught lies the question of how deeply. Across the portfolio the curriculum is pitched
at a mean Bloom level of 2.68 against the market’s 3.63, a differential of −0.95 of a level (95% CI [−1.00,−0.89] ;
Cliff’s δ=−0.45 ), so the curriculum sits roughly a full cognitive level below market demand. The deficit is significant
in nine of the eleven domains and is deepest in General and Transversal skills (−1.17), Artificial Intelligence (−0.98),
Computer Architecture (−0.91), and Systems (−0.80), and shallowest, to the point of non-significance, in Web and
12

APREPRINT- AUGUST14, 2026
occupation-family demand profile
program supply profile
CE CS DSAI IS IT
CE 0.84 0.77 0.75 0.59 0.82
CS 0.88 0.84 0.86 0.58 0.87
DSAI 0.72 0.67 0.89 0.47 0.72
IS 0.71 0.59 0.59 0.95 0.63
IT 0.91 0.88 0.82 0.61 0.87
Figure 6: Program supply profiles against occupation-family demand profiles (cosine). Own-family cells (boxed)
average 0.88 against 0.722 off-diagonal; program-to-program supply similarity falls from 0.835 on the full curriculum
to 0.535 on the major blocks, locating differentiation in the majors. Codes: CE (Computer Engineering), CS (Computer
Science), DSAI (Data Science and Artificial Intelligence), IS (Information Security), IT (Information Technology).
Mobile Development and in Emerging Technologies, where the curriculum already teaches at the applied level the
market expects. The depth gap compounds the content gap: the domains the curriculum under-supplies it also, where it
does teach them, tends to teach below the level at which the market requires them. Figure 7 plots the per-domain depth
differential with confidence intervals, and Figure 8 the full Bloom-level distribution on each side.
7 Discussion and Implications
Taken together, the four findings describe a curriculum that is broad and shallow where the labor market is applied
and deep. The misalignment is at oncestructural, in that the portfolio allocates attention to the eleven domains very
differently from the market, leaning toward algorithmic and theoretical foundations and toward general-education
breadth while under-serving systems, software engineering, security, and web development, andcognitive, in that even
where a domain is present it is typically taught roughly a full Bloom level below the depth the market expects. Both
forms of misalignment are systemic across the five programs rather than peculiar to any one of them, and they persist on
the realized-attainment basis that counts only what a graduate is guaranteed to encounter, which is to say that they are
properties of the degrees as they are actually completed rather than artifacts of catalog breadth. We are careful not to
over-read the apparent over-investment in foundations, since a labor market advertises for applied competencies far more
readily than for the theoretical groundwork it silently assumes, and the extreme case, Algorithms and Computational
Theory at a representation ratio of 0.02, surely reflects in part that postings rarely name the algorithmic competence they
presuppose; the robust half of the structural story, namely the divergence between how the curriculum and the market
allocate attention across the eleven domains, is the under-service of the applied domains, which postings state explicitly.
For curriculum governance, the systemic character of the gaps carries a direct consequence. Because the five programs
fail the market in the same places, the most efficient remedy is not a sequence of program-by-program adjustments
but a portfolio-level response, most naturally located in the shared college core that every graduate completes, and
the realized-attainment lens sharpens the prescription by distinguishing a competency absent from the curriculum
altogether from one present but reachable only through an elective most graduates never take: the former calls for new
13

APREPRINT- AUGUST14, 2026
-1.0 -0.5 0.0 0.5
General & Transversal
AI & Data Science
Computer Arch. & HW
Systems & Infrastructure
HCI & Design
Programming & Software
Software Eng. & PM
Cybersecurity & Ethics
Algorithms & Theory
Web & Mobile
Emerging Technologies
Figure 7: Per-domain Bloom-depth differential (supply minus demand) with 95% confidence intervals; a filled marker
denotes significance after false-discovery-rate control. Every domain that admits a comparison is taught below the level
demanded, deepest in General, AI, Computer Architecture, and Systems.
supply demand
0%
10%
20%
30%
40%
50%
60%
18.3%
3.7%
1 Remember
28.6%
2%
2 Understand
26.9%
42.7%
3 Apply
18.9%
30.6%
4 Analyze/Eval
7.2%
21%
5 Create
Figure 8: Bloom-level distribution of the curricular supply and the labor-market demand. The curriculum concentrates
at the lower levels (Remember through Apply) while the market mass sits at Apply through Create.
content, the latter only for promoting an existing elective into the guaranteed core, a far cheaper intervention the catalog
view cannot detect. Systems and Infrastructure is the clearest priority, as it is at once the most under-supplied applied
domain in guaranteed volume and among the most under-pitched in depth, and because the analysis localizes both
which competencies to strengthen and the cognitive level at which they fall short, a committee can act surgically at the
level of individual courses rather than through wholesale redesign.
The differentiation result tempers a common intuition. The five programs are genuinely differentiated in disciplinary
content, each leaning toward its own occupation family and diverging in the majors where differentiation is meant
to live, and this is appropriate and worth preserving; yet differentiation in content does not, on its own, close the
14

APREPRINT- AUGUST14, 2026
market gaps, because those gaps are shared. A college tempted to respond to a perceived misalignment by further
specializing its programs would therefore be addressing the wrong margin, since the programs already diverge where
the market diverges and converge precisely where they all fall short. The cognitive-depth deficit reinforces the point, for
it concerns not which topics appear in a syllabus but the demand at which they are taught, a property that program-level
specialization leaves untouched and that can be raised only by changing how competencies are taught and assessed.
Methodologically, the study makes the case that curriculum analytics is most useful to governance when conducted at
the scale at which governance decisions are made and on terms that reflect the degree as completed. Three choices
proved consequential. Reading the supply on a realized-attainment basis, rather than counting every catalog course
equally, corrected the representation ratios in the domains where it mattered most and is a prerequisite for any honest
supply-versus-demand comparison. Grounding the extraction so that every competency is verbatim and verified, and
subjecting it to a blind, independent human validation rather than treating the language model as an oracle, allowed
the reliability of the records to be quantified rather than assumed. And making the threshold-free domain-by-level
grid the primary evidence, with the embedding coverage layer reserved for corroboration and itself validated against a
human matching gold, kept the headline findings independent of any free parameter. None of these choices is specific
to one college: the instrument transfers to any institution that publishes its curricula and any labor market whose
advertisements can be collected.
8 Limitations
Several limitations bound the study, which is, in form, a case study that applies a general portfolio-alignment framework
to the curricula of a single college. It covers one College of Information Technology, so the specific gap profile, though
produced by a uniform and reproducible instrument, should be generalized to other institutions only with care; what
transfers is the framework rather than the particular findings. The demand corpus is a contemporaneous snapshot of
online advertisements from mid-2026 rather than a longitudinal series, so the temporal-responsiveness dimension of
the framework cannot be instantiated here, and each competency counts equally, so the demand profile reflects how
often a requirement is stated rather than its weighting by seniority or hiring volume. On the method, the cognitive
level is read from the governing verb, and on multi-verb outcomes a leading-verb convention is adopted that an equally
defensible highest-order-verb reading would level differently; this accounts for the few large rater disagreements
on level and is the deliberate, reproducible choice noted in Section 5. The blind validation used two raters rather
than three, and the extraction accuracy is computed against the cases on which they agree, so it is conditioned on a
consensus that excludes the genuinely contested items; the residual domain disagreement, in turn, concentrates on the
transversal-versus-technical reading of foundational mathematics and communication-framed outcomes. Finally, while
the aggregate and shared-core coverage are stable across matching techniques, the finer per-domain coverage ordering
is matcher-sensitive, which is why we report the coverage with the human-validated embedder and treat the per-domain
ranking as indicative rather than exact, and why the threshold-free representation and depth analyses, which depend on
no embedding, carry the principal weight.
9 Conclusion
This paper has taken the college, rather than the individual program, as the unit of curriculum–labor market analysis,
applying one uniform, taxonomy-anchored instrument across the full undergraduate portfolio of a College of Information
Technology and reading the curricular supply on a realized-attainment basis that respects the credit-hour and elective
constraints under which degrees are completed. Built on a grounded, blind-validated extraction and a unified labor-
market corpus of 5,186 openings, the analysis establishes that the gaps between curriculum and market are systemic
rather than program-specific, that the shared college core satisfies only about a third of the demanded competencies,
that the programs are well differentiated in disciplinary content yet homogeneous in where they fall short, and that
the curriculum is pitched roughly a full Bloom level below the market across the portfolio, most acutely in systems.
The misalignment is thus structural and cognitive at once, common to the programs, and concentrated in the applied
domains the market names most insistently.
Beyond the particular diagnosis, the contribution is an instrument and a stance: a reproducible, portfolio-scale analysis
that measures every program on the same terms, reflects what graduates actually attain, and reports its own reliability,
yielding findings a curriculum committee can act on surgically rather than impressionistically. Several extensions
would deepen it. A longitudinal demand series paired with dated revisions of the curricular record would make the
temporal-responsiveness dimension operational; weighting the demand corpus by seniority, recency, and hiring volume
would sharpen the market signal; a finer resolution of the taxonomy below its broad domains would localize gaps within
them; and applied across several institutions, the same instrument would turn a single college’s audit into comparative
evidence about how computing portfolios, as a class, align with the labor markets they serve.
15

APREPRINT- AUGUST14, 2026
Acknowledgements
The authors gratefully acknowledge the College of Information Technology and the Research and Innovation Office at the
United Arab Emirates University for their support of the article processing charge required for open access publication,
as well as for the institutional resources, including computational facilities, library access, and infrastructural support,
that enabled the literature review and the empirical analysis underlying this work.
Funding
No funding was received for conducting this study. The authors did not receive financial support from any organization
for the submitted work.
Declaration of Competing Interests
The authors declare that they have no known competing financial interests or personal relationships that could have
influenced the work reported in this paper.
Author Contributions (CRediT)
Sherzod Turaev:Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Data Curation,
Writing – Original Draft, Writing – Review & Editing, Visualization, Supervision, Project Administration.Saja
Aldabet:Methodology, Investigation, Software, Validation, Data Curation, Writing – Review & Editing.Mary John:
Methodology, Investigation, Software, Validation, Data Curation, Writing – Review & Editing.Namya Musthafa:
Visualization, Validation, Writing – Review & Editing.Mamoun Awad:Conceptualization, Validation, Data Curation,
Writing – Review & Editing, Supervision.Nazar Zaki:Conceptualization, Validation, Resources, Writing – Review &
Editing.Khaled Shuaib:Conceptualization, Validation, Resources, Writing – Review & Editing.
Data Availability
The datasets generated and analyzed during the current study, namely the curricular supply corpus, the deduplicated
labor-market demand corpus, and the extracted competency inventories with their taxonomic and cognitive annotations,
are not publicly available at this stage but are available from the corresponding author on reasonable request.
References
ABET. Criteria for accrediting computing programs, 2024–2025. Technical report, Computing Accreditation Commis-
sion, ABET, Baltimore, MD, USA, 2024. [Online]. Available: https://www.abet.org/wp-content/uploads/
2023/05/2024-2025_CAC_Criteria.pdf.
ACM Data Science Task Force. Computing competencies for undergraduate data science curricula. Technical report,
Association for Computing Machinery, New York, NY , USA, 2021. [Online]. Available:https://www.acm.org/
binaries/content/assets/education/curricula-recommendations/dstf_ccdsc2021.pdf.
ACM/IEEE-CS. Computer engineering curricula 2016 (CE2016): Curriculum guidelines for undergraduate de-
gree programs in computer engineering. Technical report, Association for Computing Machinery, New York,
NY , USA, 2016. [Online]. Available: https://www.acm.org/binaries/content/assets/education/
ce2016-final-report.pdf.
ACM/IEEE-CS. Information technology curricula 2017 (IT2017): Curriculum guidelines for baccalaureate de-
gree programs in information technology. Technical report, Association for Computing Machinery, New
York, NY , USA, 2017. [Online]. Available:https://www.acm.org/binaries/content/assets/education/
curricula-recommendations/it2017.pdf.
ACM/IEEE-CS/AAAI. Computing curricula 2020 (CC2020): Paradigms for global computing education. Technical
report, Association for Computing Machinery, New York, NY , USA, 2020.
ACM/IEEE-CS/AAAI. Computer science curricula 2023 (CS2023). Technical report, Association for Computing
Machinery, New York, NY , USA, 2024.
16

APREPRINT- AUGUST14, 2026
A. Ahadi, K. Kitto, and M.-A. Rizoiu. Skills taught vs skills sought: Using skills analytics to identify the gaps
between curriculum and job markets. InProc. 15th Int. Conf. Educational Data Mining (EDM), 2022. doi:
10.5281/zenodo.6853121.
N. R. Aljohani, A. Aslam, A. O. Khadidos, and S.-U. Hassan. Bridging the skill gap between the acquired university
curriculum and the requirements of the job market: A data-driven analysis of scientific literature.Journal of
Innovation & Knowledge, 7(3):100190, 2022. doi: 10.1016/j.jik.2022.100190.
M. Almgerbi, A. De Mauro, A. Kahlawi, and V . Poggioni. A systematic review of data analytics job requirements
and online courses.Journal of Computer Information Systems, 62(2):422–434, 2022. doi: 10.1080/08874417.2021.
1971579.
L. W. Anderson and D. R. Krathwohl.A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom’s
Taxonomy of Educational Objectives. Longman, New York, NY , USA, 2001.
A. Bamkole, M. Geissler, K. Koumadi, C. Servin, C. Tang, and C. S. Tucker. Bloom’s for computing: Enhancing
bloom’s revised taxonomy with verbs for computing disciplines. Technical report, ACM Committee for Computing
Education in Community Colleges (CCECC), 2023.
Y . Benjamini and Y . Hochberg. Controlling the false discovery rate: A practical and powerful approach to multiple
testing.Journal of the Royal Statistical Society: Series B (Methodological), 57(1):289–300, 1995. doi: 10.1111/j.
2517-6161.1995.tb02031.x.
J. Biggs and C. Tang.Teaching for Quality Learning at University. Open University Press, Maidenhead, UK, 4th
edition, 2011.
J. B. Carroll. A model of school learning.Teachers College Record, 64(8):723–733, 1963. doi: 10.1177/
016146816306400801.
N. Cliff. Dominance statistics: Ordinal analyses to answer ordinal questions.Psychological Bulletin, 114(3):494–509,
1993. doi: 10.1037/0033-2909.114.3.494.
J. Cohen. Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit.
Psychological Bulletin, 70(4):213–220, 1968. doi: 10.1037/h0026256.
H. Cramér.Mathematical Methods of Statistics. Princeton University Press, Princeton, NJ, USA, 1946.
J.-J. Decorte, S. Verlinden, J. Van Hautte, J. Deleu, C. Develder, and T. Demeester. Extreme multi-label skill extraction
training using large language models. InProc. Int. Workshop on AI for Human Resources and Public Employment
Services (AI4HR&PES), ECML-PKDD, pages 1–10, Torino, Italy, 2023.
B. Efron and R. J. Tibshirani.An Introduction to the Bootstrap. Chapman & Hall, New York, NY , USA, 1993.
European Commission. ESCO handbook: European skills, competences, qualifications and occupations. Technical
report, Publications Office of the European Union, Luxembourg, 2021. [Online]. Available: https://esco.ec.
europa.eu/system/files/2021-07/Handbook.pdf.
A. R. Feinstein and D. V . Cicchetti. High agreement but low kappa: I. the problems of two paradoxes.Journal of
Clinical Epidemiology, 43(6):543–549, 1990. doi: 10.1016/0895-4356(90)90158-L.
P. Föll, M. Hauser, and F. Thiesse. Identifying the skills expected of IS graduates by industry: A text mining approach.
InProc. 39th Int. Conf. Information Systems (ICIS), San Francisco, CA, USA, 2018.
C. B. Frey and M. A. Osborne. The future of employment: How susceptible are jobs to computerisation?Technological
Forecasting and Social Change, 114:254–280, 2017. doi: 10.1016/j.techfore.2016.08.019.
V . Garousi, G. Giray, E. Tüzün, C. Catal, and M. Felderer. Closing the gap between software engineering education and
industrial needs.IEEE Software, 37(2):68–77, 2020. doi: 10.1109/MS.2018.2880823.
A.-S. Gnehm, E. Bühlmann, and S. Clematide. Evaluation of transfer learning and domain adaptation for analyzing
german-speaking job advertisements. InProc. 13th Language Resources and Evaluation Conf. (LREC), pages
3892–3901, Marseille, France, 2022.
¸ S. Gürcan and N. E. Cagiltay. Big data software engineering: Analysis of knowledge domains and skill sets using
LDA-based topic modeling.IEEE Access, 7:82541–82552, 2019. doi: 10.1109/ACCESS.2019.2924075.
K. L. Gwet. Computing inter-rater reliability and its variance in the presence of high agreement.British Journal of
Mathematical and Statistical Psychology, 61(1):29–48, 2008. doi: 10.1348/000711006X126600.
K. Jaiswal, I. Kuzminykh, and S. Modgil. Understanding the skills gap between higher education and industry in
the UK in the artificial intelligence sector.Industry and Higher Education, 39(2):234–246, 2025. doi: 10.1177/
09504222241280441.
17

APREPRINT- AUGUST14, 2026
Joint Task Force on Cybersecurity Education. Cybersecurity curricula 2017 (CSEC2017): Curriculum guidelines for
post-secondary degree programs in cybersecurity. Technical report, ACM, IEEE Computer Society, AIS SIGSEC, and
IFIP WG 11.8, 2017. [Online]. Available: https://www.acm.org/binaries/content/assets/education/
curricula-recommendations/csec2017.pdf.
E. Karakolis, P. Kapsalis, S. Skalidakis, C. Kontzinos, P. Kokkinakos, O. Markaki, and D. Askounis. Bridging the gap
between technological education and job market requirements through data analytics and decision support services.
Applied Sciences, 12(14):7139, 2022. doi: 10.3390/app12147139.
K. Krippendorff.Content Analysis: An Introduction to Its Methodology. Sage Publications, Thousand Oaks, CA, USA,
2 edition, 2004.
L. M. McDonnell. Opportunity to learn as a research concept and a policy instrument.Educational Evaluation and
Policy Analysis, 17(3):305–322, 1995. doi: 10.3102/01623737017003305.
National Center for O*NET Development. O*NET OnLine. U.S. Department of Labor, 2026. Accessed: Jun. 2026.
[Online]. Available:https://www.onetonline.org.
D. Piróg and A. Hibszer. Utilising the potential of job postings for auditing learning outcomes and improving graduates’
chances on the labour market.Higher Education Quarterly, 78:113–134, 2024. doi: 10.1111/hequ.12449.
A. C. Porter. Measuring the content of instruction: Uses in research and practice.Educational Researcher, 31(7):3–14,
2002. doi: 10.3102/0013189X031007003.
A. Radermacher and G. Walia. Gaps between industry expectations and the abilities of graduates. InProc. 44th ACM
Tech. Symp. on Computer Science Education (SIGCSE), pages 525–530, 2013. doi: 10.1145/2445196.2445351.
SFIA Foundation. Skills framework for the information age (SFIA), 2026. Accessed: Jun. 2026. [Online]. Available:
https://sfia-online.org/en.
I. Spada, F. Chiarello, S. Barandoni, G. Ruggi, A. Martini, and G. Fantoni. Are universities ready to deliver digital
skills and competences? a text mining-based case study of marketing courses in italy.Technological Forecasting and
Social Change, 182:121869, 2022. doi: 10.1016/j.techfore.2022.121869.
W. G. Spady.Outcome-Based Education: Critical Issues and Answers. American Association of School Administrators,
Arlington, V A, USA, 1994.
K. J. Travers and I. Westbury.The IEA Study of Mathematics I: Analysis of Mathematics Curricula. Pergamon Press,
Oxford, UK, 1989.
S. Turaev, M. John, M. Awad, N. Zaki, and K. Shuaib. Large language models for curriculum–labor market alignment:
A survey, a reference framework, and six design desiderata.Submitted to IEEE Access, 2026a. Under review.
S. Turaev, M. John, M. Awad, N. Zaki, and K. Shuaib. An NLP-driven framework for curriculum–labor market alignment:
Schema-constrained LLM extraction, ESCO-anchored semantic matching, and multi-dimensional gap quantification.
arXiv preprint arXiv:2606.01982, 2026b. Zenodo supplementary: https://doi.org/10.5281/zenodo.20050816.
World Economic Forum. The future of jobs report 2025. Technical report, World Economic Forum, Geneva, Switzerland,
2025. [Online]. Available: https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf.
Z. Xu, X. Li, Y . Huan, V . Minaya, and R. Yu. From course to skill: Evaluating large language model performance in
curricular analytics. In A. I. Cristea, E. Walker, Y . Lu, O. C. Santos, and S. Isotani, editors,Artificial Intelligence in
Education (AIED 2025), volume 15882 ofLecture Notes in Computer Science, Cham, Switzerland, 2025. Springer.
doi: 10.1007/978-3-031-98465-5_26.
A. Zamecnik, A. Barthakur, H. Wang, and S. Dawson. Mapping employable skills in higher education curriculum using
LLMs. InProc. European Conf. on Technology Enhanced Learning (EC-TEL), volume 15160 ofLecture Notes in
Computer Science, pages 18–32, Cham, Switzerland, 2024. Springer. doi: 10.1007/978-3-031-72312-4_2.
M. Zhang, K. Jensen, S. Sonniks, and B. Plank. SkillSpan: Hard and soft skill extraction from English job postings. In
Proc. 2022 Conf. of the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies (NAACL-HLT), pages 4962–4984, Seattle, W A, USA, 2022. Association for Computational Linguistics.
18

APREPRINT- AUGUST14, 2026
A Derivation and Verification of the Scope Weights
This appendix derives the weights of the opportunity–attainment scope model from program structure and verifies that
the expected-scope weights recover each program’s prescribed course count and credit-hour load. It generalizes, to the
five-program portfolio, the single-program student-path derivation of the pilot.
A.1 The weighting function
Let a program comprise requirement groups G. A group g∈G offers a menu Mg of distinct courses, of which a
graduate completess g; a required group hass g =|M g|and an elective group hass g <|M g|. Modeling within-group
choice as uniform over the menu, the probability that a graduate completes course c∈M g is π(c) =s g/|Mg|, whence
the expected-scope weight is wexpected(c) =π(c) , the floor weight is wfloor(c) =1[s g =|M g|], and the ceiling weight
is wceiling(c) = 1. The uniform choice is the maximum-entropy distribution consistent with the program’s structural
constraints; where empirical registration data are available, π may be replaced by the observed selection frequencies
without altering anything that follows. For an ESCO domain d and a scope σ∈ {floor,expected,ceiling}, the supply
mass and the domain’s share are
Sσ(d) =
X
c
wσ(c)1[dom(c) =d],share σ(d) = Sσ(d)P
d′ Sσ(d′) ,(1)
the sum running over all extracted supply competencies, and theopportunity–attainment bandof a domain,
shareceiling(d)−share floor(d), measures how much of its apparent presence is contingent on elective choice rather
than guaranteed.
A.2 Normalization
The expected weights are a faithful accounting of what a graduate completes. Summing over the courses of a single
group, X
c∈Mg
wexpected(c) =
X
c∈Mg
sg
|Mg| =|M g| ·sg |Mg| =s g,(2)
so the expected number of courses a graduate completes from group g equals its slot budget, and summing over all
groups, X
c
wexpected(c) =
X
g∈G
sg =N P ,(3)
the total number of courses the program requires. When the courses of a group share a common credit value CHg,
the expected credit-hour load is P g∈G sg CHg, which equals the program’s prescribed total. The general-education
block makes the identity concrete: every program requires twenty-one credit hours over seven three-credit slots, of
which the four mandatory courses (five for Computer Engineering) carry full weight and the elective pool contributesP
c π(c) =s g further courses, namely three for Computer Science, Data Science and Artificial Intelligence, and Information Technology, and two for Computer Engineering and Information Security. The expected general-education
course count is therefore seven, and the expected load twenty-one credit hours, for every program and independently of
which electives a graduate selects. The identity depends only on the slot budgets and not on the menu sizes, which is
precisely what makes the floor and ceiling assumption-free bounds and the expected scope an unbiased point estimate
between them.
A.3 Mandatory choose-one themes
One program, Information Security, satisfies a mandatory general-education theme through a choice of one of two
equivalent courses. We treat such a theme as a group with sg = 1 and |Mg|= 2 , so that each alternative carries
expected weight π= 1 2 and the two together contribute one guaranteed course; the theme is credited to the floor because a graduate certainly completes one of its courses, even though the identity of that course is contingent. Every other
group is either fully required (sg =|M g|) or a genuine elective (sg <|M g|), and the slot budgets and menu sizes for all
five programs are those of Table 1.
B Statistical Analysis
Throughout the analysis we report effect sizes as the primary evidence, because the extracted inventories are a near-
census of the five curricula and statistical significance is therefore attained trivially at this scale; the significance tests
19

APREPRINT- AUGUST14, 2026
are secondary, and where the labor-market sample is generalized to the market it represents they are read as inferential.
This appendix defines the agreement, effect-size, multiplicity, and uncertainty measures used. The omnibus tests we
report, namely the Mann–Whitney U test, the Kruskal–Wallis H test, and the χ2 test of independence, are standard
nonparametric procedures and are used in their usual form.
B.1 Agreement
Inter-rater agreement is reported as chance-corrected coefficients rather than as raw concordance. For two raters
on the nominal domain we use Cohen’s unweighted κ (Cohen, 1968), and on the ordinal Bloom scale Cohen’s
quadratic-weightedκ,
κ= 1−
P
i,j wij Oij P
i,j wij Eij
, w ij = (i−j) 2 (K−1) 2 ,(4)
where Oij and Eij are the observed and chance-expected proportions of rating pairs over the K= 5 levels, and the
quadratic weights penalize larger level disagreements more heavily than near-misses. Because the marginal distribution
of the validity judgment is highly skewed, where nearly every extracted unit is a genuine competency, the Cohen
coefficient understates agreement through the well-known prevalence paradox (Feinstein and Cicchetti, 1990); we
therefore report, for that judgment, the prevalence- and bias-adjusted coefficient PABAK = 2P o −1 and Gwet’s
AC1 (Gwet, 2008), both of which are robust to a skewed marginal. The multi-rater nominal agreement underlying the
reliability table is summarized by Krippendorff’s alpha (Krippendorff, 2004), which generalizes the chance-corrected
agreement to arbitrary numbers of raters and missing judgments. We read κ on the conventional bands: slight up to
0.20, fair to0.40, moderate to0.60, substantial to0.80, and almost perfect above.
B.2 Effect sizes
For a difference in cognitive depth between two groups of competencies we report Cliff’sδ (Cliff, 1993), a nonparametric
dominance measure,
δ= #{(a, b) :a > b} −#{(a, b) :a < b} |A| |B| , δ∈[−1,1],(5)
where a ranges over group A and b over group B; thus δ is the probability that a competency drawn from A is taught
more deeply than one drawn from B minus the reverse, and is robust to the ordinal, non-normal level scale. We interpret
|δ| as negligible below 0.147, small below 0.33, medium below 0.474, and large otherwise. For the association between
two categorical variables, such as side and domain, we report Cramér’sV(Cramér, 1946),
V=
s
χ2
n(min(r, c)−1) ,(6)
with χ2 the test statistic, n the table total, and r and c the numbers of rows and columns, which rescales the χ2 statistic
to[0,1](small near0.1, medium near0.3, large near0.5).
B.3 Multiplicity and uncertainty
When a test is applied separately across the eleven domains, we control the false-discovery rate by the Benjamini–
Hochberg procedure (Benjamini and Hochberg, 1995): ordering the p-values p(1) ≤ · · · ≤p(m), the adjusted value
is
q(k) = min ℓ≥k min

1, m ℓ p(ℓ)  ,(7)
and a domain is reported as under-pitched when q <0.05, which bounds the expected proportion of false positives
among the flagged domains rather than the familywise error rate. Uncertainty in the portfolio-wide cognitive-depth
differential is quantified by a nonparametric bootstrap (Efron and Tibshirani, 1993): the matched supply and demand
levels are resampled with replacement B= 3,000 times, the difference of means is recomputed on each resample, and
the reported95%interval is read from the resulting bootstrap distribution.
B.4 Similarity
The alignment between a program’s supply profile and an occupation family’s demand profile (Figure 6) is the cosine
similarity of their eleven-dimensional domain-share vectorsuandv,
cos(u,v) = u·v ∥u∥ ∥v∥,(8)
20

APREPRINT- AUGUST14, 2026
which measures the angle between the two distributions of attention over domains and is invariant to their overall
magnitude.
21
