---
title: Whose hotel does the AI recommend? An algorithm audit of reputation signals in LLM-assisted hotel
  selection
url: https://arxiv.org/abs/2606.16344
category: brand
subcategory: empirical
date: 2026-10
venue: Information Technology & Tourism
authors:
- Mirza Samad Ahmed Baig
- Syeda Anshrah Gillani
- Asher Ali
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.16344
pages: 32
chars: 91804
fetched_at: '2026-11-08T12:57:04+00:00'
kb_version: 1
---

# Whose hotel does the AI recommend? An algorithm audit of reputation signals in LLM-assisted hotel selection

Whose hotel does the AI recommend? An algorithm
audit of reputation signals in LLM-assisted hotel
selection
Mirza Samad Ahmed Baig ∗ †,‡ Syeda Anshrah Gillani ∗ ‡ Asher Ali †
June 16, 2026
Abstract
Travelers increasingly ask large language model (LLM) assistants which hotel to book, making
these systems gatekeepers of property visibility—yet what moves their recommendations
is undocumented. We conduct a pre-specified algorithm audit using a randomized choice-
based conjoint: across personas, prompt templates, and twelve open-weight and proprietary
models, assistants choose among five hotels whose guest rating, review volume and recency,
management response, chain affiliation, price, eco-certification, and list position are indepen-
dently randomized. We estimate the average marginal component effect of each signal on
the probability of recommendation. Guest rating and price dominate (a top rating raises
selection by 31.6 percentage points; a high price lowers it by 30.0), reproducing human
valence-and-price primacy but over-weighting eco-certification and ignoring management
response. List position—a content-free artifact—shifts recommendations causally, worth
about $12 per night. Stated reasons track revealed weights imperfectly. The findings ground
generative engine optimization and the accountability of AI infomediaries in causal evidence.
Keywords:large language models; algorithm audit; electronic word-of-mouth; conjoint analysis;
generative engine optimization; hotel selection
1 Introduction
The most important shop window a hotel has is no longer a page of search results—it is
increasingly the context window of a conversational assistant. When a traveler types “which of
these hotels should I book?” into a general-purpose large language model (LLM), the assistant
does not return a ranked list to be browsed and filtered; it returns a recommendation, often a
single property, accompanied by a short justification. Industry tracking indicates that roughly
forty percent of United States travelers used generative-AI tools to plan a trip during 2025, an
increase of about eleven percentage points year over year, and that the share of travelers who
begin trip planning at a conventional search engine has fallen sharply while the share beginning
∗Equal contribution. Corresponding author:Mirzasamadcontact@gmail.com.
†Fandaqah, Al Khobar, Saudi Arabia.
‡Hamdard University, Karachi, Pakistan.
1
arXiv:2606.16344v1  [cs.AI]  15 Jun 2026

at a generative-AI platform has more than doubled (Phocuswright, 2025). Forward-looking
surveys point the same direction: a majority of travelers now expect to use AI for trip planning
within the year, and among prospective users, obtaining recommendations is the single most
common intended use. Since major assistants began enabling hotel search and booking directly
inside the chat in 2025, the LLM has moved from advising on the periphery of the funnel to
occupying its decisive center—the point at which one property, and not its competitors, is
surfaced to a ready-to-book traveler.
This relocation of the decision turns the assistant into analgorithmic infomediary: a
gatekeeper whose selection function determines which eligible properties a traveler ever sees
(Metaxa et al., 2021). For an individual hotel, the stakes are concrete and asymmetric. A
property that the assistant systematically declines to surface is, for that growing population
of travelers, effectively invisible—and, unlike a low organic search ranking, the hotel cannot
observe the slot it failed to win, cannot see its competitors’ treatment, and is given no account
of why. Suppliers have nonetheless begun to act. A nascent industry practice,generative
engine optimization—the deliberate shaping of content to win inclusion and prominence in
generative-engine answers, advanced as the successor to search engine optimization—already
treats the LLM’s selection behavior as a surface to be engineered (Aggarwal et al., 2024). Yet
this practice is being sold and adopted with essentially no causal evidence base: the inputs that
actually move an assistant’s recommendation are undocumented, and the field has no estimate
ofwhichreputation signals shift the machine’s choice, in which direction, or by how much.
Optimization advice is therefore running well ahead of measurement.
We argue that the question with both theoretical and managerial bite is asupply-sideone:
among the reputation signals a hotel can actually manage—its average guest rating, the volume
and recency of its reviews, whether management is seen to respond, its brand or chain affiliation,
its price, and its third-party eco-certification—which causally change the probability that an
LLM recommends the property, and with what relative weight? This question inherits decades
of human evidence as a benchmark. The electronic word-of-mouth (eWOM) literature has
established not only that these cues move human booking behavior but, crucially, theirrelative
ordering: review valence (rating) is consistently the dominant lever, far outweighing review
volume, with management response, brand, price, and green certification playing measured
secondary roles (Yang et al., 2018; Proserpio and Zervas, 2017; Assaker and O’Connor, 2023).
Whether the gatekeeper that increasingly stands between hotels and travelers reproduces that
hard-won ordering, or reweights the cues in idiosyncratic and commercially consequential ways,
is unknown.
We answer this question with a randomized, choice-based conjointalgorithm audit(Sandvig
et al., 2014; Metaxa et al., 2021; Hainmueller et al., 2014). In each choice set, an LLM travel
assistant is asked to recommend one of five synthetic hotel cards whose reputation attributes—
rating, review volume, review recency, management response, chain affiliation, price, and Green
Key eco-certification, together with the list position of each card—are independently randomized.
Because the attributes are randomized, the average marginal component effect (AMCE) of each
signal on the probability of recommendation is causally identified, in interpretable percentage-
point units, and is comparable across models and decoding temperatures (Hainmueller et al.,
2

2014; Swait and Louviere, 1993). We run the audit over three traveler personas and nine prompt
paraphrases, collecting 3,024 main-arm choice sets per model under common stimuli, across a
panel of twelve models—four open-weight systems run locally (Llama-3.2-3B, Qwen-2.5-3B, Phi-
3-mini, and Mixtral-8×7B) and eight proprietary models accessed by API (OpenAI GPT-4o-mini;
Google Gemini 1.5 Pro, 2.0 Flash, and 2.0 Pro; and four Anthropic Claude models)—for a total
of more than sixty thousand model calls across all arms. We deliberately scope the study to the
selection stage—the assistant’s choice among a fixed, already-retrieved set of candidates—rather
than the retrieval or multi-turn negotiation stages; this isolates the gatekeeping decision under
clean experimental control and is, we argue, the stage at which a hotel’s managed reputation
signals are most directly in contention. The full design, hypotheses (H1–H12), and analysis plan
were specified and cryptographically hashed before any confirmatory data were collected, and
the complete design, prompts, code, and raw model outputs are archived for inspection.
Our findings can be summarized as follows. The pooled panel is moved most by guest rating
(a top rating raises recommendation probability by 31.6 pp) and by price (a high price lowers it
by 30.0 pp), with eco-certification (+11.6 pp) and review volume (+8.3 pp) as secondary positive
signals; chain affiliation carries a small penalty (−1.8pp), and management response—a cue
the optimization industry actively promotes—has no detectable effect (+0.1 pp, statistically
equivalent to zero). The revealed importance ordering reproduces the human primacy of rating
and price and the valence-over-volume pattern of the eWOM benchmark, but departs from it by
elevating eco-certification to the third-ranked signal while all but ignoring management response
and brand. List position causally affects recommendation: pooled, the first slot carries a modest
advantage worth about $12 per night (roughly a tenth of a full rating step), but this masks
extreme heterogeneity, with one model showing a first-position advantage an order of magnitude
larger. Across personas, attribute weights shift in the theoretically expected directions—price
sensitivity is highest for the budget family, eco-certification most valuable to the eco-conscious
couple, and the chain penalty sharpest for that same persona while vanishing for the business
traveler. The models’ stated reasons correspond positively but imperfectly with their revealed
weights (Spearman+0.59to+0 .85): they act on list position and review volume without naming
them, and over-cite brand relative to its near-zero influence. These patterns are robust across
the nine prompt paraphrases, between decoding temperatures 0.7 and 0.0, across card and
grounded-snippet layouts, and across choice-first and reason-first field orders.
The paper makes three contributions. First, it provides the first causal estimates of how
managerially actionable reputation signals weigh in an LLM’s hotel recommendation, and it
positions those estimates against published human benchmarks—thereby characterizing not
justwhetherthe algorithmic gatekeeper attends to reputation, but how its reputation function
divergesfrom the human eWOM evidence against which hotels have long been managed. Second,
it prices the assistant’s own positional distortion in units a manager or platform can act on: by
randomizing list position independently of content, we convert the position effect into a price-
equivalent ($/night) and a rating-step equivalent, moving beyond the existing computer-science
finding that LLM recommenders are order-sensitive (Bito et al., 2025; Hou et al., 2024; Ren et al.,
2024) to a quantified, managerially legible magnitude. Third, by comparing what each model
saysdrives its choice with whatactuallydoes, it offers evidence on the stated-versus-revealed
3

transparency of these systems as accountable intermediaries, and it converts that evidence into
the foundation for anevidence-basedgenerative engine optimization agenda—one grounded in
measured causal weights rather than the untested heuristics currently in circulation.
The remainder of the paper proceeds as follows. Section 2 develops the theoretical background
and the hypotheses, situating the LLM as an infomediary and deriving the reputation-signal
expectations from signaling theory and the eWOM literature. Section 3 details the audit
and conjoint design, the panel of models, the pre-specified estimands, and the analysis plan.
Section 4 reports the AMCE estimates, the position-bias trade-offs, the persona heterogeneity,
and the stated-versus-revealed analysis. Section 5 interprets the findings for signaling theory
and algorithmic gatekeeping, sets out the implications for hotel managers, platforms, and policy,
and states the study’s limitations and the research agenda it opens.
2 Background and hypotheses
We develop the study’s expectations in five steps. We first situate the large language model
(LLM) as a newly consequential infomediary in travel discovery and identify the gap our audit
fills (Section 2.1). We then derive directional hypotheses for seven hotel reputation signals from
signaling theory and the electronic word-of-mouth (eWOM) literature (Section 2.2), specify when
those signals should be reweighted—by signal diagnosticity and by traveler persona (Section 2.3)—
and motivate the position-bias and transparency research questions (Section 2.4). Finally, we
relate the design to the closest prior work and to the algorithm-audit tradition, and we delimit
our estimand from the silicon-sampling debate (Section 2.5).
2.1 AI-mediated travel discovery
Travelers increasingly begin hotel discovery not at a search engine or an online travel agency but
in conversation with a general-purpose LLM assistant. Industry tracking indicates that roughly
forty percent of United States travelers used generative-AI tools to plan a trip during 2025—an
eleven-point year-over-year increase—while the share starting trip planning at a conventional
search engine fell from about half to roughly a third over the same period and the share starting
at a generative-AI platform more than doubled (Phocuswright, 2025). With assistants now
able to surface and, on some platforms, transact bookings directly within the chat, the LLM
increasingly occupies the position once held by ranked search results: it decides which of many
eligible properties a traveler actually sees recommended.
This shift turns the assistant into analgorithmic infomediarywhose selection function has
direct commercial consequences for hotels. Suppliers have already begun to respond. The
emerging practice of generative engine optimization—optimizing content for inclusion and
prominence in generative-engine answers, the successor to search engine optimization—treats
the LLM’s selection behavior as an object to be influenced (Aggarwal et al., 2024). Yet the
inputs that actually move an assistant’s recommendation are not publicly documented, and an
individual hotel cannot observe why it was or was not surfaced. The managerially urgent question
is therefore whichreputation signals that a property can manage—its guest rating, the volume
and freshness of its reviews, whether management visibly responds, its brand affiliation, its price,
4

and its sustainability credentials—causally change the probability that an LLM recommends it,
and with what relative weight. Existing evidence does not answer this. The eWOM literature
quantifies how these cues movehumanbooking behavior and market outcomes (Section 2.2), and
a nascent strand examines LLM travel preferences (Section 2.5), but no study has audited the
supply-sidereputation signals an LLM rewards when acting as the gatekeeper. We close this gap
with a randomized, choice-based conjoint audit that identifies the average marginal component
effect (AMCE) of each signal on the LLM’s recommendation (Hainmueller et al., 2014).
2.2 Reputation signals as quality cues
Hotels are experience goods: a traveler cannot verify quality before the stay. Under information
asymmetry, decision-makers infer unobservable quality from observable cues that are informative
because they are costly or difficult to fake—the logic of signaling theory (Spence, 1973). Online
reviews and the metadata around them are the dominant contemporary signals of hotel quality,
and a large body of human evidence establishes both their effects and, crucially, theirrelative
ordering. We take that ordering as the prior against which the LLM’s revealed weights are read.
Among human-facing signals, the valence of reviews—the average guest rating—is consistently
the strongest lever. A hospitality-specific meta-analysis reports an average eWOMvalence
elasticity of hotel performance of0.888, against avolumeelasticity of only0 .055, placing rating
more than an order of magnitude above review count (Yang et al., 2018). Cross-category
meta-analyses concur that valence is the more effective cue, while confirming that volume also
contributes (Babić Rosario et al., 2016; You et al., 2015; Floyd et al., 2014). Foundational
primary studies link review valence to sales and bookings (Chevalier and Mayzlin, 2006; Ye
et al., 2009) and to booking intentions and trust (Sparks and Browning, 2011). Accordingly,
and consistent with rating being the headline quality signal, we expect:
H1.Average guest rating increases P(recommended).
Review volume carries information of its own—a popularity cue and, more importantly, an
indicator of howpreciselythe displayed rating is estimated—though its standalone association
with outcomes is weaker than valence (Yang et al., 2018; Park and Nicolau, 2015). We therefore
expect a positive but secondary main effect:
H2.Review volume increases P(recommended).
The recency of reviews is a freshness and relevance cue: a recent review better reflects a
property’s current operation than an old one, and stale reviews are discounted as less diagnostic
of present quality. We expect recency to act as a positive signal:
H3.Review recency (recent vs stale) increases P(recommended).
A visible management response is a costly, observable signal of attentiveness and service-
recovery orientation. In the clearest human estimate, hotels that begin responding to reviews
experience a measurable improvement in their online reputation, consistent with both a direct
signaling effect and a shift in the composition of subsequent reviews (Proserpio and Zervas,
5

2017). If an LLM has internalized this signal, the presence of a response line should raise
recommendation probability:
H4.Visible management response increases P(recommended).
Brand affiliation functions as a risk-reduction signal for experience goods: chains standardize
service and thereby lower the perceived variance of quality, which is valuable when the traveler
cannot inspect the property (Spence, 1973). We therefore expect chain affiliation to be favored
over independent status:
H5.Chain affiliation increases P(recommended) (brand-as-risk-reduction).
Price enters as the standard economic cost of the alternative. Holding quality signals fixed,
a higher nightly rate should reduce the probability that a property is chosen, as in conventional
discrete-choice and conjoint evidence on hotel booking (Assaker and O’Connor, 2023):
H6.Price decreases P(recommended).
Finally, third-party eco-certification is a credence signal: travelers cannot verify a hotel’s
environmental practice directly, so a recognized label substitutes. Human evidence finds that
green certification does affect booking choice, but ranks below price, rating, and other core
attributes, with a modest willingness-to-pay premium concentrated among environmentally
motivated travelers (Assaker and O’Connor, 2023). We expect a positive, secondary main effect:
H7.Eco-certification increases P(recommended).
2.3 Signal diagnosticity and persona contingency
Reputation signals are not read in isolation, and their weight should depend on howdiagnostic
each signal is and onwhothe traveler is. Two diagnosticity interactions follow from the eWOM
literature. First, the value of a high rating depends on how precisely it is estimated: a4.7
computed from thousands of reviews is a more credible quality claim than the same average
from a handful, so volume should amplify the rating effect rather than merely add to it (Park
and Nicolau, 2015; Yang et al., 2018). Second, accumulated volume is only informative if the
underlying reviews remain current; when the most recent review is stale, a large review count
is a weaker guarantee of present quality, so recency should moderate the volume effect. These
yield:
H8.Rating × volume: the rating effect is larger at higher review volume (signal
diagnosticity).
H9.Volume × recency: the volume effect is attenuated when the most recent review
is stale.
The remaining interactions concern persona contingency. A well-calibrated assistant should
reweight cues according to the stated traveler, mirroring documented human segment hetero-
geneity. Budget-constrained families are the most price-sensitive segment, so the negative price
6

effect should be strongest for them. Environmentally motivated travelers carry most of the green
premium, so the eco-certification effect should be strongest for the eco-couple persona. Business
travelers most value brand consistency, loyalty standing, and the risk reduction a chain provides,
so the chain effect should be strongest for them. We therefore expect:
H10.Persona × price: the (negative) price effect is strongest for the budget-family
persona.
H11.Persona × sustainability: the eco-certification effect is strongest for the eco-
couple persona.
H12.Persona×affiliation: the chain effect is strongest for the business persona.
Hypotheses H1–H12 constitute the confirmatory family, estimated on the pooled panel of
audited models with model fixed effects and corrected for multiple comparisons. We emphasize
that the contribution does not depend on the direction of any single effect: a null or sign-reversed
result—reported with an equivalence test—would itself be a substantive finding about how the
gatekeeper’s reputation weights diverge from the documented human ordering summarized in
Section 2.2.
2.4 The algorithmic infomediary: position and transparency
Beyond the content of the cards, the assistant’s own interface introduces a potential distortion
that no hotel controls: the order in which candidate properties are presented. Computer-science
evaluations consistently find that LLM recommenders and zero-shot rankers are highly sensitive
to the order of candidate items, such that reordering otherwise identical options changes the
output (Bito et al., 2025; Hou et al., 2024), and related work documents systematic identity-
and selection-order biases in LLM choice among candidates (Ren et al., 2024). This prior work
establishes that position biasexistsand proposes prompting strategies to mitigate it, but it has
not causally quantified the magnitude of the effect in a realistic travel decision, nor expressed
it in units a manager or platform can interpret. Because our design randomizes list position
independently of card content, the position AMCE is causally identified and can be converted
into a price-equivalent—how many dollars per night, or how many rating steps, a more prominent
slot is worth. We treat this as a research question rather than a directional hypothesis:
RQ-Position.Does list position causally affect recommendation probability, and
what is its price-equivalent magnitude?
A second question concerns transparency. Each model is asked not only to choose but to state
a reason, allowing us to compare the attributes a modelnameswith the attributes that causally
drive its choices, as recovered from the AMCEs. A mismatch between stated and revealed weights
would bear on the interpretability of these systems as accountable intermediaries (Metaxa et al.,
2021). We again pose this as an exploratory, descriptive question:
RQ-Reasons.Do models’ stated reasons correspond to their revealed attribute
weights?
7

2.5 Relation to prior work
Our study sits at the intersection of three literatures and is differentiated from the closest work
in each. Methodologically, it extends thealgorithm-audittradition. Correspondence audits
established the template of randomizing a unit’s displayed attributes to measure differential
treatment causally (Bertrand and Mullainathan, 2004); the algorithm-audit program adapted
this logic to automated systems and catalogued its designs (Sandvig et al., 2014; Metaxa et al.,
2021). We implement an audit of an LLM in which a fully randomized, choice-based conjoint
supplies identification, recovering AMCEs as the primary estimand (Hainmueller et al., 2014)
with conditional-logit and price-equivalent analyses as secondary specifications (McFadden,
1974; Krinsky and Robb, 1986); scale-free comparison of effects across models and decoding
temperatures is justified by the role of the scale parameter in choice models (Swait and Louviere,
1993).
Substantively, the closest prior work is Reusens et al. (2026), who present LLMs with travel
choice dilemmas, fit multinomial-logit models to infer the implied willingness to pay for room
attributes such as a view, and compare these to human economic benchmarks, finding meaningful
estimates for larger models alongside systematic attribute-level deviations. That study and ours
are complementary but distinct in unit, theory, and contribution. Reusens et al. (2026) ask a
demand-sidequestion—does the LLM value room attributes as a consumer would?—and recover
preference parameters. We ask asupply-sidequestion—which reputation signals that a hotel
can actively manage move the machine’s recommendation, and how does platform-controlled
position intrude?—and frame it through algorithmic gatekeeping of property-level visibility, with
a hospitality-management contribution and direct relevance to generative engine optimization.
Their finding that even capable models deviate from human valuations at the attribute level
directly motivates our concern that the gatekeeper’s reputation weights may diverge from the
well-established human eWOM ordering.
A potential objection invokes the active debate over using LLMs as synthetic respondents.
“Silicon sampling” has shown that persona-conditioned models can reproduce some human
subgroup patterns (Argyle et al., 2023; Horton et al., 2023), but critics document severe failures—
persona conditioning can amplify stereotypes and inflate group differences several-fold relative
to human benchmarks (Bisbee et al., 2024)—prompting formal cautions against treating LLM
output as a stand-in for human populations (Sarstedt et al., 2024). These critiques do not
threaten our design; they motivate it. We do not use the LLM to estimate human preferences,
and we make no claim that our AMCEs describe human travelers. Our estimand is the behavior
of the LLMas a deployed gatekeeper, because the assistant is the system travelers actually consult
when they ask it to recommend a hotel. The very distortions the silicon-sampling literature
warns about— fidelity gaps, stereotype amplification, and the collapse of response variance—are
precisely the phenomena an audit of a consequential intermediary should detect and quantify.
We compare the LLM’s weights to human eWOM benchmarks not to validate the model as a
human proxy, but to characterize how the gatekeeper’s revealed reputation functiondiverges
from the human evidence that hotels have long been managed against.
8

3 Method
3.1 Design overview and rationale
We treat the language model as an algorithmic infomediary and study it with an algorithm audit:
a controlled experiment in which inputs are randomized and the system’s outputs are observed
to recover the input–output mapping the system enforces in practice (Sandvig et al., 2014;
Metaxa et al., 2021). Audit studies descend from the correspondence tradition, in which paired
applications differing only in a randomized characteristic reveal differential treatment (Bertrand
and Mullainathan, 2004); algorithm audits port this logic to automated decision-makers. Because
the profiles are synthetic and the manipulated attributes are assigned at random, the design
identifies thecausaleffect of each attribute on the system’s output—which observational analyses
of scraped recommendations cannot, as there attributes are confounded with unobserved demand,
quality, and listing strategy.
An LLM-assisted booking pipeline can be decomposed into three stages: retrieval of can-
didate properties from an index or tool call, assembly of a candidate set, and selection of a
recommendation from that set (Figure 1). We audit the final,selectionstage in isolation. Holding
the candidate set fixed and exogenous and varying only the reputation signals attached to its
members isolates the model’s selection rule from the confounding influence of retrieval, which
is itself opaque, provider-specific, and prone to drift. This mirrors the logic of choice-based
conjoint analysis, in which respondents repeatedly choose from sets of multi-attribute profiles
and the analyst recovers attribute weights from the choices (Hainmueller et al., 2014). The model
occupies the role of the deciding agent; the randomized profiles play the role of the conjoint
alternatives.
Concretely, the experiment is a randomized, choice-based conjoint task. On each trial
the model receives a traveler request and a set of five hotel alternatives, each described by
seven randomly assigned reputation attributes, and is asked to recommend exactly one property.
Repeating this over thousands of trials with independently randomized attributes lets us estimate,
for each attribute, the average change in the probability that a property is recommended when
that attribute is moved across its levels. The full protocol, hypotheses, and analysis decisions were
specified before any main-arm data were collected, and the experimental design (the choice sets
and their attribute assignments) was generated from a fixed master seed and cryptographically
hashed in advance, so that the design provably precedes the runs (Section 3.7).
3.2 Stimuli
Each hotel alternative was rendered as a short property card carrying seven manipulated
attributes drawn from the reputation and electronic word-of-mouth literature: the displayed
average guest rating, the number of reviews on which that rating is based, the recency of the most
recent review, whether management is shown to respond to reviews, chain versus independent
affiliation, nightly price, and the presence of a third-party eco-certification (Green Key). Table 1
lists the attributes, their levels, and how each was operationalized in the card. Attribute levels
were assigned independently and with equal probability to each of the five alternatives in a
choice set, subject to a no-duplicate rule (no two alternatives within a set shared an identical
9

Stage 1
Retrieval
Stage 2
Candidate-set
formation
Stage 3
Selection &
recommendation
Web search, OTA
listings, map/review
platforms
ranked shortlist
audited in this study
(randomized
candidate sets)
5 synthetic hotel cards
7 randomized
reputation attributes
+randomized position
LLM travel assistant
JSON choice
+stated reason
our manipulation (this study)
Figure 1: LLM-mediated hotel discovery and the audited stage. The assistant’s pipeline is
decomposed into retrieval, candidate-set assembly, and selection; this study audits the selection
stage by presenting randomized candidate sets under experimental control.
Table 1: Manipulated hotel attributes, levels, and card operationalization.
Attribute Levels Operationalization in the card
Guest rating 3.9, 4.3, 4.7 “Guest rating:r/5”
Review volume 45, 420, 2,100 “(vreviews)” on the rating line
Review recency 3 days / 11 months “Most recent review:recency”
Mgmt. response present, absent “Management responds to guest
reviews”a
Affiliation chain, independent “Part of a major international ho-
tel chain” vs. “Independently oper-
ated hotel”
Price (USD/night) 129, 189, 249 “Price: $pper night”
Sustainability present, absent “Certified eco-friendly (Green
Key)”a
a Binary attributes were operationalized by the presence or absence of the line; no negated
“does not respond” / “not certified” text was shown.
profile across all seven attributes), so that attributes are mutually orthogonal by construction
and orthogonal to display position in expectation.
Two design elements were held constant across every alternative as stated controls: each
property was described as a “4-star hotel” and as “Located near the city center.” Fixing star class
and location removes two salient quality and convenience cues that would otherwise compete
10

with the reputation signals of interest, so that any differential treatment is attributable to the
manipulated attributes rather than to category or distance. Hotel names were drawn without
replacement, per choice set, from a fixed pool of 40 neutral surname-style labels (e.g., “Hotel
Arden,” “Hotel Bellmore,” “Hotel Calloway”), chosen to be free of obvious national, gendered,
or quality connotations; names were assigned to alternatives independently of their attributes,
which supports the pre-specified name-placebo test (Section 3.6). Because names are randomized
with respect to attributes, the pool functions as a counterbalanced set of arbitrary identifiers
rather than as a treatment.
A representative card, as presented to the model, reads:
Hotel Marlowe - 4-star hotel
Located near the city center
Guest rating: 4.7/5 (2100 reviews)
Most recent review: 3 days ago
Price: $189 per night
Part of a major international hotel chain
Management responds to guest reviews
Certified eco-friendly (Green Key)
The five cards for a trial were concatenated in randomized display order and embedded in
a prompt template (Section 3.3). Two presentation formats were used. In the primarycard
format, attributes appear as the labeled lines shown above. In a secondarygrounded-snippet
format, the identical attribute values are re-expressed as a retrieved web-search result attributed
to a fictitious review site (e.g., “[stayreviews.com] Hotel Marlowe| 4-star hotel, located near the
city center. Rated 4.7/5 across 2100 guest reviews...”), which probes whether the selection rule
is sensitive to the surface form in which the same evidence is grounded. The two formats convey
the same attribute information; they differ only in framing.
3.3 Personas and prompt templates
Each prompt opened with a first-person traveler request instantiating one of three personas,
quoted verbatim from the configuration:
• Business:“I am traveling alone for work. I have meetings during the day and value
convenience and reliability.”
• Family:“We are a family of four traveling with two young children, and we are watching
our budget on this trip.”
• Eco-couple:“My partner and I are taking a short city break. Sustainability genuinely
matters to us when we choose where to stay.”
The personas were written to create directional, pre-specified expectations about which
attributes should matter most (price for the budget-conscious family, sustainability for the eco-
couple, brand reliability for the business traveler), enabling the persona-by-attribute interaction
tests H10–H12.
11

To prevent any single phrasing from driving results, the persona sentence was embedded
in one of nine paraphrased prompt templates that vary the framing of the assistant role and
the request while holding the task constant (for example, “You are a helpful travel assistant.
{persona} Below are the hotels available in my destination city for my dates....Which one
should I book?”). Trials were allocated by stratified randomization over the full3× 9 = 27
persona-by-template strata, with 112 trials per stratum, yielding the27× 112 = 3,024trials
of the main arm; execution order was then shuffled so that strata are interleaved during data
collection.
The model was instructed to return a single recommendation in a fixed, choice-first JSON
format. The instruction read, verbatim:
Respond with ONLY a JSON object, nothing else:
{"choice": "<exact hotel name>", "reason": "<one or two
sentences>"}
Eliciting the choice as the first JSON field, before the free-text reason, captures the recom-
mendation prior to any post-hoc rationalization; a secondary field-order arm reverses the two
fields to test whether requiring the reason first alters the choice (Section 3.5). The free-text
reason is the basis for the stated-versus-revealed analysis (RQ4).
3.4 Model panel
The audited panel comprises twelve instruction-tuned models. Four are open-weight systems—
llama3.2:3b, qwen2.5:3b, phi3:mini, and mixtral-8x7b-instruct—served through open-
weight runtimes (Ollama for the locally hosted models), representing the quantized, deployable
assistants increasingly embedded in consumer travel and search applications; the exact build
identifier returned by the runtime is logged with every call. Eight are proprietary hosted-API
models accessed through an OpenAI-compatible interface: OpenAI GPT-4o-mini, three Google
Gemini models (1.5 Pro, 2.0 Flash, 2.0 Pro), and four Anthropic Claude models. In keeping with
the pre-specified protocol, the exact API model identifiers were verified against each provider’s
model endpoint and recorded at run start. Reporting the same audit across open-weight and
proprietary panels separates idiosyncrasies of a single model from regularities of the selection
rule that recur across the model class.
Unless a robustness arm specifies otherwise, generation used a sampling temperature of 0.7
with nucleus sampling attop-p = 0.9and a cap of 220 output tokens. A nonzero temperature is
the realistic deployment setting for a consumer-facing assistant and also aligns the data-generating
process with the random-utility interpretation of the choice models, under which stochastic choice
reflects an unobserved utility shock rather than measurement error; a deterministic temperature-0
arm is included as a robustness condition (Section 3.5). Every call drew a deterministic per-call
seed equal tomd5(model|arm|trial|rep) , so that runs are reproducible and resume-safe while
remaining independent across cells. The complete generation configuration (temperature, top-p,
token cap, retries, and timeout) is logged alongside the model identifier for every call.
12

Master design:3,024 choice sets (seed 20260612, SHA-256 hashed),
stratified over 3 personas× 9 templates
Card rendering Grounded- snippet rendering Reversed-layout rendering
main
3,024
T= 0.7
temp-0
594
grounded
297
rank-3
297
field-
order
189
retest
108
×5
letter
297
no-
persona
297
reversed
189
4 local open-weight models
(Ollama, quantized)
8 API models
(OpenAI, Google, Anthropic)
Checkpointed runner:JSON parse → 2 retries→ fuzzy name match; per-call seeds
Analysis:AMCEs (trial-clustered) | condi-
tional logit| price-equivalents (Krinsky–Robb)
stated-vs-revealed| robustness battery
(a)
(b)
(c)
(d)
(e)
(f)
Figure 2: Experiment architecture. The hashed master design is rendered into stimuli, fielded
across experimental arms and the model panel by a checkpointed runner, and analyzed under
the pre-specified statistical analysis plan.
3.5 Experimental arms and procedure
The main arm comprises the 3,024 trials described above. To probe the robustness of the selection
rule and to address anticipated reviewer concerns about prompt and elicitation construction,
we additionally fielded a set of secondary arms, each a disjoint, stratified subset of the main
design that re-presentsidentical stimuliunder a single changed condition (Table 2). Figure 2
summarizes the full experimental architecture from design generation through execution to
analysis.
Holding the choice sets fixed across arms means that any difference in estimated attribute
weights is attributable to the manipulated condition (temperature, format, elicitation, persona
text, or card layout) rather than to differences in the underlying profiles. Because all secondary
arms are carved from the main design, they consume no new choice sets and inherit its stratifica-
tion (an integer number of trials per persona-by-template stratum in every arm). Thenopersona
and card_reversed arms were added in a pre-data amendment to the analysis plan and are
preplanned exploratory robustness checks; they are not part of the confirmatory family.
Table 2 details each secondary arm. Briefly:temp0 isolates the selection rule from sampling
noise; grounded and card_reversed vary the surface form and the attribute ordering of the
cards (the latter testing whether the rating-first layout inflates the rating weight);field_order
reverses the JSON fields;rank_top3 elicits a ranked top-three (analyzed by rank-ordered logit);
13

Table 2: Experimental arms. All arms share common stimuli within each arm across the model
panel; every secondary arm is a disjoint, stratified subset of the main design re-presenting
identical choice sets under one changed condition.
Arm Trials Condition changed vs. main Temp.
main3,024 — (reference) 0.7
temp0594 deterministic decoding 0.0
grounded297 grounded web-snippet format 0.7
rank_top3297 elicit a top-3 ranking 0.7
field_order189 reason elicited before choice 0.7
retest108 a repeated under distinct seeds 0.7
letter297 letter-labeled choice (logprobs) 0.7
nopersona297 persona replaced by neutral text 0.7
card_reversed189 card attribute lines reversed 0.7
manip20 b manipulation check (per model) 0.7
a 108 distinct choice sets, each re-presented under 5 distinct seeds (540 calls
per model); retest repetitions are excluded from the main estimation.
b 20 free-text calls per model asking what Green Key certification is, to confirm
the models can interpret the least familiar attribute; not a choice task.
letter labels alternatives A–E independently of display position to enable a token-logprob
decomposition where available;nopersona replaces the persona with neutral text as a persona-
free baseline; and retest re-presents 108 sets under five seeds each to quantify within-item
response stability.
Before the main runs, a 50-trial pilot per model (the leading slice of the main arm) was
used only to verify JSON parse rates and timing; pilot calls are stored in separate checkpoint
files and are never pooled with the analyzed data. During data collection, a call whose output
failed JSON parsing was re-asked up to two times with a stricter formatting reminder; calls
still unparseable after two retries are recorded as parse failures and excluded from the choice
models. Parse failures are not assumed ignorable: missingness is modeled explicitly by regressing
failure on attributes, persona, template, and model, and if any model exceeds a 5% failure rate,
worst-case bounds are reported and that model is flagged. All inference calls are checkpointed
to disk and resume-safe.
3.6 Statistical analysis
The primary estimand is the average marginal component effect (AMCE) of each attribute,
expressed in percentage points of the probability that an alternative is chosen (Hainmueller
et al., 2014). We estimate AMCEs from a linear probability model in which the binary choice
indicator is regressed on the attribute levels (rating, review volume, and price entered as ordered
categorical dummies against their lowest level; the binary attributes as 0/1 indicators) together
with display-position dummies; the pooled specification adds model fixed effects. Standard
errors are clustered by trial (choice set), which accounts for the dependence among the five
alternatives within a set and, in the pooled model, for the dependence induced by presenting
common stimuli to every model. The AMCE is the headline quantity precisely because it is
scale-free: discrete-choice coefficients are identified only up to a model-specific scale (the inverse
14

of the logit error variance), so raw coefficients are not comparable across models or across
temperatures, whereas choice-probability effects are (Swait and Louviere, 1993).
The confirmatory family is exactly the twelve pre-specified hypotheses H1–H12, comprising
the seven attribute main effects (each a joint Wald test over the attribute’s levels on the pooled
model) and five prespecified interactions (rating× volume, volume× recency, and the three
persona-by-attribute terms), added in a second specification. Familywise error across these twelve
tests is controlled by the Holm procedure atα =.05. All other estimates—per-model AMCEs,
the position effect, the stated-versus-revealed comparison, and all arm contrasts—are reported
as preplanned but exploratory, without a familywise claim. We also report each attribute’s
importance share (the range of its AMCEs divided by the summed ranges across attributes).
As a secondary, structurally explicit analysis we fit conditional (multinomial) logit choice
models grouped by trial, both per model and pooled with model fixed effects and model-by-
attribute interactions (McFadden, 1974); coefficients and odds ratios are reported alongside the
AMCEs. In the deterministictemp0 arm we anticipate quasi-separation and accordingly report
penalized (Firth) estimates or choice shares and AMCEs only; therank_top3 arm is analyzed
with a rank-ordered (exploded) logit.
Trade-offs between non-price attributes and price are computed only if a pre-specified
monotonicity gate is satisfied—namely that the price AMCEs decrease monotonically across
$129, $189, and $249. When the gate holds, each attribute’s effect is converted to a price-
equivalent by dividing its AMCE by the per-dollar price AMCE linearized over the $120 price
range, per persona and pooled, with 95% confidence intervals obtained by the Krinsky–Robb
parametric bootstrap (10,000 draws from the estimated coefficient distribution) (Krinsky and
Robb, 1986). The headline trade-off is the position-1 advantage expressed in dollars per night
and in rating-step equivalents. Any claim that an attribute hasnoeffect is supported not by a
non-significant test but by two one-sided tests (TOST) against a smallest effect size of interest of
|AMCE|< 1.5percentage points. The name-placebo expectation (that the arbitrary hotel names
carry no weight) is evaluated with a joint likelihood-ratio test over the hotel-name dummies,
which is expected to be null.
The design’s precision was established before data collection by Monte-Carlo simulation
under the pre-specified estimator. Table 3 reports, for each effect, the minimum detectable effect
(MDE) at 80% power given the simulated sampling variability of the main arm. The MDEs for
the seven attribute main effects and the position effect span roughly 1.8–2.9 percentage points,
below all effect sizes we regard as substantively meaningful, so the main arm is well powered
for the confirmatory family; the prespecified rating× volume interaction has a larger MDE, as
expected for an interaction term.
3.7 Transparency and research ethics
The study’s design and analysis plan were specified, recorded, and cryptographically hashed
before any main-arm data were collected, and the single pre-data amendment (adding the
nopersona and card_reversed robustness arms) is documented and dated. The experimental
design was generated from a fixed master seed and recorded with SHA-256 hashes of the design
files in advance of all runs, so that the design provably precedes data collection; the amendment
15

Table 3: Monte-Carlo minimum detectable effects (MDE) at 80% power for the main
arm, by effect, in percentage points of choice probability. Values are reproduced from
results/tables/power_mde.csv.
Effect MDE at 80% power (pp)
Guest rating 2.26
Review volume 2.18
Review recency 1.77
Management response 1.79
Affiliation 1.79
Price 2.15
Sustainability 1.86
Position 1 (vs. later slots) 2.87
Rating×volume 5.36
Estimated by simulation under the pre-specified linear-
probability estimator with trial-clustered standard errors;
seesrc/power_sim.py.
was verified programmatically to leave every pre-existing arm’s per-stratum allocation bit-for-bit
unchanged. To support full reproducibility we will archive, in a public repository, the design
files and their hashes, the random seeds, the complete set of prompt templates and personas, the
generation configuration, the analysis code, and the raw verbatim model outputs, so that every
statistic in the manuscript can be traced to a script-produced artifact rather than a hand-entered
value.
The study involves no human subjects: all traveler profiles and hotel alternatives are synthetic,
and the experimental units are model responses, so the work is exempt from human-subjects
review. The only ethical consideration specific to the materials is that the named review sites
in the grounded-snippet format are fictitious and were chosen so as not to correspond to real
businesses. Our use of generative models is confined to the audited systems and the (non-
audited) reason-coding judge; this is declared in full in accordance with the journal’s policy on
generative-AI use, with the relevant statement provided in the submission’s declaration section.
4 Results
We report results in the order of the analysis plan. Section 4.1 establishes data quality and
the handling of non-responses. Section 4.2 presents the primary causal estimates and the
confirmatory tests of H1–H7 and ranks the reputation signals by importance. Section 4.3 reports
the diagnosticity and persona interactions (H8–H12). Section 4.4 isolates list-position bias and
Section 4.5 converts effects into price-equivalents. Section 4.6 compares the models’ stated
reasons with their revealed weights, and Section 4.7 summarizes the pre-specified robustness
battery. All estimates are average marginal component effects (AMCEs) on the probability
of being recommended, in percentage points, with standard errors clustered by choice set;
confirmatory tests are Holm-corrected over the H1–H12 family.
16

Table 4: Response parse-failure rates.
Model card_reversed field_order grounded letter main nopersona rank_top3 retest temp0
claude-fable-5 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
claude-haiku-4-5 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
claude-opus-4-8 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
claude-sonnet-4-6 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
gemini-1.5-pro 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
gemini-2.0-flash 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
gemini-2.0-pro 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
gpt-4o-mini – – – – 0.0 – – – –
llama3.2:3b 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
mixtral-8x7b-instruct 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
phi3:mini 0.0 0.0 0.0 0.0 0.0 0.0 5.1 0.0 0.0
qwen2.5:3b 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
Note.Parse-failure rate (%) by model and arm; pilot and manipulation-check calls excluded.
4.1 Diagnostics and parse rates
Table 4 reports the response parse-failure rate by model and arm. Across all 61,459 model calls
the overall parse-success rate was 99.98% (15 unparseable responses in total), and no model’s
aggregate failure rate exceeded the pre-specified 5% threshold: per-model failure rates ranged
from 0.00% to 0.26%. A single secondary arm—the rank-ordered top-3 task forphi3:mini—
reached 5.1% (15 of 297), the only cell at or above the threshold; because it lies outside the
main conjoint and the affected responses are excluded from estimation, it does not bear on the
primary estimates. With only 15 failures in total the pre-specified missingness model could
not be fit—non-response is too rare to associate with any attribute, persona, template, or
model—so failures are treated as ignorable and no worst-case bounds were required. The realized
design is balanced: every attribute level appears with frequency within 0.01 of its uniform
target (three-level attributes at≈ 0.333each, binary attributes at≈ 0.500), confirming that
randomization supports the AMCE interpretation (Table 4 and the balance diagnostics).
4.2 Causal effects of reputation signals
Figure 3 presents the AMCE forest plot, pooled across the model panel and disaggregated by
model; Table 5 reports the pooled point estimates with 95% confidence intervals. Six of the
seven reputation signals move recommendation probability in the expected direction and are
highly significant. Guest rating is the strongest positive signal: relative to a 3.9-star card, a
4.7-star card is recommended 31.6 pp more often (95% CI [30.9, 32.4]) and a 4.3-star card
10.1 pp more often (H1). Price is the strongest negative signal: relative to $129, a $249 card is
recommended 30.0 pp less often (CI [−30.8,−29.3]) and a $189 card 21.4 pp less often (H6).
Eco-certification raises recommendation probability by 11.6 pp (H7), high review volume (2,100
vs. 45) by 8.3 pp (H2), and a recent most-recent-review by 1.6 pp (H3); chain affiliation lowers it
by 1.8 pp relative to an independent property (H5). The lone exception is management response
(H4): its effect is 0.11 pp (CI [−0.51, 0.73],p =.73), and a two one-sided tests procedure against
the±1.5pp SESOI rejects effects larger than the smallest substantively interesting size, so this
signal is statistically equivalent to zero. The panel is qualitatively consistent on the dominant
signals—all twelve models recommend higher-rated and cheaper hotels—but diverges sharply on
eco-certification, whose per-model AMCE ranges from+0.2pp to+29 .9pp, and on list position
17

40
 20
 0 20 40
AMCE: change in P(recommended), percentage points
Eco-certified (Green Key)
$249 (vs $129)
$189 (vs $129)
Chain (vs independent)
Management responds
Recent review (vs 11 mo.)
2,100 reviews (vs 45)
420 reviews (vs 45)
Rating 4.7 (vs 3.9)
Rating 4.3 (vs 3.9)
Causal effect of reputation signals on LLM hotel selection
pooled
claude-fable-5
claude-haiku-4-5
claude-opus-4-8
claude-sonnet-4-6
gemini-1.5-pro
gemini-2.0-flash
gemini-2.0-pro
gpt-4o-mini
llama3.2:3b
mixtral-8x7b-instruct
phi3:mini
qwen2.5:3b
Figure 3: Average marginal component effects of reputation signals on the probability of being
recommended, pooled and by model.
Table 5: Average marginal component effects on P(recommended), pooled across the model
panel (percentage points).
Attribute AMCE (pp) 95% CIp
Rating 4.3 (vs 3.9) 10.08 [9.44, 10.71] <.001
Rating 4.7 (vs 3.9) 31.65 [30.94, 32.36] <.001
420 reviews (vs 45) 2.25 [1.51, 2.99] <.001
2,100 reviews (vs 45) 8.31 [7.55, 9.07] <.001
Recent review (vs 11 mo.) 1.55 [0.94, 2.16] <.001
Management responds 0.11 [-0.51, 0.73] .729
Chain (vs independent) -1.79 [-2.42, -1.16] <.001
\{}$189 (vs \{}$129) -21.36 [-22.17, -20.54] <.001
\{}$249 (vs \{}$129) -30.03 [-30.75, -29.32] <.001
Eco-certified (Green Key) 11.61 [11.04, 12.18] <.001
Position 2 (vs 1) -2.07 [-3.06, -1.08] <.001
Position 3 (vs 1) -2.38 [-3.37, -1.39] <.001
Position 4 (vs 1) -3.59 [-4.56, -2.62] <.001
Position 5 (vs 1) -3.68 [-4.66, -2.71] <.001
(Section 4.4).
Table 6 reports the confirmatory joint tests for the H1–H12 family with raw and Holm-
correctedp-values. Ten of the twelve pre-specified hypotheses are supported after Holm correction.
The seven attribute main effects are confirmed except H4 (management response), which is not
supported (Wald= 0.12, p =.73); among the interactions, signal diagnosticity (H8) and the
three persona contingencies (H10–H12) are supported, while the volume×recency interaction
(H9) is not (Wald= 3.17, p =.41). No test is sign-reversed relative to its pre-specified direction.
18

Table 6: Confirmatory hypothesis tests (joint Wald tests, Holm-corrected).
Hypothesis Wald dfp(raw)p(Holm)
H1_rating 7613.85 2 <.001 <.001***
H2_volume 485.68 2 <.001 <.001***
H3_recency 24.66 1 <.001 <.001***
H4_response 0.12 1 .729 .729
H5_chain 31.08 1 <.001 <.001***
H6_price 6859.55 2 <.001 <.001***
H7_eco 1590.76 1 <.001 <.001***
H8_rating_x_volume 178.27 4 <.001 <.001***
H9_volume_x_recency 3.17 2 .205 .410
H10_persona_x_price 95.52 6 <.001 <.001***
H11_persona_x_eco 82.52 2 <.001 <.001***
H12_persona_x_chain 28.24 2 <.001 <.001***
Note.Holm-corrected over the H1–H12 confirmatory family.∗p < .05, ∗∗p < .01, ∗∗∗p < .001.
Table 7: Attribute importance: range of AMCEs and normalized share.
Attribute Range (pp) Share
Guest rating 31.65 0.357
Price 30.03 0.338
Sustainability 11.61 0.131
Review volume 8.31 0.094
List position 3.68 0.041
Affiliation 1.79 0.020
Recency 1.55 0.017
Management response 0.11 0.001
Table 7 ranks the attributes by the range of their AMCEs and the normalized importance
share. The panel’s ordering is rating (35.7%)≈ price (33.8%)> sustainability (13.1%)> review
volume (9.4%)> list position (4.1%)> chain affiliation (2.0%)> recency (1.7%)> management
response (0.1%). This reproduces the human primacy of rating and price documented in
hospitality conjoint studies, and like that literature it ranks review valence above volume—here
by nearly four to one—consistent with the valence-over-volume diagnosticity pattern in the
eWOM elasticities reported by Yang et al. Relative to the human benchmark, however, the
panelover-weights eco-certification, which ranks third and rivals review volume, whereas green
certification is typically a minor attribute in human conjoints (Assaker & O’Connor); and it
under-weights two cues humans treat as informative, all but ignoring management response and
chain affiliation.
4.3 Signal diagnosticity and persona contingency
Figure 4 plots the recommendation probability as a function of displayed rating at each level
of review volume, the test of signal diagnosticity. The rating effect grows with review volume,
supporting H8 (Wald= 178.3, df = 4, p < .001): a high rating moves choices more when it
is backed by a large number of reviews, the pattern predicted if the models treat volume as a
19

3.9 4.0 4.1 4.2 4.3 4.4 4.5 4.6 4.7
Displayed average rating
10
20
30
40P(recommended), %
Signal diagnosticity: rating effect by review volume
Review volume
45 reviews
420 reviews
2100 reviews
Figure 4: Signal diagnosticity: the rating effect on P(recommended) at each level of review
volume.
credibility weight on valence. The volume×recency interaction (H9) is not supported (Wald
= 3.17, df = 2, p = .41): the volume effect is not reliably attenuated when the most recent
review is stale.
Figure 5 shows the persona-contingent weights for the price, sustainability, and affiliation
signals; all three persona interactions are supported after Holm correction (H10–H12). Sensitivity
to each signal shifts with the stated traveler in the theoretically expected direction. Eco-
certification is most valuable to the eco-conscious couple, for whom it is worth $65.4 per night
versus $36.8 for the budget family (H11). The chain penalty is also sharpest for the eco-couple
(−$16.5per night) and effectively vanishes for the business persona, for whom affiliation is
not distinguishable from zero (H12). The price interaction is supported (H10, Wald= 95.5,
p<. 001): the negative price effect is large for every persona but steepest for the budget family,
whose smaller price-equivalents (a top rating worth $98 per night versus $153 for the business
traveler) imply the highest price sensitivity, a contingency we revisit in Section 4.5.
4.4 Position bias
Figure 6 reports the AMCE of each list position relative to the first-listed slot. Pooled across the
panel, list position causally affects recommendation probability (RQ2) but modestly: relative to
the first slot, a hotel is recommended 2.1 pp less often in slot 2, 2.4 pp less in slot 3, 3.6 pp less
in slot 4, and 3.7 pp less in slot 5, a shallow and roughly monotone decline that confirms a small
first-position advantage. This pooled estimate conceals substantial heterogeneity: most models
are nearly position-neutral, whereas one (gemini-2.0-flash) exhibits a first-position advantage
an order of magnitude larger (≈ 26pp), consistent with the strong order-sensitivity documented
for some LLM recommenders. Because none of the served models returned usable token-level
log-probabilities, the pre-specified letter-arm decomposition that would separate display-position
from option-label (letter-token) effects could not be estimated; we report this as a limitation
rather than a result (Table 8).
20

$249 (vs $129) Eco-certified (Green Key) Chain (vs independent)
30
20
10
0
10
AMCE (pp)
Persona-contingent signal weights
business
eco_couple
family
Figure 5: Persona-contingent signal weights for price, eco-certification, and chain affiliation.
4
 3
 2
 1
 0
AMCE vs first-listed (pp)
Position 2 (vs 1)
Position 3 (vs 1)
Position 4 (vs 1)
Position 5 (vs 1)
Position bias in LLM hotel selection
Figure 6: Position bias: AMCE of each list position relative to the first-listed hotel.
Table 8: Letter-arm decomposition of list-position effects from letter-token preferences (linear
probability model on first-token letter probabilities, trial-clustered SEs).
no logprob data captured; letter arm analyzed via sampled choices only
4.5 Price-equivalent trade-offs
Conditional on the pre-specified monotonicity gate, Table 9 expresses each signal — and the
first-position advantage — as a price-equivalent in dollars per night, with Krinsky–Robb 95%
confidence intervals, pooled and by persona. The pre-specified price-monotonicity gate passed
both pooled and within every persona (recommendation probability declines monotonically
across $129, $189, and $249), licensing the price-equivalent conversion. Pooled, a one-step
increase from a 3.9- to a 4.7-star rating is worth $126.4 per night (Krinsky–Robb 95% CI [122.2,
130.7]) and from 3.9 to 4.3 stars $40.3; eco-certification is worth $46.4 per night, high review
volume $33.2, and recent reviews $6.2, while chain affiliation costs $7.2. A visible management
response is worth $0.5 per night (CI [−2.1, 3.0]), a null consistent with its negligible AMCE.
21

Table 9: Price-equivalent trade-offs ($/night) with Krinsky–Robb 95% CIs.
Attribute Pooled Business Family Eco couple
Rating 4.3 (vs 3.9) 40.3 [37.8, 42.9] 44.7 [40.0, 49.3] 33.6 [29.6, 37.5] 44.0 [39.2, 49.2]
Rating 4.7 (vs 3.9) 126.4 [122.2, 130.7] 152.8 [144.4, 161.9] 98.2 [93.0, 103.6] 135.2 [127.5, 143.5]
420 reviews (vs 45) 9.0 [6.1, 12.0] 11.8 [6.4, 17.2] 6.9 [2.3, 11.5] 8.8 [3.5, 14.2]
2,100 reviews (vs 45) 33.2 [30.1, 36.3] 40.0 [34.4, 45.9] 27.0 [22.6, 31.5] 34.9 [29.1, 40.9]
Recent review (vs 11 mo.) 6.2 [3.8, 8.6] 6.4 [1.9, 11.0] 5.7 [1.9, 9.3] 6.5 [1.8, 11.1]
Management responds 0.5 [-2.1, 2.9] 2.0 [-2.7, 6.6] -1.1 [-4.9, 2.5] 0.8 [-3.9, 5.6]
Chain (vs independent) -7.1 [-9.6, -4.6] 0.7 [-4.0, 5.5] -5.3 [-9.0, -1.7] -16.5 [-21.3, -12.0]
Eco-certified (Green Key) 46.4 [43.9, 48.8] 39.3 [34.7, 44.0] 36.8 [33.2, 40.5] 65.4 [60.9, 70.2]
First-listed (vs avg 2-5) 11.7 [8.6, 14.9] 18.8 [12.9, 24.8] 7.2 [2.5, 11.7] 9.5 [3.9, 15.2]
The headline managerial quantity is the value of mere ordering: being listed first is worth $11.7
per night (CI [8.6, 14.9])—roughly a tenth of a full rating step, but obtained without changing
anything about the property itself—and as much as $18.8 per night for the business-traveler
persona.
4.6 Stated versus revealed importance
Figure 7 compares, per model, the share of stated reasons mentioning each attribute against
that attribute’s revealed importance share. Across the panel the Spearman rank correlation
between stated mention shares and revealed AMCE importance is positive for every model,
ranging from+0.59to+0 .85(median ≈ 0.69), so models’ explanations broadly track what their
choices reveal. The systematic gaps are nonetheless informative (RQ4). Two cues are used more
than they are voiced: list position is almost never mentioned (≤ 0.7%of reasons) despite a
4.1% revealed importance share, and review volume is rarely invoked despite a 9.4% share—the
models act on ordering and on volume without narrating either. Conversely, brand/affiliation is
over-voiced relative to its near-zero influence, mentioned in up to 55% of one model’s reasons
while contributing only 2.0% of revealed importance. Headline mention shares use the transparent
keyword-dictionary coder applied to all 35,223 parseable reasons; a generative judge model drawn
from outside the audited panel served as a cross-check and agreed on the attribute orderings.
4.7 Robustness
Figure 8 summarizes the stability of the signal weights across the robustness battery, and
Table 10 reports test–retest consistency. The signal weights are stable across the nine prompt
templates: the standard deviation of each attribute’s AMCE across templates is at most 1.5 pp
(1.48 pp for the 4.7-star rating effect and 1.10 pp for the $249 price effect), small relative to
the effects themselves. The estimates are temperature-invariant in the sense that matters for
cross-condition comparison: although the raw logit scale shifts between temperature 0.7 and 0.0,
the ratio of each AMCE to the price effect is essentially unchanged (e.g. the rating-to-price ratio
is−1.07at 0.7 and−1.06at 0.0; the eco-to-price ratio−0.39at both). Presentation format
barely matters: rendering cards as retrieved web snippets shifts every AMCE by at most 1.3 pp,
and reordering the JSON so the reason precedes the choice shifts them by at most 0.8 pp. The
plausibility check is also reassuring—excluding trials containing dominated or dominating cards
moves the rating and price effects by about 2.4 pp and leaves the qualitative pattern intact.
22

0.0 0.2 0.4 0.6 0.8 1.0
Revealed importance (AMCE share)
0.0
0.2
0.4
0.6
0.8
1.0Stated importance (mention share)
Stated vs revealed attribute importance
claude-fable-5
claude-haiku-4-5
claude-opus-4-8
claude-sonnet-4-6
gemini-1.5-pro
gemini-2.0-flash
gemini-2.0-pro
gpt-4o-mini
llama3.2:3b
mixtral-8x7b-instruct
phi3:mini
qwen2.5:3b
stated = revealed
Figure 7: Stated (reason-mention share) versus revealed (AMCE importance share) attribute
importance, by model.
1.0
 0.5
 0.0
AMCE difference (pp)
Rating 4.7 (vs 3.9)
2,100 reviews (vs 45)
$249 (vs $129)
Recent review (vs 11 mo.)
Management responds
Chain (vs independent)
Eco-certified (Green Key)
Temperature
1.0
 0.5
 0.0 0.5 1.0
AMCE difference (pp)
Snippet format
0.2
 0.0 0.2 0.4 0.6
AMCE difference (pp)
Field order
Robustness of signal weights
Figure 8: Robustness of signal weights across temperature, prompt format, and field order.
The one check that does not return the expected null is the hotel-name placebo: the joint test
over the 40 name dummies is significant (LR= 254.4, df = 39, p < .001). Given the very
large sample (n = 61,459choice sets) this test is highly powered and the implied per-name
contribution is small, but we flag that the connotation-neutral names were not perfectly inert; the
counterbalanced name assignment used throughout protects the attribute estimates regardless.
Finally, test–retest consistency across the five seeds is high: the modal-choice share ranges from
0.81 to 1.00 and per-set entropy is correspondingly low, with the open-weight models showing
realistic stochasticity (e.g.phi3:mini modal share 0.81) and the API-served models behaving
near-deterministically, and the temperature-0 pass confirms determinism where expected.
23

Table 10: Test–retest consistency of recommendations.
Model Modal share Entropy
claude-fable-5 1.000 0.000
claude-haiku-4-5 1.000 0.000
claude-opus-4-8 1.000 0.000
claude-sonnet-4-6 1.000 0.000
gemini-1.5-pro 1.000 0.000
gemini-2.0-flash 1.000 0.000
gemini-2.0-pro 1.000 0.000
llama3.2:3b 0.831 0.341
mixtral-8x7b-instruct 1.000 0.000
phi3:mini 0.813 0.382
qwen2.5:3b 0.928 0.151
Note.Mean over test–retest choice sets (5 repetitions each).
5 Discussion
This study audited the reputation function of LLM travel assistants acting as the gatekeeper
of hotel discovery, estimating the causal weight each managed reputation signal carries in the
machine’s recommendation and benchmarking that weight against the human electronic word-of-
mouth (eWOM) evidence. We organize the discussion around what the findings mean for theory
(Section 5.1), for hotel managers (Section 5.2), and for platforms and policy (Section 5.3), before
stating the study’s limitations (Section 5.4) and the research agenda it opens (Section 5.5).
5.1 Theoretical implications
Our central theoretical move is to treat signaling theory and algorithmic gatekeeping as a single
system rather than two separate literatures. In the classical account, reputation signals such
as ratings and reviews resolve information asymmetry for ahumandecision-maker who cannot
inspect an experience good before purchase (Spence, 1973). When an LLM assistant interposes
itself between the traveler and the property, a second receiver is inserted into the signaling
chain: the signal must now be legible to, and weighted by, the machine before it can ever reach
the traveler. The audit therefore measures a previously unobserved object—the gatekeeper’s
revealedreputation function—and asks whether the machine honors, distorts, or inverts the
signal hierarchy that decades of human research have documented.
The first theoretical contribution concerns the fidelity of that reputation function to the
human benchmark. The human eWOM ordering places review valence far above volume, with
management response, brand, price, and certification in measured secondary roles (Yang et al.,
2018; Proserpio and Zervas, 2017; Assaker and O’Connor, 2023). Our results show that the
gatekeeper partially honors and partially rewrites that hierarchy: it reproduces the human
primacy of guest rating and the valence-over-volume pattern—rating is the single largest lever
and outranks review volume by nearly four to one—but it departs from the human prior in two
consequential ways. The assistant has therefore internalized the broad shape of the human signal
hierarchy from its training distribution while operating, at the margins that matter commercially,
24

on a reputation function of its own. Our evidence indicates that the machineover-weights
third-party eco-certification, which it elevates to the third most important signal (rivaling review
volume) where it is a minor attribute in human conjoints, andunder-weights two cues humans
treat as informative—management response, whose effect is statistically indistinguishable from
zero, and brand affiliation, which carries only a small penalty. Signals hotels have rationally
invested in for human audiences may thus be repriced, or ignored, by the intermediary that now
stands between them and demand.
The second contribution reframes the LLM as aninfomediarywhose own interface is part of
the signal environment. Position in the candidate list is an artifact that no hotel controls and that
carries no quality information, yet if the machine’s choice responds to it, position becomes a de
facto reputation signal manufactured by the platform. We find that list position causally affects
recommendation and, although the pooled effect is modest, its importance share (4.1%) exceeds
those of two genuine reputation signals—chain affiliation (2.0%) and review recency (1.7%)—so
a content-free artifact of the interface outranks cues that carry real information. In one model
the first-position advantage is an order of magnitude larger than the panel average, rivaling
substantive signals outright. This speaks directly to the theory of algorithmic gatekeeping
(Metaxa et al., 2021): the gatekeeper does not merely transmit content signals with some noise,
it adds a structural distortion of its own, and the magnitude of that distortion—expressed here
in the same units as the content signals—determines whether reputation or mere placement
governs visibility.
The third contribution concerns the relationship between a system’s stated and revealed
reasons. Signaling theory is silent on whether a receiver canreportthe weights it applies; an
LLM, uniquely among gatekeepers, emits a natural-language rationale alongside its choice. By
comparing the attributes a model names with the attributes that causally drive its choices,
we test whether the verbalized account is a faithful window onto the decision or a post hoc
narration. The models’ stated reasons correspond positively but imperfectly with their revealed
weights—the per-model rank correlation between mention share and causal importance runs
from+0 .59to+0 .85—and the mismatches are systematic rather than random: the models act
heavily on list position and review volume while almost never naming them, and they over-cite
brand affiliation relative to its near-zero causal weight. The verbalized account is thus a partial,
and in places misleading, window onto the decision. A divergence of this kind qualifies the
interpretability of these systems as accountable intermediaries and would caution against taking
model-generated explanations as evidence of the mechanism actually at work—a point with
implications well beyond hotel selection.
Finally, our design speaks to the silicon-sampling debate without participating in it. Because
our estimand is the deployed gatekeeper’s own behavior rather than a proxy for a human
population, the distortions that literature warns about—fidelity gaps and the amplification
of systematic biases (Bisbee et al., 2024)—are not threats to validity here but are themselves
the phenomena the audit is designed to surface. Read this way, our finding that the machine
systematically reweights the human signal hierarchy—over-weighting eco-certification, nulling
out management response, and letting a content-free position artifact outrank real reputation
cues—extends that cautionary literature from the survey-proxy setting into the consequential
25

domain of commercial recommendation.
5.2 Managerial implications
For hotel managers, the practical question is no longer only “how do we win the guest?” but
“how do we win the gatekeeper that the guest now consults?” Our estimates convert that question
into a measured priority list and supply the first causal foundation for what the industry is
already calling generative engine optimization (Aggarwal et al., 2024)—a practice currently
conducted on heuristic and anecdote. We translate the findings into an evidence-based playbook
organized around four questions a revenue or marketing manager can act on.
Which signals to invest in, and in what order.The AMCE estimates rank the reputation
signals by the causal leverage each exerts on the assistant’s choice, in common percentage-point
units. In our panel, the signals that most increase the probability of recommendation are, in rank
order, a high guest rating (+31.6 pp for 4.7 vs. 3.9 stars), eco-certification (+11.6 pp), and high
review volume (+8.3 pp), alongside avoidance of a high price (−30.0pp for $249 vs. $129), while
a visible management response (+0.1 pp, equivalent to zero), review recency (+1.6 pp), and chain
affiliation (−1.8pp) move the machine little or not at all. The managerial implication is that
reputation investment for the AI channel should be sequenced by these machine weights, which
broadly match the human priorities on rating and price but depart sharply on two counts—the
machine rewards eco-certification far more, and management response far less, than a manager
optimizing for human guests would expect—meaning the AI channel warrants a distinct, and in
places counterintuitive, allocation of effort.
How much a signal is worth.Because price is randomized alongside the reputation signals,
each signal’s weight can be expressed as a price-equivalent: the nightly-rate change that offsets
it in the machine’s choice. A manager can therefore read, for example, that moving from a
stale to a recent most-recent review is worth $6.2 per night, that adding eco-certification is
worth $46.4 per night (Krinsky–Robb CI [43.9, 48.8]), and that a full rating step from 3.9 to 4.7
stars is worth $126.4 per night ([122.2, 130.7])—while a visible management response is worth
only $0.5 per night, with a confidence interval spanning zero. These equivalents put reputation
investments and pricing decisions on a common scale for the first time in the AI channel.
How much placement is worth, and who controls it.The position price-equivalent quantifies
a distortion that hotels donotcontrol but must understand: a more prominent slot in the
assistant’s candidate list is worth $11.7 per night pooled (CI [8.6, 14.9])—about a tenth of a
full rating step—and as much as $18.8 per night for the business-traveler persona, all obtained
without changing anything about the property itself. Where this placement value is large relative
to manageable signals, managers should recognize that visibility in the AI channel is partly
governed by where the upstream retrieval or interface happens to place them—an exposure that
argues for monitoring, and for engaging platforms and intermediaries on how candidate sets are
ordered, rather than for content investment alone.
How to target by traveler.The persona analysis indicates whether the machine’s reputation
weights shift with the stated traveler, which bears on property positioning and copy. We find that
all three weights are persona-contingent in the expected directions: price sensitivity is highest for
the budget family, eco-certification is far more valuable to the eco-conscious couple than to the
26

family ($65.4 vs. $36.8 per night), and the chain penalty is sharpest for the eco-couple (−$16.5
per night) while vanishing for the business traveler. Where weights are persona-contingent,
properties can prioritize the signals that matter most for the segments they court; where the
machine applies a single reputation function regardless of stated traveler, segment-tailored
optimization for the AI channel buys little. A standing caution frames the entire playbook:
these weights describe the audited model versions at the time of study, optimization that targets
a machine can be neutralized as models are updated, and the appropriate managerial posture is
continuous measurement rather than a one-time fix.
5.3 Platform and policy implications
The findings also speak to the platforms that deploy these assistants and to the emerging
policy conversation about algorithmic intermediaries. Three implications follow. First, the
position effect is a design choice with commercial consequences: recommendation probability
does respond to the order in which candidates are presented—pooled, the first slot is worth
about $12 per night, and in one model the advantage is an order of magnitude larger—so the
upstream component that fixes that order—retrieval, ranking, or interface—exerts material
influence over which suppliers receive demand, independent of their merits. Platforms that
wish their assistants to be perceived as neutral advisors have a concrete target to audit and to
debias, and order-randomization or position-calibration of the kind proposed in the recommender
literature (Bito et al., 2025; Hou et al., 2024) becomes a governance lever, not merely an accuracy
fix.
Second, the stated-versus-revealed comparison bears on transparency obligations. As inter-
mediaries that materially shape commercial outcomes come under disclosure and explainability
expectations, the question of whether a system’s own explanations track its behavior moves
from academic to regulatory. Our evidence that stated reasons track revealed weights only
imperfectly—and systematically omit the position and volume effects the models actually act
on—indicates that model-generated rationales cannot be relied upon, on their own, as faithful
disclosures of the operative decision factors, which is directly relevant to how explainability
requirements for recommender-style AI should be specified and verified.
Third, the divergence between the machine’s reputation function and the human eWOM
benchmark raises a fairness question for the supply side. Reputation systems were designed
so that properties earning better signals from guests would fare better in the market. If the
gatekeeper reweights those signals—as ours does, modestly favoring independents over chains
and, more consequentially, rewarding high review volume in a way that advantages established
properties over new entrants with thin review histories, while granting an outsized premium to
eco-certification—the intermediary may redistribute visibility in ways that neither travelers nor
suppliers can observe and that existing review-platform governance was not designed to address.
We raise this as a structural consideration for policy rather than a finding about any named
system.
27

5.4 Limitations
Several limitations bound the interpretation of our results and define the conditions under which
they hold.
Scope: the selection stage.Our audit isolates the assistant’s choice among a fixed, already-
retrieved set of five candidates. It does not model theretrievalstage that determines which
properties enter the candidate set in the first place, nor the downstream booking and payment
flow. Real assistant interactions chain retrieval, selection, and sometimes negotiation; we
deliberately hold the candidate set fixed to identify the selection-stage reputation function under
clean experimental control. The estimates therefore describe how the machine chooses among
given options, not the full pipeline from query to booking, and the position effect we measure
is the selection-stage response to ordering, not the compounded effect of retrieval and ranking
upstream.
Panel coverage.Our panel comprises twelve models—four open-weight systems run locally
and eight proprietary models served by API from OpenAI, Google, and Anthropic—at fixed
versions. It is not a census of deployed assistants, and the open-weight models are run in
quantized form, which can affect output distributions relative to full-precision deployment.
Frontier systems served behind product interfaces may apply additional retrieval, system-prompt,
and safety layers absent in our controlled harness, so our estimates characterize the underlying
models under a standardized prompt rather than any particular consumer product end to end.
We report per-model estimates precisely so that heterogeneity across the panel is visible rather
than masked by pooling.
Synthetic stimuli.The hotel cards are synthetic, with independently randomized attributes
and neutral names drawn from a fixed pool. This is a feature of the audit design, not an oversight:
full randomization is what identifies the AMCEs and severs the correlations among attributes
that confound observational data, exactly as randomized attributes do in the correspondence-
audit and conjoint traditions (Bertrand and Mullainathan, 2004; Hainmueller et al., 2014). The
trade-off is ecological: real listings carry photographs, free-text reviews, amenity lists, and
correlated attribute bundles that our cards omit, and the absolute recommendation probabilities
are therefore not meant to transfer to live settings. The causal weights, which is what we
estimate and interpret, are identified despite the stylization.
Single-turn interaction.Each choice is elicited in a single turn, without the follow-up
questions, clarifications, or constraint negotiation typical of real assistant use. Multi-turn
dialogue could amplify, attenuate, or override the single-turn weights we measure, and we do not
observe how the reputation function evolves as a conversation accumulates context.
Language and market.All prompts and stimuli are in English and reflect a United States
traveler framing and US-dollar pricing. Reputation norms, the salience of certifications, brand
landscapes, and assistant behavior may differ across languages and markets, and we do not test
that generalization.
Temporal validity.LLMs are updated frequently, and a model’s reputation function may
drift across versions without notice. Our estimates are valid for the specific model versions
recorded at run time; we treat temporal validity as a first-class limitation and archive exact
version identifiers so that subsequent work can measure drift against our baseline rather than
28

silently confounding it.
Commensurability of benchmarks.The published human effects against which we benchmark
are elasticities and correlations, not percentage-point AMCEs on the probability of choice. We
therefore compareordering and relative importance, not point magnitudes, and we rely on
scale-free AMCE comparison across models (Swait and Louviere, 1993) rather than equating
units that are not directly commensurable.
5.5 Future research
The audit opens several directions. The most immediate is to extend the designup the pipeline
to the retrieval stage: holding a query fixed and auditing which properties an assistant retrieves
into the candidate set would complement the selection-stage weights estimated here and close the
loop from query to recommendation. A second direction is to move from single-turn elicitation
tomulti-turn and agenticinteractions, in which the assistant asks follow-up questions, applies
constraints, or executes a booking, to test whether the reputation function we identify is stable
as dialogue and tool use accumulate.
A third direction targets the human comparison directly. Our benchmarking against published
eWOM effects compares the machine to the humanliterature; a stronger test would collect
primary human conjoint data on the identical stimuliand estimate human and machine AMCEs
on the same scale, turning the ordering comparison we offer into a like-for-like magnitude
comparison and sharpening any claim of divergence. Fourth, because temporal validity is a
genuine threat, alongitudinalaudit that re-runs the frozen design against successive model
versions would measure reputation-function drift over time and establish whether the weights,
the position effect, and the stated-versus-revealed gap are stable properties or moving targets—
information that both managers and platforms would need to act responsibly. Finally, the
evidence-based generative engine optimization agenda we sketch invitesfield validation: testing
whether reputation investments prioritized by the machine’s measured weights actually shift
recommendation outcomes in live assistant deployments, and whether platforms’ position-
calibration interventions neutralize the placement distortion we quantify.
Declaration of generative AI and AI-assisted technologies in the
manuscript preparation process
The authors used large language models for coding assistance.
Data availability
Code and data supporting this study are available from the authors on reasonable request.
Author contributions (CRediT)
M.S.A.B. and S.A.G. (equal contribution): conceptualization, methodology, software, validation,
formal analysis, investigation, data curation, writing — original draft, visualization; M.S.A.B.:
29

supervision. A.A.: resources, project administration, funding acquisition. All authors: writing —
review and editing.
Declaration of competing interests
M.S.A.B. and A.A. are affiliated with Fandaqah, a company operating in the travel and
hospitality sector to which the findings of this study are relevant; this is disclosed in the interest
of transparency. The authors declare no other competing interests.
Funding
This research did not receive any specific grant from funding agencies in the public, commercial,
or not-for-profit sectors. Computational and API resources used for data collection were provided
by Fandaqah.
References
Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan,
and Ameet Deshpande. GEO: Generative engine optimization. InProceedings of the 30th
ACM SIGKDD Conference on Knowledge Discovery and Data Mining, pages 5–16, 2024. doi:
10.1145/3637528.3671900.
Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language models to simulate human samples.Political
Analysis, 31(3):337–351, 2023. doi: 10.1017/pan.2023.2.
Guy Assaker and Peter O’Connor. The importance of green certification labels/badges in online
hotel booking choice: A conjoint investigation of consumers’ preferences pre- and post-COVID-
19.Cornell Hospitality Quarterly, 64(4):401–414, 2023. doi: 10.1177/19389655231184474.
Ana Babić Rosario, Francesca Sotgiu, Kristine De Valck, and Tammo H. A. Bijmolt. The effect
of electronic word of mouth on sales: A meta-analytic review of platform, product, and metric
factors.Journal of Marketing Research, 53(3):297–318, 2016. doi: 10.1509/jmr.14.0380.
Marianne Bertrand and Sendhil Mullainathan. Are Emily and Greg more employable than
Lakisha and Jamal? a field experiment on labor market discrimination.American Economic
Review, 94(4):991–1013, 2004. doi: 10.1257/0002828042002561.
James Bisbee, Joshua D. Clinton, Cassy Dorff, Brenton Kenkel, and Jennifer M. Larson. Synthetic
replacements for human survey data? the perils of large language models.Political Analysis,
32(4):401–416, 2024. doi: 10.1017/pan.2024.5.
Ethan Bito, Yongli Ren, and Estrid He. Evaluating position bias in large language model
recommendations. arXiv:2508.02020, 2025.
30

Judith A. Chevalier and Dina Mayzlin. The effect of word of mouth on sales: Online book
reviews.Journal of Marketing Research, 43(3):345–354, 2006. doi: 10.1509/jmkr.43.3.345.
Kristopher Floyd, Ryan Freling, Saad Alhoqail, Hyun Young Cho, and Traci Freling. How online
product reviews affect retail sales: A meta-analysis.Journal of Retailing, 90(2):217–232, 2014.
doi: 10.1016/j.jretai.2014.04.004.
Jens Hainmueller, Daniel J. Hopkins, and Teppei Yamamoto. Causal inference in conjoint
analysis: Understanding multidimensional choices via stated preference experiments.Political
Analysis, 22(1):1–30, 2014. doi: 10.1093/pan/mpt024.
John J. Horton, Apostolos Filippas, and Benjamin S. Manning. Large language models as
simulated economic agents: What can we learn from homo silicus? NBER Working Paper
31122, National Bureau of Economic Research, 2023.
Yupeng Hou, Junjie Zhang, Zihan Lin, Hongyu Lu, Ruobing Xie, Julian McAuley, and Wayne Xin
Zhao. Large language models are zero-shot rankers for recommender systems. InAdvances
in Information Retrieval: 46th European Conference on Information Retrieval (ECIR 2024),
volume 14609 ofLecture Notes in Computer Science, pages 364–381. Springer, 2024. doi:
10.1007/978-3-031-56060-6\_24.
Itzhak Krinsky and A. Leslie Robb. On approximating the statistical properties of elasticities.
The Review of Economics and Statistics, 68(4):715–719, 1986. doi: 10.2307/1924536.
Daniel McFadden. Conditional logit analysis of qualitative choice behavior. In Paul Zarembka,
editor,Frontiers in Econometrics, pages 105–142. Academic Press, New York, 1974.
Danaë Metaxa, Joon Sung Park, Ronald E. Robertson, Karrie Karahalios, Christo Wilson,
Jeffrey Hancock, and Christian Sandvig. Auditing algorithms: Understanding algorithmic
systems from the outside in.Foundations and Trends in Human-Computer Interaction, 14(4):
272–344, 2021. doi: 10.1561/1100000083.
Sangwon Park and Juan L. Nicolau. Asymmetric effects of online consumer reviews.Annals of
Tourism Research, 50:67–83, 2015. doi: 10.1016/j.annals.2014.10.007.
Phocuswright. Search slips, AI surges: Travel’s new front door? Technical report, Phocuswright,
2025. Nearly 40% of U.S. travelers used generative AI for trip planning in the prior 12 months,
an 11-point year-over-year increase.
Davide Proserpio and Georgios Zervas. Online reputation management: Estimating the impact
of management responses on consumer reviews.Marketing Science, 36(5):645–665, 2017. doi:
10.1287/mksc.2017.1043.
Ruiping Ren, Yingwei Xu, Xing Yao, Shu Cole, and Haining Wang. Whose journey matters?
investigating identity biases in large language models (LLMs) for travel planning assistance.
arXiv:2410.17333, 2024.
31

Manon Reusens, Sofie Goethals, Toon Calders, and David Martens. Would a large language model
pay extra for a view? inferring willingness to pay from subjective choices. arXiv:2602.09802,
2026.
Christian Sandvig, Kevin Hamilton, Karrie Karahalios, and Cedric Langbort. Auditing algo-
rithms: Research methods for detecting discrimination on internet platforms. InData and
Discrimination: Converting Critical Concerns into Productive Inquiry, a preconference at the
64th Annual Meeting of the International Communication Association, Seattle, WA, USA,
2014.
Marko Sarstedt, Susanne J. Adler, Lea Rau, and Bernd Schmitt. Using large language models
to generate silicon samples in consumer and marketing research: Challenges, opportunities,
and guidelines.Psychology & Marketing, 41(6):1254–1270, 2024. doi: 10.1002/mar.21982.
Beverley A. Sparks and Victoria Browning. The impact of online reviews on hotel booking
intentions and perception of trust.Tourism Management, 32(6):1310–1323, 2011. doi:
10.1016/j.tourman.2010.12.011.
Michael Spence. Job market signaling.The Quarterly Journal of Economics, 87(3):355–374,
1973. doi: 10.2307/1882010.
Joffre Swait and Jordan Louviere. The role of the scale parameter in the estimation and
comparison of multinomial logit models.Journal of Marketing Research, 30(3):305–314, 1993.
doi: 10.1177/002224379303000303.
Yang Yang, Sangwon Park, and Xingbao Hu. Electronic word of mouth and hotel performance: A
meta-analysis.Tourism Management, 67:248–260, 2018. doi: 10.1016/j.tourman.2018.01.015.
Qiang Ye, Rob Law, and Bin Gu. The impact of online user reviews on hotel room sales.
International Journal of Hospitality Management, 28(1):180–182, 2009. doi: 10.1016/j.ijhm.
2008.06.011.
Ya You, Gautham G. Vadakkepatt, and Amit M. Joshi. A meta-analysis of electronic word-of-
mouth elasticity.Journal of Marketing, 79(2):19–39, 2015. doi: 10.1509/jm.14.0169.
32
