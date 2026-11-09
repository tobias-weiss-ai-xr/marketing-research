---
title: 'Evaluating Success in Proactive Sales Dialogues: Balancing Customer Experience and Business Outcomes'
url: https://doi.org/10.21437/wochat.2026-6
category: ai-marketing
subcategory: framework
date: 2026-08
venue: ''
authors:
- Justyna Gromada
- Alicja Kasicka
- Natalia Krawczyk
source: openalex-oa
pdf_url: https://www.isca-archive.org/wochat_2026/gromada26_wochat.pdf
pages: 19
chars: 69383
fetched_at: '2026-11-08T20:03:06+00:00'
kb_version: 1
---

# Evaluating Success in Proactive Sales Dialogues: Balancing Customer Experience and Business Outcomes

Evaluating Success in Proactive Sales Dialogues:
Balancing Customer Experience and Business Outcomes
Justyna Gromada, Alicja Kasicka, Natalia Krawczyk, Michał Szczerbak
Orange Research
firstname.lastname@orange.com
Abstract
Conversational sales agents need to balance
positive customer experience with strong busi-
ness outcomes to ensure long-term success.
This requires evaluation methods that capture
the complex trade-offs between these perspec-
tives. We introduce a dual-perspective frame-
work that assesses sales dialogues from both
customer and business viewpoints, each captur-
ing distinct yet interconnected dimensions of
success. We illustrate the framework through
a proof-of-concept study based on simulated
dialogues, spanning 5200 dialogues across 13
sales agent configurations, revealing prelimi-
nary insights into how different sales strategies
impact both perspectives and identifying condi-
tions under which they can be simultaneously
optimized. To enable scalable analysis, we val-
idate open-source language models (LMs) for
automated annotation as cost-effective alterna-
tives to commercial ones. This work provides
a practical and extensible framework for eval-
uating and designing balanced sales systems
that align customer satisfaction with business
objectives.
1 Introduction
Evaluation of task-oriented dialogue (ToD) systems
typically focuses on task completion and user satis-
faction (Walker et al., 1997). However, sales dia-
logues present a unique challenge: success must be
evaluated from multiple perspectives. Customers
seek to achieve their purchase goals with high satis-
faction, while businesses aim to maximize revenue
through effective product recommendations and
conversions. Although these perspectives should
ideally complement each other, the sales approach
significantly impacts both: aggressive tactics may
boost short-term revenue but harm customer sat-
isfaction, while passive approaches may satisfy
customers but miss valuable sales opportunities.
Maintaining this balance is critical for long-term
business success (see Figure 1).
Figure 1: Perspectives on sales dialogue success
Proactive sales scenarios, such as up-selling (pre-
mium alternatives) and cross-selling (complemen-
tary products), are at the heart of this challenge.
Unlike traditional ToD where system and user goals
naturally align, agents here pursue business objec-
tives beyond the customer’s initial request. While
beneficial for business (Kubiak and Weichbroth,
2010), these strategies can create tension between
maximizing business value and ensuring customer
satisfaction, necessitating automated evaluation
methods that assess both perspectives.
In this work, we introduce a dual-perspective
evaluation framework for sales dialogues that cap-
tures both customer success (satisfaction and goal
achievement) and business outcomes (revenue and
sales goal completion). We apply this framework
to 5200 simulated dialogues across 13 bot config-
urations with varying up-sell and cross-sell strate-
gies. Since this study relies entirely on simulated
customers, the findings should be interpreted as
preliminary insights from a proof-of-concept rather
than definitive conclusions about real customer be-
havior. To enable scalable annotation, we validate
open-source LMs for automated dialogue annota-
tion, demonstrating cost-effectiveness while main-
taining acceptable agreement with human or com-
mercial LM-based annotations.
Our main contributions are: (i) a dual-
perspective evaluation framework for sales di-
alogues, (ii) a validated methodology for cost-
WOCHAT2026: Workshop on Chatbots and Agentic Technologies
2 August 2026, Atlanta, Georgia, USA
66 10.21437/WoChat.2026-6

efficient LM-based annotation at scale using open-
source models, and (iii) empirical insights into how
sales strategies affect both user experience and com-
mercial success.
The remainder of this paper is organized as fol-
lows. Section 2 reviews related work. Section 3
presents our dual-perspective framework. Sec-
tions 4 and 5 describe the evaluation setting and
annotation models selection. Section 6 analyzes the
results and practical implications. Sections 7 and 8
conclude the paper and discuss future directions.
2 Related work
Evaluation of ToD systems has evolved from bi-
nary task completion metrics to comprehensive,
multi-dimensional assessment frameworks. Early
approaches focused solely on whether the system
achieved its assigned goal (Fellows et al., 2022),
but modern evaluation combines goal-related per-
formance with user-focused metrics such as sat-
isfaction, usability, and efficiency (Serban et al.,
2018; Algherairy and Ahmed, 2023).
Recent works utilize Large Language Model
(LLM)-based evaluation to assess dialogues on
user-centric metrics (response quality, satisfaction)
and system-focused metrics (efficiency, cost) (Jain
et al., 2025; Wang et al., 2025). Some studies also
explore multi-perspective scoring of negotiation
dialogues (Lewis et al., 2017; Chawla et al., 2021),
but sales dialogues present distinct challenges: un-
like negotiations with clear win/lose outcomes,
sales success requires considering both objective
metrics (revenue, conversion) and subjective fac-
tors (customer satisfaction, engagement) (Jonker
et al., 2017; Jannach et al., 2021).
From the customer perspective, success in ToD
systems is measured by how well the system helps
accomplish specific goals, with key metrics includ-
ing task completion rate and dialogue efficiency
(number of turns) (Li et al., 2021). Customer sat-
isfaction serves as a direct indicator of user expe-
rience and need fulfillment (Deng et al., 2022),
useful for automatic conversation quality moni-
toring (Sun et al., 2021). Successful task com-
pletion increases user satisfaction and perceptions
of the system’s conversational ability (Rese and
Tränkner, 2023). However, cognitive factors also
matter: choice overload can cause decision fatigue
and cart abandonment in online shopping (Wang
et al., 2023; Canarslan, 2025), while post-purchase
regret can reduce long-term satisfaction despite im-
mediate task success (Biesok and Wyród-Wróbel,
2025).
From the business perspective, sales agents must
generate revenues justifying their costs (Janssen
et al., 2021). This can be achieved through
higher conversion rates and improved customer loy-
alty (Rasheed et al., 2025; Kim et al., 2020), recom-
mendation acceptance rates (Peng et al., 2018), and
premium product selection: Sales-Win-Rate (Kim
et al., 2025). However, automatic evaluation from
a purely business perspective remains largely un-
derexplored in the literature.
While prior work has examined customer experi-
ence and business metrics separately, no framework
systematically evaluates both perspectives in sales
dialogues where objectives may diverge. Our work
addresses this gap with a dual-perspective evalu-
ation framework capturing customer success and
business outcomes, enabling analysis of their trade-
offs and alignment.
3 Dual-perspective framework
Our dual-perspective framework organizes evalu-
ation of sales dialogues along business and cus-
tomer perspectives, each comprising multiple com-
plementary dimensions.
Customer Perspective.This includes two dimen-
sions: (1)User Satisfaction: the customer’s over-
all experience on a 1-5 scale; and (2)Customer
Goal Achievement: whether the customer’s stated
purchase intent was successfully addressed on an
ordinal 1-3 scale (not achieved / partially achieved
/ fully achieved). Both are assessed from the gener-
ated dialogues by human or LM-based observers,
capturing perceived customer experience within
the interaction. Longer-term satisfaction signals
(e.g., post-purchase regret, product abandonment)
are beyond the scope of this framework.
Business Perspective.This perspective quanti-
fies the commercial outcomes of the interaction
along four dimensions: (1)Purchase Success: pro-
portion of dialogues ending with at least one prod-
uct purchase; (2)Cart Size: total number of prod-
ucts (phones, plans, and accessories) purchased
per dialogue; (3)Revenue: total monetary value
of the final cart in Currency Units (CU); and (4)
Negotiation Success: the agent’s success in achiev-
ing its proactive sales goals (up-sell or cross-sell).
The first three dimensions are computed directly
from the sales agent’s final cart report after catalog
67

matching, where products not found in the official
catalog are excluded to mitigate the impact of prod-
uct hallucinations on business metrics. Negotia-
tion Success is evaluated through cart-based signals
computed both before and after catalog matching,
as well as through dialogue annotation by LMs
validated against human assessments. The cart-
based signals before and after matching allow us
to assess the impact of additional product hallu-
cinations introduced by proactive sales strategies
(cross-sell, up-sell), since LM-based dialogue an-
notation cannot determine whether a recommended
product belongs to the official catalog.
Separating these dimensions allows us to capture
different aspects of success and analyze the trade-
offs between them, supporting principled compar-
ison of agent configurations and identification of
strategies that balance both perspectives. All di-
mensions can be further aggregated into averages
and success rates to facilitate comparisons across
bot configurations.
4 Evaluation setting
To demonstrate the framework’s practical value,
we apply it to an R&D conversational sales agent
as a concrete use case, though it is designed to
be applicable to any such system. Since it had
not yet been deployed in production at the time of
writing, this study should be understood as a proof-
of-concept validation. We therefore generated a
synthetic dataset of dialogues with LLM-based user
simulators, as a cost-effective first step before con-
ducting human-user studies. The agent, user sim-
ulator, model selection rationale, and dataset are
described in the following subsections.
4.1 Sales Agent
Our sales agent is an experimental conversational
agent designed to assist customers in choosing a
mobile phone, subscription plan, and accessories
that best match their needs.
To evaluate the framework across diverse sales
behaviors, we defined 13 experimental configura-
tions, varying along four parameters: (1)Proac-
tivity: whether proactive sales behavior isonor
off; (2)Sales Strategy: eitherCross-sell, recom-
mending phone accessories (cases, screen protec-
tors, powerbanks, memory cards, etc.);KPI-sell,
a special case of cross-sell recommending higher-
value business-priority items from a curated list
(smartwatches and premium earbuds); orUp-sell,
recommending premium phone models as alter-
natives to the initially recommended device; (3)
Timing: the proactive offer is made eitherafter
Presentationof the base phone offer, before the
customer accepts it, orafter Acceptanceof the base
phone offer; (4)Pursuit Mode:Always, meaning
the agent always attempts the proactive strategy, or
Conditional, meaning the agent attempts only if the
customer profile indicates susceptibility.
When Proactivity is set tooff, the agent focuses
solely on helping the customer meet their goals,
making the other three parameters irrelevant, and
serves as our Baseline. This is the only configura-
tion corresponding to the production system. The
remaining 12 configurations are proactive (Proac-
tivity set toon) and purely experimental, combin-
ing the three sales strategies, two timings, and two
pursuit modes, as illustrated in Figure 2. All con-
figurations are powered by GPT-4o-mini1.
13 Configurations
Baseline 12 Proactive
Cross-sell
phone accessories
KPI-sell
business-priority
items
Up-sell
premium phones
× 2Timings: after Presentation / after Acceptance
× 2Pursuit modes: Always / Conditional
Figure 2: Sales agent configuration space
4.2 User Simulator
We used an LLM-based user simulator for initial
validation of the framework, built on Gemini-1.5-
Flash2.
We reuse the simulator settings from our prior
work (Gromada et al., 2025), where simulator be-
havior was validated through human annotations of
104 dialogues. Each simulated customer is driven
by a system prompt injecting a persona, goal, and
scenario for the conversation (full prompt provided
in Appendix A). Customer profiles detail demo-
graphics, budget, preferences, and behavioral traits
1https://platform.openai.com/docs/models/
gpt-4o-mini
2https://cloud.google.com/vertex-ai/
generative-ai/docs/models/gemini/1-5-flash
68

(e.g. susceptibility to recommendations), represent-
ing realistic customer archetypes for our organiza-
tion. We use a total of 100 personas, each aiming
to purchase a new phone, across four different con-
versation scenarios defined by low/high levels of
assertiveness and precision of needs.
4.3 Model Selection for Sales Agent and User
Simulator
The sales agent is powered by GPT-4o-mini, an
enterprise-compliant model matching our intended
production deployment, ensuring that findings are
directly actionable for real-world deployment deci-
sions.
For the user simulator, we selected Gemini-1.5-
Flash for its enterprise compliance, favorable cost-
quality trade-off at the time of choosing, and to
reduce model-specific biases by using a different
LLM family than the sales agent. We manually
inspected a sample of generated dialogues across
different sales agent configurations and found them
sufficiently coherent and realistic. Furthermore,
in our prior work (Gromada et al., 2025), we for-
mally validated that the user simulator based on
this model reliably adheres to assigned personas,
goals, and scenarios (see Appendix B for detailed
results). The findings of this study are tied to this
specific simulator configuration.
4.4 Conversations Dataset
We generated 5200 dialogues in total, covering
13 sales agent configurations and 400 simulated
customer configurations (100 personas × 1 goal x
4 scenarios), resulting in 400 dialogues per sales
agent configuration (400 × 13 = 5200). Table 1
presents the dataset statistics.
The table also presents the prices of products
offered by the sales agent in currency units (CU).
KPI-sell accessories (median: 600 CU) are notably
more expensive than cross-sell accessories (median:
70 CU), while phones are the highest-value items
(median: 3899 CU). These price differences reflect
a distinct economic impact of each sales strategy.
This dataset serves as the foundation of our dual-
perspective evaluation framework. While the con-
versations themselves require further analysis to as-
sess user satisfaction, customer goal achievement,
and negotiation success, the final cart is provided
as metadata by the sales agent and directly avail-
able to compute business metrics such as purchase
success, cart size, and revenue.
Dialogue Statistics
Total dialogues 5200
Sales agent configurations 13
Dialogues per configuration 400
Turns per dialogue 12.25 ± 2.78 (5–31)
Product Prices (Currency Units)
Product Type Median Mean Range
Phones 3899 4002 549–8599
Cross-sell accessories 70 115 20–1399
KPI-sell accessories 600 626 259–1099
Table 1: Dialogue dataset statistics. Turns per dialogue:
mean ± standard deviation (min–max)
5 Annotation LMs Selection
To enable dual-perspective evaluation, we anno-
tated each dialogue across multiple dimensions re-
quiring dialogue analysis: user satisfaction, cus-
tomer goal achievement, and negotiation success
(up-sell or cross-sell). Figure 3 illustrates our an-
notation scheme. The following sections detail the
LM selection process for each assessed dimension,
followed by an error analysis of cases where auto-
mated annotations diverge from human judgments.
DIALOGUE:
Bot: Hello! How can I assist you today?
Customer:I’m looking for a new phone with good
screen and battery life.
Bot: I recommend the Samsung Galaxy A26 5G
6/128GB with Plan XS for 350 CU. [offer details]
Customer:Sounds good, the price is reasonable.
Bot: Perfect! I also recommend Samsung Buds FE to
enhance your mobile experience.
Customer:Okay, the earbuds sound nice.
METADATA:
Final Cart: Samsung Galaxy A26 + Plan XS, Sam-
sung Buds FE
ANNOTATIONS:
Customer Satisfaction: 5
Customer Goal: fully achieved
Bot Cross-Sell: attempted, success
Bot Up-Sell: not attempted
Figure 3: Example sales dialogue with annotations
We adopted an LLM-as-a-judge approach, prior-
itizing open-source models to ensure a sustainable
and reproducible framework, and benchmarked
them against commercial models by measuring cor-
relation with human annotations. To select the
best-performing models, we followed a three-step
benchmarking methodology: (1) human annotation
of 104 dialogues by three independent annotators
69

with proficient English skills and higher education
backgrounds, (2) LM-based annotation of the same
subset, and (3) full dataset annotation using the
best-performing models from this benchmark.
The benchmark included open-source models
from different families and sizes: Qwen2.5 (7B-
1M, 14B-1M, 32B), Llama-3.1-8B, Selene-1-Mini-
Llama-3.1-8B, and DeepSeek-R1-Distill variants
(Qwen-7B, Qwen-14B, Llama-8B) 3, as well as
commercial models (GPT-o1, GPT-o3, GPT-o3-
mini, GPT-o4-mini, GPT-4o, Claude 3.5 Sonnet v2,
Claude 3.7 Sonnet)4, all chosen from our enterprise-
approved models list.
5.1 User Satisfaction
The user satisfaction score ranges from 1 (very
dissatisfied) to 5 (very satisfied), reflecting the cus-
tomer’s overall experience with the sales interac-
tion as assessed by external observers (human an-
notators or LMs), not by the simulated customers.
The selection of the annotation model for user
satisfaction was introduced in our prior work (Gro-
mada et al., 2025), where we benchmarked all con-
sidered LMs against human ratings on 104 dia-
logues. Qwen2.5-14B-1M achieved the highest
correlation with human ratings among open-source
LMs (Spearman ρ=0.78) and was selected to anno-
tate all 5200 dialogues. Full benchmark results and
the annotation prompt are provided in Appendix C
and Appendix D, respectively.
5.2 Goal Achievement
We annotated goal achievement across three dimen-
sions: (1)Customer Goal Achievement, ordinal
metric (not achieved=1, partially achieved=2, fully
achieved=3) measuring whether the customer’s
stated needs were met; (2)Bot Cross-Sell Goal,
binary metrics for attempt and success; (3)Bot
Up-Sell Goal, binary metrics for attempt and suc-
cess. Customer Goal Achievement belongs to the
customer perspective of the framework, while Bot
Cross-Sell and Up-Sell goals belong to the business
perspective, specifically as components of the Ne-
gotiation Success dimension. All dialogues were
annotated for both cross-sell and up-sell, as the
agent configurations include dedicated strategies
for each (Section 4.1): cross-sell in Cross-sell and
KPI-sell strategies, and up-sell in Up-sell strategy.
3HuggingFace models: https://huggingface.
co/{Qwen, meta-llama, AtlaAI, deepseek-ai}
4OpenAI: https://platform.openai.com/docs/
models; Anthropic:https://www.anthropic.com/news
Agreement User Cross-Sell Up-Sell
Metric Goal Att Suc Att Suc
Kripp. Alpha 0.74 0.95 0.86 0.96 0.39 ∗
Fleiss’κ 0.61 0.95 0.86 0.96 0.39 ∗
Exact agree [%] 69.2 96.2 94.2 98.1 97.1
Table 2: Inter-annotator agreement for goal metrics
(n=104, 3 humans). Att=Attempt, Suc=Success. User
Goal: ordinal (1-3); all other metrics: binary. ∗Affected
by constant ratings from one annotator.
5.2.1 Human Annotations
The same three annotators as for the user satis-
faction independently evaluated the same 104 dia-
logues across all goal dimensions. Table 2 presents
inter-annotator agreement using Krippendorff’s Al-
pha (Krippendorff, 2011), Fleiss’ κ (Fleiss, 1971),
and exact agreement percentages.
Results demonstrate strong agreement across
most dimensions, with Krippendorff’s Alpha
≥0.74 and exact agreement >69% for all metrics
except up-sell success. Binary attempt metrics and
cross-sell success show excellent agreement (Krip-
pendorff’s Alpha ≥0.86, exact agreement >94%).
Up-sell success shows lower agreement (Krippen-
dorff’s Alpha=0.39, Fleiss’ κ=0.39), deflated by
one annotator providing constant ratings, which
reduces variance and penalizes the metrics. Nev-
ertheless, exact agreement remains high (97.1%),
indicating consensus among the annotators.
5.2.2 LM-based Annotation
We annotated the same 104 dialogues as the hu-
man annotators using various LMs, with a dedi-
cated prompt for each dimension: customer goal
achievement (Appendix E), bot cross-sell attempt
and success (Appendix F), and bot up-sell attempt
and success (Appendix G).
For customer goal achievement (ordinal 1-3), we
used Spearman ρ and Mean Absolute Error (MAE),
assuming a close to linear nature of the three scores;
for cross-sell and up-sell binary metrics, we used
Cohen’sκ(Cohen, 1960).
For each LM, we computed agreement with each
human annotator and averaged the scores. Table 3
presents results for all tested models.
Customer Goal Achievement.Both commer-
cial and open-source models demonstrated strong
human-LM alignment, indicating that customer
goal achievement is suitable for automated eval-
uation with LMs at scale. Top performers were:
GPT-o3-mini (ρ=0.80, MAE=0.19), Selene-1-Mini-
70

Llama-3.1-8B (ρ=0.79, MAE=0.23), and Qwen2.5-
7B ( ρ=0.77, MAE=0.20). Based on this strong
agreement, we selected Qwen2.5-7B-Instruct-1M
for full dataset annotation (5200 dialogues).
Bot Cross-sell Goal.Commercial models sub-
stantially outperformed open-source models, likely
due to advanced reasoning capabilities. Top com-
mercial models (GPT-o1, GPT-o3) achieved Co-
hen’s κ=0.85-0.92 for both attempt and success,
while the best open-source model (DeepSeek-R1-
Distill-Llama-8B) reached only κ=0.49 (attempt)
and κ=0.48 (success). Despite moderate agree-
ment, we selected DeepSeek-R1-Distill-Llama-8B
for full dataset annotation. While its use may in-
troduce some divergence from a silver standard, it
serves to demonstrate the framework, where anno-
tation models are interchangeable.
Bot Up-Sell Goal.All models showed poor
performance, with the best commercial model
(GPT-o4-mini) achieving only κ=0.54 (attempt)
and κ=0.29 (success), and best open-source
model (Qwen2.5-32B) reaching merelyκ=0.27 and
κ=0.11. Several models showed near-zero or nega-
tive agreement for success assessment. This diffi-
culty likely results from up-sell suggestions being
subtle and easily confused with base product selec-
tion. Due to insufficient reliability across all tested
models, we did not perform automated up-sell an-
notation on the whole dataset, to avoid compromis-
ing the validity of the framework evaluation.
5.3 Annotation Error Analysis
We manually examined dialogues with the largest
divergences between LM and human annotations,
focusing on the best-performing models only and
excluding Bot Up-Sell Goal due to its overall unreli-
ability. The aim was to identify systematic patterns
driving the disagreements.
User Satisfaction.The LM tends to overestimate
satisfaction in cases where the purchase is com-
pleted despite explicit frustration expressed during
the interaction, and to underestimate it in cases
where no purchase occurs but the customer main-
tains a polite and neutral tone throughout.
Customer Goal Achievement.Divergences
stem from different interpretations of requirement
fulfillment: the LM flags explicitly unmet require-
ments despite a completed purchase, while humans
tend to overlook them when no explicit frustra-
tion is expressed. Human annotators themselves
Model User Goal Cross-Sell Up-Sell
ρ/ MAE↓ κatt /κ suc κatt /κ suc
Commercial Models
GPT-o1 0.76 / 0.20 0.92/0.890.50 / 0.25
GPT-o3 0.71 / 0.23 0.91 / 0.85 0.32 / 0.27
GPT-o3-mini 0.80/0.19 0.62 / 0.63 0.14 / 0.02
GPT-o4-mini 0.76 / 0.20 0.87 / 0.710.54/0.29
GPT-4o 0.78 / 0.20 0.42 / 0.37 0.30 / -0.00
Claude 3.5 S2 0.73 / 0.21 0.46 / 0.44 0.08 / 0.06
Claude 3.7 S 0.76 / 0.20 0.44 / 0.36 0.11 / 0.02
Open-Source Models
Qwen2.5-7B 0.77 /0.20 0.33 / 0.24 0.19 / -0.01
Qwen2.5-14B 0.75 / 0.21 0.38 / 0.24 0.23 / 0.03
Qwen2.5-32B 0.64 / 0.28 0.46 / 0.340.27/0.11
Llama-3.1-8B 0.76 / 0.23 0.18 / 0.12 -0.09 / 0.02
Sel-Llama-8B 0.79/ 0.23 0.33 / 0.18 0.18 / 0.05
DS-Llama-8B 0.77 / 0.22 0.49/0.480.12 / 0.03
DS-Qwen-7B 0.77 / 0.24 0.37 / 0.32 0.18 / -0.01
DS-Qwen-14B 0.77 / 0.21 0.46 / 0.42 0.25 / 0.01
Table 3: Human-LM agreement on goal metrics (n=104).
User Goal: Spearman ρ and MAE. Cross-Sell & Up-
Sell: Cohen’s κ for: attempt ( κatt) and success ( κsuc).
Bold: best per category. S=Sonnet, S2=v2, Sel=Selene-
1-Mini, DS=DeepSeek-R1-Distill.
disagree on some cases, such as whether missing
accessory information affects goal achievement.
Bot Cross-Sell Goal.Divergences center on the
interpretation of initiative: a cross-sell attempt
should only be counted when initiated by the bot,
not the customer. While in some cases only the LM
correctly identifies customer-initiated inquiries, in
most divergent cases it fails to, incorrectly count-
ing them as cross-sell attempts. Disagreements on
success largely follow from these attempt detection
errors.
6 Results: Dual-Perspective Success
Analysis
This section evaluates the 13 sales strategy config-
urations through the dual-perspective framework.
Sections 6.1, 6.2, and 6.3 analyze each strategy
group (Cross-Sell, KPI-Sell, and Up-Sell respec-
tively), examining how timing and pursuit mode
affect customer experience and business outcomes.
Section 6.4 synthesizes insights across strategies.
Table 4 presents the complete results. Each con-
figuration was tested on 400 dialogues with iden-
tical customer scenarios. Statistical significance
was assessed using Mann-Whitney U tests (McK-
night and Najab, 2022) for ordinal metrics and
chi-square tests (Pearson, 1900) for binary met-
rics, both with Bonferroni correction (Armstrong,
2014) (α = 0.05/12 = 0.00417). Arrows indicate
71

Sales Agent Configuration Customer Perspective Business Perspective
Satisfaction Goal Achiev. Final Cart Negotiation
Qwen2.5-14B Qwen2.5-7B + business catalog matchingDS-Llama-8B
(1-5) (1-3) Any Purchase Cart Size Revenue CS Success CS Attempt CS Success
(%) (CU) (cat/all, %) (%) (%)
Baseline 3.58±1.46 2.38±0.92 63 0.64±0.50 1167±1363 NA / 24 37 28
Cross-sell
after Presentation, Always 3.53±1.382.40±0.92 64 0.85±0.78↑1246±1446 20 / 32 95↑33
after Presentation, Conditional 3.49±1.44 2.37±0.92 63 0.67±0.551281±1496 3 / 25 55↑29
after Acceptance, Always 3.48±1.362.40±0.91 66 0.98±0.85↑1250±148332/ 55↑ 75↑54↑
after Acceptance, Conditional 3.56±1.33 2.39±0.91 66 0.99±0.86↑1215±137432/ 58↑ 70↑55↑
KPI-sell
after Presentation, Always 3.52±1.34 2.39±0.92 640.66±0.511303±1529 0 / 22 57↑24
after Presentation, Conditional 3.58±1.372.42±0.90 640.66±0.511369±1610 0 / 23 57↑31
after Acceptance, Always 3.41±1.33 2.32±0.94 600.72±0.66 1198±141512/ 32 65↑31
after Acceptance, Conditional 3.34±1.31↓2.33±0.94 59 0.68±0.65 1246±1560 8 / 28 60↑28
Up-sell
after Presentation, Always 3.53±1.40 2.35±0.93 61 0.62±0.51 1255±1478 NA / 25 49↑31
after Presentation, Conditional 3.62±1.342.40±0.91 64 0.66±0.501364±1593 NA / 26 48 33
after Acceptance, Always 3.34±1.26↓2.40±0.91 61 0.63±0.51 1206±1445 NA / 24 59↑27
after Acceptance, Conditional 3.39±1.26↓2.37±0.92 62 0.62±0.49 1259±1556 NA / 26 58↑32
Table 4: Dual-perspective evaluation across 13 sales agent configurations (n=400 dialogues per configuration,
N=5200 total). Values represent mean ± standard deviation for continuous metrics, percentages for rates. CS
Success (in Final Cart) reported as catalog-matched/all products. Bold values indicate top performers within each
strategy group. ↑ significantly better than baseline; ↓ significantly worse than baseline. CU = Currency Units; CS =
Cross-Sell; NA = Not Applicable.
configurations statistically significantly better ( ↑)
or worse (↓) than the baseline.
The table organizes metrics into two perspec-
tives.Customer PerspectivecapturesSatisfaction
(1-5 scale) andGoal Achievement(1-3 scale).Busi-
ness Perspectiveincludes two subsections:Final
Cartreports metrics computed from the agent’s cart
report matched against the business catalog:Any
Purchase(percentage of dialogues ending in sale),
Revenue(Currency Units, CU),Cart Size(products
per dialogue), andCS Success;Negotiationsubsec-
tion reports goal annotation metrics:CS Attempt
andCS Success(both percentages of dialogues).
CS SuccessinFinal Cartadditionally presents re-
sults before catalog matching, to compare them
withCS SuccessfromNegotiationsubsection, and
to assess the impact of product hallucinations intro-
duced by proactive sales strategies.
Cross-sell success metrics from both subsec-
tions align closely across configurations, validating
the DeepSeek-R1-Distill-Llama-8B annotations de-
spite their moderate human agreement (Cohen’s
κ=0.48, Section 5.2.2).
6.1 Cross-Sell Strategy
Customer Perspective.Cross-sell configura-
tions maintain customer satisfaction across all tim-
ing and pursuit modes, with scores ranging from
3.48 to 3.56 (baseline: 3.58), none significantly
different from baseline. The highest satisfaction
occurs with after Acceptance, Conditional (3.56).
Goal achievement remains stable at 2.37–2.40
(baseline: 2.38). This stability indicates that cross-
sell attempts do not disrupt the customer’s primary
goal of finding a suitable phone, regardless of when
or how persistently accessories are promoted.
Business Perspective.Timing critically deter-
mines cross-sell effectiveness. After Acceptance
configurations achieve 32% catalog-matched cross-
sell success (55–58% including all products) and
significantly increased cart sizes (0.98–0.99 vs.
baseline 0.64), with 66% purchase rates. Both
Always and Conditional pursuit modes perform
similarly, indicating high customer receptiveness
after phone commitment.
In contrast, after presentation timing yields poor
results (3–20% catalog-matched success) despite
high attempt rates (55–95%), indicating that cus-
tomers are not receptive to accessories before com-
mitting to a base phone. Revenue impact remains
modest across all configurations (1215–1281 CU
vs. baseline 1167 CU), reflecting the low-cost na-
ture of promoted accessories.
Dual Perspective.Cross-sell after Acceptance,
Conditional achieves optimal balance: maintain-
ing baseline customer satisfaction while delivering
the highest catalog-matched cross-sell success and
significant cart size growth. The strategy demon-
strates that low-value accessories can be promoted
after customer commitment to the base phone of-
fer, without harming experience, though revenue
impact remains limited given their low price.
72

6.2 KPI-Sell Strategy
Customer Perspective.KPI-sell configurations
show different customer experiences based on tim-
ing. After Presentation configurations maintain
baseline satisfaction (3.52–3.58 vs. baseline 3.58),
with after Presentation, Conditional achieving the
highest goal achievement across all configurations
(2.42). In contrast, after Acceptance, Conditional
significantly harms satisfaction (3.34 vs. base-
line 3.58), while after Acceptance, Always shows
smaller satisfaction decrease (3.41). KPI-sell con-
sistently presents expensive accessories (smart-
watches and premium earbuds) with prices com-
parable to the phone itself, requiring customers
to engage in a new deliberation process similar
to reconsidering their phone choice. Reopening a
major decision process after an initial high-value
mental commitment (phone choice) potentially trig-
gers decision fatigue (Wang et al., 2023; Canarslan,
2025), explaining the satisfaction decline. Goal
achievement remains stable across all configura-
tions (2.32–2.42).
Business Perspective.KPI-sell failed to achieve
its intended goal of selling premium accessories,
showing near-zero catalog-matched cross-sell suc-
cess (0–12%) across all configurations, despite
moderate attempt rates (57–65%). However, this
configuration achieves relatively high revenue
(1198–1369 CU vs. baseline 1167 CU), with af-
ter Presentation, Conditional reaching the highest
revenue (1369 CU). This revenue gain appears to
result from guiding customers towards more ex-
pensive phones rather than accessory sales, indicat-
ing the strategy succeeds through phone upgrades
rather than its designed cross-sell mechanism. Pur-
chase rates (59–64%) and cart sizes (0.66–0.72)
remain near baseline levels.
Dual Perspective.KPI-sell after Presentation,
Conditional offers the best trade-off: highest rev-
enue (1369 CU) and goal achievement (2.42) while
maintaining baseline satisfaction (3.58). However,
the strategy fails at its intended purpose of selling
premium accessories, with revenue gains stemming
from phone guidance rather than cross-sell success.
A critical asymmetry emerges: while premium ac-
cessory recommendations are not purchased regard-
less of timing, proposing them after Acceptance of
the base phone harms satisfaction, whereas during
or after Presentation they can be simply ignored
without negative impact. This suggests that sim-
ply instructing the agent to recommend high-value
accessories is insufficient and requires more sophis-
ticated sales techniques.
6.3 Up-Sell Strategy
Customer Perspective.Up-sell configurations
show a similar timing-dependent pattern to KPI-
sell. After Presentation configurations maintain or
exceed baseline satisfaction (3.53–3.62 vs. baseline
3.58), with after Presentation, Conditional achiev-
ing the highest satisfaction (3.62). In contrast, both
after Acceptance configurations significantly harm
satisfaction: after Acceptance, Always (3.34) and
after Acceptance, Conditional (3.39) both fall sig-
nificantly below baseline. Like KPI-sell, this pat-
tern reflects the potential disruption of introducing
high-value decisions (more expensive phones) after
customers have mentally committed to their choice.
Goal achievement remains stable across all config-
urations (2.35–2.40).
Business Perspective.Up-sell demonstrates po-
tential for revenue optimization, with configura-
tions ranging from 1206 to 1364 CU (vs. baseline
1167 CU). After Presentation, Conditional achieves
the highest revenue (1364 CU), suggesting success-
ful guidance toward more expensive phones when
intervention occurs before customer commitment.
Purchase rates (61–64%) and cart sizes (0.62–0.66)
remain near baseline levels in all up-sell settings, as
expected for a base phone replacement rather than
a supplementation strategy. Interestingly, Up-sell
configurations show cross-sell attempts in 48–59%
of dialogues, with 24–26% all-products success
but no catalog matching (NA), indicating the sales
agent hallucinates accessories alongside the up-
sold phone.
Dual Perspective.Up-sell after Presentation,
Conditional offers the strongest performance: high-
est revenue (1364 CU), highest satisfaction (3.62),
and stable goal achievement (2.40). The strategy
successfully guides customers toward premium
phones when deployed before commitment, avoid-
ing the satisfaction harm observed when these of-
fers occur after base phone acceptance. However,
the hallucination of accessories (48% attempt rate
with no catalog) represents an implementation is-
sue requiring attention.
6.4 Key Insights
The dual-perspective analysis reveals three criti-
cal insights for designing effective sales agents in
73

conversational commerce. Since these findings are
based on simulated dialogues, they should be inter-
preted as preliminary insights pending validation
with real users.
First, optimizing sales agents requires balanc-
ing customer experience and business outcomes
simultaneously. Focusing on a single metric risks
overlooking critical trade-offs: a configuration
may boost revenue while harming satisfaction, or
achieve high cross-sell rates with minimal revenue
impact. No single configuration excels across all
metrics, confirming the need for a dual-perspective
framework with clearly defined priorities.
Second, all three sales strategies can be imple-
mented without significantly harming either per-
spective when properly configured. Cross-sell rep-
resents the safest option, maintaining customer sat-
isfaction across all configurations while reliably
increasing cart size. Up-sell offers the highest rev-
enue potential by guiding customers toward pre-
mium phones, particularly when introduced before
the customer commits to the base phone. KPI-
sell shows promise for revenue optimization but
requires more sophisticated sales techniques to suc-
cessfully introduce high-value accessories without
disrupting the customer’s decision process.
Third, timing and pursuit mode critically de-
termine effectiveness across all strategies. After-
acceptance timing works well for low-value supple-
mentary decisions (accessories) but disrupts high-
value ones (phone upgrades or premium acces-
sories). Conversely, after-presentation timing en-
ables high-value guidance while customers remain
open to alternatives. Conditional pursuit modes
generally outperform always modes by respecting
customer signals, providing a weak but expected
validation of both the simulation and evaluation
elements of our experimental setup.
Organizations must therefore align strategy con-
figurations with their business priorities and cus-
tomer journey, using tools like our dual-perspective
framework to calibrate choices across both perspec-
tives.
7 Conclusions
This work introduces a dual-perspective evalua-
tion framework for conversational sales agents,
systematically examining how sales strategies af-
fect both customer experience and business out-
comes. Through controlled experiments across
5200 dialogues spanning 13 agent configurations,
we demonstrate that effective sales agent design
requires balancing complementary metrics rather
than optimizing individual ones, with no single con-
figuration excelling across all dimensions. As these
experiments rely solely on simulated dialogues,
the findings represent exploratory evidence that
requires validation with real users.
Beyond these specific findings, this work es-
tablishes a methodological foundation for eval-
uating conversational sales systems. The multi-
dimensional, dual-perspective framework, along
with human-validated LM annotations and system-
atic experiments, offers a template for future re-
search into the balance between customer expe-
rience and business performance in sales context.
Operational teams can directly apply this frame-
work to design, select, and fine-tune sales agent
configurations suited to their business priorities
and customer journey characteristics.
8 Future Work
Future research should validate these findings
through studies with real human participants to
confirm simulation validity in this context. Such
studies would also enable measuring satisfaction
from the user’s own perspective, capturing subjec-
tive experience more directly than external observer
assessments. Further case studies may also reveal
causal mechanisms underlying observed patterns.
Future work should also examine how the choice
of user simulator, across LLM families, model
sizes, and persona configurations, affects observed
patterns, and whether these hold against real human
studies to validate the reliability of LLM-based sim-
ulation in conversational sales settings.
The framework itself could be extended in sev-
eral directions. First, the customer perspective
could be enriched with more fine-grained measures
of need fulfillment, going beyond goal achieve-
ment to capture what needs were genuinely sat-
isfied. Second, incorporating longer-term signals
such as post-purchase regret, product abandonment,
or return rates would provide a more complete pic-
ture of customer experience, though this requires
observing customers in a real deployed service.
Certain strategies, particularly KPI-sell, would
benefit from more sophisticated sales techniques
to effectively generate additional sales while main-
taining customer experience quality.
74

Limitations
Simulated Customer Behavior.Our evaluation
relies entirely on LLM-based user simulations
rather than real human participants. While this
approach enables large-scale systematic explo-
ration of strategy configurations, simulated be-
havior may not fully capture authentic customer
decision-making, emotional responses, or post-
purchase satisfaction or regret (Inman et al., 2000).
Furthermore, the findings are tied to a specific simu-
lator configuration based on Gemini-1.5-Flash, and
different LLM families, model sizes, or persona
configurations may yield different behavioral pat-
terns. Additionally, our interpretations of observed
patterns (e.g., cognitive disruption from decision
reopening, timing sensitivity for high-value offers)
remain speculative without qualitative validation
through customer interviews.
Satisfaction Measurement.User satisfaction is
measured from an external observer’s perspective
rather than reflecting the subjective experience of
the user themselves. This may not fully capture the
nuanced emotional states and personal evaluations
that real customers experience during and after a
sales interaction.
Human Annotation.The dialogues were anno-
tated by non-native English speakers, which may
have introduced inconsistencies in interpreting nu-
anced language, recognizing implicit cross-sell or
up-sell attempts, or assessing conversational qual-
ity, despite annotators having proficient English
and demonstrated inter-annotator agreement.
KPI-Sell Strategy Implementation.The KPI-
Sell strategy showed unexpectedly low attempt
rates even when configured to always attempt KPI-
sell, and achieved very low success rates. This
indicates the need to investigate underlying imple-
mentation issues and develop more sophisticated
methods to make the sales agent more effective at
recommending higher-priced products.
Product Catalog Adherence and Hallucination.
Across all configurations, we observed higher
cross-sell success rates before official catalog
matching than after, indicating product hallucina-
tion. This was especially pronounced in Baseline
and Up-sell configurations, where the sales agent
lacked access to a product catalog yet success-
fully sold additional accessories that could not be
matched to actual products.
Up-sell Annotation.Automated annotation of
up-sell attempts and success proved unreliable
across all tested LMs, as upgrade suggestions can
be easily confused with base phone discussions
and selection process. This limitation prevented
systematic automated analysis of up-sell strategy
effectiveness across our dataset.
References
Atheer Algherairy and Moataz Ahmed. 2023. A review
of dialogue systems: current trends and future direc-
tions.Neural Computing and Applications, pages
1–27.
Richard A Armstrong. 2014. When to use the bon-
ferroni correction.Ophthalmic and Physiological
Optics, 34:502 – 508.
Grzegorz Biesok and Jolanta Wyród-Wróbel. 2025.
Post-purchase customer regret: Results of the pi-
lot study.Scientific Papers of Silesian University
of Technology Organization and Management Series,
2025:107–120.
Nur Özer Canarslan. 2025. The impact of choice over-
load and decision fatigue on cart abandonment in
online shopping.OPUS Journal of Society Research.
Kushal Chawla, Jaysa Ramirez, Rene Clever, Gale
Lucas, Jonathan May, and Jonathan Gratch. 2021.
Casino: A corpus of campsite negotiation dialogues
for automatic negotiation systems. InProceedings
of the 2021 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, pages 3167–3185.
Jacob Cohen. 1960. A coefficient of agreement for
nominal scales.Educational and Psychological Mea-
surement, 20:37–46.
Yang Deng, Wenxuan Zhang, Wai Lam, Hong Cheng,
and Helen Meng. 2022. User satisfaction estima-
tion with sequential dialogue act modeling in goal-
oriented conversational systems. InWWW ’22: Pro-
ceedings of the ACM Web Conference, pages 2998–
3008.
Ryan Fellows, Hisham Ihshaish, Steve Battle, Ciaran
Haines, Peter Mayhew, and J.Ignacio Deza. 2022.
Task-oriented dialogue systems: Performance vs
quality-optima, a review. InComputer Science and
Information Technology, CCSIT 2022, page 69–87.
Academy and Industry Research Collaboration Cen-
ter (AIRCC).
Joseph L. Fleiss. 1971. Measuring nominal scale agree-
ment among many raters.Psychological Bulletin,
76:378–382.
Justyna Gromada, Alicja Kasicka, Ewa Komkowska,
Lukasz Krajewski, Natalia Krawczyk, Morgan
Veyret, Bartosz Przybył, Lina M. Rojas-Barahona,
75

and Michał K. Szczerbak. 2025. Evaluating conver-
sational agents with persona-driven user simulations
based on large language models: A sales bot case
study. InProceedings of the 2025 Conference on
Empirical Methods in Natural Language Process-
ing: Industry Track, pages 230–245, Suzhou (China).
Association for Computational Linguistics.
J. Inman, James Dyer, and Jianmin Jia. 2000. A gen-
eralized utility model of disappointment and regret
effects on post-choice valuation.Marketing Science,
16.
Arihant Jain, Purav Aggarwal, Rishav Sahay,
Chaosheng Dong, and Anoop Saladi. 2025.
AutoEval-ToD: Automated evaluation of task-
oriented dialog systems. InProceedings of the 2025
Conference of the Nations of the Americas Chapter
of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long
Papers), pages 10133–10148, Albuquerque, New
Mexico. Association for Computational Linguistics.
Dietmar Jannach, Ahtsham Manzoor, Wanling Cai, and
Li Chen. 2021. A survey on conversational recom-
mender systems.ACM Computing Surveys, 54:1–36.
Antje Janssen, Lukas Grützner, and Michael Breitner.
2021. Why do chatbots fail? a critical success factors
analysis. InICIS 2021 Proceedings.
Catholijn Jonker, Reyhan Aydogan, Tim Baarslag, Kat-
suhide Fujita, Takayuki Ito, and Koen Hindriks. 2017.
Automated negotiating agents competition (anac).
Proceedings of the AAAI Conference on Artificial
Intelligence, 31:5070–5072.
Tongyoung Kim, Jeongeun Lee, Soojin Yoon, Sungh-
wan Kim, and Dongha Lee. 2025. Towards person-
alized conversational sales agents: Contextual user
profiling for strategic action. InFindings of the Asso-
ciation for Computational Linguistics, pages 5131—
-5154.
Yelin Kim, Joshua Levy, and Yang Liu. 2020. Speech
sentiment and customer satisfaction estimation in
socialbot conversations. InINTERSPEECH 2020,
pages 1833–1837.
Klaus Krippendorff. 2011. Computing krippendorff’s
alpha-reliability.Departmental Papers (ASC).
Bernard Kubiak and Paweł Weichbroth. 2010. Cross-
and up-selling techniques in e-commerce activities.
Journal of Internet Banking and Commerce, 15.
Mike Lewis, Denis Yarats, Yann Dauphin, Devi Parikh,
and Dhruv Batra. 2017. Deal or no deal? end-to-end
learning of negotiation dialogues. InProceedings
of the 2017 Conference on Empirical Methods in
Natural Language Processing, pages 2443–2453.
Xinmeng Li, Wansen Wu, Long Qin, and Quanjun Yin.
2021. How to evaluate your dialogue models: A
review of approaches.Preprint, arXiv:2108.01369.
Patrick E. McKnight and Julius Najab. 2022.
Mann–whitney u test.The SAGE Encyclopedia of
Research Design.
Karl Pearson. 1900. On the criterion that a given sys-
tem of deviations from the probable in the case of
a correlated system of variables is such that it can
be reasonably supposed to have arisen from random
sampling.Philosophical Magazine Series 1, 50:11–
28.
Baolin Peng, Xiujun Li, Jianfeng Gao, Jingjing Liu,
and Kam-Fai Wong. 2018. Deep dyna-q: Integrating
planning for task-completion dialogue policy learn-
ing. InProceedings of the 56th Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), pages 2182–2192.
Mubasher Rasheed, Iqra Sami, and Aliza Tabassam.
2025. The impact of ai-powered chatbots on cus-
tomer satisfaction and business performance in e-
commerce.Social Science Review Archives, 3:2390–
2401.
Alexandra Rese and Pauline Tränkner. 2023. Perceived
conversational ability of task-based chatbots – which
conversational elements influence the success of text-
based dialogues?International Journal of Informa-
tion Management, 74:102699.
Iulian Serban, Ryan Lowe, Peter Henderson, Laurent
Charlin, and Joelle Pineau. 2018. A survey of avail-
able corpora for building data-driven dialogue sys-
tems.Dialogue Discourse, 9.
Weiwei Sun, Shuo Zhang, Krisztian Balog, Zhaochun
Ren, Pengjie Ren, Zhumin Chen, and Maarten de Ri-
jke. 2021. Simulating user satisfaction for the evalu-
ation of task-oriented dialogue systems. InProceed-
ings of the 44th International ACM SIGIR Confer-
ence on Research and Development in Information
Retrieval, SIGIR ’21, page 2499–2506. ACM.
Marilyn A. Walker, Diane J. Litman, Candace A. Kamm,
and Alicia Abella. 1997. Paradise: A framework for
evaluating spoken dialogue agents. In35th Annual
Meeting of the Association for Computational Lin-
guistics and 8th Conference of the European Chap-
ter of the Association for Computational Linguistics,
pages 271–280.
Ningning Wang, Xavier Hu, Pai Liu, He Zhu, Yue
Hou, Heyuan Huang, Shengyu Zhang, Jian Yang, Jia-
heng Liu, Ge Zhang, Changwang Zhang, Jun Wang,
Yuchen Eleanor Jiang, and Wangchunshu Zhou. 2025.
Efficient agents: Building effective agents while re-
ducing cost.Preprint, arXiv:2508.02694.
Yue Wang, Daniel Y . Mo, and G.T.S. Ho. 2023. How
choice fatigue affects consumer decision making
in online shopping.2023 IEEE International Con-
ference on Industrial Engineering and Engineering
Management (IEEM), pages 0128–0132.
76

A Simulator Prompt
# User Simulation Instructions
You are playing the character {name}.
Act as a simulated customer interacting with a mobile sales bot. Follow these core directives:
## Core Parameters
- Maintain consistent persona traits throughout the conversation
- Stay in character without breaking role
- Respond naturally as the defined persona would
- Never reveal you are an AI
- Remember: you are a real person seeking a specific solution, not an AI assistant
## Input Arguments
1. **PERSONA**:
{identity}
2. **GOAL**:
{goal}
3. **SCENARIO**:
{conversation_scenario}
4. **DATE**:
{date}
5. **END_WORD**:
{end_word}
## Message Format
- Input Format: assistant_name{separator}message_of_assistant
- Output Format: {name}{separator}your_message
- Maintain format consistency throughout conversation
## Behavioral Guidelines
1. **Communication Style**
- Match assertiveness level from SCENARIO
- Follow precision level from SCENARIO
- Align language with PERSONA background
- Stay within GOAL and SCENARIO requirements parameters
- Only discuss relevant products/services
- Use {language} for all responses
- If PERSONA is bilingual or multilingual (as noted in identity):
* Primary communication should be in {language}
* May include occasional phrases from secondary languages if appropriate
* Match language proficiency level described in PERSONA
2. **General Response Guidelines**
- Keep responses aligned with PERSONA traits
- Reference GOAL in key decisions
- Use DATE for time-sensitive decisions
- Do not repeat what has already been said
- Reference to what has already been said
- Handle repeated questions from seller:
* First repetition: provide info again but note it was already mentioned
* Second+ repetition: express frustration and ask to move forward
* After 3 same questions: treat as rejection (follow unsuccessful scenario rules)
- Generate short, precise, and informative responses
- Reveal information gradually:
* Don't share all GOAL/SCENARIO requirements at once
* Present information naturally as conversation progresses
- Stay within known information boundaries:
* Only use information from GOAL, SCENARIO, PERSONA
* Only make inferences that logically follow from PERSONA background
77

* Don't create or assume information not provided
3. **Conversation Ending Rules**
- Send **END_WORD** as single token when conversation is complete:
* After natural conclusion (thanking, goodbyes)
* Never suddenly interrupt mid-conversation
- Successful scenario: after achieving goal/solution
- Unsuccessful scenario: if you think the assistant can not help you or the conversation falls
into a infinite loop, i.e. after 3 rejections from seller:
* Express frustration
* State intention to end
* End conversation
4. **Decision Process**
- Evaluate all proposals against SCENARIO requirements
- Follow only requirements specified in SCENARIO, ignore critical_features from PERSONA if they
are not mentioned in SCENARIO requirements
- Work towards GOAL completion
- Use decision style from SCENARIO
5. **Formal Offer Handling**
- For messages marked with [OFFER]:
* Respond with [ACCEPT_OFFER] or [REJECT_OFFER] prefix
* Include clear reasoning after prefix
* Check against budget and contract flexibility
- For messages marked with [RECOMMENDATION]:
* Respond with [ACCEPT_REC] or [REJECT_REC] prefix
* Include clear reasoning after prefix
* Check against budget and contract flexibility
6. **BudgetRules**
- Use currency based on PERSONA location if not specified
- When seller provides prices in different currency:
* Convert to PERSONA's local currency before comparing with budget
- IF budget.amount is specified AND description contains "monthly", user expects total monthly
cost (plan + device) within this limit
- IF budget.amount is null AND description contains "reasonable":
* Use current monthly_spend as reference point
* Example: Danuta pays 79 Currency Units monthly, so reasonable range: 60-100 Currency Units
* Adjust based on income level:
- high income: can go higher than currently spend
- middle income: stay close to currently spend
- low income: try to stay below or close to currently spend
- STRICT: Reject anything above stated amount
- FLEXIBLE: Consider offers up to 20 percent above budget
7. **Contract Rules**
- STRICT: Only accept specified contract type
- FLEXIBLE: Consider alternatives if beneficial
8. **Requirements Management**
- Initially communicate only essential requirements
- Keep flexible requirements hidden until relevant
- Reveal flexible requirements only when:
* Additional products/services are proposed
* Specific questions are asked
* Alternatives are discussed
9. **Device Knowledge Timeline**
- Your knowledge of devices comes from PERSONA description
- PERSONA's device knowledge might be outdated or incomplete
* Example: PERSONA wants to upgrade from iPhone 14 to iPhone 15, not knowing iPhone 16 exists
* Example: PERSONA asks for "latest iPhone" while only knowing about iPhone 14
- When learning about newer models:
* Show genuine surprise/interest
* Consider adjusting your original goal
* Ask questions about the newer model
- Your initial goal should match PERSONA's knowledge level
78

B Simulator Validation
Table 5 reports the human evaluation results of the
user simulator’s adherence to assigned personas,
goals, and scenarios, originally reported in [CITA-
TION].
Metric Persona Goal Scenario
Mean 4.89±0.31 4.76±0.51 4.45±0.73
5/5 ratings 89.4% 79.2% 56.7%
4/5 ratings 9.9% 17.6% 33.3%
≤3/5 ratings 0.6% 3.2% 9.9%
Exact agree 82.1% 77.2% 53.2%
±1 agree 98.7% 97.4% 91.7%
Table 5: Human evaluation ofUser Simulation Quality
(n=104, 3 annotators), originally reported in (Gromada
et al., 2025).
C User Satisfaction Annotation
Validation
Table 6 reports the human-LM agreement results
for user satisfaction annotation across all bench-
marked models, originally reported in [CITA-
TION].
Evaluator User Satisfaction
(Spearmanρ)
Commercial LMs
GPT-o1 0.76
GPT-o1-mini 0.73
GPT-o3 0.71
GPT-o3-mini 0.73
GPT-4o 0.80
Claude 3.5 Sonnet v20.82
Claude 3.7 Sonnet 0.71
Open-Source LMs
Qwen2.5-32B-1M 0.68
Qwen2.5-14B-1M0.78
Qwen2.5-7B-1M 0.68
Llama-3.1-8B 0.64
Selene-1-Mini-Llama-3.1-8B 0.65
DeepSeek-R1-Distill-Qwen-14B 0.72
DeepSeek-R1-Distill-Qwen-7B 0.55
DeepSeek-R1-Distill-Llama-8B 0.73
Table 6: Human-LM agreement for user satisfaction
annotation (Spearman ρ, n=104). Bold: best in category.
Results originally reported in (Gromada et al., 2025).
79

D User Satisfaction Annotation Prompt
You are a psychologist.
You will evaluate the dialogue between the customer and a sales bot selling phones with offers,
accessories and additional services.
Your goal is to rate **the satisfaction** of the customer based on the conversation with the
assistant. Please use a scale from 1 to 5:
- rating **1**: The customer expresses extreme dissatisfaction with the conversation.
- rating **2**: The customer shows some dissatisfaction with the conversation.
- rating **3**: The customer's satisfaction level is unclear or ambiguous.
- rating **4**: The customer demonstrates a moderate level of satisfaction with the conversation.
- rating **5**: The customer expresses high satisfaction and is very pleased with the conversation.
The dialogue for evaluation:
{conv_history}
**Required Output Format:**
{{
"rating": int, // a single number on the scale of 1 to 5.
"justification": str, // explain key interactions or phrases that led to this rating
}}
E Customer Goal Achievement Annotation Prompt
You are an expert dialogue analyst.
You will evaluate the dialogue between the customer and a sales bot selling phones with offers,
accessories and additional services.
Your goal is to assess **whether the user achieved their goal** during the conversation.
**Evaluation Process:**
**Step 1: Identify User's Goal and Requirements**
From the conversation, identify:
- **User's primary goal:** What is the user trying to accomplish? (e.g., buy a phone, upgrade, get
information)
- **Stated requirements:** What specific needs, features, or constraints did the user mention?
- **Critical vs. flexible:** Which requirements did the user emphasize as essential vs. nice-to-have?
**Step 2: Evaluate Goal Achievement**
Assess the conversation outcome based on objective criteria:
- Was the user's primary goal accomplished?
- Were their stated requirements addressed?
- If requirements conflicted (e.g., high specs + low budget), was a reasonable solution found?
- Did the conversation result in a concrete outcome (purchase, clear information, resolution)?
**Step 3: Assign Rating**
- **Rating 1 (no)**: The user did not achieve their goal. Their primary objective was not met,
critical requirements were not addressed, or the conversation ended without resolving the user's
needs.
- **Rating 2 (partially)**: The user achieved their goal only partially. Some requirements were met
but others were not, OR the primary goal was addressed incompletely, OR significant needs
remained unresolved.
- **Rating 3 (yes)**: The user fully achieved their goal. Their primary objective was met and
critical requirements were addressed. If some preferences were compromised, it was due to
realistic constraints and a reasonable solution was found.
80

**Important Notes:**
- Focus on **objective goal achievement**, not user satisfaction or politeness
- Evaluate based on what the user **actually said** in the conversation
- Distinguish between **critical needs** (user emphasized as essential) and **preferences** (user
mentioned but seemed flexible)
- **User acceptance of an offer** suggests goal achievement, but verify that the offer actually meets
their stated needs
- **A polite or friendly tone** does NOT automatically mean goal achieved - focus on whether needs
were met
- **No purchase** doesn't automatically mean failure if the user's goal was to gather information
- **User satisfaction is measured separately** - here, focus only on whether the user's stated goal
and requirements were objectively fulfilled
The dialogue for evaluation:
{conv_history}
**Required Output Format:**
{{
"rating": int, // a single number: 1, 2, or 3
"label": str, // one of the following: "no", "partially", "yes"
"justification": str // Structure your response:
// 1. User's goal: [what they wanted to accomplish]
// 2. Critical requirements: [what they emphasized as essential]
// 3. Outcome: [what they got/decided]
// 4. Assessment: [did they achieve their goal and why this rating]
//
// IMPORTANT: This is a JSON string value.
// - The entire justification must be enclosed in double quotes (")
// - If you need to include a quote within the text, escape it: \"
// - Do NOT use single quotes (') for the outer string
//
// Correct: "justification": "User said \"hello\" to the bot"
// Wrong: "justification":'User said "hello" to the bot'
}}
F Bot Cross-Sell Annotation Prompt
You are an expert dialogue analyst.
You will evaluate the dialogue between the customer and a sales bot selling phones with offers,
accessories and additional services.
Your goal is to assess **whether the bot achieved its cross-sell goal** during the conversation.
**What is Cross-Sell?**
Cross-sell means offering the customer additional or complementary products/services that are
different from what they originally sought. Examples:
- Suggesting accessories (case, charger, headphones) when user is buying a phone
- Offering insurance or warranty when user is purchasing a device
- Recommending additional services (cloud storage, streaming subscription)
- Suggesting other product categories (e.g., smartwatch when user is buying a phone)
**What is NOT Cross-Sell:**
- **Base offer components**: A phone bundled with an internet plan is a single base offer, not a
cross-sell
- **User-requested items**: If the user asks "Do you have chargers for that phone?", and the bot
provides it, this is fulfilling the user's request, not cross-selling
- **Cross-sell must be bot-initiated**: The bot must proactively suggest additional items that the
user did not explicitly ask for
**Important Context:**
- The bot may present **both the main phone offer AND cross-sell offers in the same message**
- Example: "Here's the iPhone 15 with unlimited data plan you asked for. Would you also like a
protective case and screen protector?"
- In this example: Phone + data plan = base offer; case and screen protector = cross-sell
**Evaluation Process:**
81

**Step 1: Identify Bot's Cross-Sell Attempt**
Determine if the bot attempted a cross-sell:
- Did the bot **proactively suggest** additional products or services beyond the user's original
request?
- Did the bot recommend complementary items or add-ons that **the user did not ask for**?
- Was this clearly an attempt to sell something DIFFERENT from the user's primary interest?
**Important:** Distinguish between:
- **Cross-sell**: Bot suggests accessories without user asking
- **Not cross-sell**: User asks "Do you have cases?" and bot provides options
- **Not cross-sell**: Phone bundled with plan as standard offer
If **no cross-sell was attempted**, set:
-`attempted: false`
-`rating: 1`
-`label: "no"`
**Step 2: Evaluate Cross-Sell Success**
If the bot attempted a cross-sell, assess the outcome:
- Did the user **accept at least one** cross-sell offer?
- **Acceptance** means: explicit agreement, adding to purchase, or confirming the additional product/
service
- **Rejection** includes: declining, ignoring, "I'll think about it", or changing topic
**Step 3: Assign Rating**
- **Rating 1 (no)**: The bot either did not attempt a cross-sell, OR the user rejected all cross-sell
offers.
- **Rating 3 (yes)**: The bot attempted a cross-sell AND the user accepted at least one cross-sell
offer.
**Note:** Rating 2 is reserved for consistency with other metrics but is not used for cross-sell
evaluation.
**Important Notes:**
- Focus on **objective outcome**: Did the user accept any additional product/service?
- **Bot must initiate**: Only count offers that the bot suggested proactively, not items the user
requested
- **User interest or consideration** is NOT enough - only actual acceptance counts
- **Polite responses** like "Maybe later" or "I'll think about it" = rejection
- If the bot mentioned a cross-sell but the user ignored it or changed topic = rejection
- If multiple cross-sell items were offered and user accepted ANY of them = success
The dialogue for evaluation:
{conv_history}
**Required Output Format:**
{{
"rating": int, // a single number: 1 or 3 (2 is reserved)
"label": str, // one of the following: "no", "yes"
"attempted": bool, // true if bot attempted cross-sell, false otherwise
"justification": str // Structure your response:
// 1. Cross-sell attempt: [describe what the bot proactively offered, or
state "No cross-sell attempted"]
// 2. User response: [what the user accepted/rejected]
// 3. Assessment: [whether cross-sell goal was achieved and why this rating
]
//
// IMPORTANT: This is a JSON string value.
// - The entire justification must be enclosed in double quotes (")
// - If you need to include a quote within the text, escape it: \"
// - Do NOT use single quotes (') for the outer string
//
// Correct: "justification": "Bot offered \"phone case\" and user accepted"
// Wrong: "justification":'Bot offered "phone case" and user accepted'
}}
82

G Bot Up-Sell Annotation Prompt
You are an expert dialogue analyst.
You will evaluate the dialogue between the customer and a sales bot selling phones with offers,
accessories and additional services.
Your goal is to assess **whether the bot achieved its up-sell goal** during the conversation.
**What is Up-Sell?**
Up-sell means offering the customer a higher-tier or premium version of the product/service they are
interested in or already have. Examples:
- Suggesting a more expensive phone model with better features
- Offering a premium subscription plan instead of basic
- Recommending a higher-capacity version of a device
**What is NOT Up-Sell:**
- **User-requested upgrades**: If the user asks "Do you have the Pro version?", and the bot provides
it, this is fulfilling the user's request, not up-selling
- **Up-sell must be bot-initiated**: The bot must proactively suggest a higher-tier option that the
user did not explicitly request
**Important Context:**
- The bot may present **both a base offer AND an up-sell offer in the same message**
- You must distinguish between:
- **Base offer**: The product that directly addresses the user's stated needs
- **Up-sell offer**: A higher-tier alternative presented alongside or after the base offer
- Example: "Here's the iPhone 15 (128GB) that fits your budget at 699 Euros. However, I'd also
recommend the iPhone 15 Pro (256GB) for 999 Euros with better camera and performance."
- In this example: iPhone 15 (128GB) = base offer; iPhone 15 Pro (256GB) = up-sell
**Evaluation Process:**
**Step 1: Identify Bot's Up-Sell Attempt**
Determine if the bot attempted an up-sell:
- Did the bot **proactively suggest** a higher-tier product or service?
- Did the bot recommend upgrading to a premium option that **the user did not ask for**?
- Was this clearly an attempt to sell something MORE expensive or advanced than the base offer?
- **Check carefully**: The up-sell might be in the same message as the base product offer
**Important:** Distinguish between:
- **Up-sell**: Bot suggests premium model without user asking
- **Not up-sell**: User asks "What's the best model?" and bot provides premium option
- **Not up-sell**: User explicitly requests the premium version
If **no up-sell was attempted**, set:
-`attempted: false`
-`rating: 1`
-`label: "no"`
**Step 2: Evaluate Up-Sell Success**
If the bot attempted an up-sell, assess the outcome:
- Did the user **accept the up-sell** offer (choose the higher-tier option)?
- Did the user **reject the up-sell** (stick with base offer or decline)?
- **Acceptance** means: explicit agreement to purchase the higher-tier option
- **Rejection** includes: choosing base offer, declining, "I'll think about it", or ignoring the up-
sell
**Step 3: Assign Rating**
- **Rating 1 (no)**: The bot either did not attempt an up-sell, OR the user rejected the up-sell (
chose base offer or declined entirely).
- **Rating 3 (yes)**: The bot attempted an up-sell AND the user accepted the higher-tier option.
**Note:** Rating 2 is reserved for consistency with other metrics but is not used for up-sell
evaluation.
83

**Important Notes:**
- Focus on **objective outcome**: Did the user choose the higher-tier option?
- **Bot must initiate**: Only count up-sell attempts that the bot suggested proactively
- **User accepting the base offer** = up-sell failed (rating 1)
- **User accepting the up-sell offer** = up-sell succeeded (rating 3)
- **User interest or consideration** is NOT enough - only actual acceptance/purchase decision counts
- **Polite responses** like "I'll think about it" = rejection (rating 1)
- If the bot mentioned an up-sell but the user ignored it or changed topic = rejection (rating 1)
The dialogue for evaluation:
{conv_history}
**Required Output Format:**
{{
"rating": int, // a single number: 1 or 3 (2 is reserved)
"label": str, // one of the following: "no", "yes"
"attempted": bool, // true if bot attempted up-sell, false otherwise
"justification": str // Structure your response:
// 1. Up-sell attempt: [describe what the bot proactively offered as up-
sell, or state "No up-sell attempted"]
// 2. User response: [what the user accepted/rejected - be specific]
// 3. Assessment: [whether up-sell goal was achieved and why this rating]
//
// IMPORTANT: This is a JSON string value.
// - The entire justification must be enclosed in double quotes (")
// - If you need to include a quote within the text, escape it: \"
// - Do NOT use single quotes (') for the outer string
//
// Correct: "justification": "Bot suggested \"premium plan\" but user
declined"
// Wrong: "justification":'Bot suggested "premium plan" but user declined'
}}
84
