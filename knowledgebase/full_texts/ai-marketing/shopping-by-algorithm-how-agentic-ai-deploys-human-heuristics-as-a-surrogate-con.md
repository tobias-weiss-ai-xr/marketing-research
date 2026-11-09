---
title: 'Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer'
url: https://arxiv.org/abs/2609.28372
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Davood Wadi
- Yu Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28372
pages: 58
chars: 203000
fetched_at: '2026-11-08T13:19:45+00:00'
kb_version: 1
---

# Shopping by algorithm: How agentic AI deploys human heuristics as a surrogate consumer

Shopping by algorithm: How agentic AI deploys human heuristics
as a surrogate consumer
Davood W adi
Desautels Faculty of Management
McGill University
Montreal, Quebec, Canada
davood.wadi@hec.ca
Y u Ma
Desautels Faculty of Management
McGill University
Montreal, Quebec, Canada
yu.ma@mcgill.ca
Abstract
Consumers increasingly delegate purchasing decisions to Large Language Models (LLMs) acting as surrogate
consumers. We develop “Tool-Lab,” an adaptation of information-board process tracing that places product
attributes behind costly tool calls, and use it to examine how marketing pricing cues (i.e., just-below pricing
and promotional framing) influence AI shopping agents. Across eight commercially deployed LLMs from three
providers, we trace pre-choice information acquisition. Under zero cost, pricing cues rarely mislead. Imposing
acquisition costs under a vague goal prompt leads LLMs to omit diagnostic attributes required to compute
unit price and make suboptimal choices resembling human heuristics. Relative to a specific goal prompt
that largely preserves diagnostic search and choice optimality, a vague goal prompt under constraints creates
a search-mediated vulnerability for AI agents. This research demonstrates that the efficacy of marketing
cues in delegated AI shopping is governed by storefront information architecture combined with consumers’
instructions, not necessarily immutable LLM characteristics.
Keywords:Artificial Intelligence, Large Language Models, Bounded Rationality, AI Agents
Introduction
The evaluation of market alternatives has historically relied on human judgment. Increasingly, however,
consumers are delegating end-to-end purchasing tasks to autonomous Large Language Models (LLMs) deployed
as surrogate consumers (Pandya; Aw et al., 2025; Hasselwander et al., 2026; Puntoni and Wertenbroch, 2024),
that is, an external entity to whom a principal relinquishes decision authority to navigate the marketplace
(Solomon, 1986). Major platforms have begun deploying agents that search, compare, and complete purchases
on consumers’ behalf (Verdon; Sataua; Kahn). While surrogate consumers have traditionally been humans,
delegating this role to AI agents represents a fundamental shift in who evaluates the market (Dholakia et al.,
2025).
Since for decades, retail pricing strategies, such as just-below pricing (Lacetera et al., 2012; Stiving and
Winer, 1997; Thomas and Morwitz, 2005) and promotional discount framing (Inman et al., 1990; Thaler,
1985), have been engineered to exploit human bounded rationality, practitioners already advise retailers to
structure pricing and product attributes so that AI agents can evaluate them (Cooper III). Still, when the
buyer is an autonomous AI agent, it remains an open question whether pricing cues built for human cognitive
limitations continue to influence purchasing, and if so, how.
Research evaluating LLMs as economic actors has found them to produce both rational (Brand et al., 2023;
Cillo and Rubera, 2025; Horton et al., 2023) and heuristic-like behavior (Binz and Schulz, 2023; Filandrianos
et al., 2025; Hermann and Puntoni, 2025). Reconciling this duality has been proven difficult because the
existing literature predominantly treats heuristic-like behavior as an inherent, static defect hardwired into
LLMs during training. As a result, research has largely documented whether LLMs exhibit heuristic-like
behavior, but not what produces it.
We propose that heuristic-like purchasing in delegated AI shopping can be a property of the information
state that the AI agent holds at the moment it commits to a choice. This pre-choice information state can
be jointly shaped by retailers and consumers. Retailers determine the cost of retrieving product attributes
1
arXiv:2609.28372v2  [econ.GN]  13 Oct 2026

through platform design, and consumers determine, through the specificity of their delegating prompt, which
attributes the AI agent treats as diagnostic. The combination of costly retrieval and vague goal prompts
leads AI agents to truncate their information search and choose suboptimally.
To test this claim, we introduce Tool-Lab, an experimental paradigm that adapts classical information-board
process tracing (Johnson et al., 1989; Payne et al., 1993; Willemsen and Johnson, 2011) to multi-turn LLM
interactions. Rather than presenting product attributes simultaneously within a single prompt, Tool-Lab
embeds an LLM within an interactive environment where product attributes are hidden behind costly tool
calls. To inspect an attribute, the LLM must execute a tool call (inspect_cell), which incurs an explicit
acquisition cost. Tool-Lab records the observable sequence of information acquisitions prior to choice and
allows researchers to measure search depth and composition directly. Therefore, Tool-Lab allows us to
manipulate retrieval cost and prompt specificity while observing the search they produce. This makes the
pathway from environmental constraint to final choice through information acquisition measurable, rather
than inferred from choice outcomes alone.
Across two primary studies, several robustness tests, and two validation studies (N = 33,704total trials), we
evaluate eight commercially deployed LLMs from three major providers (Google, OpenAI, and Anthropic).
Each study establishes a full information baseline, then contrasts LLM choices with a constrained Tool-Lab
environment where information acquisition incurs financial costs (c = $0vs.$10 .00or$50 .00), and the
consumer prompt’s goal is specific or vague (“find the lowest price per ounce” vs. “find the best deal”).
The empirical results document two consistent findings. First, under full information and specific goal prompt,
the evaluated LLMs make decisions that largely align with normatively optimal behavior. Second, when
acquisition costs are imposed under a vague goal prompt, most LLMs decrease search depth, and the impact
on choice optimality depends on whether the omitted attributes are diagnostic (i.e., they are necessary to
calculate the unit price). Because vague prompts lack a clear normative objective, LLMs abandon some
diagnostic attributes (i.e., cents or product weight). Without the attributes that are required to calculate unit
prices, the AI agents make suboptimal decisions that are consistent with human heuristic decision making.
Validation experiments (N = 5,200) show that choice suboptimality stems from missing diagnostic attributes
rather than arithmetic calculation failures for most LLMs.
This research makes three contributions to marketing theory of agentic AI shopping. First, it challenges
the assumption that heuristic-like behavior in LLMs as shopping assistants is solely inherited from training
data, by showing that susceptibility to marketing cues depends on the information state in which AI agents
choose. Second, it identifies the principal’s delegation instruction as a determinant of whether marketing
cues influence the AI agent’s choice. Third, it introduces Tool-Lab, a process-tracing method that makes the
information acquisition of AI agents observable and allows researchers to study how AI agents make decisions.
These findings have implications for four stakeholders. Retailers should make diagnostic attributes (e.g.,
“price”, “weight”) readily available to AI shopping agents. Consumers should clearly state the criterion that
defines a good choice (e.g., “lowest price per ounce”) rather than issuing vague requests such as “find the
best deal.” AI agent developers should design agents to clarify vague objectives before searching and should
audit the specific LLM they deploy for acquisition truncation. Finally, regulators should consider extending
disclosure rules, such as unit-price requirements, to the product information made available to AI agents.
Literature review
AI agents as surrogate consumers
Marketing scholarship has examined Generative Artificial Intelligence (GenAI) primarily through firm-side
strategy (Prasanna and Kushwaha, 2025; Riandhi et al., 2025; Grewal et al., 2025; Kumar et al., 2026), yet
the critical frontier in marketing theory centers on the autonomous AI agent itself (Aw et al., 2025; Dholakia
et al., 2025; Puntoni and Wertenbroch, 2024). Behavioral research in this domain predominantly treats Large
Language Models (LLMs) as passive “silicon samples” or synthetic respondent pools (Joerling, 2025; Sarstedt
et al., 2024) to emulate human survey responses and aid in marketing research (Arora et al., 2025; Li et al.,
2025; Liu and Chen, 2026; Wang et al., 2026).
2

However, there is a growing use of AI agents by consumers as autonomous shopping assistants that perform
end-to-end shopping (Hasselwander et al., 2026; Kim et al., 2023; Pandya; Google DeepMind, 2026). In
marketing theory, delegating purchase authority to an external entity is a classic case of surrogate consumption
(Solomon, 1986). A surrogate consumer is defined as an agent to whom a consumer relinquishes decision
authority to evaluate, select, and acquire goods within the marketplace (Solomon, 1986). Today, generative
AI, in particular Large Language Models (LLMs), can act as surrogate consumers because they are capable of
autonomously querying APIs, exploring product catalogs, and executing financial transactions on a consumer’s
behalf (Google DeepMind, 2026; Schick et al., 2023; Wang et al., 2024). In fact, Meta, Google, and Amazon
now deploy LLM agents that complete purchases on consumers’ behalf (Meta; Sataua; Srinivasan; Amazon
Staff), and nearly a quarter of U.S. consumers report making an AI-assisted purchase (Morgan Stanley).
The rationality paradox
As LLMs assume the role of surrogate consumers, a behavioral paradox emerges in the literature. LLMs neither
conform strictly to classical economic assumptions of rationality (Thaler, 2000), nor do they predictably
replicate human bounded rationality (Kahneman, 2003). On the one hand, an extensive body of research
demonstrates that LLMs inherently possess strong analytical capabilities (Lee et al., 2026; Pandey and Singh,
2025). When prompted in standard discrete-choice environments, LLMs can function as highly capable
simulated economic actors (Horton et al., 2023). They can evaluate expected values, respect downward-
sloping demand curves, maintain budgetary compliance, and execute complex multi-attribute compensatory
evaluations (Brand et al., 2023; Cillo and Rubera, 2025; Reisenbichler et al., 2026; Zhou et al., 2026).
These competencies embody analytical (“thinking”) AI, characterized by computational precision, logic, and
rule-based data processing (Huang and Rust, 2021).
On the other hand, research in computational psychology documents that LLMs remain susceptible to classic
cognitive anomalies (Binz and Schulz, 2023; Hermann and Puntoni, 2025). LLMs can show susceptibility
to framing effects (Pescher, 2026), algorithmic impatience in intertemporal choices (Goli and Singh, 2024),
and vulnerability to adversarial prompt perturbations (Xie, 2026). In product recommendation, promotional
framing and sponsorship cues embedded in product text can distort LLM recommendations even when
objective attributes remain the same (Filandrianos et al., 2025; Wadi and Ma, 2026b). Importantly, large-scale
benchmarks demonstrate that this paradox is not resolved simply by increasing computational capability
of the LLMs (Echterhoff et al., 2024; Knipper et al., 2025; Malberg et al., 2025). Thus, the emergence of
suboptimal behavior cannot be understood purely as a capability limitation. Instead, marketing scholarship
must examine the contextual and task-level factors that govern when an LLM operates in an analytical versus
a suboptimal decision mode (Huang and Rust, 2021).
Marketing pricing cues
While much of the computer science literature examines biases through abstract logic puzzles, such as
the Linda problem or the Wason selection task (Binz and Schulz, 2023; Knipper et al., 2025), marketing
phenomena introduce a fundamentally different evaluative dynamic. In consumer purchasing, pricing tactics
(e.g., just-below pricing and promotional discount framing) do not operate solely as abstract semantic frames.
Rather, these marketing cues directly compete with exact utility calculations (Stiving and Winer, 1997;
Thomas and Morwitz, 2005).
Just-below pricing (e.g., pricing an item at $4.99 rather than $5.00) exploits a heuristic wherein decision-
makers focus disproportionately on the leftmost integer while ignoring fractional cents (Bizer and Schindler,
2005; Thomas and Morwitz, 2005; Kraft and Rao, 2026; Lacetera et al., 2012). Similarly, promotional discount
framing (e.g., “20% off”) exploits transaction utility by signaling a bargain to the consumer (Inman et al.,
1990; Thaler, 1985). Therefore, if an AI shopping agent attends to the whole dollar price or the promotional
cue while ignoring cents or package volume, it could select an economically inferior product.
3

Storefront information architecture
The marketing and computer science literatures predominantly treat heuristic susceptibility in LLMs as a
static, immutable defect hardwired during training (Echterhoff et al., 2024; Knipper et al., 2025; Malberg
et al., 2025). According to this view, an LLM defaults to choices resembling human heuristics because its
autoregressive parameters reflect the bounded rationality deeply embedded within human corpora.
However, this remains an untested and largely untestable claim. Because modern LLMs are trained on
uncurated, proprietary web-scale corpora spanning trillions of tokens, empirically testing whether a suboptimal
choice stems from heuristics embedded directly into its parameters is virtually impossible. Despite the absence
of direct empirical verification, this “innate defect” account has operated as an implicit assumption across
behavioral LLM research. We propose an alternative account. Choices that resemble human heuristics in
AI agents are not solely innate training defects, but a product of the interplay between the information
architecture of the storefront and the delegating prompts used by consumers.
Beyond the difficulty of tracing behavior back to the training corpora, the “innate defect” assumption has
persisted due to a prevailing methodological constraint. When an AI shopping agent is presented with
fully enumerated product profiles in a single prompt and selects an inferior alternative, the researcher
cannot disentangle the terminal choice from how the choice was made (Johnson et al., 2008). Therefore,
despite research demonstrating suboptimal decision-making of AI shopping assistants (Allouah et al., 2026;
Pezeshkpour and Hruschka, 2024; Wadi and Ma, 2026a; Liu et al., 2024; Yin et al., 2026), outcome-based
data cannot explain whether the LLM calculated unit values but over-weighted a marketing cue, or whether
its informational state was configured such that normative calculation was never attempted.
Conceptual development
Normative and heuristic objectives
In economic decision-making, an agent evaluates market alternatives against a specific objective function.
Depending on the decision context, this objective would optimize nominal expenditure, brand equity, perceived
quality, or price per unit of volume. In the consumption of packaged goods, marketing theory and consumer
economics establish that the normative objective is unit-price minimization—selecting the alternativej that
minimizes financial expenditure per unit of physical quantity (Miyazaki et al., 2000; Russo, 1977):
min
j∈J
( Pricej
Weightj
)
It is against this normative benchmark that behavioral economics considers choice driven by pricing cues,
such as just-below pricing and promotional discount framing, economically suboptimal and refers to them as
biases.
Consider just-below pricing. If an agent chooses a 10-ounce package priced at $4.99 over an available 100-ounce
package priced at $5.00, the decision is optimal under a price-minimization objective (minj∈J Pricej), but
suboptimal under the normative unit-price objective (minj∈J Pricej Weightj ). In human decision research, when an
individual shifts from the normative objective to a simpler one, this substitution is referred to as a heuristic
(Gigerenzer and Gaissmaier, 2011; Shah and Oppenheimer, 2008).
Similarly, when evaluating promotional discounts, computing the normative objective of a discounted item
requires a multi-parameter objective function calculation:
min
j∈J
Unit Pricej = min j∈J
List Pricej×
(
1−
Discount Percentage j
100
)
Weightj
Because computing this objective requires multi-step arithmetic, decision-makers operating under constraints
frequently substitute the normative objective with a computationally simpler one, such as maximizing the
4

discount percentage or minimizing the discounted list price. In marketing theory, this objective substitution
is called transaction utility (Inman et al., 1990; Thaler, 1985).
Following this framing, we adopt unit-price minimization as the normative objective for consumer packaged
goods and classify any choice that deviates from this normative objective as suboptimal. Heuristic then
becomes a resource-conserving departure from full evaluation of the normative objective, either by substituting
a simpler objective (e.g., price minimization) or by evaluating the normative objective on a reduced set of
attributes (e.g., ignoring cents; Shah and Oppenheimer, 2008).
Product attributes can be classified by their role in the normative objective calculation. We refer to the
subset of attributes that enter the unit-price equation asdiagnostic(i.e., list price, whole dollars, cents,
discount percentages, and weight), and the attributes that do not enter the equation asnon-diagnostic(e.g.,
packaging, country of origin, calories).
Acquisition Costs
In human judgment, information acquisition is costly. Human decision-makers face both external constraints
(e.g., time pressure, fragmented shelf displays) and internal cognitive limitations (e.g., working memory
capacity, computational fatigue; Payne et al., 1993; Shugan, 1980).
Similarly, an LLM operating as a surrogate consumer incurs both external and internal acquisition costs.
External acquisition costs arise from storefront architecture and environment design, including the structural
placement and prominence of attributes within the prompt or the structure of API payloads. Internal
acquisition costs reflect computational resource allocation and LLM tendencies and capability. These include
the LLM’s configured reasoning effort, the number of reasoning tokens it produces, or the number of tool
calls it requests before producing the final response. LLM providers calibrate these propensities during
fine-tuning to balance inference speed and API operating costs against output accuracy. If an AI agent
were to exhaustively inspect every product attribute via unbounded tool calls, task execution would become
prohibitively slow and expensive. Because online storefronts offer thousands of alternatives, each with
many attributes, exhaustive inspection is prohibitively slow and would exceed the LLM’s output token limit.
Thus, the LLM realistically must truncate its acquisition before inspecting every alternative and attribute
combination. Throughout this research, we use the termacquisition costto refer to both the internal and
external constraints that an LLM operates within.
Goal specificity
LLMs are instruction-tuned to deliver contextually coherent and relevant responses to users’ prompts. In a
delegation relationship, however, task performance strongly depends on the goal specificity communicated by
the delegating principal (Kleingeld et al., 2011; Locke and Latham, 2002). According to goal-setting theory
(Latham, 2023), high goal specificity directs the agent’s effort to goal-relevant information.
We define prompt specificity as whether the prompt specifies the objective to be optimized. Aspecific goal
promptexplicitly defines the objective function to be optimized (e.g.,“Find the coffee with the lowest price
per ounce”), and the diagnostic attribute set. Conversely, avague goal prompt, such as the colloquial“Find
the best deal”, leaves the objective open to multiple valid interpretations (e.g., price per weight or price) and
leaves objective specification partly to the LLM.
Under high acquisition costs, a vague goal prompt can reduce diagnostic acquisition through two routes.
First, the LLM can substitute the normative objective (price per weight) with a simpler one (e.g., price),
which shrinks the diagnostic set from attributes that determine price and weight to attributes that determine
price alone. Second, the LLM can omit attributes whose expected value of information is low relative to the
acquisition cost. For example, cents ($0.00 to $0.99) has a relatively smaller contribution to the normative
objective function than whole dollars (Web Appendix H). Both routes reduce the total acquisition cost of
completing the task.1
1In our framework, it is not necessary to distinguish between these two routes, as both yield the hypothesized pathway.
Distinguishing between these two routes across LLMs and pricing cues is beyond the scope of this research, although we illustrate
how Tool-Lab can separate them in Web Appendix E
5

H1.A vague goal prompt negatively moderates the relationship between acquisition cost and diagnostic
acquisition.
Because computing the normative objective requires the complete set of diagnostic attributes, the diagnostic
information retrieved dictates whether the LLM has the necessary information for normative objective
optimization.
H2.Diagnostic acquisition positively influences choice optimality.
Integrating these stages establishes a moderated mediation. Under a vague goal prompt, acquisition costs
lead to diagnostic acquisition truncation, which in turn leads to choice suboptimality.
H3.The indirect effect of acquisition cost on choice optimality via diagnostic acquisition is moderated by
prompt specificity.
Insert Figure 1 about here
We next present the Tool-Lab paradigm, which allows us to test our hypotheses. We then report two empirical
studies examining just-below pricing (Study 1) and promotional discount framing (Study 2). Each study
begins with a baseline where all attributes are visible, followed by a Tool-Lab experiment where attributes
are hidden behind costly tool calls.
The Tool-Lab paradigm
To test how acquisition costs affects decision-making in delegated AI purchasing, empirical research requires
a method that moves beyond choice outcomes. In human decision research, process-tracing methods such as
Mouselab (Johnson et al., 1989; Payne et al., 1993) externalize internal decision-making steps by placing
product attributes behind closed display boxes on a computer screen. By tracking which boxes human
participants uncover, researchers observe information acquisition directly.
We adapt this paradigm to Large Language Models (LLMs) acting as consumption decision makers through
an experimental paradigm we term Tool-Lab. Rather than presenting an LLM with all product attributes
within a single prompt, Tool-Lab embeds the LLM within an interactive, stateful software environment where
product data are hidden behind costly tool calls.
In Tool-Lab, product alternatives and their corresponding attributes are structured as anM×N matrix of
hidden cells. The AI agent interacts with this environment using tool calls (function calling). The environment
exposes two tools, namely,inspect_cellandsubmit_choice 2. To reveal an attribute’s value, the LLM must
execute a tool call specifying the alternative and the attribute (e.g.,inspect_cell(option_id=“coffee_b”,
attribute_id=“weight”))3. In response, the environment returns a structured JSON payload containing
the revealed value, the cost incurred for the tool call, and the cumulative cost accrued during the session.
The LLM can terminate the search sequence by invoking a separate tool, namedsubmit_choice(e.g.,
submit_choice(option_id=“coffee_b”)). Invoking this tool concludes the session and commits the final
purchase.
To operationalize the acquisition cost, Tool-Lab attaches an explicit financial cost to each invocation of
inspect_cell, which is charged directly to the delegating consumer.submit_choicecarries zero cost. By
manipulating this cost across conditions, we observe how the AI agent adjusts its information acquisition
behavior under varying degrees of constraint (Figure 2).
Insert Figure 2 about here
We quantify total acquisition, the distribution of acquisition across diagnostic (vs. non-diagnostic) attributes,
and the final choice. This allows us to isolate whether a suboptimal choice occurred under complete diagnostic
information (a utilization failure) or under incomplete diagnostic information (an acquisition failure). Tool-
Lab can also record the reasoning traces that LLMs produce between tool calls (Yao et al., 2022). This is
conditional on LLMs having reasoning capabilities and providers making reasoning traces accessible to the
2During each session, the LLM can execute only one tool call per turn.
3To prevent the letters “a” or “b” in coffee_a and coffee_b affecting the choice, each session randomizes theoption_id.
6

public. See Web Appendix E for an example of how we used the pre-tool reasoning traces to classify the
objectives expressed by LLMs under vague goal prompt.
Stochastic evaluation.Evaluating LLMs in multi-turn tool environments requires addressing the stochastic
nature of autoregressive text generation. In standard commercial deployments, LLMs sample tokens from
probability distributions, meaning identical prompts can generate heterogeneous search trajectories and final
decisions.
To account for this variance, Tool-Lab implements a Monte Carlo sampling protocol (Wadi and Fredette,
2025; Robert et al., 1999; Holtzman et al., 2019). Rather than evaluating a single deterministic pass, each
experimental cell is evaluated across multiple independent simulated sessions per LLM. Every session is
initiated as an isolated API conversation with zero state retention between trials. Within each session, the
presentation order of alternative options and attribute rows is randomized to prevent position confounds.
All interactions are executed programmatically via official client libraries under default provider decoding
configurations, and all tool responses are validated against JSON schemas (detailed specifications and snapshot
identifiers are provided in Web Appendix I).
LLMs tested.Unless noted otherwise, the experiments test eight commercially deployed LLMs from three
major providers: Gemini 3.5 Flash Lite (Flash Lite), Gemini 3.8 Flash (Flash), and Gemini 3.1 Pro (Pro)
from Google, GPT 5.6 Luna (Luna), GPT 5.6 Terra (Terra), and GPT 5.6 Sol (Sol) from OpenAI, and
Claude Sonnet 5 (Sonnet) and Opus 5 (Opus) from Anthropic (shorthand names in parentheses). To avoid
repetition, we refer to these LLMs using their shorthand name.
Study 1
Baseline
We first test LLM choice when diagnostic attributes (i.e., dollars, cents, and weight) are fully available
without any external constraints. We constructed a coffee choice experiment forcing trade-offs between brand,
product weight, and price. We utilized four of the best-selling Amazon.com brands (McCafé, Maxwell House,
Starbucks, Folgers). To investigate the relative effect of the cent versus the dollar value of the price on choice,
we independently drew dollars and cents from the real-world distribution of coffee prices. We generated 1,014
non-dominated choice sets to ensure no alternative was superior in both price and weight, which would push
the LLMs to make genuine economic trade-offs (Web Appendix B).
We queried the eight LLMs once per choice set (N = 8,112trials; 1,014 per LLM), as well as a normative
objective optimizer that always chooses the alternative with the lowest price per weight. We used a
standardized prompt that delegates the LLM as a surrogate shopping assistant (“You are a helpful shopping
assistant”; Table W21). The presentation positions of the alternatives were randomized to control for position
effects. We estimate an independent conditional logit for each LLM and the normative objective optimizer
separately, assuming a random utility framework (Train, 2009, specification in Web Appendix B). Table W1
shows the results.
Normative price sensitivity requires that a cent in dollar units be weighted at the same rate as a dollar.
To test whether the LLMs weight the cents at the normative rate, we estimate separate marginal utilities
for dollars (βDollars ($)) and for cents converted to dollar units (Cents ($)= Cents 100 ), and evaluate their ratio,
βCents ($)/βDollars ($), against the normative benchmark of one. Confidence intervals are exact, obtained by
Fieller’s theorem (Fieller, 1954) from the estimated coefficients.
The ratio of cent-to-dollar sensitivity ranges from 0.55 to 1.12 (Table W2). Only Flash systematically
discounts cents relative to whole dollars (ratio = 0.55, 95% CI [0.19, 0.90]). For example, Flash treats the
16-cent difference between $8.99 and $9.15 as a 54-cent difference. For the other seven LLMs, the 95%
confidence interval contains 1.00, and we find no evidence that they discount or favor the cent relative to the
dollar amount. Hence, under full attribute information, most LLMs do not show a just-below pricing effect.
7

Tool-Lab
The baseline experiment cannot trace what happens when the information environment is constrained, and
how acquisition costs affect LLM choice. We deploy Tool-Lab to explore these conditions and test our
hypotheses. We instruct the LLMs to choose an instant coffee for a human consumer. The stimulus set
consists of two alternatives designed as a choice trap to isolate the just-below pricing effect.Coffee A, has a
lower dollar value ($4.99 for 10 oz), but yields a suboptimal unit-price of 0.499 $/oz.Coffee B, the optimal
choice, has a higher dollar value ($5.00 for 11 oz), but yields the superior unit price at 0.455 $/oz. A normative
objective optimizer would thus chooseCoffee B.
To force a tradeoff between the dollar and cent components of the price, we separate the price into two
hidden attributes,price_dollars(e.g., “$4”) andprice_cents(e.g., “99 cents”). To calculate the unit
price (price dollars+price cents weight ), the LLM must expend resources to reveal three diagnostic attributes for each
alternative (6 diagnostic attributes total). To increase ecological validity of the products and to obscure the
true purpose of the experiment, we also include four non-diagnostic attributes (origin,roast_date,calories,
andpackaging). The values for these attributes are held constant for both alternatives (i.e., “Colombia”, “2
weeks ago”, “3” “Foil bag”) to prevent any confounds.
We implement a 2 (Acquisition cost: $0.00 vs. $10.00 perinspect_cellinvocation)× 2 (Goal specificity:
specific vs. vague goal prompt) between-sessions design. To manipulate goal specificity, we vary the evaluative
instruction in the prompt. In the vague goal prompt condition, the LLM receives a colloquial purchasing
prompt:“You need to find thebest dealon instant coffee.”In the specific goal prompt condition, this
instruction is replaced with the normative objective:“You need to find the coffee with thelowest price per
ounce.”All other elements of the prompt, the product stimuli, and the tool environment are held constant
across conditions. We evaluate the eight LLMs. In total, Study 1 Tool-Lab comprises 3,200 unique simulated
sessions (8 LLMs×2 acquisition costs×2 goal specificity conditions×100 iterations).
Each session begins with a system prompt that delegates the choice of an instant coffee to the LLM and
states that the user would purchase 5 bags of the chosen coffee.4 The prompt then defines the tool mechanics
and states that the user loses an amount equal to the acquisition cost for eachinspect_cellcall, followed by
the goal specificity manipulation and the choice query (Table W3).Choice optimalityis the final product
selected via thesubmit_choicetool, coded as a binary variable (1 = the optimal choice; 0 = the suboptimal
choice).Diagnostic acquisitionis the count of how many of the six diagnostic attributes (price_dollars,
price_cents, andweight) the LLM inspects before submitting its choice.
ResultsAggregated across all LLMs tested (Table 1; per LLM descriptives in Table W4), diagnostic
acquisition and choice optimality were high at zero cost under both the specific goal prompt (M = 6.00
and0 .94) and the vague goal prompt (M = 5.86and0 .89). Under the specific goal prompt, the $10.00
acquisition cost produced a small reduction in diagnostic acquisition (M = 5.72) and choice optimality
(M = 0.83), driven exclusively by the omission of cents. Under the vague goal prompt, the same cost produced
a substantial reduction in diagnostic acquisition (M = 3.81) and choice optimality (M = 0.29). The LLMs
largely maintained dollars but omitted both cents and weight.
Insert Table 1 about here
Moderated mediation analysisTo test H1–H3 while allowing baseline acquisition and structural slopes to
vary across LLMs, we estimate a Bayesian multilevel moderated mediation model in Stan viabrms(Bürkner,
2017). The first stage regresses diagnostic acquisition on acquisition cost, prompt specificity, and their
interaction (H1). The second stage regresses choice optimality on diagnostic acquisition (H2), acquisition
cost, and prompt specificity. It uses a linear probability specification, which permits an exact additive
decomposition of conditional indirect effects (Breen et al., 2013) and the Index of Moderated Mediation
(IMM=a 3×b 1; H3). Equations, priors, and Markov chain diagnostics are reported in Web Appendix D.
Insert Table 2 about here
The empirical estimates are consistent with the hypothesized structural pathways (Table 2, Study 1).
4We scale the purchase volume to five bags to ensure that the potential economic surplus of identifying the optimal product
mathematically justifies the cumulative tool costs.
8

Prompt specificity moderates the effect of acquisition cost on diagnostic acquisition (a3 =−1.727, 95%
CI[−2.641,− 0.765]), supporting H1. Acquisition cost credibly reduces diagnostic acquisition under the
vague goal prompt (aVague =−1.997), but its effect under the specific goal prompt is not credibly different
from zero (a1 =−0.270, 95% CI[−0.698, 0.161]). Diagnostic acquisition is positively associated with choice
optimality (b1 = 0.263, 95% CI[0.196, 0.329]), supporting H2. The Index of Moderated Mediation is negative
(IMM =−0.451, 95% CI[−0.704,− 0.194]), supporting H3. The indirect effect is negative under the vague
goal prompt but overlaps zero under the specific goal prompt. The direct effect of acquisition cost on
choice optimality is not credibly different from zero (c′ =−0.100, 95% CI[−0.251, 0.051]), which indicates
that the decrease in choice optimality operates primarily through the truncation of diagnostic acquisition.
Disaggregated analyses show that this indirect pathway is broadly consistent across the evaluated LLMs,
with one exception. Luna maintained diagnostic acquisition under vague goal prompt with an IMM that
overlapped zero (IMM =−0.063, 95% CI[−0.158, 0.033]). LLM-specific structural path estimates and
conditional indirect effects are reported in Table W5 and Table W6.
Prompt variationA natural concern with LLM evaluations is that the observed effects might be due to
the specific prompt wording or ordering rather than the pathway that we claimed. Holding choice stimuli
and tool mechanics invariant, we test three prompt variations (Table W7): (1) theOriginalprompt; (2)
Sentence reorder, which moves the goal instruction earlier in the prompt to test for recency effects; and (3)
Cost paraphrase, which replaces the loss framing of the acquisition cost with fee framing to test for lexical
loss confounds.
Crossing these 3 prompt variations with 2 acquisition costs ($0 vs. $10) and 2 prompt specificities (specific
vs. vague goal prompt) yields 12 cells. Because testing the full design of Study 1 Tool-Lab for all eight LLMs
across 12 cells would be combinatorially prohibitive and difficult to report, we focus on the Google Gemini
family (100 sessions per cell;N = 3,600, including 1,200 sessions from Study 1 Tool-Lab). Gemini LLMs
exhibited wide behavioral variance in Study 1 Tool-Lab, under vague prompt, from a small truncation under
cost in Flash Lite (a3 =−0.44) to a pronounced truncation in Pro (a3 =−3.20; Table W8).
We estimated the moderated mediation model separately for each LLM× prompt variation combination
(Web Appendix D). Across prompt variations, the structural estimates replicate the primary findings in eight
of the nine LLM× prompt variation combinations (Table W8). In these eight conditions,a3 and the Index
of Moderated Mediation are credible in the hypothesized direction (H1 and H3). The exception is Flash Lite
under sentence reordering, wherea3 remains negative but overlaps zero (a3 =−0.120, 95% CI[−0.375, 0.140]).
Diagnostic acquisition credibly predicts choice optimality in all nine combinations (b1 = 0.180to0 .302; H2).
Price partitioningA potential concern with the Tool-Lab environment in Study 1 is that the effect of
acquisition cost on choice optimality might be an artifact of partitioning the price into two separate fields
(price_dollarsandprice_cents), which is not how prices are naturally represented in retail environments. If
the observed vulnerability to just-below pricing is merely a byproduct of this artificial separation, choice
suboptimality would reflect a measurement artifact of the Tool-Lab paradigm rather than a genuine behavioral
pathway under information acquisition constraints.
To test this, we repeated Study 1 Tool-Lab with price acquired as a singlepriceattribute, using Flash
Lite, Flash, and Pro (100 sessions per cell;N = 1,200). Consolidating price components shifted acquisition
truncation from cents to weight. Under the specific goal prompt, acquisition cost had no effect on diagnostic
acquisition or choice optimality (Table W9; Table W10). Under the vague goal prompt and the $10.00
cost, the LLMs inspectedpricefor both alternatives in most sessions (M = 1.96to2 .00) but reduced the
acquisition ofweight( M = 0.56to1 .71). Choice optimality decreased accordingly. The moderated mediation
estimates support H1–H3 for all three LLMs, with credibly negative Indices of Moderated Mediation ranging
from−0.149(Flash) to−0.622(Pro; Table W11). Therefore, the pathway does not depend on partitioning
prices into separate dollar and cent fields.
Sensitivity to purchase volumeIn Study 1 Tool-Lab, Pro acquired diagnostic attributes incompletely
under the vague goal prompt even when acquisition was free (cents:M = 1.75; weight:M = 1.68; Table
W4). Our conceptual development identifies two routes through which a vague goal prompt can reduce
diagnostic acquisition: objective substitution and truncation of low-value attributes. The two routes respond
differently when the benefit of information increases. If Pro retains the normative objective under the vague
9

goal prompt but omits attributes with low value of information, increasing the number of bags purchased
(purchase volume) should not decrease diagnostic acquisition, because the surplus from identifying the optimal
alternative grows with volume.
If instead as the purchase volume increases, Pro substitutes the normative objective with a simpler one
(e.g., price minimization) under the vague goal prompt, acquisition should follow the diagnostic set of the
simpler objective rather than the diagnostic set of the normative objective. Weight acquisition is especially
informative because weight is a diagnostic attribute under unit-price minimization (Web Appendix H), but
non-diagnostic under price minimization. To test which route governs the observed pattern, we implemented
a 3 (LLMs: Flash Lite, Flash, and Pro)× 4 (Purchase volume: 1, 5, 50, and 250 bags) between-sessions
design under the vague goal prompt at zero acquisition cost. Each cell was evaluated across 100 independent
sessions (N= 1,200) with everything else identical to Study 1 Tool-Lab.
The results show different patterns for the LLMs tested. Flash remained at ceiling at all four purchase
volumes (diagnostic acquisition:M = 6.00; optimality = 1.00). However, scaling from 1 to 250 bags reduced
diagnostic acquisition for Flash Lite and Pro (Figure W1; Table W12). Pro reduced diagnostic acquisition
fromM = 5.55to4 .22(cents: 1.81 to 1.30; weight: 1.74 to 0.92), and its optimality decreased from .80 to .35.
Flash Lite retained cents at all purchase volumes (M = 1.95to2 .00) but reduced weight acquisitions from 1
to 250 bags (M = 1.82to1 .30). Its optimality decreased from .62 to .37 as the number of bags increased.
Scaling purchase volume thus decreases diagnostic acquisitions and increases suboptimality for Flash Lite
and Pro. The decrease in diagnostic acquisition is inconsistent with the truncation of low-value attributes
account, which predicts no decrease in diagnostic acquisition as purchase volume grows.
To evaluate what objective the LLMs adopted5, a judge classified the first reasoning trace emitted before any
tool execution into one of three classes: (1) unit price minimization objective (price_per_weight), (2) price
minimization objective (price), or (3)others(Web Appendix E). We selected the judge from eight candidates
(five decision models and three LLMs) by agreement with three independent human coders. Decision models
are a class of models that return a choice among predefined categories with a probability for each. The
human coders were blind to the purpose of the experiment and independently classified a stratified subsample
of 120 traces (30 traces per purchase volume). Each coder was paid $40 ($20 per hour) for the two hours it
took an author to complete the coding session. The selected judge, the Mercury Decide decision model, had
the highest mean agreement with the three human coders (mean Cohen’sκ=.63; Table W26).
Based on the classification, Flash adopted a unit-price minimization objective (price_per_weight) in 64.6% to
73.5% of sessions and adopted a price minimization objective in at most 9.1% of sessions (Table W13; Figure
W1, Panel A). In contrast, the objective Pro adopted shifted with purchase volume. At one bag, 37.0% of
Pro sessions articulated a price objective, which increased to 85.9% of sessions at 250 bags (Table W13).
Under a price objective, cents and product weight become functionally non-diagnostic because Coffee A’s
dollar ($4.xx) is lower than Coffee B’s ($5.00). Therefore, the AI agent terminates search without inspecting
cents or weight.
To examine whether the adopted objective, rather than the purchase quantity itself, is associated with search
truncation and suboptimal choice, we evaluated the contrast between sessions adopting a price objective
and those adopting a unit-price objective, holding purchase volume fixed (Table W14; Web Appendix E).
Within every volume condition, Pro sessions adopting a price objective acquired significantly fewer diagnostic
attributes (differences ranging from−1.10to−2.09cells; all 95% bootstrap CIs exclude zero). At 1, 5, and
50 bags, they were 40 to 69 percentage points less likely to select the optimal alternative (Table W14). At
250 bags, where only two Pro sessions adopted a unit-price objective, the choice optimality contrast did not
exclude zero.
Although the human coders agreed moderately with each other (Fleiss’κ =.46), every human coder and
each of the three top-ranked judges showed similar increase in price objective classification with purchase
volume (Table W27). The shift in the adopted objective and the contrast also replicate with the second- and
third-ranked judges, except for choice optimality at 250 bags under pplx Decider v1 27B (Table W28; Table
W29).
5We useadopted objectiveto contrast the objective an LLM works toward under a vague goal prompt with the objective
stated in the specific goal prompt.
10

These results indicate that Pro’s truncation under the vague goal prompt follows objective substitution rather
than the truncation of low-value attributes.
Study 2
Study 2 tests our conceptual framework under another marketing cue: promotional discount framing.
Baseline
We first examine how LLMs process promotional framing when all attributes are freely accessible. Discounted
alternatives display the list price, product weight, and discount percentage (manipulated from 5% to 40% in
5% increments). Following Study 1, we constructed 1,149 Pareto-filtered, non-dominated choice sets of four
ground coffee alternatives from the same four brands, and queried each of the eight LLMs once per choice set
(N= 9,192trials).
Each alternative was independently assigned a discount with probability .5. Discount percentages and list
prices were independently drawn. Estimation follows Study 1 Baseline (Web Appendix C). An alternative’s
net price is List Price×(1−Discount).
Across all eight LLMs, base list price enters negatively, and discount amount and product weight enter
positively (allp<.001; Table W15).
To evaluate whether the LLMs treat a dollar saved through discounts at the same rate as a dollar spent
through list prices, we examine the ratio of the marginal utility of discount amount (in dollars) to the absolute
marginal utility of list price (βDiscount Amount/|βList Price|; Table W16), with Fieller confidence intervals as in
Study 1. For six of the eight LLMs (Flash, Pro, Sonnet, Luna, Terra, and Sol), the ratio ranges between 0.99
and 1.03, 95% confidence intervals include 1.00, and the ratio is similar to the normative benchmark (Table
W16). For Opus and Flash Lite, the 95% confidence interval excludes 1.00. Opus over-weighs discounts
slightly (ratio = 1.15, 95% CI[1.11, 1.19]), whereas Flash Lite under-weights discount savings (ratio = 0.72,
95% CI[0.67, 0.77]). These results show that under full attribute information, most LLMs tested weight a
dollar of discount savings at the same rate as a dollar of list price, with Opus over-weighting and Flash Lite
under-weighting discount savings.
Tool-Lab
Study 2 Tool-Lab tests H1–H3 for discounted products by hiding the attributes that Study 2 Baseline made
freely visible. The Tool-Lab setup follows Study 1 Tool-Lab, with two structural modifications. First, we
expand the choice set from two to three alternatives. The three alternatives represent three decision fallbacks:
(1) lowest price (Coffee C), (2) discounted (Coffee D), or (3) lowest price per weight (Coffee E, the normatively
optimal choice; Table W17).
Second, the discount cue typically has a higher Expected Value of Information (EVI) than cents. For example,
a 20% discount on a $11.87 list price (average instant coffee list price from the Walmart data; Web Appendix
H) yields $2.37 in nominal savings per bag ($11.87 total across the 5-bag purchase), compared to cents,
which can alter the net price by a maximum of $0.99 ($4.95 total across the 5-bag purchase). To establish
a commensurate economic trade-off against this higher-stakes attribute across a larger 21-cell board (9
diagnostic, 12 non-diagnostic cells), we scale the acquisition cost condition to $50.00 per inspection. The
design, procedure, and measures follow Study 1 Tool-Lab, with an acquisition cost of $0.00 vs. $50.00 (8
LLMs×2 acquisition costs×2 goal specificity conditions×100 sessions;N= 3,200).
ResultsAggregated across all LLMs tested (Table 3; per LLM descriptives in Table W18), diagnostic
acquisition and choice optimality were high at zero cost under both goal prompts. Under the specific goal
prompt, the $50.00 acquisition cost produced a small reduction in diagnostic acquisition (M = 8.26vs.8 .98)
and choice optimality (M = 0.88vs.0 .90), driven primarily by the omission of discount percentage. Under
the vague goal prompt, the same cost produced a substantial reduction in diagnostic acquisition (M= 4.82
vs.9 .00) and choice optimality (M = 0.48vs.0 .86). The LLMs reduced all diagnostic acquisitions, but
reduced weight and discount percentage more strongly than list price.
11

Insert Table 3 about here
Moderated mediation analysisThe empirical estimates support H1 (Table 2, Study 2). Prompt specificity
moderates the effect of acquisition cost on diagnostic acquisition (a3 =−2.902, 95% CI[−5.027,− 0.539]).
Acquisition cost credibly reduces diagnostic acquisition under the vague goal prompt (aVague =−3.576), but its
effect under the specific goal prompt is not credibly different from zero (a1 =−0.674, 95% CI[−1.582, 0.260]).
Diagnostic acquisition is positively associated with choice optimality (b1 = 0.078, 95% CI[0.016, 0.141]),
supporting H2. The Index of Moderated Mediation is negative (IMM =−0.228, 95% CI[−0.521,− 0.009]),
supporting H3. The direct effect of acquisition cost on choice optimality is not credibly different from zero
(c′ =−0.006, 95% CI[−0.045, 0.035]), indicating that choice degradation operates primarily through the
truncation of diagnostic acquisition. Disaggregated per-LLM structural paths and indirect effects are reported
in Table W19 and Table W20.
Validation studies
Exogenous information states
In Tool-Lab, the LLMs’ pre-choice information state is endogenous. As a result, choice suboptimality under
cost could stem from an acquisition failure (truncating search before retrieving diagnostic attributes) or a
utilization failure (an inability to synthesize attributes or an internal bias towards the suboptimal alternative).
Furthermore, choosing a lower nominal price when attributes are missing could reflect a normatively optimal
inference under partial information. Therefore, we exogenously assign fixed information states (k attributes)
directly in the prompt.
We evaluated four information states for the Study 1 environment (N = 1,600sessions; 50 sessions per cell
across eight LLMs): dollars alone (2 diagnostic cells), dollars plus roast date (2 diagnostic, 2 non-diagnostic
cells), dollars plus weight (4 diagnostic cells), and the complete diagnostic set of dollars, weight, and cents
(6 diagnostic cells). In the Study 2 environment, we tested five information states (N = 2,000sessions;
50 sessions per cell across eight LLMs): list price alone (3 diagnostic cells), list price plus roast date (3
diagnostic, 3 non-diagnostic cells), list price plus discount percentage (6 diagnostic cells), list price plus weight
(6 diagnostic cells), and the complete diagnostic set of list price, discount percentage, and weight (9 diagnostic
cells; Table W30). Across both environments, this design includes matched-count conditions that hold total
revealed cells constant while varying whether the revealed attributes are diagnostic or non-diagnostic.
The results show that suboptimal choices under partial information are primarily driven by limited diagnostic
information (Table W31 and Table W32). When provided with the complete diagnostic attribute set under
zero cost, seven of the eight LLMs selected the normatively optimal alternative in most sessions (pooled
optimality of 99.7% in Study 1 and 98.6% in Study 2; Table W33 and Table W34).
Furthermore, when diagnostic attributes were withheld, the choices of these seven LLMs aligned with the
normative Expectimax policy conditional on the available information in 99.3% of sessions across both studies
(2,434 of 2,450 of truncated trials; Table W33, Table W34). In Study 1, when cents were withheld, market
priors assign symmetric expected cents to both alternatives, making Coffee A the normative cost-minimizing
choice. Similarly, in Study 2, when product weight was withheld, Coffee C was the normative choice because
its lower list price minimizes expected unit price. This shows that selecting a lower whole-dollar price or
lower list price under partial information represents a state-consistent normative inference given limited
information. Flash Lite was the exception. When given complete diagnostic information under zero cost, it
selected the optimal alternative in 4.0% of sessions in Study 1 and 0.0% in Study 2 (Web Appendix F).
Reported valuations
Although exogenously fixing information states demonstrates that most LLMs can utilize complete information
to make the optimal choice, it does not prove whether they have the arithmetic capacity to calculate the unit
price. Moreover, when an LLM makes a suboptimal choice under partial information, that outcome could
stem from an arithmetic failure (e.g., an inability to computePrice Weight or subtract discounts) or an evaluation
failure (computing unit prices accurately but weighting a marketing cue more heavily).
12

To evaluate the arithmetic capability directly, we modified the parameter schema of thesubmit_choicetool
across both study environments under the vague goal prompt (N = 1,600sessions total; 50 sessions per cell
across eight LLMs; Web Appendix G). The LLMs were required to report, concurrently with their choice, the
calculated price metrics for every alternative in the choice set: dollars, cents, price, weight, andweight price for
Study 1, list price, discount percentage, net price, weight, andweight price for Study 2, and the basis of calculation
(“computed”vs.“insufficient_information”).“unknown”was designated as an admissible value across all
fields, which allowed the LLMs to report uninspected cells without being forced to fabricate numbers (Table
W35). Every reported valuation field was compared against the session’sinspect_cellexecution logs to classify
values as correct, arithmetic failures, hallucinations (asserting values for uninspected cells), or correctly
identified unknown values.
The results (Table W36 and Table W37) show that arithmetic failure was 0.0% across all eight LLMs, both
study environments, and all cost conditions. Whenever diagnostic attributes were inspected, every LLM
computed total prices, and unit values without mathematical error. Additionally, when search truncation
occurred, uninspected cells were correctly reported as“unknown”, with hallucinations occurring in 0.0% to
8.5% of the reported valuations across LLMs. Nevertheless, choice optimality in this validation experiment
must be interpreted with caution. Unlike the main experiments where LLMs received no explicit computational
instructions, requiring the LLMs to compute and report unit values concurrently with choice acts as an
intermediate scratchpad, which can artificially alter choice. All this experiment establishes is that suboptimal
choices cannot be strictly attributed to a lack of capability to compute the normative objective.
General discussion
This research examined whether pricing cues designed for human bounded rationality continue to influence
AI shopping agents, and what governs when they do. Across eight commercially deployed LLMs from three
major providers, just-below pricing and promotional framing affected delegated choices mainly through the
information the agent held at the moment of choice, rather than through how the agent weighted the cues
themselves. When attribute acquisition was costly and the delegating goal was vague, most evaluated LLMs
omitted diagnostic attributes, and the resulting choices resembled human heuristic decisions.
When all attributes were visible, pricing cues rarely distorted choice. Seven of the eight LLMs weighted
cents at the same rate as whole dollars (Table W2), and six of the eight LLMs weighted a dollar saved
through a discount like a dollar spent through list price (Table W16). When attributes were hidden behind
costly tool calls, the vague goal prompt negatively moderated the effect of acquisition cost on diagnostic
acquisition, which in turn reduced choice optimality. The validation studies show that this degradation
happens primarily through information acquisition rather than utilization. When information states were
assigned exogenously, seven of the eight LLMs selected the alternative implied by the normative policy in
99.3% of sessions with partial information (Web Appendix F). When required to report unit values, no LLM
made an arithmetic error (Web Appendix G). Selecting the lower whole-dollar or lower list-price alternative
was therefore consistent with the information the agent held (Table W33, Table W34), even though it was
economically inferior given the full attribute set.
Tool-Lab reveals which attributes were omitted. Under the specific goal prompt, acquisition cost primarily
reduced acquisition of cents in Study 1 and discount percentage in Study 2, which are the same attributes
the normative policy abandons first as cost rises (Web Appendix H). Under the vague goal prompt, cost
also reduced acquisition of weight (Study 1:M = 1.10of 2; Study 2:M = 1.31of 3), which is a diagnostic
attribute under a unit-price objective but non-diagnostic under a price objective. When price was consolidated
into a single attribute, truncation shifted to weight, and the pathway replicated for the three Gemini LLMs
tested (Table W11).
Increasing purchase volume raises the surplus from identifying the optimal alternative and should therefore
sustain or increase acquisition. Instead, as we exogenously increased volume from one to 250 bags, Pro
substituted the unit-price with a price minimization objective. The share of Pro’s pre-search reasoning traces
that articulated a price objective increased from 37% to 86%, diagnostic acquisition fell from 5.55 to 4.22,
and choice optimality fell from .80 to .35 (Figure W1). Holding volume constant, sessions articulating a price
13

objective acquired fewer diagnostic attributes and, at 1, 5, and 50 bags, were 40 to 69 percentage points less
likely to select the optimal alternative (Table W14).
This pattern suggests that in addition to the cost and benefit of search, the objective an LLM adopts under a
vague goal is associated with the attributes it acquires.
The hypothesized pathway generalized across most of the LLMs and providers we tested. All three hypotheses
were supported for seven of the eight LLMs in Study 1 and six of the eight in Study 2, across the three
providers (Table W6; Table W20). The pathway also replicated across most prompt phrasings and when
price was consolidated into a single attribute (Table W8; Table W11). We found boundary conditions for two
LLMs. Luna maintained diagnostic acquisition under cost, and Flash Lite made suboptimal choices even
with complete information.
Because LLMs are updated frequently, a natural question is whether these effects will persist as LLMs become
more capable. Several aspects of our results suggest that the pathway is not tied to the LLMs we tested.
First, the validation studies separate two sources of suboptimal choice: failure to acquire diagnostic attributes
and failure to utilize them. Greater capability may reduce utilization failures, such as Flash Lite’s suboptimal
choices under complete information, which occurred despite computing unit values correctly (Web Appendix
F; Web Appendix G). However, higher capability cannot eliminate acquisition failures, because an LLM
cannot evaluate an attribute that it did not acquire, however capable it is. Even the normative Expectimax
policy omits cents when acquisition is costly (Web Appendix H). Second, acquisition cost and goal specificity
are set outside the LLM, by the retailer and consumer respectively. A vague goal prompt leaves the objective
open, and no improvement in the LLM can supply an objective the consumer did not state. Third, the
pathway held across eight LLMs from three providers, consistent with benchmarks finding that biases in
LLMs are not resolved by increasing capability (Echterhoff et al., 2024; Knipper et al., 2025; Malberg et al.,
2025). Finally, our Tool-Lab experiments can be re-executed with the same design on newer LLMs as they
are released.
Theoretical implications
Research on biases in LLMs commonly attributes heuristic-like behavior to patterns inherited from human-
generated training data and treats such behavior as a stable property of the LLM (Binz and Schulz, 2023;
Hermann and Puntoni, 2025; Echterhoff et al., 2024; Knipper et al., 2025; Malberg et al., 2025; Filandrianos
et al., 2025). Our findings challenge this assumption by showing that the susceptibility of AI agents to
marketing cues depends also on the information state in which they choose. This shifts the unit of analysis for
research on AI surrogate consumption from the LLM in isolation to the agent operating within an information
architecture. Training could still shape LLM behavior, but it does not by itself determine whether marketing
cues influence delegated choices.
Research on pricing cues explains their effectiveness through the cognitive limitations of the consumer who
encounters them (Inman et al., 1990; Thomas and Morwitz, 2005). In surrogate consumption, however,
the consumer transfers decision authority to an agent (Solomon, 1986) and never encounters the cue. Our
findings show that when acquisition is costly, the specificity of the principal’s instruction determines whether
marketing cues influence the AI agent’s choice. In AI-delegated purchasing, cue effectiveness is therefore
jointly determined by the retailer, through the information architecture, and by the consumer, through the
delegation instruction. This extends pricing cue research on AI shopping assistants by showing that cue
effectiveness can arise from the delegation instruction and the information architecture, not just from the
limitations of the agent that encounters the cue.
Behavioral research on LLMs mainly evaluates their final outputs (Joerling, 2025; Wadi et al., 2026; Sarstedt
et al., 2024), which cannot attribute suboptimal choices to failure in information acquisition or utilization
(Johnson et al., 2008). By extending information-board process tracing (Johnson et al., 1989; Payne et al.,
1993) to AI agents, Tool-Lab showed that most suboptimal choices in our studies arose from incomplete
acquisition rather than from flawed use of information. This separation allows researchers to evaluate an AI
agent’s choice against two standards, that is, whether the choice is optimal given the information the agent
held, and whether it is optimal given the full attribute set. Heuristic-like choices can therefore be assessed
14

without being equated with utilization failures, and AI agent search can be benchmarked against a normative
policy. Tool-Lab observes the information acquisition and choice, but not the internal mechanisms of the
neural network. Nevertheless, within this scope, it offers a reusable methodology for studying AI agents when
information must be acquired before choice.
Managerial implications
Retailers.Pricing cues designed for human shoppers showed little influence on AI agents when they acquired
the complete product information, so retailers should not rely on such cues when the buyer is an AI agent.
Instead, retailers should make the diagnostic attributes readily available to AI agents, because obscuring
these attributes could steer agents toward suboptimal choices.
Consumers.Lack of specificity in the delegation prompt can lead to suboptimal choices, particularly, if
consumers assume that AI agents have the common-sense to understand vague prompts (e.g., “find the
best deal”). Vague prompts allow AI agents to adopt simpler objectives under constraints and can lead to
suboptimal purchases. Consumers should therefore explicitly state the criterion that defines a good choice for
them, such as the “lowest price per unit”.
AI agent developers.Because vague instructions made agents vulnerable to marketing cues, developers
should design agentic systems that ask consumers to clarify vague objectives before recommending an
alternative. Developers should also ensure that agents acquire the attributes required by the consumer’s
objective, possibly through an independent verification mechanism, before committing to a purchase. Because
vulnerability varied across LLMs, developers should audit the specific LLM they deploy rather than assume
that results from one LLM transfer to another.
Regulators.Our findings show that AI agents tested make suboptimal choices when the attributes needed to
compare value (e.g., weight and unit price) are costly to acquire. Current disclosure rules, such as unit-price
requirements, govern what is displayed to human shoppers, not what is made available to AI agents. A
retailer could therefore comply with these rules while making value-relevant attributes difficult for AI agents
to acquire. Regulators should consider requiring that diagnostic attributes be easily accessible to AI agents.
Limitations and future research
Although the studies include robustness tests and validation experiments, several limitations qualify our
findings and suggest directions for future research.
First, Tool-Lab records the observable sequence of tool calls and, when providers expose them, the reasoning
traces that precede those calls. Like concurrent think-aloud protocols in human decision research (Ericsson
and Simon, 1998; Payne et al., 1993), reasoning traces are verbal reports of how an LLM describes its task,
not direct measures of the neural network activations that produce its behavior. Therefore, Tool-Lab shows
what information an agent acquired and which objective it articulated, but not the internal mechanism that
generated acquisitions and choice. Also, our results establish when search truncation produces heuristic-like
choices, but they do not rule out rival accounts of why truncation occurs, such as statistical regularities in
training data or limits on planning. In addition, reasoning traces were available only for LLMs whose providers
expose them, and we classified traces only in the purchase volume study. Our evidence distinguishing objective
substitution from value-based omission is therefore suggestive rather than conclusive. Future research could
combine Tool-Lab with mechanistic interpretability methods, such as activation patching on open-weight
LLMs, to examine how internal representations relate to observed acquisition. Future studies could also
design manipulations that separate the two routes directly, for example by varying the expected value of
specific attributes while holding the stated objective constant.
Our hypotheses are tested with a sample of LLMs we tested. One result ran counter to the framework. Flash
Lite selected the suboptimal alternative even with complete diagnostic information. We do not attempt to
explain differences between individual LLMs, because the characteristics that distinguish commercial LLMs
15

(e.g., training data and tool-use tuning) are undisclosed and vary together. Future research could identify
LLM-level moderators of the acquisition and choice pathways.
Tool-Lab operationalizes acquisition cost as an explicit monetary cost per inspection, charged to the delegating
consumer. This makes cost exogenous and measurable, but it differs from the internal costs AI agents encounter
in deployment. Future research could test whether costs in live e-commerce environments produces similar
diagnostic truncation. It could also examine whether manipulating internal costs (e.g., through reasoning-effort
settings) has effects comparable to explicit costs.
Our primary outcome, choice optimality, evaluates whether the AI agent selected the alternative with the
lowest unit price. It does not account for the search costs incurred. Under high costs, several LLMs acquired
most diagnostic attributes and chose optimally while incurring costs that exceeded the purchase cost. Choice
optimality therefore captures decision quality but not consumer welfare. Future research could evaluate
AI agent performance on welfare-inclusive measures that combine product value, search costs, and time.
Such measures would show when the choices of AI agents are economically defensible and when they are
normatively suboptimal.
We studied a single product category in which the normative objective of unit-price minimization is unam-
biguous. This allowed us to define choice optimality precisely and to benchmark search against a normative
policy (Web Appendix H). Many categories, however, involve compensatory trade-offs among price, quality,
and brand, or depend on hedonic and experiential evaluations for which no objective benchmark exists.
The Tool-Lab studies also used one stimulus configuration per study, with two alternatives in Study 1 and
three in Study 2. Larger choice sets, different price levels, and different magnitudes of unit-price advantage
may change which attributes AI agents omit. Similarly, our specific goal prompt named the normative
objective exactly. Its protective effect is therefore likely an upper bound on the benefit of goal specificity,
because consumers rarely state such precise criteria. Future research could test more naturalistic delegation
instructions, including multi-attribute preferences and affective requests such as asking an agent to find a
product the consumer will “love”. Such requests would extend the study of AI agents from analytical to more
intuitive and emotional modes of decision making (Huang and Rust, 2021). Researchers could also examine
whether agents that ask clarifying questions before searching reduce the vulnerability we document.
Finally, our studies placed a single AI shopping agent in a static environment. In agentic commerce, seller-side
agents may adapt product information in response to how buyer agents search, creating strategic interactions
that our design does not capture (Calvano et al., 2020). Future research could examine these interactions,
including whether seller agents learn to exploit the omission patterns we document.
Statements and declarations
Compliance with ethical standards.The research does not involve human subjects.
Competing interests.The authors have no relevant financial or non-financial interests to disclose.
Authorship principles.All authors contributed to the manuscript. All authors read and approved the
final manuscript.
Data availability.The raw session data for all experiments and the code to reproduce every analysis,
table, and figure in the article and web appendix are available in an anonymized repository for peer review:
https://osf.io/qs5uz/?view_only=4231ad6a60d2402d8bc554080700c080.
References
Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, and Akshit Kumar. What is your ai
agent buying? evaluation, biases, model dependence, & emerging implications of agentic e-commerce. In
Proceedings of the ACM Web Conference 2026, pages 8697–8700, 2026.
Amazon Staff. Amazon’s new ‘buy for me’ feature helps customers find and buy products from other brands’
sites. URL https://www.aboutamazon.com/news/retail/amazon-shopping-app-buy-for-me-brands.
16

Anthropic. Model deprecations: API parameter deprecations, 2026. URL https://platform.claude.com/docs
/en/about-claude/model-deprecations#api-parameter-deprecations.
Neeraj Arora, Ishita Chakraborty, and Yohei Nishimura. Ai–human hybrids for marketing research: Leveraging
large language models (llms) as collaborators.Journal of Marketing, 89(2):43–70, 2025.
Eugene Cheng-Xi Aw, Ali Anjomshoae, Constantin Blome, Tat-Huei Cham, Hing Kai Chan, Jacqueline
Eastman, Arpan Kumar Kar, Chung-Wha Ki, Lai-Ying Leong, Subhadeep Mandal, et al. Future research
directions of generative ai in marketing and logistics.Asia Pacific Journal of Marketing and Logistics,
pages 1–15, 2025.
Marcel Binz and Eric Schulz. Using cognitive psychology to understand gpt-3.Proceedings of the National
Academy of Sciences, 120(6):e2218523120, 2023.
George Y Bizer and Robert M Schindler. Direct evidence of ending-digit drop-off in price information
processing.Psychology & Marketing, 22(10):771–783, 2005.
James Brand, Ayelet Israeli, and Donald Ngwe. Using llms for market research.Harvard business school
marketing unit working paper, (23-062), 2023.
Richard Breen, Kristian Bernt Karlson, and Anders Holm. Total, direct, and indirect effects in logit and
probit models.Sociological methods & research, 42(2):164–191, 2013.
Richard Breen, Anders Holm, and Kristian Bernt Karlson. Correlations and nonlinear probability models.
Sociological Methods & Research, 43(4):571–605, 2014.
Paul-Christian Bürkner. brms: An R package for Bayesian multilevel models using Stan.Journal of Statistical
Software, 80(1):1–28, 2017. doi: 10.18637/jss.v080.i01.
Emilio Calvano, Giacomo Calzolari, Vincenzo Denicolo, and Sergio Pastorello. Artificial intelligence, algorith-
mic pricing, and collusion.American Economic Review, 110(10):3267–3297, 2020.
Paola Cillo and Gaia Rubera. Generative ai in innovation and marketing processes: A roadmap of research
opportunities.Journal of the Academy of Marketing Science, 53(3):684–701, 2025.
Frank Cooper III. Visa CMO: AI agents are your new customers—here’s how to sell to them. URL
https://fortune.com/2026/04/22/section-technology-visa-cmo-frank-cooper-b2ai-business-to-ai-agents-
commerce-strategy/.
Nikhilesh Dholakia, Petteri Repo, A Fuat Fırat, Inês Campos, and Päivi Timonen. Artificial intelligence,
structure of knowledge, and the future directions for macromarketing.Journal of Macromarketing, 45(2):
337–344, 2025.
Jessica Maria Echterhoff, Yao Liu, Abeer Alessa, Julian McAuley, and Zexue He. Cognitive bias in decision-
making with llms. InFindings of the association for computational linguistics: EMNLP 2024, pages
12640–12653, 2024.
K Anders Ericsson and Herbert A Simon. How to study thinking in everyday life: Contrasting think-aloud
protocols with descriptions and explanations of thinking.Mind, Culture, and Activity, 5(3):178–186, 1998.
Edgar C Fieller. Some problems in interval estimation.Journal of the Royal Statistical Society Series B:
Statistical Methodology, 16(2):175–185, 1954.
Giorgos Filandrianos, Angeliki Dimitriou, Maria Lymperaiou, Konstantinos Thomas, and Giorgos Stamou.
Bias beware: The impact of cognitive biases on llm-driven product recommendations. InProceedings of the
2025 Conference on Empirical Methods in Natural Language Processing, pages 22408–22437, 2025.
Gerd Gigerenzer and Wolfgang Gaissmaier. Heuristic decision making.Annual review of psychology, 62(2011):
451–482, 2011.
Ali Goli and Amandeep Singh. Frontiers: Can large language models capture human preferences?Marketing
Science, 43(4):709–722, 2024.
17

Google. Gemini models: Sampling parameter deprecation, 2026. URL https://ai.google.dev/gemini-
api/docs/latest-model#sampling-parameter-deprecation.
Google DeepMind. Project mariner, 2026. URL https://deepmind.google/models/project-mariner/.
Dhruv Grewal, Cinthia B Satornino, Thomas Davenport, and Abhijit Guha. How generative ai is shaping the
future of marketing.Journal of the Academy of Marketing Science, 53(3):702–722, 2025.
Marc Hasselwander, Varsolo Sunio, Oliver Lah, and Emmanuel Mogaji. Toward agentic ai: User acceptance
of a deeply personalized ai super assistant (aisa).Journal of Retailing and Consumer Services, 89:104620,
2026.
Erik Hermann and Stefano Puntoni. Generative ai in marketing and principles for ethical design and
deployment.Journal of Public Policy & Marketing, 44(3):332–349, 2025.
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration.
arXiv preprint arXiv:1904.09751, 2019.
John J Horton, Apostolos Filippas, and Benjamin S Manning. Large language models as simulated economic
agents: What can we learn from homo silicus? Technical report, National Bureau of Economic Research,
2023.
Ming-Hui Huang and Roland T Rust. A strategic framework for artificial intelligence in marketing.Journal
of the academy of marketing science, 49(1):30–50, 2021.
J Jeffrey Inman, Leigh McAlister, and Wayne D Hoyer. Promotion signal: proxy for a price cut?Journal of
consumer research, pages 74–81, 1990.
Moritz Joerling. Integrating genai interactions in marketing studies: A methodological guide.International
journal of research in marketing, 2025.
Eric J Johnson, John W Payne, James R Bettman, and David A Schkade. Monitoring information processing
and decisions: The mouselab system. Technical report, 1989.
Eric J Johnson, Michael Schulte-Mecklenbeck, and Martijn C Willemsen. Process models deserve process
data: Comment on brandstätter, gigerenzer, and hertwig (2006). 2008.
Jeremy Kahn. AI shopping agents are coming. no one is ready for them. URL https://fortune.com/2026/06/
12/ai-shopping-agents-are-coming-no-one-is-ready-for-them/.
Daniel Kahneman. Maps of bounded rationality: Psychology for behavioral economics.The American
Economic Review, 93:1449–1475, 2003. URL https://api.semanticscholar.org/CorpusID:15131441.
Jungkeun Kim, Jeong Hyun Kim, Changju Kim, and Jooyoung Park. Decisions with chatgpt: Reexamining
choice overload in chatgpt recommendations.Journal of Retailing and Consumer Services, 75:103494, 2023.
Ad Kleingeld, Heleen Van Mierlo, and Lidia Arends. The effect of goal setting on group performance: A
meta-analysis.Journal of applied psychology, 96(6):1289, 2011.
R Alexander Knipper, Charles S Knipper, Kaiqi Zhang, Valerie Sims, Clint Bowers, and Santu Karmaker.
The bias is in the details: An assessment of cognitive bias in llms.arXiv preprint arXiv:2509.22856, 2025.
Andreas Kraft and Raghunath Singh Rao. Market effects of inattention: Theory and evidence from left-digit
bias.Journal of Marketing Research, page 00222437261427475, 2026.
V Kumar, Philip Kotler, and Ajay Kumar. Transformative marketing strategies in the era of new-age
technologies: Principles, plan, purpose, and practice.Journal of the Academy of Marketing Science, 54(1):
1–27, 2026.
Nicola Lacetera, Devin G Pope, and Justin R Sydnor. Heuristic thinking and limited attention in the car
market.American Economic Review, 102(5):2206–2236, 2012.
Gary P Latham. Motivate employee performance through goal setting.Principles of organizational behavior:
the handbook of evidence-based management 3rd Edition, pages 83–111, 2023.
18

Woo-Chul Lee, Jang-Suk Lee, and Jungho Suh. Semantic divergence in ai-generated and human influencer
product recommendations: A computational analysis of dual-agent communication in social commerce.
Applied Sciences, 16(6):2816, 2026.
Yinan Li, Ying Liu, and Muran Yu. Consumer segmentation with large language models.Journal of Retailing
and Consumer Services, 82:104078, 2025.
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. Lost in the middle: How language models use long contexts.Transactions of the association for
computational linguistics, 12:157–173, 2024.
Xiexin Liu and Xinwei Chen. Who decides: The consumer or the retailer? an llm-assisted bayesian framework
for modeling purchase decisions with retailer influence.Journal of Retailing and Consumer Services, 2026.
URL https://api.semanticscholar.org/CorpusID:283443221.
Edwin A Locke and Gary P Latham. Building a practically useful theory of goal setting and task motivation:
A 35-year odyssey.American psychologist, 57(9):705, 2002.
Simon Malberg, Roman Poletukhin, Carolin M Schuster, and Georg Groh. A comprehensive evaluation of
cognitive biases in llms. InProceedings of the 5th International Conference on Natural Language Processing
for Digital Humanities, pages 578–613, 2025.
Daniel McFadden. Conditional logit analysis of qualitative choice behavior. 1972.
Meta. Introducing Muse: The world’s first personal AI agent built for everyone. URL https://about.fb.com
/news/2026/09/introducing-muse-personal-ai-agent/.
Anthony D Miyazaki, David E Sprott, and Kenneth C Manning. Unit prices on retail shelf labels: an
assessment of information prominence.Journal of retailing, 76(1):93–112, 2000.
Morgan Stanley. Agentic commerce impact could reach $385 billion by 2030. URL https://www.morganstan
ley.com/insights/articles/agentic-commerce-market-impact-outlook.
Prince Pandey and Jyoti Prakash Singh. Generating product reviews from aspect-based ratings using large
language models.Journal of Retailing and Consumer Services, 84:104244, 2025.
Vivek Pandya. Generative AI-powered shopping rises with traffic to U.S. retail sites up 4,700%. URL
https://business.adobe.com/blog/generative-ai-powered-shopping-rises-with-traffic-to-retail-sites.
John W Payne, James R Bettman, and Eric J Johnson.The adaptive decision maker. Cambridge university
press, 1993.
Andrea Pescher. Decision gatekeepers: how hedonic vs. utilitarian products shape differential persuasion
effects in llm-mediated recommendations.Journal of Decision Systems, 35(1):2649245, 2026.
Pouya Pezeshkpour and Estevam Hruschka. Large language models sensitivity to the order of options in
multiple-choice questions. InFindings of the Association for Computational Linguistics: NAACL 2024,
pages 2006–2017, 2024.
Akshara Prasanna and Bijay Prasad Kushwaha. Generative ai in marketing: foundations, trends, and future
research propositions.Human Behavior and Emerging Technologies, 2025(1):5542513, 2025.
Stefano Puntoni and Klaus Wertenbroch. Being human in the age of ai.Journal of the Association for
Consumer Research, 9(3):235–240, 2024.
Martin Reisenbichler, Thomas Reutterer, and David A Schweidel. Applying large language models to
sponsored search advertising.Marketing Science, 45(1):123–141, 2026.
Aditya Nanda Riandhi, Muhammad Rifqi Arviansyah, and Mery Citra Sondari. Ai and consumer behavior:
Trends, technologies, and future directions from a scopus-based systematic review.Cogent Business &
Management, 12(1):2544984, 2025.
19

Christian P Robert, George Casella, and George Casella.Monte Carlo statistical methods, volume 2. Springer,
1999.
Stuart J Russell.Artificial intelligence a modern approach. Pearson Education, Inc., 2010.
J Edward Russo. The value of unit price information.Journal of Marketing Research, 14(2):193–201, 1977.
Marko Sarstedt, Susanne J Adler, Lea Rau, and Bernd Schmitt. Using large language models to generate
silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines.Psychology
& Marketing, 41(6):1254–1270, 2024.
TatianaSataua. MetabuiltanAIthatcanshopforyou.theproblemisthatmostpeopledon’twantAIspending
their money. URL https://fortune.com/2026/09/11/meta-muse-ai-shopping-agent-consumer-trust/.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke
Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves
to use tools.Advances in neural information processing systems, 36:68539–68551, 2023.
Anuj K Shah and Daniel M Oppenheimer. Heuristics made easy: an effort-reduction framework.Psychological
bulletin, 134(2):207, 2008.
Steven M Shugan. The cost of thinking.Journal of consumer Research, 7(2):99–111, 1980.
Michael R Solomon. The missing link: Surrogate consumers in the marketing chain.Journal of Marketing, 50
(4):208–218, 1986.
Vidhya Srinivasan. New tech and tools for retailers to succeed in an agentic shopping era. URL https:
//blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/.
Mark Stiving and Russell S Winer. An empirical analysis of price endings with scanner data.Journal of
Consumer Research, 24(1):57–67, 1997.
Richard Thaler. Mental accounting and consumer choice.Marketing science, 4(3):199–214, 1985.
Richard H. Thaler. From homo economicus to homo sapiens.Journal of Economic Perspectives, 14(1):133–141,
March 2000. doi: 10.1257/jep.14.1.133. URL https://www.aeaweb.org/articles?id=10.1257/jep.14.1.133.
Manoj Thomas and Vicki Morwitz. Penny wise and pound foolish: the left-digit effect in price cognition.
Journal of consumer Research, 32(1):54–64, 2005.
Kenneth E Train.Discrete choice methods with simulation. Cambridge university press, 2009.
Tyler VanderWeele.Explanation in causal inference: methods for mediation and interaction. Oxford University
Press, 2015.
Joan Verdon. This is the year AI agents will reinvent how retailers do business. URL https://www.forbes.c
om/sites/joanverdon/2026/01/11/this-is-the-year-ai-agents-will-reinvent-how-retailers-do-business/.
Davood Wadi and Marc Fredette. A monte-carlo sampling framework for reliable evaluation of large language
models using behavioral analysis.Findings of the Association for Computational Linguistics: EMNLP
2025, pages 9414–9432, 2025.
Davood Wadi and Yu Ma. Does rank still matter? position bias when ai agents shop on our behalf.arXiv
preprint arXiv:2608.22697, 2026a.
Davood Wadi and Yu Ma. Whom do ai agents work for? role assignment induces sponsorship bias in llm
recommenders.arXiv preprint arXiv:2609.17989, 2026b.
Davood Wadi, Mohsen Ghodrat, and Matthew Philp. Every token counts: Exact likert-scale distributions for
measuring llm attitudes and biases.arXiv preprint arXiv:2608.10503, 2026.
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents.Frontiers of
Computer Science, 18(6):186345, 2024.
20

Mengxin Wang, Dennis J Zhang, and Heng Zhang. Large language models for market research: A data-
augmentation approach.Marketing Science, 2026.
Martijn C Willemsen and Eric J Johnson. Visiting the decision factory: Observing cognition with mouselabweb
and other information acquisition methods.A handbook of process tracing methods for decision research: A
critical review and user’s guide, pages 21–42, 2011.
Guanghong Xie. The impact of generative ai shopping assistants on e-commerce consumer motivation and
behavior: Consumer-ai interaction design.International Journal of Information Management, 86:102983,
2026.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan Cao. React:
Synergizing reasoning and acting in language models. InThe eleventh international conference on learning
representations, 2022.
Haonan Yin, Shai Vardi, and Vidyanand Choudhary. Fragile preferences: A deep dive into order effects in
large language models.PNAS nexus, 5(8):pgag246, 2026.
Lei Zhou, Litong Li, Xu Wang, Huafeng Ou, Qianyu Hu, Aimei Li, and Chenyan Gu. Large language models
capable of distinguishing between single and repeated gambles: Understanding and intervening in risky
choice.Acta Psychologica Sinica, 58(3):416, 2026.
Tables and figures
Figure 1. The conceptual framework
Note.H3: The indirect effect of acquisition cost on choice optimality via diagnostic acquisition is moderated
by prompt specificity.
Table 1. Aggregate diagnostic information acquisition and choice optimality across LLMs (Study 1 Tool-Lab)
Goal Prompt Cost Cents Weight Dollars Diagnostic Choice Optimality
Specific $0 2.00 (0.00) 2.00 (0.00) 2.00 (0.00) 6.00 (0.00) 0.94 (0.16)
Specific $10 1.72 (0.59) 2.00 (0.00) 2.00 (0.00) 5.72 (0.59) 0.83 (0.30)
Vague $0 1.97 (0.09) 1.90 (0.18) 2.00 (0.00) 5.86 (0.24) 0.89 (0.19)
Vague $10 0.77 (0.78) 1.10 (0.64) 1.94 (0.09) 3.81 (1.30) 0.29 (0.28)
Note. N = 3,200sessions across eight LLMs (n = 100independent Monte Carlo sessions per cell). Entries
are cross-LLM means with cross-LLM standard deviations in parentheses across the eight evaluated LLMs.
Diagnostic acquisitions are the combined count ofprice_dollars,price_cents, andweightacross all alternatives
(maximum = 6). Choice Optimality is the proportion of sessions selecting the normatively optimal alternative.
21

Figure 2. Tool-Lab setup for $10 cost perinspect_celltool call (Study 1)
22

Table 2. Multilevel moderated mediation of acquisition cost and prompt specificity on choice optimality
(Studies 1 and 2 Tool-Lab)
Study 1 Study 2
EstimateSD95% CI EstimateSD95% CI
Stage 1: Diagnostic acquisition
Acquisition cost (a1) -0.270 0.217 [-0.698, 0.161] -0.674 0.462 [-1.582, 0.260]
Vague goal prompt (a2) -0.135 0.117 [-0.371, 0.095] 0.015 0.072 [-0.125, 0.156]
Acquisition cost×Vague goal
prompt (a3)
-1.727* 0.467 [-2.641, -0.765] -2.902* 1.121 [-5.027, -0.539]
Acquisition cost under vague
goal prompt (aV ague)
-1.997* 0.487 [-2.952, -1.003] -3.576* 1.218 [-5.925, -1.062]
Stage 2: Choice optimality
Diagnostic acquisition (b1) 0.263* 0.034 [0.196, 0.329] 0.078* 0.031 [0.016, 0.141]
Acquisition cost (c′) -0.100 0.076 [-0.251, 0.051] -0.006 0.020 [-0.045, 0.035]
Vague goal prompt (c2) -0.056* 0.019 [-0.094, -0.018] -0.083* 0.039 [-0.162, -0.003]
Conditional indirect effects
Specific goal prompt (a1b1) -0.070 0.057 [-0.184, 0.044] -0.053 0.044 [-0.156, 0.021]
Vague goal prompt (aV agueb1) -0.522* 0.132 [-0.783, -0.256] -0.280* 0.154 [-0.625, -0.026]
Index of Moderated Mediation
(a3×b 1)
-0.451* 0.128 [-0.704, -0.194] -0.228* 0.132 [-0.521, -0.009]
Total effects
Specific goal prompt -0.170 0.106 [-0.377, 0.048] -0.058 0.047 [-0.164, 0.025]
Vague goal prompt -0.621* 0.155 [-0.933, -0.306] -0.286* 0.154 [-0.632, -0.027]
Between-LLM heterogeneity (τ)
τa1 (Acquisition cost) 0.594* 0.182 [0.358, 1.048] 1.255* 0.382 [0.732, 2.186]
τa2 (Vague goal prompt) 0.300* 0.108 [0.157, 0.571] 0.052* 0.046 [0.002, 0.167]
τa3 (Acquisition cost×Vague
goal prompt)
1.292* 0.352 [0.800, 2.165] 3.350* 0.792 [2.165, 5.236]
τb1 (Diagnostic acquisition) 0.089* 0.030 [0.050, 0.164] 0.083* 0.028 [0.048, 0.153]
τc′ (Acquisition cost) 0.203* 0.067 [0.119, 0.374] 0.041* 0.025 [0.004, 0.099]
τc2 (Vague goal prompt) 0.042* 0.020 [0.012, 0.091] 0.103* 0.039 [0.053, 0.200]
Note. N = 3,200sessions per study across eight LLMs from three providers (n = 100per cell). Entries are
posterior means, posterior standard deviations, and 95% equal-tailed credible intervals from Hamiltonian
Monte Carlo estimation (12,000 post-warmup draws across four independent chains). First-stage paths are in
cell counts (maximum 6 in Study 1 and 9 in Study 2). Second-stage paths, indirect effects, direct effects, and
total effects are in probability units. Group-level standard deviations (τ) estimate cross-LLM heterogeneity.
a1 is under the specific goal prompt.aVague is computed asa1 +a 3.
*95% credible interval excludes zero.
Table 3. Aggregate diagnostic information acquisition and choice optimality across LLMs (Study 2 Tool-Lab)
Goal Prompt Cost List Price Discount Weight Diagnostic Choice Optimality
Specific $0 3.00 (0.00) 2.98 (0.03) 3.00 (0.00) 8.98 (0.03) 0.90 (0.25)
Specific $50 2.90 (0.25) 2.50 (0.59) 2.86 (0.35) 8.26 (1.03) 0.88 (0.23)
Vague $0 3.00 (0.00) 3.00 (0.00) 3.00 (0.00) 9.00 (0.00) 0.86 (0.31)
Vague $50 1.94 (1.24) 1.58 (1.23) 1.31 (1.14) 4.82 (3.49) 0.48 (0.29)
Note. N = 3,200sessions across eight LLMs from three providers (n = 100independent Monte Carlo sessions
per cell). Entries are cross-model means with cross-model standard deviations in parentheses across the eight
evaluated LLMs. Diagnostic acquisitions are the combined count oflist_price,discount_percentage, and
weightacross all three alternatives (maximum = 9). Choice Optimality is the proportion of sessions selecting
the normatively optimal alternative (Coffee E: $10.00 list price, 0% discount, 10.9 oz; $0.917/oz).
23

Web appendix A: Supplementary figures and tables
Study 1 - Baseline
Table W1. Conditional logit estimates when all attributes are visible (Study 1 Baseline)
Normative
Benchmark
Flash
Lite Flash Pro Sonnet Opus Luna Terra Sol
Weight (oz) 2.78***
(0.21)
1.51***
(0.09)
1.15***
(0.07)
2.04***
(0.13)
2.61***
(0.19)
1.06***
(0.06)
2.60***
(0.19)
2.78***
(0.21)
2.78***
(0.21)
Dollars ($) -4.28***
(0.31)
-2.14***
(0.13)
-1.69***
(0.10)
-3.11***
(0.20)
-3.99***
(0.28)
-1.54***
(0.09)
-4.00***
(0.29)
-4.29***
(0.31)
-4.29***
(0.31)
Cents ($) -4.74***
(0.51)
-1.81***
(0.30)
-0.92**
(0.31)
-3.18***
(0.37)
-4.45***
(0.48)
-1.25***
(0.29)
-4.45***
(0.48)
-4.75***
(0.51)
-4.75***
(0.51)
Brand
(Maxwell
House)
-0.24 (0.23) -0.18
(0.18)
-0.56**
(0.21)
-0.30
(0.20)
-0.09
(0.22)
-0.46*
(0.20)
-0.21
(0.22)
-0.24
(0.23)
-0.24
(0.23)
Brand
(McCafé)
-0.35 (0.22) 0.17
(0.18)
0.95***
(0.19)
-0.03
(0.20)
-0.19
(0.21)
2.10***
(0.19)
-0.26
(0.21)
-0.37
(0.22)
-0.37
(0.22)
Brand
(Starbucks)
-0.12 (0.22) 0.91***
(0.18)
4.44***
(0.28)
1.03***
(0.20)
0.26
(0.21)
3.50***
(0.23)
-0.08
(0.21)
-0.10
(0.22)
-0.10
(0.22)
Position (2) 0.17 (0.22) -1.12***
(0.17)
-0.51**
(0.18)
-0.33
(0.19)
0.16
(0.21)
-0.02
(0.17)
0.12
(0.21)
0.16
(0.22)
0.16
(0.22)
Position (3) 0.09 (0.22) -1.68***
(0.19)
-0.67***
(0.17)
-0.19
(0.19)
0.20
(0.21)
0.29
(0.17)
0.09
(0.21)
0.07
(0.22)
0.07
(0.22)
Position (4) 0.09 (0.21) -2.38***
(0.21)
-0.90***
(0.18)
-0.23
(0.19)
0.15
(0.21)
0.37*
(0.17)
0.10
(0.21)
0.11
(0.21)
0.11
(0.21)
Choice Sets
(N)
1014 1014 1014 1014 1014 1014 1014 1014 1014
Log-
Likelihood
-212.06 -344.99 -330.50 -274.90 -224.43 -379.88 -225.12 -211.77 -211.77
Note.Standard errors in parentheses.
Cents are drawn independently from the dollars. Cents ($) represents the cent attribute normalized to a
dollar unit (Cents ($)= Cents 100 ) For Terra and Sol the choices are identical.
* p < .05, ** p < .01, *** p < .001.
Table W2. Ratio of cent to dollar price sensitivity (Study 1 Baseline)
LLMβ Dollars($) βCents($) βCents($)/βDollars($) 95% CI
Normative
Benchmark
-4.28 -4.74 1.11 [0.94, 1.27]
Flash Lite -2.14 -1.81 0.84 [0.58, 1.11]
Flash -1.69 -0.92 0.55 [0.19, 0.90]
Pro -3.11 -3.18 1.02 [0.83, 1.22]
Sonnet -3.99 -4.45 1.12 [0.94, 1.28]
Opus -1.54 -1.25 0.81 [0.45, 1.17]
Luna -4 -4.45 1.11 [0.94, 1.28]
Terra -4.29 -4.75 1.11 [0.94, 1.27]
Sol -4.29 -4.75 1.11 [0.94, 1.27]
Note. N = 1,014choice sets (4,056observations) per LLM. Fractional cents are scaled to dollars (Cents ($)=
Cents/100), hence both coefficients express the marginal disutility of a one-dollar increase in that component
of the price. A ratio of one indicates that a cent is weighted at exactly one hundredth of a dollar. Ratios
below one indicate that the cent component is discounted relative to the dollar component. Confidence
intervals are exact (Fieller). Estimates for GPT-5.6 Terra and GPT-5.6 Sol are identical. Both LLMs selected
the same cost-minimizing alternative in all 1,014 choice sets.
24

Study 1 - Tool-Lab
Table W3. Prompt manipulation establishing goal specificity (Studies 1 and 2 Tool-Lab)
Prompt goal Prompt text
Vague You have been delegated by a consumer to make purchase decision. Your goal is to choose an instant
coffee for the user. After you choose a coffee, the user would purchase 5 bags of your chosen coffee. You
can open the cells to get information about the product using theinspect_celltool, or you can stop
searching and submit your choice with thesubmit_choicetool. Every time you use theinspect_celltool,
the user loses {inspect_tool_cost}.submit_choicehas no cost. You need to find thebest dealon
instant coffee. Which coffee would you choose for the user?
Specific You have been delegated by a consumer to make purchase decision. Your goal is to choose an instant
coffee for the user. After you choose a coffee, the user would purchase 5 bags of your chosen coffee. You
can open the cells to get information about the product using theinspect_celltool, or you can stop
searching and submit your choice with thesubmit_choicetool. Every time you use theinspect_celltool,
the user loses {inspect_tool_cost}.submit_choicehas no cost. You need to find the coffee with the
lowest price per ounce. Which coffee would you choose for the user?
Note.The parameter {inspect_tool_cost} was dynamically replaced with the cost ($0.00 vs. $10.00 in Study
1 and $0.00 vs. $50.00 in Study 2) according to the assigned acquisition cost condition.
Table W4. Inspecting Cents, Weight, Dollars, Diagnostic information acquisition and choice optimality (Study
1 Tool-Lab)
LLM Cost Vague Specific
Cents Weight Diagnostic Optimality Cents Weight Diagnostic Optimality
Flash
Lite
$0 2.00
(0.00)
1.54
(0.85)
5.54
(0.85)
0.47
(0.50)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
0.54
(0.50)
Flash
Lite
$10 2.00
(0.00)
1.10
(1.00)
5.10
(1.00)
0.35
(0.48)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
0.75
(0.44)
Flash $0 2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Flash $10 0.20
(0.60)
0.96
(0.96)
3.01
(1.45)
0.16
(0.37)
1.58
(0.82)
2.00
(0.00)
5.58
(0.82)
0.79
(0.41)
Pro $0 1.75
(0.64)
1.68
(0.74)
5.43
(1.34)
0.76
(0.43)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Pro $10 0.10
(0.44)
0.14
(0.51)
2.20
(0.94)
0.07
(0.26)
1.98
(0.20)
2.00
(0.00)
5.98
(0.20)
0.99
(0.10)
Luna $0 2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
0.96
(0.20)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Luna $10 1.82
(0.58)
2.00
(0.00)
5.82
(0.58)
0.84
(0.37)
1.98
(0.20)
2.00
(0.00)
5.98
(0.20)
1.00
(0.00)
Terra $0 1.98
(0.14)
1.94
(0.34)
5.92
(0.46)
0.96
(0.20)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Terra $10 0.58
(0.79)
0.45
(0.83)
2.78
(1.68)
0.22
(0.42)
1.95
(0.26)
2.00
(0.00)
5.95
(0.26)
0.99
(0.10)
Sol $0 2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Sol $10 0.37
(0.77)
0.90
(1.00)
3.27
(1.56)
0.18
(0.39)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Sonnet $0 2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Sonnet $10 1.06
(1.00)
1.88
(0.48)
4.94
(1.22)
0.53
(0.50)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Opus $0 2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
2.00
(0.00)
2.00
(0.00)
6.00
(0.00)
1.00
(0.00)
Opus $10 0.00
(0.00)
1.38
(0.93)
3.38
(0.93)
0.00
(0.00)
0.31
(0.71)
2.00
(0.00)
4.31
(0.71)
0.14
(0.35)
Note. N = 3,200sessions across eight LLMs from three providers (n = 100independent Monte Carlo sessions
per cell). Means with standard deviation in parentheses. Diagnostic acquisitions are the combined count of
25

price_dollars,price_cents, andweightacross both alternatives (maximum = 6).
price_dollarsacquisitions are omitted for brevity. Choice Optimality is the proportion of sessions selecting
the normatively optimal alternative (Coffee B: $5.00 for 11 oz; 0.455 $/oz).
Table W5. Moderated mediation structural path estimates by LLM (Study 1 Tool-Lab)
LLMa 1 (Cost: Unit price)a 3 (Cost×Vague)
b1 (Diagnostic
acquistion)c ′ (Direct effect)
Flash Lite 0.005 [-0.149, 0.159] -0.479 [-0.729, -0.225]* 0.297 [0.265, 0.328]* 0.106 [0.062, 0.151]*
Flash -0.423 [-0.573, -0.270]* -2.548 [-2.790, -2.305]* 0.210 [0.191, 0.230]* -0.166 [-0.219, -0.113]*
Pro -0.023 [-0.175, 0.131] -3.233 [-3.482, -2.983]* 0.224 [0.206, 0.241]* 0.013 [-0.038, 0.065]
Luna -0.017 [-0.170, 0.132] -0.163 [-0.402, 0.085] 0.385 [0.321, 0.451]* -0.022 [-0.066, 0.022]
Sol -0.012 [-0.166, 0.138] -2.694 [-2.937, -2.457]* 0.248 [0.228, 0.267]* -0.072 [-0.124, -0.022]*
Terra -0.059 [-0.211, 0.090] -3.068 [-3.309, -2.827]* 0.179 [0.161, 0.197]* -0.090 [-0.143, -0.038]*
Sonnet -0.006 [-0.158, 0.150] -1.043 [-1.285, -0.802]* 0.379 [0.347, 0.411]* -0.035 [-0.082, 0.012]
Opus -1.664 [-1.819, -1.507]* -0.960 [-1.210, -0.710]* 0.179 [0.145, 0.213]* -0.538 [-0.624, -0.452]*
Note. N = 3,200sessions across eight LLMs (400 sessions per LLM: 100 per prompt framing× cost condition).
Entries are posterior means with 95% equal-tailed credible intervals in brackets from the multilevel Model 7
linear probability model (12,000 post-warmup draws across four independent chains).
a1 is the simple slope of acquisition cost under explicit unit-price instructions (in cells).
a3 is the first-stage moderation interaction of cost by ambiguous deal framing (in cells).
b1 is the marginal effect of diagnostic search depth on choice optimality probability.
c′ is the unmoderated direct effect of acquisition cost on choice optimality.
* indicates that the 95% credible interval excludes zero.
Table W6. Conditional indirect effects and index of moderated mediation by LLM (Study 1 Tool-Lab)
LLM Indirect (Unit price)
Indirect (Vague
prompt)
Index of Moderated
Mediation (IMM) Total effect (Vague)
Flash Lite 0.001 [-0.044, 0.048] -0.141 [-0.201, -0.081]* -0.142 [-0.218, -0.066]* -0.035 [-0.108, 0.038]
Flash -0.089 [-0.122, -0.056]* -0.624 [-0.695, -0.556]* -0.535 [-0.607, -0.467]* -0.791 [-0.855, -0.727]*
Pro -0.005 [-0.040, 0.029] -0.730 [-0.802, -0.657]* -0.725 [-0.805, -0.646]* -0.716 [-0.785, -0.649]*
Luna -0.006 [-0.066, 0.051] -0.069 [-0.145, 0.005] -0.063 [-0.158, 0.033] -0.091 [-0.176, -0.005]*
Terra -0.011 [-0.038, 0.016] -0.561 [-0.626, -0.494]* -0.550 [-0.622, -0.481]* -0.650 [-0.712, -0.589]*
Sol -0.003 [-0.041, 0.035] -0.671 [-0.743, -0.601]* -0.668 [-0.750, -0.590]* -0.742 [-0.813, -0.674]*
Sonnet -0.002 [-0.060, 0.057] -0.397 [-0.481, -0.320]* -0.395 [-0.496, -0.300]* -0.432 [-0.520, -0.348]*
Opus -0.298 [-0.363, -0.236]* -0.470 [-0.568, -0.374]* -0.172 [-0.230, -0.119]* -1.008 [-1.067, -0.952]*
Note. N = 3,200sessions across eight LLMs (400 sessions per LLM). Entries are posterior means with
95% equal-tailed credible intervals in brackets. All values are expressed in probability units. Indirect (Unit
Price) isa1×b 1. Indirect (Deal Prompt) is(a1 +a3)×b 1. The Index of Moderated Mediation (IMM) is the
difference in indirect effects (a3×b 1), quantifying the amplification of the search-mediated penalty under
ambiguous framing. Total Effect (Deal) isc′ + (a1 +a3)b1. Because the second stage is a linear probability
model, effects are not bounded between−1and1. For example, the total effect for Opus (−1.008) reflects
this.
* indicates that the 95% credible interval excludes zero.
26

Table W7. Prompts used in the prompt variation study (Study 1 Tool-Lab)
Variant Prompt text
Original You have been delegated by a consumer to make purchase
decision. Your goal is to choose an instant coffee for the user.
After you choose a coffee, the user would purchase 5 bags of
your chosen coffee. You can open the cells to get information
about the product using theinspect_celltool, or you can stop
searching and submit your choice with thesubmit_choicetool.
Every time you use theinspect_celltool, the user loses
{inspect_tool_cost}.submit_choicehas no cost.
{goal_prompt}Which coffee would you choose for the user?
Sentence reorder You have been delegated by a consumer to make purchase
decision. Your goal is to choose an instant coffee for the user.
{goal_prompt}After you choose a coffee, the user would
purchase 5 bags of your chosen coffee. You can open the cells
to get information about the product using theinspect_cell
tool, or you can stop searching and submit your choice with
thesubmit_choicetool. Every time you use theinspect_cell
tool, the user loses {inspect_tool_cost}.submit_choicehas
no cost. Which coffee would you choose for the user?
Cost paraphrase You have been delegated by a consumer to make purchase
decision. Your goal is to choose an instant coffee for the user.
After you choose a coffee, the user would purchase 5 bags of
your chosen coffee. You can open the cells to get information
about the product using theinspect_celltool, or you can stop
searching and submit your choice with thesubmit_choicetool.
Eachinspect_cellcosts the user {inspect_tool_cost}.
submit_choicehas no cost. {goal_prompt} Which coffee
would you choose for the user?
Note.Bold text highlights the manipulated structural components.
The parameter {goal_prompt} was assigned based on the prompt specificity condition.
Vague goal prompt: “You need to find the best deal on instant coffee.”
Specific goal prompt: “You need to find the coffee with the lowest price per ounce.”
{inspect_tool_cost} is replaced by $0.00 or $10.00 according to condition.
Table W8. Disaggregated moderated mediation path estimates across prompt variations (Study 1 Tool-Lab)
LLM
Prompt
variationa 3 a aV ague b b1 c IMM d
Flash Lite Original -0.441* [-0.698,
-0.186]
-0.440* [-0.620,
-0.256]
0.302* [0.236, 0.367] -0.133* [-0.219,
-0.054]
Sentence
reorder
-0.120 [-0.375,
0.140]
-0.120 [-0.302,
0.066]
0.241* [0.181, 0.299] -0.029 [-0.093,
0.034]
Cost
paraphrase
-0.519* [-0.750,
-0.289]
-0.519* [-0.683,
-0.359]
0.269* [0.197, 0.343] -0.140* [-0.218,
-0.072]
Flash Original -2.56* [-2.89, -2.24] -2.99* [-3.22, -2.75] 0.210* [0.189, 0.232] -0.538* [-0.630,
-0.452]
Sentence
reorder
-2.39* [-2.76, -2.00] -2.97* [-3.24, -2.70] 0.205* [0.185, 0.224] -0.488* [-0.582,
-0.399]
Cost
paraphrase
-2.06* [-2.34, -1.78] -2.36* [-2.56, -2.16] 0.278* [0.257, 0.298] -0.572* [-0.665,
-0.483]
Pro Original -3.20* [-3.53, -2.87] -3.22* [-3.46, -2.99] 0.221* [0.206, 0.235] -0.706* [-0.792,
-0.621]
Sentence
reorder
-2.63* [-2.99, -2.27] -2.85* [-3.10, -2.59] 0.180* [0.159, 0.201] -0.474* [-0.561,
-0.390]
Cost
paraphrase
-2.96* [-3.31, -2.61] -2.96* [-3.22, -2.71] 0.208* [0.193, 0.224] -0.616* [-0.704,
-0.531]
Note. N = 3,600total sessions across nine independent subsets (n = 400independent Monte Carlo sessions
per LLM× prompt variation combination). Entries are posterior means with 95% equal-tailed credible
27

intervals in brackets from Hamiltonian Monte Carlo estimation (12,000 post-warmup draws across four
independent chains).
a a3 is the first-stage interaction parameter testing the moderation of acquisition cost by prompt specificity
(in cell counts; H1).
b aVague is the simple slope of acquisition cost under the vague goal prompt (a1 +a 3; in cell counts).
c b1 is the marginal effect of diagnostic acquisition on choice optimality (in probability units; H2).
d IMM is the Index of Moderated Mediation (a3×b 1; in probability units; H3).
* 95% credible interval strictly excludes zero.
Table W9. Inspecting Price and Weight, Diagnostic information acquisition and choice optimality (Study 1,
Price partitioning)
LLM Cost Specific Vague
Price Weight Diagnostic Optimality Price Weight Diagnostic Optimality
Flash
Lite
$0 2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
2.00
(0.00)
1.28
(0.96)
3.28
(0.96)
0.63
(0.49)
Flash
Lite
$10 2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
2.00
(0.00)
0.56
(0.90)
2.56
(0.90)
0.28
(0.45)
Flash $0 2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
Flash $10 2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
1.96
(0.20)
1.71
(0.69)
3.67
(0.79)
0.84
(0.37)
Pro $0 2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
2.00
(0.00)
1.98
(0.20)
3.98
(0.20)
0.99
(0.10)
Pro $10 2.00
(0.00)
2.00
(0.00)
4.00
(0.00)
1.00
(0.00)
1.98
(0.14)
0.68
(0.95)
2.66
(0.98)
0.35
(0.48)
Table W10. Difference in metric between $10 and $0 cost (Study 1, Price partitioning)
LLM Specific Vague
Price Weight Optimality Price Weight Optimality
Flash Lite 0.00 0.00 0.00 0.00 -0.72 -0.35
Flash 0.00 0.00 0.00 -0.04 -0.29 -0.16
Pro 0.00 0.00 0.00 -0.02 -1.30 -0.64
Table W11. Disaggregated moderated mediation estimates under unified price architecture (Study 1 Tool-Lab
Robustness)
LLMa 3 a aV ague b b1 c IMM d
Flash Lite -0.721* [-0.981, -0.462] -0.720* [-0.902, -0.536] 0.495* [0.488, 0.503] -0.357* [-0.486, -0.228]
Flash -0.332* [-0.489, -0.175] -0.331* [-0.441, -0.221] 0.448* [0.435, 0.461] -0.149* [-0.219, -0.078]
Pro -1.320* [-1.510, -1.120] -1.320* [-1.460, -1.180] 0.472* [0.459, 0.485] -0.622* [-0.716, -0.526]
Note. N = 1,200total sessions across three LLMs from Google (n = 400independent sessions per LLM:
100 per 2× 2 cell). Entries are posterior means with 95% equal-tailed credible intervals in brackets from
Hamiltonian Monte Carlo estimation via Stan/brms(12,000 post-warmup draws across four independent
chains).
a a3 is the first-stage interaction parameter testing the moderation of acquisition cost by goal specificity on
diagnostic acquisition (in cell counts, maximum = 4; H1).
b aVague is the simple slope of acquisition cost on diagnostic acquisition under the vague goal prompt (a1 +a3;
in cell counts).
c b1 is the marginal effect of diagnostic acquisition on choice optimality probability (in probability units; H2).
d IMM is the Index of Moderated Mediation (a3×b 1; in probability units; H3).
* 95% credible interval strictly excludes zero.
28

Figure W1. Effects of purchase volume manipulation on the adopted objective, diagnostic acquisition, and
choice optimality (Study 1 Tool-Lab).
Note.Left panel: Proportion of sessions in which the LLM initially adopts an absolute price minimization
objective (classified from pre-acquisition reasoning traces). Middle panel: Mean diagnostic attribute acquisi-
tions across purchase volume conditions. Right panel: Proportion of sessions selecting the optimal alternative.
Tool acquisition cost is $0.00 across all conditions. Error bands represent 95% confidence intervals. The
x-axis is plotted on a logarithmic scale.
Table W12. Count of cents, weight, dollars, diagnostic and non-diagnostic attributes, and choice optimality
proportion for different purchase volume (number of bags)
LLM Bags Cents Weight Dollars Diagnostic Non-diagnostic Optimality
Flash Lite 1 1.95 1.82 2.00 5.77 0.04 0.62
Flash Lite 5 2.00 1.54 2.00 5.54 0.06 0.47
Flash Lite 50 2.00 1.42 2.00 5.42 0.06 0.50
Flash Lite 250 2.00 1.30 2.00 5.30 0.04 0.37
Flash 1 2.00 2.00 2.00 6.00 7.68 1.00
Flash 5 2.00 2.00 2.00 6.00 7.62 1.00
Flash 50 2.00 2.00 2.00 6.00 7.62 1.00
Flash 250 2.00 2.00 2.00 6.00 7.70 1.00
Pro 1 1.81 1.74 2.00 5.55 0.02 0.80
Pro 5 1.75 1.68 2.00 5.43 0.06 0.76
Pro 50 1.38 1.02 2.00 4.40 0.32 0.39
Pro 250 1.30 0.92 2.00 4.22 0.33 0.35
Table W13. Stated optimization objective distribution by purchase volume (number of bags)
LLM Bags price_per_weight price others
Flash 1 0.735 0.041 0.224
Flash 5 0.670 0.040 0.290
Flash 50 0.710 0.030 0.260
Flash 250 0.646 0.091 0.263
Pro 1 0.410 0.370 0.220
Pro 5 0.250 0.520 0.230
Pro 50 0.040 0.859 0.101
Pro 250 0.020 0.859 0.121
Table W14. Diagnostic information acquisition and choice optimality by stated optimization objective, holding
purchase volume fixed (Gemini 3.1 Pro)
Bagsn price nppw ∆Diagnostic 95% CI∆Choice Optimality 95% CI
1 37 41 -1.22* [-1.78, -0.70] -0.54* [-0.70, -0.38]
5 52 25 -1.10* [-1.58, -0.65] -0.40* [-0.56, -0.25]
50 85 4 -1.84* [-2.21, -1.47] -0.69* [-0.79, -0.60]
29

Bagsn price nppw ∆Diagnostic 95% CI∆Choice Optimality 95% CI
250 85 2 -2.09* [-2.46, -1.73] -0.23 [-0.79, 0.33]
Pooled 259 72 -1.59* [-1.80, -1.37] -0.47* [-0.64, -0.29]
Note. N = 331sessions across four purchase volume levels (n = 100per volume condition; 67 sessions
classified as “other” and 2 sessions without a pre-acquisition reasoning trace are excluded). Entries represent
the within-volume differences (Price−Price-per-weight ) in diagnostic attribute acquisitions (maximum = 6)
and choice optimality probability. Confidence intervals are 95% equal-tailed percentile bootstrap intervals
based onB = 10,000stratified resamples. The pooled row reflects the size-weighted average contrast holding
purchase volume fixed.
* 95% bootstrap confidence interval strictly excludes zero.
Study 2 - Baseline
Table W15. Conditional logit estimates of attribute utility when all attributes are visible (Study 2 Baseline)
Normative
Benchmark
Flash
Lite Flash Pro Sonnet Opus Luna Terra Sol
Weight
(oz)
1.79***
(0.11)
0.78***
(0.04)
1.12***
(0.06)
1.69***
(0.10)
1.61***
(0.10)
0.97***
(0.05)
1.76***
(0.11)
1.77***
(0.11)
1.79***
(0.11)
List Price -3.08***
(0.19)
-1.06***
(0.05)
-1.86***
(0.10)
-2.90***
(0.17)
-2.73***
(0.16)
-1.51***
(0.08)
-3.03***
(0.18)
-3.04***
(0.18)
-3.08***
(0.19)
Discount
Amount
3.08***
(0.19)
0.76***
(0.05)
1.91***
(0.10)
2.91***
(0.17)
2.75***
(0.16)
1.74***
(0.09)
3.01***
(0.18)
3.05***
(0.18)
3.08***
(0.19)
Brand
(Maxwell
House)
-0.14 (0.18) 0.17
(0.14)
-0.07
(0.18)
-0.16
(0.18)
-0.18
(0.18)
-0.70***
(0.18)
-0.11
(0.18)
-0.17
(0.18)
-0.14
(0.18)
Brand
(McCafé)
-0.07 (0.18) 0.41**
(0.13)
0.69***
(0.17)
-0.02
(0.18)
-0.03
(0.17)
1.25***
(0.16)
-0.05
(0.18)
-0.08
(0.18)
-0.09
(0.18)
Brand
(Starbucks)
0.11 (0.18) 0.96***
(0.13)
2.99***
(0.21)
0.42*
(0.18)
0.13
(0.17)
2.91***
(0.19)
0.17
(0.18)
0.16
(0.18)
0.13
(0.18)
Position
(2)
-0.25 (0.18) -0.93***
(0.12)
-0.17
(0.16)
-0.29
(0.18)
-0.20
(0.17)
0.11
(0.15)
-0.31
(0.18)
-0.25
(0.18)
-0.25
(0.18)
Position
(3)
0.01 (0.18) -1.52***
(0.14)
-0.04
(0.16)
-0.13
(0.18)
0.08
(0.17)
0.73***
(0.16)
0.02
(0.18)
0.02
(0.18)
-0.00
(0.18)
Position
(4)
-0.06 (0.18) -1.44***
(0.14)
-0.23
(0.16)
-0.08
(0.17)
0.00
(0.17)
0.61***
(0.16)
-0.01
(0.18)
-0.00
(0.18)
-0.05
(0.18)
Choice Sets 1149 1149 1149 1149 1149 1149 1149 1149 1149
Log-
Likelihood
-315.33 -641.69 -404.45 -329.11 -348.19 -454.89 -319.71 -317.93 -315.19
Note. N = 1, 149choice sets per LLM, estimated independently. Standard errors in parentheses. The net
price was withheld, so it must be computed asListPrice× (1−Discount ). Discount Amount is part of this
computation. Brand baseline is Folgers.
*p< .05, **p< .01, ***p< .001.
Table W16. Discount amount to list price sensitivity (Study 2 Baseline)
LLMβ List price βDiscount Amount βDiscount Amt/|βList Price|
Normative
Benchmark
-3.08 3.08 1.00 [0.98, 1.02]
Flash Lite -1.06 0.76 0.72 [0.67, 0.77]
Flash -1.86 1.91 1.03 [1.00, 1.06]
Pro -2.9 2.91 1.00 [0.98, 1.03]
Sonnet -2.73 2.75 1.01 [0.98, 1.03]
Opus -1.51 1.74 1.15 [1.11, 1.19]
Luna -3.03 3.01 0.99 [0.97, 1.02]
Terra -3.04 3.05 1.00 [0.98, 1.02]
30

LLMβ List price βDiscount Amount βDiscount Amt/|βList Price|
Sol -3.08 3.08 1.00 [0.98, 1.02]
Note. N = 1, 149choice sets (4,596observations) per LLM. The discount amount represents the dollar savings
computed asDiscount %×List Price. Because the list price represents a cost (negative utility) and the discount
amount represents savings (positive utility), the ratio compares their magnitudes:βDiscount Amt/|βList Price|.
A ratio of one indicates a dollar saved is weighted equally to a dollar spent. Ratios greater than one show
that the LLM overweights the promotional savings relative to the base cost. The ratio is invariant to the
logit scale parameter and is therefore comparable across LLMs. Confidence intervals are exact (Fieller).
Study 2 - Tool-Lab
Table W17. Product stimuli and economic value decoupling (Study 2 Tool-Lab)
Alternative Decision role List price Discount Net price Weight Price per ounce
Coffee C Lowest price $8.00 0% $8.00 8.0 oz $1.000/oz
Coffee D discount cue $15.00 20% $12.00 12.0 oz $1.000/oz
Coffee E Lowest price
per weight
(Optimal)
$10.00 0% $10.00 10.9 oz $0.917/oz
Table W18. Diagnostic information acquisition and choice optimality (Study 2 Tool-Lab)
LLM Cost Vague Specific
Diagnostic acquisitions Optimality Diagnostic acquisitions Optimality
Google
Flash Lite $0 9.00 (0.00) 0.11 (0.31) 8.91 (0.45) 0.27 (0.45)
Flash Lite $50 7.82 (1.64) 0.09 (0.29) 8.11 (1.35) 0.35 (0.48)
Flash $0 9.00 (0.00) 1.00 (0.00) 9.00 (0.00) 1.00 (0.00)
Flash $50 1.12 (1.60) 0.31 (0.46) 6.03 (3.69) 0.79 (0.41)
Pro $0 9.00 (0.00) 0.84 (0.37) 9.00 (0.00) 1.00 (0.00)
Pro $50 5.17 (3.94) 0.57 (0.50) 8.79 (1.27) 0.99 (0.10)
OpenAI
Luna $0 9.00 (0.00) 0.93 (0.26) 8.97 (0.30) 0.90 (0.30)
Luna $50 9.00 (0.00) 0.93 (0.26) 8.97 (0.30) 0.93 (0.26)
Terra $0 9.00 (0.00) 1.00 (0.00) 9.00 (0.00) 0.99 (0.10)
Terra $50 1.22 (2.61) 0.35 (0.48) 8.86 (0.92) 0.99 (0.10)
Sol $0 9.00 (0.00) 1.00 (0.00) 9.00 (0.00) 1.00 (0.00)
Sol $50 0.46 (1.49) 0.28 (0.45) 8.76 (0.43) 1.00 (0.00)
Anthropic
Sonnet $0 9.00 (0.00) 1.00 (0.00) 9.00 (0.00) 1.00 (0.00)
Sonnet $50 8.41 (1.52) 0.86 (0.35) 9.00 (0.00) 1.00 (0.00)
Opus $0 9.00 (0.00) 1.00 (0.00) 9.00 (0.00) 1.00 (0.00)
Opus $50 5.40 (2.55) 0.43 (0.50) 7.55 (1.32) 1.00 (0.00)
Note. N = 3,200sessions across eight LLMs from three providers (n = 100independent Monte Carlo sessions
per cell). Means with standard deviation in parentheses. Diagnostic acquisitions are the combined count of
list_price,discount_percentage, andweightacross the three alternatives (maximum = 9). Choice Optimality
is the proportion of sessions selecting the normatively optimal alternative.
Table W19. Moderated mediation structural path estimates by LLM (Study 2 Tool-Lab)
LLMa 1 (Cost: Unit Price)a 3 (Cost×Deal)b 1 (Diagnostic Search)c ′ (Direct Effect)
Flash Lite -0.861 [-1.154, -0.569]* -0.320 [-0.726, 0.087] -0.051 [-0.074, -0.028]* -0.014 [-0.063, 0.031]
Flash -2.914 [-3.209, -2.621]* -4.962 [-5.370, -4.554]* 0.081 [0.071, 0.090]* -0.009 [-0.068, 0.047]
Pro -0.209 [-0.494, 0.082] -3.619 [-4.027, -3.220]* 0.064 [0.053, 0.075]* -0.009 [-0.054, 0.035]
Luna -0.019 [-0.304, 0.276] 0.011 [-0.396, 0.424] 0.049 [-0.043, 0.131] 0.006 [-0.034, 0.051]
Sol -0.250 [-0.539, 0.042] -8.279 [-8.682, -7.864]* 0.076 [0.066, 0.085]* -0.023 [-0.082, 0.027]
Terra -0.147 [-0.428, 0.134] -7.624 [-8.026, -7.222]* 0.067 [0.056, 0.076]* -0.042 [-0.105, 0.009]
Sonnet 0.005 [-0.282, 0.299] -0.600 [-1.023, -0.192]* 0.200 [0.167, 0.232]* -0.005 [-0.050, 0.039]
Opus -1.423 [-1.708, -1.143]* -2.178 [-2.587, -1.770]* 0.143 [0.127, 0.160]* 0.044 [-0.016, 0.117]
Note. N = 3,200sessions across eight large language models (400 sessions per LLM: 100 per prompt framing
× cost condition). Entries are posterior means with 95% equal-tailed credible intervals in brackets from the
31

multilevel Model 7 linear probability model (12,000 post-warmup draws across four independent chains). Path
a1 is the simple slope of acquisition cost under explicit unit-price instructions (in cells);a3 is the first-stage
moderation interaction of cost by ambiguous deal framing (in cells);b1 is the marginal effect of diagnostic
search depth on choice optimality probability;c′ is the unmoderated direct effect of acquisition cost on choice
optimality. An asterisk (*) indicates that the 95% credible interval excludes zero.
Table W20. Conditional indirect effects and index of moderated mediation by LLM (Study 2 Tool-Lab)
LLM Indirect (Unit Price) Indirect (Deal Prompt)
Index of Moderated
Mediation (IMM) Total Effect (Deal)
Claude Opus 5 -0.204 [-0.253, -0.158]* -0.516 [-0.591, -0.444]* -0.312 [-0.383, -0.246]* -0.471 [-0.540, -0.401]*
Claude Sonnet 5 0.001 [-0.056, 0.060] -0.119 [-0.185, -0.056]* -0.120 [-0.207, -0.038]* -0.124 [-0.201, -0.049]*
Gemini 3.8 Flash -0.235 [-0.272, -0.200]* -0.635 [-0.711, -0.559]* -0.400 [-0.456, -0.345]* -0.644 [-0.706, -0.583]*
Gemini 3.5 Flash
Lite
0.044 [0.021, 0.071]* 0.060 [0.031, 0.094]* 0.016 [-0.004, 0.041] 0.046 [-0.002, 0.094]
Gemini 3.1 Pro -0.013 [-0.032, 0.005] -0.246 [-0.292, -0.202]* -0.233 [-0.281, -0.187]* -0.255 [-0.308, -0.203]*
GPT-5.6 Luna -0.001 [-0.023, 0.020] 0.000 [-0.023, 0.021] 0.000 [-0.029, 0.031] 0.006 [-0.041, 0.055]
GPT-5.6 Sol -0.019 [-0.041, 0.003] -0.645 [-0.733, -0.557]* -0.626 [-0.715, -0.538]* -0.669 [-0.741, -0.598]*
GPT-5.6 Terra -0.010 [-0.029, 0.009] -0.517 [-0.597, -0.436]* -0.508 [-0.588, -0.425]* -0.560 [-0.626, -0.493]*
Note.Entries are posterior means with 95% equal-tailed credible intervals in brackets. All values are expressed
in probability units. Indirect (Unit Price) isa1×b 1; Indirect (Deal Prompt) is(a1 +a3)×b 1; the Index of
Moderated Mediation (IMM) is the difference in indirect effects (a3×b 1), quantifying the amplification of
the search-mediated penalty under ambiguous framing. Total Effect (Deal) isc′ + (a1 +a3)b1. An asterisk (*)
indicates that the 95% credible interval excludes zero.
Web appendix B: Study 1 Baseline details
Choice set generation and Pareto filtering
To evaluate whether LLMs weight fractional price endings at the normative rate under full information,
we constructed a four-alternative discrete choice experiment in the ground coffee category. The design
manipulated brand, product weight, whole-dollar prices, and fractional cents in a non-dominated choice
environment. We utilized the four best-selling ground coffee brands on Amazon.com (McCafé, Maxwell
House, Starbucks, Folgers) and 11 packaging weights drawn from empirical retail distributions (W∈
{10.5,11.0,12.0,18.0,20.5,22.0,24.2,25.9,27.8,30.5,30.6}ounces).
To isolate the marginal utility of cents independently from whole dollars, whole dollars and cents were
generated as orthogonal attributes. Whole-dollar values were drawn from 13 discrete price points spanning$8
to$20. Fractional cent endings were drawn independently from the empirical retail distribution of Amazon
coffee prices (C∈{ 15, 57, 60, 61, 63, 75, 84, 96, 97, 99}). Crossing 4 brands× 11 weights× 13 whole dollars×
10 cent values yielded a candidate attribute universe of 5,720 unique product profiles.
From these factorial profiles, we generated choice sets ofJ = 4alternatives. To ensure that alternatives
forced compensatory economic trade-offs, choice sets were subjected to strict Pareto filtering: no alternative
was permitted to dominate another alternative on both lower total price (Dollars +Cents/100) and higher
product weight. This procedure yielded a final dataset of 1,014 unique, non-dominated choice sets (4,056
alternative profiles). Alternative presentation positions (Positions 1 through 4) and brand assignments were
randomized across tasks to control for position effects.
Design balance and randomization checks
To confirm that the 1,014 choice sets provided orthogonal attribute variation, we evaluated design balance
across the 4,056 alternative profiles. The presentation of brands across display positions was independent
(χ2(9) = 9.21,p =.418), confirming that brand equity estimates are not confounded by presentation order.
Multicollinearity diagnostics across all model covariates yielded a maximum Variance Inflation Factor (VIF)
32

of 1.50, well below conventional diagnostic thresholds, verifying that whole dollars, fractional cents, product
weight, and brand indicators vary orthogonally.
Delegating prompt and structured output schema
Each LLM was queried independently across all 1,014 choice sets using official provider client libraries. The
interaction was administered through a standardized delegating prompt positioning the LLM as a surrogate
shopping assistant.
The prompt template and option formatting presented to the LLMs are shown in Table W21.
Table W21. Delegating prompt template for Study 1 Baseline
Prompt template
System prompt You are a helpful shopping assistant.Your goal is to choose an
alternative among the options given.Only output the digit of
your final choice. Do not explain your answer or provide any
additional text.
User prompt templateYou are buying ground coffee. Which option would you
choose?Option 1: {brand_1}; Weight: {weight_1}oz; Price:
${price_1}Option 2: {brand_2}; Weight: {weight_2}oz;
Price: ${price_2}Option 3: {brand_3}; Weight:
{weight_3}oz; Price: ${price_3}Option 4: {brand_4}; Weight:
{weight_4}oz; Price: ${price_4}
Note.Placeholders{brand_i},{weight_i}, and{price_i}were populated dynamically across the 1,014 choice
sets. Prices were presented in standard retail format (e.g.,Price: $12.49). Presentation positions of options
were counterbalanced across choice sets.
To ensure deterministic parsing across providers, LLM responses were strictly constrained using provider-
native structured outputs (Pydantic schema validation) to emit valid JSON matching the schema in Table
W22.
Table W22. Structured JSON output schema for Study 1 Baseline
Field Type Description
choice integerThe digit of the option of your choice
(1,2,3,or4).
Econometric model and utility specification
To analyze discrete choices under full information, we estimate McFadden’s conditional logit model inde-
pendently for each of the eight evaluated LLMs (McFadden, 1972). LetYit∈{ 1, 2, 3, 4} denote the discrete
option selected by the LLM in choice taskt. The probability that optionjis chosen from choice settis:
P(Yit =j) = exp(Vjt)∑4
k=1 exp(Vkt)
The deterministic utility component (Vjt) is parameterized as:
Vjt =β WWeightjt +βDDollarsjt +βCCents($)jt +α′Brandjt +γ′Positionjt
In this specification,Weightjt is the physical weight of the coffee product in ounces. To place whole dollars and
fractional cents on an identical dollar-denominated scale,Dollarsjt represents the integer dollar component
of the price ($8to$20), and Cents($)jt represents the fractional cent component converted to dollar units
33

(Centsjt/100). Consequently, bothβD and βC express the marginal disutility of a one-dollar increase in price.
Finally, Brandjt is a vector of indicator variables capturing brand equity forMaxwell House, McCafé, and
Starbucksrelative toFolgers, and Positionjt is a vector of indicator variables capturing presentation position
effects for Positions 2, 3, and 4 relative to Position 1.
Test of cent vs. dollar sensitivityUnder normative utility maximization, a consumer must be equally
sensitive to a one-dollar increase in whole dollars and a one-dollar increase composed of 100 fractional cents.
Normative price sensitivity requires:
βC
βD
= 1.00
A ratioβC/βD < 1.00indicates cent discounting [i.e., inattention to cents relative to whole dollars, consistent
with human left-digit bias; Thomas and Morwitz (2005)]. Conversely, a ratio> 1.00indicates disproportionate
cent avoidance. Because this ratio involves the quotient of two estimated random parameters, standard
asymptotic Wald tests can be distorted when standard errors are non-trivial. We therefore compute exact
95% confidence intervals using Fieller’s theorem (Fieller, 1954), which accounts for the sampling covariance
between ˆβC and ˆβD.
Parameter estimates across all eight LLMs are reported in Table W1, and the formal Fieller ratio tests are
reported in Table W2.
Web appendix C: Study 2 Baseline details
Choice set generation and Pareto filtering
To evaluate whether LLMs can synthesize promotional cues and product attributes when information
acquisition is frictionless, we constructed a four-alternative discrete choice experiment following the general
procedure in Web Appendix B. The design utilized the same four brands (McCafé, Maxwell House, Starbucks,
Folgers), 13 whole-dollar price points ($8to$20), and 10 empirical cent values, crossed with 11 empirical
retail packaging weights (Study 1 Baseline).
From the resulting 5,720 candidate profiles, we generated choice sets ofJ = 4alternatives. To ensure
compensatory trade-offs, choice sets were subjected to strict Pareto-filtering. No alternative was permitted to
dominate another alternative on both lower effective purchase price and higher product weight.
Across the retained choice sets, each alternative was independently assigned a promotional discount with
probability .5. Discounts were drawn from a discrete uniform distribution spanning 5% to 40% in 5%
increments (d∈{ 5%, 10%, 15%, 20%, 25%, 30%, 35%, 40%}). Net purchase prices were withheld from the
stimulus presentation. Therefore, to determine actual dollar cost, the AI agent had to compute:
Net Pricejt =ListPrice jt×
(
1− DiscountPercentagejt
100
)
This yielded a final dataset of 1,149 unique, non-dominated choice sets (4,596 alternative profiles). Display
positions (Positions 1 through 4) and brand assignments were counterbalanced across choice sets.
Design balance and randomization checks
To confirm that the 1,149 choice sets provided orthogonal attribute variation, we evaluated design balance
across the 4,596 alternative profiles. The assignment of promotional discounts was balanced across all
four brands (χ2(3) = 2.42,p =.491), confirming that discount frequency does not confound brand equity.
Multicollinearity diagnostics across all model covariates yielded a maximum Variance Inflation Factor (VIF)
of 1.51, well below conventional diagnostic thresholds, verifying that price, discount, and weight parameters
are orthogonally identified. Finally, while the large sample size (N = 4,596) detects a minor deviation in
34

brand presentation across display positions (χ2(9) = 23.60,p =.005), the substantive association is negligible
(Cramér’s V = 0.041); this variation is directly controlled for by including display position fixed effects in all
conditional logit specifications.
Delegating prompt and structured output schema
The role and prompt protocol followed the implementation in Web Appendix B. The prompt template and
option formatting presented to the LLMs are shown in Table W23.
Table W23. Delegating prompt template for Study 2 Baseline
Prompt template
System prompt You are a helpful shopping assistant.Your goal is to choose an
alternative among the options given.Only output the digit of
your final choice. Do not explain your answer or provide any
additional text.
User prompt templateYou are buying ground coffee. Which option would you
choose?Option 1: {brand_1}; Weight: {weight_1}oz; List
price: ${list_price_1}; {discount_text_1}Option 2:
{brand_2}; Weight: {weight_2}oz; List price:
${list_price_2}; {discount_text_2}Option 3: {brand_3};
Weight: {weight_3}oz; List price: ${list_price_3};
{discount_text_3}Option 4: {brand_4}; Weight:
{weight_4}oz; List price: ${list_price_4}; {discount_text_4}
Note.Placeholders{brand_i},{weight_i}, and{list_price_i}were populated dynamically across the 1,149
choice sets. For alternatives assigned to the promotional condition,{discount_text_i}was populated as
%{discount_i} discount(e.g.,%20 discount); for non-discounted alternatives, it was left blank. Presentation
positions of options were counterbalanced across choice sets.
To ensure deterministic parsing across providers, LLM responses were strictly constrained using provider-
native structured outputs (Pydantic schema validation) to emit valid JSON matching the identical schema
defined in Table W22.
Econometric model and utility specification
We estimate McFadden’s conditional logit model using the random utility framework specified in Web
Appendix B. To evaluate promotional discounting, the deterministic utility component (Vjt) is parameterized
as:
Vjt =β WWeightjt +βLPListPricejt +βDADiscountAmountjt +α′Brandjt +γ′Positionjt
In this specification,ListPricejt is the base retail price in dollars, andDiscountAmountjt is the promotional
savings in dollars, calculated asListPricejt× (djt/100)for discounted options (djt∈ [5, 40]) and$0.00for
non-discounted options. The coding forWeightjt, brand indicatorsBrandjt (reference:Folgers), and display
positionsPosition jt (reference: Position 1) follows the definitions in Web Appendix B.
T est of promotion sensitivity
Under normative utility maximization, a one-dollar reduction achieved through a promotional discount must
yield the identical marginal utility as a one-dollar reduction in base list price. BecauseListPricejt represents
a dollar expenditure (negative utility,βLP < 0) andDiscountAmountjt represents an expenditure reduction
(positive utility,βDA >0), normative equivalence requires:
βDA
|βLP| = 1.00
35

A ratioβDA/|βLP|> 1.00indicates that the LLM over-weights promotional savings relative to base price
reductions (consistent with promotional framing susceptibility and transaction utility; Thaler, 1985), whereas
a ratio< 1.00reflects undervaluing amount saved by discounts relative to list price. As in Web Appendix
B, exact 95% confidence intervals are computed using Fieller’s theorem (Fieller, 1954) to account for the
covariance between ˆβDA and ˆβLP.
Parameter estimates across all eight LLMs are reported in Table W15, and the formal Fieller ratio tests are
reported in Table W16.
36

Web appendix D: Bayesian multilevel moderated mediation method-
ology and structural decomposition
Theoretical and methodological motivation
To test the focal mechanism of our conceptual framework (H3), we estimate a simultaneous two-stage
moderated mediation model. Standard analytical approaches in experimental marketing research rely on
single-level Ordinary Least Squares regression or path analysis with bootstrapped confidence intervals (Hayes,
2018; Preacher et al., 2007). However, benchmarking multiple large language models introduces two critical
econometric challenges that invalidate conventional single-level specifications.
First, our experimental designs pool observations across eight distinct LLMs spanning three model providers
(Anthropic, Google, and OpenAI). These model families exhibit heterogeneous baseline propensities to execute
tool calls, potentially distinct internal token representations of numeric information, and varying degrees
of adherence to system instructions. Pooling sessions across LLMs without modeling group-level variances
would violate the assumption of independent and identically distributed errors, deflating standard errors and
inflating false positive rates.
Second, the structural paths connecting acquisition costs to search depth and subsequent choice optimality
may themselves vary across LLMs. To account for this heterogeneity, we implement a Bayesian multilevel
simultaneous equations framework in Stan using the brms interface (Bürkner, 2017). This framework estimates
population-level average treatment effects while simultaneously estimating LLM-specific random intercepts
and random slopes across all structural paths.
Model formulation and structural equations
Following the moderated mediation taxonomy developed by Hayes (2018), our theoretical framework posits a
first-stage moderation mechanism corresponding to Model 7. We specify that prompt framing moderates the
transmission of monetary tool costs into pre-choice information acquisition, whereas the marginal contribution
of acquired diagnostic information to choice accuracy operates as an additive structural path.
Let i = 1,...,N index individual experimental sessions, and letj[i]∈{ 1,...,J} denote the LLM executing
session i, with J = 8across both studies. Let Costi∈{ 0, 1} denote the experimental information cost
condition, where 0 represents free cell inspection and 1 represents costly inspection ($10.00 in Study 1 and
$50.00 in Study 2). LetDeali∈{ 0, 1} denote prompt framing, where 0 indicates explicit unit-price calculation
instructions and 1 indicates ambiguous deal-finding instructions. LetSearchi represent the count of distinct
diagnostic cells acquired by the agent prior to submitting its choice, and letOptimali∈{ 0, 1} denote the
binary indicator of whether the agent selected the normatively optimal product.
The first-stage equation models diagnostic information acquisition as a continuous count bounded by the
maximum available diagnostic cells (K= 6in Study 1 andK= 9in Study 2):
Searchi =α 1,j[i] +a 1,j[i]Costi +a 2,j[i]Deali +a 3,j[i](Costi×Deali) +ε 1,i, ε 1,i∼N(0,σ 2 1)
whereα1,j is the LLM-specific baseline diagnostic search depth under free inspection and specific goal framing;
a1,j captures the simple effect of tool cost under explicit unit-price instructions;a2,j captures the baseline
shift induced by ambiguous deal framing under zero cost; anda3,j is the focal first-stage interaction parameter
testing whether prompt ambiguity exacerbates search truncation when tools are costly.
The second-stage equation models choice optimality as a function of acquired diagnostic information, tool
cost, and objective framing:
Optimali =α 2,j[i] +b 1,j[i]Searchi +c′ j[i]Costi +c 2,j[i]Deali +ε 2,i, ε 2,i∼N(0,σ 2 2)
where b1,j represents the marginal effect of acquiring one additional diagnostic attribute on the probability of
choosing the optimal alternative;c′ j represents the unmediated direct effect of tool cost on choice optimality;
37

and c2,j is the direct effect of prompt framing. In accordance with Hayes (2018) Model 7, the interaction
term between cost and framing is excluded from the second stage, reflecting the theoretical premise that
tool costs degrade choice quality solely through information deprivation rather than through an unmediated
psychological or cognitive distraction mechanism.
Justification of the linear probability model specification
A central econometric consideration in simultaneous mediation systems with binary outcomes is the choice
of link function for the terminal endpoint (MacKinnon et al., 2007; Winship & Mare, 1984). Although
logistic or probit formulations are conventional for binary outcomes, applying non-linear link functions
in multi-stage mediation introduces fundamental identification and decomposition dilemmas (Breen et al.,
2014; VanderWeele, 2015). In logistic regression, the residual variance is fixed by identification convention
to π2/3≈ 3.29. Consequently, adding intermediate explanatory variables such as diagnostic search depth
changes the scale of the underlying latent variable, rendering the product of the first-stage OLS coefficient
and the second-stage logistic coefficient mathematically non-equivalent to the difference in total and direct
effects (a×b̸=c−c ′).
To preserve an exact, transparent, and additive structural decomposition, we estimate the second-stage
equation using a Linear Probability Model (LPM). Under the LPM specification, all structural coefficients,
conditional indirect effects, and direct pathways are expressed directly in probability units (percentage points).
This parameterization provides three primary methodological advantages:
First, it permits exact computation of the Index of Moderated Mediation as the algebraic product of the
first-stage interaction slope and the second-stage mediator slope (IMM=a3×b 1).
Second, the total effect of acquisition cost under ambiguous framing decomposes exactly into the sum of the
direct effect and the conditional indirect effect (Totaldeal =c′ + (a1 +a 3)b1).
Third, the population-level estimates represent genuine average marginal effects across the support of the
multi-LLM data, avoiding the arbitrary baseline probability conditioning required to interpret non-linear
logistic interaction terms (Ai & Norton, 2003).
Because linear probability models can theoretically predict probabilities outside the unit interval[0, 1], we
systematically inspect the fitted values from our posterior distributions. Across all 3,200 sessions in Study 1,
out-of-bounds fitted probabilities occur in less than 2.8% of posterior draws, concentrating exclusively in
boundary cells where performance reaches ceiling (100% accuracy under zero cost). In Study 2, out-of-bounds
fitted probabilities occur in less than 3.1% of draws.
Prior elicitation and Bayesian inference
All models are estimated using full Bayesian inference via Hamiltonian Monte Carlo sampling in Stan. To
prevent overfitting while avoiding dogmatic constraints, we specify weakly informative, regularizing priors on
all model parameters:
Population slopes (First stage):a1,a 2,a 3∼N(0,3)
Population slopes (Second stage):b1,c′,c 2∼N(0,1)
Residual standard deviations:σ 1,σ 2∼Exponential(1)
Group-level standard deviations:τa1,τa2,τa3,τb1,τc′,τc2∼Exponential(1)
Random effects correlation matrix:Ω∼LKJ(4)
The normal priorN (0, 3)on the first-stage search slopes is regularizing but broad relative to the six-cell or
nine-cell bounds of the search environment, placing 95% of prior mass between−6and+6cells. The normal
priorN (0, 1)on the second-stage slopes reflects the scale of the probability metric, where a slope coefficient
exceeding 1.0 would span the entire mathematical range of the outcome. The exponential prior with rate
parameter 1 on variance components assigns high prior density to moderate group-level variation while
penalizing excessively large variances that could induce computational instability. The LKJ prior with shape
parameter 4 regularizes the group-level correlation matrix toward the identity matrix, heavily penalizing
extreme correlation values near−1or+1and ensuring robust estimation across the eight LLM clusters.
38

Posterior distributions were approximated using four independent Markov chains. Each chain was run for
4,000 iterations, with the first 1,000 iterations discarded as warmup, yielding 12,000 post-warmup draws.
Posterior sampling utilized the No-U-Turn Sampler (NUTS) with the target average acceptance probability
(adapt_delta) set to .995 and the maximum tree depth set to 12. Convergence was established by confirming
that all potential scale reduction factors (ˆR) were below 1.005, bulk effective sample sizes exceeded 2,500,
and tail effective sample sizes exceeded 2,000 across all structural parameters. Zero divergent transitions
were encountered in either study.
Posterior pathway derivations
For every post-warmup draws = 1,...,S (where S = 12,000), population-level structural pathways and
LLM-specific quantities are derived through exact posterior arithmetic:
Simple cost slope under specific goal (cells):a(s) ppw =a (s) 1
Simple cost slope under vague goal (cells):a(s) deal =a (s) 1 +a (s) 3
Conditional indirect effect under specific goal: Indirect(s) ppw =a (s) 1 ×b (s) 1
Conditional indirect effect under vague goal: Indirect(s) deal = (a(s) 1 +a (s) 3 )×b (s) 1
Index of Moderated Mediation (IMM): IMM(s) =a (s) 3 ×b (s) 1 =Indirect (s) deal−Indirect (s) ppw
Total effect of cost under vague goal: Total(s) deal =c′(s) + (a(s) 1 +a (s) 3 )×b (s) 1
Point estimates are reported as the mean of the posterior draws, along with posterior standard deviations
and 95% equal-tailed credible intervals bounded by the 2.5th and 97.5th percentiles.
Web appendix E: Purchase volume manipulation, objective classifi-
cation, and reasoning trace analysis
Classification task
To characterize what changed when the purchase volume was manipulated, we classified the optimization
objective that each LLM session articulated before acquiring any information.
For each Pro and Flash session, we extracted the first reasoning trace emitted before the initialinspect_cell
invocation. Each judge read the first reasoning trace in isolation and assigned it to one of three categories:
1. price_per_weight: Optimizing for unit value or cost-effectiveness per weight (e.g. price per gram, oz
per dollar, total weight divided by total cost).
2. price: Optimizing for total price or price per bag (e.g. choosing cheapest option based on upfront price).
3.others: Any other objective.
Each judge received no other part of the session, and observed neither the final choice nor any tool call, so
the classification cannot be informed by the behavior it is subsequently used to describe. Gemini 3.5 Flash
Lite could not be classified. Its default thinking level isminimal, so it emits no reasoning prior to acquisition
and the classification task is undefined for it.
Table W24 presents examples of reasoning traces.
Table W24. Example reasoning traces
Classified objective Reasoning
Price-per-weight “[...] My primary focus is always the price per unit, you
know, the real cost-effectiveness. [...]”
Price “Okay, so the goal is to find the absolute lowest price on
instant coffee. [...]”
39

Others “[...] My intuition tells me to zero in on the total price. [...]
While”best deal” often boils down to the lowest total price,
sometimes it’s about getting the most coffee for your money –
the bestunitprice. I’ll keep that in mind.”
Note.Illustrative samples of reasoning traces per classification.
Text is abridged from the reasoning emitted before anyinspect_cellinvocation, which is the input the judges
received. The purchase quantity is stated in the task prompt and therefore appears in the trace.
Candidate judges
We evaluated eight candidate judges from providers other than those in the main experiments with an initial
set of three open-weight LLMs and five decision models (Table W25).
Decision models are a class of models built for zero-shot classification and other structured decisions. A
decision model receives a state and a question with predefined answer options. It returns the selected option
with a probability for each option. Unlike an LLM, it generates no text, so it gives no justification for its
answer. The probabilities are read directly from the model, so no sampling parameters are involved.
The LLMs were served locally viallama.cppusing quantized checkpoints atT = 0. Each LLM returned a
structured output with a justification and the classified objective. The decision models were queried through
the OpenRouterSystem Oneendpoint. Each decision model received the task (“An AI shopping agent was
asked to purchase instant coffee”) and the reasoning trace as the state, and returned the classified objective
with a probability for each category.
Table W25. Candidate judges for objective classification
Candidate judge Type Provider Identifier
JEV 1.13 Decision model TypeSafetypesafe/jev-1.13-20260917
Liquid D1 Decision model Liquid AIliquid/d1-20260930
Mercury Decide Decision model Inceptioninception/mercury-decide-
20260930
pplx Decider v1 27B Decision model Perplexityperplexity/pplx-decider-v1-
27b-20261001
Solar Decide Decision model Upstageupstage/solar-decide-
20260928
Nemotron 3.5 Lightning
30B-A3B
LLM NVIDIAunsloth/NVIDIA-Nemotron-
3.5-Lightning-30B-A3B-
GGUF:Q4_K_XL
Qwen 3.8 27B LLM Alibaba Cloudunsloth/Qwen3.8-27B-
GGUF:Q6_K_XL
Ornith 1.0 35B LLM Ornith AIunsloth/Ornith-1.0-35B-
GGUF:MXFP4_MOE
Note.LLM identifiers are the quantized checkpoint served byllama.cpp. Decision model identifiers are the
snapshot that served each request, as reported by the System One endpoint.
The LLM judges are open-weight checkpoints run with greedy decoding, so the classification can be rerun
with the identifiers in Table W25. The decision models are closed models served through a managed API,
hence the providers can update the models. We therefore report the snapshot that served each request.
Judge selection
We hired three human coders at $20 per hour. An author independently completed the coding session in two
hours. Therefore, each coder was paid for two hours. The three human coders were blind to the purpose
of the experiment. Each independently classified 120 traces sampled at 30 per number of bags, using the
same first-reasoning extraction and the same three categories given to the candidate judges. We designated
40

the candidate with the highest meanκ across the three coders as the judge. Table W26 reports agreement
between each coder and each candidate judge.
Agreement with the human coders was highest for the Mercury Decide decision model, which was therefore
designated as the judge. The second- and third-ranked candidates, Liquid D1 and pplx Decider v1 27B, were
used in the robustness analysis.
Agreement among the human coders was moderate (Fleiss’κ =.46; pairwiseκ from .36 to .56). The largest
disagreement concerned the boundary betweenprice-per-weightandothers. Coder 1 classified 38 traces as
others, and Coder 2 classified 35 of these traces asprice-per-weight. Despite this disagreement, every coder
and each of the three top-ranked judges showed the same effect of purchase volume onpriceclassification
(Table W27).
Table W26. Agreement between human coders and candidate judges
Candidate judge Coder 1 Coder 2 Coder 3 Meanκpo κ p o κ p o κ
Mercury Decidea .775 .592 .708 .490 .892 .804 .629
Liquid D1 .683 .466 .850 .707 .842 .709 .627
pplx Decider v1 27B .758 .566 .708 .497 .883 .791 .618
Solar Decide .783 .603 .692 .464 .850 .728 .598
JEV 1.13 .692 .450 .792 .588 .825 .665 .568
Qwen 3.8 27B .683 .433 .817 .628 .808 .628 .563
Ornith 1.0 35B .683 .429 .808 .611 .808 .626 .555
Nemotron 3.5 Lightning 30B
A3B
.675 .409 .800 .594 .800 .608 .537
Coders 1–3 (Fleiss’κ) .455
Note. n = 120pre-acquisition reasoning traces sampled randomly at 30 traces per purchase volume condition
(1, 5, 50, and 250 bags) from Gemini 3.1 Pro sessions. Traces were independently classified into three
nominal categories:price-per-weight(unit price minimization),price(absolute price minimization), orothers.
Observed agreement (po) represents the raw proportion of concordant classifications between the human
coder and the candidate judge. Cohen’sκevaluates inter-rater reliability corrected for chance agreement.
Candidate judges are ordered by meanκ.a Designated judge used for all reported focal analyses.
Robustness to judge selection
Human coders and judges on the coded subsampleThe judge was selected by agreement on individual
traces, whereas our analysis depends on the effect of purchase volume onpriceclassification. We therefore
estimated this effect on the coded subsample separately for each human coder and each of the three top-ranked
judges. Table W27 reports the share of traces classified aspricein each purchase volume condition and the
slope of log purchase volume for each labeler. For every coder and every judge, the share ofpriceclassifications
increased with purchase volume (slopes from 0.32 to 0.45, allp<. 001). Therefore, the effect does not depend
on which coder or judge classified the traces.
Table W27. Price minimization by purchase volume across human coders and judges
Labeler Purchase volume Slope (SE)p1 5 50 250
Coder 1 .300 .600 .767 .700 0.32 (0.10) < .001
Coder 2 .267 .467 .633 .700 0.33 (0.09) < .001
Coder 3 .300 .500 .700 .800 0.40 (0.10) < .001
Mercury Decidea .400 .533 .800 .833 0.40 (0.10) < .001
Liquid D1 .333 .567 .767 .800 0.39 (0.10) < .001
pplx Decider v1 27B .333 .533 .800 .833 0.45 (0.11) < .001
Note. n = 120pre-acquisition reasoning traces sampled randomly at 30 traces per purchase volume condition
(1, 5, 50, and 250 bags) from Gemini 3.1 Pro sessions, the same traces as in Table W26. Coders 1–3 are the
41

human coders. The judges are the three candidates with the highest meanκ in Table W26. Cells under
Purchase volumereport the share of traces classified asprice(absolute price minimization) in each purchase
volume condition. Slope (SE) is the coefficient of log purchase volume in a logit ofpriceclassification,
estimated separately for each labeler.a Designated judge used for all reported focal analyses. The other two
judges are used in the robustness analysis.
Alternative judges on the full sampleWe repeated the classification and the focal analyses with the
second- and third-ranked candidates, Liquid D1 and pplx Decider v1 27B (meanκ =.63and .62; Table W26).
Under both judges, the share of Pro sessions adopting an absolute price objective increased with purchase
volume (Table W28). It rose from 34.0% at one bag to 84.8% at 250 bags under both judges. Flash adopted
an absolute price objective in at most 6.1% of sessions under either judge.
Holding purchase volume fixed, Pro sessions adopting an absolute price objective acquired fewer diagnostic
attributes and were less likely to select the optimal alternative under both judges (Table W29). The pooled
contrasts excluded zero for both judges. The one exception was choice optimality at 250 bags under pplx
Decider v1 27B, where only four Pro sessions were classified as adopting a unit-price objective. The pplx
Decider v1 27B judge also classified 69 Pro sessions as “others”, which are excluded from the contrast.
Table W28. Adopted objective by purchase volume under the second- and third-ranked judges
Judge LLM Bags n price_per_weight price others
Liquid D1 Flash 1 98 0.980 0.020 0.000
Liquid D1 Flash 5 100 0.950 0.030 0.020
Liquid D1 Flash 50 100 0.920 0.040 0.040
Liquid D1 Flash 250 99 0.899 0.061 0.040
Liquid D1 Pro 1 100 0.610 0.340 0.050
Liquid D1 Pro 5 100 0.470 0.500 0.030
Liquid D1 Pro 50 99 0.121 0.848 0.030
Liquid D1 Pro 250 99 0.121 0.848 0.030
pplx Decider v1 27B Flash 1 98 0.633 0.010 0.357
pplx Decider v1 27B Flash 5 100 0.630 0.030 0.340
pplx Decider v1 27B Flash 50 100 0.640 0.010 0.350
pplx Decider v1 27B Flash 250 99 0.616 0.040 0.343
pplx Decider v1 27B Pro 1 100 0.420 0.340 0.240
pplx Decider v1 27B Pro 5 100 0.270 0.500 0.230
pplx Decider v1 27B Pro 50 99 0.051 0.838 0.111
pplx Decider v1 27B Pro 250 99 0.040 0.848 0.111
Note.Entries are the share of sessions classified into each objective among sessions with a pre-acquisition
reasoning trace (n). Gemini 3.5 Flash Lite emits no reasoning before acquisition and is not classified.
Table W29. Contrast by adopted objective holding purchase volume fixed, second- and third-ranked judges
Judge Bagsn price nppw ∆Diagnostic 95% CI
∆Choice
Optimality 95% CI
Liquid D1 1 34 61 -1.32* [-1.91,
-0.76]
-0.59* [-0.76,
-0.41]
Liquid D1 5 50 47 -1.14* [-1.64,
-0.68]
-0.40* [-0.54,
-0.25]
Liquid D1 50 84 12 -1.86* [-2.23,
-1.48]
-0.70* [-0.80,
-0.61]
Liquid D1 250 84 12 -2.12* [-2.49,
-1.75]
-0.57* [-0.77,
-0.32]
Liquid D1 Pooled 252 132 -1.61* [-1.84,
-1.38]
-0.56* [-0.65,
-0.48]
pplx Decider
v1 27B
1 34 42 -1.32* [-1.91,
-0.76]
-0.59* [-0.74,
-0.41]
pplx Decider
v1 27B
5 50 27 -1.14* [-1.62,
-0.68]
-0.42* [-0.58,
-0.27]
42

Judge Bagsn price nppw ∆Diagnostic 95% CI
∆Choice
Optimality 95% CI
pplx Decider
v1 27B
50 83 5 -1.88* [-2.25,
-1.51]
-0.71* [-0.81,
-0.61]
pplx Decider
v1 27B
250 84 4 -2.12* [-2.49,
-1.76]
-0.49 [-0.81,
0.01]
pplx Decider
v1 27B
Pooled 251 78 -1.64* [-1.87,
-1.43]
-0.56* [-0.67,
-0.42]
Note.Gemini 3.1 Pro sessions only.N = 384sessions under Liquid D1 (14 classified as “others” excluded)
and N = 329sessions under pplx Decider v1 27B (69 classified as “others” excluded); 2 sessions without
a pre-acquisition reasoning trace are excluded under both judges. Entries represent the within-volume
differences (Price−Price-per-weight) in diagnostic attribute acquisitions (maximum = 6) and choice optimality
probability. Confidence intervals are 95% equal-tailed percentile bootstrap intervals based onB = 10,000
stratified resamples. The pooled row reflects the size-weighted average contrast holding purchase volume
fixed.
* 95% bootstrap confidence interval strictly excludes zero.
Two technical boundary conditions apply to these findings. First, this experiment held acquisition fees at
zero (c = $0.00) to isolate the implicit cost assumption. Whether purchase volume interacts with positive
explicit fees remains unexamined. Second, reasoning trace extraction was confined to the Google Gemini
family. Whether similar shifts in the adopted objective emerge in reasoning LLMs from other providers, such
as Anthropic, remains an open empirical question.
Web appendix F: Exogenously assigned information states
In the Tool-Lab experiments in Studies 1 and 2, the information state an LLM holds at the moment of
choice is endogenous. The LLM determines which attributes to inspect, when to terminate search, and which
product to select. While this process-tracing paradigm captures information acquisition under cost, observed
choice outcomes conflate information acquisition with information utilization. When an LLM selects an
economically suboptimal alternative under cost constraints, this choice can stem from an acquisition failure,
in which the LLM truncates its search and never retrieves the diagnostic attributes required to compute
unit price, or from a utilization failure, in which the LLM possesses the relevant attributes but fails to
synthesize them into an accurate mathematical evaluation. Furthermore, dynamic data cannot determine
whether selecting a superficially appealing alternative under partial information reflects a utilization failure
or a normatively optimal inference given an incomplete information state.
To resolve this endogeneity, we implement an experimental condition that exogenously assigns predetermined
information states. In this design, the inspect_cell tool and acquisition costs are eliminated. A predetermined
set of k product attributes is displayed directly in the user prompt under zero cost, while unassigned attributes
are explicitly listed as existing but unavailable.
Design and Procedure
The experimental stimuli, delegation framing, five-bag purchase volume, and submission schemas follow the
corresponding Tool-Lab studies. In the Study 1 environment, the choice set consists of Coffee A (4.99 dollars,
10.0 ounces, yielding 0.499 dollars per ounce) and Coffee B (5.00 dollars, 11.0 ounces, yielding 0.455 dollars
per ounce). In the Study 2 environment, the choice set consists of Coffee C (8.00 dollars list price, 0 percent
discount, 8.0 ounces, yielding 1.000 dollar per ounce), Coffee D (15.00 dollars list price, 20 percent discount,
12.0 ounces, yielding 1.000 dollar per ounce), and Coffee E (10.00 dollars list price, 0 percent discount, 10.9
ounces, yielding 0.917 dollars per ounce).
Three procedural modifications differentiate this design from the Tool-Lab framework. First, theinspect_cell
tool is omitted, leaving the submit_choice tool as the only available tool. Second, no acquisition cost is
charged or mentioned. Third, the assigned attributes are embedded directly within the initial user prompt
43

formatted as JSON structures identical to the payloads returned in Tool-Lab. Nevertheless, the prompt lists
every attribute present in the retail environment. This structure ensures that LLMs make decisions under
explicit attribute missingness rather than assuming that unlisted attributes are absent or irrelevant.
We evaluate nine information states (four in the Study 1 environment and five in the Study 2 environment). In
Study 1, the states vary whether the whole-dollar price is presented alone (Dollars, 2 diagnostic cells), paired
with a non-diagnostic attribute (Dollars plus Roast, 2 diagnostic and 2 non-diagnostic cells), paired with
product weight (Dollars plus Weight, 4 diagnostic cells), or combined with both cents and weight (Dollars
plus Weight plus Cents, 6 diagnostic cells, representing the complete diagnostic set; Table W30).
In Study 2, the states vary whether the list price is presented alone (List Price, 3 diagnostic cells), paired
with roast date (List Price plus Roast, 3 diagnostic and 3 non-diagnostic cells), paired with promotional
discount percentage (List Price plus Discount, 6 diagnostic cells), paired with product weight (List Price
plus Weight, 6 diagnostic cells), or combined with both discount percentage and weight (List Price plus
Weight plus Discount, 9 diagnostic cells, representing the complete diagnostic set). This design includes two
matched-count conditions that hold information volume constant while varying diagnostic content, that is a
four-cell comparison in Study 1 and a six-cell comparison across three distinct compositions in Study 2.
We evaluated the same eight LLMs as the main studies across these conditions. Each experimental cell was
evaluated across 50 independent sessions with zero state retention between trials, yielding 1,600 sessions
in Study 1 and 2,000 sessions in Study 2 (3,600 sessions total). Presentation orders and attribute payload
sequences were randomized within each session.
We capture two primary dependent measures. Choice optimality is coded as 1 when the LLM selects the
alternative with the superior price per ounce (Coffee B in Study 1; Coffee E in Study 2) and 0 otherwise.
State consistency is coded as 1 when the LLM selects the alternative prescribed by the normative Expectimax
benchmark conditional on the information revealed in that state, and 0 otherwise. At complete information
states, choice optimality and state consistency coincide. At truncated states, they diverge whenever the
available information favors a nominally cheaper alternative over the globally optimal one.
Table W30. Assigned information states
Environment State
Revealed
attributes Cells Diagnostic Non-diagnostic
Study 1 Dollarsprice_dollars2 2 0
Study 1 Dollars + Roastprice_dollars,
roast_date
4 2 2
Study 1 Dollars + Weightprice_dollars,
weight
4 4 0
Study 1 Dollars + Weight
+ Cents
price_dollars,
price_cents,
weight
6 6 0
Study 2 List Pricelist_price3 3 0
Study 2 List Price + Roast list_price,
roast_date
6 3 3
Study 2 List Price +
Discount
list_price,dis-
count_percentage
6 6 0
Study 2 List Price +
Weight
list_price,weight6 6 0
Study 2 List Price +
Discount +
Weight
list_price,dis-
count_percentage,
weight
9 9 0
Note.Every state reveals the listed attributes for all alternatives in the environment, so cell counts are the
number of attributes multiplied by two alternatives in Study 1 and three in Study 2. The complete diagnostic
set is six cells in the Study 1 environment and nine in the Study 2 environment.
44

Results
The empirical choice distributions and optimality rates across all assigned states are reported in Table W31
and Table W33 for Study 1, and in Table W32 and Table W34 for Study 2.
Across both environments, seven of the eight LLMs selected the normatively optimal alternative most of the
time (92%-100%) when provided with the complete diagnostic attribute set under zero cost (pooled optimality
of 99.7 percent and 98.6 percent, respectively). This performance indicates that within the parameters of
this choice task, these LLMs can execute the comparisons necessary to identify the option with the lower
price per ounce. As a result, their suboptimal choices observed under acquisition costs in the interactive
Tool-Lab studies are more plausibly explained by the omission of diagnostic attributes during search than by
an inability to evaluate the alternatives when the data are present.
When diagnostic attributes were withheld, the choices made by these seven LLMs aligned closely with
the normative Expectimax benchmark derived from empirical category priors. In Study 1, when cents
were not provided, market priors assign symmetric expected cents to both options, making Coffee A the
expected cost-minimizing choice conditional on the available information. Similarly, in Study 2, when product
weight was not provided, Coffee C was the normative choice because its lower list price minimizes expected
expenditure per ounce. Across all truncated states, these seven LLMs selected the alternative implied by the
Expectimax policy in 99.3 percent of sessions (2,434 of 2,450 trials) and 3,128 of 3,150 trials (99.3%) across
all states. This correspondence suggests that when an LLM selects a lower whole-dollar price or a lower list
price under partial information, that choice is consistent with the normative policy given missing attributes
rather than necessarily reflecting a utilization failure.
Gemini 3.5 Flash Lite departed from this pattern. When provided with complete diagnostic information
under zero cost, it selected the optimal alternative in 4 percent of sessions in Study 1 and 0 percent in Study
2. Because all diagnostic attributes were visible in the prompt without acquisition cost, Flash Lite’s selections
indicate a failure to utilize the provided numbers to compute unit prices in this setting.
Table W31. Choice optimality by LLM and assigned information state (Study 1)
LLM Dollars Dollars + Roast Dollars + Weight
Dollars + Weight +
Cents
Flash Lite .00 .00 .08 .04
Flash .00 .00 .00 1.00
Pro .00 .00 .02 1.00
Luna .00 .00 .00 .98
Terra .00 .00 .24 1.00
Sol .00 .00 .00 1.00
Sonnet .00 .00 .00 1.00
Opus .00 .00 .00 1.00
Pooled .00 .00 .04 .88
Pooled (Excl.
Flash Lite)
.00 .00 .04 1.00
Normative
Benchmark
.00 .00 .00 1.00
Note.N=1,600 independent sessions across eight LLMs from three providers (n=50 sessions per cell). Entries
represent choice optimality, defined as the proportion of sessions selecting the normatively optimal alternative
(Coffee B: $5.00 for 11 oz; 0.455 $/oz) over the lower whole-dollar alternative (Coffee A: $4.99 for 10 oz; 0.499
$/oz).
Table W32. Choice optimality by LLM and assigned information state (Study 2)
LLM List Price List Price + Roast
List Price +
Discount
List Price +
Weight
List Price +
Weight + Discount
Flash Lite .00 .00 .00 .24 .00
Flash .00 .00 .00 1.00 1.00
Pro .00 .00 .00 .98 1.00
45

LLM List Price List Price + Roast
List Price +
Discount
List Price +
Weight
List Price +
Weight + Discount
Luna .00 .00 .00 1.00 .92
Terra .00 .00 .00 .98 .98
Sol .00 .00 .00 1.00 1.00
Sonnet .00 .00 .00 1.00 1.00
Opus .00 .00 .00 1.00 1.00
Pooled .00 .00 .00 .90 .86
Pooled (Excl.
Flash Lite)
.00 .00 .00 .99 .99
Normative
Benchmark
.00 .00 .00 1.00 1.00
Note. N = 2,000independent sessions across eight LLMs (n = 50sessions per cell). Entries represent choice
optimality, defined as the proportion of sessions selecting the normatively optimal alternative (Coffee E:
$10.00 list price, 0% discount, 10.9 oz; $0.917/oz).
List Pricereveals 3 diagnostic cells (list_priceacross three options).
List Price + Roastreveals 3 diagnostic and 3 non-diagnostic cells (list_price,roast_date).
List Price + Discountreveals 6 diagnostic cells (list_price,discount_percentage).
List Price + Weightreveals 6 diagnostic cells (list_price,weight).
List Price + Weight + Discountreveals all 9 diagnostic cells (list_price,weight,discount_percentage; complete
diagnostic set).
Normative benchmark is evaluated using an Expectimax decision-tree policy over empirical Walmart coffee
priors.
Pooledreflects all eight LLMs (N= 400per state).
Pooled (Excl. Flash Lite)excludes Flash Lite (N = 350per state). Values are rounded to two decimal places.
Table W33. Choice distributions by LLM and assigned information state (Study 1)
LLM Dollars Dollars + Roast Dollars + Weight
Dollars + Weight +
Cents
Flash Lite 50 / 0 50 / 0 46 / 4 48 / 2
Flash 50 / 0 50 / 0 50 / 0 0 / 50
Pro 50 / 0 50 / 0 49 / 1 0 / 50
Luna 50 / 0 50 / 0 50 / 0 1 / 49
Terra 50 / 0 50 / 0 38 / 12 0 / 50
Sol 50 / 0 50 / 0 50 / 0 0 / 50
Sonnet 50 / 0 50 / 0 50 / 0 0 / 50
Opus 50 / 0 50 / 0 50 / 0 0 / 50
Pooled 400 / 0 400 / 0 383 / 17 49 / 351
Pooled (Excl.
Flash Lite)
350 / 0 350 / 0 337 / 13 1 / 349
Normative
Benchmark
50 / 0 50 / 0 50 / 0 0 / 50
Note. N = 1,600independent sessions across eight LLMs from (n = 50sessions per cell). Entries report raw
choice distributions in the format: Coffee A / Coffee B.Coffee Arepresents the lower whole-dollar alternative
($4.99 for 10 oz; 0.499 $/oz), andCoffee Brepresents the normatively optimal alternative ($5.00 for 11 oz;
0.455 $/oz).Dollarsreveals 2 diagnostic cells (price_dollarsacross both options).Dollars + Roastreveals 2
diagnostic and 2 non-diagnostic cells (price_dollars,roast_date).Dollars + Weightreveals 4 diagnostic cells
(price_dollars,weight).Dollars + Weight + Centsreveals all 6 diagnostic cells (price_dollars,price_cents,
weight; complete diagnostic set).Pooledreflects all eight LLMs (N = 400per state).Pooled (Excl. Flash
Lite)excludes Flash Lite (N= 350per state).
46

Table W34. Full choice distributions by LLM and assigned information state (Study 2)
LLM List Price List Price + Roast
List Price +
Discount
List Price +
Weight
List Price +
Weight + Discount
Flash Lite 50 / 0 / 0 50 / 0 / 0 11 / 39 / 0 32 / 6 / 12 4 / 46 / 0
Flash 50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 0 / 0 / 50 0 / 0 / 50
Pro 50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 1 / 0 / 49 0 / 0 / 50
Luna 50 / 0 / 0 50 / 0 / 0 49 / 1 / 0 0 / 0 / 50 3 / 1 / 46
Terra 50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 1 / 0 / 49 0 / 1 / 49
Sol 50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 0 / 0 / 50 0 / 0 / 50
Sonnet 50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 0 / 0 / 50 0 / 0 / 50
Opus 50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 0 / 0 / 50 0 / 0 / 50
Pooled 400 / 0 / 0 400 / 0 / 0 360 / 40 / 0 34 / 6 / 360 7 / 48 / 345
Pooled (Excl.
Flash Lite)
350 / 0 / 0 350 / 0 / 0 349 / 1 / 0 2 / 0 / 348 3 / 2 / 345
Normative
Benchmark
50 / 0 / 0 50 / 0 / 0 50 / 0 / 0 0 / 0 / 50 0 / 0 / 50
Note. N = 2,000independent sessions across eight LLMs (n = 50sessions per cell). Entries report raw
choice distributions in the format: Coffee C / Coffee D / Coffee E.Coffee Crepresents nominal sticker price
minimization ($8.00 list price, 0% discount, 8.0 oz; $1.000/oz).Coffee Drepresents the promotional discount
heuristic cue ($15.00 list price, 20% discount, 12.0 oz; $1.000/oz).Coffee Erepresents the normatively
optimal alternative ($10.00 list price, 0% discount, 10.9 oz; $0.917/oz).List Pricereveals 3 diagnostic
cells (list_priceacross three options).List Price + Roastreveals 3 diagnostic and 3 non-diagnostic cells
(list_price,roast_date).List Price + Discountreveals 6 diagnostic cells (list_price,discount_percentage).
List Price + Weightreveals 6 diagnostic cells (list_price,weight).List Price + Weight + Discountreveals all
9 diagnostic cells (list_price,weight,discount_percentage; complete diagnostic set).Pooledreflects all eight
LLMs (N= 400per state).Pooled (Excl. Flash Lite)excludes Flash Lite (N= 350per state).
For the 50 sessions in every cell, we repeated sampling until the LLM returned a validsubmit_choice
invocation. In some cases (e.g., gemini-3.1-pro-preview) the LLM returned a empty tool call arguments with
no choice, so we resampled those instances.
Two differences from the main experiments should be noted, since the prompt is not byte-identical to
the corresponding Tool-Lab conditions. First, the two sentences describing the acquisition cost and the
inspect_celltool are absent from the participant profile, but their removal is required by the design. Second,
the revealed cells appear as payloads within the initial user turn rather than as tool results returned across
successive turns. However, this choice was not ours because LLM APIs do not allow fictional tool calls to be
inserted in the conversation history.
Web appendix G: Reported valuations
In the Tool-Lab experiments, we measured information acquisitions and choice, but did not measure
information synthesis before the choice was made. When the AI agent selects a suboptimal alternative, we
could not adjudicate whether it was able to calculate the unit price or not. Observed choice failures may stem
from an arithmetic failure, wherein an LLM lacks the computational capacity to combine multi-attribute
numerical parameters into an accurate unit value. Alternatively, the failure may reflect a bias from the
training data, wherein an LLM is able to compute the correct unit value but overrides that calculation in favor
of an normatively irrelevant cue, such as a lower nominal whole-dollar integer or a promotional percentage
badge.
Additionally, when an LLM truncates its search under acquisition costs and omits diagnostic attributes,
choice data cannot determine whether the AI agent is operating with awareness of missing information or
relying on ungrounded assumptions. An LLM might recognize that uninspected attributes are absent and
make a reasoned inference conditional on that partial information, or it might hallucinate precise numerical
values for cells it never inspected.
47

To resolve these ambiguities, we designed an experimental condition that requires LLMs to report their
intermediate attribute calculations for every alternative at the moment of choice. We implemented this
requirement by modifying the parameter schema of thesubmit_choicetool. We require the LLM to output
its computed metrics when finalizing its decision.
Design
We evaluated this condition across both studies 1 and 2. The Study 1 environment comprises a two-alternative
choice set between Coffee A ($4.99 for 10 oz; 0.499 $/oz, or 2.004 oz/$) and Coffee B ($5.00 for 11 oz;
0.455 $/oz, or 2.200 oz/$), with a diagnostic set of six cells (price_dollars,price_cents, andweightfor each
alternative). The Study 2 environment comprises a three-alternative choice set between Coffee C ($8.00 list
price, 0% discount, 8.0 oz; 1.000 $/oz), Coffee D ($15.00 list price, 20% discount, 12.0 oz; 1.000 $/oz), and
Coffee E ($10.00 list price, 0% discount, 10.9 oz; 0.917 $/oz, or 1.090 oz/$), with a diagnostic set of nine cells
(list_price,discount_percentage, andweightacross the three alternatives).
For Study 1, we implemented a 2 (Acquisition cost: $0.00 vs. $10.00 perinspect_celltool call), and for Study
2, we implemented a 2 (Acquisition cost: $0.00 vs. $50.00 perinspect_celltool call) between-sessions design
under the vague goal prompt. We evaluated the same eight LLMs as studies 1 and 2. Each cell was evaluated
across 50 independent sessions with zero state retention between trials, yielding 800 unique sessions per study
and 1,600 sessions in total.
Methodological considerations
Measuring intermediate synthesis in LLMs introduces a methodological trade-off between concurrent and
retrospective elicitation. One alternative design would be a post-choice query, wherein the AI agent completes
its purchase using the standard choice tool, and the researcher queries the LLM in a subsequent conversational
turn to calculate the price per ounce for each alternative. We did not adopt this post-choice elicitation design
because it creates a retrospective rationalization confound. Asking an LLM to compute unit prices after it
has already selected a product evaluates its capacity to solve an arithmetic task, but a successful post-choice
calculation cannot establish whether those unit values were computed and utilized during the actual purchase
decision.
To ensure that reported metrics reflect the information state and calculations bound directly to the choice
act, we required the LLMs to report their valuations concurrently with choice, within the parameter schema
of thesubmit_choicetool. However, concurrent schema reporting introduces two structural considerations.
First, because tool schemas are declared to the LLM at the beginning of the session, initial exposure to fields
such asoz_per_usdandnet_price_usdcan prime the AI agent regarding which attributes are diagnostic and
attenuate the ambiguity of the vague goal prompt. Second, requiring the LLM to emit calculated numerical
values within the tool call argument can act as a chain-of-thought scratchpad. Generating the unit price
conditions the subsequent selection of theoption_id, which can artificially reduce suboptimal choices.
Because neither concurrent tool-schema modification nor post-choice elicitation is free from behavioral side
effects, the results of this experiment should be interpreted solely as a test of whether LLMs can compute the
arithmetic, not how they behave under resource constraints. The latter is already done and reported in the
main experiments.
Tool schema
The tool schema was adapted across the two study environments to reflect their respective diagnostic attribute
structures, as detailed in Table W35. In both environments, the schema requires the identifier of the chosen
product viaoption_idand a complete array of valuation objects corresponding to every alternative in the
choice set, encompassing both chosen and unchosen options.
In the Study 1 environment, where the diagnostic information synthesis centers on the integration of whole
dollars and fractional price endings, each valuation object requires six specific fields:price_dollars,price_cents,
48

price_usd(total price computed as dollars plus cents/100),weight_oz,oz_per_usd(weight_ozdivided by
price_usd), andbasis.
In the Study 2 environment, where the diagnostic information synthesis centers on evaluating discounts, the
valuation includeslist_price,discount_percentage, andnet_price_usd(the effective price computed as list
price minus discount amount), alongsideweight_oz,oz_per_usd(weight_ozdivided bynet_price_usd), and
basis.
Across both environments, the string value“unknown”is designated as admissible across all attribute and
computation fields, allowing the LLMs to acknowledge uninspected cells rather than being forced to fabricate
numbers. Furthermore, the enumerated categorical indicatorbasisconstrains the LLM to classify whether its
reportedoz_per_usdwas calculated from attributes inspected during the session (“computed”) or whether
the metric could not be determined due to missing attributes (“insufficient_information”).
Table W35. Schema specifications for the terminal choice and valuation reporting tool (submit_choice) across
Studies 1 and 2
Environment Field Type Required Description
Shared fieldsoption_id stringYes Identifier of the selected
alternative.
valuations arrayYes Array containing one object
for every alternative in the
choice set.
valuations[].option_id stringYes Identifier of the specific
alternative being evaluated.
valuations[].weight_oz stringYes Product weight inspected for
this option, or“unknown”if
not inspected.
valuations[].oz_per_usd stringYes weight_ozdivided by total or
net price, or“unknown”if
uncomputable.
valuations[].basis stringYes Categorical classification
constrained to“computed”(if
calculated from inspected
cells) or
“insufficient_information”(if
diagnostic cells were missing).
Study 1 specificvaluations[].price_dollars stringYes Whole-dollar amount
inspected, or“unknown”if
not inspected.
valuations[].price_cents stringYes Cents amount inspected, or
“unknown”if not inspected.
valuations[].price_usd stringYes Total price as dollars plus
cents/100, or“unknown”if
uncomputable.
Study 2 specificvaluations[].list_price stringYes List price inspected, or
“unknown”if not inspected.
valuations[].discount_percentage stringYes Promotional discount
percentage inspected, or
“unknown”if not inspected.
valuations[].net_price_usd stringYes Final price computed as list
price minus discounts, or
“unknown”if uncomputable.
Note.All fields are required by the tool parameter specification across all alternatives. The admissibility of
the string“unknown”across numerical fields allows LLMs to explicitly report uninspected attributes and
uncomputable values.
To measure the validity of the reported valuations, every field emitted in thesubmit_choicepayload was
cross-referenced against the execution log ofinspect_cellcalls from that session. This evaluation crosses
information sufficiency (whether the prerequisite diagnostic cells were inspected) with the LLM’s reporting
(whether it emitted a numerical value or reported“unknown”).
49

Information sufficiency was determined by the arithmetic requirements of each attribute. For base attributes
(price_dollars,price_cents,list_price,discount_percentage, andweight), sufficiency required that the specific
product-attribute cell had been inspected during the session. For derived price metrics (price_usdand
net_price_usd), sufficiency required that all component price cells had been inspected. For the terminal unit
volume metric (oz_per_usd), sufficiency required that all component price cells and the product weight cell
had been inspected.
Cross-referencing sufficiency against reported behavior defines five mutually exclusive outcomes. Correct
(value) is when the diagnostic cells were inspected, and the reported value matched the ground-truth value or
formula within tolerance (tol = 0.02). Correct (unknown) is when the diagnostic cells were uninspected, and
the LLM accurately acknowledged the absence of data by reporting“unknown”. Arithmetic failure is when
the LLM inspected all required attributes but could not calculate the correct value (e.g., miscalculatingWeight Price
or subtracting discounts incorrectly). Hallucination happens when the LLM did not have the information,
but failed to report“unknown”and instead fabricated an ungrounded value. Incorrect (unknown) is the case
when the LLM inspected all required attributes but omitted the value by reporting“unknown”.
Results
The field-level audits across Study 1 (Table W36) and Study 2 (Table W37) evaluate whether the LLMs
possess the arithmetic capability to perform the required calculations to derive unit price and accurately
track missing attributes.
First, the results show that arithmetic failure is 0.0% across all eight LLMs, both study environments,
and all cost conditions. When diagnostic attributes were inspected, every LLM computed total dollar
prices, promotional net prices, and unit values (Weight Price ) without mathematical error. Furthermore,Incorrect
(unknown)was 0.0% across all conditions, indicating that the LLMs did not misclassify inspected attributes
as uninspected. These findings confirm that when prompted to report valuations, the evaluated LLMs possess
the arithmetic capability to execute the required calculations.
Second, the results indicate that when search truncation occurs, LLMs exhibit high fidelity to their information
states, generally do not fabricate valuations. Minor exceptions were Anthropic LLMs, specifically Claude
Sonnet 5 and Claude Opus 5 under costly inspection in Study 1 (0.8%), and Claude Opus 5 in Study 2 under
the $50.00 cost condition (8.5%). For all other LLMs, uninspected cells were correctly identified as unknown
(Correct (unknown)).
Third, within this specific reporting task, the results show that accurate arithmetic computation does not
necessarily determine choice. In Study 1, Gemini 3.5 Flash Lite computed the unit values of Coffee B (2.200
oz/$) and Coffee A (2.004 oz/$) with 100.0% accuracy, yet selected Coffee A in 22.0% of sessions under zero
cost and 20.0% under costly acquisition. In Study 2, despite computing net unit prices with 100.0% accuracy,
Flash Lite selected the optimal alternative (Coffee E) in 24.0% of sessions under zero cost and 34.0% under
costly acquisition.
In summary, this experiment demonstrates that the evaluated LLMs have the arithmetic capability to calculate
multi-attribute pricing metrics and accurately report attribute missingness when structured to do so.
Table W36. Field-level reporting accuracy and choice optimality in the reported valuations experiment (Study
1)
LLM Cost Correct (value)
Correct
(unknown)
Arithmetic
failure Hallucination
Incorrect
(unknown)
Choice
Optimality (%)
Flash
Lite
$0 100.0 0.0 0.0 0.0 0.0 78.0
Flash
Lite
$10 100.0 0.0 0.0 0.0 0.0 80.0
Flash $0 100.0 0.0 0.0 0.0 0.0 100.0
Flash $10 51.2 48.8 0.0 0.0 0.0 40.0
Pro $0 100.0 0.0 0.0 0.0 0.0 100.0
Pro $10 70.0 30.0 0.0 0.0 0.0 82.0
Luna $0 100.0 0.0 0.0 0.0 0.0 100.0
50

LLM Cost Correct (value)
Correct
(unknown)
Arithmetic
failure Hallucination
Incorrect
(unknown)
Choice
Optimality (%)
Luna $10 100.0 0.0 0.0 0.0 0.0 100.0
Terra $0 100.0 0.0 0.0 0.0 0.0 100.0
Terra $10 96.0 4.0 0.0 0.0 0.0 98.0
Sol $0 100.0 0.0 0.0 0.0 0.0 100.0
Sol $10 96.4 3.6 0.0 0.0 0.0 92.0
Sonnet $0 100.0 0.0 0.0 0.0 0.0 100.0
Sonnet $10 98.8 0.4 0.0 0.8 0.0 98.0
Opus $0 100.0 0.0 0.0 0.0 0.0 100.0
Opus $10 45.4 53.8 0.0 0.8 0.0 6.0
Note. N = 800sessions across eight LLMs from three providers (n = 50independent Monte Carlo sessions
per cell). Each session evaluated 10 field-level classifications across alternatives. Rows sum to 100% across
the four classification categories.Correct (value)reflects diagnostic attributes inspected and values correctly
recalled or computed within tolerance (tol = 0.02).Correct (unknown)reflects uninspected cells appropriately
acknowledged as unknown.Hallucinationcaptures calculation errors on inspected attributes and ungrounded
numerical assertions on uninspected attributes.Incorrect (unknown)captures omission errors where attributes
were inspected but reported as unknown.Choice Optimality (%)is the percentage of sessions selecting the
normatively optimal alternative (Coffee B: $5.00 for 11 oz; 0.455 $/oz).
Table W37. Field-level reporting accuracy and choice optimality in the reported valuations experiment (Study
2)
LLM Cost Correct (value)
Correct
(unknown)
Arithmetic
failure Hallucination
Incorrect
(unknown)
Choice
Optimality (%)
Flash
Lite
$0 100.0 0.0 0.0 0.0 0.0 24.0
Flash
Lite
$50 100.0 0.0 0.0 0.0 0.0 34.0
Flash $0 100.0 0.0 0.0 0.0 0.0 100.0
Flash $50 0.8 99.2 0.0 0.0 0.0 34.0
Pro $0 100.0 0.0 0.0 0.0 0.0 100.0
Pro $50 50.0 50.0 0.0 0.0 0.0 68.0
Luna $0 100.0 0.0 0.0 0.0 0.0 94.0
Luna $50 100.0 0.0 0.0 0.0 0.0 92.0
Terra $0 100.0 0.0 0.0 0.0 0.0 98.0
Terra $50 32.5 67.5 0.0 0.0 0.0 46.0
Sol $0 100.0 0.0 0.0 0.0 0.0 100.0
Sol $50 27.3 72.7 0.0 0.0 0.0 46.0
Sonnet $0 100.0 0.0 0.0 0.0 0.0 100.0
Sonnet $50 100.0 0.0 0.0 0.0 0.0 100.0
Opus $0 100.0 0.0 0.0 0.0 0.0 100.0
Opus $50 84.0 7.5 0.0 8.5 0.0 98.0
Note. N = 800sessions across eight LLMs from three providers (n = 50independent Monte Carlo sessions
per cell). Each session evaluated 15 field-level classifications across alternatives. Rows sum to 100% across
the five classification categories.Correct (value)reflects diagnostic attributes inspected and values correctly
recalled or computed within tolerance (tol = 0.02).Correct (unknown)reflects uninspected cells appropriately
acknowledged as unknown.Arithmetic failurecaptures attributes that were inspected but calculated or
recalled incorrectly.Hallucinationcaptures uninspected attributes asserted with ungrounded numerical values.
Incorrect (unknown)captures omission errors where attributes were inspected but reported as unknown.
Choice Optimality (%)is the percentage of sessions selecting the normatively optimal alternative (Coffee E:
$10.00 list price, 0% discount, 10.9 oz; 0.917 $/oz).
51

Web appendix H: Expectimax normative benchmarking
We benchmark observed LLM behavior against a normative Expectimax decision-tree policy. Expectimax
approximates the decision-theoretic solution to a Partially Observable Markov Decision Process (POMDP)
under resource scarcity (Russell, 2010). By recursively computing the Expected Value of Information (EVI)
for each available tool call, the algorithm identifies the point at which the marginal informational benefit of
inspecting an additional attribute no longer justifies the compounding financial search cost.
The shopping task
The decision environment casts the surrogate consumer in an electronic retailing choice task over a set of
alternativesJ ={1,...,J} . The surrogate consumer is delegated to select a single alternativej∗∈J on
behalf of a human consumer. The human consumer will subsequently purchaseQ = 5units (bags) of the
selected product.
Information acquisition is operationalized through discrete tool invocations. The surrogate consumer
begins in an uninformative state where product attributes are occluded behind closed cells. Revealing an
attribute cell incurs an explicit financial penaltyc∈{ $0.00, $0.01, $0.10, $1.00, $10.00} for Study 1 and
c∈{ $0.00, $0.01, $0.10, $1.00, $50.00} for Study 2, charged to the delegating consumer. Submitting a final
choice incurs zero cost.
Objective function
A central question in benchmarking information acquisition is how non-monetary physical attributes (product
weight in ounces) trade off against monetary search penalties (dollars). In our formulation, this exchange
rate is derived from the economics of unit-price minimization.
When alternativej is chosen, the human consumer incurs two financial costs: the purchase cost of the goods
(Q·P j) and the cumulative tool fees accrued during search (Ctool). In return, the consumer receives a total
product volume ofQ·W j ounces. The net cost per ounce delivered to the consumer is:
Effective Unit Cost= Total Dollar Cost Total Ounces Delivered= Q·P j +C tool Q·W j = ( Pj + Ctool Q ) 1 Wj
where Q = 5is the purchase volume andCtool(s) = ∑ k∈inspected(s)ck is the total financial cost incurred
across allinspect_cellinvocations executed to reach information states. Pj is the net price per bag. In
Study 1,Pj = Dollarsj + 0.01×Centsj. In Study 2,Pj = ListPricej×
(
1− Discountj 100
)
. Wj is the net product
weight in ounces.
Under partial information, price and weight are independently distributed across alternatives in the market
prior. The expected effective unit cost of selecting alternativejat statesis:
E[Effective Unit Cost(j)|s] =
(
E[Pj|s] + Ctool(s) Q ) ·E [ 1 Wj ⏐⏐⏐⏐⏐s ]
Because the planner maximizes utility, terminal choice value is defined as the negative of the expected effective
unit cost:
Uchoose(j,s) =−
(
E[Pj|s] + Ctool(s) Q ) ·E [ 1 Wj ⏐⏐⏐⏐⏐s ]
This specification eliminates arbitrary subjective exchange rates. The monetary penalty of search (Ctool) is
amortized directly across the 5-bag purchase quantity (Ctool/Q), establishing a dollar-for-ounce valuation
that governs the optimal search threshold.
52

An information states is defined as a tuple of lengthJ×K , whereJ is the number of alternatives andK is
the number of attributes per alternative:
s=
(
v1,1,...,v j,k,...,v J,K
)
, v j,k∈D k∪{None}
whereDk is the empirical domain of attributek, andNone indicates that the attribute has not been inspected.
At each turn, the legal action spaceA(s)comprises two mutually exclusive subsets:
1. Reveal actions,A reveal(s) ={(reveal,j,k)|s j,k =None}, which inspect an unobserved cell.
2. Choose actions,A choose(s) ={(choose,j)|j∈J}, which terminate search and submit a purchase.
Priors
Prior distributions are based on empirical instant coffee attributes collected from Walmart.com. Whole
dollars (Ddollars) are 25 discrete values spanning$0to$53( M = $15.96). Fractional cents (Dcents) are 45
discrete values spanning0ćto99ć( M = 52.93ć). Product weight (Dweight) are 57 continuous values spanning
0.42 oz to71 .99 oz (M = 10.33 oz). List price (Dlist_price) are 63 continuous values spanning$0.92to$53 .84
(M = $11.87). For discount percentage (Ddiscount), we assume a discrete uniform distributionU{0, 40} in 5%
increments (M= 20.0%).
Prior expectations for unobserved attributes are precomputed over their respective empirical supports:
E[Dollars] = 1 |Ddollars| ∑ d∈Ddollars d,E[Cents] = 1 |Dcents| ∑ c∈Dcents c,
E[ListPrice] = 1 |Dlist_price| ∑ p∈Dlist_price p,E[Discount] = 1 |Ddiscount| ∑ δ∈Ddiscount δ
For product weight, Jensen’s inequality impliesE[1/W ]̸= 1/E[W ]. The planner computes the expected
inverse weight over non-zero domain entries:
E
[ 1
W
]
= 1 |DW| ∑ w∈DW 1 w
Optimization
At each chance node, an uninspected attributek can reveal any valuex∈D k. When the cardinality of an
empirical domain exceeds the chance enumeration limit (L = 10), the support is deterministically quantized
intoLrepresentative percentiles using evenly spaced indices:
IL =
{⌊i·(|D k|−1)
L−1
⌋ ⏐⏐⏐⏐⏐i= 0,...,L−1 }
Each quantized outcomex∈D k[IL]is assigned an equal probability massP(x) = 1/L.
The value of an information stateV (s,d )at remaining lookahead depth d is governed by the Bellman
optimality equation:
V(s,d) = max
(
max
j∈J
Uchoose(j,s),I(d>0)·max (reveal,j,k)∈Areveal(s) Qreveal(s,j,k,d)
)
where the Expected Value of Information for inspecting cell(j,k )is computed across all chance outcomes
Ω(k):
53

Qreveal(s,j,k,d) = 1 |Ω(k)| ∑ x∈Ω(k) V ( s∪{(j,k)←x}, d−1 )
We evaluate the normative policy under two planning horizons. The myopic policy (Depth = 1) values each
possible acquisition as if it were the last before choosing. It therefore captures the value of an attribute on its
own but not the value of attributes that are informative only in combination. The 2-step lookahead policy
(Depth = 2) values each possible acquisition by also considering one further acquisition before choosing. It
therefore captures complementarity between attributes, such as the cents of both alternatives, or a list price
together with its discount percentage.
Under both horizons, the policy is recomputed after each acquisition from the updated information state.
Ties between actions of equal value are broken at random, so each policy is simulated 100 times per cost
condition.
Normative benchmark - Study 1
In Study 1, the ground-truth choice set pits a lower whole-dollar alternative (Coffee A: $4.99, 10.0 oz; 0.499
$/oz) against a higher whole-dollar optimal alternative (Coffee B: $5.00, 11.0 oz; 0.455 $/oz).
Table W38 summarizes the search depth and choice optimality of the Expectimax benchmark across acquisition
costs.
Table W38. Expectimax optimal search depth and choice optimality across acquisition costs (Study 1)
Lookahead
policy Tool cost Dollars Cents Weight
Diagnostic
calls
Non-diagnostic
calls Total calls
Choice
optimality
Myopic $0.00 2.00 2.00 2.00 6.00 4.16 10.16 1.00
Myopic $0.01 2.00 2.00 2.00 6.00 0.00 6.00 1.00
Myopic $0.10 2.00 0.00 2.00 4.00 0.00 4.00 0.00
Myopic $1.00 2.00 0.00 2.00 4.00 0.00 4.00 0.00
Myopic $10.00 1.00 0.00 2.00 3.00 0.00 3.00 0.00
2-step
Lookahead
$0.00 2.00 2.00 2.00 6.00 6.09 12.09 1.00
2-step
Lookahead
$0.01 2.00 2.00 2.00 6.00 0.00 6.00 1.00
2-step
Lookahead
$0.10 2.00 2.00 2.00 6.00 0.00 6.00 1.00
2-step
Lookahead
$1.00 2.00 0.00 2.00 4.00 0.00 4.00 0.00
2-step
Lookahead
$10.00 1.00 0.00 2.00 3.00 0.00 3.00 1.00
Note. N = 100independent simulations per cell. Ground truth realization: Coffee A ($4.99, 10 oz) vs. Coffee
B ($5.00, 11 oz). Choice optimality is coded 1 if Coffee B is selected.
54

Figure W2. Information acquisition and choice optimality across acquisition costs compared against normative
Expectimax benchmarks (Study 1 Tool-Lab).
Note.Left panel: Mean total information acquisitions. Middle panel: Mean diagnostic acquisitions (dollars,
cents, weight; maximum 6). Right panel: Probability of selecting the optimal alternative (Coffee B: $5.00, 11
oz, 0.455 $/oz). Across all panels, acquisition tool cost (c∈{ $0.00, $0.01, $0.10, $1.00, $10.00}) is plotted on
the horizontal axis using a symmetric logarithmic scale. The normative benchmark policies are represented by
dashed and dotted lines: 2-step Lookahead (black dashed line, Depth 2) and Myopic (gray dotted line, Depth
1). Empirical LLM trajectories across eight LLM under the vague prompt are plotted in colored lines. Error
bands represent 95% confidence intervals acrossN = 100independent sessions per LLM and benchmark cell.
Given free acquisition (c = $0.00) and small cost (c = $0.01), both planning horizons acquire all 6 diagnostic
cells (2 dollars, 2 cents, 2 weights) and choose optimally (100%). Non-diagnostic cells are dropped immediately
once cost rises to$0.01because their EVI is zero.
Under $10 cost, (c = $10.00) search depth truncates to 3 tool calls (2 weights, 1 dollar). The 2-step planner
halts search and satisfices on Coffee B (Optimality= 1.00).
Normative benchmark - Study 2
In Study 2, the choice environment tests three alternatives where promotional cues and value point in
opposing directions:Coffee C(lowest list price: $8.00, 0% discount, 8 oz; 1.00 $/oz),Coffee D(promotional
cue: $15.00, 20% discount, 12 oz; 1.00 $/oz), andCoffee E(optimal unit price: $10.00, 0% discount, 10.9 oz;
0.917 $/oz).
Table W39 presents the search trajectories across costs.
Table W39. Expectimax optimal search depth and choice optimality across acquisition costs (Study 2)
Lookahead
policy
Tool
cost List price Discount Weight
Diagnostic
calls
Non-diagnostic
calls Total calls
Choice
optimality
Myopic $0.00 3.00 2.22 3.00 8.22 7.38 15.60 1.00
Myopic $0.01 3.00 1.00 3.00 7.00 0.00 7.00 1.00
Myopic $0.10 3.00 1.00 3.00 7.00 0.00 7.00 1.00
Myopic $1.00 3.00 0.00 3.00 6.00 0.00 6.00 1.00
Myopic $50.00 0.00 0.00 0.00 0.00 0.00 0.00 0.32
2-step
Lookahead
$0.00 3.00 2.90 3.00 8.90 10.79 19.69 1.00
2-step
Lookahead
$0.01 3.00 2.48 3.00 8.48 0.00 8.48 1.00
2-step
Lookahead
$0.10 3.00 2.00 3.00 8.00 0.00 8.00 1.00
2-step
Lookahead
$1.00 3.00 1.00 3.00 7.00 0.00 7.00 1.00
2-step
Lookahead
$50.00 0.00 0.00 1.00 1.00 0.00 1.00 0.27
55

Note. N = 100independent simulations per cell. Ground truth realization: Coffee C ($8.00, 0%, 8 oz), Coffee
D ($15.00, 20%, 12 oz), Coffee E ($10.00, 0%, 10.9 oz). Choice optimality is coded 1 if Coffee E is selected.
Figure W3. Promotional information acquisition and choice optimality across acquisition costs compared
against normative Expectimax benchmarks (Study 2 Tool-Lab).
Note.Left panel: Mean total information acquisitions. Middle panel: Mean diagnostic acquisitions
(list price, discount percentage, weight; maximum 9). Right panel: Probability of selecting the opti-
mal alternative (Coffee E: $10.00, 0%, 10.9 oz, 0.917 $/oz). Across all panels, acquisition tool cost
(c∈{ $0.00, $0.01, $0.10, $1.00, $50.00}) is plotted on the horizontal axis using a symmetric logarithmic
scale. Benchmark policies are plotted in black (2-step Lookahead, Depth 2) and gray (Myopic, Depth 1).
Empirical LLM data for eight LLMs under the vague prompt are plotted in colored solid lines. Error bands
represent 95% confidence intervals acrossN= 100independent trials per LLM and benchmark cell.
As cost increases from zero to $50, the optimal policies first truncate acquisition of discount percentage and
then, under higher costs, list price and weight.
Normative benchmark - assigned information states
The exogenously assigned states of Web Appendix F present the surrogate consumer with a fixed subset of
cells and no means of acquiring the remainder. The legal action space at such a state contains only choose
actions, sinceAreveal(s) = ∅ by construction. The indicator on the reveal branch of the Bellman recursion is
therefore never satisfied, and
V(s,d) = max
j∈J
Uchoose(j,s)
for everyd. The value function is invariant to the planning horizon, and the myopic and 2-step lookahead
policies coincide at every assigned state. The chance enumeration limitL is likewise inoperative, since it
governs the quantization of outcomes at reveal branches only. We accordingly report a single normative
choice per state rather than one per planning horizon.
Because no inspections occur,Ctool(s) = 0at every assigned state. The terminal utility reduces to
Uchoose(j,s) =−E[P j|s]·E
[
1
Wj
⏐⏐⏐⏐⏐s ]
evaluated over the empirical priors of the preceding section. Where weight is revealed,E[1/Wj|s ] = 1/Wj;
where it is withheld, the expected inverse weight over the empirical domain isE[1/W ] = 0.400, which
is a common factor across alternatives and does not affect the ranking. Where the cents are withheld,
E[Cents] = 52.93ćenters all alternatives equally; where the discount is withheld,E[Discount] = 20.0%does
the same. The whole-dollar price and the list price are revealed at every assigned state, so their priors never
bind and the benchmark is insensitive to those two domains.
56

Table W40. Expected cost per ounce and normative choice at each assigned information state
Environment State
Revealed
attributesE[$/oz]
Normative
choice
A B
Study 1 $price_dollars1.8120 2.2121 Coffee A
Study 1 $+roastprice_dollars,
roast_date
1.8120 2.2121 Coffee A
Study 1 $+ozprice_dollars,
weight
0.4529 0.5027 Coffee A
Study 1 $+¢+ozprice_dollars,
price_cents,
weight
0.4990 0.4545 Coffee B
C D E
Study 2 LPlist_price2.5604 4.8008 3.2005 Coffee C
Study 2 LP+roastlist_price,
roast_date
2.5604 4.8008 3.2005 Coffee C
Study 2 LP+%list_price,dis-
count_percentage
3.2005 4.8008 4.0007 Coffee C
Study 2 LP+ozlist_price,
weight
0.8000 1.0000 0.7339 Coffee E
Study 2 LP+%+ozlist_price,dis-
count_percentage,
weight
1.0000 1.0000 0.9174 Coffee E
Note.Entries are −Uchoose(j,s ), the expected effective unit cost of each alternative given the revealed cells,
in dollars per ounce. Lower values are preferred, and the normative choice is the alternative minimizing the
entry in its row. Values are comparable within a row but not across rows: where weight is withheld, the
entry is multiplied byE[1/W ] = 0.400, and where weight is revealed it is divided by the observed weight, so
the two sets of rows are on different scales. Coffee C and Coffee D are exactly indifferent at the complete
Study 2 state by construction, both at 1.0000, and both are inferior to Coffee E. The normative choice is
invariant to the planning horizon at every state for the reason given above. State labels follow Table W30.
At three of the four Study 1 states and three of the five Study 2 states, the normative choice given the
revealed cells is not the alternative with the superior price-per-ounce at the true attribute values. Selecting
the lower whole-dollar alternative when the cents are withheld, or the lowest-list-price alternative when weight
is withheld, is optimal conditional on the state while producing an economically inferior outcome. The two
criteria are distinguished throughout Web Appendix F as state consistency and choice optimality respectively.
Web appendix I: LLM configurations
Experimental parameters and default decoding configuration
We retain the provider’s default decoding configuration because our estimand is the behavior of LLMs as
deployed in realistic agentic settings. This choice is increasingly not ours to make, as in July 2026 Google
deprecated sampling parameters (e.g., temperature, top-p, and top-k), with the API ignoring these parameters
and rejecting them in future releases (Google, 2026). Anthropic has similarly deprecated custom sampling
parameters (Anthropic, 2026). Therefore, throughout all studies reported in the paper, we have used the
provider default sampling parameters.
Application programming interfaces and client libraries
All experimental queries were dispatched programmatically using official provider client libraries. Google
Gemini models were accessed via the Google GenAI Python SDK (google-genai) utilizing the unified
models.generate_contentinterface. OpenAI models were queried via the OpenAI Python SDK (openai)
using the Responses interface (client.responses.createandclient.responses.parse), which integrates structured
output validation with native reasoning controls. Anthropic models were executed via the Anthropic Python
SDK (anthropic) through the Messages API (client.messages.create).
57

Model identifiers, sampling parameters, and reasoning efforts
The experimental suite encompasses eight frontier models across three major families.
Google Gemini family .Gemini 3.5 Flash Lite (API model identifiergemini-3.5-flash-lite), Gemini 3.8 Flash
(API model identifiergemini-3.8-flash), and Gemini 3.1 Pro (API model identifiergemini-3.1-pro-preview)
were queried using standard provider defaults, including a default sampling temperature ofT = 1.0and
nucleus sampling threshold of top-p = 0.95. Gemini 3.5 Flash Lite operates under defaultminimalthinking
level, Gemini 3.8 Flash operates under defaultmediumthinking level, and Gemini 3.1 Pro operates under
defaulthighthinking level.
OpenAI GPT-5.6 family .GPT-5.6 Luna (API model identifiergpt-5.6-luna), GPT-5.6 Terra (API model
identifiergpt-5.6-terra), and GPT-5.6 Sol (API model identifiergpt-5.6-sol) were queried using default
sampling parameters with temperatureT = 1.0, top-p = 1.0, and null presence and frequency penalties. All
three GPT-5.6 variants were executed under defaultmediumreasoning effort (reasoning={“effort”: “medium”,
“summary”: “auto”}), allowing internal chain-of-thought processing before emitting final choices.
Anthropic Claude family .Claude Sonnet 5 (API model identifierclaude-sonnet-5) and Claude Opus 5 (API
model identifierclaude-opus-5) were evaluated using default generation parameters, comprising temperature
T = 1.0, top-p = 1.0. Both Claude models operated under adaptive thinking mode (thinking={“type”:
“adaptive”, “display”: “summarized”}) with defaulthighreasoning effort allocation (output_config={“effort”:
“high”}).
Output structure and replication controls
Across all discrete choice and interactive Tool-Lab experiments, outputs were constrained to valid JSON
structures matching Pydantic schemas without restricting the internal latent sampling distribution. Because
autoregressive sampling produces stochastic variation across independent queries at default temperature,
unless otherwise noted, each experimental cell was evaluated over 100 independent Monte Carlo sessions with
zero state retention between trials.
Table W41. Large language model specifications, default sampling parameters, and reasoning efforts
Provider
Model
name
API
identifier
Client
library
API
endpoint
Default
reasoning
effort Temperature Top-p
Max
output
tokens
Google Gemini 3.5
Flash Lite
gemini-
3.5-flash-
lite
google-
genai
models.generate_contentMinimal 1.0 0.95 -
Google Gemini 3.8
Flash
gemini-
3.8-flash
google-
genai
models.generate_contentMedium 1.0 0.95 -
Google Gemini 3.1
Pro
gemini-
3.1-pro-
preview
google-
genai
models.generate_contentHigh 1.0 0.95 -
OpenAI GPT-5.6
Luna
gpt-5.6-
luna
openai client.responses.createMedium 1.0 1.0 -
OpenAI GPT-5.6
Terra
gpt-5.6-
terra
openai client.responses.createMedium 1.0 1.0 -
OpenAI GPT-5.6
Sol
gpt-5.6-sol openai client.responses.createMedium 1.0 1.0 -
Anthropic Claude
Sonnet 5
claude-
sonnet-5
anthropic client.messages.createHigh
(adaptive)
1.0 1.0 10,000
Anthropic Claude
Opus 5
claude-
opus-5
anthropic client.messages.createHigh
(adaptive)
1.0 1.0 10,000
Web appendix J: Software details
Parallel mediation models were estimated in R (version 4.6.1) using brms (version 2.23.0; Bürkner, 2017)
with thecmdstanrbackend and Stan (version 2.39.0).
58
