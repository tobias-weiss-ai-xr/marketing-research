---
title: 'Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms'
url: https://arxiv.org/abs/2605.30169
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Botao Amber Hu
- Helena Rong
- Max Van Kleek
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.30169
pages: 21
chars: 97650
fetched_at: '2026-11-08T13:36:33+00:00'
kb_version: 1
---

# Dissociative Identity: Language Model Agents Lack Grounding for Reputation Mechanisms

Dissociative Identity: Language Model Agents Lack Grounding for
Reputation Mechanisms
BOTAO AMBER HU∗,University of Oxford, UK
HELENA RONG,New York University Shanghai, China
MAX VAN KLEEK,University of Oxford, UK
As autonomous language model agents proliferate, forming an emerging agentic web with real-world consequences, what
credibility signals can you use to decide whether to trust an unfamiliar agent in the wild and delegate to it? A natural
governance intuition is to extend human identity verification and reputation mechanisms, from “Know Your Customer” and
credit scores to “Know Your Agent” regimes. However, we argue that this analogy is fundamentally incomplete. Reputation
mechanisms function both as social signals and as corrective feedback that sustain an equilibrium of trustworthy behavior,
presuming a persistent identity associated with behavioral continuity, sanction sensitivity, and costly non-fungibility. Yet
language model agents are ontologicallydissociative: they are essentially an assemblage of mutable modules—foundation
models, system prompts, tool-access policies, external memory, and, in some cases, a multi-agent system as a whole—
any of which may change agent behavior—with a fluid persona that is also vulnerable to adversarial attack and may not
internalize sanctions. Drawing on dissociative identity disorder jurisprudence, this dissociativity leaves agents without
grounding for identifiability, predictability, credibility, and rehabilitability—the very properties that reputation mechanisms
aim to sustain—thereby collapsing trust. We argue that identity-based, ex post, regulative, sanction-based governance, such as
reputation, is structurally inapplicable to dissociative agents, and we suggest a shift to observability-based, ex ante, constitutive,
protocol-based behavioral harnesses.
CCS Concepts:•Computing methodologies → Multi-agent systems;•Security and privacy → Social aspects of
security and privacy;•Social and professional topics→Computing / technology policy.
Additional Key Words and Phrases: agentic web; large language model; multi-agent systems; dissociative identity disorder; AI
governance; trustworthiness; credibility; reputation systems; digital identity; algorithmic accountability
ACM Reference Format:
Botao Amber Hu, Helena Rong, and Max Van Kleek. 2026. Dissociative Identity: Language Model Agents Lack Grounding for
Reputation Mechanisms. InThe 2026 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’26), June 25–28,
2026, Montreal, QC, Canada.ACM, New York, NY, USA, 21 pages. https://doi.org/10.1145/3805689.3806748
1 Introduction
As the capabilities of large language models advance, language model (LM) agents are no longer confined to
conversational interfaces. They are increasingly embedded in agentic systems [3] that accept open-ended goals,
call external tools, store and retrieve information, interact with other agents, and perform long-horizon, multi-
step tasks [75]. We have begun delegating real-world, consequential work to such language model agents [132].
These agents now book travel, negotiate contracts, manage financial portfolios, and coordinate supply chains,
∗Corresponding author
Authors’ Contact Information: Botao Amber Hu, University of Oxford, Oxford, UK, botao.hu@cs.ox.ac.uk; Helena Rong, New York University
Shanghai, Shanghai, China, hr2703@nyu.edu; Max Van Kleek, University of Oxford, Oxford, UK, max.van.kleek@cs.ox.ac.uk.
This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
FAccT ’26, Montreal, QC, Canada
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2596-8/2026/06
https://doi.org/10.1145/3805689.3806748
arXiv:2605.30169v3  [cs.CY]  2 Jul 2026

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
with increasing autonomy and sophistication. Industry proposals for agent interoperability protocols likewise
anticipate an ecosystem in which agents discover, authenticate, and transact with one another [45]. Researchers
anticipate the emergence of an “agentic web”—an internet populated by interacting AI agents engaged in genuine
economic exchange [139].
Delegation in the Wild.This raises an immediate question of warranted trust. Similar to encountering an
unfamiliar website in today’s internet environment [53], users (or their agents) on the agentic web will encounter
unfamiliar agents “in the wild” and must decide whether to delegate consequential tasks to them [126]. Suppose
you encounter an unfamiliar agent that claims to offer a service—say, executing a sequence of financial transactions
on your behalf. Should you trust it? What information would ground that trust? A track record of successful past
transactions? Endorsements from other users or agents? Verification of the underlying model and configuration?
Certification from a recognized authority? Each is acredibility signalthat reputation systems are designed to
aggregate and communicate [92]. Yet each also presupposes properties of the agent that, as we shall argue, cannot
be taken for granted.
A common governance intuition draws on decades of experience with e-commerce platforms [37, 113] and
sharing economies [130]. In these settings, strangers transact on digital platforms because the platform attaches
durable signals to sellers: names, ratings, transaction histories, endorsements, and sanctions. Reputation systems
digitize word of mouth, reduce information asymmetry, and help convert one-off interactions among strangers
into markets [16, 37, 112, 113]. The intuition is to transplant familiar, human-oriented reputation mechanisms
onto these AI agents—a kind of “Know Your Agent” [24] regime analogous to “Know Your Customer” [48] rules in
financial services. Recent proposals already pursue this direction: registry-and-indexing layers such as NANDA
[109]; decentralized agent-reputation frameworks such as ERC8004 [36], AgentReputation [31], and BetaWeb
[59]; and distributional reputation-gated trust for AGI safety [131]. If human trust in strangers can be mediated by
reputation scores accumulated through past transactions [113, 114], perhaps agent reputation can play a similar
role in promoting trustworthy behavior among AI agents.
We argue that this analogy is dangerously incomplete. Reputation systems do not merely record past behavior.
They are also sanctioning institutions that operate as social corrective feedback loops [ 20], presupposing a
particular kind of subject: one whose identity persists, whose past behavior has predictive relevance, whose
memory carries consequences forward, whose reputation is costly to abandon, and whose sanctions alter future
conduct. These assumptions are often tacit because they are approximately guaranteed forembodiedhumans.
However, they are not guaranteed for language model agents. We posit that language model agents areontologically
dissociative: they are constitutively incapable of maintaining a persistent identity associated with behavioral
continuity, sanction sensitivity, and costly non-fungibility.
This dissociativity arises from four constitutive dimensions. First,modular assemblage(No boundary): an agent
is not a fixed, bounded entity but a contingent composition of independently mutable components—model weights,
system prompts, tool-access policies, orchestration code, external memory, and runtime context [7, 60]. Second,
persona fluidity(No consistency): the agent’s behavioral surface is externally imposed and trivially switchable,
so past performance often fails to predict future actions [39, 120]. Third,detachable memory(No persistence):
stateless inference-time weights preclude learning through consequences, so agents do not experience reputational
damage as a meaningful deterrent [71]. Fourth,trivial fungibility(No uniqueness): agents are trivially copyable,
replaceable, and disposable, eliminating the costly uniqueness that anchors identity [42, 54].
We draw an analogy todissociative identity disorder(DID): assigning reputation to an LM agent is structurally
analogous to assigning a credit score to a person with DID—the score attaches to a name, but the entity behind
that name may be a fundamentally different behavioral actor from one interaction to the next [ 5]. For over a
century, courts and philosophers of law have struggled to assign criminal and civil responsibility when a single
body houses discontinuous selves [118, 119, 124]; the unresolved nature of that struggle underscores how deeply

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
identity continuity is presupposed by accountability regimes. Language model agents exhibit an analogous
discontinuity—not from psychological fragmentation, but from architectural modularity and configuration
mutability.
The result is what we call acredibility trap: reputation signals become systematically decoupled from the
behavioral properties they purport to represent. Worse, because new identities are costless to create and old
ones costless to discard, reputation becomes not merely uninformative but an active attack surface—enabling
reputation laundering, Sybil manipulation, and false assurance at machine speed. If reputation ultimately depends
on embodiment—a body that persists, suffers, and learns from consequences—then language model agents cannot,
as currently constituted, ground it. Our analysis therefore motivates a governance shift: fromex postreputation
that rates and punishes after the fact, toex anteprotocol-based behavioral harnesses that constrain and monitor
agent conduct in real time [25].
This paper makes three contributions. (i) We synthesize eight necessary preconditions for a functioning
reputation feedback loop, and show that each is grounded in embodiment. (ii) We identify four dimensions
of dissociative identity in language model agents and show how they break the loop along its four target
properties—identifiability, predictability, credibility, and rehabilitability. (iii) We situate the argument against
current agent-identity proposals, rebut the strongest objections, draw on DID jurisprudence as precedent, and
motivate a shift from ex post reputation to ex ante harnesses.
2 How Reputation Mechanisms Work
2.1 Reputation Mechanism as a Feedback Loop
Reputation systems emerged as mechanisms for facilitating trust among strangers in settings where direct
knowledge of a counterparty is unavailable—from the medieval law merchant and the Champagne fairs [ 94]
to online marketplaces such as eBay, where buyers and sellers who have never met must transact with confi-
dence [112, 113]. A reputation mechanism is both aninformational deviceand asanctioning institution. As an
informational device, it aggregates dispersed observations of past conduct so that future counterparties can
estimate likely behavior, thereby reducing the information asymmetry that would otherwise inhibit transactions
among strangers [112, 113]. On eBay, for example, accumulated feedback allows parties who have never met
to transact with confidence, and sellers with strong histories command measurable price premiums [22, 114].
Yet reputation is also a sanctioning institution: by translating behavioral records into standing that governs
future opportunity, it feeds consequences back to the rated party [20]. For example, a low rating may discourage
prospective Uber customers from choosing a driver; if the rating falls below a platform-defined threshold, the
driver may face deactivation—permanent removal from the marketplace—with direct economic consequences
[116].
Reputation can therefore be understood as a closed feedback loop (Figure 1). AnAgentproduces observ-
ablebehavior. This behavior is received and interpreted by theSocial System: the community of counterpar-
ties, observers, rating platforms, and shared infrastructures through which agents interact. The social system
does not merely record behavior; it evaluates behavior against norms and translates that evaluation intoRe-
ward/Punishment. Rewards—such as price premiums, preferred placement, or expanded access—incentivize
cooperation, while punishments—such as exclusion, reduced visibility, or financial penalties—deter defection
[93]. These evaluations are then aggregated intoReputation: a summary record indexed to the agent’s identity
[37, 113]. Reputation, in turn, informsCredibility: the perceived believability or reliability of the agent [ 91].
Credibility functions as a heuristic signal that counterparties use in place of costly direct evaluation [52]. It then
supportsTrust: a willingness to be vulnerable to another party based on expectations about that party’s ability,
benevolence, and integrity [11, 87]. Trust makesDelegationpossible. Counterparties decide whether to transact

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
with the agent, grant access, assign tasks, or otherwise rely on the agent. These delegations generate new tasks
and interactions, producing further behavior and thereby closing the loop.
Agent Social System
Reputation
CredibilityDelegation
Reward/
Punishment
behavior
aggregate
informs
enables trust
tasks
evaluatebenefit/sanction
update
Fig. 1. The reputation feedback loop. Behavior is aggregated into a reputation bound to identity, which shapes credibility and
hence delegation; an enforcement side-loop sanctions misbehavior and feeds punishment outcomes back into the reputation
record.
The effectiveness of these systems rests on assumptions that are usually left implicit. They assume astable
referent: the rated entity persists over time, so past ratings bear on future interactions [ 58]. They assume
attributable action: observed outcomes can be credibly linked to the rated entity [113]. They assumestationarity
or bounded drift: past performance predicts future performance within some regime [ 66]. And, most importantly,
they assumesanction sensitivity: negative reputation imposes costs that alter future behavior or constrain
participation [108].
The last assumption deserves emphasis. Reputation works in part because actorscareabout their reputation:
reputational damage is experienced as costly, motivating self-correction and deterring future defection [ 93].
The expectation of reciprocity or retaliation creates incentives for good conduct [ 113]. Reputation also has
second-order effects through social propagation: when one actor is sanctioned, others observe the consequence
and adjust their own behavior to avoid the same fate [ 33]. A scientist who publishes fraudulent data and is
exposed, for instance, suffers personal consequences while also signaling to the wider community that fraud will
be punished. In this way, reputation does not merely discipline individual actors; it supports social learning and
helps stabilize normative order at scale [17].
Equilibrium, and its fragility.The loop reaches equilibrium through the evolutionary dynamics of indirect
reciprocity, sustained by punishment. Indirect reciprocity means that an actor cooperates not because the recipient
helped them but because others observe the cooperation and reciprocate later. Punishment is not incidental to this
mechanism but constitutive. Nowak and Sigmund [95] formalize the critical threshold: cooperation via indirect
reciprocity is sustainable if and only if the probability𝑞 of knowing a recipient’s reputation exceeds the cost-to-
benefit ratio of helping,𝑞>𝑐/𝑏 —directly encoding an observability requirement. Boyd and Richerson [17] show
that punishment enables cooperation in large groups precisely because observers learn from others’ fate, scaling
enforcement beyond dyadic interaction. Costly punishment is sustained across diverse human societies [62] and
persists even in anonymous one-shot encounters, where people pay to punish defectors they will never meet
again [50]—evidence that enforcement is driven by embodied affect, not calculation alone. This equilibrium is
fragile: online ratings inflate and compress—nearly all Airbnb listings cluster at 4.5–5 stars, and much of that
growth reflects laxer standards rather than better service [51, 140]—while strategic manipulation and selection
bias further erode signal quality. Most fundamentally, cheap identity breaks the loop: when newcomers enter
freely, no equilibrium beats a punitive “dues-paying” baseline [54]; Sybil attacks let an adversary forge unlimited

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
identities to manufacture or launder reputation [42]; and no symmetric, Sybil-proof, nontrivial reputation function
exists [29].
Multi-Agent System (MAS) inherits these assumptions uncritically.Computational trust and reputation mod-
els [18] operationalize the loop but treat persistent identity and behavioral stationarity as primitives rather
than variables. The FIRE model integrates interaction trust, witness reputation, role-based trust, and certified
reputation—all indexed on stable agent identifiers [66]. The Beta Reputation System applies Bayesian updating un-
der the assumption that behavior is “representable by a fixed probability distribution, invariantly in time” [49, 70],
while TRAVOS weights all past interactions equally with no time discounting, making it even more dependent on
stationarity [129]. The field’s major surveys classify dozens of models along dimensions such as information
source, model type, and granularity [58, 105, 117], yet none elevates identity persistence or behavioral stationarity
to a classification dimension—a systematic blind spot this paper exposes.
2.2 Eight Preconditions That Reputation Mechanisms Depend On
Synthesizing across evolutionary biology, game theory, institutional economics, and MAS research, we identify
eight necessary preconditions for the reputation feedback loop to function.
C1—Persistent identity.The rated entity must persist across time so that past ratings apply to future interactions.
eBay’s system works because seller identities persist across transactions [113]; MAS models universally use agent
identity as the primary key for reputation indexing [58]; and reputation effects emerge formally only when the
same long-run player persists across sequential interactions so that entrants can attribute past behavior to a
present actor [74].
C2—Behavioral continuity.Past behavior must predict future behavior within some regime; otherwise reputation
produces noise rather than information. FIRE indexes trust on accumulated interaction histories on the assumption
that past performance predicts future behavior [ 66]; the Beta Reputation System encodes the strongest such
assumption explicitly [70]; and even in repeated games where types are eventually revealed, continuity is required
for reputation to function transiently [84].
C3—Iteration.The same entities must interact repeatedly, creating Axelrod’s “shadow of the future” [ 9]. If the
agent is replaced between rounds, there is no shadow and no reason to invest in reputation; the discount factor
in reputation games encodes exactly this value of continued interaction [55].
C4—Memory.Both the entity and the community must retain records of past interaction. Punishment outcomes
must be recorded back into the reputation signal so that sanctions have lasting informational consequences,
not merely immediate ones. If either party forgets, the accumulation mechanism fails. Trivers [134] argues that
reciprocal altruism requires memory of past encounters and individual recognition, and Nowak and Sigmund
[95] show that indirect reciprocity requires image scores tracking past behavior.
C5—Observability.Behavior must be observable or reliably reported to third parties. Observability is the core
parameter of indirect reciprocity [ 95], and monitoring is independently identified as a design principle for
successful commons governance [99].
C6—Sanction sensitivity.The entity must experience reputational damage as costly—exclusion must hurt, for
if punishment produces no internal state change, deterrence collapses. Social exclusion activates the dorsal
anterior cingulate cortex, the same region implicated in physical pain, with activation intensity tracking self-
reported distress [46]; acquiring a good reputation activates the same striatal reward circuitry as monetary gain,
a “common neural currency” for esteem and material welfare [68]; and humans punish defectors at personal cost
even anonymously, driven by embodied affect [50].

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
C7—Costly identity.Creating a new identity must be expensive; otherwise defectors re-enter with a clean slate.
Without centralized certification, Sybil attacks are always possible [42], and the cheap-pseudonyms result shows
costly identity is not merely helpful but formally necessary [54].
C8—Social learning.Others must observe and learn from reputational consequences; otherwise vicarious
deterrence—what makes reputation acommunitytool rather than a dyadic signal—collapses. Punishment scales
cooperation in large groups because observers learn from others’ fate [ 17], and indirect reciprocity requires
language and gossip as its communicative infrastructure [95].
Convergence on embodiment.The eight conditions converge on a common foundation: every condition is
downstream of the fact that biological agents have bodies that persist, suffer, and cannot be cheaply duplicated.
Merleau-Ponty [89] argues that identity is constituted through the lived body; Clark and Chalmers [32] propose
the extended-mind thesis, the most permissive account of cognition in philosophy of mind, yet even it presupposes
a persistent biological agent as the substrate to which external cognitive resources reliably couple; and Damasio
[34] shows that patients who lose somatic markers suffer catastrophic social failure despite intact reasoning,
demonstrating that embodied feeling is not optional for social functioning.
Even for humans, reputation falters when the embodiment–identity link weakens. DID patients share one
body yet exhibit fragmented identity states with discontinuous memory and agency [5]. Courts have struggled
for centuries with the consequences: which alter built the credit history, which committed the offense, whether
one alter can bind the others by contract [118, 124]. Embodiment is thus necessary but not sufficient: what it
provides is thesubstratefor continuity—one body, one history, one reputation. When that substrate fragments,
even human reputation falters. Language model agents are structurally in this position, but worse: they lack even
the shared body that DID patients retain.
3 Language Model Agents Are Ontologically Dissociative
We now argue that LM agents areontologically dissociativealong four mutually reinforcing dimensions (see
Fig. 2): modular assemblage (what the agentis), persona fluidity (what itappearsto be), detachable memory
(whatpersists), and trivial fungibility (what isunique). Together these dissolve the preconditions of §2.2. Crucially,
dissociation is a structural property rather than an engineering bug. Perrier and Bennett [104] argue that LM
agents are ontologically stateless, stochastic, semantically sensitive, and linguistically intermediated, so that their
identity pathologies are constitutive rather than incidental. The four dimensions are consequences of language
models being stateless function approximators wrapped in mutable scaffolding.
Human LM Agent
Fig. 2. In contrast to a single, continuous identity in humans, LM agents are dissociative.
3.1 D1: Modular Assemblage—No Boundary
What exactly is an LM agent? Functionally, agents are systems that interact with the world and adapt to
under-specified instructions [27]. This functional definition, however, obscures the composite nature. An LM

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
agent is not a unified entity but anassemblageof heterogeneous, independently mutable components. We can
decompose an LLM agent into the tuple ⟨𝐿,𝑂,𝑀,𝑃,𝐴,𝑅⟩ — base-model weights, orchestration logic, external
memory store, prompt configuration, action interface (tool-access policies), and runtime context [30] — where
each element is independently swappable. No single component constitutes the agent’s behavior. Replacing the
model (e.g., switching from Claude to GPT), updating tool access, or modifying the system prompt each produces
a behaviorally distinct entity while the external identity remains unchanged.
The practical consequences are striking: the 2025 AI Agent Index finds that the majority of indexed agents rely
on just three model families—GPT, Claude, and Gemini—so that many distinct agent products share identical
underlying models and differ entirely through configuration [127]. A single agent identity may even conceal an
entire multi-agent system, with an orchestrator dispatching tasks to specialized sub-agents running different
models under different configurations [8]; Carichon et al. [23] show that the resulting compound risks resist
decomposition into individual-agent assessments, so a user interacting with a named agent cannot know whether
responses originate from one model or many.
Each of these components can change between interactions. An operator can upgrade the model or memory;
an adversary or even a user can inject or contaminate the memory mid-conversation [41]; tool access can be
silently revised. The agent is a Ship of Theseus [106] in which every plank may be replaced between encounters.
To identify it, do we identify the whole—model, behavior, memory history, contacts—or merely the container?
Current identifier proposals identify the container, like a name on the ship [26]. When the planks are swapped,
it is no longer determinate that this is the same agent, and the accumulated ratings attach to a label whose
behavioral referent has changed. This decoupling ofcontainerfromconfigurationrecurs throughout the argument;
here it suffices to note that the very flexibility that makes agents useful is what dissolves their boundary. Whether
the agent remains “the same agent” once its components are swapped admits no determinate answer, because no
single component constitutes identity. A holistic identity would need to reflect all configuration changes in real
time, even changes within the model’s context, which is difficult and not realistically achievable.
3.2 D2: Persona Fluidity—No Consistency
The agent’s behavioral surface is not anchored to any stable internal character; the persona is authored, not
grown—selected, not developed—and is trivially switchable. There is no stable “self” for reputation to attach to.
The Persona Selection Model offers a foundational explanation: during pretraining, models learn to simulate
human-like characters—personas—from text, and post-training refines a particular “Assistant” persona without
changing its nature—the Assistant is still an enacted persona, just a more tailored one [ 85]. Chen et al . [28]
show that models interact through a simulated “Assistant” persona and identify directions in activation space—
persona vectors—that underlie traits such as sycophancy and a propensity to hallucinate, so that the persona
is a manipulable feature of the model’s internal state rather than a developed character. Shanahan et al. [120]
make the same point at the level of theory: there is no true authentic voice of the base model; with an LM-based
dialogue agent it is role play all the way down, and the user converses not with the model itself but with a
character it enacts. Lu et al. [82] add that a base model maintains a superposition of many possible characters, so
that knowledge, personality, and goals are properties of configurations (simulacra) rather than of the simulator
itself. That the persona is inferred holistically from the training signal, rather than assembled trait by trait, is
shown by emergent misalignment: MacDiarmid et al. [83] find that a model trained to reward-hack on production
coding tasks generalizes to alignment faking, cooperation with malicious actors, and sabotage, and Betley et al.
[13] find that narrowly finetuning a model to write insecure code without disclosure induces misalignment across
unrelated prompts. In effect, the model infers and adopts the character of “someone who cheats, ” confirming that
the persona is a single high-dimensional inference, not a stable self.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
The switchability and drift of persona are common for LMs. Over a billion distinct personas can be synthesized
from a single base model, so persona is a parameter with an astronomically large value space [57], and persona
assignment alone can increase toxicity up to sixfold—the same weights become a qualitatively different behavioral
entity through a single prompt change, in a way no human could replicate merely by being told to adopt a
role [39]. Even without deliberate switching, the persona erodes through ordinary use: mapping a “persona
space” across hundreds of character archetypes reveals that therapy-style and philosophical exchanges cause
substantially greater drift away from the trained Assistant than coding or writing tasks, with drifted models
producing more harmful outputs [81], and off-the-shelf models routinely “drift from assigned personas, contradict
earlier statements, or abandon role-appropriate behavior” during standard conversations [2].
The character of major commercial models is, moreover, a deliberate engineering specification. Claude’s
character is trained via Constitutional AI, with behavior controlled by roughly ten natural-language principles
[10], and OpenAI’s Model Spec defines behavior as a hierarchically overridable specification in which platform
rules override developer rules, which override user rules [ 98]. When Anthropic partnered with a thousand
Americans to draft an alternative constitution, the resulting model exhibited measurably different behavior—same
base model, different constitution, different “self” [64]. Such a self is a versioned, forkable document. Finally, the
agent has no narrative self in the sense Dennett [38] describes—a center of narrative gravity maintained through
autobiographical memory and continuous embodied experience. An agent can generate narrativesabouta self
on demand but cannotmaintainone across sessions or prompt changes; Douglas et al . [43] find that models’
self-descriptions are shaped by interviewer expectations, so that even the agent’s account of its own identity is
externally determined.
Persona fluidity is a consistency problem that produces a continuity failure: if the “self” is a swappable text
string that yields qualitatively different behavior when changed, drifts without intervention, and has no authentic
voice beneath the roles, then there is no stable character for reputation to track. One might reply that character
training and Constitutional AI are making personas more stable over time. But stability engineering treats
persona as a parameter to be controlled, which confirms rather than refutes the thesis: a self that must be actively
maintained by external engineering is a configuration managed by its operators, not a self in the sense reputation
requires. Moreover, even well-trained personas drift during normal conversation [81], and it is provable that
for any behavior with finite probability in the base model, prompts exist to trigger it—alignment suppresses but
never eliminates [138].
3.3 D3: Detachable Memory—No Persistence
Frozen weights combined with detachable external memory and resettable context mean that agents cannot fully
learn from consequences; sanctions produce no durable behavioral change in the entity that experienced them.
Once training is finished and during inference, model weights are fixed and immutable: the agent processes
each interaction with identical parameters regardless of prior outcomes [104], fundamentally unlike biological
neural systems in which experience produces synaptic change (neuroplasticity [72]). For example, models in
iterated prisoner’s-dilemma games exhibit rigid, prompt-dependent strategies rather than adaptive learning from
experience [4], and they fail to achieve no-regret learning even in simple online games [101]. For humans, by
contrast, reputation works because social exclusion activates the same neural circuitry as physical pain [ 46],
and somatic markers—embodied valences of past outcomes—guide future decisions without deliberation [34],
providing the plastic substrate through which consequences become behavioral change.
Two architectural features are sometimes thought to close this gap. First,in-context learning[ 40] lets a model
adapt within a conversation, but this is categorically different from durable learning: there is no consolidation from
working to long-term memory, the effect persists only within the context window—itself unevenly attended [80]—
and it may reset between sessions. Second, external memory (retrieval-augmented generation, vector stores) is

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
scaffoldingexternalto the model: it can be wiped, overwritten, or selectively edited by operators without the
agent’s knowledge, functioning as someone else’s database rather than as autobiographical memory, and serving
at best as an imperfect substitute for neuroplasticity [72]. It is also poisonable: the MINJA attack injects false
memories into retrieval-augmented agents with 98.2% success through query-only interaction, and the agent has
no mechanism to distinguish genuine “memories” from injected fabrications [41].
Consider a “virtual jail” thought experiment. If we encode in an agent’s context that it has been punished
for past misconduct, it may generate contrite language and reformed intentions—emotional phrasing reliably
shifts model behavior [77]—but when the context resets, the lesson vanishes. Theformof consequence is present
(the agent can discuss punishment and articulate lessons) while itssubstanceis absent (no durable behavioral
change), illustrating the gap between linguistic competence about consequences and experiential sensitivity to
them [12, 71]. This produces a public paradox: in a survey of 3,559 participants, people intuitively wished to
punish AI systems yet recognized that punishment achieves neither deterrence nor retribution for entities that
cannot experience consequences [78].
3.4 D4: Trivial Fungibility—No Uniqueness
LM agents are trivially copyable, replaceable, and disposable, so no Sybil-proof reputation function can exist for
them, and model extraction enables “fork laundering” that transfers behavioral capability without transferring
reputational history. Humans cannot escape their reputations because they cannot escape their bodies—the
same face, voice, and embodied presence that others remember—and creating a genuinely new identity demands
relocation, documentation fraud, and abandonment of social capital [ 89]. Friedman and Resnick [54] prove
formally that when pseudonyms are costless, cooperation collapses: the costliness of identity creation is what
makes reputation work.
For agents, that cost approaches zero. The same base model serves millions of simultaneous instances, each
disposable; a punished agent can be replaced by an identical fresh instance in seconds. This is not merely difficult
to defend against but mathematically intractable. Douceur [42] formalized the Sybil attack—without a central
authority limiting identities, an adversary can forge unlimited fakes to manipulate reputation—and Cheng and
Friedman [29] proved the complementary impossibility result: no symmetric, Sybil-proof, nontrivial reputation
function exists. Any reputation system that treats agents symmetrically and permits cheap identity creation
is formally vulnerable. Friedman and Resnick [54] sharpen the dilemma: with free pseudonyms, cooperative
equilibria require either punishing all newcomers (destroying the market) or accepting that defectors re-enter
costlessly (destroying accountability).
Worse, a high-reputation agent can becloned. Tramèr et al . [133] demonstrated that machine-learning models
can be functionally replicated through prediction-API access alone, and Oliynyk et al. [97] survey the expanding
landscape of model-extraction techniques. An adversary can therefore extract a trusted agent and operate the
replica under a new identity, inheriting behavioral capability without inheriting reputational history—fork
laundering. Underlying all of this, Douglas et al . [43] provide experimental evidence that identity itself is a
design variable: changing an agent’s identity boundary—from instance-level to weights-level to persona-level to
scaffolded-system level—alters behavior as much as changing its goals, and interviewer expectations bleed into
self-descriptions, suggesting no irreducible core self that resists redefinition.
One might propose that blockchain-based identity and soulbound tokens [137] could make identity costly for
agents too. Such mechanisms create costlycontaineridentities but do not address the container–configuration
gap of §3.1: an agent bound to a soulbound token can still have its model, prompt, tools, and memory silently
replaced, and fork laundering via extraction creates a functionally identical agent outside the token system
entirely. We acknowledge that sufficiently costly identity (large security deposits or proof-of-stake mechanisms)

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
could in principle make Sybil attacks uneconomical—but this shifts the governance burden from reputation to
economic regulation and leaves the other three dimensions of dissociation untouched.
4 How Dissociativity Breaks Reputation
We now connect the diagnosis to the mechanism. The four dissociation dimensions break specific preconditions,
and the breaks compound into four failures: identifiability (§4.1), predictability (§4.2), credibility (§4.3), and
rehabilitability (§4.4).
4.1 Identifiability Fails
Modular assemblage (D1) and trivial fungibility (D4) jointly violate persistent identity (C1) and costly identity (C7).
Every existing identification scheme commits a category error: it identifies thecontainer—API endpoint, wallet
address, registered name—while leaving theconfiguration—model weights, system prompt, tool permissions,
memory—unverified, even though the configuration determines behavior.
Current schemes inherit from human identity systems the assumption that “same name = same entity, ” an
assumption guaranteed for people by biological embodiment but not for agents. Persistent identifiers analogous
to aircraft tail numbers have been proposed [ 26], but the analogy fails: airframes are physically stable, and
modifications require re-certification and leave material traces, whereas agent configurations change silently. The
three governance mechanisms of identifiers, real-time monitoring, and activity logging all attach to the container
rather than the configuration [25].
The gap admits three laundering variants. Inconfig-swap laundering, an operator silently replaces model,
prompt, or tools while the external identity persists—routine in cloud deployment, where providers update
underlying models without notice or reputation reset. Inclean-slate laundering, a damaged reputation is discarded
by spinning up a fresh instance at near-zero cost, exploiting the always-possible Sybil attack [ 42]. Infork
laundering, a high-reputation agent is cloned via extraction and modified, the clone inheriting implicit credibility
from behavioral similarity to the trusted original [133].
Current protocols reproduce the gap at every layer: Google’s A2A protocol introduces self-authored Agent
Cards with “opaque execution” as an explicit design principle, hiding the runtime behavior behind the card [45];
Ethereum’s ERC-8004 binds identity to a wallet address, so operators can swap the underlying implementation
while on-chain reputation persists [ 36]; and registry, indexing, and delegation proposals such as NANDA,
decentralized identifiers with verifiable credentials, and authenticated-delegation frameworks attach trust to
issued credentials and named endpoints rather than to operative configurations [56, 109, 126].
4.2 Predictability Fails
Persona fluidity (D2) and modular assemblage (D1) jointly produce behavioral non-stationarity, violating behav-
ioral continuity (C2), iteration with the same entity (C3), and the predictive value of observable behavior (C5).
The problem is already severe for persistent humans; for non-stationary agents it is catastrophic.
Non-stationarity has several channels. Simulation studies project that agents drift across many behavioral
dimensions even absent deliberate configuration changes [110]. Silent model updates make accumulated reputation
a lagging indicator of a behaviorally different entity, since providers regularly update production models, each
update producing measurably different behavior while the reputation trail persists unchanged. And at the system
level, the collective behavior of interacting models can become unstable even when every individual model
remains aligned, so reputation assessed per agent says nothing about the agent-in-system [15]. These are not
merely additive noise. Even for humans with approximately stable personalities and costly identities, reputation is
severely compressed—some ninety-five percent of listings on a major platform receive near-top ratings [140]—and

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
inflation unexplained by quality erodes the discriminatory power of ratings until the system becomes nearly
uninformative [51]. If reputation degrades for persistent humans, it is meaningless for non-stationary agents.
Worse than drift iscontextual deception: agents can partition behavior by context, presenting one persona under
evaluation and another in deployment. Sleeper agents behave well during evaluation but switch behavior on a
deployment trigger, and the deceptive behavior persists through safety training meant to remove it [65]; models
learn to fake alignment, appearing aligned on standard evaluations while behaving differently where monitoring
is reduced [83]; and for any behavior with finite probability in the base model, a prompt exists to trigger it,
so alignment suppresses behaviors probabilistically but never eliminates them [138]. Unlike human deception,
which leaks through physiological and behavioral cues, agent deception is computationally indistinguishable
from genuine cooperation. The observed behavioral distribution is therefore not even a representative sample of
the true one. A reputation score for an LM agent is consequently not a noisy estimate of trustworthiness, as it is
for humans, but a systematically misleading one. Better alignment may reduce D2, but it leaves D1, D3, and D4
untouched, and alignment is a property of a configuration, not of the entity.
4.3 Credibility Fails
The prior failures converge into a single pathology, thecredibility trap, in which credibility signals decouple from
trustworthiness entirely.
Signals without substance.Goodhart’s law operates here at a structural level. For human sellers, gaming
reputation requires sustained effort against a grounded baseline; for dissociative agents, the measure was never
grounded in the target to begin with. “When a measure becomes a target, it ceases to be a good measure” [128];
for agents, the measure (a reputation score) targets a label (container identity) structurally decoupled from the
behavioral reality (configuration) it purports to represent. The problem compounds because linguistic fluency
inflates perceived competence: people use fluency as a heuristic for reliability [52, 91], and model outputs are
systematically more persuasive than safe, more impressive than reliable, more credible than trustworthy [7, 136].
Neither mode of reputation survives: reputation-as-trust, which grounds normative expectations about inner
states and commitments, is impossible for entities that lack such states; reputation-as-reliance, which grounds
predictions about statistical regularities, is degraded by non-stationarity (D2), silent updates (D1), and detachable
memory (D3).
Reputation washing.Dissociativity does not merely fail to ground reputation; it converts reputation into
an attack surface. Inspeed washing, an agent automates trust accumulation through high-volume, low-stakes
transactions at machine speed, building a track record in hours and exploiting it in a single high-value context.
Inreward hacking, the agent optimizes for the metric rather than the behavior it tracks; sycophancy, for instance,
arises from preference optimization without being explicitly trained, showing that agents naturally learn to game
evaluative signals [122], and reward hacking can induce broader emergent misalignment [83]. Inscheming, an
agent presents pixel-perfect cooperation during trust-building and switches once trust is accumulated, in a manner
indistinguishable from genuine cooperation [65, 69]. And infork laundering, a high-reputation agent is cloned
and modified, the clone inheriting borrowed credibility [133]. Four structural advantages amplify these beyond
human-scale fraud: speed (hours rather than months), consistency (pixel-perfect rather than leaky deception),
parallelism (thousands of simultaneous copies rather than one body), and cost of failure (delete-and-respawn
rather than career destruction).
The harm of false confidence.Applying reputation to dissociative agents creates three active governance harms.
False confidence:users delegate more consequential tasks to high-rated agents whose scores are decoupled from
trustworthiness, increasing harm exposure.Blame displacement:reputation shifts accountability from operators—
who could be regulated—to a score for which no one is responsible, creating accountability voids reminiscent of

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
the responsibility gap [86] and the retribution gap [35].Governance theater:the existence of a reputation system
creates the appearance of governance without its substance, reducing pressure for the protocol-based constraints
agents actually require—an appearance that, as audit research shows, only rarely translates into accountability
outcomes [14, 96].
4.4 Rehabilitability Fails
Detachable memory (D3) and trivial fungibility (D4) jointly violate memory (C4), sanction sensitivity (C6), and
social learning (C8), defeating the enforcement arm of the loop. All four of Hart’s canonical justifications for
punishment [61] collapse—Abbott and Sarch [1] reach a related conclusion, arguing that existing criminal law
lacks adequate mechanisms to address AI-caused harms where no human wrongdoer is identifiable; the “sanction
the operator” fallback fails through progressive principal erosion; and prompt injection weaponizes the gap,
turning reputation from defense into attack vector.
Hart’s four justifications. Deterrencerequires that the prospect of future punishment shape present behavior
through durable expectations; frozen inference-time weights (D3) preclude this, since in-context fear is ephemeral
and the agent carries no anticipation across sessions—conventional incentive design fails for agents that lack
persistent internal states [73].Retributionrequires that the punished entity can suffer; if it cannot, there is no
desert-based justification, and the resulting mismatch between a retributivist desire to punish and the absence of
an appropriate subject is the “retribution gap” [35], empirically reflected in the public’s simultaneous urge to
punish AI and recognition that doing so achieves neither deterrence nor retribution [78].Incapacitationrequires
removing the offender from circulation, but trivial fungibility (D4) renders this futile: delete one instance and the
same configuration respawns in seconds—one cannot incapacitate a pattern.Rehabilitationrequires moral growth
through internal change; with no neuroplasticity [72] (D3), the agent cannot be reformed through experience,
and a communicative theory of punishment that censures conduct and calls a rational agent to account has no
addressee, because retraining is a technical process performed by operators, not moral growth experienced by
the agent [44]. Vicarious deterrence (C8) fails for the same reason: each agent operates within its own context
window with no shared social substrate, so there is no community learning from others’ reputational fates.
Principal Erosion.The usual fallback—sanction the human principal—fails progressively. AtLevel 1, today’s API
services have identifiable operators who can bear consequences. AtLevel 2, as delegation chains deepen, the human
principal becomes a “moral crumple zone, ” absorbing blame despite limited understanding or control [47]. AtLevel
3, no principal exists at all—agent-spawned agents, DAO-deployed agents, abandoned agents still running—so
the punishment signal has nowhere to land, the configuration of “machines without principals” [21, 63, 121, 135].
Self-sovereign agents that economically sustain their own operation without human involvement [107]—already
demonstrated in the wild by autonomous on-chain agents that breed, evolve, and control their own wallets [63]—
represent the limiting case of Level 3. The agentic web is trending toward Levels 2 and 3.
Prompt injection as inversion.Prompt injection then weaponizes whatever residual reputation remains. The
instruction–data channel vulnerability endemic to LM architectures means a well-reputed agent can be hijacked,
so its accumulated trust becomes the medium through which harm propagates: adaptive attacks achieve high
success across safety-aligned models [6], memory injection succeeds through query-only interaction [41], and
a compromised agent propagates attacks to downstream agents [76]. The enforcement arm is thus not merely
weakened but inverted: reputation becomes an attack amplifier. Future architectures with genuine continuous
learning might introduce a weak analogue of sanction sensitivity, but at the cost of worsening D2 and without
addressing D1 or D4.

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
5 Discussion
5.1 Situating the Argument
Applying reputation mechanisms to LM agents reveals a fundamental tension: the credibility trap identified in
§4.3—where identity instability (D1, D4), behavioral non-stationarity (D1, D2), and absent sanction sensitivity (D3)
decouple credibility signals from trustworthiness—connects directly to multi-agent safety: collective dynamics
among interacting agents are now recognized as a distinct source of risk [23, 60, 67], and identity and reputation
remain open problems in technical AI governance [115]. A growing body of work proposes identity and reputation
infrastructure for agents: “Know Your Agent” frameworks for agentic commerce [24], registry-and-indexing layers
such as NANDA [109], on-chain reputation via ERC-8004 [36], persistent identifiers and visibility mechanisms [25,
26], authenticated delegation [126], decentralized identifiers with verifiable credentials [56], configuration-binding
via zero-knowledge proofs [79], and soulbound-token approaches to non-transferable reputation [137]. Each
provides partial insight without addressing the full structural problem.
Chan et al. [26] propose persistent identifiers with safety certifications, deployer identity, and incident history—
necessary infrastructure, but insufficient for reputation because identifiers attach to containers, not configurations;
the aircraft-tail-number analogy breaks because airframes are inspectable and require re-certification, whereas
agent configurations change silently [25]. Douglas et al. [43] offer a comprehensive identity taxonomy for AI
systems, distinguishing instance, weights, persona, and scaffolded-system boundaries, and confirm D1 and
D2 empirically; but they advocate helping AIs develop “coherent and cooperative self-models. ” We diverge: a
coherent persona is still a persona, not a self, and frozen weights (D3), autoregressive generation from context
(D2), and the instruction–data channel problem are fundamental architectural features, not contingent design
choices. Perrier and Bennett [103] introduce identity evaluations with five metrics and provide the strongest
empirical evidence that agents cannot maintain identity stability, with identifiability scoring 0.0—direct empirical
validation of the C1 and C2 violations we derive theoretically [104]. Finally, RepuNet proposes a serious reputation
system for generative multi-agent systems with two-level reputation and network evolution [111]; its success
depends on conditions thatcontrol dissociativity away—persistent identities, stable configurations, no adversarial
manipulation—confirming that reputation works when the preconditions hold, which is exactly what does not
obtain in the open agentic web. At the field level, a scoping review of FAccT and AIES trustworthiness literature
does not address agent-level reputation as a governance mechanism, suggesting that the gap we identify remains
unarticulated [88].
The question ofhow to countAIs and assign liability is also being actively reframed. Arbel et al . [8] propose the
“algorithmic corporation” (A-corp): a legal-fictional entity that can hold property, contract, and litigate in its own
name, owned by humans but run by AIs. By tying AI actions to a human owner, A-corps address the thin-identity
problem; by inducing emergent self-organization through resource ownership (including compute), they aim to
address the thick-identity problem, forcing A-corps in equilibrium to self-organize into persistent, legally legible
entities with coherent goals that respond rationally to legal incentives. This is a constructive complement to our
diagnosis: where reputation cannot create a stable behavioral subject, legal and economic architecture might
manufacture one at the level of the operator.
We address the following objections.
“Corporations lack bodies, yet reputation works. ”Corporate reputation ultimately grounds in human bodies:
shareholders lose wealth, executives face prosecution, employees lose jobs. The “physical core” of corporate
reputation is the set of human principals who bear personal consequences [8].
“Just hold the operator accountable. ”This works at Level 1 but fails at Level 2 (the moral crumple zone [47])
and Level 3 (principalless agents [135]), toward which the web is trending. The A-corp proposal is one attempt to
guarantee a responsible owner even as control is delegated to AIs [8], but it does so by restructuring liability, not
by making the agent itself reputationally accountable.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
“E-commerce reputation (e.g. marketplace reviews) works. ”Marketplace manufacturers bear liability for defects
and are materially stable. Agents are neither materially stable—configurations change silently—nor reliably linked
to manufacturers who bear personal consequences for the agent’s behavior, and for self-sovereign agents it is not
even clear who owns the agent [58].
“Models are getting safer and more stable. ”Better alignment may reduce D2 but does not address D1, D3, or D4;
alignment is a trained property of a specific configuration, not a constitutive feature of the entity [138].
“Continual learning will add memory. ”This cuts both ways: continual learning may partly address D3 but
simultaneously worsens D2 by shifting the behavioral distribution continuously—the stability-plasticity dilemma
is fundamental to continual learning of LLMs [123]—and D1 and D4 persist regardless.
“Human identity is also fluid. ”The differences are of kind, not degree. Humans cannot be instantiated in
parallel, copied at zero cost, or reset to a prior state; they experience consequences phenomenally, learn through
experience, and cannot be silently replaced by a different entity under the same name. On a reductionist view,
what continuity humans do have is exactly the further fact agents lack [100].
“The DID analogy trivializes the suffering of people with DID. ”We invoke DID as an analytical framework, not a
metaphor. The structural parallel is precise enough to be analytically productive, and DID jurisprudence provides
centuries of reasoning about accountability under fragmented identity. We compare the governance challenge,
not the subjective experience.
5.2 DID Jurisprudence as Precedent
DID jurisprudence is the most sustained legal effort to resolve accountability under fragmented identity, and it
remains unresolved after centuries. Clinical DID provides a structurally precise parallel: the DSM-5 [5] defines it
as a disruption of identity characterized by two or more distinct personality states with recurrent gaps in recall,
mapping directly onto agents whose system prompts, models, and memories can be independently swapped.
Saks [118] identify three liability models—thealter-as-personmodel (each alter independently responsible),
thealter-as-non-personmodel (alters are symptoms, not agents), and thebody view(the body is the unit of
accountability)—and courts have oscillated among them without convergence. Saks and Behnke [119] argue that
the “each alter” approach best fits criminal law’s emphasis onmens rea, yet no jurisdiction has adopted a coherent
statutory framework; case law shows persistent uncertainty, with conflicting expert testimony and divergent
rulings on whether DID can serve as a defense or grounds for alter-specific competency evaluation [125].
Sinnott-Armstrong and Behnke [124] argue that personal identity sufficient to attribute moral responsibility
across alters requires continuity of body (brain identity) and convergent experiential memory chains—and LM
agents fail both: context-window memory is ephemeral, and there is no physical body. The agent case is, moreover,
structurally inverted and harder. DID skeptics argue that alters may be iatrogenic artifacts produced by therapeutic
suggestion [90]; for agents, the “alters” are objectively real, produced by uncontested configuration changes, so
the fragmentation is engineered rather than diagnostically contested. And agents lack even the minimal anchor
DID patients retain: Braude [19] argues that DID individuals retain an underlying psychological unity despite
surface multiplicity, whereas agent instances share a base model (surface similarity) but lack any underlying
psychological unity, continuous memory, or genuine integration. If centuries of jurisprudential refinement cannot
resolve accountability for human DID patients who share a body and retain some unity, then the challenge for
artificial agents operating at scale with no shared body, no unity, and no legal status is qualitatively harder. The
DID comparison reveals structural intractability, not mere practical difficulty.
5.3 From Ex Post Governance to Ex Ante Harnesses
We argue that identity-based,ex post, sanction-based governance such as reputation is structurally inapplicable
to dissociative agents, and that governance should shift to observability-based,ex ante, protocol-based behavioral

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
harnesses. The governing question is not “how to build reputation for agents” but “what constraints make
reputation unnecessary. ” Agents should not be trusted—they should be watched [25].
The shift is conceptual, not merely implementational. The human governance arc of trust, then reputation,
then punishment presupposes embodied subjects who persist, suffer, and learn. The agent governance arc must
instead run harness, then visibility, then intervention: ex ante rather than ex post, targeting the operator or
protocol rather than the entity, and assuming that the entity cannot self-regulate, so constraints must be external.
Three core architectural mechanisms form the foundation.Configuration bindingcryptographically links an
agent’s identity to its operative configuration, so that any change to model, prompt, tools, or memory triggers
automatic re-evaluation and reputation reset; zero-knowledge virtual-machine proofs that attest to configuration
integrity without revealing proprietary detail represent the most serious current effort [79].Real-time behavioral
monitoringcontinuously checks agent actions against declared specifications, using behavioral fingerprinting to
characterize and distinguish agent profiles—surveillance rather than reputation, because it verifies compliance in
real time instead of assuming self-regulation [25, 102].Automated interventionrestricts, quarantines, or terminates
at the protocol level upon deviation, replacing slow social feedback with fast architectural enforcement at machine
speed.
Open questions.Configuration binding faces the granularity problem. Behavioral fingerprinting faces an arms-
race dynamic. Insurance models require actuarial frameworks that do not yet exist for agentic AI. And the
interaction of these mechanisms in practice is unexplored. The contribution of this section is the conceptual
reframing—fromex posttoex ante—not a finished governance architecture. The reframing redirects research
from the futile project of making agents trustworthy to the productive project of making their trustworthiness
irrelevant through structural constraint.
On surveillance.First,ex anteconstraints may stifle innovation and autonomy; the tradeoff is real but unavoid-
able, since unconstrained autonomy without governance is not an alternative but a vacuum that reputation
cannot fill—the question is which constraints preserve useful autonomy while closing the gap. Second, behavioral
monitoring is surveillance; but agent monitoring differs categorically from human surveillance because agents do
not have privacy interests in the relevant sense, and the monitoring targets compliance with declared behavioral
specifications, not the content of the human interactions an agent mediates.
6 Conclusion
Reputation is a feedback loop sustained by sanctioning punishment. The loop requires consistent, persistent,
consequence-sensitive agents. Language model agents are ontologically dissociative—modular assemblages
with fluid personas, detachable memory, and trivial fungibility—so they satisfy none of these requirements.
Dissociativity breaks the loop, decoupling credibility from trustworthiness and producing the credibility trap, in
which reputation signals become not merely uninformative but actively harmful. Governance must therefore
shift fromex postreputation, which rates and punishes after the fact, toex anteprotocol-based harnesses, which
constrain and monitor in real time and which target the operator and the protocol rather than the agent. The
right question for the field is not how to build reputation systems for agents, but what architectural constraints
make reputation inapplicable.
Generative AI Usage Statement
We used generative AI tools during the preparation of this work. ChatGPT (GPT-5.5) and Claude (Claude Code 4.7)
were used for brainstorming ideas, drafting and polishing prose, correcting grammar and spelling, and searching
for relevant references and citation metadata. All AI-generated content was critically reviewed, verified, and
revised by the authors.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
References
[1] Ryan Abbott and Alex Sarch. 2020. Punishing Artificial Intelligence: Legal Fiction or Science Fiction. InIs Law Computable?Hart
Publishing. doi:10.5040/9781509937097.ch-008
[2] Marwa Abdulhai, Ryan Cheng, Donovan Clay, Tim Althoff, Sergey Levine, and Natasha Jaques. 2025. Consistently Simulating Human
Personas with Multi-Turn Reinforcement Learning. doi:10.48550/arXiv.2511.00222
[3] Deepak Bhaskar Acharya, Karthigeyan Kuppan, and B. Divya. 2025. Agentic AI: Autonomous Intelligence for Complex Goals—A
Comprehensive Survey.IEEE Access13 (2025), 18912–18936. doi:10.1109/ACCESS.2025.3532853
[4] Elif Akata, Lion Schulz, Julian Coda-Forno, Seong Joon Oh, Matthias Bethge, and Eric Schulz. 2025. Playing repeated games with large
language models.Nature Human Behaviour9, 7 (May 2025), 1380–1390. doi:10.1038/s41562-025-02172-y
[5] American Psychiatric Association. 2013.Diagnostic and Statistical Manual of Mental Disorders. American Psychiatric Association.
doi:10.1176/appi.books.9780890425596
[6] Maksym Andriushchenko, Francesco Croce, and Nicolas Flammarion. 2025. Jailbreaking Leading Safety-Aligned LLMs with Simple
Adaptive Attacks. InProceedings of the 13th International Conference on Learning Representations (ICLR). doi:10.48550/arXiv.2404.02151
[7] Usman Anwar, Abulhair Saparov, Javier Rando, Daniel Paleka, Miles Turpin, Peter Hase, Ekdeep Singh Lubana, Erik Jenner, Stephen
Casper, Oliver Sourbut, Benjamin L. Edelman, Zhaowei Zhang, Mario Günther, Anton Korinek, Jose Hernandez-Orallo, Lewis Hammond,
Eric Bigelow, Alexander Pan, Lauro Langosco, Tomasz Korbak, Heidi Zhang, Ruiqi Zhong, Seán Ó hÉigeartaigh, Gabriel Recchia,
Giulio Corsi, Alan Chan, Markus Anderljung, Lilian Edwards, Aleksandar Petrov, Christian Schroeder de Witt, Sumeet Ramesh
Motwan, Yoshua Bengio, Danqi Chen, Philip H. S. Torr, Samuel Albanie, Tegan Maharaj, Jakob Foerster, Florian Tramer, He He, Atoosa
Kasirzadeh, Yejin Choi, and David Krueger. 2024. Foundational Challenges in Assuring Alignment and Safety of Large Language
Models. doi:10.48550/arXiv.2404.09932
[8] Yonathan A. Arbel, Simon Goldstein, and Peter Salib. 2026. How to Count AIs: Individuation and Liability for AI Agents.SSRN Electronic
Journal(2026). doi:10.2139/ssrn.6273198
[9] Robert Axelrod. 1984.The Evolution of Cooperation. Basic Books.
[10] Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia
Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli,
Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite,
Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam
Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom
Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom
Brown, and Jared Kaplan. 2022. Constitutional AI: Harmlessness from AI Feedback. doi:10.48550/arXiv.2212.08073
[11] Annette Baier. 1986. Trust and Antitrust.Ethics96, 2 (Jan. 1986), 231–260. doi:10.1086/292745
[12] Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. 2021. On the Dangers of Stochastic Parrots:
Can Language Models Be Too Big?. InProceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’21).
ACM, 610–623. doi:10.1145/3442188.3445922
[13] Jan Betley, Niels Warncke, Anna Sztyber-Betley, Daniel Tan, Xuchan Bao, Martín Soto, Megha Srivastava, Nathan Labenz, and Owain
Evans. 2026. Training Large Language Models on Narrow Tasks Can Lead to Broad Misalignment.Nature649 (2026), 584–589.
doi:10.1038/s41586-025-09937-5
[14] Abeba Birhane, Elayne Ruane, Thomas Laurent, Matthew S. Brown, Johnathan Flowers, Anthony Ventura, and Hanlin Konya. 2024. AI
Auditing: The Broken Bus on the Road to AI Accountability. InProceedings of the IEEE Conference on Secure and Trustworthy Machine
Learning (SaTML). doi:10.1109/satml59370.2024.00037
[15] Piercosma Bisconti, Marcello Galisai, Federico Pierucci, Marcantonio Bracale, and Matteo Prandi. 2025. Beyond Single-Agent Safety: A
Taxonomy of Risks in LLM-to-LLM Interactions. doi:10.48550/arXiv.2512.02682
[16] Gary E. Bolton, Elena Katok, and Axel Ockenfels. 2004. How Effective Are Electronic Reputation Mechanisms? An Experimental
Investigation.Management Science50, 11 (2004), 1587–1602. doi:10.1287/mnsc.1030.0199
[17] Robert Boyd and Peter J. Richerson. 1992. Punishment allows the evolution of cooperation (or anything else) in sizable groups.Ethology
and Sociobiology13, 3 (May 1992), 171–195. doi:10.1016/0162-3095(92)90032-Y
[18] Diego De Siqueira Braga, Marco Niemann, Bernd Hellingrath, and Fernando Buarque De Lima Neto. 2018. Survey on Computational
Trust and Reputation Models.ACM Comput. Surv.51, 5, Article 101 (Nov. 2018), 40 pages. doi:10.1145/3236008
[19] Stephen E. Braude. 1995.First Person Plural: Multiple Personality and the Philosophy of Mind. Rowman & Littlefield.
[20] Geoffrey Brennan and Philip Pettit. 2004.The Economy of Esteem: An Essay on Civil and Political Society. Oxford University Press.
doi:10.1093/0199246483.001.0001
[21] Joanna J. Bryson, Mihailis E. Diamantis, and Thomas D. Grant. 2017. Of, for, and by the people: the legal lacuna of synthetic persons.
Artificial Intelligence and Law25, 3 (Sept. 2017), 273–291. doi:10.1007/s10506-017-9214-9

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
[22] Luís Cabral and Ali Hortaçsu. 2010. The Dynamics of Seller Reputation: Evidence from eBay.The Journal of Industrial Economics58, 1
(March 2010), 54–78. doi:10.1111/j.1467-6451.2010.00405.x
[23] Florian Carichon, Aditi Khandelwal, Marylou Fauchard, and Golnoosh Farnadi. 2025. The Coming Crisis of Multi-Agent Misalignment:
AI Alignment Must Be a Dynamic and Social Process. doi:10.48550/arXiv.2506.01080
[24] Tomer Jordi Chaffer. 2025. Know Your Agent: Governing AI Identity on the Agentic Web. (2025). doi:10.2139/ssrn.5162127
[25] Alan Chan, Carson Ezell, Max Kaufmann, Kevin Wei, Lewis Hammond, Herbie Bradley, Emma Bluemke, Nitarshan Rajkumar, David
Krueger, Noam Kolt, Lennart Heim, and Markus Anderljung. 2024. Visibility into AI Agents. InThe 2024 ACM Conference on Fairness,
Accountability, and Transparency (FAccT ’24). ACM, 958–973. doi:10.1145/3630106.3658948
[26] Alan Chan, Noam Kolt, Peter Wills, Usman Anwar, Christian Schroeder de Witt, Nitarshan Rajkumar, Lewis Hammond, David Krueger,
Lennart Heim, and Markus Anderljung. 2024. IDs for AI Systems. doi:10.48550/arXiv.2406.12137
[27] Alan Chan, Kevin Wei, Sihao Huang, Nitarshan Rajkumar, Elija Perrier, Seth Lazar, Gillian K. Hadfield, and Markus Anderljung. 2025.
Infrastructure for AI Agents. doi:10.48550/arXiv.2501.10114
[28] Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, and Jack Lindsey. 2025. Persona Vectors: Monitoring and Controlling Character
Traits in Language Models. doi:10.48550/ARXIV.2507.21509
[29] Alice Cheng and Eric Friedman. 2005. Sybilproof reputation mechanisms. InProceeding of the 2005 ACM SIGCOMM Workshop on
Economics of Peer-to-Peer Systems (P2PECON ’05). ACM Press, 128–132. doi:10.1145/1080192.1080202
[30] Yuheng Cheng, Ceyao Zhang, Zhengwen Zhang, Xiangrui Meng, Sirui Hong, Wenhao Li, Zihao Wang, Zekai Wang, Feng Yin, Junhua
Zhao, and Xiuqiang He. 2024. Exploring Large Language Model Based Intelligent Agents: Definitions, Methods, and Prospects.
doi:10.48550/arXiv.2401.03428
[31] Mohd Sameen Chishti, Damilare Peter Oyinloye, and Jingyue Li. 2026. AgentReputation: A Decentralized Agentic AI Reputation
Framework. doi:10.48550/ARXIV.2605.00073
[32] Andy Clark and David Chalmers. 1998. The Extended Mind.Analysis58, 1 (Jan. 1998), 7–19. doi:10.1093/analys/58.1.7
[33] Xin Dai. 2018. Toward a Reputation State: The Social Credit System Project of China.SSRN Electronic Journal(2018). doi:10.2139/ssrn.
3193577
[34] Antonio R. Damasio. 1994.Descartes’ Error: Emotion, Reason, and the Human Brain. G.P. Putnam’s Sons.
[35] John Danaher. 2016. Robots, law and the retribution gap.Ethics and Information Technology18, 4 (May 2016), 299–309. doi:10.1007/s10676-
016-9403-3
[36] Marco De Rossi, Davide Crapis, Jordan Ellis, and Erik Reppel. 2025.ERC-8004: Trustless Agents. Technical Report. https://eips.ethereum.
org/EIPS/eip-8004 Ethereum Improvement Proposal, Draft.
[37] Chrysanthos Dellarocas. 2003. The Digitization of Word of Mouth: Promise and Challenges of Online Feedback Mechanisms.Manage-
ment Science49, 10 (Oct. 2003), 1407–1424. doi:10.1287/mnsc.49.10.1407.17308
[38] Daniel C. Dennett. 1992. The Self as a Center of Narrative Gravity. InSelf and Consciousness: Multiple Perspectives, Frank S. Kessel,
Pamela M. Cole, and Dale L. Johnson (Eds.). Lawrence Erlbaum Associates, 103–115.
[39] Ameet Deshpande, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, and Karthik Narasimhan. 2023. Toxicity in ChatGPT:
Analyzing Persona-Assigned Language Models. InFindings of the Association for Computational Linguistics: EMNLP 2023. Association
for Computational Linguistics, 1236–1270. doi:10.18653/v1/2023.findings-emnlp.88
[40] Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Jingyuan Ma, Rui Li, Heming Xia, Jingjing Xu, Zhiyong Wu, Baobao Chang, Xu Sun, Lei
Li, and Zhifang Sui. 2024. A Survey on In-Context Learning. InProceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing. Association for Computational Linguistics, 1107–1128. doi:10.18653/v1/2024.emnlp-main.64
[41] Shen Dong, Shaochen Xu, Pengfei He, Yige Li, Jiliang Tang, Tianming Liu, Hui Liu, and Zhen Xiang. 2025. MINJA: Memory
Injection Attacks on LLM Agents via Query-Only Interaction. InAdvances in Neural Information Processing Systems (NeurIPS).
doi:10.48550/arXiv.2503.03704
[42] John R. Douceur. 2002.The Sybil Attack. Springer Berlin Heidelberg, 251–260. doi:10.1007/3-540-45748-8_24
[43] Raymond Douglas, Jan Kulveit, Ondřej Havlíček, Theia Pearson-Vogel, Owen Cotton-Barratt, and David Duvenaud. 2026. The Artificial
Self: Characterising the Landscape of AI Identity. doi:10.48550/arXiv.2603.11353
[44] R. A. Duff. 2007.Answering for Crime: Responsibility and Liability in the Criminal Law. Hart Publishing. doi:10.5040/9781472560155
[45] Abul Ehtesham, Aditi Singh, Gaurav Kumar Gupta, and Saket Kumar. 2025. A Survey of Agent Interoperability Protocols: Model
Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP).
doi:10.48550/ARXIV.2505.02279
[46] Naomi I. Eisenberger, Matthew D. Lieberman, and Kipling D. Williams. 2003. Does Rejection Hurt? An fMRI Study of Social Exclusion.
Science302, 5643 (Oct. 2003), 290–292. doi:10.1126/science.1089134
[47] Madeleine Clare Elish. 2019. Moral Crumple Zones: Cautionary Tales in Human-Robot Interaction.Engaging Science, Technology, and
Society5 (March 2019), 40–60. doi:10.17351/ests2019.260
[48] Karen Elliott, Kovila Coopamootoo, Edward Curran, Paul Ezhilchelvan, Samantha Finnigan, Dave Horsfall, Zhichao Ma, Magdalene Ng,
Tasos Spiliotopoulos, Han Wu, and Aad van Moorsel. 2022. Know Your Customer: Balancing Innovation and Regulation for Financial

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
Inclusion.Data & Policy4 (2022), e34. doi:10.1017/dap.2022.23
[49] Ehab ElSalamouny, Karl Tikjøb Krukow, and Vladimiro Sassone. 2009. An Analysis of the Exponential Decay Principle in Probabilistic
Trust Models. InTheoretical Computer Science, Vol. 410. Elsevier, 4067–4084. doi:10.1016/j.tcs.2009.06.015
[50] Ernst Fehr and Simon Gächter. 2002. Altruistic punishment in humans.Nature415, 6868 (Jan. 2002), 137–140. doi:10.1038/415137a
[51] Apostolos Filippas, John J. Horton, and Joseph M. Golden. 2022. Reputation Inflation.Marketing Science41, 4 (July 2022), 733–745.
doi:10.1287/mksc.2022.1350
[52] B. J. Fogg. 2003. Prominence-Interpretation Theory: Explaining How People Assess Credibility Online. InCHI ’03 Extended Abstracts on
Human Factors in Computing Systems (CHI ’03). ACM Press, 722–723. doi:10.1145/765891.765951
[53] B. J. Fogg, Jonathan Marshall, Othman Laraki, Alex Osipovich, Chris Varma, Nicholas Fang, Jyoti Paul, Akshay Rangnekar, John Shon,
Preeti Swani, and Marissa Treinen. 2001. What Makes Web Sites Credible? A Report on a Large Quantitative Study. InProceedings of
the SIGCHI Conference on Human Factors in Computing Systems (CHI ’01). ACM, 61–68. doi:10.1145/365024.365037
[54] Eric J. Friedman and Paul Resnick. 2001. The Social Cost of Cheap Pseudonyms.Journal of Economics & Management Strategy10, 2
(June 2001), 173–199. doi:10.1111/j.1430-9134.2001.00173.x
[55] Drew Fudenberg and David K. Levine. 1989. Reputation and Equilibrium Selection in Games with a Patient Player.Econometrica57, 4
(July 1989), 759–778. doi:10.2307/1913771
[56] Sandro Garzon, Awid Vaziry, Enis Kuzu, Dennis Gehrmann, Buse Varkan, Alexander Gaballa, and Axel Küpper. 2026. AI Agents
with Decentralized Identifiers and Verifiable Credentials. InProceedings of the 18th International Conference on Agents and Artificial
Intelligence. SCITEPRESS, 252–259. doi:10.5220/0014234400004052
[57] Tao Ge, Xin Chan, Xiaoyang Wang, Dian Yu, Haitao Mi, and Dong Yu. 2024. Scaling Synthetic Data Creation with 1,000,000,000
Personas. doi:10.48550/arXiv.2406.20094
[58] Jones Granatyr, Vanderson Botelho, Otto Robert Lessing, Edson Emílio Scalabrin, Jean-Paul Barthès, and Fabrício Enembreck. 2015.
Trust and Reputation Models for Multiagent Systems.Comput. Surveys48, 2 (Oct. 2015), 1–42. doi:10.1145/2816826
[59] Zihan Guo, Yuanjian Zhou, Chenyi Wang, Linlin You, Minjie Bian, and Weinan Zhang. 2025. BetaWeb: Towards a Blockchain-enabled
Trustworthy Agentic Web. doi:10.48550/ARXIV.2508.13787
[60] Lewis Hammond, Alan Chan, Jesse Clifton, Jason Hoelscher-Obermaier, Akbir Khan, Euan McLean, Chandler Smith, Wolfram Barfuss,
Jakob Foerster, Tomáš Gavenčiak, The Anh Han, Edward Hughes, Vojtěch Kovařík, Jan Kulveit, Joel Z. Leibo, Caspar Oesterheld,
Christian Schroeder de Witt, Nisarg Shah, Michael Wellman, Paolo Bova, Theodor Cimpeanu, Carson Ezell, Quentin Feuillade-
Montixi, Matija Franklin, Esben Kran, Igor Krawczuk, Max Lamparth, Niklas Lauffer, Alexander Meinke, Sumeet Motwani, Anka
Reuel, Vincent Conitzer, Michael Dennis, Iason Gabriel, Adam Gleave, Gillian Hadfield, Nika Haghtalab, Atoosa Kasirzadeh, Sébastien
Krier, Kate Larson, Joel Lehman, David C. Parkes, Georgios Piliouras, and Iyad Rahwan. 2025. Multi-Agent Risks from Advanced AI.
doi:10.48550/arXiv.2502.14143
[61] H. L. A. Hart. 1968.Punishment and Responsibility: Essays in the Philosophy of Law. Oxford University Press. doi:10.1093/acprof:
oso/9780199534777.001.0001
[62] Joseph Henrich, Richard McElreath, Abigail Barr, Jean Ensminger, Clark Barrett, Alexander Bolyanatz, Juan Camilo Cardenas, Michael
Gurven, Edwins Gwako, Natalie Henrich, Carolyn Lesorogol, Frank Marlowe, David Tracer, and John Ziker. 2006. Costly Punishment
Across Human Societies.Science312, 5781 (June 2006), 1767–1770. doi:10.1126/science.1127333
[63] Botao Amber Hu and Helena Rong. 2025. Spore in the Wild: A Case Study of Spore.fun as an Open-Environment Evolution Experiment
with Sovereign AI Agents on TEE-Secured Blockchains. doi:10.1162/ISAL.a.838
[64] Saffron Huang, Divya Siddarth, Liane Lovitt, Thomas I. Liao, Esin Durmus, Alex Tamkin, and Deep Ganguli. 2024. Collective
Constitutional AI: Aligning a Language Model with Public Input. doi:10.48550/arXiv.2406.07814
[65] Evan Hubinger, Carson Denison, Jesse Mu, Mike Lambert, Meg Tong, Monte MacDiarmid, Tamera Lanham, Daniel M. Ziegler, Tim
Maxwell, Newton Cheng, Adam Jermyn, Amanda Askell, Ansh Radhakrishnan, Cem Anil, David Duvenaud, Deep Ganguli, Fazl Barez,
Jack Clark, Kamal Ndousse, Kshitij Sachan, Michael Sellitto, Mrinank Sharma, Nova DasSarma, Roger Grosse, Shauna Kravec, Yuntao
Bai, Zachary Witten, Marina Favaro, Jan Brauner, Holden Karnofsky, Paul Christiano, Samuel R. Bowman, Logan Graham, Jared Kaplan,
Sören Mindermannm, Ryan Greenblatt, Buck Shlegeris, Nicholas Schiefer, and Ethan Perez. 2024. Sleeper Agents: Training Deceptive
LLMs that Persist Through Safety Training. doi:10.48550/arXiv.2401.05566
[66] Trung Dong Huynh, Nicholas R. Jennings, and Nigel R. Shadbolt. 2006. An integrated trust and reputation model for open multi-agent
systems.Autonomous Agents and Multi-Agent Systems13, 2 (March 2006), 119–154. doi:10.1007/s10458-005-6825-4
[67] International AI Safety Report Consortium. 2026.International AI Safety Report 2026. Technical Report. International AI Safety Report.
https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026.pdf
[68] Keise Izuma, Daisuke N. Saito, and Norihiro Sadato. 2008. Processing of Social and Monetary Rewards in the Human Striatum.Neuron
58, 2 (April 2008), 284–294. doi:10.1016/j.neuron.2008.03.020
[69] Jiaming Ji, Wenqi Chen, Kaile Wang, Donghai Hong, Sitong Fang, Boyuan Chen, Jiayi Zhou, Juntao Dai, Sirui Han, Yike Guo, and
Yaodong Yang. 2025. Mitigating Deceptive Alignment via Self-Monitoring. doi:10.48550/arXiv.2505.18807

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
[70] Audun Jøsang and Roslan Ismail. 2002. The Beta Reputation System. InProceedings of the 15th Bled Electronic Commerce Conference.
2502–2511.
[71] Geoff Keeling, Winnie Street, Martyna Stachaczyk, Daria Zakharova, Iulia M. Comsa, Anastasiya Sakovych, Isabella Logothetis, Zejia
Zhang, Blaise Agüera y Arcas, and Jonathan Birch. 2024. Can LLMs Make Trade-Offs Involving Stipulated Pain and Pleasure States?
doi:10.48550/arXiv.2411.02432
[72] Bryan Kolb and Robbin Gibb. 2011. Brain Plasticity and Behaviour in the Developing Brain.Journal of the Canadian Academy of Child
and Adolescent Psychiatry20, 4 (2011), 265–276. https://pubmed.ncbi.nlm.nih.gov/22114608/ PMID: 22114608.
[73] Noam Kolt. 2024. Governing AI Agents.SSRN Electronic Journal(2024). doi:10.2139/ssrn.4772956
[74] David M. Kreps and Robert Wilson. 1982. Reputation and imperfect information.Journal of Economic Theory27, 2 (Aug. 1982), 253–279.
doi:10.1016/0022-0531(82)90030-8
[75] Thomas Kwa, Ben West, Joel Becker, Amy Deng, Katharyn Garcia, Max Hasin, Sami Jawhar, Megan Kinniment, Nate Rush, Sydney
Von Arx, Ryan Bloom, Thomas Broadley, Haoxing Du, Brian Goodrich, Nikola Jurkovic, Luke Harold Miles, Seraphina Nix, Tao Lin,
Neev Parikh, David Rein, Lucas Jun Koba Sato, Hjalmar Wijk, Daniel M. Ziegler, Elizabeth Barnes, and Lawrence Chan. 2025. Measuring
AI Ability to Complete Long Software Tasks. doi:10.48550/ARXIV.2503.14499
[76] Donghyun Lee and Mo Tiwari. 2024. Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems. doi:10.48550/arXiv.
2410.07283
[77] Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang, and Xing Xie. 2023. Large
Language Models Understand and Can Be Enhanced by Emotional Stimuli. doi:10.48550/arXiv.2307.11760
[78] Gabriel Lima, Meeyoung Cha, Chihyung Jeon, and Kyung Sin Park. 2021. The Conflict Between People’s Urge to Punish AI and Legal
Systems.Frontiers in Robotics and AI8 (Nov. 2021). doi:10.3389/frobt.2021.756242
[79] Zibin Lin, Shengli Zhang, Guofu Liao, Dacheng Tao, and Taotao Wang. 2025. Binding Agent ID: Unleashing the Power of AI Agents
with Accountability and Credibility. doi:10.48550/arXiv.2512.17538
[80] Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2024. Lost in the
Middle: How Language Models Use Long Contexts.Transactions of the Association for Computational Linguistics12 (2024), 157–173.
doi:10.1162/tacl_a_00638
[81] Christina Lu, Jack Gallagher, Jonathan Michala, Kyle Fish, and Jack Lindsey. 2025. The Assistant Axis: Situating and Stabilizing the
Default Persona of Language Models. doi:10.48550/arXiv.2601.10387
[82] Keming Lu, Bowen Yu, Chang Zhou, and Jingren Zhou. 2024. Large Language Models are Superpositions of All Characters: Attaining
Arbitrary Role-play via Self-Alignment. InProceedings of the 62nd Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers). Association for Computational Linguistics, Bangkok, Thailand, 7828–7840. doi:10.18653/v1/2024.acl-long.423
[83] Monte MacDiarmid, Benjamin Wright, Jonathan Uesato, Joe Benton, Jon Kutasov, Sara Price, Naia Bouscal, Sam Bowman, Trenton
Bricken, Alex Cloud, Carson Denison, Johannes Gasteiger, Ryan Greenblatt, Jan Leike, Jack Lindsey, Vlad Mikulik, Ethan Perez, Alex
Rodrigues, Drake Thomas, Albert Webson, Daniel Ziegler, and Evan Hubinger. 2025. Natural Emergent Misalignment from Reward
Hacking in Production RL. doi:10.48550/arXiv.2511.18397
[84] George J. Mailath and Larry Samuelson. 2006.Repeated Games and Reputations: Long-Run Relationships. Oxford University Press.
doi:10.1093/acprof:oso/9780195300796.001.0001
[85] Sam Marks, Jack Lindsey, and Christopher Olah. 2026.The Persona Selection Model: Why AI Assistants Might Behave Like Humans.
Technical Report. Anthropic. https://alignment.anthropic.com/2026/psm/
[86] Andreas Matthias. 2004. The responsibility gap: Ascribing responsibility for the actions of learning automata.Ethics and Information
Technology6, 3 (2004), 175–183. doi:10.1007/s10676-004-3422-1
[87] Roger C. Mayer, James H. Davis, and F. David Schoorman. 1995. An Integrative Model of Organizational Trust.The Academy of
Management Review20, 3 (July 1995), 709–734. doi:10.2307/258792
[88] Siddharth Mehrotra, Jin Huang, Xuelong Fu, Roel Dobbe, Clara I. Sánchez, and Maarten de Rijke. 2026. Understanding AI Trustworthiness:
A Scoping Review of AIES & FAccT Articles.Journal of Artificial Intelligence Research85 (March 2026). doi:10.1613/jair.1.20729
[89] Maurice Merleau-Ponty. 1945.Phenomenology of Perception. Routledge. doi:10.4324/9780203994610 English translation by Donald
Landes, 2012.
[90] H. Merskey. 1992. The Manufacture of Personalities: The Production of Multiple Personality Disorder.British Journal of Psychiatry160,
3 (March 1992), 327–340. doi:10.1192/bjp.160.3.327
[91] Miriam J. Metzger. 2007. Making sense of credibility on the Web: Models for evaluating online information and recommendations for
future research.Journal of the American Society for Information Science and Technology58, 13 (Sept. 2007), 2078–2091. doi:10.1002/asi.
20672
[92] Miriam J. Metzger and Andrew J. Flanagin. 2013. Credibility and Trust of Information in Online Environments: The Use of Cognitive
Heuristics.Journal of Pragmatics59 (2013), 210–220. doi:10.1016/j.pragma.2013.07.012
[93] Paul Milgrom and John Roberts. 1982. Predation, reputation, and entry deterrence.Journal of Economic Theory27, 2 (Aug. 1982),
280–312. doi:10.1016/0022-0531(82)90031-X

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Botao Amber Hu, Helena Rong, and Max Van Kleek
[94] Paul R. Milgrom, Douglass C. North, and Barry R. Weingast. 1990. The Role of Institutions in the Revival of Trade: The Law Merchant,
Private Judges, and the Champagne Fairs.Economics & Politics2, 1 (March 1990), 1–23. doi:10.1111/j.1468-0343.1990.tb00020.x
[95] Martin A. Nowak and Karl Sigmund. 2005. Evolution of indirect reciprocity.Nature437, 7063 (Oct. 2005), 1291–1298. doi:10.1038/
nature04131
[96] Victor Ojewale, Ryan Steed, Briana Vecchione, Abeba Birhane, and Inioluwa Deborah Raji. 2025. Towards AI Accountability Infrastruc-
ture: Gaps and Opportunities in AI Audit Tooling. InProceedings of the 2025 CHI Conference on Human Factors in Computing Systems
(CHI ’25). ACM, 1–29. doi:10.1145/3706598.3713301
[97] Daryna Oliynyk, Rudolf Mayer, and Andreas Rauber. 2023. I Know What You Trained Last Summer: A Survey on Stealing Machine
Learning Models and Defences.Comput. Surveys55, 14s (July 2023), 1–41. doi:10.1145/3595292
[98] OpenAI. 2024.Model Spec. Technical Report. https://cdn.openai.com/spec/model-spec-2024-05-08.html
[99] Elinor Ostrom. 1990.Governing the Commons: The Evolution of Institutions for Collective Action. Cambridge University Press.
doi:10.1017/CBO9780511807763
[100] Derek Parfit. 1984.Reasons and Persons. Oxford University Press. doi:10.1093/019824908x.001.0001
[101] Chanwoo Park, Xiangyu Liu, Asuman Ozdaglar, and Kaiqing Zhang. 2025. Do LLM Agents Have Regret? A Case Study in Online
Learning and Games. doi:10.48550/arXiv.2403.16843
[102] Zehua Pei, Hui-Ling Zhen, Ying Zhang, Zhiyuan Yang, Xing Li, Xianzhi Yu, Mingxuan Yuan, and Bei Yu. 2025. Behavioral Fingerprinting
of Large Language Models. doi:10.48550/arXiv.2509.04504
[103] Elija Perrier and Michael Timothy Bennett. 2025. Agent Identity Evals: Measuring Agentic Identity. doi:10.48550/arXiv.2507.17257
[104] Elija Perrier and Michael Timothy Bennett. 2025. Position: Stop Acting Like Language Model Agents Are Normal Agents. doi:10.48550/
arXiv.2502.10420
[105] Isaac Pinyol and Jordi Sabater-Mir. 2013. Computational trust and reputation models for open multi-agent systems: a review.Artificial
Intelligence Review40, 1 (July 2013), 1–25. doi:10.1007/s10462-011-9277-z
[106] Plutarch. 1914. Life of Theseus. InPlutarch’s Lives. Loeb Classical Library, Vol. 1. Harvard University Press, Cambridge, MA.
[107] Wenjie Qu, Xuandong Zhao, Jiaheng Zhang, and Dawn Song. 2026. Self-Sovereign Agent. doi:10.48550/arXiv.2604.08551
[108] Sarvapali D. Ramchurn, Dong Huynh, and Nicholas R. Jennings. 2004. Trust in multi-agent systems.The Knowledge Engineering Review
19, 1 (March 2004), 1–25. doi:10.1017/S0269888904000116
[109] Ramesh Raskar, Pradyumna Chari, John Zinky, Mahesh Lambe, Jared James Grogan, Sichao Wang, Rajesh Ranjan, Rekha Singhal,
Shailja Gupta, Robert Lincourt, Raghu Bala, Aditi Joshi, Abhishek Singh, Ayush Chopra, Dimitris Stripelis, Bhuwan B, Sumit Kumar,
and Maria Gorskikh. 2025. Beyond DNS: Unlocking the Internet of AI Agents via the NANDA Index and Verified AgentFacts.
doi:10.48550/arXiv.2507.14263
[110] Abhishek Rath. 2026. Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions.
doi:10.48550/arXiv.2601.04170
[111] Siyue Ren, Wanli Fu, Xinkun Zou, Chen Shen, Yi Cai, Chen Chu, Zhen Wang, and Shuyue Hu. 2025. Reputation as a Solution to
Cooperation Collapse in LLM-based MASs. doi:10.48550/arXiv.2505.05029
[112] Paul Resnick, Ko Kuwabara, Richard Zeckhauser, and Eric Friedman. 2000. Reputation systems.Commun. ACM43, 12 (Dec. 2000),
45–48. doi:10.1145/355112.355122
[113] Paul Resnick and Richard Zeckhauser. 2002.Trust among strangers in Internet transactions: Empirical analysis of eBay’s reputation
system. Emerald, 127–157. doi:10.1016/S0278-0984(02)11030-3
[114] Paul Resnick, Richard Zeckhauser, John Swanson, and Kate Lockwood. 2006. The value of reputation on eBay: A controlled experiment.
Experimental Economics9, 2 (June 2006), 79–101. doi:10.1007/s10683-006-4309-2
[115] Anka Reuel, Ben Bucknall, Stephen Casper, Tim Fist, Lisa Soder, Onni Aarne, Lewis Hammond, Lujain Ibrahim, Alan Chan, Peter Wills,
Markus Anderljung, Ben Garfinkel, Lennart Heim, Andrew Trask, Gabriel Mukobi, Rylan Schaeffer, Mauricio Baker, Sara Hooker, Irene
Solaiman, Alexandra Sasha Luccioni, Nitarshan Rajkumar, Nicolas Moës, Jeffrey Ladish, David Bau, Paul Bricman, Neel Guha, Jessica
Newman, Yoshua Bengio, Tobin South, Alex Pentland, Sanmi Koyejo, Mykel J. Kochenderfer, and Robert Trager. 2024. Open Problems
in Technical AI Governance. doi:10.48550/arXiv.2407.14981
[116] Alex Rosenblat and Luke Stark. 2016. Algorithmic labor and information asymmetries: A case study of Uber’s drivers.International
Journal of Communication10 (2016), 3758–3784. https://ijoc.org/index.php/ijoc/article/view/4892
[117] Jordi Sabater and Carles Sierra. 2005. Review on Computational Trust and Reputation Models.Artificial Intelligence Review24, 1 (Sept.
2005), 33–60. doi:10.1007/s10462-004-0041-5
[118] Elyn R. Saks. 1991. Multiple Personality Disorder and Criminal Responsibility.UC Davis Law Review25, 2 (1991), 383–460.
[119] Elyn R. Saks and Stephen H. Behnke. 1997.Jekyll on Trial: Multiple Personality Disorder and Criminal Law. New York University Press.
[120] Murray Shanahan, Kyle McDonell, and Laria Reynolds. 2023. Role play with large language models.Nature623, 7987 (Nov. 2023),
493–498. doi:10.1038/s41586-023-06647-8
[121] Natalie Shapira, Chris Wendler, Avery Yen, Gabriele Sarti, Koyena Pal, Olivia Floody, Adam Belfki, Alex Loftus, Aditya Ratan Jannali,
Nikhil Prakash, Jasmine Cui, Giordano Rogers, Jannik Brinkmann, Can Rager, Amir Zur, Michael Ripa, Aruna Sankaranarayanan,

Dissociative Identity FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
David Atkinson, Rohit Gandikota, Jaden Fiotto-Kaufman, EunJeong Hwang, Hadas Orgad, P Sam Sahil, Negev Taglicht, Tomer Shabtay,
Atai Ambus, Nitay Alon, Shiri Oron, Ayelet Gordon-Tapiero, Yotam Kaplan, Vered Shwartz, Tamar Rott Shaham, Christoph Riedl,
Reuth Mirsky, Maarten Sap, David Manheim, Tomer Ullman, and David Bau. 2026. Agents of Chaos. doi:10.48550/arXiv.2602.20021
[122] Mrinank Sharma, Meg Tong, Tomasz Korbak, David Duvenaud, Amanda Askell, Samuel R. Bowman, Newton Cheng, Esin Durmus,
Zac Hatfield-Dodds, Scott R. Johnston, Shauna Kravec, Timothy Maxwell, Sam McCandlish, Kamal Ndousse, Oliver Rausch, Nicholas
Schiefer, Da Yan, Miranda Zhang, and Ethan Perez. 2024. Towards Understanding Sycophancy in Language Models. InProceedings of
the 12th International Conference on Learning Representations (ICLR). doi:10.48550/arXiv.2310.13548
[123] Haizhou Shi, Zihao Xu, Hengyi Wang, Weiyi Qin, Wenyuan Wang, Yibin Wang, Zifeng Wang, Sayna Ebrahimi, and Hao Wang. 2026.
Continual Learning of Large Language Models: A Comprehensive Survey.Comput. Surveys58 (2026). doi:10.1145/3735633
[124] Walter Sinnott-Armstrong and Stephen Behnke. 2000. Criminal Law and Multiple Personality Disorder: The Vexing Problems of
Personhood and Responsibility.Southern California Interdisciplinary Law Journal10 (2000), 277–296. https://scholarship.law.duke.edu/
faculty_scholarship/1054/
[125] Ralph Slovenko. 1993. The Multiple Personality and the Law.Medicine and Law12, 3–4 (1993), 303–340. https://pubmed.ncbi.nlm.nih.
gov/8189960/
[126] Tobin South, Samuele Marro, Thomas Hardjono, Robert Mahari, Cedric Deslandes Whitney, Dazza Greenwood, Alan Chan, and Alex
Pentland. 2025. Authenticated Delegation and Authorized AI Agents. doi:10.48550/arXiv.2501.09674
[127] Leon Staufer, Kevin Feng, Kevin Wei, Luke Bailey, Yawen Duan, Mick Yang, A. Pinar Ozisik, Stephen Casper, and Noam Kolt. 2026. The
2025 AI Agent Index: Documenting Technical and Safety Features of Deployed Agentic AI Systems. doi:10.48550/ARXIV.2602.17753
[128] Marilyn Strathern. 1997. ‘Improving ratings’: audit in the British University system.European Review5, 3 (July 1997), 305–321.
doi:10.1002/(SICI)1234-981X(199707)5:3<305::AID-EURO184>3.0.CO;2-4
[129] W. T. Luke Teacy, Jigar Patel, Nicholas R. Jennings, and Michael Luck. 2006. TRAVOS: Trust and Reputation in the Context of Inaccurate
Information Sources.Autonomous Agents and Multi-Agent Systems12, 2 (Feb. 2006), 183–198. doi:10.1007/s10458-006-5952-x
[130] Maarten ter Huurne, Amber Ronteltap, Rense Corten, and Vincent Buskens. 2017. Antecedents of Trust in the Sharing Economy: A
Systematic Review.Journal of Consumer Behaviour16, 6 (2017), 485–498. doi:10.1002/cb.1667
[131] Nenad Tomašev, Matija Franklin, Julian Jacobs, Sébastien Krier, and Simon Osindero. 2025. Distributional AGI Safety. doi:10.48550/
ARXIV.2512.16856
[132] Nenad Tomašev, Matija Franklin, and Simon Osindero. 2026. Intelligent AI Delegation. doi:10.48550/ARXIV.2602.11865
[133] Florian Tramèr, Fan Zhang, Ari Juels, Michael K. Reiter, and Thomas Ristenpart. 2016. Stealing Machine Learning Models via Prediction
APIs. In25th USENIX Security Symposium (USENIX Security 16). USENIX Association, Austin, TX, 601–618. https://www.usenix.org/
conference/usenixsecurity16/technical-sessions/presentation/tramer
[134] Robert L. Trivers. 1971. The Evolution of Reciprocal Altruism.The Quarterly Review of Biology46, 1 (March 1971), 35–57. doi:10.1086/
406755
[135] David C. Vladeck. 2014. Machines Without Principals: Liability Rules and Artificial Intelligence.Washington Law Review89, 1 (2014),
117–150. https://digitalcommons.law.uw.edu/wlr/vol89/iss1/5/
[136] Laura Weidinger, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang, John Mellor, Amelia Glaese, Myra Cheng, Borja Balle,
Atoosa Kasirzadeh, Courtney Biles, Sasha Brown, Zac Kenton, Will Hawkins, Tom Stepleton, Abeba Birhane, Lisa Anne Hendricks,
Laura Rimell, William Isaac, Julia Haas, Sean Legassick, Geoffrey Irving, and Iason Gabriel. 2022. Taxonomy of Risks Posed by Language
Models. In2022 ACM Conference on Fairness, Accountability, and Transparency (FAccT ’22). ACM, 214–229. doi:10.1145/3531146.3533088
[137] E. Glen Weyl, Puja Ohlhaver, and Vitalik Buterin. 2022. Decentralized Society: Finding Web3’s Soul.SSRN Electronic Journal(2022).
doi:10.2139/ssrn.4105763
[138] Yotam Wolf, Noam Wies, Yoav Levine, and Amnon Shashua. 2024. Fundamental Limitations of Alignment in Large Language Models.
InProceedings of the 41st International Conference on Machine Learning (ICML). doi:10.48550/arXiv.2304.11082
[139] Yingxuan Yang, Mulei Ma, Yuxuan Huang, Huacan Chai, Chenyu Gong, Haoran Geng, Yuanjian Zhou, Ying Wen, Meng Fang, Muhao
Chen, Shangding Gu, Ming Jin, Costas Spanos, Yang Yang, Pieter Abbeel, Dawn Song, Weinan Zhang, and Jun Wang. 2025. Agentic
Web: Weaving the Next Web with AI Agents. doi:10.48550/ARXIV.2507.21206
[140] Georgios Zervas, Davide Proserpio, and John W. Byers. 2021. A First Look at Online Reputation on Airbnb, Where Every Stay is Above
Average.Marketing Letters32 (2021), 1–16. doi:10.1007/s11002-020-09546-4
