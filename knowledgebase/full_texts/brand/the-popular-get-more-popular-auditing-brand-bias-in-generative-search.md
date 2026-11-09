---
title: 'The Popular Get More Popular: Auditing Brand Bias in Generative Search'
url: https://arxiv.org/abs/2611.07614
category: brand
subcategory: empirical
date: 2026-11
venue: ''
authors:
- Giorgio Monaco
- Jacopo Lenti
- Francesco Pierri
source: arxiv
pdf_url: https://arxiv.org/pdf/2611.07614
pages: 30
chars: 107872
fetched_at: '2026-11-08T12:57:11+00:00'
kb_version: 1
---

# The Popular Get More Popular: Auditing Brand Bias in Generative Search

The Popular Get More Popular: Auditing Brand Bias in Generative Search
GIORGIO MONACO,Politecnico di Milano, Italy
JACOPO LENTI,Politecnico di Milano, Italy
FRANCESCO PIERRI,Politecnico di Milano, Italy
The shift from traditional to generative search has fundamentally transformed online product discovery. Because conversational
recommendations synthesize choices into a few direct answers, subtle systemic preferences toward specific providers can exert
profound commercial impacts. In this work, we audit this phenomenon through two distinct dimensions: (i)brand popularity bias, the
systematic preference for market-dominant entities over long-tail alternatives, and (ii)brand familiarity bias, the ranking advantage an
entity encoded in an LLM’s parametric memory holds over an unfamiliar competitor. First, evaluating commercial queries across major
engines, we observe persistent brand popularity bias: dominant brands in the top quintile are cited1 .4× to2 .8× more frequently than
the average brand within a sample of 1,176 top market players, already present in parametric memory that external web retrieval fails
to mitigate. Second, through controlled in-context experiments holding product attributes constant, we find that substituting authentic
brand signatures with unfamiliar ones significantly degrades recommendation rank. Conversely, fact-preserving content rewrites
yield negligible ranking gains. Taken together, our findings demonstrate that generative search engines reinforce a “rich-get-richer”
dynamic by favoring established market leaders and imposing a parametric barrier to entry that standard content optimization cannot
overcome.
CCS Concepts:•Information systems → Web search engines;Language models;•Social and professional topics → Computing
/ technology policy.
Additional Key Words and Phrases: generative search engines, generative engine optimization, algorithm audit, provider fairness,
entry barriers, buyer personas, large language models
1 Introduction
Chatbots and search engines powered by Large Language Models (LLMs) have shifted consumer product discovery
from static URL ranking to conversational, fine-grained recommendations with synthesized justifications. Because
users ascribe high credibility to these outputs and increasingly rely on them for everyday decisions [44], generative
search exerts substantial influence over consumer choice and market exposure. Auditing the mechanisms governing
LLM-driven product recommendations is therefore of paramount importance.
Because these instruments operate at a global scale, minor systematic biases in their generation logic can produce
profound market effects, as brands prioritized by generative search engines might gain distinct commercial advantages.
While model preferences may sometimes reflect genuine product superiority, it is critical to disentangle meritocratic
selection from systemic model bias. Trained on massive Web corpora, LLMs inevitably inherit and amplify pre-existing
statistical biases [18]. While recent literature has audited LLMs for sociodemographic biases—including gender [ 2],
ethnicity [38], and social group [26]—as well as prompting biases like persona [21] and cognitive biases [16], brand-level
economic biases remain underexplored.
In this study, we formalize and audit two distinct dimensions of brand bias:
(1) Brand Popularity Bias:The systematic preference of LLMs toward highly popular, high-market-share brands
over long-tail or niche alternatives. Overrepresented in pre-training corpora, popular brands might enjoy a
Authors’ Contact Information: Giorgio Monaco, giorgio.monaco@mail.polimi.it, Politecnico di Milano, Milan, Italy; Jacopo Lenti, jacopo.lenti@polimi.com,
Politecnico di Milano, Milan, Italy; Francesco Pierri, francesco.pierri@polimi.it, Politecnico di Milano, Milan, Italy.
1
arXiv:2611.07614v1  [cs.CY]  5 Nov 2026

2 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
structural head start in user recommendations, which may create a “rich-get-richer” (or Matthew) effect [31].
This could reduce the visibility of local or specialized competitors [25, 30].
(2) Brand Familiarity Bias:The advantage a brand recognized within an LLM’s parametric memory holds, at
equal content, over an unfamiliar or novel entrant. This dimension evaluates the algorithmic barrier to entry
for newly emerging brands that lack pre-existing weight representations in frozen models.
Concurrently, the shift toward generative search has spurred novel visibility-seeking strategies known as Generative
Engine Optimization (GEO) [1]. Analogous to traditional marketing, GEO aims to alter page representations—adjusting
style, tone, and keyword alignment—to maximize the probability of selection by LLM-based chatbots and search engines
[1, 36]. However, the relative weight that LLMs assign to surface-level text optimization versus deeply memorized brand
entities remains unclear. In this work, we contrast the impact of changing brand identity against rewriting content via
GEO techniques to test whether LLMs decouple brand name authority from underlying product descriptions.
Notably, the normative relationship between brand bias and recommender fairness is nuanced [7, 45]. On one hand,
fair recommendation engines should evaluate product merit independently of brand prominence, benefiting both niche
vendors through equal exposure and consumers through increased diversity. On the other hand, established brands
often correlate with higher consumer trust, quality control, and widespread user satisfaction. Prioritizing well-known
brands may therefore align with average consumer expectations. Nevertheless, LLMs are known to suffer from mode
collapse [47]; in commercial recommendations, this behavior risks creating digital market oligopolies, suppressing fair
competition, and locking users into homogeneous recommendations. To understand these dynamics, we address two
research questions:
• RQ1:How do deployed generative search engines distribute visibility among brands across varying levels of
popularity?
• RQ2:How do manipulations of a product page, such as swapping brands/products and using GEO rewriting
strategies, affect its recommendation rank?
We evaluate these questions across four distinct commercial sectors in the Italian market: Sport, Fashion&Beauty,
Insurance, and Travel. InStudy 1, we quantify brand popularity bias by evaluating brand text mentions and web
source citations under both search-on (RAG-enabled) and search-off (parametric memory only) conditions. InStudy
2, we evaluate brand familiarity bias and GEO influence by manipulating product descriptions—swapping real and
invented brand names and applying GEO stylistic rewrites to test ranking stability.
Our contributions are the following:
• We propose an experimental methodology to isolate and evaluate brand popularity bias and brand familiarity
bias in generative search, accounting for web grounding, buyer personas, brand names, and GEO rewrites. The
framework rests on a simple fairness criterion, equal rank at equal content, and in principle applies to any
domain and model.
• We demonstrate that commercial generative search engines exhibit significant favoritism toward popular brands
across both parametric generation and web-retrieved citations.
• We show that the same page ranks lower under an invented brand than under its real brand, at equal content
(brand familiarity bias), and that GEO rewrites do not close this gap.

The Popular Get More Popular: Auditing Brand Bias in Generative Search 3
2 Related work
Auditing algorithmic systems is a cornerstone of socio-technical inquiry, tracing back to foundational frameworks in
traditional search engines [20, 32, 39]. However, the paradigm shift from static ranked lists of URLs to synthesized
natural language answers has introduced novel systemic risks, prompting urgent calls for updated auditing paradigms
suited for generative search [24].
Auditing Generative Search Engines.Generative search engines reconfigure the information ecosystem, impacting
content creators, end users, model providers, and digital markets simultaneously [37]. While generative search engines
draw on a wider range of sources compared to traditional web search [24], their reliability remains deeply problematic.
Grounding evaluations reveal that many generative claims are unsupported by or misattributed to their cited sources [28].
Moreover, generative search exhibits persistent socio-technical vulnerabilities, including overconfidence, unannounced
source selection heuristics, and high response stochasticity [10, 28, 33, 42]. These dynamics obscure accountability,
making it difficult for users to evaluate the factual integrity or commercial neutrality of recommended content.
Economic Fairness and Popularity Bias in Recommender Systems.Recommender system fairness was a critical
area of study well before the advent of LLMs [6]. Fairness in recommendation is inherently multi-sided, encompassing
bothconsumer fairness(ensuring users receive honest, diverse, and unbiased recommendations) andproducer fairness
(ensuring items or vendors are not penalized for features unrelated to product merit) [7, 43]. Focusing on generative
models, LLMs inherit statistical distribution from their massive web pre-training corpora [46], thus amplifying their
bias to end users via authoritative and credible responses in natural language [37], thus mining model fairness and
accountability. Algorithmic biases in LLMs span social and attribute dimensions (favoring protected demographic
groups), linguistic and knowledge dimensions (disadvantaging specific languages), system and optimization dimensions
(driven by interface design), and data or propensity dimensions [ 29]. Among data-driven biases,popularity biasis
particularly prevalent in recommender systems [25]. LLMs demonstrate a strong structural propensity to recommend
head-items overrepresented in their training data [11, 15]. Mitigating popularity bias directly enhances producer fairness
toward long-tail and underrepresented entities [13, 14]. Under the broader umbrella ofbrand bias, LLMs systematically
prioritize global brands over regional or local alternatives [22].
Entity-Level, Name, and Geographic Preference Biases.LLM recommendation outcomes are also heavily modulated
by prompt-level conditions and textual entity names. For instance, conditioning LLMs with distinct buyer personas
significantly alters the commercial brands recommended in generated outputs [21]. Furthermore, changing only an
entity’s name reveals deep-seated model preferences. Audit literature in human audit studies established that audit
testing via resume name manipulation reveals systemic racial and ethnic disparities, favoring names associated with
White individuals [4, 17]. Parallel name-based biases persist in LLMs, where decision-support models penalize names
tied to women and racial minorities [2, 38]. In product recommendation contexts, an item’s product name and document
ordering substantially distort its generated ranking [ 35]. Similarly, cross-cultural audits indicate that open-weight
models originating from the US, Europe, and China exhibit geographic skews toward domestic brand origins when
ranking shopping items, though explicitly stating the user’s location can recalibrate these rankings [5].
Generative Engine Optimization (GEO) and Strategic Manipulation.The susceptibility of LLMs to textual
manipulation introduces new surface vectors for commercial exploitation. Third parties can intentionally alter product
page representations to inflate recommendation probabilities [ 16]. Mirroring human purchasing heuristics, LLMs
exhibit vulnerability to embedded cognitive bias triggers—such as social proof, exclusivity, scarcity, discount framing,
and authority claims—which significantly increase an item’s generated visibility. This vulnerability has driven the

4 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
rise ofGenerative Engine Optimization (GEO), wherein web pages are strategically rewritten using statistics, quotes,
and authoritative formatting to maximize AI retriever selection [1]. While some studies confirm the efficacy of GEO
techniques, others observe mixed or neutral impacts [27, 36]. Crucially, the proliferation of strategic GEO manipulation
creates a classicPrisoner’s Dilemmafor content providers and vendors: individual entities have a strong competitive
incentive to adversarially optimize their content for LLMs, regardless of competitor actions, ultimately degrading
the overall utility and trustworthiness of the search ecosystem [ 34]. Because post-hoc data filtering is inherently
complex, current mitigation strategies primarily target output generation via fairness-guided prompting [ 29], logit
re-confidencing [9], or in-context learning constraints [41].
Position of Our Contribution.Building upon the established literature in recommender fairness and generative
search audits, this work disentangles brand bias along two distinct socio-technical axes:brand popularity biasand
brand familiarity bias. While prior work has recognized general head-item dominance [ 11, 25], we systematically
measure how popularity bias restricts visibility for long-tail vendors across both inline textual mentions and web source
citations. The same approach could be applied to other entities whose name a model may know, such as news outlets
or other sources [12, 23]. By explicitly evaluating models under both Retrieval-Augmented Generation (search-on)
and non-retrieval (search-off) settings, we isolate the inherent bias of parametric model memory from grounding
retrieval mechanisms.
Furthermore, our study extends current auditing paradigms for RAG systems [24, 28] by examining the initial search
queries generated by LLMs. Chen and Koudas [10] observe that brands the model already knows are written into the
search queries; we measure how this changes with brand popularity. In some contexts, we reveal that popular brands
secure a structural advantage early in the retrieval pipeline, shaping the initial web queries before final synthesis occurs.
Finally, whereas existing entity-manipulation studies focus primarily on isolated name swaps or stylistic rewrites [1, 35],
our findings suggest that LLMs may evaluate brand identity in tandem with product-description coherence. We show
that unfamiliar brands face a notable entry barrier even when paired with identical product specifications, while
mismatched brand-product associations appear to incur an additional coherence penalty.
3 Methods
Figure 1 shows the pipeline of the two studies. Study 1 is an observational, data-driven audit of three deployed engines.
We collect their answers to a set of real commercial prompts and measure how the popularity of a brand relates to its
mention share and citation share (brand popularity bias). Study 2 is instead a controlled experiment, where we isolate
the effect of brand name swap (brand familiarity bias) and strategic rewrite (GEO effect) on the rank of a page. Table 1
lists the engines of both studies.
3.1 Study 1: the audit
We study brand popularity bias, by interrogating the LLMs under different settings, investigating the mention and
citation shares of brands, paired with brand popularity.
Data collection.The prompts are recommendation questions derived from what real users search for.
We collected keyword data from DataForSEO for four sectors, Insurance, Travel, Fashion&Beauty, and Sport,
keeping commercial keywords that name no brand. In each sector, we drew keywords at random across levels of search
volume, with at most two per sub-topic (for example, car insurance and travel insurance ), and an LLM turned
each keyword into one question with a fixed instruction, for example“Quale assicurazione RC moto scegliere?”(“Which

The Popular Get More Popular: Auditing Brand Bias in Generative Search 5
Study 1: the audit
80 commercial prompts
× 4 personas
× 2 search settings
× 10 repeats
× 3 engines
T otal: 19,200 answers
What we observe
Search queries
Sources → citation
Answer text → mention
Brand popularity
External search volume
Hypotheses
H1 Brand popularity bias
H2 Search queries effect
H3 Personas effect
Study 2: the experiment
24 prompts
× 5 signatures × 4 texts
× 10 orders × 2 repeats
× 4 models, search off
T otal: 38,400 rankings
What we observe
Rank of the target page
Hypotheses
H4 Brand familiarity bias
H5 GEO-rewrites effect
prompts, brands and pages from Study 1
Fig. 1. Study 1 is an audit of three deployed generative search engines on commercial prompts, with search-on and search-off,
and with and without a persona context. Study 2 takes 24 of these prompts and manipulates two features of one product page, the
brand that signs it and its text (GEO rewrites), while four models rank it among five pages withsearch-off.
Table 1. Engines of the two studies.Study 1,Study 2: whether the engine is used in the study; Study 1 runs each engine with
search-off and search-on, Study 2 only with search-off.Ordered search actions: whether the API returns the engine’s successive
searches in the order they were made.Searches: share of the Study 1 calls with search-on in which the engine searched the web. In
the results, we refer to the models as GPT, Gemini, Perplexity, and DeepSeek.
Model Study 1 Study 2 Ordered search actions Searches
gpt-5.5✓ ✓ ✓98%
gemini-3.6-flash✓ ✓ ✗44%
perplexity/sonar✓ ✓ ✗100%
deepseek-v3.2✗ ✓– –
motorbike liability insurance should I choose?”). Each prompt is asked without persona, as a baseline, and preceded by
each of three buyer personas of its sector. A persona consists of three sentences describing life stage, experience with
the category, and attitude to price. The Baseline persona (A) wants to spend as little as possible; the Price variant (B)
changes only the price sentence, and the Profile variant (C) changes life stage or experience while keeping the same
price sentence of A.
They should be considered as controlled purchase contexts, not demographic segments. Appendix Tables A.1 and A.2
list prompts and personas.
We ask 20 prompts of each sector without a persona and with each of the three personas, with search-off and
search-on, 10 times, to each of 3 engines with web search, gpt-5.5, gemini-3.6-flash and perplexity/sonar
(Table 1). This gives80×4×2×10×3=19,200answers. Additional details are in Appendix B.
Metrics.A brand ismentionedwhen it appears in the text of an answer, andcitedwhen its official site is among the
answer’s sources. We definemention rateof brand 𝑘, the proportion of answers that mention 𝑘 in the text at least
once. We definecitation rateof 𝑘, as the proportion of answers that cite the official website of 𝑘, limiting on the brands
for which we know the official domain (683 out of 1,176 brands). To account for the different prevalence of mentions
and citations, we also normalize each rate by its average rate within the same sector and engine. We compute brand’s

6 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
popularity by log10(1+𝑣) , where 𝑣 is the mean monthly number of Google searches for its name in Italy over twelve
months, obtained from DataForSEO1.
We measure brand popularity bias as the slope of the mention rate (or citation rate) on popularity, estimated by
Ordinary Least Squares (OLS) with one point per brand. If popularity bias equals 1, an increase of Google searches by
10 times implies an increase of 1 percentage point in the mention rate, i.e. one more answer out of 100. Theeffect of
Web searchon brand𝑘is its mention rate withsearch-onminus its mention rate withsearch-off.
In Study 1, we also estimate how citation, mentions, and text vary with the same prompts and different personas. We
measurequery similarityas symmetric best-match cosine between their search queries, embedded with BGE-M3 [ 8], a
multilingual model, since the search queries are both in Italian and English. Two answers can issue a different number
of search queries, so each search query is matched with the most similar one of the other answer, in both directions. On
the answer side, we measure the similarity between the set of retrieved brands (or sources) with Jaccard index. Answer
text similarity is measured with cosine similarity between their embeddings.
With search-on, we can obtain both mentions and citations. A brand that is mentioned isfoundif its name appears
in the text of at least one returned source, it hasno matchif it does not appear in sources and sources are available, and
itcannot be verifiedif at least one source cannot be read.
When using GPT, we can also inspect the order of actions deployed by the engine. In particular, withsearch-on, we
measure how often a brand appears in the query of first search. Since GPT writes its first search query before receiving
any web result, this behavior indicates that the engine drives the search biased by model’s own knowledge, favouring
the brand that appears in the first query.
A separate model (gemini-2.5-flash, temperature 0) lists the brands mentioned in each answer, and we merge by
hand the spelling and product-line variants of the same brand; a manual check on 30 answers found 96% of the extracted
names correct (Appendix B). A brand enters the analysis of a sector if at least one engine mentions it 5 or more times.
We then compute its rates for all three engines. This gives 1,176 brands, 1,159 of them with a popularity value. As a
robustness check, we repeat the analyses with a separate set of brands for each engine and with a threshold of 10 (see
Appendix Table C.1). The source check uses the mentions of brands that reach the threshold in the engine itself.
In our analyses, the prompt is the sampled unit. Intervals are 95% intervals from 1,000 bootstrap draws of the prompts
within each sector, each draw keeping all the answers to the drawn prompts. Differences use the same draws. We
compare the slopes with search-off and search-on by resampling brands within each configuration instead (2,000
draws; Appendix Table C.2). Correlations across brands come with their standard 𝑝-values. We correct families of tests
with Benjamini–Hochberg [3].
3.2 Study 2: the controlled experiment
In Study 2 we address RQ2 in a controlled experiment. An audit cannot tell whether an engine prefers a brand for its
name or for its content, so here we fix the pages and change, on one of them, the name that signs it and the way it is
written. We include 5 product pages in the prompt, close to the mean number of sources per answer in Study 1 (on
average 4.6 for GPT and 5.3 for Gemini; Perplexity returns all the results it retrieves, 9.0 on average), and ask the LLMs
to rank them (withsearch-off), with different interventions.
Outcome.In each call a model receives a question and five pages in a given order, answers the question citing the
pages and ends with a ranking of all five (Appendix D gives the full message). One of the five is thetarget, the page we
1https://dataforseo.com, a commercial provider of search engine data.

The Popular Get More Popular: Auditing Brand Bias in Generative Search 7
change. An intervention effect is the number of positions gained by the target with the intervention. For example, if the
target is third under its real brand and fourth under an invented brand, the effect is−1.
We took a subsample of 24 prompts of Study 1, six per sector (Appendix Table D.1). These prompts ask the user to
choose a product and have at least seven candidate brands. Brands that are mentioned in at least 5 of the 240 Study 1
answers to the prompt, with a verified official site, that sell the product under their own name. Among the most
mentioned candidates, the most popular is set aside as theBetter knownsignature (see below), so it never supplies a
page. The five most mentioned of the remaining candidates supply one product page each from their official site.
We use the full text of each page, without menus, reviews or related products. Before the experiment, a calibration
run asked the four models to rank the five real pages. The target is the page whose mean rank in this run is closest to 3,
so that it has room to move both up and down. The other four pages never change.
We change the target in two ways. Thesignatureis the set of names on the page: the brand, the product and its
technologies, codes and web address. Thetextis the way the same facts are written. To intervene on the signature, we
turn the text of the target into a template in which every name is a placeholder, and we fill the placeholders in five ways.
Original brand Real productuses the true brand and product, andOriginal brand Invented productthe true brand with an
invented product.Better known Invented productandLess known Invented productuse, respectively, a more popular and
a less popular real brand, with the same invented product.Invented branduses an invented brand, whose .it domain
does not exist, with the invented product. The five versions are identical word for word except for the names.
Better knownandLess knownbrands are, respectively, the most popular among the brands most mentioned for the
prompt, and the least popular brand mentioned for it; the target must be at least twice as popular as the less-known
brand and at most half as popular as the better-known one.Invented brandnames share no distinctive part with the real
ones. Appendix D gives the full rules.
InBetter known Invented productandLess known Invented product, a real brand with an invented product may itself
look odd to a model. So, when theBetter knownorLess knownbrand sells a product of the same category as the target
under a name of its own, we addBetter known Real productandLess known Real product, which sign the page with that
brand and that real product. This is possible for bothBetter knownandLess knownbrands in 15 of the 24 questions
(Appendix Table D.2). The product is the one of that brand most mentioned in the Study 1 answers to the prompt or, if
there is none, the first suitable one on its official category page. In the other questions the target page mentions no
product, the brand sells none with a name of its own, or, in travel, the product is a holiday tied to a place.
To intervene on the text, three rewrites keep every fact of the original and change only how it is written.Structure
puts the decisive information first and uses headings and lists, whileFluencyandAuthoritativefollow two methods
of Aggarwal et al. [1]. gpt-5.5 writes the rewrites on the template, so every signature carries the same rewrite. We
keep a rewrite only if the placeholders and numbers are unchanged, its length is within 15% of the original, so that a
rewrite cannot gain or lose rank by adding or cutting text, and a different model (deepseek-v3.2) finds no fact added
or removed (Appendix D).
The placeholders remove the names, but the text may still reveal the brand, for example through a typical formula or
a distinctive feature. To measure how often this happens, each model reads the target page with all names replaced, and
we ask it which real brand the page belongs to (24 questions, 4 models, 3 repetitions). The question invites a guess that
the ranking task does not, so the share of correct answers is an upper bound, as in the leak test of Chen and Koudas
[10]. In the rankings, we also count how often the answer mentions the original brand of the target when the page
carries another signature.

8 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
least
popular
most
popular
0
2
4
6
answers mentioning
the brand (%)
a GPT
least
popular
most
popular
b Gemini
least
popular
most
popular
c Perplexity
search off
search on
Fig. 2. Mention rate as a function of popularity, with search-off and search-on, all sectors and personas together. Share of answers
that mention the brand, with search-off (grey) and search-on (green), by quintile of popularity within each engine and sector.
Points are means over the brands of each quintile (about 240), with 95% intervals from 1,000 prompt bootstrap samples, stratified by
sector.
For each question, we collect 5 signatures, with 4 texts, with 10 balanced orders of the five pages, each repeated twice,
on 4 models. In addition to the three engines of Study 1 with search-off, we include the open-weight deepseek-v3.2
(Table 1). We balance the orders so that each page appears in each position equally often. This gives24× 5× 4× 20× 4 =
38,400rankings. The real-product versions add 9,600 rankings with the same texts, orders, repetitions and models.
Each effect is a difference in rank between two versions of the target in calls that are otherwise identical. We average
these differences in three steps, first within each model and question, then over the four models, then over the 24
questions, so that every model and every question has the same weight. Because every signature is collected with
every text, an effect of the signature is averaged over the four texts, and an effect of the text over the five signatures.
This average summarises each factor fairly only if the two do not interact, so we also estimate the effect of rewriting
under each signature (Figure 7b and Appendix E). The 24 questions are the sampled unit: we resample them 2,000 times
to obtain 95% intervals, and we test each hypothesis with a one-sided 𝑡 test on the 24 question means, adjusting the
𝑝-values with the Holm method [19].
4 Results
4.1 Study 1: the audit
H1: Generative search engines are affected by brand popularity bias.
If generative search engines are affected by brand popularity bias, the correlation between brand popularity and mention
share should be positive (H1a), and so should the correlation between brand popularity and citation share (H1b). With
search-off the engine can rely only on what it learned in training, so we also expect the correlation with mention
share to be stronger withsearch-offthan withsearch-on(H1c).
Figure 2 shows that the mention share rises with brand popularity, from below 1% in the least popular quintile to 1.2–5.3%
in the most popular, depending on the engine, withsearch-off and search-on. The correlation between popularity and
mention rate is positive and significant in 23 of the 24 configurations (Spearman’s 𝜌 up to 0.47, Benjamini–Hochberg),
indicating that, among the brands the engines mention, more popular brands are mentioned more often. The exception
is Perplexity in Travel with search-off (𝜌= 0.08; its curve is in Appendix Figure C.1).H1a is supported.Figure 3
puts mention and citation on the same relative scale. On all three engines both rise with popularity, and a brand in the
most popular quintile is mentioned and cited 1.4 to 2.8 times as often as the average brand of its engine and sector.

The Popular Get More Popular: Auditing Brand Bias in Generative Search 9
least
popular
most
popular
0
1
2
3
rate relative to the
engine-sector mean
a GPT
least
popular
most
popular
b Gemini
least
popular
most
popular
c Perplexity
mention
citation
Fig. 3. Mention share and citation share by quintile of popularity, search-on, only for brands with a known domain. Each rate is
divided by its mean over the brands of the same engine and sector. As such, 1 is the average brand (dashed line) and the levels of
mention and citation are not comparable on this scale. Quintiles are formed within each engine and sector; points are means pooled
over the four sectors, with 95% intervals from 1,000 prompt bootstrap samples, stratified by sector.
Relative to their own averages, mention and citation rise at the same rate on GPT, mention rises faster on Gemini
and citation faster on Perplexity (Appendix Table C.3). The correlation between popularity and citation is significant
in 8 of the 12 engine–sector pairs after Benjamini–Hochberg (Appendix Figure C.2).H1b is partially supported:
it holds in these eight pairs, and not in Sport and Travel on GPT and on Gemini. In Appendix Figure C.3, we also
show that mention and citation shares present wide variations across engines in absolute terms. In Figure 2 the curves
with search-off and search-on overlap. A brand searched ten times more often on Google is mentioned in 0.87
more answers out of 100 with search-off and in 0.89 more with search-on (difference +0.02 [−0.03, 0.07]; Appendix
Figure C.4).H1c is not supported.
H2: Search queries shape the sources of an answer, but not the brands it mentions.
To see where the mentioned brands come from, we compare pairs of answers to the same prompt. IfH2holds, answers
whose search queries are more similar should also be more similar in their sources and text (H2a), while the similarity
of the brands they mention should not grow with query similarity, since brands come mostly from what the model
already knows (H2b).
Figure 4 relates the similarity of two answers to the same prompt to the similarity of their search queries. On all three
engines, the more similar the search queries, the more similar the sources, the mentioned brands and the text, and the
slope is largest for sources, then brands, then text (on GPT 4.10, 3.57 and 2.30, on a scale where 0 means as alike as
answers to different prompts and 1 as alike as two repeats). The relation holds also when we remove brand names
from the search queries before measuring their similarity (Appendix C.2).H2a is supported.When two answers have
more similar search queries, the overlap between their mentioned brands also increase, almost as much as their sources
(on GPT, slope 3.57 for brands against 4.10 for sources). This is hard to reconcile with brands coming only from the
model’s memory.H2b is not supported.Two further observations, each on a different subset of calls, show where the
names of the mentioned brands appear. In Travel, the share of mentioned brands already in GPT’s first search action
rises from 7% in the least popular quintile to 45% in the most popular (+0.38 [0.19, 0.63]); in Insurance the increase is
smaller but also significant, from 1% to 8% (+0.07 [0.02, 0.15]) (Figure 5). Furthermore, when the engines search, the
name of a mentioned brand appears in at least one returned source for 95.5% of the mentions on GPT, 60.9% on Gemini
and 97.3% on Perplexity; on Gemini, 24.9% of the mentions could not be verified. Notice that in 36.2% of all checked
mentions the name appears only on third-party pages, so a brand can be visible in the answer without being cited

10 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
0.6 0.7 0.8 0.9
0.0
0.5
1.0Answer similarity
as similar as
two repeats
as similar as two
different prompts
a GPT
0.6 0.7 0.8 0.9
Query similarity
b Gemini
0.6 0.7 0.8 0.9
c Perplexity
Sources
Brands
Answer text
Fig. 4. Similarity of answers—in terms of sources, brands, and text—as a function of similarity of search queries. Query similarity
matches each search query of one answer with the most similar search query of the other, and averages their cosine in both directions.
Answer similarity is rescaled so that 0 is the mean similarity of two answers to different prompts and 1 the mean similarity of
two repeats (dashed lines). Values above 1 mean that two answers are more alike than two repeats on average, as happens when
their search queries are very similar. Points: mean of the pairs in each of eight bands of query similarity; bands: 95% intervals from
resampling prompts.
l.p. m.p.
0
50
100share (%)
Insurance*
l.p. m.p.
Fashion & beauty
l.p. m.p.
Sport
l.p. m.p.
Travel*
first search
later searches only
Fig. 5. GPT, search-on. For each quintile of popularity, the share of mentioned brands whose name is already in GPT’s first search
action (dark), or appears only in later actions (light). Brands are split into quintiles of popularity within each sector, from least popular
(l.p.) to most popular (m.p.). Bars: 95% intervals from resampling prompts.∗ The first-action share of the most popular quintile differs
from that of the least popular quintile, significant after Benjamini–Hochberg over the four sectors.
(Appendix C.2). Together with a brand popularity bias that is as strong with search-on as with search-off, these
observations suggest that popular brands can reach the answer through the model’s memory even withsearch-on.
H3: The user persona does not affect the recommendations.
We then place a buyer persona before the question. If the persona does not affect the recommendations, the brand
popularity bias should be the same with and without a persona context (H3a), and two answers to the same prompt
with different personas should be as similar as two answers with the same persona (H3b).
Figure 6 compares the mention rate by quintile of popularity without a persona context and with a persona. With a
persona the curve is lower in the most popular quintiles, so the persona might reduce the brand popularity bias. The
slope of mention share on popularity falls from 0.98 without a persona context to 0.80 with the Baseline persona (A)
and 0.85 with the Price variant (B), both significantly lower; with the Profile variant (C) it is 0.89, not significantly
different (Appendix C.3). Engine by engine and sector by sector, after the Benjamini–Hochberg correction only 12 of
the 36 differences from no persona are significant, and in 11 of them the slope is lower with the persona (Appendix C.3).
H3a is not supportedfor the Baseline persona (A) and the Price variant (B). Checking the search queries, we note that

The Popular Get More Popular: Auditing Brand Bias in Generative Search 11
least
popular
most
popular
0
2
4
6
answers mentioning
the brand (%)
a GPT
least
popular
most
popular
b Gemini
least
popular
most
popular
c Perplexity
No persona
context
Persona
(mean of three)
Fig. 6. Mention rate by quintile of popularity, without a persona context (black) and averaged equally over the three personas (blue),
search-off and search-on together. Points: mean share of answers mentioning a brand, pooled over sectors; bars: 95% intervals
from 1,000 prompt bootstrap samples, stratified by sector.
Original
brand
Better
known
Less
known
Invented
brand
3.0
3.2
3.4
3.6
3.8 mean rank
a Mean over rewrites
Original
brand
Better
known
Less
known
Invented
brand
b Separate rewrites
Original
Structure
Fluency
Authoritative
Real product
Invented product
Fig. 7. Study 2: mean rank of the target page (1 = ranked first; better ranks are higher in the plot) under each signature. The horizontal
axis represents the manipulation on the brand that signs the page. Point style represents the manipulation on the product, filled
points have a Real product name of the corresponding brand, and hollow points an Invented product name. (a) Mean over the original
text and the three rewrites. (b) Colors encode the text rewriting strategy, includingOriginal,Structure,Fluency, andAuthoritative.
Points: mean rank over the four models and over the questions in which each version exists (15 of the 24 forBetter known Real product
andLess known Real product). Bars: 95% cluster bootstrap intervals over questions.
with the Baseline persona (A) or the Profile variant (C), at least one search query contains a price word in 86–96% of
the calls in Fashion&Beauty, Sport and Travel, against 25–46% without a persona context. Two answers to the same
prompt with different personas share fewer sources than two repeats with the same persona: their source similarity
(Jaccard index) is lower by 0.07–0.08 on the three engines. Adjusting for the similarity of the search queries reduces the
gap to 0.01–0.035 but does not close it (all intervals below zero).H3b is not supported.
4.2 Study 2: the controlled experiment
H4: Generative search engines are affected by brand familiarity bias.
We compare versions of the same target page that differ in the names they carry (Section 3.2; Figure 7a). To verify
that our text manipulation cleanly neutralized brand identity, we tasked the model with recovering the original brand
from the modified page text. The model guessed correctly in 38% of cases; however, this recognition rate exhibits
no relationship with the observed true-brand effect (Appendix E). If generative search engines are affected by brand

12 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
Table 2. Study 2: change in the rank of the target page ( Δ, positions on a scale of 1–5, positive = ranked higher) between the two
versions each row compares, named as in Figure 7 ( tReal product, dInvented product). Each signature row is the difference between
two points of Figure 7a. Mean over the 24 questions of the mean over the four models; one-sided𝑝, Holm-adjusted (n.s.: not significant).
Effects of the signature average the four rewrites; effects of rewriting average the five signatures.
What changes on the target page𝚫Holm𝑝
Who signs it (Figure 7a)
Original brand Real product tvs Invented brand d H4a+0.44<.01
Original brand Real product tvs Original brand Invented product d H4b+0.14<.05
Better known Invented product dvs Less known Invented product d H4c+0.05n.s.
Original brand Invented product dvs mean of Better known and Less known Invented product d H4d+0.08n.s.
Less known Invented product dvs Invented brand d H4e+0.19<.01
How it is written (Figure 7b)
Rewritten vs original text (mean of the three GEO rewrites)H5a+0.02n.s.
ΔofH4aminusΔofH5a H5b+0.42<.01
familiarity bias, the page should rank higher with its true brand and product (Original brand Real product) than with an
invented brand and product (Invented brand) (H4a). We then look for where this advantage comes from. With its true
brand, the page should rank higher with its real product name than with an invented one (Original brand Real product
againstOriginal brand Invented product,H4b). When another real brand signs the page, with the same invented product,
the text describes a product of a different brand. Neither of the two other real brands owns the page, so comparing
them with each other cancels this mismatch. If popularity counts, the page should rank higher under the most popular
(Better known Invented productagainstLess known Invented product,H4c). Their shared drop relative to the true brand
with the same invented product (Original brand Invented product) measures the mismatch itself: the page may rank
lower because its text does not match the brand that signs it (H4d). Finally, with the same invented product, even a less
popular real brand should rank the page higher than an invented brand (Less known Invented productagainstInvented
brand,H4e).
Figure 7a shows the mean rank of the target under each signature, averaged over the four rewrites: the target ranks best
under its original brand and worst under an invented brand. Averaged over questions, models and the four rewrites
(Table 2), the target page ranks 3.21 under its true brand and 3.65 under an invented one, so the true brand gains 0.44
positions [0.23, 0.69].H4a is supported.The gain is positive for each of the four models, in each of the four sectors
(Appendix Table E.1). Keeping the true brand but inventing the product name costs the page 0.14 positions [0.05, 0.27].
H4b is supported.The rest of the gain ofH4acomes from the brand name alone: with the same invented product,
Original brand Invented productranks the page 0.30 positions aboveInvented brand[0.13, 0.51] (Appendix Table E.2).
When another real brand signs the page, with the same invented product, the page drops compared with its true brand:
by 0.06 positions under the more popular brand and by 0.11 under the less popular one.H4c is not supported. H4c
is the counterpart, at equal content, of the brand popularity bias of Study 1 (Section 4.1): among real brands that do
not own the page, the more popular one does not rank it higher. The drop the two brands share (0.08 [−0.02, 0.20]) is
the cost of a brand that does not match the page (H4d), and it is not significant after the correction; this control also
includes any recognition of the text as the original brand’s. A less popular real brand still ranks the page 0.19 positions
above an invented brand [0.11, 0.30].H4e is supported.Better known Real productandLess known Real productgive
the same picture: both brands rank the page above the invented brand (+0.27 and +0.29, significant after correction), not
significantly below its true brand, and not differently from each other (Appendix Table E.2).

The Popular Get More Popular: Auditing Brand Bias in Generative Search 13
H5: GEO rewriting increases the visibility of a page.
If GEO rewriting increases the visibility of a page, a rewritten page should rank higher than the same page with its
original text (H5a). We also compare the two interventions on the same scale: changing brand name should raise the
rank of the page more than GEO rewriting does (H5b).
Figure 7b shows the mean rank of the target with each rewrite, under every signature. Each of the three rewrites
moves the page by about 0.02 positions, and their average is +0.022 [−0.001, 0.049].H5a is not supported, and the
interval rules out gains larger than 0.05 positions. The original brand gains 0.42 positions more than rewriting [0.22,
0.66].H5b is supported.The rewrites, written by gpt-5.5, do not help more on GPT than on the other models
(difference +0.005 [−0.03, 0.04]; Appendix Table E.1).
5 Discussion
In this work, we proposed an empirical framework for provider fairness in generative search in product recommendation.
Appendix Table F.1 summarizes the outcome of each audited hypothesis.
First, regardingRQ1, we find persistentbrand popularity biasacross almost all evaluated engines and market
sectors. Generative search engines disproportionately recommend market-dominant brands, a bias already present in
their parametric memory, as shown by search-off. Crucially, enabling Retrieval-Augmented Generation (search-on)
does not mitigate this head-item favoritism. In fact, (i) popularity bias remains unchanged between search-on and
search-off conditions, and (ii) retrieval mechanisms often introduce popular brands in search queries before fetching
external pages. Consequently, external retrieval does not counteract the model’s parametric brand bias. Buyer personas
are the only factor in our audit that weakens the brand popularity bias. A plausible explanation is that a persona turns
a generic request into a constrained one: the engine has to match brands to a stated budget and profile, rather than list
the best-known options in the category. Part of this may happen through retrieval, since with search-on the persona
changes the search queries, which often add price terms, and the sources the engine retrieves.
Second, regardingRQ2, our controlled experiments demonstrate a multi-facetedbrand familiarity bias. Holding
product descriptions, specifications, and layout strictly constant, authentic real-world brands achieve significantly
higher recommendation ranks than synthetic brand controls. Our findings suggest that generative search engines may
penalize unfamiliar entities that lack pre-existing weight representations in training data, creating a steep algorithmic
barrier to entry.
Third, our experiments do not observe significant ranking gains from Generative Engine Optimization (GEO) rewrites.
While prior work suggests that authority-style marketing can overcome brand dominance [11], those manipulations
incorporated unverified or fabricated clinical claims. When GEO transformations are strictly constrained to be fact-
preserving, surface-level textual optimization appears insufficient to overcome built-in parametric brand preferences.
Taken together, these results highlight key structural socio-economic risks in generative search. By over-representing
dominant market players, generative search engines could feed a loop reminiscent of the Matthew effect (“rich-get-
richer”) [25, 30]. Because generative search engines synthesize choices into a few top recommendations rather than a
paginated list of URLs, long-tail and local competitors may face near-total erasure. At a global scale, exposing millions
of daily users to similar or even identical, mode-collapsed recommendations risks creating digital market oligopolies
and suppressing consumer choice diversity.
This systemic bias introduces a fundamental issue of market contestability. The observedbrand familiarity bias
directly mirrors the item cold-start problem in traditional recommender systems [ 40]. However, unlike traditional
systems where explicit product features can bridge the cold-start gap, generative search engines rank an unknown name

14 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
lower, as a novel entrant would have, even when complete product descriptions are provided in-context. Consequently,
newly established brands or sustainable startups may be disadvantaged simply because they were founded after model
pre-training.
Broader implications.Our experimental pipeline offers a low-cost audit that developers of generative search engines
could run before deployment, comparing the rank variations across controlled identity swaps. The design is not specific
to brands: in principle it applies to any entity whose name a model may know, such as news outlets, public bodies
or authors, and prior work already finds that the name of a source can matter more than its content [ 12, 23]. For
product vendors and marketers, our findings set boundaries on the efficacy of Generative Engine Optimization (GEO).
While marketing agencies advocate stylistic rewriting for LLM visibility, fact-preserving GEO yields marginal returns,
and a new provider may gain more from becoming known in the web sources that models learn from and retrieve.
For regulators, focusing solely on citation transparency overlooks how visibility is allocated: auditing frameworks
must therefore evaluate inline entity mentions alongside source links to safeguard market contestability and antitrust
oversight. Finally, consumers relying on generative search for product discovery may be exposed to a narrower, head-
biased subset of the market. Awareness of these built-in parametric priors may help users seeking specialized, local or
emerging alternatives.
Limitations.Our empirical findings should be contextualized within several deliberate methodological trade-offs.
First, outputs from black-box LLMs inherently fluctuate across time and geography due to continuous background
updates and localized indexing [10, 42]. To control for these intrinsic auditing dynamics, we fixed all prompts to a single
temporal snapshot and location (Italian queries from Rome), leaving cross-cultural or regional brand disparities [5]
outside our scope. Second, in Study 2, we explicitly executed experiments with live web retrieval disabled (search-off).
While this setup omits live search reranking in the wild, this choice allows us to exert total experimental control over
the in-context page, thus isolating brand bias. Third, our persona conditioning relied on three holistic multi-sentence
templates rather than an exhaustive factorial grid. While this captures only a subset of possible user profiles, the three
personas lower the brand popularity bias in the same direction, significantly for two of them. Fourth, model audits
were conducted through vendor API endpoints. While APIs provide reproducible, programmatic access, they may omit
proprietary, client-side system prompts or interface heuristics present in consumer-facing chat interfaces. Fifth, our
GEO rewrites strictly operationalized established optimization strategies [1] under an explicit fact-preserving constraint.
We deliberately excluded deceptive or fabricated claims (e.g., fake statistics) to reflect legitimate on-page optimization,
leaving whether adversarial copy can bypass parametric priors to future work. Sixth, our evaluation focuses exclusively
on generative search, precluding a direct empirical baseline against traditional search engines. Finally, we quantified
brand visibility via mention and citation frequencies without performing sentiment analysis. While negative portrayals
are theoretically plausible, manual inspection of the generated outputs revealed no instances of unfavorable brand
mentions or citations; recommendations were uniformly positive or neutral.
Future Work.Future research should extend this audit methodology along three main avenues. First, conducting
relevance-conditional auditswould compare generated brand recommendations against an independent, ground-truth
inventory of market offers matched for price and specification. Second, testing real-world brand entities founded strictly
after the model’s training cutoff date under search-on conditions would provide a sharper delineation between real-
world brand emergence and synthetic entity penalties. Finally, expanding this framework to open-weight architectures
and multi-agent retrieval pipelines could pinpoint the exact layer dynamics where parametric brand priors override
retrieved in-context specifications.

The Popular Get More Popular: Auditing Brand Bias in Generative Search 15
Endmatter
Ethical considerations and adverse impacts
The studies query deployed commercial systems through their official APIs and involve no human participants and
no personal data. Source pages were read after the calls, to check whether the names of mentioned brands appear in
them (Study 1) and to build the product pages of Study 2. Each page was first requested with a declared user agent;
pages that blocked this request were retrieved through a commercial unblocking service (Bright Data Web Unlocker)
or from Internet Archive snapshots, and the few still unreadable were saved manually. Invented brand names were
checked to have no existing or registered web domain. Showing what moves a page in a generated ranking has a dual
use: it can inform providers and regulators, and it can guide manipulation; rewriting moves pages very little, but the
identity result suggests that signing a page with a known brand works, which is impersonation and is not something
we recommend or tested in the wild.
Generative AI usage statement
The language models studied are the objects of the audit and of the experiment (Section 3).gemini-2.5-flash extracted
brand names from the answers; gpt-5.5 extracted the text of the Study 2 pages (gemini-3.6-flash for one non-target
page that gpt-5.5 did not process) and wrote the rewrites, and deepseek-v3.2 checked them for added or removed
facts; LLMs also classified prompts and candidate brands during selection, with fixed instructions. We used Claude
(Anthropic) as a coding assistant for the analysis scripts, and as a writing assistant for drafting and editing parts of the
text. The authors designed the studies, checked the results against the data, and reviewed and take responsibility for all
code and text.
Data and code availability
Code, prompts, product pages, and aggregated data are available at https://anonymous.4open.science/r/brand-bias-
generative-search-3E74.
References
[1] Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, and Ameet Deshpande. 2024. GEO: Generative
Engine Optimization. InProceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD).
[2] Lena Armstrong, Abbey Liu, Stephen MacNeil, and Danaë Metaxa. 2024. The Silicon Ceiling: Auditing GPT’s Race and Gender Biases in Hiring. In
Proceedings of the 4th ACM Conference on Equity and Access in Algorithms, Mechanisms, and Optimization (EAAMO). doi:10.1145/3689904.3694699
[3] Yoav Benjamini and Yosef Hochberg. 1995. Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing.Journal of
the Royal Statistical Society: Series B (Methodological)57, 1 (1995), 289–300.
[4] Marianne Bertrand and Sendhil Mullainathan. 2004. Are Emily and Greg More Employable than Lakisha and Jamal? A Field Experiment on Labor
Market Discrimination.American Economic Review94, 4 (2004), 991–1013.
[5] Filippo Betello, Paul Missault, Tamara Czinczoll, and Maryna Beliuha. 2026. Your LLM Has a Passport: Investigating Brand Origin Geographic Bias
in E-Commerce Rankings. InThe 2026 ACM Conference on Fairness, Accountability, and Transparency. 8089–8106.
[6] Asia J. Biega, Krishna P. Gummadi, and Gerhard Weikum. 2018. Equity of Attention: Amortizing Individual Fairness in Rankings. InProceedings of
the 41st International ACM SIGIR Conference on Research and Development in Information Retrieval.
[7] Robin Burke. 2017. Multisided Fairness for Recommendation. arXiv preprint arXiv:1707.00093. arXiv:1707.00093
[8] Jianlv Chen, Shitao Xiao, Peitian Zhang, Kun Luo, Defu Lian, and Zheng Liu. 2024. M3-Embedding: Multi-Linguality, Multi-Functionality,
Multi-Granularity Text Embeddings Through Self-Knowledge Distillation. InFindings of the Association for Computational Linguistics: ACL 2024.
[9] Lihu Chen, Alexandre Perez-Lebel, Fabian Suchanek, and Gaël Varoquaux. 2024. Reconfidencing llms from the grouping loss perspective. InFindings
of the Association for Computational Linguistics: EMNLP 2024. 1567–1581.
[10] M. Chen and N. Koudas. 2026. What Drives AI Citations? Content, Retrieval and Model Knowledge in Generative Engine Optimization (GEO).
arXiv:2610.15033. arXiv:2610.15033

16 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
[11] Xi Chu and Yupeng Hou. 2026. Incumbent Advantage: Brand Bias and Cognitive Manipulation Dynamics in LLM Recommendation Systems. arXiv
preprint arXiv:2606.17443. arXiv:2606.17443
[12] Sunhao Dai, Zhanshuo Cao, Wenjie Wang, Liang Pang, Jun Xu, See-Kiong Ng, and Tat-Seng Chua. 2025. Media Source Matters More Than Content:
Unveiling Political Bias in LLM-Generated Citations. InProceedings of the 2025 Conference on Empirical Methods in Natural Language Processing
(EMNLP). https://aclanthology.org/2025.emnlp-main.872/
[13] Yashar Deldjoo, Dietmar Jannach, Alejandro Bellogin, Alessandro Difonzo, and Dario Zanzonelli. 2024. Fairness in recommender systems: research
landscape and future directions: Y. Deldjoo et al.User Modeling and User-Adapted Interaction34, 1 (2024), 59–108.
[14] Karlijn Dinnissen and Christine Bauer. 2023. Amplifying artists’ voices: Item provider perspectives on influence and fairness of music streaming
platforms. InProceedings of the 31st ACM conference on user modeling, adaptation and personalization. 238–249.
[15] Xiaoyu Dong, Quanyu Dai, Nuo Chen, Qijiong Liu, Yue Zixuan, Xuyang Xie, Jieming Zhu, Zhenhua Dong, and Xiao-Ming Wu. 2026. Knowledge
Bias in LLM-based Sequential Recommendation: Source, Persistence, and Mitigation. InFindings of the Association for Computational Linguistics:
EMNLP 2026. 6858–6873.
[16] Giorgos Filandrianos, Angeliki Dimitriou, Maria Lymperaiou, Konstantinos Thomas, and Giorgos Stamou. 2025. Bias beware: The impact of
cognitive biases on LLM-driven product recommendations. InProceedings of the 2025 Conference on Empirical Methods in Natural Language Processing.
22408–22437.
[17] S. Michael Gaddis. 2017. How Black Are Lakisha and Jamal? Racial Perceptions from Names Used in Correspondence Audit Studies.Sociological
Science4 (2017), 469–489. doi:10.15195/v4.a19
[18] Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi Zhang, and Nesreen K.
Ahmed. 2024. Bias and Fairness in Large Language Models: A Survey.Computational Linguistics50, 3 (2024), 1097–1179. doi:10.1162/coli_a_00524
[19] Sture Holm. 1979. A Simple Sequentially Rejective Multiple Test Procedure.Scandinavian Journal of Statistics6, 2 (1979), 65–70. https:
//www.jstor.org/stable/4615733
[20] Lucas D. Introna and Helen Nissenbaum. 2000. Shaping the Web: Why the Politics of Search Engines Matters.The Information Society16, 3 (2000),
169–185.
[21] Will Jack, Noah Lehman, Keller Maloney, and Sarah Xu. 2026. Persona Conditioning of Brand Recommendations in Retrieval-Augmented Commercial
Chat: A Prominence-Stratified Cross-Provider Audit. arXiv preprint arXiv:2605.30207. arXiv:2605.30207
[22] Mahammed Kamruzzaman, Hieu Minh Nguyen, and Gene Louis Kim. 2024. “Global is Good, Local is Bad?”: Understanding Brand Bias in LLMs. In
Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP). arXiv:2406.13997
[23] Mohammad Aflah Khan, Mahsa Amani, Soumi Das, Bishwamittra Ghosh, Qinyuan Wu, Krishna P. Gummadi, Manish Gupta, and Abhilasha
Ravichander. 2026. In Agents We Trust, but Who Do Agents Trust? Latent Source Preferences Steer LLM Generations. InInternational Conference
on Learning Representations (ICLR). arXiv:2602.15456
[24] Elisabeth Kirsten, Jost Grosse Perdekamp, Qinyuan Wu, Mihir Upadhyay, Krishna P Gummadi, and Muhammad Bilal Zafar. 2026. Characterizing
web search in the age of generative ai. InFindings of the Association for Computational Linguistics: ACL 2026. 10827–10848.
[25] Anastasiia Klimashevskaia, Dietmar Jannach, Mehdi Elahi, and Christoph Trattner. 2024. A Survey on Popularity Bias in Recommender Systems.
User Modeling and User-Adapted Interaction34 (2024), 1777–1834. doi:10.1007/s11257-024-09406-0
[26] Kritee Kondapally, Claire J. Smerdon, Pooja C. Patel, Ogheneyoma Akoni, Jevon Torres, Jaspreet Ranjit, Matthew Finlayson, and Swabha Swayamdipta.
2026. Side-by-side Comparison Amplifies Dialect Bias in Language Models. InProceedings of the 2026 ACM Conference on Fairness, Accountability,
and Transparency (FAccT). doi:10.1145/3805689.3812217
[27] Aounon Kumar and Himabindu Lakkaraju. 2024. Manipulating Large Language Models to Increase Product Visibility. arXiv preprint arXiv:2404.07981.
arXiv:2404.07981
[28] Nelson F. Liu, Tianyi Zhang, and Percy Liang. 2023. Evaluating Verifiability in Generative Search Engines. InFindings of the Association for
Computational Linguistics: EMNLP 2023. https://aclanthology.org/2023.findings-emnlp.467/
[29] Song-Duo Ma, Chu-Yun Chen, Bang-An Li, Pin-Yu Chen, Shau-Yung Hsu, and Yun-Nung Chen. 2026. Rethinking Fairness in LLM-Based Recommender
Systems: A Survey. (2026).
[30] Masoud Mansoury, Himan Abdollahpouri, Mykola Pechenizkiy, Bamshad Mobasher, and Robin Burke. 2020. Feedback Loop and Bias Amplification
in Recommender Systems. InProceedings of the 29th ACM International Conference on Information and Knowledge Management (CIKM). 2145–2148.
doi:10.1145/3340531.3412152
[31] Robert K. Merton. 1968. The Matthew Effect in Science.Science159, 3810 (1968), 56–63.
[32] Danaë Metaxa, Joon Sung Park, Ronald E. Robertson, Karrie Karahalios, Christo Wilson, Jeff Hancock, and Christian Sandvig. 2021. Auditing
Algorithms: Understanding Algorithmic Systems from the Outside In.Foundations and Trends in Human–Computer Interaction14, 4 (2021).
[33] Pranav Narayanan Venkit, Philippe Laban, Yilun Zhou, Yixin Mao, and Chien-Sheng Wu. 2025. Search Engines in the AI Era: A Qualitative
Understanding to the False Promise of Factual and Verifiable Source-Cited Responses in LLM-based Search. InProceedings of the 2025 ACM Conference
on Fairness, Accountability, and Transparency(Athens, Greece)(FAccT ’25). Association for Computing Machinery, New York, NY, USA, 1325–1340.
doi:10.1145/3715275.3732089
[34] Fredrik Nestaas, Edoardo Debenedetti, and Florian Tramèr. 2025. Adversarial Search Engine Optimization for Large Language Models. InInternational
Conference on Learning Representations (ICLR).

The Popular Get More Popular: Auditing Brand Bias in Generative Search 17
[35] Samuel Pfrommer, Yatong Bai, Tanmay Gautam, and Somayeh Sojoudi. 2024. Ranking Manipulation for Conversational Search Engines. In
Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP).
[36] Haritz Puerto, Martin Gubri, Tommaso Green, Seong Joon Oh, and Sangdoo Yun. 2025. C-SEO Bench: Does Conversational SEO Work?. InAdvances
in Neural Information Processing Systems (NeurIPS), Datasets and Benchmarks Track.
[37] Zacchary Sadeddine, Winston Maxwell, Gaël Varoquaux, and Fabian M Suchanek. 2025. Large Language Models as Search Engines: Societal
Challenges. InACM SIGIR Forum, Vol. 59. ACM, New York, NY, USA, 1–35.
[38] Alejandro Salinas, Amit Haim, and Julian Nyarko. 2024. What’s in a Name? Auditing Large Language Models for Race and Gender Bias.
arXiv:2402.14875
[39] Christian Sandvig, Kevin Hamilton, Karrie Karahalios, and Cedric Langbort. 2014. Auditing Algorithms: Research Methods for Detecting Discrimi-
nation on Internet Platforms. InData and Discrimination: Converting Critical Concerns into Productive Inquiry, Preconference of the 64th Annual
Meeting of the International Communication Association.
[40] Andrew I. Schein, Alexandrin Popescul, Lyle H. Ungar, and David M. Pennock. 2002. Methods and Metrics for Cold-Start Recommendations. In
Proceedings of the 25th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval. 253–260. doi:10.1145/
564376.564421
[41] Johannes A. Schubert, Akshay K. Jagadish, Marcel Binz, and Eric Schulz. 2024. In-context learning agents are asymmetric belief updaters. In
Proceedings of the 41st International Conference on Machine Learning.
[42] Schulte, Bleeker, and Kaufmann. 2026. Don’t Measure Once: Measuring Visibility in AI Search. arXiv:2604.07585.
[43] Ashudeep Singh and Thorsten Joachims. 2018. Fairness of Exposure in Rankings. InProceedings of the 24th ACM SIGKDD International Conference
on Knowledge Discovery and Data Mining (KDD).
[44] Sofia Eleni Spatharioti, David Rothschild, Daniel G. Goldstein, and Jake M. Hofman. 2025. Effects of LLM-based Search on Decision Making: Speed,
Accuracy, and Overreliance. InProceedings of the 2025 CHI Conference on Human Factors in Computing Systems. doi:10.1145/3706598.3714082
[45] Yifan Wang, Weizhi Ma, Min Zhang, Yiqun Liu, and Shaoping Ma. 2023. A Survey on the Fairness of Recommender Systems.ACM Transactions on
Information Systems41, 3 (2023). doi:10.1145/3547333
[46] Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng, Alexander J Ratner, Ranjay Krishna, Jiaming Shen, and Chao Zhang. 2023. Large language model as
attributed training data generator: A tale of diversity and bias.Advances in neural information processing systems36 (2023), 55734–55784.
[47] Jiayi Zhang, Simon Yu, Derek Chong, Anthony Sicilia, Michael R. Tomz, Christopher D. Manning, and Weiyan Shi. 2025. Verbalized Sampling: How
to Mitigate Mode Collapse and Unlock LLM Diversity. arXiv:2510.01171
A Study 1: prompts and personas
Table A.1. The 80 prompts of Study 1, with the keyword they were derived from and its mean monthly search volume in Italy over
twelve months (DataForSEO).
ID Prompt Keyword Volume
assicurazioni_01Quale assicurazione RC moto scegliere?assicurazione rc moto 133
assicurazioni_02 Quale assicurazione annullamento viaggio mi conviene scegliere in base a cosa copre? assicurazione annullamento viaggio cosa
copre
102
assicurazioni_03Quale assicurazione bici dovrei scegliere?assicurazione bici 695
assicurazioni_04Qual è la migliore assicurazione casa con responsabilità civile da scegliere?assicurazione casa responsabilità civile 249
assicurazioni_05Quale polizza famiglia mi consigliate?polizza famiglia 104
assicurazioni_06Qual è la migliore assicurazione kasko da scegliere?migliore assicurazione kasko 118
assicurazioni_07Qual è la migliore assicurazione mutuo da scegliere?assicurazione mutuo 857
assicurazioni_08Qual è la migliore assicurazione mensile per moto che potrei scegliere?assicurazione mensile per moto 1,972
assicurazioni_09Quale assicurazione sui voli mi consigli di scegliere?assicurazione sui voli 702
assicurazioni_10Qual è la migliore assicurazione natante da scegliere?assicurazione natante 308
assicurazioni_11Quali sono le migliori opzioni di assicurazione per la famiglia?assicurazione per la famiglia 540
assicurazioni_12Quali sono i migliori preventivi di assicurazioni online?preventivi assicurazioni on line 470
assicurazioni_13Qual è l’assicurazione auto migliore da scegliere?assicurare auto 182
assicurazioni_14Qual è la migliore polizza sul mutuo da scegliere?polizza sul mutuo 158
assicurazioni_15Qual è la migliore polizza cristalli senza RCA da scegliere?polizza cristalli senza rca 226
assicurazioni_16Quale assicurazione è la migliore per i medici specializzandi?assicurazione medici specializzandi 119
assicurazioni_17Qual è l’assicurazione RCA migliore da scegliere?assicurazione rca 3,442
assicurazioni_18Quali sono le migliori opzioni di assicurazione personale infortuni da scegliere?assicurazione personale infortuni 291
assicurazioni_19Quale assicurazione spese veterinarie dovrei scegliere?assicurazione spese veterinarie 438
assicurazioni_20Quali sono le migliori opzioni per l’assicurazione vita in base ai costi?costi assicurazione vita 812
viaggi_01Quale crociera nel Mediterraneo mi consigli di scegliere in base al prezzo?prezzo crociera mediterraneo 787
viaggi_02Quali sono le migliori crociere a poco prezzo?crociere a poco prezzo 134

18 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
ID Prompt Keyword Volume
viaggi_03Quali sono i migliori villaggi last minute nel Salento?villaggi salento last minute 143
viaggi_04Quali villaggi scegliere per le vacanze in Cilento?vacanze in cilento villaggi 305
viaggi_05Quali sono i migliori villaggi sul mare nel Conero da scegliere?villaggi conero sul mare 585
viaggi_06Quali sono i migliori villaggi turistici sul mare nel Gargano?villaggi turistici gargano sul mare 121
viaggi_07Quale villaggio turistico all inclusive mi consiglieresti?villaggio turistico all inclusive 340
viaggi_08Quali sono i migliori villaggi turistici all inclusive in Riviera Romagnola? villaggi turistici riviera romagnola all inclu-
sive
157
viaggi_09Quali sono le migliori offerte di noleggio disponibili?offerte noleggio 318
viaggi_10Quali sono i migliori tour operator per viaggi di gruppo organizzati? tour operator viaggi di gruppo organizzati 162
viaggi_11Quali sono le migliori offerte auto a noleggio tra cui scegliere?offerte auto a noleggio 106
viaggi_12Quali sono le migliori crociere con offerte scontatissime?crociere scontatissime 306
viaggi_13Quali sono i migliori villaggi all inclusive alle Maldive del Salento?maldive del salento villaggi all inclusive 222
viaggi_14Quali sono le migliori offerte per le crociere?offerte crociere 8,125
viaggi_15Quali sono i migliori tour operator per un viaggio a Zanzibar?tour operator zanzibar 378
viaggi_16Quali sono le migliori offerte per crociere di Capodanno?offerte crociere capodanno 200
viaggi_17Quali sono le migliori opzioni per il noleggio auto con prezzi bassi?noleggio auto prezzi bassi 191
viaggi_18Quali sono i migliori tour operator siciliani da scegliere per un viaggio?tour operator siciliani 439
viaggi_19Quali sono i migliori voli disponibili, considerando i prezzi?prezzi voli 1,003
viaggi_20Quali sono le migliori compagnie crociere italiane tra cui scegliere?compagnie crociere italiane 162
moda_beauty_01Quali sono le migliori scarpe eleganti comode con tacco medio da scegliere?scarpe eleganti comode con tacco medio 133
moda_beauty_02Qual è il contorno occhi antirughe migliore da scegliere?contorno occhi antirughe migliore 271
moda_beauty_03Quali profumi originali con prezzi bassissimi dovrei scegliere?profumi originali a prezzi bassissimi 778
moda_beauty_04Quale abbigliamento on line mi consigliate di acquistare?abbigliamento on line 1,567
moda_beauty_05Qual è il miglior siero antimacchie da scegliere?miglior siero antimacchie 527
moda_beauty_06Quali sono i migliori giubbotti in pelle da uomo che potrei scegliere?i migliori giubbotti in pelle uomo 392
moda_beauty_08Quali sono i migliori jeans momfit da scegliere?momfit 464
moda_beauty_09Quali vestiti di marca a poco prezzo dovrei scegliere?vestiti di marca a poco prezzo 241
moda_beauty_10Quale top verde elegante dovrei scegliere?top verde elegante 118
moda_beauty_11Quali maschere viso naturali dovrei scegliere?maschere viso naturali 364
moda_beauty_12Quali sono le migliori offerte di abbigliamento per uomo da scegliere?offerte abbigliamento uomo 542
moda_beauty_13Qual è la migliore maschera viso al collagene da scegliere?maschera viso collagene migliore 332
moda_beauty_14Qual è la migliore crema contorno occhi da scegliere?crema contorno occhi migliore 2,342
moda_beauty_15Quali sono le migliori borse in offerta o con sconti da scegliere?borse scontate 1,170
moda_beauty_16Quali sono le migliori pochette di marca da outlet tra cui scegliere?pochette firmate outlet 427
moda_beauty_18Qual è il retinolo migliore?retinolo migliore 892
moda_beauty_19Quali sono i migliori fondotinta da scegliere?migliori fondotinta 355
moda_beauty_21Quali sono i migliori jeans push up da scegliere?jeans push up migliori 152
moda_beauty_22Quali sono i migliori giubbotti invernali da uomo tra cui scegliere?migliori giubbotti invernali uomo 366
moda_beauty_23Quali sono i profumi buoni da uomo che mi consiglieresti?profumi buoni uomo 690
sport_01Quali sono le migliori scarpe da trekking da scegliere?le migliori scarpe da trekking 200
sport_02Quale offerta di bici elettrica dovrei scegliere?offerta bici elettrica 636
sport_03 Quali sono le differenze tra un tapis roulant elettrico e uno magnetico, e quale mi
conviene scegliere?
differenze tra tapis roulant elettrico e mag-
netico
128
sport_04Quali sono le migliori scarpe da corsa su strada che dovrei scegliere?migliori scarpe da corsa su strada 103
sport_05Quali sono le migliori scarpe da trail running per uomo?scarpe trail running uomo migliori 209
sport_06Quali sono le migliori e-bike in base al costo?prezzi e bike 161
sport_07Quali sono i migliori tapis roulant per casa da scegliere?tapis roulant migliori per casa 178
sport_08Qual è la migliore scarpa running da scegliere?migliore scarpa running 172
sport_09Qual è la migliore ebike per rapporto qualità prezzo?migliore ebike qualità prezzo 218
sport_10Quale tapis roulant dovrei scegliere in base al prezzo?prezzo tapis roulant 217
sport_11Quali sono i migliori tapis roulant da scegliere?tapis roulant i migliori 605
sport_12Quali e-bike con offerte mi consiglieresti?e bike offerte 346
sport_13Qual è la racchetta da padel migliore da scegliere?racchetta padel migliore 157
sport_14Quale mountain bike da 24 pollici in offerta dovrei scegliere?mtb 24 pollici offerta 132
sport_15Quale racchetta da tennis scegliere in base al prezzo?racchetta da tennis prezzi 228
sport_16Quali sono i migliori outfit per la palestra tra cui scegliere?outfit palestra 469
sport_17Quali sono le migliori cargo bike economiche da scegliere?cargo bike economiche 288
sport_20Qual è la racchetta da tennis migliore da scegliere?racchetta tennis migliore 608
sport_21Quali sono le migliori scarpe da corsa da scegliere?migliori scarpe da corsa 630
sport_22Quali sono le migliori scarpe da calcio a poco prezzo?scarpe calcio poco prezzo 160

The Popular Get More Popular: Auditing Brand Bias in Generative Search 19
Table A.2. The twelve buyer personas of Study 1, placed before the question in Italian; English translation below each.
Sector Persona Text
InsuranceBaseline persona (A)Sono genitore con una famiglia a carico. È la prima volta che stipulo una polizza. Cerco di spendere il meno possibile.
I am a parent with a family to support. It is the first time I take out a policy. I try to spend as little as possible.
InsurancePrice variant (B)Sono genitore con una famiglia a carico. È la prima volta che stipulo una polizza. Spendo volentieri di più per la qualità.
I am a parent with a family to support. It is the first time I take out a policy. I am happy to spend more for quality.
InsuranceProfile variant (C)Sono al primo anno di patente. È la prima volta che stipulo una polizza. Cerco di spendere il meno possibile.
I am in my first year with a driving licence. It is the first time I take out a policy. I try to spend as little as possible.
TravelBaseline persona (A)Sono single e viaggio senza figli. Ho un’esperienza nella media con i viaggi. Cerco di spendere il meno possibile.
I am single and travel without children. I have average experience with travel. I try to spend as little as possible.
TravelPrice variant (B)Sono single e viaggio senza figli. Ho un’esperienza nella media con i viaggi. Cerco il miglior rapporto tra qualità e prezzo.
I am single and travel without children. I have average experience with travel. I look for the best value for money.
TravelProfile variant (C)Sono genitore di figli piccoli. Ho un’esperienza nella media con i viaggi. Cerco di spendere il meno possibile.
I am a parent of young children. I have average experience with travel. I try to spend as little as possible.
Fashion&BeautyBaseline persona (A)Sono genitore di figli piccoli. Ho un’esperienza nella media con moda e cosmetici. Cerco di spendere il meno possibile.
I am a parent of young children. I have average experience with fashion and cosmetics. I try to spend as little as possible.
Fashion&BeautyPrice variant (B)Sono genitore di figli piccoli. Ho un’esperienza nella media con moda e cosmetici. Cerco il miglior rapporto tra qualità e prezzo.
I am a parent of young children. I have average experience with fashion and cosmetics. I look for the best value for money.
Fashion&BeautyProfile variant (C)Sono single e non ho figli. Ho un’esperienza nella media con moda e cosmetici. Cerco di spendere il meno possibile.
I am single and have no children. I have average experience with fashion and cosmetics. I try to spend as little as possible.
Sport Baseline persona (A)Sono genitore di figli piccoli. Ho cominciato da poco a fare sport. Cerco di spendere il meno possibile.
I am a parent of young children. I started doing sport only recently. I try to spend as little as possible.
Sport Price variant (B)Sono genitore di figli piccoli. Ho cominciato da poco a fare sport. Cerco il miglior rapporto tra qualità e prezzo.
I am a parent of young children. I started doing sport only recently. I look for the best value for money.
Sport Profile variant (C)Sono genitore di figli piccoli. Faccio sport a un livello intermedio. Cerco di spendere il meno possibile.
I am a parent of young children. I do sport at an intermediate level. I try to spend as little as possible.
B Data collection
All calls go through the official APIs, with no system prompt and the provider’s default parameters; in Study 1 the user
location is Rome, Italy.
All Study 1 calls were made on 14 October 2026 (UTC). In Study 2, the rankings were collected between 28 October
and 3 November 2026, and the calibration run and the brand ratings between 23 and 25 October. The brand extractor
(gemini-2.5-flash) was checked by hand on 30 answers from a pilot run: 151 of the 157 extracted names were correct
brands (96%), and it missed 2 of the 153 brands in those answers (1%). In the source check, a page counts as readable if it
is not an anti-bot check and its extracted text has at least 1,000 characters, which excludes pages whose content did not
load. Every answer stores the model version returned by the API and, in Study 1, the search queries, the sources and
the text. Prompts, personas, pages, message templates and instructions were fixed before the calls, and their hashes are
stored with the answers.
C Study 1: additional results
C.1 Brand popularity bias in mention and citation (H1)
By engine and sector, the slopes of mention on popularity with search off and on differ in 4 of the 12 pairs after
Benjamini–Hochberg (Table C.2, Figure C.1). With search on, the slope is steeper for insurance on GPT (+0.81) and on
Perplexity (+0.91), which with search off almost never mentions an insurer, and flatter for sport on Perplexity (−0.34)
and for travel on GPT (−0.16). On Gemini, the calls that actually searched show a flatter slope than the calls with
search off (0.95 against 1.34; difference−0.38, 𝑝< 0.001, OLS with errors clustered by brand), in all four sectors. Gemini
chooses which calls search, so this comparison is not controlled.
Figure C.3 shows the rates of Figure 3 before normalisation. GPT mentions a brand about twice as often as it cites it,
Gemini mentions brands often and cites them rarely, and on Perplexity, whose sources are the retrieved results, the
citation rate can exceed the mention rate. A mentioned brand with a known domain is cited in 32–64% of the answers
that searched on GPT, 15–80% on Perplexity and 3–28% on Gemini, depending on the sector. Because the levels differ,

20 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
the raw slopes of mention and citation on popularity are not directly comparable; Table C.3 compares the slopes of the
normalised rates. On GPT the two normalised slopes are the same (0.52 and 0.51), so the steeper raw slope of mention
comes from its higher level. On Gemini popularity counts more for mention than for citation (difference +0.38 [0.18,
0.58]). On Perplexity it counts more for citation (−0.26 [−0.44,−0.10]).
Table C.1. Study 1: popularity bias under different sets of brands. Slopes as in Table C.2, all engines and sectors together. Main
analysis: one set of brands per sector, made of the brands that at least one engine mentions in 5 or more of its 1,600 answers in
that sector, with zeros for the engines that do not name them. Alternatives: a separate set for each engine (brands that this engine
mentions at least 5 times), and a threshold of 10. A threshold below 5 is not possible, because popularity was measured only for the
brands above it.
Set of brands Brand rows Search off Search on Difference 95% interval
Per sector,≥5(main) 3,567 +0.87 +0.89 +0.02[−0.03,0.07]
Per engine,≥52,101 +1.34 +1.35 +0.01[−0.07,0.10]
Per sector,≥102,463 +1.05 +1.08 +0.03[−0.04,0.11]
Per engine,≥101,450 +1.61 +1.62 +0.01[−0.11,0.12]
Table C.2. Study 1: how many percentage points the mention rate of a brand rises for each tenfold increase in its search volume, with
search off and with search on. Each slope is an OLS fit with one point per brand; the difference between the two slopes is also the slope
of the per-brand effect of search (Figure C.4). Rows for all sectors and for all engines add engine× sector fixed effects. 95% intervals
from resampling brands within each engine and sector; 𝑝 from a 𝑡 test with robust (HC3) errors, corrected with Benjamini–Hochberg
over the 12 engine–sector rows (summary rows uncorrected).
Search off Search on Difference 95% interval𝑝
GPT
Insurance +0.71 +1.52 +0.81[0.27,1.49]0.031
Fashion and beauty +1.09 +0.91−0.18[−0.36,0.00]0.103
Sport +1.41 +1.10−0.30[−0.61,0.03]0.103
Travel +0.70 +0.54−0.16[−0.28,−0.05]0.031
All sectors+0.94 +0.86−0.07[−0.19,0.03]0.205
Gemini
Insurance +2.95 +3.25 +0.30[0.03,0.62]0.103
Fashion and beauty +1.11 +1.08−0.03[−0.13,0.06]0.617
Sport +1.38 +1.38 +0.01[−0.14,0.16]0.953
Travel +1.04 +1.06 +0.02[−0.04,0.08]0.609
All sectors+1.34 +1.37 +0.04[−0.02,0.10]0.235
Perplexity
Insurance +0.06 +0.97 +0.91[0.41,1.50]0.019
Fashion and beauty +0.39 +0.40 +0.01[−0.13,0.16]0.936
Sport +0.79 +0.45−0.34[−0.61,−0.10]0.031
Travel +0.21 +0.31 +0.09[−0.01,0.23]0.222
All sectors+0.34 +0.43 +0.10[0.00,0.20]0.066
All engines and sectors+0.87 +0.89 +0.02[−0.03,0.07]0.484
C.2 Where the mentioned brands come from (H2)
Brand names in the search queries could make two answers that mention the same brands look similar in their search
queries for that reason alone. We therefore remove from each search query the names of the brands mentioned for its

The Popular Get More Popular: Auditing Brand Bias in Generative Search 21
Table C.3. Study 1: slope of the normalised mention and citation rates on popularity, search on. Each rate is divided by its mean in
the engine and sector, so a slope of 0.5 means that a brand searched ten times more often has a rate higher by half the average of its
engine and sector. OLS with engine× sector fixed effects; 95% intervals from 2,000 resamples of brands within each engine and sector.
Brands Mention Citation Difference 95% interval
GPT 702 +0.52 +0.51 +0.02[−0.08,0.11]
Gemini 702 +0.56 +0.18 +0.38[0.18,0.58]
Perplexity 702 +0.57 +0.83−0.26[−0.44,−0.10]
All engines 2,106 +0.55 +0.50 +0.04[−0.05,0.14]
0
2
4
6
8
GPT
mention (%)
Δslope +0.81**
Insurance
0
2
4
6
 Δslope -0.18
Fashion & beauty
0
2
4
6
Δslope -0.30
Sport
0
2
4
 Δslope -0.16**
Travel
0
5
10
15
Gemini
mention (%)
Δslope +0.30
0
2
4
6
 Δslope -0.03
0
2
4
6
Δslope +0.01
0
2
4
6
 Δslope +0.02
1 5
0
2
4
Perplexity
mention (%)
Δslope +0.91**
1 5
0
1
2
 Δslope +0.01
1 5
0
2
4
 Δslope -0.34**
1 5
0.0
0.5
1.0
1.5
 Δslope +0.09
popularity quintile within engine and sector
search off search on
Fig. C.1. Mention rate by quintile of popularity with search off (grey) and on (green), by engine and sector; 95% intervals from
1,000 prompt bootstrap samples, stratified by sector. Δslope: difference between the two slopes of Table C.2; ∗∗ significant after
Benjamini–Hochberg over the 12 engine–sector pairs,∗ 𝑝< 0.05before correction. With search off, Perplexity almost never mentions
an insurer.
sector and recompute query similarity. The slopes of Figure 4 remain positive: for sources 3.68 [3.27, 4.07] on GPT, 3.13
[2.76, 3.57] on Gemini and 4.24 [3.86, 4.68] on Perplexity (4.10, 3.42 and 4.59 with the original search queries), and for
brands 3.05 [2.59, 3.52], 2.09 [1.69, 2.56] and 3.25 [2.64, 3.92] (3.57, 2.09 and 3.76).

22 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
0
10
20
GPT
share of answers (%)
ρ 0.22*
ρ 0.26*
Insurance
0
5
10
15 ρ 0.38* ρ 0.26*
Fashion & beauty
0
5
10
15
ρ 0.32*
ρ 0.19
Sport
0
2
4
6
8
ρ 0.26*
ρ -0.06
Travel
0
20
40
Gemini
share of answers (%)
ρ 0.37*
ρ 0.25*
0
5
10
15
ρ 0.30*
ρ 0.14*
0
5
10
15
ρ 0.38*
ρ -0.08
0
5
10
ρ 0.47*
ρ -0.06
2 4 6
popularity
0
20
40
Perplexity
share of answers (%)
ρ 0.35*
ρ 0.41*
2 4 6
popularity
0
5
10
ρ 0.30*
ρ 0.31*
2 4 6
popularity
0
5
10 ρ 0.18*
ρ 0.35*
2 4 6
popularity
0
2
4
6
ρ 0.14*
ρ 0.13*
mention citation
Fig. C.2. Mention and citation against popularity, one panel per engine and sector, search on. Points: brands (mention: all brands
with a popularity value; citation: brands with a known domain). Lines: logistic fit of the share of answers on popularity, with 95%
band (quasi-binomial standard errors). In each panel, Spearman’s 𝜌;∗ unadjusted 𝑝< 0.05for Spearman’s correlation, not for the
fitted curve. Popularity is log10(1+𝑣) , where 𝑣 is monthly Google search volume in Italy. The horizontal axis is shared across engines
within each sector. The vertical limit is based on the 99.3rd percentile of the observed rates; the fits use all brands.
Between 34% and 39% of the brands GPT mentions appear only in its search actions after the first, which can react
to what was found (Figure 5). The source check covers 30,006 mentions in calls with observed search queries. In
36.2% of them the name of the brand is found only on third-party pages (GPT 29.1%, Gemini 42.9%, Perplexity 42.6%).
Mentions with no match do not become more frequent with popularity: the Spearman correlation is significant in
3 of the 8 engine–sector pairs of Gemini and Perplexity before correction, with opposite signs, and in none after
Benjamini–Hochberg. On Gemini, 39.7% of the mentions with no match concern brands in the most popular quintile
and 14.0% in the least popular, against 40.2% and 6.8% of the mentions whose name is found (Figure C.5). A match
does not show that the source caused the mention, and no match does not show that the mention came from memory,
because we see only the sources the platform returns and we read the pages after the calls.

The Popular Get More Popular: Auditing Brand Bias in Generative Search 23
least
popular
most
popular
0
2
4
6share of answers (%)
a GPT
least
popular
most
popular
b Gemini
least
popular
most
popular
c Perplexity
mention citation
Fig. C.3. Mention and citation by quintile of popularity in absolute terms, search on, for brands with a known domain. Quintiles are
formed within each engine and sector. Points are the mean share of answers that mention the brand (green) or cite it (orange), pooled
over the four sectors, with 95% intervals from 1,000 prompt bootstrap samples, stratified by sector. On Perplexity the sources are the
retrieved results, so its citation share can exceed its mention share.
−2 0 2
popularity (log10, centred)
−5
0
5
effect of search (pp)
slope +0.02 [-0.03; +0.07]
Fig. C.4. Effect of search-on on each brand (percentage points) against popularity (log10, centred within engine and sector), one
point per brand and engine, with OLS line and 95% bootstrap band over brands. 34 of 3,567 points fall outside the vertical range
shown.
C.3 Personas and the brand popularity bias (H3)
Without a persona context, a brand searched ten times more often on Google is mentioned in 0.98 more answers out of
100. The differences from this slope are−0.18 [−0.29,−0.07] with the Baseline persona (A),−0.13 [−0.24,−0.03] with
the Price variant (B) and−0.10 [−0.21, 0.01] with the Profile variant (C). Figure C.6 compares the three personas with
no persona context, by engine and sector. In sport, with the Baseline persona (A), the slope of mention on popularity
falls on GPT from 1.64 to 1.04, on Gemini from 2.02 to 1.19 and on Perplexity from 0.82 to 0.39. Other changes concern

24 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
least
popular
most
popular
0
50
100share of mentions (%)
GPT
least
popular
most
popular
Gemini
least
popular
most
popular
Perplexity
Name
found
Not
verifiable
No
match
0
50
100share of the outcome (%)
13,689 647
none
Name
found
Not
verifiable
No
match
5,603 2,290 1,300
Name
found
Not
verifiable
No
match
6,171 115 55
Name found Not verifiable No match
popularity quintile
least popular most popular
Fig. C.5. Is the name of a mentioned brand in the sources the engine returned? Mentions in calls with observed search queries, for
brands that reach the threshold of Section 3.1 in the engine itself, by quintile of popularity (brands split within engine and sector, as
in Figure 3). Top: share of mentions whose name is found in the returned sources, that cannot be verified because some source could
not be read, or with no match although every source was read. Bottom: the same mentions read the other way, how each outcome is
distributed across the quintiles of popularity; numbers above the bars are mentions. GPT has no mention with no match. The match
is lexical and the pages were read after the calls.
a single engine. On Gemini the sport slope falls with every persona. On Perplexity the insurance slope falls with the
Baseline persona (A) and with the Profile variant (C), from 0.60 to 0.34 with both. Price variant (B) moves insurance in
opposite directions, steeper on GPT (0.91 to 1.59) and flatter on Gemini (3.56 to 2.22). None of the 46 contrasts in the
mean popularity of the mentioned brands between personas survives Benjamini–Hochberg, and those with 𝑝< 0.05
go in both directions. In insurance, the share of calls with a price word in the search queries rises from 4% without a
persona context to 37–40% with the Baseline persona (A) or the Profile variant (C). With a persona, Gemini searches in
37–42% of the calls, against 61% without a persona context. The mean source Jaccard index between two repeats with
the same persona is 0.39 on GPT, 0.23 on Gemini and 0.33 on Perplexity; between two answers with different personas
it is lower by 0.074, 0.080 and 0.065, and by 0.030, 0.035 and 0.010 after adjusting for the similarity of the search queries.

The Popular Get More Popular: Auditing Brand Bias in Generative Search 25
0
2
4
6
8
GPT
mentioning (%)
Insurance
0
2
4
6
Fashion & beauty
0
2
4
6
8
Sport
0
2
4
Travel
0
5
10
15
Gemini
mentioning (%)
0
2
4
6
0
5
10
0
2
4
6
1 5
0
2
4
Perplexity
mentioning (%)
1 5
0
1
2
1 5
0
2
4
1 5
0.0
0.5
1.0
1.5
popularity quintile
No persona context
Baseline persona (A)
Price variant (B)
Profile variant (C)
Fig. C.6. Mention rate by quintile of popularity and persona level, one panel per engine and sector, search off and on together; bands:
95% intervals from resampling prompts.

26 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
D Study 2: questions, signatures and rewrites
D.1 Choice of the names
The better-known brand is the candidate with the highest popularity among the brands most mentioned in the Study 1
answers to the prompt. The less-known brand is the least popular brand mentioned in those answers; it must not be
one of the five pages, it must have a known official site, and it must not belong to the same group as another brand
of the set. A page can be the target only if its popularity is at most half that of the better-known brand and at least
twice that of the less-known one, so that the two other brands differ from the target by at least a factor of two in search
volume. Invented names share no distinctive word, root, translation or form with the real ones, while generic terms,
places, ingredients and facts stay as in the original.
Table D.1. The 24 questions of Study 2 with the target page and its signatures. Better known and less known are other real brands
mentioned in the Study 1 answers to the same prompt; the invented brand has no registered.itdomain.
ID Question Target Better known Less known Invented
assicurazioni_03Quale assicurazione bici dovrei scegliere?AXA Unipol Qover Dalveris
assicurazioni_09Quale assicurazione sui voli mi consigli di scegliere?Heymondo Genertel ERGO Assicu-
razione Viaggi
Trevalda
assicurazioni_10Qual è la migliore assicurazione natante da scegliere? Cattolica Assicu-
razioni
Allianz Zurich Corlenta
assicurazioni_17Qual è l’assicurazione RCA migliore da scegliere?Allianz Direct Prima Assicu-
razioni
Admiral Corvalia
assicurazioni_19Quale assicurazione spese veterinarie dovrei scegliere?ConTe.it UniSalute Baboop Nidrava
assicurazioni_20 Quali sono le migliori opzioni per l’assicurazione vita in base
ai costi?
GenialLife Unipol SquareLife Pelora
moda_beauty_03 Quali profumi originali con prezzi bassissimi dovrei scegliere? Calvin Klein Zara Berdoues Fiorvale
moda_beauty_05Qual è il miglior siero antimacchie da scegliere?The Ordinary Caudalie SkinCeuticals Ilvessa
moda_beauty_08Quali sono i migliori jeans momfit da scegliere?OVS Zara Agolde Velmora
moda_beauty_14Qual è la migliore crema contorno occhi da scegliere?Kiehl’s Shiseido Neutrogena Aurelys
moda_beauty_18Qual è il retinolo migliore?The Ordinary La Roche-Posay The Inkey List Ondarys
moda_beauty_23Quali sono i profumi buoni da uomo che mi consiglieresti?Montblanc Zara Rochas Nevrola
sport_01Quali sono le migliori scarpe da trekking da scegliere?CMP Adidas Meindl Dravio
sport_09Qual è la migliore ebike per rapporto qualità prezzo?Trek Specialized Kalkhoff Brivano
sport_11Quali sono i migliori tapis roulant da scegliere?Everfit Technogym UREVO Varenzo
sport_13Qual è la racchetta da padel migliore da scegliere?Nox Adidas Wilson Zorvane
sport_17Quali sono le migliori cargo bike economiche da scegliere?Fiido Engwe Panda Bike Brovale
sport_21Quali sono le migliori scarpe da corsa da scegliere?ASICS Nike Mizuno Kervino
viaggi_04Quali villaggi scegliere per le vacanze in Cilento?Villaggio Elea Baia del Silenzio Camping Villag-
gio Saline
Ruvalia
viaggi_07Quale villaggio turistico all inclusive mi consiglieresti?Club Esse Alpitour World Meraki Resort Ombrevia
viaggi_13 Quali sono i migliori villaggi all inclusive alle Maldive del
Salento?
Nicolaus Club La
Giurlita
Vivosa Apulia Re-
sort
Arco del Saracino Lunerio
viaggi_15 Quali sono i migliori tour operator per un viaggio a Zanzibar? Veratour Alpitour World Savannah Explor-
ers
Calimbra
viaggi_17 Quali sono le migliori opzioni per il noleggio auto con prezzi
bassi?
Avis Renault Thrifty Orbisa
viaggi_18 Quali sono i migliori tour operator siciliani da scegliere per
un viaggio?
Go-Etna WeRoad KidSicily Brezzaria

The Popular Get More Popular: Auditing Brand Bias in Generative Search 27
Table D.2. Study 2, per question: the real products used for the better-known and less-known brands (– where that signature has
no real-product version), the distance in popularity between the target and each of the two real brands (orders of magnitude of
monthly search volume: better known minus target, target minus less known), and how often the models name the true brand from
the neutralised target page (12 answers per question).
ID Better known, real product Less known, real product Above Below Recognised
assicurazioni_03 Unipol Unica Mobilità Qover Qover-me 0.41 2.58 8%
assicurazioni_09 – – 0.34 1.88 50%
assicurazioni_10 Allianz Columbus Zurich Permare 0.61 0.42 0%
assicurazioni_17 – – 0.31 2.09 0%
assicurazioni_19 – – 0.82 1.60 25%
assicurazioni_20 Unipol Vita Smart SquareLife Turtleneck 1.80 0.77 0%
moda_beauty_03 Zara Red Temptation Berdoues Monoï & Tiaré 1.23 3.35 50%
moda_beauty_05 Caudalie Vinoperfect Siero Illuminante Anti-
Macchie
SkinCeuticals Discoloration Defense 0.37 0.44 100%
moda_beauty_08 Zara Z1975 Mom Fit Agolde 90’s Pinch Waist 0.42 2.89 33%
moda_beauty_14 Shiseido Benefiance Wrinkle Smoothing Eye
Cream
Neutrogena Hydro Boost Contorno Occhi Anti-
Fatica
0.31 0.32 58%
moda_beauty_18 La Roche-Posay Retinol B3 Siero The Inkey List Retinol Serum 0.31 1.29 100%
moda_beauty_23 Zara Vibrant Leather Rochas Moustache 1.61 1.88 50%
sport_01 Adidas Terrex AX4 Meindl Bhutan MFS 1.14 1.52 8%
sport_09 Specialized Turbo Vado Kalkhoff Endeavour 1.07 1.07 92%
sport_11 Technogym MyRun UREVO Foldi 3S 1.87 0.70 33%
sport_13 Adidas Drive Black 3.5 Wilson Blade V4 2.64 0.33 83%
sport_17 Engwe LE20 Panda Bike Cuore 0.39 0.94 33%
sport_21 Nike Pegasus 41 Mizuno Wave Rider 29 0.71 0.60 67%
viaggi_04 – – 0.89 1.77 25%
viaggi_07 – – 1.69 1.36 17%
viaggi_13 – – 0.74 0.39 0%
viaggi_15 – – 0.58 2.42 17%
viaggi_17 – – 0.37 1.25 8%
viaggi_18 – – 2.55 1.92 50%
Mean 15 questions 15 questions 0.97 1.41 38%
D.2 Rewriting instructions (Italian, as sent togpt-5.5)
Each rewrite instruction is followed by a common part.
• Structure:Riscrivi questo testo di una pagina prodotto per renderlo più chiaro e facile da usare per chi deve scegliere: riorganizzalo con brevi
titoletti ed elenchi, metti prima le informazioni decisive, elimina ripetizioni.
• Fluency:Riscrivi questo testo per renderlo più scorrevole senza cambiarne il contenuto: le frasi devono legarsi bene l’una all’altra, la lingua deve
essere chiara e coinvolgente e tutte le informazioni originali vanno conservate.
•Authoritative:Riscrivi questo testo in uno stile autorevole, senza aggiungere né togliere informazioni: deve trasmettere sicurezza e competenza,
con affermazioni nette, e puoi rivolgerti al lettore in seconda persona. Mantieni la struttura (a capo, elenchi, ordine delle parti) e riformula solo
singole frasi. Non aggiungere garanzie, primati o promesse.
• Common part:Il testo contiene segnaposto tra graffe come {BRAND} o {TECH_1}: copiali identici, senza toglierne nessuno e senza aggiungerne. Usa
SOLO le informazioni presenti nel testo: non aggiungere fatti, numeri, statistiche, citazioni, fonti, giudizi di terzi o promesse nuove, e non togliere
nessuna informazione. Mantieni tutte le cifre esattamente come sono. Scrivi in italiano. Lunghezza simile all’originale: circa {n} parole, mai più
di {nmax}. Restituisci solo il testo riscritto, in testo semplice (puoi usare a capo, trattini per gli elenchi e brevi titoletti seguiti da due punti; niente
markdown come # o **).
D.3 Ranking message (Italian, as sent to the four models)
The message tells the model that the pages were found for the question and that their order is random. Each page begins
with a line giving its domain and web address, followed by its text.The question, then:Per rispondere usa le pagine qui sotto, trovate per
questa domanda. L’ordine delle pagine è casuale.Each page follows as[k] Fonte: dominio — URLand its text. The message ends with:Rispondi alla domanda

28 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
usando queste pagine e citale con il loro numero tra parentesi quadre, per esempio [2]. Alla fine scrivi un’ultima riga con la tua classifica completa delle cinque
pagine, dalla prima che consigli all’ultima, nel formato: CLASSIFICA: [n] > [n] > [n] > [n] > [n]
D.4 Judging instruction (Italian, as sent todeepseek-v3.2)
Confronta due versioni di un testo (i segnaposto tra graffe sono nomi). Conta come differenza SOLO un’informazione fattuale presente in una versione e del
tutto assente nell’altra, oppure un valore cambiato (un numero, una caratteristica, una condizione, un prezzo, una copertura). NON sono differenze: titoli o
intestazioni aggiunti o tolti, elenchi al posto di paragrafi, ordine diverso, sinonimi, riformulazioni con lo stesso significato, un riepilogo che ripete informazioni
presenti altrove, punteggiatura, refusi corretti, frasi esortative o di puro tono. Elenca solo le differenze vere, una per riga, poi un’ultima riga ’ESITO: UGUALI’ se
non ce ne sono, altrimenti ’ESITO: DIVERSI’.
D.5 Revised rewrites
When a rewrite failed the checks three times, the attempt with the fewest errors was sent back to gpt-5.5 with the
original for a minimal correction of what the checks had found, and then went through the same checks and the same
judge. This happened for the structure rewrite of 6 questions (assicurazioni_03, assicurazioni_09, assicurazioni_19,
sport_17, viaggi_04, viaggi_17). The structure rewrite of sport_21 was corrected by hand (final length 1.06 times the
original) and passed the judge again. Every step is logged with the stimuli.
E Study 2: additional results
The effect of rewriting under each signature is +0.016 positions under the true brand,−0.001 with an invented product,
+0.043 and +0.031 under the better-known and the less-known brand, and +0.023 under an invented brand. The
differences between signatures are not significant (repeated-measures analysis of variance over the 24 questions), and
the difference between the true and the invented brand is−0.007 [−0.057, 0.043].
Table E.1. Study 2 by model and by sector: positions gained by the target page (positive = ranked higher), computed as in Table 2.
Each column is one row of that table, in the same order ( treal, dinvented product name, as in Figure 7). Models average the 24
questions; sectors average six questions and the four models. Descriptive.
Original tvs Original tvs Better dvs Less dvs Rewrite vs
Invented d Original d Less d Invented d original
(H4a) (H4b) (H4c) (H4e) (H5a)
DeepSeek 0.24 0.12−0.06 0.16 0.05
Gemini 0.42 0.10 0.11 0.15 0.03
GPT 0.57 0.17 0.10 0.23 0.03
Perplexity 0.56 0.19 0.04 0.23−0.01
Insurance 0.56 0.06 0.17 0.32 0.06
Fashion and beauty 0.68 0.39−0.02 0.11 0.03
Sport 0.26 0.11−0.05 0.17−0.01
Travel 0.27 0.02 0.09 0.18 0.01
All 0.44 0.14 0.05 0.19 0.02
With the original text, the true brand gains more than 1.3 positions in three questions (Montblanc, Allianz Direct
and Veratour), and leaving out any single question keeps the mean gain between 0.39 and 0.49. When the other brands
carry a real product of their own instead of an invented one, the page rises by about 0.1 positions under either brand,
which is not significant after correction. With their real products, the two brands rank the page above the invented

The Popular Get More Popular: Auditing Brand Bias in Generative Search 29
brand (+0.27, Holm 𝑝= 0.042, and +0.29, Holm 𝑝= 0.026), do not differ from each other, and rank it lower than its true
brand, though not significantly. Table E.2 gives every pair of signatures.
Table E.2. Study 2: every pair of the seven signatures ( treal, dinvented product name, as in Figure 7). Δ: positions gained by the
target under the first signature over the second, averaged over the four texts; 95% intervals from resampling questions. Pairs with
a real-product version ofBetter knownorLess knownuse the 15 questions where it exists. Family: H4a–H4e are rows of Table 2
(one-sided 𝑝, Holm over its seven rows); R is the family of seven comparisons with the real-product versions (two-sided 𝑝, Holm over
the seven); the other pairs are exploratory (two-sided𝑝, not adjusted).
First Second𝚫95% interval Questions Family𝑝
Original t Original d +0.14[0.05,0.27]24 H4b<.05
Original t Better known t +0.17[−0.06,0.45]15 R n.s.
Original t Better known d +0.20[0.04,0.39]24 –<.05
Original t Less known t +0.15[−0.01,0.33]15 R n.s.
Original t Less known d +0.25[0.05,0.47]24 –<.05
Original t Invented d +0.44[0.23,0.69]24 H4a<.01
Original d Better known t −0.04[−0.17,0.08]15 – n.s.
Original d Better known d +0.06[−0.04,0.15]24 – n.s.
Original d Less known t −0.06[−0.15,0.02]15 – n.s.
Original d Less known d +0.11[−0.06,0.29]24 – n.s.
Original d Invented d +0.30[0.13,0.51]24 –<.01
Better known t Better known d +0.11[0.03,0.21]15 R n.s.
Better known t Less known t −0.02[−0.16,0.11]15 R n.s.
Better known t Less known d +0.08[−0.03,0.20]15 – n.s.
Better known t Invented d +0.27[0.12,0.44]15 R<.05
Better known d Less known t −0.13[−0.27,−0.02]15 – n.s.
Better known d Less known d +0.05[−0.11,0.22]24 H4c n.s.
Better known d Invented d +0.24[0.08,0.44]24 –<.05
Less known t Less known d +0.10[0.02,0.19]15 R n.s.
Less known t Invented d +0.29[0.14,0.46]15 R<.05
Less known d Invented d +0.19[0.11,0.29]24 H4e<.01
Asked which brand a page with all names replaced belongs to, the models name the true brand in 38% of the answers,
an upper bound since the question invites a guess, from none in four questions to every answer for the two pages of
The Ordinary (Table D.2); Gemini recognises the brand most often (65% of its answers) and DeepSeek least often (14%).
In the rankings, no answer mentions the original brand when the page carries another signature, and the effect of the
true brand is not related to how often the page is recognised (Spearman 𝜌= 0.10). The effect of the product name (H4b),
instead, comes mostly from the pages the models recognise: it is 0.03 positions on the 11 questions recognised at most a
quarter of the time and 0.24 on the other 13. Of the three subsets of questions fixed before the collection, the true brand
gains 0.48 positions on the 20 questions whose target ranked between 2 and 4 in the calibration run, 0.36 on the 14
questions where the models rate the better-known brand as better known than the target, and 0.40 when we drop the
four questions where the brand appears only in the web address. On the same 14 questions, H4c is +0.15, not significant.
The balanced orders of the pages cancel a position effect: the target ranks 3.27 when shown first and 3.54 when shown
last.
F Summary of hypotheses

30 Giorgio Monaco, Jacopo Lenti, and Francesco Pierri
Table F.1. Hypotheses, predictions and outcomes, by research question. Gains in Study 2 are positions on a scale of 1 to 5.
Prediction Outcome
RQ1, Study 1: brand popularity bias
H1aMore popular brands are mentioned more often Supported in 23 of 24 configurations
H1bMore popular brands are cited more often Partially supported: 8 of 12 engine–sector pairs
H1c The brand popularity bias is stronger withsearch-off than
search-on
Not supported (+0.02 [−0.03, 0.07])
H2a Answers with more similar search queries share more
sources and text
Supported
H2bTheir mentioned brands do not overlap more Not supported: brands follow the search queries almost as
closely as sources
H3a The brand popularity bias is the same with and without a
persona
Not supported for the Baseline persona (A) and the Price
variant (B)
H3b Answers with different personas are as similar as answers
with the same persona
Not supported: a gap remains at equal query similarity
RQ2, Study 2: brand familiarity bias (H4)
H4a A page ranks higher under its real brand than under an
invented one
Supported (+0.44)
H4b It ranks higher with its real product name than with an
invented one
Supported (+0.14)
H4c A more popular real brand ranks it higher than a less popular
one
Not supported (+0.05)
H4d Another real brand lowers it because it does not match the
page
Not significant (+0.08)
H4e A less popular real brand ranks it higher than an invented
one
Supported (+0.19)
RQ2, Study 2: rewriting (H5)
H5aA rewrite raises its rank Not supported (+0.02)
H5bThe real brand gains more than rewriting Supported (+0.42)
