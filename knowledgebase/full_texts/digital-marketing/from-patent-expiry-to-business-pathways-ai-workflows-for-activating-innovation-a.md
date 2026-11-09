---
title: 'From Patent Expiry to Business Pathways: AI Workflows for Activating Innovation Archives'
url: https://arxiv.org/abs/2607.10179
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Sidney Shapiro
- Mark Price
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.10179
pages: 30
chars: 88479
fetched_at: '2026-11-08T13:10:58+00:00'
kb_version: 1
---

# From Patent Expiry to Business Pathways: AI Workflows for Activating Innovation Archives

From Patent Expiry to Business Pathways:
AI Workflows for Activating Innovation Archives
Sidney Shapiro
Dhillon School of Business, University of Lethbridge
sidney.shapiro@uleth.ca
Mark Price
Opus College of Business, University of St. Thomas
pric4635@stthomas.edu
Abstract
Patent databases represent one of the largest public archives of technical knowledge, yet much
of this knowledge remains difficult to identify, interpret, and reuse once patent rights expire or
lapse. This paper proposes an AI-enabled framework for discovering expired and lapsing patents,
identifying technology trends, and translating patent disclosures into business pathways. We use
pathways to mean structured commercialization routes such as SaaS products, services, licensing
packages, consulting playbooks, training offerings, data products, or internal process tools. The
framework treats patent expiry as both a business signal and an archival transition, not primarily
as a legal problem. Legal status remains important, but it is one risk-screening input alongside
customer need, implementation feasibility, channel access, and market timing. We describe
a system architecture that combines patent metadata, maintenance-fee records, legal-status
indicators, semantic search, patent-family analysis, market signals, and generative AI workflows.
A proof of concept parses all 378 records in an official weekly CIPO ST.96 archive, identifies 20
expired, lapsed, or near-expiry candidates, tests the stability of the transparent scoring model,
and uses a locally hosted Qwen3.6 model to populate structured review packets. The evaluation
demonstrates reproducible ingestion, stable rankings under weight perturbation, and schema-
conformant model output, while also exposing incomplete legal-status coverage and the need
for register and expert review. We argue that AI can function as a discovery and translation
layer for dormant technical knowledge, but that such systems must explicitly represent legal
uncertainty, data limitations, and commercialization risk.
Keywords:patent analytics, business pathways, innovation archives, natural language processing,
entrepreneurship, expired patents, design science
1 Introduction
Patent databases are among the largest publicly accessible archives of technical knowledge. In
exchange for temporary monopoly rights, inventors disclose detailed specifications that describe
methods, systems, and applications across nearly every industry. Patent disclosure becomes public
well before expiry in many jurisdictions, but expiry or lapse can change whether the claimed
invention remains enforceable in a particular jurisdiction. In practice, this disclosed knowledge
remains difficult to discover, interpret, and operationalize at scale.
1
arXiv:2607.10179v1  [cs.IR]  11 Jul 2026

The barrier is not merely access. Patent records are written in specialized legal and technical
language. Legal status depends on jurisdiction-specific maintenance rules, patent families span
multiple national registers, and commercial viability depends on market context that is rarely en-
coded in patent metadata. Entrepreneurs, university technology transfer offices, small and medium
enterprises (SMEs), and corporate innovation teams therefore face a translation problem: public
archives exist, but actionable business pathway maps do not.
This paper proposes an AI-enabled framework for treating expired and lapsing patents as a
dynamic innovation archive. We frame patent expiry not only as a legal status change but also
as an archival transition event and a business pathway signal, a point at which disclosed technical
knowledge may become more available for reuse, reinterpretation, and commercialization. We use
the termpathwayto emphasize that the central task is exploration: identifying plausible routes
from disclosed knowledge to business action. These routes may include SaaS products, productized
services, consulting methods, training programs, licensing bundles, data products, internal workflow
tools, or research commercialization projects. Our contribution combines three themes:
1.Archival intelligence:patents as public innovation infrastructure rather than static legal
repositories;
2.AI-mediated translation:NLP and workflow automation that convert patent disclosures
into ranked business pathways and product hypotheses;
3.Responsible commercialization support:explicit representation of legal uncertainty,
family risk, customer need, implementation feasibility, and pathway-specific assumptions.
We adopt a design-science orientation [Hevner et al., 2004], presenting a conceptual architecture,
Python workflow patterns, and evaluation-oriented artifacts rather than a production patent search
platform. The workflows emphasize auditable decision logic for translating archival records into
pathway hypotheses without implying verified legal status or commercial viability for any individual
patent.
Our research questions are:
1. How can expired and lapsing patents be represented as an actionable innovation archive?
2. What AI workflows are needed to translate patent disclosures into product, service, SaaS,
data, training, or licensing pathways?
3. What business, legal, ethical, and archival risks emerge when public patent knowledge is
operationalized for commercialization?
4. How can pathway-scoring models balance technical feasibility, customer value, market access,
and intellectual-property risk?
The remainder of the paper proceeds as follows. Section 2 reviews patent systems and data
access. Section 3 surveys related work in patent NLP and expired-patent opportunity research. Sec-
tion 4 presents the system architecture. Section 5 describes Python-backed workflows. Sections 6–7
discuss implications and limitations. Section 8 concludes.
2 Background
2.1 Patent Systems and Expiry Events
Patents grant inventors time-limited exclusive rights in exchange for public disclosure. In the
United States and Canada, utility patents generally expire twenty years from the earliest effective
2

filing date, subject to maintenance or annuity fee requirements. Failure to pay required fees can
cause patents to lapse before nominal term expiration. These events, including expiry, lapse, and
abandonment, are legally distinct and must not be conflated in analytics pipelines.
Patent families link related filings across jurisdictions through priority claims, continuations,
and divisionals. A patent may be expired in one country while an equivalent family member remains
active elsewhere. International analytics therefore require both national register reconciliation and
cross-border family mapping via services such as EPO Open Patent Services (OPS) and INPADOC
legal events [European Patent Office, 2024, World Intellectual Property Organization, 2024].
2.2 Patents as Innovation Archives
Archival theory emphasizes that records acquire meaning through context, provenance, and use
[Yeo, 2007, Society of American Archivists, 2024]. Patent databases traditionally function as re-
trieval systems for legal and technical documents. We argue they should also be understood as
innovation archiveswhose value increases when expiry signals are linked to interpretive metadata:
legal status, family relationships, semantic similarity, implementation difficulty, and commercial-
ization readiness.
Expiry is therefore not merely a legal endpoint. It is an archival and business signal indicating
that disclosed knowledge may transition from protected asset to reusable technical input, subject to
family risk, regulatory constraints, customer demand, implementation cost, and market conditions.
2.3 Data Access: United States, Canada, and Beyond
Patent analytics systems depend on tiered data ingestion because no single source provides author-
itative legal status, full text, and family linkage globally.
United States.The USPTO Open Data Portal (ODP) provides bulk data, patent file-wrapper
records, maintenance-fee event data, and API-based search [United States Patent and Trademark
Office, 2026a,b]. Maintenance fee payment status can be verified through the USPTO Maintenance
Fees Storefront. PatentsView and Google Patents Public Data on BigQuery offer research-friendly
longitudinal tables and full text [Google, 2024]. Recent API migrations highlight the need for
robust sync architectures that tolerate source churn.
Canada.The Canadian Intellectual Property Office (CIPO) distributes patents primarily
through IP Horizons bulk downloads, ST.96 XML files, and quarterly researcher CSV/TXT datasets
[Canadian Intellectual Property Office, 2026a,b]. Unlike the US, Canada does not offer a public
patent REST API; programmatic access is bulk-first. Records may appear in English, French, or
both, adding NLP complexity. Legal status events conform to WIPO ST.27 when provided in
ST.96 exports.
International context.EPO OPS, WIPO PATENTSCOPE, PATSTAT, and Lens.org pro-
vide family linkage, legal events, and aggregated bibliographic data across jurisdictions [Lens.org,
2024]. Other national offices, including JPO, KIPO, and CNIPA, maintain distinct access models.
Production systems should treat international coverage as optional enrichment layers rather than
assuming uniform API availability.
Table 1 summarizes US–Canada differences most relevant to our architecture.
2.4 NLP for Patent Documents
Patent NLP differs from general-domain text processing because claims, the legally operative por-
tion of a patent, use specialized syntax, antecedent basis, and long coordination structures [Hu
3

Table 1: Comparison of patent data access in the United States and Canada.
Dimension United States Canada
API access USPTO Open Data Portal (ODP)
APIs; PatentsView migration
No public patent REST API;
bulk/XML downloads
Full text ODP file wrappers; BigQuery
public dataset
ST.96 XML; quarterly researcher
CSV/TXT
Expiry drivers 20-year term; maintenance fees at
3.5, 7.5, 11.5 years
20-year term; annual annuities
from second anniversary
Authoritative
lapse check
Maintenance Fees Storefront Admin status in register; fee his-
tory
Family/legal
status
ODP plus EPO OPS/INPADOC ST.27 in ST.96; EPO OPS for for-
eign equivalents
Language English English and French bilingual
records
Update ca-
dence
Daily/weekly ODP deltas Weekly XML; quarterly researcher
sets
et al., 2016]. Recent surveys document widespread use of transformer models for classification, re-
trieval, and summarization [Jiang and Goetz, 2024, Shomee et al., 2025]. Domain-adapted models
such as PatentBERT demonstrate that claims alone can support CPC classification tasks [Lee and
Hsiang, 2020].
For entrepreneurship workflows, however, text-only models are insufficient. Pathway identifi-
cation requires integrating claims and descriptions with maintenance status, family risk, citation
networks, customer segments, implementation assumptions, route-to-market choices, and scoring
rubrics that encode commercial feasibility and legal uncertainty.
3 Related Work
3.1 Patent NLP and Analytics
Patent analytics has long supported R&D intelligence, competitive landscaping, and technology
forecasting [Bloom et al., 2013]. Earlier technology-mining work treated patents as structured traces
of inventive activity that could be combined with bibliometrics, assignee networks, and classification
codes to identify emerging domains [Porter and Cunningham, 2005]. Patent landscaping practice
similarly emphasizes search strategy, corpus curation, family grouping, and analyst interpretation
rather than document retrieval alone [World Intellectual Property Organization, 2015]. These
traditions are important for expired-patent analytics because opportunity discovery depends on
the quality of the constructed corpus before any AI model is applied.
NLP methods address classification, clustering, citation analysis, summarization, and semantic
retrieval. Transformer-based approaches now dominate, with task-specific adaptations for multi-
label CPC prediction, claim parsing, and similarity search [Jiang and Goetz, 2024, Lee and Hsiang,
2020]. Recent surveys also note a shift from single-document classification toward multimodal and
workflow-oriented patent analysis, where text, drawings, citations, legal events, and external market
signals are combined [Shomee et al., 2025]. Our framework follows this direction by treating AI
outputs as intermediate artifacts in a larger analytic process.
Claim parsing remains challenging because dependent claims inherit limitations from parent
claims, and antecedent references must be resolved before scope can be interpreted [Hu et al.,
4

2016]. These challenges matter for product translation workflows: a plain-language summary that
ignores claim dependency structure may overstate or understate protectable scope.
3.2 Technology Opportunity Discovery
Technology opportunity discovery uses patent corpora to identify promising directions for R&D,
product development, and diversification. Studies in this area often combine semantic similarity,
citation links, technology life-cycle indicators, and market or product terms to surface candidate
opportunities [Song et al., 2017]. The expired-patent setting changes the problem: the question is
not only whether a technology area appears promising, but which business pathways might make
specific disclosed knowledge useful. Legal status matters, but the pathway question is broader
because the same disclosure can support different business routes with different customers, revenue
models, capabilities, and risks.
This distinction creates a need for richer pathway representations. A ranked patent list may
be useful for expert searchers, but entrepreneurs and SMEs need explanations, route-to-market
options, implementation assumptions, and warnings about what the ranking does not prove. Our
workflow design therefore emphasizes interpretable scores, pathway hypotheses, and review packets
rather than optimization of retrieval metrics alone.
3.3 Expired Patents and Open Innovation
A growing literature treats expired patents as sources of reusable technical knowledge. Yun et al.
[2021] analyze expired patents as technology opportunities, emphasizing that public-domain dis-
closures can reduce search costs for firms seeking implementable ideas. Work on higher-education
institutions similarly frames expired patents as resources for academic entrepreneurship [Mafu,
2023].
This literature connects naturally to work on absorptive capacity and open innovation. Firms
benefit from external knowledge only when they can recognize, assimilate, and apply it [Cohen
and Levinthal, 1990]. Open innovation similarly argues that useful knowledge often lies outside
firm boundaries and must be actively searched, evaluated, and recombined [Chesbrough, 2003].
Expired patents can therefore be viewed as an underused external knowledge pool, but only for
organizations with enough technical, legal, and market capability to interpret them.
Our contribution extends this line by integrating expiry analytics with archival framing, multi-
jurisdiction data engineering, and AI workflows that produce structured pathway hypotheses and
review packets rather than retrieval results alone. The aim is not to automate invention or legal
clearance. It is to reduce the interpretive burden that prevents public patent knowledge from
becoming practically usable.
3.4 Decision Support and Legal-Tech Boundaries
Patent analytics tools often blur the boundary between information retrieval and legal advice.
Freedom-to-operate (FTO) analysis requires expert judgment across active family members, con-
tinuations, trademarks, regulatory requirements, and product-specific claim mapping. Credible
systems must therefore function asdecision support: they organize evidence, flag uncertainty, and
route users to professional review rather than declaring legal safety.
This boundary is especially important for generative AI systems because fluent summaries can
obscure uncertainty. Risk-management guidance for AI systems emphasizes context, documenta-
tion, transparency, and human oversight for consequential decisions [National Institute of Standards
and Technology, 2023]. In patent opportunity workflows, those principles translate into provenance
5

Tier 1
USPTO ODP / CIPO
Bulk & Registers
Tier 2
EPO OPS / Lens
Family & Legal
Tier 3
Analytics
Warehouse
Sync
Scheduler
Legal Status
Engine
NLP Pipeline
Claims & Search
Opportunity
Scoring
Expiry
Discovery
Trend
Detection
Patent-to-
Product
Due Diligence
Packet
Patent Innovation Archive System Architecture
Figure 1: Patent innovation archive system architecture with tiered ingestion, NLP processing, and
workflow outputs.
fields, confidence annotations, visible legal cautions, and exportable records that experts can in-
spect.
Design-science research in information systems provides a suitable methodological anchor for
presenting an artifact-oriented framework with explicit evaluation criteria [Hevner et al., 2004].
Rather than claiming a universal model of commercialization success, the present paper specifies
an artifact class, its intended users, its data dependencies, and the evaluation evidence that future
deployments should collect.
4 System Design
We propose a tiered architecture that separates authoritative national sources, cross-border aggre-
gators, and derived analytics stores. Figure 1 illustrates the major components.
4.1 Tiered Data Ingestion
Tier 1 (national authority).USPTO ODP file wrapper and maintenance-fee records; CIPO
ST.96 XML and researcher datasets for Canadian patents. Tier 1 sources are preferred for legal-
status reconciliation.
Tier 2 (aggregators).EPO OPS for family and legal events; Lens.org or BigQuery for cross-
jurisdiction search and enrichment; WIPO PATENTSCOPE for PCT collections.
Tier 3 (analytics warehouse).A canonical schema stores normalized patent identifiers,
bibliographic fields, legal events, family identifiers, embeddings, opportunity scores, and workflow
6

outputs. Sync jobs combine bulk baseline loads with incremental deltas and on-demand enrichment
for candidate patents.
4.2 Database and Table Design
The system should not be implemented as a Python script operating over loose files. Python is
useful for ingestion, scoring, NLP calls, and packet generation, but the durable analytic object is a
database. A production version should use a relational database or analytical warehouse, such as
PostgreSQL, DuckDB, BigQuery, or Snowflake, with tables that preserve source provenance and
support repeatable joins across patent, legal-status, family, market, compliance, and contract data.
Listing 1 sketches a minimum relational schema. The intent is not to prescribe one vendor-
specific database, but to show the normalized entities that the workflows require.
Listing 1: Minimum warehouse schema for patent pathway analytics.
1CREATE TABLE patents (
2pa te nt _i d TEXT PRIMARY KEY ,
3j u r i s d i c t i o n TEXT NOT NULL ,
4p u b l i c a t i o n _ n u m b e r TEXT ,
5a p p l i c a t i o n _ n u m b e r TEXT ,
6title TEXT ,
7abstract TEXT ,
8c l a i m s _ t e x t TEXT ,
9f i l i n g _ d a t e DATE ,
10g r a n t _ d a t e DATE ,
11e s t i m a t e d _ e x p i r y _ d a t e DATE ,
12s o u r c e _ u r l TEXT ,
13s o u r c e _ s n a p s h o t _ i d TEXT ,
14u p d a t e d _ a t T IM ES TA MP
15) ;
16
17CREATE TABLE l e g a l _ e v e n t s (
18event_id TEXT PRIMARY KEY ,
19p at en t_ id TEXT R E F E R E N C E S patents ( pa te nt _i d ) ,
20e v e n t _ d a t e DATE ,
21e v e n t _ c o d e TEXT ,
22e v e n t _ t e x t TEXT ,
23s o u r c e _ s y s t e m TEXT ,
24c o n f i d e n c e NUMERIC
25) ;
26
27CREATE TABLE p a t e n t _ f a m i l i e s (
28f am il y_ id TEXT ,
29p at en t_ id TEXT R E F E R E N C E S patents ( pa te nt _i d ) ,
30j u r i s d i c t i o n TEXT ,
31l e g a l _ s t a t u s TEXT ,
32PRIMARY KEY ( family_id , pa te nt _i d )
33) ;
34
35CREATE TABLE c pc _c od es (
36p at en t_ id TEXT R E F E R E N C E S patents ( pa te nt _i d ) ,
37cpc_code TEXT ,
38PRIMARY KEY ( patent_id , cpc_code )
39) ;
7

40
41CREATE TABLE p a t h w a y _ s c o r e s (
42p at en t_ id TEXT R E F E R E N C E S patents ( pa te nt _i d ) ,
43run_id TEXT ,
44o p p o r t u n i t y _ s c o r e NUMERIC ,
45c o m m e r c i a l _ r e l e v a n c e NUMERIC ,
46s a a s _ f e a s i b i l i t y NUMERIC ,
47f a m i l y _ r i s k TEXT ,
48s c o r e _ e x p l a n a t i o n JSON ,
49PRIMARY KEY ( patent_id , run_id )
50) ;
51
52CREATE TABLE p a t h w a y _ p a c k e t s (
53p ac ke t_ id TEXT PRIMARY KEY ,
54p at en t_ id TEXT R E F E R E N C E S patents ( pa te nt _i d ) ,
55run_id TEXT ,
56c a n d i d a t e _ p a t h w a y s JSON ,
57e v i d e n c e _ b u n d l e JSON ,
58u n r e s o l v e d _ r i s k s JSON ,
59r e v i e w e r _ d e c i s i o n TEXT ,
60c r e a t e d _ a t T IM ES TA MP
61) ;
Adjacent public-record tables can follow the same pattern. Procurement notices, compliance
filings, standards references, contracts, and litigation records should each have stable identifiers,
source URLs, collection timestamps, normalized text fields, and embedding references. The impor-
tant design rule is to keep raw source snapshots, normalized fields, derived features, and generated
interpretations separate. This makes it possible to reproduce a pathway packet, inspect a model
output, rerun a scoring method, or explain why a record appeared in a candidate list.
4.3 Legal-Status Engine
The legal-status engine computes estimated expiry dates, maintenance states, and family-risk in-
dicators. It applies jurisdiction-specific rules: US maintenance windows at 3.5, 7.5, and 11.5 years;
Canadian annuities from the second anniversary. When sources disagree, national register status
overrides derived estimates. All outputs include provenance fields and confidence annotations.
4.4 NLP Pipeline
The NLP pipeline performs:
1. document segmentation (claims, description, abstract);
2. normalization and OCR cleanup for legacy scans;
3. CPC/IPC classification for domain filtering;
4. dense retrieval over claims and abstracts for semantic domain search;
5. generative summarization and pathway-hypothesis drafting with structured output schemas;
6. scoring models for commercial relevance, pathway fit, and SaaS feasibility.
8

Domain Query Semantic Retrieval Expiry & Maintenance Family Risk Check Pathway Scoring Pathway Hypothesis Review Export
End-to-End Patent Pathway Workflow
Figure 2: End-to-end workflow from domain query to pathway review export.
Claims-first retrieval aligns with patent NLP findings [Lee and Hsiang, 2020], while generative
layers must be constrained by structured metadata to reduce hallucination risk. In the proposed
pipeline, AI is used for retrieval, normalization, classification, summarization, and pathway drafting,
but not for unreviewed legal clearance. Deterministic rules reconcile dates and register events; NLP
models translate dense technical and legal text into reviewable claims, assumptions, and questions.
The decision-making layer is therefore hybrid. Embedding models retrieve related patents and
external records; classifiers route documents into domains and pathway types; extraction models
identify claim elements, actors, inputs, outputs, and operational constraints; generative models
draft summaries and pathway hypotheses under a schema. The system then asks a narrower decision
question: which candidates deserve expert attention, what evidence supports that attention, and
what uncertainty must be resolved before action?
4.5 Opportunity Scoring
Pathway scores combine commercial relevance, SaaS feasibility, expiry or lapse status, and family-
risk penalties. Scores are explanatory rather than predictive in the illustrative implementation:
each component is exposed to users and auditors. This design supports entrepreneurship use cases
where transparency matters as much as ranking accuracy. A high score should be read as a prompt
for pathway exploration, not as a finding that a business is viable or legally cleared.
4.6 Workflow Orchestration
Four workflow modules consume the analytics warehouse:
•expiry discovery;
•trend detection;
•patent-to-pathway translation;
•pathway review packet generation.
Figure 2 shows the end-to-end path from domain query to exportable expert-review packet.
The modules pass structured objects rather than static reports. Expiry discovery returns can-
didate records with status provenance and family risk. Trend detection returns clusters and aban-
donment signals that can be joined to market, compliance, or contract evidence. Patent-to-pathway
translation returns candidate business routes with assumptions and required inputs. The review-
packet generator binds these outputs into a decision artifact that preserves source evidence, model
outputs, uncertainty fields, and recommended next checks. Table 2 summarizes the inputs, pro-
cessing steps, and primary outputs of each module.
9

Table 2: Workflow inputs, processing steps, and outputs.
W orkflow Processing Steps Primary Outputs
Expiry discov-
ery
Semantic domain filter; ex-
piry/lapse check; maintenance
review; family risk flag
Ranked opportunity list; plain-
language summaries; scores
Trend detection Time-series filing analysis;
CPC clustering; assignee aban-
donment signals
White-space clusters; domain
signals; structured review
prompts
Patent-to-
pathway
Claim summarization; pathway
hypothesis generation; MVP
scoping
Product, service, SaaS, train-
ing, and internal-tool concepts
Pathway review Register reconciliation; family
mapping; citation/continuation
checks; market assumptions
Structured review packet; un-
certainty notes; expert actions
5 Python Workflow Patterns
We describe four Python workflow patterns for converting patent records into reviewable pathway
artifacts. These examples should be read as orchestration code over the database schema in List-
ing 1, not as a recommendation to build the system in Python alone. In practice, SQL or warehouse
queries retrieve candidate records, Python applies scoring, NLP, and packet-generation logic, and
the resulting pathway packets are written back to durable tables for review and audit. The purpose
of the code is to make the decision logic auditable: what data are required, where AI is used, which
checks remain deterministic, and which judgments must be deferred to human reviewers or counsel.
5.1 Data Model
The canonicalPatentRecorddataclass is a typed application-layer view of rows frompatents,
patent families,cpc codes, andpathway scores. It captures bibliographic fields, legal status,
family identifiers, scoring attributes, and text excerpts. Derived methods includedays to expiry,
family risk,opportunity score, andscore explanation. Listing 2 is deliberately close to
runnable Python: a reader could hydrate it from SQL query results, CSV, JSON, ODP, CIPO, or
OPS and then reuse the workflow functions below.
Listing 2: Usable patent record model and scoring helpers.
1from d a t a c l a s s e s import da ta cl as s
2from datetime import date
3from enum import Enum
4
5class L e g a l S t a t u s ( str , Enum ) :
6ACTIVE = " active "
7EXPIRED = " expired "
8LAPSED = " lapsed "
9UNKNOWN = " unknown "
10
11@ d a t a c l a s s ( frozen = True )
12class P a t e n t R e c o r d :
13p at en t_ id : str
14title : str
15abstract : str
10

16c l a i m s _ e x c e r p t : str
17j u r i s d i c t i o n : str
18f i l i n g _ d a t e : date
19e x p i r y _ d a t e : date | None
20l e g a l _ s t a t u s : L e g a l S t a t u s
21m a i n t e n a n c e _ s t a t u s : str
22c pc _c od es : list [ str ]
23f am il y_ id : str
24a c t i v e _ f a m i l y _ m e m b e r s : int
25s o u r c e _ u r l : str
26c o m m e r c i a l _ r e l e v a n c e : float = 0.5
27s a a s _ f e a s i b i l i t y : float = 0.5
28
29def d a y s _ t o _ e x p i r y ( self , as_of : date ) -> int | None :
30if self . e x p i r y _ d a t e is None :
31return None
32return ( self . e x p i r y _ d a t e - as_of ) . days
33
34@ pr op er ty
35def f a m i l y _ r i s k ( self ) -> str :
36if self . a c t i v e _ f a m i l y _ m e m b e r s >= 3:
37return " high "
38if self . a c t i v e _ f a m i l y _ m e m b e r s > 0:
39return " medium "
40return " low "
41
42def o p p o r t u n i t y _ s c o r e ( self , as_of : date ) -> float :
43s t a t u s _ b o n u s = 0.15 if self . l e g a l _ s t a t u s in {
44L e g a l S t a t u s . EXPIRED , L e g a l S t a t u s . LAPSED } else 0.0
45days = self . d a y s _ t o _ e x p i r y ( as_of )
46e x p i r y _ b o n u s = 0.10 if days is not None and 0 <= days <= 730 else
0.0
47f a m i l y _ p e n a l t y = min (0.35 , self . a c t i v e _ f a m i l y _ m e m b e r s * 0.08)
48raw = (0.40 * self . c o m m e r c i a l _ r e l e v a n c e
49+ 0.30 * self . s a a s _ f e a s i b i l i t y
50+ s t a t u s _ b o n u s + e x p i r y _ b o n u s - f a m i l y _ p e n a l t y )
51return round ( max (0.0 , min (1.0 , raw ) ) , 3)
52
53def s c o r e _ e x p l a n a t i o n ( self , as_of : date ) -> dict [ str , object ]:
54return {
55" score " : self . o p p o r t u n i t y _ s c o r e ( as_of ) ,
56" status " : self . l e g a l _ s t a t u s . value ,
57" d a y s _ t o _ e x p i r y " : self . d a y s _ t o _ e x p i r y ( as_of ) ,
58" f a m i l y _ r i s k " : self . family_risk ,
59" a c t i v e _ f a m i l y _ m e m b e r s " : self . a c t i v e _ f a m i l y _ m e m b e r s ,
60" source " : self . source_url ,
61}
The weights in Listing 2 are heuristic and intentionally transparent. In a deployed system, they
should be calibrated against expert labels or observed downstream decisions. The implementation
should expose each component so that analysts can perform sensitivity checks rather than treating
the score as a black-box prediction.
11

5.2 Workflow 1: Expiring Patent Discovery
The expiry discovery workflow filters patents by domain keywords, selects records that are ex-
pired or nearing expiry within a configurable horizon, and ranks candidates by opportunity score.
Outputs include plain-language summaries, source links, legal-status provenance, and structured
metadata for each candidate. Listing 3 shows a complete filter that can operate over any iterable
ofPatentRecordobjects.
Listing 3: Expiry discovery filter and ranking.
1def d o m a i n _ m a t c h ( patent : PatentRecord , keywords : list [ str ]) -> bool :
2text = " " . join ([
3patent . title , patent . abstract , patent . claims_excerpt ,
4" " . join ( patent . cp c_ co de s )
5]) . lower ()
6return any ( k . lower () in text for k in keywords )
7
8def d i s c o v e r _ c a n d i d a t e s (
9patents : list [ P a t e n t R e c o r d ] ,
10keywords : list [ str ] ,
11as_of : date ,
12max_days : int = 730 ,
13t hr es ho ld : float = 0.45 ,
14) -> list [ dict [ str , object ]]:
15rows = []
16for patent in patents :
17if not d o m a i n _ m a t c h ( patent , keywords ) :
18continue
19days = patent . d a y s _ t o _ e x p i r y ( as_of )
20expired = patent . l e g a l _ s t a t u s in {
21L e g a l S t a t u s . EXPIRED , L e g a l S t a t u s . LAPSED }
22nearing = days is not None and 0 <= days <= max_days
23if not ( expired or nearing ) :
24continue
25
26score = patent . o p p o r t u n i t y _ s c o r e ( as_of )
27if score < t hr es ho ld :
28continue
29
30rows . append ({
31" p at en t_ id " : patent . patent_id ,
32" title " : patent . title ,
33" score " : score ,
34" status " : patent . l e g a l _ s t a t u s . value ,
35" d a y s _ t o _ e x p i r y " : days ,
36" f a m i l y _ r i s k " : patent . family_risk ,
37" w h y _ r a n k e d " : patent . s c o r e _ e x p l a n a t i o n ( as_of ) ,
38" s o u r c e _ u r l " : patent . source_url ,
39})
40return sorted ( rows , key = lambda r : r [ " score " ] , reverse = True )
12

5.3 Workflow 2: Trend Detection
Trend detection aggregates filing counts by year, counts expired patents by CPC prefix, and iden-
tifies assignees abandoning patent families. In this paper, trend analysis is treated as an input
to pathway review rather than as a stand-alone chart. The useful output is not a line graph; it
is a set of candidate technology clusters with enough context to decide whether further review is
warranted.
Listing 4 shows the core pattern. The workflow treats each CPC prefix as a rough technology
bucket, compares expired and active coverage, and emits a white-space signal only when expired
records outnumber active records and unresolved family risk remains low. The output is a structured
cluster list, not a chart, so it can feed directly into pathway review.
Listing 4: Trend and white-space detection over CPC prefixes.
1from c o l l e c t i o n s import Counter , d e f a u l t d i c t
2
3def c p c _ p r e f i x ( code : str ) -> str :
4return code . split ( " / " ) [0]
5
6def w h i t e s p a c e _ c l u s t e r s (
7patents : list [ P a t e n t R e c o r d ] ,
8m i n _ e x p i r e d : int = 3 ,
9m a x _ a c t i v e : int = 1 ,
10) -> list [ dict [ str , object ]]:
11e x p i r e d _ b y _ c p c = Counter ()
12a c t i v e _ b y _ c p c = Counter ()
13examples = d e f a u l t d i c t ( list )
14
15for patent in patents :
16for code in patent . cp c_ co de s :
17prefix = c p c _ p r e f i x ( code )
18if patent . l e g a l _ s t a t u s in {
19L e g a l S t a t u s . EXPIRED , L e g a l S t a t u s . LAPSED }:
20e x p i r e d _ b y _ c p c [ prefix ] += 1
21examples [ prefix ]. append ( patent . pa te nt _i d )
22elif patent . l e g a l _ s t a t u s == L e g a l S t a t u s . ACTIVE :
23a c t i v e _ b y _ c p c [ prefix ] += 1
24
25clusters = []
26for prefix , e x p i r e d _ c o u n t in e x p i r e d _ b y _ c p c . items () :
27a c t i v e _ c o u n t = a c t i v e _ b y _ c p c [ prefix ]
28if e x p i r e d _ c o u n t >= m i n _ e x p i r e d and a c t i v e _ c o u n t <= m a x _ a c t i v e :
29clusters . append ({
30" c p c _ p r e f i x " : prefix ,
31" e x p i r e d _ c o u n t " : expired_count ,
32" a c t i v e _ c o u n t " : active_count ,
33" e x a m p l e _ p a t e n t s " : examples [ prefix ][:5] ,
34" r e v i e w _ p r o m p t " : (
35" Check whether demand , c o m p l i a n c e pressure , "
36" or i m p l e m e n t a t i o n cost has changed . " )
37})
38return sorted ( clusters , key = lambda c : c [ " e x p i r e d _ c o u n t " ] , reverse = True
)
13

The same pattern can be extended beyond filing counts. A practical deployment should join
patent records with maintenance-fee events, family-level legal events, assignee histories, product
categories, public procurement notices, compliance filings, standards references, incident reports,
or contract-tracking data. These adjacent datasets help distinguish a technically interesting dis-
closure from an actionable pathway. For example, an expired safety-monitoring disclosure is more
meaningful if procurement contracts show continuing demand for inspection software, compliance
filings reveal recurring reporting burdens, or standards changes create new documentation require-
ments.
5.4 Workflow 3: Patent-to-Pathway Translation
Given a selected patent, the translation workflow produces aProductHypothesisobject that is
used as a pathway hypothesis. It includes a technical summary, plain-language claim explanation,
product interpretations, SaaS options, required data inputs, user segments, MVP features, compet-
itive substitutes, legal caution flags, and recommended next steps. The workflow explicitly treats
legal review as one pathway gate, not as the whole business problem.
Listing 5 illustrates the structured-output approach. In a production system, the lists would be
generated or enriched by a constrained LLM call, but the output schema would remain explicit so
downstream tools can validate required fields. The example below uses a small rule catalog because
it is transparent and testable; a model can draft the prose, but the pathway categories, required
evidence, and caution flags remain controlled.
Listing 5: Patent-to-pathway structured output.
1P A T H W A Y _ R U L E S = {
2" saas " : {
3" keywords " : [ " da sh bo ar d " , " alert " , " monitor " , " workflow " ] ,
4" evidence " : [ " buyer demand " , " i n t e g r a t i o n data " , " security review "
] ,
5} ,
6" service " : {
7" keywords " : [ " i n s p e c t i o n " , " audit " , " a s s e s s m e n t " ] ,
8" evidence " : [ " r e p e a t a b l e method " , " expert delivery capacity " ] ,
9} ,
10" training " : {
11" keywords " : [ " p ro ce d ur e " , " ch ec kl is t " , " s u p e r v i s o r " ] ,
12" evidence " : [ " c u r r i c u l u m fit " , " r e g u l a t o r y training need " ] ,
13} ,
14" c o m p l i a n c e _ t o o l " : {
15" keywords " : [ " report " , " record " , " incident " , " c o m p l i a n c e " ] ,
16" evidence " : [ " filing burden " , " forms " , " re te nt io n o b l i g a t i o n s " ] ,
17} ,
18}
19
20def t r a n s l a t e _ t o _ p a t h w a y s ( patent : P a t e n t R e c o r d ) -> dict [ str , object ]:
21text = f " { patent . title } { patent . abstract } { patent . c l a i m s _ e x c e r p t } " .
lower ()
22caution = [
23" Verify legal status against the national register . " ,
24" Review active family members before c o m m e r c i a l i z a t i o n . " ,
25]
26if patent . a c t i v e _ f a m i l y _ m e m b e r s :
27caution . append (
14

28f " { patent . a c t i v e _ f a m i l y _ m e m b e r s } active family member ( s )
remain . " )
29
30options = []
31for name , rule in P A T H W A Y _ R U L E S . items () :
32hits = [ k for k in rule [ " keywords " ] if k in text ]
33if hits :
34options . append ({
35" pathway " : name ,
36" m a t c h _ t e r m s " : hits ,
37" r e q u i r e d _ e v i d e n c e " : rule [ " evidence " ] ,
38" f i r s t _ t e s t " : f " I nt e rv ie w 5 target users about { name }. " ,
39})
40
41return {
42" p at en t_ id " : patent . patent_id ,
43" t e c h n i c a l _ s u m m a r y " : patent . abstract ,
44" p l a i n _ l a n g u a g e _ c l a i m s " : (
45f " This record d es c ri be s { patent . title . lower () }. "
46f " Key claim text : { patent . c l a i m s _ e x c e r p t [:500]} " ) ,
47" c a n d i d a t e _ p a t h w a y s " : options ,
48" l e g a l _ c a u t i o n _ f l a g s " : caution ,
49}
The pathway object should be treated as a branching device, not as a recommendation. A
single disclosure can produce several candidate routes, each with its own evidence requirements. A
SaaS pathway requires data integration, workflow adoption, cybersecurity review, and subscription
willingness. A consulting or training pathway may require less software development but more
domain credibility and repeatable delivery methods. A contract-tracking or compliance pathway
depends on whether the disclosed method maps to forms, audits, obligations, and renewal events
that organizations already manage. Expanding the code around pathways is therefore more useful
than showing a small synthetic table of ranked records.
5.5 Workflow 4: Pathway Review Packet
The pathway review workflow assembles a structured packet for expert review. It verifies expiry
and maintenance indicators from sample metadata, reports family and citation risk tiers, notes
international equivalent status, and lists recommended actions including formal FTO review when
needed. The packet states clearly that it is not legal advice, but its main purpose is broader:
organizing business, technical, and legal questions so a team can decide which pathway deserves
further exploration.
Listing 6 shows how legal uncertainty is represented as review metadata rather than as a binary
clearance decision. The function builds an exportable packet that can be serialized as JSON,
attached to a CRM record, sent to a legal reviewer, or used as an agenda for customer discovery.
Listing 6: Pathway review packet construction.
1def b u i l d _ r e v i e w _ p a c k e t (
2patent : PatentRecord ,
3h y p o t h e s i s : dict [ str , object ] ,
4evidence : dict [ str , object ] ,
5as_of : date ,
6) -> dict [ str , object ]:
15

7u n r e s o l v e d = [
8" This packet supports pathway review and is not legal advice . " ,
9" National register status should override derived es ti ma te s . " ,
10]
11if patent . f a m i l y _ r i s k != " low " :
12u n r e s o l v e d . append ( " Active family members require counsel review . " )
13if patent . l e g a l _ s t a t u s == L e g a l S t a t u s . UNKNOWN :
14u n r e s o l v e d . append ( " Legal status is unknown or not yet r e c o n c i l e d . "
)
15
16return {
17" p at en t_ id " : patent . patent_id ,
18" g e n e r a t e d _ o n " : as_of . is of or ma t () ,
19" status " : patent . l e g a l _ s t a t u s . value ,
20" m a i n t e n a n c e _ s t a t u s " : patent . ma in te na nc e_ st at us ,
21" f a m i l y _ r i s k " : patent . family_risk ,
22" score " : patent . o p p o r t u n i t y _ s c o r e ( as_of ) ,
23" h y p o t h e s i s " : hypothesis ,
24" evidence " : evidence ,
25" u n r e s o l v e d _ r i s k s " : unresolved ,
26" n e x t _ a c t i o n s " : [
27" Confirm legal status in the national register . " ,
28" Review family members through OPS or INPADOC . " ,
29" Select one pathway for customer di sc ov er y . " ,
30" Estimate build , delivery , and c o m p l i a n c e costs . " ,
31" C o m m i s s i o n FTO review if launch risk warrants it . " ,
32] ,
33}
Listing 7 sketches the additional evidence-gathering layer. The goal is to convert archival
research into action by attaching each pathway hypothesis to the records that would support or
weaken it. In practice, eachsearch *function can wrap a real API, bulk-file query, or manually
curated spreadsheet.
Listing 7: Evidence hooks for pathway assessment.
1def c o l l e c t _ e v i d e n c e ( patent : PatentRecord , clients : dict ) -> dict [ str ,
object ]:
2terms = [ patent . title , patent . abstract , * patent . cp c_ co de s ]
3evidence = {
4" register " : clients [ " register " ]. status ( patent . pa te nt _i d ) ,
5" family " : clients [ " family " ]. events ( patent . fa mi ly _i d ) ,
6" co nt ra ct s " : clients [ " co nt ra ct s " ]. search ( terms , limit =10) ,
7" c o m p l i a n c e " : clients [ " c o m p l i a n c e " ]. search (
8terms =[ " i n s p e c t i o n " , " incident " , " audit " , * terms ] ,
9limit =10) ,
10" s ta nd ar ds " : clients [ " st an da rd s " ]. match ( patent . c l a i m s _ e x c e r p t ) ,
11}
12evidence [ " r e v i e w _ q u e s t i o n s " ] = [
13" Do c on tr ac ts show re cu rr in g buyer demand ? " ,
14" Do c o m p l i a n c e records show a repeated re po rt in g burden ? " ,
15" Do s ta nd ar ds or r e g u l a t i o n s make adoption more likely ? " ,
16" Does any active family member cover the same pathway ? " ,
17]
18return evidence
16

Table 3: Expiry discovery over the full weekly CIPO ST.96 archive. The five records shown are the
top expired, lapsed, or near-expiry candidates by opportunity score. Days to expiry is estimated
from the twenty-year term; a lapsed or inactive status can arise earlier through abandonment, so
those rows may still show a positive term estimate. The final row is the highest-scoring active
record, included as a contrast: high pathway interest does not imply public-domain readiness.
Record Title Est. status Days to expiry Score
CA2616010 Medication Compliance System And Associ-
ated Methods
active or pend-
ing
11 0.44
CA3129424 Peelable Coloured Paint Swatches lapsed or inac-
tive
4,961 0.41
CA2680705 Materials For And Method For Manufactur-
ing Container With Stacking Shoulders And
Resulting Container
lapsed or inac-
tive
1,174 0.41
CA2687626 Glass Yarns Suitable For Reinforcing Organic
And/Or Inorganic Materials
lapsed or inac-
tive
676 0.40
CA3097433 Method For Treatment Of Elements Obtained
By An Additive Manufacturing Process
lapsed or inac-
tive
4,664 0.34
CA3090703 Configuration Systems And Methods For Se-
cure Operation Of Networked Transducers
active or pend-
ing
4,631 0.54
19
20def m a k e _ p a c k e t ( patent : PatentRecord , clients : dict , as_of : date ) -> dict :
21h y p o t h e s i s = t r a n s l a t e _ t o _ p a t h w a y s ( patent )
22evidence = c o l l e c t _ e v i d e n c e ( patent , clients )
23return b u i l d _ r e v i e w _ p a c k e t ( patent , hypothesis , evidence , as_of )
5.6 Real-Data Proof of Concept
To move beyond synthetic examples, we implemented a bounded proof of concept using an official
CIPO ST.96 weekly bulk archive. The workflow downloads the July 2025 weekly CIPO XML
package, parseseverypatent record it contains (378 records in this release, rather than the 25-
record sample used in an earlier draft), and for each record extracts title, abstract, claims excerpt,
assignee, filing date, publication date, document status, and IPC classifications. It estimates a
twenty-year expiry date from the filing date, derives an estimated legal status, computes the expiry-
focused opportunity score from Section 5, and writes a structured JSON review artifact together
with a provenance manifest that records the archive URL, its SHA256 hash, and the parse date.
The score now applies the same expiry and status bonuses used in Listing 2, so expired, lapsed,
and near-expiry records are ranked as expiry-discovery candidates rather than being crowded out
by high-interest active filings. Of the 378 parsed records, 11 are estimated expired or lapsed and 20
fall within the expiry-discovery window (expired, lapsed, or within 730 days of estimated expiry).
Table 3 shows the top five expiry-discovery candidates, with the highest-scoring active record
appended as a contrast. The purpose of the run is not to claim that these records are commercially
attractive or legally available for reuse. The contrast row makes the central caution concrete: an
active record can outscore genuine near-expiry records on pathway interest alone, so the workflow
must separate pathway interest from public-domain readiness. The proof of concept therefore
validates the ingestion, scoring, and packet-generation pattern over the full archive, not the business
value of any individual record.
For the local drafting layer we used the Qwen3.6 model served through a local Ollama instance,
17

with sampling temperature 0.1, JSON-constrained output, and hybrid reasoning disabled so that the
token budget produces the requested structured fields rather than hidden chain-of-thought. The
model drafted a technical summary, candidate pathways, required evidence, legal cautions, and
reviewer questions for the top near-expiry record and for the active contrast record; a deterministic
template supplies the same fields when the model is unavailable. Appendix A reproduces one full
prompt and response. In our trial, model summaries were useful for quick technical orientation,
but pathway evidence and reviewer questions still benefited from deterministic schema controls.
This supports the design choice made throughout the framework: model outputs should be routed
into structured packets with source fields, uncertainty labels, and human-review gates rather than
treated as final recommendations.
We selected a local model for reasons that are operational as well as technical. Patent records
are public, but pathway packets may combine them with proprietary customer notes, unpublished
product concepts, internal scoring assumptions, or counsel-directed review questions. Local infer-
ence keeps these inputs within the analyst’s environment, avoids transmitting them to a third-party
model provider, and permits organizations to apply their own retention, access-control, and audit
policies. It also fixes the model version and decoding settings for reproducibility, allows offline or
restricted-network deployment, and makes per-record processing costs more predictable at larger
volumes. These benefits do not make local output inherently more accurate; the same provenance,
schema validation, uncertainty labels, and human-review requirements apply regardless of where a
model is hosted.
5.7 Evaluation
Because the framework is an artifact rather than a validated product, we report bounded, automatic
evaluation over the real and synthetic corpora. These measures characterize ingestion coverage,
status-derivation consistency, scoring robustness, and structured-output quality. They are not a
substitute for expert inter-rater assessment of pathway quality, which we identify as future work in
Section 7.
Corpus composition.Table 4 summarizes the parsed CIPO corpus. Most records are active
or pending, which is expected for a recent weekly archive, and only a small minority are expired or
lapsed. This distribution is itself a finding: a single weekly release is a weak source of public-domain
candidates, so production expiry discovery should accumulate multiple releases or query historical
baselines rather than a single week.
Status-derivation check.Table 5 maps the raw CIPO document-status text to the derived
category. The keyword rule classifies granted, examination, and abandonment states confidently,
but leaves compliant and allowed applications asunknown, giving definitive coverage of roughly
77%. The residualunknownbucket reflects incomplete vocabulary coverage, not evidence of expiry,
and marks a concrete target for improving the legal-status engine.
Scoring sensitivity .Table 6 perturbs each transparent weight by±20% and reports top-5
overlap and Kendall’sτagainst the baseline ranking. Rankings are stable (τabove 0.87 on the
real corpus and above 0.90 on the synthetic corpus, with top-5 overlap of four or five out of five),
which indicates that the heuristic weights are explanatory and robust rather than finely tuned to
a particular result.
Structured-output quality .Table 7 records the Qwen3.6 drafting-layer behavior. Every live
call returned the five required keys and parsed as valid JSON without repair, confirming that a
constrained local model can populate the packet schema reliably. This is an output-format check,
not a judgment of summary fidelity, which requires expert review.
Illustrative ranking.To show the expiry-focused score behaving as intended when public-
18

Table 4: Real CIPO ST.96 corpus composition. The proof of concept now parses the entire weekly
archive (378 records of 378 XML entries) rather than a 25-record sample. Status is derived from
the CIPO document-status text and a twenty-year term estimate as of the paper reference date.
Estimated status Records Share
estimated expired 3 0.8%
lapsed or inactive 8 2.1%
active or pending 279 73.8%
unknown 88 23.3%
T otal parsed378 100.0%
Near-expiry or expired 20 5.3%
Source:cipo st96 weekly 20250727.zip; SHA256 73c10795647018a5. . . ; reference date 2026-07-09.
Table 5: Status-derivation check: raw CIPO document-status text mapped to the derived category.
The keyword rule confidently classifies granted, examination, and abandonment states, but leaves
compliant and allowed applications asunknown, so definitive coverage is 76.7%. The residual
unknownbucket is a data-quality limitation, not evidence of expiry.
Raw CIPO status text Derived category Records
Examination active or pending 184
Granted and Issued active or pending 81
Application Compliant unknown 72
Pre-Grant active or pending 14
Allowed unknown 14
Deemed Abandoned and beyond the Period of
Reinstatement
lapsed or inactive 5
Granted and Issued estimated expired 3
Deemed Abandoned lapsed or inactive 2
Deemed Expired lapsed or inactive 1
Conditionally Allowed unknown 1
Entered National Phase unknown 1
domain records are present, Table 8 reports the top of the synthetic workplace-safety corpus,
where expired records with low family risk rise to the top of the ranking. The synthetic corpus
complements the real archive: the real data validates ingestion and scoring at scale, while the
synthetic data illustrates the expiry-discovery ranking that a multi-release production corpus would
surface.
5.8 Reproducibility
Workflow scripts should be versioned with fixed source snapshots, schema definitions, and model
prompts. A reproducible package should record the patent data release, register query time, embed-
ding model, prompt template, scoring weights, and reviewer decisions. The practical implementa-
tion pattern is to keep deterministic code, model prompts, and human review decisions in separate
files: code computes fields and packets, prompts draft summaries and questions, and reviewers
record acceptance, rejection, or escalation. This separation keeps the manuscript focused on the
framework while documenting how live deployments would connect to ODP, CIPO bulk feeds, OPS
enrichment endpoints, compliance repositories, and contract databases.
19

Table 6: Scoring sensitivity to weight perturbation. Each row perturbs one transparent weight
from Listing 2 by±20% and reports top-5 overlap and Kendall’sτrank correlation against the
baseline ranking, on the real CIPO corpus and the synthetic corpus. Highτvalues indicate the
ranking is stable and the weights are explanatory rather than finely tuned.
Real CIPO Synthetic
PerturbationTop-5τTop-5τ
Commercial weight +20% 5/5 0.886 5/5 0.962
Commercial weight−20% 5/5 0.873 5/5 0.962
SaaS weight +20% 5/5 0.877 5/5 0.981
SaaS weight−20% 4/5 0.876 5/5 0.962
Status bonus +20% 5/5 0.887 5/5 0.924
Expiry bonus +20% 4/5 0.887 4/5 0.905
Table 7: Structured-output quality for the local Qwen3.6 drafting layer. Reasoning is disabled so
the token budget produces the requested JSON rather than hidden chain-of-thought. Every live
call returned the five required keys (technical summary, candidate pathways, required evidence,
legal cautions, and reviewer questions) and parsed without repair.
Property V alue
Model qwen3.6:latest
Reasoning mode disabled (think=false)
Sampling temperature 0.1
Output format JSON (format=json)
Live structured calls 2
All required keys present 2/2
JSON parses without repair yes
Example response tokens 514
Example generation time 98.0 s
Concretely, the proof of concept records its own provenance. A generated manifest pins the
CIPO archive URL, its SHA256 hash, the number of XML entries seen and parsed, and the refer-
ence date used for expiry estimation. The full parsed corpus, the selected candidate output, the
evaluation tables, and one complete Qwen3.6 request and response are written to the repository
so the artifacts can be inspected without rerunning the model. The pipeline regenerates end to
end through the workflow, evaluation, and paper build steps, and a deterministic mode reproduces
every field except the model-drafted prose when no local model is available.
6 Discussion and Implications
6.1 Analytics and Innovation Management
Patent expiry analytics can support corporate white-space analysis, university technology scouting,
and incubator deal flow screening. By ranking expired and lapsing patents with explicit family-risk
annotations, the framework helps analysts prioritize review time rather than treating all public-
domain disclosures as equally usable. The framing in this paper is deliberately pathway-oriented:
the goal is to identify plausible business routes, not to solve a legal problem in isolation.
Trend detection adds temporal context: clusters of expiring patents in a domain may indicate
20

Table 8: Top-ranked synthetic records from the illustrative workplace safety corpus.
Record ID Juris. Status F amily Risk Comm. SaaS Opp.
SYN-US-007 US expired low 0.77 0.92 0.78
SYN-US-005 US expired low 0.80 0.87 0.77
SYN-US-002 US expired low 0.76 0.88 0.76
SYN-US-010 US active low 0.88 0.93 0.73
SYN-US-004 US active low 0.85 0.96 0.73
technology areas where early patents no longer block implementation but market demand has grown,
such as workplace safety analytics benefiting from modern cloud, IoT, and NLP infrastructure
unavailable at original filing dates.
The framework also changes the role of patent analytics from retrospective intelligence to op-
erational discovery. Conventional patent dashboards often ask what competitors are filing, which
assignees dominate a field, or where citation activity is concentrated. Expiry-oriented workflows
ask a different question: which disclosures are becoming easier to act on, and what business path-
ways could they support? This shift makes legal-status data, family coverage, customer fit, route
to market, and implementation metadata first-order analytic variables.
For innovation managers, this suggests a staged workflow. First, domain filtering and semantic
search identify a broad opportunity pool. Second, pathway classification translates each disclosure
into candidate routes such as software, services, training, data, licensing, or internal operations.
Third, legal-status and family-risk checks remove or downgrade records that are not ready for reuse.
Fourth, market screening produces hypotheses that can be tested through customer discovery,
prototyping, or expert review. The value of AI is strongest in the transitions between these stages,
where large volumes of technical text must be converted into concise, reviewable artifacts.
Scaling this workflow from one weekly archive to national or international collections requires
separating inexpensive corpus-wide computation from selective, higher-cost interpretation. Bulk
and incremental feeds can be normalized into partitioned warehouse tables, while deterministic
expiry rules, status mappings, classification filters, and precomputed embeddings reduce millions
of records to a much smaller candidate set. Family reconciliation and market-evidence joins can
then operate on that set, with local or hosted language models invoked only for the highest-
priority records and batched where infrastructure permits. Caching source snapshots, embeddings,
and generated packets prevents unnecessary recomputation, while run identifiers and versioned
scoring rules preserve auditability across updates. This funnel architecture makes processing cost
grow mainly with newly ingested or shortlisted records rather than requiring every patent to be
reinterpreted on every run.
This also reframes patent work as one instance of a broader class of archival research that leads
to action. Organizations already make decisions from other archives: compliance filings, inspection
records, public procurement notices, contract renewals, standards documents, litigation dockets,
grant databases, and regulatory submissions. These records are often public or semi-public, but
they are fragmented, technical, and difficult to convert into operational choices. Patent archives
have the same problem. Their value increases when they are connected to adjacent evidence about
obligations, buyers, renewal cycles, implementation constraints, and market demand.
6.2 Examples of Business Pathways
A single technical disclosure may support multiple pathways. In workplace safety analytics, an
expired mobile inspection patent-like record could support a SaaS pathway: a subscription platform
21

for inspections, audit trails, corrective actions, and dashboards. The same record could support
a service pathway: a consulting firm uses the disclosed workflow to deliver standardized safety
audits. It could support a training pathway: the disclosure becomes the basis for supervisor
checklists, simulations, and compliance workshops. It could also support an internal-tool pathway:
a manufacturer adapts the concept for its own safety operations without selling software externally.
Other pathway examples differ by asset type. A sensor-monitoring disclosure may lead to
an IoT integration kit, a managed monitoring service, or a data product that benchmarks safety
conditions across facilities. A semantic-analysis disclosure for incident reports may lead to a root-
cause analytics SaaS, an API embedded in existing EHS platforms, or an expert-review workflow
for insurers and regulators. A legacy notification disclosure may not justify a standalone venture
but may still support a low-cost emergency communication template for SMEs.
These examples show why the paper does not treat the problem as purely legal. Legal status
helps determine whether a pathway is worth deeper review, but it does not choose the customer,
pricing model, implementation stack, channel partner, or evidence needed to validate demand.
The pathway frame keeps the analytic focus on business action while preserving legal caution as a
necessary constraint.
The public-domain question is central but not sufficient. A patent may be expired, abandoned,
or otherwise no longer enforceable in one jurisdiction, while related family members, later improve-
ments, trademarks, copyright, trade secrets, regulatory obligations, or contractual restrictions still
matter. AI can help assess whether intellectual property appears to have moved into the public
domain by reconciling expiry dates, maintenance events, terminal disclaimers, family records, and
national-register status. It should express that result as a provenance-backed risk assessment, not
as an unconditional permission statement.
6.3 Entrepreneurship and SME Access
Entrepreneurs and SMEs often lack resources for comprehensive patent landscaping and FTO
review. An AI-enabled archive workflow lowers search and interpretation costs by generating plain-
language summaries and pathway-oriented business hypotheses. However, equitable access requires
deliberate design: if only well-resourced actors can operationalize public-domain knowledge, patent
archives may reinforce rather than reduce innovation inequality.
Tools intended for broad entrepreneurial use should expose scoring rubrics, provide exportable
pathway packets for advisors and legal counsel, and avoid implying that expired status equals
commercial freedom.
The strongest entrepreneurial use case is early-stage pathway screening rather than final go or
no-go decisions. A founder can use the system to learn what technical approaches have already
been disclosed, identify older solutions that may be newly practical, and prepare a more focused
conversation with engineers, customers, advisors, or counsel. This can reduce wasted search effort,
but it does not remove the need for market validation. Many expired patents describe technically
coherent inventions that failed because the timing, cost structure, regulatory context, channel
access, or customer demand was unfavorable.
The framework can also support teaching and incubator programs. Students and early-stage
teams can work from structured packets that include a technical summary, candidate pathway
interpretations, risk flags, and follow-up questions. This turns patent archives into learning objects
for opportunity recognition, while preserving the warning that a disclosure is not the same as a
viable venture.
22

6.4 Institutional and Public-Sector Use
Universities, public research organizations, and economic-development agencies have a distinct
interest in dormant technical knowledge. Technology-transfer offices usually focus on owned in-
ventions, active licensing portfolios, and sponsored research. Expired-patent archives widen the
search space to include public technical knowledge that can inform new research projects, student
ventures, regional innovation programs, or applied training.
Public-sector use also raises a policy question. Patent systems are justified partly by the bar-
gain between disclosure and time-limited exclusivity. If disclosed knowledge remains practically
inaccessible after expiry, the public side of that bargain is weakened. AI-mediated archive tools
can help realize the disclosure function of the patent system by improving findability, comprehen-
sion, and reuse. This is an archival and information-access argument, not only an entrepreneurship
argument.
The same logic applies to compliance and contract archives. A public agency or university
might use NLP to identify recurring compliance burdens, compare them with expired technical
disclosures, and identify where a low-cost workflow tool, training product, or shared service could
reduce administrative friction. A regional development office might combine procurement data
with expired patents to find technologies for which public buyers already reveal demand. In these
settings, the output is not simply a search result; it is a pathway packet that turns archival traces
into a testable intervention.
6.5 Archival Practice
Archivists and information scientists may view this framework as extending archival description into
actionable intelligence. Richer metadata, including legal status, family links, semantic clusters, and
implementation difficulty, could improve reuse of public technical records. Expiry events become
cataloging signals analogous to declassification or rights expiration in other archival domains.
This framing implies that patent archives should be described not only by bibliographic meta-
data and legal classifications, but also by reuse conditions. Provenance, jurisdiction, maintenance
status, family relationships, and uncertainty fields become part of the descriptive apparatus. Such
metadata can help users understand why a record appears in an opportunity list and what evidence
supports its status.
At the same time, archival enrichment must avoid overclaiming. A system that labels a record
as an opportunity is performing interpretation, not neutral cataloging. Interfaces and exported
packets should therefore preserve the distinction between source metadata, derived analytics, and
generated interpretation. This separation supports auditability and allows expert users to challenge
or revise the system’s assumptions.
6.6 Responsible AI Considerations
Generative components must be constrained by structured outputs and provenance tracking. Sum-
maries should cite source fields; uncertainty should appear in user interfaces and exports; human
review should be mandatory before commercial decisions. These principles align with responsible
AI expectations in high-stakes decision support contexts.
AI is already well suited to the pipeline tasks that make this kind of assessment possible. Re-
trieval models can connect a technical claim to semantically similar patents, procurement descrip-
tions, compliance obligations, and product categories even when the vocabulary differs. Extrac-
tion models can identify claim elements, deadlines, parties, jurisdictions, maintenance events, and
contractual obligations. Generative models can then draft plain-language explanations, pathway
23

Table 9: Risk categories and limitations for AI-enabled patent archive workflows.
Category Representative Limitations
Legal Expired status does not guarantee freedom to operate; family
members may remain active; PTA/PTE adjustments affect ex-
piry
Data API churn and rate limits; source disagreement; register lag;
Canada bulk-only access; scraping brittleness
NLP Claim parsing difficulty; hallucination in summaries; US/EPO-
heavy training bias; bilingual CA records
Ethical Public-domain knowledge may benefit well-resourced actors; re-
quires explicit uncertainty and human review
hypotheses, and reviewer questions. The value comes from chaining these steps under a controlled
schema so that each generated conclusion remains tied to source evidence.
For NLP-assisted decision-making, the important design choice is to separate candidate gen-
eration from decision authority. The system may recommend that a disclosure be reviewed for
public-domain reuse, that a contract cluster suggests buyer demand, or that a compliance filing
points to a recurring workflow problem. It should not decide, by itself, that a product is legally
clear, commercially viable, or ethically appropriate. A defensible pipeline gives analysts ranked
candidates, reasons, contrary signals, and unresolved questions.
Responsible design also requires attention to failure modes. A model may hallucinate product
features, simplify claim scope incorrectly, ignore active family members, or produce overconfident
rankings from incomplete legal-status data. These errors are not merely technical defects because
they can influence investment, product strategy, or legal exposure. The safest design pattern is to
make the system conservative by default: show uncertainty, require source links, penalize unresolved
family risk, and avoid binary clearance labels.
Finally, the framework should be evaluated with the people who would use it. Patent attorneys,
technology-transfer professionals, entrepreneurs, and archivists will judge usefulness differently.
Attorneys may prioritize provenance and legal caution, while entrepreneurs may prioritize speed
and product clarity. A mature system should support these different review modes without hiding
the underlying evidence.
7 Risks and Limitations
Table 9 summarizes major risk categories. We expand on the most critical limitations below.
7.1 Legal Uncertainty as a Pathway Constraint
Expired or lapsed status in one jurisdiction does not guarantee freedom to operate. Active family
members, continuations, reissues, design patents, trademarks, trade secrets, and regulatory ap-
provals may still affect commercialization. US expiry estimation is complicated by patent term
adjustment (PTA), patent term extension (PTE), and terminal disclaimers. INPADOC and aggre-
gator legal events are indicative rather than authoritative for non-EPO authorities.
Our framework therefore supports pathway review and due diligence; it does not replace counsel.
The point is to make legal uncertainty visible early enough that teams can choose, revise, or abandon
pathways before investing heavily.
24

7.2 Data Engineering Constraints
Patent data ecosystems experience API churn, rate limits, and migration events, as exemplified by
USPTO’s PEDS-to-ODP transition and intermittent PatentsView API availability. Canada’s bulk-
only access model requires scheduled ingestion rather than interactive scraping of HTML registers.
Cross-jurisdiction schema differences (ST.36, ST.96, USPTO JSON) increase normalization cost.
Remote database sync strategies should prefer licensed bulk and API paths over brittle scraping
of national office websites or commercial front ends.
7.3 Generative AI and Public Data Access
Generative AI introduces a new data-access paradox for public-interest analytics. The same models
that make large archives easier to search and interpret have also increased the commercial value
of bulk text, code, images, and platform data. In response, some data holders have tightened
APIs, raised prices, restricted scraping, or moved access into licensing arrangements. Twitter/X’s
API changes disrupted academic and public-interest research access [Murtfeldt et al., 2024], and
Reddit’s API changes were widely interpreted as part of a broader shift toward monetizing platform
data used by AI developers [Shakir, 2023]. Recent research on web scraping similarly notes that
generative AI has contributed to platforms restricting official data channels, pushing researchers
toward more legally and ethically complex collection methods [Brown et al., 2024].
This matters for patent and innovation-archive research because the relevant data are often
public in purpose but not frictionless in practice. Patent records, maintenance events, procurement
notices, compliance filings, standards references, and contract records may be intended for public
inspection, yet they depend on APIs, bulk files, search portals, rate limits, robots policies, and
institutional budgets. If data providers respond to AI scraping by closing endpoints or imposing
broad anti-bulk restrictions, legitimate analysis of public records becomes harder even when the
underlying records remain nominally public.
The risk is not only technical inconvenience. Reduced programmatic access can privilege large
firms that can pay for licensed data while excluding universities, SMEs, journalists, public agencies,
and independent researchers. It can also weaken reproducibility because researchers may be unable
to re-run a query, archive a source snapshot, or document why a record was unavailable at a later
date. For the framework proposed here, this means that data-access governance is part of the
research design: systems should prefer official bulk releases, respect published terms, cache source
snapshots where permitted, record access dates and endpoint versions, and distinguish unavailable
data from negative evidence.
The policy implication is that public data infrastructure should separate harmful bulk extrac-
tion from accountable public-interest analysis. Anti-scraping rules may be necessary to protect
privacy, server capacity, creator rights, and platform sustainability, but overly broad restrictions
can undermine the public value of records that were disclosed precisely so they could be examined.
For patent archives, the disclosure bargain is weakened if AI-driven access controls make public
technical knowledge practically inaccessible to the smaller organizations most likely to need search
and translation support.
7.4 NLP and Generative AI Limits
Claim language remains out-of-domain for general LLMs because patent claims are not ordinary
technical prose. They use dependencies, antecedent references, nested limitations, jurisdiction-
specific conventions, and intentionally broad drafting strategies. A model that produces a fluent
summary may still miss the operative limitation, collapse dependent claims into independent ones,
25

or describe the specification as if every disclosed embodiment were actually claimed. This matters
because pathway assessment depends on the difference between what a document teaches, what it
claims, what has expired, and what may still be protected elsewhere.
The appropriate use of NLP is therefore staged. First, retrieval and classification models can
reduce search cost by finding related patents, assigning likely technology domains, and connecting
patent text to adjacent records such as procurement descriptions, compliance filings, standards,
or contracts. Second, extraction models can identify entities, claim elements, dates, jurisdictions,
assignees, maintenance events, family members, and technical inputs or outputs. Third, generative
models can translate these structured inputs into plain-language summaries, pathway hypotheses,
reviewer questions, and caution flags. At each stage, the output should remain linked to source
fields so that a reviewer can inspect why the model produced a candidate pathway.
The reason for this staged design is that different pipeline tasks carry different risks. Seman-
tic retrieval errors may omit relevant prior art or overemphasize superficially similar documents.
Extraction errors may misread maintenance events, miss an active family member, or attach a
legal event to the wrong jurisdiction. Generative errors may invent product features, overstate
public-domain status, or turn an uncertain signal into a confident recommendation. These failures
are especially consequential when the output influences investment, product design, or freedom-to-
operate review.
Bilingual Canadian records require language-aware pipelines that can preserve English and
French source text, avoid mixing claim terms across languages, and handle cases where abstracts,
claims, or legal events are unevenly translated. Training data bias toward US and EPO corpora
may also underperform on smaller jurisdictions, older scanned records, or administrative event codes
that are poorly represented in general model training. For this reason, production systems should
evaluate models by jurisdiction and document type rather than assuming that strong performance
on US patent abstracts generalizes to Canadian legal-status reconciliation or pathway assessment.
Generative AI should not be used as an unbounded adviser in this context. It should oper-
ate inside schemas that require citations to source fields, explicit uncertainty labels, missing-data
indicators, and separation between source metadata, deterministic legal-status calculations, model-
generated interpretation, and human review. The practical goal is not to automate a final decision
about whether intellectual property is in the public domain. The goal is to make a complex archive
more navigable by producing a concise, evidence-linked packet that helps experts decide what to
verify next and why.
7.5 Evaluation Scope
The present paper develops architecture, reproducible workflow patterns, and a bounded CIPO
ST.96 proof of concept rather than a validated production system. The proof of concept now parses
an entire weekly archive and the evaluation in Section 5.7 reports automatic measures: corpus com-
position, status-derivation coverage, scoring sensitivity, and structured-output quality. These are
deliberately modest. They confirm that ingestion, scoring, and packet generation behave consis-
tently at archive scale, but they do not validate expiry accuracy against authoritative registers,
the fidelity of model summaries, pathway quality, or commercialization outcomes. In particular,
a single weekly release yields few expired records, and status derivation leaves roughly a quarter
of records in anunknownbucket, so the current evidence speaks to engineering reliability rather
than decision quality. Expert inter-rater assessment of summaries and pathways, register-checked
expiry precision, and longitudinal case studies remain future work.
For a production evaluation, we would treat expiry discovery as an information-retrieval task,
legal-status reconciliation as a data-quality task, and patent-to-pathway translation as an expert-
26

review task. Minimum evaluation artifacts should include a gold-standard sample checked against
national registers, inter-rater assessment of summary fidelity and pathway usefulness, ablation tests
for family-risk penalties, and longitudinal follow-up on whether generated pathway packets improve
analyst review time.
8 Conclusion
This paper presented an AI-enabled framework for discovering expired and lapsing patents, de-
tecting domain trends, and translating patent disclosures into entrepreneurship-oriented business
pathways. By treating patent expiry as a business signal, legal-status input, and archival transition,
we connect patent analytics, innovation archive theory, and responsible commercialization support.
The proposed architecture uses tiered ingestion from US, Canadian, and international sources;
a legal-status engine; an NLP pipeline; pathway scoring; and four workflow modules backed by
auditable Python patterns. Rather than relying on weak illustrative charts or tables, the paper
emphasizes how archival records can be converted into structured review packets that combine
patent status, pathway hypotheses, compliance or contract evidence, and unresolved legal and
market questions.
Future work includes live integration with USPTO ODP and CIPO bulk feeds, expert evalua-
tion of summary fidelity, cross-border family-risk benchmarking, and longitudinal case studies with
entrepreneurs and technology transfer offices. We hope this framework helps researchers and prac-
titioners view patent databases not only as legal search systems but as dynamic innovation archives
that AI can help activate, with explicit attention to uncertainty, equity, and expert review.
References
Nicholas Bloom, Mark Schankerman, and John Van Reenen. Identifying technology spillovers and
product market rivalry.Econometrica, 81(4):1347–1393, 2013. doi: 10.3982/ECTA9466.
Megan A. Brown, Andrew Gruen, Gabe Maldoff, Solomon Messing, Zeve Sanderson, and Michael
Zimmer. Web scraping for research: Legal, ethical, institutional, and scientific considerations.
arXiv preprint arXiv:2410.23432, 2024. URLhttps://arxiv.org/abs/2410.23432.
Canadian Intellectual Property Office. Ip horizons: Download intellectual property data,
2026a. URLhttps://ised-isde.canada.ca/site/canadian-intellectual-property-
office/en/canadian-intellectual-property-statistics/ip-horizons-download-
intellectual-property-data.
Canadian Intellectual Property Office. Pay maintenance fees: Applications and patents,
2026b. URLhttps://ised-isde.canada.ca/site/canadian-intellectual-property-
office/en/patents/maintain-your-patent-application-or-granted-patent/pay-
maintenance-fees-applications-and-patents.
Henry William Chesbrough.Open Innovation: The New Imperative for Creating and Profiting from
Technology. Harvard Business School Press, 2003.
Wesley M. Cohen and Daniel A. Levinthal. Absorptive capacity: A new perspective on learning
and innovation.Administrative Science Quarterly, 35(1):128–152, 1990. doi: 10.2307/2393553.
European Patent Office. Open patent services (ops), 2024. URLhttps://www.epo.org/en/
searching-for-patents/data/web-services/ops.
27

Google. Patents public data on bigquery, 2024. URLhttps://github.com/google/patents-
public-data.
Alan R. Hevner, Salvatore T. March, Jinsoo Park, and Sudha Ram. Design science in information
systems research.MIS Quarterly, 28(1):75–105, 2004. doi: 10.2307/25148625.
Mengke Hu, David Cinciruk, and John MacLaren Walsh. Improving automated patent claim
parsing: Dataset, system, and experiments.arXiv preprint arXiv:1605.01744, 2016. URLhttps:
//arxiv.org/abs/1605.01744.
Lekang Jiang and Stephan Goetz. Natural language processing in patents: A survey.arXiv preprint
arXiv:2403.04105, 2024. URLhttps://arxiv.org/abs/2403.04105.
Jieh-Sheng Lee and Jieh Hsiang. Patent classification by fine-tuning BERT language model.World
Patent Information, 61:101965, 2020. doi: 10.1016/j.wpi.2020.101965.
Lens.org. Lens api documentation, 2024. URLhttps://docs.api.lens.org/.
Mhlambululi Mafu. Expired patents as an opportunity for higher education institutions.Frontiers
in Research Metrics and Analytics, 8:1115457, 2023. doi: 10.3389/frma.2023.1115457.
Ryan Murtfeldt, Naomi Alterman, Ihsan Kahveci, and Jevin D. West. RIP Twitter API: A eulogy
to its vast research contributions.arXiv preprint arXiv:2404.07340, 2024. URLhttps://arxiv.
org/abs/2404.07340.
National Institute of Standards and Technology. Artificial intelligence risk management framework
(AI RMF 1.0), 2023. URLhttps://www.nist.gov/itl/ai-risk-management-framework.
Alan L. Porter and Scott W. Cunningham.Tech Mining: Exploiting New Technologies for Com-
petitive Advantage. Wiley, 2005.
Umar Shakir. Reddit’s upcoming API changes will make AI companies pony up,
2023. URLhttps://www.theverge.com/2023/4/18/23688463/reddit-developer-api-
terms-change-monetization-ai.
Homaira Huda Shomee, Zhu Wang, Sathya N. Ravi, and Sourav Medya. A survey on patent
analysis: From NLP to multimodal AI.Proceedings of the 63rd Annual Meeting of the Association
for Computational Linguistics, 2025. URLhttps://aclanthology.org/2025.acl-long.419/.
Society of American Archivists. Dictionary of archives terminology: Provenance, 2024. URL
https://dictionary.archivists.org/entry/provenance.html.
Kisik Song, Karp Soo Kim, and Sungjoo Lee. Discovering new technology opportunities based
on patents: Text-mining and F-term analysis.Technovation, 60-61:1–14, 2017. doi: 10.1016/j.
technovation.2017.03.001.
United States Patent and Trademark Office. Open data portal, 2026a. URLhttps://data.uspto.
gov/.
United States Patent and Trademark Office. Patentsview transition guide, 2026b. URLhttps:
//data.uspto.gov/support/transition-guide/patentsview.
World Intellectual Property Organization. Guidelines for preparing patent landscape reports, 2015.
URLhttps://www.wipo.int/publications/en/details.jsp?id=3938.
28

World Intellectual Property Organization. Patentscope, 2024. URLhttps://www.wipo.int/en/
web/patentscope.
Geoffrey Yeo. Concepts of record (1): Evidence, information, and persistent representations.The
American Archivist, 70(2):315–343, 2007. doi: 10.17723/aarc.70.2.u327764v1036756q.
Siyeong Yun, Kisik Song, Chulhyun Kim, and Sungjoo Lee. From stones to jewellery: Investigating
technology opportunities from expired patents.Technovation, 103:102235, 2021. doi: 10.1016/j.
technovation.2021.102235.
A Local LLM Pathway Example
This appendix reproduces one complete drafting-layer exchange from the real-data proof of concept.
The record is CA2616010, “Medication Compliance System and Associated Methods,” a granted
CIPO patent whose twenty-year term estimate places it about eleven days from expiry as of the
reference date, making it a genuine expiry-discovery candidate. The prompt is constructed only
from parsed patent text and instructs the model to return strict JSON without asserting legal
clearance. The response was produced by Qwen3.6 through a local Ollama instance with sampling
temperature 0.1, JSON-constrained output, and hybrid reasoning disabled.
Listing 8: Prompt sent to the local model (abstract and claims truncated for space).
1Return strict JSON with keys technical_summary , ca nd id at e_ pa th wa ys ,
2required_evidence , legal_cautions , and r e v i e w e r _ q u e s t i o n s .
3Use only the supplied patent text . Do not claim legal cl ea ra nc e .
4
5Patent : CA 26 16 01 0
6Title : M E D I C A T I O N C O M P L I A N C E SYSTEM AND A S S O C I A T E D METHODS
7Status : Granted and Issued
8Es ti ma te d legal status : a c t i v e _ o r _ p e n d i n g
9Abstract : A system for m o n i t o r i n g m e d i c a t i o n c o m p l i a n c e in a patient
10includes an e l e c t r o n i c pill that includes a drug - t r a n s p o r t i n g device
11and an antenna p o s i t i o n e d on a surface of the drug - t r a n s p o r t i n g device .
12A detector is p o s i t i o n a b l e external a g a s t r o i n t e s t i n a l tract of a
13patient for d et ec ti ng a presence of the antenna ...
14Claims excerpt : What is Claimed is : 1. A method for making an e l e c t r o n i c
15pill adapted for m o n i t o r i n g for m e d i c a t i o n c o m p l i a n c e in a patient ...
Listing 9: Structured JSON returned by Qwen3.6 (lists abbreviated).
1{
2" t e c h n i c a l _ s u m m a r y ": " The patent de sc ri be s an e l e c t r o n i c pill system
3for m o n i t o r i n g m e d i c a t i o n c o m p l i a n c e . The core co mp on en t is an
4i n g e s t i b l e m e d i c a t i o n delivery device equipped with an antenna on
5its exterior surface ... The system includes an external detector
6capable of sensing the presence of the antenna within the patient ’ s
7g a s t r o i n t e s t i n a l tract ." ,
8" c a n d i d a t e _ p a t h w a y s ": [
9" I n g e s t i b l e te le me tr y systems for p h y s i o l o g i c a l m o n i t o r i n g " ,
10" Smart pill t e c h n o l o g i e s for ad he re nc e tracking " ,
11" External - to - internal wireless c o m m u n i c a t i o n devices " ,
12" Flexible s ub st ra te e l e c t r o n i c s for b i o m e d i c a l a p p l i c a t i o n s "
29

13] ,
14" r e q u i r e d _ e v i d e n c e ": [
15" Claims d et ai li ng the specific antenna ma te ri al s " ,
16" Method for wrapping the flexible su bs tr at e and antenna " ,
17" S p e c i f i c a t i o n s for the external detector " ,
18" Details on t em po ra r y power storage in the pill "
19] ,
20" l e g a l _ c a u t i o n s ": [
21" Based solely on the provided text ; not legal advice or an FTO
22opinion ." ,
23" Status is ’ active_or_pending ’; verify m a i n t e n a n c e and expiry with
24official records ." ,
25" Claims are limited to the de sc ri be d method and c o n f i g u r a t i o n ." ,
26" Do not rely on this summary for c o m m e r c i a l cl ea ra nc e ."
27] ,
28" r e v i e w e r _ q u e s t i o n s ": [
29" How do the antenna ma te ri al s affect r e g u l a t o r y c l a s s i f i c a t i o n ?" ,
30" What is the o p e r a t i o n a l range of the external detector ?" ,
31" Does power storage allow reliable data t r a n s m i s s i o n ?" ,
32" How does s ub st ra te wrapping affect d i s s o l u t i o n rate ?"
33]
34}
Two properties of this exchange support the design choices in the main text. First, the model
produced well-formed JSON that populated every required field, so it can be consumed directly by
the packet schema without post-hoc repair. Second, and more importantly, the useful content is
interpretive rather than authoritative: the summary and pathways aid orientation, but the legal
cautions and reviewer questions are exactly the items the framework insists must be verified by a
human before any commercial or freedom-to-operate decision. The deterministic fallback produces
the same field structure with template text when no local model is available, so downstream tooling
behaves identically whether or not the model is present.
30
