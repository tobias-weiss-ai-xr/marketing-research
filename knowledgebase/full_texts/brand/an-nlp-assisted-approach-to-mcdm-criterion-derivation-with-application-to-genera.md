---
title: An NLP-Assisted Approach to MCDM Criterion Derivation, with Application to Generative AI Assistants
url: https://doi.org/10.33707/akuiibfd.1957354
category: brand
subcategory: framework
date: 2026-10
venue: Afyon Kocatepe Üniversitesi İktisadi ve İdari Bilimler Fakültesi Dergisi
authors:
- Damla Aydin
source: openalex-oa
pdf_url: https://dergipark.org.tr/en/download/article-file/6043450
pages: 15
chars: 67712
fetched_at: '2026-11-08T19:40:12+00:00'
kb_version: 1
---

# An NLP-Assisted Approach to MCDM Criterion Derivation, with Application to Generative AI Assistants

Geliş/Received: 22.05.2026 | Revizyon/Revised: 18.09.2026 |Kabul/Accepted: 24.09.2026
How to cite this article / Bu makaleye atıf vermek için:
Aydın, D., (2026). An NLP-Assisted Approach to MCDM Criterion Derivation, with Application to Generative AI Assistants. KOCATEPEİİBFD, 28(Special Issue),
252-266. https://doi.org/10.33707/akuiibfd.1957354

Research Article (Special Issue) | Araştırma Makalesi (Özel Sayı)

An NLP-Assisted Approach to MCDM Criterion Derivation, with Application to
Generative AI Assistants

Damla Aydın Res. Assist., Ph.D., Eskişehir Osmangazi University, Türkiye, dgeldisen@ogu.edu.tr, 0000-0003-3837-5572

Corresponding author/Sorumlu yazar: Damla Aydın
Abstract
Work on multi -criteria decision making (MCDM) has gone mostly into aggregation and weighting. The upstream stage, where the criterion
set is actually formed, has had less attention, and what attention it has had stays close to expert driven procedures such as Delphi,
valuefocused thinking, and BWM or SWARA style validation. We propose a reusable NLP-assisted pipeline for that criterion derivation stage,
aimed at decision objects that change quickly. Sentence- BERT embeddings are projected with UMAP, clustered with HDBSCAN, and
represented under BERTopic; a documented thematic abstraction step then raises the topics to higher order criteria. Run over 4,099 cleaned
Google Play reviews from five generative AI assistants, the pipeline returns six robust candidate criteria (access and cost policy, service
continuity, multimodal capability, conversational modality robustness, multilingual fidelity, conversation management) and one provisional
criterion, task domain breadth, that is flagged across all four fragility diagnostics. The abstraction step replicates at Krippendorff’s alpha =
0.947, and a brand masked replication recovers six of the seven. An illustrative FUCOM-RAFSI operationalization shows how the criteria feed
a downstream workflow without our claiming any platform ranking. We offer the framework as a source of candidate criteria for  MCDM
workflows, not as a decision support instrument.
Keywords: Multi-criteria Decision-making; Criterion Derivation; BERTopic; NLP JEL Codes: C44, C88, D81, M15

Çok Kriterli Karar Vermede Kriter Türetimine Doğal Dil İşleme Destekli Bir
Yaklaşım ve Üretken Yapay Zekâ Asistanları Üzerinde Bir Uygulama
Öz
Çok kriterli karar verme (ÇKKV) çalışmaları büyük ölçüde ağırlıklandırma ve toplulaştırmaya yönelmiştir. Kriter setinin asıl oluşturulduğu yukarı
akış aşaması ise daha az ilgi görmüş, gördüğü ilgi de Delphi, değer odaklı düşünme ve BWM ya da SWARA temelli doğrulama gibi uzman odaklı
prosedürlerin yakınında kalmıştır. Bu çalışma, hızla değişen karar nesneleri için söz konusu kriter türetme aşamasına yönelik, yeniden
kullanılabilir ve doğal dil işleme (NLP) destekli bir süreç önermektedir. Cümle BERT gömmeleri UMAP ile indirgenmekte, HDBSCAN ile
kümelenmekte ve BERTopic altında temsil edilmekte; ardından belgelenmiş bir tematik soyutlama adımı konuları daha üst düzey kriterlere
taşımaktadır. Beş üretken yapay zekâ asistanına ait temizlenmiş 4.099 Google Play yorumu üzerinde çalıştırıldığında süreç alt ı sağlam aday
kriter (erişim ve maliyet politikası, hizmet sürekliliği, çok modlu yetenek, konuşma kipinin dayanıklılığı, çok dillilik başarımı, konuşma yönetimi)
ile dört kırılganlık testinin tamamında işaretlenen bir koşullu kriter (görev alanı genişliği) vermektedir. Soyut lama adımı Krippendorff alfa =
0.947 düzeyinde tekrarlanmakta, marka maskeli tekrar analizinde yedi kriterin altısı yeniden elde edilmektedir. Açıklayıcı bi r FUCOM-RAFSI
uygulaması, herhangi bir platform sıralaması iddia edilmeden, kriterlerin aşağı akış bir iş akışı nı nasıl beslediğini göstermektedir. Çerçeveyi,
bir karar destek aracı olarak değil, ÇKKV iş akışları için aday kriter kaynağı olarak sunuyoruz.
Anahtar Kelimeler: Çok Kriterli Karar Verme; Kriter Türetimi; BERTopic; Doğal Dil İşleme JEL Kodları: C44, C88, D81, M15
Introduction
This paper draws on three research streams: methodological work on criterion derivation within multi criteria decision making
(MCDM), the use of natural language processing (NLP) for managerial decision support, and the study of user generated content
(UGC) in information systems and management research. We treat criterion derivation as an MCDM stage in its own right .
Neglecting it biases every downstream weighting and aggregation step, however well those steps handle uncertainty in expert
preference.
MCDM methods such as AHP (Saaty, 1980, 2008), BWM (Rezaei, 2015), MABAC (Pamucar & Cirovic, 2015), MARCOS (Stevic et al.,
2 0 2 0 ) ,  E D A S ,  W A S P A S ,  a n d  t h e i r  f u z z y  v a r i a n t s  n o w  f o r m  a n  e s t a b l i s h e d  s e t  o f  t o o l s  f o r  w e i g h t i n g  a n d  r a n k i n g .  M o s t
methodological innovation has gone into aggregation. The upstream stage has not been left out. Value-focused thinking (Keeney,
1992, 1996) sets out procedures for identifying fundamental objectives, and structured Delphi approaches (Dalkey & Helmer,

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
253
1963; Linstone & Turoff, 1975) give iterated expert convergence. BWM and SWARA based work has also formalized criterion -set
validation (Rezaei, 2016; Mi et al., 2019). In practice, criteria usually come from literature distillation, Delphi consensus , or small
expert workshops calibrated by AHP style pairwise comparison. Each route is defensible, and each carries assumptions. Literature
distillation reuses earlier vocabulary and tends to lag behind fast moving objects, and Delphi panels carry the priors of a small,
often homogeneous informant pool. Our narrower claim to novelty is that large scale unprompted user discourse, used as a
candidate criterion source for MCDM, is still comparatively underexplored.
Generative AI assistants such as ChatGPT, Gemini, Claude, Copilot, and DeepSeek are objects of exactly this kind. People use them
across many personal productivity settings, they change on a roughly quarterly cadence, and their evaluative criteria have not yet
settled in the literature. When the usual knowledge base for criterion derivation is thin or out of date, is there a principled way to
draw on large-scale user discourse instead?
App-store reviews are a workable complement, and current NLP makes them usable. Reviews of generative AI mobile applications
are large scale and naturally occurring. They record what users treat as important. Self selection toward praise or complaint colors
them, but recurring evaluative concerns still come through. We model them with BERTopic, pairing semantic embeddings with
clustering, and read  off the recurrent themes. These themes are subsequently abstracted into higher order dimensions that
correspond to MCDM criteria, including access and pricing policy, multimodal capability, conversational robustness, and
conversation management. Expert ju dgment does not disappear. It simply moves, from generating the criteria to interpreting,
validating, and weighting them.
The study is exploratory and its scope is deliberately narrow. We offer the framework as a source of candidate criteria for l ater
MCDM work on generative AI assistants, not as a substitute for expert evaluation and not as a ready decision support tool. It stops
at one point. A candidate criterion set, grounded in user discourse and traceable to the text. Weighting and ranking, by AHP, BWM,
T O P S I S ,  MA B AC ,  M A RC O S ,  o r ED A S ,  be l o ng  t o  l a t e r  a ppl i ca t i o ns.  S o  do  t he  c r i t e r i a  t ha t  r e vi e w s c a nno t  c a pt ur e  we ll ,  suc h as
response accuracy, factuality, hallucination control, latency, and data handling privacy. Those will need expert -based evaluation
later.
MCDM research has long centered on weighting consistency, aggregation stability, and the representation of uncertainty. Even
so, any downstream ranking is only as good as the upstream criterion set it works from. We therefore move the methodological
focus from aggregation to the formation of the criterion set, especially for fast -changing decision objects whose evaluative
dimensions are not yet settled in the literature.
Three implications follow. First, the unit of novelty is the pipeline rather than any one algorithmic component. Second, the
empirical product is a candidate framework for the mobile app surface, a starting point for expert refinement and not a final
taxonomy. Third, the stance is exploratory and mechanism-identifying, not confirmatory.
The contribution is fourfold, with a clear hierarchy. First, and primarily , we propose a reusable NLP assisted pipeline for the
criterion derivation stage of MCDM workflows. It couples Sentence BERT embeddings, UMAP projection, HDBSCAN clustering, and
BERTopic topic representation with a thematic abstraction step that raises data-driven topics to higher order criteria. The pipeline
does not commit to any particular downstream weighting method and carries over to other domains that have large bodies of
user generated discourse.
Second, we run the pipeline on 4,099 cleaned English language Google Play reviews, drawn from an initial 10,000 across five
assistants (ChatGPT, Gemini, Claude, Copilot, and DeepSeek), and obtain a candidate criterion framework for evaluating
generative AI  assistants on the mobile -app surface. The framework is a source of candidate criteria that complements expert
driven derivation rather than replacing it.
Third, we report a replicability assessment with several strands. Two independent coders classify the topics at Krippendorff’s alpha
= 0.947 (eleven way) and 1.000 (substantive vs. non -substantive). A brand masked replication recovers six of seven criteria; an
HDBSCAN sweep recovers all seven at the central operating point; swapping the encoder to all -mpnet-base-v2 recovers six o f
seven; a within -window consistency check recovers six of seven in each half; and an LDA baseline at k = 20 finds an identifiable
counterpart for every substantive BERTopic  topic. C7 (task -domain breadth) is flagged across all four fragility diagnostics and is
therefore treated as a provisional criterion rather than a fully established one.
Fourth, and with comparatively less immediacy, we illustrate how the six robust criteria (C1- C6) can be operationalised  within
FUCOM-RAFSI in a hypothetical managerial and academic productivity setting; C7 remains a provisional candidate and is excluded
from this illustration. The resulting ranking is not a verdict on the platforms, but a direct consequence of the evaluati on
architecture, namely the criteria set as specified, the weight vector derived through FUCOM, and the decision matrix of score s.
This application constitutes less than 20% of the completed manuscript and serves only to demonstrate the framework's

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
254
applicability, not to guide practitioners. The framework is not itself a decision support system. Dimensions such as response
accuracy, factual articulation, hallucination risk, latency, and privacy cannot be inferred from mobile application reviews, and
future research should establish their definitions, scales, and units.
1. Related Work
Three literatures are reviewed here: criterion derivation in MCDM, NLP and topic modeling in business and information systems
research, and user-perception evaluation of generative AI assistants.
1.1. Criterion Derivation in MCDM
MCDM research offers a large stock of methods for weighting  criteria and ranking alternatives. AHP remains among the most
established, eliciting pairwise expert judgments (Saaty, 1980, 2008). BWM lightens the cognitive load by anchoring on the bes t
and worst criteria (Rezaei, 2015, 2016). Other methods widen the t oolbox: outranking and reference -point approaches such as
MABAC (Pamučar & Ćirović, 2015), MARCOS (Stević et al., 2020), EDAS (Keshavarz Ghorabaee et al., 2015), and WASPAS (Zavadskas
et al., 2012). A separate line extends all of them under fuzzy, intuitionistic fuzzy, hesitant fuzzy, neutrosophic, and rough set
representations.
Far less has been said about where the criteria come from in the first place. The usual recipe mixes a literature synthesis, an expert
consensus step like Delphi (Dalkey & Helmer, 1963; Linstone & Turoff, 1975), and a few smaller expert evaluations tuned through
consistency-oriented methods such as AHP and BWM. Hesitant and fuzzy variants address uncertainty in expressed preferences
but not the sampling logic; the criteria still come from a small, purposively chosen pool. Recent surveys (Mi et al., 2019) note that
elicitation is often reported only in summary.
A narrower strand treats the criterion set as a problem of its own, separate from weighting. Value focused thinking (Keeney, 1992,
1996) puts fundamental objectives first, before any alternatives, and hands down a set of diagnostics, completeness,
decomposability, operationality, measurability, non -redundancy, that the field later absorbed. BWM and SWARA based work
(Rezaei, 2016) ties the two back together. It screens candidate criteria for operationality and non redundancy, then moves into
pairwise comparison. What none of this questions is where the candidates start. They start with experts and analysts. Our mov e
is to widen that pool, adding large -scale unprompted user discourse as a further source that feeds the same pro cedures rather
than displacing them.
1.2. NLP and Topic Modeling in Business and IS Research
Unsupervised modeling of latent themes in text has advanced quickly. Early work used Latent Dirichlet Allocation (Blei et al., 2003)
on online reviews, financial disclosures, social media, and customer service records. LDA-based studies mined tourism reviews for
service quality dimensions (Guo, Barnes, & Jia, 2017), and comparable e -commerce work surfaced product attribute and trust
dimensions. LDA has well -known limitations: bag -of-words assumptions, sensitivity to preprocessing, and semantically diffuse
topics.
Contextual embeddings ease several of these limitations. Sentence-BERT (Reimers and Gurevych, 2019) produces dense semantic
representations of short texts. BERTopic (Grootendorst, 2022) couples these with UMAP and HDBSCAN and uses class -based TF-
IDF for in terpretable descriptors, and on short user generated texts it yields more coherent topics than LDA. Recent studies in
marketing, hospitality, IS, and education have used it to extract evaluation themes from reviews, course feedback, and open ended
surveys (An, Oh, & Lee, 2023).
A smaller line of work links UGC mining to the construction of decision criteria: review derived themes have fed service qual ity
frameworks in tourism and product comparison rubrics in e -c om me r c e  ( S ha r m a  & S har m a ,  2 0 1 9) .  W e  c a r r y t hi s i de a  o ve r  t o
generative AI assistants and make the step from topics to MCDM ready criteria explicit.
1.3. Evaluation of Generative AI Tools
Two literatures evaluate LLM assistants. One benchmarks raw model capability on standardized tasks (Hendrycks et al., 2021;
Liang et al., 2023), useful for technical comparison but a step removed from how anyone actually uses  the tools. The other, in IS
and management, asks why people adopt them. Here TAM and UTAUT variants applied to AI chatbots keep returning the same
handful of drivers, perceived usefulness, ease of use, trust, behavioral intention (Strzelecki, 2024), while  a parallel productivity
literature tracks what the tools do to knowledge work (Brynjolfsson, Li, & Raymond, 2025; Noy & Zhang, 2023; Dell’Acqua et al .,
2023).
What stays thin on either side is the set of criteria the professionals themselves apply. The instruments currently in use la rgely
inherit their constructs from earlier technologies, and this inheritance tends to overlook what is distinctive to generative AI,
including hallucination risk, prompt sensitivity, conversational memory, citation behaviour ,  a n d  t h e  i t e r a t i v e  n a t u r e  o f  c o-
production. Our contribution sits in that gap. It is a candidate criterion set read inductively out of UGC, one to set beside  expert

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
255
elicited instruments and check against them.
2. Methods
The pipeline is documented end to end below. Section 2.1 sets out the research design and analytical scope, Sections 2.2 and 2.3
the data sourcing and corpus construction, and Section 2.4 the deterministic preprocessing funnel. Section 2.5 covers the BERTopic
NLP pipeline, its parameters, and its stability diagnostics.
2.1. Research Design
The study takes an exploratory, mechanism identifying stance. It begins by retrieving app- store reviews, then cleans and
standardizes them through deterministic preprocessing. We analyze the cleaned corpus with BERTopic, built on sentence
transformer embeddings, and let topics emerge without supervision. In the last step the researchers read the substantive topics
and abstract them into higher order evaluation criteria.
The paper does not perform MCDM weighting, ranking, or alternative evaluation. Platform level statistics describe where the
discourse of each criterion is concentrated in our sample, not relative performance. Criterion validation is downstream and out of
scope.
2.2. Data Source and Scope
Google Play reviews offer three things: scale, cheap retrieval, and evaluative language that arises on its own, not in reply to a
researcher’s construct list. The low cost also cuts the selection bias that expert panels carry. Three limits come with it, and Section
7 takes them up: one store (Google Play), one language (English), one device class (Android mobile). iOS, desktop, and enterp rise
users do not appear, and the reviewer base tilts toward individuals rather than enterprise administrators. The frame work should
be read as a floor on user-surfaced criteria.
2.3. Corpus Construction
Retrieval ran on 2026-05-12 (UTC) through google-play-scraper, with country=us and lang=en. For each app we made two passes,
Sort.NEWEST and Sort.MOST_RELEVANT, deduplicated on reviewId, and kept exactly 2,000 per platform, so the raw N is 10,000.
The app IDs: ChatGPT com.openai.chatgpt, Gemini com.google.android.apps.bard, Claude com.anthropic.claude, Copilot
com.microsoft.copilot, DeepSeek com.deepseek.chat. The two sort modes are there to widen coverage on recency and on salience
at once.
2.4. Preprocessing
Preprocessing was a deterministic five -step funnel, and we logged the count and the threshold at every step so it can be rebuilt.
The per-step retention counts are reported in Table 1.
Table 1. Preprocessing Funnel.
Step N retained
Raw 10,000
After reviewId de-duplication 10,000
After text-normalization de-duplication 6,803
After length filter (≥25 characters, ≥4 tokens) 4,437
After English-only language filter 4,099
Source: Authors.
Text normalization lowercases the body, strips URLs, emoji, and ASCII control characters, collapses whitespace, and drops
redundant punctuation. Deduplication on the normalized surface removes near -identical short reviews. The length filter sets
MIN_CHARS = 25 and MIN_TOKENS = 4. Language detection uses langdetect with DetectorFactory.seed = 42, applied after the
length filter to steady short text detection; non-en reviews are dropped. In all, the funnel removes 5,901 of 10,000, or 59.0 percent,
and Section 3 gives the per-platform consequences. Short, generic praise reviews are the ones it strips most. The English only filter
then flips the platform ranking, becaus e ChatGPT’s reviews lean heavily non -English, with Indonesian, Arabic, Afrikaans, Dutch,
French, and Russian especially common.
The English-only filter (country=us and lang=en during retrieval and langdetect during preprocessing) only determines the review's
language, not the complaint's topic. As such, C5 (multilingual fidelity) results from English -speakers writing to the effect that the
chatbot responded in a language that they did not request (e.g. The ubiquitous "asked for English, was answered in Chinese"
complaint that arose with DeepSeek). The filter merely changes scope; it doesn’t get rid of the term. Instead of receiving it  in
Chinese, Arabic, Turkish, Indonesian, and the myriad other languages, thi s kind of multilingual feedback is entirely excluded. It is
therefore likely that C5 is actually under-specified, encoding only the "was promised English, got something else" component. This
is precisely the same decision that results in ChatGPT being 8 percent of the de -duplicated portion of the overall dataset, and so
the analysis of the English filter herein should be considered alongside Section 3.

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
256
2.5. NLP Pipeline
Cleaned reviews are encoded with all-MiniLM-L6-v2 (Reimers & Gurevych, 2019), which returns 384 dimensional  embeddings. At
22M parameters the model runs on a single CPU, appears widely in published BERTopic applications (An et al., 2023), and gives
semantically coherent representations of short user generated texts. To check that the criterion set is not tied to one encoder, we
re-encoded the corpus with all -mpnet-base-v2 (110M parameters, 768 -dim) and held everything else fixed; the mpnet  run
recovered 16 topics with 14.7 percent outliers and six of seven substantive criteria (C1- C6 recovered; C7 not recovered), in line
with three other independent fragility diagnostics. A fuller benchmark against bge-small-en-v1.5, e5-small-v2, or domain-adapted
variants with c_v/c_npmi (Röder, Both, & Hinneburg, 2015) is a reasonable follow up.
Embeddings go through UMAP for reduction (n_neighbors = 15, n_components = 5, min_dist = 0.0, metric = "cosine",
random_state = 42). HDBSCAN then clusters them ( min_cluster_size = 41, min_samples = 5, metric = "euclidean",
cluster_selection_method = "eom"). The min_cluster_size follows max(20, round(0.01 * N)). For N = 4,099 that is 41, roughly one
percent of the corpus. The point of the rule is balance: it suppre sses micro -clusters without killing rarer themes, such as
multilingual fidelity at just 59 documents.
A sweep over `min_cluster_size ∈ {20, 30, 41, 60, 80}` probed how sensitive the result is to that choice. At 20 there are 26 topics,
11.5 percent outliers, and all seven criteria recover; at 41, 20 topics, 9.8 percent outliers, and again all seven. Push it to 60 and 80
and the structure thins to 14 then 13 to pics, while recovery slips to five of seven, C7 going first and C6 after. The operating point
we picked therefore sits inside a stable band. C7 is the recurring weak spot: across all four checks, brand masking (Section 5), the
sweep, the encoder substitution, and the within window consistency check (Section 3), it is the first criterion to break.
Topic representation used BERTopic 0.17.4. Its CountVectorizer filtered English stop -words, throwing out high- frequency, low -
content tokens like “the,” “and,” and “is.” An n -gram range of (1, 2) let it keep single words alongside short phrases, “customer
support,” say, or “response quality.” A min_df of 5 removed anything appearing in fewer than five documents, which cuts noise.
For each topic we read the most distinctive terms from class -based TF-IDF weighting. Those terms are what we used to interpret
the cluster. For reproducibility we fixed UMAP’s random seed and ran HDBSCAN under a fixed input order, so repeated runs of
the pipeline cluster the same way.
The step from BERTopic topics to MCDM ready criteria was an interpretive reading. Each topic was judged on three things: its top
c-TF-IDF terms, up to five representative documents from BERTopic , and its spread across platforms. The 20 topics then fell into
four groups. First, substantive evaluative topics, gathered around coherent concerns that could be paraphrased as candidate
MCDM criteria. Second, global -affect topics, generic praise or undir ected comparisons with no specific evaluative dimension.
Third, platform-identity topics, where the platform name, not the content, held the cluster together. Fourth, the heterogeneous
residue under HDBSCAN topic −1.
Substantive topics were merged into higher order criteria, treating the topic as symptom and the criterion as the underlying
evaluative dimension. Two topics on message limits and pro -tier access (T3, T19) merge into C1, and two on account suspension
and phone verification (T12, T15) merge into C2; the remaining substantive topics each map to one criterion (C3 through C7). We
rename the original label “productivity domain coverage” to task domain breadth to avoid overpromising the claim a 43 document
cluster can support.
For replicability, two coders worked independently. Each sorted the 21 topics (20 substantive plus noise) into one of eleven
categories: seven substantive (C1 -C7), two global affect sub -types, one platform -identity, and one outlier. They agreed on 20 of
21, or 95.2 percent. Krippendorff’s alpha (Krippendorff, 2019) is 0.947 for the elevenway  coding and 1.000 once it collapses to
three (substantive vs. global -affect vs. other). The one disagreement, T10, fell between affect sub -types and never reached the
criterion set.
We kept the codes, intermediate tables, and manifest records needed to rebuild the corpus and topic model from the raw Google
Play data. The UMAP and langdetect procedures both used the fixed random seed 42. Preprocessing records hold the filter
thresholds and the document counts at each stage, and the BERTopic  records hold the embedding model, the hyperparameters,
and the outlier share. Visualizations of intertopic distances and topic sizes are kept with the supplementary materials.
To check that the substantive topics are not artefacts of the embedding -plus-density-clustering pipeline, we ran an LDA baseline
(Blei et al., 2003) at k = 20 on the same cleaned corpus. For each substantive BERTopic topic, its top fifteen c- TF-IDF terms were
compared with the top fifteen weighted terms of the LDA topics by the Jaccard index. Section 3 reports the outcome. Every one
of the nine substantive BERTopic topics has an identifiable LDA counterpart: two stron g pairings (Jaccard ≥ 0.15), seven weak
(0.07–0.15), and none unmatched.

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
257
Section 5 gives the full procedure and artefacts for the brand-masked replication. In brief, product names, parent companies, and
model variants are masked during preprocessing and the full pipeline is re -run with everything else fixed. The high dominance
platform identity surface drops from four topics to one; six of seven substantive criteria (C1-C6) recover with strong term overlap;
C7 does not recover and is flagged.
3. Results
The preprocessing funnel left an analyzable corpus of 4,099 English language reviews out of the 10,000 drawn (41.0 percent
retention). Table 2 gives the per platform counts.
Table 2. Cleaned Corpus by Platform.
Platform Clean N Share of corpus
Claude 1,269 31.0 %
DeepSeek 1,071 26.1 %
Copilot 1,061 25.9 %
Gemini 371 9.1 %
ChatGPT 327 8.0 %
Total 4,099 100.0 %
Source: Authors.
Cleaning leaves the corpus unbalanced, unlike the even raw draw. ChatGPT and Gemini hold the smallest shares; Claude,
DeepSeek, and Copilot each hold a quarter to a third. Two mechanisms explain it. First, the normalization deduplication and length
filters cut the very short reviews (“good”, “best AI app”) that crowd the most popular apps. Second, the English only filter tilts
things further, since ChatGPT’s pool is mostly non- English. So the criterion-level shares in Table 5 are not quality verdicts, and
Section 7 spells out the generalisation limit.
BERTopic returned 20 substantive topics plus the HDBSCAN noise cluster (topic −1). The noise cluster collects documents that no
coherent density based cluster could claim with confidence. It holds 403 of them, 9.83 percent of the corpus, which is about what
BERTopic usually reports on short user generated texts (An et al., 2023). Table 3 lays out the topics.
Table 3. Selected Discovered Topics Illustrating the Topic Landscape.
Topic Count Top terms (abridged)
−1 403 pilot, good, limit, ai, like, free, just, chat
0 881 good, helpful, useful, love, information, great, easy
1 625 app, good, good app, great app, use, love app, update
2 346 ai, best ai, best, ai tool, tool, used, free
3 230 limit, messages, pro, message, limits, subscription, usage
4 194 claude, ai, claude ai, best, ve, just, like
6 158 image, images, photo, create, generate, pictures, picture
12 81 account, reason, disabled, got, lost, just, support
13 72 voice, feature, mode, read, talk, stops, audio, button
14 59 language, chinese, english, china, app, voice, answer
16 54 chats, history, chat, search, option, feature, delete
18 43 coding, documents, great, writing, content, interface
19 41 opus, llm, claude, pro, market, limits, years, model
Source: Authors.
The largest topics (0, 1, 2) are generic affective clusters with no concrete evaluative object. Smaller topics instead point to specific
features such as “voice,” “image,” “language,” and “chats,” or to service mechanisms such as “limit,” “subscription,” and
“account.”
We assigned each outlier to its nearest substantive topic by cosine similarity. The outliers are not wholly off topic. Their centroid
structure mixes affective and substantive evaluative tokens. The nearest criterion shares were C1 32.5 percent, C7 27.0 percent,
C6 12.2 percent, C3 10.2 percent, C4 8.2 percent, C5 6.2 percent, and C2 3.7 percent. Mean cosine similarity to the nearest centroid
was 0.435, below wi thin topic levels, so the outliers are genuinely more distant and more heterogeneous. That C7 is over
represented among them fits its status as the smallest substantive cluster.
The classification scheme from Section 2.5 produces the distribution in Table 4. To separate evaluative content from generic or
platform specific discourse, we placed all discovered topics into four broad categories and split the global-affect class into positive
and comparative sub types.

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
258
Table 4. Four-Class Topic Taxonomy.
Class Topics Documents
Substantive evaluative (used as criteria) 3, 6, 12, 13, 14, 15, 16, 18, 19 792
Global affect - positive 0, 1, 2, 9, 10 2,085
Global affect - comparative 11, 17 151
Platform identity 4, 5, 7, 8 668
Outlier/heterogeneous (HDBSCAN noise) −1 403
Total  4,099
Source: Authors.
Substantive content is 19.3 percent, global affect 54.6 percent, platform identity 16.3 percent, and outliers 9.8 percent. Th e
majority share of global affect is itself a finding about the register, and we hedge the claim accordingly: of the substantively
evaluative content, the salient dimensions are these seven.
Substantive topics merge into seven criteria:  C1 access and cost policy (T3, T19; 271 docs); C2 service continuity and accou nt
stability (T12, T15; 135 docs); C3 multimodal capability (T6; 158 docs); C4 conversational modality robustness (T13; 72 docs) ; C5
multilingual fidelity (T14; 59 docs); C6 conversation management (T16; 54 docs); C7 task domain breadth (T18; 43 docs). Aggregate
criterion mass is 792 documents across nine substantive topics. Definitions, representative excerpts, axiomatic audit, and inter
coder reliability are in Section 4.
Table 5 gives the platform level shares of each criterion’s documents. A share shows where the discourse of a criterion is
concentrated, not how well a platform performs.
Table 5. Platform Share of Substantive Criteria (Row-Normalized To 1.0).
Criterion ChatGPT Claude Copilot DeepSeek Gemini
C1 Access & cost
policy 0.037 0.738 0.066 0.122 0.037
C2 Service continuity
& account 0.015 0.852 0.081 0.044 0.007
C3 Multimodal
capability 0.203 0.070 0.291 0.291 0.146
C4 Conversational
modality robustness 0.042 0.458 0.097 0.319 0.083
C5 Multilingual fidelity 0.000 0.136 0.085 0.661 0.119
C6 Conversation
management 0.019 0.278 0.315 0.333 0.056
C7 Task-domain
breadth (provisional) 0.023 0.465 0.209 0.302 0.000
Source: Authors.
C1 and C2 lean hard toward Claude (73.8 and 85.2 percent). That fits how prominent Claude’s pro-tier and Opus session limits are
in the lexicon. C5 leans toward DeepSeek (66.1 percent), on the back of the default to Chinese complaint. C3 is more even , 15-30
percent across Copilot, DeepSeek, ChatGPT, and Gemini, with Claude lowest at 7.0 percent. C6 and C7 spread across Claude,
Copilot, and DeepSeek with no clear leader. Two things move these shares: reviewer attention and per platform clean N. The
distinction between platform concentrated supporting complaints and platform general abstracted criteria is in Section 4.
3.1. Sensitivity to Platform-Size Imbalance
Given the platform imbalance in the cleaned corpus (Claude 31.0%, DeepSeek 26.1%, Copilot 25.9%, Gemini 9.1%, ChatGPT 8.0%),
the shares reported in Table 5 could in principle be inflated by the disproportionate number of Claude users. Two complementary
checks rule this out. First, the per platform rate P(criterion | platform), which is independent of platform size, reaches 15.76% for
Claude on C1, compared with 3.06% for ChatGPT, 3.08% for DeepSeek, 2.70% for Gemini, and 1.70% for Copilot; on C2 it is 9.06%
for Claude against a maximum of 1.04% elsewhere. Claude users are thus roughly five times (C1) and nine times (C2) more likely
than users of other platforms to raise these issues. Second, a balanced subsample bootstrap (B = 1,000; n = 327 per platform,
corresponding to the smallest subsample) yields a Cl aude share of 0.598 for C1 (95% CI 0.525- 0.667) and 0.783 for C2 (95% CI
0.683-0.872). Both intervals lie well above the equal share null of 0.20, indicating that the concentration of C1 and C2 among
Claude users reflects a platform effect rather than a sa mpling artefact. The reproduction script is
code/15platformsubsample_sensitivity.py, with artefacts in outputs/sensitivity/.
Several criteria from expert derived rubrics did not surface as separate topics. Response accuracy, hallucination control, la tency,
and privacy appeared only diffusely or were absent from the surface lexicon, and enterprise integration and API issues were not

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
259
to be expected in a public mobile store corpus. The seven criteria are therefore a corpus bounded floor, to be widened during
expert validation.
On the same cleaned corpus, LDA (k = 20) produced an identifiable counterpart for each of the nine substantive BERTopic topic s.
Two converged strongly (Jaccard ≥ 0.15). The other seven overlapped weakly but not trivially (0.07-0.15). No substantive BERTopic
topic dropped out, which supports convergent validity.
As a within-window consistency check (not a test of long -term temporal drift), we split the corpus into two halves at the median
review date within the roughly ten-day collection window and re-ran the analysis on each half with the same settings. The earlier
half produced 24 topics and the later half 18. Six of the seven criteria (C1-C6) recovered in both halves. Only C7 failed to reappear
consistently, in line with the earlier checks that mark it as the most fragile criterion. As the time slice for the data to b e included
in the collection was tight, approximately 10 days prior to retrieval, it reflects the internal reliability of the topic structure over the
slice rather than any potential drift over time and is documented here as such.
4. Candidate Criterion Framework
Derived from BERTopic  over 4,099 cleaned English Google Play reviews across five generative AI mobile applications (ChatGPT,
Gemini, Claude, Copilot, DeepSeek). Table 6 comes first. It shows how the clustered documents fall across the four topic clas ses
from Section 3, before the criterion-level definitions follow.
Table 6. Share Of the Clustered Corpus by Topic Class.
Class Documents Share
Substantive evaluative (C1–C7) 792 19.3 %
Global affect (positive + comparative) 2,236 54.6 %
Platform-identity surface 668 16.3 %
HDBSCAN outliers (topic −1) 403 9.8 %
Total 4,099 100 %
Source: Authors.
4.1. The Candidate Criteria (C1–C7)
The seven criteria are presented in Table 7. (C7 was originally labelled productivity domain coverage but is renamed task- domain
breadth here in order to avoid overclaiming.) C7 constitutes the smallest cluster (43 documents, only two above the
min_cluster_size = 41 threshold), did not re -emerge in the brand masked analysis, and is the only criterion flagged by all four
fragility diagnostics. It is therefore retained as a candidate criterion for the framework but is not carried forward into the FUCOM-
RAFSI demon stration; whether it should be promoted to a full criterion, collapsed into a broader construct such as perceived
utility, or discarded altogether is left to an expert panel.
Table 7. Candidate Criteria C1–C7.
Criterion Topics n_docs Definition and representative excerpt
C1 Access & cost
policy T3, T19 271 Message limits, free-vs-paid caps, pro tier value, model tier pricing. “the only flaw is the limit hits just after one message sometimes.”
C2 Service
continuity &
account stability
T12, T15 135 Unexplained suspensions, phone verification failures. “My account was disabled for no reason.”
C3 Multimodal
capability T6 158 Image generation and image conditioned editing. “I would like a image creation and if I can add my own image.”
C4 Conversational
modality
robustness
T13 72 Voice mode quality: echo, audio loops, audio routing. “voice mode not having echo cancelation.”
C5 Multilingual
fidelity T14 59
Honoring declared language; avoiding unsolicited switching. “the
response is always in Chinese even when my default language is set to
English.”
C6 Conversation
management T16 54 History search, archive, deletion. “Please add the archived chats.”
C7 Task domain
breadth
(provisional)
T18 43 Range of high value tasks praised. “it is the best app for coding.”
Source: Authors.
Note. C7 is retained as a candidate criterion pending the decision of the expert panel (denoted F6 below) to promote, collapse, or
drop it. C7 was flagged across all four fragility diagnostics, namely brand masked replication, min_cluster_size sweep, encod er

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
260
substitution, and the within window consistency check. Its underlying cluster comprises 43 documents, only two above the
min_cluster_size = 41 threshold.
Global affect topics, platform identity clusters and HDBSCAN outliers were not abstracted into criteria. Criteria emphasized in
expert rubrics that did not emerge as distinct topics: response accuracy / factuality / hallucination control (mentions diffuse),
latency (cross cutting), privacy / data handling (absent from the surface lexicon), enterprise integration / API (mobile revi ewers
are individual end-users). Expert validation should treat C1-C7 as a floor and add expert anchored criteria.
4.2. Suitability For Uncertainty Representations
The candidate criteria differ in content, and also in the kind of uncertainty they seem to carry. Some are about whether a feature
is there at all. Others involve clashing judgments, blurry boundaries, or context bound linguistic calls. Earlier work has pulled these
apart, graded membership, hesitation, affirm and deny structures, through fuzzy, hesitant fuzzy, intuitionistic fuzzy, and rough set
approaches (Zadeh, 1965; Atanassov, 1986; Torra & Narukawa, 2009; Pawlak, 1982). Different representations may therefore fit
different criteria, as Table 8 lays out.
Table 8. Natural Uncertainty Representations for C1–C7.
Criterion Natural representation
C1 Crisp/interval on operational; linguistic on policy
C2 Intuitionistic-fuzzy or rough-set (vague boundary; affirm-and-deny pairs)
C3 Hesitant-fuzzy on modality quality; crisp on presence
C4 Intuitionistic-fuzzy (paired positive/negative reliability)
C5 Hesitant-fuzzy (multiple dimensions of fidelity)
C6 Crisp on feature presence; linguistic on ergonomics
C7 Hesitant-fuzzy (“high-value tasks” contested)
Source: Authors.
The mapping is conceptual, not operational. We mean it as a first read on suitability, one that guides later expert validatio n and
measurement design, not as a settled measurement structure.
4.3. Specificity of supporting complaints vs. generality of the criterion
Several criteria rest on topics concentrated in  one platform (C1 73.8 percent Claude, C2 85.2 percent Claude, C5 66.1 percent
DeepSeek). With one exception, this conflates the supporting complaints with the criterion itself. The complaint that DeepSeek
defaults to Chinese is platform concentrated, yet the underlying criterion, namely that an assistant should respond in the user's
chosen language, is platform general and corresponds to what any expert panel would formulate. The same holds for C1, where
Claude account discourse stands behind the platform general “access and cost should be tolerable and fair,” and for C3, where
image generation complaints spread across four platforms stand behind “reliable multimodal affordances.” We carry the criterion
forward. Topic concentration tells us where the discourse surfaced, not how portable the criterion is.
The exception is C2. We keep it because account stability belongs in any rubric for a cloud hosted assistant, but its support ing
topic is heavily specific to Claude account suspensions; this corpus does not establish the criterion outside the Claude case. Expert
validation should test whether C2 survives in a non Claude concentrated panel.
4.4. Inter-coder reliability of the topic-to-criterion abstraction
To keep the topic-to-criterion step from resting on one reader, two coders worked independently. Each sorted the 21 topics into
eleven categories: seven substantive criteria (C1 -C7), two global affect sub types, platform identity, and outlier. They agreed on
20 of 21, a raw rate of 95.2 percent. Krippendorff’s alpha (Krippendorff, 2019) for the full scheme was 0.947, well past the 0.80
mark usually read as strong agreement.
Collapsing the scheme to the central distinction, substantive vs. global -affect vs. other, raised Krippendorff’s alpha to 1.000, that
is, complete agreement. The one disagreement, on T10, lay only between two affect -related sub-types and left the substanti ve
criterion set (C1-C7) untouched.
High agreement does not remove every interpretive limit. The coders used the same framework, but another team might build
the codebook differently or draw the category boundaries elsewhere. The figures here speak to the consistency of the coding,
then, not to the existence of one uniquely correct reading.
5. Robustness Check: Brand-Masked Replication
One worry is that some clusters track brand strings, not evaluative substance. The primary run gives reason to check. Four of
twenty topics (T4 “claude”, T5 “copilot”, T7 “deepseek”, T8 “gemini”) drew over 51 percent of their mass from one platform, three
of them over 94 percent. If C1-C7 were lexical artefacts, masking the brand vocabulary would make them fall apart.

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
261
We replaced four classes of token in the cleaned 4,099 review corpus, case insensitively and at whole word boundaries. Table 9
gives the scheme.
Table 9. Brand-Masking Token Replacement Scheme.
Class Examples Replacement
Product names
“chatgpt”, “chat gpt”, “claude”,
“gemini”, “copilot”, “deepseek”, “deep
seek”, “bard”, “claude ai”
AITOOL
Parent companies “openai”, “anthropic”, “google”, “microsoft” AICORP
Model variants “opus”, “sonnet”, “haiku” AIVARIANT
Source: Authors.
Masking touched 1,121 of the 4,099 documents (27.4 percent). Everything else stayed fixed: the rest of the preprocessing, the
embedding model, the UMAP and HDBSCAN hyperparameters, the vectorizer configuration, and the random seed.
The masked run recovered 16 topics (vs. 20) with an outlier share of 14.1 percent (vs. 9.8). Defining a high dominance topic as one
whose modal platform supplies at least 90 percent of mass, the original run produced four. The masked run yields a single such
case (T9, an account suspension cluster that remains 94 per cent Claude driven by virtue of the substantive "account disabled"
narrative rather than the brand token). Clusters that owe their existence to a single repeated brand string dissolve once that string
is masked, whereas clusters anchored in substantive themes persist.For  each criterion C1-C7 we drew diagnostic terms from its
original top-keyword list. We then asked whether any masked topic carried at least two of them among its top 15 c -TF-IDF terms.
The recovery results are reported in Table 10.
Table 10. Criterion Recovery Under Brand Masking: Diagnostic Term Matches And Best -Matching Masked Topics.
Criterion Diagnostic matches Best-matching masked topic
C1 Access & cost policy 6 of 7 T7: pro, limit, limits, subscription, plan, paid, usage
C2 Service continuity & account stability 5 of 7 T15: number, phone, sign, trying, account, verify
C3 Multimodal capability 6 of 6 T4: image, images, photo, create, generate, pictures
C4 Conversational modality robustness 3 of 6 T8: voice, feature, mode, talk, read, stops
C5 Multilingual fidelity 3 of 5 T12: language, english, chinese, china, answer
C6 Conversation management 4 of 5 T10: chats, chat, history, option, search, delete
C7 Task-domain breadth 0 of 5 Not recovered as a distinct topic
Source: Authors.
Six of the seven criteria reappear, among them the highest -mass cases (C1, C3) and the strongest platform -asymmetry case (C2).
What anchors the substantive criteria is shared evaluative vocabulary, not brand mentions.
C7 (task-domain breadth) does not recover, and two readings fit. C7 was already the smallest cluster (43 documents in T18) and
sat just above the min_cluster_size = 41 floor, so small embedding perturbations push it under the threshold. Its diagnostic
vocabulary (“coding”, “documents”, “writing”) also overlaps with generic praise, so once brand identity stops anchoring a separate
cluster, task-breadth mentions are pulled into the large global -affect cluster. C7 is flagged. Expert validation should test whether
it is better treated as a sub-facet of a broader applied-utility dimension.
Masking splits two of the single -cluster criteria. C1 splits along an operational/policy axis (masked T6: in -session cap experience;
T7: evaluation of paid -tier policy). C3 splits along create versus refine (masked T4: image creation; T13: comparative and
modification framings). We treat these as interpretive hints for expert validation and do not change the primary criterion co unt
on the strength of a single robustness run.
The platform-identity clusters in the primary analysis were lexical-surface artefacts and do not undercut the substantive criterion
set. C1-C6 recover with high term overlap. C7 stays fragile and flagged.
6. Expert Validation and Downstream MCDM Illustration
This section connects criterion derivation to downstream MCDM use. It first sets the expert validation requirements and then
sketches a FUCOM -RAFSI illustration on hypothetical inputs. The illustration is intended to show procedural continuity between
the derived criterion set and downstream MCDM aggregation. It is not a benchmark of the platforms, and the weights and ranking
should not be read as validated importances or a platform verdict. This caveat applies to the entire section and to Table 11, and it
is not repeated at each downstream step.

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
262
6.1. Bridge From Criterion Derivation to Downstream Operationalization
The preceding sections produced a candidate framework, not a validated instrument. The seven dimensions (C1 -C7) came from
4,099 reviews and held up under four diagnostics, with abstraction at Krippendorff’s alpha = 0.947. The pipeline delivers a floor
on user surfaced dimensions. It does not deliver weights, scores, or a panel preferred alternative.
Downstream operationalization runs in three steps. An expert panel checks the criteria for relevance and non redundancy. Weights
are then elicited with FUCOM (Pamučar, Stević, & Sremac, 2018), the procedure with the lightest pairwise burden and full
consistency by construction. Alternatives are aggregated with RAFSI (Žižović, Pamučar, Albijanić, Chatterjee, & Pribićević, 2020),
whose standardized interval transformation removes rank reversal under amendment. The illustration here uses hypothetical
inputs loosely shaped by the asymmetries and platform level differences seen in the corpus. This constitutes a secondary
contribution, demonstrating how user-derived evaluative dimensions can be carried forward into a subsequent MCDM workflow.
Its point is procedural continuity, not a real  platform evaluation. The FUCOM -RAFSI configuration should be read as a workflow
demonstration of how UGC -derived candidate criteria can be operationalized downstream, not as a validated benchmark of the
five platforms.
6.2. Expert Panel Design
This expert panel is intended for the planned follow up study and was not convened in the present round, as ethics approval f or
the elicitation was still under institutional review and had not been granted in time. The panel would comprise six to ten
informants, drawn from academics working on MCDM or generative AI evaluation, doctoral students conducting language model
evaluation within decision analysis or HCI, and generative AI user developers with managerial or academic productivity roles,
thereby introducing methodological expertise, technical familiarity, and user experience into the triangulation. The proposed size
is consistent with Delphi and BWM criterion -validation practice on bounded objects, and no claim of statistical power is made.
Three tasks would be undertaken. Confirmation of the C1 -C7 criterion set, elicitation of FUCOM weights (ordering together with
n - 1 consecutive pair ratios), and optional scoring of the platforms on a five - to nine point ordinal scale.
6.3. FUCOM Weighting of the Candidate Criteria
We use FUCOM (Pamučar et al., 2018) to illustrate downstream weighting. AHP would require many pairwise comparisons.
FUCOM compares only consecutively ranked criteria, which lightens the elicitation load on experts while preserving weight
consistency.
In the illustrative scenario, a hypothetical managerial/academic -productivity expert ordered the criteria C2 > C1 > C4 > C7 > C6 >
C3 > C5. No formal panel was available. The authors (two academic researchers and two white collar users of generative AI),
working together in an informal setting and not in the role of the members of a professional body, decide upon the ranking jointly,
as a stand -in for a plausible managerial and productivity- oriented preference, loosely shaped by the corpus asymmetries and
usage patterns in the data. Consecutive preference ratios were then combined with geometric means before the FUCOM
computation. We make no claim to validated expert weights; the aim is only to show how the criteria could run inside a FUCOM -
based workflow.
Consecutive preference ratios were then set between adjacent criteria. The FUCOM procedure returned the normalized weight
vector in Table 11.
Table 11. FUCOM Weights Under an Illustrative Preference Ordering (Not Elicited From a Validated Expert Panel).
Rank Criterion w
1 C2 Service continuity and account stability 0.290
2 C1 Access and cost policy 0.241
3 C4 Conversational modality robustness 0.161
4 C7 Task-domain breadth 0.124
5 C6 Conversation management 0.088
6 C3 Multimodal capability 0.059
7 C5 Multilingual fidelity 0.037
 Sum 1.000
Source: Authors.
Note. The preference ordering was set by the author team for illustrative purposes only; no formal expert panel was convened.
Weights should be read as a demonstration of the FUCOM procedure, not as validated criterion importances.
Two criteria lead the weights: service continuity and account stability (C2) and access and cost policy (C1), which together take
53.1 percent of the total. That fits managerial and productivity priorities, where steady access and predictable conditions t end to
matter more than specialized features. Conversational modality robustness (C4) comes next at 16.1 percent. Multilingual fidel ity

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
263
(C5) takes the lowest illustrative weight. None of these values is empirically validated; they only show how the framework co uld
be operationalized downstream, and a different panel would likely order the priorities differently.
6.4. RAFSI as a Downstream Aggregation Step
As weights can be elicited (FUCOM in Sect. 6.3 as an example), RAFSI iovi et al., 2020 can be used to perform the aggregation step,
combining weights with a decision matrix to provide an ordered list of alternatives. The use of a standardized interval trans form
avoids rank reversal when a matrix amendment occurs, a common operation when platforms are introduced or removed later.
Appendix A shows worked RAFSI calculation steps on synthetic inputs. The resulting ranking is not published as a platform
assessment.
7. Discussion and Limitations
7.1. Implications
The pipeline's outputs speak to three audiences, each with its own consequence.
C1 (access and cost policy) and C2 (service continuity and account stability) constitute the two largest components of the
substantive complaint mass: user dissatisfaction on the mobile app layer is apparently less about capability and more about access
policy and account management. C1 and C2 are the two policy and procedural levers that would be expected to have the largest
impact on perceived quality of the mobile layer well before a question of capability has a chance to emerge.
The pipeline is better positioned as an upstream candidate generator preceding expert elicitation rather than as a substitute  for
it. Its function is to seed the initial criterion pool with a corpus anchored set of user-surfaced dimensions. This pool can then feed
an opening Delphi round or a BWM/SWARA-style validation study. The criterion set is thereby made less dependent on any single
expert panel.
Since criteria from the public mobile app UGC consistently fail to account for enterprise -side problems, such as data residency,
single sign-on (SSO) and audit trails, latency, hallucinations and privacy controls, the rubric should be thought of as supplem ental
to the rubric developed on the basis of internal expert opinion rather than as an independent selection tool. The ability to add the
expert guided questions must be required before using either as the basis for any decision to operate any of these types of services.
7.2. Limitations
Corpus boundary conditions. The corpus of this study is bounded by the publicly visible surface of Google Play Store reviews,
captured at a single extraction date (12 May 2026, UTC) and reflecting an individual user's mobile view of the US storefront.
Properties specific to enterprise deployments, such as data residency, API performance, SSO, audit logging, and citation practices,
fall outside this window. External validity is therefore restricted to the deployment environments currently accessible to consumer
users; self hosted or open source deployments, as well as app store ecosystems outside the US, would plausibly yield criterion
vectors with a substantially different structure. The production corpus is also comparatively imbalanced (Claude 1,269, DeepSeek
1,071, Copilot 1,061, Gemini 371,  ChatGPT 327). However, the per platform balanced subsample bootstrap reported in Section
3.5 shifts Claude's share of C1 and C2 by no more than 14 percentage points, with Claude still dominant, indicating that the
reported concentration is not an artefact of the sampling regime.
Statistical fragility of small criteria. Three criteria rest on low -proportion clusters, namely C5 (59 documents, ~1.4%), C6 (54
documents, ~1.3%), and C7 (43 documents, ~1.0%). These proportions are density -clustering diagnostics rather than concerns -
per-user estimates. They indicate that the concern does not form a dense, single cluster, not that it is unimportant to users. Since
HDBSCAN operates on density and these clusters sit close to the min_cluster_size = 41 threshold, the sensitivity scan eliminates
C7 at min_cluster_size = 60 and both C6 and C7 at 80. C5 is further constrained by the restriction of the corpus to English-language
reviews. These three criteria should accordingly be read as tentative rath er than confirmed candidates.
Snapshot horizon. Once collapsed, platform level distributions are perishable rather than stable estimates. A sound stability test
would replicate the identical google play scraper protocol (the same five applications, country = us, lang = en, NEWEST and
MOST_RELEVANT sweep s, and a 2,000 review cap per platform) at three, six, and twelve months. Stability would be
operationalised as the Jaccard overlap between the diagnostic term vectors of each decision object across snapshots, with criteria
falling below a pre registered  threshold (for instance, 0.30) returned to arbitration. Such a design would also yield an initial
empirical estimate of the time scale over which criterion structures shift for decision objects that are updated on an approximately
quarterly basis.
Scope: candidate framework, not validated instrument. What this study delivers is a draft criterion set rather than a validated
MCDM instrument. Expert validation remains outstanding and is indispensable for the weaker, less salient dimensions, namely
accuracy, latency, privacy, and enterprise integration. The follow up expert panel outlined in Section 6.2 will reconcile the upper

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
264
bounds derived from user -generated content with the lower bounds supplied by experts, elicit FUCOM weights, and generate
alternative scores across the documented criterion set. The identification of a "winner" belongs to that study rather than to  the
present one.
Conclusion
This paper has proposed an NLP -supported procedure for criterion derivation, understood as one stage within a multi stage
decision making process addressed to rapidly evolving decision objects. The procedure combines Sentence BERT embeddings,
UMAP, HDBSCAN, and BERTopic with a documented process of thematic abstraction that elevates data derived topics into higher
level evaluative criteria. It was applied to 4,099 pre processed Google Play reviews of five generative AI mobile assistants, yielding
a candidate set of six robust criteria (C1- C6) together with one provisional candidate, C7 (task domain breadth), which is retained
in the criterion set but excluded from the FUCOM - RAFSI demonstration. The six robust criteria are access and pricing policy;
continuity of service experience and account stability; multimodal functionality; robustness of the conversational modality;
multilingual fidelity; and conversation control.
The abstraction step was replicated at Krippendorff's alpha = 0.947, and the robust criteria withstood a brand masked replication
(six of seven recovered, with C7 flagged), a full hyperparameter sweep, encoder substitution, an alternative temporal partiti on,
the balanced subsample sensitivity test reported in Section 3.5, and a convergent validity baseline based on LDA.
The paper is deliberately bounded in what it claims. No verdict on the platforms is issued. The FUCOM illustration in Section 6,
together with the RAFSI worked example in Appendix A, is configurational and contingent on a hypothetical managerial weight
vector and decision matrix, and this  caveat is anchored once in Section 6 and once at Table 11 rather than repeated throughout.
Criteria that are absent from the mobile app register, such as response accuracy, factuality, hallucination control, latency,  and
data-handling privacy, must instead be introduced through expert and literature elicitation at the validation stage.
The next step is an expert validation follow up. A panel of six to ten informants would reconcile the UGC derived floor with expert
anchored criteria, elicit FUCOM weights, and score the alternatives under documented heterogeneity. That study, not this one ,
will speak to platform preference.
This research article has been licensed with Creative Commons Attribution -  Non-Commercial 4.0 International
License. Bu araştırma makalesi, Creative Commons Atıf - Gayri Ticari 4.0 Uluslararası Lisansı ile lisanslanmıştır.
Author Contributions
The author has not declared any other contributors.
Acknowledgments
The author(s) did not provide acknowledgment.
Funding and Support
The author(s) did not report any funding or support information.
Conflict of Interests
The author(s) did not report any conflict of interest.
Ethics Statement
The author(s) did not report ethical committee approval as the research content does not require.
References
An, Y., Oh, H., & Lee, J. (2023). Marketing insights from reviews using topic modeling with BERTopic and deep clustering network.
Applied Sciences, 13(16), 9443. https://doi.org/10.3390/app13169443
Atanassov, K. T. (1986). Intuitionistic fuzzy sets. Fuzzy Sets and Systems, 20(1), 87– 96. https://doi.org/10.1016/S0165-
0114(86)80034-3
Blei, D. M., Ng, A. Y., & Jordan, M. I. (2003). Latent Dirichlet allocation. Journal of Machine Learning Research, 3, 993 –1022.
Brynjolfsson, E., Li, D., & Raymond, L. R. (2025). Generative AI at work. The Quarterly Journal of Economics, 140(2), 889– 942.
https://doi.org/10.1093/qje/qjae044
Dalkey, N., & Helmer, O. (1963). An experimental application of the Delphi method to the use of experts. Management Science,
9(3), 458–467. https://doi.org/10.1287/mnsc.9.3.458
Dell’Acqua, F., McFowland III, E., Mollick, E. R., Lifshitz -Assaf, H., Kellogg, K., Rajendran, S., Krayer, L., Candelon, F., & Lakhani, K.
R. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge
worker productivity and quality (Harvard Business School Working Paper No. 24 -013).
https://doi.org/10.2139/ssrn.4573321

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
265
Grootendorst, M. (2022). BERTopic: Neural topic modeling with a class -based TF-IDF procedure. arXiv preprint arXiv:2203.05794.
https://doi.org/10.48550/arXiv.2203.05794
Guo, Y., Barnes, S. J., & Jia, Q. (2017). Mining meaning from online ratings and reviews: Tourist satisfaction analysis using latent
Dirichlet allocation. Tourism Management, 59, 467–483. https://doi.org/10.1016/j.tourman.2016.09.009
Hendrycks, D., Burns, C., Basart, S., Zou, A., Mazeika, M., Song, D., & Steinhardt, J. (2021). Measuring massive multitask la nguage
understanding. In Proceedings of the International Conference on Learning Representations (ICLR).
https://doi.org/10.48550/arXiv.2009.03300
Keeney, R. L. (1992). Value-Focused Thinking: A Path to Creative Decisionmaking. Harvard University Press.
Keeney, R. L. (1996). Value -focused thinking: Identifying decision opportunities and creating alternatives. European Journal of
Operational Research, 92(3), 537–549. https://doi.org/10.1016/0377-2217(96)00004-5
Keshavarz Ghorabaee, M., Zavadskas, E. K., Olfat, L., & Turskis, Z. (2015). Multi-criteria inventory classification using a new method
of Evaluation Based on Distance from Average Solution (EDAS). Informatica, 26(3), 435 –451.
https://doi.org/10.15388/Informatica.2015.57
Krippendorff, K. (2019). Content Analysis: An Introduction to Its Methodology (4th ed.). SAGE Publications.
https://doi.org/10.4135/9781071878781
Liang, P., Bommasani, R., Lee, T., Tsipras, D., Soylu, D., Yasunaga, M., Zhang, Y., Narayanan, D., Wu, Y., Kumar, A., et al. (2023).
Holistic evaluation of language models. Transactions on Machine Learning Research.
https://doi.org/10.48550/arXiv.2211.09110
Linstone, H. A., & Turoff, M. (Eds.). (1975). The Delphi Method: Techniques and Applications. Addison -Wesley.
Mi, X., Tang, M., Liao, H., Shen, W., & Lev, B. (2019). The state-of-the-art survey on integrations and applications of the best worst
m e t h o d  i n  d e c i s i o n  m a k i n g :  W h y ,  w h a t ,  w h a t  f o r  a n d  w h a t ’ s  n e x t ?  O m e g a ,  8 7 ,  2 0 5–225.
https://doi.org/10.1016/j.omega.2019.01.009
Noy, S., & Zhang, W. (2023). Experimental evidence on the productivity effects of generative artificial intelligence. Science ,
381(6654), 187–192. https://doi.org/10.1126/science.adh2586
Pamučar, D., & Ćirović, G. (2015). The selection of transport and handling resources in logistics centers using Multi -Attributive
Border Approximation Area Comparison (MABAC). Expert Systems with Applications, 42(6), 3016 –3028.
https://doi.org/10.1016/j.eswa.2014.11.057
Pamučar, D., Stević, Ž., & Sremac, S. (2018). A new model for determining weight coefficients of criteria in MCDM models: Ful l
Consistency Method (FUCOM). Symmetry, 10(9), 393. https://doi.org/10.3390/sym10090393
Pawlak, Z. (1982). Rough sets. International Journal of Computer & Information Sciences, 11(5), 341– 356.
https://doi.org/10.1007/BF01001956
Reimers, N., & Gurevych, I. (2019). Sentence -BERT: Sentence embeddings using Siamese BERT -networks. In Proceedings of the
2019 Conference on Empirical Methods in Natural Language Processing (EMNLP) (pp. 3982– 3992).
https://doi.org/10.18653/v1/D19-1410
Rezaei, J. (2015). Best -worst multi -criteria decision -making method. Omega, 53, 49– 57.
https://doi.org/10.1016/j.omega.2014.11.009
Rezaei, J. (2016). Best -worst multi-criteria decision -making method: Some properties and a linear  model. Omega, 64, 126– 130.
https://doi.org/10.1016/j.omega.2015.12.001
Röder, M., Both, A., & Hinneburg, A. (2015). Exploring the space of topic coherence measures. In Proceedings of the Eighth AC M
International Conference on Web Search and Data Mining (WSDM ’15) (pp. 399 –408).
https://doi.org/10.1145/2684822.2685324
Saaty, T. L. (1980). The Analytic Hierarchy Process. McGraw-Hill.
Saaty, T. L. (2008). Decision making with the analytic hierarchy process. International Journal of Services Sciences , 1(1), 83 –98.
https://doi.org/10.1504/IJSSCI.2008.017590
Sharma, P., & Sharma, A. (2019). Ranking hotels using aspect ratings based sentiment classification and interval -valued
neutrosophic TOPSIS. International Journal of System Assurance Engineering and Management, 10(5), 973 –983.
https://doi.org/10.1007/s13198-019-00827-4
Stević, Ž., Pamučar, D., Puška, A., & Chatterjee, P. (2020). Sustainable supplier selection in healthcare industries using a new MCDM
method: Measurement of alternatives and ranking according to COmpromise solution (MARCOS). Computers & Industrial
Engineering, 140, 106231. https://doi.org/10.1016/j.cie.2019.106231
Strzelecki, A. (2024). To use or not to use ChatGPT in higher education? A study of students’ acceptance and use of technolog y.

KOCATEPEİİBFD 28(Special Issue)
 Aydın (2026).
266
Interactive Learning Environments, 32(9), 5142–5155. https://doi.org/10.1080/10494820.2023.2209881
Torra, V., & Narukawa, Y. (2009). On hesitant fuzzy sets and decision. In 2009 IEEE International Conference on Fuzzy Systems (pp.
1–8). IEEE. https://doi.org/10.1109/FUZZY.2009.5276884
Zadeh, L. A. (1965). Fuzzy sets. Information and Control, 8(3), 338 –353. https://doi.org/10.1016/S0019-9958(65)90241-X
Zavadskas, E. K., Turskis, Z., Antucheviciene, J., & Zakarevicius, A. (2012). Optimization of weighted aggregated sum product
assessment. Elektronika ir Elektrotechnika, 122(6), 3–6. https://doi.org/10.5755/j01.eee.122.6.1810
Žižović, M., Pamučar, D., Albijanić, M., Chatterjee, P., & Pribićević, I. (2020). Eliminating rank reversal  problem using a new multi-
attribute model — The RAFSI method. Mathematics, 8(6), 1015. https://doi.org/10.3390/math8061015
