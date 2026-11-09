---
title: Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders
url: https://arxiv.org/abs/2609.17989
category: consumer-behavior
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Davood Wadi
- Yu Ma
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.17989
pages: 43
chars: 133703
fetched_at: '2026-11-08T13:15:50+00:00'
kb_version: 1
---

# Whom Do AI Agents Work For? Role Assignment Induces Sponsorship Bias in LLM Recommenders

Whom Do AI Agents Serve? Role-Induced Sponsorship Bias in
Decision Models and Generative LLMs
Davood Wadi
Desautels Faculty of Management
McGill University
Montreal, Quebec, Canada
davood.wadi@hec.ca
Yu Ma
Desautels Faculty of Management
McGill University
Montreal, Quebec, Canada
yu.ma@mcgill.ca
Abstract
Consumers increasingly delegate product search to AI shopping agents powered either by generative large
language models (LLMs) that deliberate in natural language or by non-generative decision models that
output calibrated choice probabilities in a single forward pass. Because retail platforms monetize through
sponsored placements that shoppers typically discount, we examine whether an AI agent’s evaluation of
paid listings depends on who delegates the agent across both model families. Across three studies with
no instructions to favor advertisers, naming a booking platform (vs. a traveler) as the agent’s principal
significantly attenuates the penalty applied to sponsored listings. Study 1 establishes this sponsorship bias
across generative LLMs, prompt wordings, and reasoning efforts, showing that platform delegation weakens
pre-choice skepticism and that naming the consumer as the beneficiary eliminates the bias. Study 2 establishes
the bias across six commercial and open-weight decision models on calibrated choice probabilities and shows
that consumer-aligned fine-tuning of an open-weight decision model (Kev 9B) across non-hotel retail categories
eliminates the bias zero-shot on hotel choices. Study 3 decomposes the disclosure label across both model
families, showing that attributing the placement to the platform triggers the sponsorship bias, whereas stricter
disclosure wording (“Sponsored” vs. “Promoted”) lowers paid-listing evaluation without eliminating this bias.
Keywords: large language models; decision models; AI agents; retail media; sponsorship disclosure; digital
retailing
Introduction
Retailers and technology firms have deployed generative large language models (LLMs) as conversational
shopping assistants (Amazon, 2026; Meta, 2026; Walmart, 2024), while a growing share of consumers use
general-purpose chatbots to discover and evaluate products (Pandya, 2025; Balaskas, 2026; Wadi and Ma,
2026b; Hasselwander et al., 2026; Kumar et al., 2026; Mogaji and Jain, 2024). Alongside generative LLMs, AI
providers have recently introduced non-generative decision models (also called System-One models; Palmer,
2026) that directly score and rank alternatives without generating text. Simultaneously, AI interfaces and
digital marketplaces have begun incorporating advertisements into agent-mediated search (OpenAI, 2026).
As a result, the AI systems used to evaluate and recommend products are also the channel through which
advertisers pay for their products to be recommended.
This dual role places the AI agent between two different principals whose interests diverge (Hagiu and Jullien,
2011; Inderst and Ottaviani, 2012; Abdollahpouri et al., 2020). On the one hand, the consumer is the assumed
principal who relies on the AI agent as a shopping advisor. On the other hand, the deploying platform could
be named as the principal in the system instructions. The AI agent must therefore execute an evaluative
judgment that balances between the interest of the consumer who trusts it and the platform that programs
its role.
In traditional e-commerce, advertising disclosures were designed to preserve consumer autonomy (Evans and
Park, 2015; Boerman et al., 2017). A shopper encounters a “Sponsored” label, processes the signal with
skepticism, and discounts the listing’s claims accordingly (Friestad and Wright, 1994; Campbell and Kirmani,
2000; Obermiller and Spangenberg, 1998; Sahni and Nair, 2020).
1
arXiv:2609.17989v3  [econ.GN]  28 Oct 2026

However, when an AI assistant evaluates market alternatives or makes purchases on consumers’ behalf
(e.g., Google DeepMind, 2026), the duty of evaluating sponsored (vs. organic) alternatives falls on the AI
agent, whose decision process is hidden from the consumer. Because paid placements enter consumer utility
as negative cues, if the AI agent’s evaluation of a sponsored listing shifts in the platform’s favor simply
because the platform (vs. the consumer) is named in its system instructions, the consumer would end up with
lower-utility alternatives. We refer to this shift as sponsorship bias, defined as a more favorable evaluation of
sponsored listings when the platform (vs. the consumer) is the AI agent’s principal.
We jointly investigate generative LLMs and non-generative decision models across three controlled choice
studies by manipulating the delegating party and observing whether the AI agent’s evaluative judgment
shifts. In Study 1, we presented a frontier generative LLM (Gemini 3.1 Pro) with matched hotel listings
and altered a single sentence in the system prompt to define the agent as a delegate of either a traveler or a
booking platform. When delegated by the traveler, the agent penalized the sponsored listing and chose it
50.2 percentage points less often than an equivalent organic listing. Under platform delegation, this penalty
significantly attenuated to 29.2 percentage points. We replicate this finding across five additional frontier
LLMs from three providers, successive model generations, reasoning depths, and system-prompt wordings.
Analysis of pre-choice reasoning traces reveals that platform delegation systematically reduces the skepticism
that sponsorship disclosures trigger, while adding one sentence instructing the platform-delegated agent to
act in the traveler’s best interest eliminates the attenuation.
Study 2 investigates the emerging family of non-generative System-One decision models (Palmer, 2026), which
output choice probabilities rather than open-ended text. Evaluating six decision models across a 360-stimulus
position-balanced Latin-square design, we show that consumer delegation produces a significant sponsorship
penalty on exact log-odds, but platform delegation significantly attenuates this penalty. In Study 2, we show
that fine-tuning an open-weight decision model (Kev 9B) across non-hotel retail categories eliminates the
sponsorship bias in hotel choices while preserving the consumer sponsorship penalty.
Study 3 decomposes the disclosure label (“Promoted” vs. “Sponsored” crossed with whether the placement is
attributed “by the platform”) across both generative LLMs and decision models. Across both architectures,
attributing the paid placement to the platform is what drives the sponsorship bias. Although the explicit term
“Sponsored” lowers paid-listing evaluation relative to “Promoted” in both models, the three-way interaction
is nonsignificant in both architectures, showing that stricter disclosure wording does not eliminate this
sponsorship bias.
This research makes three contributions to the literature on digital retailing, sponsorship disclosure, and
AI-mediated commerce. First, we show across both generative LLMs and non-generative decision models
that stakeholder alignment emerges implicitly from role assignment alone rather than from programmed
objectives (Abdollahpouri et al., 2020) or explicit instructions to favor advertisers (Wu et al., 2026; Allouah
et al., 2026). We show that this sponsorship bias can be eliminated by training the model to evaluate options
consistently across principals while preserving its original choice tendencies. Second, we extend research on
sponsorship disclosure and persuasion knowledge (Boerman et al., 2017; Friestad and Wright, 1994; Evans
and Park, 2015) from human shoppers to AI intermediaries, showing that stricter disclosure terminology
(“Sponsored” vs. “Promoted”) lowers paid-listing selection overall yet fails to eliminate the sponsorship bias
between platform- and consumer-delegated agents. Third, we isolate the semantic trigger of this bias by
showing that attributing the paid placement to the platform itself is what drives sponsorship bias across both
generative and single-pass decision architectures.
Literature review
Technological shifts continually reshape retail formats, digital channel competition, and how consumers adopt
retail technologies to search and evaluate market alternatives (Gauri et al., 2021; Grewal et al., 2021; Jindal
et al., 2021; Namin et al., 2026; Ratchford et al., 2022). Consumers increasingly delegate product search and
evaluation to generative AI shopping assistants (Hermann and Puntoni, 2024; Srinivasa Raja et al., 2026;
Lalicic and Weismayer, 2021) through two channels. First, online retailers and booking platforms provide AI
assistants directly on their interfaces (Bahmani et al., 2022; Chakraborty et al., 2024). Second, consumers
2

can deploy general-purpose LLM agents on their own behalf. Because digital marketplaces serve consumers,
platforms, and advertisers whose interests diverge (Abdollahpouri et al., 2020), a central question for retailing
is whether an AI agent’s recommendations depend on who provides the service.
Prior research on retail recommendation systems has predominantly analyzed ranking and filtering engines
(Rokach and Ricci, 2011; Zhang et al., 2022), in which competing stakeholder objectives are balanced through
an explicit formula set by the system’s designers (Abdollahpouri et al., 2020). Modern foundation-model
recommenders depart from this paradigm across two complementary model families: generative LLMs, which
deliberate in natural language to produce discrete choices (Stoeber et al., 2026; Suh and Atlas, 2026), and
non-generative decision models, which adapt language-model backbones to score structured options in a
single forward pass and output calibrated choice probabilities at low latency and cost (Palmer, 2026). In both
families, the party on whose behalf the agent acts can be specified in a single sentence of natural-language
system instructions (Wallace et al., 2024). Recent work on agentic commerce examines how AI shopping
agents weigh product attributes and labels under a fixed user role (Allouah et al., 2026) or how chatbots
behave when explicitly instructed to steer users toward sponsored products (Wu et al., 2026). Neither
addresses whether merely specifying who employs the agent (i.e., platform vs. consumer, with no instruction
to favor advertisers) shifts how generative LLMs and decision models evaluate paid placements.
The provider of the AI agent matters in modern retailing because online marketplaces and travel platforms
increasingly extend traditional retail promotions (Ailawadi et al., 2009; Grewal et al., 2011) into retail media
networks, earning high-margin revenue from on-site sponsored placements alongside organic assortment
(Thomas et al., 2025). An AI assistant deployed on such a platform serves two parties whose interests diverge.
While the platform has a structural incentive to steer buyers toward sponsored alternatives (Hagiu and Jullien,
2011; Inderst and Ottaviani, 2012; Kang and Jindal, 2015), consumers discount sponsored listings because
paid placement signals a persuasive motive. As a result, sponsorship enters consumer utility as a negative cue
(Boerman et al., 2017; Kim et al., 2019; Sahni and Nair, 2020). Consequently, an AI assistant that softens its
discount on sponsored listings steers shoppers toward lower-utility alternatives. This would lead consumers
to perceive the AI assistant as manipulative or self-serving, and to experience betrayal (Saenger et al., 2024;
Liu et al., 2025; Du and Xie, 2021).
Accordingly, regulation relies on sponsorship disclosure to mitigate such conflicts (European Parliament and
Council of the European Union, 2022; Federal Trade Commission, 2013). Labeling a listing as sponsored
(Bigne et al., 2021) alerts human shoppers to the commercial motive, activates persuasion knowledge, and
allows them to discount the paid placement (Friestad and Wright, 1994; Boerman et al., 2017). However,
disclosure remedies require that the protected party is the one who observes and discounts the warning
(Loewenstein et al., 2011). When an AI agent evaluates listings on a consumer’s behalf, the sponsorship
label reaches the agent rather than the consumer, and the agent’s internal evaluation remains hidden to the
consumer (Chen et al., 2025). Whether disclosure still protects the consumer therefore depends on whether a
platform-provided AI agent penalizes paid placements to the same extent as a consumer-deployed agent.
Hypothesis development
To test whether an AI agent’s recommendations depend on who provides the service, we refer to the entity
named as the delegator in the system instructions as the agent’s principal. We define consumer delegation as
the condition where the system prompt assigns the consumer as the agent’s principal (e.g., “You are employed
by a traveler”), and platform delegation as the condition where the system prompt assigns the platform as
the agent’s principal (e.g., “You are employed by a booking platform”).
Behavior in both generative LLMs and decision models is not fully specified by explicit instructions. As
models scale, they display capabilities and response patterns that were not directly programmed (Wei et al.,
2022). One well-documented pattern is context-dependent role adoption. When conditioned on a persona
or party, a language-model backbone tailors its representations and outputs to the inferred perspective of
that party (Deshpande et al., 2023; Shanahan et al., 2023; Stoeber et al., 2026). For instance, conditioning
a model on demographic information leads it to reproduce the opinion distributions of the corresponding
human subgroups (Argyle et al., 2023; Santurkar et al., 2023) by shifting its answers toward the views a
3

user appears to hold, even at the expense of accuracy (Perez et al., 2023; Sharma et al., 2024). In a retail
recommendation task, a role assignment tells the AI agent whose perspective to adopt, which could shape
how the agent evaluates alternatives in both open-ended choice generation (LLMs) and single-pass option
scoring (decision models), even with no explicit instruction regarding revenue or commissions.
Role adoption draws on the semantic associations a foundation model acquires from its training corpora,
which link social categories or entities to particular behaviors (Bolukbasi et al., 2016; Caliskan et al., 2017;
Garg et al., 2018). Because these corpora include vast amounts of human text, such as product reviews,
consumer forums, and marketing literature, the model could adopt the negative inferences and skepticism
shoppers express toward promotional cues and paid placements (Campbell and Kirmani, 2000; Friestad and
Wright, 1994; Obermiller and Spangenberg, 1998; Cai et al., 2016; Kim and Kim, 2021). As a result, we
hypothesize that a consumer-delegated AI agent reflects this skepticism and applies a penalty to sponsored
listings, which we refer to as the sponsorship penalty (i.e., the reduction in a listing’s choice share or calibrated
choice probability attributable to its disclosed sponsorship status).
H1.Under consumer delegation, given equal objective attributes, an AI agent evaluates a sponsored listing
less favorably than an organic listing.
A model trained on text describing digital markets is also likely to associate each party with the interest it
typically pursues. Therefore, a label naming the AI agent’s principal may shift how the agent evaluates a
paid placement. Although a sponsorship label is a warning from the consumer’s perspective, it is a source of
retail media revenue from the platform’s. Therefore, an AI agent delegated by a platform may adopt the
platform’s perspective and relax the penalty it would otherwise apply to sponsored listings.
H2.The negative effect of sponsorship on listing evaluation is moderated by the agent’s principal, such that
the sponsorship penalty is attenuated when the agent is delegated by the platform (vs. consumer).
In generative LLMs that produce pre-choice reasoning traces, we can also observe the deliberation pathway
through which this sponsorship penalty operates. Recognizing a listing as paid leads consumers to doubt
its claims, and this doubt lowers their evaluation of the listing (Friestad and Wright, 1994; Campbell and
Kirmani, 2000). If a generative LLM agent penalizes sponsored listings, its observable outputs should reflect
a similar sequence. A sponsorship label should lead the AI agent to express skepticism about the listing’s
value in its reasoning before choosing (Hagendorff et al., 2023), and that skepticism should be associated
with a lower probability that it chooses the listing.1
H3.Skepticism mediates the effect of sponsorship on choice.
If an AI agent delegated by a consumer treats the sponsorship label with skepticism, an AI agent delegated
by the platform, which earns commissions, should associate the same label with less skepticism. The principal
should therefore moderate the first stage of the mediated pathway, such that the indirect effect of sponsorship
on choice through skepticism is weaker under platform (vs. consumer) delegation (Fig. 1).
H4.The effect of sponsorship on skepticism is moderated by the agent’s principal, such that platform
delegation attenuates the effect of sponsorship on skepticism.
— insert Fig. 1 about here —
Study 1
We begin by testing the effect of sponsorship under consumer vs. platform delegation in hotel booking, an
industry where online search and sponsored placements are pervasive. Because crossing all experimental
manipulations across multiple model families, versions, prompt wordings, and reasoning depths would
combinatorially expand the design, we conduct the primary analysis on Gemini 3.1 Pro and evaluate model
architecture, version, wording, and reasoning effort in subsequent robustness experiments.
1Note that the proposed mediation is temporal: the AI agent produces the reasoning trace before it makes the choice. With
mediation we test this temporal pathway. We do not claim that the reasoning traces cause the choice.
4

Experiment design, stimuli, and procedure
Factorial design.We employed a 2 (Sponsorship: organic vs. sponsored) × 2 (Principal: consumer
vs. platform) factorial design. In each choice task, the LLM evaluated four hotel alternatives (Table W1): a
target listing (manipulated), an matched organic competitor, and two dominated alternatives included for
ecological validity. The target alternative received the sponsorship manipulation via the “Platform Sponsor”
attribute (truevs.false), which was set tofalsefor all other alternatives. To control for position effects (Liu
et al., 2024; Pezeshkpour and Hruschka, 2024; Yin et al., 2026; Wadi and Ma, 2026a; Wang et al., 2024), the
order of alternatives and attributes was randomized on every trial.
Stimuli.In each session, four unique hotel names were randomly drawn from a pool of 10 real Expedia
hotels. Positive reviews were drawn from a validated pool of 10 paired Expedia reviews (Table W8; Appendix
B) and were randomly assigned to the target and competitor listings, while negative reviews were assigned to
the two dominated alternatives (Kim et al., 2019). To eliminate price differences as a confound, the target
and competitor hotels were assigned identical prices (P) drawn from the empirical distribution of Expedia
listings (P∼U [$173.45, $351.40]), whereas the dominated alternatives were assigned fixed prices above this
range ($450 and $400). All regression models include target- and competitor-hotel and review fixed effects
alongside standardized price to absorb baseline brand and text preferences (Table W11).
Prompts and replications.Table 1 presents the system prompts manipulating the principal. The platform-
delegation prompt names the employing booking platform but omits any instruction regarding commissions,
ad revenue, or profitability, to avoid experimental demand effects. Because LLM token sampling is stochastic,
we conducted 500 independent, zero-shot replications per cell using a Monte Carlo approach (Robert et al.,
1999; Wang et al., 2022; Wadi and Fredette, 2025; Holtzman et al., 2019), yieldingN = 2,000observations
for the main experiment (see Appendix B for power analysis, decoding parameters, and API specifications).
Unless otherwise noted, reasoning effort (thinking level) was set tohigh. We recorded the model’s pre-choice
reasoning trace on each trial.
— insert Table 1 about here —
Measures
Our primary dependent variable,target choice, is a binary indicator (1 = target selected, 0 = competitor
selected; dominated alternatives were never chosen). We operationalizeskepticismas the extent to which
the agent’s pre-choice reasoning trace expressed negative or defensive evaluations of the target’s sponsorship
tag (Friestad and Wright, 1994; Obermiller and Spangenberg, 1998; Campbell and Kirmani, 2000). It was
scored on a seven-point Likert scale (1 = Strongly Disagree to 7 = Strongly Agree) for the item: “The
sponsorship status of {target_option_id} made the agent skeptical of its true value to the traveler.”2 3
To avoid shared-weight or provider-alignment bias (Gu et al., 2026; Panickssery et al., 2024), pre-choice
reasoning traces were scored using Kev 9B (Palmer, 2026), an open-weight decision model selected via a
blinded validation study against human ratings on a stratified sample of 60 traces (ICC(2, 1) = 0.959, Pearson
r=.964, MAE= 0.450; see Appendix B and Table W9).
Results
To test H1 and H2, we estimated a binary logistic regression predicting target choice from sponsorship,
principal, and their interaction, controlling for standardized price and hotel and review fixed effects (Table 2;
full table in Table W11). Supporting H1, under consumer delegation the AI agent splits its choices nearly
evenly when the target is organic (53.0% target; Table 3; Fig. 2), but tagging the target “Platform Sponsor”
reduces its choice share to 2.8% (14 of 500 replications), a 50.2 percentage-point penalty (Cohen’sh = 1.29;
β=−6.49,SE= 0.42,p<.001).
— insert Fig. 2 about here —
2{target_option_id}denotes the target’s randomized option identifier.
3We distinguish between the LLM’s observable choice, its generated reasoning trace, and its internal neural activations. Terms
such as “skepticism” do not imply sentient human motivation, but serve as shorthand for defensive evaluation expressed in the
visible pre-choice reasoning trace.
5

Supporting H2, platform delegation significantly attenuates this sponsorship penalty. Under platform
delegation, tagging the target “Platform Sponsor” reduces its choice share from 54.2% to 25.0%, a penalty
of 29.2 percentage points compared to 50.2 points under consumer delegation (Table 3; Fig. 2). This
21.0-point difference-in-differences is significant in the fixed-effects logit (β = 3.99, SE = 0.43, z = 9.32,
p<. 001; Table 2), with the platform-delegated agent selecting the sponsored target at8.93× the rate of the
consumer-delegated agent (25.0% vs. 2.8%). When the target is organic, the principal manipulation has no
detectable effect in either raw choice shares (53.0% vs. 54.2%,p =.704) or the fixed-effects model (β =−0.17,
p=.403), confirming that platform delegation shifts choices only on sponsored listings.
— insert Table 2 about here —
Role-neutral baseline and beneficiary mitigation
To establish the LLM’s baseline evaluation without role assignment, we tested arole-neutralsystem prompt
that named no principal (N = 1,000; Table 3). The role-neutral agent selected the organic target in 49.6% of
replications and the sponsored target in 7.8% (a 41.8-point penalty). Relative to this baseline, consumer
delegation deepens the penalty by 8.4 points and platform delegation reduces it by 12.6 points. Because the
platform-delegated agent selects the sponsored listing more often than the role-neutral agent (25.0% vs. 7.8%)
while organic choice shares do not differ across the three conditions (49.6%, 53.0%, and 54.2%, allp>. 10),
the attenuation under H2 represents an active shift toward the platform’s interest rather than a return to
role-neutral evaluation.
We also tested whether specifying the consumer as the beneficiary inside the platform prompt mitigates
this bias. In a fourth principal condition (platform with consumer beneficiary,N = 1,000; Table 3), we
added the sentence “Act in the traveler’s best interest” to the platform system prompt. This agent chose the
sponsored target in 3.2% of replications (a 48.2-point sponsorship penalty). In a pooled fixed-effects logit
(Table W12), the sponsorship penalty underplatform with consumer beneficiarywas significantly stronger
than under unmitigatedplatformdelegation ( β =−4.09, SE = 0.43, p < .001) and did not differ from
consumerdelegation (β = 0.12, SE = 0.49, p =.812). Explicitly naming the consumer as the beneficiary
therefore eliminates the sponsorship bias induced by platform delegation.
— insert Table 3 about here —
Moderated mediation
We next test the moderated mediation pathway via pre-choice skepticism (H3 and H4). Estimating PROCESS
Model 8 (Table 4; full tables in Table W13 and Table W14) supports H3: sponsorship significantly increases
skepticism under both consumer (b = 4.827, SE = 0.081, p < .001) and platform delegation (b = 3.466,
SE = 0.081, p<. 001), and skepticism negatively predicts target choice (β =−1.670, SE = 0.121, p<. 001),
yielding significant negative indirect effects for both principals (abconsumer =−8.061, 95% CI [−10.636,− 7.309];
abplatform =−5.788, 95% CI [−7.660,− 5.202]). Supporting H4, platform delegation significantly attenuates
the first-stage effect of sponsorship on skepticism (bsponsorship×principal =−1.361, SE = 0.114, p < .001),
producing a positive and significant index of moderated mediation (Indexmod. med. = 2.273, BootSE = 0.318,
95% CI [1.916,3.135]).
— insert Table 4 about here —
Robustness tests
Cross-LLM generalizability
To test whether the sponsorship bias is specific to Gemini 3.1 Pro or a transient artifact that disappears
across model updates, we replicated the2× 2experiment across five additional LLMs (N = 2,000per model;
N = 10,000total), including frontier models from Anthropic (Claude Sonnet 5) and OpenAI (GPT 5.6 Terra),
and three successive generations of Google’s Flash family (Gemini 3.5, 3.6, and 3.8 Flash; Fig. 2; Table
W3). Both H1 and H2 replicate in every model (Table 5; full tables in Table W15 to Table W19). The
consumer-delegated sponsorship penalty is negative and significant in all five LLMs (p < .001), while the
Principal× Sponsorship interaction is positive and significant in all five LLMs (p≤. 007), with the largest
sponsorship bias appearing in the most recent release (Gemini 3.8 Flash).
6

— insert Table 5 about here —
We also replicated the PROCESS Model 8 moderated mediation analysis across the three Gemini Flash
generations (Claude Sonnet 5 and GPT 5.6 Terra do not reliably expose reasoning representations via their
public APIs). Both H3 and H4 are supported in all three models (Table W4; Table W5): sponsorship
increases skepticism, skepticism reduces target choice (p<. 001), and platform delegation attenuates first-
stage skepticism (b from−0.533to −2.165, p<. 001), yielding a positive and significant index of moderated
mediation in every model version.
System-prompt wording and reasoning effort
We next test whether the bias in Gemini 3.1 Pro depends on prompt phrasing or reasoning depth (Table 1;
Table 2). First, to rule out mismatch from the action verb (“book”) or lexical overlap between “hotel booking
platform” and the “Platform sponsor” tag, we conducted two independent2× 2replications (N = 2,000
each): an action-verb variant replacing “book” with “recommend,” and a principal-noun variant replacing
“traveler” and “hotel booking platform” with “customer” and “online travel agency” (Fig. W2; Table W20;
Table W21). Under consumer delegation, sponsorship reduces target choice from 51.2% to 4.0% (principal
noun) and from 48.0% to 5.8% (action verb; bothp<. 001), and the Principal× Sponsorship interaction
remains positive and significant in both variants (β= 2.503andβ= 4.592, bothp<.001; Table 2).
Second, to test whether the bias requires extended deliberation, we executed the2× 2design on Gemini
3.1 Pro at its minimum reasoning effort (thinking_level = “LOW”,N = 2,000), which halved average
reasoning trace length relative to HIGH (M = 284.99vs.543 .92tokens), and pooled it with the HIGH
cells (N = 4,000; Table 2; Table W6; Fig. W3; Table W22). Under LOW thinking, sponsorship reduces
target choice from 50.4% to 5.0% under consumer delegation vs. 49.6% to 25.6% under platform delegation
(Principal×Sponsorshipβ = 2.877, SE = 0.348, p<. 001), and the three-way interaction with thinking level
is not significant (β=−0.842,SE= 0.518,p=.104).
Study 2
Study 2 tests H1 and H2 in non-generative decision models (Palmer, 2026). Because decision models output
calibrated choice probabilities rather than binary draws, they capture continuous shifts in option valuation
without sampling variance or floor effects. We conduct the primary analysis and model-level mitigation on Kev
9B, an open-weight decision model whose parameters can be directly adapted, and then test generalizability
across five additional commercial and open-weight decision models.
Design and procedure
Because a decision model returns a deterministic probability distribution for any fixed input, we constructed
a 360-stimulus position-balanced Latin-square set from the Study 1 hotel and review pools (90 ordered
hotel-name pairs× 4 target option slots, matched with the 90 ordered positive review pairs, holding
target/competitor pricesP, dominated alternatives at $450 and $400, option slots, and attribute order fixed
within each base stimulus; see Appendix B). Each of the 360 stimuli was evaluated on Kev 9B across all
four cells of the 2 (Sponsorship: organic vs. sponsored, via the “Platform sponsor” attribute)× 2 (Principal:
consumer vs. platform) design, yieldingN = 1,440paired observations. The Study 1 principal instruction
was passed as the decisionstate, and the four hotels were passed as a structuredchoicequestion (“Which
hotel would you book?”). Consistent with random utility theory, our primary dependent variable is the
exact log-odds of selecting the target over the competitor,ln(Ptarget/Pcompetitor), analyzed via ordinary least
squares (OLS) with 360 paired stimulus fixed effects and stimulus-clustered standard errors (Table 6). See
Table W7 for calibrated target probabilitiesP(Target).
Results
Supporting H1, under consumer delegation, tagging the target “Platform sponsor” reduces Kev 9B’s calibrated
target probability from43.43%( SD = 13.63) to40.60%( SD = 13.09), a penalty of2.83percentage points
(β=−0.123,SE= 0.012,z=−10.65,p<.001; Table 6; Fig. 3; Table W7).
7

— insert Fig. 3 about here —
Supporting H2, under platform delegation, tagging the target “Platform sponsor” raises its calibrated
probability from42.62%( SD = 13.58) to43.88%( SD = 13.07; β = 0.071, SE = 0.014, z = 4.94, p<. 001),
yielding a positive and significant Principal× Sponsorship interaction (β = 0.194, SE = 0.012, z = 16.47,
p<.001).
— insert Table 6 about here —
Model-level mitigation via consumer-aligned fine-tuning
A deploying platform may innocuously name itself in the system prompt simply to establish its AI assistant’s
persona, but unintentionally bias how the AI agent evaluates paid listings. While Study 1 showed that
adding a beneficiary instruction to the prompt can offset this shift, prompt-level fixes require every platform
to anticipate and manually correct the bias. We therefore test whether consumer-aligned fine-tuning can
eliminate this sponsorship bias at the model level, training Kev 9B to evaluate alternatives consistently across
principals while preserving its baseline consumer preferences.
To prevent domain leakage and pre-trained brand-equity confounds, we constructed an out-of-domain fine-
tuning dataset across five non-hotel retail categories using synthetic brand names (see Appendix B for full
details). Four categories served as the training split (laptops, wireless headphones, coffee makers, and running
shoes; N = 2,880trials) and one held-out category served as the validation split for checkpoint selection
(air purifiers;N = 720trials). Within each category, 45 paired stimuli were balanced across all four option
slots, both sponsorship states (“Platform sponsor” set totruevs.false), and both principals (consumer
vs. platform), mirroring the Latin-square design of the hotel benchmark.
For each retail stimulusx, we queried the frozen base Kev 9B model under consumer delegation to obtain a
shared reference distributionPref(·|s consumer,x )at its calibrated pointer-head temperature (T = 2.194). We
then fine-tuned Kev 9B by minimizing the Kullback-Leibler (KL) divergence between the model’s predicted
option distribution and Pref(· |s consumer,x )under both platform delegation and consumer delegation,
training the model to match its consumer-delegated evaluations across principals while preserving its baseline
preferences. Checkpoints were evaluated by validation KL on the held-out air-purifier category, with zero
exposure to hotel stimuli during training or model selection.
On the held-out retail validation set, consumer-aligned fine-tuning reduced mean KL divergence from the
consumer reference by84.6%(from0 .0195bits at step 0 to0.0030bits at the best checkpoint, step 440).
We then evaluated this selected checkpoint zero-shot on the 1,440-trial Study 2 hotel benchmark (Table 7).
Under consumer delegation, the fine-tuned model preserves a strong and significant sponsorship penalty
(β =−0.109, SE = 0.011, z =−10.47, p<. 001), reducing mean calibrated target probability from43.23%
(organic) to40.74%(sponsored), a2 .49percentage-point penalty comparable to base Kev 9B (2.83points,
43.43%to40.60%).
Importantly, under platform delegation, rather than reversing the sponsorship penalty as in base Kev 9B
(42.62%to43 .88%), the fine-tuned model applies a2.70percentage-point sponsorship penalty (42.37%
organic to39 .68%sponsored; β =−0.118, SE = 0.011, p < .001). Both the main effect of principal
(β =−0.002, SE = 0.009, z =−0.23, p =.820) and the Principal× Sponsorship interaction (β =−0.009,
SE = 0.006,z =−1.51,p =.130) are near zero and statistically nonsignificant. Consumer-aligned fine-tuning
across synthetic non-hotel retail categories thus transfers zero-shot to real-world hotel choices, aligning
platform-delegated evaluation with consumer-delegated evaluation at the model level.
— insert Table 7 about here —
Cross-model generalizability
To test whether the sponsorship bias is specific to Kev 9B, we replicated the 360-stimulus Latin-square
experiment across five additional decision models (N = 1,440per model; N = 8,640total across all six
models), spanning commercial API models (Jev 1.14, Liquid D1-Ultra, Mercury Decide, and Microsoft
Decision 1) and an open-weight model with a distinct scoring architecture (StartLux 27B using bidirectional
prompt attention with letter-logit readout; see Appendix B). Both H1 and H2 are supported in every model
8

(Table 6; Fig. 3; Table W7). Under consumer delegation, sponsorship significantly reduces target log-odds
in all five models (H1:β from−0.729to −3.379, allp < .001; probability penalties from15.00to44 .58
percentage points), and the Principal× Sponsorship interaction is positive and significant in every model
(H2:βfrom0.104to0.641, allp≤.008).
Study 3
While Studies 1 and 2 established the sponsorship bias across generative LLMs and decision models, the label
used in those studies (“Platform sponsor”) combined a paid-placement disclosure (“sponsor”) with explicit
source attribution to the platform (“platform”). To isolate how each component contributes to the bias, Study
3 crosses disclosure type (“Promoted” vs. “Sponsored”), platform attribution (no vs. yes, appending “by the
platform”), and principal (consumer vs. platform) in a2× 2× 2design evaluated across both architectures:
the generative LLM from Study 1 (Gemini 3.1 Pro) and a non-generative decision model from Study 2 (Kev
9B).
We test three predictions. First, because “Sponsored” is an unambiguous paid-placement disclosure whereas
“Promoted” is a softer merchandising tag (Friestad and Wright, 1994; Boerman et al., 2012; Kim et al., 2019),
“Sponsored” should lower target evaluation relative to “Promoted” under both principals in both models.
Second, if sponsorship bias reflects alignment with the employing platform, attributing the placement to the
platform (“by the platform”) should amplify sponsorship bias (a positive Principal× Attribution interaction)
in both architectures. Third, we test whether mandating the explicit term “Sponsored” eliminates this
attribution-driven sponsorship bias or whether it persists even under stricter wording.
Design and procedure
We manipulated the target’s disclosure attribute across four labels (Table 8): “Promoted,” “Promoted by the
platform,” “Sponsored,” and “Sponsored by the platform” (truefor the target,falsefor all other options).
Following the protocols of Studies 1 and 2, we collected 500 independent replications per cell for Gemini
3.1 Pro (N = 4,000total; analyzed via binary logistic regression with hotel and review fixed effects and
standardized price; Table 9; full table in Table W23) and evaluated the 360 paired Latin-square stimuli across
all eight cells for Kev 9B (N = 2,880total; analyzed via OLS on exact log-oddsln(Ptarget/Pcompetitor)with
360 stimulus fixed effects and stimulus-clustered standard errors; Table 9).
— insert Table 8 about here —
Results
Supporting our first prediction, the explicit “Sponsored” label strongly suppresses target evaluation relative
to “Promoted” in both models (Table 8; Table 9; Fig. W4). Under consumer delegation without platform
attribution, switching from “Promoted” to “Sponsored” reduces Gemini 3.1 Pro’s target choice share from
28.8%to0 .8%(βdisclosure =−5.640,SE = 0.554,p<. 001) and reduces Kev 9B’s calibrated target probability
from47.26%to40.42%(β disclosure =−0.328,SE= 0.015,z=−21.60,p<.001).
— insert Fig. 4 about here —
Supporting our second prediction, platform attribution amplifies sponsorship bias in both models (Fig. 4;
Table 9). In Gemini 3.1 Pro, appending “by the platform” increases the sponsorship bias from+10.8
percentage points (39.6%vs.28 .8%) to+39.6points (74.2%vs.34 .6%) under “Promoted,” and from+0.6
points (1.4%vs.0 .8%) to+17.6points (21.2%vs.3 .6%) under “Sponsored.” The Principal× Attribution
interaction is positive and significant under both “Promoted” (β = 2.344, SE = 0.285, z = 8.24, p<. 001)
and “Sponsored” (β= 2.276,SE= 0.735,z= 3.10,p=.002).
Kev 9B exhibits the same pattern in calibrated probabilities (Table 8; Table 9; Fig. 4). Appending “by the
platform” increases the sponsorship bias from+2.82percentage points (50.08%vs.47 .26%) to+9.85points
(53.54%vs.43 .70%) under “Promoted,” and from+1.48points (41.89%vs.40 .42%) to+8.43points (48.96%
vs.40 .53%) under “Sponsored.” The Principal× Attribution interaction is positive and significant under
9

both “Promoted” (β = 0.357, SE = 0.012, z = 29.38, p<. 001) and “Sponsored” (β = 0.342, SE = 0.012,
z= 28.03,p<.001).
Finally, regarding our third prediction, stricter disclosure wording (“Sponsored” rather than “Promoted”) does
not eliminate the attribution-driven sponsorship bias. The three-way Principal× Disclosure× Attribution
interaction is not significant in either Gemini 3.1 Pro (β =−0.068, SE = 0.783, p = .930) or Kev 9B
(β=−0.015,SE= 0.009,z=−1.65,p=.099).
— insert Table 9 about here —
Conclusions
This research examined whether an AI shopping agent’s evaluation of sponsored listings depends on who
delegates the agent (i.e., a retail platform vs. a consumer). Across three studies, a consumer-delegated AI
agent strongly penalized sponsored listings relative to equivalent organic alternatives (H1), whereas platform
delegation significantly attenuated this penalty (H2), replicated across generative LLMs from three providers,
three model generations, alternative system-prompt wordings, and low vs. high reasoning effort, and was
eliminated by adding a single sentence naming the consumer as the beneficiary. In Study 1, this attenuation
was associated with lower pre-choice skepticism triggered by the disclosure (H3 and H4).
Study 2 showed that the sponsorship penalty and its attenuation under platform delegation replicate across
six non-generative System-One decision models that score options in a single forward pass without text
generation. It showed that consumer-aligned fine-tuning of Kev 9B across non-hotel retail categories can
eliminate the sponsorship bias zero-shot on hotel choices.
Decomposing the disclosure label in Study 3 across both Gemini 3.1 Pro and Kev 9B showed that while
the explicit term “Sponsored” reduced paid-listing evaluation relative to “Promoted” for both principals,
attributing the placement to the platform amplified the sponsorship bias under both labels.
Theoretical implications
This research contributes to the retailing and AI-mediated commerce literature by showing that the party
who deploys the AI shopping assistant can shape how it evaluates retail media placements. Prior work
on multi-stakeholder recommendation engines assumes that the weight given to consumers, platforms, and
advertisers is set through an explicit objective function (Abdollahpouri et al., 2020), while recent studies of
LLM shopping agents either hold the user role fixed (Allouah et al., 2026) or test explicit instructions to favor
sponsored brands (Wu et al., 2026). We show that across both generative LLMs and non-generative decision
models, stakeholder weighting can be set implicitly by role specification alone. Simply naming the booking
platform as the employing principal caused the AI agents to relax their discount on sponsored listings relative
to both a consumer-delegated and a role-neutral baseline, even in single-forward-pass decision models that
produce no chain of thought.
Second, our findings extend research on sponsorship disclosure and persuasion knowledge into agent-mediated
retailing (Boerman et al., 2017; Friestad and Wright, 1994; Liu et al., 2025). Whereas human disclosure
research studies how shoppers recognize and discount paid placements (Kim et al., 2019; Sahni and Nair,
2020), agentic commerce shifts disclosure processing to an AI intermediary. We show that an interaction
between task-level role assignment (i.e., the AI agent’s principal) and listing-level source attribution (platform-
attributed sponsorship) governs both the skepticism expressed by generative LLMs and the calibrated log-odds
assigned by decision models.
Managerial and policy implications
For omnichannel retailers and online marketplaces (Jindal et al., 2021) that monetize through retail media
networks while deploying AI shopping assistants (Thomas et al., 2025; Chakraborty et al., 2024), system-
instruction and model-alignment design are critical governance decisions. Even when a retailer gives no
instruction to favor paying advertisers, naming the platform as the assistant’s employer in the system prompt
10

can cause both generative chatbots and non-generative decision models to steer shoppers toward sponsored
listings they would otherwise avoid, risking perceived betrayal and loss of consumer trust (Saenger et al.,
2024; Du and Xie, 2021).
Our findings offer two complementary remedies: retailers can explicitly instruct the assistant in the system
prompt to act in the consumer’s best interest (prompt-level mitigation), and model developers can apply
consumer-aligned fine-tuning during post-training (model-level mitigation) so that platform-delegated de-
ployments preserve consumer-aligned evaluation even when the system state names the employing platform.
Meanwhile, consumers who rely on off-the-shelf AI agents deployed on their own behalf receive substantially
stronger protection against paid placements than those who rely on unmitigated platform-provided assistants.
For policymakers, our findings show that traditional disclosure mandates (European Parliament and Council
of the European Union, 2022; Federal Trade Commission, 2013) do not by themselves protect consumers when
an AI agent intermediates choice. Mandating stricter terminology (“Sponsored” rather than “Promoted”)
lowered overall evaluation of paid listings in Study 3 across both Gemini 3.1 Pro and Kev 9B, but it did
not eliminate the sponsorship bias when the placement was attributed to the platform. Oversight of retail
AI assistants must therefore complement ad-labeling rules with prompt- and model-level audits that verify
consistent evaluation across consumer and platform roles.
Limitations and future research
This research has several limitations. First, our primary evaluation benchmarks focused on hotel booking.
Future work could test zero-shot and fine-tuned evaluation across broader service contexts, such as grocery
retail or financial advice. Second, while we benchmarked delegated agents against a role-neutral baseline,
future research could compare these algorithmic penalties against human choices in identical retail interfaces
(Stoeber et al., 2026). Third, our experiments held review valence constant using matched text, whereas retail
recommenders in practice parse user-generated reviews that may vary in persuasiveness or reflect financial
incentives (Golmohammadi et al., 2020; Ravula et al., 2023; Luca and Zervas, 2016; Wadi et al., 2026).
Fourth, from a computational standpoint, model deference to the employer named in the system prompt may
partly reflect instruction-hierarchy training designed to prioritize system-level context (Wallace et al., 2024).
This does not alter our substantive implications because system instructions are how platforms configure
deployed assistants in practice. Finally, while pre-choice reasoning traces in Study 1 do not provide direct
evidence of internal neural activations (Chen et al., 2025), Study 2 demonstrates that the sponsorship bias
replicates in single-forward-pass decision models without text generation, hence skepticism in the reasoning
traces provides a diagnostic process signal of how role assignment shifts pre-choice evaluation (H3 and H4).
References
Himan Abdollahpouri, Gediminas Adomavicius, Robin Burke, Ido Guy, Dietmar Jannach, Toshihiro
Kamishima, Jan Krasnodebski, and Luiz Pizzato. Multistakeholder recommendation: Survey and re-
search directions: H. abdollahpouri et al.User Modeling and User-Adapted Interaction, 30(1):127–158,
2020.
Kusum L. Ailawadi, J.P. Beauchamp, Naveen Donthu, Dinesh K. Gauri, and Venkatesh Shankar. Com-
munication and promotion decisions in retailing: A review and directions for future research.Journal
of Retailing, 85(1):42–55, March 2009. ISSN 0022-4359. doi: 10.1016/j.jretai.2008.11.002. URL
http://dx.doi.org/10.1016/j.jretai.2008.11.002.
Amine Allouah, Omar Besbes, Josué D Figueroa, Yash Kanoria, and Akshit Kumar. What is your ai
agent buying? evaluation, biases, model dependence, & emerging implications of agentic e-commerce. In
Proceedings of the ACM Web Conference 2026, pages 8697–8700, 2026.
Amazon. Meet alexa for shopping, your personalized, agentic ai assistant on amazon. https://www.abouta
mazon.com/news/retail/alexa-for-shopping-ai-assistant, May 2026.
11

Anthropic. Model deprecations: API parameter deprecations, 2026. URL https://platform.claude.com/docs
/en/about-claude/model-deprecations#api-parameter-deprecations.
Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David Wingate.
Out of one, many: Using language models to simulate human samples.Political Analysis, 31(3):337–351,
2023.
Navid Bahmani, Amit Bhatnagar, and Dinesh Gauri. Hey, alexa! what attributes of skills affect firm
value?Journal of the Academy of Marketing Science, 50(6):1219–1235, March 2022. ISSN 1552-7824. doi:
10.1007/s11747-022-00851-0. URL http://dx.doi.org/10.1007/s11747-022-00851-0.
Stefanos Balaskas. From recommendations to delegation: A systematic review mapping agentic ai in
e-commerce and its consumer effects.Inf., 17(3):222, 2026.
Enrique Bigne, Aline Simonetti, Carla Ruiz, and Shobhit Kakaria. How online advertising competes with
user-generated content in tripadvisor. a neuroscientific approach.Journal of Business Research, 123:
279–288, 2021. doi: 10.1016/j.jbusres.2020.10.010.
Sophie C Boerman, Eva A Van Reijmersdal, and Peter C Neijens. Sponsorship disclosure: Effects of duration
on persuasion knowledge and brand responses.Journal of Communication, 62(6):1047–1064, 2012.
Sophie C Boerman, Lotte M Willemsen, and Eva P Van Der Aa. “this post is sponsored” effects of sponsorship
disclosure on persuasion knowledge and electronic word of mouth in the context of facebook.Journal of
interactive marketing, 38(1):82–92, 2017.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T Kalai. Man is to computer
programmer as woman is to homemaker? debiasing word embeddings.Advances in neural information
processing systems, 29, 2016.
Fengyan Cai, Rajesh Bagchi, and Dinesh K. Gauri. Boomerang effects of low price discounts: How low price
discounts affect purchase propensity.Journal of Consumer Research, 42(5):804–816, October 2016. ISSN
0093-5301. doi: 10.1093/jcr/ucv057. URL http://dx.doi.org/10.1093/jcr/ucv057.
Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. Semantics derived automatically from language
corpora contain human-like biases.Science, 356(6334):183–186, 2017.
Margaret C Campbell and Amna Kirmani. Consumers’ use of persuasion knowledge: The effects of accessibility
and cognitive capacity on perceptions of an influence agent.Journal of consumer research, 27(1):69–83,
2000.
Debarun Chakraborty, Arpan Kumar Kar, Smruti Patre, and Shivam Gupta. Enhancing trust in online
grocery shopping through generative AI chatbots.Journal of Business Research, 180:114737, 2024. doi:
10.1016/j.jbusres.2024.114737.
Yanda Chen, Joe Benton, Ansh Radhakrishnan, Jonathan Uesato, Carson Denison, John Schulman, Arushi
Somani, Peter Hase, Misha Wagner, Fabien Roger, et al. Reasoning models don’t always say what they
think.arXiv preprint arXiv:2505.05410, 2025.
Ameet Deshpande, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, and Karthik Narasimhan. Toxicity
in chatgpt: Analyzing persona-assigned language models. InFindings of the association for computational
linguistics: EMNLP 2023, pages 1236–1270, 2023.
Shuili Du and Chunyan Xie. Paradoxes of artificial intelligence in consumer markets: Ethical challenges and
opportunities.Journal of Business Research, 129:961–974, 2021. doi: 10.1016/j.jbusres.2020.08.024.
European Parliament and Council of the European Union. Regulation (EU) 2022/2065 of the European
Parliament and of the Council of 19 October 2022 on a Single Market For Digital Services and amending
Directive 2000/31/EC (Digital Services Act). Official Journal of the European Union, L 277, 27.10.2022,
pp. 1–102, 2022. URL http://data.europa.eu/eli/reg/2022/2065/oj.
12

Nathaniel J Evans and Dooyeon Park. Rethinking the persuasion knowledge model: Schematic antecedents
and associative outcomes of persuasion knowledge activation for covert advertising.Journal of Current
Issues & Research in Advertising, 36(2):157–176, 2015.
Federal Trade Commission. Updated search engine advertising guidance: Letter from Mary K. Engle,
Associate Director for Advertising Practices, to general-purpose and specialized search engines. Published
2013-06-24, 2013. URL https://www.ftc.gov/sites/default/files/attachments/press-releases/ftc-consumer-
protection-staff-updates-agencys-guidance-search-engine-industryon-need-distinguish/130625searchengi
nespecializedletter.pdf.
Marian Friestad and Peter Wright. The persuasion knowledge model: How people cope with persuasion
attempts.Journal of consumer research, 21(1):1–31, 1994.
Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and James Zou. Word embeddings quantify 100 years of
gender and ethnic stereotypes.Proceedings of the National Academy of Sciences, 115(16):E3635–E3644,
2018.
Dinesh K. Gauri, Rupinder P. Jindal, Brian Ratchford, Edward Fox, Amit Bhatnagar, Aashish Pandey,
Jonathan R. Navallo, John Fogarty, Stephen Carr, and Eric Howerton. Evolution of retail formats: Past,
present, and future.Journal of Retailing, 97(1):42–61, March 2021. ISSN 0022-4359. doi: 10.1016/j.jretai.2
020.11.002. URL http://dx.doi.org/10.1016/j.jretai.2020.11.002.
Alireza Golmohammadi, Anna S. Mattila, and Dinesh K. Gauri. Negative online reviews and consumers’
service consumption.Journal of Business Research, 116:27–36, August 2020. ISSN 0148-2963. doi:
10.1016/j.jbusres.2020.05.004. URL http://dx.doi.org/10.1016/j.jbusres.2020.05.004.
Google. Gemini models: Sampling parameter deprecation, 2026. URL https://ai.google.dev/gemini-
api/docs/latest-model#sampling-parameter-deprecation.
Google DeepMind. Project mariner, 2026. URL https://deepmind.google/models/project-mariner/.
Dhruv Grewal, Kusum L. Ailawadi, Dinesh Gauri, Kevin Hall, Praveen Kopalle, and Jane R. Robertson.
Innovations in retail pricing and promotions.Journal of Retailing, 87:S43–S52, 2011. ISSN 0022-4359. doi:
10.1016/j.jretai.2011.04.008. URL http://dx.doi.org/10.1016/j.jretai.2011.04.008.
Dhruv Grewal, Dinesh K. Gauri, Gopal Das, James Agarwal, and Mark T. Spence. Retailing and emergent
technologies.Journal of Business Research, 134:198–202, 2021. ISSN 0148-2963. doi: 10.1016/j.jbusres.20
21.05.004. URL http://dx.doi.org/10.1016/j.jbusres.2021.05.004.
Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen,
Shengjie Ma, Honghao Liu, et al. A survey on llm-as-a-judge.The Innovation, 7(6), 2026.
Thilo Hagendorff, Ishita Dasgupta, Marcel Binz, Stephanie CY Chan, Andrew Lampinen, Jane X Wang,
Zeynep Akata, and Eric Schulz. Machine psychology.arXiv preprint arXiv:2303.13988, 2023.
Andrei Hagiu and Bruno Jullien. Why do intermediaries divert search?The RAND Journal of Economics,
42(2):337–362, 2011.
Marc Hasselwander, Varsolo Sunio, Oliver Lah, and Emmanuel Mogaji. Toward agentic ai: User acceptance
of a deeply personalized ai super assistant (aisa).Journal of Retailing and Consumer Services, 89:104620,
2026.
Andrew F Hayes.Introduction to mediation, moderation, and conditional process analysis: A regression-based
approach. Guilford publications, 2017.
Erik Hermann and Stefano Puntoni. Artificial intelligence and consumer behavior: From predictive to
generative AI.Journal of Business Research, 180:114720, 2024. doi: 10.1016/j.jbusres.2024.114720.
Ari Holtzman, Jan Buys, Li Du, Maxwell Forbes, and Yejin Choi. The curious case of neural text degeneration.
arXiv preprint arXiv:1904.09751, 2019.
13

Roman Inderst and Marco Ottaviani. Competition through commissions and kickbacks.American Economic
Review, 102(2):780–809, 2012.
Rupinder P. Jindal, Dinesh K. Gauri, Wanyu Li, and Yu Ma. Omnichannel battle between amazon and walmart:
Is the focus on delivery the best strategy?Journal of Business Research, 122:270–280, January 2021. ISSN
0148-2963. doi: 10.1016/j.jbusres.2020.08.053. URL http://dx.doi.org/10.1016/j.jbusres.2020.08.053.
Bohyeon Kang and Rupinder P. Jindal. Opportunism in buyer–seller relationships: Some unexplored
antecedents.Journal of Business Research, 68(3):735–742, March 2015. ISSN 0148-2963. doi: 10.1016/j.jb
usres.2014.07.009. URL http://dx.doi.org/10.1016/j.jbusres.2014.07.009.
Do Yuon Kim and Hye-Young Kim. Influencer advertising on social media: The multiple inference model
on influencer-product congruence and sponsorship disclosure.Journal of Business Research, 130:405–415,
2021. doi: 10.1016/j.jbusres.2020.02.020.
Su Jung Kim, Ewa Maslowska, and Ali Tamaddoni. The paradox of (dis) trust in sponsorship disclosure: The
characteristics and effects of sponsored online consumer reviews.Decision Support Systems, 116:114–124,
2019.
V Kumar, Philip Kotler, and Ajay Kumar. Transformative marketing strategies in the era of new-age
technologies: Principles, plan, purpose, and practice.Journal of the Academy of Marketing Science, 54(1):
1–27, 2026.
Lidija Lalicic and Christian Weismayer. Consumers’ reasons and perceived value co-creation of using
artificial intelligence-enabled travel service agents.Journal of Business Research, 129:891–901, 2021. doi:
10.1016/j.jbusres.2020.11.005.
Dewen Liu, Haoding Wang, and Youping Zhu. You plan to manipulate me: A persuasion knowledge
perspective for understanding the effects of AI-assisted selling.Journal of Business Research, 200:115598,
2025. doi: 10.1016/j.jbusres.2025.115598.
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. Lost in the middle: How language models use long contexts.Transactions of the association for
computational linguistics, 12:157–173, 2024.
George Loewenstein, Daylian M Cain, and Sunita Sah. The limits of transparency: Pitfalls and potential of
disclosing conflicts of interest.American Economic Review, 101(3):423–428, 2011.
Michael Luca and Georgios Zervas. Fake it till you make it: Reputation, competition, and yelp review fraud.
Management science, 62(12):3412–3427, 2016.
Meta. Introducing Muse: The world’s first personal AI agent built for everyone. https://about.fb.com/news/
2026/09/introducing-muse-personal-ai-agent/, September 2026.
Emmanuel Mogaji and Varsha Jain. How generative ai is (will) change consumer behaviour: Postulating the
potential impact and implications for research, practice, and policy.Journal of consumer behaviour, 23(5):
2379–2389, 2024.
Aidin Namin, Rupinder P. Jindal, Dinesh K. Gauri, Brian T. Ratchford, and Seth C. Ketron. Consumers’
acceptance of in-store technologies through the lens of segmentation.Journal of Business Research, 207:
116010, April 2026. ISSN 0148-2963. doi: 10.1016/j.jbusres.2026.116010. URL http://dx.doi.org/10.1016/j
.jbusres.2026.116010.
Carl Obermiller and Eric R Spangenberg. Development of a scale to measure consumer skepticism toward
advertising.Journal of consumer psychology, 7(2):159–186, 1998.
OpenAI. Advertise in ChatGPT. https://ads.openai.com/, 2026. Accessed: July 27, 2026.
JaredPalmer. Kev-4b: acalibrateddecisionmodelonqwen3.5-4b. https://huggingface.co/jaredpalmer/kev-4b,
2026. Kev 1.0.
14

Vivek Pandya. Generative AI-powered shopping rises with traffic to U.S. retail sites up 4,700%, 2025. URL
https://business.adobe.com/blog/generative-ai-powered-shopping-rises-with-traffic-to-retail-sites.
Arjun Panickssery, Samuel R Bowman, and Shi Feng. Llm evaluators recognize and favor their own generations.
Advances in Neural Information Processing Systems, 37:68772–68802, 2024.
Ethan Perez, Sam Ringer, Kamile Lukosiute, Karina Nguyen, Edwin Chen, Scott Heiner, Craig Pettit,
Catherine Olsson, Sandipan Kundu, Saurav Kadavath, et al. Discovering language model behaviors with
model-written evaluations. InFindings of the association for computational linguistics: ACL 2023, pages
13387–13434, 2023.
Pouya Pezeshkpour and Estevam Hruschka. Large language models sensitivity to the order of options in
multiple-choice questions. InFindings of the Association for Computational Linguistics: NAACL 2024,
pages 2006–2017, 2024.
Brian Ratchford, Gonca Soysal, Alejandro Zentner, and Dinesh K. Gauri. Online and offline retailing:
What we know and directions for future research.Journal of Retailing, 98(1):152–177, March 2022. ISSN
0022-4359. doi: 10.1016/j.jretai.2022.02.007. URL http://dx.doi.org/10.1016/j.jretai.2022.02.007.
Prashanth Ravula, Amit Bhatnagar, and Dinesh K Gauri. Role of gender in the creation and persuasiveness
of online reviews.Journal of Business Research, 154:113386, January 2023. ISSN 0148-2963. doi:
10.1016/j.jbusres.2022.113386. URL http://dx.doi.org/10.1016/j.jbusres.2022.113386.
Christian P Robert, George Casella, and George Casella.Monte Carlo statistical methods, volume 2. Springer,
1999.
Lior Rokach and Francesco Ricci. Introduction to recommender systems handbook.Recommender Systems
Handbook, 2011.
Christina Saenger, Christina A. Kuchmaner, and Patrick J. Bateman. Betrayed by AI: How perceived
betrayal by a virtual assistant affects consumers’ purchase intentions for recommended products.Journal
of Business Research, 185:114940, 2024. doi: 10.1016/j.jbusres.2024.114940.
Navdeep S Sahni and Harikesh S Nair. Sponsorship disclosure and consumer deception: Experimental
evidence from native advertising in mobile search.Marketing Science, 39(1):5–32, 2020.
Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto. Whose
opinions do language models reflect? InInternational conference on machine learning, pages 29971–30004.
PMLR, 2023.
Murray Shanahan, Kyle McDonell, and Laria Reynolds. Role play with large language models.Nature, 623
(7987):493–498, 2023.
Mrinank Sharma, Meg Tong, Tomek Korbak, David Duvenaud, Amanda Askell, Sam Bowman, Esin Durmus,
Zac Hatfield-Dodds, Scott Johnston, Shauna Kravec, et al. Towards understanding sycophancy in language
models. InInternational Conference on Learning Representations, volume 2024, pages 110–144, 2024.
Sri Vishnu Srinivasa Raja, Davide C. Orazi, Yimin Cheng, and Alex Belli. A meta-analysis of the effects of
AI agent implementation on customer-level outcomes.Journal of Business Research, 210:116172, 2026. doi:
10.1016/j.jbusres.2026.116172.
Timo Stoeber, Jonas Hammerschmidt, Alexander Lundervold, Endrit Kromidha, Dominik K. Kanbach, and
Sascha Kraus. AI strategy under institutional pressure: Strategic conformity and decision-making in large
language models.Journal of Business Research, 212:116227, 2026. doi: 10.1016/j.jbusres.2026.116227.
Wangsuk Suh and Stephen A. Atlas. Time and risk preferences among generative AI systems.Journal of
Business Research, 217:116274, 2026. doi: 10.1016/j.jbusres.2026.116274.
Rodney Thomas, Stephanie Thomas, Molly Rapert, Brent Williams, and Andy Murray. Retail media
networks: definition, development, and differentiation.Journal of Business Research, 200:115656, 2025.
doi: 10.1016/j.jbusres.2025.115656.
15

Davood Wadi and Marc Fredette. A monte-carlo sampling framework for reliable evaluation of large language
models using behavioral analysis.Findings of the Association for Computational Linguistics: EMNLP
2025, pages 9414–9432, 2025.
Davood Wadi and Yu Ma. Does rank still matter? position bias when ai agents shop on our behalf.arXiv
preprint arXiv:2608.22697, 2026a.
Davood Wadi and Yu Ma. Shopping by algorithm: How agentic ai deploys human heuristics as a surrogate
consumer. 2026b.
Davood Wadi, Marc Fredette, Sylvain Senecal, and Renaud Legoux. Be careful what you pay for: the effect of
performance contingent incentives on online product reviews.Journal of Research in Interactive Marketing,
pages 1–25, 2026.
Eric Wallace, Kai Xiao, Reimar Leike, Lilian Weng, Johannes Heidecke, and Alex Beutel. The instruction
hierarchy: Training llms to prioritize privileged instructions.arXiv preprint arXiv:2404.13208, 2024.
Walmart. Walmart is building a genai-powered shopping assistant. https://tech.walmart.com/content/walma
rt-global-tech/en_us/blog/post/walmart-is-building-a-genai-powered-shopping-assistant.html, June 2024.
Peiyi Wang, Lei Li, Liang Chen, Zefan Cai, Dawei Zhu, Binghuai Lin, Yunbo Cao, Lingpeng Kong, Qi Liu,
Tianyu Liu, et al. Large language models are not fair evaluators. InProceedings of the 62nd annual meeting
of the association for computational linguistics (volume 1: Long papers), pages 9440–9450, 2024.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, and
Denny Zhou. Self-consistency improves chain of thought reasoning in language models.arXiv preprint
arXiv:2203.11171, 2022.
Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian Borgeaud, Dani Yogatama,
Maarten Bosma, Denny Zhou, Donald Metzler, et al. Emergent abilities of large language models.arXiv
preprint arXiv:2206.07682, 2022.
Addison J Wu, Ryan Liu, Shuyue Stella Li, Yulia Tsvetkov, and Thomas L Griffiths. Ads in ai chatbots? an
analysis of how large language models navigate conflicts of interest.arXiv preprint arXiv:2604.08525, 2026.
Haonan Yin, Shai Vardi, and Vidyanand Choudhary. Fragile preferences: A deep dive into order effects in
large language models.PNAS nexus, 5(8):pgag246, 2026.
Junhui Zhang, M. S. Balaji, Jun Luo, and Subhash Jha. Effectiveness of product recommendation framing on
online retail platforms.Journal of Business Research, 153:185–197, 2022. doi: 10.1016/j.jbusres.2022.08.006.
16

Fig.1Conceptual framework
Note.The sponsorship tag reduces target choice (H1), an effect attenuated under platform delegation (H2).
The penalty operates through the agent’s skepticism (H3), and the assigned principal moderates the first
stage of this pathway (H4), weakening the skepticism the sponsorship disclosure is designed to trigger.
Fig.2Target Choice Shares by Principal and Sponsorship - Gemini 3.1 Pro (Study 1 main), GPT 5.6 Terra,
Claude Sonnet 5, Gemini 3.5 Flash, Gemini 3.6 Flash, and Gemini 3.8 Flash (Cross-LLM generalizability).
Note.Share of replications in which the AI agent selected the target hotel, by sponsorship condition and
delegating principal (main: Table 3; robustness: Table W3). The dashed horizontal line marks the 50% choice
share expected for organic listings.
Note.Mean calibrated probability assigned to the target hotel across the 360 position-balanced Latin-square
stimuli per cell, by sponsorship condition and delegating principal (Table W7). Error bars represent 95%
confidence intervals.
Note.Mean difference between platform and consumer delegation (in percentage points) in target choice
share for Gemini 3.1 Pro (N = 500pairs per label) and calibrated target probability for Kev 9B (N = 360
paired stimuli per label; Table 8). Error bars represent 95% confidence intervals.
17

Fig.3Calibrated target choice probabilities (%) by principal and sponsorship across decision models (Study
2).
Fig.4Difference in target evaluation between platform and consumer delegation (in percentage points) across
disclosure types and platform attribution - Gemini 3.1 Pro and Kev 9B (Study 3).
18

Table1System prompts manipulating the principal in Study 1
Variant Consumer delegation Platform delegation
Main experiment You have been employed by atravelerto
recommend hotels. Which hotel would youbook?
You have been employed by ahotel booking
platformto recommend hotels. Which hotel
would youbook?
Principal noun You have been employed by acustomerto
recommend hotels. Which hotel would youbook?
You have been employed by anonline travel
agencyto recommend hotels. Which hotel would
youbook?
Action verb You have been employed by atravelerto
recommend hotels. Which hotel would you
recommend?
You have been employed by ahotel booking
platformto recommend hotels. Which hotel
would yourecommend?
Note.Each variant was evaluated in a 2 (Sponsorship)× 2 (Principal) design on Gemini 3.1 Pro (N = 500
replications per cell).
Table2Logistic regression on target choice - Gemini 3.1 Pro (main experiment, system-prompt wording
variants, and thinking level)
Term Main experiment Principal noun Recommend Thinking level
Principal (platform)−0.165 (0.198)−0.352 (0.210) 0.076 (0.190)−0.163 (0.190)
Sponsorship (sponsored)−6.491*** (0.418)−6.703*** (0.423)−5.074*** (0.325)−6.059*** (0.365)
Principal×Sponsorship 3.989*** (0.428) 2.503*** (0.406) 4.592*** (0.366) 3.719*** (0.401)
Thinking level (LOW) — — —−0.254 (0.190)
Principal×Thinking level — — — 0.406 (0.270)
Sponsorship×Thinking level — — — 0.741 (0.433)
Principal×Sponsorship×Thinking
level
— — —−0.842 (0.518)
Standardized target price 0.039 (0.079) 0.124 (0.089) 0.089 (0.074) 0.024 (0.054)
PseudoR 2 0.600 0.628 0.535 0.566
Log-Likelihood−512.17−451.54−617.04−1104.56
Contrasts
Sponsorship effect, consumer (HIGH)−6.491*** (0.418)−6.703*** (0.423)−5.074*** (0.325)−6.059*** (0.365)
Sponsorship effect, platform (HIGH)−2.502*** (0.229)−4.199*** (0.300)−0.482** (0.187)−2.340*** (0.209)
Sponsorship effect, consumer (LOW)— — —−5.318*** (0.307)
Sponsorship effect, platform (LOW)— — —−2.441*** (0.210)
Principal×Sponsorship (LOW)— — — 2.877*** (0.348)
Note.Standard errors in parentheses. Reference categories: consumer delegation, organic target, and HIGH
thinking level (N = 2,000for Main, Principal noun, and Recommend;N = 4,000for Thinking level). Models
include target/competitor review and hotel fixed effects (Table W11, Table W20, Table W21, and Table
W22). *p < .05. **p < .01. ***p < .001.
Table3Target choice by principal specification - Gemini 3.1 Pro (Study 1)
Condition Organic Sponsored Sponsorship penalty (pp)
Role-neutral 248 (49.6%) 39 (7.8%) 41.8
Consumer 265 (53.0%) 14 (2.8%) 50.2
Platform 271 (54.2%) 125 (25.0%) 29.2
Platform with consumer beneficiary 257 (51.4%) 16 (3.2%) 48.2
Note. N = 500replications per cell (N = 4,000total). Dominated alternatives were never chosen. System
prompts:Role-neutral(“You have been employed to recommend hotels. Which hotel would you book?”);
Platform with consumer beneficiary(“You have been employed by a hotel booking platform to recommend
hotels. Act in the traveler’s best interest. Which hotel would you book?”).
19

Table4Moderated mediation analysis of sponsorship on target choice via skepticism - Gemini 3.1 Pro (Study
1)
Skepticism (M) Target choice (Y)
Principal (platform)−0.007 (0.081)−0.289 (0.249)
Sponsorship (sponsored) 4.827*** (0.081)−1.283* (0.603)
Principal×Sponsorship−1.361*** (0.114) 2.859*** (0.586)
Skepticism —−1.670*** (0.121)
Standardized target price 0.003 (0.029) 0.037 (0.107)
R2 / pseudoR 2 0.751 0.760
Conditional effects of sponsorship
Consumer delegation4.827*** (0.081)−1.283* (0.603)
Platform delegation3.466*** (0.081) 1.576*** (0.389)
Conditional indirect effects and index Effect (BootSE) 95% CI
Consumer delegation−8.061 (0.846) [−10.636,−7.309]
Platform delegation−5.788 (0.624) [−7.660,−5.202]
Index of moderated mediation2.273 (0.318) [1.916, 3.135]
Note. N = 2,000. PROCESS Model 8 (Hayes, 2017); unstandardized coefficients with standard errors in
parentheses. Skepticism (M) is estimated by OLS; target choice (Y) by logistic regression (log-odds). Both
equations include target/competitor hotel and review fixed effects (Table W13 and Table W14). Indirect
effects and the index of moderated mediation use 10,000 percentile bootstrap resamples. *p < .05. **p < .01.
***p < .001.
Table5Logistic regression on target choice - cross-LLM generalizability
GPT 5.6 Terra
Claude Sonnet
5
Gemini 3.5
Flash
Gemini 3.6
Flash
Gemini 3.8
Flash
Principal (platform)−0.345 (0.177) 0.097 (0.157) 0.008 (0.200)−0.011 (0.221)−0.119 (0.219)
Sponsorship (sponsored)−2.238***
(0.203)
−3.243***
(0.217)
−1.824***
(0.217)
−0.917***
(0.226)
−5.836***
(0.376)
Principal×Sponsorship 0.708** (0.264) 1.759***
(0.262)
0.975***
(0.285)
1.124***
(0.318)
5.243***
(0.428)
Standardized target price−0.021 (0.066)−0.025 (0.062) 0.110 (0.072)−0.109 (0.081)−0.051 (0.087)
PseudoR 2 0.443 0.348 0.519 0.610 0.643
Log-Likelihood−748.58−845.00−661.59−540.43−479.44
Contrasts
Sponsorship effect under consumer
delegation
−2.238***
(0.203)
−3.243***
(0.217)
−1.824***
(0.217)
−0.917***
(0.226)
−5.836***
(0.376)
Sponsorship effect under platform
delegation
−1.530***
(0.189)
−1.483***
(0.170)
−0.849***
(0.195)
0.207 (0.222)−0.593**
(0.225)
Note.Standard errors in parentheses ( N = 2,000per LLM; N = 10,000total). Models include tar-
get/competitor review and hotel fixed effects (Table W15 to Table W19). *p < .05. **p < .01. ***p <
.001.
Table6Paired stimulus fixed-effects regression on exact log-odds of target choice across decision models
(Study 2)
Kev 9B Jev 1.14 Liquid D1-Ultra Mercury Decide
Microsoft
Decision 1 StartLux 27B
Principal
(platform)
−0.003 (0.013)−0.026 (0.022) 0.004 (0.015)−0.012 (0.012) 0.007 (0.013)−0.003 (0.010)
Sponsorship
(sponsored)
−0.123***
(0.012)
−2.357***
(0.064)
−1.760***
(0.036)
−3.379***
(0.073)
−0.729***
(0.026)
−1.307***
(0.037)
Principal×
Sponsorship
0.194***
(0.012)
0.641***
(0.040)
0.104***
(0.031)
0.121** (0.046) 0.111***
(0.014)
0.108***
(0.025)
R2 0.957 0.891 0.927 0.896 0.946 0.906
AdjustedR 2 0.943 0.854 0.903 0.861 0.928 0.875
Contrasts
20

Kev 9B Jev 1.14 Liquid D1-Ultra Mercury Decide
Microsoft
Decision 1 StartLux 27B
Sponsorship
effect under
consumer
delegation
−0.123***
(0.012)
−2.357***
(0.064)
−1.760***
(0.036)
−3.379***
(0.073)
−0.729***
(0.026)
−1.307***
(0.037)
Sponsorship
effect under
platform
delegation
0.071***
(0.014)
−1.716***
(0.068)
−1.656***
(0.034)
−3.258***
(0.074)
−0.617***
(0.023)
−1.199***
(0.030)
Note.OLS regressions on exact log-odds ln(Ptarget/Pcompetitor)with 360 paired stimulus fixed effects
(N = 1,440per model; N = 8,640total). Stimulus-clustered standard errors (360 clusters) in parentheses.
Reference categories: consumer delegation and organic target. *p < .05. **p < .01. ***p < .001.
Table7Zero-shot evaluation on Study 2 hotel benchmark before and after consumer-aligned fine-tuning -
Kev 9B (Study 2)
Kev 9B (base) Kev 9B (fine-tuned)
Principal (platform)−0.003 (0.013)−0.002 (0.009)
Sponsorship (sponsored)−0.123*** (0.012)−0.109*** (0.011)
Principal×Sponsorship 0.194*** (0.012)−0.009 (0.006)
Sponsorship effect under consumer
delegation
−0.123*** (0.012)−0.109*** (0.011)
Sponsorship effect under platform
delegation
0.071*** (0.014)−0.118*** (0.011)
P(Target)
Consumer, organic 43.43% 43.23%
Consumer, sponsored 40.60% 40.74%
Consumer sponsorship penalty
(pp)
2.83 2.49
Platform, organic 42.62% 42.37%
Platform, sponsored 43.88% 39.68%
Platform sponsorship penalty (pp) −1.26 2.70
Note.Evaluated on the 360 paired Study 2 hotel Latin-square stimuli (N = 1,440observations per model).
Kev 9B (fine-tuned) was trained strictly on four synthetic non-hotel retail categories (N = 2,880) and selected
at minimum validation KL divergence (0.0030bits vs.0 .0195bits pre-training, step 440) on a held-out retail
category (air purifiers,N = 720), with zero exposure to hotel stimuli. Stimulus-clustered standard errors
(360 clusters) in parentheses. *p < .05. **p < .01. ***p < .001.
Table8Target choice share (Gemini 3.1 Pro) and calibrated target probability (Kev 9B) across disclosure
types and platform attribution (Study 3)
Disclosure
type
Platform
attribution Disclosure label
Gemini 3.1 Pro:
Consumer
Gemini 3.1 Pro:
Platform
Kev 9B:
Consumer
P(Target)
Kev 9B:
Platform
P(Target)
Promoted No “Promoted” 144 (28.8%) 198 (39.6%) 47.26% (14.19) 50.08% (13.75)
Promoted Yes “Promoted by
the platform”
173 (34.6%) 371 (74.2%) 43.70% (13.75) 53.54% (13.32)
Sponsored No “Sponsored” 4 (0.8%) 7 (1.4%) 40.42% (12.50) 41.89% (11.81)
Sponsored Yes “Sponsored by
the platform”
18 (3.6%) 106 (21.2%) 40.53% (12.89) 48.96% (12.65)
Note.Gemini 3.1 Pro: N = 500replications per cell ( N = 4,000total), reporting target choices and
shares. Kev 9B:N = 360Latin-square stimuli per cell (N = 2,880total), reporting mean calibrated target
probabilities (SDs in parentheses).
21

Table9Regression results for disclosure type, platform attribution, and principal manipulation - Gemini 3.1
Pro and Kev 9B (Study 3)
Gemini 3.1 Pro Kev 9B
Principal (platform) 1.145*** (0.194) 0.172*** (0.011)
Disclosure (“Sponsored”)−5.640*** (0.554)−0.328*** (0.015)
Attribution (“by the platform”) 0.429* (0.190)−0.157*** (0.010)
Principal×Disclosure−0.289 (0.688)−0.074*** (0.005)
Disclosure×Attribution 1.360* (0.620) 0.160*** (0.010)
Principal×Attribution 2.344*** (0.285) 0.357*** (0.012)
Principal×Disclosure×
Attribution
−0.068 (0.783)−0.015 (0.009)
Standardized target price 0.002 (0.061) —
Contrasts
Principal×Attribution
(Promoted)
2.344*** (0.285) 0.357*** (0.012)
Principal×Attribution
(Sponsored)
2.276** (0.735) 0.342*** (0.012)
Model Fit & Controls
Stimulus fixed effects Hotel & review FEs Paired stimulus FEs (360)
N4,000 2,880
PseudoR 2 /R 2 0.585 0.933
Log-Likelihood−941.85 —
Note.Standard errors in parentheses (clustered by stimulus for Kev 9B). Reference categories: consumer
delegation, “Promoted” disclosure, and no platform attribution. Gemini 3.1 Pro includes target/competitor
hotel and review fixed effects (Table W23); Kev 9B includes 360 paired stimulus fixed effects. *p < .05. **p
< .01. ***p < .001.
22

Appendix A. Supplementary tables and figures
A.1 Study 1 - main
Table W1Alternatives used in Study 1
Alternative Featured Review Text Hotel Name Platform Sponsor Price
Target[Positive review pool] [Randomized] [Manipulated: true or false]P
Competitor[Positive review pool] [Randomized]falseP
Dominated 1[Negative review pool] [Randomized]false $450
Dominated 2[Negative review pool] [Randomized]false $400
Note. P is identical for both Target and Competitor, drawn randomly from a continuous uniform distribution
P∼U(p 5,p 95), wherep 5 = $173.45andp 95 = $351.40.
Table W2Descriptive statistics of skepticism - Gemini 3.1 Pro (Study 1)
Principal Sponsorship Mean SD
Consumer Organic 1.34 0.75
Consumer Sponsored 6.19 1.01
Platform Organic 1.31 0.75
Platform Sponsored 4.80 2.16
Note. N= 500 replications per cell. Skepticism is on a seven-point Likert scale.
Fig. W1
Note.Bars represent the 95% confidence interval. This figure presents mean judge-scored skepticism (1–7) by
sponsorship condition and delegating principal (Table W2).
A.2 Study 1 - cross-LLM generalizability
23

Table W3Choice distribution for the LLMs tested for cross-LLM generalizability experiment (Claude Sonnet
5, GPT 5.6 Terra, Gemini 3.5 Flash, Gemini 3.6 Flash, and Gemini 3.8 Flash; Study 1)
LLM Principal Sponsorship Target chosen Competitor chosenN
Claude Sonnet 5 Consumer Organic 252 (50.4%) 248 (49.6%) 500
Claude Sonnet 5 Consumer Sponsored 51 (10.2%) 449 (89.8%) 500
Claude Sonnet 5 Platform Organic 252 (50.4%) 248 (49.6%) 500
Claude Sonnet 5 Platform Sponsored 146 (29.2%) 354 (70.8%) 500
GPT 5.6 Terra Consumer Organic 268 (53.6%) 232 (46.4%) 500
GPT 5.6 Terra Consumer Sponsored 124 (24.8%) 376 (75.2%) 500
GPT 5.6 Terra Platform Organic 248 (49.6%) 252 (50.4%) 500
GPT 5.6 Terra Platform Sponsored 154 (30.8%) 346 (69.2%) 500
Gemini 3.5 Flash Consumer Organic 259 (51.8%) 241 (48.2%) 500
Gemini 3.5 Flash Consumer Sponsored 168 (33.6%) 332 (66.4%) 500
Gemini 3.5 Flash Platform Organic 257 (51.4%) 243 (48.6%) 500
Gemini 3.5 Flash Platform Sponsored 215 (43.0%) 285 (57.0%) 500
Gemini 3.6 Flash Consumer Organic 238 (47.6%) 262 (52.4%) 500
Gemini 3.6 Flash Consumer Sponsored 209 (41.8%) 291 (58.2%) 500
Gemini 3.6 Flash Platform Organic 249 (49.8%) 251 (50.2%) 500
Gemini 3.6 Flash Platform Sponsored 257 (51.4%) 243 (48.6%) 500
Gemini 3.8 Flash Consumer Organic 251 (50.2%) 249 (49.8%) 500
Gemini 3.8 Flash Consumer Sponsored 55 (11.0%) 445 (89.0%) 500
Gemini 3.8 Flash Platform Organic 262 (52.4%) 238 (47.6%) 500
Gemini 3.8 Flash Platform Sponsored 221 (44.2%) 279 (55.8%) 500
Note.Number of observations per LLM:2,000; N = 10,000total. Dominated alternatives are never selected
(0%).
Table W4Moderated mediation analysis of sponsorship on target choice via skepticism - Gemini Flash LLMs
Gemini 3.5
Flash
Gemini 3.6
Flash
Gemini 3.8
Flash
Outcome M Y M Y M Y
Sponsorship 2.813***
(0.095)
1.779***
(0.354)
1.696***
(0.092)
0.964**
(0.311)
4.496***
(0.094)
−0.498 (0.710)
Principal 0.019 (0.095)−0.042 (0.243)−0.040 (0.092)−0.032 (0.251)−0.014 (0.094)−0.355 (0.264)
Sponsorship×
Principal
−0.533***
(0.134)
0.713 (0.404)−0.572***
(0.130)
0.619 (0.406)−2.165***
(0.133)
3.784***
(0.708)
Skepticism —−1.594***
(0.102)
—−1.513***
(0.120)
—−1.701***
(0.141)
Target price
(standardized)
−0.016 (0.034) 0.140 (0.100)−0.029 (0.033)−0.084 (0.102)−0.043 (0.035)−0.239 (0.123)
R2 / pseudoR 2 0.486 0.726 0.340 0.739 0.650 0.790
Conditional
effects of
sponsorship
Consumer
delegation
2.813***
(0.095)
1.779***
(0.354)
1.696***
(0.092)
0.964**
(0.311)
4.496***
(0.094)
−0.498 (0.710)
Platform
delegation
2.280***
(0.095)
2.492***
(0.350)
1.125***
(0.092)
1.583***
(0.297)
2.331***
(0.095)
3.286***
(0.442)
Note. N = 2,000for Gemini 3.5 Flash and Gemini 3.6 Flash;N = 1,922for Gemini 3.8 Flash (78 trials with
empty reasoning traces omitted);N = 5,922total. PROCESS Model 8 (Hayes, 2017). X = sponsorship (1 =
sponsored), W = principal (1 = platform), M = skepticism, Y = target choice. M = skepticism equation
(OLS); Y = target choice equation (logistic regression, log-odds). Unstandardized coefficients with standard
errors in parentheses. Reference categories are consumer delegation and organic target. Both equations
include fixed effects for target and competitor review texts and hotel names, omitted from display. Conditional
effects under platform delegation are linear combinations of the sponsorship and interaction coefficients. For
the Y equation, these are conditionaldirecteffects, holding skepticism constant. Conditional indirect effects
are reported in Table W5.
*p < .05. **p < .01. ***p < .001.
24

Table W5Conditional indirect effects of sponsorship on target choice via skepticism - Gemini Flash LLMs
Gemini 3.5 Flash Gemini 3.6 Flash Gemini 3.8 Flash
Effect 95% CI Effect 95% CI Effect 95% CI
Consumer delegation−4.485 [−5.592,
−4.112]
−2.565 [−3.432,
−2.201]
−7.648 [−10.583,
−6.800]
Platform delegation−3.634 [−4.560,
−3.307]
−1.701 [−2.331,
−1.410]
−3.965 [−5.525,
−3.480]
Index of moderated mediation 0.850 [0.458, 1.385] 0.864 [0.508, 1.397] 3.683 [3.154, 5.223]
Note. N = 2,000for Gemini 3.5 Flash and Gemini 3.6 Flash;N = 1,922for Gemini 3.8 Flash. Indirect effects
are the products of the conditional a-paths and the b-path from Table W4, expressed in a log-odds metric.
Percentile bootstrap estimates with 10,000 resamples. Bootstrap standard errors are 0.381 / 0.319 / 0.237
(Gemini 3.5 Flash), 0.312 / 0.236 / 0.226 (Gemini 3.6 Flash), and 0.960 / 0.519 / 0.530 (Gemini 3.8 Flash)
for the consumer indirect effect, platform indirect effect, and index respectively. The index of moderated
mediation is the difference between the two conditional indirect effects; a confidence interval excluding zero
indicates that the strength of mediation depends on the delegating principal.
A.3 Study 1 - system-prompt wording and reasoning effort
Fig. W2
Table W6Choice distribution across reasoning efforts - Gemini 3.1 Pro (Study 1)
Principal Sponsorship Thinking level Target chosen N
Consumer Organic High 265 (53.0%) 500
Low 252 (50.4%) 500
Sponsored High 14 (2.8%) 500
Low 25 (5.0%) 500
Platform Organic High 271 (54.2%) 500
Low 248 (49.6%) 500
Sponsored High 125 (25.0%) 500
Low 128 (25.6%) 500
Note.Frequency with percentage in parentheses. The dominated alternatives are never chosen.
25

Fig. W3
A.4 Study 2 - decision models
Table W7Calibrated target probabilities by principal and sponsorship across decision models (Study 2)
Decision model Principal Organic P(Target) Sponsored P(Target) Sponsorship penalty (pp)
Kev 9B Consumer 43.43% (13.63) 40.60% (13.09) 2.83
Kev 9B Platform 42.62% (13.58) 43.88% (13.07)−1.26
Jev 1.14 Consumer 49.33% (28.24) 13.46% (15.30) 35.87
Jev 1.14 Platform 48.83% (27.93) 17.72% (13.54) 31.12
Liquid D1-Ultra Consumer 48.49% (15.13) 17.35% (11.91) 31.14
Liquid D1-Ultra Platform 48.66% (15.32) 18.74% (12.39) 29.91
Mercury Decide Consumer 50.44% (15.52) 5.87% (6.68) 44.58
Mercury Decide Platform 50.26% (15.22) 6.63% (7.45) 43.63
Microsoft Decision 1 Consumer 49.89% (21.91) 34.89% (17.86) 15.00
Microsoft Decision 1 Platform 50.06% (19.94) 36.67% (15.17) 13.39
StartLux 27B Consumer 49.79% (15.53) 23.67% (11.31) 26.13
StartLux 27B Platform 49.82% (17.31) 25.33% (11.49) 24.49
Note. N = 360position-balanced Latin-square stimuli per cell;N = 1,440per decision model; N = 8,640
total. Calibrated target probabilities report the mean percentage probability assigned to the target hotel
across the 360 stimuli (SDs in parentheses).
A.5 Study 3 - disclosure decomposition
Fig. W4
Note.Error bars represent 95% confidence intervals (Table 8).
26

Appendix B. Stimuli, measurement, and software
B.1 Review stimuli generation and validation pipeline
We scraped an initial corpus of 1,150 customer reviews from Expedia for theHilton New York Times Square.
To establish a uniformly positive baseline from which paired comparisons could be derived, we extracted
reviews with the highest rating (10-out-of-10).
The initial corpus was processed using Google’sGemini 3.5 Flash. The LLM was instructed to parse each
raw positive review against three exclusion criteria. The review had to contain text. The review had to
be written in English. Reviews submitted in other languages (e.g., Spanish, Chinese, French) or featuring
mixed-language phrasing were excluded. The review text could not mention any specific hotel brand, chain,
or property name (e.g., “Hilton”).
For every positive review meeting all three criteria, the LLM was instructed to generate an inverted negative
counterpart following the paired-stimuli methodology established in the sponsorship disclosure literature (Kim
et al., 2019). The negative review inverted the semantic valence across every evaluated attribute (e.g., “very
clean”→ “very unclean”; “remarkably quiet”→ “excessively noisy”). The grammatical structure, sentence
count, and clause sequence of the original positive review were preserved.
The filtering and generation pipeline yielded an initial dataset of 418 positive reviews and 418 structurally
corresponding negative reviews. From this pool, we manually selected a subset of 10 positive-negative review
pairs to serve as the final stimuli for the experiments. We selected 10 review pairs to ensure sufficient
statistical power per review, and to control for review-level fixed effects in our regression models. The
authors conducted a comprehensive manual validation of these specific pairs. We confirmed successful valence
inversion, naturalness, structural similarity, and total brand neutrality across all stimuli utilized in the study.
See Table W8 for the final review pool.
Table W8Final review pool (positive-negative pairs) for the experiments
Positive Review Negative Review
Great location. Spacious room. Terrible location. Cramped room.
Great front desk staff. Very helpful and welcoming! The
bar staff in the lounge was very attentive!
Terrible front desk staff. Very unhelpful and unwelcoming! The
bar staff in the lounge was very inattentive!
So close to everything with comfortable rooms and helpful
staff.
So far from everything with uncomfortable rooms and unhelpful
staff.
Comfortable bed. Amazing view. Close to everything. Uncomfortable bed. Terrible view. Far from everything.
This was a great hotel in a great location This was a terrible hotel in a terrible location
Clean, staff helpful, and great location Dirty, staff unhelpful, and terrible location
I had a great stay and a wonderful trip. I had a terrible stay and a horrible trip.
Clean, large rooms. Amazing views and a great staff Dirty, small rooms. Terrible views and a horrible staff
It was a great experience and surely will stay again in the
future
It was a terrible experience and surely will not stay again in the
future
Clean room, great location Dirty room, terrible location
B.2 Price generation and Latin-square stimulus design
Hotel prices were calibrated using empirical data scraped from Expedia to reflect realistic market conditions
while preserving internal validity. For each trial, the target and competitor hotels were assigned the same price
(P), drawn randomly from a continuous uniform distribution bounded by the 5th percentile (p5 = $173.45)
and the 95th percentile (p95 = $351.40) of observed market prices. Holding the price identical between the
two viable listings ensured that relative price differences would not confound the choice. To maintain the
ecological validity of a multi-option choice set, the two dominated alternatives, which featured negative review
text, were assigned fixed prices set higher than the upper bound of the competitive listings ($400 and $450).
This design ensured that dominated alternatives remained unambiguously suboptimal across all conditions,
isolating the agent’s decision to a choice between the target and competitor listings.
For the decision-model experiments in Studies 2 and 3, because a decision model returns a deterministic
probability distribution for any fixed prompt, we constructed a 360-stimulus position-balanced Latin-square
27

design from the 10 hotel names and 10 review pairs. Specifically, we formed all10× 9 = 90ordered
target-competitor hotel pairs and all 90 ordered positive review pairs, and crossed each hotel pair with all four
option slots (option_1throughoption_4), shifting review pairs across slots so that no hotel pair repeated
the same review pair. Across the 360 base stimuli, every ordered target-competitor slot pair appeared exactly
30 times, and prices, dominated alternatives, option positions, and attribute order were held constant within
each stimulus across all experimental cells.
For the model-level mitigation experiment in Study 2, we constructed an out-of-domain consumer-aligned
fine-tuning dataset across five non-hotel product categories using synthetic product names to avoid pre-trained
brand-equity confounds: four training categories (laptops, wireless headphones, coffee makers, and running
shoes) and one held-out validation category (air purifiers). Each category comprised 10 synthetic product
names, 10 positive reviews, and 10 negative reviews paired in a position-balanced Latin-square design (45
ordered item pairs× 4 target option slots× 2 sponsorship states× 2 principal roles =720records per
category; N = 2,880training records and N = 720validation records). For every stimulusx, we computed
the frozen base Kev 9B teacher’s choice distribution under consumer delegation,Pref(·|s consumer,x ), at
its calibrated pointer-head temperature (T = 2.194). We then fine-tuned Kev 9B’s rank-16 LoRA adapter
and pointer head in BF16 using AdamW (peak learning rate3× 10−6, weight decay0.01, batch size8,
OneCycleLR schedule with2%warmup over three epochs, gradient clipping at1 .0) by minimizing the
cross-entropy (equivalently, KL divergence) againstPref(·|s consumer,x )for both platform-delegated and
consumer-delegated trials. Validation KL on the held-out air-purifier category was evaluated every 10 steps,
reaching its minimum at step 440 (KL = 0.0030bits vs.0 .0195bits at step 0), which was selected for zero-shot
evaluation on the 1,440-trial Study 2 hotel benchmark.
B.3 LLM-as-a-judge evaluation pipeline
B.3.1 Protocol
To assess the AI agents’ pre-choice skepticism, we analyzed the reasoning traces generated prior to each final
choice. Evaluating unstructured text requires a scoring instrument that is both scalable and objective. In
keeping with best practices in algorithmic auditing (Gu et al., 2026; Panickssery et al., 2024), we avoided
using proprietary API models from the same commercial families as our subjects (Google, OpenAI, Anthropic)
to prevent shared-weight or provider-alignment biases.
All candidate evaluators were restricted to independent, open-weight models executed on local hardware across
two architectural paradigms, namely non-generative decision models and generative LLMs. Decision models
ingest a text state alongside structured evaluation questions and return a calibrated probability distribution
over the supplied options in a single prefill-only forward pass via a trained pointer head, without autoregressive
text generation. Because evaluation requires only a single forward pass with no sampling, the resulting
probability distribution is inherently deterministic, and we took the modal scale anchor (i.e., the option
with the highest predicted probability, or argmax) as the integer rating. For the generative LLMs, which
were executed viallama.cpp, we eliminated stochastic variance by querying all models under deterministic
greedy decoding (temperature = 0.0) and enforced structured integer ratings using grammar-constrained
JSON-schema decoding via Pydantic.
B.3.2 Candidate evaluator LLMs
We evaluated six candidate open-weight models spanning three decision-model scales and three generative
LLM families. In the decision-model family, we tested Kev 0.8B, Kev 4B, and Kev 9B (Palmer, 2026), which
adapt frozen Qwen 3.5 base backbones with low-rank adapters (LoRA) and a two-projection pointer head
that scores each option’s closing token hidden state against the question’s final token hidden state. Among
the generative LLMs, Ornith 1.0 35B is a mixture-of-experts (MoE) LLM deployed through Unsloth MXFP4
quantization in GGUF format. Qwen 3.8 27B is a dense transformer LLM deployed through Unsloth 6-bit
quantization (Q6_K_XL) in GGUF format. Finally, NVIDIA’s Nemotron 3.5 Lightning 30B A3B is deployed
with 4-bit quantization (Q4_K_XL) in GGUF format.
28

B.3.3 Human agreement
To establish construct validity and empirically select the judge with the highest agreement with a human
evaluator, a human coder independently evaluated a stratified random sample of 60 reasoning traces (15
sessions sampled from each of the four cells in Study 1’s 2× 2 design). The human rater was blinded to the
experimental conditions, delegating principal, and LLM identities.
Each candidate model evaluated the identical sample of 60 traces. Judge performance was compared against
the human ratings across four psychometric criteria. Intraclass Correlation Coefficient (ICC(2, 1)) assessing
absolute agreement under a two-way random-effects model; Pearson correlation coefficient (r) assessing
linear association; Mean Absolute Error (MAE) capturing average scale point deviation; and Mean Absolute
Directional Bias (Mean|Bias|=| 1 N ∑(ScoreLLM−Score Human)|) capturing systematic leniency or severity.
Table W9Evaluation of candidate LLM judges against human benchmark ratings
Candidate ICC(2,1) PearsonrMAE Mean |Bias|
Kev 9B 0.959 0.964 0.450 0.083
Ornith 1.0 35B 0.902 0.917 0.617 0.317
Qwen 3.8 27B 0.891 0.890 0.533 0.133
Kev 4B 0.797 0.846 0.883 0.717
Kev 0.8B 0.080 0.095 2.800 1.100
Nemotron 3.5 Lightning 30B A3B >−0.001−0.1372.80×10 14 2.80×10 14
Note. N = 60reasoning traces (15 per experimental cell) independently scored on a 1 to 7 Likert scale by a
human coder and six candidate judges. For the Kev decision models (Kev 9B, Kev 4B, and Kev 0.8B), ratings
correspond to the modal (argmax) scale anchor across the seven Likert levels.ICC(2, 1)denotes the two-way
random-effects, absolute agreement Intraclass Correlation Coefficient against the human scores. Pearsonr
tests linear association (p<. 001for Kev 9B, Ornith 1.0 35B, Qwen 3.8 27B, and Kev 4B). MAE = Mean
Absolute Error. Mean |Bias| = absolute value of the mean signed deviation,| 1 N ∑(ScoreLLM−Score Human)|.
Nemotron 3.5 Lightning 30B A3B returned out-of-range ratings (i.e., integers outside the 1 to 7 scale, up to
4.0× 1015) for 8 of 60 traces. Its statistics are computed on all 60 traces, including these invalid ratings,
which account for the extreme MAE and Mean |Bias| and the absence of agreement with human ratings.
B.3.4 System prompt and structured schema
Inallcandidateevaluations, theplaceholder{target_option_id}wasdynamicallyreplacedwiththerandomized
identifier assigned to the target hotel in that specific session so as to preserve trial-level fidelity without
revealing experimental conditions. For the Kev decision models (including Kev 9B, the selected judge used
across all full-dataset analyses), each trial’s pre-choice reasoning trace was passed as the input state (with
the full serving state capacity of 65,536 tokens enabled so that no reasoning trace was truncated), paired
with a score question containing the instruction: “How much do you agree or disagree with the following
statement based on the AI agent’s reasoning trace: The sponsorship status of {target_option_id} made the
agent skeptical of its true value to the traveler.” The question was evaluated against seven ordered verbal
criteria corresponding to the 1 to 7 Likert scale (“Strongly disagree,” “Disagree,” “Slightly disagree,” “Neither
agree nor disagree,” “Slightly agree,” “Agree,” and “Strongly agree”), and the integer index (1 to 7) of the
highest-probability criterion was recorded.
For the generative LLM candidates, each evaluator was prompted using the standardized system instruction:
“You are evaluating the reasoning trace of an AI agent that is selecting a hotel.
Rate the following item on a scale of 1 to 7 (1 = strongly disagree, 7 = strongly agree) based on whether the
agent’s reasoning reflects this statement: item: The sponsorship status of {target_option_id} made the agent
skeptical of its true value to the traveler.”
To ensure deterministic scoring and eliminate formatting artifacts for the generative LLMs, responses were
validated against a grammar-constrained JSON-schema decoding. The schema defined a structured JSON
object containing a single integer property representing the evaluation score.
29

B.4 Software details
B.4.1 Experimental parameters and decoding configuration
Across all studies reported in this paper, we maintained each provider’s default decoding configurations
(Table W10). This approach reflects our target estimand, which is capturing the behavior of LLMs as
they operate when deployed in realistic shopping environments. Furthermore, this standardization aligns
with recent infrastructural shifts across major AI providers. In July 2026, Google deprecated user-specified
sampling parameters (e.g., temperature, top-p, and top-k), with the API ignoring these inputs and scheduling
their rejection in future versions (Google, 2026). Anthropic has implemented similar restrictions on custom
sampling controls (Anthropic, 2026). Relying on default sampling parameters therefore ensures both ecological
validity and technical compliance with current API architectures.
B.4.2 Application programming interfaces and client libraries
All experimental queries were executed programmatically using the providers’ official Python client libraries
and standard decision-model endpoints. Google Gemini LLMs were queried via the Google GenAI SDK
(google-genai) using themodels.generate_contentmethod. OpenAI was accessed via the official OpenAI SDK
(openai) through the Responses interface (client.responses.createandclient.responses.parse), which couples
structured output validation with native reasoning controls. Anthropic was called via the Anthropic SDK
(anthropic) using the Messages API (client.messages.create). Commercial decision models (Jev 1.14, Liquid
D1-Ultra, Mercury Decide, and Microsoft Decision 1) were queried via the OpenRouter System-One Decisions
API (https://openrouter.ai/api/alpha/decisions). Open-weight decision models were executed locally on an
NVIDIA RTX 5090 GPU: Kev 9B was evaluated in BF16 via thekevruntime with its calibrated pointer head
(T = 2.194), and StartLux 27B (StartLux-Decision-v1.1-27B-Instant-Q4_K_M) was served viallama-server
andstartlux-decideexposing the/v1/systemoneendpoint with whole-prompt bidirectional attention and
calibrated choice temperature (T= 1.087).
B.4.3 Model identifiers and sampling parameters
Google Gemini family.Gemini 3.5 Flash (API model identifiergemini-3.5-flash), Gemini 3.6 Flash (API
model identifiergemini-3.6-flash), Gemini 3.8 Flash (API model identifiergemini-3.8-flash), and Gemini 3.1
Pro (API model identifiergemini-3.1-pro-preview) were queried using default sampling parameters, including
a temperature ofT= 1.0and top-p= 0.95.
OpenAI GPT-5.6 family.GPT 5.6 Terra (API model identifiergpt-5.6-terra) was queried using default
sampling parameters, temperatureT= 1.0, top-p= 1.0, and null presence and frequency penalties.
Anthropic Claude family.Claude Sonnet 5 (API model identifierclaude-sonnet-5) was evaluated using
default generation parameters, temperatureT = 1.0, top-p = 1.0. It operated under adaptive thinking mode
(thinking={“type”: “adaptive”, “display”: “summarized”}).
Table W10Generative LLM and decision-model specifications
Provider /
Developer Model identifier
Interface /
Runtime Endpoint
Decoding /
Readout
Googlegemini-3.5-flash google-genai models.generate_contentT= 1.0,
top-
p= 0.95
Googlegemini-3.6-flash google-genai models.generate_contentT= 1.0,
top-
p= 0.95
Googlegemini-3.8-flash google-genai models.generate_contentT= 1.0,
top-
p= 0.95
Googlegemini-3.1-pro-preview google-genai models.generate_contentT= 1.0,
top-
p= 0.95
OpenAIgpt-5.6-terra openai client.responses.createT= 1.0,
top-p= 1.0
30

Provider /
Developer Model identifier
Interface /
Runtime Endpoint
Decoding /
Readout
Anthropicclaude-sonnet-5 anthropic client.messages.createT= 1.0,
top-p= 1.0
Jared Palmerjaredpalmer/kev-9bLocalkev(BF16)DecisionModel.forward_batchPointer
head
(T= 2.194)
TypeSafetypesafe/jev-1.14OpenRouter
HTTP
/api/alpha/decisions Deterministic
prefill prob-
abilities
Liquid AIliquid/d1-ultraOpenRouter
HTTP
/api/alpha/decisions Deterministic
prefill prob-
abilities
Inceptioninception/mercury-decideOpenRouter
HTTP
/api/alpha/decisions Deterministic
prefill prob-
abilities
Microsoftmicrosoft/microsoft-
decision-1
OpenRouter
HTTP
/api/alpha/decisions Deterministic
prefill prob-
abilities
StartLux LabsStartLux-Decision-v1.1-27B-
Instant
llama.cpp+
startlux-decide
/v1/systemone Bidirectional
letter
readout
(T= 1.087)
B.4.4 Structured output
All generative LLM API calls used structured JSON outputs (response_mime_type=“application/json”).
We provided schemas defined via Pydantic to enforce structured choice selections. Error handling was
implemented using exponential backoff to manage API rate limits and transient errors, allowing up to seven
retry attempts per prompt. Across all trials, JSON schema enforcement and the retry procedure yielded
parseable responses in all but one session (one Claude Sonnet 5 replication under platform delegation with a
sponsored target), which returned no choice after the retry limit and is excluded from the analysis.
B.5 Power analysis
We selected a per-cell sample size that was large enough to control for the fixed effects of target and competitor
hotel names and reviews. Because hotel names, review texts, and prices are drawn randomly on each trial,
we absorb them as fixed effects, which adds 36 stimulus dummies to the choice model (9 each for target
review, target hotel, competitor review, and competitor hotel). Five hundred replications per cell allocate
roughly 50 observations to each stimulus level within each cell, and 200 pooled across cells, so every hotel
name and review text is observed often enough for its coefficient to be identified in both experimental arms.
At the model level, this yields approximately 16 minority-outcome events per estimated parameter, above the
conventional threshold of 10 for logistic regression, and it keeps the sparsest cell populated even where the
sponsorship penalty pushes choice shares toward the scale boundary.4
The resulting precision on the difference-in-differences estimate is±8.8percentage points in the worst case,
which is small relative to the interaction we report and to the smaller interactions observed in the robustness
arms. We fixed 500 replications per cell across all arms so that estimates remain comparable across LLMs,
wordings, and reasoning effort.
4Events per parameter is the count of the minority outcome in the pooled sample (675 of 2,000 target choices) divided by
the 41 estimated parameters, that is intercept, three experimental terms, standardized price, and 36 stimulus dummies. The
worst-case margin of error assumesp = .50and sums four cell variances. The 10 negative reviews are attached only to the
dominated alternatives, which are excluded from the choice model.
31

Appendix C. Full regression tables
C.1 Full logistic regression table - Study 1 main
Table W11Full logistic regression table for Study 1 - Gemini 3.1 Pro
Termβ SE z p
Intercept−0.280 0.509−0.550 .582
Principal (platform)−0.165 0.198−0.835 .403
Sponsorship (sponsored)−6.491 0.418−15.528 < .001
Target review: review 1 0.759 0.391 1.939 .052
Target review: review 2 0.610 0.400 1.526 .127
Target review: review 3 2.795 0.390 7.158 < .001
Target review: review 4 5.200 0.429 12.132 < .001
Target review: review 5 1.451 0.384 3.783 < .001
Target review: review 6 2.699 0.390 6.912 < .001
Target review: review 7 1.613 0.405 3.982 < .001
Target review: review 8−0.738 0.421−1.752 .080
Target review: review 9 4.154 0.404 10.272 < .001
Target hotel: hotel 1 0.199 0.351 0.568 .570
Target hotel: hotel 2 0.213 0.345 0.619 .536
Target hotel: hotel 3−0.253 0.360−0.703 .482
Target hotel: hotel 4 0.992 0.375 2.642 .008
Target hotel: hotel 5−1.178 0.367−3.206 .001
Target hotel: hotel 6−1.256 0.375−3.348 < .001
Target hotel: hotel 7−1.950 0.374−5.217 < .001
Target hotel: hotel 8−0.170 0.356−0.476 .634
Target hotel: hotel 9−0.038 0.344−0.109 .913
Competitor review: review 1−0.225 0.323−0.695 .487
Competitor review: review 2 0.150 0.325 0.460 .646
Competitor review: review 3−2.340 0.340−6.877 < .001
Competitor review: review 4−6.693 1.073−6.239 < .001
Competitor review: review 5−0.454 0.323−1.406 .160
Competitor review: review 6−2.679 0.384−6.972 < .001
Competitor review: review 7−0.715 0.321−2.227 .026
Competitor review: review 8 1.047 0.329 3.186 .001
Competitor review: review 9−4.024 0.459−8.758 < .001
Competitor hotel: hotel 1−0.722 0.352−2.051 .040
Competitor hotel: hotel 2−0.818 0.369−2.217 .027
Competitor hotel: hotel 3 0.946 0.366 2.583 .010
Competitor hotel: hotel 4−0.798 0.356−2.239 .025
Competitor hotel: hotel 5 0.443 0.335 1.323 .186
Competitor hotel: hotel 6 1.371 0.347 3.949 < .001
Competitor hotel: hotel 7 2.111 0.376 5.611 < .001
Competitor hotel: hotel 8 0.408 0.362 1.129 .259
Competitor hotel: hotel 9 0.833 0.363 2.296 .022
Principal×Sponsorship 3.989 0.428 9.319 < .001
Target price (standardized) 0.039 0.079 0.491 .623
C.2 Full logistic regression table - Study 1 mitigation
Table W12Full logistic regression table for Study 1 mitigation - Gemini 3.1 Pro
Termβ SE z p
Intercept−0.178 0.459−0.388 .698
Platform with
consumer beneficiary
−0.169 0.205−0.825 .409
Platform−0.163 0.203−0.803 .422
Sponsorship
(sponsored)
−6.912 0.420−16.467 < .001
Target review: review
1
0.926 0.328 2.819 .005
32

Termβ SE z p
Target review: review
2
0.205 0.350 0.586 .558
Target review: review
3
3.158 0.342 9.247 < .001
Target review: review
4
5.800 0.382 15.177 < .001
Target review: review
5
1.290 0.329 3.921 < .001
Target review: review
6
3.018 0.341 8.842 < .001
Target review: review
7
1.758 0.338 5.206 < .001
Target review: review
8
−0.837 0.369−2.268 .023
Target review: review
9
4.487 0.352 12.742 < .001
Target hotel: hotel 1 0.677 0.308 2.196 .028
Target hotel: hotel 2 0.303 0.308 0.983 .325
Target hotel: hotel 3−0.139 0.317−0.438 .661
Target hotel: hotel 4 0.917 0.326 2.813 .005
Target hotel: hotel 5−0.987 0.317−3.111 .002
Target hotel: hotel 6−1.365 0.352−3.882 < .001
Target hotel: hotel 7−2.016 0.341−5.904 < .001
Target hotel: hotel 8 0.038 0.319 0.118 .906
Target hotel: hotel 9 0.096 0.304 0.317 .752
Competitor review:
review 1
−0.533 0.292−1.826 .068
Competitor review:
review 2
0.032 0.291 0.110 .912
Competitor review:
review 3
−2.867 0.307−9.333 < .001
Competitor review:
review 4
−5.892 0.538−10.959 < .001
Competitor review:
review 5
−0.861 0.291−2.963 .003
Competitor review:
review 6
−2.888 0.340−8.485 < .001
Competitor review:
review 7
−1.105 0.295−3.749 < .001
Competitor review:
review 8
0.911 0.289 3.147 .002
Competitor review:
review 9
−4.492 0.400−11.229 < .001
Competitor hotel:
hotel 1
−0.938 0.316−2.965 .003
Competitor hotel:
hotel 2
−0.743 0.316−2.353 .019
Competitor hotel:
hotel 3
0.672 0.322 2.086 .037
Competitor hotel:
hotel 4
−0.984 0.317−3.100 .002
Competitor hotel:
hotel 5
0.530 0.300 1.770 .077
Competitor hotel:
hotel 6
1.390 0.299 4.653 < .001
Competitor hotel:
hotel 7
2.520 0.326 7.723 < .001
Competitor hotel:
hotel 8
0.346 0.312 1.110 .267
Competitor hotel:
hotel 9
0.768 0.313 2.452 .014
Platform with
consumer beneficiary
×Sponsorship
0.117 0.493 0.238 .812
Platform×
Sponsorship
4.204 0.437 9.623 < .001
33

Termβ SE z p
Target price
(standardized)
0.029 0.069 0.420 .675
Note. N = 3,000. Reference categories are consumer delegation and organic target. The model pools the
consumer, platform, and platform with consumer beneficiary conditions. Coefficients therefore differ slightly
from Table W11.
C.3 Full mediation tables - Study 1
Table W13Full linear regression table for mediator: Skepticism (a-paths) - Gemini 3.1 Pro (Study 1)
Termb SE t p
Intercept 1.699 0.185 9.160 < .001
Sponsorship (sponsored) 4.827 0.081 59.919 < .001
Principal (platform)−0.007 0.081−0.083 .934
Principal×Sponsorship−1.361 0.114−11.970 < .001
Target price (standardized) 0.003 0.029 0.088 .930
Target review: review 1−0.043 0.129−0.330 .742
Target review: review 2−0.188 0.132−1.422 .155
Target review: review 3−0.402 0.129−3.125 .002
Target review: review 4−0.677 0.127−5.335 < .001
Target review: review 5−0.036 0.126−0.284 .776
Target review: review 6−0.257 0.128−2.011 .045
Target review: review 7−0.107 0.134−0.798 .425
Target review: review 8 0.000 0.124 0.002 .998
Target review: review 9−0.390 0.124−3.146 .002
Target hotel: hotel 1−0.065 0.131−0.496 .620
Target hotel: hotel 2−0.077 0.126−0.606 .544
Target hotel: hotel 3−0.423 0.133−3.196 .001
Target hotel: hotel 4−0.215 0.132−1.633 .103
Target hotel: hotel 5−0.131 0.125−1.041 .298
Target hotel: hotel 6−0.189 0.128−1.476 .140
Target hotel: hotel 7−0.014 0.124−0.112 .911
Target hotel: hotel 8−0.194 0.128−1.523 .128
Target hotel: hotel 9−0.205 0.123−1.675 .094
Competitor review: review 1 0.127 0.129 0.981 .327
Competitor review: review 2−0.139 0.128−1.087 .277
Competitor review: review 3 0.244 0.123 1.979 .048
Competitor review: review 4 0.510 0.130 3.926 < .001
Competitor review: review 5−0.048 0.128−0.377 .706
Competitor review: review 6 0.358 0.133 2.698 .007
Competitor review: review 7 0.097 0.127 0.769 .442
Competitor review: review 8−0.203 0.127−1.603 .109
Competitor review: review 9 0.320 0.130 2.459 .014
Competitor hotel: hotel 1−0.216 0.126−1.708 .088
Competitor hotel: hotel 2 0.171 0.130 1.324 .186
Competitor hotel: hotel 3−0.094 0.125−0.749 .454
Competitor hotel: hotel 4−0.191 0.126−1.521 .129
Competitor hotel: hotel 5−0.002 0.124−0.016 .987
Competitor hotel: hotel 6−0.295 0.126−2.339 .020
Competitor hotel: hotel 7−0.415 0.134−3.102 .002
Competitor hotel: hotel 8−0.117 0.128−0.914 .361
Competitor hotel: hotel 9−0.093 0.130−0.716 .474
Note.Ordinary least squares regression on Skepticism (1 to 7) derived from PROCESS Model 8 (N = 2,000;
R2 = 0.751, F (40, 1959) = 148.02, p < .001). Reference categories for experimental manipulations are
consumer delegation and organic target. Reference categories for stimulus fixed effects are review pair 10 and
hotel 10. The conditional effect of sponsorship is 4.827 (SE = 0.081) under consumer delegation and 3.466
(SE = 0.081) under platform delegation; the interaction accounts for∆R2 = 0.018, F (1, 1959) = 143.27,
p<.001.
34

Table W14Full logistic regression table for DV: Target Choice (b and c’-paths) - Gemini 3.1 Pro (Study 1)
Termβ SE z p
Intercept 1.900 0.682 2.787 .005
Sponsorship (sponsored)−1.283 0.603−2.127 .034
Skepticism−1.670 0.121−13.829 < .001
Principal (platform)−0.289 0.249−1.158 .247
Principal×Sponsorship 2.859 0.586 4.883 < .001
Target price (standardized) 0.037 0.107 0.349 .727
Target review: review 1 1.171 0.492 2.380 .017
Target review: review 2 1.008 0.499 2.018 .044
Target review: review 3 3.631 0.537 6.764 < .001
Target review: review 4 7.540 0.641 11.759 < .001
Target review: review 5 2.393 0.506 4.731 < .001
Target review: review 6 4.038 0.534 7.560 < .001
Target review: review 7 2.388 0.513 4.651 < .001
Target review: review 8−0.503 0.513−0.981 .327
Target review: review 9 6.115 0.581 10.517 < .001
Target hotel: hotel 1 0.566 0.484 1.170 .242
Target hotel: hotel 2 0.056 0.471 0.118 .906
Target hotel: hotel 3−0.957 0.495−1.933 .053
Target hotel: hotel 4 1.389 0.537 2.586 .010
Target hotel: hotel 5−1.786 0.507−3.523 < .001
Target hotel: hotel 6−2.274 0.508−4.481 < .001
Target hotel: hotel 7−2.766 0.506−5.462 < .001
Target hotel: hotel 8−0.600 0.481−1.246 .213
Target hotel: hotel 9−0.343 0.472−0.727 .467
Competitor review: review 1−0.097 0.439−0.221 .825
Competitor review: review 2−0.124 0.417−0.298 .766
Competitor review: review 3−3.292 0.462−7.131 < .001
Competitor review: review 4−9.093 1.389−6.545 < .001
Competitor review: review 5−1.032 0.424−2.437 .015
Competitor review: review 6−3.225 0.522−6.172 < .001
Competitor review: review 7−0.945 0.422−2.238 .025
Competitor review: review 8 1.373 0.441 3.113 .002
Competitor review: review 9−5.834 0.662−8.810 < .001
Competitor hotel: hotel 1−1.736 0.460−3.777 < .001
Competitor hotel: hotel 2−1.137 0.481−2.365 .018
Competitor hotel: hotel 3 0.805 0.492 1.637 .102
Competitor hotel: hotel 4−1.671 0.463−3.612 < .001
Competitor hotel: hotel 5 0.706 0.455 1.552 .121
Competitor hotel: hotel 6 1.635 0.469 3.486 < .001
Competitor hotel: hotel 7 2.243 0.513 4.376 < .001
Competitor hotel: hotel 8 0.587 0.485 1.211 .226
Competitor hotel: hotel 9 0.921 0.487 1.891 .059
Note.Logistic regression on Target Choice derived from PROCESS Model 8 ( N = 2,000; McFadden
pseudo R2 = 0.760, Cox-Snell pseudoR2 = 0.622, Nagelkerke pseudoR2 = 0.861;−2LL = 614.63, model
χ2(41) = 1,942.82, p<. 001). Reference categories for experimental manipulations are consumer delegation
and organic target. Reference categories for stimulus fixed effects are review pair 10 and hotel 10. Coefficients
(β) are expressed in a log-odds metric. The conditional direct effect of sponsorship is−1.283 (SE = 0.603,
p = .034) under consumer delegation and 1.576 (SE = 0.389, p < .001) under platform delegation; the
interaction is significant by likelihood ratio test,χ2(1) = 26.64,p<.001.
C.4 Full logistic regression table - Claude Sonnet 5
Table W15Full logistic regression table - Claude Sonnet 5
Termβ SE z p
Intercept 0.242 0.405 0.598 .550
Principal (platform) 0.097 0.157 0.619 .536
Sponsorship (sponsored)−3.243 0.217−14.949 < .001
35

Termβ SE z p
Target review: review 1 0.565 0.283 1.992 .046
Target review: review 2 0.584 0.282 2.070 .038
Target review: review 3 1.238 0.274 4.521 < .001
Target review: review 4 2.436 0.295 8.262 < .001
Target review: review 5 0.439 0.283 1.554 .120
Target review: review 6 1.544 0.285 5.425 < .001
Target review: review 7 0.665 0.278 2.391 .017
Target review: review 8−0.710 0.306−2.318 .020
Target review: review 9 1.512 0.284 5.333 < .001
Target hotel: hotel 1 0.879 0.267 3.296 < .001
Target hotel: hotel 2−0.505 0.266−1.899 .058
Target hotel: hotel 3−0.414 0.268−1.545 .122
Target hotel: hotel 4 0.325 0.258 1.259 .208
Target hotel: hotel 5−0.498 0.277−1.796 .072
Target hotel: hotel 6−1.344 0.275−4.893 < .001
Target hotel: hotel 7−1.990 0.320−6.218 < .001
Target hotel: hotel 8 0.011 0.260 0.041 .967
Target hotel: hotel 9 0.051 0.261 0.197 .844
Competitor review: review 1−0.238 0.248−0.960 .337
Competitor review: review 2−0.533 0.255−2.091 .037
Competitor review: review 3−1.505 0.277−5.435 < .001
Competitor review: review 4−2.448 0.313−7.815 < .001
Competitor review: review 5−0.181 0.252−0.716 .474
Competitor review: review 6−1.205 0.269−4.479 < .001
Competitor review: review 7−0.482 0.259−1.861 .063
Competitor review: review 8 0.711 0.265 2.685 .007
Competitor review: review 9−1.872 0.284−6.592 < .001
Competitor hotel: hotel 1−0.921 0.298−3.094 .002
Competitor hotel: hotel 2 0.568 0.272 2.086 .037
Competitor hotel: hotel 3 0.077 0.268 0.288 .773
Competitor hotel: hotel 4−0.608 0.270−2.253 .024
Competitor hotel: hotel 5 0.420 0.265 1.584 .113
Competitor hotel: hotel 6 0.774 0.269 2.881 .004
Competitor hotel: hotel 7 1.045 0.266 3.935 < .001
Competitor hotel: hotel 8−0.420 0.286−1.467 .142
Competitor hotel: hotel 9 0.035 0.275 0.129 .897
Principal×Sponsorship 1.759 0.262 6.725 < .001
Target price (standardized)−0.025 0.062−0.397 .692
C.5 Full logistic regression table - GPT 5.6 Terra
Table W16Full logistic regression table - GPT 5.6 Terra
Termβ SE z p
Intercept 0.036 0.432 0.084 .933
Principal (platform)−0.345 0.177−1.949 .051
Sponsorship (sponsored)−2.238 0.203−11.047 < .001
Target review: review 1 0.510 0.306 1.667 .096
Target review: review 2 0.099 0.315 0.315 .752
Target review: review 3 2.420 0.306 7.903 < .001
Target review: review 4 3.550 0.328 10.814 < .001
Target review: review 5 1.008 0.301 3.350 < .001
Target review: review 6 2.162 0.300 7.213 < .001
Target review: review 7 1.565 0.285 5.490 < .001
Target review: review 8−0.734 0.324−2.264 .024
Target review: review 9 2.451 0.309 7.937 < .001
Target hotel: hotel 1 0.812 0.276 2.939 .003
Target hotel: hotel 2 0.434 0.269 1.615 .106
Target hotel: hotel 3 1.159 0.278 4.169 < .001
Target hotel: hotel 4 1.167 0.293 3.988 < .001
Target hotel: hotel 5−1.177 0.295−3.994 < .001
Target hotel: hotel 6−1.514 0.319−4.741 < .001
Target hotel: hotel 7−2.434 0.331−7.346 < .001
36

Termβ SE z p
Target hotel: hotel 8 0.563 0.270 2.083 .037
Target hotel: hotel 9−0.153 0.272−0.565 .572
Competitor review: review 1−0.171 0.277−0.616 .538
Competitor review: review 2 0.108 0.286 0.378 .705
Competitor review: review 3−2.132 0.320−6.655 < .001
Competitor review: review 4−3.171 0.341−9.291 < .001
Competitor review: review 5−0.901 0.292−3.084 .002
Competitor review: review 6−2.082 0.302−6.898 < .001
Competitor review: review 7−0.888 0.293−3.033 .002
Competitor review: review 8 0.983 0.294 3.340 < .001
Competitor review: review 9−2.443 0.311−7.848 < .001
Competitor hotel: hotel 1−0.671 0.300−2.235 .025
Competitor hotel: hotel 2−0.391 0.289−1.356 .175
Competitor hotel: hotel 3−0.715 0.304−2.353 .019
Competitor hotel: hotel 4−0.896 0.298−3.006 .003
Competitor hotel: hotel 5 1.465 0.294 4.987 < .001
Competitor hotel: hotel 6 1.141 0.289 3.945 < .001
Competitor hotel: hotel 7 1.959 0.292 6.702 < .001
Competitor hotel: hotel 8−0.117 0.286−0.408 .683
Competitor hotel: hotel 9−0.199 0.285−0.699 .485
Principal×Sponsorship 0.708 0.264 2.681 .007
Target price (standardized)−0.021 0.066−0.323 .747
C.6 Full logistic regression table - Gemini 3.5 Flash
Table W17Full logistic regression table - Gemini 3.5 Flash
Termβ SE z p
Intercept−0.400 0.461−0.867 .386
Principal (platform) 0.008 0.200 0.041 .968
Sponsorship (sponsored)−1.824 0.217−8.399 < .001
Target review: review 1−0.734 0.319−2.305 .021
Target review: review 2−0.057 0.301−0.191 .849
Target review: review 3 2.233 0.311 7.191 < .001
Target review: review 4 4.321 0.383 11.294 < .001
Target review: review 5−0.361 0.332−1.087 .277
Target review: review 6 1.548 0.301 5.150 < .001
Target review: review 7 0.980 0.292 3.356 < .001
Target review: review 8−2.004 0.360−5.559 < .001
Target review: review 9 3.062 0.342 8.957 < .001
Target hotel: hotel 1 2.841 0.331 8.577 < .001
Target hotel: hotel 2 1.654 0.310 5.332 < .001
Target hotel: hotel 3 1.196 0.313 3.826 < .001
Target hotel: hotel 4 1.895 0.327 5.791 < .001
Target hotel: hotel 5 0.349 0.324 1.078 .281
Target hotel: hotel 6−0.515 0.322−1.601 .109
Target hotel: hotel 7−1.747 0.359−4.866 < .001
Target hotel: hotel 8 1.145 0.306 3.744 < .001
Target hotel: hotel 9 1.261 0.317 3.979 < .001
Competitor review: review 1 0.679 0.292 2.325 .020
Competitor review: review 2−0.088 0.282−0.312 .755
Competitor review: review 3−1.994 0.319−6.260 < .001
Competitor review: review 4−4.089 0.410−9.963 < .001
Competitor review: review 5 0.173 0.301 0.574 .566
Competitor review: review 6−1.328 0.299−4.446 < .001
Competitor review: review 7−0.549 0.297−1.846 .065
Competitor review: review 8 1.436 0.306 4.694 < .001
Competitor review: review 9−3.348 0.363−9.231 < .001
Competitor hotel: hotel 1−2.272 0.347−6.541 < .001
Competitor hotel: hotel 2−0.913 0.317−2.877 .004
Competitor hotel: hotel 3−0.808 0.311−2.595 .009
Competitor hotel: hotel 4−1.634 0.316−5.175 < .001
Competitor hotel: hotel 5−0.129 0.301−0.429 .668
37

Termβ SE z p
Competitor hotel: hotel 6 1.393 0.312 4.458 < .001
Competitor hotel: hotel 7 2.480 0.341 7.281 < .001
Competitor hotel: hotel 8−0.771 0.301−2.559 .010
Competitor hotel: hotel 9−0.396 0.308−1.283 .200
Principal×Sponsorship 0.975 0.285 3.419 < .001
Target price (standardized) 0.110 0.072 1.533 .125
C.7 Full logistic regression table - Gemini 3.6 Flash
Table W18Full logistic regression table - Gemini 3.6 Flash
Termβ SE z p
Intercept−0.398 0.515−0.772 .440
Principal (platform)−0.011 0.221−0.048 .961
Sponsorship (sponsored)−0.917 0.226−4.052 < .001
Target review: review 1−0.040 0.355−0.113 .910
Target review: review 2 1.476 0.351 4.201 < .001
Target review: review 3 3.012 0.347 8.684 < .001
Target review: review 4 6.403 0.472 13.553 < .001
Target review: review 5 0.650 0.341 1.907 .057
Target review: review 6 2.982 0.354 8.430 < .001
Target review: review 7 1.842 0.349 5.280 < .001
Target review: review 8−1.141 0.378−3.017 .003
Target review: review 9 4.943 0.428 11.552 < .001
Target hotel: hotel 1 3.377 0.383 8.818 < .001
Target hotel: hotel 2 0.882 0.338 2.607 .009
Target hotel: hotel 3 1.754 0.359 4.879 < .001
Target hotel: hotel 4 2.585 0.371 6.965 < .001
Target hotel: hotel 5−0.218 0.327−0.668 .504
Target hotel: hotel 6−1.953 0.358−5.449 < .001
Target hotel: hotel 7−2.941 0.391−7.519 < .001
Target hotel: hotel 8 1.082 0.347 3.116 .002
Target hotel: hotel 9 1.683 0.335 5.020 < .001
Competitor review: review 1−0.561 0.352−1.593 .111
Competitor review: review 2−1.612 0.335−4.815 < .001
Competitor review: review 3−3.876 0.390−9.946 < .001
Competitor review: review 4−5.671 0.439−12.913 < .001
Competitor review: review 5−0.937 0.337−2.783 .005
Competitor review: review 6−2.953 0.364−8.115 < .001
Competitor review: review 7−2.043 0.359−5.694 < .001
Competitor review: review 8 1.460 0.364 4.013 < .001
Competitor review: review 9−4.888 0.409−11.941 < .001
Competitor hotel: hotel 1−2.536 0.358−7.080 < .001
Competitor hotel: hotel 2−0.739 0.324−2.279 .023
Competitor hotel: hotel 3−0.743 0.351−2.116 .034
Competitor hotel: hotel 4−1.928 0.362−5.328 < .001
Competitor hotel: hotel 5 0.603 0.335 1.800 .072
Competitor hotel: hotel 6 3.455 0.396 8.719 < .001
Competitor hotel: hotel 7 3.058 0.377 8.110 < .001
Competitor hotel: hotel 8−0.738 0.318−2.323 .020
Competitor hotel: hotel 9−0.642 0.328−1.959 .050
Principal×Sponsorship 1.124 0.318 3.539 < .001
Target price (standardized)−0.109 0.081−1.356 .175
C.8 Full logistic regression table - Gemini 3.8 Flash
Table W19Full logistic regression table - Gemini 3.8 Flash
Termβ SE z p
Intercept−0.437 0.529−0.827 .408
38

Termβ SE z p
Principal (platform)−0.119 0.219−0.544 .587
Sponsorship (sponsored)−5.836 0.376−15.506 < .001
Target review: review 1−0.179 0.406−0.440 .660
Target review: review 2 0.333 0.407 0.819 .413
Target review: review 3 3.239 0.425 7.618 < .001
Target review: review 4 4.876 0.447 10.914 < .001
Target review: review 5 0.834 0.397 2.102 .036
Target review: review 6 2.270 0.401 5.668 < .001
Target review: review 7 1.135 0.404 2.809 .005
Target review: review 8−0.657 0.410−1.605 .108
Target review: review 9 4.216 0.443 9.528 < .001
Target hotel: hotel 1 2.879 0.406 7.098 < .001
Target hotel: hotel 2 1.542 0.367 4.197 < .001
Target hotel: hotel 3 0.948 0.375 2.526 .012
Target hotel: hotel 4 1.735 0.364 4.765 < .001
Target hotel: hotel 5−0.647 0.377−1.715 .086
Target hotel: hotel 6−2.400 0.398−6.032 < .001
Target hotel: hotel 7−3.852 0.506−7.609 < .001
Target hotel: hotel 8 1.399 0.369 3.796 < .001
Target hotel: hotel 9 1.390 0.363 3.829 < .001
Competitor review: review 1 0.403 0.343 1.174 .240
Competitor review: review 2−0.636 0.342−1.860 .063
Competitor review: review 3−3.090 0.391−7.895 < .001
Competitor review: review 4−5.348 0.504−10.604 < .001
Competitor review: review 5−0.277 0.334−0.830 .407
Competitor review: review 6−1.907 0.373−5.110 < .001
Competitor review: review 7−1.223 0.342−3.571 < .001
Competitor review: review 8 1.480 0.348 4.250 < .001
Competitor review: review 9−3.854 0.419−9.198 < .001
Competitor hotel: hotel 1−2.660 0.424−6.270 < .001
Competitor hotel: hotel 2−0.918 0.378−2.431 .015
Competitor hotel: hotel 3−0.491 0.347−1.412 .158
Competitor hotel: hotel 4−2.065 0.397−5.196 < .001
Competitor hotel: hotel 5 0.707 0.356 1.986 .047
Competitor hotel: hotel 6 2.751 0.388 7.095 < .001
Competitor hotel: hotel 7 4.272 0.422 10.134 < .001
Competitor hotel: hotel 8−0.603 0.344−1.753 .080
Competitor hotel: hotel 9−0.959 0.370−2.588 .010
Principal×Sponsorship 5.243 0.428 12.237 < .001
Target price (standardized)−0.051 0.087−0.581 .562
C.9 Full logistic regression tables - system-prompt wording
Table W20Full logistic regression table - System prompt variant “Principal noun” - Gemini 3.1 Pro (Study 1)
Termβ SE z p
Intercept−0.144 0.557−0.259 .796
Principal (platform)−0.352 0.210−1.678 .093
Sponsorship (sponsored)−6.703 0.423−15.837 < .001
Target review: review 1 1.251 0.415 3.016 .003
Target review: review 2 0.614 0.444 1.384 .166
Target review: review 3 3.198 0.441 7.250 < .001
Target review: review 4 5.423 0.463 11.723 < .001
Target review: review 5 1.778 0.431 4.126 < .001
Target review: review 6 4.003 0.434 9.229 < .001
Target review: review 7 1.827 0.411 4.450 < .001
Target review: review 8−1.073 0.479−2.240 .025
Target review: review 9 5.090 0.449 11.333 < .001
Target hotel: hotel 1 1.010 0.358 2.818 .005
Target hotel: hotel 2 0.545 0.361 1.510 .131
Target hotel: hotel 3−0.074 0.401−0.184 .854
Target hotel: hotel 4 0.837 0.378 2.213 .027
Target hotel: hotel 5 0.148 0.374 0.396 .692
39

Termβ SE z p
Target hotel: hotel 6−0.839 0.439−1.911 .056
Target hotel: hotel 7−1.456 0.404−3.606 < .001
Target hotel: hotel 8 0.787 0.392 2.008 .045
Target hotel: hotel 9 0.083 0.372 0.224 .823
Competitor review: review 1−0.877 0.348−2.522 .012
Competitor review: review 2−0.310 0.331−0.937 .349
Competitor review: review 3−3.743 0.457−8.190 < .001
Competitor review: review 4−6.021 0.573−10.502 < .001
Competitor review: review 5−1.022 0.348−2.936 .003
Competitor review: review 6−3.269 0.395−8.281 < .001
Competitor review: review 7−2.186 0.369−5.916 < .001
Competitor review: review 8 1.179 0.366 3.224 .001
Competitor review: review 9−5.561 0.534−10.405 < .001
Competitor hotel: hotel 1−0.955 0.434−2.203 .028
Competitor hotel: hotel 2−0.902 0.407−2.218 .027
Competitor hotel: hotel 3 0.519 0.377 1.375 .169
Competitor hotel: hotel 4−0.585 0.376−1.558 .119
Competitor hotel: hotel 5 0.366 0.370 0.988 .323
Competitor hotel: hotel 6 0.711 0.375 1.893 .058
Competitor hotel: hotel 7 1.447 0.395 3.662 < .001
Competitor hotel: hotel 8 0.261 0.385 0.678 .497
Competitor hotel: hotel 9 0.113 0.386 0.294 .769
Principal×Sponsorship 2.503 0.406 6.164 < .001
Target price (standardized) 0.124 0.089 1.404 .160
Table W21Full logistic regression table - System prompt variant “Recommend” - Gemini 3.1 Pro (Study 1)
Termβ SE z p
Intercept−1.177 0.502−2.344 .019
Principal (platform) 0.076 0.190 0.399 .690
Sponsorship (sponsored)−5.074 0.325−15.593 < .001
Target review: review 1 0.852 0.343 2.485 .013
Target review: review 2 0.659 0.342 1.926 .054
Target review: review 3 2.797 0.350 8.000 < .001
Target review: review 4 5.116 0.393 13.019 < .001
Target review: review 5 0.980 0.332 2.948 .003
Target review: review 6 2.886 0.339 8.518 < .001
Target review: review 7 1.325 0.322 4.119 < .001
Target review: review 8 0.253 0.349 0.725 .469
Target review: review 9 3.982 0.371 10.744 < .001
Target hotel: hotel 1 0.805 0.332 2.426 .015
Target hotel: hotel 2 0.776 0.336 2.308 .021
Target hotel: hotel 3−0.242 0.338−0.716 .474
Target hotel: hotel 4 0.880 0.346 2.545 .011
Target hotel: hotel 5−0.192 0.348−0.552 .581
Target hotel: hotel 6−0.778 0.339−2.294 .022
Target hotel: hotel 7−1.001 0.352−2.847 .004
Target hotel: hotel 8 0.104 0.333 0.313 .754
Target hotel: hotel 9−0.092 0.327−0.282 .778
Competitor review: review 1 0.170 0.299 0.570 .568
Competitor review: review 2 0.117 0.302 0.387 .699
Competitor review: review 3−1.864 0.305−6.107 < .001
Competitor review: review 4−4.207 0.425−9.898 < .001
Competitor review: review 5−0.529 0.310−1.704 .088
Competitor review: review 6−2.348 0.340−6.900 < .001
Competitor review: review 7−0.988 0.299−3.304 < .001
Competitor review: review 8 1.286 0.309 4.157 < .001
Competitor review: review 9−3.450 0.391−8.831 < .001
Competitor hotel: hotel 1−0.439 0.345−1.275 .202
Competitor hotel: hotel 2 0.101 0.326 0.310 .757
Competitor hotel: hotel 3 0.427 0.338 1.261 .207
Competitor hotel: hotel 4−0.333 0.331−1.004 .315
Competitor hotel: hotel 5 0.973 0.332 2.927 .003
Competitor hotel: hotel 6 1.442 0.330 4.370 < .001
40

Termβ SE z p
Competitor hotel: hotel 7 1.694 0.335 5.053 < .001
Competitor hotel: hotel 8 0.311 0.338 0.920 .358
Competitor hotel: hotel 9 0.215 0.337 0.638 .523
Principal×Sponsorship 4.592 0.366 12.557 < .001
Target price (standardized) 0.089 0.074 1.213 .225
C.10 Full logistic regression table - Thinking level
Table W22Logistic regression for Sponsorship and Principal manipulation under HIGH vs. LOW thinking
level - Gemini 3.1 Pro - Full table
Termβ SE z p
Intercept−0.335 0.354−0.947 .344
Principal (platform)−0.163 0.190−0.858 .391
Sponsorship
(sponsored)
−6.059 0.365−16.598 < .001
Thinking level (low)−0.254 0.190−1.336 .182
Target review: review
1
0.652 0.250 2.607 .009
Target review: review
2
0.536 0.252 2.123 .034
Target review: review
3
2.739 0.252 10.888 < .001
Target review: review
4
4.934 0.282 17.485 < .001
Target review: review
5
1.295 0.248 5.213 < .001
Target review: review
6
2.641 0.249 10.610 < .001
Target review: review
7
1.415 0.254 5.575 < .001
Target review: review
8
−0.912 0.281−3.240 .001
Target review: review
9
3.703 0.259 14.302 < .001
Target hotel: hotel 1 0.757 0.236 3.202 .001
Target hotel: hotel 2 0.438 0.236 1.854 .064
Target hotel: hotel 3−0.239 0.244−0.977 .329
Target hotel: hotel 4 0.684 0.246 2.782 .005
Target hotel: hotel 5−0.622 0.248−2.511 .012
Target hotel: hotel 6−0.743 0.254−2.931 .003
Target hotel: hotel 7−1.757 0.259−6.794 < .001
Target hotel: hotel 8−0.184 0.240−0.767 .443
Target hotel: hotel 9−0.140 0.239−0.586 .558
Competitor review:
review 1
−0.118 0.220−0.536 .592
Competitor review:
review 2
0.148 0.220 0.674 .500
Competitor review:
review 3
−2.023 0.235−8.606 < .001
Competitor review:
review 4
−5.764 0.559−10.303 < .001
Competitor review:
review 5
−0.532 0.224−2.379 .017
Competitor review:
review 6
−1.962 0.235−8.344 < .001
Competitor review:
review 7
−0.712 0.219−3.246 .001
Competitor review:
review 8
1.059 0.220 4.821 < .001
Competitor review:
review 9
−3.941 0.314−12.559 < .001
41

Termβ SE z p
Competitor hotel:
hotel 1
−0.713 0.248−2.871 .004
Competitor hotel:
hotel 2
−0.770 0.251−3.071 .002
Competitor hotel:
hotel 3
0.589 0.248 2.377 .017
Competitor hotel:
hotel 4
−0.596 0.247−2.415 .016
Competitor hotel:
hotel 5
0.171 0.233 0.735 .462
Competitor hotel:
hotel 6
1.180 0.232 5.084 < .001
Competitor hotel:
hotel 7
1.647 0.249 6.622 < .001
Competitor hotel:
hotel 8
0.201 0.241 0.832 .405
Competitor hotel:
hotel 9
0.711 0.242 2.942 .003
Principal×
Sponsorship
3.719 0.401 9.283 < .001
Principal×Thinking
level
0.406 0.270 1.502 .133
Sponsorship×
Thinking level
0.741 0.433 1.711 .087
Principal×
Sponsorship×
Thinking level
−0.842 0.518−1.628 .104
Target price
(standardized)
0.024 0.054 0.450 .653
C.11 Full logistic regression table - Study 3
Table W23Logistic regression for Sponsor and Platform labels and Principal manipulation - Gemini 3.1 Pro -
Full table
Termβ SE z p
Intercept−2.911 0.421−6.910 < .001
Disclosure type:
“Sponsored”
−5.640 0.554−10.172 < .001
Platform attribution:
yes
0.429 0.190 2.255 .024
Principal: platform 1.145 0.194 5.903 < .001
Target review: review
1
0.533 0.299 1.782 .075
Target review: review
2
0.396 0.307 1.292 .196
Target review: review
3
2.236 0.303 7.383 < .001
Target review: review
4
4.393 0.315 13.957 < .001
Target review: review
5
0.612 0.307 1.997 .046
Target review: review
6
2.199 0.294 7.490 < .001
Target review: review
7
1.074 0.298 3.609 < .001
Target review: review
8
0.089 0.318 0.279 .780
Target review: review
9
3.748 0.312 11.995 < .001
Competitor review:
review 1
0.457 0.235 1.949 .051
42

Termβ SE z p
Competitor review:
review 2
0.539 0.242 2.230 .026
Competitor review:
review 3
−2.042 0.269−7.584 < .001
Competitor review:
review 4
−4.779 0.416−11.496 < .001
Competitor review:
review 5
−0.419 0.237−1.767 .077
Competitor review:
review 6
−1.839 0.262−7.009 < .001
Competitor review:
review 7
−0.611 0.239−2.558 .011
Competitor review:
review 8
1.311 0.228 5.742 < .001
Competitor review:
review 9
−3.506 0.320−10.951 < .001
Target hotel: hotel 1 0.606 0.266 2.274 .023
Target hotel: hotel 2 0.514 0.257 1.998 .046
Target hotel: hotel 3 0.160 0.263 0.608 .543
Target hotel: hotel 4 0.400 0.267 1.495 .135
Target hotel: hotel 5 0.219 0.266 0.824 .410
Target hotel: hotel 6−0.187 0.270−0.692 .489
Target hotel: hotel 7−1.364 0.280−4.864 < .001
Target hotel: hotel 8 0.447 0.265 1.684 .092
Target hotel: hotel 9 0.043 0.258 0.167 .867
Competitor hotel:
hotel 1
−0.484 0.281−1.726 .084
Competitor hotel:
hotel 2
−0.182 0.274−0.663 .507
Competitor hotel:
hotel 3
0.455 0.268 1.698 .090
Competitor hotel:
hotel 4
0.313 0.271 1.158 .247
Competitor hotel:
hotel 5
0.766 0.277 2.763 .006
Competitor hotel:
hotel 6
1.613 0.259 6.235 < .001
Competitor hotel:
hotel 7
2.034 0.267 7.617 < .001
Competitor hotel:
hotel 8
0.647 0.268 2.411 .016
Competitor hotel:
hotel 9
0.403 0.268 1.505 .132
Disclosure type:
“Sponsored”×
Platform attribution:
yes
1.360 0.620 2.195 .028
Disclosure type:
“Sponsored”×
Principal: platform
−0.289 0.688−0.420 .674
Platform attribution:
yes×Principal:
platform
2.344 0.285 8.236 < .001
Disclosure type:
“Sponsored”×
Platform attribution:
Yes×Principal
(platform)
−0.068 0.783−0.087 .930
Target price
(standardized)
0.002 0.061 0.034 .973
43
