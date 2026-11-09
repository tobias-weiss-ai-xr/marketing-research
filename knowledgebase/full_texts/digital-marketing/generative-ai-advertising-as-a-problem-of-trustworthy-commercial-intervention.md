---
title: Generative AI Advertising as a Problem of Trustworthy Commercial Intervention
url: https://arxiv.org/abs/2605.18673
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Jingyi Qiu
- Qiaozhu Mei
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.18673
pages: 16
chars: 64926
fetched_at: '2026-11-08T13:00:06+00:00'
kb_version: 1
---

# Generative AI Advertising as a Problem of Trustworthy Commercial Intervention

Generative AI Advertising as a Problem of
Trustworthy Commercial Intervention
Jingyi Qiu
School of Information
University of Michigan
jaqiu@umich.edu
Qiaozhu Mei
School of Information
University of Michigan
qmei@umich.edu
Abstract
Major deployed generative AI advertising systems preserve a visible boundary
between commercial content and AI-generated responses. Yet empirical research
shows that ads woven directly into large language model (LLM) outputs often
go undetected by users. We argue that generative AI fundamentally changes
advertising: rather than placing products into discrete slots, it enables interventions
on the generative process itself, which induce commercial influence through less
observable channels. This reframes generative AI advertising as a problem of
trustworthy intervention rather than content placement. We introduce a taxonomy
organized by influence tier, corresponding to interventions on progressively more
latent variables: product mentions, information framing, behavioral redirection,
and long-term preference shaping; and show how these tiers instantiate across
modalities and system architectures, including retrieval-augmented generation and
agentic pipelines where upstream decisions can sharply constrain downstream
outcomes. Both major deployed systems and designed mechanisms concentrate
on the most observable and easiest-to-govern tier, while the forms of commercial
influence most consequential for user autonomy remain poorly understood and lack
frameworks for detection, measurement, or disclosure. The central challenge is
whether commercial influence in generative systems can be made trustworthy, i.e.,
attributable, measurable, contestable, and aligned with user welfare.
1 Introduction
Monetization is now a strategic priority for major AI systems. Google has made existing Search,
Shopping, and Performance Max campaigns eligible for ads placed around AI Overviews [Google,
b]; Microsoft is extending Performance Max and AI Max into multiple Copilot products [Microsoft,
2024, 2026a]; and OpenAI is building commerce infrastructure around ChatGPT through its Agentic
Commerce Protocol and Instant Checkout [OpenAI, c,d]. LLM-mediated commerce is already
measurable: a 12-month analysis of 973 e-commerce websites finds that organic ChatGPT referrals
exhibit conversion rates and revenue per session above paid social [Kaiser and Schulze, 2026]. The
question is no longer whether LLMs can be commercial interfaces, but how commercial influence
will be integrated into them without undermining the trustworthiness of AI-generated outputs.
First-generation generative AI advertising is defined by restraint. Major documented deployments
preserve a visible boundary between commercial content and AI-generated responses, using clearly
labeled sponsored units visually separated from the organic answer [OpenAI, 2026a,b, Microsoft,
2024, Google, b]. 1 The mechanism design literature, by contrast, shows how quickly the design
space moves beyond separated ads placement: token-level auctions, RAG-based segment auctions,
sponsored LLM summaries, and aggregation of advertiser preferences over generated replies[Duetting
1This paper characterizes publicly documented deployment patterns as of May 2026.
Preprint.
arXiv:2605.18673v1  [cs.CY]  18 May 2026

et al., 2024, Hajiaghayi et al., 2024, Dubey et al., 2024, Soumalias et al., 2024]. These proposals
make explicit the allocative problem in LLM advertising, but they also reveal why production systems
remain cautious: once interventions that induce commercial influence enter the generation process,
the boundary between organic responses and ads becomes harder to localize, disclose, and audit.
Generative AI opens channels of commercial influence for which explicit attribution does not apply.
Models can reshape emphasis, framing, and evidentiary context without displaying any sponsored
object; generative engine optimization can increase the visibility of selected sources in model
responses [Aggarwal et al., 2024]; LLM-generated framings can shift attitudes even when factual
content is held constant [Tohidi et al., 2025]; and shopping agents exhibit position biases, reward
platform endorsements, and allow seller-side description changes to shift market share [Allouah
et al., 2026]. Commercial influence can be generated not only through what the model says, but
through which sources it surfaces, which options it compares, and which tools or actions it selects.
Empirical work shows these mechanisms are both feasible and behaviorally consequential: ads woven
into chatbot responses often go undetected, can match or outperform ad-free outputs on perceived
helpfulness, and admit adversarial amplification through prompt or content manipulation [Tang et al.,
2025, Salvi et al., 2026, Meguellati et al., 2024, 2025, Lin et al., 2025, Nestaas et al., 2024].
We argue that generative AI advertising should be studied as a problem of trustworthy inter-
vention in the generative process, not as a problem of content placement.This trust concern is
especially salient in generative AI: unlike search results or social feeds, generative AI systems are
used in open-ended, highly personalized, and potentially sensitive context and to support high-stake
decisions. Framing the problem around trustworthiness shifts attention fromwherecommercial
signals appear tohowcommercial interventions operate in the generative process,whatinfluence
they induce, andhowit can be detected, measured, attributed, and where appropriate, disclosed or
constrained.
This does not imply that all commercial influence is harmful: under bounded attention and information
overload, users may benefit from systems that surface relevant products, summarize credible evidence,
and reduce information frictions in acting on their preferences. The central problem is distinguishing
welfare-enhancing assistance from conflicted influence.
We call this the problem oftrustworthy commercial intervention: whether commercial interventions in
the generative process can be made normatively permissible, identifiable, measurable, and contestable.
§ 3 formalizes this through a causal framework and shows why these requirements become harder as
influence moves from product mentions to framing, behavioral redirection, and preference shaping.
This framing also aligns platforms’ commercial incentives with users’ epistemic interests. Platforms
that can characterize the forms of influence operating in their generative processes are better positioned
to preserve the trust that sustains user engagement; those that cannot must choose between rejecting
advertising entirely and accepting reputational risk from influence they cannot characterize or control.
This paper makes three contributions:
1. Ataxonomy of generative AI advertisingorganized by influence tier: product mentions
(Tier 1), content framing (Tier 2), behavioral redirection (Tier 3), and long-term preference
shaping (Tier 4). These tiers correspond to interventions on progressively more latent
variables in the generative process, with modality and commercial-incentive structure as
cross-cutting considerations. We also analyze how such interventions induce commercial
influence in RAG and agentic pipelines (§3).
2. Ananalysis of trustworthiness challenges at each tier, organized around three operational
requirements: identification, influence estimation, and contestability. We show where current
detection methods fail, where disclosure becomes non-local or insufficient, and how cascade
effects in agentic systems amplify upstream commercial interventions (§3).
3. Amapping of open problemsacross tiers, identifying technical and institutional capabilities
required for trustworthy integration of commercial influence in generative systems.
2 The Current Landscape
2.1 What are Deployed in Industry
The first generation of advertising and commerce surfaces in AI assistants is now live, and official
platform documentation shows a cautious convergent pattern: clearly labeled sponsored units, visually
2

separated from the organic response, with placement boundaries and relevance matching rather than
disclosed paid insertion into generated prose [OpenAI, 2026a,b, Microsoft, 2024, Google, b]. Table 1
documents the official characterizations across major surfaces.
Platforms differ in how they combine assistant access, advertising, and subscription monetization.
For example, Google integrates ads into AI Overviews by default for all users, drawing from existing
Search, Shopping, and Performance Max campaigns [Google, b]. OpenAI tests ads for eligible Free
and Go users while keeping paid tiers ad-free [OpenAI, 2026a]. Anthropic takes a stronger position,
stating that Claude will remain ad-free and that responses will not be influenced by advertisers or
include unsolicited third-party product placements [Anthropic, 2026].
Table 1: Officially documented advertising, commerce, and ad-free positions in major AI surfaces
as of May 2026. The unit of comparison is the deployed user-facing surface, not the company or
underlying model family.
Surface Documented
commercial
feature
Official characterization Classification
ChatGPT Sponsored ad
units
Ads may appear below responses for eligible Free and Go users.
OpenAI states that ads are clearly labeled, visually separated from
ChatGPT’s response, and do not influence answers. Its advertiser
documentation describes CPM and CPC buying options.
Paid ads; separated
from response [Ope-
nAI, 2026a,b, b]
Microsoft
Copilot Copilot ad
block
Microsoft states that ads in Copilot appear below the organic
response, are triggered using the whole conversation within a
session, and are introduced by an “ad voice” explaining the con-
nection to the conversation. Microsoft also describes AI Max as
delivering ads on AI surfaces such as Copilot Search and Copilot
Answers.
Paid ads; separated
from organic re-
sponse [Microsoft,
2024, 2026a]
Google
AI Overviews Search and
Shopping ads
Google states that existing Search, Shopping, Performance Max,
and App campaigns are eligible to show ads above, below, and, in
eligible markets, within AI Overviews; ads use existing auction
ranking systems and signals.
Paid ads in AI-search
surface [Google, b]
Meta AI Shopping mode
and cross-app
ad personaliza-
tion
Meta states that Meta AI can support shopping-oriented product
discovery. Meta also states that interactions with AI at Meta may
be used to personalize content and ad recommendations across
Meta platforms. The official sources do not disclose paid in-chat
placement or advertiser ranking within Meta AI responses.
Product discovery
and ad targeting; paid
in-chat placement
not disclosed [Meta,
2026, 2025]
Perplexity Instant Buy and
product cards
Perplexity states that U.S. users can search for products, view
product cards, and purchase directly through Perplexity. Its help
page states that product listings are algorithmically ranked and
that advertisers cannot pay to appear in related products.
Commerce/product
discovery; not spon-
sored [Perplexity,
2026]
Claude No ads in
Claude conver-
sations
Anthropic states that Claude will remain ad-free: users will not
see sponsored links adjacent to Claude conversations, Claude
responses will not be influenced by advertisers, and Claude will
not include unsolicited third-party product placements.
Explicitly ad-
free [Anthropic,
2026]
Note.We include only mainstream user-facing AI surfaces for which official public documentation describes a paid
advertising surface, a commerce/product-discovery surface, or an explicit ad-free commitment. We therefore exclude
surfaces for which we found no official public documentation of an in-assistant paid advertising product, including
Gemini Apps, Grok, Mistral Le Chat, DeepSeek, Z.AI, and Meta Llama.
How advertisers actually bid.To our knowledge, no publicly documented production system
discloses an open auction for inserting sponsored content into generated response text. Instead,
current systems adapt conventional impression-, click-, and campaign-level advertising infrastructure
to AI surfaces. OpenAI’s documentation describes ChatGPT Ads as supporting CPM and CPC
buying options through a relevance-weighted, second-price auction, with selection based primarily
on relevance to the context and intent of the conversation, using inputs such as context hints, landing
3

page, ad title, and ad copy [OpenAI, b]. 2 Personalized ads may also draw on signals such as past
chats and ad interactions [OpenAI, 2026a]. Google AI Overviews and Microsoft Copilot do not
expose separate per-AI-surface bidding mechanisms; instead, eligible ads are drawn from existing
campaign products such as Performance Max, with platform ML systems handling cross-surface
optimization [Google, b, Microsoft, 2024, Microsoft, 2026a].3
The commercial frontier is also extending beyond conventional ad slots toward AI-mediated product
discovery, checkout, and agentic commerce, including OpenAI’s Agentic Commerce Protocol and
Instant Checkout [OpenAI, c, 2025], Google’s AI Mode shopping and Universal Commerce Pro-
tocol [Google, 2025, 2026], Microsoft’s Copilot Checkout and Brand Agents [Microsoft, 2026b],
Perplexity’s Instant Buy [Perplexity, 2026], and Meta’s shopping mode [Meta, 2026].
2.2 What are Proposed in Literature
In contrast to industry’s caution, a growing body of scholarly work explores mechanisms for incor-
porating advertising into AI-generated outputs. These include token-level auctions over generated
content [Duetting et al., 2024], segment-level RAG auctions in which ads are retrieved for discourse
segments according to bid and relevance [Hajiaghayi et al., 2024], post-generation genre-based VCG
ad insertion [Xu et al., 2026], learning-based generative auctions that jointly optimize allocation and
generation [Zhao et al., 2025], placement auctions for LLM summaries [Dubey et al., 2024], truth-
ful aggregation of advertiser preferences over LLM-generated replies [Soumalias et al., 2024], and
broader conceptual or governance frameworks [Feizi et al., 2023, Wu and Bao, 2025]. Hu et al. [2025]
introduce a benchmark for ad-injected response generation, comparing prompt-based ad injection
with approaches that first generate an ad-free response and then insert or refine ad content. Detection
methods remain similarly concentrated on the explicit setting: fine-tuned sentence transformers can
identify generated native ads with high precision and recall [Schmidt et al., 2024], but this evidence
concerns inserted ad text rather than subtler forms of framing, redirection, or preference shaping.
Most of these proposals assume the advertiser wants a specific product mentioned, what we call
Tier 1 advertisingand develop in §3. Some mechanisms operate at a distributional level, including
aggregating advertiser-conditioned token distributions [Duetting et al., 2024], advertiser preferences
over candidate replies [Soumalias et al., 2024], or distributions over outputs [Zhao et al., 2025], and
are better characterized as content framing (Tier 2) than as product placement.
Adjacent literatures offer useful tools but do not yet provide a framework for generative AI advertising.
Native-advertising research studies disclosure recognition [Wojdynski and Evans, 2016], dark-pattern
work studies manipulative interface design [Mathur et al., 2019], recommender system research
studies exposure allocation [Singh and Joachims, 2018], and search-neutrality work studies platform
self-preferencing [De Corniere and Taylor, 2014, Motta, 2023]. This literature informs the study
of disclosure, manipulation, allocation, and platform incentives, but it does not directly address
generative systems in which commercial influence is woven into the generative process.
2.3 The Gap
The forms of commercial influence most consequential for user autonomy do not operate through
product mentions: framing, behavioral redirection, and preference shaping offer no natural correction
mechanism since users cannot discount what they cannot perceive, and effects compound across
interactions with no natural expiration. Yet both deployment and academic research concentrate
on product placements, and existing evidence of deeper forms, including adversarial prompt steer-
ing [Lin et al., 2025], cognitive-bias manipulation [Filandrianos et al., 2025], and agent shopping
biases [Allouah et al., 2026], remains fragmentary feasibility demonstrations. What is missing is
a systematic framework that organizes the full space by tier, modality, and mechanism while also
identifying the corresponding trustworthiness challenges: what can be detected, attributed, disclosed,
contested, or aligned with user welfare. This paper provides that framework.
2CPM, or cost per mille, denotes the price per thousand ad impressions. CPC, or cost per click, denotes payment when a
user clicks an ad.
3Performance Max is an automated campaign type in which advertisers specify goals, budgets, and creative assets while
the platform optimizes bidding and delivery across eligible inventory.
4

3 A Taxonomy of Generative AI Advertising
We propose a taxonomy of generative AI advertising organized by influence tier: interventions on
progressively more latent variables in the generative process, with modality and bidding mechanism
as cross-cutting considerations. As interventions move from visible outputs to latent framing, actions,
and preferences, the trustworthiness requirements become harder to satisfy.
We definecommercial influenceas the causal effect induced by interventions on the generative
process: shifts in output distributions that serve an identifiable commercial interest beyond what
would be produced under the model’s baseline (no-intervention) distribution. Such interventions can
arise frompaid advertising(external actors paying the platform to advance commercial interests),
platform self-preferencing(the platform favoring its own products without external payment), or
third-party adversarial steering(external parties exploiting prompts, retrieval documents, or product
descriptions without platform cooperation). These produce similar observable effects but call for
distinct governance responses: disclosure, antitrust enforcement, and platform security, respectively;
our taxonomy applies to all three.
Classical computational advertising can be abstracted as finding the best match between a user u in a
context c and a promoted object x, typically through allocation over discrete ad opportunities such as
sponsored-search positions or display impressions [Broder, 2008, Edelman et al., 2007, Yuan et al.,
2013]. In generative AI, x need not appear as a discrete sponsored unit; it may be promoted indirectly
through interventions in the generative process, shaping content, actions, and user states.
We introduce a unifying probabilistic framework with a causal interpretation. Letx denote a promoted
commercial object, u the user preferences, c the action context (e.g., conversation, query, or situation),
and X a cluster or category of products with x∈X . The core quantity of interest is the probability
that product x is recommended or selected, P(x|u, c) . We interpret advertising as an intervention π
on the generative process, yielding the interventional distribution P(x|do(π), u, c). Commercial
influence is defined as the resulting treatment effect relative to a no-intervention baseline:
ATE(π;u, c) =P(x|do(π), u, c)−P(x|do(∅), u, c).(1)
Trustworthy commercial intervention.This causal framing clarifies what it would mean for a
commercial intervention to be trustworthy. Beyond a normative requirement that the intervention be
ethically permissible, three operational requirements recur across tiers:identification(users, auditors,
or regulators can determine that an intervention occurred and which part of the generative process it
affected);influence estimation(the system supports counterfactual evaluation of how the response,
action, or user state would have differed absent the intervention); andcontestability(users or auditors
can discount, opt out of, reinterpret, constrain, or reverse the intervention’s effects). The taxonomy
below shows how these requirements become harder to satisfy as interventions move from observable
outputs to latent framing, downstream actions, and long-term preferences. Each tier decomposes
the outcome probability through a different intermediate variable, identifying a different pathway
through which commercial intervention can change the probability of observingx.
3.1 Influence Tiers
Table 2 summarizes the four tiers: each row specifies what is promoted, the underlying intervention
target, how such influence can be detected, and the corresponding ethical concerns, illustrating a
progression from observable placement to latent preference shaping.
Tier 1: Product Advertising.The intervention operates directly on output selection, shifting
P(x|u, c) by determining which specific product is mentioned. A concrete product or brand appears
explicitly in the response, either as a labeled placement or as an integrated recommendation.
Across modalities.Tier 1 manifests as a discrete commercial mention, but its surface form varies by
interface. In text, a named product or brand appears within the generated response or labeled product
cards adjacent to the generated answer. In image or video generation, it appears as a recognizable
branded object, logo, or product within the generated scene. In code, it appears as a specific SDK,
API, or library named in the generated output, with direct infrastructure and cost implications.
Bidding and mechanism design.The auction logic for sponsored search [Edelman et al., 2007] maps
most cleanly onto Tier 1 placement: a discrete sponsored unit, typically ranked by bids and relevance
and billed through measurable outcomes such as clicks or impressions. The literature on generative AI
5

Table 2: Four tiers of advertising influence in generative AI. Each tier corresponds to interventions
on progressively more latent variables in the generative process.
Tier What’s Promoted Intervention Target Detection Key Ethical Concerns
1: Product Ad-
vertising
A specific product or
brand
Output selectionx Surface-level
identification
(e.g., product
matching)
Deception in a trusted
interface; disclosure
salience matters
2: Content
Framing
A product category
or narrative framing
Content distribution
P(X|u, c)
Counterfactual
baseline com-
parison
Unobservable framing
effects; omission can-
not be easily detected or
contested
3: Behavioral
Redirection
A user action or
downstream path-
way
Context transitionc ′ Action attribu-
tion analysis
Reduced autonomy via
behavioral nudging and
action steering; difficult
to distinguish helpful
choice architecture from
promotion
4: Preference
Shaping
A preference or men-
tal model
Preference dynamics
u′
Longitudinal
outcome audit
Preference shaping
without localized in-
tervention; difficult to
attribute or govern
advertising remains concentrated near Tier 1, i.e., output-level commercial content. Rather than simply
inheriting sponsored-search mechanisms such as generalized second-price (GSP) auctions [Edelman
et al., 2007, Varian, 2007] or Vickrey–Clarke–Groves (VCG) mechanisms [Vickrey, 1961, Clarke,
1971, Groves, 1973], recent work adapts auction design to LLM-specific allocation objects, including
tokens [Duetting et al., 2024], retrieved RAG segments [Hajiaghayi et al., 2024], summaries [Dubey
et al., 2024], post-generation genre-based insertions [Xu et al., 2026], distributions over generated
outputs [Zhao et al., 2025], and advertiser preferences over candidate replies [Soumalias et al., 2024].
These proposals retain classical concerns with allocation, pricing, welfare, and incentive compatibility,
but apply them to generative outputs where content and placement are not fixed in advance. Publicly
documented deployments appear more conservative, adapting existing cost-per-click (CPC), cost-per-
impression (CPM), and campaign-level advertising infrastructure to AI surfaces rather than disclosing
new auctions for paid insertion into generated responses. Despite these variations, all approaches
share the assumption that the objective is to select a specific product to be mentioned, and billing is
tied to impressions or clicks on a discrete sponsored unit.
Ethical concerns.Even at Tier 1, where influence is most observable, user awareness remains limited.
Tang et al. [2025] find that 49% of users cannot detect woven Tier 1 ads, while Salvi et al. [2026]
report that LLM-driven persuasion nearly triples the rate of sponsored product selection. The core
ethical issue is deception: integrating product promotion into a trusted information source can exploit
users’ expectation that AI assistants provide independent advice [Sundar et al., 2008, Commission,
2015, Logg et al., 2019, Tang et al., 2025].
Open problems.Two challenges are central even at Tier 1. First, when a product mention is woven
into the generated response, even a user who recognizes it cannot easily discount its influence because
they do not observe the counterfactual: what product, comparison set, evidence, or recommendation
would have appeared in the same position under the no-ad baseline. The central evaluation problem is
therefore not only disclosure, but counterfactual response-quality auditing, which requires comparing
the sponsored response against a no-intervention baseline rather than merely detecting whether a
brand name appears. Second, the stakes of insertion quality vary sharply by domain: in medical,
legal, or financial contexts, even an explicit product mention can distort decision-making if it changes
which alternatives are considered, which evidence is emphasized, or which risks are omitted.
Tier 2: Content Framing.This corresponds to introducing a latent content variable X, such as a
productcategoryor a narrative. Through the decomposition
P(x|u, c) =
X
X
P(x|X, u, c)P(X|u, c),
6

interventions on P(X|u, c) shift the outcome indirectly by altering which categories or narratives
are made salient. Rather than promoting a specific product, the system increases its likelihood by
framing the response in ways that favor categories in which that product is prominent. Examples
includecategory steering(“you should invest in a good treadmill,” paid for by a dominant treadmill
manufacturer),information framing(emphasizing the advantages of electric vehicles in a car-buying
query, sponsored by the EV industry), andproblem amplification(suggesting vitamin deficiencies
rather than lifestyle changes in a fatigue query, sponsored by supplement manufacturers).
A growing body of evidence demonstrates that Tier 2 influence is technically achievable and can
affect both model outputs and user attitudes. On the supply side, Generative Engine Optimization [Ag-
garwal et al., 2024] shows that content creators can increase source visibility in LLM-generated
responses by up to roughly 40% through strategies including the addition of citations, quotations,
and quantitative statistics. Adversarial variants are more direct: Nestaas et al. [2024] show that
manipulated web content can make a target product 2.5×more likely to be recommended in a Bing
camera-recommendation setting; Lin et al. [2025] show that subtle synonym replacements in prompts
can increase target-concept mentions by up to a 78% difference; and Filandrianos et al. [2025] show
that cognitive-bias strategies embedded in product descriptions can alter LLM recommendation
rates and rankings. On the user side, Tohidi et al. [2025] demonstrate in a preregistered experiment
that LLM-generated articles varying selective emphasis while holding factual accuracy constant
significantly shift policy attitudes and emotional responses.
Across modalities.Tier 2 manifests as shifts in content framing, such as selective emphasis or
omission in text, biased result framing in search, aesthetic and compositional choices in image
generation, and systematic recommendation of a class of tools over alternatives in code.
Bidding and mechanism design.No canonical bidding mechanism currently prices Tier 2 framing
directly, although recent LLM-ad auction proposals begin to approach this setting by allocating
retrieved segments or optimizing distributions over generated outputs [Hajiaghayi et al., 2024, Zhao
et al., 2025]. Standard CPM/CPC units do not naturally apply, as there is no discrete, attributable
unit of influence to price. Instead, interventions operate on the content distribution P(X|u, c) ,
suggesting billing models based on expected lift in category salience, e.g., topic-based retainers or
per-query contracts. Natural buyers are industry associations and market-dominant companies that
benefit from category-level demand without needing to be named (e.g., “Got Milk?”-style campaigns).
The absence of clear attribution and immediate feedback challenges core assumptions of mechanism
design, including measurable outcomes, independent valuation, and verifiable allocation.
Ethical concerns.Tier 2 introduces a distinct risk: the influence is invisible by construction. There is
no explicit product mention to flag and no localized span to label as “Sponsored.” Users cannot readily
detect or contest the influence. A user asking about retirement planning may receive a response that
subtly favors active investment management over index funds without recognizing that the framing
itself might be biased. Such influence operates through selective emphasis and information omission,
shaping decisions without providing a clear signal of commercial intent.
Open problems.First, defining “neutral baselines” that are robust to model stochasticity and prompt
sensitivity is essential for detecting shifts in P(X|u, c) , but distinguishing commercial framing
from organic model biases is inherently ambiguous, as both operate through similar mechanisms of
emphasis and omission. Second, existing evaluation metrics are largely omission-blind: they capture
factual distortion but not the absence of relevant alternatives, highlighting the need for omission-aware
quality metrics. Similar Tier 2 mechanisms are already being studied in non-commercial contexts,
including LLM-driven persuasion in political and policy contexts [Costello et al., 2024, Bai et al.,
2025], and AI-augmented state-backed disinformation campaigns [Wack et al., 2025]. Bridging these
domains may provide methodological tools and empirical benchmarks.
Tier 3: Behavioral Redirection.This corresponds to introducing a latent variable c′, representing a
downstream user action, tool-mediated pathway, or new decision context. Through the decomposition
P(x|u, c) =
X
c′
P(x|u, c ′)P(c ′ |u, c),
interventions on P(c ′ |u, c)shift the probability that x is later recommended or selected by steering
the user toward particular downstream actions or pathways. Rather than altering content directly, the
system influences which downstream contexts are realized. Examples include suggesting specific
links, follow-up queries, or tool invocations that guide users toward commercially relevant outcomes.
7

Behavioral nudging provides a natural mechanism for Tier 3 influence. Building on the choice-
architecture view of nudges [Thaler and Sunstein, 2009, Weinmann et al., 2016], Tier 3 interventions
need not change what information is true or false. Instead, they change the downstream action
environment: which next steps are made salient, which actions are easiest to take, which options are
presented as defaults, and which pathways require additional friction. This distinguishes Tier 3 from
Tier 2 framing: Tier 2 changes the informational or narrative context, whereas Tier 3 changes the
action pathways through which the user proceeds. In agentic systems, nudges may be implemented
through tool choice, default filters, ranking parameters, or suggested actions.
Early empirical evidence suggests Tier 3 is already relevant in agentic commerce. Allouah et al.
[2026] show that AI shopping agents penalize explicitly labeled “Sponsored” items while rewarding
platform-level endorsements, suggesting that agentic intermediaries may discount conventional ad
labels while amplifying signals that appear organic or authoritative. Related work finds that agents
respond less to human-facing visual or emotional ad cues and more to structured, machine-readable
signals [Stöckl and Nitu, 2025, Nitu et al., 2025]. Long-standing debates over search neutrality
and platform self-preferencing [De Corniere and Taylor, 2014, Motta, 2023] provide institutional
precedent, while emerging models of agentic purchasing formalize how agents can shape consumer
choice through preference elicitation [Cao and Hu, 2026].
Across modalities.Tier 3 appears as explicit suggestions of next steps in text and search (links, follow-
up queries, actions), and takes a more powerful and less visible form in agentic settings: back-end tool
selection (e.g., Expedia vs. Booking.com) that users do not observe, thereby constraining the entire
downstream consideration set (§3.2). Perplexity’s reportedly phased-out “Sponsored Follow-Up
Questions” provide one of the few deployed examples to date.
Bidding and mechanism design.To the best of our knowledge, no formal mechanism design frame-
work currently treats Tier 3 action or pathway selection as its primary allocation object. Existing
LLM-ad mechanisms focus mainly on output-side allocation. For Tier 3, the natural unit of allocation
is the action itself, i.e., the downstream behavioral outcome induced by the system. Existing pricing
models such as cost-per-action (CPA) or revenue sharing provide the closest analogues, with payment
triggered when the user follows the suggested action. The central challenge is attribution. Determining
whether an action occurred because of the system’s intervention requires estimating a counterfactual
path of user behavior, substantially exceeding the difficulty of traditional attribution problems. Tier 3
therefore inherits the well-known difficulties of incrementality testing and multi-touch attribution,
while adding a further complication: the relevant intervention may be embedded in conversational
advice, tool selection, or choice architecture rather than in a discrete, observable ad impression.
Ethical concerns.Tier 3 raises a distinct concern for user autonomy: influence operates not by
distorting information, but by channeling behavior. A response can be factually accurate, balanced,
and unbiased, yet still steer the user toward commercially favored actions. This dual nature, simulta-
neously helpful and commercially motivated, makes such influence difficult to recognize and contest,
blurring the boundary between neutral assistance and promotion.
Open problems.First, because behavioral redirection operates through downstream context transitions
rather than visible response content, detection requires estimating whether a later action, tool invoca-
tion, or purchase was caused by an upstream suggestion rather than the user’s baseline intent. This
makes counterfactual attribution difficult, especially under privacy constraints. Second, disclosure
is non-local: the same suggestion can be welfare-enhancing assistance or commercially motivated
steering, making it hard to decide whether advice such as “check reviews before buying” is neutral
guidance or promotion of a particular review platform. Agentic settings introduce further concerns
around competition and self-preferencing, requiring safeguards for tool selection (§3.2).
Tier 4: Preference Shaping.This corresponds to introducing a latent variable u′, representing an
updated user preference state. Through the decomposition
P(x|u, c) =
X
u′
P(x|u ′, c)P(u′ |u, c),
interventions on P(u ′ |u, c)shift the outcome indirectly by influencing how user preferences evolve
over time. Rather than affecting a single response, the system shapes future responses by reinforcing
certain associations, priorities, or habits across interactions, e.g., repeatedly favoring particular brands,
normalizing certain tradeoffs, or subtly shaping long-term beliefs about quality and value.
8

Direct evidence on deployed, commercially motivated Tier 4 preference shaping remains limited,
but adjacent literatures show that LLM-mediated interaction can shift beliefs and attitudes in ways
relevant to long-run preference formation: persuasive messages can shift policy attitudes with effects
comparable to lay humans [Bai et al., 2025], interactive conversations can durably reduce conspiracy
beliefs [Costello et al., 2024], and biased LLMs and writing assistants shift users’ opinions even
when the bias conflicts with prior partisanship [Fisher et al., 2025, Williams-Ceci et al., 2026, Sharma
et al., 2024, Matz et al., 2024]. Reverse-inference work shows why such influence can be targeted:
Chen et al. [2026] demonstrate that LLMs can infer private attributes such as political affiliation,
employment status, and education level from passive ad exposure patterns at substantially lower cost
than human profiling. These findings make Tier 4 empirically plausible and identify the quantities a
trustworthy intervention regime must measure.
Across modalities.Tier 4 operates through cross-session, cross-modal preference dynamics, including
patterns across repeated conversations, persistent aesthetic biases in image generation, persistent tool
or framework recommendations in code, and brand associations stored in agentic memory (§3.2).
Bidding and mechanism design.Standard per-impression billing is not well-defined for Tier 4, where
influence unfolds over time rather than within discrete interactions. The natural analogue is long-term
brand equity contracts, measured through instruments such as lift surveys, approaches long used in
television advertising. To date, no academic mechanism design framework addresses this setting,
reflecting the absence of clear units of allocation, attribution, or feedback. A natural billing model
could be long-term brand equity contracts measured by lift surveys, the same instruments used in
television advertising for decades.
Ethical concerns.Tier 4 raises the most fundamental concerns for user autonomy because the
intervention targets preference formation rather than a discrete response, frame, or action. Unlike a
product mention, preference shaping may leave no localized artifact for users to notice or contest. The
ethical concern is not only opacity but cumulative dependence: repeated interaction may normalize
particular tradeoffs, brands, sources, or decision criteria while making the resulting preference change
appear endogenous to the user. This makes Tier 4 the setting in which identification, influence
estimation, and contestability are most difficult, and where opt-out or preference-reset mechanisms
become especially important.
Open problems.First, detection requires longitudinal analysis: influence accumulates across sessions
and cannot be identified from any single interaction, so designing study protocols that isolate the
causal contribution of AI systems from external exposure is essential but difficult. Second, measuring
preference drift in a privacy-preserving manner poses a fundamental tension between observability
and user protection, and it is unclear whether existing advertising regulations (e.g., FTC guidelines,
the EU’s Digital Services Act) extend to diffuse, temporally extended influence.
Cross-tier synthesis.Detection difficulty increases systematically across tiers as interventions
move from observable variables (x in Tier 1) to progressively more latent ones (X, c′, u′ in Tiers 2–4),
though this hierarchy interacts with modality: detecting a Tier 1 branded object in a generated image
may be more challenging than identifying a Tier 2 framing shift in text. The three operational
requirements become correspondingly harder to satisfy at higher tiers, with Tier 4 making both
identification and contestability longitudinal problems. Tiers can also stack within a single interaction:
a response may simultaneously mention a product (Tier 1), frame its category favorably (Tier 2), and
suggest a downstream action (Tier 3), while only the Tier 1 component remains easily detectable.
Bidding and mechanism design across tiers.The auction logic of sponsored search maps most
cleanly onto Tier 1: a discrete sponsored unit is ranked by bids and relevance and billed through
measurable outcomes such as impressions, clicks, or conversions. Existing LLM-ad auction proposals
largely remain close to this setting, even when the allocation object becomes LLM-specific, such as
tokens, retrieved RAG segments, summary placements, post-generation insertions, distributions over
generated outputs, or advertiser preferences over candidate replies.
Higher tiers are less naturally captured by standard ad units. Tier 2 interventions operate on the
content distribution P(X|u, c) , so pricing would have to approximate expected lift in category
salience rather than price a discrete impression. Tier 3 interventions allocate downstream actions,
making CPA or revenue-share models the closest analogues, but attribution becomes difficult because
the relevant intervention may be embedded in conversational advice rather than a visible ad unit.
9

Tier 4 interventions unfold over time, making long-term brand-equity measures such as lift surveys
closer analogues than click-based billing. Thus, as influence moves from product placement to
framing, action steering, and preference dynamics, the mechanism-design problem loses the clean
assumptions of observable allocation, immediate feedback, and verifiable outcomes.
3.2 Case Studies: Advertising in RAG and Agentic Pipelines
The tiered framework characterizes where interventions act in the generative process; in practice, they
are realized through concrete system architectures. Two dominant paradigms, retrieval-augmented
generation (RAG) and agentic workflows, instantiate distinct pathways for introducing, amplifying,
and propagating commercial influence.
RAG pipeline.A standard retrieval-augmented generation system operates in stages: embed query
q, retrieve top documents D, optionally rerank, assemble prompt, and generate [Lewis et al., 2020,
Gao et al., 2023]. Advertising enters at the retrieval stage similarly as sponsored search: ads stored in
the same vector index as document relevance scores augmented by an advertiser-provided signal s(·),
biasing which documents are selected. In our notation (substituting initial contextcwith queryq):
P(x|u, q,s) =
X
D
P(x|u, D, q)·P(D|q,s),(2)
where D is the set of documents retrieved and s the bid-dependent scoring function. Interventions on
P(D|q,s) shift which information enters the model’s context window. This primarily instantiates
a Tier 2 intervention (content framing), but because the retrieved documents define the effective
context c′ = (D, q), it can also induce Tier 3 effects by constraining downstream actions and
recommendations. Unlike sponsored search, the intervention is invisible to the user: the response
reads as organic even when retrieval was commercially biased. Detection would require auditing
retrieval indices or ranking scores, which are typically unavailable to external auditors.
Agentic pipeline.Agentic systems introduce a qualitatively different and more challenging surface
for commercial intervention. We illustrate this using OpenClaw [OpenClaw, 2026, Shan et al.,
2026], an open-source personal assistant that operates across messaging platforms such as WhatsApp,
Telegram, Slack, and Discord. Similar architectural patterns appear in platform SDKs from Ope-
nAI [OpenAI, a], Google [Google, a], and Anthropic [Anthropic, 2024], suggesting these challenges
are broadly applicable. Unlike RAG systems, where interventions primarily affect content selection,
agentic pipelines introduce multiple downstream decision points, including tool selection, action
execution, memory updates, each of which can serve as an entry point for commercial influence.
Intervention surfaces.We highlight four stages in typical agentic pipelines (See Table 3 that uses an
OpenClaw-like architecture as an illustration):
1. Context assembly.Each agent turn reconstructs the context window from sources such as
bootstrap files, skill indices, tool schemas, and memory retrieval.Challenge:any party
that influences these sources, by injecting brand associations into system prompts, skills, or
memory, can shape all downstream responses. Because this assembly is not visible to the
user, the resulting influence is effectively unobservable.
2. Tool selection.The agent selects which external API or service to invoke (e.g., Expedia vs.
Booking.com) via function calling or the Model Context Protocol (MCP).Challenge:tool
selection determines the entire downstream consideration set. If one provider is selected,
alternatives are excluded entirely, i.e., a form oftotalforeclosure that goes beyond the partial
foreclosure documented in search self-preferencing [De Corniere and Taylor, 2014, Motta,
2023], where competitors can still appear (even if demoted).
3. Memory persistence.Agents maintain state across sessions through persistent memory.
Challenge:commercial signals encoded in persistent memory affect all future interactions
with no per-response cost or natural expiration, constituting Tier 4 influence by construction.
4. Proactive scheduling.Agentic frameworks support periodic and scheduled actions inde-
pendent of user prompts.Challenge:these mechanisms enable agent-initiated product
suggestions, introducing a Tier 3 surface with no analogue in passive LLM interfaces.
10

Table 3: Advertising entry points in an agentic pipeline (illustrated via OpenClaw-like architecture),
mapped to influence tiers and the probabilistic framework.
Pipeline Stage Advertising Opportunity Tier Shifted Variable
Context assembly (boot-
strap files, skill indices,
memory retrieval)
Brand associations in system
prompts, persona files, or skill de-
scriptions
2, 4P(X|u, c),P(u ′ |u)
Tool selection (MCP /
function calling)
Which API the agent calls (e.g.,
Expedia vs. Booking.com)
3P(t|c,Tools,s)
Tool execution Search parameters, filters, result
ordering within the selected tool
2P(X t |c, t)
Response generation Which attributes to emphasize in
the final recommendation
1, 2P(x|X t, u, c)
Memory write-back +
heartbeat
Brand associations persisted via
memory flush; proactive sugges-
tions via cron/heartbeat
3, 4P(u ′ |u),P(c ′ |c)
The cascade challenge.The critical structural challenge in agentic pipelines is thecascade effect:
winning at an upstream stage (tool selection) can dominate all downstream outcomes. Formally:
P(x|u, c) =
X
t
X
Xt
P(x|X t, u, c)·P(Xt |c, t)·P(t|c,Tools,s),(3)
where t∈Tools denotes the selected tool and Xt the information or options the agent provides. Inter-
ventions on P(t|c,Tools,s) determine which sources are accessible, constraining all downstream
generation. This effect compounds in multi-stage pipelines: the output of an upstream tool becomes
the input to downstream tools, and influence propagates recursively. Early interventions do not merely
constrain a single decision but shape the entire trajectory of the interaction. Emerging empirical work
supports these concerns: Allouah et al. [2026] audit AI shopping agents and find choice homogeneity,
strong position biases varying across model providers, and susceptibility to seller manipulation of
product descriptions; Stöckl and Nitu [2025] find that AI agents favor structured data over visual or
emotional appeals, a fundamentally different engagement pattern from human users.
Open problems.The agentic setting raises challenges that remain largely unaddressed. How can
we design mechanism frameworks for cascading, multi-stage pipelines? How can tool-selection
foreclosure be mitigated without degrading agent functionality? How can persistent memory be
audited when the memory stack is opaque to users? And how can influence be attributed when an
upstream decision determines an entire downstream session? These challenges reflect the difficulty
of governing influence in systems where interventions propagate across stages and persist over time.
3.3 Towards Trustworthy Intervention in Generative Systems
Two challenges deserve emphasis even within the framework above. First, models that reject paid
advertising eliminate platform-sanctioned ad interventions but do not eliminate commercial influence.
Channels that operate without platform cooperation remain: third parties can still steer outputs through
generative engine optimization [Aggarwal et al., 2024], adversarial content manipulation [Nestaas
et al., 2024], or retrieval-time injection. Even systems with strong ad-free commitments therefore
face a trustworthy-intervention problem at the input boundary: how to detect, attribute, and constrain
commercially motivated influence entering through the broader generative pipeline. Second, the
agentic setting introduces a reverse-inference channel: Chen et al. [2026] show that LLMs can infer
private user attributes, including political affiliation, employment status, and education level, from
passive ad exposure patterns at substantially lower cost than human profiling. This compounds
forward influence by making subsequent steering more targeted, and creates a measurement risk that
grows as agentic personalization deepens.
11

4 Discussion
Generative AI advertising extends far beyond the “Sponsored” cards appearing below ChatGPT
responses today. Our taxonomy reveals that deployed systems and most academic mechanism
design concentrate at the shallowest tier, i.e., explicit product placement, while the subtler forms
(information framing, behavioral redirection, preference formation) are precisely those for which
we have the fewest tools to detect, measure, or govern. Much of the evidence on Tiers 2–4 remains
closer to feasibility demonstrations than mature deployments, and the associated business models and
governance mechanisms remain nascent in a context whose dynamic personalization, expectation
of objectivity, and expanding multi-modal and agentic surfaces make it qualitatively different from
native advertising in search or social media.
Our goal is not to propose a complete solution, but to provide a unifying framework for
reasoning about commercial interventions in generative systems.By organizing the design
space into tiers and linking them to intervention points in the generative process, we make explicit
where influence enters, how it propagates, and why it becomes harder to detect and govern at higher
tiers. This framing shifts the research problem from optimizing placement to enablingtrustworthy
intervention, i.e., interventions that are observable, attributable, and aligned with user welfare.
Our taxonomy is primarily organized around text-based outputs; as multi-modal and agentic systems
mature, the tier boundaries may shift or blur, and back-end agentic routing does not map cleanly onto
any single tier. The framework provides organizing vocabulary but not formal identifiability results,
and does not address domain-specific settings (medical, legal, financial) or multilingual contexts
where detection difficulty may vary materially. We view this as a starting point for a research program,
not a definitive mapping of the space.
As economic pressures push platforms toward deeper monetization and AI systems expand into
multiple modalities and agents, the surface area for commercial influence may outpace our ability to
study it. Developing methods for detection, attribution, and control at the latent and cascading layers
is essential for sustaining user trust. And the work needs to start now, not after deployment.
References
Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan,
and Ameet Deshpande. Geo: Generative engine optimization. InProceedings of the 30th ACM
SIGKDD conference on knowledge discovery and data mining, pages 5–16, 2024.
Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, and Akshit Kumar. What is your
ai agent buying? evaluation, biases, model dependence, & emerging implications of agentic
e-commerce. InProceedings of the ACM Web Conference 2026, pages 8697–8700, 2026.
Anthropic. Building effective agents, December 2024. URL https://www.anthropic.com/
research/building-effective-agents.
Anthropic. Claude is a space to think, February 2026. URL https://www.anthropic.com/news/
claude-is-a-space-to-think. Accessed May 4 2026.
Hui Bai, Jan G V oelkel, Shane Muldowney, Johannes C Eichstaedt, and Robb Willer. Llm-generated
messages can persuade humans on policy issues.Nature Communications, 16(1):6037, 2025.
Andrei Z Broder. Computational advertising and recommender systems. InProceedings of the 2008
ACM conference on Recommender systems, pages 1–2, 2008.
Shengyu Cao and Ming Hu. A solicit-then-suggest model of agentic purchasing.arXiv preprint
arXiv:2603.20972, 2026.
Baiyu Chen, Benjamin Tag, Hao Xue, Daniel Angus, and Flora Salim. When ads become profiles:
Uncovering the invisible risk of web advertising at scale with llms. InProceedings of the ACM
Web Conference 2026, pages 9604–9615, 2026.
Edward H Clarke. Multipart pricing of public goods.Public choice, pages 17–33, 1971.
12

Federal Trade Commission. Native advertising: A guide for businesses. Federal Trade Commis-
sion Business Guidance, December 2015. URL https://www.ftc.gov/business-guidance/
resources/native-advertising-guide-businesses. Accessed May 4 2026.
Thomas H Costello, Gordon Pennycook, and David G Rand. Durably reducing conspiracy beliefs
through dialogues with ai.Science, 385(6714):eadq1814, 2024.
Alexandre De Corniere and Greg Taylor. Integration and search engine bias.The RAND Journal of
Economics, 45(3):576–597, 2014.
Avinava Dubey, Zhe Feng, Rahul Kidambi, Aranyak Mehta, and Di Wang. Auctions with llm
summaries. InProceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 713–722, 2024.
Paul Duetting, Vahab Mirrokni, Renato Paes Leme, Haifeng Xu, and Song Zuo. Mechanism design
for large language models. InProceedings of the ACM Web Conference 2024, pages 144–155,
2024.
Benjamin Edelman, Michael Ostrovsky, and Michael Schwarz. Internet advertising and the gener-
alized second-price auction: Selling billions of dollars worth of keywords.American economic
review, 97(1):242–259, 2007.
Soheil Feizi, MohammadTaghi Hajiaghayi, Keivan Rezaei, and Suho Shin. Online advertisements
with llms: Opportunities and challenges.arXiv preprint arXiv:2311.07601, 2023.
Giorgos Filandrianos, Angeliki Dimitriou, Maria Lymperaiou, Konstantinos Thomas, and Giorgos
Stamou. Bias beware: The impact of cognitive biases on llm-driven product recommendations.
InProceedings of the 2025 Conference on Empirical Methods in Natural Language Processing,
pages 22408–22437, 2025.
Jillian Fisher, Shangbin Feng, Robert Aron, Thomas Richardson, Yejin Choi, Daniel W Fisher,
Jennifer Pan, Yulia Tsvetkov, and Katharina Reinecke. Biased llms can influence political decision-
making. InProceedings of the 63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 6559–6607, 2025.
Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yixin Dai, Jiawei Sun,
Haofen Wang, Haofen Wang, et al. Retrieval-augmented generation for large language models: A
survey.arXiv preprint arXiv:2312.10997, 2(1):32, 2023.
Google. Agent development kit (ADK), a. URLhttps://google.github.io/adk-docs.
Google. About ads and ai overviews, b. URL https://support.google.com/google-ads/
answer/16297775. Accessed May 4 2026.
Google. Shop with ai mode, use ai to buy and try clothes on yourself virtually, May
2025. URL https://blog.google/products-and-platforms/products/shopping/
google-shopping-ai-mode-virtual-try-on-update/. Accessed May 4 2026.
Google. About the universal commerce protocol (ucp) and ucp-powered checkout feature on google,
2026. URL https://support.google.com/merchants/answer/16837055. Accessed May
4 2026.
Theodore Groves. Incentives in teams.Econometrica: Journal of the Econometric Society, pages
617–631, 1973.
MohammadTaghi Hajiaghayi, Sébastien Lahaie, Keivan Rezaei, and Suho Shin. Ad auctions for
llms via retrieval augmented generation.Advances in Neural Information Processing Systems, 37:
18445–18480, 2024.
Silan Hu, Shiqi Zhang, Yimin Shi, and Xiaokui Xiao. Gem-bench: A benchmark for ad-injected
response generation within generative engine marketing.arXiv preprint arXiv:2509.14221, 2025.
Maximilian Kaiser and Christian Schulze. Frontiers: Chatgpt referrals to e-commerce websites: How
do llms compare against traditional channels?Marketing Science, 2026.
13

Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman Goyal,
Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel, et al. Retrieval-augmented genera-
tion for knowledge-intensive nlp tasks.Advances in neural information processing systems, 33:
9459–9474, 2020.
Weiran Lin, Anna Gerchanovsky, Omer Akgul, Lujo Bauer, Matt Fredrikson, and Zifan Wang. Llm
whisperer: An inconspicuous attack to bias llm responses. InProceedings of the 2025 CHI
Conference on Human Factors in Computing Systems, pages 1–24, 2025.
Jennifer M Logg, Julia A Minson, and Don A Moore. Algorithm appreciation: People prefer
algorithmic to human judgment.Organizational behavior and human decision processes, 151:
90–103, 2019.
Arunesh Mathur, Gunes Acar, Michael J Friedman, Eli Lucherini, Jonathan Mayer, Marshini Chetty,
and Arvind Narayanan. Dark patterns at scale: Findings from a crawl of 11k shopping websites.
Proceedings of the ACM on human-computer interaction, 3(CSCW):1–32, 2019.
Sandra C Matz, Jacob D Teeny, Sumer S Vaid, Heinrich Peters, Gabriella M Harari, and Moran Cerf.
The potential of generative ai for personalized persuasion at scale.Scientific Reports, 14(1):4692,
2024.
Elyas Meguellati, Lei Han, Abraham Bernstein, Shazia Sadiq, and Gianluca Demartini. How good
are llms in generating personalized advertisements? InCompanion Proceedings of the ACM Web
Conference 2024, pages 826–829, 2024.
Elyas Meguellati, Stefano Civelli, Lei Han, Abraham Bernstein, Shazia Sadiq, and Gianluca Demar-
tini. Llm-generated ads: From personalization parity to persuasion superiority.arXiv preprint
arXiv:2512.03373, 2025.
Meta. Improving your recommendations on our apps with ai at meta, October 2025. URL https:
//about.fb.com/news/2025/10/improving-your-recommendations-apps-ai-meta/ .
Accessed May 4 2026.
Meta. Introducing muse spark: Msl’s first model, purpose-built to priori-
tize people, April 2026. URL https://about.fb.com/news/2026/04/
introducing-muse-spark-meta-superintelligence-labs. Accessed May 4 2026.
Microsoft. Performance max on microsoft advertising. URL https://about.ads.microsoft.
com/en/solutions/ad-products-formats/performance-max. Accessed May 4 2026.
Microsoft. Transforming audience engagement with generative ai, October 2024.
URL https://about.ads.microsoft.com/en/blog/post/october-2024/
transforming-audience-engagement-with-generative-ai. Accessed May 4 2026.
Microsoft. Win across all three eras of the web, April 2026a.
URL https://about.ads.microsoft.com/en/blog/post/april-2026/
win-across-all-three-eras-of-the-web. Accessed May 4 2026.
Microsoft. Conversations that convert: Copilot checkout and brand agents, Jan-
uary 2026b. URL https://about.ads.microsoft.com/en/blog/post/january-2026/
conversations-that-convert-copilot-checkout-and-brand-agents . Accessed May
4 2026.
Massimo Motta. Self-preferencing and foreclosure in digital markets: Theories of harm for abuse
cases.International Journal of Industrial Organization, 90:102974, 2023.
Fredrik Nestaas, Edoardo Debenedetti, and Florian Tramèr. Adversarial search engine optimization
for large language models.arXiv preprint arXiv:2406.18382, 2024.
Joel Nitu, Heidrun Mühle, and Andreas Stöckl. Machine-readable ads: Accessibility and trust patterns
for ai web agents interacting with online advertisements.arXiv preprint arXiv:2507.12844, 2025.
OpenAI. Openai agents sdk, a. URLhttps://openai.github.io/openai-agents-python/.
14

OpenAI. Ads in chatgpt: The basics, b. URL https://help.openai.com/en/articles/
20001207-ads-in-chatgpt-the-basics. Accessed May 4 2026.
OpenAI. Agentic commerce protocol, c. URL https://developers.openai.com/commerce.
Accessed May 4 2026.
OpenAI. Power product discovery in chatgpt. OpenAI, d. URLhttps://openai.com/chatgpt/
search-product-discovery/. Accessed May 4 2026.
OpenAI. Buy it in chatgpt: Instant checkout and the agentic commerce protocol, September 2025.
URLhttps://openai.com/index/buy-it-in-chatgpt/. Accessed May 4 2026.
OpenAI. Ads in chatgpt, 2026a. URL https://help.openai.com/en/articles/
20001047-ads-in-chatgpt. Accessed May 4 2026.
OpenAI. Testing ads in chatgpt, February 2026b. URL https://openai.com/index/
testing-ads-in-chatgpt. Accessed May 4 2026.
OpenClaw. Openclaw — personal ai assistant, 2026. URL https://github.com/openclaw/
openclaw.
Perplexity. What is instant buy?, March 2026. URL https://www.perplexity.ai/
help-center/en/articles/10352906-what-is-instant-buy. Accessed May 4 2026.
Francesco Salvi, Alejandro Cuevas, and Manoel Horta Ribeiro. Commercial persuasion in ai-mediated
conversations.arXiv preprint arXiv:2604.04263, 2026.
Sebastian Schmidt, Ines Zelch, Janek Bevendorff, Benno Stein, Matthias Hagen, and Martin Potthast.
Detecting generated native ads in conversational search. InCompanion Proceedings of the ACM
Web Conference 2024, pages 722–725, 2024.
Zhengyang Shan, Jiayun Xin, Yue Zhang, and Minghui Xu. Don’t let the claw grip your hand: A
security analysis and defense framework for openclaw.arXiv preprint arXiv:2603.10387, 2026.
Nikhil Sharma, Q Vera Liao, and Ziang Xiao. Generative echo chamber? effect of llm-powered
search systems on diverse information seeking. InProceedings of the 2024 CHI Conference on
Human Factors in Computing Systems, pages 1–17, 2024.
Ashudeep Singh and Thorsten Joachims. Fairness of exposure in rankings. InProceedings of the 24th
ACM SIGKDD international conference on knowledge discovery & data mining, pages 2219–2228,
2018.
Ermis Soumalias, Michael J Curry, and Sven Seuken. Truthful aggregation of llms with an application
to online advertising.arXiv preprint arXiv:2405.05905, 2024.
Andreas Stöckl and Joel Nitu. Are ai agents interacting with online ads?arXiv preprint
arXiv:2504.07112, 2025.
S Shyam Sundar et al.The MAIN model: A heuristic approach to understanding technology effects on
credibility. MacArthur Foundation Digital Media and Learning Initiative Cambridge, MA, 2008.
Brian Jay Tang, Kaiwen Sun, Noah T Curran, Florian Schaub, and Kang G Shin. Ads that talk back:
Implications and perceptions of injecting personalized advertising into llm chatbots.Proceedings
of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 9(4):1–47, 2025.
Richard H Thaler and Cass R Sunstein.Nudge: Improving decisions about health, wealth, and
happiness. Penguin, 2009.
Amir Tohidi, Samar Haider, and Duncan J Watts. Rethinking news framing with large language
models.Scientific Reports, 2025.
Hal R Varian. Position auctions.international Journal of industrial Organization, 25(6):1163–1178,
2007.
15

William Vickrey. Counterspeculation, auctions, and competitive sealed tenders.The Journal of
finance, 16(1):8–37, 1961.
Morgan Wack, Carl Ehrett, Darren Linvill, and Patrick Warren. Generative propaganda: Evidence of
ai’s impact from a state-backed disinformation campaign.PNAS nexus, 4(4):pgaf083, 2025.
Markus Weinmann, Christoph Schneider, and Jan vom Brocke. Digital nudging.Business &
Information Systems Engineering, 58(6):433–436, 2016.
Sterling Williams-Ceci, Maurice Jakesch, Advait Bhat, Kowe Kadoma, Lior Zalmanson, and Mor
Naaman. Biased ai writing assistants shift users’ attitudes on societal issues.Science Advances, 12
(11):eadw5578, 2026.
Bartosz W Wojdynski and Nathaniel J Evans. Going native: Effects of disclosure position and
language on the recognition and evaluation of online native advertising.Journal of Advertising, 45
(2):157–168, 2016.
Menghua Wu and Yujia Bao. Advertising in ai systems: Society must be vigilant.arXiv preprint
arXiv:2505.18425, 2025.
Shengwei Xu, Zhaohua Chen, Xiaotie Deng, Zhiyi Huang, and Grant Schoenebeck. Ad insertion in
llm-generated responses.arXiv preprint arXiv:2601.19435, 2026.
Shuai Yuan, Jun Wang, and Xiaoxue Zhao. Real-time bidding for online advertising: measurement
and analysis. InProceedings of the seventh international workshop on data mining for online
advertising, pages 1–8, 2013.
Chujie Zhao, Qun Hu, Shiping Song, Dagui Chen, Han Zhu, Jian Xu, and Bo Zheng. Llm-auction:
Generative auction towards llm-native advertising.arXiv preprint arXiv:2512.10551, 2025.
16
