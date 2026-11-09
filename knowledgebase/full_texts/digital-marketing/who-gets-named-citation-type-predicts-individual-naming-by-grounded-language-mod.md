---
title: 'Who Gets Named: Citation Type Predicts Individual Naming by Grounded Language Models, and a Roster
  Instrument Captures 0.5% of It'
url: https://arxiv.org/abs/2607.23893
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors: []
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.23893
pages: 28
chars: 87670
fetched_at: '2026-11-08T13:21:53+00:00'
kb_version: 1
---

# Who Gets Named: Citation Type Predicts Individual Naming by Grounded Language Models, and a Roster Instrument Captures 0.5% of It

Who Gets Named: Citation Type Predicts Individual Naming by
Grounded Language Models, and a Roster Instrument Captures
0.5% of It
Dmitrij Żatuchin 1
1Rankfor.AI OÜ, Tallinn, Estonia
July 2026
Abstract
Prior work on AI brand visibility measures the firm: does a model recommend a company, and
does that track its reputation. This study asks the question one level down, in categories where
the buyer picks a person. It issued 2,400 grounded API calls on 24 July 2026: 120 buyer-intent
prompts, four models (GPT-5.6 Sol, Gemini 3.6 Flash, Perplexity Sonar Pro, Grok 4.5), five
iterations each, four European markets and five query languages. Every response was coded for
whether it named an individual professional, by a rule cascade that never consults a roster and
that drops detections resolving to a same-named American city (precision 96.9%; recall 61.7%
against roster ground truth, so every rate below is a lower bound). All inference corrects for
clustering within prompt: on the primary outcome the intraclass correlation is 0.258, the design
effect 5.90 and the effectiven407 against a nominal 2,400.
Models named an individual in 25.8% of responses. Category dominates: real estate 35.4%
and car dealerships 32.9% against insurance 9.1% (χ2 = 159.3, p = 5.8 × 10−8 after the design-
effect correction). Models differ four-fold, from Grok 38.0% to Gemini 9.3%. Citation type
predicts naming and citation volume does not: naming responses cite the individual’s own site
2.6 points more often (95% CI+1.4to+3 .9) and category portals 4.3 points more often, cite
social platforms less, and cite firm-owned pages at the same rate (44.1% against 45.5%). On nine
matched translation pairs, English prompts named an individual in 36.7% of responses against
15.6% for the same question in the local language (OR 3.14; clusteredp = 0.074, so the direction
is clear and the design cannot close it). A 939-person roster built from public LinkedIn search
matched 128 of 27,293 name-shaped mentions (0.47%); 26 of the 939 people were ever named;
and the roster-derived rates, 0.0% to 25.4%, measure that overlap. Roster-based measurement of
individual AI visibility sees a small and unrepresentative slice of what models do.
1 Introduction
A generative model answering a buyer’s question performs an act of gatekeeping: of everyone and
everything that could satisfy the query, it surfaces one name. Work on AI-mediated brand visibility
has established that this happens at the level of the firm, and that it diverges from firm reputation
in ways that matter commercially [Żatuchin, 2026a]. Whether the same act operates at the level of
the individual is unmeasured, and a large set of commercial categories turns on it: the ones where
the buyer’s decision is “which person.”
Real estate transactions, vehicle purchases and insurance placement share a feature: the buyer
picks a specific human being to act for them. A query such as “best real estate agent in Warsaw”
1
arXiv:2607.23893v2  [cs.IR]  1 Aug 2026

asks for a name. Whether a grounded model supplies one, and what decides that, is what this paper
measures.
The Recommendation Gap.The construct is the distance between two quantities: how often
a generative model recommends an entity, and how far the entity’s public standing predicts that
it should. Public standing is what independent sources record: review scores, press coverage,
professional registration, standing among peers. Recommendation is the share of answers, across
repeated draws from one prompt, that name the entity in reply to a buyer-intent question. The
gap is what remains of recommendation once standing is accounted for. Measuring it takes three
commitments, fixed before collection: a prompt set a buyer would plausibly type; repeated sampling
of every prompt, because one call to a non-deterministic model is one draw; and a naming rule, fixed
in advance, that decides what counts as a recommendation. Prior work fixes the entity as a firm
[Żatuchin, 2026a]. This paper fixes it as a person and measures the recommendation term alone,
holding standing constant by design: the question is whether the model names anyone at all. This is
a naming-rate study inside the Recommendation Gap programme, and it computes no gap.
Two adjacent brand-level constructs sit nearby. The AIVO Paradox measures visibility against
purchase-recommendation win rate inside one model conversation [de Rosen, 2026], and the Linkage
Gap measures what a model holds about a brand against what it deploys at the recommendation
turn [Sheals & de Rosen, 2026]. Both compare two model behaviours. The Recommendation Gap
compares a model behaviour against an external record of standing.
Three research questions organise the study.
• RQ1 (naming rate).In hyperlocal, person-centric buying categories, what share of grounded
model responses name an individual professional, and what moves that share: category, market,
model, or query language?
• RQ2 (source predictors).Does the composition of a grounded response’s citations predict
whether it names an individual?
• RQ3 (cross-model agreement).When more than one model names someone, do they agree
on who?
A fourth question arrived from the data and is answered in Section 5: what does a roster-based
instrument measure when it is pointed at this problem, and how much of the answer does it see?
2 Related work
2.1 Brand-level AI visibility measurement
A body of measurement work establishes that generative model recommendations diverge from
classical search rankings and from firm reputation. A twelve-brand study across five industries
found the correlation between narrative reputation quality and AI recommendation frequency
indistinguishablefromzero(Spearman ρ = 0.056)[Żatuchin,2026a]. Afifty-brand, five-industrystudy
using five-iteration replication (Section 2.4) found a mean Gini coefficient of 0.28 for recommendation-
share concentration and 41.6% cross-model agreement on the top-recommended brand across three
model families [Żatuchin, 2026b]. A 128-brand, twelve-market, thirteen-language citation-provenance
study found that 85.7% of the URLs a grounded model cites when discussing a brand point to
third-party domains the brand does not control [Żatuchin, 2026c].
2

Larger surveys reach the same shape at scale: 100,000 prompt responses across 100 brands
[Kumar, 2026], 160,860 citation records across eight Chinese-language platforms [Zhen et al., 2026],
and 252,000 paired retrieval trials isolating which document features win a citation [Vishwakarma et
al., 2026]. An analysis of 2.8 million results across 243 countries places AI search inside the wider
information market [Aral et al., 2026], and separate work shows that incumbent brands hold an
advantage in what a model recommends [Chu & Hou, 2026]. Audit work on the citation layer itself
finds that source-cited answers support their claims less often than their presentation implies [Venkit
et al., 2025], and that Google’s AI Overviews carry the same problem in a consumer-health domain
[Hu et al., 2025]. Entity-level audit frameworks now exist for bias in model outputs [Elbouanani et
al., 2026]. Throughout, the mechanism under study is brand-level, and no named individual human
is the object of recommendation.
2.2 Individual-level naming in generative models
Individual-level naming has been audited before. Goethals et al. [2025] score GPT-4, Claude and
Llama-3 on whether they name real Nobel laureates and leading figures in a field, and report
correctness, refusal and gender parity. Barolo et al. [2025] score six open-weight models against
American Physical Society and OpenAlex records; Espín-Noboa & Méndez [2026] extend that audit
to 22 models under temperature, prompt-constraint and web-search-grounded conditions; Sánchez-
Guzmán et al. [2026] vary persona language and location across 43 models and six disciplines. All
four ask who a model names when asked for an expert, and all four ask it about scholars. Wang et
al. [2026] verify the output of four commercial people-search products against live web evidence, and
Baum [2026] measures naming of political candidates. Sumbilon [2026] tests one professional entity
across six answer engines and reports how much independent corroboration each engine needs before
it names anyone.
Two literatures sit closer to a purchase. In industry, FlyDragon [2026] reports an average 8.4%
AI citation share for United States real estate agents across 12,400 responses, five answer surfaces
and 192 metropolitan areas at five iterations per query. It publishes neither its prompt set, its agent
roster, its matching rule nor its model versions. A trade column by one of its authors carries the
result to practitioners [Darani, 2026]. Wilde [2026c] and companion studies [Wilde, 2026b,a] test
515 Miami-Dade and Broward businesses and 379 further health practices on local recommendation
prompts and find 98.8% to 99.6% never named, taking the business as the unit of naming. A vendor
benchmark covers professional services on 40 buyer questions and again scores firms [Authority
Specialist, 2026], and a simulation study evaluates legal-service discoverability without live model
calls [Clarity Infra Research Group & Chen, 2025]. Sarkhedi [2026a] published an open protocol
for auditing personal brand visibility in June 2026, and Sarkhedi [2026b] a six-signal framework for
it, neither with a primary measurement attached; a companion practitioner framework reports 523
consultancy engagements and queries no model [Sarkhedi, 2026c]. Singh [2026] follows one individual
through seven months of entity disambiguation. Carr [2026] registered a five-model study of local
business recommendation in February 2026 that had posted no data, code or materials when this
paper was written.
This study takes the question to the individual inside commercial buyer-intent categories, where
the named person is the object of the purchase decision, and outside the United States, across four
European markets and five query languages. To the author’s knowledge it is the first measurement
of individual-level naming by grounded generative models in commercial buyer-intent categories that
publishes its prompt set, its roster construction rule, its detection rule and its matching procedure,
and the first conducted outside the United States. The disclosure qualifier carries the weight:
FlyDragon holds the ground on individuals in a commercial category and withholds the method.
3

2.3 Individual-level algorithmic visibility
A distinct literature examines algorithmic visibility of individual workers on digital platforms as
a labour-market outcome. Algorithmic management research treats platform-mediated visibility,
task allocation and ranking as core mechanisms by which platform workers are governed, a body of
work large enough to have supported a 103-source interdisciplinary systematic review [Chigbu, 2026].
Within it, platform-mediated visibility is a site of demographic disparity. A study of 108 online
freelancers found systematic gender- and race-based patterns in how digital labour platforms make
individual workers visible to clients [Munoz et al., 2023]. A large observational study of TaskRabbit
and Fiverr put the disparity at an incidence rate ratio near 0.90 on review counts [Hannák et al.,
2017]. Generative systems carry demographic structure of their own: a cross-model audit of 41
occupations finds stable race and gender patterns in the personas models produce [van der Linden et
al., 2025].
That literature has been extended to generative answer surfaces for scholars and public figures
[Goethals et al., 2025, Barolo et al., 2025, Espín-Noboa & Méndez, 2026, Sánchez-Guzmán et al.,
2026] and to local businesses as entities [Wilde, 2026c]. It has not been extended to commercial
service professionals as individuals, where the visibility act sits inside a purchase decision. Section 8
states what this design can and cannot say about the demographic dimension.
2.4 The dice-roll replication standard
Because a single call to a non-deterministic generative model is a single draw from a distribution, this
study adopts the replication design established and power-analysed across five prior studies, roughly
190,000 observations [Żatuchin, 2026d]. That work showsn = 5replications detects only large effects
(d >1.2, power > 0.80), with metric convergence reaching 80% of its asymptotic value byn = 7and
test-retest reliability crossing 0.70 atn≥ 8. Independent work reaches the same conclusion from
other angles: prompt paraphrase alone moves measured visibility enough to need a confidence-aware
protocol [Kirichenko, 2026], prompt wording shifts brand visibility across 288 human-written prompts
[Ehrlinspiel et al., 2026], and identical client profiles draw different professional advice on repeat
asking [Agliata & Hasso, 2026]. This study uses then = 5tier throughout. Section 3.6 shows that
clustering within prompt bounds precision here.
2.5 Language and morphology in grounded output
A line of work measures cross-language divergence in grounded brand recommendations directly. A
sixty-six-brand study spanning twelve European languages (35,640 responses, three models) found
that AI-constructed brand reputation varies by query language, and that switching from English to
a brand’s own language raises recommendation frequency far more for local brands (+0.80) than for
global corporations (+0.15) [Żatuchin et al., 2026e]. A variance-components decomposition (12,933
responses, 20 brands, 8 languages, 3 models) found query language alone explains 26.5% of response
variance against brand identity’s 1.5% [Żatuchin, 2026f]. Section 4.4 extends that work to whether
an individual gets named at all.
Polish and Lithuanian inflect personal surnames by sentence role, which puts entity boundaries
out of step with token boundaries and makes the matching task need morpheme-level treatment
[Bareket & Tsarfaty, 2021]. No prior work in this literature reports a name-matching procedure
designed for surnames that inflect by grammatical case. Section 3.4 reports the check this study ran
and states its limit; Christen [2006] benchmarks the personal-name matching techniques a general
solution would use.
4

3 Method
3.1 Design and prompts
The design crosses four markets (Poland, Ireland, the Netherlands, and a combined Lithuania/Estonia
“Baltics” market, treated jointly because each economy is individually small and because prior work in
this programme already treats the Baltic states as one unit [Żatuchin, 2026a]) with three categories:
real estate agents, car dealership sales representatives and insurance brokers.
For each (market, category) pair the study used seven English buyer-intent prompts: five short
generic variants (“Who’s the best [category] in [city]?”, “Recommend a [category] in [city]”) and
two attribute-carrying variants, an expat-buyer framing and a first-time-buyer framing. That split
matches this programme’s own finding on the length and attribute-carrying share of real buyer
prompts [Żatuchin, 2026a]. Poland, the Netherlands and each Baltic city also received three local-
language prompts per category: two short generic variants and one attribute-carrying variant, in
Polish, Dutch, Lithuanian and Estonian. Ireland received English prompts only. This gives 120
unique prompts: Poland 30, Ireland 21, Netherlands 30, Baltics 39. Appendix A prints all 120
verbatim.
Nine English prompt slots have an exact local-language translation in the same city and category,
and the rest do not. Section 4.4 treats those nine as the inferential language test and the full set as
descriptive.
3.2 Models and collection
Four providers span the commercially deployed grounded-model families as of July 2026: GPT-
5.6 Sol (OpenAI), Gemini 3.6 Flash (Google), Perplexity Sonar Pro, and Grok 4.5 (xAI). Each
model identifier and grounding mechanism was live-verified against the provider’s production API
immediately before collection, with a single test call confirming a grounded response carrying citation
metadata.
A fix made mid-collection.The first 600 OpenAI calls used the Chat Completions end-
point. Chat Completions does not support genuine web search for the GPT-5.x family: the
web_search_options parameter is restricted to a separate family of dedicated*-search-preview
models, so those calls were an ungrounded, training-knowledge-only pass, inconsistent with the
other three providers. The implementation was corrected to the Responses API with a genuine
web_search tool invocation, and all 600 OpenAI calls were re-collected before any analysis reported
here. The correction is disclosed because the failure mode is generic and cheap to repeat: an API
endpoint silently not supporting the grounding tool a researcher assumes it does.
Each (prompt, model) pair was queried five times, giving120× 4 × 5 = 2,400calls. All 2,400
were issued in one continuous session on 24 July 2026.
Every call requested live web-search grounding. Grounding did not always arrive. Of the 2,400
responses, 2,223 (92.6%) carry at least one citation and 177 (7.38%) carry none. The shortfall is
concentrated. 137 of the 177 are OpenAI, which returned no citation on 22.83% of its 600 calls (95%
CI 19.65 to 26.36), against Gemini 31, Perplexity 7 and Grok 2. Zero-citation responses are also
uneven by market: Ireland 78 of 420 (18.6%), Poland 52 of 600, Netherlands 29 of 600, Baltics 18 of
780. Every market-level comparison below therefore carries a differential-grounding component, and
Section 3.6 reports a grounded-only sensitivity run.
A further 140 responses, all OpenAI, ask a disambiguating question in place of an answer (Ireland
66, Poland 43, Netherlands 31; operational rule: under 700 characters and containing a question
mark). They ask which Dublin, Warsaw or Amsterdam the user means, which is itself a result and is
5

reported in Section 4.6. Four clarifying responses also carry citations, so the two exclusions overlap
by four and the analysis population excluding both is 2,219 (92.5%).
3.3 The professional roster
The study also built a roster of 939 named individuals across the same four markets and three
categories, by LinkedIn people search in Classic mode using keyword and location facets. A Sales
Navigator seat, which would have allowed further faceted filtering, was not available. Table 1 gives
the per-cell sizes.
Table 1: Roster composition by market and category.
Market Real estate Car dealers Insurance
Poland 98 79 78
Ireland 73 75 71
Netherlands 89 75 75
Baltics (LT+EE) 80 79 67
Inclusion rule.A candidate entered the roster if and only if, at collection time, a citable,
resolving linkedin.com/in/ profile URL named the individual in the target role. The rule is
deliberately narrow, for two reasons independent of statistical convenience. It keeps every roster row
traceable to one external URL, so a removal request is a one-line action. It also keeps the sample
inside the most defensible category of public professional data under the Art. 6(1)(f) legitimate-
interest basis: data the subject or their employer published so that a prospective client would find it.
No purchased contact records, no enrichment-tool outputs without a resolving public profile, and no
source that is not itself a citable public URL entered the file. This is a convenience sample bounded
by LinkedIn’s own search surfacing, and Section 5 reports what that turns out to mean.
What the roster is, measured.The roster carries no city field. Itslocation column holds
the subject’s self-declared LinkedIn region, and for 393 of 939 rows (41.9%) that string is the bare
market name; 497 rows (52.9%) resolve below country level. Counting a row as city-bounded when
the prompted city appears inlocation or headline, and allowing the Polish stemwarszawand
the Lithuanian genitiveVilniaus, gives Poland 15.7%, Ireland 16.4%, Netherlands 23.4% and the
Baltics 35.0%. Ireland’s figure cannot be read: its one named row carries the market-name fallback,
so Ireland supplies no test of city-boundedness.
Feeding every roster name through the extractor inside a neutral carrier sentence, 759 names
(80.8%) recover exactly, 46 (4.9%) only under the fuzzy fallback, and 134 (14.3%, 95% CI 12.2 to
16.6) never recover. The rate is not uniform: Poland 5.1%, Ireland 14.6%, Baltics 4.0%, Netherlands
33.5%. The dominant cause is the Dutchtussenvoegsel: 67 of 239 Dutch rows carry a lower-case
particle and all 67 are unrecoverable. The rest are names above three tokens (29), punctuation or
emoji in the name field (24), and non-ASCII initial capitals (7). The 14.3% is a floor, measured in
the friendliest carrier position.
Thirty rows (3.2%) trade under a firm name built from the individual’s own name. For those the
person-versus-firm distinction is undecidable from the output string alone, and the bias runs toward
under-counting: the firm string carries extra capitalised tokens (“SurnameMakelaardij”), which the
extractor emits as a three-word span matching no roster row. Three of the 26 individuals a model
ever named hold such a firm.
6

3.4 Two ways of deciding that a response named someone
Roster matching (the instrument).Model output was scanned for name-shaped spans and
matched against the 939-person roster by exact normalised string match, with a fuzzy fallback
(surname edit distance≤ 1, given-name prefix match). This produced 128 matched mentions across
114 of the 2,400 responses. Fifteen of the 128 are fuzzy matches, not exact ones, and ten responses
rest entirely on a fuzzy match; restricting to exact matches moves the Baltics rate from 13.97% to
12.69% (99/780) and leaves the other three markets unchanged, so nothing reported here depends
on the fuzzy rule.
Because Polish and Lithuanian inflect surnames by sentence role, a stemmed re-check ran on the
Polish subsample before any market difference was treated as real. Eight hundred and seventy name-
shaped strings surviving a company-and-generic-phrase filter, drawn from 2,779 distinct unmatched
strings and 6,976 raw mentions, were reduced to five-character stems on both given name and
surname and compared against a stemmed Poland roster. This produced zero additional matches. A
positive control confirmed the pipeline recovers repeated identical matches in the Baltics subsample.
The check is reported because it ran, and its limit is stated with it: it tested the 870 strings a
company-and-generic filter had already passed, and that filter is the kind of instrument whose
coverage is in question. Five-character truncation was chosen because it over-matches, which is what
a test for a false zero needs; a general solution should use the phonetic and similarity-based methods
benchmarked by Christen [2006].
A second defect is measured. The shipped matcher used an ASCII word class, so any name
beginning with a non-ASCII capital could never match. Scanning every response for the literal roster
names of its own market and category, diacritic-folded and word-bounded, finds 43 occurrences across
six people that the matcher never recorded. One Baltic car-sales professional is named unambiguously
as a person in 19 separate responses and scores zero every time. Correcting it moves Baltics real
estate from 25.38% to 25.77%, Baltics car dealers from 16.15% to 19.62%, and Netherlands car
dealers from 0.00% to 1.00%. Counting the eponymous-firm strings as person namings instead takes
Netherlands real estate to 10.5% and the Dutch market total to 3.8%, which is the honest upper
bound on the same cell.
Roster-free detection (the primary outcome).The roster matched 128 of 27,293 name-
shaped mentions the models emitted, 0.47%, and 128 of 1,876 spans the detector resolves to
individuals, 6.8%. Any outcome defined by roster membership therefore measures the intersection of
two populations. The primary outcome is a rule cascade applied to the response text, which never
opens the roster. Six stages run in order: markdown stripping; candidate generation, meaning two
or three capitalised tokens plus nobiliary particles; a shape gate; a lexical gate against corporate,
geographic and generic blocklists in five languages plus street suffixes; a company-adjacency test on
the whole enclosing capitalised run; and a positive-evidence requirement. That last stage demands a
given-name gazetteer hit, a role apposition, or an address verb or title before the span. An eponym
rule then removes spans that are firm names shaped like personal names, tested against company-
shaped runs in the same response and market and against brand keys derived from cited domains.
A final stage drops detections resolving to a business or person in a same-named American city:
Dublin, Ohio; Warsaw, Indiana; Amsterdam, New York. Each such domain was adjudicated against
the live site, the stated address and, where the site was unclear, a company register. That stage
defines the geo-corrected outcome used throughout. Appendix B states the cascade as pseudocode.
Two measured properties bound everything that follows.Precisionis 96.9% (155 of 160 detections
audited in two independent passes, 95% CI 92.9 to 98.7).Recallagainst the 128 roster mentions is
61.7% (Baltics 62.6%); the misses are gazetteer gaps on given names such asXander,Raimondand
Leho. Every naming rate below is a lower bound, and the gap is larger in the Baltics than elsewhere,
7

which works against the market comparison in Section 4.1. A corpus-induced gazetteer was tested
as a recall fix and rejected: it added 86 names, all spurious, and inflated every market.
3.5 Citation source classification
Every citation URL was reduced to a registrable hostname, giving 20,580 citations across 2,182
distinct domains. The classification reported here replaces the one applied at collection time, and
both are described, because the difference changes the answer to RQ2.
What the collection pipeline did.The collection-time classifier tested each hostname against
an allowlist of roughly forty domains and one registry-hint pattern, and returnedemployer-owned
page as its else-default. Against 2,182 observed domains that default absorbed 2,110 of them and
17,945 of 20,580 citations (87.2%), includingreddit.com, the single most-cited domain in the corpus
at 746 citations. Three substring bugs compound it: the registry hintfi.ee matches delfi.ee
(4 citations), the bare hintregister matches inforegister.ee (35), and the social-domain entry
x.com matches carfax.com (21), yandex.com (10) and global.remax.com (2). The failure mode
deserves a name: an allowlist with a substantive else-default reports its own default category as a
finding.
The replacement.All 2,182 domains were classified under a twenty-category taxonomy set
out in a written coding manual, with a controllability axis (owned, paid, earned, not-acquirable)
recorded alongside. The 800 highest-volume domains, carrying 18,201 citations (88.4% of the corpus),
were classified one by one against the live site; the remaining 1,382 were assigned by published
rule and flagged low-confidence. The taxonomy separates three things the oldemployer-owned
page bucket conflated: the firm’s own site (firm-site), the individual professional’s own site
(individual-site), and category portals (vertical-portal). Four hundred and seventy-eight
domains sit in unclassified; nothing defaults into a substantive category. The classification is
LLM-assisted and is described as such in the deposit.
Adversarial audit.An independent pass re-read all 100 top-ranked domains against the
cited paths and five live pages, and found no third-party platform coded as a firm’s own page. A
portal-signature test across all 472firm-site and individual-site rows in ranks 1 to 800 found
no host coded as a firm showing platform behaviour. Eleven rows in ranks 1 to 800 carry a label
the audit would change, together 179 citations, 0.87% of the corpus. In the rule-coded tail, one
rule labelled 359 hosts as a firm’s own site because a trade word appears in the domain string,
carrying 650 citations. That reproduces the original defect in miniature. Demoting every such row
to unclassified leaves all four surviving contrasts in Section 4.3 unchanged to two decimal places,
and moves onlyfirm-site, a null under both codings.
The individual-site boundary.A later pass withdrew the inference that a person’s name
in a domain, or a sole-trader registration, implies that one person delivers the service. A business
named after someone can employ staff. Under a corrected rule requiring positive evidence of solo
operation, verified against each live site and its sitemap, 41 of 70individual-site domains left
the class, which fell from 70 domains and 706 citations to 29 and 319. The contrast resting on that
boundary lost about one percentage point and kept its sign in every treatment of the unresolved
rows (Section 4.3).
Employer identity.Testing whether naming responses cite the named person’s own employer
requires resolving each named individual to an employer domain, which the roster headline supports
for 313 of 939 individuals (33.3%; Ireland 53.0%, Baltics 51.3%, Netherlands 30.5%, Poland 3.1%).
On the 26 individuals ever named, audited one by one, citations landing on that person’s own
employer domain number 34 of 975 (3.49%, 95% CI 2.10 to 5.13), and 25 of 114 naming responses
(21.9%) cite it at least once. For 51.1% of person-citation pairs the roster row names no employer at
8

all, so the claim is undefined for the majority of them.
3.6 Statistical approach
Each of the 120 prompts was answered 20 times (four models, five iterations), so responses are not
independent. On the primary geo-corrected outcome the intraclass correlation within prompt is
0.258, which gives a design effect of1 + (¯m−1)ρ = 5.90at ¯m= 20and an effective sample size of
407 against a nominal 2,400. On the roster-matched outcome the same three quantities are 0.266,
6.06 and 396. Clustering is what bounds precision in this design. The nominaln overstates it more
than fivefold.
Single proportions carry Wilson intervals, and zero cells carry Clopper-Pearson bounds. Between-
prompt comparisons are widened by the design effect before testing (Rao-Scott), with the design
effect computed within arm and size-weighted. Pooling the two arms is wrong here: every prompt
sits entirely inside one arm of every between-prompt contrast, so a pooled design effect absorbs the
arm mean difference into between-prompt variance and penalises large effects hardest. The two
estimators differ materially: on the Vilnius language contrast they give 3.83 within arm against 5.35
pooled.
Model is the exception. Because model is crossed with prompt, prompt clustering acts as blocking
for model contrasts and improves their precision, so a between-cluster design effect would correct
in the wrong direction. Model contrasts are tested by exact within-prompt randomisation (20,000
permutations of the outcome inside each prompt, model labels fixed) and by Cochran-Mantel-Haenszel
stratified on prompt, and the two agree.
Families of comparisons are corrected by Holm. Citation-composition intervals come from a
cluster bootstrap that resamples whole prompts, 10,000 draws, seed 20260726. A bootstrap over
responses understates those intervals by roughly a third. Where an arm contains zero events (Poland
under the roster instrument, 0 of 600) the report gives the Clopper-Pearson upper bound and the
rule of three, because both GEE and unpenalised logistic regression return separation artifacts on
that cell.
The multivariable model is a logistic mixed model with a random intercept on prompt, fitted by
variational Bayes, with market, category, model and query language as fixed effects (Table 7). A
GEE with an exchangeable working correlation clustered on prompt is fitted alongside as a check on
the standard errors.
Five sensitivity analyses run alongside the primary results. They restrict to the 2,223 responses
returning at least one citation; to the 2,219-response analysis population, which also drops the 140
clarifying responses; to exact-match-only roster matching; to the detector without its geographic
stage; and to the citation taxonomy with the tail rule demoted. None reverses a reported direction.
4 Results
4.1 RQ1: category dominates, market mostly does not separate
Models named an individual professional in 619 of 2,400 responses, 25.79% (95% CI 24.08 to 27.58).
Table 2 gives the rate by market and category, and Figure 1 plots the same cells with prompt-level
cluster-bootstrap intervals.
Category.Real estate (35.4%) and car dealerships (32.9%) are indistinguishable from each other
(p = 0.62) and both far exceed insurance (9.1%). Real estate against insurance givesχ2 = 159.3and
p = 5.8 × 10−8 at a within-arm design effect of 5.41; car dealers against insurance givesp = 4.9 × 10−7
at 5.37. Before the geographic stage the same two contrasts giveχ2 = 178.8, p = 4.2 × 10−9 and
9

0 10 20 30 40 50 60 70
Responses naming an individual (%),
roster-free detector, EU-only
Real estate
Car dealers
Insurance
All three
Real estate
Car dealers
Insurance
All three
Real estate
Car dealers
Insurance
All three
Real estate
Car dealers
Insurance
All three
55.8
39.6
1.5
32.3
43.5
26.0
24.5
31.3
16.4
40.7
11.4
22.9
14.0
25.5
2.0
13.8
Baltics (LT+EE)
Poland
Ireland
Netherlands
(a)
0 10 20 30
Responses naming a roster member (%),
roster overlap only
25.4
16.2
0.4
14.0
0
0
0
0
1.4
0
0
0.5
1.5
0
0
0.5
(b)
Real estate
Car dealers
Insurance
All three
Figure 1: Naming rate by market and category. Panel (a) plots the primary outcome, the geo-
corrected roster-free detector, and matches Table 2. Panel (b) plots the roster-matched diagnostic
on its own scale. Intervals are prompt-level cluster bootstrap, 10,000 draws.
10

Table 2: Naming rate by market and category, primary outcome (geo-corrected, roster-free detector).
Cells hold 200 responses in Poland and the Netherlands, 140 in Ireland, 260 in the Baltics. Paren-
thesised values give the rate before the geographic stage, where it differs.
Market Real estate Car dealers Insurance All
Poland 43.5% (44.0) 26.0% (28.0) 24.5% (25.5) 31.3% (32.5)
Ireland 16.4% (29.3) 40.7% (44.3) 11.4% 22.9% (28.3)
Netherlands 14.0% 25.5% (28.0) 2.0% 13.8% (14.7)
Baltics 55.8% 39.6% 1.5% 32.3%
All 35.4% (37.8) 32.9% (34.6) 9.1% (9.4) 25.8% (27.3)
p = 1.7 × 10−7. This is the largest and best identified effect in the study. It holds inside every
market, with one qualification: insurance sits near floor in the Baltics (1.5%) and the Netherlands
(2.0%) and stays meaningfully positive in Poland (24.5%) and Ireland (11.4%). The Irish insurance
figure rests on two recurring named experts, one appearing in 15 of 140 Irish insurance responses
and one in 5. Two people carry that figure, so it is a statement about them.
Market.Poland 31.3% (95% CI 27.8 to 35.2), Baltics 32.3% (29.1 to 35.7), Ireland 22.9% (19.1
to 27.1), Netherlands 13.8% (11.3 to 16.8). Pairwise at within-arm design effects with Holm over six
comparisons, two contrasts clear: Poland against the Netherlands (pHolm = 0.0003) and the Baltics
against the Netherlands (pHolm = 0.012). Ireland against the Netherlands does not (pHolm = 0.31),
and none of the Poland, Baltics and Ireland contrasts come close (allpHolm ≥ 0.31). The defensible
statement is that the Netherlands is last and the other three do not separate in this design. Design
effects differ sharply by market (Poland 2.31, Ireland 4.81, Netherlands 4.16, Baltics 8.86), which is
informative on its own: Baltic responses agree with each other inside a prompt far more than Polish
ones do.
4.2 RQ1b: models differ more than markets
Grok names an individual in 38.0% of its 600 responses, Perplexity 34.0%, GPT-5.6 Sol 21.8%
and Gemini 9.3% (Table 3, Figure 2). Because every one of the 120 prompts was answered by all
four models, model is a within-prompt factor, and the test is exact within-prompt randomisation:
χ2 = 157 .7, permutation p < 0.0001over 20,000 draws. Cochran-Mantel-Haenszel stratified on
prompt agrees on every pair except Grok against Perplexity: Grok against Geminiz = 13 .48,
Perplexity against Geminiz = 12.30, GPT against Geminiz = 6.85( p = 7.2 × 10−12), Grok against
GPTz= 7.49, Perplexity against GPTz= 5.79, and Grok against Perplexityz= 1.80,p= 0.071.
Table 3: Naming rate by model,n = 600per model, Wilson 95% intervals. The roster-matched
column is the diagnostic of Section 5.
Model Primary outcome 95% CI Roster-matched
Grok 4.5 38.0% 34.2 to 42.0 6.7%
Perplexity Sonar Pro 34.0% 30.3 to 37.9 5.8%
GPT-5.6 Sol 21.8% 18.7 to 25.3 3.3%
Gemini 3.6 Flash 9.3% 7.3 to 11.9 3.2%
The GPT-against-Gemini contrast deserves its own line, because it is the one model comparison
this design was already powered for: 21.83% against 9.33%, a gap of 12.5 points, OR 2.71, Fisher
11

0 10 20 30 40 50
Responses naming an individual (%),
roster-free detector, EU-only
Grok 4.5
Perplexity Sonar Pro
ChatGPT (GPT-5.6 Sol)
Gemini 3.6 Flash
38.00
34.00
21.83
9.33
χ2(3) = 157.7, Rao-Scott p = 6.7 × 10−6
(a)
0.0 2.5 5.0 7.5 10.0
Responses naming a roster member (%),
roster overlap only
6.67
5.83
3.33
3.17
χ2(3) = 12.4, Rao-Scott p = 0.562
(b)
Figure 2: Naming rate by model under both outcome definitions.
p= 2.6×10 −9, Cohen’sh= 0.351, needing 359 responses per arm at 80% power against 600 held.
The same comparison on the roster-matched outcome is 3.33% against 3.17%, a gap of 0.17 points,
Fisher p = 1, and the omnibus model effect there falls fromχ2 = 12.4to a Rao-Scott χ2 = 2.05,
p = 0.562. The roster-matched measure compresses all four models toward zero and cannot separate
them. Only the roster-free ordering is reported as a result.
4.3 RQ2: citation type predicts naming, citation volume does not
Responses that named an individual and responses that did not cite a similar number of sources.
Under the roster instrument the means are 8.55 and 8.58, with a cluster-bootstrap interval on the
difference of −1.34to+1 .17and d = −0.003; under the primary outcome they are 7.90 and 8.81.
Volume carries no signal.
Composition does. Table 4 gives the gap in each source type’s share of an arm’s citations, under
both outcome definitions, with prompt-level cluster-bootstrap intervals. Figure 3 plots the full
twenty-category breakdown.
Table 4: Citation composition: gap in percentage points between naming and firm-only responses
(named minus firm-only). Intervals are prompt-level cluster bootstrap, 10,000 draws, seed 20260726.
Bold marks the three contrasts this section reports as findings. Six rows exclude zero under both
definitions; the three in bold are the ones that also hold under the geographic correction and the
tail-rule sensitivity and carry a mechanism the text can name.
Source type Roster instrument Primary outcome
individual-site+5.05[+1.08,+8.90]+2.58[+1.41,+3.91]
vertical-portal+6.17[+2.49,+10.08]+4.27[+1.73,+6.91]
social-network−3.21[−4.28,−2.01]−2.19[−3.50,−0.85]
review-platform−5.53[−7.23,−3.98]−1.70[−3.96,+0.61]
public-register−1.80[−2.77,−0.86]−1.56[−2.63,−0.52]
news-media−1.97[−2.73,−1.08]−1.04[−1.73,−0.35]
firm-site+1.08[−5.01,+7.34]−1.41[−5.45,+2.62]
general-directory+0.20[−1.71,+2.51]+1.36[−0.15,+2.93]
unclassified−2.03[−3.14,−0.59]−1.50[−2.32,−0.65]
12

0.1 0.3 1 3 10 30
Share of the arm's citations (%), log scale
vertical-portal
individual-site
content-site
professional-network
general-directory
job-board
data-aggregator
network-site
industry-association
reference-work
video-platform
search-surface
community-forum
review-platform
matching-service
news-media
unclassified
public-register
firm-site
social-network
0
(a)
Naming responses
Firm-only responses
−10 −5 0 5 10
Named arm minus firm-only arm
(percentage points of citations)
(b)
Roster-free outcome
Roster-matched outcome
Figure 3: Citation composition by source type, naming against firm-only responses, all twenty
categories. The roster-free series here is the detector before its geographic stage, where the individual-
site gap is+2.36and the vertical-portal gap+4 .42; Table 4 gives the geo-corrected values,+2.58
and+4.27, which is the difference between the two.
13

Firm-owned pages carry no signal.Naming responses take 44.05% of their citations from
firm sites and firm-only responses 45.46%, and the gap interval spans zero; under the classification
used before the individual-site re-adjudication the same two shares are 44.3% and 44.1%. The
original analysis of this corpus reported 95.5% against 86.8% and read the difference as the paper’s
mechanism. That split was an artifact of the else-default described in Section 3.5, which swept
87.2% of citations into a bucket labelledemployer-owned page . On the 26 individuals ever named,
citations landing on that person’s own employer domain number 34 of 975, 3.49%.
What does distinguish themis the individual’s own site and the category portal, together
with the absence of social platforms. Under the primary outcome, naming responses take 3.52% of
their citations from a site one person delivers, against 0.94% for firm-only responses, and 11.02%
from vertical portals against 6.75%. Both survive the change of outcome definition, the geographic
correction and the tail-rule sensitivity. Without the geographic stage the same two gaps are+2.36
(+1.26to+3 .64) and+4 .42(+1 .93to+6 .98). The individual-site contrast survived a harder test as
well: withdrawing the inference that a person-named domain implies a solo operator removed 41 of
70 domains from the class and cost the contrast about one point, and it still excludes zero in all
three treatments of the unresolved rows.
Two caveats belong in the same breath. First, 108 of the 114 naming responses under the roster
instrument sit in two cells, Baltics real estate and Baltics car dealers, so every pooled contrast
on that outcome is partly a market and category comparison. Stratified inside that stratum the
individual-site gap falls to+3.91( −1.51to+9 .40) and vertical-portal to+1.86( −1.59to+5 .64),
whose intervals at n = 108are too wide to establish an absence. Second, the roster-matched
individual-site contrast rests on 62 named-arm citations across nine domains and eight prompt
clusters, every one of them Baltics real estate, and one domain carries 27 of the 62. The primary
outcome does not have that problem to the same degree, with 619 naming responses spread across
all four markets, and it is where the finding should be argued.
Review platforms do not survive.The pooled roster-matched gap of−5.53looks like the
strongest row in the table, and it collapses under both stress tests:−0.82( −1.67to −0.03) inside
the Baltic stratum, and−1.70( −3.96to+0 .61) under the primary outcome. It is close to pure
market and category composition, and it is not reported as a finding. Social platforms are the one
contrast that strengthens under stratification (−5.83, −7.76to −3.39) and holds under the change
of outcome.
4.4 Query language: a within-city effect and an informative null
Nine English prompt slots have an exact local-language translation in the same city and category.
Those nine pairs are the inferential test, because they hold market, category, city, model, iteration
count and question wording fixed by construction, and vary only the language of the query.
On the matched pairs, and on the primary outcome, English named an individual
in 66 of 180 responses (36.67%) against 28 of 180 (15.56%) for the translation.Fisher
p = 7.3 × 10−6, OR 3.14. The direction is the same in all three pair groups: 40.0% against 13.3% in
Vilnius, and 35.0% against 16.7% in each of the two Tallinn groups.
That Fisher test treats 360 responses as independent, and they are not. Under the design-effect
correction inside the contrast’s own subset (6.49) the same comparison givesp = 0.074, and a sign-flip
permutation over the nine pairs givesp = 0.095on a mean paired difference of+21.1points. The
direction is unambiguous and nine clustered pairs cannot close it, which is what the design supports.
The roster instrument sees the same contrast on the same 360 responses at a smaller absolute scale:
33 of 180 (18.33%) against 9 of 180 (5.00%), OR 4.27, Fisherp = 1.1 × 10−4, Rao-Scott p = 0.031.
Both instruments agree on sign and on rank; they disagree on level, because a roster-derived rate
14

measures overlap with a list (Section 5) and the primary outcome measures naming.
Weaker grounding would predict fewer citations in the local language. The opposite holds: Baltic
responses average 7.55 citations in English and 12.26 in the local language.
Table 5 gives the full within-city picture under both outcome definitions.
Table 5: Naming rate by query language within city.p-values are Rao-Scott at the within-arm design
effect.
City Local language English Localp
Primary outcome
Vilnius Lithuanian 47.1% (113/240) 19.4% (35/180)0.046
Tallinn Estonian 38.3% (69/180) 19.4% (35/180) 0.162
Amsterdam Dutch 19.0% (80/420) 1.7% (3/180)0.0007
Warsaw Polish 29.0% (122/420) 36.7% (66/180) 0.224
Pooled 30.5% (384/1260) 19.3% (139/720)0.027
Roster instrument
Vilnius Lithuanian 20.8% (50/240) 3.3% (6/180)0.0076
Tallinn Estonian 22.8% (41/180) 6.7% (12/180)0.021
Amsterdam Dutch 0.2% (1/420) 1.1% (2/180) 0.22
Warsaw Polish 0.0% (0/420) 0.0% (0/180) undefined
Pooled 7.3% (92/1260) 2.8% (20/720) 0.067
The pooled direction holds under both definitions and clears 0.05 under the primary one. Which
city carries it does not agree between the two. The roster instrument puts the effect in Vilnius
and Tallinn and cannot see Amsterdam at all, because Amsterdam has three roster matches in 600
responses. The primary outcome puts the largest effect in Amsterdam and loses Tallinn to the Baltic
design effect near eight.
Warsaw is the informative cell. Under the roster instrument it is 0 against 0, formally undefined
at any sample size. Under the primary outcome it is a well-powered null inside a high-rate market:
29.0% English against 36.7% Polish,p = 0.22, with the point estimate pointing the other way. A
language effect that is real in Amsterdam and Vilnius and absent in Warsaw is heterogeneous across
cities, and no general property of non-English querying will explain it. That settles the question the
original analysis left open, which was whether the language contrast could be separated from roster
coverage at all.
4.5 Naming concentration
Of the 939 roster members, 26 (2.8%) were named at least once, across 128 mentions in 114 responses.
The distribution among those 26 is steep: the most-named individual takes 21.9% of mentions, the
top three 45.3%, the top five 57.8% and the top ten 79.7%, with a Gini coefficient of 0.545 across
the named and 0.987 across the full roster (Figure 5). Fourteen of the 26 are named once or twice.
Prior work at brand level reports a mean Gini of 0.28 for recommendation share across fifty
brands [Żatuchin, 2026b]. Individual naming in this corpus is far more concentrated than that.
Whatever produces it does not spread across a market.
15

English Local
language
0
10
20
30
40
50Responses naming a roster member (%)
18.3
5.0
6 of 9 pairs fall, 1 rises, 2 tie
OR 4.27, Fisher p = 1.1 × 10−4
paired permutation p = 0.062
(a)
0 10 20 30 40
Responses naming a roster member (%)
Vilnius
Tallinn
Amsterdam
Warsaw
Pooled
p = 0.024
p = 0.044
p = 0.276
n.d.
p = 0.088
(b) English query Local-language query
Figure 4: Naming rate by query language, roster-matched outcome in both panels. Panel (a) gives
the nine matched translation pairs, 18.33% against 5.00%; panel (b) holds city fixed and pools all
prompts. Table 5 carries the same comparisons under the primary outcome, where the matched
pairs run 36.67% against 15.56%. The two instruments agree on sign and rank and differ on level,
for the reason Section 5 gives.
1 5 10 15 20 25
Roster individuals, ranked by number of times named (de-identified)
0
5
10
15
20
25
30
Times named across
2,400 responses
26 of 939 roster individuals (2.8%) were named at least once.
The top 3 take 45.3% of all 128 mentions. Gini = 0.545.
0
20
40
60
80
100
Cumulative share of
all name mentions (%)
Figure 5: Concentration of naming across the 26 individuals ever named.
16

4.6 Retrieval geography and eponymous firms
Wrong-city retrieval.Ask a grounded model for the best car dealer in Warsaw and some of what
comes back is in Indiana. This is a retrieval failure with a measurable size, and this section measures
it.
Every generic-TLD domain carrying three or more citations was adjudicated against its live site,
its stated address, the register record where the site was unclear, and the path of the page the model
actually cited: 296 domains and 6,671 citations, each decided from the cited page itself. Seventy-five
domains resolve to the United States. Forty-four of them are local businesses inside the prompted
city’s American homonym, and they carry 355 citations: dealerships in Warsaw, Indiana; insurance
agencies in Amsterdam, New York; car franchises in Dublin, Ohio. A further 37 citations sit on
European or global domains whose cited page is American, so the unit that has to be adjudicated is
the page (Section 4.6). Together that gives 367 citations to an American local business, 1.78% of the
corpus, and 780 citations to an American page of any kind, 3.79%. One hundred and eighty-two
of the 2,400 responses (7.6%) cite at least one American local business, and 294 (12.2%) cite an
American page of some kind.
The concentration is where the mechanism shows. Table 6 gives the American local share by city.
Warsaw runs at 4.7%, Dublin 1.9% and Amsterdam 1.4%, against Vilnius 0.2% and Tallinn 0.1%.
Vilnius and Tallinn have no American twin, and their leakage is a twentieth of Warsaw’s. Polish
car dealers are the worst cell in the study at 10.3% American local and 15.1% American in total,
because Warsaw, Indiana holds a Toyota store, a GMC store, a Nissan store, a Chrysler store, a
Chevrolet store and several used lots, and every one of them turns up in answers about Poland. A
second mechanism operates without a namesake town: Tallinn’s dealer Ideal Auto collides in name
with Ideal Auto Sales of Waukesha, Wisconsin, and an Ideal Auto in Minot, North Dakota, and
both American pages enter the Baltic cell.
Table 6: Wrong-city retrieval by prompted city. “American local” counts citations whose cited page
is that of a business in the city’s American homonym; “any American page” adds national directories,
brand locators, American job searches and other United States pages. The unit is the cited page, so
a page on a European or global host counts where the page itself is American. Denominator is every
citation issued for that city.
City American local Share Any American page Share Citations
Warsaw 231 4.68% 416 8.43% 4,932
Dublin 55 1.91% 182 6.32% 2,882
Amsterdam 70 1.35% 129 2.49% 5,183
Vilnius 6 0.18% 33 1.02% 3,244
Tallinn 5 0.12% 20 0.46% 4,339
Corpus 367 1.78% 780 3.79% 20,580
An automated first pass flagged 27 domains on a name-plus-generic-TLD heuristic. It was right
on 23 of them and wrong on four, and the four wrong ones carry 153 citations, more than a third
of the flagged volume: a London insurance broker whose cited pages are all European locale paths
served by its Estonian and Polish subsidiaries, a Kraków agency on a.com domain, and two Dutch
brokers registered with the KvK. Running the same adjudication over the 266 domains the heuristic
never flagged found 55 more American ones worth 495 citations, more than the entire flagged set.
The heuristic was both wrong on its heaviest calls and blind to the larger problem, which is why the
adjudication is evidence-based throughout. Two domains sit outside the European and American
17

categories, a Vancouver broker and an American rating agency’s global ranking, and they are counted
in neither. Seven domains carrying 52 citations returned low confidence, and every one was counted
as European, which is the conservative direction for a contamination estimate.
The host is the wrong unit.Adjudicating hosts misses a second route. Indeed, Yelp, Facebook,
LinkedIn, TikTok, Reddit, Tripadvisor and the App Store all serve the European market and all of
them served American pages into these answers: Indeed job searches in Warsaw, Indiana and Dublin,
California (12 citations); the Yelp category page for real-estate agents in Dublin, Ohio (5); the Yelp
listing for Toyota of Warsaw, Indiana (5); the Facebook page of Nissan of Warsaw (2); a LinkedIn
mechanic-jobs page for Warsaw, Indiana; a TikTok tag; a Reddit thread from Indianapolis; Kia’s
American dealer locator; and the App Store page for an American app called Ideal Auto, which
shares its name with a Tallinn dealer. Thirty-seven citations across ten domains, 12 of them naming
one American firm. A host-level rule scores every one of them as European, and a reader following
the link lands in the United States.
At the level of the naming outcome, dropping detections that resolve to American individuals or
businesses removes 23 of Ireland’s 119 naming responses, 7 of Poland’s 195, 5 of the Netherlands’
88 and 0 of the Baltics’ 252. Ireland falls from 28.3% to 22.9%, Poland from 32.5% to 31.3%, the
Netherlands from 14.7% to 13.8%, and the market ordering changes from Poland≈ Baltics > Ireland
> Netherlands to Baltics ≈ Poland > Ireland > Netherlands. A second count works from the
response text. The share of responses naming any American state, spelled-out country or American
twin city, counting responses that name nobody, is 42.4% in Ireland, 25.8% in Poland, 9.2% in the
Netherlands and 1.2% in the Baltics.
The contamination does not explain the result. Responses citing an American local business
name an individual at 31.9% against 25.3% for the rest, and deleting every one of those 182 responses
moves the corpus naming rate from 25.79% to 25.29%.
One model handles the ambiguity differently. GPT-5.6 Sol declines to answer pending disam-
biguation in 66 of its 105 Irish calls, 43 of 150 Polish, 31 of 150 Dutch and 0 of 195 Baltic. The
other three answer, and some of them answer about Ohio.
Eponymous firms.Two hundred and forty-nine of 1,876 detections (13.3%) are firm names
shaped like personal names. This is overwhelmingly Irish: 212 of 444 Irish detections (47.8%), against
6.6% in the Netherlands, 2.2% in Poland and 1.7% in the Baltics. In 68 of the 197 Irish responses
carrying any detection (34.5%), every detection is an eponymous firm. Without the eponym rule
Ireland has the highest naming rate of any market (46.9%); with it, the third. The same structure
appears in the roster-matched data: of the five naming events outside the Baltics, four are agency
brands whose roster rows are agency owners.
Where a firm is named after its principal, “the model named a person” and “the model named
a company” are not separable propositions from the output string alone. Any individual-level
AI-visibility metric has to say which of the two it counts. This one counts the person, at a measured
cost in recall.
4.7 RQ3: cross-model agreement, by three definitions
Thirty-one (prompt, iteration) tuples have two or more of the four models naming at least one
roster-matched individual. Among those 31, all naming models produced an identical name set in
9 cases (29.0%, 95% CI 16.1 to 46.6); every naming model’s set shared at least one person in 14
(45.2%); and at least one pair of naming models overlapped in 16 (51.6%).
The word “identical” belongs only to the first of the three. Prior work at company level reports
41.6% cross-model agreement on the top-recommended brand under the same replication design
[Żatuchin, 2026b]. That figure is an identity comparison on a single top-ranked entity, so the
18

comparable quantity here is 29.0%.
The comparison does not survive its own denominator. The 31 tuples come from 11 prompts and
19 individuals, and a prompt-cluster bootstrap on the 45.2% figure returns an interval of 17.4 to 71.4,
which contains the 41.6% brand-level comparator and most other values a reader might propose.
Roughly 1,500 tuples would be needed to separate the two. RQ3 is reported here as a descriptive note
with its interval, and it carries no conclusion. Constantin [2026] measured cross-engine consensus
on 278 production responses to 56 buyer-intent prompts across seven cities and five systems, and
reports convergence conditional on category with no single pooled rate, which bounds the question
without settling it.
5 What a roster-based instrument measures
Individual-level AI visibility is naturally measured against a roster: assemble a list of real professionals,
ask the model, count matches. This study ran that design alongside the roster-free one on the
identical 2,400 responses. The comparison is worth reporting because the roster design produces a
clean, plausible and misleading result.
Across the corpus the models emitted 27,293 name-shaped mentions. The 939-person roster
matched 128 of them, 0.469%, spread across 114 responses. Against the individuals the roster-free
detector resolves, roster capture is 128 of 1,876, 6.8%. Twenty-six of the 939 people were ever named.
The resulting rates are 0.0% in Poland (0 of 600, Clopper-Pearson upper bound 0.61%), 0.48%
in Ireland, 0.50% in the Netherlands and 13.97% in the Baltics, with one cell, Baltics real estate,
carrying the result at 25.38% (66/260, cluster-adjusted interval 17.7 to 33.9). Only that cell and
Baltics car dealers survive Holm correction across the twelve cells. The 0.0% to 25.4% range is a
roster-overlap statistic.
Read as model behaviour, the table says grounded models never name a real individual in Poland.
Read as an instrument property, it says a 255-person LinkedIn-derived sample of the Polish market
intersected the models’ actual naming behaviour zero times, while the models named individuals in
31.3% of Polish responses. The second reading is the correct one, and the diagnostic that separates
the two is not available inside the roster design: 27,165 unmatched name-shaped mentions were
discarded as extraction noise, and the observation that they do not affect the roster-matched result
is exactly why that result cannot answer RQ1.
Restricting the roster to the prompted city sharpens the point. Every prompt names a city; the
roster does not, so a response can match a member who works 300 km away. Against city-filtered
rosters the Baltic rate falls from 13.97% to 8.46% and the Dutch rate from 0.50% to 0.33%. Ireland
is not testable, because its one named row carries the market-name fallback in its location field.
Within the Baltics the two cities behave differently: 78.6% of Vilnius’s named responses attach to
a roster row that mentions Vilnius, against 26.4% for Tallinn, so Tallinn’s rate is substantially a
country-level rate reported under a city label.
This caution applies to any roster built this way. A roster instrument reports the intersection
of two populations, and its measured rate falls with the size of the market being sampled, which
manufactures a market effect ordered by market size. Here the roster design orders markets Baltics≫
Netherlands ≈ Ireland > Poland, and the roster-free design orders them Baltics≈ Poland > Ireland
> Netherlands. A roster-based product metric for individual AI visibility, sold on the promise that it
tells a professional whether models name them, would have reported zero to every Polish subscriber
in this sample while the models were naming Polish individuals in nearly a third of answers.
19

6 Discussion
6.1 What predicts naming
Table 7 gives the multivariable model. Every fixed effect in it survives the random intercept on
prompt, and the ordering matches the marginal tables.
Table 7: Logistic mixed model, random intercept on prompt, outcome = named an individual
(primary). Odds ratios with 95% intervals. Reference levels: Baltics, real estate, Gemini, English.
Random-effect standard deviation on prompt 1.30. A GEE with an exchangeable working correlation
clustered on prompt returns the same signs and the same significant terms, withα= 0.243.
Term OR 95% CI
Market: Poland 1.29 1.06 to 1.57
Market: Ireland 0.39 0.30 to 0.51
Market: Netherlands 0.20 0.16 to 0.27
Category: car dealers 0.91 0.76 to 1.08
Category: insurance 0.08 0.06 to 0.11
Model: GPT-5.6 Sol 3.51 2.80 to 4.41
Model: Perplexity 8.61 7.00 to 10.61
Model: Grok 11.29 9.19 to 13.87
Query language: local 0.30 0.24 to 0.38
Category and model dominate. Insurance cuts the odds of naming by a factor of twelve against
real estate, and the model answering the question moves them by a factor of eleven from bottom to
top. Market sits below both, and query language cuts the odds by a factor of three.
The citation result changes shape once source domains are classified on what they are. Naming
responses and firm-only responses cite the same number of sources, and they cite firm-owned pages
at the same rate. The mechanism proposed in the original analysis of this corpus, that a person
becomes visible because their name is legible on the employer’s domain, is not supported. What
separates the two is a surface the individual controls, plus a category portal, plus the absence of
social platforms.
The honest reading is narrower than the original and points the other way. A named individual’s
visibility tracks a first-party surface the individual owns. The employer’s own website predicts
nothing. The effect is small, 2.6 points of citation share on 619 naming responses, and it is stable
across four stress tests, so a stratified replication with more naming events in more than one market
is the necessary next step.
6.2 What this says about measuring individual AI visibility
Three properties of this corpus complicate any individual-level metric, and none of them is specific
to this study.
The first is the roster problem of Section 5. Any instrument defined by membership of a list
reports the intersection of that list with model behaviour, and reports it as if it were model behaviour.
The second is the eponym problem of Section 4.6. In categories where firms are named after
their principals, and Irish estate agency is one, the output string does not decide whether a person
or a company was named. Forty-eight per cent of Irish person-shaped detections are firm brands,
and the rule that removes them changes which market ranks first.
20

The third is retrieval geography. A grounded model asked for the best car dealer in Warsaw
returns dealerships in Warsaw, Indiana, and a metric that counts names without checking where
they are will count them. Correcting for it moves Ireland by 5.5 points.
A measurement that ignores all three will still produce a number, and the number will be wrong
in a direction that varies by market.
7 Ethics, data protection and competing interests
Human-subjects status.No person took part in this study. Nobody was recruited, enrolled,
interviewed or surveyed, and no intervention ran on anyone. The experiment issued 2,400 calls to
four commercial APIs and compared the returned text against a list of publicly listed professionals.
Nobody was contacted, and nobody was harmed.
No institutional ethics committee reviewed this study. The work was designed and run by
Rankfor.AI OÜ, which is the controller, and it follows the Estonian Code of Conduct for Research
Integrity. Estonian law makes prior committee review compulsory for research that processes special
categories of personal data without consent (Personal Data Protection Act, §6(4)). This study has
no participants and no special-category data, so that requirement does not apply.
Personal-data status.“No human participants” and “no personal data” are separate claims.
The first holds here. The second does not. Public availability settles nothing on its own, and
Zimmer’s account of the Tastes, Ties and Time release is the standing demonstration [Zimmer, 2010].
The roster is personal data. It holds 939 living, identifiable people in Poland, Ireland, the
Netherlands, Lithuania and Estonia, each with a name, a public professional headline, a city or
region, and a resolvinglinkedin.com/in/ URL (Section 3.3). It came from public LinkedIn search
results on 24 July 2026. It carries no email address, no telephone number, no purchased record and
no special-category data. Those 939 people are data subjects, and building and querying that file is
processing, whatever its source. The stored model output is a second surface, since it names people
outside the roster. The lawful basis is Art. 6(1)(f) GDPR, legitimate interest.
Legitimate interest assessment.A written three-part assessment was completed before
publication. Purpose: whether grounded models name individual professionals is unmeasured, and
it bears on how a class of workers becomes visible to buyers (Section 2.3). Necessity: the study
asks whether a model namesrealpeople, so synthetic or pseudonymised names cannot answer it.
Balance: subjects and their employers published this data so that prospective clients would find it,
the processing yields no decision about any individual, nobody was contacted, and 26 of the 939 were
ever named by any model. Against that, the subjects do not know, could not object beforehand,
and the aggregate result speaks to their professional visibility. The assessment concludes that the
interest carries, conditional on the safeguards below, and marks Art. 14 transparency as its weakest
limb. Rankfor.AI’s data protection officer reviewed and signed off the assessment, including the
Art. 14(5)(b) reliance and the retention period, before submission.
Article 14 transparency.The data was obtained indirectly, so Art. 14 applies and its clock
runs one month from collection. The study relies on the research exemption in Art. 14(5)(b), and
the reliance is contestable: 939 is a small cohort and the data was days old, both of which weigh
against a disproportionate-effort claim (Recital 62). No contact details are held, and acquiring 939
of them would mean collecting more data than the study needs. Art. 14(5)(b) requires appropriate
measures from any controller relying on it, and names publication as one. A standing notice at
https://open.rankfor.ai/resources/research-data-protection-notice gives the controller,
source, purpose, lawful basis, retention and objection route, published whether or not a supervisory
authority accepts the exemption.
21

Safeguards, retention and objection.Art. 89(1) safeguards apply [EDPB, 2026]. Four fields
per person were collected and no more. The design is pseudonymised throughout: individuals appear
in the analysis and in the deposit as opaque identifiers, and no personal data enters the public
deposit. The identifying roster sits in a private, access-controlled file under one named custodian,
apart from the analysis outputs, and it is deleted by 31 July 2028 unless a fresh assessment justifies
keeping it. Objection and erasure requests go todpo@rankfor.ai and are honoured on receipt; a
request removes the individual from the roster and from any retained response text, and the affected
aggregate figures are recomputed and corrected on the record. No individual is named in this paper,
its figures or its supplementary materials.
Competing interests.The author holds a commercial interest in Rankfor.AI, a vendor selling
AI-visibility measurement and services, and the dual affiliation appears on the title page. The interest
is specific and points in a particular direction: an individual-visibility gap is what such a product
exists to close. Three design features bound what that interest could do to the numbers, and they
are named here so a reader can check each one. The inclusion rule was fixed before collection. The
primary outcome was moved off the roster-derived measure whose headline supported the commercial
framing most strongly, and Section 5 sets out why. The citation claim that made the cleanest sales
argument, that a person becomes visible through the employer’s own website, is reported here as not
supported. The aggregate dataset, the domain coding, the coding manual and the detector source
are published, so every figure can be recomputed. No client of Rankfor.AI appears in the roster or
the analysis.
Funding.Rankfor.AI paid the API and tooling costs. No external, public or client funding
supported this work, and nobody outside the author approved the manuscript before submission.
Author contributions (CRediT).Dmitrij Żatuchin: conceptualization, methodology, software,
validation, formal analysis, investigation, data curation, writing (original draft), writing (review and
editing), visualization, project administration, funding acquisition.
8 Limitations
1. Detector recall bounds every rate from below.The detector demands positive evidence
before accepting a candidate, which buys precision (96.9%) at the cost of recall (61.7% against
the 128 roster mentions, 62.6% in the Baltics). Every naming rate here is a lower bound, and
the shortfall is uneven across markets: a hand audit of the dropped pool puts the genuine-
individual share at 36.4% in the Baltics against 4.5% in the Netherlands, which compresses
the market ordering reported above and does not create it.
2. Eponymous firms and retrieval geography are handled by rule.13.3% of detections
are firm names shaped like personal names, concentrated in Ireland (47.8%), and the rule that
removes them changes which market ranks first. Residual unresolvable ambiguity is roughly
10% of detections, 7.2% flagged and about 3.1% silent, concentrated in the Netherlands. The
geographic stage rests on adjudication of 296 domains, and a false negative there inflates the
market it sits in. The adjudication covers generic-TLD domains with three or more citations;
below that line sit 346 hosts carrying 933 citations, 265 of them cited once, and European
country-code domains were not adjudicated because a.pl, .ie, .nl, .lt or .ee address cannot
be an American homonym.
3.Differential grounding.177 responses (7.38%) returned no citation, 137 of them from one
model and 78 of them in one market. The grounded-only sensitivity run reverses nothing, and
the confound is real.
22

4. Single time point and exploratory replication depth.All 2,400 calls were issued inside
a two-hour window on one day, at the exploratory tier of five iterations [Żatuchin, 2026d].
Grounded model behaviour varies with the web corpus a search tool indexes at query time,
and this study makes no claim about temporal stability. The clustering correction, not the
nominal n, is what bounds precision: effectiven is 407 on the primary outcome and 396 on
the roster-matched one.
5. The prompt sets are not translation-matched throughout.Of seven prompt slots per
Baltic category, three are true English/local translation pairs. The pooled English-against-local
comparison therefore mixes a language contrast with a prompt-wording contrast, which is why
Section 4.4 leads on the nine matched pairs and reports the pooled figures as descriptive.
6. Convenience roster.The roster reflects what LinkedIn’s Classic-mode search surfaced.
Section 5 treats that as the object of study, and it means no roster-derived rate here is a
population estimate.
7. Cross-model agreement is indeterminate.The 31 tuples behind the 45.2% overlap figure
come from 11 prompts and 19 individuals; the prompt-cluster interval runs 17.4 to 71.4, and
two alternative identity rules on the same tuples give 29.0% and 51.6%.
8. The design cannot resolve a demographic dimension.Work on platform-mediated
visibility reports gender disparities near an incidence rate ratio of 0.90 [Hannák et al., 2017].
With 26 individuals ever named, the smallest gap this design could detect at 80% power is
roughly 25 percentage points, and an effect of the size that literature reports would be detected
here with probability 0.06. No demographic result is reported, and none should be read into
the silence.
9. Several contrasts are out of reach, and are named as such.Table 8 lists the comparisons
this design cannot support at 80% power. Real estate against car dealers, Poland against the
Baltics, and Grok against Perplexity are nulls the design could not have resolved.
9 Conclusion
Grounded language models name an individual professional in about a quarter of answers to buyer-
intent questions, and what moves that share is not what a marketing account of it would predict.
Category moves it most: insurance cuts the odds of naming by a factor of twelve against real estate,
in every market tested. The model answering moves it almost as much, from 9.3% for Gemini to
38.0% for Grok on identical prompts. Query language moves it by a factor of three, and on nine
exact translation pairs English named an individual 36.7% of the time against 15.6% for the same
question asked in Lithuanian or Estonian. National market, the variable a commercial reader reaches
for first, comes last and separates only the Netherlands from the rest.
When a model does name a person, the citation trail that leads there runs through a surface the
individual controls and through category portals. The employer’s own website carries no signal at all.
That reverses the mechanism the first analysis of this corpus proposed, and it holds under four stress
tests: a change of outcome definition, stratification, a geographic correction, and the withdrawal of
every domain whose only claim to being one person’s site was that a person’s name appeared in it.
The measurement lesson has the widest reach. A roster is the obvious instrument for this question,
and it fails at it. A 939-person roster built under a defensible public-data rule matched 0.47% of
23

Table 8: Power at the primary outcome. Responses per arm needed at 80% power andα = 0.05,
after inflation by the within-arm design effect, against what the design supplies.
Contrast Needed per arm Have Verdict
Grok vs Gemini 87 600 powered
Amsterdam: English vs Dutch 106 252 powered
Perplexity vs Gemini 128 600 powered
Real estate vs insurance 195 800 powered
Car dealers vs insurance 229 800 powered
Poland vs Netherlands 280 600 powered
GPT-5.6 Sol vs Gemini 359 600 powered
Grok vs GPT-5.6 Sol 362 600 powered
Baltics vs Netherlands 536 678 powered
Perplexity vs GPT-5.6 Sol 697 600 under
Vilnius: English vs Lithuanian 378 206 under
Tallinn: English vs Estonian 704 180 under
Ireland vs Netherlands 1,260 494 under
Warsaw: English vs Polish 1,369 252 under
Poland vs Ireland 1,434 494 under
Baltics vs Ireland 2,596 546 under
Grok vs Perplexity 7,375 600 under
Real estate vs car dealers 25,915 800 under
Poland vs Baltics 215,737 678 under
the name-shaped text the models produced and 6.8% of the individuals they named, surfaced 26
people, and reported zero for an entire national market in which the models were naming individuals
in nearly a third of answers. Two further properties would distort any naive count: half of Irish
person-shaped output is agency brands named after their founders, and a measurable share of answers
about European cities describe their American homonyms. Anyone building an individual-level
AI-visibility metric has to solve all three before the number means anything, and the shortest route
to a defensible one runs through detection from the text. A list can only find the people already on
it.
10 Data and code availability
Aggregated, feature-coded response-level data is published on Zenodo under CC BY 4.0 athttps:
//doi.org/10.5281/zenodo.21612690: market, category, city, query language, model, iteration,
citation count, source-type counts and both naming indicators. The deposit also holds the domain
coding table, the coding manual, the detector source and the geographic adjudication record,
documented as a datasheet [Gebru et al., 2021]. The coding table carries 2,117 rows against the
2,182 domains analysed here: 66 person-named hosts are masked for the reason given below and
pooled under one label.
Every result in Sections 4 onward recomputes from those files, with two exceptions stated here:
the per-cell roster sizes in Table 1 and the filtered candidate pool behind the Polish stemmed re-check
derive from the withheld roster and the withheld response text, and appear in this paper only.
Response text is not published, because it contains third-party personal data the subjects did
24

not provide (Section 7). The identifying roster, names and LinkedIn profile URLs, is not published
and is held in an access-controlled research file. Individuals a model named appear as 26 opaque
pseudonyms. A re-identification audit tests the linkage route: no response flagged as naming an
individual cites a host built from that individual’s own name, which required masking 66 such hosts
(508 citations, 2.5% of the citation table) across naming and firm-only responses alike. Masking is
applied globally, so the flag is uninformative overall: 3.1% of citations on naming responses against
2.4% otherwise, Fisherp = 0.20. Within the Baltics, where naming concentrates, a response carrying
a masked host is 2.7 times more likely to be a naming response (p = 0.0004). That conditional
dependence is stated because every analysis here is stratified by market. Anyone who re-runs a
public prompt may recover some names from the model itself; median per-call reproduction across
the 57 (person, prompt) pairs where naming occurred is 5%. That residual is accepted because the
alternative is withholding the concentration and cross-model results entirely.
The README documents the environment (Node 22.19.0,openai 6.26.0, @google/genai 1.43.0),
the four API keys and the exact commands. Cost was about USD 24 at July 2026 list prices. The
pipeline records no token counts, so that figure is list-price arithmetic on measured call volumes and
no billed total is available.
A Prompt set
All 120 prompts appear verbatim in the deposit, grouped by market, category and language, with the
prompt identifier used in the response-level table. The nine matched translation pairs of Section 4.4
are flagged there.
B Detection cascade
The detection cascade of Section 3.4 is published as source and as pseudocode in the deposit,
including the blocklists, the gazetteer, the eponym test, the geographic stage and the fuzzy-match
thresholds used by the roster matcher.
References
Agliata, N., Hasso, T. (2026). Generative AI as an investment advisor: same client, different advice.
Preprints.org. https://doi.org/10.20944/preprints202605.0909.v1
Aral, S., Li, H., Zuo, R. (2026). The rise of AI search: implications for information markets and
human judgement at scale.arXiv:2602.13415.
Authority Specialist (2026).Professional Services AI Search Visibility Benchmark 2026, edition
2026-07. https://authorityspecialist.com/industry/professional (retrieved 26 July 2026).
Bareket, D., Tsarfaty, R. (2021). Neural modeling for named entities and morphology (NEMO2).
Transactions of the Association for Computational Linguistics, 9. arXiv:2007.15620.
Barolo, D., Valentin, C., Karimi, F., Galárraga, L., Méndez, G.G., Espín-Noboa, L. (2025). Whose
name comes up? Auditing LLM-based scholar recommendations.arXiv:2506.00074.
Baum, Z. (2026). Algorithmic electability: generative AI, gendered political bias, and LGBTQ
candidates. APSA Preprints. https://doi.org/10.33774/apsa-2026-p31md
25

Carr, T.R. (2026). What makes AI name you? Determinants of local business recom-
mendation across five generative models. OSF preregistration, registered 9 February 2026.
https://doi.org/10.17605/osf.io/eufw2
Chigbu, B.I. (2026). Algorithmic management in the global gig economy: an interdisciplinary
systematic literature review and critical discourse analysis.Frontiers in Sociology, 11:1743445.
https://doi.org/10.3389/fsoc.2026.1743445
Christen, P. (2006). A comparison of personal name matching: techniques and practical issues.
InSixth IEEE International Conference on Data Mining Workshops (ICDMW’06), 290–294.
https://doi.org/10.1109/ICDMW.2006.2
Chu, X., Hou, Y. (2026). Incumbent advantage: brand bias and cognitive manipulation dynamics in
LLM recommendation systems.arXiv:2606.17443.
Clarity Infra Research Group, Chen, F. (2025). Generative engine optimisation (GEO): an insti-
tutional framework and experimental evaluation for legal-service discoverability in AI search
ecosystems. Zenodo. https://doi.org/10.5281/zenodo.17294708
Constantin, D. (2026). Cross-engine consensus in AI-generated brand recommendations: an
empirical study across seven cities and five large language models. Zenodo preprint.
https://doi.org/10.5281/zenodo.21395597
Darani, R. (2026). Most agents are invisible in AI search, and the top 1% dominate.HousingWire, 5
May 2026. Opinion column by a FlyDragon co-founder.
de Rosen, T. (2026). The AIVO paradox: systematic divergence between AI visibility
and AI purchase recommendation outcomes across consumer brand categories. Zenodo.
https://doi.org/10.5281/zenodo.19568058
European Data Protection Board (2026).Guidelines 1/2026 on processing of personal data for
scientific research purposes, Version 1.0, public consultation 16 April to 25 June 2026.
Ehrlinspiel, J., Landwehr, M., Rudzki, T. (2026). Prompt tracking works, but not as a one-prompt
measurement system: prompt wording and brand visibility in AI answer engines. Working paper.
https://doi.org/10.2139/ssrn.6914539
Elbouanani, A., Tuo, A., Popescu, A. (2026). A scalable entity-based framework for auditing bias in
large language models. InFindings of the Association for Computational Linguistics: ACL 2026.
https://doi.org/10.18653/v1/2026.findings-acl.1689
Espín-Noboa, L., Méndez, G.G. (2026). Whose name comes up? II: Benchmarking and intervention-
based auditing of LLM-based scholar recommendation.arXiv:2602.08873.
FlyDragon (2026).The 2026 State of AI SEO in Real Estate.Industry benchmark report Vol. II,
Report No. FD-26-Q2-001, April 2026. Non-peer-reviewed vendor report; prompt set, agent roster,
matching rule and model versions not disclosed.
Gebru, T., Morgenstern, J., Vecchione, B., Wortman Vaughan, J., Wallach, H., Daumé III, H.,
Crawford, K. (2021). Datasheets for datasets.Communications of the ACM, 64(12), 86–92.
https://doi.org/10.1145/3458723
26

Goethals, S., Rhue, L., Sundararajan, A. (2025). Fairness principles across contexts: evaluating
gender disparities of facts and opinions in large language models.AI and Ethics, 6(1), print issue
February 2026, published online 5 December 2025. https://doi.org/10.1007/s43681-025-00876-5
Hannák, A., Wagner, C., Garcia, D., Mislove, A., Strohmaier, M., Wilson, C. (2017). Bias in
online freelance marketplaces: evidence from TaskRabbit and Fiverr. InProceedings of the 2017
ACM Conference on Computer Supported Cooperative Work and Social Computing (CSCW ’17),
1914–1933.
Hu, D., Baumann, J., Urman, A., Lichtenegger, E., Forsberg, R., Hannak, A., Wilson, C. (2025).
Auditing Google’s AI Overviews and featured snippets: a case study on baby care and pregnancy.
arXiv:2511.12920.
Kirichenko, S. (2026). How reproducible is AI search visibility? Prompt-paraphrase sensitivity and
a confidence-aware measurement protocol for generative engine optimization. Zenodo preprint.
https://doi.org/10.5281/zenodo.21498260
Kumar, P. (2026). Generative engine optimization at scale: measuring brand visibility across AI
search engines.arXiv:2606.20065.
Munoz, I., Kim, P., O’Neil, C., Dunn, M., Sawyer, S. (2023). Platformization of inequality: gender
and race in digital labor platforms.arXiv:2309.16887.
Sánchez-Guzmán, A., Eberhard, L., Helic, D., Espín-Noboa, L. (2026). Whose name comes up? III:
Persona prompting effects in LLM-based scholar recommendation.arXiv:2605.28187.
Sarkhedi, B. (2026). Auditing personal brand visibility in large language mod-
els: an open, reproducible protocol and scoring instrument. Zenodo preprint.
https://doi.org/10.5281/zenodo.20703583
Sarkhedi, B. (2026). How large language models surface personal brands: an entity-signal frame-
work and cross-system analysis of ChatGPT, Claude, and Perplexity. SSRN working paper.
https://doi.org/10.2139/ssrn.6942498
Sarkhedi, B. (2026). Personal brand equity in the age of algorithmic discovery: a practi-
tioner framework from 500+ brand engagements across 14 countries. SSRN working paper.
https://doi.org/10.2139/ssrn.6639718
Sheals, P., de Rosen, T. (2026). Beyond visibility: the linkage gap and the case for a third layer of
AI-native brand infrastructure. Zenodo. https://doi.org/10.5281/zenodo.20848721
Singh, A.K. (2026). From invisible to cited: a case study of generative engine op-
timisation for AI search recognition among Indian student founders. Zenodo preprint.
https://doi.org/10.5281/zenodo.19678290
Sumbilon, N. (2026). Cross-engine citation divergence: a cold-tested benchmark of entity recognition
across six AI answer engines. Zenodo. https://doi.org/10.5281/zenodo.21252896
van der Linden, I., Kumar, S., Dixit, A., Sudan, A., Danda, S., Anastasiu, D.C., Lukoff, K. (2025).
Generating the modal worker: a cross-model audit of race and gender in LLM-generated personas
across 41 occupations.arXiv:2510.21011.
27

Venkit, P.N., Laban, P., Zhou, Y., Mao, Y., Wu, C.-S. (2025). Search engines in the AI era: a
qualitative understanding to the false promise of factual and verifiable source-cited responses in
LLM-based search. InProceedings of the 2025 ACM Conference on Fairness, Accountability, and
Transparency (FAccT ’25), 1325–1340. https://doi.org/10.1145/3715275.3732089
Vishwakarma, R., Kumar, S., Jamidar, R. (2026). What gets cited: competitive GEO in AI answer
engines.arXiv:2605.25517.
Wang, W., Shi, T., Zhang, S., Xia, B., Xie, Z., Zeng, C., Zhang, Q., Ai, L., Yu, Y., Zhang, K., Tang,
F. (2026). PeopleSearchBench: a multi-dimensional benchmark for evaluating AI-powered people
search platforms.arXiv:2603.27476.
Wilde, K.H. (2026). AI search citation factors for local health practices. AEOGeoAI Research Team,
Zenodo, 27 June 2026. https://doi.org/10.5281/zenodo.20949938
Wilde, K.H. (2026). Pennsylvania AI search visibility study 2026. AEOGeoAI Research Team,
Zenodo. https://doi.org/10.5281/zenodo.21186327
Wilde, K.H. (2026). Miami AI search visibility study 2026: analysis of 515 Miami-Dade and
Broward businesses across ChatGPT, Claude and Gemini. AEOGeoAI Research Team, Zenodo.
https://doi.org/10.5281/zenodo.21271084
Żatuchin, D. (2026). Reputation vs. recommendation: a dual measurement of narrative quality and
AI recommendation frequency across brands. Manuscript under journal review. Replication data:
https://doi.org/10.5281/zenodo.19225834.
Żatuchin, D. (2026). Who owns the AI recommendation? A multi-industry empirical map of brand
category ownership across large language models.arXiv:2606.23057.
Żatuchin, D. (2026). How large language models source brand reputation across languages and
markets.arXiv:2606.25787; dataset on Zenodo, 10.5281/zenodo.20829524, CC BY 4.0.
Żatuchin, D. (2026). The Dice Roll Method: a standardized protocol for measuring stochastic bias
in large language model outputs.International Journal of Data Science and Analytics (Springer),
under review.
Żatuchin, D. et al. (2026). The language blind spot: how query language and brand recognition tier
shape AI-constructed brand reputation across twelve European languages.arXiv:2606.23165.
Żatuchin, D. (2026). Where does the noise come from? A variance-components decomposition of
non-determinism in LLM brand answers.arXiv:2607.13304.
Zhen, T., Liu, Y., Zhang, G., Niu, Y. (2026). What do Chinese-language generative search engines
cite and surface? A large-scale empirical study.arXiv:2607.15771.
Zimmer, M. (2010). “But the data is already public”: on the ethics of research in Facebook.Ethics
and Information Technology, 12(4), 313–325. https://doi.org/10.1007/s10676-010-9227-5
28
