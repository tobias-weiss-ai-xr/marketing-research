---
title: How Large Language Models Source Brand Reputation Across Languages and Markets
url: https://arxiv.org/abs/2606.25787
category: digital-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Dmitrij Zatuchin
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.25787
pages: 12
chars: 30005
fetched_at: '2026-11-08T13:03:38+00:00'
kb_version: 1
---

# How Large Language Models Source Brand Reputation Across Languages and Markets

How Large Language Models Source Brand
Reputation Across Languages and Markets
Dmitrij ˙Zatuchin1,2*
1*Department of Information Technologies, Estonian Entrepreneurship
University of Applied Sciences (EUAS), Tallinn, Estonia.
2Rankfor.AI, Tallinn, Estonia.
Corresponding author(s). E-mail(s): dmitrij.zatuchin@eek.ee;
Abstract
When a large language model (LLM) answers a question about a company, it
grounds the answer in retrieved web sources, and those sources decide what
the model says. Most analysis of AI brand visibility looks at the answer text.
This study looks one step earlier, at the citations. We merge three Rankfor.AI
datasets covering 128 brands across 12 home markets and 13 languages, and
analyse 167,551 URL-grounded citations (with 189,974 total attribution rows
including keyword and implicit sources). We classify each citation by domain
and source type and measure where AI gets its brand information, by language
and by market. Four patterns hold across the corpus. First, AI grounds brand
answers overwhelmingly in third-party sources: 85.7% of URL citations point to
sites the brand does not own, against 14.3% owned. Second, the source base is
concentrated and long-tailed: 80% of citations come from about 18% of domains,
and the domain-rank distribution fits a Zipf law (exponentα= 0.86,R 2 =
0.983). Third, one reference site dominates almost everywhere: Wikipedia is the
most-cited domain in 11 of 12 languages, the single exception being Lithuanian,
where the national business dailyvz.ltedges it (4.38% of Lithuanian citations).
Fourth, the source mix is market-specific at the margin: for 46 Polish national
brands the most-cited domain is YouTube, and four HR and careers portals
together supply 637 citations against 297 for Polish Wikipedia, about twice as
many. Models differ in citation behaviour, with Perplexity citing the most (90,276
of 131,514 backbone citations) and grounding in the widest domain set (15,995
domains). We measure what LLMs cite; we do not claim that the citation mix
equals real reputation or human perception. The findings point marketers toward
earned media and generative engine optimisation, since the third-party web, the
encyclopedia, and (per market) specific local outlets are where AI reads a brand.
1
arXiv:2606.25787v1  [cs.IR]  24 Jun 2026

Keywords:Large language models, AI search, Brand reputation, Citation analysis,
Source attribution, Generative engine optimisation, Earned media, Multilingual NLP
1 Introduction
When a buyer asks an AI assistant which logistics provider to trust or which payroll
tool to buy, the model does not invent the answer from memory alone. Grounded
models retrieve web pages first, then write an answer from what they retrieved [1]. The
retrieved pages, the citations, decide what the model can say about a brand. Whoever
the model reads becomes what the model knows.
Most monitoring of AI brand visibility studies the answer text: the sentiment,
the recommendation, the named competitor. This study looks one step earlier, at the
sources the model pulls before it writes. The question is practical for any marketing
team: where does AI get its information about your brand, and can you influence it.
If AI mostly reads a brand’s own website, the brand can write its way to a better
answer. If AI mostly reads third parties, the brand has to earn coverage on sites it
does not control.
The sourcing question matters because the citations are not a neutral mirror.
Generated answers cite imperfectly: in one audit of generative search, only 51.5% of
generated sentences were fully supported by their citations and only 74.5% of cita-
tions supported the sentence they were attached to [3], and attribution frameworks
exist precisely because grounding is hard to verify [2]. AI search systems also act
as gatekeepers: citations concentrate among a small set of outlets [7], AI search sur-
faces fewer long-tail and more low-credibility sources than traditional search [8], and
which sources get cited is engine-dependent and unstable [9, 10]. Source-side strategy
can move the result: optimising the cited sources raises a site’s visibility in genera-
tive answers by about 40% [4], and AI search shows a systematic bias toward earned
(third-party authoritative) media over brand-owned content [5].
Reputation has measurable economic stakes. It is a multi-stakeholder construct
built from observable signals [11], and firms with stronger reputations sustain better
financial performance [12]. As AI answers mediate more of how stakeholders form
those impressions, the sourcing layer becomes part of reputation management.
This is Rankfor.AI research. We merge three of our citation datasets, covering
Northern and Baltic Europe, Poland, and a Central and Eastern European cohort,
into one cross-market view of LLM sourcing. The Nordic-Baltic dataset is the source-
side companion to our analysis of how query language and brand-recognition tier
shape AI-constructed brand reputation across twelve European languages [13]: that
paper measures what AI says, and the present one measures the citations beneath
those answers. The work also extends our multi-industry map of AI recommendation
share [14] from what gets recommended to where the recommendation is sourced. We
classify every citation by domain and source type and ask four questions:
Q1 (Owned vs third-party).What share of brand citations point to the brand’s own
site versus third-party sites?
2

T able 1The three merged source datasets. “Rows” counts the native row unit of each file.
Dataset Row unit Rows
Nordic-Baltic (NB) brand×lang×model×
prompt×citation
150,093
Poland (PL) brand×prompt×model×
iteration (citation arrays)
4,151 records /
35,880 citations
Central and Eastern Europe (CEE) attributed source mention 4,001
Q2 (Source mix and concentration).What is the source-type mix, and how concen-
trated is the domain base (the long tail, Zipf fit)?
Q3 (Top sources by language and market).Which domains dominate, and does the
top source change by language and by market?
Q4 (Model differences).Do models differ in how much they cite, what they cite, and
how often they cite the brand’s own site?
We frame the work as measurement. We report where LLMs source brand informa-
tion within a defined sample of brands, languages, and models. We do not claim the
citation mix equals real-world reputation or human perception; we measure a property
of the models’ retrieval and output, which is consequential because those citations are
what the answer is built from.
2 Data and Method
2.1 Three merged datasets
The analysis merges three Rankfor.AI citation datasets (Table 1). Each was collected
by querying grounded LLMs about brands and recording the sources the models cited.
Across the three, the corpus covers 128 distinct brand names (NB 66, PL 57,
CEE 20, with some names overlapping such as Reserved, InPost, Allegro), 13 distinct
languages (NB’s 12 plus Hungarian from CEE), and 12 home markets (the eleven NB
markets: Czech Republic, Denmark, Estonia, Finland, Germany, Latvia, Lithuania,
Norway, Poland, Slovakia, Sweden; plus Hungary).
2.2 Citation counts and what is analysable
The merged total is 189,974 attribution rows, which includes keyword-attributed and
implicit-knowledge rows that carry no URL. The subset that can be analysed by
domain is 167,551 URL-grounded citations: 131,514 from NB, 35,880 from PL, and
157 from CEE. The union of resolved hosts across the three is 22,543 unique domains;
NB alone contributes 23,404 hosts, which normalise to 20,815 registrable domains.
2.3 Mergeability is uneven, and we state it up front
Only NB and PL carry per-citation URLs that resolve to real domains. CEE attributed
96.1% of its sources by keyword (for example “tier1 news”) with no URL; only 157 of
3

its 4,001 rows (3.9%) have a resolvable URL. The merged dataset is therefore a URL-
grounded backbone of NB plus PL, with a small CEE keyword-attribution cross-link,
not one homogeneous citation table. Every domain-level and long-tail figure below is
computed on the URL-grounded data, and CEE is reported separately wherever its
keyword method would distort a URL-based figure.
2.4 One methodology fix before any domain analysis
23,027 NB rows (17.5% of all URL rows, all from Gemini) carry the redirec-
tor hostvertexaisearch.cloud.google.comwhere the real source domain should
be. The real domain sits in the citation-title field (for exampleapple.com,
fashionnetwork.com). All 23,027 were resolved from the title (100% resolution).
This step is load-bearing: without it, the redirector host wins every language and
Wikipedia loses its top-source position everywhere. Every NB domain figure below is
post-resolution.
2.5 How citations were classified
Each URL citation was reduced to its registrable domain (Wikipedia language subdo-
mains aggregated towikipedia.org). An “owned” citation is one where the brand’s
token appears in the cited domain (for examplewise.comfor Wise), applied uni-
formly across all three models so the resolved Gemini rows count correctly. The data
also carry a typed source-type label (company website, wikipedia, industry report,
tier1 news, social media, review platform, government, financial directory, academic,
and a catch-all other web). We report both the brand-token owned rate and the typed
label, and we flag where the label misleads.
2.6 Statistics
The long-tail summary uses the cumulative domain-frequency distribution. The Zipf
fit is a log-log regression on the top-1,000 domain ranks (scipy.stats.linregress).
The source-type by language association uses a chi-square test with Cram´ er’sV. All
counts are direct from the files.
2.7 Honest limits
Three limits bound the reading. First, the three datasets were collected under related
but not identical protocols, so the merge is a backbone plus a cross-link, not a single
homogeneous table. Second, owned-detection depends on the vertex resolution; the
raw NB file is pre-resolution for Gemini, and any owned-rate split by model must use
the resolved domain. Third, citations are scored at the source level, so when a model
lists several brands and cites one source, that source attaches to all brands named in
the response. We return to these in Section 5.
4

T able 2Owned versus third-party citation share, NB
URL-grounded backbone (131,514 citations). “Owned” is the
brand’s token in the resolved domain.
Split Owned Third-party
Overall (URL citations) 14.3% 85.7%
Bycompany websitelabel 16.4% 83.6%
B2B brands 13.1% 86.9%
B2C brands 15.7% 84.3%
3 Findings
3.1 Q1: AI grounds brand answers in third-party sources, not
owned ones
On the NB URL-grounded backbone (131,514 citations, the only large dataset with
reliable owned-domain detection), 85.7% of citations point to sites the brand does not
own and 14.3% point to owned domains (Table 2). Read against all 150,093 NB rows
including the no-URL implicit-knowledge rows, the split is 14.4% owned, 76.1% third-
party, and 9.5% implicit. The typed company website label gives a slightly higher
owned share (16.4%) because it counts on a different base. The reading is the same
under every base: AI reads third parties about a brand four to six times as often as it
reads the brand’s own site.
The split holds for both buyer types, and B2C brands are slightlymoreself-cited
than B2B (15.7% versus 13.1%). Self-citation does not vanish; it concentrates. The
most self-cited brands (among those with at least 1,500 NB citations) are Tatra Banka
at 34.4% owned (2,041 citations), Statkraft 33.9% (2,080), ESET 33.2% (2,059), Wise
32.4% (2,054), Allianz 29.2% (1,969), and Pipedrive 27.5% (2,149). At the other end,
several brands draw 0.0% owned citations: AI never grounds in their own site (Slovak
Telekom, PKN Orlen, Swedbank Estonia, Kiwi.com, Latvijas G¯ aze, Swedbank Latvia).
A brand’s own website is a minority source even for the best self-cited brand, and a
non-source for many.
3.2 Q2: The source mix is dominated by the open web, and
the domain base is concentrated
The typed source-type mix on NB URL citations is one large bucket and a set of small
ones (Table 3). The catch-all other web (trade press, local news, blogs, marketplaces
that the typed categories miss) holds 77.0% of citations. Owned company sites are
16.4%, Wikipedia 3.9%, and every typed news, review, government, and academic
category is small, because most real news and review domains land in other web
and never reach a typed bucket. The honest summary of the typed labels: the open
third-party web is the dominant ground, ahead of any curated category.
The domain base behind that web is concentrated. On a registrable-domain basis
(20,815 domains), 80% of all citations come from 3,778 domains, about 18.2% of the
5

T able 3Typed source-type mix, NB URL citations
(131,514 rows).
Source type Share Count
other web (open third-party) 77.0% 101,285
company website (owned) 16.4% 21,626
wikipedia 3.9% 5,192
industry report 1.0% 1,301
tier1 news 0.7% 907
social media 0.4% 563
review platform 0.3% 394
government 0.1% 192
financial directory 0.03% 38
academic 0.01% 16
base. Half of all citations come from just 547 hosts (2.3% of the 23,404 hosts). The
remaining 20% of citations spread across more than 17,000 tail domains. The domain-
rank distribution fits a Zipf law: a log-log regression on the top-1,000 ranks gives
exponentα= 0.86 (R 2 = 0.983), so then-th-ranked domain receives roughly 1/n 0.86
of citations. A small head of domains carries most of what AI reads; the long tail is
real but thin.
The source-typemixbarely shifts across languages. The chi-square test is signifi-
cant (χ2 = 1906.4,p <0.001) but the effect size is small (Cram´ er’sV= 0.036): at this
sample size significance is cheap, and the smallVis the honest summary. What varies
across languages is not the type mix but which specific domains lead, which is Q3.
3.3 Q3: Wikipedia leads almost everywhere, with one local
exception
The most-cited domains overall (NB, all 12 languages, registrable level) are Wikipedia
(5,800 citations), YouTube (2,826), Statista (1,310), then a run of owned sites and
social platforms:wise.com(908),tatrabanka.sk(733),eset.com(697), Reddit
(619),europa.eu(600),printful.com(599),pipedrive.com(592). The head is a
reference site, a video platform, and a statistics portal, then brand sites and social. The
shape matches independent industry measurements: a 30M-citation analysis across AI
engines ranks Wikipedia and Reddit among the top domains for every engine, with
YouTube and social close behind [15], and a brand-citation analysis across engines
reports a similar non-corporate mix led by YouTube and Reddit [6].
The per-language top source is more revealing (Table 4). Wikipedia is the single
most-cited domain in 11 of 12 languages, with shares from 3.71% (Polish) to 5.70%
(Finnish). The one exception is Lithuanian, where the national business dailyvz.lt
(Verslo ˇ zinios) edges Wikipedia at 4.38%. The exception is instructive: it is exactly
the kind of local business outlet that an English-only or Wikipedia-centric view of AI
sourcing would miss, and it appears in a smaller-language market where local press
fills space the encyclopedia does not.
6

T able 4Per-language top-1 cited domain, NB
(post vertex-resolution). Wikipedia leads 11 of 12
languages; Lithuanian is the exception.
Language T op-1 domain Share
Finnish (fi) wikipedia.org 5.70%
Norwegian (no) wikipedia.org 4.91%
English (en) wikipedia.org 4.75%
Latvian (lv) wikipedia.org 4.60%
Czech (cs) wikipedia.org 4.45%
German (de) wikipedia.org 4.41%
Swedish (sv) wikipedia.org 4.40%
Lithuanian (lt) vz.lt 4.38%
Estonian (et) wikipedia.org 4.37%
Danish (da) wikipedia.org 3.96%
Slovak (sk) wikipedia.org 3.78%
Polish (pl) wikipedia.org 3.71%
T able 5Source split by language family, NB URL citations (owned by resolved domain).
F amily Citations Owned Wikipedia Tier-1 news Domains
Uralic (et, fi) 21,189 15.5% 5.0% 0.9% 4,846
Baltic (lt, lv) 21,313 15.0% 4.3% 1.2% 4,452
Germanic (sv, no, da, de, en) 54,956 14.8% 4.5% 0.6% 10,566
Slavic (pl, cs, sk) 34,056 12.5% 4.0% 0.3% 6,974
The same localisation pattern shows in the per-family source split (Table 5). Uralic
(Estonian, Finnish) and Baltic (Lithuanian, Latvian) responses lean more on owned
sites and Wikipedia (15.5% and 15.0% owned, 5.0% and 4.3% Wikipedia), consistent
with a thinner native web where AI falls back to the brand’s own site and the ency-
clopedia. Slavic responses (Polish, Czech, Slovak) are the least owned-heavy (12.5%)
and least Wikipedia-heavy (4.0%). Baltic carries the highest tier-1-news rate (1.2%),
driven by the Lithuanian and Latvian business press such asvz.lt. Germanic spans
the most domains (10,566), because it includes English plus four national languages
with deep web corpora.
3.4 Q3 (market): in Poland, AI cites job portals about a
brand more than it cites Wikipedia
The market-specific source mix is sharpest in Poland. We resolved the Polish citations
to publisher domains the same way we resolved the Nordic-Baltic set, because Gem-
ini’s Polish citations also arrive as Google grounding redirectors that would otherwise
win the ranking. After resolution, the most-cited single domain across the 46 Polish
national brands (35,880 citations) isyoutube.com(2,289 citations, 6.4%), ahead of
7

T able 6Per-model citation behaviour, NB (post vertex-resolution). Owned is by
resolved domain; the typed label is shown to expose the Gemini artifact.
Model Citations Domains Owned (dom.) Owned (lbl.) Wiki.
Perplexity Sonar Pro 90,276 15,995 16.8% 20.7% 4.9%
Gemini 3.1 Pro 23,032 6,568 5.8% 0.0% 2.6%
GPT-5.4 (OpenAI) 18,206 3,284 12.9% 16.2% 4.3%
the price-comparison and marketplace sitesceneo.plandallegro.pl. The market-
specific pattern sits just below that head: four HR and careers portals (pl.indeed.com
176,livecareer.pl169,interviewme.pl159,randstad.pl133) supply 637 cita-
tions between them, against 297 for Polish Wikipedia. The recruitment portals out-cite
Polish Wikipedia by about 2.1 times. The report’s percentage framing (“HR 10.6%
versus Wikipedia 4.6%”) is computed against a curated authoritative-media pool that
excludes marketplaces, video, and the long tail; the ranking holds against the full
resolved pool while the percentages are smaller, so we report the counts and the 2.1x
ranking and treat the headline percentages as base-dependent.
The reading is concrete for a marketing team. In a market with strong employer-
review and recruitment sites, AI reads those sites to describe a brand. Where a brand
stands on a careers portal is part of what AI says about it, in some markets more than
the encyclopedia entry.
3.5 Q4: models differ in how much they cite and what they cite
Citation behaviour is not uniform across models (Table 6). On the NB backbone, Per-
plexity Sonar Pro cites the most by a wide margin: 90,276 of 131,514 citations (68.6%),
grounding in the widest domain set (15,995 domains). Gemini 3.1 Pro contributes
23,032 citations across 6,568 domains, and GPT-5.4 contributes 18,206 across 3,284
domains. Perplexity is both the highest-volume citer and the highest self-citer (16.8%
owned by resolved domain), and it grounds in Wikipedia most (4.9%).
The Gemini owned-rate figure carries a measurement lesson. Gemini’s typed label
reads 0.0% owned, but its resolved-domain owned rate is 5.8%. The label is zero
because every Gemini citation arrived as avertexaisearchredirector and the type
classifier ran on the redirector, not the real domain. Once resolved, Gemini’s self-
citation moves from a phantom 0% to a real 5.8%. The same artifact appears in the
Poland data: Gemini reads 0.0% owned there too, because its Polish citations are
google.comredirect URLs (Poland per-model: Perplexity 27,591 citations at 18.7%
owned, OpenAI 1,116 at 11.7%, Gemini 7,173 at a redirector-inflated 0.0%). Any
owned-rate comparison across models must resolve the redirector first, or it will report
a model artifact as a brand finding. Across both datasets, Perplexity is the highest-
volume and highest self-citing model, and Gemini grounds in the most fragmented
domain set.
8

4 What This Means for Brands
The sourcing data point to a clear practical reading for marketers, stated as what the
data shows.
Earn coverage; do not rely on your own site.AI grounds brand answers in
third-party sources 85.7% of the time. A brand’s own website is a minority source even
for the most self-cited brands, and a non-source for many. Owned content matters,
and writing a clear company page is necessary, but it is not where AI mostly reads a
brand. The data align with the wider finding that AI search favours earned media over
owned content [5], and with an independent analysis of 23,000-plus brand citations
that splits sourcing into roughly half earned, a third commercial, and under a quarter
owned [16]. The same point holds at the level of individual brand citations here.
Win the head of the distribution.Eighty percent of citations come from about
18% of domains, and the rank distribution is Zipf (α= 0.86). The sources that decide
most AI answers are a small, identifiable set. For these brands that head includes
Wikipedia, YouTube, Statista, Reddit, and the brand’s own site, plus, per market,
specific local outlets. Coverage on the head domains is worth more than scattered
coverage in the tail, which is the operational core of generative engine optimisation [4].
T reat Wikipedia as near-universal, and local outlets as market-specific.
Wikipedia leads 11 of 12 languages. A weak or missing Wikipedia presence is a weak
spot in almost every language at once. At the same time, the source that beats
Wikipedia in Lithuanian (vz.lt) and the recruitment portals that beat Wikipedia in
Poland show that local sourcing is real and market-specific. A source strategy built
only in English, or only around Wikipedia, will miss the outlet that actually leads in
a given market.
Audit per market and per model.The Poland HR-portal pattern and the per-
language top-1 differences mean the sources that describe a brand change by market.
The per-model differences mean they change by engine too: Perplexity cites widely
and often, GPT cites a narrow set, and Gemini’s redirector hides its real sources until
resolved. A single English, single-model audit reports one slice of where AI reads a
brand.
5 Limitations
The merge is a backbone plus a cross-link.Only NB and PL carry resolvable URLs.
CEE attributed 96.1% of its sources by keyword and contributes 157 URL rows to the
backbone and nothing to the domain long-tail or Zipf fit. CEE keyword distributions
(which over-detect “government” and “tier1 news” because they match source names
in prose, not cited URLs) are reported separately and never merged into URL-based
figures.
Owned-detection depends on redirector resolution.The raw NB file is pre-resolution
for Gemini; 23,027 rows had to be resolved from the citation title before any domain
analysis. The brand-token owned rule (brand name in the domain) is a heuristic that
can miss owned sites that do not contain the brand token and can over-count where
a third-party domain happens to contain it.
9

Source-level, not entity-anchored, attribution.A citation attaches to the response,
so when a model lists several brands and cites one source, that source attaches to
all brands named. Entity-anchored scoring would tighten the per-brand owned and
source-mix figures.
Percentage bases differ across reports.The Poland HR-versus-Wikipedia counts
are solid (460 versus 202), but the percentage framing depends on which denominator
pool is used; we report the counts and the ranking and flag the percentages as base-
dependent.
Temporal and version scope.The datasets reflect specific model versions over their
collection windows. Grounded models change their retrieval frequently, so the specific
domain shares and per-model counts are time- and version-dependent.
Measurement, not ground truth.We measure what LLMs cite. We do not claim the
citation mix equals real-world reputation or how people in each market regard these
brands. The citations are consequential because they are what the answer is built
from, not because they are a verified reputation signal.
6 Conclusion
Across 167,551 URL-grounded citations about 128 brands in 13 languages and 12
markets, the sourcing of AI brand answers has a stable shape. AI grounds those answers
in third-party sources 85.7% of the time and in the brand’s own site only 14.3% of
the time. The source base is concentrated: 80% of citations come from about 18%
of domains, fitting a Zipf law (α= 0.86,R 2 = 0.983). Wikipedia is the most-cited
domain in 11 of 12 languages, with Lithuanian the exception, where the business daily
vz.ltleads. The source mix is market-specific at the margin: in Poland the most-
cited domain is YouTube, and four HR and careers portals out-cite Polish Wikipedia
about 2 to 1 (637 versus 297 citations). Models differ, with Perplexity citing the most
and most widely, and Gemini’s redirector masking its real sources until resolved.
The practical implication for brands is consistent across every cut of the data: AI
reads the third-party web, the encyclopedia, and, per market, specific local outlets,
far more than it reads a brand’s own pages. Earned media and a deliberate presence
on the small head of domains that AI actually cites are where a brand can move what
AI says about it. We measure where AI gets its information; the consistency of that
sourcing across 12 markets is what makes it actionable.
Data Availability .The merged citation tables (per-citation domain and source-
type classifications, the per-language and per-market aggregates, and the per-model
breakdowns), together with the analysis script that reproduces the headline numbers
and tables in this paper from the three source datasets, are openly available on Zenodo
at https://doi.org/10.5281/zenodo.20829524 (CC BY 4.0). A live, browsable version
of the underlying index is available at https://open.rankfor.ai/index-2026.
Code Availability .The data-collection and citation-classification pipeline is pro-
vided in the Zenodo deposit.
Acknowledgements.The author thanks the Estonian Entrepreneurship University
of Applied Sciences for institutional support.
10

Declarations
• F unding:This research received no external funding.
• Competing interests:D. ˙Zatuchin is affiliated with both the Estonian
Entrepreneurship University of Applied Sciences (EUAS) and Rankfor.AI, which
develops AI brand-intelligence tools. The three datasets analysed here are Rank-
for.AI research data. The analysis, methodology, and conclusions were the author’s
own; the company had no separate influence on study design or interpretation
beyond the author’s role.
• Ethics approval:Not applicable. The study analysed publicly accessible AI
systems and did not involve human subjects.
• Consent to participate / for publication:Not applicable.
• Author contribution:D. ˙Z. conceived the study, designed the methodology,
performed the citation classification and analysis, and wrote the manuscript.
References
[1] Lewis P, Perez E, Piktus A, Petroni F, Karpukhin V, Goyal N, et al (2020)
Retrieval-augmented generation for knowledge-intensive NLP tasks. In: Advances
in Neural Information Processing Systems 33 (NeurIPS 2020). arXiv:2005.11401
[2] Rashkin H, Nikolaev V, Lamm M, Aroyo L, Collins M, Das D, Petrov S, Singh
Tomar G, Turc I, Reitter D (2023) Measuring attribution in natural language
generation models. Computational Linguistics 49(4):777–840. arXiv:2112.12870
[3] Liu NF, Zhang T, Liang P (2023) Evaluating verifiability in generative search
engines. In: Findings of the Association for Computational Linguistics: EMNLP
2023. arXiv:2304.09848
[4] Aggarwal P, Murahari V, Rajpurohit T, Kalyan A, Narasimhan K, Deshpande A
(2024) GEO: generative engine optimization. In: Proceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining (KDD ’24).
arXiv:2311.09735
[5] Chen M, Wang X, Chen K, Koudas N (2025) Generative engine optimization:
how to dominate AI search. arXiv:2509.08919
[6] Kumar P (2026) Generative engine optimization at scale: measuring brand
visibility across AI search engines. arXiv:2606.20065
[7] Yang KC (2025) News source citing patterns in AI search systems.
arXiv:2507.05301
[8] Aral S, Li H, Zuo R (2026) The rise of AI search: implications for information
markets and human judgement at scale. arXiv:2602.13415
11

[9] Kirsten E, Grosse Perdekamp J, Wu Q, Upadhyay M, Gummadi KP, Zafar MB
(2025) Characterizing web search in the age of generative AI. arXiv:2510.11560
[10] Li A, Sinnamon L (2024) Generative AI search engines as arbiters of pub-
lic knowledge: an audit of bias and authority. Proceedings of the Association
for Information Science and Technology 61(1):205–217. https://doi.org/10.1002/
pra2.1021 (also arXiv:2405.14034)
[11] Fombrun CJ, Gardberg NA, Sever JM (2000) The Reputation Quotient: a multi-
stakeholder measure of corporate reputation. Journal of Brand Management
7(4):241–255. https://doi.org/10.1057/bm.2000.10
[12] Roberts PW, Dowling GR (2002) Corporate reputation and sustained superior
financial performance. Strategic Management Journal 23(12):1077–1093. https:
//doi.org/10.1002/smj.274
[13] ˙Zatuchin D (2026) The language blind spot: how query language and brand
recognition tier shape AI-constructed brand reputation across twelve European
languages. arXiv:2606.23165
[14] ˙Zatuchin D (2026) Who owns the AI recommendation? A multi-industry empirical
map of brand category ownership across large language models. arXiv:2606.23057
[15] Peec AI (2026) Top domains cited by AI search: analysis based
on 30M sources. Peec AI, 19 June 2026. https://peec.ai/blog/
top-domains-cited-by-ai-search-analysis-based-on-30m-sources
[16] Dombrowski C (2026) How LLMs source brand information: an analysis of
23,000+ AI citations. Omniscient Digital, 8 January 2026. https://beomniscient.
com/blog/how-llms-source-brand-information/
12
