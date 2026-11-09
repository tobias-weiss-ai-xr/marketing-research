---
title: 'From Augmentation to Reconstruction: Guiding the AI Disruption to the Good Place'
url: https://arxiv.org/abs/2605.29207
category: consumer-behavior
subcategory: empirical
date: 2026-05
venue: ''
authors:
- David M. Rothschild
- Jake M. Hofman
- Markus Mobius
- Brendan Lucier
- Eleanor Dillon
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.29207
pages: 5
chars: 22598
fetched_at: '2026-11-08T13:01:00+00:00'
kb_version: 1
---

# From Augmentation to Reconstruction: Guiding the AI Disruption to the Good Place

FROMAUGMENTATION TORECONSTRUCTION:
GUIDING THEAI DISRUPTION TO THEGOODPLACE
PERSPECTIVE ONAI DISRUPTION
David M. Rothschild∗ Jake M. Hofman Markus Mobius Brendan Lucier
Eleanor Dillon Daniel G. Goldstein Nicole Immorlica Aleksandrs Slivkins
May 29, 2026
ABSTRACT
Artificial intelligence feels omnipresent, yet the disruption many expect has not fully arrived. The
main reason is not model capability, nor even the tools built to harness those models. Rather,
most organizations are still using AI to accelerate workflows designed for a pre -AI world. We
offer a three-stage lens—Augmentation, Automation, and Reconstruction—and argue that the most
consequential disruption resides in the third stage where workflows and markets are rebuilt around del-
egation, machine-to-machine interaction, continuous monitoring, and auditable constraints. Achiev-
ing this system-level transformation takes time: it requires trust and accountability infrastructure,
machine-legible and interoperable data and interfaces, the design and adoption of these new workflows,
and economic incentives that favor reconstruction rather than local optimization: the complementary
investments that produce the familiar “productivity J-curve” of general-purpose technologies. We
illustrate this transition through examples in consumer markets, education, news, and coding. Finally,
we emphasize a normative point: the agentic future is not predetermined. Leaders must both skate
to where the puck is going and actively steer it toward a good place, ensuring innovation delivers
welfare gains felt by businesses and consumers around the world.
KeywordsAI Disruption·Market Design·Agentic Web·Good Place
Public discussion of artificial intelligence often overemphasizes current AI performance on a narrow set of familiar
tasks. We marvel at models that can ace standardized tests; we love to challenge AI agents’ ability to navigate web
interfaces and social media. These feats capture attention but they distract from the more consequential impacts to
come. The real story is not whether AI can pass exams or navigate our digital environments or surpass benchmarks in
our current digital world, but how it will fundamentally reshape how people learn, work, and coordinate their lives.
The right questions will include whether it helps people acquire new skills, make better decisions, or collaborate more
effectively? Today’s AI agents that competently browse the web will feel misplaced in a future digital ecosystem that is
expressly designed for AI agents to communicate, negotiate, and transact with each other on our behalf.
While it is useful in the short term to explore how AI can augment humans within existing workflows, the greatest
disruptions will emerge as we redesign tasks, tools, and environments around AI’s distinctive strengths [Bresnahan
et al., 1996]. This shift, from asking how well AI mimics people to asking what becomes possible when systems are
rebuilt to leverage AI’s capabilities, is central to realizing AI’s long-term impact [Demirer et al., 2026].
History offers a helpful analogy. Early factory electrification replaced steam engines with electric motors, delivering
modest productivity gains. It was only when factory layouts and production processes were redesigned, taking advantage
of electricity’s flexibility and decentralization, that productivity surged [David, 1990, Brynjolfsson and Hitt, 2000].
Today, AI is often deployed in similarly conservative ways, drafted into familiar routines such as summarizing articles,
assisting with homework, or managing shopping lists [Dillon et al., 2025]. These applications are useful, but they
capture only a small share of AI’s potential. Far larger gains will come when entire processes are designed from the
ground up around what AI does well, for example: marketplaces where personal agents continuously coordinate, search,
and negotiate on a user’s behalf; education systems organized around persistent, adaptive learning loops that track
∗All authors are at Microsoft Research. Contact: David@ResearchDMR.com
arXiv:2605.29207v1  [econ.GN]  28 May 2026

Guiding the AI Disruption to the Good PlacePERSPECTIVE ONAI DISRUPTION
and build mastery over time; or information ecosystems in which agents monitor sources, evaluate credibility, and
synthesize evolving narratives tailored to users’ goals.
Three stages of AI integration
To understand why disruption has not yet fully arrived, it helps to distinguish three stages of AI integration [Rothschild
et al., 2026]. These stages are conceptual rather than chronological, and organizations may occupy multiple stages
simultaneously. However, only the final stage produces genuine structural transformation. These stages map onto
the “productivity J-curve” of general-purpose technologies (i.e., GPTs) [Brynjolfsson et al., 2021], but whereas that
framework describes the aggregate pattern of delayed gains, our contribution is to characterize the organizational
transitions—from task-level enhancement to workflow redesign—that give rise to it.
Stage 1: Augmentation
In Stage 1, AI enhances discrete tasks currently being performed by humans within existing workflows. This is the dom-
inant mode of AI use today: drafting emails, summarizing documents, generating code suggestions, answering customer
questions, or producing first-pass analyses. Humans retain control over sequencing, judgment, and accountability.
Stage 1 spreads quickly because it does not require organizational redesign. It integrates easily into workflows built for
human coordination and oversight. The gains are real—but largely local. Bottlenecks shift rather than disappear. Faster
drafting still waits on approvals; faster analysis still feeds slow decisions. Augmentation improves speed and allows
users to shift their attention to other tasks, but does not change the workflow structure.
Stage 2: Automation
In Stage 2, routine tasks move “under the hood" and require less human awareness. Consider education: a Stage 1
implementation might help a teacher draft a lesson plan or generate practice problems. In Stage 2, these tasks are largely
delegated. AI generates lesson plans, creates assessments, and assists with grading, while students interact with tutors
that adapt explanations in real time. Both teachers and students focus less on content delivery mechanics and more on
higher-level objectives: structuring learning paths, interpreting results, and guiding progress.
For product and operations leaders, Stage 2 often feels like the first “real” productivity step-change because it reduces
coordination drag and frees scarce attention. Still, Stage 2 typically runs inside human-era architectures: forms, queues,
approvals, and meetings. AI works harder inside the system, but the system itself remains largely unchanged.
Yet Stage 2 is best understood as transitional rather than terminal. This stage is also characterized by substantial
complementary investment in data, infrastructure, and organizational processes: much of it intangible and only partially
reflected in measured output. Observed productivity may therefore understate underlying progress, reflecting both the
accumulation of intangible investments and the fact that early gains, often concentrated among initial adopters, may be
one-time level shifts rather than sustained improvements in measured output per unit of work. Whether this manifests
as a temporary slowdown (i.e., “J-curve”) or continued but muted growth (i.e., a “hockey-stick” shaped pattern of
productivity growth) remains uncertain. This creates a particularly unsettled moment for workers, as workflows begin to
shift but are not yet fully reconstructed. In this environment, firms may favor capital deepening and partial automation
over broad investment in new skills, even as longer-run opportunities may expand.
Many will worry that the disruption ends here with slow or negative growth, and massive worker displacement. The
concern is not that automation leads to a “bad” outcome per se, but that stopping here risks locking in systems optimized
around legacy workflows, limiting the broader gains that come from redesigning how work is organized. As such, Stage
2 is best understood not as a stable endpoint, but as a transitional, suboptimal equilibrium in AI integration.
Stage 3: Reconstruction
Stage 3 is where the long -anticipated disruption actually resides, and why it has not yet emerged at scale. In Re-
construction, workflows are redesigned around AI’s distinctive capabilities: speed, parallelism, memory, continuous
monitoring, and machine -to-machine interaction. Steps are re -sequenced, eliminated, or converted into auditable
constraints. Governance is engineered directly into workflows rather than layered on after the fact. Human roles shift to
align with the higher-level tasks afforded by the automation of routine subtasks. Efficiency gains change the calculus on
which forms of work are most valuable, leading to new approaches that were previously considered infeasible. In this
process, the activity itself is redefined: what it means to “shop,” “learn,” or “code” changes, rather than simply how
those tasks are executed. For AI, this stage of adoption remains early and uneven, with coding among the first domains
where elements of reconstruction are beginning to emerge.
2

Guiding the AI Disruption to the Good PlacePERSPECTIVE ONAI DISRUPTION
Domain Stage 1: Augmentation Stage 2: Automation Stage 3: Reconstruction
ShoppingAI helps draft a shopping list,
suggest products, or summarize
reviews. The user still browses,
compares, and decides.
Users delegate defined tasks (e.g.,
“reorder groceries” or “find a flight
under $500”), and AI executes
across platforms with limited
oversight.
A personal agent continuously
manages consumption: it
anticipates needs, coordinates
with multiple vendor agents,
negotiates over price and terms,
and enables dynamically
customized products (e.g.,
made-to-measure goods produced
on demand). Markets shift from
browsing interfaces to discovery
and quality assurance powering
agent-to-agent coordination.
EducationAI helps students complete
assignments, explain concepts,
and generate practice problems.
Teachers may use it to draft lesson
plans or test questions.
AI systems generate lesson plans,
create assessments, and assist with
grading. Students interact with AI
tutors that adapt explanations in
real time.
Education is reorganized around
continuous, personalized learning
loops: AI tracks mastery,
generates tailored instruction,
assesses progress, and feeds
results back into curriculum
design. The emphasis shifts from
static outputs (assignments and
tests) to dynamic skill acquisition
and ongoing evaluation.
News AI summarizes articles, highlights
key points, and aggregates
headlines from multiple sources.
Users receive personalized daily
briefings that integrate across
sources and formats, with filtering
based on preferences and past
behavior.
News consumption becomes an
interactive, continuously updated
dialogue: personal agents monitor
sources, evaluate credibility,
cross-check claims, and
synthesize evolving narratives
tailored to the user’s goals. The
unit of consumption shifts from
discrete articles to adaptive,
agent-curated understanding.
Coding AI provides quick assistance when
developers get stuck—suggesting
code snippets, debugging errors,
and explaining unfamiliar
functions—while humans still
write and structure most code.
AI automates segments of the
coding pipeline, including code
generation, testing, refactoring,
and documentation, allowing
developers to delegate
well-scoped tasks with oversight.
Software development workflows
are restructured around AI agents
that can plan, generate, and iterate
on code end-to-end; humans shift
primarily to problem formulation,
architectural guidance, and
editing, with agent-to-agent
coordination increasingly
handling execution.
Table 1: Illustrative progression from augmentation to reconstruction across everyday domains. In each case, the shift is
not simply from humans doing tasks faster to AI doing the same tasks automatically, but from task support to workflow
redesign around delegation, continuous monitoring, and machine-to-machine coordination.
This is where the long-anticipated disruption actually resides, and where the returns to earlier investments are finally
realized, as systems are rebuilt around AI’s strengths rather than adapted from legacy processes. Yet Stage 3 remains
early and uneven. Coding is perhaps the furthest along: AI-native workflows are beginning to restructure development
around agents, shifting humans upstream into ideation and downstream into curation and editing. The transition
depends on institutional conditions: trust, interoperability, workflow redesign, and aligned incentives, that remain
underdeveloped. We turn to these next.
Table 1 illustrates the progression across four domains, spanning B2C, B2B, and B2E examples. In each case, the
shift is not simply from humans doing tasks faster to AI doing them automatically, but from task support to workflow
redesign around delegation and machine-to-machine coordination.
3

Guiding the AI Disruption to the Good PlacePERSPECTIVE ONAI DISRUPTION
AI Integration in Consumer Markets
The distinction between stages is vivid in consumer markets, particularly shopping.
Today’s digital economy still assumes humans browse, search, and compare offerings through interfaces designed to
capture attention and facilitate navigation. AI typically appears as a layer on top: recommendations, chatbots, and
personalization. These are Stage 1 improvements. More recently, there is increasing interest in autonomous shopping
agents that act as personal assistants to which simple shopping tasks can be delegated. These are an initial wave of
Stage 2 integration.
A reconstructed, Stage 3 market looks different. In anagentic market, consumers delegate tasks to personal assistant
agents and firms deploy service agents that represent products, pricing, policies, and constraints. Transactions shift
from human-to-interface interaction to agent-to-agent coordination. The consumer expresses goals and constraints
once; their agent then queries and negotiates with multiple provider agents across the economy. Firms compete less
on visibility and more on value, responsiveness, and trustworthiness, expressed in machine-readable terms. Product
recommendation shifts from a centralized service provided by platform intermediaries to an emergent outcome of more
decentralized (and open) discovery and quality-assurance systems, enabling more direct, agent-to-agent interaction.
An agentic market is more than a chatbot bolted onto a website. It is a fundamentally different market mechanism,
characterized by lower communication friction, faster matching, and new forms of discovery and competition [Rothschild
et al., 2026].
If agentic markets are increasingly plausible, why do they not yet dominate? While the Stage 3 disruption presupposes
Stage 2 integration, the more binding constraints are institutional rather than technical. System-wide change depends
on trust and accountability infrastructure, complementary machine-legible and interoperable data and interfaces, the
design of agent-first workflows, and economic incentives that support reconstruction rather than local optimization.
These complementary conditions remain underdeveloped, limiting autonomy even as agentic capabilities improve. Four
constraints stand out.
Trust and accountability remain unresolved at scale.Delegating meaningful authority to agents requires auditability,
constraint enforcement, clear assignment of responsibility, and alignment of incentives. Organizations must be able to
inspect agent behavior, evaluate outcomes, respond to failures, and provide recourse when things go wrong. They must
know that their agent is perfectly aligned with their interests. Until trust infrastructure – instrumentation, monitoring,
evaluation, incident response, and liability frameworks –becomes routine, most firms will constrain agents to assistive
or advisory roles rather than granting true autonomy.
Data and interfaces lag behind agentic needs.Reliable agentic execution requires clean, interoperable data and
explicit, machine-readable policy definitions. Many organizations have not yet made their own operations sufficiently
legible for machines to act autonomously, let alone to interoperate with external agents. Weak interfaces and brittle data
pipelines raise error rates and compound risk, necessitating stronger harnesses and control layers before multi-agent
systems can operate robustly at scale.
Workflows remain fundamentally human-centric.Most enterprise systems still assume humans mediate every
interaction: reading screens, filling out forms, and resolving exceptions. Agent -first systems instead require APIs,
protocols, and machine-readable rules that allow agents to transact, coordinate, and escalate without constant human
intervention. This is a structural redesign of workflows and infrastructure, not an incremental layer added on top of
existing tools.
Incentives favor optimization over reinvention.It is safer and easier to use AI to optimize within existing business
models than to rebuild markets and organizations from the ground up. Firms must pursue transformation while
continuing to meet short-term revenue targets, which discourages large-scale reconstruction. Yet the largest gains from
agentic systems come precisely from redesigning how work and exchange are organized. This creates a misalignment:
incumbents can afford the upfront costs of new infrastructure but lack incentives to disrupt themselves, while smaller or
newer firms have stronger incentives to be transformative but more limited capacity to invest.
This creates a natural question: if Stage 2 delivers real gains at lower risk, why would any firm voluntarily undertake
the cost of reconstruction? The answer is that Stage 2 equilibria are stable only in the absence of competitive
pressure. Once any actor, an entrant unburdened by legacy systems or a consortium that solves the coordination
problem, demonstrates a reconstructed workflow, the calculus shifts rapidly. Moreover, prolonged Stage 2 optimization
accumulates organizational debt around legacy architectures, making eventual reconstruction more expensive. The
question is not whether reconstruction will occur, but whether incumbents will lead it or be disrupted by it.
4

Guiding the AI Disruption to the Good PlacePERSPECTIVE ONAI DISRUPTION
Guiding the AI Disruption to the Good Place
In technology, leaders often invoke the hockey metaphor:skate to where the puck is going. AI makes that advice feel
urgent. But in an agentic economy, skating alone is not enough.
AI will reshape how work is done and how markets function. How large the gains are, whether they are broadly
distributed, whether ecosystems remain open, and whether consumers and businesses retain meaningful agency all
depend on choices made now [Rothschild et al., 2026].
Left to default incentives, AI risks reinforcing walled gardens: agents embedded in proprietary ecosystems that preserve
friction, lock in users, and concentrate surplus. While large platforms have the capital and technical capacity to invest
in agentic systems, they are naturally disincentivized from designs that threaten existing business models. As a result,
the default trajectory delays the broader societal gains of advanced agentic coordination and instead hardens today’s
market structures into more automated versions of the status quo. Avoiding this outcome requires deliberate early
experimentation with more open, auditable, and transformative designs: before lock-in becomes irreversible.
This is the difference between reacting to where the puck appears headed andactively directing the puck towards a
good outcome.
A practical way for organizations to prepare, without overreaching, is to treat advanced agentic coordination (Stage 3) as
an organizational capability to be built over time to optimize long-term impact, rather than as a feature to be purchased
or a demo to be admired. This shifts attention from isolated tools to system-level design: who agents represent, how
authority is delegated, and how value is created and shared. Or more actionably:
• Invest in machine-readable data and interfaces that enable agent-to-agent interaction
• Redesign workflows to be AI-native, rather than layering automation onto existing processes
• Define clear delegation boundaries and accountability structures for agent-driven decisions
We remain generally early in this transition not only because the technology continues to evolve, but because reconstruc-
tion is difficult and because leaders have yet to make explicit choices about what kind of agentic economy they wish to
build. The central question is no longer whether AI will transform business, but whether that transformation will move
toward openness, competition, and broad-based welfare, or simply harden today’s power structures into faster, more
automated versions of the status quo.
AI’s advance is inevitable. Its impact on society is not.
References
Timothy Bresnahan, Shane Greenstein, David Brownstone, and Ken Flamm. Technical progress and co-invention in
computing and in the uses of computers.Brookings Papers on Economic Activity. Microeconomics, 1996:1–83, 1996.
Mert Demirer, John J Horton, Nicole Immorlica, Brendan Lucier, and Peyman Shahidi. Chaining tasks, redefining
work: A theory of ai automation. Technical report, National Bureau of Economic Research, 2026.
Paul A David. The dynamo and the computer: an historical perspective on the modern productivity paradox.The
American economic review, 80(2):355–361, 1990.
Erik Brynjolfsson and Lorin M Hitt. Beyond computation: Information technology, organizational transformation and
business performance.Journal of Economic perspectives, 14(4):23–48, 2000.
Eleanor W Dillon, Sonia Jaffe, Nicole Immorlica, and Christopher T Stanton. Shifting work patterns with generative ai.
Technical report, National Bureau of Economic Research, 2025.
David M Rothschild, Markus M Mobius, Jake M Hofman, Eleanor Dillon, Daniel G Goldstein, Nicole Immorlica,
Sonia Jaffe, Brendan Lucier, Aleksandrs Slivkins, and Matthew V ogel. The agentic economy.Communications of the
ACM, 69(2):39–42, 2026.
Erik Brynjolfsson, Daniel Rock, and Chad Syverson. The productivity j-curve: How intangibles complement general
purpose technologies.American Economic Journal: Macroeconomics, 13(1):333–372, 2021.
5
