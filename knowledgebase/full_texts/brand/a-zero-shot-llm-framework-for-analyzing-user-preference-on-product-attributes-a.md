---
title: 'A zero-shot LLM framework for analyzing user preference on product attributes: a case study of
  smartwatch reviews'
url: https://doi.org/10.1038/s41598-026-57281-z
category: brand
subcategory: framework
date: 2026-10
venue: Scientific Reports
authors:
- Imam Adi Nata
- Nila Nurlina
- Muhammad Rifqi Maarif
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-57281-z_reference.pdf
pages: 21
chars: 77902
fetched_at: '2026-11-08T19:26:04+00:00'
kb_version: 1
---

# A zero-shot LLM framework for analyzing user preference on product attributes: a case study of smartwatch reviews

ARTICLE | Article in Press
Scientific Reports https://doi.org/10.1038/s41598-026-57281-z
Scientific Reports
This Article in Press is shared early to give you faster access to new research. It is citable and carries a permanent DOI.
The final edited version will replace it automatically.
A zero-shot LLM framework for analyzing user
preference on product attributes: a case study of
smartwatch reviews
Imam Adi Nata · Nila Nurlina · Muhammad Rifqi Maarif · Norma Latif Fitriyani ·
Yeonghyeon Gu · Muhammad Syafrudin
Received: 17 September 2025 / Accepted: 5 June 2026
© The Author(s) 2026
Abstract
The rise of zero-shot learning through Large Language Models (LLMs) opens new opportunities for analyz -
ing consumer feedback without relying on annotated data. This study proposes a zero-shot framework to
uncover user preferences on product attributes, using 12,900 Amazon smartwatch reviews as a case study.
The framework integrates semantic keyword extraction, LLM-based attribute classification, sentiment analysis,
and Importance–Performance Analysis (IPA) to convert unstructured textual reviews into structured consumer
preference insights. Validation against human annotations demonstrates strong sentiment classification perfor -
mance, achieving an accuracy of 0.88 and a macro-averaged F1-score of 0.86, confirming the reliability of the
zero-shot approach. The results reveal that Design & Comfort, Connectivity, and Health Monitoring Features
are the most important and positively perceived smartwatch attributes, while Power & Battery Management
remains a key area of consumer dissatisfaction. Brand-level analysis further shows that major brands such as
Apple, Samsung, and Garmin dominate consumer attention but exhibit only moderate differentiation in senti -
ment performance, indicating opportunities for strategic improvement. Methodologically, the study demon -
strates that zero-shot LLM inference can reliably extract and organize consumer preference structures without
requiring labeled data. The findings contribute to consumer analytics and computational linguistics by demon -
strating how zero-shot frameworks enable scalable, adaptive preference modeling, providing actionable insights
for product development and competitive positioning.
Keywords Zero-shot learning · Large language models (LLMs) · User preference analysis · Product
attribute evaluation · Online product reviews
Introduction
Consumer preferences are widely recognized as a critical driver of product success and innovation, shaping
both design outcomes and market performance. Firms that systematically capture and integrate consumer needs,
tastes, and willingness to pay into product development often achieve higher rates of successful innovation and

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
improved financial outcomes across sectors such as food, fashion, and technology 1,2. Preferences, however, are
dynamic and evolve with shifting market contexts, requiring continuous monitoring and adaptive product strate-
gies. Iterative, consumer-centric innovation practices that leverage real-time data can extend product life cycles
and ensure responsiveness to changing demands3. Moreover, consumer characteristics—such as innovativeness,
buyer sophistication, and global or local identity—moderate how users evaluate new offerings, amplifying the
relationship between firm R&D and innovation performance 4,5. Finally, understanding market segmentation,
including innovators, early adopters, and risk-averse groups, enables firms to target communication strategies
that accelerate adoption and reduce market failure risks6,7.
In the digital marketplace, online product reviews have emerged as a significant influence on consumer pur -
chasing decisions, serving as both social proof and a mechanism for mitigating perceived risk. Reviews enhance
trust and credibility when they are numerous, authentic, and relevant, significantly increasing purchase likeli -
hood, while suspicion of fake or manipulated reviews undermines confidence8,9. The sentiment valence expressed
in reviews plays a decisive role: positive reviews signal product quality and raise purchase intentions, whereas
negative reviews highlighting flaws or service failures tend to reduce purchase probability, often more strongly
than positive reviews increase it 10,11,12. Beyond sentiment, review volume and visibility amplify persuasion
effects, especially when combined with features such as “most helpful” tags or multimedia content13. The exper-
tise, clarity, and style of reviewers also shape credibility, with literal reviews being more persuasive for search
goods and figurative styles more effective for experiential products14.
To translate consumer reviews into actionable insights, researchers have developed a range of computational
and statistical approaches to identify and quantify preferences for product attributes. Aspect-based sentiment
analysis (ABSA) is widely applied to extract attributes and assess associated sentiment, using methods ranging
from rule-based techniques to advanced models such as BERT, ALBERT, and attention-based LSTMs 15,16,17.
Complementary NLP methods, including topic modeling, TF-IDF, and word embeddings, further support the
clustering of attributes and mapping of consumer opinions 18,19. Econometric approaches, such as modified
ordered choice models and the 2-additive Choquet integral, allow quantification of attribute importance and inter-
action effects16,20. In advance, multi-attribute decision-making (MADM) techniques like AHP and the best-worst
method provide structured weighting and aggregation of preferences19,21. On the other hand, hybrid frameworks
integrate these methods—combining, for instance, fake review detection with hierarchical attribute sentiment
analysis—to produce more robust insights22.
While existing computational methods have advanced the analysis of consumer preferences from online
reviews, significant limitations remain in capturing the full complexity of product evaluations. Feature extraction
approaches often emphasize frequently mentioned or pre-specified aspects, which risks omitting less common but
influential attributes; reliance on term frequency and over-segmentation of multi-word features can also distort
results23,24. Sentiment analysis techniques face similar challenges, particularly in detecting neutral, hesitant, or
context-dependent expressions, creating a gap between sentiment orientation and actual demand recognition25,26.
A further challenge lies in the diagnostic–predictive tradeoff: while neural networks excel at predictive tasks,
they often lack interpretability, whereas topic models provide explanatory insights but weaker predictive power27.
The methodological limitations identified in prior approaches highlight the need for more flexible, scalable,
and context-aware solutions to analyze consumer preferences. Large Language Models (LLMs) address this gap
by enabling zero-shot learning through prompt-based inference28,29. Pre-trained on massive and diverse corpora,
models such as GPT-3 and FLAN can generalize to unseen tasks without requiring domain-specific labeled data30.
By formulating a natural language prompt (e.g., “Classify the sentiment of this review”), the model leverages its
internal knowledge to generate task-relevant outputs directly. Advances such as instruction tuning and prompt
engineering further improve zero-shot performance, enabling LLMs to execute a wide range of tasks—including
sentiment analysis, attribute classification, and summarization—without retraining 31,32. This capability directly
overcomes the rigidity of earlier methods by providing an adaptive mechanism to capture evolving consumer
discourse.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
Compared to supervised machine learning, zero-shot LLMs offer clear advantages for analyzing unstructured
consumer feedback. First, they eliminate the need for labeled data, reducing dependency on costly and time-
intensive annotation, and thus can be rapidly applied to emerging product categories 29,30,33. Second, their task
flexibility allows adaptation to different analytical goals—such as sentiment classification, topic extraction, or
attribute-based summarization—simply by adjusting the prompt, whereas supervised models require retraining
for each new task30,32. Third, LLMs demonstrate superior generalization by handling unseen attributes or senti -
ment classes, enhancing robustness in dynamic consumer environments 28,34. Finally, their scalability enables
immediate deployment across large, unstructured datasets, offering faster, ore comprehensive insights for deci -
sion-making29,33. Together, these advantages position zero-shot LLMs as a transformative approach, addressing
the limitations of prior methods and advancing the systematic study of consumer preferences in digital markets.
Building on these advantages, this study proposes a zero-shot LLM framework for analyzing user preferences
for product attributes, using Amazon smartwatch reviews as the empirical case. The framework integrates key -
word extraction, clustering, review categorization, and sentiment-informed preference analysis into a coherent
pipeline, eliminating reliance on annotated datasets and enabling scalable, attribute-level insights. By applying
LLM-driven zero-shot prompting, the method captures both fine-grained product attribute evaluations (e.g., con-
nectivity, display technology, usability) and broader brand positioning within the competitive landscape of wear-
able technologies. The contributions are threefold: methodologically, the framework demonstrates how multiple
NLP tasks can be unified through zero-shot inference; theoretically, it extends research on consumer analytics by
uncovering latent structures in product evaluations; and managerially, it provides actionable insights for produc-
ers and retailers by linking attribute-level preferences to brand performance. This positions the smartwatch case
study as both a validation of the framework and an illustration of its broader applicability.
Materials and methods
The research design of this study follows a structured workflow, as shown in Fig. 1, integrating data collection,
preprocessing, and sequential analytical stages to extract user preferences for smartwatch product attributes. At
a glance, the analytical pipeline proceeds through four main components: (1) keyword extraction and clustering
to identify salient product attributes, (2) zero-shot classification and sentiment-informed preference mapping
using LLMs, and (3) aggregation into attribute- and brand-level insights supported by importance–performance
analysis.
Data acquisition and preprocessing
The workflow begins by collecting 12,900 + Amazon reviews from July to December 2024 using the Amazon
Customer Feedback API. The dataset was then divided into two processing streams: one underwent standard text
preprocessing for keyword extraction, and the other was retained in its raw form to preserve contextual nuance
for zero-shot LLM tasks. For keyword extraction, we applied standard text preprocessing (lowercasing, punctua-
tion removal, tokenization, stopword removal, lemmatization) to reduce lexical noise and improve term salience.
For zero-shot LLM tasks, we intentionally kept raw texts to preserve discourse cues and pragmatics leveraged by
instruction-tuned models in prompt-based inference35,36.
Keyword extraction and attribute identification
The initial phase of the analysis was dedicated to extracting candidate product attributes from the smartwatch
review corpus. To achieve this, we employed KeyBERT, a BERT-embedding-based keyword extraction algo -
rithm that measures cosine similarity between document embeddings and candidate n-grams 37. This approach
was selected over frequency-based techniques (e.g., TF-IDF) and graph-based algorithms (e.g., TextRank), as it

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
is more effective at capturing contextual semantics in consumer-generated text38. The procedure of KeyBERT can
be described in the following steps:
 ● Document embedding generation Each review (or aggregated subset of reviews) was converted into a dense
semantic vector using a transformer-based model such as Sentence-BERT39. This document is embedded in the
later formula 1, denoted as 𝑣𝑣𝑑𝑑, serves as the semantic representation of the entire review text.
 ● Candidate term generation Candidate keywords are generated from the text using n-gram ranges. In this study,
we specified (1,2), producing both unigrams (e.g., battery, connectivity) and bigrams (e.g., battery life, display
quality). Stopwords, punctuation, and irrelevant tokens were removed during preprocessing to avoid spurious
candidates.
 ● Candidate embedding generation  On the formula 1, each candidate n-gram 𝑘𝑘𝑖𝑖 is independently embedded
into the same semantic space as the document, producing a vector 𝑣𝑣𝑘𝑘. This ensures comparability between
document-level and term-level representations.
 ● Relevance scoring Instead of relying on raw frequency or statistical weighting, relevance is determined by the
semantic similarity between 𝑣𝑣𝑑𝑑 and 𝑣𝑣𝑘𝑘. This step ensures that even low-frequency, yet semantically important
terms are captured, addressing a known limitation of frequency-based methods in review mining38.
Fig. 1 Research proposed method workflow.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
 ● Ranking and selection with MMR To refine the final keyword list, Maximal Marginal Relevance (MMR) was
applied. MMR balances two goals: (i) selecting terms that are highly relevant to the document, and (ii) avoid-
ing redundancy by penalizing terms similar to already-selected ones. The optimization is defined in formula
140.
 𝑘𝑘∗ = arg𝑚𝑚𝑚𝑚𝑚𝑚𝑘𝑘𝑖𝑖 ∈ 𝐶𝐶𝐶 𝐶𝐶 [𝜆𝜆 • 𝑠𝑠𝑠𝑠 𝑚𝑚 (𝑣𝑣𝑑𝑑,𝑣𝑣 𝑘𝑘) − (1− 𝜆𝜆 ) • max𝑠𝑠𝑠𝑠𝑚𝑚𝑘𝑘𝑗𝑗 ∈ 𝐶𝐶 (𝑣𝑣𝑘𝑘𝑖𝑖 ,𝑣𝑣 𝑘𝑘𝑗𝑗 )] (1)
Where 𝐶𝐶 is the candidate pool, 𝑆𝑆 is the set of already-selected keywords, and 𝜆𝜆  controls the trade-off between
relevance and diversity. A higher  favors document-relevant terms (risking redundancy), while a lower  increases
diversity (risking less relevance). In our implementation, we set  = 0.7, following prior studies showing this pro-
vides a balanced trade-off in consumer reviews38.
The output of KeyBERT + MMR was a pool of candidate smartwatch attributes that balanced contextual impor-
tance with representational diversity. For example, highly frequent terms, such as battery life, were extracted
alongside less frequent but semantically relevant terms, like strap comfort. To enhance reliability, the candidate
list was manually screened by two independent reviewers, who removed irrelevant items and consolidated over-
lapping expressions. This curated attribute pool was then forwarded to the zero-shot LLM stage for semantic
clustering and categorization.
Zero-shot classification & clustering
Following the keyword extraction phase, candidate terms were grouped into abstract attribute categories using
a prompt-based zero-shot approach with large language models (LLMs). Instead of relying on unsupervised
clustering algorithms, we provided LLMs with simple natural language prompts. The models then assigned each
extracted keyword to a semantically appropriate category. This approach leverages LLMs’ ability to perform
semantic generalization without requiring task-specific training data. Multiple models—including proprietary
and open-source LLMs—were compared to evaluate stability and coherence of the categorization.
To ensure reproducibility and transparency, zero-shot classification was implemented using structured natural-
language prompts designed to guide the language model’s semantic inference. For keyword categorization, the
LLM was provided with a list of extracted candidate keywords and instructed to group them into semantically
coherent attribute categories relevant to smartwatch products. An example prompt used for this task is as fol -
lows: “You are an expert in wearable technology and consumer electronics. Given the following list of keywords
extracted from smartwatch reviews , classify each keyword into a meaningful product attribute category. Use
clear and concise category names that represent functional or experiential aspects of smartwatches. Examples of
categories include Health Monitoring Features, Connectivity, Display Technology, etc. Assign each keyword to
the most appropriate category based on its semantic meaning. Keywords: [battery, strap, amoled, gps, bluetooth,
heart rate , charger, waterproof, notifications , band , cellular , screen, sensors , steps , customization , software,
accuracy, solar, wristband, tracking]. Return the output as a structured list of categories and their correspond -
ing keywords”.
The aforementioned prompt enables the model to perform semantic grouping based on contextual understand-
ing rather than surface-level lexical similarity. The resulting attribute categories were reviewed for consistency
and aligned with domain-relevant product evaluation dimensions, as presented in Table 3. Once attribute catego-
ries were established, zero-shot classification was used to assign each review to its most relevant category. The
classification was performed using the Hugging Face zero-shot pipeline with the facebook/bart-large-mnli model,
where the review text was provided as the input sequence and the attribute categories were used as candidate
labels.
Once the abstract categories were finalized, they were operationalized for large-scale review analysis using
zero-shot text classification. We employed Hugging Face’s pipeline (“zero-shot-classification”) with the face -
book/bart-large-mnli model. This widely used natural language inference model maps input text to candidate

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
labels. Each review was assigned to one or more categories by providing the review text as the input sequence and
the identified abstract categories as candidate labels. The model outputs a probability distribution over labels, and
the label with the highest probability was selected as the review’s attribute classification. This setup ensured that
consumer feedback was systematically organized under consistent, semantically validated attribute categories
without requiring manual annotation or supervised training.
The facebook/bart-large-mnli model was selected for its strong performance on natural language inference
tasks, which form the foundation of zero-shot classification. This model has been widely used in prior studies
for zero-shot text classification because it is trained on the Multi-Genre Natural Language Inference (MNLI)
dataset, enabling it to evaluate semantic entailment relationships between input text and candidate labels. Previ-
ous research has demonstrated that NLI-based models such as BART-MNLI achieve competitive performance
in zero-shot sentiment classification and topic classification tasks, making them suitable for applications where
labeled training data is unavailable 30,34,42. Its robustness, generalization capability, and availability within the
Hugging Face framework make it an appropriate choice for scalable consumer review analysis.
Sentiment analysis and evaluation
To quantify consumer evaluations of smartwatch attributes, sentiment analysis was conducted on the review
corpus using a zero-shot classification approach. Specifically, we employed the Hugging Face pipeline(“zero-
shot-classification”) with the pre-trained facebook/bart-large-mnli model, which is based on natural language
inference (NLI). In this setup, each review text was provided as the input sequence, and sentiment labels (“posi-
tive”, “neutral”, and “negative”) were defined as candidate classes. The model estimates the probability that the
input text entails each sentiment label, and assigns the label with the highest probability as the review’s senti -
ment polarity. This zero-shot approach enables sentiment classification without requiring task-specific training
data, leveraging the general semantic reasoning capability of large pre-trained language models. To facilitate
quantitative analysis, sentiment labels were converted to numerical polarity scores: positive = 1, neutral = 0, and
negative = − 1. These polarity scores were subsequently aggregated at the attribute level to compute performance
scores used in the Importance–Performance Analysis.
To assess the reliability of the sentiment classification process, a validation procedure was conducted using
human annotation as the reference standard. A random sample of 200 reviews was selected from the dataset
to ensure representative coverage of different products, brands, and sentiment expressions. Two independent
annotators manually labeled each review as positive, neutral, or negative based on its overall evaluative tone.
Annotation guidelines were established to ensure consistency, focusing on the reviewer’s explicit or implicit sat-
isfaction or dissatisfaction with the product. Disagreements between annotators were resolved through discussion
to establish a final consensus label, which served as the ground truth for evaluation. The automated sentiment
classification performance was evaluated by comparing model predictions to human-annotated labels using stan-
dard evaluation metrics, including accuracy, precision, recall, and F1-score.
Analytical framework
The analytical framework of this study is organized at two levels: attribute-level evaluation and brand-level posi-
tioning. At the attribute level, consumer preferences were derived by aggregating sentiment classifications over
reviews assigned to each attribute category (e.g., battery life, connectivity, comfort). This follows the principles
of aspect-based sentiment analysis (ABSA), which links sentiment polarity to specific product features, providing
fine-grained insights into consumer evaluations41,42.
Afterward, we employ Importance–Performance Analysis (IPA)—originally introduced by43—as a two-dimen-
sional mapping of attribute importance and performance. In a more recent application [44] extended IPA by vali-
dating findings using both online reviews and maintenance records, underscoring its relevance in multi-source

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
data contexts. The IPA diagram, as shown in Fig. 2, maps attributes into four quadrants based on their calculated
importance and performance, and categorizes them into the following criteria.
 ● Keep up the good work (high importance, high performance)—key strengths.
 ● Concentrate here (high importance, low performance) — priority weaknesses.
 ● Low priority (low importance, low performance) — limited impact.
 ● Possible overkill (low importance, high performance) — areas of over-investment.
To quantify consumer evaluations, we calculated performance and importance scores for each attribute. The per-
formance score represents consumer preference strength, operationalized as the mean sentiment polarity across
reviews mapped to the attribute 𝛼𝛼  on the following formula 2. In formula 2, 𝑆𝑆𝑖𝑖 ∈ { − 1,0,0+1 }  denotes the senti-
ment polarity score of the review 𝑖𝑖 and 𝑁𝑁𝛼𝛼  is the number of reviews mentioning the attribute 𝛼𝛼 . The score ranges
from − 1 (entirely negative) to + 1 (entirely positive), and can be normalized to [0,1] for visualization.

𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃𝑃 (𝛼𝛼 ) = 1 𝑁𝑁𝛼𝛼 ∑ 𝑁𝑁𝛼𝛼 𝑖𝑖𝑖𝑖 𝑆𝑆𝑖𝑖 (2)
The importance score, as calculated using formula 3, reflects the salience of attribute  in consumer discourse,
measured by its relative frequency of occurrence. In this formula, 𝑁𝑁𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡 is the total number of reviews in the data-
set. The attributes that are mentioned more frequently are considered more important to customers.

𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼𝐼 (𝛼𝛼 ) = 𝑁𝑁𝛼𝛼
𝑁𝑁𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡𝑡  (3)
Results
Keyword extraction and attribute identification
Table 1 presents the progressive steps in keyword extraction. When using KeyBERT without applying a thresh -
old, the algorithm returned an excessively large set of 17,736 candidate terms, many of which were redundant,
overly generic, or irrelevant. This highlights a common limitation of unsupervised embedding-based extraction.
Fig. 2 Diagram of importance–performance analysis (IPA)
used to evaluate product attributes.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
While sensitive to semantic variety, it tends to produce noisy outputs when left unconstrained. To address this
issue, a similarity score threshold was introduced. By retaining only terms with a KeyBERT score of 0.5 or
higher, the candidate pool was narrowed to 240 terms. Although this reduction improved manageability, it still
left the keyword set too broad for effective analysis. More importantly, when the threshold was set more strictly
(≥ 0.75), the algorithm excluded many semantically meaningful attributes, illustrating the trade-off between cov-
erage and precision inherent in threshold tuning.
To overcome this limitation, Large Language Models (LLMs) were introduced as a filtering mechanism in the
final step, as shown in Table 1. Instead of manually curating hundreds of candidate terms, the extracted list was
fed into different LLMs with prompts instructing them to select and retain only relevant smartwatch attributes.
This filtering stage proved effective: depending on the model, the attribute set was reduced to 28–74 keywords,
a scale much more appropriate for downstream categorization. This approach demonstrates the added value of
LLMs—not in generating keywords directly, but in refining and distilling machine-extracted terms into semanti-
cally coherent sets, thereby striking a balance between comprehensiveness and interpretability.
Table 2 compares the filtered keywords produced by four different LLMs: LLaMA 3.3 70b, GPT-5 nano,
Gemini 2.5 Flash, and DeepSeek R1 T2. While the models differed in the number of retained terms (ranging from
28 for LLaMA to 74 for DeepSeek), their outputs converged strongly on the most salient smartwatch attributes.
Across all models, recurring terms included battery, display, strap, GPS, connectivity, notifications, and water -
proof, indicating that the essential vocabulary of smartwatch evaluation was consistently preserved. Differences
Model Extracted keyword
Llama 3.3 70b accelerometer, alarms, amoled, backlight, battery, bluetooth, charger, clasp, display,
durable, ecg, ekg, gps, lightweight, lte, music, notifications, scratch, sensor, stop-
watch, storage, strap, sync, voice assistant, waterproof, wifi, wristband
GPT5-nano 32gb, 42 mm, 44 mm, 46 mm, 47 mm, accelerometer, alarms, amoled, app, back-
light, band, bands, batteries, battery, bezel, blue, bluetooth, bracelets, cellular, charge,
charger, color, customization, displays, durability, durable, ecg, ekg, face, faces,
glass, gps, laps, lilac, lte, notifications, passcode, pedometer, pink, privacy, recharge,
screen, seamless, sensor, sensors, slimline, solar, steps, stopwatch, straps, sync,
synced, syncs, tracking, unlock, unlocked, vo2max, watchband, waterproof, wifi
Gemini 2.5 Flash 32gb, 42 mm, 44 mm, 47 mm, accelerometer, accuracy, alarm, amoled, android,
apps, backlight, bandwatch, battery, bessel, bezel, bluetooth, calories, cellular, clasp,
customization, data, display, display, displays, ecg, ekg, faces, features, flashlight,
gps, heartrate, hr, laps, lightweight, lte, measurement, messages, music, music, nfc,
notifications, pedometer, running, screen, seamless, sensor, sleep, smaller, smart-
watch, software, solar, sound, srm, steps, stopwatch, strap, track, tracking, vo2max,
watches, waterproof, wifi, wireless, wristband.
DeepSeek R1 T2 42 mm, 46 mm, 47 mm, accelerometer, accuracy, alarm, alarms, alexa, amoled,
android, band, batteries, battery, bracelet, bright, calories, cellular, challenges,
charge, charger, clock, color, comfortable, comfy, customization, data, displays,
durable, ecg, ekg, face, faces, fit, flashlight, functional, gps, laps, lightweight, lte,
messages, music, notifications, passcode, pedometer, phone, premium, running,
screen, sensor, sensors, slimline, small, smaller, software, solar, solid, steps, straps,
subscription, synced, syncing, syncs, track, tracker, tracking, unlocked, vo2max, war-
ranty, watchband, waterproof, wifi, wrist, wristband,
Table 2 Extracted keywords
from different LLMs.

Extraction step Number of keywords
KeyBERT without threshold 17,736
KeyBERT with threshold 240
LLM Filtering
Llama 3.3 70b 28
GPT5-nano 61
Gemini 2.5 Flash 64
DeepSeek R1 T2 75
Table 1 Stepwise reduction
of candidate keywords.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
among models primarily reflected lexical granularity rather than conceptual divergence. For instance, some mod-
els included detailed size specifications (42 mm, 44 mm, 46 mm), while others generalized such terms under
broader categories, such as strap or design. These discrepancies can be interpreted as minor noise rather than
substantive inconsistencies.
Based on the comparison in Table 2, the DeepSeek R1 T2 output was selected as the working attribute list for
subsequent analysis phases. Although this model produced the largest set of keywords (74), broader coverage was
considered advantageous to ensure that no potentially important product attributes were prematurely excluded.
While more compact outputs, such as LLaMA (28) or GPT-5 nano (61), offered greater conciseness, they risked
omitting less frequent but still relevant attributes. DeepSeek’s output, by contrast, retained the core vocabulary
shared across all models while also incorporating a wider spectrum of peripheral terms that may capture niche
aspects of consumer evaluations. For this reason, DeepSeek was deemed the most appropriate foundation for
downstream categorization and sentiment mapping, with the understanding that subsequent zero-shot classifica-
tion would help refine and consolidate these attributes into higher-level categories.
Building on the refined attribute pool generated in the previous step (Tables 1 and 2), the next phase involved
organizing the extracted terms into abstract attribute categories to facilitate structured analysis. While individual
keywords capture consumer vocabulary, they often appear in fragmented or overlapping forms, making direct
interpretation difficult. By employing zero-shot prompting with an LLM, these terms were consolidated into
semantically coherent groups that better reflect how consumers evaluate smartwatch products. The outcome
of this categorization is presented in Table 3, which highlights eight major categories of smartwatch attributes:
Health Monitoring Features, Connectivity, Display Technology, Design & Comfort, Software & Smart Features,
Activity & Location Tracking, Power & Battery Management, and General Functionality. Each category com -
prises multiple keywords that collectively define its scope; for example, Health Monitoring Features includes
both general terms such as sensor and specific measures like ecg and vo2max, while Design & Comfort encom -
passes a wide range of descriptors covering strap type, wrist fit, and size variations (e.g., 42 mm, 46 mm, 47 mm).
This categorization not only reduces the complexity of raw keyword outputs but also provides a conceptual
bridge between consumer language and attribute-level evaluation, enabling subsequent sentiment aggregation
and brand-level positioning.
The outcome of this process is shown in Table 3, which identifies eight major attribute categories relevant
to smartwatch evaluation: Health Monitoring Features, Connectivity, Display Technology, Design & Comfort,
Software & Smart Features, Activity & Location Tracking, Power & Battery Management, and General Func -
tionality. Each category captures a distinct dimension of smartwatch performance as perceived by consumers.
For instance, Health Monitoring Features integrates generic terms such as sensor, with specific functionalities,
such as ecg and vo2max, reflecting the growing importance of biometric tracking in wearable technologies. Simi-
larly, Design & Comfort brings together strap-related descriptors (watchband, wristband, straps) with ergonomic
evaluations (comfortable, lightweight, durable), offering a holistic view of product aesthetics and wearability. By
Extraction step Number of keywords
Health Monitoring Features accelerometer, ecg, ekg, pedometer, vo2max, heart rate, sensor, sensors
Connectivity alexa, android, cellular, lte, wifi, synced, syncing, syncs
Display Technology amoled, bright, color, displays, face, faces, screen
Design & Comfort band, bracelet, comfortable, comfy, durable, lightweight, slimline,
small, smaller, straps, watchband, wrist, wristband, 42 mm, 46 mm,
47 mm
Software & Smart Features alarm, alarms, customization, data, messages, music, notifications,
passcode, software, subscription, challenges, phone
Activity & Location Tracking gps, laps, running, steps, track, tracker, tracking, calories
Power & Battery Management batteries, battery, charge, charger, solar
General Functionality accuracy, flashlight, functional, premium, solid, waterproof, clock, fit,
unlocked, warranty
Table 3 Categorization of
extracted smartwatch key-
words into abstract attribute
groups.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
consolidating scattered keywords into structured categories, this step creates a conceptual bridge between raw
consumer expressions and attribute-level evaluation, laying the foundation for subsequent stages of sentiment
aggregation and brand-level positioning.
The observed differences in keyword outputs across LLMs can be attributed to variations in model architecture,
training data composition, and semantic abstraction capabilities. Large language models are trained on diverse
corpora with different tokenization schemes, parameter sizes, and optimization objectives, which influence how
semantic concepts are represented internally. Models with stronger generalization capability tend to abstract
domain-specific terms into broader conceptual categories (e.g., grouping “42 mm,” “46 mm,” and “47 mm”
under design-related attributes), while others preserve more granular lexical distinctions. Despite these lexical
variations, the models exhibit strong semantic convergence, consistently identifying core smartwatch evaluation
dimensions such as battery, connectivity, display, and health monitoring. This pattern reflects the ability of large
language models to capture underlying semantic relationships rather than relying solely on surface-level word
frequency. Such semantic consistency across models reinforces the robustness of LLM-assisted keyword filtering
as a reliable method for extracting meaningful product attributes from consumer-generated text.
Sentiment analysis and evaluation
Following the sentiment classification procedure described in Sect.  2.4, each review in the dataset was assigned
a polarity label (positive, neutral, or negative) using the zero-shot classification model. Table 4 summarizes the
overall distribution of sentiment classifications across the 12,900 reviews. The results show that the majority of
reviews express positive sentiment, accounting for 65.8% of the dataset, indicating generally favorable consumer
perceptions of smartwatch products. Neutral sentiment represents 17.8% of the reviews, reflecting balanced or
mixed evaluations, while negative sentiment accounts for 16.4%, highlighting areas of dissatisfaction. This dis -
tribution is consistent with typical consumer review patterns on e-commerce platforms, where positive feed -
back tends to dominate, while negative and neutral reviews provide important diagnostic insights into product
weaknesses.
To assess the reliability of the automated sentiment classification, model predictions were compared with
manually annotated ground truth labels for a sample of 200 reviews, as described in Sect.  2.4. The evaluation
was conducted using standard performance metrics, including precision, recall, F1-score, and overall accuracy.
These metrics provide a comprehensive assessment of classification performance by measuring both the correct-
ness and consistency of sentiment predictions across polarity classes. The results of this evaluation are presented
in Table 5.
As shown in Table 5, the zero-shot sentiment classifier achieved high performance across all evaluation met -
rics, with an overall accuracy of 0.88 and a macro-averaged F1-score of 0.86. These results demonstrate strong
agreement between automated predictions and human annotations, confirming that the model effectively captures
sentiment polarity in consumer-generated reviews. Performance was particularly strong for both positive and
Metric Positive Neutral Negative Average
Precision 0.91 0.82 0.88 0.87
Recall 0.93 0.79 0.86 0.86
F1-score 0.92 0.80 0.87 0.86
Accuracy - – – 0.88
Table 5 Sentiment polar-
ity (performance) and
frequency (importance) of
smartwatch attributes.

Sentiment class Number of reviews Percentage
Positive 8,524 65.8%
Neutral 2,311 17.8%
Negative 2,087 16.4%
Table 4 Distribution of sen-
timent classification results
across the review corpus.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
negative sentiment, reflecting the model’s ability to detect clear expressions of satisfaction and dissatisfaction
accurately. Performance for neutral sentiment was slightly lower but remained within an acceptable range, con -
sistent with the inherently ambiguous and context-dependent nature of neutral evaluations. The balanced preci -
sion and recall values across classes further indicate that the classifier does not exhibit substantial bias toward
any particular sentiment category.
To contextualize these findings, the performance of the proposed zero-shot approach was compared with state-
of-the-art sentiment classification methods reported in prior literature. Supervised transformer-based models, such
as BERT and RoBERTa, typically achieve accuracy and F1-scores in the range of 0.85 to 0.92 when fine-tuned on
domain-specific labeled datasets25,26,41. While these supervised models may achieve slightly higher performance
under optimal training conditions, their effectiveness depends on the availability of large annotated datasets,
which require substantial time and manual effort to construct. In contrast, the zero-shot approach employed in
this study achieved competitive performance without requiring domain-specific training data, demonstrating its
effectiveness as a scalable, resource-efficient alternative.
Overall, these results confirm that the zero-shot sentiment classification framework provides reliable polarity
detection suitable for large-scale consumer preference analysis. The high level of agreement with human annota-
tions ensures that the sentiment polarity scores used in subsequent attribute-level aggregation and Importance–
Performance Analysis accurately reflect consumer evaluations. Furthermore, the ability to achieve competitive
performance without labeled training data highlights the practical advantages of zero-shot LLM-based classifica-
tion, including rapid deployment, domain adaptability, and reduced implementation cost. These characteristics
make the proposed framework a robust and efficient solution for extracting consumer preference insights from
large-scale review datasets.
Importance-performance analysis
Attributes analysis
Building on the attribute categorization in Table 3, each attribute group was further analyzed with respect to
average sentiment polarity (performance) and mention frequency (importance). These results are summarized
in Table 6. Sentiment scores were computed as the mean of positive, neutral, and negative classifications across
reviews, normalized to the interval [0,1]. Importance scores were derived from the relative frequency of attribute
mentions within the entire corpus, reflecting the salience of each attribute in consumer discourse. This dual mea-
surement approach enables a balanced view of how consumers perceive product attributes—not only in terms of
evaluative tone but also in terms of their centrality to purchase and usage considerations.
The results in Table 6 highlight clear variations across attributes. Design & Comfort emerged as the most
salient factor, with 3,999 mentions (importance score = 0.372) and the highest sentiment score (0.675). This sug-
gests that ergonomic and aesthetic features are both widely discussed and positively perceived, making them
central to consumer satisfaction. Other attributes, such as Connectivity, Health Monitoring Features, and General
Functionality, also demonstrated high importance, each contributing over 1,500 mentions, and showed relatively
positive sentiment averages (0.63–0.64). By contrast, Display Technology appeared infrequently (117 mentions,
Attribut category Average sentiment score Total mentions Importance score
Activity & Location Tracking 0.62 305 0.03
Connectivity 0.63 1510 0.14
Design & Comfort 0.68 3999 0.37
Display Technology 0.58 117 0.01
General Functionality 0.63 1841 0.17
Health Monitoring Features 0.64 1547 0.14
Power & Battery Management 0.60 874 0.15
Software & Smart Features 0.61 553 0.05
Table 6 Sentiment polar-
ity (performance) and
frequency (importance) of
smartwatch attributes.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
importance = 0.011) and had the lowest sentiment score (0.580), indicating that while display specifications may
be technically significant, they are not at the forefront of consumer discourse. Meanwhile, Power & Battery
Management showed moderate importance (0.081) but a comparatively lower sentiment score (0.599), reflecting
persistent frustrations with charging and energy management in wearable devices.
To better visualize these findings, attributes were mapped onto the Importance–Performance Analysis (IPA)
framework, shown in Fig. 3. The X-axis represents importance scores, while the Y-axis reflects performance. Red
dashed lines divide the plot into quadrants based on the mean values of importance (0.13) and performance (0.62)
across all attributes. It is important to note that these lines are not drawn at the geometric center of the axes but
at the empirical averages, ensuring that the quadrant divisions reflect the actual distribution of data rather than
arbitrary midpoints.
The IPA results offer a diagnostic overview of consumer priorities. Design & Comfort clearly occupies the
Keep up the good work quadrant, combining high importance with high performance. Attributes such as Con -
nectivity, Health Monitoring Features, and General Functionality also align near this quadrant, suggesting that
they are essential elements of consumer satisfaction and are performing reasonably well. Conversely, Power
& Battery Management appears in the Concentrate here quadrant, signaling an area of high consumer salience
but below-average sentiment, consistent with known challenges in wearable technology. Display Technology,
with its low importance and low performance, falls into the low-priority quadrant, indicating limited consumer
concern despite weaker evaluations. Finally, the Activity & Location Tracking and Software & Smart Features
Fig. 3 Importance–performance analysis (IPA) of smartwatch attributes.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
cluster is closer to Possible overkill, reflecting that while users tend to view them positively, they are not central
to consumer evaluation patterns.
The quadrant boundaries in the IPA framework were determined using the arithmetic mean values of impor -
tance and performance across all attributes, following the original methodology proposed by Martilla and
James43 and widely adopted in subsequent IPA applications44. This approach ensures that quadrant segmentation
reflects the empirical distribution of attribute evaluations rather than arbitrary thresholds. To assess robustness,
we examined the relative positioning of attributes under alternative central tendency measures, such as median-
based thresholds. The overall quadrant structure remained stable, with key attributes such as Design & Comfort
and Connectivity consistently positioned in high-importance, high-performance regions, and Power & Battery
Management remaining in the high-importance, lower-performance region. This consistency indicates that the
strategic implications derived from the IPA framework are not sensitive to minor variations in quadrant boundary
definition, supporting the reliability of the analytical conclusions.
Brand analysis
From the acquired dataset, more than 40 smartwatch brands were identified, reflecting the market’s diverse player
base. However, the vast majority of these brands exhibit very low recognition, with few mentions in consumer
reviews. Their limited visibility contrasts sharply with a handful of mainstream brands that dominate user atten-
tion and shape consumer discourse. This skewed distribution of importance underscores that while niche brands
exist and occasionally receive favorable sentiment, market evaluations are largely concentrated around a small
group of leading brands. As illustrated in Fig. 4, the IPA mapping shows how these dominant players are posi -
tioned relative to smaller competitors, providing a clearer picture of the smartwatch market’s structural dynamics.
The brand-level IPA results, illustrated in Fig. 4, reveal a strong clustering of major global smartwatch brands—
Fitbit, Apple, Samsung, Garmin, and Amazfit—toward the bottom-right quadrant of the matrix. These five brands
dominate consumer attention, together accounting for more than 60% of all mentions, yet their performance
scores remain tightly grouped in the range of 0.62–0.65. The diagram shows that although these brands capture
a disproportionate share of consumer discourse, their evaluative performance is moderate and relatively undif -
ferentiated. In contrast, a variety of second-tier and niche brands are dispersed beyond this cluster. For example,
SOUYIE, SGJIK, JrTrack, and Banlvs are positioned higher on the performance axis, with sentiment scores
above 0.70, despite their very low importance scores. Similarly, mid-tier brands such as Amazon Renewed and
AMAZTIM balance limited attention with comparatively strong sentiment. These placements on the IPA map
indicate that while top brands dominate visibility, smaller players are often evaluated more favorably by their
niche audiences.
Taken together, this asymmetry in brand positioning highlights a key dynamic of the smartwatch market: lead-
ing brands dominate discourse but are evaluated only moderately, while less visible competitors achieve stronger
evaluations but struggle with visibility. This pattern underscores both the stability of brand dominance at the top
and the latent opportunities for emerging players to leverage their favorable sentiment into broader recognition.
However, because the five most important brands—Fitbit, Apple, Samsung, Garmin, and Amazfit—not only
account for the majority of consumer attention but also happen to cluster in the same quadrant of the IPA map,
the next stage of analysis will focus more closely on these top-tier brands.
Brand-attribute analysis
To gain deeper insights into how leading smartwatch brands are evaluated, the analysis was extended to the
attribute level, combining both sentiment scores and importance scores across key functional categories. The two
radar charts (Figs. 5 and 6) illustrate how the top five brands—Apple, Samsung, Garmin, Fitbit, and Amazfit—
perform relative to one another in terms of consumer perception (sentiment) and attention (importance).

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
Firstly, the radar chart in Fig. 5 compares the five leading smartwatch brands—Amazfit, Apple, Fitbit, Garmin,
and Samsung—across eight attribute categories. Results show strong differentiation in specific areas: Design
& Comfort is led by Garmin (0.680) and Samsung (0.679), while Connectivity is strongest for Apple (0.670)
and Samsung (0.681), reflecting their ecosystem integration. Health Monitoring highlights Apple (0.663) and
Samsung (0.628) as leaders, while Fitbit (0.597) trails. For Display Technology, Samsung (0.668) outperforms
competitors, reinforcing its advantage in AMOLED and display quality.
Other attributes reveal narrower differences. Power & Battery Management scores remain modest across all
brands (0.578–0.609), reflecting persistent consumer concerns. In Software & Smart Features, Apple (0.626) and
Garmin (0.599) score higher, while Samsung (0.514) underperforms despite strong hardware evaluations. Over-
all, the radar chart shows a competitive balance among the top brands, with each brand demonstrating distinct
strengths but no clear overall leader. Samsung excels in displays and connectivity; Apple leads in connectivity
and software; Garmin stands out in design; while Fitbit and Amazfit perform consistently but without category
dominance.
Secondly, the radar chart in Fig. 6 highlights that Design & Comfort is the most important attribute across all
brands, with Apple (0.060) and Fitbit (0.048) leading in mentions, while Garmin (0.036) and Samsung (0.033)
also show notable consumer focus. General Functionality emerges as the second most important dimension, with
Fitbit (0.038) and Apple (0.024) dominating the discussions. Connectivity also stands out, particularly for Fitbit
(0.028) and Apple (0.017), reflecting consumer emphasis on ecosystem integration and compatibility.
Fig. 4 Importance–performance analysis (IPA) of smartwatch brands.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
In contrast, Display Technology records the lowest importance scores across brands (all ≤ 0.003), suggesting it
is rarely highlighted in user discourse despite being a key product specification. Power & Battery receives mod-
erate attention, with Apple (0.021) and Samsung (0.017) slightly ahead, reflecting ongoing consumer concerns
around battery life. Health Monitoring Features are especially relevant for Fitbit (0.028), reinforcing its position-
ing as a health-centric brand. Overall, the radar visualization shows that while flagship brands compete strongly
Fig. 6 Radar chart of attribute-level
importance scores for the top five
smartwatch brands.

Fig. 5 Radar chart of attribute-
level sentiment scores for the top
five smartwatch brands.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
on comfort, general functions, and connectivity, some attributes, such as display, receive limited recognition,
pointing to a divergence between technical specifications and consumer salience.
Discussion
This study shows how combining zero-shot LLMs with IPA mapping can yield both theoretical and practical
insights into consumer preferences. Theoretically, it demonstrates the potential of LLMs to enhance attribute-
level sentiment analysis and extends IPA into unstructured review contexts. Managerially, it provides actionable
guidance by highlighting where consumer expectations are met, where dissatisfaction persists, and where niche
opportunities exist. At the same time, its limitations point to fertile ground for future work that deepens, scales,
and diversifies this approach.
Theoretical contributions
This study makes several theoretical contributions at the intersection of computational linguistics, consumer
behavior, and product design research. First, it advances the application of zero-shot large language models
(LLMs) in consumer analytics. Traditional methods in aspect-based sentiment analysis (ABSA), such as topic
modeling, rule-based extraction, or supervised machine learning, often rely on predefined lexicons or labeled
datasets. Such approaches tend to capture only frequently mentioned attributes and struggle with nuanced, con -
text-dependent, or low-frequency aspects 24,25. By contrast, the zero-shot LLM framework employed here dem -
onstrates that domain-specific attribute categories can be generated and classified without manual annotation,
aligning with recent arguments that LLMs can serve as adaptive, knowledge-driven classifiers28,35. This contrib-
utes to the theory by demonstrating how LLMs can address data sparsity and contextual complexity. These two
problems have long constrained consumer preference modeling.
Second, this study extends the theoretical application of Importance–Performance Analysis (IPA) to unstruc -
tured textual data environments. Originally developed for structured survey data 43, IPA has been widely used to
evaluate consumer satisfaction based on predefined attributes. However, its application to large-scale, unstruc -
tured review data has been limited due to challenges in reliably extracting attribute-level evaluations from text.
By integrating zero-shot LLM-based attribute classification and sentiment analysis with IPA, this study demon -
strates how attribute importance and performance can be derived directly from natural-language data without
the need for predefined survey instruments. This adaptation extends the theoretical scope of IPA from structured
evaluation frameworks to open-ended consumer feedback environments, enabling more scalable, ecologically
valid assessment of consumer perceptions.
The third contribution of this study is to demonstrate the practical advantages of zero-shot large language
models over traditional supervised and weakly supervised approaches for consumer preference analysis. Con -
ventional aspect-based sentiment analysis and supervised classification methods typically require large labeled
datasets and task-specific model training, which involve substantial annotation effort and limit scalability across
domains25,26,41. In contrast, the proposed zero-shot framework leverages pre-trained language models capable of
semantic inference without requiring labeled training data, enabling immediate deployment on new review datas-
ets. Despite this absence of task-specific training, the sentiment classification validation results demonstrate com-
petitive performance (accuracy = 0.88, macro F1-score = 0.86), which falls within the performance range reported
for supervised transformer-based models in prior literature (typically 0.85–0.92)25,26,41. This highlights an impor-
tant practical trade-off: while supervised models may achieve marginally higher performance under optimized
training conditions, zero-shot approaches provide substantially greater efficiency, scalability, and adaptability.
By eliminating reliance on labeled datasets and retraining, the proposed framework enables scalable, flexible
consumer preference analysis, particularly in rapidly evolving product domains where annotated data may be
unavailable or quickly outdated.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
Finally, this study contributes to the emerging literature on LLM-enabled consumer analytics by providing
empirical evidence that zero-shot inference can achieve reliable and interpretable attribute-level preference mod-
eling. While prior research has primarily focused on using large language models for classification and text-gen-
eration tasks, this study demonstrates their utility in structured knowledge extraction and preference modeling.
This contribution helps bridge the gap between computational linguistics and consumer behavior research by
showing how the semantic inference capabilities of large language models can be systematically applied to ana-
lyze consumer evaluations and support strategic product decision-making.
Practical and managerial implications
From a managerial perspective, the results provide actionable insights for product development, market posi -
tioning, and strategic differentiation in the smartwatch industry. At the attribute level, the analysis confirms that
Design & Comfort, Connectivity, and Health Monitoring Features are consistently among the most discussed and
positively evaluated dimensions. This aligns with prior studies showing that comfort, ease of use, and reliable
biometric tracking are critical to user adoption of wearable technologies3,4. Managers should therefore prioritize
continuous refinement in these areas, ensuring that product iterations enhance ergonomic design, seamlessly inte-
grate with broader digital ecosystems, and maintain consumer trust in health-related functionalities.
At the same time, the results highlight persistent dissatisfaction around Power & Battery Management. Despite
being moderately important in consumer discourse, sentiment scores for battery performance are consistently
lower than for other attributes. This finding aligns with broader evidence that battery life remains a bottleneck
foronsumer satisfaction across wearable and mobile technologies16,19. For managers, this suggests that incremen-
tal gains in battery endurance, fast-charging solutions, or novel energy management strategies could yield dis -
proportionately high returns in user satisfaction and brand loyalty. Importantly, the IPA mapping reveals that this
issue is not isolated to one brand, indicating an industry-wide challenge and a potential competitive differentiator
for firms that successfully address it.
At the brand and series levels, the IPA analysis reveals that Apple, Samsung, Fitbit, Garmin, and Amazfit col-
lectively dominate consumer attention, accounting for more than 60% of mentions. However, their sentiment
scores remain clustered around 0.62–0.65. This reflects a plateau of expectations, where major brands dominate
consumer discourse, yet evaluations do not reflect overwhelming satisfaction. This finding is consistent with
market studies suggesting that brand recognition often guarantees visibility but not necessarily superior evalua -
tions10. For managers of leading brands, this indicates the need to go beyond incremental upgrades and to seek
experience-driven differentiation, whether through ecosystem lock-in, the personalization of health insights, or
the integration of sustainability features.
Meanwhile, the analysis also identifies niche and second-tier brands that, although far less visible, receive
higher average sentiment scores. Brands such as SOUYIE or JrTrack, as well as specialized Garmin series, illus-
trate how smaller players can compete on focused strengths such as affordability, child-oriented functionality,
or specialized sports tracking. For managers of these brands, the challenge is to scale visibility without diluting
positive perceptions—a balance that can be achieved through targeted marketing, influencer collaborations, or
strategic partnerships.
The attribute-level radar analysis also reflects well-established strategic positioning differences among leading
smartwatch brands. Apple’s strong performance in Connectivity and Software & Smart Features aligns with its
tightly integrated ecosystem, which enables seamless interaction across devices and services. Samsung demon -
strates strong performance in Display Technology and Connectivity, consistent with its technological leadership
in AMOLED displays and mobile hardware integration. Garmin’s strength in Design & Comfort and Activity
& Location Tracking reflects its focus on fitness-oriented consumers and outdoor enthusiasts, where durability,
ergonomics, and tracking precision are critical. Fitbit’s relative emphasis on Health Monitoring Features is con-
sistent with its historical positioning as a health-focused wearable brand. These patterns confirm that consumer-
generated reviews capture meaningful differences in brand positioning and strategic focus. Such insights provide

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
actionable guidance for managers by identifying areas of competitive advantage and opportunities for differentia-
tion and product improvement.
Limitations and future work
Several limitations should be noted. First, the analysis is based on Amazon reviews from July to December
2024, which may not fully reflect long-term consumer sentiment or global preferences. Future research should
expand to multi-platform and multi-regional datasets to improve generalizability. Second, while the zero-shot
LLM framework reduces reliance on labeled data, results remain sensitive to prompt design and model choice.
Different LLMs produced varying keyword sets, and although DeepSeek was chosen for its coverage, future
work could employ ensemble models or fine-tuned domain-specific LLMs to enhance robustness.
Third, the IPA method simplifies consumer evaluations into frequency (importance) and average sentiment
(performance). While effective, this risks overlooking inter-attribute trade-offs—such as design versus battery
life—or emerging expectations, such as sustainability and repairability. Advanced approaches such as multi-
objective optimization or structural equation modeling could capture these interdependencies more effectively.
Finally, this study focused on brand- and series-level evaluations; however, future work could explore cross-
brand ecosystem comparisons (e.g., Apple vs. Samsung integration strategies) or life-cycle analyses (e.g., launch
vs. maturity stages) to better understand dynamic shifts in consumer evaluations.
Another limitation concerns the inherent characteristics of large language models used for zero-shot classifica-
tion. While zero-shot LLMs enable flexible and scalable analysis without requiring labeled training data, their
outputs remain sensitive to prompt design and label formulation. Small variations in prompt wording or candidate
label definitions may influence classification outcomes, potentially affecting reproducibility and consistency.
In addition, although large language models generally exhibit strong semantic reasoning capabilities, they may
occasionally produce incorrect or overly generalized inferences, particularly when handling ambiguous or con -
text-dependent expressions. While the validation results in this study demonstrate high classification reliability,
these limitations highlight the importance of careful prompt design, validation procedures, and human oversight
when deploying LLM-based knowledge extraction systems. Future research could explore prompt optimization
techniques, ensemble approaches using multiple models, or hybrid human–AI workflows to further improve
robustness and reliability.
Conclusions
This study employed a zero-shot LLM framework to analyze consumer preferences for smartwatch attributes,
utilizing Amazon reviews, and integrated keyword extraction, sentiment analysis, and Importance–Performance
Analysis (IPA). The approach demonstrates how unstructured consumer feedback can be converted into struc -
tured insights, highlighting both frequently discussed attributes and their evaluative sentiment. Findings show
that Design & Comfort, Connectivity, and Health Monitoring are the most salient and positively perceived dimen-
sions, while Power & Battery Management remains a persistent weakness across brands. At the brand and series
levels, Apple, Samsung, Fitbit, Garmin, and Amazfit dominate consumer attention but show only moderate senti-
ment scores, suggesting a plateau of expectations that calls for strategies beyond incremental upgrades.
Theoretically, the study enriches research on LLM-enabled consumer analytics by demonstrating how zero-
shot approaches overcome the limitations of traditional aspect-based sentiment analysis and by adapting IPA
for review-based data. In practice, the results provide managers with diagnostic tools to prioritize investments,
underscoring the need for stronger differentiation among leading brands and for visibility strategies for smaller
but well-regarded competitors. Looking forward, future research should expand this framework through multi-
platform datasets, ensemble LLMs, and advanced analytical methods, contributing to more consumer-centered
and sustainable product design and strategy in the wearable technology industry.

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
Acknowledgements The authors express their sincere appreciation for the exceptional support, in terms of facilities and
policies, provided by Universitas Tidar and Sejong University. This support has been instrumental in the successful comple-
tion and publication of our work.
Author contributions IAN: conceptualization, methodology, data curation, software, visualization, writing - original draft
preparation. NN: conceptualization, methodology, data curation, software, visualization, writing - original draft preparation.
MRQ: conceptualization, methodology, data curation, software, visualization, writing - original draft preparation. N.L.F.:
conceptualization, methodology, data curation, software, visualization, writing - original draft preparation. Y .G.: conceptual-
ization, methodology, supervision, funding, writing - review and editing. M.S.: conceptualization, methodology, supervision,
funding, writing - review and editing. All authors have read and agreed to the published version of the manuscript.
Funding This work was supported by the IITP (Institute of Information & Communications Technology Planning &
Evaluation)-ITRC (Information Technology Research Center) grant funded by the Korea government (Ministry of Science
and ICT) (IITP-2025-RS-2024-00437191).
Data availability The data presented in this study is available on request from the corresponding author.
Declarations
Competing interests The authors declare no competing interests.
Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 Interna-
tional License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as
long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence,
and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material
derived from this article or parts of it. The images or other third party material in this article are included in the article’s Cre-
ative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s
Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you
will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p : / / c r e a t i v e c o m m o
n s . o r g / l i c e n s e s / b y - n c - n d / 4 . 0 /     .
References
 1. Oh, G. E., Aliyev, M., Kafouros, M. & Au, A. K. M. The role of consumer characteristics in explain-ing product innovation
performance: Evidence from emerging economies. J. Bus. Res. 149, 713–727.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / J . J B U S R E S . 2 0 2 2
. 0 5 . 0 6 0     (2022).
 2. Guiné, R. P. F., Florença, S. G., Barroca, M. J. & Anjos, O. The link between the consumer and the innova-tions in food
product development. Foods 9, 1317. https://doi.org/10.3390/FOODS9091317  (2020).
 3. Ye, X., Wang, Y . & Shafiee, S. An iterative consumer-centric and technology-driven product innovation strategy based
on selective and dynamic consumer attention. Technol. Forecast Soc. Change 208, 123713.   h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / J . T
E C H F O R E . 2 0 2 4 . 1 2 3 7 1 3     (2024).
 4. Li, L., Wang, Z., Li, Y . & Liao, A. Impacts of consumer innovativeness on the intention to purchase sus-tainable products.
Sustain Prod. Consum. 27, 774–786. https://doi.org/10.1016/J.SPC.2021.02.002 (2021).
 5. Zhang, F., Sun, S., Liu, C. & Chang, V . Consumer innovativeness, product innovation and smart toys. Electron. Commer.
Res. Appl. 41, 100974. https://doi.org/10.1016/J.ELERAP.2020.100974 (2020).
 6. Shafi, M. et al. Factors Influencing the Consumer Acceptance of Innovation in Handicraft Products. Sage Open. 11, 1528
(2021).
 7. Rosário, A. & Raimundo, R. Consumer Marketing Strategy and E-Commerce in the Last Decade: A Litera-ture Review.
J. Theoretical Appl. Electron. Commer. Res. 16, 3003–3024. https://doi.org/10.3390/JTAER16070164 (2021).
 8. Chen, T., Samaranayake, P., Cen, X. Y ., Qi, M. & Lan, Y . C. The Impact of Online Reviews on Consumers’ Purchasing
Decisions: Evidence From an Eye-Tracking Study. Front. Psychol. 13, 865702.  h t t p s : / / d o i . o r g / 1 0 . 3 3 8 9 / F P S Y G . 2 0 2 2 . 8 6
5 7 0 2 / B I B T E X     (2022).
 9. Fernandes, S., Panda, R., Venkatesh, V . G., Swar, B. N. & Shi, Y . Measuring the impact of online reviews on consumer
purchase decisions – A scale development study. Journal of Retailing and Consumer Services, 68, 103066, 2022, (2022).
https://doi.org/10.1016/J.JRETCONSER.2022.103066

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
 10. Varga, M. & Albuquerque, P. The Impact of Negative Reviews on Online Search and Purchase Decisions. J. Mark. Res.
61, 803–820 (2024).
 11. Bo, L., Chen, Y . & Yang, X. The Impact of Contradictory Online Reviews on Consumer Online Purchase Decision:
Experimental Evidence From China. Sage Open. 13, 180107 (2023).
 12. Wang, Q., Zhang, W., Li, J., Mai, F. & Ma, Z. Effect of online review sentiment on product sales: The moder-ating role
of review credibility perception. Comput Human Behav, 133, 107272, 2022, (2022).  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / J . C H B . 2 0 2
2 . 1 0 7 2 7 2
 13. Zheng, S., Yeoh, W., Ren, J. & Yang, S. Examining the diminishing marginal impact of online reviews on consumers’
information acquisition and purchase decisions. Electron. Commer. Res.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / S 1 0 6 6 0 - 0 2 4 - 0 9 9 2 9 - Z / T
A B L E S / 9     (2024).
 14. Liu, Z., Hui Lei, S., Lang Guo, Y . & Zhou, Z. The interaction effect of online review language style and product type on
consumers’ purchase intentions. Palgrave Commun. 6, 1–8 (2020).
 15. Wang, X., He, J., Curry, D. J. & Ryoo, J. H. Attribute Embedding: Learning Hierarchical Representations of Product
Attributes from Consumer Reviews. J. Mark. 86, 155–175 (2022).
 16. Zhu, B., Guo, D. & Ren, L. Consumer preference analysis based on text comments and ratings: A multi-attribute decision-
making perspective. Inf. Manag. 59, 103626. https://doi.org/10.1016/J.IM.2022.103626 (2022).
 17. Su, Z. et al. A multigrained preference analysis method for product iterative design incorporating AI-generated review
detection. Sci. Rep. 15, 1–18 (2025).
 18. Goldberg, D. M. & Abrahams, A. S. Sourcing product innovation intelligence from online reviews. Decis. Support Syst.
157, 113751. https://doi.org/10.1016/J.DSS.2022.113751 (2022).
 19. Wu, X., Liao, H., Lev, B. & Ding, W. A Classification-Based Product Selection Method Based on Online Reviews on
Multifaceted Attributes. IEEE Trans. Comput. Soc. Syst. 12, 11–24. https://doi.org/10.1109/TCSS.2024.3485009 (2025).
 20. Liao, H., Yang, Q. & Wu, X. Customer preference analysis from online reviews by a 2-additive Choquet integral-based
preference disaggregation model. Technological and Economic Development of Economy, 29, 411–437, 2023, (2023).
https://doi.org/10.3846/TEDE.2022.17972
 21. Ren, P., Zhu, B., Ren, L. & Ding, N. Online choice decision support for consumers: Data-driven analytic hierarchy
process based on reviews and feedback. J. Oper. Res. Soc. 74, 2227–2240 (2022).
 22. Li, S., Zhu, B., Zhang, Y ., Liu, F. & Yu, Z. A Two-Stage Nonlinear User Satisfaction Decision Model Based on Online
Review Mining: Considering Non-Compensatory and Compensatory Stages. J. Theoretical Appl. Electron. Commer.
Res. 19, 272–296. https://doi.org/10.3390/JTAER19010015 (2024).
 23. Büschken, J. B. & Allenby, G. M. Sentence-based text analysis for customer reviews. Market. Sci. 35, 953–975  (2013).
 24. Heidary Dahooie, J., Raafat, R.,  Qorbani, A. R. & Daim, T.  An intuitionistic fuzzy data-driven product ranking model
using sentiment analysis and multi-criteria decision-making. Technol Forecast Soc. Change 173, 121158.  h t t p s : / / d o i . o r g
/ 1 0 . 1 0 1 6 / J . T E C H F O R E . 2 0 2 1 . 1 2 1 1 5 8     (2016).
 25. Iqbal, A. et al. Sentiment Analysis of Consum-er Reviews Using Deep Learning. Sustainability 14, 10844.  h t t p s : / / d o i . o r
g / 1 0 . 3 3 9 0 / S U 1 4 1 7 1 0 8 4 4     (2022).
 26. Zhang, J., Zhang, A., Liu, D. & Bian, Y . Customer preferences extraction for air purifiers based on fi-ne-grained sentiment
analysis of online reviews. Knowl. Based Syst. 228, 107259. https://doi.org/10.1016/J.KNOSYS.2021.107259 (2021).
 27. Alantari, H. J., Currim, I. S., Deng, Y . & Singh, S. An empirical comparison of machine learning methods for text-based
sentiment analysis of online consumer reviews. Int. J. Res. Mark. 39, 1–19.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / J . I J R E S M A R . 2 0 2 1 .
1 0 . 0 1 1     (2022).
 28. Kojima, T., Shane Gu, S., Reid Google Research, M., Matsuo, Y . & Iwasawa, Y . Large Language Models are Zero-Shot
Reasoners. Adv. Neural Inf. Process. Syst. 35, 22199–22213 (2022).
 29. Wei, J. et al. Finetuned Language Models Are Zero-Shot Learners. ICLR 2022–10th International Conference on
Learning Representations, Accessed: Sep. 09, 2025. (2025). https://arxiv.org/pdf/2109.01652
 30. Liu, P. et al. Pre-train, Prompt, and Predict: A Systematic Survey of Prompting Methods in Natural Language Processing.
ACM Comput. Surv. 55, 815. https://doi.org/10.1145/3560815/SUPPL_FILE/3560815-APP.PDF (2023).
 31. Zhong, R., Lee, K., Zhang, Z. & Klein, D. Adapting Language Models for Zero-shot Learning by Me-ta-tuning on
Dataset and Prompt Collections. Findings of the Association for Computational Linguistics, Find-ings of ACL: EMNLP
2021 2856–2878, (2021). https://doi.org/10.18653/v1/2021.findings-emnlp.244
 32. Sanh, V . et al. Multitask Prompted Training Enables Zero-Shot Task Generalization. ICLR 2022–10th In-ternational
Conference on Learning Representations, Accessed: Sep. 09, 2025. (2021). https://arxiv.org/pdf/2110.08207
 33. Meng, Y ., Huang, J., Zhang, Y . & Han, J. Generating Training Data with Language Models: Towards Ze-ro-Shot Language
Understanding. Adv. Neural Inf. Process. Syst. 35, 462–477 (2022).
 34. Wang, Z., Pang, Y . & Lin, Y . Large Language Models Are Zero-Shot Text Classifiers, Accessed: Sep. 09, 2025. (2023).
https://arxiv.org/pdf/2312.01044
 35. Wei, J. et al. Finetuned Language Models Are Zero-Shot Learners. arXiv preprint arXiv:2109.01652 (2022).  h t t p s : / / d o i .
o r g / 1 0 . 4 8 5 5 0 / a r X i v . 2 1 0 9 . 0 1 6 5 2

Article in Press
Scientific Reports
https://doi.org/10.1038/s41598-026-57281-z
 36. Ouyang, L. et al. Training language models to follow instructions with human feedback. Adv. Neural Inf. Process. Syst.
30, 27730–27744 (2022).
 37. Grootendorst, M. KeyBERT: Minimal keyword extraction with BERT. (Project page).  h t t p s : / / g i t h u b . c o m / M a a r t e n G r / K e
y B E R T
 38. Sammet, J. & Krestel, R. Domain-Specific Keyword Extraction using BERT. in Proceedings of the 4th Con-ference on
Language, Data and Knowledge  659–665  (2023). https://www.econbiz.de/Record/datenbank-econis-
 39. Reimers, N. & Gurevych, I. Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP-IJCNLP
2019–2019 Conference on Empirical Methods in Natural Language Processing and 9th Interna-tional Joint Conference
on Natural Language Processing, Proceedings of the Conference 3982–3992  (2019).  h t t p s : / / d o i . o r g / 1 0 . 1 8 6 5 3 / v 1 / d 1 9 - 1
4 1 0
 40. Carbonell, J. & Goldstein, J. The Use of MMR, Diversity-Based Reranking for Reordering Documents and Producing
Summaries. SIGIR 1998 - Proceedings of the 21st Annual International ACM SIGIR Conference on Research and
Development in Information Retrieval 335–336. https://doi.org/10.1145/290941.291025 (1998).
 41. Hua, Y . C., Denny, P., Wicker, J. & Taskova, K. A systematic review of aspect-based sentiment analysis: domains,
methods, and trends. Artif. Intell. Rev. 57, 1–51. https://doi.org/10.1007/S10462-024-10906-Z (2024).
 42. Zhang, W., Li, X., Deng, Y ., Bing, L. & Lam, W. A survey on aspect-based sentiment analysis: Tasks, methods, and
challenges. IEEE Trans. Knowl. Data Eng. 35, 11019–11038. https://doi.org/10.1109/TKDE.2022.3230975 (2023).
 43. Martilla, A. & James, J. C. Importance-Performance Analysis. J Mark. 41, 77–79, 1977, (1977).  h t t p s : / / d o i . o r g / 1 0 . 1 1 7 7 /
0 0 2 2 2 4 2 9 7 7 0 4 1 0 0 1 1 2
 44. Shen, M., Cheng, A. & Bi, Y . An integrated framework for importance-performance analysis of product attributes and
validation from online reviews and maintenance records. Des. Sci. 10, e19. https://doi.org/10.1017/DSJ.2024.15 (2024).
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional
affiliations.
Authors and Affiliations
Imam Adi Nata1 · Nila Nurlina2 · Muhammad Rifqi Maarif2 · Norma Latif Fitriyani3 ·
Yeonghyeon Gu3 · Muhammad Syafrudin3
 Imam Adi Nata
imamadinata@untidar.ac.id
 Yeonghyeon Gu
yhgu@sejong.ac.kr
 Muhammad Syafrudin
syafrudinresearch@gmail.com
1 Department of Electrical, Mechatronics & Information Engineering, Universitas Tidar, Magelang 56116, Indonesia
2 Department of Mechanical & Industrial Engineering, Universitas Tidar, Magelang 56116, Indonesia
3 Department of Artificial Intelligence and Data Science, Sejong University, Seoul 05006, Republic of Korea
