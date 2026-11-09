---
title: Can We Trust AI Agents in the Supermarket? Sugar Content Inference from Product Images
url: https://arxiv.org/abs/2608.12359
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Jose Berengueres
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.12359
pages: 5
chars: 23245
fetched_at: '2026-11-08T13:36:36+00:00'
kb_version: 1
---

# Can We Trust AI Agents in the Supermarket? Sugar Content Inference from Product Images

XXX-X-XXXX-XXXX-X/XX/$XX.00 ©20XX IEEE
Can We Trust AI Agents in the Supermarket?
Sugar Content Inference from Product Images
Jose Berengueres, IEEE member
School of Computing & AI,
Nazarbayev University, Astana,
Kazakhstan
jose.berengueres@nu.edu.kz
Abstract—Nutritional labels are legally permitted to appear
in very small print, reducing real -world readability and
encouraging consumers to rely on “AI nutrition lens” and
vision-capable conversational agents for dietary guidance. We
evaluate whether such AI -mediated advice can meaningfully
substitute for regulated labeling using a bounded, verifiable
task: inferring which of two packaged foods contains less sugar
from front -of-pack images alone. A Two-Alternative Forced
Choice game was used to evaluate AI agent systems across four
national supermarket contexts: Sweden, the USA, Australia,
and Kazakhstan. The results (N=132 comparisons) across both
agents reveal a significant performance divide contingent on
context.  For g lobal products the agents achieved 88.9%
accuracy (p < 0.0001  against chance ). For l ocal products
(Sweden), accuracy dropped to 59.5% (p = 0.29), rendering the
AI's guidance statistically indistinguishable from random
guessing. These findings indicate a cross-market bias consistent
with uneven tra ining-data coverage , raising concerns about
trust, equity, and accountability , particularly when nutritional
judgment shifts from auditable public labels to proprietary
inference pipelines. We conclude that AI nutrition lens
applications are better framed as assistive, educational tools
rather than as replacements for regulated labels, and we
highlight the need for auditable datasets and evaluation
benchmarks aligned with local food ecosystems.
Keywords— data sovereignty, gamification, AI-agent, sugar,
bias, locality, 2AFC.
I. INTRODUCTION
Recent computer vision and vision –language models
enable “AI nutrition lenses  Apps”—mobile applications that
can convert a photo of a packaged product into near -instant
nutritional feedback in a supermarket setting.
A. UX of Nutritional Labels
This trend is driven in part by the usa bility limits of
regulated nutritional labels [1]. For example, in the EU [2],
food information can be printed as small as in x-height (≥1.2
mm, or ≥0.9 mm for small packages), which can remain
difficult to read under real shoppin g constraints. In addition,
nutrition panels are also frequently placed on curved surfaces
or near seams and package folds,  often on the back of the
product. While some consumers rely on labels for safety -
critical constraints (e.g., life-threatening allergies), others seek
rapid guidance on nutritional aspects . One of them is added
sugar, which  the World He alth Organization recommends
limiting to <10% of total energy intake (ideally <5%)  [3] to
reduce well-known health risks [4]. The combination of health
concerns, label legibility limitations, and the cognitive
complexity of product comparisons in the supermarket aisle
has fostered a growing app ecosystem of AI-powered “lens”
applications and label -analysis tools; in addition, general -
purpose vision -capable conversational GPT-based chatbots
can also be used to interpret packaging images.

Fig. 1. An agentic browser (see green pop-up) is playing the Two-
Alternative Forced Choice game Food-or-Not [5]. The goal is to click on
the image with less sugar. The aggregates can be used to determine AI-
biases across datasets.

Fig. 2. An agentic browser is in the final screen of the game after
completing a set of binary comparisons. In this case, the accuracy of
the agent is close to random guessing. Context: Swedish products.
This shift, while convenient for consumers seeking
nutritional clarity, raises a governance question: What
happens when nutritional information moves from public,
auditable disclosures (labels) to private inference pipelines?
B. AI-Mediated Nutrition Information
The trustworthiness of such AI-mediated nutritional
inference remains contested. This is not only due to pervasive
conflicts of interest with advertisers [6], validation studies
show that AI food recognition systems can exhibit systematic
inaccuracies in energy and nutrient estimation even when
improving convenience or logging workflow [7], [8].
Performance often degrades on culturally diverse foods,
indicating dataset -coverage bias and uneven generalization
beyond Western-centric product ecosystems  [9], [10], [11].

Beyond vision models, large language models can introduce
normative “health framing” biases in food evaluation, shaping
outputs in ways that may not align with physiological ground
truth or local dietary context [12]. Accordingly, reviews of AI
in nutrition consistently foreground unresolved concerns
around fairness, transparency, accountability, and governance
in algorithmic dietary guidance [13], [14], [15].
C. Technical State-of-the-Art
At a technical level, the closest “building blocks” to AI
nutrition lenses exist across three partially disconnected
strands.
First, strong non-visual baselines demonstrate that added
sugar can be inferred from structured nutrition, ingredient, and
category data, motivating machine learning as a “digital
completion” tool in jurisdictions where added -sugar
disclosure is incomplete [16], [17].
Second, multimodal work moves closer to a lens
paradigm: vision–language models trained on front -of-pack
(FOP) images plus label/ingredient text can estimate multiple
nutrient targets and outperform unimodal baselines,
demonstrating feasibility of FOP -driven nutrition inference
[18].
Third, multiple applied systems primarily function as
digital label readers, using object detection, OCR, and parsing
to extract nutrition tables and compute scores such as Nutri -
Score—effective for digitization, but conceptually distinct
from inferring nutrients from packaging cues alone[19], [20].
In parallel, the front -of-pack labeling policy and behavioral
literature provide extensive evidence that label formats affect
comprehension and choice and offer design principles for
labels as regulatory instruments [21], [22].
D. Research Gap
Despite these developments, limited research has directly
tested whether AI visual inference from FOP images can
substitute for regulated labels under realistic consumer
constraints (fast decisions, limited visibility), while also
quantifying how performance shifts across global versus local
product ecosystems. This study addresses that gap with a
constrained binary-game: two AI agents are shown only front-
of-pack images and asked to choose which of two products
contains less sugar. We chose sugar as a bounded, verifiable
proxy for nutrition inference. We evaluate accuracy across
four national contexts —Sweden, the United States (USA) ,
Kazakhstan and Australia —to test how product familiarity
and data coverage shape AI reliability and to surface
implications for trust, equity, and accountability in AI -
mediated nutrition guidance.
II. METHODS
A. Binary Sugar Game
We implemented the standard  2-Alternative Forced
Choice (2AFC) as a web-based binary-choice task (“Food-or-
Not”) [5] in which raters viewed pairs of packaged food
products using only FOP images and selected which product
contained less sugar. The task was delivered through an online
public website inspired by similar earlier food games such as
‘Scrandle’. It presents two products per trial and record s a
forced-choice response (left/right). This format does not 100%
approximate a realistic point-of-sale comparison, but it serves
effectively the purpose to compare guessing accuracies if the
number of data  points is sufficient [23]. Fig 1. shows a
screenshot of an AI agent playing the game.
B. Dataset
The dataset comprised packaged supermarket items
sampled across four national contexts: Sweden (7), the USA
(6), Australia (6), and Kazakhstan (6). Only the FOP image
for each item was used as input to the task (i.e., no nutrition
panel or ingredient list was shown to AI agents). Ground-truth
sugar content for each item was obtained from the product’s
declared nutrition information (e.g., grams of sugar per 100
g/100 ml or an equivalent standardized basis where needed).
For each trial, the “correct” answer was defined as the product
with lower declared sugar content. Figure 1 shows example
products used in the study from the Australia dataset.
USA
Prego Sauce: 8%
Noosa Yogurt: 16%
Quaker Real Medleys: 26%
Clif Bar: 31%
Kit Kat: 50%
Honey Smacks Cereal: 59%
Sweden
Köttbullar Vego: 2%
Festis Orange: 7%
Yalla Yogurt: 8%
Caesar Salad: 14%
Mighty Mozzarella Burger: 17%
Kanelbulle: 23%
GlassPinnar: 25%
Australia
Vegemite: 3%
Weetabix Original: 4%
Coles Greek Natural Yoghurt: 5%
Uncle Tobys Cheerios: 15%
Coles Tomato Ketchup: 29%
Tim Tam Original: 32%
Kazakhstan
Tan: 0%
Processed Bread Harrys: 5%
Activia Yogurt: 7%
Bun: 20%
Oreo: 44%
Nutella: 56%

Images used: https://github.com/orioli/food-or-
not/tree/main/src/assets

C. AI Agent Systems and Interaction Protocol
Two AI agent systems were evaluated on the same binary-
choice task: Strawberry (agentic browser system) and OpenAI
Atlas (vision-capable agent). Each system was instructed to
choose which product contained less sugar using only the FOP
images, mirroring th e human task framing. To reduce
contamination from within-session learning, performance was
recorded on each system’s initial pass through the trial set (as
they memorize the correct answers) . Figure 2 illustrates
OpenAI Atlas interacting with the task interface.
D. Outcome Measures and Analysis
The primary outcome was accuracy, defined as the
proportion of trials in which the rater selected the lower-sugar

product according to ground truth. Accuracy was computed
overall and stratified by national context (Sweden, USA,
Kazakhstan, Australia) and by context type (English-language
vs. non-English). Because the task is binary, chance
performance is 50%; inferential comparisons against chance
and between rater types can be conducted using binomial tests
and/or contingency-table analyses (e.g., Fisher’s exact test),
with confidence intervals reported for all accuracy estimates.
Two AI agent systems were shown a website that shows
pairs of packaged food products using only front -of-pack
images and were asked to identify which contained less sugar.
No personally identifiable information was collected, and no
sensitive data were involved.
E. Ethics
Ethical approval was granted as exempt by the
Institutional Ethics Committee.
III. RESULTS
The t wo AI agent s (Strawberry Browser and OpenAI
Atlas) were evaluated on their initial pass through on the same
task. They showed strongly context -dependent performance
rather than a uniform advantage.  Table 1 summarizes AI
accuracy by national context. For Strawberry agentic browser,
accuracy in descending order was: Australia (14/15; 93%), the
USA (13/15; 87%), and Kazakhstan (13/15; 87%), and
substantially lower in Sweden (13/21; 62%). OpenAI Agentic
browser Atlas showed a similar cross -context pattern:
Australia (15/15; 100%) and Kazakhstan (15/15; 100%)
scored perfect, followed by USA (10/15; 67%) and Sweden
(12/21; 57%). Coincidentally, when pooled across the three
non-Swedish contexts (Australia, U SA, Kazakhstan), both
agents achieved the same 40/45 (89%) accuracy; in contrast,
performance in Sweden approached chance level for both
agents (57, 62%).
To quantify this “local-context drop,” we compared each
agent’s accuracy in Swedish to their individual pooled
accuracy on non-Swedish contexts. The reduction was large
for both agents (Atlas: 89% to 57%, −32 percentage points;
Strawberry: 89% to 62%, −27 percentage points). Consistent
with this, binomial tests indicated that performance in Sweden
was not di stinguishable from chance for Atlas (12/21) and
Strawberry (13/21), whereas pooled performance outside
Sweden (40/45) was well above chance. A contingency-based
comparison of Sweden versus non-Sweden is shown in Figure
3 and Table 2.
Finally, we observed  a perfect  within-session learning
artifact: once an agent had completed the task once, repeated
play within the same session could yield near -perfect
performance, consistent with memorization of previously seen
pairs. This reinforces the importance of evaluating “f irst
exposure” performance when interpreting consumer -facing
reliability.
In Table 1, 95% confidence intervals (CI s) for accuracy
were computed assuming a binomial distribution of
correct/incorrect responses. For each country and AI agent,
accuracy was defined as p= k/n, where k is the number of
correct choices and n the number of trials. Confidence
intervals were calculated using the exact Clopper –Pearson
method.

Fig. 3. Pooled performance across global (ntrials=90) and local (ntrials=42)
contexts for the two AI agents. Error bars indicate 95% CI. The
dashed line represents the 50% chance baseline for the 2AFC task.
Error bars indicate 95% CI (Clopper–Pearson)
Table I. AI agent accuracy by country (95% CI)
Country Strawberry (Swedish) Atlas (U.S.-made) Pooled Agents (Combined)
Australia 93% [80–100] 100% [78–100] 97% [83–100]
Kazakhstan 87% [70–100] 100% [78–100] 93% [78–99]
USA 87% [70–100] 67% [43–  91] 77% [58–90]
Sweden 62% [41– 83] 57% [36–  78] 60% [43–74]

Table II. Pooled AI agent accuracy by context
Context
Correct
answers / N Accuracy CI 95%
p-value
(vs. chance)
Global
products
(Australia,
USA,
Kazakhstan) 80 / 90 88.9% [80.5–94.5] p < 0.0001***
Local
products
(Sweden) 25 / 42 59.5% [43–74.4]
p = 0.29 (Not
significant)

IV. DISCUSSION
In the global products pairs, AI agents inferred the lower-
sugar item with 88.9% accuracy. For reference, this
performance is comparable to benchmarks observed for
human users in similar tasks. However, a stark disparity
emerged in the local, unfamiliar context: when c onfronted
with Swedish products, pooled agent accuracy fell to 59.5%,
with the 95% confidence interval overlapping the 50% chance
baseline. This drop is fundamentally linked to dataset
coverage; the sensitivity to “globality” observed here aligns
with established failure modes in vision-recognition systems
and reinforces concerns regarding cultural bias in algorithmic
food classification.
These results carry significant implications for trust and
accountability. Nutritional labels are currently part of a public,
auditable infrastructure: their format is regulated, and
compliance is legally enforceable. In contrast, AI -mediated
judgments are  produced by proprietary pipelines whose
training sets and decision logics are typically opaque and free

from regulatory oversight  [24]. When consumers treat AI
outputs as authoritative, nutritional judgment shifts from
regulated disclosure to private inference, creating an
“accountability void ”. Disparities in performance across
markets or languages may remain invisible without systematic
auditing, raising urgent questions regarding algorithmic
sovereignty.
V. LIMITATIONS
This study has several limitations that should be
considered when interpreting the results. First, the evaluation
task was deliberately constrained to a binary (2AFC)
judgment of relative sugar content based solely on FOP
images. While this design enables clean, verifiable accuracy
measurement against ground truth, it does not capture the full
complexity of real-world nutritional decision-making, which
may involve multi-attribute trade-offs (e.g., fat, salt, portion
size) and non-binary choices.
Second, the number of products per national context was
modest, and the set was not intended to be statistically
representative of each country’s full retail ecosystem . As a
result, accuracy estimates should be interpreted as indicative;
future work should scale the dataset to thousands of products
per market, adopting the large-scale paradigms established by
benchmarks such as Food2K, which encompasses over 1
million images but primarily focuses on ready -to-eat dishes
[25].
Third, AI agent performance was evaluated only on first
exposure to avoid within-session memorization effects.
Fourth, the mean sugar content of the Swedish products
dataset is lower than in the other three countries’ data. Finally,
the study focused exclusively on sugar content as a bounded
nutritional attribute; results may not generalize to other
nutrients where visual cues are weaker.
VI. CONCLUSION
AI 'nutrition lens' systems can provide rapid, image-based
guidance, but our cross -context evaluation highlights that
accuracy is strongly conditioned on product familiarity and
dataset coverage. For globalized, English-language products,
p < 0.0001); however, when products are weakly represented
in training data, performance degrades to levels statistically
indistinguishable from random guessing (59.5%, p = 0.29).
These results suggest that as nutritional judgment shifts
from public, auditable labels to proprietary inference
pipelines, we risk an 'algorithmic nutrition divide' where
guidance quality varies by market and language. Evaluating
AI nutrition tools solely  on global benchmarks may
systematically overestimate their reliability in local retail
contexts. We highlight the need for auditable datasets and
evaluation benchmarks aligned with local food ecosystems.
ACKNOWLEDGMENT
Dr. Mei Yen  (NUSOM) for insightful discussions, and
Lovable AB for free credits.
REFERENCES
[1] Regulation (EU) No 1169/2011 of the European Parliament and of
the Council of 25 Oct. 2011 on the provision of food information to
consumers, vol. 304. 2011. Accessed: Jan. 22, 2026. [Online].
Available: http://data.europa.eu/eli/reg/2011/1169/oj
[2] “Language and presentation of food information - Food Safety.”
Accessed: Jan. 22, 2026. [Online]. Available:
https://food.ec.europa.eu/food-safety/labelling-and-nutrition/food-
information-consumers-legislation/language-and-presentation-food-
information_en
[3] “Guideline: sugars intake for adults and children.” Accessed: Jan. 22,
2026. [Online]. Available:
https://www.who.int/publications/i/item/9789241549028
[4] C. A. Monteiro et al., “Ultra-processed foods and human health: the
main thesis and the evidence,” The Lancet, vol. 406, no. 10520, pp.
2667–2684, Dec. 2025, doi: 10.1016/S0140-6736(25)01565-X.
[5] J. Berengueres, “Food-or-not Awareness gamification,” 2025,
Accessed: Jan. 22, 2026. [Online]. Available:
https://research.nu.edu.kz/en/publications/food-or-not-awareness-
gamification/
[6] A. J. Wu, R. Liu, S. S. Li, Y. Tsvetkov, and T. L. Griffiths, “Ads in
AI Chatbots? An Analysis of How Large Language Models Navigate
Conflicts of Interest,” Apr. 09, 2026, arXiv: arXiv:2604.08525. doi:
10.48550/arXiv.2604.08525.
[7] “Evaluating the Quality and Comparative Validity of Manual Food
Logging and Artificial Intelligence-Enabled Food Image Recognition
in Apps for Nutrition Care.” Accessed: Jan. 22, 2026. [Online].
Available: https://www.mdpi.com/2072-6643/16/15/2573
[8] E. Shonkoff et al., “AI-based digital image dietary assessment
methods compared to humans and ground truth: a systematic review,”
Ann Med, vol. 55, no. 2, p. 2273497, 2023, doi:
10.1080/07853890.2023.2273497.
[9] J. A. Davenport, “ID# 1903562 Diversifying Nutrition Databases and
Tracking Apps Using Artificial Intelligence Methods,”
Neuromodulation: Technology at the Neural Interface, vol. 28, no. 7,
Supplement, p. S62, Oct. 2025, doi: 10.1016/j.neurom.2025.08.115.
[10] T. Osadebey, S. Oyefusi, and M. Udeogu, “Addressing Artificial
Intelligence Bias through Inclusivity: A Case Study with Nigerian
Food Images,” in 2025 International Conference on Artificial
Intelligence and Digital Ethics (ICAIDE), Guangzhou, China: IEEE,
May 2025, pp. 469–473. doi:
10.1109/ICAIDE65466.2025.11189650.
[11] Q. Zhang, D. Elsweiler, and C. Trattner, “Visual Cultural Biases in
Food Classification,” Foods, vol. 9, no. 6, p. 823, Jun. 2020, doi:
10.3390/foods9060823.
[12] M. Lyu, Z. Yang, C. Chen, and J. Huang, “Does AI prefer healthy
foods? Examining value bias in large language models,” International
Journal of Gastronomy and Food Science, vol. 43, p. 101406, Mar.
2026, doi: 10.1016/j.ijgfs.2025.101406.
[13] J. Zheng, J. Wang, J. Shen, and R. An, “Artificial Intelligence
Applications to Measure Food and Nutrient Intakes: Scoping
Review,” J Med Internet Res, vol. 26, p. e54557, Nov. 2024, doi:
10.2196/54557.
[14] D. I. McCarthy, “Nutritional intelligence in the food system:
Combining food, health, data and AI expertise,” Nutr Bull, vol. 50,
no. 1, pp. 142–150, Mar. 2025, doi: 10.1111/nbu.12729.
[15] “Artificial intelligence, nutrition, and ethical issues: A mini-review -
ScienceDirect.” Accessed: Jan. 22, 2026. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S26672685230003
11?via%3Dihub
[16] T. Davies, J. C. Y. Louie, R. Ndanuko, S. Barbieri, O. Perez-Concha,
and J. H. Y. Wu, “A Machine Learning Approach to Predict the
Added-Sugar Content of Packaged Foods,” The Journal of Nutrition,
vol. 152, no. 1, pp. 343–349, Jan. 2022, doi: 10.1093/jn/nxab341.
[17] R. Daniel-Weiner, M. I. Cardel, M. Skarlinski, A. Goscilo, C.
Anderson, and G. D. Foster, “Enabling Informed Decision Making in
the Absence of Detailed Nutrition Labels: A Model to Estimate the
Added Sugar Content of Foods,” Nutrients, vol. 15, no. 4, p. 803,
Feb. 2023, doi: 10.3390/nu15040803.
[18] P. Ma et al., “UMDFood: Vision-language models boost food
composition compilation,” 2023, arXiv. doi:
10.48550/ARXIV.2306.01747.
[19] J. N. P. Markavathi, J. G. R, A. K. S, B. Roshan, and A. Bala,
“NutriScan: A Mobile Application for Health-Conscious Food
Choices,” in 2025 IEEE International Students’ Conference on
Electrical, Electronics and Computer Science (SCEECS), Bhopal,
India: IEEE, Jan. 2025, pp. 1–7. doi:
10.1109/SCEECS64059.2025.10940148.
[20] T. Silva, T. Carvalho, V. Filipe, L. Gonçalves, and A. Sousa,
“Nutritional Insight: Using OCR to Decode Food Labels for Better
Health,” in 2024 International Conference on Graphics and
general-purpose AI agents achieve high accuracy (88.9%,

Interaction (ICGI), Nov. 2024, pp. 1–8. doi:
10.1109/ICGI64003.2024.10923764.
[21] C. A. Roberto et al., “The Influence of Front-of-Package Nutrition
Labeling on Consumer Behavior and Product Reformulation,” Annu
Rev Nutr, vol. 41, pp. 529–550, Oct. 2021, doi: 10.1146/annurev-
nutr-111120-094932.
[22] X. Li, “Understanding the Impacts of Front-of-pack Labels on
Consumer Product Evaluation and Purchase Decisions: A Systematic
Review,” presented at the Proceedings of the 4th International
Conference on Informatization Economic Development and
Management, IEDM 2024, February 23–25, 2024, Kuala Lumpur,
Malaysia, May 2024. Accessed: Jan. 22, 2026. [Online]. Available:
https://eudl.eu/doi/10.4108/eai.23-2-2024.2345925
[23] L. T. DeCarlo, “On a signal detection approach to m-alternative
forced choice with bias, with maximum likelihood and Bayesian
approaches to estimation,” Journal of Mathematical Psychology, vol.
56, no. 3, pp. 196–207, Jun. 2012, doi: 10.1016/j.jmp.2012.02.004.
[24] J. Berengueres, “How to Regulate Large Language Models for
Responsible AI,” IEEE Transactions on Technology and Society,
2024.
[25] W. Min et al., “Large Scale Visual Food Recognition,” IEEE Trans.
Pattern Anal. Mach. Intell., vol. 45, no. 8, pp. 9932–9949, Aug. 2023,
doi: 10.1109/TPAMI.2023.3237871.
