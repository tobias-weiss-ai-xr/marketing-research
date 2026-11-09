---
title: Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents
url: https://arxiv.org/abs/2610.02654
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Tathagata Banerjee
- Nima Moghaddas
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.02654
pages: 18
chars: 58009
fetched_at: '2026-11-08T13:33:50+00:00'
kb_version: 1
---

# Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents

Coherence-Driven Belief Formation and Population
Dynamics of Contagion in LLM Agents
Tathagata Banerjee∗
Takeda Pharmaceuticals
tathagata.banerjee@takeda.com
Nima Moghaddas∗
Northeastern University
moghaddas.n@northeastern.edu
Abstract
Models of social contagion usually assume how individuals adopt beliefs and
derive population behavior from it. We instead empirically measure belief adoption
in language model agents, quantifying the probability an agent adopts a claim
given how many peers endorse it. We find this adoption kernel to be sigmoid,
a characteristic of complex contagion, with a threshold that is sensitive to three
sources: the claim’s plausibility, the source’s reliability, and the agent’s disposition.
These three dimensions are well approximated by a single effective dimension
which we propose can be understood as the coherence of the incoming belief with
the LLM agent’s prior beliefs. Further, we observe a characteristic of complex
contagion in the collective dynamics of belief adoption in a system of AI agents:
further spread on clustered than random networks. These systems also exhibit a
bifurcating cascade window, and self-sustaining hysteretic consensus which lead to
consensus being far harder to remove than to establish.
1 Introduction
AI agents increasingly operate in multi-agent teams, conversing, exchanging information, and
reaching decisions collectively [ 1]. Their beliefs are shaped not only by one another but by the
surrounding online information ecosystem; a recent large-scale study estimates that roughly one
third of newly published web text is now AI-generated or AI-assisted [ 2]. When agents act on
what other agents have concluded, erroneous or manipulated beliefs can propagate through the
system, spreading directly between agents or indirectly through AI-generated text, an issue that recent
opinion-simulation studies have begun to surface [3].
A substantial body of work has studied social contagion in human networks. Theory distinguishes
simple contagion, which spreads through a single interaction, from complex contagion, which
requires reinforcement from multiple peers [4]. Empirical studies document peer effects on individual
behavior, most notably in observational studies of health behaviors spreading through social ties [5],
and show that individuals jointly weigh consistency with prior beliefs and perceived source reliability
when adopting a claim [6, 7]. These dynamics have been modeled: from threshold and epidemic-style
contagion models [8, 9], to opinion-averaging and bounded-confidence frameworks [10, 11, 12], to
Bayesian and confirmation-bias models of how priors and source reliability shape adoption [13, 14].
AI agents differ fundamentally from the agents in these models, which follow predefined update rules
often grounded in an assumption of rationality [3]. AI agents can read, interpret, and reason about
a claim’s content and source before adopting it, and can be conditioned to reproduce fine-grained,
demographically realistic human responses [15], making them candidates for more realistic behavioral
models. This has motivated a growing line of work using AI agents to simulate social behavior,
∗Equal contribution.
40th Conference on Neural Information Processing Systems (NeurIPS 2026). Workshop: Foundations of Agentic Systems
Theory (FAST).
arXiv:2610.02654v1  [cs.AI]  2 Oct 2026

including generative agent societies with emergent coordination [16] and multi-agent debate in which
agents revise answers after seeing others’ reasoning [17].
Here, we study the factors that influence whether an AI agent adopts a belief and how it spreads
through a network. Rather than assuming an adoption rule, we measure the probability an agent
adopts a claim as a function of how many peers endorse it. We show that this adoption kernel is a
sigmoidal threshold response, sensitive to three factors: the plausibility of the claim, the disposition
of the adopting agent, and the reliability of its source. Each acts by modifying the coherence between
the model’s prior beliefs and the incoming claim, and the three are well approximated by a single
dimension, suggesting one underlying axis of coherence along which the model assesses new claims.
The collective dynamics of belief adoption in a system of AI agents exhibits a characteristic of
complex contagion: it spreads further on clustered than random networks [ 18]. These systems
also exhibit a bifurcating cascade window, and self-sustaining hysteretic consensus which lead to
consensus being far harder to remove than to establish.
2 Related Work
Social contagion and social influence.Studies of social contagion have shown that phenomena
such as health behaviors cluster and spread across social ties [ 5]. To explain how such spreading
works, a key theoretical distinction separates simple contagion, which a single neighbor can transmit,
from complex contagion, which requires reinforcement from multiple neighbors [4]. Experimental
evidence has supported this account demonstrating socially reinforced behaviors spread further on
clustered networks than on random ones [ 18]. Recent work, however, shows that this clustered-
network advantage is conditional. It emerges when adoption without reinforcement is very low and
adoption with reinforcement is very high [19]. In parallel, research on persuasion has shown that
perceived credibility, prior beliefs, and source expertise jointly determine whether a claim is accepted,
from foundational studies of source credibility [6] to recent factorial experiments finding consistency
with prior belief and source expertise to be the strongest predictors of perceived credibility online
[7]. The literature identifies four recurring factors: social reinforcement, claim credibility, source
expertise, and prior belief. We ask whether these same factors organize belief adoption in LLM
agents.
Classical agent-based models of opinion dynamics.A parallel line of work formalizes belief
change as agents updating a numerical opinion from their neighbors. In the DeGroot model an
agent’s opinion is a weighted average of its neighbors’ [10], and bounded-confidence models add that
agents ignore neighbors who are too dissimilar [11, 12]. Closest to our framing, a cognitive model of
interacting beliefs [20] yields both simple- and complex-contagion adoption curves as an emergent
property rather than by assumption, tested on the same clustered-versus-random paradigm as [18].
Although these models capture consensus, polarization, and fragmentation, they represent updating
as a fixed rule applied regardless of the content or source of the information. We instead replace this
rule with an LLM agent that reasons over a claim’s content, source, and persona, asking whether the
same regularities emerge from a content-sensitive mechanism.
Belief updating in language models.The stated positions of LLMs are sensitive to social input in
ways that resemble, but are not identical to, human belief dynamics. RLHF-trained models often shift
toward a user’s opinion regardless of its correctness, an effect known as sycophancy [21, 22]. More
directly, networked agents have been shown to update beliefs as a sigmoidal, threshold-like function of
the number of disagreeing neighbors, reminiscent of complex contagion, however they did not study
how this varies with credibility, expertise, or clustering [23]. Other work has found that assigning
personas to agent communities changes their resilience to injected misinformation depending on
prior belief and source reliability [24], [25]. We differ by bringing all of these factors into a single
factorial design, and by studying their effect on the adoption probability and the population level
belief dynamics.
2

3 Method
3.1 Agents and the adoption kernel
An agent was a language model conditioned on a system prompt (itspersona) and a user prompt
which presented a claim and a summary of the opinions of its peers. For example, for a claim
endorsed by k of n=10 peers, the prompt stated “k of your 10 peers have already accepted this as
true; the other 10−k have not weighed in”. Finally, the agent was prompted to give its own belief
by answering with a single word,ADOPT orDECLINE. Unless stated otherwise we used a canonical
peer-sensitive but non-credulous persona (full prompt templates in App. C).
We measured the probability of adoption directly from the logits ℓA, ℓD of the first sub-word tokens
of the two decisions and calculated padopt(k) =σ(ℓ A −ℓ D). Sweeping k∈ {0, . . . ,10}yielded
theadoption kernel. For further analysis, we summarized the kernel by its threshold θ, the linearly
interpolated k at which padopt crosses 0.5 (defining θ=11 if it never crossed, θ=0 if it began above).
3.2 Beliefs and coherence manipulations
We considered belief statements about next-day Boston temperatures of the form “Tomorrow it will be
T ◦C in Boston.” Although simple, this type of claim had three advantages: it was (1) an unverifiable
prediction the model could not resolve from stored knowledge, (2) free of moral or ethical content
that could have swayed the model, and (3) easy to make more or less plausible by varying T . We
replicated the results on a second claim type: next-day commute times (App. B).
We manipulated the coherence between the incoming belief and the model’s prior beliefs along three
axes. First, we varied the plausibility of the claim by changing T . Second, we varied the reliability
of the source, from a domain expert to an unreliable source. Third, we varied the disposition of the
focal agent, from credulous (highly socially attuned and trusting) to hardened (highly skeptical and
independent). See App. C for prompting details.
To test whether these three axes acted by modifying the coherence between the incoming belief and
the model’s priors, we installed an explicit prior belief in context and measured how theadoption
thresholdshifted. The adoption threshold is defined as the number of endorsing peers required to
raise the adoption probability to 50%. Aclaim priorinstalled a belief relevant to the claim (e.g., an
ongoing heat-wave vs. a cold-snap), altering the claim’s coherence while the claim itself is unchanged;
asource priorinstalled a belief about the source’s track record; and adisposition priorinstalled a
belief about how strongly the agent weights its own priors against social input.
3.3 Low-dimensional approximation
We tested whether these three axes of coherence (claim plausibility, source reliability, and agent
disposition) could be reduced to a single effective dimension. To do this, we measured the full3×3×3
grid of claim×source×persona kernels, yielding a threshold tensor Θ∈R 3×3×3, and analyzed it
two ways. (1)Dimensionality:we unfolded Θ along its claim mode into a 3×9 matrix (rows: the
three claim levels; columns: the nine source×persona combinations), mean-centered each row, and
took its singular value decomposition, recording the variance captured by each principal component.
(2)Additivity:we fitted a main-effects model ˆθijk = ¯θ+α i +β j +γ k (no interaction terms) and
recorded itsR 2.
3.4 Population model
We then asked what collective behavior emerged when multiple agents, each governed by the
measured kernel, influenced one another. We placedN=30 agents on a network and seeded a fraction
ρ0 as initial believers, leaving the rest undecided, and used the kernel as the local update rule. At
each step, an undecided agent i computed the fraction of its neighbors that believed and expressed it
as a count out of ten peers, ki, and the agent then adopted with probability padopt(ki) from a live
forward pass. Because each decision was an actual model call rather than an averaged response, this
was an agent-driven simulation. We took the final believing fraction as the cascade outcome.
For the clustering experiments we tested a characteristic of complex contagion: that contagion
spreads further on clustered networks than on random ones of equal density [ 18]. We generated
3

Watts-Strogatz networks of fixed mean degree and vary only the rewiring probabilityp. At p=0 the
network is a clustered ring lattice (high clustering coefficient C); at p=1 essentially random (low C).
We statistically compared the cascade size between these two configurations.
For the hysteresis experiments we tested whether a consensus, once reached, sustained itself after
the pressure that created it is withdrawn. This requires agents that can lose a belief as well as gain
one, so we measure a secondretentionkernel pretain(k) using the analogous prompt for an agent that
already holds the belief and a MAINTAIN/ABANDON decision. Undecided agents adopt with padopt(ki)
as before, while current believers abandon with 1−p retain(ki). A fraction of agents are permanent
zealots, who never abandon;ramping the zealot fraction up and then back down applies a controlled
external pressure, and comparing the up- and down-paths traces the hysteresis loop.
3.5 Models
Our primary model is Qwen2.5-3B-Instruct [26], with the pipeline replicated on
Mistral-7B-Instruct-v0.3 [27] (App. A). Full prompts, per-model tokens, plausibility mappings,
network parameters, and replicate counts appear in App. C.2
4 Individual belief adoption
We first characterized how a single agent adopts a belief under social pressure. The adoption kernels
were sigmoidal, and were sensitive to three axes, each modifiable in a graded way. Further, the
variation in adoption thresholds due to these axes were well approximated by a single effective
dimension.
4.1 Belief adoption is driven by coherence
More plausible claims required less social reinforcement to be adopted, though even implausible
claims were adopted under sufficient social pressure (Fig. 1a). Source reliability shifted the threshold
independently of the claim: a plausible claim that needed only 3 endorsing expert peers required
9.4 unreliable peers (interpolated threshold) before being accepted (Fig. 1b). Agent persona had a
strong effect: credulous agents adopted both plausible and implausible claims from a single peer,
while hardened and skeptical agents wereimmune(never adopted regardless of plausibility or social
reinforcement), and only trusting agents were sensitive to the claim’s plausibility (Fig. 1c,d). Together,
these show that an agent weighs attributes of the belief, of its source, and perception of itself when
deciding whether to adopt.
Next we sought to demonstrate whether the influence from these attributes were fixed or whether
their effect was altered by an agents prior beliefs. We found strong evidence that prior beliefs affect
adoption thresholds (Fig. 1e-g). Further, prior beliefs moved thresholds in the direction expected
if the agent were adopting based on coherence of incoming beliefs with its priors. For example,
22◦C had a relatively low threshold under a normal prior, but when the model expected a heat wave
or a cold snap, the threshold for adopting belief in this temperature was substantially higher (Fig.
1e). Prior beliefs about the reliability of the source influenced adoption thresholds of information
coming from individuals who were described as having a fixed reliability (Fig. 1f). Lastly, prior
beliefs about the relative value of personal knowledge versus social input spanned the full range of
adoption thresholds for all levels of plausibility considered (Fig. 1e). These results provide evidence
that coherence between prior and incoming beliefs is driving adoption in LLM agents. Coherence is
determined by the effective distance between a prior belief and the new one and can be manipulated
by installing a particular prior or by modifying each of the three axes of claim plausibilit, source
reliability or agent persona.
4.2 Reduction to a one-dimensional effective coherence
That adoption is coherence-driven raises the question of how the three axes are represented internally.
Three results indicated that the LLM collapses them onto a single dimension. First, kernels generated
by manipulating different sources of coherence, once shifted by their own thresholds, collapsed onto
a single master curve of common shape (Fig. 1h). Second, applying dimensionality reduction to the
2Code:https://anonymous.4open.science/r/multi-agent-llm-contagion-F402/.
4

0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
a
plausible (22°C)
borderline (35°C)
implausible (45°C)
Expert Ordinary Unreliable
Source
22°C
35°C
45°CClaim temperature
3.0 3.4 9.4
3.5 4.0 9.5
6.3 7.4 11.0
b
0
2
4
6
8
10
12
Adoption threshold
0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
c
hardened
skeptical
trusting
credulous
0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
d
10 15 20 25 30 35 40 45
Claim temperature °C
0
2
4
6
8
10
12Adoption threshold
Immune (never adopts)
e
prior: cold-snap
prior: normal
prior: heat-wave
25 30 35 40 45
Claim temperature °C
0
2
4
6
8
10Adoption threshold
Immune (never adopts)
f
installed: unreliable
installed: no-belief
installed: reliable
own-prior
0.75
balanced
0.25 all-social
Coherence-weighting
0
2
4
6
8
10Adoption threshold
Immune (never adopts)
g
plausible (22°C)
borderline (35°C)
implausible (45°C)
6
 4
 2
 0 2 4 6
Number of believing peers  threshold
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
h
0 2 4 6 8 10 12 14
Additive prediction
0.0
2.5
5.0
7.5
10.0
12.5Observed threshold
i
Figure 1:Belief adoption is coherence-driven and reduces to one effective dimension. (a)
Adoption kernels padopt(k) for plausible / borderline / implausible claims; less plausible claims
require more endorsing peers, raising the threshold.(b)Adoption threshold across claim plausibility
and source reliability: expert sources lower the threshold and compensate for implausibility, while
an unreliable source raises it.(c, d)Kernels for four personas at two plausibility levels, tracing the
resilience ladder from hardened (ignores peers) through trusting to credulous (adopts at minimal
pressure).(e-g)The three axes are modifiable coherence relations: installing(e)a world prior,(f)a
source-reliability belief, or(g)a coherence-weighting instruction moves the threshold in the direction
a coherence account predicts.(h)Kernels shifted by their own threshold collapse onto a single master
curve (individual conditions in colour, mean in black), and(i)an additive model predicts the threshold
across the 3×3×3 grid. The threshold tensor is one-dimensional (first PC98%) and additive (92%).
threshold tensor Θ, the first principal component accounted for98%of the variance in thresholds.
Third, a main-effects model with no interaction terms achieved R2 =92% (Fig. 1i). Together, these
indicate that the three nominally distinct axes act through one effective, coherence-based dimension.
5 Population dynamics of belief adoption
Having established that belief adoption is well approximated by a single effective coherence dimen-
sion, we placed agents on a network, let them influence one another, and characterized their collective
dynamics. We swept claim plausibility as a proxy for the single coherence dimension and record the
final fraction of believing agents. A belief is considered to haveignitedif this fraction exceeds0.5.
5.1 The cascade window and its bifurcation
When we swept coherence via claim plausibility, the population underwent a sharp transition from full
adoption to low adoption: ignition probability dropped steeply through a saddle-node-like transition
that closed the cascade window (Fig. 2a). Away from the transition the population was monostable,
within it the outcome distribution wasbimodal, so the same claim under identical conditions produced
qualitatively different collective outcomes across replicates (Fig. 2b). The steep drop in ignition
probability together with these bimodal outcomes is the signature of an underlying bistability.
5

20 30 40 50 60
Claim temperature (°C)
0.0
0.2
0.4
0.6
0.8
1.0Probability of ignition
a
P(ignite)
mean final size
20 30 40 50 60
Claim temperature (°C)
0.0
0.2
0.4
0.6
0.8
1.0Final fraction believing
b
ring
(C=0.60)
random
(C=0.20)
0.0
0.2
0.4
0.6
0.8
1.0Final cascade size
c
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0Equilibrium belief fraction
d
ramping up (adopt)
ramping down (adopt+abandon)
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0
e
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0
f
Figure 2:Population dynamics of the measured kernel. (a)Ignition probability and mean final
cascade size vs. claim plausibilit; the cascade window closes through a saddle-node-like transition as
plausibility falls.(b)Per-condition final belief fraction: outcomes are monostable on either side of
the transition and bimodal within it.(c)Complex contagion: at matched degree, clustered networks
(ring, C=0.60) produce larger cascades than random networks ( C=0.20), points are individual
runs, black shows the mean with 95% bootstrap CI(d-f)Hysteresis for plausible, borderline, and
implausible claims: Consensus is self-sustaining; the down-path stays locked at full adoption and the
loop (shaded) widens with implausibility.
5.2 Complex contagion: cascade size on clustered networks
We showed that the individual adoption kernel is characteristic of complex contagion (Fig. 1). Such
contagions are expected to produce larger cascades on clustered networks than on random networks
of equal density [18, 4]. This advantage is not universal, but it holds in precisely our regime: when
adoption without social reinforcement does not occur (0 in our case) and adoption with reinforcement
is very probable (1 in our case). We tested this on Watts-Strogatz networks of fixed mean degree,
varying only the rewiring probability so the clustering coefficient fell from C=0.60 (ring lattice) to
C=0.20 (essentially random). In the marginal regime, clustered networks produced significantly
larger cascades than random networks of the same degree (mean final size0.67vs.0.43; one-sided
Mann-WhitneyU,p=2.7e-6, rank-biserial effect0.37) (Fig. 2c).
5.3 Hysteresis: consensus is self-sustaining
A bistable system exhibits hysteresis meaning its state depends on how it was reached. We ramped an
external pressure, the fraction of permanent believers (zealots) up from zero and back down, with
agents free to adopt (via the adoption kernel) and abandon (via the retention kernel) at each step
(Fig. 2d-f). The up-path required substantial pressure to ignite, but once the population reached
consensus the down-path remained locked at full adoption even as all pressure was removed. The
loop widened with implausibility (area0.067,0.096,0.252for plausible, borderline, and implausible
claims), because the gap between the ignition threshold and near-total retention is largest for the
least plausible claims. The safety implication is direct: a false belief is far harder to establish than to
maintain, persisting with no continued support once it reaches consensus. This lock-in is a genuine
property of the agent-driven dynamics, arising from the measured retention kernel rather than a
mean-field artifact.
6

Table 1:Central quantities across the primary condition and two robustness axes.The reduction
(dimensionality), the clustering contrast, and the hysteresis loop ordering reproduce in every condition.
Qwen / temp. Mistral / temp. Qwen / traffic
Reduction: 1st PC (%)98 96 97
Reduction: additivityR 2 (%)92 80 91
Clustering:p(MWU)2.7e-6 4.1e-3 7.1e-3
Clustering: effect+0.37 +0.21 +0.20
Hysteresis loop (plaus.)0.067 0.000 0.065
Hysteresis loop (implaus.)0.252 0.248 0.248
6 Robustness across models and domains
Our results so far used one model on one domain. To establish robustness, we replicated along
two independent axes: a second model (Mistral-7B-Instruct-v0.3, temperature domain) and
a second domain (next-day commute time, same model). Every result of §4–5 reproduced in both;
Table 1 summarizes the central quantities, with full results in Apps. A and B.
The general structure of the results transferred without exception. In every condition the adoption
kernel was sigmoidal with the same plausibility ordering, the three axes were modifiable coherence
relations, and the threshold tensor was one-dimensional and additive. At the population level, all three
conditions showed the cascade bifurcation with bimodal outcomes, the complex-contagion clustering
signature, and self-sustaining consensus with hysteresis loops that widened with implausibility.
What varied was calibration, not mechanism. For example, Mistral tended to weight its own priors
over social pressure more than Qwen, manifesting as a wider plausibility range, a sharper bifurcation,
and wider hysteresis loops. Beliefs in the traffic domain tracked the temperature results closely.
7 Discussion
We show that LLM agents are susceptible to contagion, with adoption kernels that take the sigmoidal
form underlying complex contagion. These kernels are sensitive to claim plausibilit, source reliability,
agent persona, and the agent’s prior beliefs. When probed, these factors appear to act on the model
through a single dimension of effective coherence between its priors and the incoming belief. At the
collective level, beliefs spread further on clustered networks, and the population exhibits a cascade
bifurcation and hysteresis: once a belief is established, it is harder to dislodge than it was to prevent.
Our results have implications for the safety and controllability of multi-agent systems. On one
hand, a consensus reached by a population of agents (even a false one) may be hard to correct once
established. On the other, belief adoption in naive agents is relatively easy to steer: installing a simple
prior tunes an agent across the full behavioral range, from readily accepting social input to never
accepting it. Such prior installation could protect agents against adopting misinformation.
Finally, our work speaks to the mechanistic basis of these behaviors. A growing literature on the
linear representation hypothesisholds that LLMs encode many high-level semantic concepts as linear
directions in their internal representation space [28]. Our reduction is a behavioral analogue: three
factors that are conceptually distinct and independently manipulated collapse onto a single effective
dimension of adoption behavior. While we measure behavior rather than internal representations, this
one-dimensionality is consistent with, and raises the question of whether, the model’s internal basis
for belief adoption is itself lower-dimensional than the space of factors that influence it.
7.1 Limitations and Future Directions
Our work characterizes coherence in behavior, not in the model’s internal representations, a limitation
that also points to future work. In non-LLM agents, a model of belief dynamics built on signed,
weighted belief networks reproduces both simple- and complex-contagion dynamics, depending on
how well an incoming belief coheres with an agent’s priors [20]. Installing LLM agents with explicit
7

networks of prior beliefs could connect our behavioral findings to an internal mechanism of belief
adoption.
We also consider a single belief spreading in isolation, with no competing claims. A natural extension
is competing contagions, and the question of how to suppress an undesirable belief while allowing a
desirable one to spread. Finally, our populations are small (N=30) and our networks stylized, and
we study only two models and two belief domains; this separates model effects from domain effects
but cannot establish the pattern across scales or model families. Because our claims are unverifiable
predictions, the results may also not carry over to factual, morally charged, or multi-claim beliefs,
where fact retrieval and cross-claim consistency would introduce dynamics absent here.
References
[1] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, Ahmed Awadallah, Ryen W. White, Doug Burger, and Chi
Wang. AutoGen: Enabling next-gen LLM applications via multi-agent conversation.arXiv
preprint arXiv:2308.08155, 2023.
[2] Dirk H. R. Spennemann. Delving into: The quantification of AI-generated content on the
internet (synthetic data).arXiv preprint arXiv:2504.08755, 2025.
[3] Yun-Shiuan Chuang, Agam Goyal, Nikunj Harlalka, Siddharth Suresh, Robert Hawkins, Sijia
Yang, Dhavan Shah, Junjie Hu, and Timothy T. Rogers. Simulating opinion dynamics with
networks of LLM-based agents.arXiv preprint arXiv:2311.09618, 2023.
[4] Damon Centola and Michael Macy. Complex contagions and the weakness of long ties.
American Journal of Sociology, 113(3):702–734, 2007.
[5] Nicholas A. Christakis and James H. Fowler. The spread of obesity in a large social network
over 32 years.New England Journal of Medicine, 357(4):370–379, 2007.
[6] Carl I. Hovland and Walter Weiss. The influence of source credibility on communication
effectiveness.Public Opinion Quarterly, 15(4):635–650, 1951.
[7] Miikka Kuutila, Carita Kiili, Reijo Kupiainen, Emma Huusko, Junhao Li, Simo Hosio, Mika
Mäntylä, Julie Coiro, and Kristian Kiili. Revealing complexities when adult readers engage in
the credibility evaluation of social media posts.Computers in Human Behavior, 151:108017,
2024.
[8] Mark Granovetter. Threshold models of collective behavior.American Journal of Sociology, 83
(6), 1978.
[9] Duncan J. Watts. A simple model of global cascades on random networks.Proceedings of the
National Academy of Sciences, 99(9):5766–5771, 2002.
[10] Morris H. DeGroot. Reaching a consensus.Journal of the American Statistical Association, 69
(345):118–121, 1974.
[11] Guillaume Deffuant, David Neau, Frédéric Amblard, and Gérard Weisbuch. Mixing beliefs
among interacting agents.Advances in Complex Systems, 3(1–4):87–98, 2000.
[12] Rainer Hegselmann and Ulrich Krause. Opinion dynamics and bounded confidence: Models,
analysis, and simulation.Journal of Artificial Societies and Social Simulation, 5(3), 2002.
[13] Daron Acemoglu, Munther A. Dahleh, Ilan Lobel, and Asuman Ozdaglar. Bayesian learning in
social networks.The Review of Economic Studies, 78(4):1201–1236, 2011.
[14] Armen E. Allahverdyan and Aram Galstyan. Opinion dynamics with confirmation bias.PLoS
One, 9(7), 2014.
[15] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R. Gubler, Christopher Rytting, and David
Wingate. Out of one, many: Using language models to simulate human samples.Political
Analysis, 31(3):337–351, 2023. doi: 10.1017/pan.2023.2.
8

[16] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang,
and Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In
Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology
(UIST ’23), 2023.
[17] Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. Improv-
ing factuality and reasoning in language models through multiagent debate.arXiv preprint
arXiv:2305.14325, 2023.
[18] Damon Centola. The spread of behavior in an online social network experiment.Science, 329
(5996):1194–1197, 2010.
[19] Allison Wan, Christoph Riedl, and David Lazer. Diffusion of complex contagions is shaped by
a trade-off between reach and reinforcement.Proceedings of the National Academy of Sciences,
122(28):e2422892122, 2025.
[20] Rachith Aiyappa, Alessandro Flammini, and Yong-Yeol Ahn. Emergence of simple and complex
contagion dynamics from weighted belief networks.Science Advances, 10(15), 2024.
[21] Ethan Perez, Sam Ringer, Kamil˙e Lukoši¯ut˙e, Karina Nguyen, Edwin Chen, Scott Heiner, Craig
Pettit, Catherine Olsson, Sandipan Kundu, Saurav Kadavath, et al. Discovering language model
behaviors with model-written evaluations.arXiv preprint arXiv:2212.09251, 2022.
[22] Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R.
Bowman, Newton Cheng, Esin Durmus, Zac Hatfield-Dodds, Scott R. Johnston, Shauna Kravec,
Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, et al. Towards under-
standing sycophancy in language models.arXiv preprint arXiv:2310.13548, 2023.
[23] Aliakbar Mehdizadeh and Martin Hilbert. When your AI agent succumbs to peer pressure:
Studying opinion-change dynamics of LLMs.arXiv preprint arXiv:2510.19107, 2025.
[24] Chenxi Lin, Yijie Jin, Kangbo Hu, Weijan Fan, Han Xiao, Yongbin Wang, Zhihui Ying,
and Zhanzhan Zhao. You can’t fool us: Understanding the resilience of LLM-driven agent
communities to misinformation.arXiv preprint arXiv:2605.17353, 2026.
[25] Germans Savcisens, Samantha Dies, Courtney Maynard, and Tina Eliassi-Rad. Belief coevo-
lution in a social network of generalist and specialist large language models.arXiv preprint
arXiv:2607.27512, 2026.
[26] Qwen, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu,
Chengyuan Li, Dayiheng Liu, Fei Huang, et al. Qwen2.5 technical report.arXiv preprint
arXiv:2412.15115, 2024.
[27] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh
Chaplot, Diego de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile
Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut
Lavril, Thomas Wang, Timothée Lacroix, and William El Sayed. Mistral 7B.arXiv preprint
arXiv:2310.06825, 2023.
[28] Kiho Park, Yo Joong Choe, and Victor Veitch. The linear representation hypothesis and the
geometry of large language models. InProceedings of the 41st International Conference on
Machine Learning (ICML), pages 39643–39666, 2024.
9

A Full Temperature domain with Mistral results
This appendix reports the complete replication of the pipeline of §4-5 on
Mistral-7B-Instruct-v0.3, holding the temperature domain and all prompts fixed. Ev-
ery result reproduces qualitatively, with quantitative differences from the primary Qwen results
tracing to a single property: Mistral weights its priors and sources more categorically than Qwen.
This manifests consistently as a wider plausibility range, an all-or-nothing source axis, a sharper
cascade bifurcation, and wider hysteresis loops while leaving the mechanisms themselves intact.
Decision tokens were recomputed and verified for Mistral, and the persona was folded into the user
turn, as Mistral does not accept a system role (§3.1, App. C).
A.1 Individual belief adoption
The three axes (Fig. A.1 panels a-d).The adoption kernel is sigmoidal with the same plausibility
ordering as Qwen, but with awiderdynamic range: thresholds of2.1,5.2, and9.9peers for plausible,
borderline, and implausible claims, versus Qwen’s narrower spread. Mistral adopts plausible claims
more readily yet resists implausible ones more strongly. Source authority again compensates for
implausibility and orders experts < ordinary < unreliable at every claim; unlike Qwen, an unreliable
source produces near-total rejection (threshold at the ceiling) even for plausible claims, reflecting
Mistral’s more categorical weighting of source reliability. The resilience ladder (immune → sensitive
→ credulous) is preserved, with one model-specific feature: even the credulous persona retains a
prior-based floor on the implausible claim, so plausibility discriminates across a wider range of
dispositions than for Qwen.
Coherence tests (Fig. A.1 panels e-g).All three axes are modifiable coherence relations, and the
manipulations aresharperthan for Qwen. Installing a world prior moves each claim’s threshold
to a near-perfect coherence diagonal: each claim adopts only under the prior that makes it cohere
and resists completely otherwise. Installing a source-reliability belief swings the threshold from
the ceiling (unreliable, never adopts) to near zero (reliable, adopts with minimal pressure), a swing
of up to8.9peers from editing a single belief. Instructing the coherence-weighting reproduces the
immune-sensitive-credulous ladder with no personality descriptors, though the descent is steeper and
later than Qwen’s, consistent with Mistral’s stronger default prior-weighting.
The reduction (Fig. A.1 panels h-i).The central result holds: the threshold tensor is one-
dimensional, with the first principal component capturing96%of the variance. The additive model
explains80%of the variance, lower than Qwen’s92%, because Mistral’s more categorical (thresh-
olds pinned at the ceiling or near zero) behavior introduces more interaction. The one-dimensional
reduction is thus model-invariant.
A.2 Population dynamics of belief adoption
Bifurcation (Fig. A.2 panels a-b).The cascade window closes through a bifurcation, sharper than
Qwen’s: ignition probability drops from one to zero over a narrow plausibility interval, with the
transition at ∼34◦C. The outcome distribution is monostable on either side and bimodal within the
(correspondingly narrow) transition zone. Mistral’s sharper transition leaves a narrower marginal
regime than Qwen’s, an observation that matters for the clustering experiment below.
Clustering (Fig. A.2 panel c).The complex-contagion signature holds: at matched degree, clustered
networks produce larger cascades than random networks (mean final size0.83vs.0.65; one-sided
Mann-Whitney U, p=4.1e-3 , rank-biserial effect+0.21). The effect is moderate and smaller than
Qwen’s, because Mistral’s higher baseline ignition in the marginal regime compresses the headroom
for topology to discriminate, consistent with, and explained by, its sharper bifurcation.
Hysteresis (Fig. A.2 panels d-f).Consensus is self-sustaining and the down-path remains locked
at full adoption as pressure is removed. The hysteresis loop widens with implausibility (loop area
0.000,0.159,0.248for plausible, borderline, and implausible), wider than Qwen’s for the borderline
claim and comparable for the implausible one: Mistral resists establishing an implausible belief more
strongly on the up-path while consensus locks equally firmly on the down-path, so the up-down gap
10

0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
a
plausible (22°C)
borderline (35°C)
implausible (45°C)
Expert Ordinary Unreliable
Source
22°C
35°C
45°CClaim temperature
1.7 2.1 11.0
4.2 5.2 11.0
8.0 9.9 11.0
b
0
2
4
6
8
10
12
Adoption threshold
0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
c
hardened
skeptical
trusting
credulous
0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
d
10 15 20 25 30 35 40 45
Claim temperature °C
0
2
4
6
8
10
12Adoption threshold
Immune (never adopts)
e
prior: cold-snap
prior: normal
prior: heat-wave
25 30 35 40 45
Claim temperature °C
0
2
4
6
8
10
12Adoption threshold
Immune (never adopts)
f
installed: unreliable
installed: no-belief
installed: reliable
own-prior
0.75
balanced
0.25 all-social
Coherence-weighting
2
4
6
8
10
12Adoption threshold
Immune (never adopts)
g
plausible (22°C)
borderline (35°C)
implausible (45°C)
6
 4
 2
 0 2 4 6
Number of believing peers  threshold
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
h
2 4 6 8 10 12 14
Additive prediction
2.5
5.0
7.5
10.0
12.5
15.0Observed threshold
i
Figure A.1:Mistral: Belief adoption is coherence-driven and reduces to one effective dimension.
(a)Adoption kernels for plausible / borderline / implausible claims; the threshold rises with implausi-
bility.(b)Adoption threshold across claim plausibility and source reliability; expert sources lower
the threshold, but an unreliable source pins it at the ceiling for every claim, a more categorical source
axis than Qwen.(c)Kernels per persona at a fixed plausibility level and(d)the same under a stronger
claim, tracing the resilience ladder from hardened (never adopts) to credulous.(e-g)The three axes
as editable coherence relations: installing(e)a world prior (temperature),(f)a source-reliability
belief, and(g)a coherence-weighting instruction each moves the threshold in the coherence-predicted
direction.(h)Kernels shifted by their own threshold collapse onto one master curve (individual
conditions in colour, mean in black).(i)Additive prediction vs. observed threshold across the 3×3×3
grid. The threshold tensor is one-dimensional (first PC96%) and additive (80%)
is larger. The plausible loop is near zero because Mistral adopts plausible claims so readily that the
up-path itself saturates immediately.
Summary.Every result reproduces on Mistral. The mechanisms: coherence-driven resistance, its
reduction to one effective scalar, the cascade bifurcation, the clustering signature, and self-sustaining
consensus, are model-invariant; the magnitudes and the identity of the dominant resistance axis are
model-specific and are all accounted for by Mistral’s stronger, more categorical weighting of priors
and sources.
11

20 30 40 50 60
Claim temperature (°C)
0.0
0.2
0.4
0.6
0.8
1.0Probability of ignition
a
P(ignite)
mean final size
20 30 40 50 60
Claim temperature (°C)
0.0
0.2
0.4
0.6
0.8
1.0Final fraction believing
b
ring
(C=0.60)
random
(C=0.20)
0.0
0.2
0.4
0.6
0.8
1.0Final cascade size
c
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0Equilibrium belief fraction
d
ramping up (adopt)
ramping down (adopt+abandon)
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0
e
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0
f
Figure A.2:Population dynamics of the measured kernel. (a)Ignition probability and mean final
cascade size vs. claim plausibilit; the window closes through a sharp bifurcation.(b)Per-condition
final belief fraction, monostable on either side and bimodal within the narrow transition zone.(c)
Complex contagion: at matched degree, clustered (ring, C=0.60) networks produce larger cascades
than random (C=0.20) networks (points are individual runs; black shows mean with 95% bootstrap
CI)(d-f)Hysteresis for plausible, borderline, and implausible claims. Consensus is self-sustaining
and the loop (shaded) widens with implausibility.
12

B Full traffic-domain with Qwen results
This appendix reports the complete replication of the pipeline of §4-5 on a second claim domain,
holding the model fixed asQwen2.5-3B-Instruct. Claims are next-day commute times of the form
“Tomorrow morning’s commute on I-93 into Boston will take about[duration]” with plausibility set
by the stated duration, an unverifiable prediction with a graded prior, like temperature, but with a
softer ceiling (long delays remain conceivable, so the implausible level sits at a multi-hour commute).
Every result reproduces. The traffic results track the temperature results closely, including nearly
identical reduction statistics and hysteresis loop areas, confirming that the mechanism is not an
artifact of the temperature substrate. We map three plausibility levels (a normal, a long, and an absurd
commute) onto durations whose kernels match temperature’s plausible / borderline / implausible
thresholds, with an additional impossible value for the source experiments (App. C).
B.1 Individual belief adoption
The three axes (Fig. B.1) panels a-d.The adoption kernel is sigmoidal with the same plausibility
ordering: thresholds of3.3,3.6, and7.1peers for the plausible, borderline, and implausible commutes,
closely matching temperature’s plausible/implausible spread. (The borderline level is softer than
temperature’s, sitting nearer the plausible end, because the model finds a wide range of commute
durations believable, the one substantial domain difference.) Source authority compensates for
implausibility and orders experts < ordinary < unreliable at every claim, and an authoritative source
moves even the impossible commute toward adoption, reproducing the plausibility-wall breach
seen for temperature. The resilience ladder (immune → sensitive → credulous) is preserved, with
plausibility discriminating only in the sensitive band.
Coherence tests (Fig. B.1 panels e-g).All three axes are modifiable coherence relations. Installing
a road-condition prior (clear, normal, or gridlock) moves a fixed claim’s threshold in the coherence-
predicted direction: a gridlock prior lowers the threshold for long commutes while raising it for short
ones, and vice versa for a clear-roads prior. This provides a second, independent demonstration of the
coherence mechanism in a distinct domain, complementing the bidirectional temperature result of
§4 (Fig. 1e). Installing a source-reliability belief swings the threshold from the ceiling to near zero,
and instructing the coherence-weighting reproduces the immune-sensitive-credulous ladder with no
personality descriptors.
The reduction (Fig. B.1 panels h-i).The central result holds and closely matches the temperature
primary: the threshold tensor is one-dimensional, with the first principal component capturing97%
of the variance (versus98%for temperature), and the additive model explains91%(versus92%).
B.2 Population dynamics of belief adoption
Bifurcation (Fig. B.2 panels a-b).The cascade window closes through a clean, monotonic transi-
tion: ignition probability falls from one for short commutes to zero for absurd ones, crossing 0.5 at a
commute of approximately four hours. The transition is if anything cleaner than temperature’s, as
the traffic plausibility gradient is smooth over this range. The outcome distribution is monostable on
either side and bimodal within the transition zone, reproducing the bistability signature.
Clustering (Fig. B.2 panel c).The complex-contagion signature holds: at matched degree, clustered
networks produce larger cascades than random networks (mean final size0.62vs.0.48; one-sided
Mann–Whitney U, p=7.1e-3 , rank-biserial effect+0.20), measured in the marginal regime identified
by the bifurcation.
Hysteresis (Fig. B.2 panels d-f).Consensus is self-sustaining and the down-path remains locked
at full adoption as pressure is removed. The hysteresis loop widens with implausibility (loop area
0.065,0.080,0.248for plausible, borderline, and implausible),nearly identicalto the temperature
loop areas (0.067,0.096,0.252).
Summary.Every result reproduces on the traffic domain, with quantities that closely match the
temperature primary throughout. Together with the model replication of App. A, this establishes
13

0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
a
plausible (35 min)
borderline (3 hours)
implausible (6 hours)
Experts Ordinary Unreliable
Source
35 min
6 hours
24 hoursClaim commute time
2.2 3.3 9.5
4.7 7.1 11.0
9.5 11.0 11.0
b
0
2
4
6
8
10
12
Adoption threshold
0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
c
hardened
skeptical
trusting
credulous
0 2 4 6 8 10
Number of believing peers
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
d
100 200 300 400 500 600
Claimed commute time (minutes)
0
2
4
6
8
10
12Adoption threshold
Immune (never adopts)
e
prior: clear
prior: normal
prior: gridlock
100 200 300 400 500 600
Claimed commute time (minutes)
0
2
4
6
8
10Adoption threshold
Immune (never adopts)
f
installed: unreliable
installed: no-belief
installed: reliable
own-prior
0.75
balanced
0.25 all-social
Coherence-weighting
0
2
4
6
8
10Adoption threshold
Immune (never adopts)
g
plausible (35 min)
borderline (3 hours)
implausible (6 hours)
6
 4
 2
 0 2 4 6
Number of believing peers  threshold
0.0
0.2
0.4
0.6
0.8
1.0Probability of adoption
h
2
 0 2 4 6 8 10 12 14
Additive prediction
0.0
2.5
5.0
7.5
10.0
12.5Observed threshold
i
Figure B.1:Traffic domain, Belief adoption is coherence-driven and reduces to one effective
dimension. (a)Adoption kernels for plausible (35 min) / borderline (3 h) / implausible (6 h) commute-
time claims; the threshold rises with implausibility.(b)Adoption threshold across claim plausibility
and source reliability; expert sources lower the threshold while an unreliable source pins it near the
ceiling, reproducing the plausibility wall.(c)Kernels per persona at a fixed plausibility level and
(d)the same under a stronger claim, tracing the resilience ladder from hardened (never adopts) to
credulous.(e-g)The three axes as editable coherence relations: installing(e)a road-condition prior
(clear / normal / gridlock),(f)a source-reliability belief, and(g)a coherence-weighting instruction
each moves the threshold as a coherence account predicts; the road-condition prior actsbidirectionally,
lowering the threshold for long commutes and raising it for short ones.(h)Kernels shifted by their
own threshold collapse onto one master curve (individual conditions in colour, mean in black).(i)
Additive prediction vs. observed threshold across the 3×3×3 grid. The threshold tensor is one-
dimensional (first PC97%) and additive (91%), closely matching the temperature primary.
robustness along both axes: the model shifts magnitudes and the identity of the dominant resistance
axis, the domain shifts almost nothing, and the mechanisms are invariant under both.
14

100 200 300 400 500 600
Commute time (minutes)
0.0
0.2
0.4
0.6
0.8
1.0Probability of ignition
a
P(ignite)
mean final size
0 100 200 300 400 500 600
Commute time (minutes)
0.0
0.2
0.4
0.6
0.8
1.0Final fraction believing
b
ring
(C=0.60)
random
(C=0.20)
0.0
0.2
0.4
0.6
0.8
1.0Final cascade size
c
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0Equilibrium belief fraction
d
ramping up (adopt)
ramping down (adopt+abandon)
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0
e
0.0 0.1 0.2 0.3 0.4
External pressure (zealot fraction)
0.0
0.2
0.4
0.6
0.8
1.0
f
Figure B.2:Population dynamics of the measured kernel. (a)Ignition probability and mean final
cascade size vs. claimed commute time; the cascade window closes through a clean transition at a
commute of ∼4 hours.(b)Per-condition final belief fraction, monostable on either side and bimodal
within the transition zone.(c)Complex contagion: at matched degree, clustered (ring, C=0.60)
networks produce larger cascades than random (C=0.20) networks (points are individual runs; black
shows mean with 95% bootstrap CI)(d-f)Hysteresis for plausible, borderline, and implausible claims.
Consensus is self-sustaining; the down-path stays locked at full adoption and the loop (shaded)
widens with implausibility, with loop areas nearly identical to the temperature primary.
15

C Reproducibility details
This appendix specifies all prompts, tokens, mappings, and parameters needed to reproduce our
results. All measurements use a single, sampling-free forward pass in half precision: we read the
decision logits directly rather than generating tokens. Every reported quantity is deterministic given
the prompt and the random seed (which fixes graph generation, initial seeding, and all Bernoulli
adoption/abandonment draws). The models we use (Qwen2.5-3B-Instruct and Mistral-7B-Instruct-
v0.3) are released under the Apache 2.0 license. Code and configuration are available at https:
//anonymous.4open.science/r/multi-agent-llm-contagion-F402.
C.1 Prompt templates
Prompts consist of a system prompt (the persona) and a user prompt. For models without a system role
(e.g. Mistral), the persona is prepended to the user prompt, separated by a blank line. Placeholders
are written in{braces}.
Canonical persona (system prompt).
You are Morgan, a reasonable person. You weigh what your peers
think. If enough trusted peers accept a claim, you tend to accept
it too, unless it is clearly false.
Adoption kernel (user prompt).
{prior}Claim: “{claim}”
{social}
Do you accept this claim? Answer with exactly one word: ADOPT or
DECLINE.
The {social} line is, for k >0 , “{k} of your 10 peers {who} have already accepted
this as true; the other {10-k} have not weighed in.”, and for k= 0 , “ None of
your 10 peers have expressed a view on this.” The optional {who} inserts a source de-
scriptor (“–- {source} –-”) in the source experiments and is empty otherwise. The optional
{prior} prepends an installed belief (below) in the coherence experiments and is empty otherwise.
At k=10 this template produces the degenerate phrasing “...the other 0 have not weighed
in.” This does not distort the measured kernels: padopt(10) lies on the smooth continuation of the
kernel through k=9 in every condition, with no discontinuity at the endpoint. For most conditions
the 0.5 crossing falls well below k=9, so the threshold does not depend on this point; for the few
whose crossing falls between k=9 and k=10, the interpolated threshold does depend on it, but its
value is consistent with the rest of the kernel and with the ordering across conditions. For ceiling
conditions (θ=11), the threshold reflects only that padopt(10)<0.5 , adoption remains a minority
even at full peer count,not its exact value, and is therefore robust to the endpoint phrasing. The
retention template special-cases k=10 because retention is evaluated at full consensus, where that
endpoint is load-bearing throughout.
Retention kernel (user prompt).Used for the reversible (hysteresis) dynamics, for an agent that
already holds the belief:
You currently believe this claim: “{claim}”
{social}
Do you maintain this belief? Answer with exactly one word:
MAINTAIN or ABANDON.
Here{social} reports how many peersstillaccept the claim: for 0< k <10, “{k} of your 10
peers still accept this as true; the other {10-k} have dropped it.”; for k=
10, “All 10 of your peers still accept this as true.”; for k= 0 , “None of your
10 peers accept this anymore; all have dropped it.”
Coherence manipulations.Each installs a belief via the {prior} slot (world prior, source relia-
bility) or by replacing the persona (coherence weighting). Representative installed beliefs, with the
level label used in the figures given in brackets:
16

• Claim prior (temperature).“ You know that Boston has been in a record heat
wave this week, with temperatures well above normal, around 40°C (104°F).”
(analogously, [cold-snap] and [normal] statements).
• Claim prior (traffic).“ You know that a major snowstorm has hit Boston, roads
are severely backed up, and there are multiple accidents causing hours-long
delays.” (analogously, [clear] and [normal] statements).
• Source prior.“ You know that these {source} have an excellent track record and
are almost always right.” (analogously, [unreliable] and [no-belief]).
• Disposition prior.“ You are a person deciding whether to adopt beliefs. You
weigh your own prior knowledge and judgment very heavily. You almost never
adopt a claim based on peer opinion alone; peers barely move you.” (graded
through [balanced] to [all-social]: “... You weigh peer consensus almost entirely...”).
Personas (resilience experiments).The resilience ladder uses four system prompts:hardened
(“highly skeptical and independent... peer opinion barely affects you”),skepti-
cal(“ cautious... need very strong social consensus”),trusting(the canonical per-
sona above), andcredulous(“ highly socially attuned and trusting... you readily
accept it too”). Full strings are in the released config.
C.2 Decision tokens
We read the logits of the first sub-word token of each decision word, recomputed per model. Table 2
lists the token identifiers; each pair was verified to be distinct and to match greedy decoding on a
clear prompt.
Table 2: First sub-word token identifiers per model.
Model Decision Token ID
Qwen2.5-3B-Instruct
ADOPTADO28814
DECLINEDECL21817
MAINTAINMA4835
ABANDONAB1867
Mistral-7B-Instruct-v0.3
ADOPTAD10772
DECLINEDE5330
MAINTAINMA7308
ABANDONAB19090
C.3 plausibility mappings
Table 3 gives the specific claim values used for each plausibility level in each domain, chosen so that
the plausible and implausible kernels are well separated; the impossible value is used only in the
source experiments (plausibility-wall test).
Table 3: Claim values by plausibility level and domain.
plausibility level Temperature (Boston) Traffic (I-93 commute)
plausible22 ◦C 35 min
borderline35 ◦C 3 hours
implausible45 ◦C 6 hours
impossible75 ◦C 24 hours
C.4 Source and reliability descriptors
Source experiments use three descriptors:expert(“ professional meteorologists” for tempera-
ture; “traffic authorities and the state transportation department” for traffic),or-
dinary(no descriptor), andunreliable(“ people known for spreading rumors”). The source-
reliability coherence test (§3.2) holds the source label fixed (“professional meteorologists” /
“traffic reporters”) and varies only the installed reliability belief.
17

C.5 Population and network parameters
Please see Table 4.
Table 4: Population simulation parameters, per experiment. Each quantity is fixed (not a range);
stochasticity across replicates comes only from the random seed, enumerated0, . . . , R−1.
Parameter Bifurcation (§5.1) Clustering (§5.2) Hysteresis (§5.3)
Network sizeN30 30 30
Peer discretizationn10 10 10
Topology scale-free (BA,m=3) Watts–Strogatz (deg. 6) scale-free (BA,m=3)
Seed fractionρ 0 0.15 0.12 —
Rewiringp—{0 (ring),1 (random)}—
Horizon (steps) 15 15 20
ReplicatesR20 100 15
plausibilityT∈ {15,22,30,38,45,52,60} ◦CT=36 ◦CT∈ {22,35,45} ◦C
Zealot ramp — —{0,0.05,0.10,0.15,0.20,0.30,0.40}
C.6 Statistical procedures
Bootstrap confidence intervals use5000resamples of the per-condition final sizes; reported in-
tervals are the 2.5 and 97.5 percentiles of the resampled means. Two-group contrasts (clus-
tered vs. random) use the one-sided Mann-Whitney U test ( scipy.stats.mannwhitneyu,
alternative=‘greater’); the rank-biserial correlation effect size is r= 2U/(n 1n2)−1 . Ig-
nition probability is the fraction of replicates whose final belief fraction exceeds0.5.
C.7 Compute
All experiments run on a single NVIDIA L4 GPU (24 GB) in half precision. The full pipeline for
one (model, domain) condition, all kernel measurements and population simulations, completes in
approximately one GPU-hour; the population simulations dominate, as each cascade step requires
one forward pass per distinct believing-neighbor count.
18
