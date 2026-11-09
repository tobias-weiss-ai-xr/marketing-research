---
title: 'Large Behavior Model: A Promptable Digital Twin of the Retail Customer'
url: https://arxiv.org/abs/2607.06993
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Wachiravit Modecrua
- Krittin Pachtrachai
- Touchapon Kraisingkorn
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.06993
pages: 17
chars: 44994
fetched_at: '2026-11-08T13:21:46+00:00'
kb_version: 1
---

# Large Behavior Model: A Promptable Digital Twin of the Retail Customer

Large Behavior Model: A Promptable Digital Twin of
the Retail Customer
Wachiravit Modecrua, Krittin Pachtrachai, Touchapon Kraisingkorn
Amity Research and Application Center (ARAC),
Amity AI Holdings Co., Ltd.
{wachiravit, krittin, touchapon}@amity.co
July 13, 2026
Abstract
Customer behavior modeling underpins recommendation, marketing, and decision support,
yet existing approaches either optimize predictive accuracy without explaining decisions or sim-
ulate users without grounding them in real behavioral data. We present the Large Behavioral
Model (LBM) that learns customer decision making directly from large-scale retail transactions
through a unified Person–Environment formulation. Customer state is represented by a behav-
ioral profile derived from historical purchases, while product context is incorporated through
retrieval-augmented generation. The model is trained using continued pre-training on verbalized
behavioral data, supervised fine-tuning for decision generation, and reinforcement learning with
verifiable rewards for evidence-based calibration.
We evaluate the proposed framework on purchase prediction, hard-negative discrimination,
basket completion, promotion response, and cross-domain voucher redemption. The model con-
sistently outperforms frontier general-purpose language models on in-domain retail tasks while
demonstrating strong zero-shot and fine-tuned transfer across retailers and decision domains.
Ablation studies show that continued pre-training is the primary driver of behavioral generaliza-
tion, retrieval is most effective when applied during both training and inference, and reinforce-
ment learning improves reliance on explicit behavioral evidence over generic language-model
priors. These results demonstrate that behavioral knowledge encoded in transaction histories
can be effectively learned by language models, providing a scalable foundation for customer
digital twins and behavior simulation.
1 Introduction
Understanding and predicting human decision-making is a long-standing problem in fields in-
cluding economics, marketing, recommender systems, and artificial intelligence. Accurate behav-
ioral models enable a wide range of applications, such as personalized recommendation, demand
forecasting, promotion planning, pricing optimization, and market research [1–3]. Despite decades
of research, faithfully modeling the behavior of an individual remains challenging because decisions
arise from the interaction between relatively stable personal preferences and the context in which
choices are made. This perspective is consistent with Lewin’s field theory, which characterizes
behavior as a function of both the person and the environment [4]. Consequently, models that
capture only population-level patterns often fail to explain why two seemingly similar customers
make different decisions under the same circumstances.
1
arXiv:2607.06993v2  [cs.AI]  10 Jul 2026

In retail, this challenge is particularly evident. Large retailers routinely make pricing, pro-
motion, and assortment decisions for millions of customers, yet their understanding of customer
preferences is still largely informed by surveys, focus groups, and consumer panels [3,5]. Although
these methods remain indispensable in marketing research, they are expensive, slow to update, and
typically cover only a small fraction of the customer population. More importantly, stated pref-
erences collected through questionnaires often differ from revealed preferences observed through
actual purchasing behavior, motivating the increasing use of transaction data for behavioral mod-
eling [6]. Consequently, retailers possess abundant behavioral data but relatively limited tools for
transforming those observations into faithful simulations of individual customer decisions.
To address this limitation, previous research has developed a wide range of behavioral mod-
els. Classical discrete choice models estimate purchasing probabilities from utility-maximization
principles [1,2], while recommender systems and sequential recommendation models learn user rep-
resentations from historical interactions to predict future purchases [7–12]. These approaches have
achieved considerable success in tasks such as purchase prediction, recommendation, and sequential
decision modeling. However, they are generally optimized for a single downstream task, requiring
separate models for recommendation, promotion response, basket completion, demand forecasting,
and related applications. As a result, they do not provide a unified behavioral model capable of
answering diverse questions about the same customer.
Recent advances in large language models (LLMs) suggest a different direction. Modern foun-
dation models exhibit strong reasoning, instruction-following, and in-context learning capabilities,
allowing a single model to perform a wide variety of tasks through natural-language prompting
alone [13–16]. This flexibility has inspired a growing body of research on using LLMs to simulate
human behavior, including social interactions, survey responses, economic decision making, and
online shopping behaviors [17–21]. More recent work has explored personalized shopping agents
through reinforcement learning and behavioral datasets [22,23]. Despite these promising devel-
opments, existing approaches predominantly represent individuals using demographic information,
manually designed personas, or synthetic profiles [24–26]. While these representations capture
broad population characteristics, they contain limited evidence of an individual’s actual behav-
ioral history. Consequently, simulated responses often reflect the prior knowledge encoded in the
foundation model rather than the behavioral patterns exhibited by the individual being simulated,
leading to a persistent gap between simulated and real-world behavior [27–29].
Recent work has also explored personalizing language models through user representations and
embeddings to better capture user-specific preferences [30–32]. However, these approaches focus
primarily on improving recommendation or personalization rather than faithfully simulating indi-
vidual decision-making across diverse behavioral tasks.
This paper investigates a simple but fundamental question:Can language models become faithful
simulators of individual consumer behavior when grounded in longitudinal behavioral evidence rather
than generic language-model priors?
We propose theLarge Behavior Model (LBM), a language-model framework for person-
alized behavioral simulation that grounds customer decisions in two complementary sources of
information: persistent behavioral evidence derived from historical transactions and the current
decision environment. Inspired by Lewin’s formulation that behavior emerges from the interaction
between the person and the environment [4], we model customer behavior as
B=f(P,E),(1)
2

wherePdenotes a customer’s persistent behavioral representation learned from longitudinal
purchasing history, andErepresents the products and contextual information available at the time
of decision. In LBM, the behavioral representation is learned through lightweight personalization
modules, while contextual information is supplied dynamically through retrieval-augmented gener-
ation (RAG) [33]. This explicit separation allows the same underlying language model to simulate
a broad range of customer behaviors—including purchase prediction, basket completion, promotion
response, market survey answering, and review generation—without training separate models for
each task.
Extensive experiments on large-scale retail transaction data demonstrate that grounding lan-
guage models in longitudinal behavioral evidence substantially improves customer-level decision
simulation. Across multiple behavioral tasks, LBM consistently outperforms frontier foundation
models while generalizing across retailers, product catalogs, and application scenarios. These re-
sults suggest that behavioral evidence provides a stronger foundation for personalized decision
simulation than relying solely on the generic priors encoded in large language models. Moreover,
because personalization is achieved through lightweight behavioral adaptation rather than separate
models for individual customers, the proposed framework scales efficiently to millions of users while
remaining practical for self-hosted deployment. The contributions of this work are summarized as
follows.
Contributions
1.A formulation for personalized behavioral simulation.We formulate customer behavior
as the interaction between persistent behavioral characteristics and the decision environment,
extending classical behavioral theory to language-model-based simulation and providing a uni-
fied framework for modeling diverse customer behaviors.
2.The Large Behavior Model (LBM).We propose a personalized language-model architecture
that grounds behavioral simulation in longitudinal transaction histories through behavioral rep-
resentations and retrieval-augmented contextual grounding. Unlike conventional recommender
systems [7–9,11] that solve individual prediction tasks, LBM supports multiple behavioral sim-
ulation tasks using a single shared language model.
3.A scalable behavioral learning framework.We develop a four-stage training pipeline
combining continual pre-training, supervised fine-tuning, and reinforcement learning to align
language models with customer behavior. Comprehensive ablation studies quantify the contri-
bution of each stage and highlight the importance of jointly learning behavioral representations
and contextual grounding.
4.A benchmark for customer-level behavioral simulation.We construct a benchmark
spanning multiple retail decision-making tasks—including purchase prediction, basket comple-
tion, promotion response, and survey simulation—with carefully designed hard negatives and
varying levels of behavioral ambiguity to evaluate customer-specific reasoning.
5.Evidence that behavioral grounding outperforms foundation-model priors.Across
both in-domain and cross-domain evaluations, we demonstrate that grounding language models
in longitudinal behavioral evidence consistently improves personalized decision simulation over
frontier foundation models. These findings suggest that behavioral evidence is a more effective
basis for simulating individual consumer behavior than relying solely on the generic priors
encoded in large language models.
3

2 System Overview
We present the Large Behavior Model (LBM), a framework for simulating individual consumer
decisions from historical transaction data. Rather than learning a separate model for each down-
stream task, LBM models customer behavior as the interaction between a persistent behavioral
profile and a dynamic decision environment. This decomposition enables a single language model
to generalize across multiple retail decision tasks—including purchase prediction, basket comple-
tion, promotion response, and survey-style preference elicitation—using only prompt conditioning.
Figure 1 provides an overview of the complete system. Raw retail transactions are transformed
into behavioral representations and supervised decision examples, while a retrieval module injects
product knowledge at inference time to construct the decision environment.
Overview of the pipeline.The pipeline consists of three stages. First, historical transaction
logs are processed to construct a persistent behavioral representation for each customer. Second,
real purchase events are converted into supervised behavioral decision examples spanning multiple
prediction tasks. Finally, during inference, the model combines the customer representation with
retrieved product knowledge to simulate decisions under the current shopping context. This design
separates long-term customer behavior from short-term environmental context while allowing both
to be encoded in natural language.
Retail
datasource
Simulated reactions
purchase / next-item prediction /
promotion / survey reaction /
reviews
Large Behavior Model
Qwen3-8B / 3.5-9B +
LoRA
Live-shelf showing
top-3 SKUs
Decision points
Shopping-DNA profile
PERSON
ENVIRONMENT
Persona
Extractor
Behavior
Extractor
Figure 1:From raw transactions to simulated decisions. The Persona Extractor summarizes stable demo-
graphic/lifestage traits while a Behavior Extractor derives decision points from raw transactions, together
forming the Shopping-DNA profile. Person is supplied by a per-segment LoRA adapter plus a system prompt
built from this profile; Environment is supplied by RAG at decision time. The same weights answer purchase,
basket, promotion, survey, and review questions, selected by the prompt.
Person–Environment decomposition.We hypothesize that customer decisions arise from the
interaction of persistent behavioral preferences and the current decision context. We therefore
formulate behavioral simulation as modeling two complementary factors: Person and Environment.
•Person (P):a persistent representation derived from historical purchasing behavior that
captures long-term preferences, shopping habits, and behavioral tendencies.
•Environment(E):adynamicrepresentationoftheproductsavailableinthecurrentdecision
context, retrieved from the product knowledge base.
4

Consumer behavior is therefore modeled as
B=f(P,E),(2)
where the language model predicts decisions conditioned jointly on the customer representation
and the surrounding shopping environment.
This separation is central to our framework. Rather than memorizing customer-specific be-
havior within model parameters, customer identity is supplied through prompt conditioning, while
environmental knowledge is retrieved dynamically at inference time. The resulting architecture
naturally generalizes to unseen customers without retraining. The design also enables the same un-
derlying model to be reused across multiple behavioral tasks—including purchase prediction, basket
completion, promotion response, and survey-style reasoning—without requiring task-specific archi-
tectures.
2.1 Data
We construct our dataset from large-scale retail transaction logs and product catalog informa-
tion. The data supports two core purposes: (i) learning persistent behavioral representations of
customers, and (ii) constructing realistic decision environments for behavioral simulation.
2.1.1 Transaction data
Thecoredatasetconsistsofanonymizedretailtransactionrecords, whereeachentrycorresponds
to a single product purchased within a customer basket. Each record contains a masked customer
identifier, timestamp, product identifier, quantity, unit price, applied discounts, and final net spend.
Transactions are aggregated into baskets, representing individual shopping trips. Each basket
contains multiple items, forming sequential decision contexts that reflect real-world purchasing
behavior. Products are structured within a hierarchical taxonomy spanning division, section, and
item levels, enabling multi-resolution behavioral modeling.
From these logs, we derive: (i) historical purchase sequences per customer, used to construct
behavioral representations, and (ii) observed purchase decisions, used as supervision signals for
learning decision-making behavior.
2.1.2 Product catalog
We construct a product knowledge base containing all available SKUs, along with structured
metadata including product names, category hierarchy, and price statistics.
Each product is embedded into a dense vector space to enable semantic retrieval of similar
items. This retrieval mechanism is used to construct the decision environment at inference time by
selecting a small set of relevant candidate products.
2.1.3 Dataset scale
In addition to the primary cohort, we construct multiple evaluation splits for behavioral simu-
lation, including held-out within-domain test sets and harder negative-sampling-based evaluations
5

Table 1:Dataset summary for the primary retail cohort.
Train Test
Transactions 159,667 40,665
Customers 1,500 1,500 (held-out baskets)
Products (catalog) 38,516 (same)
designed to test decision boundaries under ambiguity. We further evaluate cross-domain general-
ization on external retail and consumer behavior datasets. Table 1 summarizes the primary dataset
used in this work.
2.1.4 Summary of usage
The dataset serves two roles in our framework: (i) constructing persistent customer behavioral
representations, and (ii) defining realistic decision environments for simulation at inference time.
3 Method
The Large Behavior Model (LBM) treats customer decision making as a conditional reasoning
problem. Rather than learning a separate model for each downstream task, the model conditions on
two complementary sources of information: (i) a persistent representation of the customer derived
from historical transactions, and (ii) a dynamic decision environment describing the products cur-
rently under consideration. This factorization enables a single language model to simulate multiple
retail behaviors while sharing a common behavioral representation.
Figure 2 summarizes the complete training pipeline, while Figure 3 illustrates how progressively
richer behavioral evidence affects downstream decision quality.
3.1 Problem formulation
We formulate behavioral prediction as
B=f(P,E),(3)
wherePdenotes the persistent customer representation andEdenotes the decision environment
available at inference time.
The persistent representation captures long-term purchasing tendencies, whereas the environ-
ment describes the immediate choice context. This decomposition allows the same underlying
model to support purchase prediction, basket completion, promotion response, survey reasoning,
and other consumer decision tasks without task-specific architectures.
3.2 Customer representation
Each customer is represented using two complementary components: a structured behavioral
profile and a lightweight behavioral adapter.
6

Shopping-DNA profile.We first construct a structured prompt exclusively from transactions
observed during the training period. The resulting Shopping-DNA summarizes stable behavioral
characteristics including demographic information (when available), life stage, price sensitivity,
category preferences, repeat purchasing patterns, basket statistics, temporal shopping behavior,
channel usage, and promotion affinity. No information from the evaluation period is included,
preventing future information leakage.
Behavioral adapters.To complement the prompt representation, we fine-tune LoRA adapters
on behavioral decision data.
Two adaptation strategies are investigated.
•Segment-level adaptersare trained on customer groups defined by life stage or retail
personas. These adapters provide complete customer coverage, including cold-start users.
•User-level adaptersare trained separately for individual customers. Although they can
outperform segment models when abundant history is available (typically 80–300 behavioral
examples), they do not generalize to sparse or unseen customers.
Consequently, all experiments in this paper adopt segment-level adaptation as the primary
deployment strategy.
3.3 Decision environment via retrieval
The second component of the framework models the customer’s immediate decision environ-
ment.
Each product in the retail catalog is embedded into a dense vector space, and a ChromaDB
index is used to retrieve the top-ksemantically similar products (typicallyk= 3) using cosine
similarity. These retrieved products are injected directly into the model prompt during behavioral
reasoning.
Our ablation studies demonstrate that retrieval is effective only when it remains part of the
decision context. Incorporating retrieved information during both supervised training and infer-
ence substantially improves prediction accuracy, whereas inserting retrieval into the continual pre-
training corpus degrades performance. These results indicate that retrieval functions as contextual
evidence rather than model knowledge.
3.4 Four-stage training pipeline
The LBM is trained using a progressive four-stage pipeline illustrated in Figure 2. Rather than
optimizing a single objective, each stage contributes a distinct capability.
1.Behavioral data collectionprovides large-scale retail transaction histories.
2.Continual pre-training (CPT)adapts the language model into a behavior model capable
of learning general purchasing patterns.
3.Supervised fine-tuning (SFT)teaches structured decision formats and behavioral reason-
ing over transaction-derived prompts.
7

4.GRPO reinforcement learningcalibrates decision making by encouraging reliance on
explicit behavioral evidence while discouraging generic language-model priors.
Figure 2 illustrates how these stages progressively transform a general-purpose language model
into a customer behavior simulator.
Our empirical study consistently shows that CPT provides the majority of transferable behav-
ioral knowledge, while SFT primarily improves response formatting. GRPO further strengthens
robustness by calibrating the model’s confidence according to evidence contained in the prompt.
4. GRPO
promptable customer profile and
calibrates evidence over prior
3. SFT
customer voice +
decision format
2. CPT
behavior model
(generalization engine)
1. Data
proprietary retail
transactions
Figure 2:A prompt change re-instantiates any customer; CPT generalizes, SFT format-overfits, GRPO
calibrates evidence-over-prior trust. The four-stage recipe chained onverbalizedbehavior. Each stage adds
capability a zero-shot frontier model lacks; CPT is the backbone, SFT supplies the decision interface, and
GRPO generalizes and calibrates trust in the in-prompt evidence.
3.5 B-task formulation
We evaluate the model on four behavioral prediction tasks constructed from real transaction
logs.
Table 2:Behavioral evaluation tasks (B1–B4).
Task Objective Construction
B1 Purchase (positive) Actual purchased items with retrieved context.
B2 Purchase (negative) Hard negatives sampled from same and different sec-
tions.
B3 Basket completion Predict next item given partial basket context.
B4 Promotion response Evaluate response to discounts vs counterfactual offers.
To construct robust decision boundaries, negative samples are generated using both intra-
category and cross-category perturbations.
3.6 B-hard evaluation and prompt sensitivity
Wefurtherdefineadifficultyladder(B-hard)toevaluatesensitivitytocontextualsignalstrength.
Performance increases sharply when explicit similarity information is included in the prompt,
demonstrating that model performance is strongly driven by the quality of in-context evidence
rather than internal computation of similarity.
This indicates that the model primarily operates as an evidence-conditioned decision system
rather than a latent similarity engine.
3.7 Training dynamics and key findings
We summarize four main empirical findings:
8

Figure 3:The B-hard difficulty ladder: the model represents a customer only to the resolution the prompt
encodes. With no in-prompt evidence (v1) accuracy is near chance; raw similar-item names (v2) reach∼60%;
a singlelegiblesimilarity line (v3) reaches 95.9% (vs. 73.4% for GPT-5.5). The bottleneck is prompt signal,
not weights.
•CPT provides generalization, SFT improves format adherence.CPT is responsible
for transfer performance, while SFT primarily shapes output structure.
•Retrieval must be present at inference time.Removing retrieval significantly reduces
performance, while misplacing it in pre-training is detrimental.
•Reasoning supervision is task-dependent.Rationale training improves transfer tasks
but may reduce performance on fixed-format evaluation.
•Data packing affects learning stability.Improper multi-turn packing leads to shortcut
learning and degraded generalization.
3.8 Key insight: evidence over prior
A central property of the model is that decisions are primarily driven by explicit behavioral
evidence in the prompt rather than generic priors learned during pre-training. This is reinforced
through reinforcement learning, which calibrates the model’s reliance on observed customer history
over population-level stereotypes.
4 Experiments and Results
4.1 In-domain Evaluation: Real Retailer
We evaluate the LBM on held-out transaction decision tasks (Table 3) and a harder negative-
sampling variant (Table 4). On the classic-B benchmark (n= 5,091), the LBM outperforms
GPT-5.5 on average and across all tasks except a near tie on B1. On the harder B-hard v4 set
9

(n= 2,490), which introduces adversarial hard negatives, the performance gap increases to +15.7pp
on average, driven primarily by large gains on B2.
Table 3:Classic-B held-out evaluation (n= 5,091). Higher is better.
ModelB1 B2 B3 B4AVG
Our LBM (base + SFT-Retailer-data) 84.297.6 71.1 76.0 82.2
GPT-5.584.875.5 57.9 72.8 72.7
Table 4:B-hard v4 with hard negatives (n= 2,490). Higher is better.
ModelB1 B2 B3 B4AVG
Our LBM (GRPO v5 + SFT-Lazada)98.6 98.9 81.6 52.0 82.8
GPT-5.5 94.5 51.4 70.9 51.6 67.1
Across both benchmarks, gains are most pronounced on hard-negative discrimination (B2),
indicating that performance improvements are driven by improved evidence grounding rather than
memorization.
Figure 4:In-domain task-by-task comparison on classic-B (held-out,n= 5,091). The LBM matches the
frontier on B1 and beats it on hard negatives (B2), basket (B3), promotion (B4), and on average (+9.5
points).
4.1.1 Stage-wise scaling results
We further evaluate system performance across deployment scales. In a proof-of-concept setting
(10 users), Segment-LoRA + RAG achieves 78.0% accuracy on purchase tasks (B1+B2), compared
to 75.9% for GPT-5.5 and 72.5% for the base model. At larger scale (662 users, 24,979 test
prompts), the LoRA lift increases substantially, reaching +15.2pp for purchase prediction, while
promotion prediction shows weaker gains (+2.7pp), indicating reduced generalization under weaker
signal conditions.
10

Overall, the best configuration (v5 + SFT) achieves 88.7% average accuracy across B1–B4,
compared to 80.1% for GPT-5.5, corresponding to consistent gains of +9–13pp across tasks.
4.1.2 GRPO-based calibration
We train the model through a reinforcement learning curriculum: SFT-v5→GRPO-v1 (300
steps; verifiable YES/NO rewards; NO-class upweighted; Jaccard reward for B3)→GRPO-v4/v5
(adding B4 affinity and B3 co-occurrence constraints).
On the D2 trip-discrimination task (2AFC real vs decoy), performance improves from 54.6%
(SFT-v5) to 68.9% (GRPO-v5 + SFT), compared to 81.2% for GPT-5.5. The remaining gap
reflects residual limitations in reward calibration rather than representation capacity. This gap is
consistent with the segment-level (rather than per-user) adapter granularity used here: D2’s decoy-
discrimination task may require finer-grained purchase-sequence signal than the current segment
adapters encode, an avenue we leave to future user-level adapter scaling (Section 3.2).
4.2 Out-of-domain Evaluation: Lazada Voucher Redemption
We evaluate cross-domain generalization on the DMBGN benchmark (SIGKDD’21), consisting
of 12,480 held-out cases with no session overlap with training data. The task requires ranking
voucher redemption likelihood, measured via AUC.
This setting introduces three simultaneous shifts: (i) domain shift (grocery→e-commerce),
(ii) geography shift (Thailand→SEA-wide), and (iii) task shift (purchase prediction→voucher
redemption).
Figure5:Voucher-redemptionranking accuracy(AUC) on theDMBGN benchmark (SIGKDD’21). Trained
only on Retailer Data, the LBM transfers zero-shot to Lazada (0.772, above the frontier GPT-5.5); fine-tuned
on Lazada it reaches 0.827. Both LBM bars (blue) clear the GPT-5.5 baseline at every level.
Despite being trained only on Retailer data, the model achieves strong zero-shot transfer (0.772
AUC), surpassing GPT-5.5. After fine-tuning on Lazada data, performance increases to 0.827 AUC,
outperforming both GPT-5.5 and prior SOTA baselines.
Notably, the model remains competitive even in the zero-shot regime, suggesting that behavioral
representations learned from retail transactions generalize across platforms when prompt structure
11

is preserved.
4.2.1 Cross-market transfer analysis
We further evaluate transfer across heterogeneous datasets:
Online Shoppers (UCI, Turkey):The base model achieves 0.849 AUC (log-prob), close to a
strong GBDT ceiling (0.933). SFT reduces performance (0.781), consistent with format overfitting.
Tmall (IJCAI-15):Zero-shot prompt performance ranges from 0.53–0.59 AUC, improving
to 0.619 with enriched prompts, but remaining below feature-engineered SOTA (0.703), indicating
loss of structured temporal signals.
Shopee (SEA):GPT-5.5 dominates (0.825 vs 0.65), suggesting that when signal is embedded
in platform-specific identifiers or engineered features, prompt-based generalization is insufficient.
Overall, we observe a consistent pattern: the model transfers effectively when behavioral signals
are expressible in natural language or coarse structured features, but degrades when predictive
signal is encoded in IDs or high-dimensional engineered features.
4.2.2 Cross-dataset survey transfer (Twin-2K-500)
We evaluate a reasoning-chain LoRA trained on Amazon grocery survey data on 414 unseen
users (16,560 items). The model achieves 71.7% accuracy, outperforming GPT-5.5 (70.6%) and a
base aggregation baseline (70.3%).
Key findings are: (i) cross-person augmentation improves generalization, (ii) class balance must
match deployment distributions, (iii) reasoning supervision improves structural consistency rather
than memorized answers, and (iv) prompt-level aggregation outperforms baked-in aggregation
mechanisms.
5 Discussion
Behavior simulation is an information problem.A central finding of this work is that
behavioral simulation is primarily an information problem rather than a model-size problem.
Across our experiments, the largest performance gains arise from improving how customer be-
havior is represented—through Shopping DNA, retrieval-augmented decision contexts, and prompt
construction—rather than simply scaling the underlying language model. In particular, the B-
hard experiments demonstrate that providing explicit behavioral evidence dramatically improves
decision quality, while stronger frontier models without such evidence remain limited by generic
behavioral priors. These results suggest that faithful customer representation is a more important
bottleneck than model capacity for behavioral simulation.
Evaluation scope and future directions.Our evaluation focuses on behavioral decision-
making tasks with objective ground truth, including purchase prediction, basket completion, pro-
motion response, and cross-domain transfer. These tasks permit quantitative evaluation against
real customer decisions and standardized benchmarks.
Although the LBM can also be prompted to generate customer-facing natural language—such as
product reviews, shopping rationales, or survey responses—these capabilities are not quantitatively
12

evaluated in the current work. Unlike purchase decisions, there is generally no unique ground-
truth review for a given customer and product, making automatic evaluation substantially more
challenging. Consequently, review generation should be viewed as a qualitative capability enabled
by the same behavioral representation rather than as a validated benchmark in this paper.
An important direction for future work is the development of evaluation protocols for open-
endedbehavioralgeneration, includingreviewsynthesis, conversationalshoppingagents, andvirtual
consumerstudies. Suchevaluationswilllikelyrequirehumanassessmentorpreference-basedmetrics
in addition to traditional automatic benchmarks, complementing the decision-centric evaluation
presented here.
Behavioral language models.Continued pre-training on verbalized behavioral data has been
shown to yield strong customer simulation models (e.g., Adobe LCBM [20]). SFT further improves
alignment with behavioral outputs (OPeRA [21]). Reinforcement learning with verifiable rewards
has recently emerged as a scalable approach to behavioral modeling (Customer-R1 [23], Shop-
R1 [22]), often incorporating persona conditioning and difficulty-aware reward shaping.
Our work extends this line by explicitly chaining CPT, SFT, and GRPO on a unified verbalized
behavioral representation, with a clean separation betweenpersonandenvironmentcomponents.
We contrast this with token-level recommender systems (e.g., HSTU [11], TIGER [12]), which
scale effectively for ranking but do not support simulation or language-conditioned reasoning.
Prompt conditioning and generalization.Recent studies demonstrate that prompt-based
persona conditioning can match or exceed per-user fine-tuning in many settings (Stanford 1,000-
person study [19]; Twin-2K-500 [34]). Demographic-only representations are weak predictors of
behavior (SCOPE [24]), while richer behavioral summaries significantly improve fidelity. Synthetic
persona corpora (Nemotron [25]) provide complementary prior distributions.
Fidelity limits of simulation.Prior work consistently shows a ceiling in behavioral fidelity.
Full persona models often collapse toward demographic baselines (Funhouse Mirrors [28]), and long-
context conditioning can degrade performance beyond a threshold (Long Context, Less Focus [29]).
These findings align with our observation that prompt signal quality, rather than model capacity,
is the limiting factor.
Evaluation methodology.Reliable evaluation requires (i) real held-out decisions, (ii) hard neg-
ative sampling, and (iii) variance-aware metrics rather than point accuracy alone. Prior work (CMU
Sim2Real [27]) shows that LLM-based simulators can overestimate downstream performance due to
excessive cooperativeness and reduced behavioral friction. Our evaluation explicitly avoids model-
generated users and uses real transaction data with adversarial negatives.
We further highlight that spurious artifacts (e.g., price-ending leakage in prior datasets) can
inflate performance; our evaluation explicitly controls for such effects.
6 Conclusion and Future Work
We presented a behavioral language modeling framework for customer simulation that combines
continued pre-training, supervised fine-tuning, reinforcement learning, and retrieval-augmented
13

prompting within a unified Person–Environment formulation. Rather than treating customer mod-
eling as a recommendation problem over tokenized interaction histories, our approach models pur-
chasing behavior as language-conditioned decision making, allowing the same model to simulate,
explain, and predict customer actions.
Across multiple retail benchmarks, the proposed framework consistently outperformed frontier
general-purpose language models on behavior prediction tasks. In the in-domain evaluation, the
model achieved substantial improvements on purchase prediction, hard-negative discrimination,
basket completion, and promotion response while remaining competitive on simpler purchase de-
cisions. More importantly, the learned behavioral representation generalized beyond the training
domain, transferring from grocery retail to e-commerce voucher redemption with strong zero-shot
performance and further improvements after task-specific fine-tuning. These results suggest that
behavioral knowledge acquired from transaction histories can transfer across retailers, markets, and
decision types when customer state and environmental context are represented explicitly.
Our experiments also provide several empirical insights into behavioral language modeling.
Continued pre-training serves as the primary source of behavioral generalization, whereas super-
vised fine-tuning mainly teaches the desired response format. Retrieval is most effective when
incorporated during both training and inference, but not during continued pre-training. Finally,
reinforcement learning improves the model’s calibration by encouraging decisions to rely on explicit
behavioral evidence rather than generic language-model priors.
Despite these encouraging results, several limitations remain. The current approach still relies
on handcrafted textual summaries of customer behavior, which inevitably compress rich trans-
actional histories into natural language descriptions. Performance also degrades when predictive
signals are primarily encoded in platform-specific identifiers or highly engineered numerical features
rather than semantically interpretable behavioral patterns. Furthermore, while prompt condition-
ing enables strong zero-shot personalization, it does not learn continuous user representations that
can evolve over time.
Future work will focus on three directions. First, we plan to replace manually constructed
behavioral summaries with learned customer representations that map transaction histories directly
into continuous prompt embeddings or soft prompts. Second, we will extend the framework to
larger multi-region and multi-vertical behavioral datasets to improve robustness and cross-domain
transfer. Finally, we aim to explore downstream applications beyond purchase prediction, including
personalizedrecommendation, counterfactualcustomersimulation, virtualmarketexperimentation,
and decision-support systems. More broadly, we believe behavioral language models provide a
promising foundation for scalable digital twins that bridge structured behavioral data with the
reasoning capabilities of modern language models.
References
[1] D. McFadden, “Conditional logit analysis of qualitative choice behavior,” inFrontiers in
Econometrics, P. Zarembka, Ed. Academic Press, 1974, pp. 105–142.
[2] K. E. Train,Discrete Choice Methods with Simulation, 2nd ed. Cambridge University Press,
2009.
[3] M. Wedel and P. K. Kannan, “Marketing analytics for data-rich environments,”Journal of
Marketing, vol. 80, no. 6, pp. 97–121, 2016.
14

[4] K. Lewin,Principles of Topological Psychology. McGraw-Hill, 1936.
[5] N. K. Malhotra,Marketing Research: An Applied Orientation, 7th ed. Pearson, 2019.
[6] P. M. Guadagni and J. D. C. Little, “A logit model of brand choice calibrated on scanner
data,”Marketing Science, vol. 2, no. 3, pp. 203–238, 1983.
[7] Y. Koren, R. Bell, and C. Volinsky, “Matrix factorization techniques for recommender sys-
tems,”Computer, vol. 42, no. 8, pp. 30–37, 2009.
[8] X. He, L. Liao, H. Zhang, L. Nie, X. Hu, and T.-S. Chua, “Neural collaborative filtering,” in
Proceedings of the 26th International Conference on World Wide Web (WWW). International
World Wide Web Conferences Steering Committee, 2017, pp. 173–182.
[9] W.-C. Kang and J. McAuley, “Self-attentive sequential recommendation,” inProceedings of
the IEEE International Conference on Data Mining (ICDM). IEEE, 2018, pp. 197–206.
[10] F. Sun, J. Liu, J. Wu, C. Pei, X. Lin, W. Ou, and P. Jiang, “BERT4Rec: Sequential rec-
ommendation with bidirectional encoder representations from transformer,” inProceedings of
the 28th ACM International Conference on Information and Knowledge Management (CIKM).
ACM, 2019, pp. 1441–1450.
[11] J. Zhaiet al., “Actions speak louder than words: Trillion-parameter sequential transducers for
generative recommendations,”arXiv preprint arXiv:2402.17152, 2024.
[12] S. Rajputet al., “Recommender systems with generative retrieval,” inAdvances in Neural
Information Processing Systems (NeurIPS), 2023.
[13] L. Ouyang, J. Wu, X. Jianget al., “Training language models to follow instructions with
human feedback,” inAdvances in Neural Information Processing Systems (NeurIPS), vol. 35,
2022, pp. 27730–27744.
[14] A. Dubey, A. Jauhri, A. Pandeyet al., “The Llama 3 herd of models,”arXiv preprint
arXiv:2407.21783, 2024.
[15] Qwen Team, “Qwen3 technical report,”arXiv preprint arXiv:2505.09388, 2025.
[16] Gemma Team, M. Riviere, S. Pathaket al., “Gemma 2: Improving open language models at
a practical size,”arXiv preprint arXiv:2408.00118, 2024.
[17] J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein, “Generative
agents: Interactive simulacra of human behavior,” inProceedings of the 36th Annual ACM
Symposium on User Interface Software and Technology (UIST). ACM, 2023, pp. 1–22.
[18] L. P. Argyle, E. C. Busby, N. Fulda, J. R. Gubler, C. Rytting, and D. Wingate, “Out of one,
many: Using language models to simulate human samples,”Political Analysis, vol. 31, no. 3,
pp. 337–351, 2023.
[19] J. S. Park, C. Q. Zou, A. Shaw, B. M. Hill, C. Cai, M. R. Morris, R. Willer, P. Liang, and M. S.
Bernstein, “Generative agent simulations of 1,000 people,”arXiv preprint arXiv:2411.10109,
2024.
15

[20] A. Khandelwal, A. Agrawal, A. Bhattacharyyaet al., “Large content and behavior models
to understand, simulate, and optimize content and behavior,” 2024. [Online]. Available:
https://arxiv.org/abs/2309.00359
[21] Y. Lu, J. Huang, Y. Hanet al., “Can llm agents simulate multi-turn human
behavior? evidence from real online customer behavior data,” 2026. [Online]. Available:
https://arxiv.org/abs/2503.20749
[22] Y. Zhang, T. Wang, J. Gesiet al., “Shop-r1: Rewarding llms to simulate human
behavior in online shopping via reinforcement learning,” 2026. [Online]. Available:
https://arxiv.org/abs/2507.17842
[23] Z. Wang, Y. Lu, Y. Zhang, J. Huang, and D. Wang, “Customer-r1: Personalized simulation
of human behaviors via rl-based llm agent in online shopping,” 2025. [Online]. Available:
https://arxiv.org/abs/2510.07230
[24] P. N. Venkit, Y. Li, Y. Pruksachatkun, and C.-S. Wu, “The need for a socially-
grounded persona framework for user simulation,” 2026. [Online]. Available: https:
//arxiv.org/abs/2601.07110
[25] NVIDIA, “Nemotron-personas: Multilingual, region-specific synthetic persona datasets,”
https://huggingface.co/collections/nvidia/nemotron-personas, 2026, hugging Face Collection,
accessed 2026.
[26] B. Ni, Y. Wang, L. Wanget al., “A survey on llm-based conversational user simulation,”
inProceedings of the 19th Conference of the European Chapter of the Association for
Computational Linguistics (Volume 1: Long Papers). Association for Computational
Linguistics, 2026, p. 4266–4301. [Online]. Available: http://dx.doi.org/10.18653/v1/2026.
eacl-long.200
[27] X. Zhou, W. Sun, Q. Maet al., “Mind the sim2real gap in user simulation for agentic tasks,”
2026. [Online]. Available: https://arxiv.org/abs/2603.11245
[28] T. Peng, G. Gui, M. Bruckset al., “Digital twins as funhouse mirrors: Five key distortions,”
2026. [Online]. Available: https://arxiv.org/abs/2509.19088
[29] S. Gu, “Long context, less focus: A scaling gap in llms revealed through privacy and
personalization,” 2026. [Online]. Available: https://arxiv.org/abs/2602.15028
[30] L. Ning, L. Liu, J. Wu, N. Wu, D. Berlowitz, S. Prakash, B. Green, S. O’Banion, and J. Xie,
“User-llm: Efficient llm contextualization with user embeddings,” 2024. [Online]. Available:
https://arxiv.org/abs/2402.13598
[31] M. R. I. Hossain, L. Feng, L. Sigal, and M. O. Ahmed, “Do llms benefit from
user and item embeddings in recommendation tasks?” 2026. [Online]. Available:
https://arxiv.org/abs/2601.04690
[32] L. Wang, X. Mou, X. Liu, X. Huang, and Z. Wei, “Curp: Codebook-based continuous
user representation for personalized generation with llms,” 2026. [Online]. Available:
https://arxiv.org/abs/2602.00742
16

[33] P. Lewis, E. Perez, A. Piktuset al., “Retrieval-augmented generation for knowledge-intensive
nlp tasks,” inAdvances in Neural Information Processing Systems, vol. 33, 2020, pp. 9459–
9474.
[34] O. Toubia, G. Z. Gui, T. Peng, D. J. Merlau, A. Li, and H. Chen, “Twin-2k-500: A dataset
for building digital twins of over 2,000 people based on their answers to over 500 questions,”
arXiv preprint arXiv:2505.17479, 2025.
A Reproducibility
Base models.Qwen3-8B (PoC / Phase-7) and Qwen3.5-9B (G2 / cross-dataset), in 4-bit via
Unsloth.
LoRA.Rankr= 8,α= 16, dropout 0, applied to all attention and MLP modules (∼0.42%
of parameters trainable); per-segment (lifestage / NielsenIQ persona) for coverage, per-user only
where≥300 pairs are available.
RAG.A 1,024-dimensional embedding model into ChromaDB under cosine similarity; top-3
SKUs per decision; present inbothtraining and inference.
Training.SFTTrainer (TRL) with Unsloth; GRPO via TRL GRPOTrainer with Unsloth Patch-
FastRL, using hand-written verifiable rewards (exact YES/NO and format; NO-rows weighted×2;
Jaccard on B3),∼300–500 steps with 8 rollouts; assistant-only loss masking;<think>empty at
training andenable_thinking=Falseat inference for fixed templates.
Evaluation.vLLM (tensor-parallel 8 on H100×8) batched at 2,000 prompts; LLM-as-judge via
DeepSeek-V3/V4 on BytePlus (rule-based where possible, LLM otherwise; 0.08% judge-error rate).
Metrics: accuracy/precision/recall/F1 (purchase), hit-rate/Jaccard (basket), and AUC (voucher;
first-token log-probability of P(YES) plus a verbalized “Likelihood: NN” self-consistency).
Hardware.TrainingandevaluationonRunPodH100×8andalocalH2096GB;aCUDA_HOME
fix is required for flashinfer JIT, and batch inference avoids EngineCore OOM.
17
