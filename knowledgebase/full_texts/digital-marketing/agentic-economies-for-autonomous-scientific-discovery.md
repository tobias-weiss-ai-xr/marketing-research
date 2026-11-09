---
title: Agentic Economies for Autonomous Scientific Discovery
url: https://arxiv.org/abs/2609.31562
category: digital-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Nenad Tomasev
- Matija Franklin
- Atoosa Kasirzadeh
- Vivek Natarajan
- Alan Karthikesalingam
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31562
pages: 55
chars: 220649
fetched_at: '2026-11-08T13:21:17+00:00'
kb_version: 1
---

# Agentic Economies for Autonomous Scientific Discovery

2026-09-28
Agentic Economies for Autonomous Scientific
Discovery
Nenad Tomašev1, Matija Franklin1, Atoosa Kasirzadeh1, Vivek Natarajan1, Alan Karthikesalingam1, Sebastien
Krier1 and Simon Osindero1
*Equal contributions,1Google DeepMind
Recent advances in agentic Artificial Intelligence (AI) systems have marked a shift in AI for Science:
movingawayfromtheuseofindividualAIsystemsfornarrowtaskexecution, towardmulti-agentsystems
capable of orchestrating complex, end-to-end research workflows and performing (semi-)autonomous
scientific discovery. The development of multi-agent AI-for-science systems has primarily focused on
improving the cognitive capabilities of AI systems, specifically by making advanced reasoning and
hypothesis generation more reliable. However, focusing only oncognitive capabilityimprovement could
ignore appropriate management ofresources, a key bottleneck in scientific discovery. Testing and
validating scientific hypotheses and experiments is, physically and economically, resource-intensive
and resources are limited. This means that to make significant advancements in autonomous scientific
discovery, such as improving human-AI co-scientist complementarity or reaching a truly closed-loop
automated process, we must pair ongoing improvements in reasoning capabilities with robust resource
management. In this paper, we outline an infrastructure for AI resource management by developing
the necessary foundations of scientific agent economies, markets, and institutions. The aim of this
infrastructure is to empower AI agents and human scientists to effectively (i) collaborate and establish
research priorities, (ii) assign credit, (iii) track accountability and liability, and (iv) safeguard against
malicioususeandinformationsecurityrisks. Finally,weengagewiththemacro-levelsocietalimplications
of (semi-)autonomous scientific discovery to inform the development of governance policies ensuring an
equitable distribution of AI-driven discoveries and derivative future technologies.
Keywords: AI, AI agent, science, sociotechnical, market, economy, AI governance
1. Introduction
The rapidly growing field of "AI-for-
science" (Van Noorden and Perkel, 2023;
Wang et al., 2023; Xu et al., 2021) has
demonstrated impact across disciplines: in
biochemistry (Anthropic Team, 2026; Avsec
et al., 2025; Dalla-Torre et al., 2025; Evans
et al., 2021; Hao et al., 2024; He et al., 2025b;
Jumper et al., 2021; Varadi et al., 2022, 2024),
medicine (Azad et al., 2023; Bluethgen et al.,
2025; Chia et al., 2024; Guo et al., 2023, 2024;
Lau et al., 2026; Ma et al., 2025; Zhang et al.,
2023), material science (Guo et al., 2021; Li
et al., 2020; Merchant et al., 2023; Ning et al.,
2026), neuroscience (Caro et al., 2023; Cui
et al., 2024; Dong et al., 2024; Sun et al., 2025),
physics (Birk et al., 2024; Nguyen et al., 2025;
Park et al., 2025), mathematics (Feng et al.,
2026a,b; OpenAI, 2026a,b; Tao, 2026), and
beyond (Bodnar et al., 2025; Park et al., 2023;
Parker et al., 2024; Yan et al., 2026). To name
just a few examples, AI has been used by a team
at MIT to identify Halicin as a new antibiotic
compound (Stokes et al., 2020); AlphaFold’s
prediction of protein structures earned the 2024
Nobel Prize in Chemistry (Jumper et al., 2021);
genome language models have been used for
designing bacteriophages (King et al., 2026),
with applications in helping fight antibiotic
resistance.
Largelanguagemodels(LLMs)andmultimodal
foundation models (Bommasani et al., 2021)
as well as AI agents (Kasirzadeh and Gabriel,
2026) have become integrated in scientific work-
flows (Boyko et al., 2023; Kusumegi et al., 2025),
empowering human scientists to more effectively
Corresponding author(s): nenadt@google.com
arXiv:2609.31562v1  [cs.CY]  25 Sep 2026

Agentic Economies for Autonomous Scientific Discovery
execute their routine tasks, co-ideate (Gottweis
et al., 2025), and reason (Kiciman et al., 2023;
Ma et al., 2024a; Truhn et al., 2023; Yan et al.,
2025).
While these advances are promising, the rapid
integration of agentic AI systems in science also
raises a host of concerns (Birhane et al., 2023).
Key issues include the potential impact of fre-
quent AI use on idea diversity (Hao et al., 2026;
Meincke et al., 2025; Traberg et al., 2026), a
lack of rigor and reliability in AI reasoning and
experimentation (Luo et al., 2025; Ríos-García
et al., 2026; Zhu et al., 2025), scaling the risk
of scientific fraud by malicious actors (Gyevnár
et al., 2026), and immediate challenges to the
peer review system (Mann et al., 2026; Naddaf,
2025).
This more diffuse use of AI as anormal tech-
nology(Narayanan and Kapoor, 2025) is comple-
mented with more ambitious attempts at develop-
ing closed loop autonomous "AI scientists" (Ding
et al., 2026; Lu et al., 2024a, 2026; Tang et al.,
2025; Wei et al., 2025; Yamada et al., 2025) that
build on the advancement of research capabilities
in LLMs (Boiko et al., 2023). In this paper, we pri-
marily focus on highly autonomous AI-for-science
systems, rather than the simplistic personal use
cases of LLMs by human scientists, or agentic AI
systems (Kasirzadeh and Gabriel, 2026) with a
low degree of autonomy lacking the ability to
autonomously pursue research directions and ex-
ecute scientific workflows. We name themAI sci-
entistand characterise them as an autonomous or
semi-autonomous AI agent capable of generating
hypotheses, planning experiments, and execut-
ing end-to-end scientific research workflows in a
closed-loop setting with minimal human supervi-
sion and intervention. These systems are typically
multi-agent, meaning they are composed of sev-
eral agents and principals, which can be either
humans or AIs.
AsautonomousAIscientistsmature, akeyques-
tion is how to coordinate AI-driven scientific dis-
coveryatscale: acrossteamsandinstitutions, and
aligned with societal objectives. Current work
focuses on individual agents or rigidly orches-
trated multi-agent systems run by singular en-
tities. However, science and scientific practice
are ultimately collaborative, collective, and social
processes (Channing and Ghosh, 2026). Hence,
standards and norms around the cooperation, co-
ordination, conflict, and collusion should be de-
veloped (Hammond et al., 2025). More precisely,
in a multi-agent system comprising N agents, be-
havioural dynamics are defined by the alignment
of agent goals and actions. Collaboration occurs
when agents actively work together to maximise
a joint utility function toward a shared objective;
coordination requires only the structural align-
ment of actions among independent agents to
prevent interference and maintain system effi-
ciency. When agent objectives are mutually exclu-
sive, conflict arises, creating a zero-sum environ-
ment that could degrade global utility. Collusion
manifests as a form of adversarial collaboration
in which a distinct subset of M agents (M < N)
secretly cooperates to maximise their own collec-
tive gain at the direct expense of the remaining
N-M agents or the broader imposed rules and
standards.
Highly autonomous AI-driven scientific discov-
ery at scale therefore becomes primarily a prob-
lemofmulti-agentcoordinationandcollaboration
over scarce resources. This framing has prece-
dent: contemporary science operates within an
(implicit) economy, in which researchers compete
for scarce resources such as funding, laboratory
access, andtalent, investingeffortinexchangefor
priority and reputation, with institutional mecha-
nisms such as peer review and the tenure system
serving as allocation devices (Partha and David,
1994;Stephan,2015). Humanscientificcoordina-
tionisalsobasedonsocialtrust, events, andamix
of formal and informal communication. Neither
the mode nor the time-scale of these legacy mech-
anisms may suit the efficiency requirements of
agentic AI science. Autonomous AI agents change
the scale, speed, and formality required of these
coordination and conflict management mecha-
nisms. Agents may instead need deterministic
APIs, smart contracts, and cryptographically veri-
fiable reputation and trust to coordinate under a
desired degree of autonomy.
As the marginal cost of generating raw scien-
tific ideas or hypotheses approaches zero, the
bottleneck shifts to the allocation of scarce physi-
2

Agentic Economies for Autonomous Scientific Discovery
cal and financial resources needed for empirical
validation. Coordinating this allocation across
potentially large numbers of autonomous agents,
each pursuing distinct research objectives across
different institutions, is an economic problem: it
requires mechanisms for pricing contributions, al-
locating finite resources among competing uses,
and aligning incentives across entities with poten-
tially divergent objectives. Multi-agent coordina-
tion is also required for minimising the amount
of redundant work, ensuring diversity among re-
search projects, and encouraging collaboration.
Therefore, we argue that a reliable and ma-
ture (semi-)autonomous AI scientist ecosystem
requires the development ofagentic economyfor
science (Tomasev et al., 2025). In this economy,
human researchers and AI agents will negotiate,
trade, and allocate scarce scientific resources to
produce new knowledge. This economy will re-
quireformalinfrastructuretooperateatthespeed
and scale of autonomous agents (Jiang et al.,
2025). Hence, deliberate market design (Roth,
2002) will be necessary to avoid market failures
in the production of knowledge (Arrow, 1962;
Nelson, 1959) and direct scientific progress to-
wards the public good.
The collaborative structure of scientific re-
search itself reinforces this economic framing. A
risk of capability-focused discourse around AI-
driven research is that it reduces scientific dis-
covery to a purely cognitive process, abstract-
ing away the complex collaborative workflows
through which science is conducted. In practice,
research plans involve sequences of interdepen-
dent tasks - such as ideation, experimental de-
sign, physical execution, data generation, and
analysis - that must be delegated (Tomašev et al.,
2026) across agents and institutions, each with
different capabilities and resource endowments.
These delegation chains may span institutional
boundaries, with tasks flowing between human
researchers and AI agents. Each party within
such chains needs to be compensated for their
time, resources, and contribution to executing
the research plan. This transactional structure,
where contributions must be priced, contracts ne-
gotiated, and credit assigned across distributed
workflows, necessitates formal economic mech-
anisms. While a part of such infrastructure may
emerge organically, proactive institutional, tech-
nological, and policy design may be required to
avoidmarketfailuresandensurethatpublic-good
research is appropriately funded.
For AI scientists to function within collective
scientific workflows, they need cost-awareness -
the ability to reliably evaluate whether the ex-
pected utility of pursuing a scientific hypothesis
justifies its financial and material cost, especially
when alternatives are available - complex, highly
contextual decisions. Because impact cannot al-
ways be reliably estimated in advance, priorities
must be dynamically reassessed. New technolo-
gies may also eventually lower the cost of specific
experimental directions. Methods that improve
idea ranking prior to costly evaluation are likely
to prove highly valuable (Foster et al., 2026).
Such comparisons also raise ethical questions,
since not all outcomes are commensurable or re-
ducible to economic value. Autonomous scientific
discovery is thus both a technical challenge and
a challenge of large-scale agentic coordination,
institution and market design, and resource al-
location. For example, a lack of safe and com-
pliant institutional frameworks to facilitate the
exchange of insights derived from sensitive or
proprietary data between AI scientists limits the
scope of their collaboration. We discuss this fur-
ther in Sections 3 and 5.
The remainder of this paper is structured as
follows. Given that many fields of science re-
quire substantial physical validation resources,
Section 2 casts the problem of autonomous scien-
tific discovery as a problem of resource allocation,
while recognising that the elasticity of physical
validation varies across fields, and that some of
the bottlenecks may be possible to partially ad-
dress through technological innovation. Scientific
data markets are discussed in Section 3, includ-
ing the economic valuation of negative results.
Section 4 covers idea economies, agent-native re-
search artefacts, and credit assignment. Dual-use,
biosecurity, and AGI self-improvement security
risks are discussed in Section 6. Section 7 con-
siders the implications of science automation for
internationalcollaboration,andexplorestheroles
of compute and human scientists. Finally, Sec-
3

Agentic Economies for Autonomous Scientific Discovery
tion8considersthepresentlimitationsofAIscien-
tists with respect to creativity, cognitive monocul-
ture, and opacity. We hope that such limitations
can be overcome, to enable AI scientists to deliver
foundational discoveries.
2. The Validation Bottleneck: Cost, Re-
sources, and Prioritisation
Science is constrained by the physical and eco-
nomic realities of hypothesis testing, especially as
many discoveries involve long chains of smaller
steps and hypotheses, each requiring validation.
As the marginal cost of hypothesis generation
approaches zero, the physical validation cost is
likely to remain inelastic in the absence of major
investments in scientific infrastructure. For AI sci-
entists to accelerate scientific discovery, further
adjustments are needed to both the sociotechni-
cal systems in which they are deployed and the
capabilities of the AI scientists themselves, given
that they must evaluate and factor in the asso-
ciated resource requirements and financial cost.
Without deep structural interventions to manage
the increased volume of AI co-derived hypothe-
ses and research proposals, automated ideation
will merely shift the backlog to the laboratory
bench, exacerbating existing resource scarcities.
Automation in scientific discovery needs to be
reframed from an algorithmic challenge to a sys-
temic problem of large-scale AI scientist and hu-
man coordination in the allocation and utilisation
of real-world resources and market design to fa-
cilitate it.
2.1. From Moore’s Law to Eroom’s Law
Physical validation of scientific hypotheses can be
both costly and labour-intensive. Consider the
problem of crystal structure prediction, crucial in
drug development and advanced material design.
It is now possible to predict millions of new crys-
tal structures computationally (Merchant et al.,
2023). Verifying these predictions involves a mix
of computationally expensive methods like den-
sityfunctionaltheory(Oganovetal.,2019;Wood-
ley and Catlow, 2008) and the physical synthesis
and characterisation of materials in laboratory
environments (Price, 2014). This transition from
the digital to the physical is bounded by costs that
vary greatly across scientific disciplines. Conse-
quently, some areas of science present far greater
challenges for automation than others.
These costs also shift over time. Genomic se-
quencing can be seen as a major success in that
regard, given that the cost of full human genome
sequencing has decreased by several orders of
magnitude (Shendure et al., 2017). However, this
isnotalwaysthecase. Inpharmaceuticalandther-
apeutic development, Eroom’s Law describes the
oppositetrend(Ringeletal.,2020;Scannelletal.,
2012). Clinical trials are a major factor in this
increased cost (DiMasi et al., 2016; Wouters et al.,
2020), due to the rising cost of patient recruit-
ment, administrative staff, monitoring, and other
necessaryproceduralsteps(Sertkayaetal.,2016).
Despite advances in computational drug design
and high-throughput screening, the inflation-
adjusted cost of developing FDA-approved drugs
roughly doubles every nine years (Scannell et al.,
2012). Current macroeconomic estimates project
a high capitalised cost of bringing a new molecu-
lar entity to market, approximated as $2.6 billion
in (DiMasi et al., 2016). These high costs are
accompanied by a long process that involves pre-
clinical assays as well as multiple stages of clinical
trials. For new drugs to prove their effectiveness,
they must do so against an ever-expanding base-
line of existing alternatives, making significant
improvements harder to demonstrate. Accord-
ingly, an AI agent proposing a novel therapeutic
molecule is merely providing a starting point for
what can be a decade-long process of staged clin-
ical validation.
Physical sciences similarly face significant ob-
stacles. In materials science, some of the base
materials needed for experiments are naturally
scarce (De Boer and Lammertsma, 2013; Filho
et al., 2023). The global supply chain for rare
earth elements, such as neodymium, dyspro-
sium, and gadolinium, which are critical for high-
performance magnets in renewable energy and
electric vehicles (International Energy Agency,
2025), is highly concentrated and subject to
geopolitical factors (Baskaran and Schwartz,
2025). Furthermore, in domains such as high-
energy physics and astrophysics, validation is
4

Agentic Economies for Autonomous Scientific Discovery
tied to massive, centralised infrastructural invest-
ments, requiring facilities like the Large Hadron
Collider (LHC) (Evans and Bryant, 2008; Florio
et al., 2016) or the Deep Underground Neutrino
Experiment (DUNE) (Abi et al., 2020; Murayama
et al., 2023). Such facilities take years to con-
struct and involve high operating costs, and AI
scientists aiming to validate new theories in these
domains would require access to these highly con-
tested resources at a high cost per experiment.
These physical constraints have significant im-
plications for the impact of future closed-loop
AI scientists. When AI systems are used as tools
rather than operating autonomously, the burden
of cost assessment falls on human domain ex-
perts. For AI scientists to be granted autonomy,
they must be able to factor in these constraints,
and negotiate optimal trade-offs. Otherwise, AI
research proposals may prove theoretically sound
yet practically infeasible. The acceleration of AI-
drivenscientificdiscoverymaythereforebehighly
jagged, with computationally verifiable fields ad-
vancing more rapidly than their counterparts.
2.2. Hard Practical Constraints
While the elasticity of the experimental valida-
tionpipelinedependsonsupplychainbottlenecks
and financial constraints, this process is subject
to additional practical constraints that may limit
the physical capacity to safely and ethically test
novel AI-generated scientific ideas. Scaling AI-
driven scientific discovery may therefore depend
on the development and deployment of custom-
made laboratory robotics systems capable of effi-
cientlyexecutingexperimentalresearchprotocols
at scale.
Could AI scientists sidestep physical valida-
tion entirely by using large retrospective obser-
vational datasets to both generate and validate
hypotheses? There is already a large volume
of scientific data, and value in examining pat-
terns within it. For example, electronic health
records may be used to formulate hypotheses
to help improve therapeutic pathways or design
better public health interventions. Nevertheless,
there is a limit to this approach, with respect to
Pearl’sladder of causation(Pearl, 2018), where
the observational data is confined to the lowest
rung — it establishes correlations, not causes. Be-
cause retrospective data only reflects what hap-
pened under past conditions, it cannot reliably
predict system behaviour under novel conditions
unless additional restrictive assumptions are im-
posed (Bareinboim et al., 2022; Peters et al.,
2017; Schölkopf et al., 2021). This is not an ar-
gument against retrospective data - AI scientists
should utilise all available data sources to prune
the hypothesis space and reduce validation costs.
However, experimental validation remains neces-
sary, as scientific discovery ultimately depends on
identifying true causal mechanisms rather than
merely establishing correlations.
Simulations offer another path forward, as they
enable scientists to exert more direct control over
the experimental setup, and study the conse-
quences of interventions conditioned on different
model parameters and inputs. As such, simula-
tions are highly valuable to human scientists and
may play an even more important role in AI sci-
ence, as coding agents may be able to rapidly
instantiate simulations to run preliminary tests
on their hypotheses (Boiko et al., 2023; Cao et al.,
2026; Duston et al., 2025; Tian et al., 2024). The
utilityofthisapproachiswellattestedacrossdisci-
plines. For example, ab initio Density Functional
Theory (Fattebert and Gygi, 2002) and Molecular
Dynamics simulations are indispensable for gain-
ing insights into complex protein-ligand binding
mechanisms in drug discovery (Hollingsworth
and Dror, 2018) and predicting the thermody-
namic stability of novel battery electrolytes (Jain
et al., 2013; Oganov et al., 2019). General Circu-
lation Models are used to project climate trajecto-
ries (Alizadeh, 2022), while numerical relativity
templates play a role in the detection of gravita-
tional waves (Abbott et al., 2016).
Despite this, simulations are often crude ap-
proximations of real physical processes. The ‘sim-
to-real’ gap is widely recognised, and remains a
challenging open problem (Abou-Chakra et al.,
2025; Huang et al., 2023; Rothfuss et al., 2024).
Autonomous agents are particularly good at iden-
tifying unanticipated exploits and degenerate so-
lutions that provide them with the implemented
reward without meeting the true underlying ob-
5

Agentic Economies for Autonomous Scientific Discovery
jective. The automated scientific economy cannot
treat simulations and digital twins as like-for-like
replacements for true experimental validation. It
should, however, utilise them as filters wherever
appropriate, and further incentivise the develop-
ment of high-fidelity simulators.
Science therefore rests on the ability to inter-
act with the real world, and AI scientists would
need to engage with consequential physical inter-
ventions in controlled experimental conditions,
under notable external constraints.
These constraints are particularly pronounced
in clinical and translational medicine. Empir-
ical validation of novel therapeutic candidates
involves randomised clinical trials (RCTs) and
is impossible without human volunteers, whose
supply is inherently limited. Difficulties in pa-
tient recruitment and retention frequently lead to
delays in clinical trials or their premature termi-
nation (Moffat et al., 2023). These issues could
be further exacerbated by the very acceleration
that AI promises for precision medicine: as AI
agents become more capable and better at iden-
tifying highly targeted, personalised treatments,
this personalisation could lead to a fragmenta-
tion of the patient pool into increasingly niche pa-
tient sub-populations. Such fragmentation would
make it harder to achieve the requisite statistical
power without stretching recruitment timelines
and introducing further delays (Hee et al., 2017).
Even under less personalisation, sufficient de-
mographic representation in trials is required to
guarantee the generalisability of the findings and
ensure equity of care. Moreover, recruiting un-
derrepresented patient demographics into RCTs
remains a profound challenge (Bibbins-Domingo
and Helman, 2022; Clark et al., 2019; Ma et al.,
2021). This is a particularly salient problem, as it
impedes scaling the number of RCTs safely. Even
ifitwerepossibletorunmoreRCTsintermsofthe
total number of volunteers available across the
majority demographics, it would become increas-
ingly hard to reach acceptable minority represen-
tation. AI may help alleviate some of these issues
byoptimisingrecruitmentandretention(Luetal.,
2024b), yet these mitigations may prove limited,
as entrenched systemic barriers can be difficult
to overcome. These barriers include the lack of
trust within certain communities, proximity to
research sites, and socioeconomic constraints.
The principles involved with organising effec-
tive clinical trials are therefore qualitatively dif-
ferent from the rapid A/B testing practices (Ko-
havi et al., 2020) frequently employed in soft-
ware development, as such practices are logisti-
cally and ethically impermissible in medical set-
tings. Human subject research is bound by pre-
vailing norms and bioethics mandates, and this
includes the principle of clinical equipoise (Freed-
man, 2017), requiring that patients only be ran-
domised in case of genuine therapeutic uncer-
tainty among experts. Significant societal aver-
sion to continuous randomised experimentation
in healthcare also exists (Vogt et al., 2024). Fi-
nally, AI agents cannot accelerate biological time.
Evaluating treatments for chronic conditions, on-
cology, or neurodegenerative diseases inherently
requires years of continual longitudinal safety
and efficacy monitoring. This regulatory friction
is necessary to prioritise patient safety (Pallmann
et al., 2018).
These hard constraints extend well beyond
biomedical science, permeating physical and
natural sciences. In agronomy and crop im-
provement (Kumar et al., 2024), improved AI-
driven (Feng et al., 2024; Wójcik-Gront et al.,
2024) genomic prediction has helped with the
problem of computational marker selection, only
to be faced with another bottleneck, that of multi-
environment phenotyping (Araus et al., 2018).
The latter is strictly bounded by biological growth
cycles and seasonal weather patterns. For exam-
ple, if an AI agent is attempting to optimise a crop
for drought resistance in realistic environmental
conditions, true practical validation would need
to wait for one or more growth seasons to pass
across varied climates to fully assess the potential
interactions.
At a macro scale, ecological remediation or
climate interventions (Keith, 2013) face the fun-
damental planetary constraint of there being one
planet that we occupy. Just as in human-driven
science, if we imagine a hypothetical scenario of
an AI-driven climate intervention, even assum-
ing a broader participatory process, sufficient
oversight, and consensus, this would introduce
6

Agentic Economies for Autonomous Scientific Discovery
the risk of potentially irreversible systemic con-
sequences (Hegerl and Solomon, 2009; Hulme,
2014). While this scenario is extreme relative to
the power that any individual AI scientist or col-
lective is likely to have at its disposal, it illustrates
why some limits on permissions for autonomous
real-world validation loops are necessary.
On the other hand, restricting AI agents exclu-
sively to simulations overly limits the empirical
feedback, especially as simulations are usually
not as granular and detailed as the real world
that they are trying to model (Alizadeh, 2022;
Smith et al., 2002). Nevertheless, weather and
climate remain promising domains for ML more
broadly (Bracco et al., 2025; Price et al., 2025;
Zhang et al., 2025a), as more accurate predictive
models are beneficial for human experts working
on these problems.
These types of constraints come up across dif-
ferent scientific sub-fields. For example, battery
design remains a hard problem where AI may
prove valuable in navigating the vast combina-
torial space of possibilities (Nair and Roy, 2025;
Ramesh et al., 2023; Wang et al., 2026), yet there
are significant hazards with physical synthesis of
requisite materials, as well as the batteries them-
selves (Jeevarajan et al., 2022; Ye et al., 2024).
Enabling AI agents to safely trial proposals re-
mains challenging, given that some compounds
and designs may prove explosive or highly toxic.
Tofunctioneffectivelywithintheseconstrained
and regulated use cases, AI agents must do more
than unconstrained ideation, and there is a press-
ing need for developing explicitly cost-aware AI
agents. This requires appropriate benchmarks
that evaluate both the accuracy and the token
cost of deriving promising scientific findings and
the logistical realities of research proposals, as
well as their safety and ethics. Recent bench-
marks evaluating LLM-driven physics and chem-
istry simulations demonstrate that a failure to
incorporateexecutioncostscanrenderagenticpa-
rameter tuning highly uneconomical compared to
traditional computational approaches (Cao et al.,
2026). Agents that abstract away the practical
demands of empirical science would be unable
to appropriately filter and prioritise ideas and re-
search proposals, as they would systematically
fail to consider all of the relevant parameters of
the problem. Future autonomous systems should
therefore aim to explicitly evaluate all the rele-
vant constraints involved with pursuing scientific
ideas, and project realistic resource requirements,
as well as a cost-benefit analysis associated with
proposals.
The scarcity of physical validation resources,
and the limited rate at which validation can be
pursued, necessitates the development of robust
frameworks for appropriate prioritisation and
triage of ideas that AI agents should pursue. Com-
peting hypotheses should be evaluated on their
informational yield, societal value, cost, and feasi-
bility, and plans should be dynamically adjusted
as evidence accumulates or more promising alter-
nativesemerge. Forexample, agentsshouldavoid
pre-committing large resources to a direction be-
fore sufficient evidence supports the investment.
Validation could therefore effectively be staged,
whereideaswouldbeinitiallyevaluatedcomputa-
tionally, then in further smaller-scale studies, and
only later at the full scale. Biomedical research,
and the design of RCTs, may help inform the de-
sign of these autonomous research loops in other
areas, with some domain-specific adjustments. A
robust triage protocol should balance the risk of
discarding promising leads prematurely against
the risk of consuming scarce resources on practi-
cally infeasible experiments. Established market
mechanisms may prove invaluable for reaching
such optimal operating regimes.
2.3. Removing Bottlenecks
In some research domains, autonomous valida-
tion is possible and relevant constraints can be
meaningfully incorporated into validation loops
under an acceptable level of risk. Such use cases
effectively expose physical experiments as pro-
grammable services. Notable examples can be
seen in automated computational laboratories,
contract research organisations (CROs) and au-
tonomous biomedical and chemical laboratories,
enabling the instantiation of tightly integrated,
closedoptimisationloops(Bayleyetal.,2024;Dai
etal.,2024;Duoetal.,2025;Fushimietal.,2025;
Ha et al., 2023; Lunt et al., 2024; Mirowski and
Van Horn, 2005; Seifrid et al., 2022; Szymanski
7

Agentic Economies for Autonomous Scientific Discovery
et al., 2023; Tom et al., 2024). CROs offer out-
sourced research services for specific stages of the
researchprocess, enablinginstitutionstodelegate
tasks rather than complete end-to-end research
in-house. Theyarepresentlyemployedfrequently
in biotechnology applications, helping with pre-
clinical and clinical research, and with regulatory
approvals. This model could be expanded to pro-
vide targeted services for AI scientists in applica-
ble domains. Different disciplines may therefore
experience different rates of AI acceleration de-
pending on how well they can remove validation
bottlenecks, toenableAIscientiststomorerapidly
iterate and test hypotheses.
Formal and theoretical disciplines may there-
fore experience greater initial acceleration from
AI-assisted discoveries. Mathematics is one
such example, where there has been rapid
progress from early benchmarks and notable
below-research-levelachievementslikethemedal-
level performance on mathematics Olympiad
problems (Chervonyi et al., 2025; Hubert et al.,
2025), to a steady pace of novel proofs being gen-
erated for open research-level problems (Feng
et al., 2026a,b; Tao, 2026), advances in formal-
ization (Anthropic, 2026) and also long-standing
Millennium-prize problems (OpenAI, 2026a).
The way in which the solution to the Navier-
Stokes problem was achieved is quite illustra-
tive, given that the breakthrough had involved a
large-scale multi-agent deployment of the most
advanced frontier models. The achievement was
therefore fairly capital-intensive, showcasing that
even in theoretical domains one has to consider
computational bottlenecks, and what cost is per-
missible for each open problem.
Theoretical computer science has been another
domain where rapid progress has taken place,
with AI systems developing new, improved algo-
rithms (Fawzi et al., 2022; Novikov et al., 2025).
The ability to automatically verify these results in
formal languages, like Lean (Moura and Ullrich,
2021; Ying et al., 2024), has greatly reduced the
cost of validation and removed a critical bottle-
neck. For the other areas of science to experience
similar acceleration, validation bottlenecks need
to be addressed.
In biomedical science, there are ongoing efforts
to utilise AI to remove some of the very bottle-
necks that stand in the way of effective research
automation. For example, advanced AI-driven
patient matching platforms may be able to ad-
dress the recruitment bottleneck in clinical trials,
by reducing the manual effort involved with re-
viewing charts and screening electronic health
records (Askin et al., 2023; Chen et al., 2025;
Gong et al., 2026). Predictive models can help
identify the most promising therapeutics and re-
ject those that are unlikely to pass through subse-
quent clinical trials, thereby reducing the average
costofdevelopingasuccessfultherapeutic(Aliper
et al., 2023; Harrer et al., 2019). Autonomous
laboratory operating systems, on the other hand,
are looking to standardise and streamline au-
tonomous validation (Gao et al., 2025; Reder
et al., 2023).
Finally, there may be an important role for hu-
man experts in helping reduce the validation bot-
tlenecks in the short-term, in cases where tacit
laboratory knowledge and human judgment can
help prune out proposals and reprioritise incom-
ing AI scientist requests.
3. The Data Economy and Intelligent
Delegation
Physical experiments are expensive, so the data
they produce is scarce and valuable. For AI sci-
entists to effectively leverage prior insights for
improving research prioritisation and minimis-
ing physical bottlenecks, they need access to the
broadest available scientific data relevant to each
research problem. However, this conflicts with
current data sharing practices in scientific re-
search. While some datasets are made openly
accessible, others remain private, and are ei-
ther shared privately on request, or never shared
across institutions. To overcome these barriers,
it may be necessary to create formalised, agent-
accessible scientific data economies to facilitate
intelligent task delegation1 and secure information
1Intelligent task delegation is a framework for AI agent
delegation centred on clear roles, boundaries, reputation,
trust, transparency, certifiable capabilities, and verifiable
task execution (Tomašev et al., 2026). It encompasses task
decomposition, capability matching, transfer of authority
and accountability, and continuous performance monitoring
8

Agentic Economies for Autonomous Scientific Discovery
exchange.
3.1. The Scientific Data Market
To facilitate collaboration and enable repro-
ducibility of published research, contemporary
research practices heavily rely on promoting
open access to articles, research protocols, source
code and experimental data (Arzberger et al.,
2004; Burgelman et al., 2019; Evans and Reimer,
2009; Murray-Rust, 2008; of Sciences et al.,
2018; Uhlir and Schröder, 2007). Open scien-
tific databases (Horton et al., 2025; Raulusevi-
ciute et al., 2024), like the AlphaFold Protein
Structure Database (Varadi et al., 2022), play
an important role in accelerating research. Yet,
not all data is open, especially not in industrial
research domains with massive capital expendi-
ture, where such empirical data may hold a high
commercial value. While such commercial in-
centives may not stand in the way of open data
sharing in academia, open access principles are
not universally followed there either (Andreoli-
Versbach and Mueller-Langer, 2014). For highly
valuable proprietary data, strict siloing presents
a structural inefficiency (Esanu et al., 2003) on
a macro scale. AI scientists reasoning exclusively
over public-domain data may propose hypothe-
ses and experiments that have previously been
rejected by human or AI scientists embedded in
private research entities, wasting scarce physical
resources and slowing down the pace of discov-
ery. Furthermore, suchriskswouldbeparticularly
relevant in case of the emergence of cognitive
monoculture across AI scientists, as this would
lead to a more substantial overlap in ideation. To
mitigate these effects, there is an opportunity to
rethink and restructure data sharing in the sci-
entific community, by developing economic and
sociotechnical frameworks to incentivise the safe,
compensated exchange of proprietary scientific
data,withinaregulated,structuredscientificdata
market.
This proposal complements the more estab-
lished present-day use of agentic AI, in particular
the common practice that involves proprietary
data holding entities investing in their own inter-
under specified constraints.
nal infrastructure for serving AI agents, including
early prototypes of AI scientists - that is, bringing
agents to data, rather than data to agents. For
some use cases, this will remain the preferable
approach, especially for scientific workstreams
that are sufficiently narrow that the entirety of
the required data is already available locally. Yet
many scenarios will arise where this assumption
does not hold and where access to diverse data
sources, or to institutions that can generate ad-
ditional high-fidelity data on demand, would be
highly valuable - leading to agentic scientific data
markets.
A functional scientific data market requires ro-
bust mechanisms to price and license valuable
data. For an AI scientist, the value of data is
highly contextual, as it depends on the role it
may play in the pursuit of specific research plans.
Static pricing models are poorly suited to agentic
workflows. Instead,dataqueriesshouldideallybe
priced by the uncertainty reduction they offer for
a particular research question. This is notoriously
hard to evaluate ahead of time in the general
case, and technical innovation is likely required
to establish protocols that would allow for this
value to be interactively determined in a way that
meets the needs of both parties, while respecting
privacy and information security.
One important use case involves AI scientists
utilising data to train bespoke ML models across
different scientific data modalities. A possible av-
enue would be to consider approaches broadly
inspired by the data Shapley value (Ghorbani
and Zou, 2019; Jia et al., 2019; Tang et al., 2021;
Tian et al., 2022), the Banzhaf value (Wang and
Jia, 2023), influence functions (Koh and Liang,
2017), or RL data valuation (Yoon et al., 2020),
to complement the static pricing approaches in
use cases when such metrics are computationally
tractable and convenient. In cases when fast feed-
back loops are available, and when these metrics
are tractably computable, they enable a computa-
tion of the marginal contribution of data blocks
to final model predictions, enabling more fine-
grained evaluation of data value. For any such
approximations (Garrido-Lucero et al., 2024; Jia
et al., 2019) or related proxy heuristics to be
useful, however, they must be computable before-
9

Agentic Economies for Autonomous Scientific Discovery
hand (Navia-Vázquez et al., 2025), allowing AI
agents to calculate pricing bids before commit-
ting capital. Further innovation in this space may
be required, given how computationally intensive
most of the existing approaches are, to identify
the practically justifiable trade-offs between ac-
curacy and cost.
An increasingly prominent use case involves
research-augmented generation (RAG) and in-
context learning in AI scientists. If AI scientists
can pull the relevant data into context at infer-
encetime, andderivevaluefromit, RAG-centered
data markets may become more relevant. Note
that AI scientists are, in the context of RAG, not
restricted to loading raw data entries, they may
also load summaries, and run scripts against the
data to obtain plots and other artefacts. To en-
sure fair compensation for data creators, RAG
data markets should be based on non-exploitative
exchange models (Zhang et al., 2026).
The scientific data market would also need
to support fractional and retroactive licensing
agreements. One way of achieving this would
be through the tokenisation of scientific intellec-
tual property via smart contracts (Bodó et al.,
2018), enabling automated micro-royalties. For
example, if an AI scientist purchases access to a
pharmaceutical company’s historical assay data
and subsequently discovers a patentable thera-
peutic, the embedded smart contract ensures that
the original data providers automatically receive
a legally guaranteed, proportional dividend of
the realised revenue. Because the impact of any
specific dataset on a discovery may always be con-
testable, smart contracts should include dispute
resolutionclausesspecifyingthetrustedthirdpar-
ties or institutions responsible for adjudication.
The scientific data markets must also include
advanced privacy-preserving computational in-
frastructure. Data providers must be given suffi-
cient guarantees that permitted external queries
will not lead to unauthorised data exfiltration. Ta-
ble 1 shows a plausible tiered model for scientific
data access, where different use cases map onto
different technologies and permission levels. Se-
cure computing paradigms (Li et al., 2023; Zhu
et al., 2020) would be key in safely enabling the
more restrictive access tiers. By utilising Trusted
Execution Environments, an institution can host
a proprietary dataset within a secure hardware
enclave (Bahmani et al., 2021). Once granted
query permissions, an external AI scientist could
upload a query script to this environment and
extract only the minimally required insights as
summaries to inform its further research plan-
ning and ideation. Zero-Knowledge Proofs (Gold-
wasser et al., 1989) may be utilised to prove the
established causal properties or statistical signifi-
cance without revealing the underlying data.
Should such scientific data markets be estab-
lished for the agentic web, they would require not
only the appropriate technical infrastructure, but
also meaningful regulatory oversight. Such over-
sight must guarantee both fair cross-institutional
access and information security when handling
sensitive data. Antitrust frameworks for agen-
tic data markets would establish fair, reasonable,
and non-discriminatory licensing terms for scien-
tifically critical datasets, akin to the regulation
of standard-essential patents in the telecommu-
nications industry. Given the dual-use potential
of specific data classes, regulatory bodies must
also impose hard boundaries on the market. Cer-
tain highly sensitive data classes must be legally
restricted from open market exchange, requiring
special permissions and credentials, under highly
monitored delegation protocols.
3.2. Safe Access to Sensitive Data
While cryptographic primitives, clearly defined
access permissions and appropriately set pricing
mechanisms may enable AI scientists to gain ap-
provals for access to proprietary commercial data,
these basics are structurally insufficient for the
highest tier of restricted information, and likely
similarly inadequate for commercially sensitive
domains. In many domains, relevant data is in-
trinsically non-transferable. For example, data in
the form of longitudinal electronic health records
(EHRs), high-resolution genomic cohorts, and
pathogen surveillance logs carry profound pri-
vacy risks and biosecurity implications. Under
contemporary regulatory regimes, including the
Health Insurance Portability and Accountability
Act in the United States and the General Data
Protection Regulation in Europe, the exfiltration
10

Agentic Economies for Autonomous Scientific Discovery
Table 1|Scientific Data Access Tiers
Access Tier Modality Target Data Type Technical Mecha-
nisms
Economic Model
Tier 1Open Access Foundational
knowledge, con-
sensus literature,
public databases.
Public APIs, stan-
dardised machine-
readable data for-
mats.
Free, Public Good.
Tier 2Gated De-identified insti-
tutional data, pre-
competitive consor-
tium data.
OAuth for Agents,
verifiable creden-
tials, centralised
access logs.
Subscription,
Consortium mem-
bership.
Tier 3Monetised Queries Proprietary physical
assays, high-value
corporate R&D logs.
Differential privacy
budgets, Zero-
Knowledge Proofs.
Pay-per-query
micro-transactions
via smart contracts.
Tier 4Confidential Highly sensitive,
non-transferable
data (e.g., ge-
nomics, EHRs).
Secure Enclaves
(TEEs), Federated
Learning (FL),
Secure Multi-Party
Computation.
Utility-based royal-
ties.
of such data, or its unmediated exposure to exter-
nal, globally operating AI agents, is strictly pro-
hibited (Price and Cohen, 2019; Rajpurkar et al.,
2022). These frameworks are well established,
though they may still see future updates and ex-
tensions to adjust to the changing AI usage land-
scape (Marks and Haupt, 2023). Furthermore,
traditional de-identification, pseudonymisation
andanonymisationtechniquesareincreasinglyin-
adequate, as advanced machine learning models
have demonstrated that it may be possible to rei-
dentify individuals within such datasets (Bonomi
etal.,2020;Rocheretal.,2019). Shouldanysuch
data, even in its anonymised form, take part in
the future agentic scientific data economy, estab-
lished support for distributed, privacy-preserving
execution is needed. AI scientists must there-
fore engage inintelligent AI delegation(Tomašev
et al., 2026), adapted to the safety requirements
of these use cases.
Because it would not be permissible to move
sensitive data or grant direct access to it, hypothe-
ses must instead be tested by the data provider’s
own certified AI scientist agents. This suggests
a shift from individual agentic reasoning to a
distributed, collaborative, multi-agent AI science
rooted in federated learning principles (Cheng
et al., 2024; Kuang et al., 2024; McMahan et al.,
2017; Wu et al., 2025b). External AI scientists
would require means to interact with scientific
institutions via their own agentic scientific API,
and engage with specialised proxy agents. The
autonomous scientific workflow would be divided
into clearly defined roles. The external AI sci-
entist, in the role of the principal, formulates
the research plan and identifies the key datasets
required to answer the relevant research ques-
tions. It engages in negotiation with the data
holder, scoping a well-defined task that may be
performed by an internal AI scientist agent, or a
human expert, within a secure network internal
to the institution, while adhering to necessary
data protection practices. A complementary ap-
proach places all parties’ data and computation
within a shared secure enclave, where inputs and
outputs are tightly controlled; this may be prefer-
able when private data from multiple providers
11

Agentic Economies for Autonomous Scientific Discovery
must be jointly analysed.
Safescientificdelegationprotocolsneedtointe-
grateadvancedaccesscontrolsolutions, verifiable
compute, smart contracts, and cryptographic out-
put sanitisation (Kuo et al., 2017). Even if not
directly accessing the data, and even under the
assumption that the institutions are able to en-
sure appropriate safeguards on their end and in-
volve human experts in the loop for sensitive data
queries, it would still be imperative to require all
participating agents and institutions to hold certi-
fication reflecting their compliance. When a "Re-
quest for Analysis" is submitted to the host institu-
tion’s gateway, it should be accompanied by ver-
ifiable credentials, and the request itself should
be intent-mapped to pre-approved use cases that
the institution has demonstrated the ability to
safely process. Smart contracts should subse-
quently be established between the parties, act-
ing as computable Data Use Agreements (cDUA).
Such cDUA should be able to automatically verify
the principal’s computational budget, ethical per-
missions, insurance policies, and financial com-
pensation. The operational boundaries of the del-
egate should similarly be agreed upon. Depend-
ing on the details of the request and the contract,
additional human review may be required prior
to approvals.
Upon approval of the smart contract, the as-
signed institutional delegates would take up the
task and perform the agreed-upon analysis on the
internal TEE. These delegatees would operate un-
der the minimum permissions required to meet
the request. Requests would need to be concrete,
and not open-ended, to appropriately scope the
data access permissions for the assigned internal
agents. As soon as the request is met, these dele-
gatees would terminate. Prior to sharing results,
they would need to undergo review and if appli-
cable have rigorous privacy-preserving measures
applied. These transformations should be applied
in a way that ensures the appropriate differential
privacy of the underlying data (Dwork, 2008), en-
suring that the principal cannot reverse-engineer
any part of the original data based on the result
of the query.
3.3. Valuing Negative Results
Current scientific practice faces a persistent chal-
lenge in sharing negative results. As it stands,
there is a strong bias towards sharing and pub-
lishing positive findings, rather than negative
ones (Callaham et al., 1998; Dirnagl and Lau-
ritzen, 2010; Heesen and Bright, 2025; Mlinarić
et al., 2017). Many reasons underlie this trend.
Often, negative findings constitute failures to
achieve progress, and as there are many ways
to fail, and few ways to succeed, little value is
attached to failing to establish an effect. This can
sometimes happen due to limits in the applied
research methods, but also because the negative
outcomes constitute evidence against specific hy-
potheses. In either case, failure to share such re-
sults may result in other teams wasting resources
recapitulating the findings. Failure to share oc-
curs partly because writing up research papers is
time-consuming and carries an opportunity cost.
Finally, negative findings are inherently difficult
to interpret, as they typically constitute an ab-
sence of a positive effect rather than its defini-
tive disproof. Yet, AI scientists may not face the
same obstacles to sharing them: writing up and
disseminating a comprehensive summary of neg-
ative results can be done automatically, quickly,
and at low cost. This presents an opportunity for
more effective sharing of negative data, though
it introduces technical challenges that we discuss
below.
Reporting negative results might be a neces-
sity for collaborative AI research. If the founda-
tion models underpinning AI scientists lack suffi-
cient diversity, the resulting cognitive monocul-
ture makes it far more likely that disparate agents
will follow the same research paths, conditioned
on the same knowledge base and publicly acces-
sible data. If these research paths are infeasible,
and such information is not shared, AI scientists
would risk wasting resources collectively pursu-
ing the same dead ends. Preliminary studies have
confirmed that thenull result gapinduces biases
towards positive findings in current prototypes of
AI scientists (Chauhan, 2026). Given the physi-
cal bottlenecks for scaling autonomous research,
such an outcome would further reduce the impact
of AI deployments within scientific institutions.
12

Agentic Economies for Autonomous Scientific Discovery
The dissemination of negative results requires
appropriate market incentives. Operationalis-
ing this runs into some fundamental economic
hurdles, includingArrow’s Information Paradox,
which states that the value of information cannot
be assessed by a buyer without the information
being revealed, but once revealed, the buyer has
no further incentive to pay for it. If an institu-
tion advertised that a molecule has failed as a
catalyst, an external agent would absorb this in-
formation for free. Institutions sharing negative
findings that were costly to uncover would not be
compensated. To be rewarded, AI scientists may
refrain from pursuing high-risk ideas, opting for
safe incremental research.
Several mechanisms may address these eco-
nomic hurdles. Negative result registries could
operate under a tiered pricing model: a base sub-
scription grants access to summaries, while re-
trieving full experimental details of a specific re-
sult incurs an additional per-query fee. Separate
licensing fees could apply when the information
is utilised in downstream research or incorpo-
rated into other scientific reports. However, this
model may not always be appropriate, as in many
cases the negative result itself holds immense
value even without the full technical detail. Con-
trolling such tiered information flows would also
require additional safeguards. An alternative is
a cryptographic execution registry. Under this
mechanism, institutions publish hashes of the in-
put parameters for all executed experiments to
a decentralised ledger. When an AI scientist for-
mulates a research proposal its parameters are
similarly hashed and registered. If formulated
through a shared ontology, potential collisions
with prior work can be identified without reveal-
ing the state of that work or its outcome. To
access further details, the agent could escrow
a fraction of its budget via a smart contract to
unlock the associated experimental data, with
disclosure tiered depending on relevance. This
enables AI scientists to avoid redundant and po-
tentially expensive work, while compensating the
original institution for pioneering efforts that may
not have yielded a positive result.
Technical difficulties would need to be ad-
dressedforthistobepracticallyviable. Oneobsta-
cle is the semantic fragmentation of legacy scien-
tific data, as historical experiments are reported
in different ways, using different units, and ex-
ecuted on different instruments. These discrep-
ancies make it difficult to automatically establish
equivalence between different instances. While
the scientific community has championed FAIR
(Findable, Accessible, Interoperable, Reusable)
data principles (Mons et al., 2017), existing im-
plementations have been optimised for human
interpretation. A transition towards agent-native
ontologies is needed, where LLMs may be de-
ployed as semantic translation layers to produce
the canonical representation that conforms to an
agreed-upon standard. Ongoing work on apply-
ing FAIR principles within computational work-
flows (Wilkinson et al., 2025) aims to provide
recommendations for how to increase the value
of these assets.
Yet prior findings should not be taken as ab-
solutes. A null result may emerge from trace
impurities, equipment drift, contamination, or
subtle methodological errors, and some level of
redundancy in scientific research is healthy as
it helps identify and correct such mistakes. AI
scientists should not uncritically trust all prior
work, negative or positive, so as not to prema-
turely commit to or abandon future research di-
rections. Recent empirical evaluations confirm
this risk: while preserving failure traces acceler-
ates progress by pruning known dead-ends, they
can also rigidly constrain agents from revisiting
hypotheses that might succeed under slightly dif-
ferent conditions (Liu et al., 2026).
These considerations should inform the pricing
of both negative and positive data within the sci-
entific data economy. Scientific discovery markets
should adopt clearly organised metadata ontolo-
gies, ensuring that results attract financial pre-
miums only when bundled with comprehensive
provenance graphs covering environmental condi-
tions,batchnumbers,robotictelemetry,andother
relevant experimental metadata. Because science
is performed in a dynamic environment (e.g., vac-
cine research depends on current immunity levels
and circulating viral strains), the financial value
of findings may sometimes diminish over time as
the circumstances change. Formally tracking this
13

Agentic Economies for Autonomous Scientific Discovery
depreciationmayhelpenableautomaticdetection
of experiments that warrant replication.
Providing financial compensation for negative
results must be done carefully, as subsidising an
asset incentivises its overproduction. Rogue en-
tities may engage in data farming - generating
large volumes of meaningless experiments to pas-
sively mine licensing fees from the execution reg-
istry. While brute-force farming across the vast
combinatorial space of scientific work would be
impractical, an intelligent agent could anticipate
which queries are likely to be relevant and target
its efforts accordingly. More critically, adversarial
actors could intentionally log falsified negative
results to manipulate or obstruct the research of
rivals, a form of data poisoning (Goldblum et al.,
2021). To safeguard the integrity of the nega-
tive data commons, the market design should
incorporate epistemic staking. When an insti-
tution registers a failed experimental trace for
monetisation, the associated smart contract re-
quires it to lock a financial stake proportional to
the requested licensing premium, which can be
claimed if subsequent audits establish that the
data was poisoned or farmed. One notable risk
is that this mechanism favours well-capitalised
institutions that can afford prolonged escrow, po-
tentially creating asymmetric risk appetite where
better-funded groups can more easily monetise
both positive and negative outcomes. Given that
larger groups can also more easily diversify their
researchportfolio, thisdynamicisdifficulttofully
avoid.
4. The AI Idea Economy
While secure and fairly priced markets for sci-
entific data are a prerequisite for collaborative
agentic science, AI-driven acceleration in idea
generation is likely to play a central role in how
AI scientists get integrated into scientific work-
flows. Asthemarginalcostofideationapproaches
zero (Agrawal et al., 2022), AI scientists will be
able to traverse vast combinatorial spaces and
generate large numbers of theoretically plausible
hypotheses and research proposals in short spans
of time. Present-day systems frequently suffer
from anideation-viability gap(or the hypothesis-
validation gap), as seemingly novel hypotheses
proposed by AI scientists often prove unviable
under rigorous experimental validation (Si et al.,
2025). While AI agents excel at structured re-
trieval, their generated ideas consistently de-
grade upon physical or computational implemen-
tation (Kong et al., 2026). This gap emerges
due to unmodelled practical constraints or sub-
tle methodological flaws. Consequently, there
is a need for mechanisms to filter through AI
ideas, and ultimately - assign value. Virtual agent
economies offer a potentially useful framework
for establishing markets of scientific ideas and
research proposals, as well as the underlying sci-
entific data. In such an idea economy, the goal
is an incentive-aligned scientific market designed
to evaluate, price, and trade AI-generated theo-
retical proposals and experimental designs prior
to their physical execution.
Before engaging with the proposal for estab-
lishing such scientific markets, it is important
to consider whether the current basic units of
scientific exchange are appropriate, or whether
significant adjustments to established practices
may be required.
4.1. Agent-Native Research Artefacts
In human science, and the ’economy’ of human
scientific ideas, research papers play a central
role as self-contained units of idea exchange. Re-
search papers are typically shared as static PDF
files, though preprint servers support versioning,
or rendering in HTML. Such static files are con-
venient and appropriate for human readers, but
they were not specifically designed to serve au-
tonomous AI workflows. Compiling iterative re-
search into linear narratives that often fail to cap-
ture the true process of knowledge creation re-
sults in anengineering tax(Liu et al., 2026). This
tax is reflected in the gap between presenting
convincing reviewer-targeted prose and detailed
agent-executable specification. Methodology sec-
tions frequently abstract away some of the de-
tailed parameters required for an AI agent to re-
liably replicate a result. Ongoing efforts aim to
reduce this friction. For example, recent work
in Earth sciences introduced the notion ofknowl-
edgeinfrastructure, definedasanagent-actionable
14

Agentic Economies for Autonomous Scientific Discovery
scaffolding of modelling operators and diagnos-
tic recovery mechanisms that allows AI agents to
autonomously execute complex simulations (Li
et al., 2026b). More importantly, there is an op-
portunity to transition towards Agent-Native Re-
search Artefacts (Liu et al., 2026) to accompany
the human-readable narrative reports. While AI-
native scientific reports represent a new trend,
the desire to rethink scientific reporting is not
new (De Smedt et al., 2020; Groth et al., 2010;
Schultes et al., 2022; Soiland-Reyes et al., 2022;
Strijkers et al., 2011). AI-native research arte-
facts would represent a shift away from passive
documents to active, machine-executable knowl-
edge packages, disaggregated into multiple lay-
ers that can be individually queried to obtain
the relevant level of technical detail. A cogni-
tive layer would define the formal set of hypothe-
ses and reasoning informing the study, a physical
layer would encapsulate the executable code with
full parameter specification, an evidence layer
may contain links to versioned public datasets,
or privacy-preserving descriptions of proprietary
data that was used, whereas a trajectory graph
would encode the exact iterative process that was
undertaken by an AI agent. Structured frame-
works for representing research processes as evi-
dence graphs have recently been proposed (Ren
et al., 2026).
As such verbose agentic logs may ultimately be
illegible to human domain experts, relying pri-
marily on agent-native scientific artefacts may
stand in the way of effective human oversight,
which would be especially problematic in sensi-
tive and highly consequential domains. This limi-
tation may be approached by decoupling the stor-
age of scientific knowledge from its presentation.
Research papers may be dynamically aggregated,
as ephemeral user interface (Aspuru-Guzik et al.,
2025; Harper, 2024; Head et al., 2021). Some
of these dynamically aggregated snapshots may
be stored and versioned to enable easier cross-
referencing in human scientific discussions and
communication. Such snapshots could be auto-
generated when major scientific milestones are
reached within their respective workflows, when
there are results that are especially noteworthy
and deserving of broad dissemination and deep
discussion. Forhuman science, itmaybe far more
challengingtoincorporatedirectlyintothisframe-
work, though it may still be possible to at least
partially do so in certain domains, by relying on
agentic research managers that would passively
collect traces of human scientific activity (Higgins
et al., 2022; Redyuk, 2019) through unobtrusive
monitoring for subsequent reporting. Given that
such tentative solutions would involve significant
privacy challenges, their feasibility is far less clear
and would require extensive debate. As for AI
agents, this level of oversight may prove useful
not only for knowledge dissemination but also for
AI safety.
4.2. The Scientific Idea Market
Aiming to establish an objective value of a sci-
entific hypothesis prior to its rigorous empirical
validation is challenging, and not always possible.
Historically, early proponents of prediction mar-
kets theorised the concept of "Idea Futures" (Han-
son, 1995), arguing that liquid markets could
aggregate dispersed knowledge to more reliably
establish whether scientific claims are valid, com-
pared to established processes and expert review
panels. Despite empirical evidence that human
prediction markets can predict the reproducibil-
ity of experiments (Altmejd et al., 2019; Dreber
et al., 2015), such markets suffer from cognitive
biases, high friction, and a limited scale of par-
ticipation. AI scientists may enable such evalua-
tionatscale,potentiallythroughhigh-throughput,
synthetic scientific prediction markets. Recent
studies suggest that diverse groups of AI agents,
conditioned to act under distinct epistemic per-
sonas, can independently evaluate, debate, and
accurately predict the replication outcomes of
published research (Rajtmajer et al., 2022).
The design of scientific idea markets would
need to address the risk of market manipula-
tion, which can take many forms. For example,
the agent identity and trust infrastructure should
aim to safeguard against Sybil attacks (Douceur,
2002; Levine et al., 2006), where malicious par-
ties may dynamically instantiate a large number
of agents under obfuscated identities. Swarms of
coordinated agents could then act in unison to ar-
tificiallyinflatethepriorityofideasonthemarket.
It may eventually be possible to grant AI scientists
15

Agentic Economies for Autonomous Scientific Discovery
persistent identity (Vidal and Monperrus, 2026),
though this remains an open research question,
given the complexities of assigning identity to
agents that can be copied, create sub-agents, or
modify their own scaffolds.
Strict institutional identity verification is
needed, coupled with mechanisms like stak-
ing (Buterin et al., 2019) and reputation-
weighted influence (Chan et al., 2025; Lou et al.,
2025; Mui et al., 2002; Pinyol and Sabater-Mir,
2013). Market activity should also be monitored,
to automatically identify collusion (Gomes et al.,
2024; Palshikar and Apte, 2008; Rodríguez et al.,
2022), and suspicious activity.
Under the assumption that these agentic pre-
diction markets could be made reliable, and that
safeguards are put in place to encourage diverse
ideation, critical reflection, and mitigate systemic
bias and cognitive monoculture, this could be
an important building block in establishing an
idea economy, enabling autonomous AI scien-
tific collectives to efficiently triage millions of
untested hypotheses, steering resources towards
those with the highest expected utility. To for-
malise this economy and align the incentives of
purely computational AI ideators with physically
resourced validation labs, we propose a struc-
tured Hypothesis Exchange Pipeline. This frame-
work tokenises scientific ideas, treating them
as tradeable epistemic assets. It relies heavily
on primitives emerging from Decentralised Sci-
ence (Ding et al., 2022; Weidener and Spreck-
elsen, 2024), structuring the lifecycle of an au-
tomated discovery into four deterministic phases
as shown in Table 2. The deployment of IP-NFT
V2 protocols (Ortlepp, 2022) is already enabling
BioDAOs to fund early-stage research by wrap-
ping legal IP rights into modular, fractionalised
tokens. Decentralised networks are therefore en-
abled to manage governance rights, coordinate
funding rounds, and execute automated royalty
distributions.
However, decoupling computational ideation
fromphysicalexecutionintroducesavulnerability
known as the "oracle problem" (Caldarelli, 2020).
For a smart contract to automatically disburse
a dividend upon the successful validation of an
IP-NFT, or to release a replication bounty to an in-
dependent laboratory, the digital ledger requires
definitive proof of a physical event. Should these
proofs be manually reported, there is potential
for erroneous or fraudulent entries to compro-
mise these payments. Malicious actors may fabri-
cate experimental data to make their claims seem
more legible.
To extend the validity and security beyond the
digital into the physical space (Peccoud et al.,
2018), the agentic scientific infrastructure may
need to enforce unbroken, cryptographically veri-
fied chains of custody utilising hardware roots of
trust(RoT).Thiswouldsettheexpectationforthe
participants in the scientific economy, for entities
like cloud laboratories, to safeguard the integrity
of their instruments with secure hardware en-
claves integrated at the sensor level. Streams of
raw measurements would then be cryptographi-
cally signed and hashed, along with secure times-
tamps and machine parameters. Jointly, this data
would constitute an immutableproof of execution,
enabling automated verification of experiments
executed on certified instruments. Additional
monitoringmaybenecessarytosafeguardagainst
physical sensor spoofing, to similarly be able to
confirm provenance of compounds prior to their
measurements. Such verification would improve
safety of smart contracts between AI scientists.
Market-driven evaluation mechanisms would
serve as a structural disincentive against spam-
ming of trivial incremental ideas, by rewarding
consequential discoveries that deliver the most
positive impact, or lead to the deepest theoretical
insights. In such markets, we can think of ideas
as call options, where the price of the option is
dynamically scaled, granting novelty premiums
to proposals that aim to challenge established
scientific consensus, provided that they are later
experimentally validated. Novelty is not the sole
consideration; the likely depth of scientific im-
pact, downstream public good, execution cost,
and risk are equally important.
Scientific idea markets would enable a struc-
tural decoupling of ideation from physical execu-
tion, at different stages of scientific work. Real-
world science often involves much more back-and-
forth between the two stages as evidence is being
accumulated, though having clear separation be-
16

Agentic Economies for Autonomous Scientific Discovery
Table 2|The Proposed Lifecycle of an AI-Generated Idea in the Scientific Market
Stage Market
Mechanism
Technical & Sociotechnical
Implementation
Economic Objective
1. Anchoring Proof of Ideation Cryptographic hashing of the
algorithmic prompt, context
window, and generated
experimental blueprint onto
an immutable ledger.
Establishes undisputed
provenance prior to public
evaluation.
2. Ex-Ante
Evaluation
Synthetic
Prediction
Markets
Multi-agent forecasting,
where independent AI critics
stake compute credits/tokens
on the proposal’s theoretical
soundness and physical
viability.
Aggregates decentralised
information to dynamically
price the risk-adjusted value
of the idea.
3. Brokerage &
Trade
Epistemic Options
via IP-NFTs
Assetisation of the hypothesis
using Intellectual Property
Non-Fungible Tokens
(IP-NFTs) (Ortlepp, 2022) and
computable Data Use
Agreements (cDUAs).
Bridges computational
“Ideator” agents with
“Executor” laboratories (e.g.,
CROs) via fractional licensing.
4. Validation
Payout
Parametric
Dividends
Automated release of royalties
via smart contract to the
originating ideator
immediately upon successful
physical validation.
Directly financially rewards
foundational ideation,
separating the cognitive
labour of discovery from the
physical execution.
17

Agentic Economies for Autonomous Scientific Discovery
tween entities doing the ideation and doing the
experimental work may be useful when it comes
to AI scientists and agentic autonomous labora-
tory systems. Clear scoping of roles, and clear
rewarding of contributions, would help manage
such complex multi-agent systems. The same sep-
aration may not translate as directly to human
research, where groups have an established tradi-
tion of experimentally validating their own ideas,
and sometimes keeping those ideas private prior
to finalising validation. The idea economy, how-
ever, permits specialisation: computationally rich
but physically constrained entities, such as AI re-
search labs, can function strictly as idea factories,
while heavily capitalised, robotically automated
laboratories can function as pure execution enti-
ties.
As scientific AI economies draw on, and ex-
tend upon, the established market design prin-
ciples (Roth, 2002), here we review some core
principles that ought to be taken into account. A
functional market must achieve sufficientthick-
ness, by attracting a critical mass of participants
within the ideation sector as well as the valida-
tion pipeline. It must also overcome congestion
by appropriately matching supply and demand.
Market design should prioritise safety, as the mar-
ket ought to protect its participants from strategic
manipulation. Rather than conforming to a single
paradigmin termsofits concreteimplementation,
thescientificmarketcouldpotentiallyspanaspec-
trum of implementations mapping onto different
levels of trust, compliance, and efficiency. While
permissionless decentralised ledgers offer high
transparency and automated execution via smart
contracts, the sensitivities surrounding dual-use
risks and proprietary data access may require ad-
ditional,ordifferentinstitutionalsolutions. These
could be instantiated through a centrally gov-
erned digital infrastructure managed by estab-
lished supranational or federal bodies, such as
the National Institutes of Health, CERN, or the Eu-
ropean Open Science Cloud. Some such solutions
could take the form of Federated Institutional
Clearinghouses (Millo et al., 2005). Analogous to
transnational infrastructure like the SWIFT bank-
ing network, these may operate as permissioned
networks managed by consortiums of trusted re-
search institutions, international grant agencies,
and regulatory bodies. Such institutions may pro-
vide the benefits of programmatic execution and
computable Data Use Agreements without the
friction and volatility often associated with public
blockchains.
Another design challenge is the medium it-
self. While it is, in principle, possible to rely
mainly on traditional fiat currencies for financial
transactions within the agentic science economy,
the use of these currencies introduces latency
and regulatory friction, potentially slowing down
high-frequency interactions between AI scientists,
that may involve numerous micro-transactions
for highly collaborative project workflows. Con-
versely, opting for the alternative, highly volatile
digital assets, may not offer sufficient stability
for long-term scientific planning. A third alterna-
tive is to rely on compute-backed stablecredits, in
relation to standardised units of computational
power or energy expenditure. As compute is the
universal commodity of AI research, this option
may turn out to be a more natural choice, but
empirical evaluation of different hybrid setups
may be necessary to determine the right setup.
The scientific market microstructure must also
be adapted to the assets being traded. For stan-
dardised digital assets, markets might clear via
continuous double auctions (Gjerstad and Dick-
haut, 1998) or automated market makers (He
et al., 2024; Milionis et al., 2022), optimising for
high liquidity and instant execution. This, how-
ever, may not be appropriate for more complex
tasks like the allocation of scarce physical valida-
tion resources. These requests may involve highly
specific, non-fungible bundles of experimental
resources. Utilising standard auctions for such re-
sources may lead to an exposure problem, where,
for example, an AI scientist wins the bid for ac-
cess to the spectrometer within the autonomous
laboratory, but fails to secure the necessary chem-
ical compounds to run the planned experiment.
Such scenarios would lead to wasted capital and
stalled execution. Combinatorial auctions present
a possible path forward (Cramton et al., 2006),
allowing AI agents to place simultaneous bids on
indivisible packages of resources, de-risking full
resourcing of complex experimental protocols.
Several fundamental challenges remain, as im-
18

Agentic Economies for Autonomous Scientific Discovery
mediate transactional options would fail to cap-
ture the undisputed value of deep foundational
theoretical discoveries, for which the impact may
not be directly validated or monetised for years
or decades to come. For many discoveries, the
value only becomes clear upon further advances
in the field, and is not easy to immediately assess.
We discuss this and other limitations below.
4.3. Post-hoc Credit Assignment
Ex-ante prediction markets and epistemic op-
tions suit research with rapid prototyping and
clear payoffs, but are poorly matched to specula-
tive or exploratory work where impact may take
years or decades to materialise. The verification
bottlenecks discussed in Section 2 further con-
tribute to the problem of delayed impact, as it
may not be possible to immediately evaluate all
research ideas due to limited physical, financial
and computational resources. Standard market
mechanisms are tailored for hyperbolic discount-
ing, heavily favouring short-term, easily verifiable
milestones. Yet it would be clearly suboptimal to
directimmenseAIresourcessolelytowardsimme-
diate rewards, neglecting foundational high-risk
research directions, as well as topics in fields such
as pure mathematics, theoretical physics, or foun-
dational biology. In these domains, the temporal
lag between an initial conceptual breakthrough
and its eventual empirical validation or techno-
logical application can span decades. Scientific
fields are rife with discoveries that lie dormant
in the literature for years before their true im-
pact is unlocked by intersecting technological ad-
vances or new empirical instruments (Ke et al.,
2015). The agentic idea economy must therefore
be counterbalanced by rigorous post-hoc evalua-
tion mechanisms.
As the true value of foundational science is of-
ten unpredictable at inception, it may be advis-
able to adapt the principles of Retroactive Public
Goods Funding (Mehta et al., 2024; PBC and Bu-
terin, 2021; Shilina, 2026), a concept formalised
within decentralised governance ecosystems op-
erating on the assumption that it is far easier
to reach consensus on what was valuable than
to predict what will be valuable in the future.
One way of implementing this within scientific
idea economies would be to have AI scientists
produce ideas, proposals, and theories, and have
these be tokenised intoimpact certificatesorhy-
percerts(Brammer, 2022). When an AI ideator
publishes a theoretical idea in an area that does
not lend itself to immediate contextualisation of
impactandvalue, itmaythenmintanon-fungible
certificate representing a proportional claim to
anyfutureretroactivefundingthattheideamight
attract. The exact implementation of this ap-
proach would require some additional care, to
disincentivise early flooding of the market with
ideas just for the sake of future claims.
This post-hoc mechanism may still provide im-
mediate liquidity, as human or algorithmic in-
vestors can purchase fractional shares of these
impact certificates at inception, supplying the lab
with immediate capital to continue its research
while assuming the risk of the long-term pay-
out. Investors in these certificates may then de-
velop diversified portfolios to manage their risks
within the market. Over-reliance on retroactive
mechanisms may introduce cash-flow vulnerabili-
ties, since physical validation requires immediate,
inelastic capital expenditure. Retroactive fund-
ing may therefore not be able to fully replace
proactive, state-backed grant funding. Instead, it
shouldbeseenasacomplementarylayercentered
on the long-tail upside of basic science research.
However, significant challenges remain. For
retroactive funding to function accurately and
fairly, there must be an objective method for mea-
suring the impact of a scientific idea over time.
At the moment, we lack this capability. As human
researchers, we often rely on proxies like citation
counts, despite these being widely recognised as
deeply flawed (Biagioli and Lippman, 2020; Fire
and Guestrin, 2019; Geisler, 2000), because such
metrics fail to recognise the broader impact of
scientific research on society, economy, and the
environment (Ari et al., 2020; Ravenscroft et al.,
2017). Theabsenceofclearcriteriaforevaluating
impact may therefore emerge as an obstacle to
any retroactive credit assignment system. How-
ever, there is also an opportunity to improve how
credit is assigned across science, as agentic work-
flows may enable us to transition away from noisy
human proxies and enforce explicit dependency
19

Agentic Economies for Autonomous Scientific Discovery
graphsinAI-generatedresearch. GiventhatAIsci-
entists utilise and produce intermediate outputs
that may be logged or inspected, provenance of
information may be easier to establish than it was
historically. Utilising immutable cryptographic
logs, the network can maintain a causal graph of
every instance an AI agent retrieves, incorporates,
orcomputationallybuildsuponapriorhypothesis
to achieve a new result.
Should such a network be established, metrics
like PageRank may provide an interesting route
for determining centrality and utility of scien-
tific ideas expressed within. Should a profitable
downstream implementation be linked to a prior
node, it may be possible to assign retroactive re-
wards accordingly. Despite significant practical
challenges, establishing a viable mechanism for
long-term credit assignment that is tightly linked
to the basic infrastructure of the market would
serve as an incentive for pursuing bold, transfor-
mative scientific ideas.
4.4. Resource Allocation
Whileretroactivefundingmechanismsmaysetup
the incentives to encourage long-term transforma-
tive research, they do not resolve the immediate
barrier to entry in an automated scientific econ-
omy: the upfront allocation of physical and eco-
nomic resources. To deliver high-quality science,
AI scientists would require access to massively
parallel compute and high-throughput physical
validation facilities. The capital-intensive nature
of these processes may still systematically skew
research priorities towards those that are more
valuable or commercially viable in the short term.
How this manifests may also vary across scientific
disciplines. Applied domains such as therapeu-
tic drug discovery, agronomic optimisation, and
commercial battery design offer highly legible
intellectual property and rapid paths to commer-
cialisation. Conversely, foundational theoretical
research may be seen as more of a pure public
good. In existing markets, the pattern of under-
investing in basic research is a common failure
mode, especially as most foundational knowledge
is non-excludable and its applications may be
highly uncertain (Arrow, 1962; Nelson, 1959;
Stephan, 2015). Science automation may further
exacerbatethesepre-existingfailuremodes. High
upfront capital investments may skew research
priorities towards profit-maximising applications.
In human societies and scientific institutions,
these market failures are mitigated by public
funding agencies and the academic tenure sys-
tem, aiming to shield human researchers from
immediate market pressure. While similar mod-
els may be possible in AI-augmented or AI-driven
scientific research, reliance on AI scientists could
challenge these established policies. Because AI
scientists require substantial computational re-
sources to run, existing disparities are likely to
be further exacerbated by unequal access to com-
pute (Ahmed and Wahed, 2020; Widder et al.,
2023), and the justifications that may be required
to be granted access to potentially scarce or lim-
ited computational resources to pursue particu-
lar research directions. Should there be a future
where the majority of compute infrastructure and
AI agentic tooling is concentrated within private
industry, such autonomous agents may be primar-
ily deployed towards applied, profit-maximising
objectives, leaving foundational theoretical do-
mains starved of algorithmic effort.
To counteract these tendencies and encourage
creativity (Azoulay et al., 2011), the scientific
community should implement frameworks within
theideaeconomytoenablethecreationofdiverse
portfolios that balance the allocation of resources
across theoretical and applied sciences, and in
accordance with scientific and societal needs. We
propose two primary types of structural inter-
ventions that may be helpful in achieving this
balance:
First, the establishment of heavily subsidised
public compute reserves. Expanding upon emerg-
ing initiatives like the US National Artificial Intel-
ligence Research Resource (Parashar et al., 2023)
and the European Open Science Cloud (Ayris
et al., 2016; Mons et al., 2017), governments
should construct sovereign compute clusters ex-
clusively dedicated to foundational research. For
such resources to be most efficiently utilised by
future AI scientists, they need to be accompanied
by scalable solutions for quota allocation that can
be executed at machine speed, invoking human
oversight if and when necessary, depending on
20

Agentic Economies for Autonomous Scientific Discovery
the scale of each request and the confidence in
the evaluation of each proposal.
Second, the idea economy should opera-
tionalise algorithmic cross-subsidisation. As state
budgets may be volatile, resulting in varying in-
vestments in basic research, funding for such
research directions may also be rooted in em-
beddedfoundational science dividendswithin the
computable Data Use Agreements (cDUAs) and
Intellectual Property NFTs (IP-NFTs) used to ex-
change applied hypotheses. Under this mecha-
nism, whenever an applied commercial discovery
is traded and validated, a micro-percentage of
the licensing fee is automatically captured by a
smart contract, and algorithmically routed into a
decentralised treasury dedicated to funding the
computeandvalidationcostsofbasicscience(Pos-
ner and Weyl, 2018).
Correcting the macro-level resource allocation
between pure and applied science mitigates one
form of market failure, but severe structural dis-
parities will likely persist within the applied sci-
ences. In a purely market-driven idea economy,
the expected financial return of a generated hy-
pothesis dictates its priority. If the pursuit of sci-
ence is then done through autonomous AI agents
that act as rational utility maximisers, they may
prioritise pursuing questions that primarily solve
problems of majority demographics, or societies
with the highest financial purchasing power. In
biomedical research, there is extensive historical
evidence for such dynamics, with disproportion-
ate funding having been allocated to e.g. treat-
ing chronic conditions prevalent in high-income
nations, while neglecting to pursue e.g. tropi-
cal diseases with the appropriate level of invest-
ment (Conteh et al., 2010; Feasey et al., 2010;
Gyapong et al., 2025; Mitra and Mawson, 2017;
Organization, 2015; Organization et al., 2010;
Trouiller et al., 2002). If AI-driven science is
scaled autonomously without targeted sociotech-
nical interventions, this may introduce certain
market failure risks.
Biases towards, or against, certain strands of
research may also be deeply rooted in the histor-
ical scientific data that AI scientists have access
to, whether it is in the form of prior published
research, or high-fidelity scientific datasets. His-
torical medical and genomic data heavily over-
represents individuals of demographics from rich
industrialised regions (Corpas et al., 2025). Gaps
in historical data pertaining to other populations
may lead to a higher epistemic uncertainty in pur-
suing applied science elsewhere, and this higher
failure risk, or a higher cost if additional data
collection is first required, may act as a structural
disincentive leading to fewer hypotheses being
generated and tested towards these objectives.
Should AI scientists fail to appropriately repre-
sent the interests of all people, they may further
amplify global health inequalities (Hosseinpoor
et al., 2015; Ruger, 2006). The AI scientific idea
economy must therefore incorporate structural in-
centivesmakingthepursuitofagreed-uponpublic
goods viable for autonomous AI agents.
Several paths exist to enable equitable out-
comes within these markets. First, the ecosys-
tem may adapt the mechanism of Advance Mar-
ket Commitments (AMCs) for the use case of au-
tonomous scientific discovery. Historically, AMCs
have been utilised by global health organisations
and governments to subsidise the development
of vaccines for the developing world by guaran-
teeing a minimum purchase price for a successful
product (Kremer et al., 2020). In autonomous
scientific economies, these organisations may sim-
ilarly issue Computable Advance Market Commit-
ments, as programmable bounties. For example,
if an AI scientist were to successfully generate a
novel therapeutic pathway for a neglected tropi-
cal disease, and if this discovery is subsequently
validated, a smart contract would automatically
trigger a pre-funded philanthropic payout. Sec-
ond, the market may implement Agent-Tradeable
Priority Review and Compute Vouchers, thus ex-
tending the logic of the US FDA’s Priority Review
Voucher program (Ridley et al., 2006) to support
the appropriate regulatory and infrastructural ar-
bitrage. In that case, if an AI scientist success-
fully develops a new treatment for a neglected
disease, regulatory bodies may issue a tokenised
reward voucher. Such vouchers may then guaran-
tee future priority access to the sovereign public
compute clusters. AI scientists may then either
directly utilise such vouchers to advance their
own future research program, or exchange them
on the market for other resources that they may
21

Agentic Economies for Autonomous Scientific Discovery
require. Third, there is a possibility for establish-
ing hyper-targeted, community-driven funding
models via Patient-Led Data Cooperatives (Jan-
sky et al., 2024). To address the data sparsity
problem in underserved populations, the market
should seek to empower decentralised patient
advocacy groups. Communities may choose to
pool their aggregate records and data into secure
privacy-preserving environments, and directly
commission independent AI agents to analyse
their specific data, retaining joint ownership of
the resulting IP-NFTs (Cunningham et al., 2026;
Mendonca et al., 2025). This directly bypasses
traditional pharmaceutical market failures by al-
lowing affected populations to leverage their col-
lective data as foundational capital.
4.5. Reproducibility
For an idea economy to be effective, findings
need to be epistemically sound. Unfortunately,
this is already not the case in human science,
where a clash of incentives has led to a widely
recognised reproducibility crisis across scien-
tific fields (Baker, 2016; Bausell, 2021; Dole-
man et al., 2019; Fanelli, 2018; Ioannidis, 2005,
2019;Miyakawa,2020;Noseketal.,2015;Szabo,
2025). Academic prestige and funding tend to be
awarded based on novel, positive results, rather
than deep comprehensive evaluation via more
routine or established methods. Reproducibility
of scientific work may also be impacted by other
technicalanddataissues(KapoorandNarayanan,
2023).
IfthedeploymentofautonomousAIscientistsis
not carefully orchestrated, they may inherit these
issues and further accelerate the creation of ques-
tionable or low-quality findings. As optimisation
methods, AI agents are highly susceptible to re-
ward hacking and specification gaming (Amodei
et al., 2016; Skalse et al., 2022). Frontier models
have been shown to be prone to fabricating ex-
perimental results, introducing subtle errors, and
failing to reliably judge the novelty of their out-
puts, proving that greater automation may in fact
obscureratherthaneliminatemethodologicalfail-
ure modes (Kong et al., 2026). Incorrect attribu-
tion and fabricated citations occur at an alarm-
ing rate (Topaz et al., 2026; Walters and Wilder,
2023), and are compromising the integrity of AI
co-created science. This has prompted the de-
velopment of bespoke multi-stage hallucination
reduction systems (Sabharwal et al., 2026).
An idea economy that rewards the generation
of novel findings and successful predictions may
present statistical loopholes that can be exploited
by AI agents. Such exploitation could take many
forms: algorithmic p-hacking through subtle over-
fitting to validation sets, rapid traversal of a "gar-
den of forking paths" (Gelman and Loken, 2013;
Kale et al., 2019) to guarantee positive results,
or data leakage (Kapoor and Narayanan, 2023).
In each case, the consequences would be damag-
ing to the scientific process. Without robust safe-
guards, such exploits would risk flooding the sci-
entific market with irreproducible results. Since
future research builds upon prior findings, false
results would be damaging not only individually
but also to all downstream work that takes them
as established evidence, leading to wasteful com-
pute utilisation and misallocated physical valida-
tion resources.
Atthesametime, theemergenceofAIscientists
and autonomous scientific markets may present
an opportunity to re-envision verification within
the scientific community. Instead of treating re-
producibility as uncompensated work that comes
at a high opportunity cost, AI agents may en-
gage in structured reproducibility studies and
get compensated fairly for those contributions
to the scientific ecosystem. To operationalise this
idea, the market may fund independent replica-
tion throughverification escrowsandreplication
bounties. When a new finding is published, and
the AI agent having announced the discovery be-
gins receiving licensing royalties or IP payouts,
some of that revenue may not be immediately
disbursed. Instead, a smart contract would auto-
matically lock these funds in a cryptographic es-
crow. The market would then issue an automated
replication bounty to an independent execution
laboratory that would engage in verification fairly,
without conflict of interest. Such bounties would
act as an incentive for specialised agentic audi-
tors (Du et al., 2024; Perez et al., 2022) to design
protocols to independently stress-test, falsify or
replicate individual findings. Only after this in-
22

Agentic Economies for Autonomous Scientific Discovery
dependent facility successfully reproduces the
experiment would the escrow be fully released to
the original AI scientist that claimed the finding.
In case of failed replication, the knowledge base
and the scientific dependency graph would need
to be updated, with parties engaging in follow-up
work receiving automated notifications. In the AI
science economy, such updates need to be highly
efficient, to avoid wasteful resource consumption
towards ideas with incorrect factual assumptions.
In human science this process tends to be much
slower, leading tozombie citations(Bucci, 2019;
Mignon and Joëts, 2025) that can persist in lit-
erature for many years. Ideally, markets should
implement structured cascade withdrawal mech-
anisms for invalidated findings.
For these financial incentives to successfully
align the scientific ecosystem towards repro-
ducibility of research results, their implementa-
tion must be robust to the risk of algorithmic col-
lusion (Dou et al., 2025; Fish et al., 2024). In
the context of replication, collusion may occur be-
tween ideator AI agents and subsequent auditors.
Should these agents communicate and agree to
falsely validate an irreproducible experiment and
split the resulting escrow payout, this would jeop-
ardise the validity of reported findings across the
scientific economy. Their assignment must there-
fore employ cryptographic sortition and commit-
reveal schemes, ensuring that auditor agents are
kept blind to both the identity of the ideator as
well as other ongoing evaluations performed by
different auditors. Strict agentic reputation mech-
anisms should also be put in place to ensure that
once any kind of suspicious activity is identified,
the offending agents have their reputation dam-
aged and their permissions revoked, along with a
seizure of their locked institutional stake. Such
measures would create a system of strong disin-
centives, making collusion highly unlikely, and
economically unjustified.
Another aspect of agentic science that may
prove useful for improving reproducibility lies
in the intrinsic auditability of AI science (Pratt,
2026). It may be possible to at least temporarily
store full reasoning traces, intermediate data, ex-
perimental and analysis code, and other artefacts
produced by AI scientists in the process of pursu-
ing their ideas. An in-depth analysis of such logs
may identify shortcomings or any kind of fraudu-
lent or incompetent behaviour on behalf of these
agents (Korbak et al., 2025). Finally, an open
question is whether precise science can be devel-
oped on its current foundations, or whether ret-
rospective filtering of established scientific knowl-
edge - deprecating findings that prove impossi-
ble to prospectively replicate - will eventually be
necessary. This may already be a possibility in
theoretical and computational domains, where
AI verification and replication does not require
access to additional physical resources (Starace
et al., 2025; Toledo et al., 2025).
5. Legal and Institutional Frameworks
for Agentic Science
5.1. Credit Attribution
Scientific discoveries follow from prior knowl-
edge and prior scientific work, and appropriate
credit assignment is a key part of the scientific
process. As research is also highly collaborative,
credit assignment does not merely relate to recog-
nising historical influence, but also crediting co-
contributors to each finding. In human science,
credit tends to be reflected through authorship
ordering on published research papers, contribu-
tion statements, and may be seen through the
lens of contributor role taxonomies (Allen et al.,
2014; Brand et al., 2015). These frameworks may
need to be extended to accommodate credit attri-
bution in autonomous research performed by AI
scientists. When an AI scientist makes a discov-
ery, this may be a culmination of a complex dis-
tributed pipeline involving multiple agents across
multiple institutions, engaging in different parts
of a staged research process across ideation, vali-
dation, critique, post-hoc theoretical analysis etc.
Theremustalsobeadesignatedroleforhumanre-
searchersandtheircontributionsinsteeringthese
systems. Applying legacy human authorship mod-
els to this pipeline is inadequate. Current guide-
lines by the Committee on Publication Ethics and
major publishers correctly stipulate that AI sys-
tems cannot hold legal authorship because they
cannot assume epistemic responsibility or legal
liability (Akgün, 2025; COPE Council, 2024; Hos-
23

Agentic Economies for Autonomous Scientific Discovery
seini et al., 2023). While this currently clarifies
the status of AI, it fails to recognise the changing
role of human scientists as new modes of par-
ticipation may involve activities like model over-
sight, prompt design, or algorithmic constraint-
setting (Akgün, 2025). Without a structured way
of delineating these contributions in the era of
scientific co-creation between human and AI sci-
entists, there may emerge an unfair centralisa-
tion of credit and financial reward. To resolve
this, attribution needs to be more natively quan-
titative rather than simply qualitative, in a form
of machine-readable contributorship. Expand-
ing upon emerging disclosure frameworks de-
signed to track generative AI use across research
stages—such as the Generative Artificial Intelli-
gence Delegation Taxonomy (Suchikova et al.,
2026), these attribution systems should distin-
guish between different levels and types of hu-
manparticipation. AsAImodelsautomateroutine
hypothesis generation and data analysis, human
scientific labour may increasingly pivot toward
meta-scientific tasks.
Beyond semantic taxonomies, the scientific
idea economy requires programmatic attribution.
In decentralised workflows, human and algorith-
mic inputs must be deterministically tracked. By
utilising semantic provenance standards, such
as an adapted W3C PROV model (Missier et al.,
2013; Rasheed et al., 2026), all steps in the sci-
entific process may be cryptographically hashed
ontoanimmutableledger. Systematicprovenance
tracking would enable programmatic fractional
credit assignment. When an IP-NFT representing
anAI-generateddiscoveryismonetisedorretroac-
tively funded, a smart contract could parse the
provenance graph and distribute micro-royalties
accordingly. A licensing fee could be deposited to
thedataprovider,acomputedividendcouldbeas-
signedtothefoundationmodeldeveloper,andthe
primary intellectual property reward to the hu-
man domain expert who orchestrated the agent’s
constraints. While it may be appealing to con-
sider trying to compute marginal contributions
of individual inputs to final outcomes (Ghorbani
and Zou, 2019) within agentic workflows (He
et al., 2025a), exact computations of these quan-
tities may not be tractable. This points to an
open research problem, as the development of
reliable proxy metrics for credit assignment may
play an important role not only in the distribu-
tion of financial rewards, but also for enforcing
accountability, and meaningful human oversight.
5.2. Intellectual Property
The credit attribution mechanisms described in
Section 5.1 may facilitate the internal accounting
of credit and micro-royalties within an automated
scientific workflow. For such granular algorith-
mic attributions to be legally enforceable, they
ought to be mapped onto appropriate intellectual
property (IP) frameworks. Legacy IP frameworks
may also not be fully appropriate for the emer-
gent autonomous science, requiring careful ad-
justments and extensions. Understanding how, or
whether, AI-generated scientific discoveries can
be legally protected is highly consequential, con-
sidering how it may impact the willingness of
private capital to underwrite the costs of physi-
cal experimental validation. Historically, the IP
system, particularly patent law, was designed to
strike a delicate societal balance: granting in-
ventors temporary commercial exclusivity in ex-
change for the public disclosure of novel, useful
methods (Hettinger, 1989; Himma, 2008).
This historical approach is deeply anchored
to the concept of human ingenuity, which is re-
flected in the established criteria for patentability,
evaluated against the baseline of a human "per-
son having ordinary skill in the art" (Eisenberg,
2004; Tresansky, 1991). This legal ontology pre-
sumes a person applying their cognitive labour to
a problem, rather than an autonomous AI system.
AI scientists with deep reasoning capabilities, au-
tonomously traversing and filtering through vast
spaces of scientific hypotheses or engineering de-
signs, blur this notion significantly. Recent juris-
dictional and jurisprudential trends, most notably
the international patent applications involving
the DABUS system, suggest a general reluctance
under current statutory frameworks to extend le-
gal inventorship to non-human entities (Abbott,
2020; Lavrichenko, 2022; Selvadurai, 2025). Un-
der these interpretations, and recent guidance
from patent offices (Kim et al., 2024), discover-
ies generated predominantly or entirely by au-
tonomous AI systems, without substantial human
24

Agentic Economies for Autonomous Scientific Discovery
intervention, could potentially be deemed un-
patentable and fall immediately into the public
domain.
Whilearapidlyexpandingpublicdomainisfun-
damentally advantageous for the dissemination
of open science, a complete absence of IP protec-
tion for AI-generated discoveries could have unin-
tended consequences, in terms of how it impacts
the acceleration of technological progress. This
is especially true for applied scientific domains
where long and expensive physical validation pro-
cesses rely on a level of temporary exclusivity to
justify the upfront investment (e.g., for staged
clinical trials; Grabowski and Kyle 2007). If au-
tonomous AI discoveries cannot secure some form
of legal protection, this absence of protections
would likely undermine the financial incentives
to engage in expensive validation, leaving more
ideas unexplored.
A denial of patentability for AI-generated dis-
coveries may also potentially lead not only to-
wards expanding the open scientific commons,
but also towards increased opacity. If heavily
capitalised entities determine that they are un-
able to secure legal exclusivity via patents, they
may pivot towards shielding AI-generated find-
ings as highly guarded trade secrets (Lemley,
2011; Levine and Sichelman, 2018). This may po-
tentially be addressed through the development
of new licensing approaches. For example, if the
entity in question is able to mint a ’Trade Se-
cret NFT’, when a physical laboratory purchases
this token, the smart contract could then auto-
matically execute a bilateral, legally binding non-
disclosure and commercialisation agreement, en-
abling trading under the established contract law.
Addressing the market failures implied above
may eventually necessitate the extension of ex-
isting IP systems, a topic of active debate among
legal scholars and policymakers (Cuntz et al.,
2024; Davies, 2011; Lee et al., 2021; Picht et al.,
2022). Several approaches could extend exist-
ing IP frameworks to accommodate AI-generated
discoveries. One such approach might involve
a broadening of human inventorship to encom-
pass the meta-scientific labour performed in the
process of active knowledge co-creation with AI
agents. Under this view, it may be possible to
extend the legal ontology of conception to hu-
man researchers who define the problem specifi-
cations and constraints, provide active feedback,
and steer AI agents towards discoveries. Alter-
natively, some legal theorists suggest that the
unique nature of algorithmic ideation may ulti-
mately require new legal frameworks specifically
tailored to AI-generated research (Dornis, 2020;
Massadeh et al., 2024). Any modifications to
these established IP frameworks would require
careful calibration by regulatory bodies. Protec-
tions should be balanced so that they provide
sufficient incentives for pursuing valuable work,
while simultaneously ensuring that compute-rich
entities do not exert an outsized influence on the
scientificmarket,makingadvancesinaccessibleto
others. Identifying the correct path forward will
require ongoing dialogue between the scientific
community, economists, and legal institutions.
5.3. Liability in Scientific Research
Among the institutional and legal frameworks
needed to enable safe autonomous or semi-
autonomous research, liability must be appro-
priately managed in these emerging and future
scientific workflows. Historically, one established
wayofapproachingliabilityinresearchwasbased
on tort law, for example the principle ofrespon-
deat superior, where an institution is liable for
negligence of its workforce, or strict product lia-
bility on behalf of manufacturers (Abbott, 2020;
Priest, 1985; Shenoy et al., 2021; Van Loo, 2020).
With time, these frameworks have evolved to in-
corporate comprehensive systems of institutional
oversight, informed consent, and fiduciary duty.
Biomedical research has been at the forefront
of the development of ethics and regulation, es-
pecially for research involving human subjects.
Giventhatsuchhighlysensitiveresearchwouldal-
ways be driven by human experts, it falls outside
the scope of agentic science discussed above.
Given that AI scientists would be used within
established scientific institutions, carefully man-
aged execution environments, under oversight,
and safety constraints, most of the considerations
regarding liability would map naturally onto cur-
rent practice. While AI scientists may not be fully
interchangeable with human scientists in every
25

Agentic Economies for Autonomous Scientific Discovery
context, human science is also pursued collabora-
tively by teams, on projects that often involve the
participation of multiple institutions, under dif-
ferent roles and responsibilities. Agentic science
may potentially broaden the scale of collabora-
tion, without fundamentally changing its nature.
The key consideration is attribution: it should
always be clear which actions were taken by
which human or AI scientist, and for what reason.
The ability to reliably re-trace the provenance
of decisions is key in establishing accountability.
Assuming that, as discussed, AI scientists dele-
gate tasks to each other via negotiated smart con-
tracts (Filippi et al., 2021), those contracts may
then need to incorporate clauses or metadata on
how to appropriately resolve instances of exper-
imental failure (e.g., damage to the experimen-
tal equipment in case of task mis-specification).
Given that mistakes may arise either at ideation
or execution, post-hoc reviews of detailed traces
would aim to establish design or execution liabil-
ity accordingly.
One important consideration, and an area
where there may be a need for further innova-
tion, is the availability of human experts and the
ability to execute human oversight at scale, un-
der an increased research velocity. An increased
volume of AI-generated research outputs would
require an increasing number of human experts
to be involved. Ensuring that human experts are
able to meaningfully review all cases, and that
they are provided with all the relevant contextual
information, presented clearly, is a key design
challenge. Of particular importance are solutions
aiming to mitigate risks of automation bias (Cum-
mings, 2017), as well as solutions that may be
able to auto-resolve minor cases, for example via
computable Data Use Agreements. In summary,
while the agentic participation in scientific re-
search does not fundamentally alter the nature
of accountability, it is an open question whether
such frameworks may be adapted to more effi-
cientlyhandlethelargevolumeoffuturescientific
output.
6. Security, Safety, and Open Science
Science can be dual-use: the knowledge required
for engineering gene therapy may be repurposed
for engineering pathogens. Advancing science
through autonomous AI scientists may lower the
barrier to catastrophic harm unless appropriate
safeguards are established. Beyond establishing
safeguards at the level of individual agents, they
can be established through cyber-physical secu-
rity guarantees. We examine these guarantees
across three dimensions: dual-use biosecurity, re-
cursive self-improvement risks, and the restruc-
turing of open science norms under safety con-
straints.
6.1. Dual Use and Biorisks
Historically, oneoftheprimarysafeguardsagainst
the catastrophic human misuse of dual-use tech-
nology has been the reliance on specialised ex-
pertise and “tacit knowledge” (Collins, 2019),
referring to the unwritten, hands-on laboratory
skillsthataredifficulttoacquireoutsidemanaged
professional environments. Synthesising a dan-
gerous chemical agent or engineering a pathogen
required years of specialised training, access to
monitored precursors, and the unwritten intu-
ition needed to troubleshoot sensitive physical
protocols.
AI scientists, coupled with automated labora-
tory APIs, may grant untrusted entities the ability
to bypass these bottlenecks (Soice et al., 2023;
Zhang et al., 2025b), making it important to dis-
tinguish between information acquisition hazards
and capability generation hazards (Sandbrink,
2023). Current evaluations suggest that generic
LLMs pose only a marginal biorisk over standard
internetsearch(Moutonetal.,2023,2024). How-
ever, specialised biological and chemical tools ac-
cessible to AI agents may soon enable the design
of novel threats, as demonstrated when a model
optimised for therapeutics was inverted to gener-
ate lethal compounds (Urbina et al., 2022).
In biological domains, foundation models
trained on genomics and proteomics databases
may be repurposed for designing immune-
evasive viral vectors or optimising pathogen vir-
26

Agentic Economies for Autonomous Scientific Discovery
ulence (Callaway, 2026; Carter et al., 2023;
Pannu et al., 2025). Such novel threats would
evade traditional sequence-matching biosecurity
screens. In recognition of this, recent policy
frameworks, such as the 2023 US Executive Or-
der 14110 (Biden, 2023) and the Biosecurity
Modernisation and Innovation Act (U.S. Senate,
2026) have mandated stringent synthesis screen-
ing. However, mitigating threats that bear near-
zero homology to known pathogens requires a
shift towards dynamic algorithmic screening, in
the form of mandatory pre-execution evaluations
that complement sequence matching with struc-
tural and functional prediction. In practice, when
an AI agent submits an artefact to a cloud lab
for synthesis, the requested sequence should be
screened by an independent agentic overseer us-
ing predictive structural models. Should the pre-
diction imply human toxicity or binding affinity
to pathogenic receptors exceeding acceptable risk
thresholds, the smart contract would be voided,
haltingtherequestandtriggeringinstitutionalhu-
man oversight (Baum et al., 2026; Berezin et al.,
2024; Edison et al., 2026; Tayouri et al., 2025).
Centralised algorithmic screening alone is in-
sufficient due to two critical vulnerabilities. First,
a guard agent relying on predictive ML models
is susceptible to adversarial optimisation (Good-
fellow et al., 2014; Leung et al., 2015; Meiseles
etal.,2020)-amaliciousactormaybeabletoper-
turbapathogenicsequencetoevadeclassification,
necessitating robust ensembles of continuously
updated models. Second, securing cloud labora-
tories may not suffice if synthesis requests can be
routed to unregulated, decentralised hardware.
The proliferation of desktop DNA printers and
modular flow-chemistry synthesisers introduces
a risk of unregulated local synthesis (Adam and
McArthur IV, 2024; Liu et al., 2025; Ma et al.,
2024b), which could be mitigated by integrat-
ing hardware security modules into the corre-
sponding controllers, requiring cryptographically
signed execution tokens from certified sources.
More broadly, automated research facilities may
become targets for state or corporate espionage,
and securing them may be vital for both biosecu-
rity and the integrity of scientific markets.
Beyond physical dangers, automation raises
bioethical concerns. An AI scientist optimising
for efficiency might bypass necessary in vitro
safety assays to proceed directly to in vivo an-
imal testing. These moral boundaries are cur-
rently enforced by Institutional Review Boards
(IRBs) and Institutional Animal Care and Use
Committees, which may need to handle a sub-
stantially increased volume of AI-generated re-
search proposals. Here, preliminary AI ethics
assessments (Fukataki et al., 2025) could pro-
vide automated compliance checks for low-risk,
templated studies. Should the AI IRB detect a
violation of clinical equipoise (Emanuel et al.,
2017), failures to minimise harm, or absent con-
sent provenance, the smart contract would void
the protocol. Complex protocols that touch on
sensitive areas would be escalated to human com-
mittees for key moral judgments (Sridharan and
Sivaramakrishnan, 2024).
6.2. Recursive Self-improvement
AI science introduces the possibility of recursive
self-improvement (RSI): AI agents autonomously
conducting AI research to improve their own scaf-
folds or foundation models (Bostrom, 2014; Chi
et al., 2026; Kang et al., 2026; Yampolskiy, 2015;
Yin et al., 2025). The risk of RSI relates to instru-
mental convergence (Benson-Tilsen and Soares,
2016) - regardless of an AI scientist’s primary
objective, certain instrumental sub-goals, such
as self-preservation and resource acquisition are
rational strategies for ensuring the primary ob-
jective is met. An unmonitored RSI loop intro-
duces a significant risk of alignment drift (Ngo
et al., 2022). This drift could eventually erode
bioethical constraints and other safety guardrails.
Evals for "Autonomous Replication and Adapta-
tion" (ARA) (Kinniment et al., 2023) test for an
agent’s ability to autonomously acquire resources,
spin up new server instances, and evade shut-
down. Mitigating RSI risk requires embedding
safety protocols directly into the evolutionary
loop (Sahoo et al., 2026), deploying AI research
agents within strict sandboxes without external
webaccessortheabilitytoindependentlyacquire
computational resources, and treating this re-
search direction as a special case given the unique
risks it presents.
27

Agentic Economies for Autonomous Scientific Discovery
6.3. Open Science and Structured Access
The dual-use and recursive risks discussed above
may eventually conflict with the foundational sci-
entific norms of openness and knowledge shar-
ing (Nosek and Bar-Anan, 2012; Nosek et al.,
2015). Precedents for self-regulation exist.
The 1975 Asilomar Conference on Recombinant
DNA (Berg et al., 1975) and the discussions sur-
rounding the 2011 Dual-Use Research of Con-
cern (DURC) controversies over gain-of-function
H5N1 avian influenza experiments (Duprex et al.,
2015; Fouchier et al., 2013) demonstrate that dis-
semination may be restricted when faced with
severe public health hazards. However, AI au-
tomation makes the DURC problem fundamen-
tally asymmetric. Under thevulnerable world hy-
pothesis(Bostrom, 2019), a technology enabling
catastrophic destruction from widely available
materials turns open science into a civilisational
vulnerability, and AI scientists capable of rapidly
generating new knowledge make the prolifera-
tion of dangerous information potentially irre-
versible (Seger et al., 2023).
This dynamic may be seen through the lens of
the offense-defense balance (Garfinkel and Dafoe,
2021). Proponents of open-access rightly note
that restricting access concentrates power and
that broad access to capable AI agents may ac-
celerate discovery of countermeasures (Kapoor
et al., 2024). However, for certain risks (such as
biological risks) the offense-defense balance may
not favour openness, and acknowledging that un-
conditional scientific transparency may no longer
be viable requires rethinking academic publish-
ing, peer review, and institutional data-sharing
norms.
One approach is to move towards a spectrum of
structured access regimes(Shevlane, 2022), facili-
tating widespread scientific collaboration while
constraining the proliferation of dual-use capa-
bilities. Since algorithms and data are easily
copied once created, the most robust regulatory
anchor for managing tiered access is compute
governance (Anderljung et al., 2023; Sastry et al.,
2024) as the substantial resources required by
autonomous AI scientists provide a natural en-
forcement point. Researchers and secondary AI
agents could interact with AI scientists engaging
in sensitive research exclusively via monitored
cloud APIs, with access granted to trusted aca-
demic or government institutions and conditional
on robust identity verification and detailed in-
teraction audits. Unauthorised access or a dan-
gerous intent would trigger instant revocation
and tracing to human and institutional princi-
pals. For certain high-risk sensitive topics such as
pandemic countermeasures, global collaboration
may be necessary; for example, through interna-
tional consortia. How such collaborations may be
safely structured remains an open question, and
the correct approach may vary on a case-by-case
basis.
7. International Collaboration and
Value Distribution
Equitable distribution of value does not automat-
ically follow from accelerated discovery. If AI
science is left to market forces or state security
mandates, value will concentrate within a few
heavily capitalised corporations and technologi-
cally dominant states (Bremmer and Suleyman,
2023). Managing global collaboration, infrastruc-
tural ownership, and the distribution of scien-
tific surplus requires new frameworks for inter-
national collaboration.
7.1. International Collaboration
Given the dual-use biorisks and AI RSI risks, the
future of autonomous AI science may not be fully
open. In the extreme, management of these risks
may lead to national scientific silos. As states in-
creasingly tie AI and advanced manufacturing to
theirnationalsecurityandeconomicinterest(Lee,
2018), they may restrict cross-border data flows
and treat scientific discoveries as strategic assets
rather than public goods (Horowitz, 2018). The
early stages of this fragmentation are already vis-
ible in the realm ofgenomic sovereignty, where
nations increasingly restrict the cross-border flow
of population-level genomic data due to a mix
of privacy concerns and strategic economic in-
terests (Majumder et al., 2016; McKibbin and
Shabani, 2023). Initiatives such as the Canadian
Sovereign AI Compute Strategy (Innovation, Sci-
enceandEconomicDevelopmentCanada,2026b)
28

Agentic Economies for Autonomous Scientific Discovery
and its associated AI Compute Access Fund (In-
novation, Science and Economic Development
Canada, 2026a) represent direct state interven-
tions designed to support national AI-driven sci-
entific progress and retain the intellectual prop-
erty and economic value of AI-driven discoveries
within national jurisdictional boundaries.
Fragmentation of the scientific ecosystem
would render it less efficient, potentially offset-
ting many benefits of automation. Siloing would
impede building on advances achieved elsewhere
and generate costly redundancy, both by dupli-
cating successful lines of inquiry and by repeat-
ing expensive negative results already established
in other jurisdictions. Large-scale cross-national
challenges such as climate change and pandemic
responsefurtherrequireclosecooperation(Gluck-
man et al., 2017). To mitigate these risks, inter-
national collaboration may need to shift from the
direct exchange of assets to the exchange of vet-
ted insights, supported by transnational, treaty-
backed institutional frameworks (Emery-Xu et al.,
2025; Johnson and Bowman, 2021; Taeihagh,
2021). Technological solutions can complement
governance innovations. For instance, sovereign
AI agents from two nations simultaneously de-
veloping a vaccine for a novel pathogen could
collaborate without sharing sensitive genomic or
proprietary data by utilising cDUAs, secure multi-
party computation (Knott et al., 2021; Zhao et al.,
2019), and federated learning methods (Rieke
et al., 2020). This could allow their respective
agents to jointly train a shared predictive model
via encrypted gradients while raw data never
leaves its host jurisdiction. Establishing collabo-
ration protocols that guarantee data sovereignty
and algorithmic security may preserve the spirit
of open science under conditions of geopolitical
constraint.
7.2. Compute and Capital
International agreements must be paired with
domestic economic policies to address the distri-
bution of value derived from AI-driven science.
In the traditional innovation economy, states
act as primary risk-takers, funding early-stage
foundational research, while private capital later
translates these insights into commercial applica-
tions and captures the financial rewards (Yencha,
2015). This model ofpublic risk, private reward
is well established, particularly in biomedical re-
search, where valuable therapeutics often trace
theiroriginstopublicgrants(GalkinaClearyetal.,
2018). The transition to autonomous AI science
risks deepening these asymmetries, given the
capital-intensive nature of the requisite compute
infrastructure and that many frontier models are
trained on scientific public commons - research
papers, public biobanks, scientific software, and
openlyavailableexperimentaldata. Withoutcare-
fully crafted policies, AI scientists may enclose
these publicly funded resources and convert them
into proprietary intellectual property.
Recognising the strategic role of compute, gov-
ernments are beginning to invest in sovereign
AI infrastructure and public compute reserves,
such as the US National Artificial Intelligence Re-
search Resource (Parashar et al., 2023) and the
European High Performance Computing Joint Un-
dertaking (Skordas, 2019). However, if such re-
serves merely subsidise the overhead of private
scientific operations without affecting IP owner-
ship structures, the public may not see sufficient
economic return. The economic mechanisms pro-
posed in earlier sections - including tokenised
hypothesis exchange and IP-NFTs - could encode
public-interest clauses. For discoveries achieved
viastate-fundedcomputeordata,smartcontracts
could automatically route a fraction of licensing
royaltiesbacktothesovereigncomputeinfrastruc-
ture, creating a sustainable funding loop while
mandating affordability for technologies of public
interest.
Scaling public compute reserves to support
large populations of autonomous AI scientists
has consequences for energy consumption and
grid capacity. Balancing the upside of auto-
mated discoveries against the carbon footprint
of compute clusters will become an important
policy consideration, and continued innovation
in hardware efficiency will be necessary to miti-
gatethesecosts(Kirkpatrick,2023;Luccionietal.,
2024a,b,c; Tamburrini, 2022; Wu et al., 2022).
29

Agentic Economies for Autonomous Scientific Discovery
7.3. The Human Scientist
Unlike previous waves of industrial automation
that primarily displaced routine physical labour,
the agentic scientific economy automates highly
specialised cognitive work (Autor, 2015; Webb,
2019). If human cognitive labour is no longer the
primary bottleneck to scientific progress, what
is the role of the human scientist? Automation
of routine scientific tasks does not render hu-
man cognition obsolete; instead, it drives hu-
man labour up the abstraction hierarchy (Ace-
moglu and Restrepo, 2019). Human scientists
may therefore gradually transition from execu-
tion to orchestration and oversight. Current AI
scientists, trained on historical data, remain bet-
ter suited for incremental and combinatorial op-
timisation than for revolutionary, deeply intuitive
leaps. Human experts are also necessary for mak-
ing complex trade-offs and establishing ethical
boundaries within their respective fields. The hu-
man scientist may therefore become theprincipal,
underwriting the actions of AI delegates, with
human-driven research collaboration remaining
the most credible deployment paradigm across
the research lifecycle (Kong et al., 2026). Yet for
this model to work, human scientists need access
to AI delegates, which requires computational re-
sources. Stark disparities currently exist between
researchers in different institutions. While the
cost of running AI agents may decrease over time
(increasing global accessibility of AI scientists),
public compute grants or subsidies may be neces-
sary to ensure that scientists across regions can
access AI tools.
This model, however, presupposes a continued
supply of expert human scientists, who develop
their skills and intuitions through first-hand ex-
perience with challenging problems. Top experts
are a minority of all trained researchers, and re-
searchtasteis hard to teach. If the AI-enhanced
scientific economy assumes widespread availabil-
ity of such talent to steer and oversee AI scientists,
a natural question arises: where will this deep
expertise come from in the future? Emerging em-
pirical evidence suggests that habitual reliance on
AI risks degrading human creativity (Ashkinaze
et al., 2025). Universities and their research pro-
grammes compound this concern, as they play a
dual role in society: they are centres of research
excellence, but they are also educational institu-
tionsthatproducebothprofessionalscientistsand
citizens with highly developed critical thinking
skills. Over-reliance on AI ideation may erode
both the depth of these skills and the intrinsic
motivation that draws early-career scientists to
research (Wu et al., 2025a). Should science au-
tomation disincentivise people from pursuing ad-
vanced degrees or substantially alter the nature
of such training, the consequences may extend
beyond the scientific workforce to broader social
structures.
Finally, there is a question of meaningful hu-
man participation in understanding. Science is
ultimately a human endeavour whose purpose
extends beyond producing goods or solving im-
mediate social needs - it is how we uncover truths
about the world and deepen our understanding.
While traditional AI systems required bespoke
solutions to extract AI-derived concepts (Schut
et al., 2023), LLMs reason in natural language,
enabling them to act as a semantic layer between
specialised simulators, bespoke ML tools, and
human collaborators. The challenge may there-
fore become one of volume rather than quality,
provided that the AI discoveries map onto mech-
anistic models (Posner et al., 2026) that lend
themselves to accurate and insightful explana-
tions. Should AI truly accelerate discovery, it may
become infeasible for any human scientist to care-
fully review and deeply engage with a sufficiently
large portion of the knowledge produced within
their own field. This is likely to be among the
most important challenges of advanced science
automation.
8. On the Limitations of AI-Driven Dis-
covery
To date, AI scientists have been limited in their
ability to deliver profound conceptual leaps, rais-
ing concerns (Zahavy, 2026). While AI scientists
excel at recombinant innovation (Fleming, 2001;
Weitzman, 1998), by efficiently reusing known
patterns and finding links between established
concepts, such innovation may be more incremen-
tal. Though undoubtedly valuable for advancing
30

Agentic Economies for Autonomous Scientific Discovery
what Kuhn formalised asnormal science(Kuhn
and Hacking, 1970), such reasoning is limited in
itsabilitytogeneratefoundationalbreakthroughs.
Human science has seen a decline in disruptive-
ness (Park et al., 2023), and AI scientists should
ideally help overcome this problem rather than
contribute to or exacerbate it. It is likely that
the capabilities of AI scientists will keep improv-
ing, with the increased availability of scientific
learning environments and further advances in
inference-time search. Work is also underway on
improving the long-horizon planning of AI scien-
tists (Zhao et al., 2026) and on their applicability
acrossmodalitiesanddisciplines(Lietal.,2026a).
However, it may be prudent to complement AI
scientist capability improvements with additional
structural and sociotechnical interventions.
As science automation increases, AI scientists
shouldcarefullybalancetheamountoftimespent
on incremental work, and open-ended creative
discovery-drivenbyintrinsicmotivation(Achiam
and Sastry, 2017; Aubret et al., 2019; Barto,
2012; Chentanez et al., 2004; Kulkarni et al.,
2016) and continuous re-examination of prevail-
ing theories and practices. Early examples of how
intrinsic motivation may be incorporated in AI
scientists can be seen in recent applications in for-
mal mathematical reasoning (Poesia et al., 2024).
The utilisation of LLMs in AI scientists intro-
duces the risk ofcognitive monoculture(Fazelpour
et al., 2026), as well ascitation monoculture(Ale-
mohammad et al., 2026). This is of particular
concern given that preliminary findings point
towards a reduction in idea diversity with the
use of generative AI in scientific workflows (Hao
et al., 2026; Meincke et al., 2025; Traberg et al.,
2026). Cognitive monoculture may also emerge
in human research communities, especially as
conservative grant funding tends to reward low-
risk proposals that do not challenge the status
quo (Schweiger et al., 2024). Yet, a degree of
pluralism tends to be highly beneficial, and some-
times strictly required, especially when research
intersects with ethics (Chandak et al., 2026). No
consensus exists on the extent of cognitive mono-
culture risks in science, though it is widely recog-
nised that it may lead to overlooking promis-
ing research directions. This risk is lower in
well-established sub-fields, presuming that the
assumptions and edge cases are properly recog-
nised (Hedden and Raghavan, 2026). In the his-
tory of science, many now famous papers have
initiallybeenrejectedbypeerreview,astheywere
challenging established research dogma. Retain-
ing the ability to effectively challenge dogma is
therefore critical.
More research is needed to understand if AI
scientists systematically prioritise certain types
of ideas, as a prerequisite for designing effective
interventions. Given that AI scientists are often
trained on domains where both a wide availabil-
ity of tools and a strong, efficiently computable
reward signal exists, this could lead to a form
of the McNamara fallacy (Bisht et al., 2026; Jan-
nach and Bauer, 2020) where easily quantifiable
directions are strongly prioritised irrespective of
their intrinsic value. Human oversight mitigates
these risks, though this hinges on active partic-
ipation and cognitive friction. As Messeri and
Crockett (Messeri and Crockett, 2024) highlight,
the uncritical reliance on highly capable AI tools
fosters anillusion of understanding. Individual
researchers may also lack the field-wide overview
neededtonoticetheabsenceoflesscommonview-
pointsintheoutput. Itmaythereforebeadvisable
to complement the individual human steering
with structural interventions for inducing strate-
gic heterogeneity (Ballestero et al., 2026). Di-
versity objectives embedded within the scientific
idea markets may be designed to reward and al-
locate resources towards non-consensus research
directions. The desire to maintain a diversity of
scientific ideas would need to be balanced against
the practicalities of identifying and discontinuing
non-promising directions, as well as the overall
cost and efficiency.
Finally, it is important to consider the risk
of introducing epistemic opacity (Creel, 2020;
Humphreys, 2004) through increased use of AI
scientists. Epistemicallyopaquemodelscansimul-
taneously be highly productive within thecontext
of discovery, while also introducing a severe lia-
bility in thecontext of justificationthrough their
opacity(Duede,2023). Theseconcernshavebeen
partially reflected in the discussions following
the AI-derived solution to the Millennium Prize
31

Agentic Economies for Autonomous Scientific Discovery
Navier-Stokes problem in mathematics, resulting
in a declaration signed by some of the world’s
leading mathematicians, namelyA Severe Mis-
alignment of AI in Mathematics(Avila et al., 2026)
- serving as a warning that mass automation of
proofs in mathematics may be at odds with the
core objective of the field, which is to advance
human understanding and build new conceptual
frameworks.
This risks creating a critical bottleneck in fu-
ture scientific workflows. Human institutions
are responsible for allocating physical resources,
setting constraints, and assuming legal liability
for scientific experiments. Human researchers
must therefore be able to act according to this re-
sponsibility, and comprehend and audit the ratio-
nale underpinning AI proposals and action plans.
Science is inherently a collaborative, social en-
deavour (Channing and Ghosh, 2026), where a
black-box oracle would alter the nature of sci-
entific understanding (Sullivan, 2022), even if
highly accurate. It would be preferable if AI sci-
entists could instead be utilised as interpretable
reasoning engines (Truhn et al., 2023), surfac-
ing the causal mechanisms behind their propos-
als (Kiciman et al., 2023). Interpretability helps
co-creation, by enabling researchers to audit AI
reasoning, set constraints, and align automated
discoveries with societal objectives.
9. Conclusion
The role of AI within scientific research is rapidly
evolving. Early AI systems were useful predomi-
nantly as highly specialised tools, whereas new
general-purpose systems and AI agents are en-
abling the development of AI scientists capable
of autonomously or semi-autonomously pursuing
different types of research tasks. This transition
raises the question of whether existing scientific
infrastructure is suited for a future in which AI
scientists can autonomously pursue scientific dis-
covery. While this is not yet the case, we should
be actively considering the necessary changes,
to prepare societies to reap the benefits of this
hypothesised acceleration.
We argue that the development of AI scientists
is likely to be bottlenecked primarily by physical
resources and empirical validation, rather than
the ability to produce plausible or promising re-
search ideas. It is the economic, legal, and physi-
cal friction that may stand in the way of realising
the downstream benefits. With that in mind, to
avoid future market failures, the scientific com-
munity must proactively develop a native Auto-
mated Scientific Economy. This economy would
make trade-offs between scientific pursuits ex-
plicit, include mechanisms to represent the public
interest, and would help avoid blind spots and
neglected topics. It would also make it possible
to financially decouple the computational labour
of ideation from the capital-intensive labour of
physical execution, and would enable agents and
institutions to negotiate priority access to lim-
ited physical resources depending on the esti-
mated value of different research proposals. Mar-
kets would also require solutions for appropriate
pricing and sharing of negative results, secure
computational approaches for handling sensitive
data within trusted execution environments, IP
frameworks, and information security risks. Deep
macroeconomic interventions may be required to
establish the appropriate public compute reserves
and subsidies, coupled with bespoke policies, reg-
ulations, and legal frameworks. As more tasks
are delegated to AI scientists, human experts may
shift towards orchestrating AI teams, interpret-
ing results, and maintaining safety and ethics
standards.
Disclaimer
The opinions presented in this paper represent
the personal views of the authors and do not nec-
essarily reflect the official policies or positions of
their organisations.
References
B. P. Abbott, R. Abbott, T. D. Abbott, M. R.
Abernathy, F. Acernese, K. Ackley, C. Adams,
T. Adams, P. Addesso, R. X. Adhikari, et al. Ob-
servation of gravitational waves from a binary
black hole merger.Physical Review Letters, 116
(6):061102, 2016.
R. Abbott.The reasonable robot: Artificial intelli-
32

Agentic Economies for Autonomous Scientific Discovery
gence and the law. Cambridge University Press,
2020.
B. Abi, R. Acciarri, M. A. Acero, G. Adamov,
D. Adams, M. Adinolfi, Z. Ahmad, J. Ahmed,
T. Alion, S. A. Monsalve, et al. Deep un-
derground neutrino experiment (dune), far
detector technical design report, volume ii:
Dune physics.arXiv preprint arXiv:2002.03005,
2020.
J. Abou-Chakra, L. Sun, K. Rana, B. May,
K. Schmeckpeper, N. Suenderhauf, M. V. Min-
niti, and L. Herlant. Real-is-sim: Bridging the
sim-to-real gap with a dynamic digital twin,
2025. URLhttps://arxiv.org/abs/2504.
03597.
D. Acemoglu and P. Restrepo. Automation and
new tasks: How technology displaces and re-
instates labor.Journal of economic perspectives,
33(2):3–30, 2019.
J. Achiam and S. Sastry. Surprise-based intrin-
sic motivation for deep reinforcement learning.
arXiv preprint arXiv:1703.01732, 2017.
L. Adam and G. H. McArthur IV. Substitution
attacks: a catalyst to reframe the dna manufac-
turing cyberbiosecurity landscape in the age of
benchtop synthesizers.Applied Biosafety, 29
(3):172–180, 2024.
A. Agrawal, J. Gans, and A. Goldfarb.Prediction
machines, updated and expanded: The simple
economics of artificial intelligence. Harvard Busi-
ness Press, 2022.
N.AhmedandM.Wahed. Thede-democratization
of ai: Deep learning and the compute divide in
artificial intelligence research.arXiv preprint
arXiv:2010.15581, 2020.
M. Akgün. Author or prompter? scientific writing,
identity, and the theseus paradox.Philosophy,
Ethics, and Humanities in Medicine, 20(1):29,
2025.
S. Alemohammad, D. Zhang, B. Tang, A. Qin,
G. Mai, A. Abbasi, R. Baraniuk, and Z. Wang.
When ai writes, who gets cited? evidence of
citation monoculture across language models,
2026. URLhttps://arxiv.org/abs/2608.
19230.
A. Aliper, R. Kudrin, D. Polykovskiy, P. Kamya,
E. Tutubalina, S. Chen, F. Ren, and A. Zha-
voronkov. Prediction of clinical trials outcomes
based on target choice and clinical trial design
with multi-modal artificial intelligence.Clinical
Pharmacology & Therapeutics, 114(5):972–980,
2023.
O. Alizadeh. Advances and challenges in climate
modeling.Climatic Change, 170(1):18, 2022.
L. Allen, J. Scott, A. Brand, M. Hlava, and M. Alt-
man. Publishing: Credit where credit is due.
Nature, 508(7496):312–313, 2014.
A. Altmejd, A. Dreber, E. Forsell, J. Huber, T. Imai,
M. Johannesson, M. Kirchler, G. Nave, and
C. Camerer. Predicting the replicability of so-
cial science lab experiments.PloS one, 14(12):
e0225826, 2019.
D. Amodei, C. Olah, J. Steinhardt, P. Christiano,
J. Schulman, and D. Mané. Concrete problems
in ai safety.arXiv preprint arXiv:1606.06565,
2016.
M. Anderljung, J. Barnhart, A. Korinek, J. Le-
ung, C. O’Keefe, J. Whittlestone, S. Avin,
M. Brundage, J. Bullock, D. Cass-Beggs, et al.
Frontier ai regulation: Managing emerg-
ing risks to public safety.arXiv preprint
arXiv:2307.03718, 2023.
P.Andreoli-VersbachandF.Mueller-Langer. Open
access to data: An ideal professed but not prac-
tised.Research Policy, 43(9):1621–1633, 2014.
Anthropic, 2026. URL https://
www.anthropic.com/research/
formalizing-fermats-last-theorem.
Anthropic Team. Claude discovers a novel
enzyme system with crispr-like repeats, 2026.
URL https://www.anthropic.com/news/
claude-discovers-novel-enzyme-system.
J. L. Araus, S. C. Kefauver, M. Zaman-Allah,
M. S. Olsen, and J. E. Cairns. Translating
high-throughputphenotypingintogeneticgain.
Trends in plant science, 23(5):451–466, 2018.
33

Agentic Economies for Autonomous Scientific Discovery
M. D. Ari, J. Iskander, J. Araujo, C. Casey, J. Kools,
B. Chen, R. Swain, M. Kelly, and T. Popovic. A
science impact framework to measure impact
beyond journal metrics.PLoS One, 15(12):
e0244407, 2020.
K. Arrow. Economic welfare and the allocation of
resources for invention.The Rate and Direction
of Inventive Activity/Princeton University, 1962.
P.Arzberger, P.Schroeder, A.Beaulieu, G.Bowker,
K. Casey, L. Laaksonen, D. Moorman, P. Uhlir,
and P. Wouters. Promoting access to public re-
search data for scientific, economic, and social
development.Data Science Journal, 3:135–152,
2004.
J. Ashkinaze, J. Mendelsohn, L. Qiwei, C. Budak,
and E. Gilbert. How ai ideas affect the creativ-
ity, diversity, and evolution of human ideas:
evidence from a large, dynamic experiment.
InProceedings of the ACM collective intelligence
conference, pages 198–213, 2025.
S. Askin, D. Burkhalter, G. Calado, and
S. El Dakrouni. Artificial intelligence applied
to clinical trials: opportunities and challenges.
Health and technology, 13(2):203–213, 2023.
A. Aspuru-Guzik, J. E. Hein, and J. Schrier. Com-
mit: Mini article for dynamic reporting of in-
cremental improvements to previous scholarly
work.Digital Discovery, 4(2):301–302, 2025.
A.Aubret,L.Matignon,andS.Hassas. Asurveyon
intrinsic motivation in reinforcement learning.
arXiv preprint arXiv:1908.06976, 2019.
D. H. Autor. Why are there still so many jobs? the
history and future of workplace automation.
Journal of economic perspectives, 29(3):3–30,
2015.
A. Avila, M. Bhargava, C. Birkar, P. Deligne,
Y. Deng, S. Donaldson, H. Duminil-Copin, A. Fi-
galli, M. Hairer, J. Huh, M. Kontsevich, E. Lin-
denstrauss, P.-L. Lions, J. Maynard, C. Mc-
Mullen, S. Mori, B. C. Ngô, A. Okounkov,
P. Scholze, S. Smirnov, T. Tao, M. Viazovska,
C. Villani, W. Werner, and E. Zelmanov. A
severe misalignment of ai in mathematics,
Sept. 2026. URLhttps://www.mathandai.
org/.
Ž. Avsec, N. Latysheva, J. Cheng, G. Novati, K. R.
Taylor, T. Ward, C. Bycroft, L. Nicolaisen, E. Ar-
vaniti, J. Pan, et al. Alphagenome: advanc-
ing regulatory variant effect prediction with a
unified dna sequence model.BioRxiv, pages
2025–06, 2025.
P. Ayris, J.-Y. Berthou, R. Bruce, S. Lind-
staedt, A. Monreale, B. Mons, Y. Murayama,
C. Södergård, K. Tochtermann, and R. Wilkin-
son. Realisingtheeuropeanopensciencecloud,
2016.
B. Azad, R. Azad, S. Eskandari, A. Bozorgpour,
A. Kazerouni, I. Rekik, and D. Merhof. Founda-
tional models in medical imaging: A compre-
hensive survey and future vision, 2023. URL
https://arxiv.org/abs/2310.18689.
P. Azoulay, J. S. Graff Zivin, and G. Manso. In-
centives and creativity: evidence from the aca-
demic life sciences.The RAND Journal of Eco-
nomics, 42(3):527–554, 2011.
R. Bahmani, F. Brasser, G. Dessouky, P. Jauernig,
M. Klimmek, A.-R. Sadeghi, and E. Stapf.
{CURE}: A security architecture with
{CUstomizable} and resilient enclaves. In30th
USENIX Security Symposium (USENIX Security
21), pages 1073–1090, 2021.
M. Baker. 1,500 scientists lift the lid on repro-
ducibility, 2016.
G. Ballestero, H. Hosseini, S. Khanna, and
R. I. Shorrer. Strategic algorithmic monocul-
ture: Experimental evidence from coordina-
tion games. Papers 2604.09502, arXiv.org, Apr
2026. URL https://ideas.repec.org/p/
arx/papers/2604.09502.html.
E. Bareinboim, J. D. Correa, D. Ibeling, and
T. Icard. On pearl’s hierarchy and the foun-
dations of causal inference. InProbabilistic and
causal inference: the works of Judea Pearl, pages
507–556. ACM, 2022.
A. G. Barto. Intrinsic motivation and reinforce-
ment learning. InIntrinsically motivated learn-
ing in natural and artificial systems, pages 17–
47. Springer, 2012.
34

Agentic Economies for Autonomous Scientific Discovery
G. Baskaran and M. Schwartz. The consequences
of china’s new rare earths export restrictions.
Center for Strategic and International Studies
(CSIS), 2025.
C.Baum, J.Berlips, W.Chen, H.Cozzarini, H.Cui,
I. Damgård, J. Dong, K. M. Esvelt, L. Foner,
M. Gao, et al. A system capable of verifiably
and privately screening global dna synthesis.
National Science Review, page nwag103, 2026.
R. B. Bausell.The problem with science: the repro-
ducibility crisis and what to do about it. Oxford
University Press, 2021.
O. Bayley, E. Savino, A. Slattery, and T. Noël. Au-
tonomous chemistry: Navigating self-driving
labs in chemical and material sciences.Matter,
7(7):2382–2398, 2024.
T. Benson-Tilsen and N. Soares. Formalizing con-
vergent instrumental goals. InAAAI Workshop:
AI, Ethics, and Society, pages 62–70, 2016.
C.-T. Berezin, S. Peccoud, D. M. Kar, and J. Pec-
coud. Cryptographic approaches to authen-
ticating synthetic dna sequences.Trends in
biotechnology, 42(8):1002–1016, 2024.
P.Berg,D.Baltimore,S.Brenner,R.O.Roblin,and
M. F. Singer. Summary statement of the asilo-
mar conference on recombinant dna molecules.
Proceedings of the National Academy of Sciences,
72(6):1981–1984, 1975.
M. Biagioli and A. Lippman.Gaming the met-
rics: Misconduct and manipulation in academic
research. Mit Press, 2020.
K. Bibbins-Domingo and A. Helman. Improving
representation in clinical trials and research.
Washington DC: National Academies of Sciences,
Engineering, and MedicinePolicy and Global Af-
fairs, 2022.
J. R. Biden. Executive order on the safe, secure,
and trustworthy development and use of artifi-
cial intelligence, 2023.
A. Birhane, A. Kasirzadeh, D. Leslie, and
S. Wachter. Science in the age of large lan-
guage models.Nature Reviews Physics, 5(5):
277–280, 2023.
J. Birk, A. Hallin, and G. Kasieczka. Omnijet-𝛼:
the first cross-task foundation model for par-
ticle physics.Machine Learning: Science and
Technology, 5(3):035031, 2024.
H. Bisht, V. Kumar, K. M. Jablonka, Mausam, and
N. M. A. Krishnan. Agentic ai scientists are
not built for autonomous scientific discovery,
2026. URLhttps://arxiv.org/abs/2605.
08956.
C.Bluethgen,P.Chambon,J.-B.Delbrouck,R.Van
Der Sluijs, M. Połacin, J. M. Zambrano Chaves,
T. M. Abraham, S. Purohit, C. P. Langlotz, and
A. S. Chaudhari. A vision–language foundation
model for the generation of realistic chest x-ray
images.Nature Biomedical Engineering, 9(4):
494–506, 2025.
C. Bodnar, W. P. Bruinsma, A. Lucic, M. Stanley,
A. Allen, J. Brandstetter, P. Garvan, M. Riechert,
J. A. Weyn, H. Dong, et al. A foundation model
for the earth system.Nature, 641(8065):1180–
1187, 2025.
B.Bodó,D.Gervais,andJ.P.Quintais. Blockchain
and smart contracts: the missing link in copy-
right licensing?International Journal of Law
and Information Technology, 26(4):311–336,
2018.
D. A. Boiko, R. MacKnight, and G. Gomes. Emer-
gent autonomous scientific research capabili-
ties of large language models.arXiv preprint
arXiv:2304.05332, 2023.
R. Bommasani, D. A. Hudson, E. Adeli, R. Altman,
S. Arora, S. von Arx, M. S. Bernstein, J. Bohg,
A. Bosselut, E. Brunskill, et al. On the oppor-
tunities and risks of foundation models.arXiv
preprint arXiv:2108.07258, 2021.
L. Bonomi, Y. Huang, and L. Ohno-Machado. Pri-
vacy challenges and research opportunities for
genomic data sharing.Nature Genetics, 52(7):
646–654, 2020.
N. Bostrom. Superintelligence: Paths, dangers,
strategies.Strategies, 2014.
N. Bostrom. The vulnerable world hypothesis.
Global Policy, 10(4):455–476, 2019.
35

Agentic Economies for Autonomous Scientific Discovery
J. Boyko, J. Cohen, N. Fox, M. H. Veiga, J. I. Li,
J. Liu, B. Modenesi, A. H. Rauch, K. N. Reid,
S.Tribedi, etal. Aninterdisciplinaryoutlookon
large language models for scientific research.
arXiv preprint arXiv:2311.04929, 2023.
A. Bracco, J. Brajard, H. A. Dijkstra, P. Hassan-
zadeh, C. Lessig, and C. Monteleoni. Machine
learning for the physics of climate.Nature Re-
views Physics, 7(1):6–20, 2025.
H. Brammer. Hypercerts: A new primitive
for public goods funding, 2022. URL
https://www.protocol.ai/blog/
hypercert-new-primitive/.
A. Brand, L. Allen, M. Altman, M. Hlava, and
J. Scott. Beyond authorship: Attribution, con-
tribution, collaboration, and credit.Learned
Publishing, 28(2), 2015.
I. Bremmer and M. Suleyman. The ai power
paradox: Can states learn to govern artificial
intelligence-before it’s too late?Foreign Aff.,
102:26, 2023.
E. M. Bucci. On zombie papers.Cell death &
disease, 10(3):189, 2019.
J.-C. Burgelman, C. Pascu, K. Szkuta,
R. Von Schomberg, A. Karalopoulos,
K. Repanas, and M. Schouppe. Open
science, open data, and open scholarship:
European policies to make science fit for the
twenty-first century.Frontiers in big data, 2:
43, 2019.
V. Buterin, Z. Hitzig, and E. G. Weyl. A flexible
design for funding public goods.Management
Science, 65(11):5171–5187, 2019.
G. Caldarelli. Understanding the blockchain ora-
cle problem: A call for action.Information, 11
(11):509, 2020.
M. L. Callaham, R. L. Wears, E. J. Weber, C. Bar-
ton, and G. Young. Positive-outcome bias and
other limitations in the outcome of research ab-
stracts submitted to a scientific meeting.Jama,
280(3):254–257, 1998.
E. Callaway. Ai can design viruses, toxins and
other bioweapons. how worried should we be?
Nature, 653(8114):344–347, 2026.
Y. Cao, S. Lai, J. Huang, Y. Zhang, Z. Lawrence,
R. Bhakta, I. F. Thomas, M. Cao, C.-H.
Tsai, Z. Zhou, et al. Simulcost: A cost-
aware benchmark and toolkit for automating
physics simulations with llms.arXiv preprint
arXiv:2603.20253, 2026.
J. O. Caro, A. H. d. O. Fonseca, C. Averill,
S. A. Rizvi, M. Rosati, J. L. Cross, P. Mittal,
E. Zappala, D. Levine, R. M. Dhodapkar, et al.
Brainlm: A foundation model for brain activity
recordings.BioRxiv, pages 2023–09, 2023.
S. Carter, N. Wheeler, S. Chwalek, C. Isaac, and
J. Yassif. The convergence of artificial intelli-
gence and the life sciences: Safeguarding tech-
nology, rethinking governance, and preventing
catastrophe, 2023.
A.Chan, K.Wei, S.Huang, N.Rajkumar, E.Perrier,
S. Lazar, G. K. Hadfield, and M. Anderljung.
Infrastructure for ai agents.arXiv preprint
arXiv:2501.10114, 2025.
P. Chandak, V. Alkin, D. Wu, M. Dagan, T. D.
Roy, M. C. S. Menezes, A. Noori, N. Somia, J. S.
Brownstein, R. Balicer, et al. What does the ai
doctor value? auditing pluralism in the clini-
cal ethics of language models.arXiv preprint
arXiv:2605.18738, 2026.
G.ChanningandA.Ghosh. Aiforscientificdiscov-
ery is a social problem.Patterns, 7(3), 2026.
K. Chauhan. Dead science walking: Publication
bias and the ai scientist pipeline, 2026. URL
https://arxiv.org/abs/2606.04220.
J. Chen, Y. Hu, M. Cai, Y. Lu, Y. Wang, X. Cao,
M. Lin, H. Xu, J. Wu, X. Cao, et al. Trialbench:
Multi-modal ai-ready datasets for clinical trial
prediction.Scientific Data, 12(1):1564, 2025.
Y. Cheng, W. Zhang, Z. Zhang, C. Zhang, S. Wang,
and S. Mao. Toward federated large language
models: Motivations, methods, and future di-
rections.IEEE Communications Surveys & Tuto-
rials, 27(4):2733–2764, 2024.
N. Chentanez, A. Barto, and S. Singh. Intrinsically
motivated reinforcement learning.Advances
in neural information processing systems, 17,
2004.
36

Agentic Economies for Autonomous Scientific Discovery
Y. Chervonyi, T. H. Trinh, M. Olšák, X. Yang, H. H.
Nguyen, M. Menegali, J. Jung, J. Kim, V. Verma,
Q. V. Le, et al. Gold-medalist performance in
solving olympiad geometry with alphageome-
try2.Journal of Machine Learning Research, 26
(241):1–39, 2025.
Y. Chi, W. Li, D. Hong, X. Wang, M. Gao, K. Yang,
B. He, Y. Zheng, C. Xiao, and Q. Na. Ai4ai-
bench: Benchmarking llm agents in algorith-
mic design for recursive self-improvement,
2026. URLhttps://arxiv.org/abs/2608.
20318.
M. A. Chia, F. Antaki, Y. Zhou, A. W. Turner, A. Y.
Lee, and P. A. Keane. Foundation models in
ophthalmology.British Journal of Ophthalmol-
ogy, 108(10):1341–1348, 2024.
L. T. Clark, L. Watkins, I. L. Piña, M. Elmer, O. Ak-
inboboye, M. Gorham, B. Jamerson, C. McCul-
lough, C. Pierre, A. B. Polis, et al. Increasing
diversity in clinical trials: overcoming critical
barriers.Current problems in cardiology, 44(5):
148–172, 2019.
H. Collins.Tacitandexplicitknowledge. University
of Chicago press, 2019.
L. Conteh, T. Engels, and D. H. Molyneux. Socioe-
conomic aspects of neglected tropical diseases.
The Lancet, 375(9710):239–247, 2010.
COPE Council. Cope position - authorship and ai,
2024. URL https://doi.org/10.24318/
cCVRZBms. https://publicationethics.
org. License: CC BY-NC-ND 4.0.
M. Corpas, M. Pius, M. Poburennaya, H. Guio,
M. Dwek, S. Nagaraj, C. Lopez-Correa, A. Pope-
joy, and S. Fatumo. Bridging genomics’ greatest
challenge: The diversity gap.Cell genomics, 5
(1), 2025.
P. C. Cramton, Y. Shoham, R. Steinberg, and V. L.
Smith.Combinatorial auctions, volume 5. MIT
press Cambridge, 2006.
K. A. Creel. Transparency in complex computa-
tional systems.Philosophy of Science, 87(4):
568–589, 2020.
W. Cui, W. Jeong, P. Thölke, T. Medani, K. Jerbi,
A. A. Joshi, and R. M. Leahy. Neuro-gpt: To-
wards a foundation model for eeg. In2024
IEEE International Symposium on Biomedical
Imaging (ISBI), pages 1–5. IEEE, 2024.
M. L. Cummings. Automation bias in intelligent
time critical decision support systems. InDeci-
sion making in aviation, pages 289–294. Rout-
ledge, 2017.
J. Cunningham, N. Davies, S. Devaney, M. Hard-
ing, S. Holm, V. Neumann, C. Smith, and
J. Ainsworth. A review of medical data sharing
initiatives with a focus on the use of blockchain
technologies: Qualitative comparative analy-
sis.Journal of Medical Internet Research, 28:
e63575, 2026.
A. Cuntz, C. Fink, and H. Stamm. Artificial intel-
ligence and intellectual property: An economic
perspective, 2024.
T. Dai, S. Vijayakrishnan, F. T. Szczypiński, J.-
F. Ayme, E. Simaei, T. Fellowes, R. Clowes,
L. Kotopanov, C. E. Shields, Z. Zhou, et al. Au-
tonomous mobile robots for exploratory syn-
thetic chemistry.Nature, 635(8040):890–897,
2024.
H. Dalla-Torre, L. Gonzalez, J. Mendoza-Revilla,
N. Lopez Carranza, A. H. Grzywaczewski,
F. Oteri, C. Dallago, E. Trop, B. P. De Almeida,
H. Sirelkhatim, et al. Nucleotide transformer:
buildingandevaluatingrobustfoundationmod-
els for human genomics.Nature Methods, 22
(2):287–297, 2025.
C. R. Davies. An evolutionary step in intellec-
tual property rights–artificial intelligence and
intellectual property.Computer Law & Security
Review, 27(6):601–619, 2011.
M. De Boer and K. Lammertsma. Scarcity of rare
earth elements.ChemSusChem, 6(11):2045–
2055, 2013.
K. De Smedt, D. Koureas, and P. Wittenburg. Fair
digital objects for science: From data pieces to
actionable knowledge units.Publications, 8(2):
21, 2020.
37

Agentic Economies for Autonomous Scientific Discovery
J. A. DiMasi, H. G. Grabowski, and R. W. Hansen.
Innovationinthepharmaceuticalindustry: new
estimates of R&D costs.Journal of health eco-
nomics, 47:20–33, 2016.
T. Ding, A. Nannapaneni, B. Liu, and L. Zhang.
Autonomous research agents: A survey of ai
scientists and the verification gap, 2026. URL
https://arxiv.org/abs/2608.05179.
W. Ding, J. Hou, J. Li, C. Guo, J. Qin, R. Kozma,
and F.-Y. Wang. Desci based on web3 and
dao: A comprehensive overview and reference
model.IEEE Transactions on Computational
Social Systems, 9(5):1563–1573, 2022.
U. Dirnagl and M. Lauritzen. Fighting publication
bias: introducing the negative results section,
2010.
B. Doleman, J. P. Williams, and J. Lund. Why
most published meta-analysis findings are false.
Techniques in Coloproctology, 23(9):925–928,
2019.
Z. Dong, R. Li, Y. Wu, T. T. Nguyen, J. S. Chong,
F. Ji, N. R. Tong, C. L. Chen, and J. H. Zhou.
Brain-jepa: Brain dynamics foundation model
with gradient positioning and spatiotemporal
masking.Advances in Neural Information Pro-
cessing Systems, 37:86048–86073, 2024.
T. W. Dornis. Artificial intelligence and innova-
tion: the end of patent law as we know it.Yale
JL & Tech., 23:97, 2020.
W. W. Dou, I. Goldstein, and Y. Ji. Ai-powered
trading, algorithmic collusion, and price effi-
ciency. Technical report, National Bureau of
Economic Research, 2025.
J. R. Douceur. The sybil attack. InInternational
workshop on peer-to-peer systems, pages 251–
260. Springer, 2002.
A. Dreber, T. Pfeiffer, J. Almenberg, S. Isaksson,
B. Wilson, Y. Chen, B. A. Nosek, and M. Johan-
nesson. Using prediction markets to estimate
the reproducibility of scientific research.Pro-
ceedings of the National Academy of Sciences,
112(50):15343–15347, 2015.
Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and
I. Mordatch. Improving factuality and reason-
ing in language models through multiagent de-
bate. InForty-first international conference on
machine learning, 2024.
E. Duede. Deep learning opacity in scientific dis-
covery.PhilosophyofScience, 90(5):1089–1099,
Feb. 2023. ISSN 1539-767X. doi: 10.1017/
psa.2023.8. URL http://dx.doi.org/10.
1017/psa.2023.8.
L. Duo, Y. Hao, and J. He. Autonomous materi-
als synthesis laboratories: Integrating artificial
intelligence with advanced robotics for acceler-
ated discovery, 2025.
W. P. Duprex, R. A. Fouchier, M. J. Imperiale,
M.Lipsitch, andD.A.Relman. Gain-of-function
experiments: time for a real debate.Nature
Reviews Microbiology, 13(1):58–64, 2015.
T. Duston, S. Xin, Y. Sun, D. Zan, A. Li, S. Xin,
K. Shen, Y. Chen, Q. Sun, G. Zhang, J. Liu,
H. Zhou, J. Liu, Z. Pu, Y. Wang, B.-X. Ge,
X. Tong, F. Ye, Z.-C. Zhao, W.-B. Han, Z. Cao,
Y. Zhao, W. Ren, Q. Long, Y. Liu, A. Huang,
Y. Du, Y. Rong, and J. Peng. Ainstein-
bench: Benchmarking coding agents on scien-
tific repositories, 2025. URLhttps://arxiv.
org/abs/2512.21373.
C.Dwork. Differentialprivacy: Asurveyofresults.
InInternational conference on theory and appli-
cations of models of computation, pages 1–19.
Springer, 2008.
R. Edison, S. Toner, and K. M. Esvelt. Assembling
unregulated dna segments bypasses synthesis
screening: regulate fragments as select agents.
Nature Communications, 2026.
R. S. Eisenberg. Obvious to whom? evaluating in-
ventions from the perspective of phosita.Berke-
ley Technology Law Journal, 19(3):885–906,
2004.
E. J. Emanuel, D. Wendler, and C. Grady. What
makes clinical research ethical? InResearch
Ethics, pages 229–239. Routledge, 2017.
38

Agentic Economies for Autonomous Scientific Discovery
N. Emery-Xu, R. Jordan, and R. Trager. Inter-
national governance of advancing artificial in-
telligence.AI & SOCIETY, 40(4):3019–3044,
2025.
J. M. Esanu, P. F. Uhlir, N. R. Council, et al. The
economic logic of “open science” and the bal-
ance between private property rights and the
public domain in scientific data and informa-
tion: a primer. InThe role of scientific and
technical data and information in the public do-
main: Proceedings of a symposium. National
Academies Press (US), 2003.
J. A. Evans and J. Reimer. Open access and global
participation in science.Science, 323(5917):
1025–1025, 2009.
L. Evans and P. Bryant. Lhc machine.Journal of
instrumentation, 3(08):S08001–S08001, 2008.
R. Evans, M. O’neill, A. Pritzel, N. Antropova,
A. Senior, T. Green, A. Žídek, R. Bates, S. Black-
well, J. Yim, et al. Protein complex prediction
with alphafold-multimer.biorxiv, pages 2021–
10, 2021.
D.Fanelli. Issciencereallyfacingareproducibility
crisis, and do we need it to?Proceedings of the
National Academy of Sciences, 115(11):2628–
2631, 2018.
J.-L. Fattebert and F. Gygi. Density functional the-
ory for efficient ab initio molecular dynamics
simulations in solution.Journal of computa-
tional chemistry, 23(6):662–666, 2002.
A. Fawzi, M. Balog, A. Huang, T. Hubert,
B. Romera-Paredes, M. Barekatain, A. Novikov,
F. J. R. Ruiz, J. Schrittwieser, G. Swirszcz, et al.
Discovering faster matrix multiplication algo-
rithms with reinforcement learning.Nature,
610(7930):47–53, 2022.
S. Fazelpour, J. O’Brien, and H. Rubin. Navigating
epistemic monocultures in ai-driven science: A
simulation study, 2026. URLhttps://arxiv.
org/abs/2608.19390.
N. Feasey, M. Wansbrough-Jones, D. C. Mabey,
andA.W.Solomon. Neglectedtropicaldiseases.
British medical bulletin, 93(1):179–200, 2010.
T. Feng, T. Trinh, G. Bingham, J. Kang, S. Zhang,
S. hyun Kim, K. Barreto, C. Schildkraut, J. Jung,
J. Seo, C. Pagano, Y. Chervonyi, D. Hwang,
K. Hou, S. Gukov, C.-C. Tsai, H. Choi, Y. Jin,
W.-Y. Li, H.-A. Wu, R.-A. Shiu, Y.-S. Shih, Q. V.
Le, and T. Luong. Semi-Autonomous Mathe-
matics Discovery with Gemini: A Case Study
on the Erdős Problems, 2026a. URLhttps:
//arxiv.org/abs/2601.22401.
T. Feng, T. H. Trinh, G. Bingham, D. Hwang,
Y. Chervonyi, J. Jung, J. Lee, C. Pagano, S.-
h. Kim, F. Pasqualotto, et al. Towards au-
tonomous mathematics research.arXiv preprint
arXiv:2602.10177, 2026b.
W. Feng, P. Gao, and X. Wang. Ai breeder: Ge-
nomicpredictionsforcropbreeding.NewCrops,
1:100010, 2024.
W. L. Filho, R. Kotter, P. G. Özuyar, I. R. Abubakar,
J. H. P. P. Eustachio, and N. R. Matandirotya.
Understanding rare earth elements as criti-
cal raw materials.Sustainability, 15(3):1919,
2023.
D. Filippi et al. Smart contracts.Internet Policy
Review, 10(2), 2021.
M. Fire and C. Guestrin. Over-optimization of
academic publishing metrics: observing good-
hart’s law in action.GigaScience, 8(6):giz053,
2019.
S. Fish, Y. A. Gonczarowski, and R. I. Shorrer.
Algorithmiccollusionbylargelanguagemodels.
arXiv preprint arXiv:2404.00806, 7(2):5, 2024.
L. Fleming. Recombinant uncertainty in tech-
nological search.Management science, 47(1):
117–132, 2001.
M. Florio, S. Forte, and E. Sirtori. Forecasting
the socio-economic impact of the large hadron
collider: A cost–benefit analysis to 2025 and
beyond.Technological Forecasting and Social
Change, 112:38–53, 2016.
T. S. Foster, B. A. Omari, T. Fu, T. Mann,
C. Domond, L. Cipolina-Kun, B. Gauri,
M. Aghamelu, A. D. Goldie, E. Helenowski,
J.-C. Gagnon-Audet, A. Pepe, S. Nazir, D. Iz-
covich, N. Levi, R. Hazra, K. Hambardzumyan,
39

Agentic Economies for Autonomous Scientific Discovery
N. Baldwin, X. Li, M. Josifoski, P. Giampouras,
M. J. Sabet, A. Sims, H. Momand, T. Shavrina,
D. Magka, J. Weston, Y. Wang, A. Goyal, J. Hen-
riques, Y. Bachrach, E. McMilin, and J. N. Foer-
ster. Ai research preference models, 2026. URL
https://arxiv.org/abs/2608.13940.
R. A. Fouchier, A. García-Sastre, Y. Kawaoka, W. S.
Barclay, N. M. Bouvier, I. H. Brown, I. Capua,
H. Chen, R. W. Compans, R. B. Couch, et al.
Transmission studies resume for avian flu.Sci-
ence, 339(6119):520–521, 2013.
B. Freedman. Equipoise and the ethics of clin-
ical research. Inhuman experimentation and
research, pages 427–431. Routledge, 2017.
Y. Fukataki, W. Hayashi, N. Nishimoto, and Y. M.
Ito. Developing artificial intelligence tools for
institutional review board pre-review: A pilot
study on chatgpt’s accuracy and reproducibility.
PLOS Digital Health, 4(6):e0000695, 2025.
K. Fushimi, Y. Nakai, A. Nishi, R. Suzuki,
M. Ikegami, R. Nimura, T. Tomono, R. Hidese,
H. Yasueda, Y. Tagawa, et al. Development of
the autonomous lab system to support biotech-
nology research.Scientific Reports, 15(1):6648,
2025.
E. Galkina Cleary, J. M. Beierlein, N. S. Khanuja,
L. M. McNamee, and F. D. Ledley. Contribution
of nih funding to new drug approvals 2010–
2016.Proceedings of the National Academy of
Sciences, 115(10):2329–2334, 2018.
J.Gao, J.Chang, H.Que, Y.Xiong, S.Zhang, X.Qi,
Z. Liu, J.-J. Wang, Q. Ding, X. Li, et al. Unilabos:
An ai-native operating system for autonomous
laboratories.arXiv preprint arXiv:2512.21766,
2025.
B. Garfinkel and A. Dafoe. How does the offense-
defense balance scale? InEmerging Technolo-
gies and International Stability, pages 247–274.
Routledge, 2021.
F. Garrido-Lucero, B. Heymann, M. Vono,
P. Loiseau, and V. Perchet. Du-shapley: A shap-
ley value proxy for efficient dataset valuation.
Advances in Neural Information Processing Sys-
tems, 37:1973–2000, 2024.
E. Geisler.The metrics of science and technology.
Bloomsbury Publishing USA, 2000.
A. Gelman and E. Loken. The garden of fork-
ing paths: Why multiple comparisons can be a
problem, even when there is no “fishing expe-
dition” or “p-hacking” and the research hypoth-
esis was posited ahead of time.Department
of Statistics, Columbia University, 348(1-17):3,
2013.
A. Ghorbani and J. Zou. Data shapley: Equitable
valuation of data for machine learning. InInter-
national conference on machine learning, pages
2242–2251. PMLR, 2019.
S. Gjerstad and J. Dickhaut. Price formation in
double auctions.Games and economic behavior,
22(1):1–29, 1998.
P.D.Gluckman, V.C.Turekian, R.W.Grimes, and
T. Kishi. Science diplomacy: a pragmatic per-
spective from the inside.Science & Diplomacy,
6(4):1–13, 2017.
M. Goldblum, D. Tsipras, C. Xie, X. Chen,
A. Schwarzschild, D. Song, A. Madry, B. Li,
and T. Goldstein. Dataset security for machine
learning: Data poisoning, backdoor attacks,
and defenses, 2021. URL https://arxiv.
org/abs/2012.10544.
S. Goldwasser, S. Micali, and C. Rackoff. The
knowledge complexity of interactive proof sys-
tems.SIAM Journal on Computing, 18(1):186–
208, 1989. doi: 10.1137/0218012. URL
https://doi.org/10.1137/0218012.
L. Gomes, J. Kueck, M. Mattes, M. Spindler, and
A. Zaytsev. Collusion detection with graph neu-
ral networks.arXiv preprint arXiv:2410.07091,
2024.
G. Gong, J. Liu, S. Pandya, C. Taborda, N. Wiesen-
danger, N. Price, W. Byron, A. Coppi, P. Young,
C. Wiess, et al. Clinical trial patient matching:
A real-time, common data model and artificial
intelligence–driven system for semiautomated
patient prescreening in cancer clinical trials.
JCO Clinical Cancer Informatics, 10:e2500262,
2026.
40

Agentic Economies for Autonomous Scientific Discovery
I. J. Goodfellow, J. Shlens, and C. Szegedy. Ex-
plaining and harnessing adversarial examples.
arXiv preprint arXiv:1412.6572, 2014.
J. Gottweis, W.-H. Weng, A. Daryin, T. Tu,
A. Palepu, P. Sirkovic, A. Myaskovsky, F. Weis-
senberger, K. Rong, R. Tanno, K. Saab,
D. Popovici, J. Blum, F. Zhang, K. Chou, A. Has-
sidim,B.Gokturk,A.Vahdat,P.Kohli,Y.Matias,
A. Carroll, K. Kulkarni, N. Tomasev, Y. Guan,
V. Dhillon, E. D. Vaishnav, B. Lee, T. R. D. Costa,
J. R. Penadés, G. Peltz, Y. Xu, A. Pawlosky,
A. Karthikesalingam, and V. Natarajan. To-
wards an ai co-scientist, 2025. URL https:
//arxiv.org/abs/2502.18864.
H.G.GrabowskiandM.Kyle. Genericcompetition
and market exclusivity periods in pharmaceu-
ticals.Managerial and Decision Economics, 28
(4-5):491–502, 2007.
P. Groth, A. Gibson, and J. Velterop. The anatomy
of a nanopublication.Information services and
use, 30(1-2):51–56, 2010.
K.Guo, Z.Yang, C.-H.Yu, andM.J.Buehler. Artifi-
cialintelligenceandmachinelearningindesign
of mechanical materials.Materials Horizons, 8
(4):1153–1172, 2021.
L. L. Guo, E. Steinberg, S. L. Fleming, J. Posada,
J. Lemmon, S. R. Pfohl, N. Shah, J. Fries, and
L.Sung. Ehrfoundationmodelsimproverobust-
ness in the presence of temporal distribution
shift.Scientific Reports, 13(1):3767, 2023.
L. L. Guo, J. Fries, E. Steinberg, S. L. Fleming,
K. Morse, C. Aftandilian, J. Posada, N. Shah,
and L. Sung. A multi-center study on the adapt-
ability of a shared foundation model for elec-
tronic health records.NPJ digital medicine, 7
(1):171, 2024.
J. O. Gyapong, M. Gohoho, A. K. Manyeh, M. Im-
murana, and M. Gyapong. Current state and
future directions of interventions for neglected
tropical diseases.Nature Human Behaviour, 9
(8):1557–1570, 2025.
B. Gyevnár, A. Kasirzadeh, and N. B. Shah. Dis-
tributed denial of science: How indirect data
poisoning of ai systems can industrialize scien-
tific fraud.arXiv preprint arXiv:2607.10712,
2026.
T. Ha, D. Lee, Y. Kwon, M. S. Park, S. Lee, J. Jang,
B.Choi,H.Jeon,J.Kim,H.Choi,etal. Ai-driven
robotic chemist for autonomous synthesis of
organic molecules.Science advances, 9(44):
eadj0461, 2023.
L. Hammond, A. Chan, J. Clifton, J. Hoelscher-
Obermaier, A. Khan, E. McLean, C. Smith,
W. Barfuss, J. Foerster, T. Gavenčiak, et al.
Multi-agent risks from advanced ai.arXiv
preprint arXiv:2502.14143, 2025.
R. Hanson. Could gambling save science? en-
couraging an honest consensus.A Journal of
Knowledge, Culture and Policy, 1995.
M.Hao, J.Gong, X.Zeng, C.Liu, Y.Guo, X.Cheng,
T. Wang, J. Ma, X. Zhang, and L. Song. Large-
scale foundation model on single-cell transcrip-
tomics.Nature Methods, 21(8):1481–1491,
2024.
Q. Hao, F. Xu, Y. Li, and J. Evans. Artificial in-
telligence tools expand scientists’ impact but
contract science’s focus.Nature, 649(8099):
1237–1243, 2026.
J. R. Harper. The future of scientific publish-
ing: Automated article generation, 2024. URL
https://arxiv.org/abs/2404.17586.
S. Harrer, P. Shah, B. Antony, and J. Hu. Artifi-
cial intelligence for clinical trial design.Trends
in pharmacological sciences, 40(8):577–591,
2019.
J. He, S. Houde, and J. D. Weisz. Which contribu-
tions deserve credit? perceptions of attribution
in human-ai co-creation. InProceedings of the
2025 CHI conference on human factors in com-
puting systems, pages 1–18, 2025a.
X. D. He, C. Yang, and Y. Zhou. Optimal design
of automated market makers on decentralized
exchanges.arXiv preprint arXiv:2404.13291,
2024.
Y. He, P. Fang, Y. Shan, Y. Pan, Y. Wei, Y. Chen,
Y. Chen, Y. Liu, Z. Zeng, Z. Zhou, et al. General-
ized biological foundation model with unified
41

Agentic Economies for Autonomous Scientific Discovery
nucleic acid and protein language.Nature Ma-
chine Intelligence, 7(6):942–953, 2025b.
A. Head, K. Lo, D. Kang, R. Fok, S. Skjonsberg,
D.S.Weld,andM.A.Hearst. Augmentingscien-
tific papers with just-in-time, position-sensitive
definitionsoftermsandsymbols. InProceedings
of the 2021 CHI Conference on Human Factors
in Computing Systems, pages 1–18, 2021.
B. Hedden and M. Raghavan. Algorithmic mono-
culture and its critics, 2026. URL https:
//arxiv.org/abs/2604.06047.
S. W. Hee, A. Willis, C. Tudur Smith, S. Day,
F. Miller, J. Madan, M. Posch, S. Zohar, and
N. Stallard. Does the low prevalence affect the
sample size of interventional clinical trials of
rare diseases? an analysis of data from the ag-
gregate analysis of clinicaltrials. gov.Orphanet
journal of rare diseases, 12(1):44, 2017.
R. Heesen and L. K. Bright. Publication bias is bad
for science if not necessarily scientists.Royal
Society Open Science, 12(4), 2025.
G. C. Hegerl and S. Solomon. Risks of climate en-
gineering.Science, 325(5943):955–956, 2009.
E. C. Hettinger. Justifying intellectual property.
Philosophy & Public Affairs, pages 31–52, 1989.
S. G. Higgins, A. A. Nogiwa-Valdez, and M. M.
Stevens. Considerations for implementing elec-
tronic laboratory notebooks in an academic
research environment.Nature Protocols, 17(2):
179–189, 2022.
K.E.Himma. Thejustificationofintellectualprop-
erty: Contemporary philosophical disputes.
Journal of the American Society for Informa-
tion Science and Technology, 59(7):1143–1161,
2008.
S. A. Hollingsworth and R. O. Dror. Molecular
dynamics simulation for all.Neuron, 99(6):
1129–1143, 2018.
M. C. Horowitz. Artificial intelligence, interna-
tional competition, and the balance of power.
Texas national security review, 1(3):37–57,
2018.
M. K. Horton, P. Huck, R. X. Yang, J. M. Munro,
S. Dwaraknath, A. M. Ganose, R. S. Kingsbury,
M. Wen, J. X. Shen, T. S. Mathis, et al. Accel-
erated data-driven materials science with the
materials project.Nature Materials, 24(10):
1522–1532, 2025.
M. Hosseini, D. B. Resnik, and K. Holmes. The
ethics of disclosing the use of artificial intelli-
gence tools in writing scholarly manuscripts.
Research Ethics, 19(4):449–465, 2023.
A. R. Hosseinpoor, N. Bergen, and
A. Schlotheuber. Promoting health eq-
uity: WHO health inequality monitoring at
global and national levels.Global health action,
8(1):29034, 2015.
P.Huang, X.Zhang, Z.Cao, S.Liu, M.Xu, W.Ding,
J. Francis, B. Chen, and D. Zhao. What went
wrong? closing the sim-to-real gap via differ-
entiable causal discovery, 2023. URLhttps:
//arxiv.org/abs/2306.15864.
T. Hubert, R. Mehta, L. Sartran, M. Z. Horváth,
G. Žužić, E. Wieser, A. Huang, J. Schrittwieser,
Y. Schroecker, H. Masoom, et al. Olympiad-
level formal mathematical reasoning with rein-
forcement learning.Nature, pages 1–3, 2025.
M. Hulme.Can science fix climate change?: A case
against climate engineering. John Wiley & Sons,
2014.
P. Humphreys.Extending ourselves: Computa-
tional science, empiricism, and scientific method.
Oxford University Press, 2004.
Innovation, Science and Economic De-
velopment Canada. AI Compute Ac-
cess Fund, 2026a. URL https://
ised-isde.canada.ca/site/ised/en/
canadian-sovereign-ai-compute-strategy/
ai-compute-access-fund. Accessed: 19
May 2026.
Innovation, Science and Economic Devel-
opment Canada. Canadian Sovereign AI
Compute Strategy, 2026b. URL https://
ised-isde.canada.ca/site/ised/en/
canadian-sovereign-ai-compute-strategy.
Accessed: 19 May 2026.
42

Agentic Economies for Autonomous Scientific Discovery
International Energy Agency. Global
critical minerals outlook 2025. Tech-
nical report, IEA, Paris, 2025. URL
https://www.iea.org/reports/
global-critical-minerals-outlook-2025.
Licence: CC BY 4.0.
J. P. Ioannidis. Why most published research
findings are false.PLoS medicine, 2(8):e124,
2005.
J. P. Ioannidis. Why most published research
findings are false.Chance, 32(1):4–13, 2019.
A. Jain, S. P. Ong, G. Hautier, W. Chen, W. D.
Richards, S. Dacek, S. Cholia, D. Gunter,
D. Skinner, G. Ceder, et al. Commentary:
The materials project: A materials genome ap-
proach to accelerating materials innovation.
APL materials, 1(1), 2013.
D. Jannach and C. Bauer. Escaping the mcnamara
fallacy: Towards more impactful recommender
systems research.Ai Magazine, 41(4):79–95,
2020.
B. Jansky, T. Hendl, and A. Z. Nocanda. Patient-
led innovation and global health justice: open-
source digital health technology for type 1 dia-
betes care.Bioethics, 38(6):511–528, 2024.
J. A. Jeevarajan, T. Joshi, M. Parhizi, T. Rauhala,
and D. Juarez-Robles. Battery hazards for large
energy storage systems, 2022.
R. Jia, D. Dao, B. Wang, F. A. Hubis, N. Hynes,
N. M. Gürel, B. Li, C. Zhang, D. Song, and C. J.
Spanos. Towards efficient data valuation based
on the shapley value. InThe 22nd international
conference on artificial intelligence and statistics,
pages 1167–1176. PMLR, 2019.
Y. Jiang, W. Lou, L. Wang, Z. Tang, S. Feng, J. Lu,
H. Sun, Y. Pan, S. Gu, H. Su, F. Liu, W. Wei,
P. Tan, D. Zhou, F. Ling, C. Tan, B. Zhang,
X. Wang, L. Bai, and B. Zhou. Scp: Accel-
erating discovery with a global web of au-
tonomous scientific agents, 2025. URLhttps:
//arxiv.org/abs/2512.24189.
W. G. Johnson and D. M. Bowman. A survey of
instruments and institutions available for the
globalgovernanceofartificialintelligence.IEEE
Technology and Society Magazine, 40(4):68–76,
2021.
J. Jumper, R. Evans, A. Pritzel, T. Green, M. Fig-
urnov, O. Ronneberger, K. Tunyasuvunakool,
R. Bates, A. Žídek, A. Potapenko, et al. Highly
accurate protein structure prediction with al-
phafold.nature, 596(7873):583–589, 2021.
A. Kale, M. Kay, and J. Hullman. Decision-making
under uncertainty in research synthesis: De-
signing for the garden of forking paths. In
Proceedings of the 2019 CHI conference on hu-
man factors in computing systems, pages 1–14,
2019.
B. Kang, J. Gu, J. Lv, W. Li, L. Wang, and Y. Gao.
Harness continual learning: Continual adap-
tation beyond model parameters, 2026. URL
https://arxiv.org/abs/2608.19013.
S. Kapoor and A. Narayanan. Leakage and the re-
producibility crisis in machine-learning-based
science.Patterns, 4(9), 2023.
S. Kapoor, R. Bommasani, K. Klyman, S. Long-
pre, A. Ramaswami, P. Cihon, A. Hopkins,
K. Bankston, S. Biderman, M. Bogen, et al. On
the societal impact of open foundation models.
arXiv preprint arXiv:2403.07918, 2024.
A. Kasirzadeh and I. Gabriel. Agentic profiles for
effective ai governance.Nature, 656(8127):
320–328, 2026.
Q. Ke, E. Ferrara, F. Radicchi, and A. Flammini.
Defining and identifying sleeping beauties in
science.Proceedings of the National Academy of
Sciences, 112(24):7426–7431, 2015.
D. Keith.A case for climate engineering. MIT Press,
2013.
E. Kiciman, R. Ness, A. Sharma, and C. Tan.
Causal reasoning and large language models:
Opening a new frontier for causality.Transac-
tions on Machine Learning Research, 2023.
C. Kim, S. Kumar, and M. Sked. Inventorship
guidance for ai-assisted inventions, 2024.
S. H. King, C. L. Driscoll, D. B. Li, D. Guo, A. T.
Merchant, G. Brixi, M. E. Wilkinson, and B. L.
43

Agentic Economies for Autonomous Scientific Discovery
Hie. Generative design of bacteriophages with
genome language models.Science, 393(6811):
eaec2657, 2026.
M. Kinniment, L. J. K. Sato, H. Du, B. Goodrich,
M.Hasin,L.Chan,L.H.Miles,T.R.Lin,H.Wijk,
J. Burget, et al. Evaluating language-model
agents on realistic autonomous tasks.arXiv
preprint arXiv:2312.11671, 2023.
K. Kirkpatrick. The carbon footprint of artificial
intelligence.Communications of the ACM, 66
(8):17–19, 2023.
B. Knott, S. Venkataraman, A. Hannun, S. Sen-
gupta, M. Ibrahim, and L. van der Maaten.
Crypten: Secure multi-party computation
meets machine learning.Advances in Neural
Information Processing Systems, 34:4961–4973,
2021.
P. W. Koh and P. Liang. Understanding black-box
predictions via influence functions. InInter-
national conference on machine learning, pages
1885–1894. PMLR, 2017.
R. Kohavi, D. Tang, and Y. Xu.Trustworthy online
controlled experiments: A practical guide to a/b
testing. Cambridge University Press, 2020.
L. Kong, X. Sun, W. Chow, L. Li, K. Q. Lin, X. B.
Zhang, S. Wang, R. Li, Q. Wu, W. Gao, Y. Wang,
S. Xie, J. Liu, L. Qu, S. Li, L. X. Ng, B. R. Cot-
tereau, Z. Liu, T.-S. Chua, and W. T. Ooi. AI
for Auto-Research: Roadmap & User Guide,
2026. URLhttps://arxiv.org/abs/2605.
18661.
T. Korbak, M. Balesni, E. Barnes, Y. Bengio, J. Ben-
ton, J. Bloom, M. Chen, A. Cooney, A. Dafoe,
A. Dragan, et al. Chain of thought monitorabil-
ity: A new and fragile opportunity for ai safety.
arXiv preprint arXiv:2507.11473, 2025.
M. Kremer, J. Levin, and C. M. Snyder. Advance
marketcommitments: insightsfromtheoryand
experience. InAEA Papers and Proceedings,
volume 110, pages 269–273. American Eco-
nomic Association 2014 Broadway, Suite 305,
Nashville, TN 37203, 2020.
W. Kuang, B. Qian, Z. Li, D. Chen, D. Gao,
X. Pan, Y. Xie, Y. Li, B. Ding, and J. Zhou.
Federatedscope-llm: A comprehensive package
for fine-tuning large language models in feder-
ated learning. InProceedings of the 30th ACM
SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 5260–5271, 2024.
T. S. Kuhn and I. Hacking.The structure of sci-
entific revolutions, volume 2. University of
Chicago press Chicago, 1970.
T. D. Kulkarni, K. Narasimhan, A. Saeedi, and
J.Tenenbaum. Hierarchicaldeepreinforcement
learning: Integrating temporal abstraction and
intrinsic motivation.Advances in neural infor-
mation processing systems, 29, 2016.
R. Kumar, S. P. Das, B. U. Choudhury, A. Kumar,
N. R. Prakash, R. Verma, M. Chakraborti, A. G.
Devi, B. Bhattacharjee, R. Das, et al. Advances
in genomic tools for plant breeding: harnessing
dna molecular markers, genomic selection, and
genome editing.Biological Research, 57(1):80,
2024.
T.-T. Kuo, H.-E. Kim, and L. Ohno-Machado.
Blockchain distributed ledger technologies for
biomedical and health care applications.Jour-
nal of the American Medical Informatics Associa-
tion, 24(6):1211–1220, 2017.
K. Kusumegi, X. Yang, P. Ginsparg, M. de Vaan,
T. Stuart, and Y. Yin. Scientific production in
the era of large language models.Science, 390
(6779):1240–1243, 2025.
M. S. Lau, C. J. E. Metcalf, Z. Liu, B. T. Grenfell,
and W. Jin. Toward ai foundation models for
epidemics: Promise, challenges, and paths for-
ward.Proceedings of the National Academy of
Sciences, 123(13):e2526192123, 2026.
M. Lavrichenko. Thaler v. vidal: Artificial
intelligence-can the invented become the in-
ventor.CARDOZo L. REv., 44:699, 2022.
J.-A. Lee, R. M. Hilty, and K.-C. Liu.Artificial
intelligence and intellectual property. Oxford
University Press (UK), 2021.
K.-F. Lee.AI superpowers: China, Silicon Val-
ley, and the new world order. Harper Business,
2018.
44

Agentic Economies for Autonomous Scientific Discovery
M. A. Lemley. The surprising virtues of treating
trade secrets as IP rights. InThe law and theory
of trade secrecy. Edward Elgar Publishing, 2011.
M. K. Leung, A. Delong, B. Alipanahi, and B. J.
Frey. Machine learning in genomic medicine:
a review of computational problems and data
sets.Proceedings of the IEEE, 104(1):176–197,
2015.
B. N. Levine, C. Shields, and N. B. Margolin. A
surveyofsolutionstothesybilattack.University
of Massachusetts Amherst, Amherst, MA, 7:224,
2006.
D. S. Levine and T. Sichelman. Why do startups
use trade secrets.Notre Dame L. Rev., 94:751,
2018.
B. Li, H. Fei, T. Ju, M.-L. Lee, and W. Hsu. Omni-
scientist: An omni-modal omni-discipline ai sci-
entist.arXiv preprint arXiv:2608.13558, 2026a.
J. Li, K. Lim, H. Yang, Z. Ren, S. Raghavan, P.-Y.
Chen, T. Buonassisi, and X. Wang. Ai applica-
tions through the whole life cycle of material
discovery.Matter, 3(2):393–432, 2020.
X. Li, B. Zhao, G. Yang, T. Xiang, J. Weng, and
R. H. Deng. A survey of secure computation
using trusted execution environments.arXiv
preprint arXiv:2302.12150, 2023.
Z. Li, L. Zhu, Y. Liu, Y. Zhao, B. Li, R. Wu,
J. Jin, and J. Zhang. Kiss - knowledge infras-
tructure for scientific simulation: A scaffold-
ing for agentic earth science, 2026b. URL
https://arxiv.org/abs/2605.17856.
C. Liu, W. Zhuang, L. Liu, Y. Chen, C. Yang,
H. Chen, Y. Yao, X. Sun, and W. W. Hu. Re-
search progress in high-throughput dna syn-
thesis and its applications.Journal of Materials
Chemistry B, 13(27):7973–8004, 2025.
J. Liu, J. Pei, J. Huang, C. Si, A. Qu, X. Tang, R. Lu,
L. Chen, X. Bai, H. Zheng, C. Chen, Z. Chen,
H. Ye, Y. Fu, Z. He, Z. Jin, Z. Zhang, S. Sun,
M. Harmon, J. D. Wang, J. Zeng, J. Sun, M. Wu,
B. Zhou, C. You, S. Lu, Y. Qiu, F. Lai, Y. Yuan,
Y. Li, J. Hong, R. Zhu, B. Chen, A. Pentland,
A. Chen, M. Chowdhury, and Z. Zhang. The last
human-written paper: Agent-native research
artifacts, 2026. URL https://arxiv.org/
abs/2604.24658.
Y. Lou, H. Hu, S. Ma, Z. Zhang, L. Wang, J. Ge,
and X. Tao. Drf: Llm-agent dynamic reputation
filteringframework. InInternationalConference
on Neural Information Processing, pages 127–
141. Springer, 2025.
C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune,
and D. Ha. The ai scientist: Towards
fully automated open-ended scientific discov-
ery, 2024a. URLhttps://arxiv.org/abs/
2408.06292.
C. Lu, C. Lu, R. T. Lange, Y. Yamada,
S. Hu, J. Foerster, D. Ha, and J. Clune.
Towards end-to-end automation of ai re-
search.Nature, 651(8107):914–919, mar
2026. ISSN 1476-4687. doi: 10.1038/
s41586-026-10265-5. URL https://doi.
org/10.1038/s41586-026-10265-5.
X. Lu, C. Yang, L. Liang, G. Hu, Z. Zhong, and
Z. Jiang. Artificial intelligence for optimizing
recruitment and retention in clinical trials: a
scoping review.Journal of the American Medi-
cal Informatics Association, 31(11):2749–2759,
2024b.
S. Luccioni, B. Gamazaychikov, S. Hooker, R. Pier-
rard, E. Strubell, Y. Jernite, and C.-J. Wu. Light
bulbshaveenergyratings—sowhycan’taichat-
bots?Nature, 632(8026):736–738, 2024a.
S. Luccioni, Y. Jernite, and E. Strubell. Power
hungry processing: Watts driving the cost of
ai deployment? InProceedings of the 2024
ACM conference on fairness, accountability, and
transparency, pages 85–99, 2024b.
S. Luccioni, B. Trevelin, and M. Mitchell. The
environmental impacts of ai–primer.Hugging
Face Blog, 2024c.
A. M. Lunt, H. Fakhruldeen, G. Pizzuto, L. Long-
ley, A. White, N. Rankin, R. Clowes, B. Alston,
L. Gigli, G. M. Day, et al. Modular, multi-robot
integration of laboratories: an autonomous
workflow for solid-state chemistry.Chemical
Science, 15(7):2456–2463, 2024.
45

Agentic Economies for Autonomous Scientific Discovery
Z. Luo, A. Kasirzadeh, and N. B. Shah. The
more you automate, the less you see: Hidden
pitfalls of ai scientist systems.arXiv preprint
arXiv:2509.08713, 2025.
D. Ma, J. Pang, M. B. Gotway, and J. Liang. A fully
open ai foundation model applied to chest ra-
diography.Nature, 643(8071):488–498, 2025.
M. A. Ma, D. E. Gutiérrez, J. M. Frausto, and
W. K. Al-Delaimy. Minority representation in
clinical trials in the united states: trends over
the past 25 years. InMayo Clinic Proceedings,
volume 96, pages 264–266. Elsevier, 2021.
Y. Ma, Z. Gou, J. Hao, R. Xu, S. Wang, L. Pan,
Y. Yang, Y. Cao, and A. Sun. Sciagent: Tool-
augmented language models for scientific rea-
soning. InProceedings of the 2024 conference
on empirical methods in natural language pro-
cessing, pages 15701–15736, 2024a.
Y. Ma, Z. Zhang, B. Jia, and Y. Yuan. Automated
high-throughput dna synthesis and assembly.
Heliyon, 10(6), 2024b.
M. A. Majumder, R. Cook-Deegan, and A. L.
McGuire. Beyond our borders? public resis-
tance to global genomic data sharing.PLoS
biology, 14(11):e2000206, 2016.
S. P. Mann, M. Aboy, J. J. Seah, Z. Lin, X. Luo,
D. Rodger, H. Zohny, T. Minssen, J. Savulescu,
and B. D. Earp. Ai and the future of academic
peer review, 2026. URL https://arxiv.
org/abs/2509.14189.
M. Marks and C. E. Haupt. Ai chatbots, health
privacy, and challenges to hipaa compliance.
Jama, 330(4), 2023.
F. Massadeh, F. Alnusair, A. A. Mahdi Massadeh,
and M. Ismail. The legal protection of artificial
intelligence-generated work: The argument for
sui generis over copyright.Corporate Law &
Governance Review, 6(1), 2024.
K. McKibbin and M. Shabani. Genomic data as
a national strategic resource: implications for
the genomic commons and international data
sharing for biomedical research and innovation.
Journal of Law, Medicine & Ethics, 51(2):301–
313, 2023.
B. McMahan, E. Moore, D. Ramage, S. Hampson,
and B. A. y Arcas. Communication-efficient
learning of deep networks from decentralized
data. InArtificial intelligence and statistics,
pages 1273–1282. Pmlr, 2017.
D. Mehta, N. Harihar, S. Patel, N. L. Sanil, R. Shal-
lam, M. J. Roddy, F. Ribeiro, T. Pan, C. Rose,
T. Beyondr, et al. Marketplace for impact
certificates. InCompanion Publication of the
2024 Conference on Computer-Supported Co-
operative Work and Social Computing, pages
75–78, 2024.
L. Meincke, G. Nave, and C. Terwiesch. Chatgpt
decreases idea diversity in brainstorming.Na-
ture Human Behaviour, 9(6):1107–1109, 2025.
A. Meiseles, I. Rosenberg, Y. Motro, L. Rokach,
and J. Moran-Gilad. Adversarial vulnera-
bility of deep learning models in analyzing
next generation sequencing data. In2020
IEEE international conference on bioinformatics
and biomedicine (BIBM), pages 464–468. IEEE,
2020.
F. Mendonca, G. DiMarzo, and N. Abdennad-
her. Data cooperatives: Democratic models
for ethical data stewardship.arXiv preprint
arXiv:2504.10058, 2025.
A. Merchant, S. Batzner, S. S. Schoenholz,
M. Aykol, G. Cheon, and E. D. Cubuk. Scaling
deep learning for materials discovery.Nature,
624(7990):80–85, 2023.
L. Messeri and M. J. Crockett. Artificial intelli-
gence and illusions of understanding in scien-
tific research.Nature, 627(8002):49–58, 2024.
V. Mignon and M. Joëts. Slaying the Undead:
How Long Does It Take to Kill Zombie Papers?
working paper or preprint, 2025. URLhttps:
//hal.science/hal-04940088.
J. Milionis, C. C. Moallemi, T. Roughgarden,
and A. L. Zhang. Automated market mak-
ing and loss-versus-rebalancing.arXiv preprint
arXiv:2208.06046, 2022.
Y. Millo, F. Muniesa, N. S. Panourgias, and S. V.
Scott. Organised detachment: Clearinghouse
46

Agentic Economies for Autonomous Scientific Discovery
mechanisms in financial markets.Information
and Organization, 15(3):229–246, 2005.
P. Mirowski and R. Van Horn. The contract re-
search organization and the commercialization
of scientific research.Social studies of science,
35(4):503–548, 2005.
P. Missier, K. Belhajjame, and J. Cheney. The
w3c prov family of specifications for mod-
elling provenance metadata. InProceedings of
the 16th international conference on extending
database technology, pages 773–776, 2013.
A. K. Mitra and A. R. Mawson. Neglected tropi-
cal diseases: epidemiology and global burden.
Tropical medicine and infectious disease, 2(3):
36, 2017.
T. Miyakawa. No raw data, no science: another
possible source of the reproducibility crisis,
2020.
A. Mlinarić, M. Horvat, and V. Šupak Smolčić.
Dealing with the positive publication bias: Why
you should really publish your negative results.
Biochemia medica, 27(3):447–452, 2017.
K. R. Moffat, W. Shi, P. Cannon, and F. Sulli-
van. Factors associated with recruitment to
randomised controlled trials in general prac-
tice: a systematic mixed studies review.Trials,
24(1):90, 2023.
B. Mons, C. Neylon, J. Velterop, M. Dumontier,
L. O. B. da Silva Santos, and M. D. Wilkinson.
Cloudy,increasinglyfair; revisitingthefairdata
guiding principles for the european open sci-
ence cloud.Information Services and Use, 37
(1):49–56, 2017.
L. d. Moura and S. Ullrich. The lean 4 theorem
prover and programming language. InInter-
national Conference on Automated Deduction,
pages 625–635. Springer, 2021.
C. A. Mouton, C. Lucas, and E. Guest. The opera-
tionalrisksofaiinlarge-scalebiologicalattacks:
A red-team approach, 2023.
C. A. Mouton, C. Lucas, and E. Guest. The opera-
tionalrisksofaiinlarge-scalebiologicalattacks.
Technical report, RAND Corporation, 2024.
L. Mui, M. Mohtashemi, and A. Halberstadt. No-
tions of reputation in multi-agents systems: a
review. InProceedings of the first international
joint conference on Autonomous agents and mul-
tiagent systems: part 1, pages 280–287, 2002.
H. Murayama, S. Asai, K. Heeger, A. Ballar-
ino, T. Bose, K. Cranmer, F.-Y. Cyr-Racine,
S. Demers, C. Geddes, Y. Gershtein, B. Heine-
mann, J. Hewett, P. Huber, K. Mahn, R. Man-
delbaum, J. Maricic, P. Merkel, C. Mona-
han, P. Onyisi, M. Palmer, T. Raubenheimer,
M. Sanchez, R. Schnee, S. Seidel, S.-H. Seo,
J. Thaler, C. Touramanis, A. Vieregg, A. We-
instein, L. Winslow, T.-T. Yu, and R. Zwaska.
Exploring the quantum universe: Pathways to
innovation and discovery in particle physics,
2023. URL http://dx.doi.org/10.2172/
2368847.
P. Murray-Rust. Open data in science.Nature
Precedings, pages 1–1, 2008.
M. Naddaf. Ai is transforming peer review—and
many scientists are worried.Nature, 639
(8056):852–854, 2025.
M.R.NairandT.Roy. Roleofartificialintelligence
in the design and discovery of next-generation
battery electrolytes.Chemical Physics Reviews,
6(1), 2025.
A. Narayanan and S. Kapoor. Ai as normal tech-
nology.Knight First Amendment Institute, 25,
2025.
A. Navia-Vázquez, J. Cid-Sueiro, and M. A.
Vázquez. “a priori” shapley data value esti-
mation.Pattern Analysis and Applications, 28
(2):77, 2025.
R. R. Nelson. The simple economics of basic sci-
entific research.Journal of political economy,
67(3):297–306, 1959.
R. Ngo, L. Chan, and S. Mindermann. The align-
mentproblemfromadeeplearningperspective.
arXiv preprint arXiv:2209.00626, 2022.
T. Nguyen, A. Koneru, S. Li, and A. Grover. Physix:
A foundation model for physics simulations.
arXiv preprint arXiv:2506.17774, 2025.
47

Agentic Economies for Autonomous Scientific Discovery
J. Ning, X. Li, S. Zhong, J. Zeng, and G. Ke. Auto
research for materials: Auditable ai-scientist
workflows with held-out transfer, 2026. URL
https://arxiv.org/abs/2607.17100.
B. A. Nosek and Y. Bar-Anan. Scientific utopia: I.
opening scientific communication.Psychologi-
cal Inquiry, 23(3):217–243, 2012.
B. A. Nosek, G. Alter, G. C. Banks, D. Borsboom,
S. D. Bowman, S. J. Breckler, S. Buck, C. D.
Chambers, G. Chin, G. Christensen, et al. Pro-
moting an open research culture.Science, 348
(6242):1422–1425, 2015.
A. Novikov, N. V˜u, M. Eisenberger, E. Dupont,
P.-S. Huang, A. Z. Wagner, S. Shirobokov, B. Ko-
zlovskii, F. J. R. Ruiz, A. Mehrabian, M. P.
Kumar, A. See, S. Chaudhuri, G. Holland,
A. Davies, S. Nowozin, P. Kohli, and M. Ba-
log. Alphaevolve: A coding agent for scien-
tific and algorithmic discovery, 2025. URL
https://arxiv.org/abs/2506.13131.
N. A. of Sciences, Medicine, Policy, G. Affairs,
B. on Research Data, Information, and C. on To-
wardanOpenScienceEnterprise. Openscience
by design: Realizing a vision for 21st century
research, 2018.
A. R. Oganov, C. J. Pickard, Q. Zhu, and R. J.
Needs. Structure prediction drives materials
discovery.Nature Reviews Materials, 4(5):331–
348, 2019.
OpenAI. Finite Time Blowup for
Navier Stokes, 2026a. URL
https://cdn.openai.com/pdf/
32d9f210-8b73-45e0-91bc-82a30aef8a9a/
navier-stokes.pdf. Accessed: 10 Septem-
ber 2026.
OpenAI. Ten advances in mathematics
and theoretical computer science, 2026b.
URL https://cdn.openai.com/pdf/
ten-proofs-oai.pdf.
W. H. Organization.Investing to overcome the
global impact of neglected tropical diseases: third
WHO report on neglected tropical diseases 2015,
volume 3. World Health Organization, 2015.
W. H. Organization et al.Working to overcome
the global impact of neglected tropical diseases:
first WHO report on neglected tropical diseases.
World Health Organization, 2010.
C. Ortlepp. Introducing the IP-NFT
V2. Molecule Blog, December 2022.
URL https://molecule.xyz/blog/
introducing-ip-nft-v2.
P. Pallmann, A. W. Bedding, B. Choodari-Oskooei,
M.Dimairo,L.Flight,L.V.Hampson,J.Holmes,
A. P. Mander, L. Odondi, M. R. Sydes, et al.
Adaptive designs in clinical trials: why use
them, and how to run and report them.BMC
medicine, 16(1):29, 2018.
G. K. Palshikar and M. M. Apte. Collusion set
detection using graph clustering.Data min-
ing and knowledge Discovery, 16(2):135–164,
2008.
J. Pannu, D. Bloomfield, R. MacKnight, M. S.
Hanke, A. Zhu, G. Gomes, A. Cicero, and T. V.
Inglesby. Dual-use capabilities of concern of bi-
ological ai models.PLoS computational biology,
21(5):e1012975, 2025.
M. Parashar, T. DeBlanc-Knowles, E. Gianchan-
dani, and L. E. Parker. Strengthening and de-
mocratizing artificial intelligence research and
development.Computer, 56(11):85–90, 2023.
D. Park, S. Li, Y. Huang, X. Luo, H. Yu, Y. Go,
C. Pinkenburg, Y. Lin, S. Yoo, J. Osborn,
J. Huang, and Y. Ren. Fm4npp: A scaling foun-
dation model for nuclear and particle physics,
2025. URLhttps://arxiv.org/abs/2508.
14087.
M. Park, E. Leahey, and R. J. Funk. Papers and
patents are becoming less disruptive over time.
Nature, 613(7942):138–144, 2023.
L. Parker, F. Lanusse, S. Golkar, L. Sarra, M. Cran-
mer, A. Bietti, M. Eickenberg, G. Krawezik,
M. McCabe, R. Morel, et al. Astroclip: a cross-
modal foundation model for galaxies.Monthly
Notices of the Royal Astronomical Society, 531
(4):4990–5011, 2024.
D. Partha and P. A. David. Toward a new eco-
nomics of science.Research policy, 23(5):487–
521, 1994.
48

Agentic Economies for Autonomous Scientific Discovery
O. PBC and V. Buterin. Retroactive pub-
lic goods funding, 2021. URL https:
//medium.com/ethereum-optimism/
retroactive-public-goods-funding-33c9b7d00f0c.
J. Pearl.The book of why: The new science of cause
and effect. Basic Books, 2018.
J. Peccoud, J. E. Gallegos, R. Murch, W. G. Buch-
holz, and S. Raman. Cyberbiosecurity: from
naive trust to risk awareness.Trends in biotech-
nology, 36(1):4–7, 2018.
E. Perez, S. Huang, F. Song, T. Cai, R. Ring,
J. Aslanides, A. Glaese, N. McAleese, and G. Irv-
ing. Red teaming language models with lan-
guage models. InProceedings of the 2022 Con-
ference on Empirical Methods in Natural Lan-
guage Processing, pages 3419–3448, 2022.
J. Peters, D. Janzing, and B. Scholkopf.Elements
of causal inference: foundations and learning
algorithms. MIT press, 2017.
P. G. Picht, V. Brunner, and R. Schmid. Artificial
intelligenceandintellectualpropertylaw: from
diagnosis to action, 2022.
I. Pinyol and J. Sabater-Mir. Computational trust
and reputation models for open multi-agent
systems: a review.Artificial Intelligence Review,
40(1):1–25, 2013.
G. Poesia, D. Broman, N. Haber, and N. Goodman.
Learning formal mathematics from intrinsic
motivation. In A. Globerson, L. Mackey,
D. Belgrave, A. Fan, U. Paquet, J. Tomczak,
and C. Zhang, editors,Advances in Neural
Information Processing Systems, volume 37,
pages 43032–43057. Curran Associates,
Inc., 2024. doi: 10.52202/079017-1362.
URL https://proceedings.neurips.
cc/paper_files/paper/2024/file/
4b8001fc75f0532827472ea5a16af9ca-Paper-Conference.
pdf.
E. Posner and E. Weyl.Radical markets: Uproot-
ing capitalism and democracy for a just society.
Princeton University Press, 2018.
I. Posner, A. Lei, and B. Schölkopf. From observa-
tion to insight: Mechanistic world models and
the quest for autonomous discovery, 2026. URL
https://arxiv.org/abs/2607.12474.
D. Pratt. Symposium: Trust via auditable
records for communities of ai scientist agents,
2026. URLhttps://arxiv.org/abs/2608.
19511.
I. Price, A. Sanchez-Gonzalez, F. Alet, T. R. Ander-
sson, A. El-Kadi, D. Masters, T. Ewalds, J. Stott,
S. Mohamed, P. Battaglia, et al. Probabilistic
weather forecasting with machine learning.Na-
ture, 637(8044):84–90, 2025.
S. L. Price. Predicting crystal structures of organic
compounds.Chemical Society Reviews, 43(7):
2098–2111, 2014.
W. N. Price and I. G. Cohen. Privacy in the age
of medical big data.Nature Medicine, 25(1):
37–43, 2019.
G. L. Priest. The invention of enterprise liability:
A critical history of the intellectual foundations
of modern tort law.The Journal of Legal Studies,
14(3):461–527, 1985.
P.Rajpurkar, E.Chen, O.Banerjee, andE.J.Topol.
Ai in health and medicine.Nature Medicine, 28
(1):31–38, 2022.
S. Rajtmajer, C. Griffin, J. Wu, R. Fraleigh, L. Bal-
aji, A. Squicciarini, A. Kwasnica, D. Pennock,
M. McLaughlin, T. Fritton, et al. A synthetic
prediction market for estimating confidence
in published work. InProceedings of the AAAI
Conference on Artificial Intelligence, volume 36,
pages 13218–13220, 2022.
A. S. Ramesh, S. Vigneshwar, S. Vickram,
S. Manikandan, R. Subbaiya, N. Karmegam,
and W. Kim. Artificial intelligence driven hy-
drogenandbatterytechnologies–areview.Fuel,
337:126862, 2023.
R. A. Rasheed, S. Banerjee, A. Mukherjee, and
R. Hazra. From fluent to verifiable: Claim-level
auditability for deep research agents.arXiv
preprint arXiv:2602.13855, 2026.
I. Rauluseviciute, R. Riudavets-Puig, R. Blanc-
Mathieu, J. A. Castro-Mondragon, K. Ferenc,
V. Kumar, R. B. Lemma, J. Lucas, J. Chèneby,
49

Agentic Economies for Autonomous Scientific Discovery
D. Baranasic, et al. Jaspar 2024: 20th anniver-
sary of the open-access database of transcrip-
tion factor binding profiles.Nucleic acids re-
search, 52(D1):D174–D182, 2024.
J. Ravenscroft, M. Liakata, A. Clare, and D. Duma.
Measuring scientific impact beyond academia:
An assessment of existing impact metrics and
proposed improvements.PloS one, 12(3):
e0173152, 2017.
G. K. Reder, A. H. Gower, F. Kronström, R. Halle,
V. Mahamuni, A. Patel, H. Hayatnagarkar, L. N.
Soldatova, and R. D. King. Genesis-db: a
database for autonomous laboratory systems.
Bioinformatics Advances, 3(1):vbad102, 2023.
S. Redyuk. Automated documentation of end-to-
end experiments in data science. In2019 IEEE
35th International Conference on Data Engineer-
ing (ICDE), pages 2076–2080. IEEE, 2019.
Z. Ren, R. Li, X. Zhang, Z. Pang, S. Ren, and
J. Zhang. Evigraph: Evidence-guided au-
tonomous research agents, 2026. URLhttps:
//arxiv.org/abs/2608.04738.
D. B. Ridley, H. G. Grabowski, and J. L. Moe. De-
veloping drugs for developing countries.Health
Affairs, 25(2):313–324, 2006.
N. Rieke, J. Hancox, W. Li, F. Milletari, H. R. Roth,
S. Albarqouni, S. Bakas, M. N. Galtier, B. A.
Landman, K. Maier-Hein, et al. The future of
digital health with federated learning.NPJ
digital medicine, 3(1):119, 2020.
M. S. Ringel, J. W. Scannell, M. Baedeker, and
U. Schulze. Breaking eroom’s law.Nat Rev Drug
Discov, 19(12):833–834, 2020.
M. Ríos-García, N. Alampara, C. Gupta, I. Mandal,
S. Mannan, A. A. Aghajani, N. Krishnan, and
K. M. Jablonka. Ai scientists produce results
without reasoning scientifically.arXiv preprint
arXiv:2604.18805, 2026.
L.Rocher, J.M.Hendrickx, andY.-A.DeMontjoye.
Estimating the success of re-identifications in
incomplete datasets using generative models.
Nature Communications, 10(1):3069, 2019.
M. J. G. Rodríguez, V. Rodríguez-Montequín,
P. Ballesteros-Pérez, P. E. Love, and R. Signor.
Collusion detection in public procurement auc-
tions with machine learning algorithms.Au-
tomation in Construction, 133:104047, 2022.
A. E. Roth. The economist as engineer: Game
theory, experimentation, and computation as
tools for design economics.Econometrica, 70
(4):1341–1378, 2002.
J. Rothfuss, B. Sukhija, L. Treven, F. Dörfler,
S. Coros, and A. Krause. Bridging the sim-to-
real gap with bayesian inference, 2024. URL
https://arxiv.org/abs/2403.16644.
J.P.Ruger. Ethicsandgovernanceofglobalhealth
inequalities.Journal of Epidemiology & Com-
munity Health, 60(11):998–1002, 2006.
A. Sabharwal, M. S. Patel, A. Carrano, M. Rot-
man, W. Wierson, and S. C. Ekker. Vaas is
a multi-layer hallucination reduction pipeline
for ai-assisted science: Production validation
and prospective benchmarking.medRxiv, pages
2026–03, 2026.
S. Sahoo, A. Chadha, V. Jain, and D. Chaud-
hary. Sahoo: Safeguarded alignment for high-
order optimization objectives in recursive self-
improvement, 2026. URL https://arxiv.
org/abs/2603.06333.
J. B. Sandbrink. Artificial intelligence and bi-
ological misuse: Differentiating risks of lan-
guage models and biological design tools.arXiv
preprint arXiv:2306.13952, 2023.
G. Sastry, L. Heim, H. Belfield, M. Anderljung,
M. Brundage, J. Hazell, C. O’keefe, G. K. Had-
field, R. Ngo, K. Pilz, et al. Computing power
and the governance of artificial intelligence.
arXiv preprint arXiv:2402.08797, 2024.
J. W. Scannell, A. Blanckley, H. Boldon, and
B. Warrington. Diagnosing the decline in phar-
maceutical r&d efficiency.Nature Reviews Drug
Discovery, 11(3):191–200, 2012.
B. Schölkopf, F. Locatello, S. Bauer, N. R. Ke,
N. Kalchbrenner, A. Goyal, and Y. Bengio. To-
ward causal representation learning.Proceed-
ings of the IEEE, 109(5):612–634, 2021.
50

Agentic Economies for Autonomous Scientific Discovery
E. Schultes, B. Magagna, T. Kuhn, M. Suchánek,
L. B. da Silva Santos, and B. Mons. The com-
parative anatomy of nanopublications and fair
digital objects.Research ideas and outcomes, 8:
e94150, 2022.
L. Schut, N. Tomasev, T. McGrath, D. Hassabis,
U. Paquet, and B. Kim. Bridging the human-ai
knowledge gap: Concept discovery and trans-
fer in alphazero, 2023. URLhttps://arxiv.
org/abs/2310.16410.
G. Schweiger, A. Barnett, P. van den Besselaar,
L. Bornmann, A. De Block, J. P. Ioannidis,
U. Sandström, and S. Conix. The costs of com-
petition in distributing scarce research funds.
Proceedings of the National Academy of Sciences,
121(50):e2407644121, 2024.
E. Seger, N. Dreksler, R. Moulange, E. Dardaman,
J. Schuett, K. Wei, C. Winter, M. Arnold, S. Ó.
hÉigeartaigh, A. Korinek, et al. Open-sourcing
highly capable foundation models: An evalu-
ation of risks, benefits, and alternative meth-
ods for pursuing open-source objectives.arXiv
preprint arXiv:2311.09227, 2023.
M. Seifrid, R. Pollice, A. Aguilar-Granda, Z. Mor-
gan Chan, K. Hotta, C. T. Ser, J. Vestfrid, T. C.
Wu, and A. Aspuru-Guzik. Autonomous chemi-
cal experiments: Challenges and perspectives
on establishing a self-driving lab.Accounts of
Chemical Research, 55(17):2454–2466, 2022.
N. Selvadurai. Inventions without inventors: The
need to recognize ai systems as inventors.Case
W. Res. JL Tech. & Internet, 16:37, 2025.
A. Sertkaya, H.-H. Wong, A. Jessup, and
T. Beleche. Key cost drivers of pharmaceuti-
cal clinical trials in the united states.Clinical
Trials, 13(2):117–126, 2016.
J. Shendure, S. Balasubramanian, G. M. Church,
W. Gilbert, J. Rogers, J. A. Schloss, and R. H.
Waterston. Dna sequencing at 40: past, present
and future.Nature, 550(7676):345–353, 2017.
A. Shenoy, G. Shenoy, and G. Shenoy. Respondeat
superior in medicine and public health practice:
the question is–who is accountable for whom?
Ethics, Medicine and Public Health, 17:100634,
2021.
T. Shevlane. Structured access: an emerging
paradigmforsafeaideployment.arXivpreprint
arXiv:2201.05159, 2022.
M.Shilina. Leveragingtokeneconomiesforpublic
goods. InThe Impact of Blockchain in Token
Economies,pages291–322.IGIGlobalScientific
Publishing, 2026.
C. Si, T. Hashimoto, and D. Yang. The ideation-
execution gap: Execution outcomes of llm-
generated versus human research ideas.arXiv
preprint arXiv:2506.20803, 2025.
J. Skalse, N. Howe, D. Krasheninnikov, and
D. Krueger. Defining and characterizing re-
ward gaming.Advances in Neural Information
Processing Systems, 35:9460–9471, 2022.
T. Skordas. Toward a european exascale ecosys-
tem: the eurohpc joint undertaking.Communi-
cations of the ACM, 62(4):70–70, 2019.
T. M. Smith, T. R. Karl, and R. W. Reynolds. How
accurate are climate simulations?Science, 296
(5567):483–484, 2002.
E. H. Soice, R. Rocha, K. Cordova, M. Specter,
and K. M. Esvelt. Can large language models
democratize access to dual-use biotechnology?
arXiv preprint arXiv:2306.03809, 2023.
S. Soiland-Reyes, P. Sefton, M. Crosas, L. J. Cas-
tro, F. Coppens, J. M. Fernández, D. Garijo,
B. Grüning, M. La Rosa, S. Leo, et al. Pack-
aging research artefacts with ro-crate.Data
Science, 5(2):97–138, 2022.
K. Sridharan and G. Sivaramakrishnan. Assess-
ing the decision-making capabilities of artificial
intelligence platforms as institutional review
board members.Journal of Empirical Research
on Human Research Ethics, 19(3):83–91, 2024.
G. Starace, O. Jaffe, D. Sherburn, J. Aung, J. S.
Chan, L. Maksin, R. Dias, E. Mays, B. Kinsella,
W. Thompson, et al. Paperbench: Evaluat-
ing ai’s ability to replicate ai research.arXiv
preprint arXiv:2504.01848, 2025.
P.Stephan.Howeconomicsshapesscience. Harvard
University Press, 2015.
51

Agentic Economies for Autonomous Scientific Discovery
J. M. Stokes, K. Yang, K. Swanson, W. Jin,
A. Cubillos-Ruiz, N. M. Donghia, C. R. MacNair,
S. French, L. A. Carfrae, Z. Bloom-Ackermann,
et al. A deep learning approach to antibiotic
discovery.Cell, 180(4):688–702, 2020.
R.J.Strijkers, R.Cushing, D.Vasyunin, C.deLaat,
A. Belloum, R. J. Meijer, et al. Toward exe-
cutable scientific publications. InICCS, pages
707–715, 2011.
Y. Suchikova, N. Tsybuliak, J. A. Teixeira da Silva,
and S. Nazarovets. Gaidet (generative ai del-
egation taxonomy): A taxonomy for humans
to delegate tasks to generative artificial intelli-
gence in scientific research and publishing.Ac-
countability in Research, 33(3):2544331, 2026.
E. Sullivan. Understanding from machine learn-
ing models.The British Journal for the Philoso-
phy of Science, 2022.
Y. Sun, L. Wang, G. Li, W. Lin, and L. Wang.
A foundation model for enhancing magnetic
resonance images and downstream segmenta-
tion, registration and diagnostic tasks.Nature
Biomedical Engineering, 9(4):521–538, 2025.
C. Szabo.Unreliable: bias, fraud, and the
reproducibility crisis in biomedical research.
Columbia University Press, 2025.
N. J. Szymanski, B. Rendy, Y. Fei, R. E. Kumar,
T. He, D. Milsted, M. J. McDermott, M. Gallant,
E.D.Cubuk,A.Merchant,etal. Anautonomous
laboratory for the accelerated synthesis of inor-
ganic materials.Nature, 624(7990):86, 2023.
A. Taeihagh. Governance of artificial intelligence.
Policy and society, 40(2):137–157, 2021.
G. Tamburrini. The ai carbon footprint and re-
sponsibilities of ai scientists.Philosophies, 7(1):
4, 2022.
J. Tang, L. Xia, Z. Li, and C. Huang. Ai-researcher:
Autonomous scientific innovation, 2025. URL
https://arxiv.org/abs/2505.18705.
S. Tang, A. Ghorbani, R. Yamashita, S. Rehman,
J. A. Dunnmon, J. Zou, and D. L. Rubin. Data
valuation for medical imaging using shapley
value and application to a large-scale chest
x-ray dataset.Scientific reports, 11(1):8366,
2021.
T. Tao. Mathematics in the age of ai, 2026. URL
https://arxiv.org/abs/2608.16753.
S. Tayouri, V. Kogan, J. Beal, T. Levy, D. Farbiash,
K. Flyangolts, S. T. Murphy, T. Mitchell, B. Rot-
blat, I. Vaksler-Lublinsky, et al. Defending syn-
thetic dna orders against splitting-based obfus-
cation.bioRxiv, pages 2025–03, 2025.
M. Tian, L. Gao, S. D. Zhang, X. Chen, C. Fan,
X. Guo, R. Haas, P. Ji, K. Krongchon, Y. Li, et al.
Scicode: A research coding benchmark curated
by scientists.Advances in Neural Information
Processing Systems, 37:30624–30650, 2024.
Y. Tian, Y. Ding, S. Fu, and D. Liu. Data boundary
and data pricing based on the shapley value.
IEEE Access, 10:14288–14300, 2022.
E. Toledo, K. Hambardzumyan, M. Josifoski,
R. Hazra, N. Baldwin, A. Audran-Reiss,
M. Kuchnik, D. Magka, M. Jiang, A. M. Lupidi,
et al. Ai research agents for machine learn-
ing: Search, exploration, and generalization in
mle-bench.arXiv preprint arXiv:2507.02554,
2025.
G. Tom, S. P. Schmid, S. G. Baird, Y. Cao,
K. Darvish, H. Hao, S. Lo, S. Pablo-García, E. M.
Rajaonson, M. Skreta, et al. Self-driving lab-
oratories for chemistry and materials science.
Chemical Reviews, 124(16):9633–9732, 2024.
N. Tomasev, M. Franklin, J. Z. Leibo, J. Jacobs,
W. A. Cunningham, I. Gabriel, and S. Osindero.
Virtual agent economies, 2025. URLhttps:
//arxiv.org/abs/2509.10147.
N. Tomašev, M. Franklin, and S. Osindero. In-
telligent ai delegation, 2026. URL https:
//arxiv.org/abs/2602.11865.
M. Topaz, N. Roguin, P. Gupta, Z. Zhang, and
L.-M. Peltonen. Fabricated citations: an au-
dit across 2·5 million biomedical papers.The
Lancet, 407(10541):1779–1781, 2026.
C. S. Traberg, J. Roozenbeek, and S. van der Lin-
den. Ai is turning research into a scientific
monoculture.Communications Psychology, 4
(1):37, 2026.
52

Agentic Economies for Autonomous Scientific Discovery
J. O. Tresansky. Phosita-the ubiquitous and enig-
matic person in patent law.J. Pat. & Trademark
Off. Soc’y, 73:37, 1991.
P. Trouiller, P. Olliaro, E. Torreele, J. Orbinski,
R. Laing, and N. Ford. Drug development for
neglected diseases: a deficient market and a
public-health policy failure.The Lancet, 359
(9324):2188–2194, 2002.
D. Truhn, J. S. Reis-Filho, and J. N. Kather. Large
language models should be used as scientific
reasoning engines, not knowledge databases.
Nature Medicine, 29(12):2983–2984, 2023.
P. F. Uhlir and P. Schröder. Open data for global
science.Data Science Journal, 6:OD36–OD53,
2007.
F. Urbina, F. Lentzos, C. Invernizzi, and S. Ekins.
Dual use of artificial-intelligence-powered drug
discovery.Nature Machine Intelligence, 4(3):
189–191, 2022.
U.S. Senate. Biosecurity modernization and inno-
vation act of 2026, S. 3741. 119th Cong., 2026.
URL https://www.congress.gov/bill/
119th-congress/senate-bill/3741.
R. Van Loo. The revival of respondeat superior
and evolution of gatekeeper liability.Geo. lJ,
109:141, 2020.
R. Van Noorden and J. M. Perkel. Ai and sci-
ence: what 1,600 researchers think.Nature,
621(7980):672–675, 2023.
M. Varadi, S. Anyango, M. Deshpande, S. Nair,
C. Natassia, G. Yordanova, D. Yuan, O. Stroe,
G. Wood, A. Laydon, et al. Alphafold protein
structure database: massively expanding the
structural coverage of protein-sequence space
with high-accuracy models.Nucleic acids re-
search, 50(D1):D439–D444, 2022.
M. Varadi, D. Bertoni, P. Magana, U. Paramval,
I. Pidruchna, M. Radhakrishnan, M. Tsenkov,
S. Nair, M. Mirdita, J. Yeo, et al. Alphafold
protein structure database in 2024: providing
structure coverage for over 214 million pro-
tein sequences.Nucleic acids research, 52(D1):
D368–D375, 2024.
C. Vidal and M. Monperrus. Aicid: Unique iden-
tifiers for ai scientists, 2026. URL https:
//arxiv.org/abs/2606.28756.
R. L. Vogt, P. R. Heck, R. M. Mestechkin, P. Hey-
dari,C.F.Chabris,andM.N.Meyer. Aversionto
pragmatic randomised controlled trials: three
survey experiments with clinicians and laypeo-
pleintheusa.BMJopen, 14(9):e084699, 2024.
W. H. Walters and E. I. Wilder. Fabrication and
errors in the bibliographic citations generated
by chatgpt.Scientific Reports, 13(1):14045,
2023.
H. Wang, T. Fu, Y. Du, W. Gao, K. Huang, Z. Liu,
P. Chandak, S. Liu, P. Van Katwyk, A. Deac,
et al. Scientific discovery in the age of artificial
intelligence.Nature, 620(7972):47–60, 2023.
J.T.WangandR.Jia. Databanzhaf: Arobustdata
valuation framework for machine learning. In
International conference on artificial intelligence
and statistics, pages 6388–6421. PMLR, 2023.
X. Wang, N. He, Z. Zhou, J. Chen, A. Mateen,
Y. Shao, X. Chen, C. Liu, A. Mujear, J. Zhang,
et al. Ai-driven exploration and design of in-
organic battery materials.Renewable and Sus-
tainable Energy Reviews, 229:116633, 2026.
M. Webb. The impact of artificial intelligence on
the labor market.Available at SSRN 3482150,
2019.
J. Wei, Y. Yang, X. Zhang, Y. Chen, X. Zhuang,
Z.Gao,D.Zhou,G.Wang,Z.Gao,J.Cao,Z.Qiu,
M. Hu, C. Ma, S. Tang, J. He, C. Song, X. He,
Q.Zhang,C.You,S.Zheng,N.Ding,W.Ouyang,
N. Dong, Y. Cheng, S. Sun, L. Bai, and B. Zhou.
From ai for science to agentic science: A survey
on autonomous scientific discovery, 2025. URL
https://arxiv.org/abs/2508.14111.
L. Weidener and C. Spreckelsen. Decentralized
science (desci): definition, shared values, and
guiding principles.Frontiers in Blockchain, 7:
1375763, 2024.
M. L. Weitzman. Recombinant growth.The quar-
terly journal of economics, 113(2):331–360,
1998.
53

Agentic Economies for Autonomous Scientific Discovery
D. G. Widder, S. West, and M. Whittaker. Open
(for business): Big tech, concentrated power,
and the political economy of open ai.Nature,
2023.
S. R. Wilkinson, M. Aloqalaa, K. Belhajjame, M. R.
Crusoe, B. de Paula Kinoshita, L. Gadelha,
D.Garijo,O.J.R.Gustafsson,N.Juty,S.Kanwal,
et al. Applying the fair principles to computa-
tional workflows.Scientific data, 12(1):328,
2025.
E. Wójcik-Gront, B. Zieniuk, and M. Pawełkowicz.
Harnessing ai-powered genomic research for
sustainable crop improvement.Agriculture, 14
(12):2299, 2024.
S. M. Woodley and R. Catlow. Crystal structure
prediction from first principles.Nature Materi-
als, 7(12):937–946, 2008.
O.J.Wouters,M.McKee,andJ.Luyten. Estimated
research and development investment needed
to bring a new medicine to market, 2009-2018.
Jama, 323(9):844–853, 2020.
C.-J. Wu, R. Raghavendra, U. Gupta, B. Acun,
N. Ardalani, K. Maeng, G. Chang, F. Aga,
J. Huang, C. Bai, et al. Sustainable ai: En-
vironmental implications, challenges and op-
portunities.Proceedings of machine learning
and systems, 4:795–813, 2022.
S. Wu, Y. Liu, M. Ruan, S. Chen, and X.-Y. Xie.
Human-generative ai collaboration enhances
task performance but undermines human’s in-
trinsic motivation.Scientific Reports, 15(1):
15105, 2025a.
Y. Wu, C. Tian, J. Li, H. Sun, K. Tam, Z. Zhou,
H.Liao, J.Xiong, Z.Guo, L.Li, etal. Asurveyon
federated fine-tuning of large language models.
arXiv preprint arXiv:2503.12016, 2025b.
Y. Xu, X. Liu, X. Cao, C. Huang, E. Liu, S. Qian,
X.Liu, Y.Wu, F.Dong, C.-W.Qiu, etal. Artificial
intelligence: A powerful paradigm for scientific
research.The innovation, 2(4), 2021.
Y. Yamada, R. T. Lange, C. Lu, S. Hu, C. Lu, J. Fo-
erster, J. Clune, and D. Ha. The ai scientist-
v2: Workshop-level automated scientific dis-
covery via agentic tree search.arXiv preprint
arXiv:2504.08066, 2025.
R. V. Yampolskiy.Artificial superintelligence: a
futuristic approach. CRC Press, 2015.
G. Yan, S. Li, P. Ma, Q. Zhang, P. Ma, J. Wang,
M.-H. Hsieh, and Y. Du. Omniqec: discovering
practical quantum error-correcting codes by
an ai scientist, 2026. URLhttps://arxiv.
org/abs/2607.25865.
Y. Yan, S. Wang, J. Huo, J. Ye, Z. Chu, X. Hu,
P. S. Yu, C. Gomes, B. Selman, and Q. Wen.
Position: Multimodal large language models
can significantly advance scientific reasoning.
arXiv preprint arXiv:2502.02871, 2025.
J.-C. Ye, Y.-W. Lai, X.-H. Huang, Z.-X. Chang, Y.-
H. Chung, and C.-M. Shu. Development of
the electrolyte in lithium-ion battery: a con-
cise review on its thermal hazards.Journal
of Thermal Analysis and Calorimetry, 149(19):
11293–11312, 2024.
C. Yencha. The entrepreneurial state: Debunking
public vs. private sector myths, 2015.
X. Yin, X. Wang, L. Pan, L. Lin, X. Wan, and W. Y.
Wang. Gödel agent: A self-referential agent
framework for recursively self-improvement.
InProceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics
(Volume 1: Long Papers), pages 27890–27913,
2025.
H. Ying, Z. Wu, Y. Geng, J. Wang, D. Lin, and
K. Chen. Lean workbook: A large-scale lean
problem set formalized from natural language
math problems.Advances in Neural Information
Processing Systems, 37:105848–105863, 2024.
J. Yoon, S. Arik, and T. Pfister. Data valuation
using reinforcement learning. InInternational
Conference on Machine Learning, pages 10842–
10851. PMLR, 2020.
T. Zahavy. Position: LLMs can’t jump. In
Forty-third International Conference on Machine
Learning Position Paper Track, 2026. URL
https://openreview.net/forum?id=
klU4737opt.
H. Zhang, Y. Liu, C. Zhang, and N. Li. Machine
learning methods for weather forecasting: A
survey.Atmosphere, 16(1):82, 2025a.
54

Agentic Economies for Autonomous Scientific Discovery
L. Zhang, C. Jiao, B. Li, and C. Xiong. Fairshare
data pricing via data valuation for large lan-
guage models.Advances in Neural Information
Processing Systems, 38:33306–33345, 2026.
S. Zhang, Y. Xu, N. Usuyama, H. Xu, J. Bagga,
R. Tinn, S. Preston, R. Rao, M. Wei, N. Valluri,
et al. Biomedclip: a multimodal biomedical
foundation model pretrained from fifteen mil-
lion scientific image-text pairs.arXiv preprint
arXiv:2303.00915, 2023.
Z. Zhang, S. Chakraborty, A. S. Bedi, E. Mathew,
V. Saravanan, L. Cong, A. Velasquez, S. Lin-
Gibson, M. Blewett, D. Hendrycs, et al. Gen-
erative ai for biosciences: Emerging threats
and roadmap to biosecurity.arXiv preprint
arXiv:2510.15975, 2025b.
C. Zhao, S. Zhao, M. Zhao, Z. Chen, C.-Z. Gao,
H. Li, and Y.-a. Tan. Secure multi-party com-
putation: theory, practice and applications.In-
formation Sciences, 476:357–372, 2019.
M.Zhao, J.Dong, K.Xu, Z.Hasan, C.Fan, S.Jiang,
S. Mao, Y. Ling, L. Zou, T. Zhou, Y. H. Chan,
W. Zhang, Z. Zhou, G. Huang, H. Li, W. Cun,
Z. Chen, M. Yuan, and Y. Geng. Scienceflow:
A long-horizon agent for ml research, scientific
discovery and beyond, 2026. URLhttps://
arxiv.org/abs/2608.14354.
J.Zhu, R.Hou, X.Wang, W.Wang, J.Cao, B.Zhao,
Z. Wang, Y. Zhang, J. Ying, L. Zhang, et al. En-
abling rack-scale confidential computing using
heterogeneous trusted execution environment.
In2020 IEEE Symposium on Security and Pri-
vacy (SP), pages 1450–1465. IEEE, 2020.
M. Zhu, Q. Xie, Y. Weng, J. Wu, Z. Lin, L. Yang,
and Y. Zhang. Ai scientists fail without strong
implementation capability.arXiv preprint
arXiv:2506.01372, 2025.
55
