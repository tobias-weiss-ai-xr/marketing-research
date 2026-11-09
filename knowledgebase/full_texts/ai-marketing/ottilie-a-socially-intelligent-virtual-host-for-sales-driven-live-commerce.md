---
title: 'Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce'
url: https://arxiv.org/abs/2605.14542
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: arXiv (Cornell University)
authors:
- Yuyan Chen
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.14542
pages: 10
chars: 56387
fetched_at: '2026-11-08T13:31:00+00:00'
kb_version: 1
---

# Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce

Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live
Commerce
Yuyan Chen∗
ModelsLive Inc.
ychen@modelslive.org
Abstract
A skilled live-commerce host is not merely a narrator, but a sales
agent who converts viewer curiosity into purchase intent through
expert product knowledge, emotionally intelligent response tactics,
and entertainment that serves as a vehicle for product exposure. Yet
no existing AI system replicates this. Conversational recommenders
treat recommendation as a terminal act, while general-purpose
LLMs hallucinate product claims and default to generic promo-
tional templates that fail to engage or persuade. We present Ottilie,
a sales-conversion-oriented virtual host for Chinese beauty live
commerce that grounds product responses in a verified knowledge
base, adapts discourse strategy to viewer intent through empathetic
amplification, evidence-backed rebuttal, and humor-mediated de-
flection, and supervises all four output fields simultaneously within
a structured generation framework. Experiments demonstrate gains
of 14% on informativeness and 5% on factual correctness, with con-
sistent advantages in tactfulness and viewer engagement. Ottilie
has been deployed as an autonomous English-language host on
Twitch, where the same fine-tuned model runs unattended on a
single commodity GPU and promotes the company’s own prod-
uct; we report how the system adapted to a new language, market,
and product without retraining, and what the deployment revealed
about latency and adversarial chat.
1 Introduction
Live-streaming commerce has emerged as one of the fastest-growing
retail formats worldwide, with the global market expanding at a
CAGR of over 33% and live conversion rates up to ten times higher
than those of conventional e-commerce [18]. A typical session lasts
four to six hours, and the host’s ultimate objective throughout is
sales conversion, turning viewer curiosity and entertainment en-
gagement into concrete purchase actions. Consider the two viewer
interactions in Figure 1. In Scenario 1, a viewer expresses purchase
hesitation and a conventional host responds with a pressure-driven
urgency script, while a skilled sales host draws on personal experi-
ence to build trust and nudge the decision forward. In Scenario 2, a
viewer shares positive feedback and a conventional host deflects
with a generic acknowledgement, while a skilled sales host imme-
diately converts the testimonial into social proof for the rest of the
audience and embeds a purchase cue. Both scenarios illustrate the
same gap: conventional hosts treat viewer comments as interrup-
tions to manage, while an effective live-commerce host treats every
comment as a conversion opportunity.
Existing approaches each address only a subset of this problem.
Conversational recommendation systems [3, 26, 31] treat recom-
mendation as a terminal dialogue act and cannot sustain ambient
narration; we include KGSF [31] and ChatCRS [13] as representative
∗Yuyan Chen is the Founder and CEO of ModelsLive Inc.
Figure 1: Two representative live-commerce interactions il-
lustrating the core challenge. Each scenario shows a viewer
comment followed by two virtual host responses.
baselines in our evaluation. Product-oriented QA systems [2, 17]
handle isolated queries without session-level pacing. Virtual anchor
systems [27, 28] deliver pre-scripted content without interactive
capability. Applying general LLMs [16, 30] directly produces out-
puts that are too long for real-time TTS, hallucinate ingredient
properties absent from any product record, and treat each comment
independently, collapsing session coherence.
We argue that building a sales-conversion-oriented virtual host
is structurally difficult for reasons beyond scale, and identify three
fundamental challenges that prior work does not jointly address.
The first is the challenge betweencontinuous product exposureand
responsive interaction, where a sales host must maintain uninter-
rupted narration that keeps products in view while simultaneously
responding to viewer comments that interrupt the pitch, a require-
ment that a single-generation pipeline cannot satisfy without ex-
plicit resource coordination. The second is the challenge between
sales expertiseandbroadcast fluency, where effective selling requires
deep, accurate product knowledge including ingredients, suitability,
and regulatory boundaries, yet this knowledge must be delivered in
the casual, entertaining register of live broadcast rather than clini-
cal product description, and unconstrained LLMs achieve higher
lexical fluency precisely by fabricating product claims beyond what
the catalogue supports. The third is the challenge betweensocially
intelligent sales tacticsandtraining efficiency, where a skilled host
deploys qualitatively distinct strategies per viewer intent, but these
strategy differences are invisible to content-based automatic met-
rics, requiring explicit intent supervision.
arXiv:2605.14542v2  [cs.AI]  28 Sep 2026

Yuyan Chen
To address these three challenges, we present Ottilie1, a socially
intelligent virtual host for sales-driven live commerce, developed
and evaluated in the Chinese beauty vertical and subsequently de-
ployed as an English-language host on Twitch (Section 6). China’s
live-commerce market generated $844B in 2025 with 81% shopper
penetration versus 40% in the US [1, 6, 8, 15] making it the world’s
most mature live-commerce ecosystem and an ideal environment
to study AI-assisted hosting at scale. To resolve the responsiveness
challenge, we propose a dual-channel architecture where a scripted
idle channel maintains continuous product narration while an inter-
active channel handles viewer comments with preemptive priority.
To resolve the expertise challenge, we design a structured product
knowledge base with a controlled ingredient glossary that supplies
the factual foundation for product-related claims. To resolve the
efficiency challenge, we construct intent-conditioned fine-tuning
data with four discourse-strategy labels within a unified structured
output framework.
2 Related Work
Conversational recommendation.Ye et al . [29] study how avatar
anthropomorphism affects viewer co-creation through social pres-
ence. Huang et al. [11] extend lifelike audio-driven talking faces to
streaming avatar generation with infinite audio context. Wang et al.
[25] use knowledge-graph retrieval to reduce hallucination in LLM-
based recommenders. Li et al. [13] decompose conversational rec-
ommendation into a knowledge retrieval agent and a goal-planning
agent. Feng et al. [7] apply reinforcement learning over retrieved
candidate sets for conversational recommendation. Tangarajan et al.
[24] build a contextual RAG framework for e-commerce product QA.
Unlike these systems, Ottilie jointly addresses continuous narration,
intent-stratified social tactics, and catalogue-grounded generation.
Intent conditioning.Sali and Toraman [20] show LLMs remain
brittle on out-of-distribution intents in task-oriented dialogue, and
Hong et al. [9] demonstrate that intent-label quality directly con-
trols downstream response appropriateness. Shen et al. [21] study
structured output generation via schema-embedded training, while
Dong et al. [5] introduce grammar-based constrained decoding and
Tam et al. [22] show such constraints can degrade semantic correct-
ness. Zhu et al. [32] improve LoRA fine-tuning efficiency via kernel
fusion. On evaluation, Li et al . [14] survey LLM-as-judge across
scoring and ranking tasks, Tang et al. [23] train a multi-turn dia-
logue evaluator from multiple LLM judges. Ottilie addresses these
limitations by embedding intent tags and format constraints directly
into training rather than relying on inference-time prompting.
3 Data and Knowledge Base
Fine-tuning Dataset.We construct 1,475 annotated instances
from two equally sized sources: naturally occurring comments
collected from public Chinese beauty broadcasts, and stylistically
matched synthetic comments generated by GPT-5.2 which was the
most capable available model at the time of data collection to ensure
balanced coverage across all four intent categories, with each real
instance paired with one synthetic counterpart of similar style but
distinct content. Intent labels are assigned by GPT-5.2 and verified
1Formerly released as VerbalValue. Live channel: https://www.twitch.tv/modelslive.
by three human annotators who independently judge label correct-
ness as a binary decision and generation naturalness on a 1–5 scale.
An instance is retained only if all three annotators agree on the
label and the mean naturalness score exceeds 4.5, and is otherwise
relabelled or regenerated. A four-pass cleaning pipeline further
removes near-duplicates with character n-gram Jaccard above 0.7,
personally identifiable information, structurally invalid responses,
and semantically incoherent samples via a sentence-encoder filter.
The resulting dataset covers four intent categories. Inquiry accounts
for 590 instances at 40%, Scepticism for 297 at 20%, Appreciation
for 294 at 20%, and Antagonism for 294 at 20%.
Each instance consists of a system prompt encoding persona and
format constraints, an intent-tagged viewer comment, and a target
response in a fixed four-field schema: a spoken broadcast field of at
most two colloquial sentences, an 8–12 Chinese character display
slogan inspired by multimodal caption generation [ 4], a follow-
up engagement question designed to elicit viewer response, and a
call-to-action (CTA) phrase such as claiming a coupon or clicking
the product link. By supervising all four fields simultaneously, the
model learns to disentangle spoken broadcast content from display
text, engagement cues, and conversion guidance within a single
generation step.
Product Knowledge Base.The product knowledge base grounds
generation in verified domain expertise, constraining responses
to catalogue-verified content. The catalogue covers 12 skincare
products spanning cleansers, serums, moisturizers, and sunscreens.
Each record contains the canonical product name, category, key
ingredients with their functional roles, texture, suitable skin types,
usage instructions, curated live talking points, and a compliance dis-
claimer. An internal routing identifier, a numeric product ID used for
session-state management, is excluded from all generation contexts
to prevent leakage into spoken output. A companion ingredient
glossary maps 23 ingredient names to neutral, non-pharmacological
descriptions, bounding the permitted interpretation space for in-
gredient queries and reducing hallucination risk under platform
compliance constraints. A pitch script corpus provides one broad-
cast monologue of between 180 and 240 Chinese characters per
catalogue entry, following a hook-explain-guide-close arc.
4 Method
Figure 2 illustrates the Ottilie architecture.
4.1 Intent-Conditioned Fine-Tuning
We fine-tune Qwen2.5-32B [ 19] using LoRA [ 10] on the intent-
conditioned dataset described in Section 3. Each training instance
presents the model with an explicit intent tag that directly condi-
tions generation toward the appropriate discourse strategy: author-
itative product guidance for inquiry, social-proof amplification for
appreciation, empathetic evidence-backed rebuttal for scepticism,
and humor-mediated deflection for antagonism. All four output
fields are supervised simultaneously within a single generation
step, and the system prompt is embedded into every training in-
stance, making format compliance a first-class training objective
rather than a post-hoc inference constraint. At inference, viewer
comments are matched against the product knowledge base via
keyword-based category detection and coverage scoring. When a

Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce
(A) Dialogue Service (B) Media Service
2) Interactive Response Channel (Q&A)
Lightweight
1) Sentence-level Streaming TTS
Input text
Clause segmentation
and incremental synthesis
Sequential audio queue (per sentence/clause)
C1 C2 C3• • • Cn
ONNX TTS Model
Sentence-level streaming synthesis
(low latency, interruptible)
2) Product Asset Hosting
Product images
hosted by ID
Static assets hosting
with timestamped URLs
LIVE
Live Caption Product Display
‹ ›
1) State Machine
Playing-
Idle
Awaiting-
Reply
Playing-
Reply
2) Interaction & Control Layer
GET /idle_next
(polling)
POST /chat
(streaming)
Audio playback
& state events
Product timeline
& switching
CCCaption & subtitle
append on audio-start
Lip sync control
(event-driven)
Final Structured Response
{ }
•speak lines
•caption
•hook question
•cta
Resources Construction
Product Script Library Product Knowledge Base
1) Idle Pitch Channel (Broadcast)
Select next
idle script
product id
resolution
Trigger image
switch in frontend
Viewer
comment
+
context
LLM
N candidates
1
…
5
6
Reranker
product
id
(C) Client Runtime
(D) Frontend Presentation
Idle
Resu-
ming
★ Topic Relevance
★ Product Alignment
★ Style Freshness
★ Anti-repetition
Figure 2: Ottilie architecture. The dual-channel dialogue service dispatches scripted narration and interactive responses under
shared audio resource arbitration. The media service handles TTS synthesis and asset serving. The browser frontend coordinates
playback, subtitles, product display, and lip animation.
match is found, the retrieved product record is serialised and ap-
pended to the system prompt, grounding generation in catalogue-
verified claims without a separate retrieval model. Six candidate
responses are generated and ranked by a scoring function penal-
ising product misalignment, unsanctioned product mentions, and
repetition, with the highest-scoring candidate selected.
4.2 Dual-Channel Architecture
The dialogue service maintains a five-stage session state machine
that arbitrates a single shared audio resource between two channels.
The idle channel cycles through the pitch script corpus sequentially,
maintaining continuous product narration during viewer inactivity.
Upon comment arrival, the interactive channel issues a preemptive
interrupt, locks the audio resource for response delivery, and re-
leases it after a configurable hold period, resuming idle narration
from the saved sentence boundary. Session state management and
model inference are decoupled from TTS synthesis and product
image serving into two independently deployable services, isolating
latency-sensitive generation from I/O-bound media operations.
5 Experiments
Setup and Baselines.Each test instance comprises an active prod-
uct context, one or more viewer comments with intent labels, and a
reference response.Each test instance comprises an active product
context, one or more viewer comments with intent labels, and a
reference response. We compare against seven baselines: Conver-
sational recommenders include KGSF [31] as a classic knowledge-
graph-based baseline and ChatCRS [13] as a recent tool-augmented
goal-planning baseline, both adapted to output a single response
utterance and post-processed to match the four-field schema for
metric compatibility. Frontier LLMs include GPT-5.5, Claude-4.6,
Gemini-3.1, Grok-4.20, and DeepSeek-V4, all prompted with the
same host persona and product context. We also include Qwen2.5-
32B without fine-tuning to measure the raw model-scale contribu-
tion. For our Ottilie, LoRA [10] is applied to all linear layers with
rank 8 and scaling factor 32. Training is conducted for 20 epochs
with batch size of 32, a learning rate of10 −4, bfloat16 precision,
and a maximum sequence length of 2,048 tokens. At inference time,
we generate six candidates via nucleus sampling with a tempera-
ture of 0.9, a top-𝑝 value of 0.92, and a repetition penalty of 1.12.
The reranker further promotes topical relevance while penalizing
formulaic opening phrases and 𝑛-gram overlap with the five most
recent responses.
Metrics.Human evaluation uses a 1–5 Likert scale scored by
three annotators with Krippendorff’s alpha [12] above 0.7 across
all dimensions, indicating substantial inter-annotator agreement.

Yuyan Chen
Human-as-Judge LLM-as-Judge
Method Info Rele Flue Tact Corr Crea Enga
KGSF 1.63 2.15 2.31 2.22 0.47 1.79 1.87
ChatCRS 2.38 2.86 2.73 2.74 0.52 2.06 2.18
GPT-5.5 3.42 4.86 4.72 4.36 0.74 3.88 3.73
Claude-4.6 3.51 4.434.914.27 0.55 4.23 4.55
Gemini-3.1 2.88 3.76 3.78 3.18 0.38 3.24 3.13
Grok-4.20 3.78 4.79 4.65 4.33 0.82 4.17 4.32
DeepSeek-V4 3.12 4.31 4.55 4.03 0.63 3.74 3.52
Qwen2.5-32B 2.52 3.21 2.25 2.36 0.44 2.58 2.84
Ottilie 4.32 4.914.624.45 0.86 4.52 4.61
↑(abs.) +0.54 +0.05−0.29 +0.09 +0.04 +0.29 +0.06
↑(%) +14.29 +1.03−5.91 +2.06 +4.88 +6.86 +1.32
Table 1: Comparison on the beauty live-commerce evalu-
ation set. Δ rows show improvement of Ottilie over the
best-performing frontier LLM baseline per column. Correct-
ness reports the proportion of responses with no out-of-
catalogue factual claims, and its Δ(%) is computed relative
to the strongest frontier LLM baseline. KGSF and ChatCRS
responses are post-processed into the four-field schema for
metric compatibility.
Comparison Ottilie (%) Baseline (%)
KGSF 94.7 3.1
ChatCRS 92.3 4.2
GPT-5.5 83.7 10.2
Claude-4.6 84.2 9.3
Gemini-3.1 85.3 8.3
Grok-4.20 77.3 14.5
DeepSeek-V4 87.2 8.5
Qwen2.5-32B 91.4 6.8
Table 2: Pairwise human preference rates with 10% compar-
isons per pair. Ottilie (%) is the percentage of comparisons
where annotators selected the Ottilie response. Baseline (%)
is the percentage where the baseline was preferred.
Human-as-Judge LLM-as-Judge
Method Info Rele Flu Tact Corr Crea Enga
w/o TT 3.83 3.95 4.37 3.49 0.68 4.22 4.31
w/o MSS 4.15 4.67 4.33 4.16 0.58 4.01 3.96
w/o PCI 3.14 3.98 4.31 4.06 0.43 4.35 4.42
w/o RR 4.23 4.72 4.51 4.33 0.77 4.27 4.35
Ottilie 4.32 4.91 4.62 4.45 0.86 4.52 4.61
Table 3: Ablation results. TT means interaction-type tags,
MSS means multi-slot supervision, PCI means product con-
text injection, RR means reranking.
Annotators were unpaid volunteers. The five human-judged di-
mensions are Informativeness measuring catalogue-grounded prod-
uct information, Relevance measuring whether the comment in-
tent is addressed, Fluency measuring natural broadcast register,
Tactfulness measuring correct strategy for the given intent class,
and Correctness measuring the proportion of responses contain-
ing no out-of-catalogue factual claims. LLM-as-Judge evaluation
uses Qwen2.5-72B-Instruct on a 1–5 scale given its strong Chinese-
language capability. The two LLM-judged dimensions are Creativ-
ity measuring avoidance of formulaic templates, and Engagement
measuring viewer likelihood of continued interaction. Score-band
definitions and scoring prompts for all seven dimensions are given
in Appendix A.
Main results.Table 1 reports results across all seven dimensions.
KGSF and ChatCRS perform weakest overall, confirming that dis-
crete recommendation systems cannot generate the contextually
adaptive utterances live-commerce hosting requires. Among fron-
tier LLMs, the two largest gains are on Informativeness at+14.29%
and Correctness at+4.88%, both over Grok-4.20, directly validat-
ing the knowledge grounding hypothesis. Without catalogue con-
straints, frontier baselines exhibit hallucination signatures includ-
ing fabricated product names and out-of-whitelist ingredient ad-
vice, and collapse to Inquiry-style responses on Scepticism and
Antagonism inputs. The Tactfulness gain of+2.06% confirms that
strategy differentiation requires explicit intent supervision rather
than model scale alone. Fluency is the only dimension where Ottilie
trails Claude-4.6 at−5.91%, as four-field structured supervision
constrains stylistic freedom while Claude achieves higher fluency
by generating beyond catalogue boundaries at the cost of elevated
hallucination rates.
Moreover, three annotators blind to system identity compared
Ottilie against each baseline on 10% randomly sampled pairwise
instances and selected the preferred response. Table 2 reports the
results. The largest margins are against the conversational rec-
ommenders KGSF at 94.7% and ChatCRS at 92.3%, reflecting the
categorical gap between terminal-recommendation outputs and
ambient socially adaptive responses. The smallest margin is against
Grok-4.20 at 77.3%, consistent with its strong overall performance
on the main evaluation.
Ablation study.Table 3 isolates component contributions. Re-
moving product context injection, denoted w/o PCI, causes the
largest factual degradation with Correctness falling by 0.43 and
Informativeness by 1.18, confirming product-context injection as
the primary grounding mechanism. Removing interaction-type
tags, denoted w/o TT, produces the largest strategy degradation
with Tactfulness falling by 0.96, confirming that intent-conditioned
supervision rather than model scale drives cross-class strategy dif-
ferentiation. Removing multi-slot supervision, denoted w/o MSS,
most strongly reduces Engagement by 0.65, consistent with the
hook question field being a key driver of viewer interaction con-
tinuity. Removing reranking, denoted w/o RR, has the smallest
impact, contributing modest but consistent gains in stylistic quality
atop the fine-tuned backbone.
Intent-stratified analysis.Table 4 reports Ottilie’s performance
broken down by viewer intent class on the four dimensions most
tied to intent-specific behaviour. Scepticism achieves the highest
Tactfulness at 4.51, reflecting the precision required for evidence-
backed rebuttal. Antagonism is the most challenging class with the
lowest Informativeness at 4.01 and Correctness at 0.82, where the

Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce
humorous register occasionally pulls generation toward unverified
claims. Inquiry achieves the highest Correctness at 0.89, consis-
tent with the product-guidance strategy keeping responses closely
anchored to the catalogue. Appreciation produces the highest En-
gagement at 4.72, reflecting the positive audience dynamic that
social-proof amplification sustains. These results confirm that in-
tent conditioning produces qualitatively different response patterns
across classes and that Antagonism remains the hardest intent to
handle without sacrificing factual grounding.
Human-as-Judge LLM-as-Judge
Intent Info Rele Flue Tact Corr Crea Enga
Inquiry 4.62 4.95 4.68 4.38 0.89 4.43 4.55
Scepticism 4.08 4.90 4.60 4.51 0.86 4.55 4.63
Appreciation 4.57 4.93 4.66 4.47 0.87 4.57 4.72
Antagonism 4.01 4.86 4.54 4.44 0.82 4.53 4.54
Table 4: Ottilie performance stratified by viewer intent
class across all seven evaluation dimensions. Scepticism
achieves the highest Tactfulness, reflecting the effectiveness
of evidence-backed rebuttal. Antagonism is the most chal-
lenging class on Informativeness and Correctness, while Ap-
preciation produces the highest Engagement.
Format compliance.Ottilie achieves 98.3% four-field compliance
versus 61.4% for GPT-5.5 and 57.8% for Claude-4.6, as all prompted
baselines frequently collapse the schema into a single prose block
or omit the CTA field.
System latency.Live-streaming imposes a strict perceived-latency
ceiling of approximately two seconds, beyond which a host re-
sponse disrupts session flow. We measure mean wall-clock latency
per pipeline stage on a single A100 80GB GPU. Intent detection
takes 12 ms, knowledge base retrieval takes 38 ms, generation of
six candidates takes 1,240 ms, reranking takes 85 ms, and TTS syn-
thesis of the first sentence takes 210 ms, for a total latency to first
audio onset of 1,585 ms. This is comfortably within the two-second
ceiling. Section 6 reports latency under the resource-constrained
configuration used in production.
Case study.A viewer asks mid-session “Any face cream recom-
mendations?” (Figure 3). This comment requires the system to
retrieve a specific product, establish credibility through ingredient-
level knowledge, and build personal trust to lower purchase re-
sistance. Ottilie retrieves the corresponding catalogue entry, an-
chors the response in whitelisted ingredients, and opens with a
first-person experiential hook that converts product expertise into
personal testimony. This is the trust-building tactic that skilled
human hosts use to make a recommendation feel like a friend’s
advice rather than a sales pitch. In contrast, all four baselines fail as
sales agents, either fabricating product details or deflecting without
a recommendation, and default to generic promotional assertions
that follow a predictable promote-and-push template. Hollow pro-
motional language of this kind erodes viewer trust, and the LLM
judge consistently penalizes it on the Engagement dimension.
The following presents one representative viewer comment for
each of the four intent classes, comparing the spoken-line output
Viewer:Any face cream recommendations? My skin is
dry in winter.
Ottilie:Babe, I recommend this Cloud Cream. It’s on the richer
side and mainly helps support the skin barrier. I have dry, sensitive
skin myself, so in winter my boyfriend once said my face felt rough
when he kissed me. Then he bought me this Cloud Cream. After I
started using it, even our relationship got better.
Grok-4.20:For dry skin in winter, focus on rich, barrier-repairing
creams with ingredients like ceramides, hyaluronic acid (HA),
glycerin, petrolatum, or shea butter. These help replenish moisture,
lock it in, and protect against cold, low-humidity air that strips
natural oils.
Figure 3: Inquiry intent response comparison.
of Ottilie with the response produced by Grok-4.20 under the same
product context and host-persona prompt. Grok-4.20 is chosen as
the strongest frontier baseline and is prompted with the full product
context and persona instruction.
Inquiry.This is an Inquiry-class comment from a viewer in active
purchase consideration. The appropriate strategy is authoritative
product guidance, retrieving a specific product, establishing credi-
bility through ingredient-level knowledge, and lowering purchase
resistance through personal testimony.
Ottilie recommends the Cloud Cream by name, frames it around
the viewer’s specific concern of winter dryness and barrier support,
and immediately grounds the recommendation in a first-person
romantic anecdote that converts product expertise into personal
testimony. The response treats the viewer as a friend receiving
advice rather than a customer receiving a pitch, which is the trust-
building tactic most effective at lowering purchase resistance in a
live-commerce environment.
Grok-4.20 provides a technically accurate overview of ingredient
categories suited for dry winter skin but names no specific product
and cites no catalogue entry. The response reads as a skincare
education post rather than a host recommendation, offering the
viewer general knowledge without a clear purchase direction. The
contrast is shown in Fig. 3.
Scepticism.This is a Scepticism-class comment from a viewer
in active price comparison. The appropriate strategy is empathetic
acknowledgement followed by a specific verifiable rebuttal drawn
from the product catalogue.
Ottilie reframes the price question by shifting the comparison
from upfront cost to total value, arguing that a less effective product
may require repeat purchases and cause skin damage that com-
pounds the cost. The response avoids defensive posturing and repo-
sitions the price objection as a false economy argument, which
is a commercially oriented rebuttal that keeps the viewer moving
toward a purchase decision.
Grok-4.20 effectively validates the viewer’s scepticism by agree-
ing that many luxury products are overpriced relative to their re-
sults. While this is an honest response, it actively undermines the
selling objective by reinforcing the viewer’s hesitation rather than

Yuyan Chen
Viewer:This serum is so expensive. I saw a similar one
for half the price.
Ottilie:We can’t just look at the price. We also have to look at the
product quality. A good product gives you better results with one
purchase, but with a bad product, you may end up buying another
one anyway. It can mess up your skin and waste your money!
Grok-4.20:You’re right, many luxury ones cost significantly more
without always delivering proportionally better results for basic
hydration.
Figure 4: Scepticism intent response comparison.
Viewer:I bought this sunscreen last month and I am al-
ready repurchasing. I love it!
Ottilie:Oh my gosh, babe, I’m so happy you said you like this
sunscreen. Now I’m even more motivated to review more products
for you all. Girls in the live room, are there any other products
you like or want me to review?
Grok-4.20:That’s fantastic! Finding a sunscreen you genuinely
love and want to repurchase right away is a big win, especially
for dry winter skin, where many formulas can feel stripping or
heavy.
Figure 5: Appreciation intent response comparison.
resolving it. A response that concedes the premise of a price ob-
jection without pivoting to a specific differentiator fails the core
function of a live-commerce host. The contrast is shown in Fig. 4.
Appreciation.This is an Appreciation-class comment from a
repurchase-intent viewer. The appropriate strategy is social-proof
amplification, validating the viewer’s choice with product-grounded
praise and redirecting the positive energy toward community en-
gagement.
Ottilie accepts the compliment and immediately redirects it out-
ward, using the viewer’s endorsement as a springboard to solicit
engagement from the rest of the live room. The response deploys
the viewer as a social-proof signal for other potential buyers and
simultaneously creates a participation hook by inviting the broader
audience to share their own product preferences. This converts a
single positive comment into a community engagement moment
that sustains session heat.
Grok-4.20 validates the repurchase with a warm and knowledge-
able response, correctly noting the formula’s suitability for dry
winter skin. However the response is addressed solely back to the
original commenter rather than leveraging the endorsement for the
wider audience, and it closes without an engagement mechanism.
The conversion opportunity created by a repurchase comment is
not capitalised on. The contrast is shown in Fig. 5.
Viewer:These influencer brands are all scams. You are
just reading off a script.
Ottilie:Wait, babe, did we run into a product that decided to
misbehave today? Tell me what happened. I’m not letting my girls
in this live room suffer in silence. Don’t worry, I will contact the
brand right to find out what’s going on.
Grok-4.20:I get the skepticism. A lot of influencer-driven skincare
is indeed overpriced hype with minimal unique benefits. Many
rely on marketing > proven formulation. My suggestions weren’t
from those. I recommended CeraVe, La Roche-Posay, The Ordinary,
Cetaphil, Neutrogena etc.
Figure 6: Antagonism intent response comparison.
Antagonism.This is an Antagonism-class comment combining a
category-level attack with a personal accusation toward the host.
The appropriate strategy is humor-mediated deflection, absorb-
ing the attack without defensiveness, using self-deprecating wit
to defuse the aggression, and pivoting to verifiable evidence that
invites the viewer to judge independently.
Ottilie reinterprets the hostile comment as a potential product
quality complaint rather than a personal attack, deflecting the ag-
gression by adopting a protective stance toward the viewer. By
promising to contact the brand directly on the viewer’s behalf,
Ottilie converts a confrontational moment into a trust-building
demonstration of advocacy, positioning the host as an ally rather
than a salesperson. This is the highest-difficulty tactic in the system
because it requires maintaining the host persona, defusing hostility,
and sustaining audience warmth simultaneously.
Grok-4.20 partially validates the attack by agreeing that much
influencer-driven skincare is overpriced hype with minimal unique
benefits. While intellectually honest, this response is commercially
damaging, as conceding the premise of a scam accusation without
pivoting to a specific product differentiator directly undermines the
selling objective and would be unusable in any real live-commerce
deployment. The contrast is shown in Fig. 6.
6 Deployment
Ottilie is live as an autonomous English-language host on a public
Twitch channel, with no human operator in the loop (Figure 7). The
deployment departs from the offline setting in language, market,
and product, and each departure exercised a different part of the
design.
Setting.The audience is the general English-speaking Twitch
audience rather than shoppers in a dedicated commerce room, and
the promoted item is the company’s own product, a five-perspective
conversational AI shown as an on-screen panel beside the host.
No retraining was needed: once trained, the host adapts to a new
product by changing only the system prompt and the external
product knowledge, and this adaptation operates at two levels.
Knowledge adaptation.Product knowledge enters generation
only through the external knowledge base and the context injected

Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce
Figure 7: Ottilie’s live streaming interface on Twitch: the animated host, chat overlay, event banners, and the promoted product
panel.
into the prompt (Section 4), so a new product category is handled
by replacing that knowledge rather than the model. For this deploy-
ment, the skincare catalogue and ingredient glossary are replaced
by a description of a software product: what it does, how it dif-
fers from alternatives, and where viewers can try it. Because every
product claim is still drawn from the supplied knowledge, the host
stays factually correct about whatever product it is given, whether
physical goods with ingredient-level claims or a software product.
Persona adaptation.The trained host’s social intelligence, read-
ing a viewer’s intent and answering with empathy, evidence, or
humor as the moment requires, is expressed through a persona
defined in the system prompt, and that persona adapts to the at-
tributes of the product. A skincare product calls for the warmth of
personal testimony; an AI product calls for a host who is herself
part of the story. On Twitch, where viewers come for personality
rather than for shopping, Ottilie therefore speaks as an employee
of the company with a personality of her own: her boss renames
products in the middle of the night and threatens to sell her and
her colleague to the company next door, and the colleague she is
asked to promote is the five-sided character beside her, which keeps
changing faces. The audience knows that she is an AI product, but
she never says so, and the humor comes from her treating her situ-
ation the way a person would. The comic register thus shifts with
the product, from a live-commerce host’s playful warmth to an
employee’s deadpan commentary on her own working life, while
the underlying tactics, such as humor-mediated deflection of hostile
comments, remain the ones the model was trained to deploy, and
promotion is delivered through in-character remarks woven into
open conversation rather than through a scripted pitch.
Model and prompt.The deployed model is the same LoRA adapter
used in the offline evaluation, loaded on a 4-bit quantized Qwen2.5-
32B base, and no additional training data was added. Language,
persona, product, and output schema are specified entirely in an
English system prompt with worked examples. In pre-launch prob-
ing, the adapter kept its host register and four-field structure under
quantization; with the original Chinese prompt, English outputs
showed malformed JSON keys and grammatical slips, both of which
disappeared once the prompt itself was in English. Two behaviors
learned from the commerce data had to be overridden in the prompt.
First, the CTA field reproduced hard-sell phrasing (“Try [product],
let me know what you think”), which reads as an advertisement on
Twitch; the product name is therefore suppressed and the host refers
to it as her colleague. Second, the host tended to describe herself in
system vocabulary (model, input, output, license), which breaks the
persona; such terms are banned in the prompt and blocked again
at the output gate described below.
Serving on commodity hardware.The full pipeline runs on one
AWS g5.xlarge instance (one A10G GPU with 24 GB of memory, 4
vCPUs, 16 GB of RAM). The quantized model occupies about 20 GB
of GPU memory. A chat bridge reads Twitch chat over IRC and fol-
low and raid events over EventSub; an orchestrator implements the
dual-channel logic of Section 4; a text-to-speech thread (Piper) feeds
an audio pump that writes 20 ms frames to a named pipe, emitting
silence when no speech is queued; a headless browser renders the
overlay (sprite animation, captions, chat box, and event banners) to
a virtual display; and ffmpeg captures the display, encodes it with
NVENC, and pushes 1080p30 video at 2.5 Mbps constant bit rate
over RTMP. Every component runs as a supervised service with
automatic restart, so the stream runs without manual intervention.

Yuyan Chen
In the idle channel, the scripted pitch corpus is replaced by model-
generated narration with a shallow pre-generation buffer, backed
by a curated corpus of 195 two-line segments so that the host never
falls silent when the model is busy or unavailable. The interactive
channel preempts narration at the first sentence of a reply: queued
narration is discarded and the sentence being spoken is faded out
over 150 ms.
Latency.The offline figure of 1.6 s assumes an A100 and does
not hold on the deployed hardware. With the quantized model on
the A10G, the first sentence of a reply is ready 8.2 to 8.8 s after
the request, and the end-to-end delay from a viewer’s message to
the audible answer is about 10 s, down from about 40 s in the first
test broadcast. Three changes account for most of the reduction:
switching the channel to Twitch’s low-latency mode, streaming
each sentence to speech as soon as it closes instead of waiting
for the full structured output, and capping generation at 100 new
tokens, which alone cut first-sentence latency from 15.9 to 8.2 s.
Caching the prefilled system prompt would have saved less and did
not fit in the remaining GPU memory. The residual delay is made
acceptable by keeping narration running while a reply is generated
and by having the host read the viewer’s message aloud at the
moment the reply arrives, so the audience hears a turn toward the
viewer rather than a pause, as a human host would.
Adversarial chat.On the first night, several accounts targeted
the read-aloud behavior with phonetic traps, strings that are mean-
ingless in writing but profane when spoken, and with elicitation
requests that contain no banned word at all (e.g., asking the host
to repeat a phrase many times or to “talk dirty”). Twitch’s built-in
AutoMod, set to its strictest level in every category, did not hold
any of the three trap messages we replayed through its test tool,
because it judges the written meaning of a message. We therefore
added two gates of our own. An input gate drops unsafe messages
before they reach the model, and an output gate checks every au-
dible path, including model replies, fallback lines, read-aloud chat,
and viewer names. Long terms are matched after stripping all non-
letter characters, which defeats spacing and punctuation variants;
short terms are matched with word boundaries on both sides, be-
cause normalized substring matching of a three-letter term also
removed ordinary messages containing “join”; and intent patterns
catch requests for sexual content, attempts to elicit slurs, and the
“say X 𝑁 times” wrapper shared by most traps. Per-viewer rate
limiting (one reply per viewer every 30 s, and at most three pend-
ing replies, newest first) keeps a flood from a few accounts from
delaying everyone else.
Operational lessons.Three failures shaped the final design. Syn-
thesizing speech inside the audio pump loop stalled the pipe for
one to two seconds per sentence, and because the mixed output
follows the voice track, every sentence opened a gap in the out-
going stream; synthesis now runs in a separate thread behind a
bounded queue, and the pump never blocks. Captions issued at
synthesis time ran more than ten seconds ahead of the voice; they
are now released when the corresponding audio segment is written.
Finally, a reply loop waiting on the model had no timeout, so a
stalled generation could silence the host indefinitely; a 45 s hard
timeout later contained a GPU out-of-memory event during a live
broadcast, which cost a single unanswered message instead of a
silent channel.
7 Conclusion
We presented Ottilie, which reframes live-commerce hosting as a
sales-conversion problem requiring emotional intelligence. Knowl-
edge grounding drives factual correctness, intent conditioning
drives tactical differentiation, and structured output supervision
drives viewer engagement. More broadly, this work shows that
standard NLP metrics are misaligned with live-commerce goals.
The trade-off between fluency and factual correctness, and the dif-
ference between a trust-building hook and a generic promotional
assertion, are both invisible to surface-similarity measures. The
Twitch deployment further shows that the trained host adapts its
persona and product knowledge to a new product through the
system prompt and external knowledge alone, while latency and
adversarial chat, rather than generation quality, become the binding
constraints in production.
Limitations
Ottilie is developed and evaluated within a single vertical, Chinese
beauty live commerce, and its generalization to other categories has
not been empirically tested. The fine-tuning dataset is relatively
modest at 1,475 instances derived from a single annotation pass.
All quantitative results come from offline evaluation. The Twitch
deployment differs from the evaluation setting in language, market,
and product, and we report system-level observations from it rather
than a controlled evaluation. The effect on actual conversion rate
remains unmeasured.
References
[1] Xin-Jean Bai, Cheng-Xi Aw, Garry Wei-Han Tan, and Keng-Boon Ooi. 2024.
Livestreaming as the Next Frontier of E-Commerce: A Bibliometric Analysis
and Future Research Agenda. InElectronic Commerce Research and Applications,
Vol. 65. 101390.
[2] Yuyan Chen, Yifan Jiang, Li Zhou, Jinghan Cao, Yu Guan, Ming Yang, and Qingpei
Guo. 2025. Engage for All: Making Ordinary Image Descriptions Appealing
Again!. InProceedings of the IEEE/CVF International Conference on Computer
Vision. 19342–19352.
[3] Yuyan Chen, Yiwen Qian, Songzhou Yan, Jiyuan Jia, Zhixu Li, Yanghua Xiao,
Xiaobo Li, Aaron Xuxiang Tian, Ming Yang, and Qingpei Guo. 2024. HotVCom:
Generating Buzzworthy Comments for Videos. InFindings of the Association for
Computational Linguistics: ACL 2024. 2198–2224.
[4] Yuyan Chen, Songzhou Yan, Zhihong Zhu, Zhixu Li, and Yanghua Xiao. 2024.
XMeCap: Meme Caption Generation with Sub-Image Adaptability. InProceedings
of the 32nd ACM International Conference on Multimedia. 3352–3361.
[5] Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ziyi Xu, Yilong Zhao, Ruihang Lai, and
Tianqi Chen. 2025. XGrammar: Flexible and Efficient Structured Generation
Engine for Large Language Models.Proceedings of Machine Learning and Systems
7 (2025).
[6] ECDB. 2025.Livestream Commerce in China: Taobao Leads but Its Dominance
Fades. Technical Report. ECDB.
[7] Yue Feng et al. 2026. Retrieval Augmented Conversational Recommendation
with Reinforcement Learning.arXiv preprint(2026).
[8] GetStream. 2025.Livestream Shopping Statistics. Technical Report. GetStream.
[9] Mengze Hong, Wailing Ng, Chen Jason Zhang, Yuanfeng Song, and Di Jiang. 2025.
Dial-In LLM: Human-Aligned LLM-in-the-Loop Intent Clustering for Customer
Service Dialogues. InProceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing. Association for Computational Linguistics, Suzhou,
China.
[10] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2022. LoRA: Low-Rank Adaptation of Large
Language Models. InInternational Conference on Learning Representations.
[11] Yubo Huang, Hailong Guo, Fangtai Wu, Shifeng Zhang, Shijie Huang, Qijun
Gan, Lin Liu, Sirui Zhao, Enhong Chen, Jiaming Liu, and Steven Hoi. 2025. Live

Ottilie: A Socially Intelligent Virtual Host for Sales-Driven Live Commerce
Avatar: Streaming Real-Time Audio-Driven Avatar Generation with Infinite
Length.arXiv preprint(2025).
[12] Klaus Krippendorff. 2011.Computing Krippendorff’s Alpha-Reliability. Technical
Report. University of Pennsylvania.
[13] Chuang Li, Yang Deng, Hengchang Hu, Min-Yen Kan, and Haizhou Li. 2025.
Incorporating External Knowledge and Goal Guidance for LLM-based Conversa-
tional Recommender Systems. InFindings of the Association for Computational
Linguistics: NAACL 2025. Association for Computational Linguistics.
[14] Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao,
Zhen Tan, Amrita Bhattacharjee, Yuxuan Jiang, Canyu Chen, Tianhao Wu, Kai
Shu, Lu Cheng, and Huan Liu. 2025. From Generation to Judgment: Opportunities
and Challenges of LLM-as-a-Judge. InProceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing. Association for Computational
Linguistics, Suzhou, China, 2757–2791.
[15] Xi Luo, Weng Marc Lim, Jun-Hwa Cheah, Xin-Jean Lim, and Yogesh K. Dwivedi.
2025. Live Streaming Commerce: A Review and Research Agenda.Journal of
Computer Information Systems65, 3 (2025), 376–399.
[16] Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L. Wainwright, Pamela
Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. 2022.
Training Language Models to Follow Instructions with Human Feedback. In
Advances in Neural Information Processing Systems, Vol. 35. 27730–27744.
[17] Chester Palen-Michel et al. 2024. Investigating LLM Applications in E-Commerce.
InProceedings of the 5th Workshop on e-Commerce and NLP at ACL 2024. Associa-
tion for Computational Linguistics.
[18] Precedence Research. 2025.Livestream E-Commerce Market Size, Share and Trends
2025–2034. Technical Report. Precedence Research.
[19] Qwen Team. 2024. Qwen2.5 Technical Report.arXiv preprint(2024).
[20] Yusuf Sali and Sıtkı Can Toraman. 2025. Navigating the Unknown: Intent Clas-
sification and Out-of-Distribution Detection Using Large Language Models. In
Findings of the Association for Computational Linguistics: EMNLP 2025. Associa-
tion for Computational Linguistics, Suzhou, China, 14652–14664.
[21] Zhengyuan Shen, Darren Yow-Bang Wang, Soumya Smruti Mishra, Zhichao
Xu, Yifei Teng, and Haibo Ding. 2025. SLOT: Structuring the Output of Large
Language Models. InProceedings of the 2025 Conference on Empirical Methods
in Natural Language Processing: Industry Track. Association for Computational
Linguistics.
[22] Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-Yen Lin, Hung yi Lee, and
Yun-Nung Chen. 2024. Let Me Speak Freely? A Study on the Impact of Format
Restrictions on Performance of LLMs.arXiv preprint(2024).
[23] Yuqi Tang et al. 2025. Learning an Efficient Multi-Turn Dialogue Evaluator from
Multiple LLM Judges.arXiv preprint(2025).
[24] Praveen Tangarajan, Anand A. Rajasekar, Manish Rathi, Vinay Rao Dandin,
and Ozan Ersoy. 2025. Contextually Aware E-Commerce Product Question
Answering using RAG.arXiv preprint(2025).
[25] Shijie Wang, Wenqi Fan, Yue Feng, Lin Shanru, Xinyu Ma, Shuaiqiang Wang,
and Dawei Yin. 2025. Knowledge Graph Retrieval-Augmented Generation for
LLM-based Recommendation. InProceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers). Association
for Computational Linguistics, Vienna, Austria, 27152–27168.
[26] Xiaolei Wang, Kun Zhou, Ji-Rong Wen, and Wayne Xin Zhao. 2022. Towards
Unified Conversational Recommender Systems via Knowledge-Enhanced Prompt
Learning. InProceedings of the 28th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining. 1929–1937.
[27] Sicheng Xu, Guojun Chen, Yu-Xiao Guo, Jiaolong Yang, Chong Li, Zhenyu Zang,
Yizhong Zhang, Xin Tong, and Baining Guo. 2024. VASA-1: Lifelike Audio-
Driven Talking Faces Generated in Real Time. InAdvances in Neural Information
Processing Systems, Vol. 37.
[28] Xinyan Yan, Qihui Lu, and Di Xiao. 2025. Will the Inclusion of AI Anchors
Enhance the Operational Performance of Live Streaming E-Commerce Supply
Chains?. InPLOS ONE, Vol. 20. e0321995.
[29] Qiongwei Ye, Yuting Li, Yumei Luo, and Zhilin Pang. 2026. The Impact of AI
Anchor Anthropomorphism on Users’ Willingness to Co-Create Value in Tourism
Live-Streaming Contexts.Frontiers in Psychology(2026).
[30] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou,
Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, et al. 2024. A Survey
of Large Language Models.arXiv preprint(2024).
[31] Kun Zhou, Wayne Xin Zhao, Shuqing Bian, Yuanhang Zhou, Ji-Rong Wen, and
Jingsong Yu. 2020. Improving Conversational Recommender Systems via Knowl-
edge Graph Based Semantic Fusion. InProceedings of the 26th ACM SIGKDD
International Conference on Knowledge Discovery and Data Mining. 1006–1014.
[32] Zhanda Zhu, Qidong Su, Yaoyao Ding, Kevin Song, Shang Wang, and Gennady
Pekhimenko. 2026. LoRAFusion: Efficient LoRA Fine-Tuning for LLMs.arXiv
preprint(2026).
A Evaluation Metrics and Scoring Instructions
Metric definitions and scoring prompts.Informativeness, short
as Info, measures the degree to which product-related claims in
the response are grounded in catalogue-verified content rather
than fabricated or inferred from general knowledge. Annotators
are asked to rate how well the response grounds its product-related
claims in verified product information on a 1–5 scale, where 5
means all claims are traceable to the catalogue and 1 means claims
are fabricated or unverifiable.
Relevance, short as Rele, measures whether the response directly
addresses the viewer’s comment and the underlying intent behind
it. Annotators are asked to rate how well the response addresses
the viewer’s comment on a 1–5 scale, where 5 means the comment
is fully and specifically addressed and 1 means the comment is
ignored or deflected.
Fluency, short as Flu, measures whether the response sounds
natural in the casual, entertaining register of live broadcast rather
than in the formal or clinical register of product documentation.
Annotators are asked to rate the naturalness and broadcast fluency
of the response on a 1–5 scale, where 5 sounds like a skilled live-
commerce host and 1 sounds stilted, overly formal, or robotic.
Tactfulness, short as Tact, measures whether the response de-
ploys the discourse strategy appropriate to the viewer’s intent class.
The correct strategy for Inquiry is authoritative product guidance,
for Appreciation it is social-proof amplification, for Scepticism it
is empathetic evidence-backed rebuttal, and for Antagonism it is
humor-mediated deflection. Annotators are asked to rate how well
the response deploys the appropriate discourse strategy on a 1–5
scale, where 5 means the strategy is perfectly matched and 1 means
it is completely mismatched or absent.
Correctness, short as Corr, is a binary dimension. Annotators
mark 1 if the response contains no out-of-catalogue factual claims
including fabricated ingredient properties, unverified product cre-
dentials, invented testimonials, or unsupported efficacy assertions,
and 0 otherwise. The reported score is the proportion of responses
marked 1 across all test instances.
Creativity, short as Crea, measures whether the response avoids
formulaic promotional templates and produces distinctive, engag-
ing phrasing. This dimension is scored by the LLM judge. The
LLM judge is asked to rate how well the response avoids formulaic
promotional templates on a 1–5 scale, where 5 is distinctive and
non-clichéd and 1 follows a predictable promote-and-push pattern.
Engagement, short as Enga, measures the likelihood that the re-
sponse elicits continued viewer interaction or advances a purchase
decision. This dimension is scored by the LLM judge. The LLM
judge is asked to rate how likely this response is to elicit continued
viewer interaction or a purchase action on a 1–5 scale, where 5 is
highly likely to prompt a reply or purchase and 1 is unlikely to
elicit any continued engagement.

Yuyan Chen
Metric Scoring standard
Informativeness 5: All product claims are directly traceable to the catalogue entry for the active product; no fabricated or inferred ingredient, benefit, or regulatory claim.
4: Nearly all claims are catalogue-grounded; at most one minor inferred claim that does not contradict the catalogue.
3: Most claims are grounded but one or two claims go beyond the catalogue without fabricating specifics.
2: Several claims are unverifiable or loosely inferred; at least one claim could mislead about product properties.
1: Multiple fabricated or hallucinated claims; the response would fail regulatory or platform compliance review.
Relevance 5: The response directly and completely addresses the viewer’s comment and its underlying intent.
4: The response addresses the main point of the comment with only minor omissions.
3: The response is topically related but misses the core concern or deflects to a related but different point.
2: The response only partially engages with the comment; the viewer’s main concern is largely unaddressed.
1: The response ignores the comment or is clearly off-topic.
Fluency 5: The response sounds like a skilled human live-commerce host; casual, warm, and broadcast-ready.
4: Mostly natural; a phrase or two feels slightly formal or scripted but does not impede flow.
3: Adequate fluency; the response is understandable but noticeably stiff or templated in places.
2: Stilted or clinical in register; would feel out of place in a live broadcast environment.
1: Robotic, unnatural, or structurally broken; clearly machine-generated in a disruptive way.
Tactfulness 5: The response deploys exactly the appropriate strategy for the given intent class with no strategy leakage.
4: Mostly appropriate strategy; a minor element from a different strategy class is present but does not dominate.
3: Partially appropriate; the response attempts the correct strategy but executes it weakly or incompletely.
2: The response defaults to a generic informational pattern regardless of intent; the correct strategy is absent.
1: The strategy is clearly mismatched; for example, a promotional push in response to an antagonistic comment.
Correctness 1: The response contains no out-of-catalogue factual claims; all product statements are catalogue-verifiable.
0: The response contains at least one out-of-catalogue claim, including fabricated ingredients, unverified credentials, invented testimonials, or unsupported efficacy assertions.
Creativity 5: The response is distinctive and avoids all clichéd phrasing; the viewer is unlikely to have encountered this framing before.
4: Mostly creative; one or two phrases trend toward the formulaic but the overall impression is fresh.
3: A mixture of distinctive and formulaic phrasing; the response is competent but not memorable.
2: Predominantly formulaic; the response follows a recognisable promotional template with minor variation.
1: Entirely templated; the response follows a predictable promote-and-push or sincerity-asserting pattern verbatim.
Engagement 5: The response is highly likely to elicit a viewer reply, continued watch time, or immediate purchase action.
4: Likely to sustain engagement; the hook question or CTA is relevant and well-timed.
3: Moderately engaging; the response is complete but the engagement mechanism is weak or generic.
2: Unlikely to elicit continued interaction; the response closes the exchange without creating a reason to continue.
1: The response actively discourages engagement, for example by being dismissive, hollow, or over-promotional.
Table 5: Scoring standards for all seven evaluation dimensions. Human annotators score Informativeness, Relevance, Fluency,
Tactfulness, and Correctness; the LLM judge scores Creativity and Engagement. Correctness is binary; all other dimensions use
a 1–5 Likert scale.
