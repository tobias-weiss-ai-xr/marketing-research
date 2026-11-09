---
title: Rethinking Sales Lead Scoring with LLM-based Hierarchical Preference Ranking
url: https://arxiv.org/abs/2606.04387
category: ai-marketing
subcategory: empirical
date: 2026-06
venue: ''
authors:
- Chenyu Zhang
- Yiwen Liu
- Yin Sun
- Xinyuan Zhang
- Yuji Cao
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.04387
pages: 8
chars: 27684
fetched_at: '2026-11-08T13:26:21+00:00'
kb_version: 1
---

# Rethinking Sales Lead Scoring with LLM-based Hierarchical Preference Ranking

RETHINKINGSALESLEADSCORING WITHLLM-BASED
HIERARCHICALPREFERENCERANKING ∗
Chenyu Zhang, Yiwen Liu, Yin Sun, Xinyuan Zhang, Yuji Cao, Junming Jiao, Juyi Qiao
Intelligent Business Team, Li Auto Inc.
ABSTRACT
Sales lead conversion in high-stakes domains (e.g., automotive, real estate) differs fundamentally from
e-commerce recommendation due to prolonged decision cycles and multi-stage funnels. Traditional
lead scoring methods—rule-based scorecards, machine learning, or pointwise CTR models—face
severe challenges: sparse supervision, a semantic gap in unstructured CRM logs, and inability
to capture relative lead priority. While Large Language Models(LLMs) offer superior semantic
understanding of customer interactions, general-purpose LLMs are ill-suited for lead ranking: they
generate text rather than comparable scores, and lack alignment with the hierarchical priorities of
sales funnels. We introduce an LLM-based discriminative framework for sales lead scoring, which
supports joint modeling of structured CRM features and unstructured customer interactions. On top of
this framework, we propose HPRO (Hierarchical Preference Ranking Optimization), which augments
sales lead scoring with a hierarchical preference ranking objective. HPRO employs a margin-aware
Bradley-Terry formulation to transform sparse binary labels into dense, funnel-aware preference
pairs, enabling lead scoring to leverage both pointwise and pairwise supervision. Experiments on
large-scale data from a leading NEV brand demonstrate state-of-the-art classification (AUC 0.8161)
and ranking performance (+39.7% precision among top-ranked leads). A 132-day online A/B test
validates 9.5% sales volume uplift, confirming real-world commercial impact.
KeywordsSales Lead Scoring·Large Language Models·Preference Optimization·Learning to Rank
1 Introduction
Lead scoring—ranking sales leads by conversion likelihood—is central to modern Customer Relationship Management
(CRM) [1, 2]. The commercial importance of this task is reflected in substantial industry investment: platforms such as
Salesforce Einstein, SAP CRM, and Act-On deploy machine learning-based scoring systems to prioritize high-potential
leads [3, 4, 5]. Formally, lead scoring can be modeled as a prediction task akin to Click-Through Rate (CTR) estimation:
given a lead’s profile and interaction history, the objective is to estimate the probability of conversion [6, 7].
In standard recommendation scenarios, user feedback (clicks, views) arrives within seconds of an impression, providing
dense supervision for model training [8, 9]. However, long-chain sales—prevalent in domains such as automotive, real
estate, and enterprise B2B—involve extended decision cycles spanning weeks or months [10, 11]. Directly transplanting
recommendation paradigms to this setting reveals fundamental incompatibilities.
A typical automotive purchase progresses through multiple funnel stages: Lead → Telemarketing → Store Visit → Test
Drive → Order [3, 12, 13]. This creates a critical challenge: the supervision signal is sparse not because positive labels
are rare, but because the signal indicating conversion intent is diffused across a long decision horizon. A customer
who completed a test drive and one who merely browsed the website are both labeled as “non-converted” if neither
ultimately purchases—yet their intent levels differ substantially. Standard binary supervision conflates these cases,
treating qualitatively different negatives as identical and discarding valuable process information [14, 15].
Existing methods are ill-suited to this setting. Rule-based scorecards depend on expert heuristics that scale poorly [16,
17]. Modern CRM platforms (e.g., Salesforce Einstein) have adopted machine learning methods that excel at structured
∗Email address: cyzhang57@outlook.com
arXiv:2606.04387v1  [cs.IR]  3 Jun 2026

Running Title for Header
features but optimize only terminal lock-in labels [ 18, 19]. Given the structural similarity to conversion prediction,
deep CTR models—DeepFM [9], DCN [20], xDeepFM [21], AutoInt [22]—offer a natural alternative. However, these
models assume dense, immediate feedback and encode text as shallow embeddings, failing to capture semantic signals
in sales dialogues.
Large Language Models (LLMs) offer superior semantic understanding and can interpret the rich, unstructured signals
embedded in CRM logs—such as customer sentiment and implicit intent [23, 24]. However, general-purpose LLMs are
misaligned with lead ranking requirements. Recent benchmarks such as CRMArena [25, 26] reveal that LLMs struggle
with CRM tasks requiring structured reasoning over business objects and adherence to domain-specific rules. More
fundamentally, generative models produce text rather than actionable scores—they lack mechanisms for comparable
ranking outputs. This motivates a discriminative design: augmenting an LLM backbone with task-specific heads that
output scalar scores amenable to ranking and calibration.
We propose HPRO (Hierarchical Preference Ranking Optimization), a framework that transforms sparse terminal
supervision into dense, funnel-aware preference signals. The key insight is that while binary labels are uninformative
about intermediate intent, the sales funnel itself encodes a natural preference hierarchy: test-drive customers are more
engaged than phone-only inquiries. HPRO reformulates lead scoring as a Learning-to-Rank problem, constructing
hierarchical preference pairs across funnel stages (e.g., Test Drive ≻ Store Visit ≻ Phone Call) and optimizing a
margin-aware Bradley-Terry objective [27] where margins encode business priors about preference strength. This
formulation draws inspiration from recent advances in preference optimization for LLMs [ 28, 29], adapting these
techniques to the sales domain.
This paper makes three contributions:
• We introduce a discriminative LLM architecture that combines a semantic backbone with pointwise (calibration)
and pairwise (ranking) heads, enabling joint modeling of tabular and textual features for sales lead scoring.
• We propose HPRO, which converts sparse binary supervision into hierarchical preference pairs derived from
funnel stages. The margin-aware formulation explicitly injects domain knowledge about stage importance into
the optimization objective.
• Experiments on leads from a leading NEV brand show HPRO achieves state-of-the-art AUC of 0.8161 (+2.3%
over baselines). A rigorous 5-month online A/B test demonstrates9.5% sales volume uplift, validating
real-world commercial impact.
2 Related Work
Lead Scoring.Traditional lead scoring relies on rule-based scorecards [ 15] with manually assigned weights, prone to
subjective bias [3]. Machine learning methods—Logistic Regression, Decision Trees [19], and ensemble models like
XGBoost [17, 16]—improved accuracy on structured CRM data. Modern platforms such as Salesforce Einstein deploy
ML-based scoring [18], while some work explores funnel-aware analysis [12]. However, these approaches optimize
only terminal labels, failing to capture semantic signals in dialogues or leverage intermediate supervision in long-chain
sales.
Deep CTR Models.Deep CTR models—DeepFM [ 9], DCN [20], xDeepFM [21], AutoInt [22]—have achieved
strong results in recommendation by modeling high-order feature interactions. Graph-based extensions [30, 31] further
capture entity relations. However, these methods assume dense, immediate feedback (clicks/views) unavailable in
long-chain sales, and encode text as shallow embeddings, losing semantic nuance critical for distinguishing customer
intent.
LLMs for CRM.LLMs have transformed CRM by enabling semantic understanding of unstructured interactions [ 23,
24]. Yet benchmarks like CRMArena [25] reveal that general-purpose LLMs struggle with structured reasoning over
business objects and domain-specific rules. More fundamentally, generative LLMs lack mechanisms for producing
ranking scores aligned with sales funnel hierarchy. This motivates our discriminative design: asLLR augments an LLM
backbone with task-specific heads, while HPRO injects funnel-aware preferences via margin-based optimization.
Comparison with Preference Optimization Methods.Recent preference optimization methods such as DPO [ 28]
and ORPO [29] are designed to align generative models with human preferences in text generation. HPRO differs from
these approaches in three aspects: it targets business ranking effectiveness rather than generation quality, constructs
preference pairs automatically from funnel stages instead of manual annotations, and introduces hierarchical margins
to encode domain-specific business priorities. HPRO also differs from traditional learning-to-rank methods, which
2

Running Title for Header
Sales Dialogue
Unstructured Text Features
Type C:
Type B:
…
Type A:
Hierarchical-wiseSamples
User Feature Sales Record
In CRM Systerm
StructuredFeatures
Feature Processing & Hierarchical Sampling
…
B
A
Matrix BMatrix A
Trainable LoRA Adapter
Qwen Backbone
Frozen Transformer Layers
Inject LoRA matrix
LoRA Fine-tuning Details
𝐹𝑢𝑛𝑛𝑒𝑙	𝐴𝑙𝑖𝑔𝑛𝑚𝑒𝑛𝑡
Margin m
LHPRO(Pairwise Loss)
𝑅𝑒𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎𝑡𝑖𝑜𝑛	𝐿𝑒𝑎𝑟𝑛𝑖𝑛𝑔
LCE (Semantic Loss)
𝐿𝑜𝑐𝑘	𝑃𝑟𝑒𝑑𝑖𝑐𝑡𝑖𝑜𝑛
LBCE (Pointwise Loss)
Optimization Objectives
>
Total
Loss
∑
Pairwise
Head
Pointwise
Head
[CLS]
Special token
Text
Embedding HiddenState
Candidate
size
Feature dim
Transformer
Structured
FeaturesEmbedding
𝐿!"#=−1 𝑁&[𝑦$𝑙𝑜𝑔𝜎𝑠%&$’(𝑥$ + )
$*+
1−𝑦$log	(1−𝜎(𝑠%&$’((𝑥$)))]
𝐿"#=−&𝑙𝑜𝑔𝑃∅-.’(𝑣(/0-.(|𝑥$)
’
$*+
𝑙𝑜𝑔𝜎(𝑠%/$0𝑥1−𝑠%/$0𝑥2−𝑚)
𝑆(𝑥!)
𝑆(𝑥")
Figure 1: Overview of the proposed framework. Left: Feature processing and hierarchical sampling from structured
and unstructured inputs. Middle: LLM backbone with LoRA adaptation. Right: Three optimization objectives
corresponding to the triple-head mechanism.
typically assume either explicit relevance labels or uniformly weighted pairwise preferences, whereas our setting
provides only sparse terminal labels and funnel-derived preference strengths.
3 Methodology
3.1 Problem Formulation
We formulate lead scoring as aLearning-to-Rankproblem augmented with probability calibration. Let D=
{(xi, yi)}N i=1 denote the dataset, where each sample xi = (Ti, Li) comprises tabular features Ti (e.g., demographics,
behavioral statistics) and dialogue features Li (e.g., sales conversation transcripts). The binary label yi ∈ {0,1}
indicates whether final conversion (order lock-in) occurred.
3.2 Model Architecture
To bridge semantic understanding with actionable ranking, we propose a discriminative LLM architecture that augments
a pre-trained language model with task-specific heads. We term this architecture asLLR (LLM-based Lead Ranking in
Auto Sales), illustrated in Figure 1.
Backbone with LoRA.We employ a Large Language Model as the encoder to extract high-dimensional semantic
representations htext ∈R d from the final hidden state. We utilize Low-Rank Adaptation (LoRA) [32] for parameter-
efficient fine-tuning.
Triple-Head Mechanism.Three task-specific heads branch from the backbone’s final hidden state:
1. Semantic Head( ϕgen): The LLM’s original vocabulary projection layer (Rd →R |V| ), retained for next-token
prediction. This head serves as a representation regularizer, preventing catastrophic forgetting during domain
adaptation.
2. Pointwise Head( ϕpoint): A linear projection (Rd →R ) outputting a scalar score spoint(x) for conversion
probability estimation.
3. Pairwise Head( ϕpair): A separate linear projection (Rd →R ) outputting a ranking score spair(x), optimized
via HPRO for relative ordering across funnel stages.
3

Running Title for Header
3.3 Hierarchical Preference Ranking Optimization
Standard pointwise objectives treat all non-converted samples as identical negatives, discarding valuable process
information. We propose HPRO to construct dense supervision from funnel hierarchy.
3.3.1 Funnel-Aware Preference Construction
We define a funnel hierarchy F={L lock, Ldrive, Lcall, Ldef eat} ordered by engagement depth, where Llock denotes
order lock-in andL def eatdenotes lost leads. A mappingΦ :X → Fassigns each sample to its funnel stage.
We construct preference pairs(x w, xl)whereΦ(x w)≻Φ(x l), categorized into three tiers with associated margins:
•Global Dominance(P global, marginm g): Lock-in vs. Defeat—the strongest preference signal.
•Key Action(P key, marginm k): Test Drive vs. No Drive—a critical intermediate indicator.
•Soft Signal(P sof t, marginm s): Long Call vs. Short Call—a dense but noisy behavioral signal.
3.3.2 Margin-Aware Bradley-Terry Objective
HPRO extends the Bradley-Terry model [27] by injecting funnel-derived margins as probabilistic constraints. For a
preference pair(x w, xl)with marginm, the preference probability is:
P(x w ≻x l|m) =σ(s pair(xw)−s pair(xl)−m),(1)
whereσ(·)is the sigmoid function. The HPRO loss maximizes the log-likelihood:
LHP RO=−E (xw,xl,m)∼Dpair [logσ(s pair(xw)−s pair(xl)−m)].(2)
The margin m encodes business priors: larger margins for global dominance pairs enforce clearer separation in the
score space, while smaller margins for soft signals allow finer discrimination. In our experiments, we set mg = 1.0,
mk = 0.5, andm s = 0.1.
3.4 Training Objective
The total objective jointly optimizes all three heads:
Ltotal =αL BCE +λ 1LHP RO+λ 2LCE .(3)
Pointwise Loss (L BCE ).Binary cross-entropy for conversion probability calibration:
LBCE =− 1 N
NX
i=1
[yi logσ(s point(xi)) + (1−y i) log(1−σ(s point(xi)))].(4)
Pairwise Loss (L HP RO).As defined in Eq. (2), optimizing relative ordering based on hierarchical priors.
Semantic Loss (LCE ).Cross-entropy for QA-style target prediction, preserving the backbone’s linguistic capabilities:
LCE =− 1 N
NX
i=1
logP ϕgen (vtarget|xi),(5)
wherev target is the target answer token (e.g., “Yes” or “No” for conversion prediction).
Optimization Strategy.We observe that purely discriminative losses lead to overfitting; LCE acts as a regularizer
preserving linguistic capability. We apply differential learning rates: task heads use the base rate 5×10 −5, while
backbone (LoRA) parameters employ a 20× lower rate to prevent overfitting. The loss weights α= 2.0 , λ1 = 1.0, and
λ2 = 0.5emphasize pointwise calibration while maintaining ranking and regularization objectives.
4 Experiments
To validate the proposed HPRO framework, we conducted a multi-stage evaluation progressing from offline benchmark-
ing to mechanism analysis, and finally to real-world deployment.
4

Running Title for Header
4.1 Experimental Setup
Datasets.We evaluate on two proprietary datasets from a leading New Energy Vehicle (NEV) retail system, collected
from different operational periods:
• Benchmark Dataset(340k samples, 1.45% positive): An earlier collection enabling fair comparison with
CTR baselines under consistent feature engineering.
• Industrial Dataset(6.14M samples, 1.33% positive): A recent full-scale production dataset with richer
intermediate behavioral signals (e.g., test drives, call durations) required for training the HPRO module.
Both datasets are split 7:3 (train/test) with strict temporal ordering to prevent look-ahead bias.
Baselines.We compare asLLR against six industrial CTR models: Wide&Deep [ 8], DeepFM [9], xDeepFM [21],
DCN [20], DCN-M [33], and AutoInt [22]. All baselines share consistent hyperparameters (batch size 256, embedding
dimension 8).
Implementation.We fine-tune Qwen1.5-1.8B (Scenario 1) and Qwen2.5-1.5B (Scenario 2) with LoRA. Dialogues
are truncated to 2,000 tokens. Full hyperparameters and training scripts are provided in our code repository.
Table 1: Results on Benchmark Dataset. Upper: comparison with CTR baselines. +htext denotes injection of
asLLR-extracted textual embeddings. Lower: ablation on asLLR components.
Model Embedding AUC Gain
Upper: Comparison with CTR baselines
W&D [8] - 0.7860 -
DeepFM [9] - 0.7917 -
xDeepFM [21] - 0.7808 -
DCN [20] - 0.7862 -
DCN-M [33] - 0.7900 -
AutoInt [22] - 0.7896 -
W&D [8]+h text 0.7951 +0.0091
DeepFM [9]+h text 0.7976 +0.0059
xDeepFM [21]+h text 0.7895 +0.0087
DCN [20]+h text 0.7911 +0.0049
Lower: Ablation on asLLR components
asLLR (Base) - 0.7921 -
asLLR +L CE - 0.8081 -
asLLR + HPRO (Full)-0.8161-
4.2 Scenario 1: Comparative Benchmarking
This Scenario investigates whether the LLM backbone can bridge the semantic gap in unstructured CRM logs better
than feature interaction-based models. Table 1 presents the results.
Superiority of LLM Backbone.The base asLLR model achieves an AUC of 0.7921, surpassing the strongest baseline
(DeepFM: 0.7917). This corroborates that pre-trained knowledge within the LLM captures latent customer intents more
effectively than shallow embedding lookups.
Embedding Transferability.To quantify representation quality, we inject the textual embedding htext extracted
from asLLR into traditional baselines. As shown in Table 1, this injection yields consistent performance lifts across
all baselines (avg. +0.007 AUC), confirming that asLLR learns representations complementary to traditional tabular
features.
Ablation on asLLR Variants.The lower section of Table 1 isolates component contributions. Adding semantic
regularization (LCE ) improves AUC to 0.8081, validating that the auxiliary language modeling Scenario prevents
catastrophic forgetting. The full model with HPRO achieves0.8161, a +3.0% improvement over the base model.
5

Running Title for Header
Table 2: Ranking effectiveness on the industrial dataset. P@K% and R@5.0% denote precision and recall at top K% (or
5.0%) of ranked leads. Relative Lift is computed with respect to asLLR (w/o HPRO).
Method AUC Precision Recall P@0.1% P@1.0% R@5.0%
Funnel+Recency 0.6332 3.28% 1.50% 9.23%
Funnel+CTR (DeepFM, Two-stage) 0.6898 7.21% 1.90% 18.76%
Funnel+CTR (DeepFM, Direct) 0.7382 14.41% 10.14% 21.85%
asLLR (w/o HPRO) 0.7491 18.44% 11.56% 23.94%
asLLR (w/ HPRO) 0.7583 25.76% 13.33% 25.18%
Relative Lift +1.2% +39.7%+15.3% +5.2%
4.3 Scenario 2: Ranking Effectiveness on Industrial Data
We include three industrial baselines to evaluate different ways of incorporating funnel information into lead prioriti-
zation: “Funnel+Recency”, a rule-based heuristic that ranks leads by funnel stage and then recency; “Funnel+CTR
(DeepFM, Two-stage)”, which first groups leads by funnel stage and then applies DeepFM within each stage; and
“Funnel+CTR (DeepFM, Direct)”, which treats funnel stage as an explicit input feature and directly predicts a ranking
score with DeepFM. As shown in Table 2, simple heuristic ranking is clearly insufficient for this task: Funnel+Recency
achieves only 0.6332 AUC and 3.28% P@0.1%. Moreover, the two-stage design underperforms direct Funnel+CTR
ranking (0.6898 vs. 0.7382 AUC), suggesting that funnel stage should not be imposed as a hard ranking constraint.
Compared with asLLR (w/o HPRO), the full model improves AUC from 0.7491 to 0.7583 and increases P@0.1% from
18.44% to 25.76%, corresponding to a relative improvement of 39.7%. It also outperforms Funnel+CTR (DeepFM,
Direct), the strongest industrial baseline in our comparison, whose P@0.1% is 14.41%. These gains are especially
important in practice because sales teams can only follow up a very limited fraction of leads, making precision at
the very top of the ranked list a key determinant of operational efficiency. Overall, the results suggest that funnel
information is most effective when used as structured preference supervision rather than as a rigid ranking rule.
0 25 50 75 100 125
Date
0.0
0.2
0.4
0.6
0.8
1.0Accumulated Sales
Experimental Group
Control Group
Difference Value
0.0
0.2
0.4
0.6
0.8
1.0
Difference Value
Figure 2: Cumulative conversion rates (left axis) and relative difference (right axis, shaded) over 132 days. Stable 9.5%
gap validates HPRO’s effectiveness
6

Running Title for Header
4.4 Online Performance Validation
We conducted a province-wide A/B test across all sales operations in a single Chinese province (anonymized) for
132 days. Sales specialists were stratified into two groups with equivalent baselines: a control group using traditional
CTR-based lead ranking and an experimental group using HPRO-based recommendations. The experiment employed
stratified sampling across four sales capability tiers and 7/14/30-day lock-in counts (lock-ins) as the primary balancing
metric and lead follow-up volumes as a secondary factor. Figure 2 shows a 9.5% relative uplift in lead conversion
(two-sided t-test,p <0.001), validating HPRO’s real-world sales impact.
5 Conclusion
We introduce a discriminative LLM framework for lead scoring in long-chain sales scenarios. Our key contribution,
HPRO, transforms sparse binary supervision into dense, funnel-aware preference signals via a margin-aware Bradley-
Terry objective. Experiments on large-scale NEV retail data demonstrate state-of-the-art classification (AUC 0.8161)
and ranking performance (+39.7% P@0.1%). A 132-day online A/B test validates 9.5% sales volume uplift, confirming
real-world commercial impact.
Although our experiments focus on automotive sales, the proposed framework is applicable to other long-horizon sales
domains whenever intermediate customer actions form a meaningful engagement hierarchy. In such cases, the stage
definitions and margin settings can be adapted to domain-specific business processes.
References
[1] Russell S Winer. A framework for customer relationship management.California management review, 43(4):89–
105, 2001.
[2] Adrian Payne and Pennie Frow. A strategic framework for customer relationship management.Journal of
marketing, 69(4):167–176, 2005.
[3] Migao Wu, Pavel Andreev, and Morad Benyoucef. The state of lead scoring models and their impact on sales
performance.Information Technology and Management, 25(1):69–98, 2024.
[4] SAP. Lead Scoring in SAP CRM, 2022. Accessed: 2025-05-20.
[5] Act-On. AI Predictive Lead Scoring, 2023. Accessed: 2025-05-20.
[6] Paolo Guenzi and Johannes Habel. Mastering the digital transformation of sales.California Management Review,
62(4):57–85, 2020.
[7] Jamie P Monat. Industrial sales lead conversion modeling.Marketing Intelligence & Planning, 29(2):178–194,
2011.
[8] Heng-Tze Cheng, Levent Koc, Jeremiah Harmsen, Tal Shaked, Tushar Chandra, Hrishi Aradhye, Glen Anderson,
Greg Corrado, Wei Chai, Mustafa Ispir, et al. Wide & deep learning for recommender systems. InProceedings of
the 1st workshop on deep learning for recommender systems, pages 7–10, 2016.
[9] Huifeng Guo, Ruiming Tang, Yunming Ye, Zhenguo Li, and Xiuqiang He. Deepfm: a factorization-machine based
neural network for ctr prediction.arXiv preprint arXiv:1703.04247, 2017.
[10] Peter C Verhoef, Thijs Broekhuizen, Yakov Bart, Abhi Bhattacharya, John Qi Dong, Nicolai Fabian, and Michael
Haenlein. Digital transformation: A multidisciplinary reflection and research agenda.Journal of business research,
122:889–901, 2021.
[11] Niladri Syam and Arun Sharma. Waiting for a sales renaissance in the fourth industrial revolution: Machine
learning and artificial intelligence in sales research and practice.Industrial marketing management, 69:135–146,
2018.
[12] Richard Conde. Necessary condition analysis for sales funnel optimization.Journal of marketing analytics, pages
1–13, 2025.
[13] L Boogar. The three stages of lead scoring: Lambs, ducks & kudus. the madkudu blog post, 2019.
[14] Juan Pablo Usuga Cadavid, Samir Lamouri, and Bernard Grabot. Trends in machine learning applied to demand &
sales forecasting: A review. InInternational conference on information systems, logistics and supply chain, 2018.
[15] D McDonnell. The evolution from traditional to predictive lead scoring. demand gen report, 2019.
[16] Laura González-Flores, Jessica Rubiano-Moreno, and Guillermo Sosa-Gómez. The relevance of lead prioritization:
a b2b lead scoring model based on machine learning.Frontiers in Artificial Intelligence, 8:1554325, 2025.
7

Running Title for Header
[17] Mateusz Mazur, Ondrej Stopka, Mária Stopková, Jiˇrí Hanzl, Anna Borucka, and Robert Czerniak. Assessing
the success of automotive sales transactions using selected machine learning algorithms.Applied Sciences,
15(21):11562, 2025.
[18] Migao Wu, Pavel Andreev, and Morad Benyoucef. Smart sales: amplifying the power of predictive lead scoring in
b2b sales. 2024.
[19] Raphael Couronné, Philipp Probst, and Anne-Laure Boulesteix. Random forest versus logistic regression: a
large-scale benchmark experiment.BMC bioinformatics, 19(1):270, 2018.
[20] Ruoxi Wang, Bin Fu, Gang Fu, and Mingliang Wang. Deep & cross network for ad click predictions. In
Proceedings of the ADKDD’17, pages 1–7. 2017.
[21] Jianxun Lian, Xiaohuan Zhou, Fuzheng Zhang, Zhongxia Chen, Xing Xie, and Guangzhong Sun. xdeepfm:
Combining explicit and implicit feature interactions for recommender systems. InProceedings of the 24th ACM
SIGKDD international conference on knowledge discovery & data mining, pages 1754–1763, 2018.
[22] Weiping Song, Chence Shi, Zhiping Xiao, Zhijian Duan, Yewen Xu, Ming Zhang, and Jian Tang. Autoint:
Automatic feature interaction learning via self-attentive neural networks. InProceedings of the 28th ACM
international conference on information and knowledge management, pages 1161–1170, 2019.
[23] Erik Brynjolfsson, Danielle Li, and Lindsey Raymond. Generative ai at work.The Quarterly Journal of Economics,
140(2):889–942, 2025.
[24] Shakked Noy and Whitney Zhang. Experimental evidence on the productivity effects of generative artificial
intelligence.Science, 381(6654):187–192, 2023.
[25] Kung-Hsiang Huang, Akshara Prabhakar, Sidharth Dhawan, Yixin Mao, Huan Wang, Silvio Savarese, Caiming
Xiong, Philippe Laban, and Chien-Sheng Wu. Crmarena: Understanding the capacity of llm agents to perform
professional crm tasks in realistic environments. InProceedings of the 2025 Conference of the Nations of the
Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1:
Long Papers), pages 3830–3850, 2025.
[26] Kung-Hsiang Huang, Akshara Prabhakar, Onkar Thorat, Divyansh Agarwal, Prafulla Kumar Choubey, Yixin Mao,
Silvio Savarese, Caiming Xiong, and Chien-Sheng Wu. Crmarena-pro: Holistic assessment of llm agents across
diverse business scenarios and interactions.arXiv preprint arXiv:2505.18878, 2025.
[27] Ralph Allan Bradley and Milton E Terry. Rank analysis of incomplete block designs: I. the method of paired
comparisons.Biometrika, 39(3/4):324–345, 1952.
[28] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and Chelsea Finn. Direct
preference optimization: Your language model is secretly a reward model.Advances in neural information
processing systems, 36:53728–53741, 2023.
[29] Jiwoo Hong, Noah Lee, and James Thorne. Orpo: Monolithic preference optimization without reference model.
arXiv preprint arXiv:2403.07691, 2024.
[30] Zonghan Wu, Shirui Pan, Fengwen Chen, Guodong Long, Chengqi Zhang, and Philip S Yu. A comprehensive
survey on graph neural networks.IEEE transactions on neural networks and learning systems, 32(1):4–24, 2020.
[31] Haiyang Yu, Limei Wang, Bokun Wang, Meng Liu, Tianbao Yang, and Shuiwang Ji. Graphfm: Improving large-
scale gnn training via feature momentum. InInternational conference on machine learning, pages 25684–25701.
PMLR, 2022.
[32] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen,
et al. Lora: Low-rank adaptation of large language models.ICLR, 1(2):3, 2022.
[33] Ruoxi Wang, Rakesh Shivanna, Derek Cheng, Sagar Jain, Dong Lin, Lichan Hong, and Ed Chi. Dcn v2: Improved
deep & cross network and practical lessons for web-scale learning to rank systems. InProceedings of the web
conference 2021, pages 1785–1797, 2021.
8
