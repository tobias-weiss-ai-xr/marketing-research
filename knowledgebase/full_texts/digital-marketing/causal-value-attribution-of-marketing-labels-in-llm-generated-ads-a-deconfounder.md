---
title: 'Causal Value Attribution of Marketing Labels in LLM-Generated Ads: A Deconfounder Approach'
url: https://arxiv.org/abs/2610.23025
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- "Danhong You</name>\n      <arxiv:affiliation>Eric</arxiv:affiliation>\n    </author>\n    <author>\n\
  \      <name>Wei Jiang</name>\n      <arxiv:affiliation>Eric</arxiv:affiliation>\n    </author>\n  \
  \  <author>\n      <name> Zhiqiang</name>\n      <arxiv:affiliation>Eric</arxiv:affiliation>\n    </author>\n\
  \    <author>\n      <name> Zheng"
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.23025
pages: 74
chars: 157616
fetched_at: '2026-11-08T13:23:03+00:00'
kb_version: 1
---

# Causal Value Attribution of Marketing Labels in LLM-Generated Ads: A Deconfounder Approach

1

Causal Value Attribution of Marketing Labels in LLM-Generated Ads:
A Deconfounder Approach

Danhong You
Shanghai Jiao Tong University
dan1559187326@sjtu.edu.cn
Wei Jiang
Shanghai Jiao Tong University
jiangwei@sjtu.edu.cn
Zhiqiang (Eric) Zheng*
University of Texas at Dallas
ericz@utdallas.edu
Abstract
As AI-generated content becomes commoditized, economic value increasingly shits from final artifacts
to the upstream expertise used to specify inputs that steer LLM generation . Yet organizations lack
systematic methods for valuing this expertise: although they routinely record granular skill primitives,
they face the challenge of  determining which individual skills or configurations causally improve
performance. We ground this emerging problem in generative marketing, where structured expert labels
serve as explicit skill primitives that condition LLM-generated advertisements. Identifying their causal
effects is hard because outcomes are shaped by stochastic LLM mediation, high -dimensional
interactions among multiple labels , and multimodal confounding. To address th ese challenges,  we
propose D-V AE (Deconfounder Variational Autoencoder), a counterfactual -inference framework that
integrates a multi -treatment deconfounder with causal representation learning . D -V AE recovers a
causally disentangled latent representation of expert labeling logic and provides PAC-based theoretical
bounds on  omitted-variable bias arising from  single-treatment confounder s. Applied to 29,177
foundation-makeup ad creatives, D-V AE significantly outperforms state-of-the-art benchmarks in out-
of-sample prediction and counterfactual inference, enabling causal attribution of both individual labels
and label combinations to user engagement. A controlled field experiment provides direct evidence of
its practical value. Label configurations recommended by D-V AE increase total engagement by 32.7%
relative to control configurations and achieve performance statistically indistinguishable from that of
human experts. A simulation study with a known ground-truth causal structure further demonstrates D-
V AE’s superior ability to causally attribute value to individual skills under complex confounding and
treatment interactions . Overall, this study advocates shift ing the analytical focus from valuing AI-
generated products to valuing  the skills that produce them. By converting expert know-how into
scalable, causally grounded recommendations , the framework provides  a methodological foundation
for pricing and optimizing AI-augmented skill portfolios.

Keywords: Skill Valuation, Causal Inference, Marketing Label Attribution, Deconfounder Method,
Large Language Model

 2

1. Introduction
Large language models (LLMs) have drastically reduced the marginal cost of digital content generation
(Stanford HAI 2025). Consequently, producing final artifacts is no longer scarce; what remains scarce
is the skill —the structured know-how to effectively steer, condition, and combine model capabilities
for reliable, high -value outcomes. This technological shift signals a br oader business model
transformation: moving from valuing end products to valuing the upstream skills that produce them.
This transition has already been materialized. The global AI prompt and skill marketplace was
projected to reach $1.74 billion in 2025 (Grand View Research, 2026), with organizations increasingly
licensing and optimizing domain-specific instructions and workflow configurations rather than merely
consuming outputs. Yet, traditional pricing mechanisms and academic valuation frameworks remain
anchored to final products. To value skills effectively, we must pivot methodologically: decomposing
observed product value into the attributable contributions of constituent skills.

Figure 1. Example of an ad creative (copy) and user engagement
We ground this emerging problem in AI-augmented marketing content creation, where LLMs are
increasingly embedded into daily creative workflows (Arora et al., 2025; Reisenbichler et al., 2026). A
prevalent practice is “label -to-copy”: marketers translate campaign intent into structured labels —
compact representations of expert knowledge spanning product efficacy, brand tonality, and audience
persona, which then steer LLM generation ( Zhao et al., 2023 ; Cillo & Rubera, 2025). In our context,

 3

skill refers to the ability to select appropriate labels that guide an LLM in generating ad copies for  a
target audience. The selected labels serve as observable proxies — skill primitives  — while the
underlying logic governing their selection constitutes the latent skill of interest. Consider a campaign
for the makeup brand Carslan Foundation (Figure 1): the creative direction is guided by a label vector
𝐿 specifying efficacy cues (e.g., lightweight, hydrating), tonality cues (e.g., tech-driven aesthetics), and
persona cues (e.g., beauty enthusiasts). Conditioned on this configuration, the LLM generates a copy
𝑋 which leads to user engagement 𝑌 (e.g., likes, comments, collects) that reflects the market resonance
of the chosen label setup. Figure 2(a) formalizes this causal chain: observable  label (𝐿 ) → LLM -
mediated product ( 𝑋) → realized product value ( 𝑌). However, while individual labels are routinely
archived in marketing databases, the strategic logic that binds them remains tacit and highly context
dependent.

Figure 2: Two Causal Structures (a) the causal path of label, copy and user engagement, where
copy is the mediator; (b) the latent label space inference and direct effect on user engagement.
This creates a critical valuation gap: organizations possess granular records of skill primitives
(corresponding to chosen labels) but lack systematic insight into which combinatorial strategies actually
drive performance. Should a student-targeting campaign prioritize “affordability” or a “co-branded IP”
hook? How must the label combination adapt when shifting from everyday utility to holiday gifting?
These decisions hinge on the latent skill: the ability to select and combine labels for a given target
audience. This maps directly onto our core methodological quest: how do we measure the causal value
of label configurations when only aggregate product outcomes (engagements) are observed? Attributing

 4

value to th e underlying skill through observed label configurations requires decomposing aggregate
performance into constituent contributions, a task complicated by high -dimensional label spaces,
complex interactions, and the absence of ground-truth causal signals at the individual-label and label-
configuration levels . In LLM -driven ad creation, this valu e attribution  problem manifests as three
identification challenges for estimating the causal effect of label configurations on engagement:
First, the label-engagement relationship is fully mediated by stochastic LLM generation. Labels do
not directly drive outcomes  (because customers do not see labels directly) ; they operate exclusively
through the generated copy. But identical label sets can yield semantically aligned but stylistically
divergent texts due to stochastic decoding and lexical variation (Renze  & Guven, 2024). This
uncontrolled mediator noise brought by LLM generation obscures the true causal contribution of the
label combination.
Second, the treatment space is high -dimensional and inherently interactive, rendering
experimentation economically prohibitive. Labels form sparse, discrete vectors whose effects are
nonlinear and strongly dependent on combinatorial configurations (e.g., efficacy × tonality × persona).
The resulting combinatorial dimensionality explosion makes exhaustive A/B or factorial testing
operationally infeasible.
Third, latent and multimodal confounding systematically bias observational identification. Latent
confounds are persistent and heterogeneous in scope: some affect multiple labels simultaneously (multi-
treatment confounds), while others affect only a single label (single-treatment confounds). Real-world
ads integrate text and imagery that jointly drive engagement, and these visual features are frequently
co-determined with label choices (e.g., “tech-driven” positioning systematically paired with minimalist
visuals). Failure to account for th ese latent and cross-modal dependenc ies creates structured
confounding that masks the attributed value of individual skills.
These challenges motivate D -V AE (Deconfounder Variational Autoencoder), a counterfactual
inference framework designed to estimate the causal value of expert-selected labels in LLM-mediated
marketing. The central idea is to shift the object of intervention from realized copies to a latent skill
space that faithfully represents the expert logic behind label selection. This shift is necessary because
realized copies contain stochastic narrative and stylistic variation introduced by the LLM, while raw

 5

label vectors are sparse, high -dimensional, and confounded by unobserved campaign and platform
conditions. D -V AE therefore learns an intervention-ready representation that preserves label -driven
semantic intent (Yang et al., 2021), separates it from mediat or-side noise, and adjusts it for observed
and latent confounding. Specifically, multimodal LLM representations are used to capture content -
related and visual confounders (Imai & Nakamura, 2025), the multi-label assignment structure is used
to infer shared latent confounders (Wang & Blei, 2019), and the single label -specific confounders is
theoretically bounded (Oster, 2019). Counterfactual label interventions are then performed in the
deconfounded latent space, enabling causal inference under alternative label configurations (Figure 2b).
Empirical analyses of 29,177 paid ad creatives show that D -V AE learns high-fidelity label
representations (MSEX = 0.1103; mean squared error for ad copy  reconstruction), accurately predicts
observed engagement outcomes (MSEY = 0.0330; mean squared error for engagement prediction ), and
produces causally coherent counterfactual estimates after adjusting for confound ing, achieving an
Interchange Intervention Accuracy (IIA; percentage of latent interventions that reproduce the outcome
of corresponding label interventions ) score of 96.7%. A supplementary controlled field experiment
provides direct  evidence of practical value : label configurations optimized by D -V AE increased
engagement by 32.7% relative to the control configurations (p = 0.0053) and  achieved performance
statistically indistinguishable from that of human experts.
Finally, we conduct a simulation study to evaluate the method more systematically and examine its
generalizability. Synthetic data allow us to specify the ground -truth causal effects as well as the
magnitude and structure of latent confound ing. The simulation captures a general and increasingly
common setting in which skills L steers an LLM to generate a high-dimensional, unstructured artifact
X, which subsequently affects a downstream outcome Y. We instantiate this setting in a labor market
context, where job candidates select keywords to guide LLM in generating self-descriptions intended
to attract recruiters’ attentions. The results comprehensively demonstrate D-V AE’s superior causal -
attribution performance and identify important boundary conditions for its effective application.
Our contributions are threefold:
Theoretically, we formalize a skill -to-product causal value attribution framework that shifts the
analytical lens from valuing final outputs to valuing the upstream skills that generate them. We model

 6

the causal pathway: Skill → LLM-mediated product → downstream value (e.g., L → X → Y). This
reflects the operational reality of AI -augmented workflows: practitioners no longer control the final
output directly; instead, they intervene at the skill level by designing, selecting, and combining input
specifications to steer LLM generation . While prior literature predominantly estimates the effect of
realized content on outcomes (X→Y) (Xiao et al., 2024; Kapoor & Kumar, 2025), we ground valuation
at the actionable skill -intervention stage. By treating the marketing label -to-copy workflow as a
canonical instantiation, we provide a generalizable structure for decomposing product-level value into
constituent skill contributions.
Methodologically, we develop a counterfactual representation learning framework designed to
identify and disentangle label contributions in high-dimensional generative workflows. Standard causal
inference tools often struggle in high-dimensional, unstructured settings, while representation learning
methods can yield biased effects when confounding is not addressed. Our approach learns a latent causal
label space and adjusts for both observed and partially identifiable confounders, enabling more reliable
counterfactual engagement prediction.
Practically, we translate skill valuation into actionable portfolio optimization and pricing insights
for AI-augmented organizations. In complex generative workflows, multiple label components (e.g.,
efficacy cues, tonality frames, audience targeting) are combined, making it challenging for standard
predictive models to disentangle causal drivers from spurious correlations. Our counterfactual
attribution framework quantifies the causal value of labels, revealing which configurations genuinely
drive performance. Applied to the marketing domain, this enables firms to audit, price, and optimize
their skill inventories—allocating resources toward high-ROI skill combinations, retiring redundant or
ineffective ones.
2. Literature Review
Our study intersects three related streams: GenAI in marketing content generation, deconfounder
method and causal representation learning.
2.1 AI in Marketing: Content Generation, Value Attribution and User Engagement
Generative AI powered by LLMs has been deployed widely in marketing applications, including

 7

automated copy generation (Liu et al., 2025; Reisenbichler et al., 2026), ad creative design (Chen et al.,
2024; Kapoor & Kumar, 2025), traffic allocation (Ye et al., 2025), and live-streaming commerce (Wang
et al., 2025). Empirical evidence suggests that LLMs reduce content production costs while increasing
productivity, and  human–AI collaboration  can outperform either human or AI alone (Boussioux et
al,2024; Hartmann et al., 2025). Yet, effective use is uneven: experts can craft more precise prompts
aligned with brand strategy, whereas novices often rely on inefficient trial-and-error (Chen et al., 2024).
Recent advances have explored agentic and skill -based workflows for LLM -driven marketing
content generation. These approaches typically decompose marketing expertise into modular “skills”
or specialized agent roles (e.g., strategist, designer, copywriter) w ithin multi-agent systems (Wang et
al., 2025; Quan et al., 2025). This line of work showcases a move from holistic evaluation of LLM
outputs toward component -level assessment of agent  skills. Some research decomposes LLM -based
workflows into stages such as planning, tool selection, tool calling, and response generation stages,
proposing benchmarks such as CToolEval and AgentQuest to evaluate agents in modular settings (Guo
et al., 2024; Gioacchini et al., 2024). Close to our objetives, CapaBench uses Shapley values to quantify
the marginal contribution and interaction effects of modules such as planning, reasoning, action
execution, and reflection in LLM agents (Yang et al., 2025). Related attribution work in RAG and model
interpretability further traces generated answers to retrieved documents or model predictions to
influential training examples (Qi et al., 2024; Wang et al., 2024). However, these studies focus on
technical modules, retrieved evidence, or training data, leaving unclear the causal value of skills,
individually or in combination, in shaping LLM-generated content and downstream engagement, when
confounds are present but unobserved.
Alongside GenAI, a large literature uses machine learning to predict marketing outcome and
personalize delivery. Typical approaches build user profiles from their historical behavior (Trusov et al.,
2016; Märtin et al., 2023) and train models on clicks and conversions ( Rafieian & Yoganarasimhan,
2021; Chen et al., 202 4) to optimize content allocation (Besbes et al., 2016), often improving
personalization accuracy (Yoganarasimhan, 2020). However, these methods do not aim to determine
value attribution of content creation causally. For example, higher engagement for creatives with a co-
branded IP label may reflect the label’s effect or simply the fact that such labels are more common in

 8

high-budget, high-quality campaigns. Complementary work examines user psychology  (Deng et al.,
2022; Sun et al., 2025) or content features (Xiao et al., 2024; Ellickson et al., 2023) as possible drivers
to engagement , but these are typically downstream insights that provide limited guidance during
upstream content creation.
Methodologically grounded causal studies of LLM -driven marketing remain limited. Existing
work commonly (i) treats LLM outputs as static inputs for engagement prediction via regressions or
black-box neural models (Chen & Chan, 2024; Kapoor & Kumar, 2025), leaving decoding stochasticity
unaddressed; (ii) estimates the average effect of AI assistance using experiment s (Ye et al., 2025;
Reisenbichler et al., 2026), but does not identify the effects of specific prompt components or label
combinations; or (iii) studies human –AI workflows using econometrics at the workflow level but not
at the level of combinatorial label inputs (Wang et al., 2025; Lou & Xie, 2021).
In advertising practice, experts often operationalize marketing knowledge into structured labels
that serve as prompts for LLMs. We therefore study labels not merely as observable content features,
but as upstream interventions in the content-generation process, and aim to identify their indirect causal
effects on engagement as well as the marginal and combinatorial value of individual labels.
2.2 Deconfounder Methods
Confounding is particularly severe in GenAI -driven marketing because it arises from both
observable multimodal factors (e.g., text –image pairing) and latent drivers (e.g., campaign budget,
platform dynamics). These factors jointly shape label choice and engagement but are rarely fully
measured, leaving causal identification confounded.
Existing methods have only partially addressed this problem. Classical proxy -based approaches
require strong and often unverifiable links between observed proxies and latent confounders (Frost
1979). Matching and representation-balancing approaches (e.g., propensity score matching, TARNet)
can reduce imbalance in measured covariates, but they cannot recover confounding information absent
from the data (Caliendo & Kopeinig 2008; Shalit et al., 2017). ML-based causal estimators  such as
Meta-Learners (Künzel et al., 2019) and Double Machine Learning (Chernozhukov et al., 2018) flexibly
adjust for observed covariates, but their validity  still rests on selection on observables , not on
unobserved confounds. This is a critical limitation in our setting, where label choices and engagement

 9

are shaped by external semantic factors, campaign conditions, and market context that are not directly
observed — and LLM -mediated generation compounds the issue by routing the label –engagement
relationship through an additional unobserved process: how the LLM produces the ad copy.
The use of an LLM, however, also creates a new opportunity. Unlike traditional ML estimators
(e.g., double machine learning) that are trained solely on the study data, pretrained LLMs have already
encoded external semantic associations from their large tra ining corpus. These associations are
unobserved in the study data but shape both how labels are transformed into ad copy and how users
respond to the generated content. In effect, a powerful LLM has already absorbed some, if not all, of
the confounding signals during generation. Recent GenAI-Powered Inference (GPI) builds on this idea,
recovering confounding information from LLM representations that encode semantic knowledge
beyond observed variables (Imai & Nakamura 2025).
We adopt this logic but adapt it to a different causal structure: labels, generated content, and
engagement are observed, while the external semantic factors implicitly reflected in the LLM's
generation process are not. We therefore learn a latent representation from this process and exploit the
multi-treatment label structure to separate shared confounding from the marginal and combinatorial
value of individual labels. This contrasts with the Deconfounder framework of Wang and Blei (2019),
which infers sha red latent confounders primarily from treatment co -occurrence patterns; our setting
demands recovering confounding signals embedded in both combinatorial label assignment and LLM-
mediated semantic transformation.
2.3 Causal Representation Learning
Causal representation learning embeds causal structure into latent variables to enable intervention
and “what-if” reasoning. In LLM applications, prior work has integrated Structural Causal Models
(SCM) with generative models for counterfactual generation, including SCM-V AE (Komanduri et al.,
2022) and DEAR (Shen et al., 2022), while diffusion-based approaches such as DiffPO (Ma et al., 2024)
model potential outcome distributions to estimate treatment effects. Among these, C-V AE (Yang et al.,
2021) is especially influential  and relevant : unlike standard V AEs that encourage statistical
independence among latent factors (Kingma & Welling, 2013), it imposes causal dependencies through
a weakly supervised conditional prior 𝑃(𝑍 ∣ 𝐿) and a learnable SCM layer that induces a DAG over

 10

latent dimensions. This design supports interventions that propagate through a structured latent space,
making it attractive for workflows where labels encode strategic intents.
However, C-V AE is not sufficient for our problem for three reasons. First, C-V AE incorporates
related signals ( 𝐿) mainly as auxiliary supervision for latent factor learning. While we also employ
labels 𝐿 to guide representation learning, engagement 𝑌 serves as the ultimate causal target whose
response to interventions on 𝐿 must be explicitly predicted. Second, it does not address confounders
that jointly affect label selection and engagement. Third, it does not explicitly model the stochastic
mediation through 𝑋, where identical labels can yield variant copies that complicate identification of
label effects.
In sum, the literature reveals a divide: deconfounder methods account for confounds but often lack
strong counterfactual prediction in complex generative pipelines, while causal representation learning
enables intervention in latent space but does not guarantee adequate adjustment for confounders. Our
problem requires both: (1) recovering confounders from partially observed data, and (2) modeling the
causal mechanism from labels to engagement to support counterfactual prediction without relying on
actual copy generation. This motivates combining deconfounding with causal representation learning.
3.  Research Context and Theoretical Background
This section discusses the research context on LLM-enabled ad generation and provides theoretical
backgrounds for estimating the causal effect of labeling skills on user engagement.
3.1 Research Context: Marketing Label Attribution
We frame our research context as a marketing attribution problem: how do marketer -selected labels
causally influence user engagement in an LLM-assisted creative pipeline? Consider a campaign where
marketers specify a binary label vector 𝐿 ∈ {0,1}𝐾 that encodes the strategic attributes, such as “long-
wear” + “skin-nourishing” versus “natural finish” + “oily/acne-prone friendly” characterizing the brand,
product, and target persona  for some cosmetics product . Each element 𝐿𝑗 = 1  indicates that label
𝑗 (e.g., “oil control”) is selected, and 0 otherwise. Given 𝐿, an LLM generates marketing copy 𝑋 ∈ 𝒳,
but this mapping is inherently stochastic: even with the same labels, decoding variability can yield
different wording, tone, and narrative framing. Moreover, the generated copy often includes elements

 11

not explicitly specified in 𝐿 , such as usage scenarios, temporal framing, or persona cues  that can
materially affect how audiences respond , added by LLM to improve user engagement. Such
improvements reflect the ability of LLM rather than the skills of the marketers, and if not isolated out,
can confound the value attribution of labels. User engagement 𝑌 ∈ ℝ𝑁(e.g., likes, comments, collects)
is then realized as the audience reaction to the full creative 𝑋, rather than to the label choices 𝐿 alone.
This setting implies a mediated pathway, 𝐿 → 𝑋 → 𝑌: labels shape engagement indirectly by steering
the generated content, but they do not directly determine it. This creates a core identification challenge
for marketing: the same label configuration can produce distinct copies with different engagement
outcomes, making it difficult to causally attribute engagement differences to labels rather than to
stochastic or incidental variations in generated text. Example 1 illustrates this workflow.
We model this workflow using a SCM 𝑀 = ⟨{𝐿, 𝑋, 𝑌}, {𝑓𝑋, 𝑓𝑌}, 𝑃(𝑢)⟩, where 𝑋: = 𝑓𝑋(𝐿, 𝜀𝑋), 𝑌: =
𝑓𝑌(𝑋, 𝜀𝑌). Here 𝜀𝑋 represents unobserved factors in the generation process (e.g., decoding randomness
and latent narrative choices) and 𝜀𝑌  captures unobserved drivers of audience response. Figure 2(a)
visualizes this causal structure.
In defining the causal estimand, we focus on the first -stage content -response effect of label
configurations. This scope reflects the operational structure of common large-scale AI-assisted content
production. In our setting, advertisers produce hundreds o f ad copies per day; at this scale, channels,
budgets, and KOL (Key Opinion Leader) selections are not redesigned separately for each label
configuration. Instead, distribution resources (budgets, channel and KOL choices) are managed and
adjusted at much c oarser monthly or quarterly level. Firms typically re -allocate budget or choose a
Example 1:  Label -Driven Narrative Divergence in LLM-Generated Marketing Copy
A marketer uses label vector 𝐿  to guide the generation of copy 𝑋 . We compare two label configurations
differing only in highlighted product benefits:

𝓵𝟏: long-wear + skin-nourishing
Generated copy: This office-to-gallery makeup foundation is a winner! As a CBD office worker, I wore it
12 straight hours—coffee runs, pitches, gallery selfies—and my skin stayed flawless. An intern even asked
if it was my natural skin!
𝓵𝟐: natural finish + oily/acne-prone friendly (same ingredients).
Generated copy: Strangers asked for my foundation link on the high -speed train! 17 hours of wear —
baggage chaos, client meetings, clubbing—zero patchiness, even under a mask!

Though both makeup foundation copies recommend the same product, they carry distinct ive contextual details:
𝑿𝓵𝟏 centers on a CBD office lifestyle, 12-hour wear, and a junior colleague’s compliment;
𝑿𝓵𝟐 focuses on a frequent business traveler persona, 17-hour wear, and a stranger’s link request.

 12

different distribution channel only when certain label combinations stand the test of time. Our causal
attribution method provides the foundation to the firm for determining the value of labels. Under this
setup, which reflects the practical decision sequence in AI-enabled marketing, value attribution informs
later resource allocation, not the other way around.
This implies that, when we estimate how engagement would change if the label configuration were
altered for a given creative context, it suffices to hold constant the deployment environment observed
in the data. We do not need to anticipate how the choice of a different label would change the resource
reallocation in an endogenous manner in our setting.
3.2 Why label effects are hard to identify: ITE, Mediation, and Confounding
In practice, marketing decisions operate at both overall portfolio and individual campaign levels1,
each requiring distinct causal estimands. Standard estimands such as the average treatment effect (ATE)
effectively summarize population-level engagement shifts and remain highly valuable for identifying
mean effects to  guide broad resource allocation  at the portfolio level  in our setting . However, for
personalized creative optimization, the central question shifts from “what works on average?” to “how
would engagement change if we altered the label configuration for this specific ad  campaign?” This
requires an individual-level counterfactual query formalized as the Individual Treatment Effect (ITE).
ITE isolates the context-specific causal pathway by accounting for stochastic LLM mediation, tracing
how a particular label shift alters the generated narrative and subsequently drives engagement for a
given audience.
To illustrate this distinction, consider a creative 𝑋ℓ1 targeting the CBD-office-worker, generated
under label ℓ1 in Example 1. The operational question is a within -campaign counterfactual: had the
label used ℓ2 instead, what would engagement have become for this exact product, brand, and visual
context? The ITE directly addresses this by evaluating how the label intervention reshapes the copy
narrative for that specific campaign. By comparison, an ATE estimate averages across a portfolio of
campaigns with different audiences and market conditions. The same label shift may amplify

1
 A campaign refers to a targeted advertising initiative, while a portfolio means a collection of campaigns. For
example, swapping a label from "speed" to "comfort" to target a different group of customers in a single ad
represents a specific campaign, while  prioritizing "sustainability" vs. "performance" themes across all Q4 ads
consists of a portfolio of campaigns.

 13

engagement for students while diminishing it for urban professionals. While ATE provides essential
macro-level insights for strategy formulation, it inherently masks the heterogeneous mediation
mechanisms that marketers must navigate when tailoring individual creatives.
Consequently, in our setting where decisions hinge on precise audience-context alignment, the key
estimand is an individual-level mediated effect: the change in engagement induced by changing labels
through the change in generated copy. Under our SCM 𝐿 → 𝑋 → 𝑌, labels influence engagement only
via the LLM -generated copy. Accordingly, for two-label configurations ℓ0, ℓ1 ∈ {0,1}𝐾 , the natural
direct effect (NDE) is structurally zero:
NDEℓ0,ℓ1(y) = P (Yℓ1,Xℓ0 = y) − P (Yℓ0,Xℓ0 = y) = 0 (1)
because there is no direct arrow 𝐿 → 𝑌 (because advertisers do not display the labels directly to users,
users see ad copies instead). The natural indirect effect (NIE) captures the change in engagement driven
by the label-induced change in copy:
NIEℓ0,ℓ1(𝑦) = P (𝑌ℓ0,Xℓ1 = 𝑦) − P(𝑌ℓ0,𝑋ℓ0 = 𝑦). (2)
 Then the ITE of intervention (ℓ0 → ℓ1) is
ITEℓ0,ℓ1(𝑦)  =  NDEℓ0,ℓ1(𝑦) + NIEℓ0,ℓ1(𝑦) = NIEℓ0,ℓ1(𝑦). (3)
Intuitively, NIE asks how engagement would change if we kept the “downstream engagement response
mechanism” fixed at label setting ℓ0, but replaced the realized copy Xℓ0, with the counterfactual copy
𝑋ℓ1  that would have been generated under an alternative label configuration.  The difficulty is that
NIEℓ0,ℓ1(𝑦) is generally not identifiable under either Pearl’s observational (Layer 1) or interventional
(Layer 2) scenarios, when the mediation pathway is affected by unobserved factors  (See Figure 1 in
Appendix D). Even with randomized assignment of 𝐿 , identifying NIE  requires, for the  same
unit/campaign, access to both the factual outcome under (ℓ0, Xℓ0)  and the counterfactual outcome
under (ℓ0, Xℓ1). This directly reflects the Fundamental Problem of Causal Inference (Holland, 1986):
a single campaign cannot simultaneously realize two different copies generated under different label
configurations. In generative marketing, this problem is amplified be cause 𝑋 is not a deterministic
function of 𝐿: stochastic decoding and emergent narrative choices inject variability (e.g., lifestyle cues,

 14

temporal framing) that are difficult to fully observe or control, and that may correlate with both label
selection and engagement.
As a side note , non -identifiability does not imply non -realizability (Raghavan & Bareinboim,
2025). Identifiability asks whether the counterfactual quantity is computable from observed
interventional distributions; realizability asks whether we can design a procedure that can approximate
or sample from the relevant counterfactual distribution. In our context, while we cannot observe both
𝑌ℓ0,Xℓ1  and 𝑌ℓ0,Xℓ0  for the same campaign from historical logs, we may still be able to make
counterfactual reasoning operational by constructing proxy interventions that emulate the label-induced
narrative shift in a controlled space.
This motivates the following  latent-space intervention framework. Rather than requiring the
platform to (unrealistically) regenerate a copy under alternative labels and re -run the campaign, we
learn a causal representation in which the label -induced narrative components can be perturbed in a
structured way. Doing so makes the counterfactual query  “What would engagement have been under
an alternative label configuration?” to be operational (realizable) without relying on repeated trial-and-
error deployments or on directly observing impossible counterfactual outcomes.
3.3 Latent Space Perspective: Construction and Rationale
Although counterfactual reasoning is theoretically realizable, neither the discrete label space nor
the stochastic ad copy space supports valid, unconfounded interventions. Directly editing the realized
copy 𝑋  violates ceteris paribus by altering uncontrolled stylistic or narrative features. Conversely,
swapping factual labels and regenerating copy injects uncontrolled decoding variation, breaking the
isolation of the 𝐿 → 𝑌 pathway. To enable valid proxy interventions, we construct a causally structured
latent representation 𝑍𝐿  that separates label -driven variation from stochastic mediation and
environmental noise.
The latent space 𝑍𝐿 is not postulated abstractly; rather, it is learned directly from the generative
pipeline through a joint optimization objective. Specifically, we extract 𝑍𝐿  from the LLM’s high -
dimensional hidden-state representation 𝑅 = ℎ𝜙(𝑋) of the generated marketing copy 𝑋 (Figure 2(b)).
Following the Interchange Intervention approach (Li et al. 2026) and the Distributed Alignment Search

 15

method (DAS; Geiger et al.,2024), we treat the expert label vector 𝐿 as a high-level causal variable and
learn 𝑍𝐿 as its distributed realization within the model’s hidden -state space, rather than as a localized
neuron, coordinate, or surface -level textual feature. This extraction is guided by two simultaneous
objectives:
1. Label supervision: 𝑍𝐿 is constrained to align with the observed expert label vector 𝐿, ensuring
it captures strategic intent rather than arbitrary stylistic fluctuations;
2. Outcome supervision: 𝑍𝐿 is optimized to predict downstream user engagement 𝑌, anchoring
the representation in actual market resonance.
Formally, we reparametrized the generative process through 𝑍𝐿 = ℎ𝜃(𝑅) with a loss function
ℒ(𝜃) = ℒ𝑙𝑎𝑏𝑒𝑙(𝑍𝐿, 𝐿) + λℒ𝑜𝑢𝑡𝑐𝑜𝑚𝑒(𝑍𝐿, 𝑌), yielding the structural equations:
𝑋 = 𝑓(𝑍𝐿, 𝜀𝑋), 𝑌 = 𝑔(𝑍𝐿, 𝜀𝑌),  s.t. 𝐿 − 𝐿′ = 0  ⟹ 𝑍𝐿 = 𝑍𝐿 ′ ⟹ E[Y∣𝑍𝐿] =E[Y'∣𝑍𝐿 ′ ]. (4)
How  𝑍𝐿  addresses mediator-induced bias? The effectiveness of this design rests on two
complementary insights. First, leveraging the LLM’s internal representations provides a rich semantic
proxy for latent contextual factors  (Imai &Nakamura, 2025). LLMs trained on vast, diverse corpora
encode, in their hidden states, not only explicit semantics but also narrative conventions, emotional
tones, and stylistic priors. These internal states naturally absorb many of the contextual signals that co-
vary with treatment generation and audience response. Second, the joint optimi zation with label
supervision and outcome alignment purposefully filters out such stochastic decoding noise. Identical
label sets can yield semantically aligned but lexically divergent copies due to LLM-induced randomness.
The latent space compresses this variation into a stable, continuous representation that preserves the
causal core of marketer intent (underlying skills of deliberately choosing certain labels) while
discarding incidental narrative artifacts. Consequently, intervening on 𝑍𝐿  bypasses the noisy 𝐿 →
𝑋 generation step for counterfactual prediction, isolating the true causal signal of label semantics from
mediator-induced stochasticity.
Under this construction, 𝑍𝐿 satisfies two formal requirements for valid counterfactual reasoning:
(1) Intervention Fidelity (Label-to-Latent Equivalence): 𝑍𝐿  preserves the causal role of the labels
in the generation mechanism. Intervening on 𝑍𝐿 should reproduce the downstream effect of

 16

intervening on 𝐿 : 𝔼[𝑌 ∣ 𝑑𝑜(𝑍𝐿 = 𝑧)] ≈ 𝔼[𝑌 ∣ 𝑑𝑜(𝐿 = ℓ)] . Conceptually, this metric is
analogous to the Interchange Intervention Accuracy (IIA) metric proposed in Li et al. (2026 )
and Geiger et al. (2024) where intervening on a subset of input space is interchangeable to
intervening on the whole space.
(2) Disentanglement from Stochastic Mediation: 𝑍𝐿 isolate the stable, label-driven semantic signal
from the stochastic decoding noise and emergent narrative artifacts in 𝑋. By compressing the
𝐿 → 𝑋  pathway into a continuous representation, 𝑍𝐿  makes counterfactual prediction
realizable without requiring actual copy regeneration.
However, satisfying these two requirements ensures only that our intervention is coherent and stable;
it does not guarantee that the resulting estimates are unbiased  in a causal sense . As detailed next, the
system remains vulnerable to external confounders—such as campaign budget, platform algorithms, or
cross-modal visual factors—that jointly influence both label selection and user engagement. Therefore,
achieving robust Causal Inference of Engagement requires addressing these remaining sources of bias,
which motivates the deconfounding framework discussed next.
3.4 Sources and Complexity of Confounding
Even with a well-constructed latent label space 𝑍𝐿, the causal system of our research context, as
specified in Figure 3, can remain confounded. Such confounding impedes both (i) identification of the
causal effect of labels on engagement and (ii) learning causal relations within the latent label structure
(𝑒. 𝑔. , 𝑍𝐿𝑖 → 𝑍𝐿𝑗).
The confounders can arise from two sources. The first is copy-induced confounders (embedded in
𝑋). The generated copy 𝑋 contains stylistic and narrative artifacts 𝑋𝐿̃ that are not explicitly encoded
in the label vector 𝐿 but are systematically co-produced with it. Examples include context choice (e.g.,
“CBD office worker” vs. “frequent traveler” in Example 1), emotional tone, temporal framing, and
incidental character interactions. These features are not randomized or controlled during generation,
and they can influence engagement directly. As a result, they create spurious associations between
𝐿 and 𝑌, and can also induce apparent dependencies across label dimensions. For instance, the frequent
co-occurrence of “618” and “gift-for-self” may reflect campaign conventions rather than a true causal

 17

link between the underlying label semantics. While such artifacts can be partially summarized via LLM
embeddings (𝑋𝐿), they remain a source of confounding unless explicitly accounted for.
The second source comes from unobserved environment  (𝐸𝑢). Beyond what is expressed in the
copy, there may exist confounders jointly affect label choice and engagement. We group these into:
• Marketer-level factors: tacit expertise, preferences, and risk attitudes that shape how labels are
interpreted and translated into narrative form.
• Market-level dynamics: competition intensity, campaign budget, trending topics, and seasonal
demand shifts that influence both label selection and consumer response.
• Platform-level factors: algorithm configurations, audience segmentation logic, and cross -
campaign interference that affect exposure and engagement but are typically unobserved in logs.

Figure 3: Proposed Causal Structure
Note: X (marketing copy) and E (environmental variables containing observed C and unobserved
𝐸𝑢 ) are the confounders of 𝑍𝐿𝑖 →𝑍𝐿𝑗  and 𝑍𝐿 →Y, where 𝑍𝐿𝑖  (latent causal label variables),
𝑍𝐿𝑗(latent result label variables), Y is the user engagement.

Some observed environmental variables can serve as proxies for parts of the latent environment,
denoted 𝐶 (controls). Examples include publish time, text–image coherence metrics, influencer (KOL)
attributes (e.g., followers, historical like/collect rates), and brand popularity. Conditioning on (𝑋𝐿, 𝐶)
can reduce bias. However, it does not eliminate unobserved selection, meaning the conditional
independence required for causal identification in the latent space generally fails:
𝑌𝑍 ⊥ 𝑍𝐿 ∣  𝑋𝐿, C (5)
This remaining dependence motivates our use of deconfounder methods in the multiple-cause
setting, together with an explicit discussion of omitted-variable bias bounds, since one cannot
enumerate and measure all unobserved confounders in generative marketing environments.

 18

4. Method: D-V AE
In this section, we propose D-V AE (Deconfounder V ariational Autoencoder), a unified framework that
addresses the identification challenges discussed in Section 3 for causal skill attribution, whose effects
are mediated by LLM . D-V AE jointly models three interwoven structures. First, it characterizes the
confounding structure of multi-label assignment, distinguishing shared confounders affecting multiple
labels from single-label confounders that cannot be recovered from co-occurrence alone. Second, it uses
the recovered confounder information to construct a confounder-adjusted latent representation of expert
labeling logic. Third, it embeds this representation in a way that interventions on one label can propagate
through learned dependencies among labels.
4.1 Structure of Treatment Confounder: Multi- vs. Single-Treatment Confounder
Our approach draws on a key insight from Wang & Blei (2019): when treatments are high-dimensional
and combinatorial, their joint patterns reveal information about shared latent confounders that
simultaneously influence multiple labels. Intuitively, if certain label combinations (e.g., “co-branded IP”
+ “beauty enthusiast”) repeatedly co -occur across campaigns, this regularity likely stems from a
common hidden driver—such as campaign budget or market niche. By modeling these co-occurrence
patterns, we can construct a proxy for that shared confounder and account for it.
However, real-world labeling involves a more complex confounding structure: not all confounders
affect multiple labels. Some  may influence only one label while also boosting engagement , e.g., the
temporary popularity of a specific cartoon IP . These single -cause confounders leave no trace in the
covariance structure across labels and are therefore unrecoverable by any extant deconfounder methods.
Wang & Blei’s framework simply assumes such confounders are absent; while our work explicitly
factors in their presence.
Our contribution is to prove the theoretical bounds of the impact of single-cause confounders and
establish the conditions as to when they are ignorable, relative to the shared confounders. Crucially, we
extend Oster’s (2019) linear sensitivity logic by constructing a worst -case scenario over a W -2
ambiguity ball following Wasserstein DRO (distributionally robust optimization) approaches (Esfahani
& Kuhn 2018). This diagnostic extends naturally to nonlinear models, including neural networks, under

 19

Lipschitz-type regularity.
Formally, when dealing with multiple binary treatment L = (𝐿1, … , 𝐿𝐾)⊤ ∈ {0,1}𝐾, unobserved
confounders 𝐸𝑢  may appear in two distinct channels: (1) common confounder 𝑒𝑚 ∈ 𝑅𝑀 , which
simultaneously influences the selection of multiple ( ≥ 2 ) treatment labels; (2) single -treatment
confounders {𝑒𝑠 (𝑗)}𝑗=1 𝐾  , where each 𝑒𝑠 (𝑗) ∈ 𝑅  affects only the 𝑗 -th treatment 𝐿𝑗 . This structure is
illustrated in Figure 4(a).

Figure 4: The Confounders Problem of Causal Inference on Label to User Engagement
Importantly, while we denote a distinct 𝑒𝑠 (𝑗) for each 𝐿𝑗 for notational clarity, this does not imply
that every treatment necessarily has its own unique unobserved driver, some may share components or
be unaffected. In practical multi -label selection settings, common confounders are  likely to be  more
prevalent. This is because label assignment typically occurs in a joint decision process, campaign
managers rarely select each label in complete isolation. Consider a marketing campaign , a platform-
wide trending topic (e.g., a beauty festival) or campaign budget may act as a common confounder 𝑒𝑚,
simultaneously increasing the likelihood of selecting multiple labels such as “co-branded IP”, “beauty
enthusiasts”, “cost-effective”, and “tech -infused”. And the popularity of a certain IP may serve as a
single-treatment confounder 𝑒𝑠 (1) that boosts user engagement through the appeal of the IP, while also
affecting the adoption of the co -branded IP label. Similarly, a shopping festival  𝑒𝑠 (3)  may elevate
preference for the “cost -effective” label and independently heighten user responsiveness to discount -
related content.

 20

4.2 Deconfounder under multiple treatments
To operationalize this separation, we impose a factorized latent -confounder model that
distinguishes shared cross -label dependency from label-specific residual confounding. The standard
Gaussian priors is leveraged to fix the scale of otherwise unobserved latent factors and provide a
regularized parameterization. Our deconfounder approach assumes the following generative structure:
𝑒𝑚 ∼ 𝑁(0, 𝐼𝑀), 𝑒𝑠 (𝑗) ∼ 𝑁(0,1), ∀𝑗 = 1, … , K, (6)
with mutual independence:
𝑒𝑚 ⊥ 𝑒𝑠 (𝑗), 𝑒𝑠 (𝑗) ⊥ 𝑒𝑠 (𝑘) for j ≠ 𝑘.
The treatment assignment follows a factorized model conditional on the latent confounders:
𝐿𝑗 ∣ 𝑒𝑚, 𝑒𝑠 (𝑗) ∼ 𝐵ernoulli (σ (λ𝑗 ⊤𝑒𝑚 + θ𝑗𝑒𝑠 (𝑗))) , 𝑗 = 1, … , K, (7)
or equivalently,  P( 𝐿1, … , 𝐿𝐾 ∣∣ 𝑒𝑚, 𝑒𝑠 ) = ∏ 𝑃 ( 𝐿𝑗 ∣∣ 𝑒𝑚, 𝑒𝑠 (𝑗) )𝐾 𝑗=1 , where es  =
  (es (1),   … ,  es (K)) ⊤ ,  λj  ∈ RM, and θ𝑗 ∈ 𝑅.
Building on the factorized treatment-assignment model above, we specify the following outcome
equation:
𝑌 = 𝛽⊤𝐿 + Γ𝑒𝑚 + Θ⊤𝑒𝑠 + 𝑋𝐿̃⊤ 𝛼 + 𝜌⊤𝐶 + 𝜖 (8)
where 𝑒𝑚  and 𝑒𝑠  capture pre -treatment confounding in label assignment: 𝑒𝑚  absorbs common
sources that induce cross -label dependenc y, while 𝑒𝑠  captures treatment -specific assignment
heterogeneity. In contrast, 𝑋̃𝐿 plays a different role. Let
𝑋𝐿 = 𝜙LLM(𝑋), 𝑋̃𝐿 = 𝑋𝐿 − 𝔼[ 𝑋𝐿 ∣∣ 𝐿 ], (9)
where 𝑋𝐿 ∈ ℝ𝑇denotes the LLM representation of the generated copy. The residual 𝑋̃𝐿 is the 𝐿-
orthogonal component of the representation, isolating post-assignment variation that is not explained
by the label vector 𝐿 but may still affect 𝑌. Thus, while 𝑒𝑚 and 𝑒𝑠 deconfound the assignment of
labels, 𝑋̃𝐿 partials out mediator-side nuisance variation in the generated copy. 𝐶 ∈ ℝ𝑄denotes

 21

observed covariates (controls), ϵ denotes the noise term ϵ ∼ 𝒩(0, τ2). Then given 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶, the
ignorability condition holds:
𝑌(𝑙) ⊥ 𝐿| 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 (10)
Under this condition, the estimator of 𝛽̂ in the regression model would yield an unbiased estimate
of the true causal effect 𝛽. Specifically, the projection of the unobserved confounders onto the treatment
space is eliminated, ensuring that 𝔼[𝛽̂] = 𝛽. As specified in Figure 3 , we decompose the confounder
source as environmental factors 𝐸 = (𝐶, 𝐸𝑢).  The unobserved environmental component 𝐸𝑢  is
represented by the latent factors (𝑒𝑚, 𝑒𝑠), while the observed environmental component is captured by
𝐶, and the copy-level confounder is controlled by conditioning on the LLM -derived representation of
the generated copy 𝑋𝐿in the outcome model, which yields the following deconfounding property:
Theorem 1 (Conditional Deconfounding of 𝑍𝐿): Suppose that 𝑒𝑚, 𝑒𝑠, 𝐶, and 𝑋𝐿 sufficiently
capture the unobserved environmental, observed environmental, and copy-level confounders,
respectively. Then, under the specified DGP (8),
𝑌(𝑧) ⊥ 𝑍𝐿 ∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿, 𝐶 (11)
Consequently, after adjustment for (𝑒𝑚, 𝑒𝑠, 𝑋𝐿, 𝐶) the estimator 𝛽̂ obtained through 𝑍𝐿 is unbiased
for 𝛽, the true causal effect of 𝐿 on 𝑌: 𝔼[𝛽̂] = 𝛽.
4.3 Bound of the Single Treatment Confounders
However, single-treatment confounders {𝑒𝑠 (𝑗)}  are unidentifiable from the observed treatment
matrix alone. While we may observe some covariates 𝐶 ∈ 𝑅𝑄  that partially proxy for these latent
factors, they are unlikely to fully capture all sources of single-cause idiosyncratic variations. This raises
a critical question: if we estimate the common confounder 𝑒𝑚  while omitting the single -treatment
confounders 𝑒𝑠 but partially controlled by 𝐶, when can the resulting omitted variable bias be ignorable?
 This question reveals a key limitation acknowledged in Wang & Blei (2019): their deconfounder
assumes all unobserved confounding is shared across treatments, rendering it oblivious to single-cause
confounders that are common in real -world marketing. Because such confounders generate no cross -
label correlation, they cannot be recovered by factor models, yet they can still bias causal estimates. To

 22

answer this, we establish a theoretical Probably Approximately Correct (PAC) bound on the omitted
bias (Theorem 2) to assess whether  𝑒𝑚 dominates 𝑒𝑠 . When 𝑒𝑠 is omitted, given 𝑛 samples, we
get the estimator 𝛽̂ under the following model:
𝑌𝑖 = 𝐿𝑖 ⊤𝛽̂ + 𝑒̂𝑚,𝑖 ⊤ Γ̂ + 𝑋̃𝐿𝑖 𝑇 𝛼̂ + 𝐶𝑖 ⊤𝜌̂ + 𝜖̂𝑖 (12)
where e𝑚̂  estimated via Logit-Probabilistic PCA (Logit-PPCA) of 𝐿. The bias from e𝑠 is scaled by
the fraction of outcome variance unexplained after conditioning on e𝑚. If e𝑚 dominates the label
selection process, the residual variance attributable to e𝑠 is small, naturally capping the worst-case
bias. This yields our main theoretical result:
Theorem 2 (Bound under Single-Treatment Confounding): Under the above DGP (eq. 12), with
𝑒𝑚̂ estimated via Logit-PPCA, and assuming (i) 𝑒𝑚 dominates 𝑒𝑠 in explaining label co-variation,
and (ii) 𝜆𝑚𝑖𝑛(𝐸[𝑉𝑎𝑟( 𝐿 ∣∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ≥ 𝜆 > 0, then for any 𝜂 ∈ (0,1), there exists a constant 𝐴0
(depending only on model primitives) such that:
𝑃 (∥ 𝛽̂ − 𝛽 ∥2≤ 𝐴0(1 + √𝑀/𝑛 + 𝑀/𝐾)) ≥ 1 − 𝜂. (13)
The key insight is that the omitted bias from 𝑒𝑠 is bounded in population, while the estimation error
in 𝑒𝑠̂  decays at rate √𝑀/𝑛 + 𝑀/𝐾. Together, these ensure that the estimation bias interval remains
narrow even when single-treatment confounders are unobserved.
We then extend this guarantee to more generic nonlinear outcome settings, such as neural
networks, provided the structural function belongs to a Lipschitz-continuous class with bounded
weights and activations: 𝑌 = 𝑓(𝐿, 𝑒𝑚, 𝑋𝐿̃, 𝐶; 𝛽) + 𝜖 and the estimator is the M-estimator (empirical
risk minimizer)
𝛽̂ = arg min 1 𝑛
𝛽∈𝛣
∑ ℓ(
𝑛
𝑖=1
𝑌𝑖, 𝑓(𝐿𝑖, 𝑒̂𝑚,𝑖, 𝑋̃𝐿𝑖, 𝐶𝑖; 𝛽)), (14)
where ℓ is a convex loss. The same PAC bound holds with an identical convergence rate. This result
hinges on the multi-label structure, because labels are selected jointly and exhibit rich combinatorial
variation, their observed correlation matrix reveals the dominant source of confounding. The full

 23

proof is provided in Online Appendix A.
In practice, real data may violate this dominance assumption. We therefore develop an empirical
sensitivity diagnostic test to assess its robustness based on observable-control shifts. By tracking how
the estimated effect changes as observed confounders are progressively adjusted in the bias
decomposition plim 𝛽̂ = 𝛽 + 𝐵𝑒̂𝑚 + 𝐵𝑒𝑠, the diagnostic quantifies how large the remaining
unobserved bias would need to be to materially change the estimate, without imposing subjective
sensitivity parameters. Let 𝑃0 denote a reference distribution embodying the equal selection
benchmark δ = 1, where the relative selection strength of 𝑒𝑠 matches that of the estimated shared
proxy 𝑒̂𝑚. We consider all plausible confounding distributions within a Wasserstein-2 ball of radius
ε ≥ 0 around 𝑃0: 𝒫𝜀 = {𝑃: 𝑊2(𝑃, 𝑃0) ≤ 𝜀}, 𝜀 = |𝛿𝑜𝑏𝑠 − 1|. This nonparametric construction bounds
how far the true distribution of unobservables can deviate from the dominance condition without
imposing restrictive parametric forms on 𝑒𝑠. The Wasserstein-2 distance is particularly well-suited for
nonlinear outcome models. By the Kantorovich–Rubinstein duality, 𝑊2  controls the expectation of
any 1-Lipschitz function of the confounders. Combined with the Lipschitz continuity of the structural
function 𝑓(with constant 𝐿𝑓 < ∞, as assumed in Section 4), any bias or marginal effect under 𝑃 ∈
𝒫𝜀 deviates from that under 𝑃0 by at most 𝑂(𝐿𝑓 ⋅ 𝜀).
 We compare two models: (1) Uncontrolled Regression: 𝑌𝑖 = 𝐿𝑖 ⊤𝛽 + +𝑋̃𝐿𝑖 𝑇 α + 𝐶𝑖 ⊤𝜌 + ϵ𝑖,
with estimator 𝛽uncontrolled ,    𝑅2 = 𝑅uncontrolled   (or pseudo - 𝑅2  based on the empirical loss) ; (2)
Controlled Regression: 𝑌𝑖 = 𝐿𝑖 ⊤𝛽 + 𝑒̂𝑚,𝑖 ⊤ Γ + 𝑋̃𝐿𝑖 𝑇 α + 𝐶𝑖 ⊤𝜌 + ϵ𝑖, with estimator β ̃, 𝑅2 = 𝑅̃.
Then invert Oster’s formula (adapted to the multi-treatment and M-estimator setting) to obtain the
observed selection ratio:
𝛿̂obs = 𝑅̃ − 𝑅uncontrolled 𝑅max − 𝑅uncontrolled (15)

 24

A small 𝜀 indicates that 𝑒̂𝑚 has already absorbed the dominant fraction of confounding variation,
leaving minimal explanatory power for 𝑒𝑠 to exploit.
For any 𝑃 ∈ 𝒫𝜀, the bias-adjusted causal effect (extended to M-estimators via Lipschitz-bounded
gradients) takes the closed form:
𝛽adj(𝑃) = 𝛽̃ + 𝛿(𝑃) 𝛽̃ − 𝛽uncontrolled 𝑅̃ − 𝑅uncontrolled (𝑅max − 𝑅̃) (16)
where 𝛿(𝑃) = Cov(𝐿, 𝑒𝑠 ∣ 𝑃)/Cov(𝐿, 𝑒̂𝑚) is the effective selection ratio under 𝑃. The worst-case
identified set for the causal parameter is therefore:
[𝛽𝐿, 𝛽𝑈] = [inf 𝑃∈𝒫𝜀𝛽adj(𝑃),  sup𝑃∈𝒫𝜀 𝛽adj(𝑃)]. (17)
Under the maintained identification condition, the width of [𝛽𝐿, 𝛽𝑈] grows linearly with
𝜀 (i. e. , 𝑂(𝐿𝑓 ⋅ 𝜀) but remains strictly bounded by 𝑂(√𝑀/𝑛 + 𝑀/𝐾 + 𝐿𝑓 ⋅ 𝜀).
We validate the PAC bound by comparing the empirical identified set with the theoretical PAC
radius 𝑟PAC = 𝐶(1 + √𝑀/𝑛 + 𝑀/𝐾) from Theorem 2. The bound is deemed robust and informative
if: 𝛽𝑈 − 𝛽𝐿 ≤ 2𝑟PAC, and [𝛽𝐿, 𝛽𝑈] overlaps with the PAC interval centered at 𝛽̃.
In our empirical setting  (Appendix C Algorithm 1 ), we find that after controlling for both
observed confounders 𝐶 and the estimated common factor 𝑒𝑚̂, the relative ratio 0.07% is rather small,
and the resulting bias -adjusted region for β: [β̂ − bias, β̂], does not contain the zero vector, and the
bound is robust across reasonable choices of δ. This provides strong evidence that our deconfounder
strategy effectively mitigates the dominant source of omitted -variable bias in multi -label treatment
settings. Formally, we provide the following corollary.
Corollary (Proxy-Controlled Unconfoundedness ): Given the observed marketing copy  X  (the
corresponding LLM representation 𝑋𝐿 ), environmental variables C  and estimated common
confounder 𝐸𝑚̂ , the potential outcome 𝑌𝑧 and label space 𝑍𝐿 are approximately satisfying
𝑌𝑧 ⊥ 𝑍𝐿 ∣ 𝑋𝐿, C, 𝐸𝑚̂  (18)
4.4 Counterfactual Prediction via Causal V AE
After deconfounding, we then make counterfactual inference through intervening latent space 𝑍𝐿.
We aim not to reconstruct or edit content, but to infer how changes in label would alter user engagement.

 25

This differs fundamentally from C-V AE, which embeds a learnable SCM into the latent space to support
do-interventions on weakly supervised label factors for which  the outcome of interest is the
reconstructed sample itself (Yang et al., 2021). Further, C-V AE lacks two essential components for our
task: (1) it assumes all relevant confounders are either observed or ignorable, an unrealist assumption
that we directly address through deconfounder  and (2) it uses a single -path latent representation that
forces causal factors to also encode environmental noise from 𝑋 and 𝐸, thereby contaminating the
causal signal with spurious correlations. Without explicit modeling these confounders or  having a
mechanism to isolate the engagement-predictive component of label semantics, C-V AE’s interventions
may reflect spurious correlation rather than true causal effects.

Figure 5: Architecture of the D-V AE
Note: Inputs 𝑋 (marketing copy), 𝐿 ∈ {0,1}𝐾 (label vector), 𝐶 (observed covariates), and
𝐸̂𝑚  (estimated common confounder) are jointly encoded into a structured latent space 𝑍𝑒 =
[𝑍𝑒,𝐿, 𝑍extra]. The causal subspace 𝑍𝑒,𝐿 ∈ ℝ𝐾 is refined by a SCM layer (adjacency matrix 𝐴) to yield
the intervention -ready representation 𝑍𝐿 . The auxiliary subspace 𝑍extra   captures residual variation
from 𝑋, C, and 𝐸̂𝑚. The full latent state 𝑍𝑑 = [𝑍𝐿, 𝑍extra] is decoded to reconstruct 𝑋̂ and predict user
engagement 𝑌̂.

In contrast, our D-V AE addresses both gaps by integrating an estimated shared confounder (Section
4.1) and a dual -path latent architecture that decouples causal label semantics ( 𝑍𝐿 ) from auxiliary
variation ( 𝑍𝑒𝑥𝑡𝑟𝑎 ). This enables a principled multi -task formulation where 𝑍𝐿  parallelly supports
marketing copy reconstruction and engagement prediction. Grounded in behavior -aware V AE
frameworks (Rao et al., 2023), sharing 𝑍𝐿 across tasks captures robust global semantics, while task -
specific decoding prevents overfitting. Specifically, reconstruction acts as a semantic regularizer to
preserve textual fidelity, whereas prediction aligns the latent space with the downstream behav ioral
objective. Crucially, engagement (𝑌) is strictly excluded from the encoder. Given the causal pathway

 26

𝐿 → 𝑋 → 𝑌 , conditioning on 𝑌  induces post -treatment and mediator -collider bias, contaminating
𝑍𝐿 with outcome-dependent shortcuts and violating the counterfactual premise of 𝑑𝑜(𝐿) interventions.
By learning 𝑍𝐿  solely from confounder -adjusted 𝑋  and optimizing it via parallel losses, our
architecture ensures that engagement forecasts under label interventions remain causally valid, robust
to stylistic noise, and free from outcome leakage, as illustrated in Figure 5.
The model takes as input the marketing copy 𝑋, label vector 𝐿 ∈ {0,1}𝐾, observed environment
covariates 𝐶 , estimated unobserved common confounders 𝐸𝑚  from Section 4.1. Specifically, the
marketing copy is represented by the last hidden state of LLM. These are encoded into a structured
latent space 𝑍𝑒 = [𝑍𝑒,𝐿, 𝑍extra], where 𝑍𝑒,𝐿 ∈ 𝑅𝑃 is dedicated to the representation of labels. Since the
dimensions of 𝑍𝑒,𝐿  is independent, in order to model dependencies among labels, we introduce a
Causal Layer (Figure 6a) that applies a learnable adjacency matrix 𝐴 ∈ 𝑅𝑃×𝑃 (parameterizing directed
information flow across label dimensions) and leak the information 𝜖 from first reparametrized 𝑍𝑒,𝐿:
𝑧𝑗 = 𝑓𝑗 (∑ 𝐴𝑗𝑘 ⋅ 𝑧𝑒,𝐿𝑗𝑘
𝐾
𝑘=1
, 𝜖𝑗; θ𝑗) . (19)
The DAG constraint ℒ𝐷𝐴𝐺 = tr(𝑒𝐴⊙𝐴𝑇 ) − 𝑃 enforces acyclicity, and sparsity is encouraged by
ℒ𝑠𝑝𝑎𝑟𝑠𝑒 = ‖𝐴‖1.
When we intervene on a specific label 𝐿𝑗 to get counterfactual (flip the label and keep other labels
unchanged), the intervention is applied to the corresponding latent space 𝑍𝐿, which then interacts with
other latent labels through the Latent Interaction Network 𝐴 to directly influence user engagement
(Figure 6b). For instance, activating the “dating-ready” label directly perturbs the label-aligned latent
space Z𝐿, which then propagates through A. This propagation induces structured shifts in the latent
space ZL: dimensions causally linked to social/romantic contexts are activated, whereas those encoding
routine or purely functional usage are suppressed. Then the latent space capturing the interactions
between labels 𝑍𝑑 = [𝑍𝐿, 𝑍extra]  is decoded to marketing copy 𝑋  and the user engagement Y. The
updated joint representation Z𝑑 = [Z𝐿, Zextra] thus captures the scenario -shifted semantic distribution.
When decoded, these latent changes translate into precise textual adaptations —such as shifting from
baseline “daily commute” phrasing to “dating-ready, complexion enhancing” cues, full example can be

 27

seen in Appendix B.

(a) SCM in Latent Label Space
(b) Flip on Factual 𝐿𝑗 through label space 𝑍𝐿 to get counterfactual 𝑌𝑐
Figure 6: Causal Layer of D-V AE and Counterfactual Estimation
The inference of 𝑍𝐿 as a proxy for intervention relies on two mechanisms. First, we enforce label
supervision via
ℒ𝑙𝑎𝑏𝑒𝑙 = ‖𝑔(𝑍𝐿) − 𝐿‖2 2 (20)
which ensures 𝑍𝐿 faithfully reconstructs 𝐿, where 𝑔 is an MLP. Second, 𝑍𝐿 is used in the decoder to
reconstruct both 𝑋 and 𝑌. Specifically, the text reconstruction loss
ℒ𝑋 = ‖𝑋 − 𝑋̂‖2 2 (21)
forces 𝑍𝐿 to learn how label selection 𝐿 shape the marketing copy 𝑋, while the outcome prediction
loss
ℒ𝑌 = ‖𝑌 − 𝑌̂‖2 2 (22)
ensures 𝑍𝐿 captures how labels drive engagement.
However, restricting all causal reasoning to 𝑍𝐿 risks discarding information about other covariates
( 𝑋𝐿̃, 𝐸𝑚̂ , 𝐶 ) due to the label supervision, leading to prediction bias. As Melnychuk et al. (202 3)

 28

emphasize, low-dimensional causal representations reduce variance in low -sample CATE estimation
but often violate ignorability assumption. To resolve this, we introduce an auxiliary subspace 𝑍𝑒𝑥𝑡𝑟𝑎 ∈
𝑅𝑑𝑒𝑥𝑡𝑟𝑎 that captures residual variation from 𝑋𝐿̃, 𝐶, and 𝐸𝑚̂ . The full latent space 𝑍 = [𝑍𝐿, 𝑍𝑒𝑥𝑡𝑟𝑎]
is used in the decoder for reconstruction and prediction, ensuring confounders are controlled without
contaminating the causal subsystem since 𝑍𝐿  and 𝑍𝑒𝑥𝑡𝑟𝑎  are independent and the SCM structure
doesn’t change 𝑍𝑒𝑥𝑡𝑟𝑎. These guarantee that intervening on 𝑍𝐿 simultaneously controls 𝑋 and other
downstream factors to predict 𝑌.
The inductive biases (Li et al., 2024) in this case are:
ℒ𝑐𝑎𝑢𝑠𝑎𝑙ℓ = 𝐶𝐸(𝒞(𝐿𝑖, 𝛺), 𝐿𝑗) − 𝛾𝐶𝐸(𝒞(𝐿𝑖0, 𝛺), 𝐿𝑗),
ℒ𝑐𝑎𝑢𝑠𝑎𝑙𝑦 = 𝑀𝑆𝐸(𝒟(𝐿𝑖, 𝛺), 𝑌) − 𝛿𝑀𝑆𝐸(𝒟(𝐿𝑖0, 𝛺), 𝑌). (23)
where CE and MSE stand for Cross-Entropy loss and Mean Square Error, respectively. 𝒞 is a classifier
of labels, 𝒟 is the decoder, 𝐿𝑖 is the original value, 𝐿𝑖0 denotes that wiping out 𝐿𝑖 by setting it to
zero, 𝛺 are other inputs of classifier and predictor, γ, δ denotes a dynamic parameter. We introduce
Counterfactual forward (iteratively feeding counterfactual generated by flipping on 𝐿𝑖 to 𝐿𝑖0  through
the model during training) to remove the inductive bias (Online Appendix C Algorithm 3).
The model is trained under a causally informed ELBO with other mentioned constraints,
ℒ𝐸𝐿𝐵𝑂 = 𝐸𝑞𝑍[log 𝑝(𝑋|𝑍𝑑)] + 𝐸𝑞𝑍[log 𝑝(𝑌|𝑍𝑑)] − 𝐷𝐾𝐿 (𝑞(𝑍𝑑|𝑋, 𝐿, 𝐶, 𝐸𝑚̂ ) | 𝑝(𝑍𝑑|𝑋, 𝐿, 𝐶, 𝐸𝑚̂ )) (24)
which consists of two parts: the reconstruction term, which decomposes into ℒ𝑋 (for copy 𝑋) and ℒ𝑌
(for user engagement); the KL divergence term which regularizes the posterior toward a confounder -
conditioned prior to preserving ignorability.
By Lagrange multiplier method, we have the new loss function:
ℒ𝐷−𝑉𝐴𝐸 = −ℒ𝐸𝐿𝐵𝑂 + 𝛼ℒ𝑙𝑎𝑏𝑒𝑙 + 𝛽(ℒ𝐷𝐴𝐺 + ℒ𝑠𝑝𝑎𝑟𝑠𝑒) + 𝜉 (ℒ𝑐𝑎𝑢𝑠𝑎𝑙ℓ + ℒ𝑐𝑎𝑢𝑠𝑎𝑙𝑦) (25)
where 𝛼, 𝛽, 𝜉  denote regularization hyperparameters. The detailed algorithm implementation is in
Appendix C algorithm 2.
Theorem 3 (C ausal Consistency of D -V AE): Under the Proxy-Controlled Unconfoundedness
condition, let 𝑌̂𝑖(ℓ)  denote the counterfactual outcome predicted for unit 𝑖  by intervening on

 29

𝑍𝐿  according to label configuration ℓ , D -V AE is causally consistent provided that the latent -
intervention approximation error and outcome-prediction error vanish as the sample size grows:
𝑌̂𝑖(ℓ) →
𝑝
𝔼[𝑌𝑖(ℓ) ∣ 𝐶𝑖, 𝐸̂𝑚,𝑖, 𝑍extra,𝑖]. (26)
Consequently, for any two label configurations ℓ1 and ℓ0 , the estimated causal effect for unit 𝑖
satisfies
𝜏̂𝑖(ℓ1, ℓ0) = 𝑌̂𝑖(ℓ1) − 𝑌̂𝑖(ℓ0) →
𝑝
𝜏𝑖(ℓ1, ℓ0) ≡ 𝔼[𝑌𝑖(ℓ1) − 𝑌𝑖(ℓ0) ∣ 𝐶𝑖, 𝐸̂𝑚,𝑖, 𝑍𝑒𝑥𝑡𝑟𝑎,𝑖]. (27)
Averaging 𝜏̂𝑖(ℓ1, ℓ0)  across units yields a consistent estimate  𝜏̂(ℓ1, ℓ0)  of the corresponding A TE
𝜏(ℓ1, ℓ0) ≡ 𝔼[𝜏𝑖(ℓ1, ℓ0)].
 In summary, the workflow of D-V AE (Figure 7) first recovers multiple treatment confounders via
Logit-PPCA and computes a theoretical PAC bound, then validating whether the empirical W -bound
width satisfies the threshold condition 𝑊[𝛽𝐿,𝛽𝑈] ≤ 2𝑟PAC; if violated, iterative deconfounding is applied
until the bound is satisfied, or otherwise terminates. Once this condition holds, the framework activates
the D -V AE architecture to learn a causally disentangled latent label space Z𝐿 , enabling robust
counterfactual engagement prediction and causal inference of label combination.

Figure 7: Workflow of D-V AE
Note: The iterative deconfounding denotes a refinement step that seeks to recover or proxy for 𝑒𝑠
when the PAC W-bound condition is not satisfied.

5. Data, Analysis and Results
5.1 Data Description and Variables
Our data are provided by a leading Chinese marketing agency with over 20 years of experience in the

 30

advertising industry. The agency was among the first in China to integrate generative AI into its content
production pipeline and has developed a mature, expert-driven labeling system for marketing creatives.
The dataset contains 29,177 branded contents (BGC) and professionally generated contents (PGC) used
in advertising creatives across three complexion product categories: liquid foundation, pressed powder,
and cushion compacts. All content was launched on the Little Red Book platform (also known as RED
or Xiaohongshu). These three categories share similar formulation technologies & applications, and
target customer segments—such as coverage, longevity, skin feel, and compatibility with sensitive or
oily skin—making them well suited for studying the transferability of expert labeling logic. Moreover,
these categories are among the most actively marketed and consumer-engaged beauty segments on RED.
As a result, they generate high-volume, high-quality content that reflects real-world GenAI deployment
in expert-guided marketing workflows. The sample includes posts created by the agency between June
1, 2024, and September 1, 2025 using an internally fine-tuned LLM specialized in beauty copywriting.
 The majority of these marketing copies range from 50 to 400 Chinese characters in length. For
each post, we examined three user engagement metrics: number of likes, comments, and collects (See
Figure 1 for an example). As shown in Figure 2 in Appendix D, these metrics exhibit a typical power-
law distribution; therefore, we applied a logarithmic transformation to all engagement variables in
subsequent modeling to mitigate skewness.
 The dataset is accompanied by a glossary of 72 expert-curated labels, derived from their marketing
experience. These labels span multiple dimensions: target audience (e.g., age, occupation, usage
scenario), product ingredients, claimed benefits, sensory experience, brand attributes, and content
format. How to choose the right labels in a campaign represents the core marketing skill of these experts.
Table 1. Descriptive Statistics of Variables
Type Variable Definition count mean std min max
Engagement
Likes The number of user likes 29,177 38.68 126.48 0 2,908
Comments The number of user comments 29,177 168.56 338.22 0 3,000
Collects The number of user collects 29,177 62.28 141.35 0 2,792

 31

Label
Description
Number of
Assigned
Labels2
Number of marketing
labels assigned with the
marketing copy
29,177 11.24 7.08 2 46
Controls
Copy_len
Length of the
marketing copy in
Chinese characters
29,177 355.05 231.93 3 1,930
Copy_image_c
oherence
Semantic coherence
similarity score
between text and
images
29,177 0.23 0.12 0 0.51
Emojis_num number of emojis used in the marketing copy 29,177 3.61 5.99 0 89
Image_num Number of images included in the post 29,177 5.67 3.77 0 19
Brand_popular
ity
Average engagement
score of the brand on
Red
29,177 3175.1 0 3,925.1 5 0 46,899
KOL_fans Number of followers of KOL 29,177 54,958. 97 168,25 3.96 58 8,366, 415
KOL_works
Number of posts
previously published
by the KOL
29,177 469.39 819.91 1 12,700
KOL_likes KOL’s historical total likes  29,177 318,06 7.83 886,94 8.43 12 99,717 ,750
KOL_collects KOL’s historical total collects received 29,177 131,21 5.11 319,76 7.04 0 13,714 ,744
Kol_level
KOL tier as classified
by the platform (tier 1
= top-tier, tier 2 = mid-
tier, …)
29,177 3.99 0.87 1 6
Is_holiday
Whether the copy was
published on a public
holiday (0 = no, 1 =
yes)
29,177 0.05 0.22 0 1
Day_of_week
The day of week the
copy was published (0-
6 represents Monday-
Sunday)
29,177 2.73 1.86 0 6
Publish_hour
The hour of day the
copy was published (0-
23)
29,177 8.25 3.96 0 23

For textual representation of marketing copies (𝑒𝑚𝑑(𝑋)), we used the last hidden state of Qwen3-32B,
a leading open-source LLM, as the semantic embedding of each copy. Additionally, we counted the
number of emojis in each post (Das et al., 2019), a feature particularly salient on RED, where emotional
and visual cues also drive user engagement. For multimodal content, we computed text -image
coherence using the Qwen -VL model and recorded the number of images included in each post
(Copy_image_coherence). We also controlled for several external factors related to channel and

2 The 72-label glossary generates a high-dimensional combinatorial assignment space, with 2,448 observed
two-label combinations and 50,013 observed three-label combinations in the data.

 32

platform in distribution stage that may influence engagement:  whether the marketing copy  was
published on a public holiday (Is_holiday), on a weekend ( Day_of_week), the specific hour of
publication (Publish_hour), the overall brand popularity index on RED (Brand_popularity), and key
KOL characteristics, including follower count  (KOL_fans), total number of past posts ( KOL_works),
historical total engagement ( KOL_likes, KOL_collects), and platform-verified KOL tier ( KOL_level).
Table 1 presents the descriptive statistics for those variables.
5.2 Model Evaluation and Results
5.2.1 Deconfounding Performance: Confounding Bias Mitigation
First, w e evaluate whether our proposed  deconfounding strategy effectively mitigates unobserved
confounding effects. We implement the deconfounder framework to identify the common confounders
𝐸𝑚 of multi-treatment 𝐿. Then we assess deconfounder performance following Wang & Blei (2019)
in terms of out-of-sample predictive score:
Predictive Score = ℙ (𝑡(𝐿repheld) < 𝑡(𝐿held)) , 𝑡(⋅) = 𝔼𝐸𝑚∣𝐿obs[log 𝑝( 𝐿held ∣∣ 𝐸𝑚 )], (28)
which tests whether the factor model can plausibly reconstruct unseen(held-out) labels; a score of 0.72
≫ 0.1 of our method confirms effective capture of shared confounding.
 To empirically assess the PAC guarantee from Theorem 2, we examine the W-bound as specified
in Section 4.3 . Given 𝑀 = 12 , 𝑛 = 29,177 , and 𝐾 = 72 , with 𝜂 = 0.05 , we calibrate 𝑐 =
0.17  based on the observed signal -to-noise ratio (mean causal effect ≈ 0.081 , residual variance ≈
0.78) and the 𝑅2 gain ≈ 0.13, yielding a theoretical PAC radius of 𝑟PAC = 0.243. The data -driven
Wasserstein radius 𝜀 =∣ 𝛿̂obs − 1 ∣ produces an empirical bias width of 𝑊[𝛽𝐿,𝛽𝑈] ≈ 0.033 and a mean
relative bias of 0.07% . Applying the diagnostic criterion 𝑊[𝛽𝐿,𝛽𝑈] ≤ 2𝑟PAC , the bound is deemed
highly informative, as the empirical width is substantially smaller than the 95% high -probability
threshold. This confirms that the small -bias condition holds robustly as we discussed before  Proxy-
Controlled Unconfoundedness Corollary, validating the ignorability of single-treatment confounds for
the subsequent D-V AE causal inference.
5.2.2 D-V AE performance: ITE Estimation
 Next, we show how D-V AE tackles with causality in terms of: (1) Intervention Fidelity and (2)

 33

Causal Inference of Engagement as discussed in Section 3.2. Intervention Fidelity examines whether
interventions in the latent label space 𝑍𝐿  faithfully reproduce the downstream effects of directly
manipulating the original label vector 𝐿. This requires that (i) semantic changes induced by a label
intervention are coherently reflected in the regenerated copy, and (ii) causal dependencies among labels
are respected during generation, preserving narrative consistency. We measure  Intervention Fidelity
through quantitative reconstruction loss (MSEX) and Causal Inference of Engagement by out-of-sample
counterfactual prediction accuracy ( MSEY). Together, these criteria ensure that Z𝐿  functions as an
actionable, causally disentangled proxy for marketer labels.
 To understand whether interventions on 𝐿  are faithfully propagated through 𝑍𝐿, we first conduct
a diagnostic check as an illustration: we add the “dating -ready” label to the original label set and
generate a new copy using the intervened 𝑍𝐿. As illustrated in Figure 8(b), the resulting copy naturally
incorporates dating-related messaging (“perfect for daily wear or a date —gives you that fresh, radiant
look that boosts your charm”) and delete the related scenario of “8 a.m. rush” while preser ving the
original functional claims. This coherent semantic shift demonstrates that 𝑍𝐿 successfully translates
discrete label interventions into contextually appropriate textual variations, thereby satisfying the
requirement of Intervention Fidelity. In another 100 random cases, we conducted the same diagnostic
test, the model achieves an IIA score of 96.7% (Li et al. 2026).  Moreover, our model achieves a low
marketing copy embedding reconstruction loss on the test set ( MSEX= 0.1103), indicating that the
decoder conditioned on 𝑍𝐿 and the auxiliary subspace 𝑍𝑒𝑥𝑡𝑟𝑎 produces marketing copies semantically
aligned with the originals. As shown in Figure 8(a), the reconstructed copy retains core product claims
such as suitability for combination-oily skin, balanced oil control and hydration, and all-day wearability.
It omits brand-specific slang and emotional expressions including “another all-day face-sticker monster”
and “devotee of Little Mix Cat”. This is not a failure of reconstruction but an inherent design feature of
𝑍𝐿. Under the posterior mean across multiple stochastic samples, 𝑍𝐿 prioritizes generalizable, high-
frequency semantic signals and filters out rare stylistic and non -structural noise. This property is
consistent with standard V AE-based compressive representations ( Kingma & Welling, 2013). The
abstractive characteristic positions  𝑍𝐿  as a causal proxy for strategic label choice, rather than a

 34

verbatim stylistic replicator.
Original Marketing Copy Reconstruction Marketing Copy (a)

Intervention Marketing Copy (b)
Figure 8: Illustration of Reconstruction and Intervention
Turning to Causal Inference of Engagement, our model achieves a low user engagement prediction
loss on the test set (MSEY = 0.0330). To estimate ITE, we sample 50 times in 𝑍𝐿 when intervening on
certain labels to predict counterfactuals, then take the mean difference between these predictions and
the factual value. In the diagnostic example (Fig.8), when the “dat ing-ready” label is introduced, the
model predicts the following mean individual causal effect on user e ngagement: Δ Y =
[ 3.6%, 1.8%, 3.4%] for likes, comments and collects, respectively with all corresponding p -values<
0.05. This pattern is behaviorally explainable: dating -themed content may increase both immediate
social reactions, such as likes and comments, and utility -related actions, such as collecting, because it
combines emotional appeal with occasion-specific relevance. Thus, the directional changes in 𝑌̂ reflect
genuine user psychology rather than algorithmic artifacts. For space consideration, we only report the
estimated individual treatment effect (ITE) for 10 labels (or label combinations) that are most impactful
for our specific case study in Table 2.
Table2.  ITE in the “Carslan Little Mix Cat Foundation” Campaign
Label
Intervention likes likes effect interval comments comments effect interval collects collects effect interval
dating-ready 3.6% [2.8%,  4.4%] 1.8% [1.4%,  2.2%] 3.4% [2.7%,  4.0%]
promotional
campaigns 6.7% [5.8%,  7.6%] 3.4% [2.9%,  3.8%] 6.1% [5.3%,  6.9%]
sensitive skin 6.6% [5.7%,  7.5%] 3.4% [2.9%,  3.8%] 6.1% [5.2%,  7.0%]

 35

Note: All the p-values of ITE are <0.05. The intervals are 95% Confidence Intervals.
5.2.3 D-V AE Performance: ATE Estimation
 To provide more generalizable insights into the causal contribution of individual marketing labels,
we examine the estimated A TE for each label across 24,800 campaigns in terms of the three engagement
dimensions. The ATE is calculated as a weighted average based on the ITEs in each campaign. Given
the high heterogeneity of ITEs, we use a normal distribution as the weighting scheme. The results reveal
distinct patterns of label efficacy  (Table 3). Labels conveying broad product benefits or leveraging
external social hooks consistently drive immediate social engagement. Specifically, “skin beautifying,”
“charity/CSR campaigns,” and “promotional campaigns” show the strongest positive effects across the
two positive engagement dimensions, likes and comments, with estimated total effects of +26.7%,
+26.3%, and +23.9%, respec tively, and all effects statistically significant (p < 0.001).  These labels,
however, exhibit a consistent trade -off: while they amplify short -term customer reactions, they are
associated with negative or null effects on long -term utility -driven actions  in terms of collects,
suggesting their appeal is primarily emotional or transactional. Conversely, labels targeting specific
demographics, such as “male audience” ( –16.7%), “domestic brand” ( –16.1%), show strong negative
effects on collects (all p < 0.001), indicating that such positioning may be perceived as less worthy of
future reference by users. This pattern underscores the importance of aligning label strategy with
campaign objectives: promot ional or cause -related labels excel at driving virality, whereas
coverage 2.9% [1.9%, 3.9%] 1.4% [0.8%, 1.8%] 2.6% [1.6%, 3.5%]
cost-effective 1.3% [0.4%,  2.1%] 0.5% [0.1%,  1.0%] 1.3% [0.5%, 2.1%]
business-
occasion -0.7% [-1.5%,  -0.1%] -0.5% [-1.0%,  -0.1%] -0.7% [-1.5%, 0.0%]
co-branded
campaign -2.1% [-3.2%,  -1.0%] -1.0% [-1.6%,  -0.5%] -1.9% [-2.9%,  -0.9%]
co-branded
campaign
+new design
9.5% [8.6%, 10.3%] 4.6% [4.2%,  5.0%] 8.6% [7.8%,  9.3%]
cost-effective
+dating-
ready
4.6% [3.9%,  5.4%] 2.3% [1.9%,  2.7%] 4.3% [3.6%,  5.0%]
oil control
+breathabilit
y +coverage
4.0% [3.4%, 4.6%] 2.0% [1.7%, 2.3%] 3.8% [3.2%, 4.4%]

 36

demographic-specific cues may sacrifice long-term engagement for short-term targeting precision.
Table 3.  ATE of Most Influential Labels Across Campaigns
Labels
Intervention likes likes effect interval comments comments effect interval collects collects effect interval
skin
beautifying 18.4% [18.0%, 18.8%] 8.3% [8.0%,  8.6%] -4.0% [-4.4%,  -3.7%]
charity/CSR
campaigns 18.2% [17.9%, 18.6%] 8.1% [7.8%,  8.5%] -4.4% [-4.8%,  -4.0%]
promotional
campaigns 16.6% [16.2%, 17.0%] 7.3% [7.0%,  7.6%] -4.0% [-4.4%,  -3.7%]
male
audience 3.0% [2.6%, 3.3%] 0.3% [0.1%, 0.7%] -16.7% [-17.0%,  -16.3%]
domestic
brand 4.2% [3.9%, 4.6%] 1.2% [0.8%,  1.5%] -16.1% [-16.5%,  -15.8%]
natural
gradient +
coverage
6.0% [5.4%, 6.6%] 3.8% [3.3%,  4.4%] 0.3% [0.1%,  0.5%]
oil control +
coverage 1.4% [0.8%, 1.9%] 2.8% [2.4%,  3.3%] 1.0% [0.5%,  1.5%]
cost-
effective+
coverage
1.1% [0.5%, 1.6%] 3.3% [2.8%,  3.8%] 0.8% [0.2%,  1.4%]
oil control +
oily skin +
coverage
4.6% [4.2%, 5.0%] 5.6% [5.1%,  6.0%] 1.3% [0.8%,  1.8%]
dry skin +
oily skin +
coverage
2.8% [2.3%, 3.3%] 4.5% [4.0%,  4.9%] 1.3% [0.7%,  1.8%]
oil control +
even skin
tone +
coverage
1.2% [0.7%, 1.7%] 3.6% [3.1%,  4.0%] 1.0% [0.5%,  1.5%]
Note: “Most Influential Labels” are defined based on the absolute magnitude of the estimated
coefficients. All the p-values of ATE are <0.001. The intervals are 95% Confidence Intervals.

Beyond marginal ATE of single labels, our analysis of label combinations reveals critical non-
linear interactions that significantly amplify engagement effects. Crucially, while individual labels are
constrained by an inherent trade-off that consistently yields negative or null effects on long-term
collects, strategically designed combinations break this limitation, transforming isolated drawbacks
into universally positive gains across all engagement dimensions. Contrary to the intuition that
frequently co-occurring labels are optimal, we find that the highest-value combinations are frequently
underutilized in practice, suggesting substantial room for efficiency gains in expert label selection
strategies. Among the top 150 frequent two-label combinations, the highest-value pairs are strikingly

 37

underused. The most promising combination is [natural gradient +coverage] (frequency rank 139),
which delivers positive effects across all engagement metrics: 6.0% likes, 3.8% comments, and a
modest but statistically significant 0.3% lift in collects. Two other coverage-centric pairs also
demonstrate Pareto-improving patterns: [oil control + coverage] (rank 38) yields 1.4% likes and 2.8%
comments with a 1.0% collects lift, while [cost-effective + coverage] (rank 53) achieves 1.1% likes,
3.3% comments, and 0.8% collects. Notably, all three combinations share "coverage" as a core
anchor, indicating that functional benefit framing may serve as a robust engagement multiplier when
paired with complementary attributes.
 This pattern is more intriguing in three-label combinations. The most impactful triplets are not
those most frequently used, but rather those that precisely fuse core efficacy with a targeted persona—
a combination largely overlooked in current practice. The highest -performing combination  is [oil
control + oily skin + coverage], which achieves the strongest engagement lift of 11.5%, driven by robust
gains in likes (+4.6%) and comments (+5.6%). Despite its superior performance, this synergistic trio
ranks only 133rd in historical usage frequency. [dry skin + oily skin + coverage] (rank 61) yields a
notable 8.6% lift, directly addressing the nuanced needs of combination skin users who experience both
dryness and oiliness. Even more revealing is [oil control + even skin tone + coverage] (rank 77), which
achieves a total effect of + 5.8%, highlighting the value of emphasizing product feel and wearability
alongside functional benefits. These results underscore that the most effective labeling strategies may
not be the most common ones, but those that address specific user needs with precision.
5.3 Ablation Analysis
 Here, we  demonstrate the contribution of each of the main components in D -V AE through an
ablation analysis. We first compare the ful l model against C-V AE as our benchmark since it also
supports SCM-based counterfactual interventions. We do not consider purely predictive yet non-causal
machine learning baselines, as they are not designed to support valid counterfactual reasoning.
Compared to the chosen benchmark , D-V AE achieves a reconstruction loss of  0.1103, while C-V AE
yields significantly higher reconstruction loss ( 0.1214, difference = 9.2%, p=  0.0002). In terms of
prediction losses, D-V AE achieves 0.0330, while C-V AE yields a higher value of 0.0339 (difference =
2.7%, p = 0.0292).

 38

Table 4. Ablation study
 Intervention
Fidelity
Causal Inference
of Engagement
MSEX  MSEY
MSEY  PER
DIMENSION
D-V AE (Full) 96.7% Yes 0.1103 0.0330
[0.0281,0.0365,
0.0345]
C-V AE
(w/o deconfounder Module)
83.5% No 0.1214 0.0339
[0.0296,0.0380,
0.0344]
w/o 𝑍𝑒𝑥𝑡𝑟𝑎 Module 51.7% No 0.1077 0.0381
[0.0323, 0.0432,
0.0387]
w/o SCM Module 20.3% No 0.0920 0.0302
[0.0265,0.0331,
0.0309]
w/o Inductive Bias Module 48.4% No 0.1133 0.0353
[0.0295,0.0404,
0.0359]
Note: Each row removes one module from the full model at a time. Intervention Fidelity is quantified
via IIA Score across 100 samples, which measures (i) success rate on the intervened label and (ii)
preservation of non-intervened attributes subject to compatibility constraints with the intervened label.
MSEX and MSEY are reported as auxiliary diagnostics.

We then investigate the incremental contribution of  other architectural components, with results
summarized in Table 4. The full model achieves high intervention fidelity (96.7%), demonstrating
precise semantic control during label interventions. Ablating the auxiliary subspace 𝑍𝑒𝑥𝑡𝑟𝑎 reduces
fidelity to 51.7%. Intriguingly, while this variant yields a marginally lower MSEX (−2.4%), the fidelity
drops suggest that there are uncontrolled variations brought by LLM and environments leaking into the
causal subspace 𝑍𝐿 , which distorts intervention boundaries. Removing the SCM module causes a
catastrophic collapse in fidelity (20.3%). Although it achieves the lowest MSEX (−16.6% relative to full),
the generated text becomes logically incoherent: for example, activating the “dating-ready” label inserts
romantic cues while retaining contradictory “early-morning student” context (e.g., “8 a.m. rush”) in the
Carslan Campaign (Figure8). Without the SCM  component, label dimensions are modeled
independently, preventing semantically coherent propagation and breaking narrative consistency.
Finally, ablating the Inductive Bias module reduces fidelity to 48 .4%. The absence of counterfactual
forward debiasing leaves residual narrative traces from the original copy (e.g., “budget -conscious”
phrasing persists under “premium” interventions).
Regarding Causal Inference of Engagement, valid out-of-sample counterfactual prediction requires

 39

both faithful interventions and a disentangled latent causal structure. Only the full model supports
reliable engagement inference. Removing 𝑍𝑒𝑥𝑡𝑟𝑎 increases MSEY by 15.5% and the Inductive Bias
ablation raises MSEY by 7.0%, reflecting biased engagement estimates due to unremoved confounding
traces. Notably, the SCM-ablated variant achieves the lowest MSEY but exhibits a markedly elevated
KL divergence (1.97 vs.  ≈0 for others), indicating a latent posterior that severely diverges from the
confounder-conditioned prior. This suggests that the model  likely memorizes spurious surface co -
occurrences rather than learning the underlying causal mechanism, rendering its low prediction error
invalid for counterfactual scenarios. The full model’s balanced MSEY (0.0330) and stable per-dimension
errors ([0.0281, 0.0365, 0.0345]) demonstrate robust, structurally sound engagement inference. Here,
MSEY and posterior diagnostics act as auxiliary validators: they yield a low value when corroborating
causal validity, but a low value alone cannot certify causal validity when structural constraints are
violated, making it a necessary but not sufficient indicator.
Collectively, these results confirm that 𝑍𝐿 functions as an interpretable and causally disentangled
embedding of 𝐿. It not only reconstructs and intervenes on copy with semantic fidelity but also yields
engagement predictions grounded in true label -driven mechanisms. This dual effectiveness enables
direct optimization of label selection for desired outcomes without requiring observing counterfactuals.
In the next section, we evaluate whether these counterfactual insights can empower non -expert
marketers to make data-informed copywriting decisions.
5.4 Direct Evidence from Controlled Experiment
To evaluate how the counterfactual predictions generated by D-V AE can effectively support real-
world marketing decisions, we conduct a  small-scale controlled experiment to assess whether D-V AE
recommended label configurations yield higher user engagement compared to expert -driven
optimization, C-V AE based intervention, and the unmodified original copy as the baseline control. We
randomly select 30 foundation-related marketing copies from our dataset; each originally annotated
with 15 –20 expert labels. For each copy, we allow the addition or removal of up to 5 labels
(approximately 25%–33% of the initial set), a range that provides sufficient flexibility to explore multi-
level label combinations while preserving thematic coherence. The total number of labels after
modification is capped at 25 to avoid logical inconsistencies (e.g., simultaneously selecting mutually

 40

exclusive labels such as “premium pricing” and “high value-for-money”).
A panel of five senior marketing experts with  at least 3 years of industry experience manually
optimizes the label set for each post. In parallel, D-V AE and C-V AE automatically select label
configurations that maximize predicted counterfactual engagement under identical constraints (detailed
in Appendix C Algorithm 4). To isolate the effect of label selection from generative model variability,
all four versions: original (control), expert -modified, D-V AE-modified, and C-V AE-modified are
generated using the same LLM (Qwen-3) conditioned on their respective label sets.  To validate that
label interventions produced semantically coherent shifts in ad copy, we conducted an automated
manipulation check using a different LLM (GPT-5.4). For each intervened ad, the model scored (1–10)
how well the modified copy reflected the intended label changes —specifically, emphasizing added
labels and de -emphasizing removed ones. Across all 90  (3×30) manipulated creatives, the average
alignment score was 8. 5 (SD = 0.78), with 9 7.8% of cases scoring ≥7. This confirms that our
interventions successfully induced the targeted semantic shifts in generated contents.
We randomly recruited 120 participants from the beauty-focused RED users. The sample reflects
the distribution of RED users with a majority identifying as female and exhibiting diverse makeup needs
(e.g., “Learn Makeup,” “Date Makeup,” “Anti -aging Skincare”). Detailed demographic distributions
are provided in Appendix E. We then randomly assigned them to one of the four experimental conditions
to decide whether to like, comment, or collect it. We use the aggregated engagement score (sum of the
three actions) per post per condition as our unit of analysis.
As shown in Figure 9, both the expert and D-V AE conditions achieve higher engagement than the
control and C-V AE conditions. To formally test this pattern, we perform a two -way ANOV A without
replication, treating version type (4 levels) and original copy ID ( 30 groups) as fixed factors. Results
(Table 5) reveal a highly significant main effect of version type ( 𝑝 < 0.001), confirming that the choice
of label intervention strategy has a significant impact on user engagement. The effect of copy ID is also
statistically significant (  𝑝 < 0.001 ), reflecting expected heterogeneity in baseline appeal across
different ad creatives. Importantly, the significance of version type persists even after accounting for
this creative-level variation, supporting the conclusion that label intervention consistently influences
engagement outcomes. Post-hoc pairwise comparisons (Table 6) with Bonferroni correction ( 𝛼 =

 41

0.0125) further show that D-V AE performs equivalently well as human experts do ( 𝑝 = 0.9332), and
both significantly outperform the control (  𝑝 = 0.0053  for D-V AE; 𝑝 = 0.0097  for Expert). In
contrast, C-V AE shows no significant improvement over the unmodified baseline ( 𝑝 = 0.3081).

Figure 9. The Mean Total Engagement by Version Group (with 95% CI)
These findings demonstrate that the counterfactual predictions produced by D -V AE translate
directly into measurable real-world impact: labels recommended by the model enable non-expert users
to generate marketing creatives that achieve engagement statistic ally indistinguishable from those
crafted by seasoned professionals. This validates that expert marketing skills can be successfully
digitized and replicated.
Table 5. Results of Two-way ANOV A Without Replication
Source Sum of Squares df F-value Pr(>F)
C(version) 607.1 3 6.448103 0.000541
C(copy_id) 3057.8 29 3.359728 0.000007
Residual 2730.4 87 - -

Table 6. Results of Independent Samples T-tests (Bonferroni-corrected)
Comparison Group t-value df
Two-tailed
p-value
Bonferroni-
corrected α
Significance
Expert vs D-VAE -0.0842 58 0.9332 0.0125 no
Expert vs Control 2.6765 58 0.0097 0.0125 yes
D-VAE vs Control 2.8994 58 0.0053 0.0125 yes
C-VAE vs Control 1.0283 58 0.3081 0.0125 no

 42

The inferior performance of the C-V AE baseline stems from its inability to adjust for unobserved
confounders. A concrete example is the “Carslan Little Mix Cat Foundation” campaign (Fig. 8). The
original high -performing labels emphasized suitability for co mbination skin, oil control, skin -
nourishing benefits, and co-branded design. Our D-V AE correctly identifies efficacy-related labels (e.g.,
“sensitive-skin friendly,” “natural ingredients,” and “buildable coverage”) as the true drivers of
engagement. In co ntrast, C -V AE spuriously recommends “business occasion” and “high -income
audience”, labels that co -occur with premium brands’ high -budget professional campaigns on RED,
creating a confounding correlation overlooked by C -V AE (Fig. 4(b)). For a mass-market product like
Carslan, such mismatched positioning produces inauthentic messaging and lower engagement. By
incorporating a deconfounder that captures latent shared factors (e.g., brand tier and KOL expertise),
D-V AE successfully disentangles causal signals from platform-induced noise, yielding both accurate
and operationally interpretable recommendations.
6. Simulation Study
Having established D-V AE’s empirical credibility in a large-scale, real-world marketing application and
further demonstrated its practical value through a controlled field experiment, we turn to two remaining
questions. First, how accurately can D-V AE recover causal effects when the  ground truth is known?
Second, how does the framework generalize beyond the setting of marketing-label attribution?
 These questions are difficult to answer with observational data because true causal effects and
latent confounders are inherently unobserved. Real -world validation must therefore rely on indirect
evidence, such as counterfactual prediction, intervention co nsistency, and application -specific
diagnostics. A simulation study overcomes this limitation by allowing us to specify both the ground -
truth causal effects as well as the level and structure of unobserved confounding. It therefore provides
a direct and systematic test of causal-effect recovery.
  We design the simulation around a general class of GenAI-mediated settings which we instantiate

 43

in a labor-market setting: job candidates select keywords to guide an LLM in generating professional
biographies intended to attract recruiters’ interest. By varying the form and intensity of shared and
attribute-specific confounding, we evaluate D -V AE’s causal-recovery accuracy, robustness, and
boundary conditions.
We begin by formalizing the general class of problems to which D-V AE applies.
Table 7. Generic Data Structure and Notation
Notation Status Description
𝐿𝑖 Observed A 𝐾-dimensional vector of actionable attributes or skill primitives for unit 𝑖
𝑋𝑖 Observed A high-dimensional unstructured artifact generated by an LLM
𝑌𝑖 Observed The downstream outcome
𝐶𝑖 Observed/Optional Pre-treatment covariates that may be observed for adjustment
𝑒𝑚,𝑖 Latent A shared confounder affecting multiple dimensions of 𝐿𝑖 and 𝑌𝑖
𝑒𝑠,𝑖,𝑗 Latent A single-treatment confounder affecting a focal attribute 𝐿𝑖𝑗 and 𝑌𝑖
𝑅𝑖
= ℎ𝜙(𝑋𝑖) Learned A representation of semantic and stylistic information contained in the artifact
𝑌𝑖(ℓ) Counterfactual The outcome that would be observed under attribute configuration 𝐿𝑖 = ℓ
6.1 Generic Problem Formulation for GenAI-Mediated Skill Valuation
 Many GenAI -augmented workflows share a common causal -attribution problem. A d ecision
selects multiple actionable skill primitives, and these inputs steer LLM to generate a high-dimensional
artifact that drives a performance outcome. The empirical objective is not merely to predict performance,
but to determine which individual attributes (skills) and attribute configurations causally improve it.
The marketing-label application examined in this study represents one practical instance of this broader
problem.
 Consider 𝑁  observational units indexed by 𝑖 = 1, … , 𝑁  (see Table 7 for key notations and

 44

descriptions). For each unit, the analysts observe
𝒟𝑁 = {(𝐿𝑖, 𝑋𝑖, 𝑌𝑖, 𝐶𝑖)}𝑖=1 𝑁 ,  𝐿𝑖 = (𝐿𝑖1, … , 𝐿𝑖𝐾)⊤ ∈ ℒ,
where 𝐿𝑖 is a 𝐾-dimensional vector of attributes, 𝑋𝑖 is the artifact generated by the LLM, 𝑌𝑖 is the
downstream outcome, and 𝐶𝑖 contains observed pre-treatment covariates. The focal causal pathway is
𝐿𝑖 → 𝑋𝑖 → 𝑌𝑖: the selected attributes shape the generated artifact, which in turn influences performance.
 Attribute assignment is generally not randomized. We distinguish a shared confounder 𝑒𝑚,𝑖, which
can affect several attributes jointly, from an attribute -specific confounder 𝑒𝑠,𝑖𝑗, which affects a focal
attribute and the outcome without necessarily inducing dependence across attributes. A generic
structural system is
𝐿𝑖𝑗 = 𝑔𝑗(𝑒𝑚,𝑖, 𝑒𝑠,𝑖𝑗, 𝜀𝑖𝑗 𝐿 ),   𝑗 = 1, … , 𝐾.
𝑋𝑖 = 𝑔𝑋(𝐿𝑖, 𝐶𝑖, 𝑒𝑚,𝑖, 𝜀𝑖 𝑋),  𝑌𝑖 = 𝑔𝑌(𝐿𝑖, 𝑋𝑖, 𝐶𝑖, 𝑒𝑚,𝑖, 𝑒𝑠,𝑖, 𝜀𝑖 𝑌). (29)
where 𝑒𝑠,𝑖 = (𝑒𝑠,𝑖1, … , 𝑒𝑠,𝑖𝐾)
⊤
. The joint assignment pattern of 𝐿𝑖 may contain information about 𝑒𝑚,𝑖,
whereas an attribute-specific confounder need not leave a comparable cross-attribute signature. In
addition, 𝑋𝑖 is a stochastic, high-dimensional mediator whose semantic and stylistic variation may
affect 𝑌𝑖 beyond what is encoded directly in 𝐿𝑖. The learned representation 𝑅𝑖 = ℎ𝜙(𝑋𝑖) is therefore
used to summarize mediator-side information relevant to counterfactual prediction.
 Let 𝑌𝑖(ℓ) denote the potential outcome under the joint intervention 𝐿𝑖 = ℓ. For attribute 𝑗, the
average causal effect of changing its value from 𝑎′ to 𝑎, while averaging over a reference distribution
𝑄−𝑗 of the remaining attributes, is
𝜏𝑗(𝑎, 𝑎′) = 𝔼𝐿𝑖,−𝑗∼𝑄−𝑗[𝑌𝑖(𝑎, 𝐿𝑖,−𝑗) − 𝑌𝑖(𝑎′, 𝐿𝑖,−𝑗)].
For a binary attribute, the conventional contrast is 𝜏𝑗 = 𝜏𝑗(1,0). More generally, the causal effect of
replacing one complete attribute configuration ℓ′ with another configuration ℓ is
𝜏(ℓ, ℓ′) = 𝔼[𝑌𝑖(ℓ) − 𝑌𝑖(ℓ′)].

 45

 Both estimands are total effects: they allow interventions on 𝐿𝑖 to propagate through the
generated artifact 𝑋𝑖 before affecting 𝑌𝑖. The estimation objective is to recover these effects despite
three identification challenges: latent confounding shared across multiple attributes, confounding
specific to a single attribute, and high-dimensional stochastic mediation through the LLM-generated
artifact.
D-V AE addresses these challenges by combining a multi -treatment deconfounder with causal
representation learning. The deconfounder uses joint attribute -assignment patterns to recover shared
latent structure, while the representation model captures intervention-relevant variation in 𝑋𝑖. Because
single-treatment confounders cannot generally be recovered from cross-attribute dependence alone, D-
V AE’s theoretical analysis characterizes the remaining omitted -variable bias through PAC -based
bounds rather than assuming it away. In empirical applications, where true causal effects are unobserved,
causal fidelity is evaluated indirectly through intervention consistency and predictive diagnostics,
including IIA, MSEX , and MSEY . In the simulation, the data -generating process supplies the ground -
truth effects, allowing direct evaluation through bias, RMSE, and confidence-interval coverage.
6.2  Simulation Design: LLM-Generated Political Candidate Biographies
 To evaluate D-V AE against known causal effects and outside the marketing application, we adapt
the candidate -biography simulation of Imai and Nakamura (2025), which builds on the political
candidate profile experiment of Fong and Grimmer (2016). In that setting, survey respondents evaluate
biographies of political candidates, and the focal textual feature is a candidate’s military background.
Imai and Nakamura use Llama 3 –8B to generate 4,000 biographies of hypothetical politicians, code
military background  using the keywords such as  “military,” “veteran,” and “army,” and represent
confounding features using a politics -and-education topic and TextBlob sentiment. We use the same
4,000-biography corpus as a realistic textual foundation, but extend the design to a multi -attribute
treatment space and a fully specified data -generating process with known causal effects. The
biographies retain semantic, stylistic, and narrative variation beyond the coded attributes, thereby

 46

preserving the high-dimensional mediator-side complexity that motivates D-V AE.
For biography 𝑖, let 𝐿𝑖 = (𝐿𝑖1, 𝐿𝑖2, 𝐿𝑖3, 𝐿𝑖4, 𝐿𝑖5)⊤ ∈ {0,1} denote five binary attributes. We set 𝐿𝑖𝑗 =
1  when the biography contains at least one term from the dictionary for attribute 𝑗 , and 𝐿𝑖𝑗 = 0
otherwise. The attributes capture elite education ( 𝐿𝑖1; e.g., Ivy League, honors degree, law degree),
political experience ( 𝐿𝑖2 ; e.g., congress, senate, mayor), military experience ( 𝐿𝑖3 ; military, veteran,
army), business and economic experience ( 𝐿𝑖4 ; e.g., business, budget, finance), and public -service
orientation (𝐿𝑖5; e.g., healthcare, education reform, community). The military dictionary reproduces the
coding used by Imai and Nakamura (2025); the remaining four attributes are study-specific extensions
informed by prior research on candidate competence, experience, an d public orientation. We inspect
marginal frequencies and pairwise co -occurrence before estimation to rule out near -degenerate labels
and severe overlap problems.
We next construct shared and attribute-specific confounders that are known to the simulation but
withheld from the estimators.  The shared multi-treatment confounder  𝑒𝑚,𝑖 = (𝑒𝑚1,𝑖, 𝑒𝑚2,𝑖, 𝑒𝑚3,𝑖)
⊤

captures social capital, seniority, and civic orientation. These components are proxied by biography -
level cues such as prominent family or high-status careers, biography length or number of offices held,
and community-service or public -service language. The single-treatment confounder 𝑒𝑠,𝑖  targets the
military attribute 𝐿𝑖3 and captures national -security salience. We first compute a security score 𝑆𝑖 sec
from terms such as “national security,” “public safety,” and “law enforcement,” which do not overlap
with the military-label dictionary. We then orthogonalize this score with respect to the remaining labels
and the shared confounder:
 𝑒𝑠,𝑖 = 𝑆𝑖 sec − 𝔼̂[𝑆𝑖 sec ∣ 𝐿𝑖,−3, 𝑒𝑚,𝑖].
This residualization isolates security -related semantic variation associated specifically with 𝐿𝑖3

 47

rather than with general label co -occurrence. Finally, define 𝑀𝑖 = sentiment(𝑋𝑖) ∈ [−1,1]  as the
TextBlob polarity score of biography 𝑋𝑖 . Imai and Nakamura (2025) use TextBlob sentiment as a
confounding feature in their simulation. We retain the same text summary but assign it a distinct role in
our data-generating process: 𝑀𝑖 captures outcome-relevant mediator-side variation embedded in the
generated biography and is not supplied to the estimators as a structured control.
 The synthetic candidate-evaluation score is generated by the following DGP:
𝑌𝑖 = 𝛽⊤𝐿𝑖 + 𝐿𝑖 ⊤𝐵𝑒𝑚,𝑖 + 𝛤⊤𝑒𝑚,𝑖 + 𝛼𝑚𝑀𝑖 + Θ𝑒𝑠,𝑖 + 𝜖𝑖 (29)
The disturbance satisfies 𝜖𝑖 ∼ 𝑁(0, 0.52). The vector 𝛽 = (0.3,0.2,0.35,0.15,0.25) contains the
baseline attribute effects, 𝛤 = (0.3, −0.20,0.25)  governs the effect of the shared confounding, B
allows each attribute effect to vary with the shared confounder, and 𝛼𝑚 = 0.20  controls the
contribution of biography sentiment. The interaction matrix is
𝐵 =
(

0.12 0.04 0.02
0.03 0.10 0.08
0.02 0.06 0.05
0.08 0.08 0.04
0.05 0.03 0.09)

 .
The parameters are calibrated to reflect the core structure in Equation (29): the direct effects of 𝐿𝑖
and the shared confounder 𝑒𝑚 are the main determinants of 𝑌𝑖, because they represent the target causal
signal and the central identification challenge. Treatment -effect heterogeneity and mediator -side
variation play smaller but meaningful roles, preserving the 𝐿𝑖 → 𝑋𝑖 → 𝑌𝑖 mechanism without allowing
these components to dominate, while the disturbance term prevents the outcome from becoming nearly
deterministic. Under this calibration, differences in performance across estimators primarily reflect their
ability to recover th e effects of 𝐿𝑖 while accounting for shared confounding, mediator -side variation,
and treatment heterogeneity, rather than sensitivity to the exact numerical values of the coefficients.
Because the structural model is known, causal fidelity can be evaluated against the exact sample-

 48

average effect. Holding 𝐿𝑖,−𝑗, 𝑒𝑚,𝑖, 𝑒𝑠,𝑖, 𝑀𝑖, and 𝜀𝑖 fixed, define the unit-level effect of attribute 𝑗 as
 𝛥𝑖𝑗 = 𝑌𝑖(1, 𝐿𝑖,−𝑗) − 𝑌𝑖(0, 𝐿𝑖,−𝑗).
The corresponding ground-truth sample-average effect is
 𝜏𝑗 ⋆ = 1 𝑛 ∑ 𝛥𝑖𝑗
𝑛
𝑖=1
= 𝛽𝑗 + 1 𝑛 ∑ 𝐵𝑗⋅
𝑛
𝑖=1
𝑒𝑚,𝑖.
Thus, the simulation provides an exact benchmark against which the estimated attribute effects can
be evaluated, while retaining heterogeneous effects through the interaction between 𝐿𝑖 and 𝑒𝑚,𝑖.
We evaluate four confounding scenarios (Table 8), holding all other parameters fixed and varying
only the outcome sensitivity 𝛩 to the military -specific confounder. Let ∥ 𝛤 ∥2 denote the Euclidean
magnitude of the shared-confounder coefficient vector.
Table 8: Four Scenarios of Different Confounding Structure
Scenario
Single-confounder
strength
Interpretation
Shared only 𝛩 = 0 Only confounding shared across multiple attributes affects the outcome.
Weak single 0 < 𝛩 <∥ 𝛤 ∥2 Introduces a modest confounder specific to the military attribute.
Bounded single 𝛩 =∥ 𝛤 ∥2 Sets single -treatment confounding equal to the magnitude of shared confounding.
Strong single 𝛩 = 2 ∥ 𝛤 ∥2 Stress-tests D -VAE under dominant single -treatment confounding.
 This sequence progressively weakens the multi -treatment deconfounder condition. It therefore
tests whether D -V AE can recover attribute-level causal effects when confounding is shared across
treatments, when a focal attribute has additional idiosyncratic co nfounding, and when that single -
treatment confounding becomes the dominant source of bias.
6.3  Estimators and Evaluation Metrics
 For each biography, we extract an internal representation 𝑅𝑖 from the hidden states of Qwen-3. D-
V AE and Gen-AI Powered Inference (GPI) then use these representations directly. For the conventional

 49

estimators, we additionally construct BERT embeddings as text-level controls (Devlin et al., 2019). We
compare D-V AE with three established benchmarks: ordinary least squares  (OLS), which provides a
transparent linear estimate of average attribute effects; Double Machine Learning (DML), which uses
flexible nuisance models and orthogonization to reduce bias from observed covariates (Chernozhukov
et al., 2018); and Causal Forest (CF), which accommodates heterogenous treatment effects through tree-
based estimation and sample splitting. For each conventional estimators, we evaluate both a baseline
specification and a BERT-augmented specification. GPI is the closest GenAI-based benchmark because
it similarly leverages LLM-derived text representations for causal inference (Imai and Nakamura, 2025).
 All estimators are evaluated using identical simulated-samples and use the same 70%/30% train–
test split within each replication. The biography corpus, attribute labels, confounders, and ground-truth
effects are held fixed across methods, while outcome noise is regenerated for each Monte Carlo seed .
Each estimator is then refitted and used to recover the five attribute-specific average treatment effects.
We conduct 50 Monte Carlo replications for each confounding scenario.
 Performance is evaluated using mean absolute bias, RMSE, and the empirical coverage of
bootstrap 95% confidence intervals. Mean absolute bias captures systematic deviation s from the
ground-truth effects, whereas RMSE captures both bias and variation across simulation replications and
places greater weight on large errors. Lower values of both metrics indicate more accurate causal effect
recovery. Coverage measures the proportion of confidence intervals that contains the corresponding
true effects, with values near 95% indicating well-calibrated uncertainty. Together, these metrics assess
both point-estimation accuracy and inferential reliability.
6.4  Simulation Results
 Figure 10 reports the  results. Across all four confounding scenarios, D -V AE achieves the lowest

 50

mean absolute bias, RMSE, and among the best for coverage confidence intervals , demonstrating
consistently stronger recovery of the ground -truth attribute effects. Conventional estimators that rely
only on structured covariates—OLS, DML, and CF—perform substantially worse in this text-mediated
setting. Adding BERT embeddings improves their performances, reducing average absolute bias by
36.3%, 33.3%, and 26.5% respectively. Nevertheless, all BERT-augmented estimators remain less
accurate than D -V AE. Although BERT-augmented CF attains  relatively high confidence -interval
coverage in some scenarios, its substantially larger bias and RMSE indicate that coverage alone does
not translate into accurate effect recovery.

Figure 10. Model Performance of Average Label Effect Inference Across Scenarios
 D-V AE also outperforms GPI, the closest GenAI -based benchmark. Relative to  GPI, D -V AE
reduces absolute bias by 33.6%, 23.6%, 17.3%, and 34.6% in the shared -only, weak-single, bounded-
single, and strong -single scenarios, respectively. The corresponding RMSE reductions are 38.1%,
25.4%, 10.8%, and 29.5%. D-V AE’s bootstrap 95% confidence-interval coverage is 52%, 36%, 32%,
and 72% across the four scenarios, compared with 32%, 32%, 52%, and 60% for GPI. Thus, D-V AE
provides more accurate point estimates in every scenario and achieves comparable or better interval
coverage in three of the four scenarios. However, coverage remains below the nominal 95% level for
both methods, indicating that uncertainty calibration remains challenging even when point -estimation

 51

accuracy improves.
 The attribute-level results clarify the source of D-V AE’s advantage (Figure 11). D-V AE performs
particularly well for elite education ( 𝐿1), business and economic experience ( 𝐿4), and public -service
orientation (𝐿5). These attributes benefit most from modeling the joint assignment structure, suggesting
that their confounding is largely shared across attributes. GPI is occasionally competitive for political
experience (𝐿2), whose effect appears more readily recoverable from the LLM representation alone.
Military experience ( 𝐿3 ) is the most difficult attribute for all estimators because the simulation
deliberately assigns its focal confounder only to that treatment. Such single-treatment confounding may
not generate cross -attribute dependence and therefore cannot be fully recove red from treatment co -
occurrence. D-V AE nevertheless remains comparatively robust when this confounding is bounded.
Figure 11. Model Performance of Individual Label Effect Inference
 Overall, the simulation provides a direct ground -truth assessment of causal fidelity and
demonstrates that D -V AE generalizes beyond marketing-label attribution. Its advantage is strongest
when shared confounding remains informative, but narrows as single-treatment confounding becomes

 52

dominant. These findings both support D -V AE’s applicability to high -dimensional, LLM-mediated,
multi-attribute settings and identify an important boundary condition: the framework is most effective
when the joint treatment structure contains sufficient information about the dominant latent confounders.
7. Discussion
We introduce a deconfounding framework that attributes engagement outcomes to labels, shifting the
analytical focus from evaluating AI-generated products to upstream skill assessment. In modern AIGC
workflows, practitioners no longer control final artifacts directly, instead they intervene via structured
inputs such as labels as explicit skill primitives. However, a concomitant challenge arises: identical
skill configurations can yield stochastic outputs, and skill value attribution is systematically
confounded by unobserved confounds such as firm budget constraints, LLM capability and platform
matching algorithms. Causal inference that determines the causal impact of skill on final performance
is thus essential: it needs to isolate the true actionable drivers of downstream value from spurious
correlations and mediator noise.
 Methodologically, D -V AE contributes by adapting deconfounding and causal representation
learning to a new causal object: upstream skill configurations in stochastic LLM-mediated production.
Standard deconfounder methods use treatment co-occurrence to recover shared latent confounders, but
they do not address settings where treatment effects are mediated through generated content or where
label-specific confounders may still bias attribution. D -V AE accommodates this logic by combining
multi-label confounder recovery with an explicit bound on omitted bias from single -treatment
confounders in nonlinear situations. V AE variants, by contrast, learn structured latent factors mainly for
disentangled generation or sample -level interventions. D -V AE repurposes the latent space for causal
skill valuation: it represents expert label-selection logic, separates label-driven semantic variation from
auxiliary environmental and mediator -side noise, and predicts downstream engagement under label
interventions. The resulting framework attributes performance to actionable label configurations rather
than to incidental wording, platform selection, or historical co-occurrence. This makes D-V AE a unified
framework for valuing AI -augmented skills, rather than a direct application of existing causal or
generative models.

 53

 Empirically, D-V AE identifies valuable yet underutilized skill configurations, showing how latent
expertise can be translated into economically meaningful interventions. Our simulation study extends
this evidence to a broader class of multi-attribute, LLM-mediated attribution problems and reveals how
the framework’s performance varies as confounding shifts from shared to attribute-specific sources. A
controlled experiment provides complementary evidence  of practical impact : D-V AE-recommended
label configurations increased total engagement by 32.7% relative to the original campaigns and
performed comparably to configurations developed by senior experts. Taken together, these findings
show that D -V AE can transform historical expert decisions into scalable , auditable guidance for
selecting and combining AI-augmented skills. This capability enables organizations to move beyond ad
hoc prompt engineering, costly trial-and-error, and exhaustive live experimentation toward systematic
causal evaluation and optimization of skill portfolios.
 Our work carries three key implications. First, it establishes a skill -to-product value attribution
paradigm, resolving the identification gap in stochastic LLM mediation and providing a generalizable
structure for decomposing aggregate outcomes into cons tituent skill contributions. Second, by
formalizing expert labeling logic as a causally disentangled latent representation, we demonstrate that
tacit know-hows can be systematically extracted and operationalized—democratizing high-quality AI-
augmented creation. Third, our deconfounded counterfactual framework provides a methodological
foundation for pricing and optimizing AI-augmented skill portfolios. Managers can now simulate what-
if skill interventions, identify synergistic combinations, and allocate creative resources based on causal
ROI rather than historical frequency, turning generative AI into an insight-driven co-pilot.
 We acknowledge three limitations. First, our implementation focuses on a single product category
(complexion cosmetics); marketing label systems emphasizing formulation and sensory cues may not
directly transfer to domains with distinct attribute structures. Future work could develop cross-domain
skill representations that capture shared structural mappings between strategic inputs and consumer
response. Second, we assume a static label ontology, whereas expert knowledge and market trends
evolve continuously. Extending this framework to dynamic causal models would allow firms to track
how the marginal value of specific skills shifts with competitive activity, platform algorithms, or
seasonal demand.  Finally, our framework estimates the first -stage content -response value of label

 54

configurations under routine deployment conditions. This is the decision layer at which firms first need
causal evidence before reallocating budget, channels, or KOL resources, they must know which label
combinations create engagement value within comparab le creative contexts. A natural extension is to
integrate this first-stage valuation with second-stage allocation decisions. In practice, firms may update
budgets, influencer matching, or channel strategies monthly or quarterly after observing which label
configurations perform well. Future work could therefore combine D -V AE with dynamic allocation
models that jointly optimize label selection and distribution resources over time.
Reference
Arora N, Chakraborty I, Nishimura Y (2025) AI-human hybrids for marketing research: Leveraging
large language models as collaborators. J. Marketing 89(2):43–70.
Besbes O, Gur Y, Zeevi A (2016) Optimization in online content recommendation services: Beyond
click-through rates. Manufacturing Service Oper. Management 18(1):15–33.
Boussioux L, Lane JN, Zhang M, Jacimovic V, Lakhani KR (2024) The crowdless future? Generative
AI and creative problem-solving. Organ. Sci. 35(5):1589–1607.
Caliendo M, Kopeinig S (2008) Some practical guidance for the implementation of propensity score
matching. J. Econom. Surveys 22(1):31–72.
Chen G, Huang L, Xiao S, Zhang C, Zhao H (2024) Attending to customer attention: A novel deep
learning method for leveraging multimodal online reviews to enhance sales prediction. Inform.
Systems Res. 35(2):829–849.
Chen Z, Chan J (2024) Large language model in creative work: The role of collaboration modality
and user expertise. Management Sci. 70(12):9101–9117.
Chernozhukov V, Chetverikov D, Demirer M, Duflo E, Hansen C, Newey W, Robins J (2018)
Double/debiased machine learning for treatment and structural parameters. Econometrics J.
21(1):C1–C68.
Cillo P, Rubera G (2025) Generative AI in innovation and marketing processes: A roadmap of
research opportunities. J. Acad. Marketing Sci. 53(3):684–701.
Conley TG, Hansen CB, Rossi PE (2012) Plausibly exogenous. Rev. Econom. Statist. 94(1):260–272.
Das G, Wiener HJD, Kareklas I (2019) To emoji or not to emoji? Examining the influence of emoji
on consumer reactions to advertising. J. Bus. Res. 96:147–156.
Deng H, Wang W, Li S, Lim KH (2022) Can positive online social cues always reduce user avoidance
of sponsored search results? MIS Quart. 46(1):35–70.
Devlin J, Chang M-W, Lee K, Toutanova K. 2019. BERT: Pre-training of deep bidirectional
transformers for language understanding. Proc. 2019 Conf. North Amer. Chapter Assoc. Comput.
Linguistics: Human Language Technologies, V ol. 1, 4171–4186.

 55

Ellickson PB, Kar W, Reeder JC III (2023) Estimating marketing component effects: Double machine
learning from targeted digital promotions. Marketing Sci. 42(4):704–728.
Esfahani PM, Kuhn D (2018) Data-driven distributionally robust optimization using the Wasserstein
metric: Performance guarantees and tractable reformulations. Math. Programming 171(1–2):115–
166.
Fong C, Grimmer J (2016) Discovery of treatments from text corpora. Proc. 54th Annual Meeting of
Assoc. Comput. Linguistics, (ACL,Berlin, Germany), 1600–1609.
Frost PA (1979) Proxy variables and specification bias. Rev. Econom. Statist. 61(2):323–325.
Geiger A, Wu Z, Potts C, Icard T, Goodman N (2024) Finding alignments between interpretable
causal variables and distributed neural representations. CLeaR, PMLR 236:160–187.
Gioacchini L, Siracusano G, Sanvito D, Gashteovski K, Friede D, Bifulco R, Lawrence C (2024)
AgentQuest: A modular benchmark framework to measure progress and improve LLM agents.
Proc. 2024 Conf. North American Chapter Assoc. Comput. Linguistics: Human Language Tech.,
Demonstrations (Assoc. Comput. Linguistics), 190–200.
Grand View Research (2026) Artificial intelligence prompt marketplace market report. Accessed May
24, 2026, https://www.grandviewresearch.com/industry-analysis/artificial-intelligence-ai-prompt-
marketplace-market-report.
Guo Z, Huang Y, Xiong D (2024) CToolEval: A Chinese benchmark for LLM-powered agent
evaluation in real-world API interactions. Findings ACL 2024 (Assoc. Comput. Linguistics),
15711–15724.
Hartmann J, Exner Y, Domdey S (2025) The power of generative marketing: Can generative AI create
superhuman visual marketing content? Internat. J. Res. Marketing 42(1):13–31.
Holland PW (1986) Statistics and causal inference. J. Amer. Statist. Assoc. 81(396):945–960.
Imai K, Nakamura K (2025) Causal representation learning with generative artificial intelligence:
Application to texts as treatments. Preprint, submitted September 6,
https://arxiv.org/abs/2410.00903.
Kapoor A, Kumar M (2025) Frontiers: Generative AI and personalized video advertisements.
Marketing Sci. 44(4):733–747.
Kingma DP, Welling M (2013) Auto-encoding variational Bayes. Preprint, submitted December 20,
https://arxiv.org/abs/1312.6114.
Komanduri A, Wu Y, Huang W, Chen F, Wu X (2022) SCM-VAE: Learning identifiable causal
representations via structural knowledge. Proc. IEEE Internat. Conf. Big Data (IEEE, Osaka,
Japan), 1014–1023.
Kü nzel SR, Sekhon JS, Bickel PJ, Yu B (2019) Metalearners for estimating heterogeneous treatment
effects using machine learning. Proc. Natl. Acad. Sci. 116(10):4156–4165.
Li P, Tan J, Jabbar A, Icard T, Geiger A (2026) Bucketing the good apples: A method for diagnosing
and improving causal abstraction. Preprint, https://arxiv.org/pdf/2605.02234.

 56

Li X, Sun S, Feng R (2024) Causal representation learning via counterfactual intervention. Proc.
AAAI Conf. Artificial Intelligence 38(4):3234–3242.
Liu H, Tahmasbi A, Haque ES, Jain P (2025) LLMs for customized marketing content generation and
evaluation at scale. Preprint, submitted January 22, https://arxiv.org/abs/2506.17863.
Lou C, Xie Q (2021) Something social, something entertaining? How digital content marketing
augments consumer experience and brand loyalty. Internat. J. Advertising 40(3):376–402.
Ma Y, Melnychuk V, Schweisthal J, Feuerriegel S (2024) DiffPO: A causal diffusion model for
learning distributions of potential outcomes. NeurIPS 37:43663–43692.
Mä rtin C, Bissinger BC, Asta P (2023) Optimizing the digital customer journey: Improving user
experience by exploiting emotions, personas, and situations for individualized user interface
adaptations. J. Consumer Behav. 22(5):1050–1061.
Melnychuk V, Frauen D, Feuerriegel S (2023) Bounds on representation-induced confounding bias
for treatment effect estimation. Preprint, submitted November 19,
https://arxiv.org/abs/2311.11321.
Oster E (2019) Unobservable selection and coefficient stability: Theory and evidence. J. Bus.
Econom. Statist. 37(2):187–204.
Pearl J (2018) The Book of Why: The New Science of Cause and Effect (Basic Books, New York),
27–57.
Qi J, Sarti G, Ferná ndez R, Bisazza A (2024) Model internals-based answer attribution for trustworthy
retrieval-augmented generation. Proc. 2024 Conf. Empirical Methods Natural Language
Processing (Assoc. Comput. Linguistics), 6037–6053.
Quan Y, Li X, Chen Y (2025) CRMAgent: A multi-agent LLM system for e-commerce CRM
message template generation. Preprint, submitted July 11, https://arxiv.org/abs/2507.08325.
Rafieian O, Yoganarasimhan H (2021) Targeting and privacy in mobile advertising. Marketing Sci.
40(2):193–218.
Raghavan A, Bareinboim E (2025) Counterfactual realizability. Preprint, submitted March 14,
https://arxiv.org/abs/2503.11870.
Rao Q, Liu Y, Pan W, Zhong M (2023) BVAE: Behavior-aware variational autoencoder for multi-
behavior multi-task recommendation. Proc. 17th ACM Conf. Recommender Systems (ACM,
Singapore), 625–636.
Reisenbichler M, Reutterer T, Schweidel DA (2026) Applying large language models to sponsored
search advertising. Marketing Sci. 45(1):123–141.
Renze M, Guven E (2024) The effect of sampling temperature on problem solving in large language
models. Findings EMNLP (Assoc. Comput. Linguistics, Miami, FL), 7346–7356.
Shalit L, Johansson FD, Sontag D (2017) Estimating individual treatment effect: generalization
bounds and algorithms. Proc. 34th Int. Conf. Mach. Learn. (PMLR, Sydney, Australia), 3076–
3085.

 57

Shen X, Liu F, Dong H, Lian Q, Chen Z, Zhang T (2022) Weakly supervised disentangled generative
causal representation learning. J. Mach. Learn. Res. 23(241):1–55.
Stanford Institute for Human-Centered AI (2025) AI Index Report 2025. Stanford University,
accessed May 24, 2026, https://aiindex.stanford.edu/report/.
Sun H, Xie P, Sun Y (2025) The inverted L-shaped effect of personalization on consumer attitudes in
AI-generated ads: Striking the right balance between utility and threat. J. Advertising Res.
65(2):237–258.
Trusov M, Ma L, Jamal Z (2016) Crumbs of the cookie: User profiling in customer-base analysis and
behavioral targeting. Marketing Sci. 35(3):405–426.
Wang H, Shimose Y, Takamatsu S (2025) BannerAgency: Advertising banner design with
multimodal LLM agents. Preprint, submitted March 14, https://arxiv.org/abs/2503.11060.
Wang J, Lin X, Qiao R, Foo CS, Low BKH (2024) Helpful or harmful data? Fine-tuning-free Shapley
attribution for explaining language model predictions. Proc. 41st Internat. Conf. Machine Learn.
(PMLR 235), 50960–50991.
Wang L, Huang N, He Y, Liu D, Guo X, Sun Y, Chen G (2025) Artificial intelligence (AI) assistant
in online shopping: A randomized field experiment on a livestream selling platform. Inform.
Systems Res. 36(4), 2358-2374.
Wang Y , Blei DM (2019) The blessings of multiple causes. J. Amer. Statist. Assoc. 114(528):1574–
1596.
Xiao T, Wei H, Chen S (2024) Prominent or subtle: The impact of brand prominence on social media
advertisement engagement. J. Retailing and Consumer Services 80:103897.
Yang M, Liu F, Chen Z, Shen X, Hao J, Wang J (2021) Causal V AE: Disentangled representation
learning via neural structural causal models. Proc. IEEE/CVF Conf. Comput. Vis. Pattern
Recognit. (CVPR), 9593–9602.
Yang Y , Huang B, Qi S, Feng C, Hu H, Zhu Y , Hu J, et al. (2025) Who's the MVP? A game-theoretic
evaluation benchmark for modular attribution in LLM agents. Preprint, submitted February 1,
https://arxiv.org/abs/2502.00510.
Ye Z, Yoganarasimhan H, Zheng Y (2025) LOLA: LLM-assisted online learning algorithm for
content experiments. Marketing Sci. 44(5): 995–1016.
Yoganarasimhan H (2020) Search personalization using machine learning. Management Sci.
66(3):1045–1070.
Zhao X, Fang X, He J, Huang L (2023) Exploiting expert knowledge for assigning firms to industries:
A novel deep learning method. MIS Quart. 47(3):1147–1176.

 58

Online Appendix A: Bound of Confounding effects
In this appendix, we provide a bound to quantify the bias when single confounder is omitted. We first
describe the data -generating process that includes both shared and label -specific unobserved
confounders. Second, we explain how the shared confounder is estimated from label co -occurrence
using Logit-PPCA. Third, we introduce the setup and present Theorem 2, which shows that estimation
bias bound is tight with high probability, ensuring robust causal inference. and we extend this bound to
nonlinear case.  Finally, we discuss the robustness of bound based on Oster’s sensitivity analysis
framework.

1. Data-Generating Process (DGP)
Let (Y, 𝐿, X, C) ∈ ℝ𝑁×{0,1}𝐾 × ℝ𝑇 × ℝ𝑄 satisfy:
𝐿 ∼ ∏ Bernoulli
𝐾
𝑘=1
(𝜎(𝜆𝑘 ⊤𝑒𝑚 + 𝜃𝑘𝑒𝑠,𝑘)) (1𝑎)

𝑌 = 𝛽⊤𝐿 + Γ𝑒𝑚 + Θ⊤𝑒𝑠 + 𝑋𝐿̃⊤ 𝛼 + 𝜌⊤𝐶 + 𝜖 (1𝑏)
where:
• 𝑒𝑚 ∈ ℝ𝐿: unobserved common confounders, 𝑒𝑚 ∼ 𝒩(0, 𝐼𝑀)
• 𝑒𝑠 ∈ ℝ𝐾: unobserved single-treatment confounders, 𝑒𝑠 ∼ 𝒩(0, 𝐼𝐾)
• Λ ∈ ℝ𝐾×𝐿: factor loading matrix, ∥ Λ ∥𝑜𝑝≤ Φ, 𝜆min(Λ⊤Λ) ≥ 𝑐Λ > 0
• Θ = diag(𝛉) ∈ ℝ𝐾×𝐾, 𝛉 = (𝜃1, … , 𝜃𝐾)⊤, ∥ 𝛉 ∥∞≤ 𝜃max
• 𝜎(𝑧) = (1 + 𝑒−𝑧)−1: logistic link function
• 𝑋𝐿̃ ∈ ℝ𝑇, 𝑋𝐿̃ ≔ 𝑋 − proj( 𝑋 ∣ 𝐿 ) = 𝑋 − 𝔼[ 𝑋 ∣ 𝐿 ]
• 𝐶 ∈ ℝ𝑄: observed covariates (controls)
• ϵ ∼ 𝒩(0, τ2), independent of (𝐿, 𝑋, 𝐶, 𝑒𝑚, 𝑒𝑠)
2. Estimation of 𝒆𝒎
Let {𝐿𝑖}𝑖=1 𝑛  be 𝑛 i.i.d. copies of 𝐿. Define the logit-transformed proxy matrix 𝑍 ∈ ℝ𝑛×𝐾:
𝑍𝑖𝑘 = logit(L𝑖𝑘 + 0.5) = logit ( L𝑖𝑘 + 0.5 1 − L𝑖𝑘 + 0.5) ,  𝑖 = 1, … , 𝑛, ; 𝑘 = 1, … , 𝐾. (2)
The add-half correction (+0.5) is applied to both the numerator and denominator of the logit
argument to avoid log0 and is standard in binary data analysis.
Under the DGP (1a), the conditional expectation of the logit is linear:
𝔼[logit( 𝐿𝑘 ∣∣ 𝑒𝑚, 𝑒𝑠 )] = 𝜆𝑘 ⊤𝑒𝑚 + 𝜃𝑘𝑒𝑠,𝑘. (3)
Stacking 𝑛 copies of 𝑒𝑠 into 𝐄𝑠 ∈ ℝ𝑛×𝐿, the ideal (unobserved) logit matrix is:
𝐋𝐌 = 𝐄𝑚Λ⊤ + 𝐄𝑠Θ⊤. (4)
We approximate 𝑍 by dropping the single-treatment term 𝐄𝑠Θ⊤ and modeling the residual as i.i.d.
Gaussian:
𝑍 = 𝐄𝑚Λ⊤ + Ψ, Ψ𝑖𝑘 ∼ i.i.d. 𝒩(0, 𝜎2). (5)
Justification of (5)
• The omitted term 𝐄𝑠Θ⊤ has bounded Frobenius norm: ∥ 𝐄𝑠Θ⊤ ∥𝐹 2≤ 𝑛𝐾𝜃max2 .
• The logit of a Bernoulli random variable with success probability in (0,1) is sub-Gaussian
with variance factor ≤ 4. The add-half correction introduces 𝑂(1) bias, absorbed into 𝜎2.
Apply Probabilistic PCA (PPCA) to 𝑍 via the EM algorithm to obtain Λ̂, 𝜎̂2, and the posterior mean:
𝐄̂𝑚 = 𝑍Λ̂(Λ̂⊤Λ̂ + 𝜎̂2𝐼𝑀)−1. (6)
Let 𝑒̂𝑠,𝑖 ⊤  be the 𝑖-th row of 𝐄̂𝑚.

3. Regression Setup and Bias Decomposition
Let {𝑌𝑖, 𝐿𝑖, 𝑋𝑖, 𝐶𝑖}𝑖=1 𝑛  be i.i.d. samples. Define:
Regression: 𝑌𝑖 = 𝐿𝑖 ⊤𝛽̂ + 𝑒̂𝑚,𝑖 ⊤ Γ̂ + 𝑋̃𝐿𝑖 𝑇 𝛼̂ + 𝐶𝑖 ⊤𝜌̂ + 𝜖̂𝑖, estimator 𝛽̂, 𝑅2 = 𝑅̃

 59

Theorem 2: PAC Guarantee on Effect Estimation Bias Bound
Under the DGP (1a)–(1b), with 𝒆̂𝒔 estimated via Logit-PPCA (6), and assuming:
 𝜆𝑚𝑖𝑛(𝐸[𝑉𝑎𝑟( 𝐿 ∣∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ≥ 𝜆 > 0, then for any 𝜂 ∈ (0,1), there exists a constant 𝑐 =
𝑂 (
Φ∥Γ∥𝐹𝜃max𝜌
𝑐0𝜆2 ) (depending only on the model primitives) such that:
𝑷 (∥ 𝛽̂ − 𝛽 ∥2≤ 𝒄 (𝟏 + √𝐌 𝒏 + √𝐌 𝑲)) ≥ 𝟏 − 𝜼. (9)

Before the formal proof, we need some lemmas.

Lemma 1: Finite-Sample Error Bound for 𝑒̂𝑚

Logit-PPCA Estimation Error: Under the DGP (1a)–(1b) and PPCA estimation (6), for any 𝜂 ∈
(0,1),
𝑃 (1 𝑛 ∥ 𝐄̂𝑚 − 𝐄𝑚 ∥𝐹 2≤ 𝐶 (𝑀 𝑛 + 𝑀 𝐾)) ≥ 1 − 𝜂 (10)
where 𝐶 = 𝑂(Φ2 + 𝜃max2 + 𝜏2) is a universal constant.
Lemma 1 shows that the estimation error of the shared confounder 𝐄̂𝑚 shrinks at a
𝑂(√log(1/𝜂)/𝑛)rate with high probability. This means that with enough historical data, we can
reliably recover the dominant source of confounding. The detailed proof of Lemma 1 is in last part
since it is not the main result.
Bias Decomposition: plim𝑛→∞𝛽̂ = 𝛽 + 𝐵𝑒̂𝑚 + 𝐵𝑒𝑠.We decompose the total bias into two parts to
separate two distinct error sources: (1) the “estimation error” from using an imperfect proxy 𝑬̂𝑚, and
(2) the “omitted-variable bias” from the fundamentally unobserved single-label confounders 𝑬𝑠. This
separation lets us handle them differently: the first vanishes with more data (Lemma2), while the
second is bounded via the characteristic of single confounder (Lemma3).
Lemma 2: Bias from 𝑒̂𝑚 Estimation Error
∥ 𝐵𝑒̂𝑚 ∥2≤
∥𝛤∥𝐹∥𝛬∥𝑜𝑝
𝜆𝑚𝑖𝑛(𝔼[Var( 𝐿∣∣∣𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ⋅ √1 𝑛 ∥ 𝑬̂𝑚 − 𝑬𝑚 ∥𝐹 2. (11)
Proof: The bias arises from the projection of 𝑌 onto 𝐿 after partial control of 𝑒𝑚. The coefficient of
the residual 𝑒̂𝑚 − 𝑒𝑚 is bounded by the signal strength
∥ Γ ∥𝐹∥ Λ ∥𝑜𝑝 and the inverse information matrix.
Lemma 3: Bias from Uncontrolled 𝑒𝑠
∥ 𝐵𝑒𝑠 ∥2≤
∥Θ∥2
𝜆min(𝔼[Var( 𝐿∣∣∣𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ≤ 𝐶𝑠 < ∞. (12)
Proof: The bias from 𝑒𝑠 is the population regression coefficient of 𝐿 on 𝑒𝑠 times ΘT, bounded by
the maximum single-treatment effect. Lemma 3 shows that even though 𝐄𝑠 is omitted, its worst-case
bias is scaled by the fraction of outcome variance left unexplained after controlling for 𝐄̂𝑚. If 𝐄̂𝑚
explains most of the variation, this residual—and thus the potential bias—is small.

 60

Proof of Theorem 2:
Our proof aims to show that both are well-controlled under two high-probability conditions: (1) the
shared confounder 𝑬𝑚  explains a dominant fraction of label co-variation, and (2) the estimated proxy
𝑬̂𝑚 is accurate.
Let ℰ1, ℰ2 be the events defined below. We first show 𝑃(ℰ1 ∩ ℰ2) ≥ 1 − 𝜂, and on this event, the
parameter 𝛽 estimation bias is bounded.
Event ℰ1: Bias from êm Estimation is small and bounded.
ℰ1 = {∥ 𝐵𝑒̂𝑚 ∥2≤ ∥ Γ ∥𝐹∥ Λ ∥𝑜𝑝 𝜆min(𝔼[Var( 𝐿 ∣∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ⋅ √1 𝑛 ∥ 𝐄̂𝑚 − 𝐄𝑚 ∥𝐹 2≤ 𝐶1√𝑀 𝑛 + 𝑀 𝐾} (13)
By Lemma 1 with 𝜂/2, 𝑃(ℰ1) ≥ 1 − 𝜂/2.
Event ℰ2: Sampling error of 𝛽̂ is small.
Let 𝑉 ∈ ℝ𝑛×𝑝 be the design matrix in the regression whose rows consist of(𝐿, 𝐄̂𝑚, 𝑋̃, 𝐶), where
𝑝 ≔  𝐾 + 𝑀 + 𝑇 + 𝑄.
The OLS estimator satisfies:
√𝑛(𝛽̂ − plim𝛽̂) → 𝑑 𝒩(0, (𝑉⊤𝑉)−1𝑉⊤Var(𝜖)𝑉(𝑉⊤𝑉)−1).
The variance is 𝑂(p/𝑛). By sub-Gaussian concentration:
ℰ2 = {∥ 𝛽̂ − plim𝛽̂ ∥2≤ 𝐶2√𝐾 + 𝑀 + 𝑇 + 𝑄 𝑛 } ,  𝑃(ℰ2) ≥ 1 − 𝜂/2. (14)
On ℰ1 ∩ ℰ2:
∥ 𝛽̂ − 𝛽 ∥2≤∥ 𝛽̂ − plim𝛽̂ ∥2 +∥ plim𝛽̂ −  𝛽 ∥2
       ∥ 𝛽̂ − 𝛽 ∥2≤∥ 𝛽̂ − plim𝛽̂ ∥2 +∥ 𝐵𝑒̂𝑚 ∥2 +∥ 𝐵𝑒𝑠 ∥2
Then,
∥ 𝛽̂ − 𝛽 ∥2≤ 𝐶1√𝑀 𝑛 + 𝑀 𝐾 + 𝐶2√𝐾 + 𝑀 + 𝑇 + 𝑄 𝑛 + 𝐶𝑠  ≤  c√𝑀 𝑛 + 𝑀 𝐾
By union bound: 𝑃(ℰ1 ∩ ℰ2) > 1 − 𝜂. Thus, Theorem 2 holds.
4. Nonlinear Settings
We now extend Theorem 2 and the bias bound to arbitrary nonlinear outcome models, including
neural networks. The linear specification 𝑌 = 𝛽⊤𝐿 + Γ𝑒𝑚 + Θ⊤𝑒𝑠 + 𝑋𝐿̃⊤ 𝛼 + 𝜌⊤𝐶 + 𝜖 is replaced by
a general structural equation
𝑌 = 𝑓(𝐿, 𝑒𝑚, 𝑋𝐿̃, 𝐶; 𝛽) + ϵ,

 61

where𝑓: ℝ𝑀+𝐾+𝑄+𝑇 → ℝ𝑃 is a nonlinear function of any form (e.g., a deep feed-forward neural
network with parameters 𝛽 ∈ ℝ𝐾, ϵ ∼ 𝑁(0, τ^2) independent of all other variables, and  𝛽 contains
the causal parameters of interest (for example, the weights on the 𝐿-input layer or the average
marginal effect 𝔼[∂𝑓/ ∂𝐿]). We assume f belongs to a function class ℱ that is Lipschitz continuous
with respect to its inputs with (data-dependent) Lipschitz constant 𝐿𝑓 < ∞ (this holds for standard
neural networks with bounded weights and Lipschitz activations such as ReLU, tanh, or sigmoid).
The estimator is now the M-estimator (empirical risk minimizer)
𝛽̂ = arg min
𝛽∈Β
1
𝑛 ∑ ℒ (𝑌𝑖, 𝑓(𝐿𝑖, 𝑒𝑚,𝑖̂ , 𝑋𝐿𝑖̃ , 𝐶𝑖; 𝛽))
𝑛
𝑖=1
,
where ℒ is a convex loss (e.g., squared error for regression, cross-entropy for classification) and
em̂  is still the Logit-PPCA proxy from (6). Let 𝛽∗ be the population minimizer under the true
confounders (𝑒𝑚, 𝑒𝑠). The goal is to bound the estimation error ||𝛽̂ − 𝛽∗||
Generalized bias decomposition
Under standard regularity (the population objective is strongly convex or satisfies a restricted strong
convexity condition with curvature λ𝑚𝑖𝑛 > 0 we have the population-level decomposition
plim𝑛→∞𝛽̂ = 𝛽∗ + 𝐵𝑒𝑚̂ + 𝐵𝑒𝑠,
where 𝐵𝑒𝑚̂  is the bias induced by the proxy estimation error 𝑒𝑚̂ − 𝑒𝑚, 𝐵𝑒𝑠 is the omitted-variable
bias from the unobserved single-label confounders 𝑒𝑠.
Lemma 2' (Nonlinear bias from 𝑒𝑚̂ error)
||𝐵𝑒𝑚̂ || ≤ 𝐿𝑓 ⋅ ||Γ||eff ⋅ 1 λ𝑚𝑖𝑛(𝔼[Var( 𝐿 ∣∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ⋅ √1 𝑛 ||𝐸𝑚̂ − 𝐸𝑚||𝐹 2
where ||Γ||eff is the effective loading of the shared confounder in the nonlinear map 𝑓 (replaces
||Γ||F in the linear case; for a neural network it is bounded by the product of layer norms). The proof
follows from the mean-value theorem applied to the first-order condition of the M-estimator: the
gradient of the loss with respect to the confounder input is bounded by 𝐿𝑓.
Lemma 3' (Nonlinear bias from uncontrolled 𝑒𝑠 )
||𝐵𝑒𝑠|| ≤ 𝐿𝑓 ⋅ ||Θ||2 λ𝑚𝑖𝑛(𝔼[Var( 𝐿 ∣∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) ≤ 𝐶𝑠′ < ∞.
The proof is identical to Lemma 3, replacing the linear coefficient by the Lipschitz constant of 𝑓
w.r.t. the 𝑒𝑠 input.)
Sampling error of the nonlinear estimator
Under standard conditions for empirical risk minimization (e.g., the loss ℒ is Lipschitz and the
function class ℱ has bounded Rademacher complexity or covering number), the estimation error
around the population limit satisfies
∥ 𝛽̂ − plim𝛽̂ ∥= 𝑂𝑝 (√𝑑eff 𝑛 ),

 62

where 𝑑eff is the effective dimension of the neural network (e.g., number of parameters times a
logarithmic factor for overparameterized nets; see). This is the direct nonlinear analogue of the sub-
Gaussian OLS bound (14).
Using Lemmas 2' and 3' for the bias terms and the NN generalization bound for the sampling error.
Lemma 1 (proxy error ∥ 𝐸𝑚̂ − 𝐸𝑚 ∥𝐹) continues to hold unchanged because it depends only on the
label co-occurrence model (Logit-PPCA), not on the outcome 𝑓. The total error is
∥ 𝛽̂ − 𝛽∗ ∥≤∥ 𝛽̂ − plim𝛽̂ ∥ +∥ 𝐵𝑒𝑚̂ ∥ +∥ 𝐵𝑒𝑠 ∥
                                       ≤ 𝐶1 ′√𝑀 𝑛 + 𝑀 𝐾 + 𝐶2 ′√𝑑eff/n + 𝐶𝑠′ ≤ 𝑐′√𝑀 𝑛 + 𝑀 𝐾 ,
where the 𝑂(√𝑑eff/n) term is absorbed into the leading rate because 𝑑eff is treated as fixed or
grows slower than 𝑛 (standard in high-probability NN bounds). Thus, in nonlinear cases:
ℙ (||𝛽̂ − 𝛽∗|| ≤ 𝑐′(1 + √𝑀/n + √𝑀/K)) ≥ 1 − η.
For a feed-forward NN with D layers, ReLU activations, and bounded weights (spectral norm ≤ G
per layer), the Lipschitz constant satisfies 𝐿𝑓 ≤ 𝐺𝐷. The effective dimension 𝑑𝑒𝑓𝑓 can be taken as
𝑂(width × depth × log 𝑛) under overparameterization. The same rate √𝑀/n + M/K is preserved;
the only change is that the universal constant 𝑐′ now scales with the network depth and width (still
independent of sample size 𝑛).

5. Robustness Check on Bias Bound

This section provides a detailed robustness analysis of the PAC guarantee on the estimation bias bound
in Theorem 2 (and its nonlinear extension to M-estimators). The baseline result shows that ||β̂ − β||2
is controlled at rate 𝑂(√𝑀/n + √𝑀/K) with high probability whenever the shared confounder 𝑒𝑠
dominates the label -specific confounder  𝑒𝑠 (i.e., ||Γ||𝐹 ≫ ||Θ||2 , θ𝑚𝑎𝑥 small, and
λ𝑚𝑖𝑛(𝔼[Var( 𝐿 ∣∣ 𝑒𝑚, 𝑒𝑠, 𝑋𝐿̃, 𝐶 )]) > 0.  In practice, however, real datasets may exhibit moderate
violations of this dominance assumption—label-specific confounding may be stronger than anticipated
because of unobserved heterogeneity across treatments or imperfect label co -occurrence patterns
captured by Logit-PPCA. The purpose of this robustness check is twofold: (i) to quantify the maximum
allowable deviation from 𝑒𝑚 ≫ 𝑒𝑠 before the PAC bound ceases to be informative for causal inference,
and (ii) to give applied researchers a transparent, computable diagnostic that can be reported directly
from the fitted Logit-PPCA output and the outcome regression.
To achieve this, we embed the original bias decomposition 𝑝𝑙𝑖𝑚β̂ = β + 𝐵𝑒𝑚̂ + 𝐵𝑒𝑠  into the
coefficient-stability framework of Oster (2019), while imposing distributional robustness via a
Wasserstein ball around the reference distribution that embodies “𝑒𝑚 dominates 𝑒𝑠”. This combination
inherits the intuitive interpretation of Oster’s δ while accommodating the high-dimensional, possibly
nonlinear nature of our multi -dimensional treatment 𝐿 ∈ {0,1}𝐾  and the M-estimator used in the
nonlinear extension.

Uncontrolled Regression: 𝑌𝑖 = 𝐿𝑖 ⊤𝛽 + +𝑋̃𝐿𝑖 𝑇 α + 𝐶𝑖 ⊤𝜌 + ϵ𝑖,
estimator 𝛽uncontrolled,   𝑅2 = 𝑅uncontrolled(or pseudo − 𝑅2 based on the empirical loss)

 63

Controlled Regression: 𝑌𝑖 = 𝐿𝑖 ⊤𝛽 + 𝑒̂𝑚,𝑖 ⊤ Γ + 𝑋̃𝐿𝑖 𝑇 α + 𝐶𝑖 ⊤𝜌 + ϵ𝑖, estimator β ̃, 𝑅2 = 𝑅̃
Let 𝑃0 be the reference distribution that embodies the “equal selection” benchmark 𝛿 = 1.0 .
Specifically, 𝑃0 is defined as the distribution under which the relative confounding strength satisfies
𝛿(𝑃0) = Cov(𝐿, 𝑒𝑠 ∣ 𝑃0) Cov(𝐿, 𝑒̂𝑚) = 1,
while the absolute magnitude of the label-specific confounder remains small: 𝑒𝑠 ∼ 𝒩(0, 𝜎𝑠2𝐼𝐾)with
𝜎𝑠2(equivalently 𝜃max) sufficiently small that the shared loading matrix Γstill explains the dominant
fraction of label co-variation. In other words, 𝑃0 corresponds to a scenario in which the selection on
the unobserved single-treatment confounder 𝑒𝑠 is equal in relative strength to the selection on the
observable Logit-PPCA proxy 𝑒̂𝑚, after proper normalization by the variance explained by 𝑒̂𝑚. This
normalization ensures that 𝛿 = 1 is a meaningful and internally consistent benchmark even when the
raw scale of 𝑒𝑠 is kept modest.
We then consider all possible confounding distributions 𝑃 that lie inside the Wasserstein-2 ball of
radius 𝜀 ≥ 0 around this reference:  𝒫𝜀 = {𝑃: 𝑊2(𝑃, 𝑃0) ≤ 𝜀}.
The Wasserstein-2 distance is chosen because it provides a natural, nonparametric way to bound how
far the true distribution of unobservables can deviate from the dominance assumption without requiring
strong parametric restrictions on 𝑒𝑠.
Invert Oster’s formula to obtain the observed selection ratio
𝛿̂obs = 𝑅̃−𝑅uncontrolled 𝑅𝑚𝑎𝑥−𝑅uncontrolled  ,
This measures the fraction of additional explained variation attributable to the Logit-PPCA proxy (the
“observable” shared confounding) relative to the maximum possible. Under the reference distribution
𝑃0 (equal selection δ=1), we expect this ratio to be close to 1 after appropriate normalization; any
deviation quantifies violation of the dominance assumption 𝑒𝑚 ≫ 𝑒𝑠. We then set the Wasserstein
ball radius as
𝜀 =∣ 𝛿̂obs − 1.0 ∣.
For any 𝑃 ∈ 𝒫ε, define the effective selection ratio
δ(𝑃) = Cov(𝐿, 𝑒𝑠∣∣𝑃 ) Cov(𝐿,𝑒𝑚̂ ) ,
which is the direct multivariate analogue of Oster’s scalar δ  (the relative degree of selection on
unobservables versus observables). The bias -adjusted effect (marginal effect in the nonlinear case)
under distribution 𝑃 then takes the Oster-style closed form
βadj(𝑃) = β̃ + δ(𝑃) ⋅ β̃ − βuncontrolled 𝑅̃(𝑃) − 𝑅uncontrolled ⋅ (𝑅𝑚𝑎𝑥(𝑃) − 𝑅̃(𝑃)),
where 𝑅̃(𝑃)  is the effective 𝑅2  (or pseudo-𝑅2 ) evaluated under 𝑃 , and 𝑅𝑚𝑎𝑥(𝑃) = Π ⋅ 𝑅̃(𝑃) with
Π ∈ [1.25,2] to allow for residual idiosyncratic variation or measurement error in the outcome. In the
nonlinear M-estimator setting, the formula continues to hold after replacing the linear projection
coefficients by the appropriate Lipschitz-bounded gradients of the loss function (see Lemma 2').
The worst-case identified set for the causal parameter is therefore
[β𝐿, β𝑈] = [ inf 𝑃∈𝒫ε βadj(𝑃) , sup 𝑃∈𝒫ε βadj(𝑃)].
When ε = 0 (perfect dominance), this set collapses exactly to the original PAC interval of Theorem 2.

 64

For ε > 0, the width of the identified set grows linearly in ε because the M-estimator loss is Lipschitz
continuous and the Wasserstein distance admits a Kantorovich dual representation; nevertheless, under
the maintained condition λ𝑚𝑖𝑛 > 0 , the width remains bounded by 𝑂(√𝑀/n + √𝑀/K + ε) . This
explicit rate makes transparent the tradeoff between sample size, dimension, and the degree of allowable
violation of the dominance assumption.
To incorporate prior beliefs about the plausibility of different values of δ (i.e., how strongly 𝑒𝑚 still
dominates 𝑒𝑠), we follow the three complementary strategies of Conley et al. (2008) for “plausibly
exogenous” instruments:
1. Support restriction: δ ∈ [0, δ𝑚𝑎𝑥]  with δ𝑚𝑎𝑥 = θ𝑚𝑎𝑥/||Γ||𝐹 . The identified set is the union of
Oster-style intervals over this support.
2. Distributional prior: δ ∼ 𝒩+(0, σδ 2) (half-normal with mean zero and exponentially decaying tails),
where σδ is calibrated from the ratio of residual label -specific variance (after extracting 𝑒𝑠̂ ) to the
explained shared variance. This prior directly encodes the belief that extreme violations are increasingly
unlikely.
3. Beta-dependent prior: δ(β) = 𝑓(||β||), allowing the relative strength of confounding to depend on
the magnitude of the causal effect itself (convenient in the full Bayesian implementation).
Diagnostic test for violation of the dominance assumption
After fitting Logit-PPCA and the outcome regression, compute the PAC radius
𝑟PAC = 𝑐(1 + √𝑀/n + √𝑀/K)
directly from Theorem 2 (with universal constant c as defined there). The original PAC bound is deemed
non-informative (and cannot be trusted for causal claims) if the worst -case identified set
[β𝐿, β𝑈]violates the PAC guarantee in a statistically meaningful way. Formally, this occurs if
𝑤𝑖𝑑𝑡ℎ(β𝑈 − β𝐿) > 2𝑟PAC
or if the entire identified set[𝛽𝐿, 𝛽𝑈] lies outside the PAC interval centered at 𝛽̃ with radius 𝑟PAC.

Detailed Proof of Lemma 1
We split the error into three controllable parts:
∥ 𝐄̂𝑚 − 𝐄𝑚 ∥𝐹 2 = ∥ 𝐄𝑚Λ⊤ − 𝐋𝐌 ∥𝐹 2
⏟
(i) omitted 𝑒𝑠
 + ∥ 𝐋𝐌 − 𝑍 ∥𝐹 2
⏟
(ii) logit noise
 + ∥ 𝑍 − 𝐄̂𝑚Λ⊤ ∥𝐹 2
⏟
(iii) PPCA error
.
The claim follows by bounding each term with high probability and applying the union bound.
(i) Omitted single-treatment term
By (4) the ideal logit matrix is 𝐋𝐌 = 𝐄𝑚Λ⊤ + 𝐄𝑠Θ⊤.
Hence
∥ 𝐄𝑚Λ⊤ − 𝐋𝐌 ∥𝐹 2=∥ 𝐄𝑠Θ⊤ ∥𝐹 2= ∑ ∑(
𝐾
𝑘=1
𝑛
𝑖=1
𝜃𝑘𝑒𝑠,𝑖,𝑘)2 ≤ 𝜃max2 ∑ ∥
𝑛
𝑖=1
𝑒𝑠,𝑖 ∥2 2.
Because 𝑒𝑠,𝑖 ∼ 𝒩(0, 𝐼𝐾) independently,
1
𝑛 ∑ ∥
𝑛
𝑖=1
𝑒𝑠,𝑖 ∥2 2= 𝐾 + 𝑂𝑝(√𝐾).
Thus

 65

1
𝑛   ∥ 𝐄𝑚Λ⊤ − 𝐋𝐌 ∥𝐹 2≤ 𝜃max2 𝐾 + 𝑂𝑝(√𝐾) = 𝑂(1)
with probability 1 (deterministic bound up to an 𝑂𝑝(√𝐾/𝑛) term that vanishes).
(ii) Logit-transformation noise
For a single entry, let 𝑝𝑖𝑘 = 𝜎(𝜆𝑘 ⊤𝑒𝑚,𝑖 + 𝜃𝑘𝑒𝑠,𝑖,𝑘).
The true conditional logit is
ℓ𝑖𝑘 ≡ logit(𝑝𝑖𝑘) = 𝜆𝑘 ⊤𝑒𝑚,𝑖 + 𝜃𝑘𝑒𝑠,𝑖,𝑘.
The observed proxy is
𝑍𝑖𝑘 = logit(𝐿𝑖𝑘 + 0.5).
Define the noise 𝜓𝑖𝑘 = 𝑍𝑖𝑘 − ℓ𝑖𝑘. We show that 𝜓𝑖𝑘 is sub-Gaussian with variance factor 𝜎𝜓 2 ≤
4.
• Bounded support after add-half:
𝐿𝑖𝑘 + 0.5 ∈ [0.5,1.5], so 𝑍𝑖𝑘 ∈ [logit(0.5), logit(1.5)] = [0,1] almost surely.
Hence |𝜓𝑖𝑘| ≤ 2+∥ ℓ𝑖𝑘 ∥∞.
The term ∥ ℓ𝑖𝑘 ∥∞≤∥ Λ ∥𝑜𝑝∥ 𝑒𝑚 ∥2+ 𝜃max ∥ 𝑒𝑠 ∥2≤ Φ√𝑀 + 𝜃max√𝐾 with probability 1
(Gaussian tail).
  The bounded bias from the add-half correction contributes at most 𝑂(𝑛𝐾) to the Frobenius
norm of the error. After dividing by 𝑛, this becomes 𝑂(𝐾). Since 𝐾 is fixed (𝐾 << 𝑛), the
term 𝑂(𝐾) is a constant with respect to the sample size 𝑛. In the final error bound, this
constant is absorbed into the universal constant.
• Sub-Gaussian tail for the stochastic part:
Conditional on (𝑒𝑚, 𝑒𝑠), 𝐿𝑖𝑘 ∼ Bernoulli(𝑝𝑖𝑘).
The random variable logit(𝐿𝑖𝑘 + 0.5) − ℓ𝑖𝑘 is a function of a single Bernoulli draw.
A bounded function of a Bernoulli is sub-Gaussian with variance factor at most 4.
Hence 𝜓𝑖𝑘 ∼
cond
sub-G(𝜎𝜓 2) with 𝜎𝜓 2 ≤ 4.
• Unconditional concentration:
By the sub-Gaussian maximal inequality
𝑃 ( 1 𝑛𝐾 ∑ 𝜓𝑖𝑘 2
𝑖,𝑘
  ≥  4 + 𝑡)   ≤  2exp(−𝑛𝐾𝑡/8).
Choosing 𝑡 = 8log(2/𝜂)/(𝑛𝐾) yields
𝑃 (1 𝑛   ∥ 𝐋𝐌 − 𝑍 ∥𝐹 2 ≥  4𝐾 + 8𝐾log(2/𝜂) 𝑛 )   ≤  𝜂.
The term 4𝐾 contributes 𝑂(𝐾/𝑛) to the normalized error, which is dominated by the 𝑂(𝐿/𝐾)
identification term in the final bound when 𝑛 ≫ 𝐾2/𝐿. The logarithmic term 𝑂(𝐾log(1/𝜂)/𝑛)
vanishes as 𝑛 → ∞, hence 𝑜(1).

 66

(iii) PPCA estimation error on the perturbed model
Conditional on the realized 𝑍, the working model is the exact linear factor model
𝑍 = 𝐄𝑚Λ⊤ + Ψ,  Ψ𝑖𝑘 ∼ i.i.d. 𝒩(0, 𝜎2).
Let 𝐄̂𝑚 (oracle) be the PPCA posterior mean when Λ, 𝜎2 are known.
A standard result for Gaussian factor models states that, for any 𝜂 > 0,
𝑃 (1 𝑛   ∥ 𝐄̂𝑚 (oracle) − 𝐄𝑚 ∥𝐹 2 ≤   𝐶oracle (𝑀 𝑛 + 𝑀 𝐾))   ≥  1 − 𝜂,
with 𝐶oracle = 𝑂(∥ Λ ∥𝑜𝑝2 + 𝜎2) = 𝑂(Φ2 + 𝜎2).
The estimated 𝐄̂𝑚 differs from the oracle only because Λ̂, 𝜎̂2 are obtained by EM.
The EM algorithm for PPCA converges to the MLE at the parametric rate.
By a uniform deviation argument on the likelihood, the estimation error satisfies
∥ Λ̂ − Λ ∥𝑜𝑝= 𝑂𝑝 (√𝐾𝑀 𝑛 ) ,  |𝜎̂2 − 𝜎2| = 𝑂𝑝 (√𝐾 𝑛).
These rates are faster than the 𝑂(𝑀/𝑛 + 𝑀/𝐾) target, so the additional error introduced by
plugging Λ̂, 𝜎̂2 into the posterior mean formula is
∥ 𝐄̂𝑚 − 𝐄̂𝑚 (oracle) ∥𝐹 2= 𝑂𝑝 (𝐾𝑀2 𝑛 + 𝑀𝐾 𝑛 ) = 𝑂 (𝑀 (𝑀 𝑛 + 𝐾 𝑛)).
Dividing by 𝑛 gives an 𝑂(𝑀/𝑛 + 𝑀/𝐾) term that is absorbed into the same constant.
Define the events
ℰ1 = {1 𝑛 ∥ 𝐄𝑚Λ⊤ − 𝐋𝐌 ∥𝐹 2≤ 𝐶𝑠} ,  ℰ2 = {1 𝑛 ∥ 𝐋𝐌 − 𝑍 ∥𝐹 2≤ 𝐶𝜓} ,  
ℰ3 = {1 𝑛 ∥ 𝐄̂𝑚 − 𝐄𝑚 ∥𝐹 2≤ 𝐶ppca (𝑀 𝑛 + 𝑀 𝐾)}.
From (i)–(iii) we have 𝑃(ℰ1) = 1, 𝑃(ℰ2) ≥ 1 − 𝜂/2, 𝑃(ℰ3) ≥ 1 − 𝜂/2.
On ℰ1 ∩ ℰ2 ∩ ℰ3,
1
𝑛 ∥ 𝐄̂𝑚 − 𝐄𝑚 ∥𝐹 2≤ 𝐶𝑠 + 𝐶𝜓 + 𝐶ppca (𝑀 𝑛 + 𝑀 𝐾) ≤ 𝐶 (𝑀 𝑛 + 𝑀 𝐾),
where 𝐶 = max{𝑛/𝐶𝑠, 𝑛/𝐶𝜓, 𝐶ppca} is finite and depends only on Φ, 𝜃max, 𝜏.
By the union bound, 𝑃(ℰ1 ∩ ℰ2 ∩ ℰ3) ≥ 1 − 𝜂. This concludes the proof of (10).

Online Appendix B: Counterfactual Process Details
1. Intervention Setup & Label Configuration
We conduct a targeted counterfactual intervention on the semantic label space of the “Carslan Little
Mix Cat Foundation” campaign by activating the "Date-Ready" label (𝐿13) while holding all other
labels unchanged. The label configuration is as follows:
• Original Label Set (15 active labels):

 67

Lightweight, Hydrating, Breathable, Coverage, Oil-Control, Even Skin Tone, Skin-Nourishing; Daily
Use, Commute-Friendly; Student, Beauty Enthusiast, Dry/Combination Skin; Plant Extracts, Co-
Branding Campaign, New Design
• Intervened Label Set: "Dating-Ready" (𝐿13 = 1)explicitly activated.
2. Latent Space (𝒁𝑳) Propagation & Dimensional Shifts
The intervention directly perturbs the label-aligned latent representation Z𝐿 ∈ ℝP. Through the
learned causal adjacency matrix A, this perturbation induces structured shifts across specific latent
dimensions. Table B.1 reports the 10 dimensions with the largest absolute changes (∣ Δ𝑧 ∣), capturing
how the intervention rewires the semantic representation.
Table B.1 Latent Space (𝑍𝐿) Intervention Changes
Dim. Index  Original Value Δ𝑧 Direction Interpreted Semantic Role
21  0.0952 -0.1562 Suppressed Routine commute / baseline context
56  0.0460 -0.1299 Suppressed Pure functional / utilitarian focus
71  -0.0667 +0.1227 Activated Social/romantic scenario cue
15  -0.0572 +0.1173 Activated Emotional appeal / charm
23  -0.0065 -0.1153 Suppressed Neutral product specification
1  0.0010 +0.1081 Activated Scenario transition marker
36  0.0174 +0.1063 Activated Lifestyle integration cue
30  0.0449 -0.1054 Suppressed Baseline functional trait
66  0.0110 -0.0990 Suppressed Contextual down-weight
14  0.0591 -0.0981 Suppressed Generic engagement trigger

Activating 𝐿13induces a clear semantic pivot in 𝐙𝐿. Dimensions encoding romantic/social contexts
and emotional value (Dims 71, 15, 1, 36) are activated, while those tied to routine functionality and
neutral specifications (Dims 21, 56, 23, 30, 66) are suppressed. This confirms that the interaction
graph 𝐀 successfully routes the label intervention into a coherent latent reconfiguration, effectively
shifting the representation from a utility-driven to a scenario-driven mode without destabilizing
unrelated features.
3. Reverse Mapping: From Text Back to Latent Shifts
To validate interpretability, we perform a post-hoc analysis mapping textual adaptations back to latent
dimensional changes: (1) Newly emphasized phrases ("date-night", "boosts complexion",
"likeability") align with activated dimensions (71, 15, 1, 36), confirming these dimensions encode
social/romantic contextual cues. (2) Downplayed functional emphasis (reduced focus on "8-hour
wear" as the sole selling point) aligns with suppressed dimensions (21, 56, 23), confirming these
encode routine/utilitarian traits. (3) Preserved core messaging (lightweight texture, creamy finish,
suitability for combination skin) remains stable, reflecting unchanged dimensions in 𝐙𝐿.

 68

Online Appendix C: D-VAE Algorithms
Algorithm 1: Probabilistic Factor Model for Deconfounder

Input：
 𝐿: 𝑛 × 𝐾 matrix of assigned causes (𝑛 individuals, 𝐾 causes),𝑌: 𝑛 × 𝑁 matrix of
outcomes,𝑀: Dimension of common confounder 𝑒𝑚
Output：
 𝐸̂𝑚: 𝑛 × 𝑀 matrix of estimated common confounders (𝑒𝑠)
Procedure:
Repeat
1. Model Specification:
For each individual 𝑖 ∈ {1, . . . , 𝑛} and cause 𝑗 ∈ {1, . . . , 𝐾}, define:
𝐿[𝑖, 𝑗] ∼ Bernoulli(𝜎(𝜃𝑗 ⊤ ⋅ 𝑒𝑚[𝑖]))
where 𝜎(𝑥) =
1
1+𝑒−𝑥, 𝑒𝑚[𝑖] ∼ 𝒩(0, Λ𝑐) (Λ𝑐 ∈ ℝ𝑀×𝑀), 𝜃𝑗 ∈ ℝ𝑀.
2. Parameter Estimation:
Maximize ELBO for variational inference to estimate {𝜃̂𝑗}𝑗=1 𝐾  and Λ̂𝑐:
ℒcommon = ∑ ∑ 𝔼𝑞(𝑒𝑚[𝑖]|L)
𝐾
𝑗=1
𝑛
𝑖=1
[log𝑝(L[𝑖, 𝑗]|𝑒𝑚[𝑖], 𝜃𝑗)] − 𝐷KL(𝑞(𝑒𝑚[𝑖]|𝐿)||𝑝(𝑒𝑚[𝑖]))
where 𝑝(L[𝑖, 𝑗]|𝑒𝑚[𝑖], 𝜃𝑗) = [𝜎(𝜃𝑗 ⊤𝑒𝑚[𝑖])]𝐿[𝑖,𝑗][1 − 𝜎(𝜃𝑗 ⊤𝑒𝑚[𝑖])]1−L[𝑖,𝑗], 𝑝(𝑒𝑚[𝑖]) =
𝒩(0, Λ𝑐), 𝑞(𝑒𝑚[𝑖]|𝐿) = 𝒩(𝜇𝑖 𝑐, Σ𝑖 𝑐).
3. Predictive Check:
3.1 Hold out subset of causes per individual: 𝐿𝑖,held, 𝐿𝑖,obs.
3.2 Fit model to {𝐿𝑖,obs}𝑖=1 𝑛 , obtain 𝑝(𝑒𝑚[𝑖]|𝐿𝑖,obs).
3.3 Sample replicated 𝐿𝑖,held rep ∼ ∫ 𝑝(𝐿𝑖,held|𝑒𝑚𝑐 [𝑖])𝑝(𝑒𝑚[𝑖]|𝐿𝑖,obs)𝑑𝑒𝑚[𝑖].
3.4 Compute discrepancy: 𝑡(𝐿𝑖,held) = 𝔼𝑒𝑠𝑐[log𝑝(𝐿𝑖,held|𝑒𝑠[𝑖])|𝐿𝑖,obs].
3.5 Predictive score = 𝑝(𝑡(𝐿𝑖,held rep ) < 𝑡(𝐿𝑖,held)).
until predictive score is satisfactory
foreach individual 𝑖 do 𝑒̂𝑚[i] = 𝔼[𝑒𝑚[𝑖]|𝐿𝑖] = 𝜇𝑖 𝑐.
Return 𝐸̂𝑚 = {𝜇𝑖 𝑐}𝑖=1 𝑛 .

 69

Algorithm 2: D-VAE Training Procedure
Input:
Marketing text 𝑋, labels 𝐿 ∈ {0,1}𝐾, environment variables 𝐶 ∈ ℝ𝑄, interaction metrics
𝑌 ∈ ℝ𝑁; pre-computed common confounder 𝐸̂𝑚 ∈ ℝ𝑛×𝑀 ; hyperparameters about loss
weight: 𝜆1, 𝜆2, 𝜆3, 𝜆4, 𝜆5, 𝜆6, 𝜆7.
Output:
Reconstructed embeddings 𝑒̂𝑋 ∈ ℝ𝐿𝑚𝑎𝑥×𝑇, predicted interactions 𝑒̂𝑌 ∈ ℝ𝑁, generated text
(inference).
Procedure:
1. Preprocess Data:
1.1 Encode 𝑋 using Qwen-3: 𝑒𝑋 ∈ ℝ𝐿𝑚𝑎𝑥×𝑇, 𝑡𝑜𝑘𝑒𝑛𝑋 ∈ ℤ𝐿𝑚𝑎𝑥.
1.2 Decompose 𝐿 into one-hot vector: 𝑒𝐿 ∈ ℝ𝐾.
1.3 Normalize 𝐸: 𝑒𝐸 ∈ ℝ𝑄; normalize 𝑌: 𝑒𝑌 ∈ [0,1]𝑁.
1.4 Concatenate: 𝑒𝑖𝑛𝑝𝑢𝑡 = [𝑒𝑋, 𝑒𝐿, 𝑒C, 𝑒𝐸𝑚] ∈ ℝ𝐿𝑚𝑎𝑥×(𝑇+𝐾+Q+𝑀).
2. Encode to Latent Space:
2.1 Transformer encoder on 𝑒𝑖𝑛𝑝𝑢𝑡: Compute 𝜇𝑍, log𝜎𝑍 2 ∈ ℝ𝐿𝑚𝑎𝑥×𝑑𝑧.
2.2 Conditional prior with confounders:
Compute 𝜇𝐿,𝐸,conf, log𝜎𝐿,𝐸,conf 2 = MLP([𝑒𝐿, 𝑒C, 𝑒𝐸𝑚]), broadcast to ℝ𝐿𝑚𝑎𝑥×𝑑𝑧.
2.3 Reparameterize: 𝑍0 = 𝜇𝑍 + 𝜎𝑍 ⊙ 𝜖, 𝜖 ∼ 𝒩(0, 𝐼); split 𝑍𝑒 = [𝑍𝑒,L, 𝑍extra],
𝑍𝑒,L ∈ ℝ𝐿𝑚𝑎𝑥×𝐾.
3. Apply Causal Layer:
3.1 For each token 𝑖 in 𝑍𝑒,𝐿, 𝐴 ∈ ℝ𝐾×𝐾 is the learnable adjacent matrix of 𝑍𝐿,
then update:
𝑧𝑖,𝑗 = 𝑓𝑗 (∑ 𝐴𝑗𝑘
𝐾
𝑘=1
⋅ 𝑧𝑒𝑖,𝑘, 𝜖𝑖,𝑗; 𝜃𝑗)
3.2 Concatenate: 𝑍 = [𝑍𝐿, 𝑍𝑒𝑥𝑡𝑟𝑎] ∈ ℝ𝐿𝑚𝑎𝑥×𝑑𝑧.
4. Decode Outputs:
4.1 Text branch: Transformer decoder on 𝑍: 𝑒̂𝑋 ∈ ℝ𝐿𝑚𝑎𝑥×𝑇.
4.2 Interaction branch: MLP on 𝑍: 𝑒̂𝑌 ∈ ℝ𝑃.
4.3 Label supervision: 𝑒̂𝐿 = 𝑔(𝑍𝐿).
5. Compute Counterfactual Loss:
Call Counterfactual Forward (Algorithm 3) to compute ℒ𝑐𝑎𝑢𝑠𝑎𝑙.
6. Compute Other Losses:
6.1 Reconstruction: ℒ𝑋 = ||𝑒𝑋 − 𝑒̂𝑋||2 2.
6.2 Prediction: ℒ𝑌 = ||𝑒𝑌 − 𝑒̂𝑌||2 2.
6.3 KL Divergence: ℒKL = 𝐷KL(𝑞(𝑍|𝑒𝑖𝑛𝑝𝑢𝑡)||𝑝(𝑍|𝑒𝑈, 𝑒𝐸𝑐, 𝑒𝐸𝑠)).
6.4 DAG Constraint: ℒDAG = tr(𝑒𝐴⋅𝐴𝑇 ) − 𝐾.
6.5 Sparse Regularization: ℒsparse = ||𝐴||1.
6.6 Label Supervision: ℒlabel = ||𝑔(𝑍L) − 𝑒𝐿||2 2.
7. Optimize:
7.1 Compute Total loss:
 ℒ = 𝜆1ℒ𝑋 + 𝜆2ℒ𝑌 + 𝜆3ℒKL + 𝜆4ℒDAG + 𝜆5ℒsparse + 𝜆6ℒlabel + 𝜆7ℒcausal
7.2 Backpropagate and update parameters via Adam.
8. Inference/Generation:
8.1 Mix embeddings: 𝑒𝑋,mixed = 𝛼𝑒̂𝑋 + (1 − 𝛼)𝑒𝑋,raw.
8.2 Qwen-3 to generate new token id sequence then decode to text.
8.3 For causal attribution: Intervene on interested 𝑈𝑗, compute individual effect
based on interaction difference.

 70

Algorithm 3: Counterfactual Forward (Intervention and Debiasing)
Input:
Labels 𝑒𝐿 ∈ ℝ𝐾, environment 𝑒C ∈ ℝ𝑄, common confounders 𝑒𝐸𝑚 ∈ ℝ𝑀, initial latents
𝑍𝑒 ∈ ℝ𝐿𝑚𝑎𝑥×𝑑𝑧, causal matrix 𝐴 ∈ ℝ𝐾×𝐾. Hyperparameters about causal loss 𝛾, 𝛿.
Output:
Counterfactual loss ℒcausal; intervened predictions 𝑒̂𝑌,int𝑗.
Procedure:
1. Factual Forward:
1.1 Compute 𝑍L via causal layer on 𝑍𝑒,L.
1.2 Concatenate: 𝑍𝑑 = [𝑍L, 𝑍extra].
1.3 Decode 𝑍: 𝑒̂𝑌 ∈ ℝ𝑃.
2. Interventions:
Intervene on labels set 𝑗 in [1, 𝐾],
2.1 Construct 𝑒𝑈𝑗: Set sub-dimensions to baseline do(𝑈𝑗 = 0)
2.2 Conditional prior: 𝜇𝐿𝑗,𝐸,conf, log𝜎𝐿𝑗,𝐸,conf 2 = MLP([𝑒𝐿𝑗, 𝑒C, 𝑒𝐸𝑚])
2.3 Sample 𝑍L,int𝑗 ∼ 𝒩(𝜇𝐿𝑗,𝐸,conf, 𝜎𝐿𝑗,𝐸,conf 2 ) for 10 times.
3. Causal Propagation:
3.1 Apply causal layer: 𝑍L, intj = 𝑓 (𝐴 ⋅ 𝑍𝐿,𝑖𝑛𝑡𝑗, 𝜖).
3.2 Concatenate: 𝑍𝑖𝑛𝑡𝑗 = [𝑍𝐿,𝑖𝑛𝑡𝑗, 𝑍𝑒𝑥𝑡𝑟𝑎].
4. Decode Intervened Outputs:
Decode 𝑍𝑖𝑛𝑡𝑗: 𝑒̂𝑌,𝑖𝑛𝑡𝑗 ∈ ℝ𝑃 for 10 times and take mean.
5. Compute Counterfactual Losses:
5.1 𝑍 → 𝑌:
 ℒcausal,𝑌 = MSE(𝑒̂𝑌, 𝑒𝑌) − 𝛾MSE(𝑒̂𝑌,𝑖𝑛𝑡𝑗, 𝑒𝑌)
5.2 𝑍 → 𝑍:
 ℒcausal,𝐴 = CE(𝑔(𝑍L), 𝑒𝐿) − 𝛿CE(𝑔(𝑍L,𝑖𝑛𝑡𝑗), 𝑒𝐿).
5.3 Total: ℒcausal = ℒcausal,Y + ℒcausal,A.
6. Return:
Return ℒcausal, 𝑒̂𝑌,𝑖𝑛𝑡𝑗.

 71

Algorithm 4: Optimal Label Intervention Search for Maximum Interaction
Input:
𝐿: {0,1}72 matrix of binary labels
data: Model input data, including Marketing text 𝑋, environment variables C ∈ ℝ𝑄,
common confounders 𝑒𝐸𝑚 ∈ ℝ𝑀, trained D-VAE model.
max_flips: Maximum number of labels to intervene (default: 5).
inference.causal_intervention: Function to compute counterfactual interaction predictions
𝑒̂𝑌,𝑖𝑛𝑡 ∈ ℝ𝑁.
Output:
𝐿̂: 1 × 72 matrix of optimal flipped labels.
𝑆: Set of flipped label indices (|𝑆| ≤ max_flips).
best_score: Maximum predicted interaction sum.
Procedure:
1. Initialization:
1.1 Initialize empty flip set: 𝑆 = ∅.
1.2 Set current labels: 𝐿current = 𝐿, baseline interaction: 𝑒̂𝑌,base = 𝑒𝑌 ,Set initial
score: best_score = ∑ 𝑒̂𝑌,base 𝑃 𝑝=1 [𝑝].
1.3 Initialize optimal outputs: best_S = ∅, 𝑈̂ = 𝑈.
2. Greedy Search for Optimal Flips:
For 𝑡 = 1 to max_flips:
2.1 Initialize temporary maximum score: max_score = best_score.
2.2 Initialize best candidate tag: 𝑗∗ = None.
2.3 For each tag 𝑗 ∈ {1,2, … ,72}\𝑆:
 a. Construct intervention set: 𝑆′ = 𝑆 ∪ {𝑗}.
 b. Compute counterfactual interaction:
 𝑒̂𝑌,int = D-VAE.inference.causal_intervention(𝑋, 𝐶, 𝑒𝐸𝑚,intervention = 𝑆′)
 c. Calculate score: score𝑗 = ∑ 𝑒̂𝑌,int 𝑃 𝑝=1 [𝑝].
 d. If score𝑗 > max_score: Update max_score = score𝑗, Set 𝑗∗ = 𝑗.
2.4 If 𝑗∗ = None: Break (no further improvement possible).
2.5 Update flip set: 𝑆 = 𝑆 ∪ {𝑗∗}.
2.6 Update current labels:
 𝐿current[: , 𝑗∗] = 1 − 𝐿current[: , 𝑗∗]
2.7 Update optimal outputs: best_S = 𝑆, 𝐿̂ = 𝐿current, best_score = max_score.
3. Return:
Return 𝐿̂, best_S, best_score.

 72

Online Appendix D: Supplementary Charts

Figure 1: Pearl’s Causal Ladder: Data Distributions Across Three Levels of Causality

Figure 2: User Engagement Distribution in Our Dataset

 73

Online Appendix E: Additional Information on the Field Experiment
1. Manipulation Check
1.1 Prompt Template for LLM-based Manipulation Check
1.2 Manipulation Check Score
2. Demographic Distributions of Respondents

You are an expert marketing analyst. I will provide you with:
A target label change: one or more labels added and/or removed;
The original ad copy (before intervention);
The modified ad copy (after intervention).
Your task is to evaluate whether the modified copy faithfully reflects the intended label change by:
Emphasizing content consistent with the added label(s), and
Removing or de-emphasizing content associated with the removed label(s).
For each label in the intervention, assign a score from 1 to 10, where:
1–3: The copy contradicts or ignores the label;4–6: The copy weakly or ambiguously aligns with the
label;7–10: The copy clearly and coherently embodies the label’s intent.

 74
