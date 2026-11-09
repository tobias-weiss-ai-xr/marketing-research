---
title: Power Couple? AI Growth and Renewable Energy Investment
url: https://arxiv.org/abs/2603.26678
category: digital-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Luyi Gui
- Tinglong Dai
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.26678
pages: 55
chars: 175153
fetched_at: '2026-11-08T13:11:18+00:00'
kb_version: 1
---

# Power Couple? AI Growth and Renewable Energy Investment

Power Couple? AI Growth and Renewable Energy Investment
Luyi Gui∗ Tinglong Dai†
∗Paul Merage School of Business, University of California, Irvine; Irvine, California 92697, email:luyig@uci.edu
†Carey Business School, Johns Hopkins University, Baltimore, Maryland 21202; Data Science and AI Institute, Johns Hopkins
University, Baltimore, Maryland 21218, email:dai@jhu.edu
Abstract.Artificial intelligence (AI) and renewable energy are increasingly being described as a “power
couple,” based on the idea that rapid growth in AI will spur clean-energy investment. Yet growing AI
demand could also deepen reliance on fossil power. We study when each outcome arises in a game in which
renewable-capacity investment and AI scaling interact. The key is how the market value of greater AI
capability grows relative to the energy needed to achieve it. When value grows at least as fast as energy use
(market-led scaling), the developer pushes toward frontier capability even when additional electricity comes
from fossil sources. Renewable investment can then enable further AI growth without eliminating fossil
use. As climate damages increase, AI becomes more valuable for adaptation, strengthening incentives to
sustain frontier capability despite the associated emissions. We call this the “adaptation trap. ” When energy
requirements grow faster than capability value (resource-led scaling), energy costs place greater limits on AI
expansion. Renewable investment then makes additional capability less costly while also reducing emissions.
As climate damages rise, the growing value of AI for adaptation can justify enough clean-capacity expansion
to support AI entirely with renewable power. We call this the “adaptation pathway. ” A calibrated case
study shows that both mechanisms can arise at empirically plausible magnitudes. The results suggest that
decarbonizing AI requires renewable capacity to keep pace with the growth of compute demand.
Key words:artificial intelligence, renewable energy, scaling law, sustainable operations
1. Introduction
Over the past few years, artificial intelligence (AI) has emerged as both a significant climate challenge
anda promising climate solution. Frontier training and large-scale inference consume substantial elec-
tricity: data centers consumed about 415 TWh of electricity in 2024, roughly 1.5% of the global total,
and their consumption is projected to more than double by 2030 (International Energy Agency 2025);
training a single state-of-the-art model can require energy comparable to that used by thousands
of households in a year (International Energy Agency 2025). At the same time, AI is increasingly
deployed to support climate action: optimizing grids for renewable integration, improving weather
and climate forecasts, and strengthening disaster response and other adaptation efforts (Choi et al.
2024; Rolnick et al. 2019; Stauffer 2025). This dual role has sharpened industry and policy debate
over AI’s net implications for climate change.
1
arXiv:2603.26678v3  [cs.CY]  20 Aug 2026

2Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
It is generally agreed that the climate impact of AI hinges onhowits energy demand is met: AI
will exacerbate climate change if powered primarily by fossil fuels, but can be a solution if powered
by carbon-free renewable energy. Today, fossil power (natural gas and coal) still supplies most of
the energy used by data centers worldwide (International Energy Agency 2025). As such, the latter
scenario has been strongly advocated: the United Nations recently urged AI developers to run data
centers on 100% renewable energy by 2030 (Volcovici 2025). Understanding how the energy mix
powering AI will evolve, and whether this “100% renewable by 2030” vision can be achieved, remains
an open question. Prevailing views fall into two camps.
A first view frames AI’s energy footprint as a capacity problem: renewables are scaling, so most
incremental data-center load will likely be met by new renewable supply. The International Energy
Agency projects that renewables will meet about half of the growth in data-center electricity demand,
with natural gas and coal supplying much of the remainder, and the split varying substantially across
scenarios (International Energy Agency 2025). Some go further, arguing that AI-driven demand
could itself accelerate clean investment and hasten substitution away from fossil generation (Fransoo
et al. 2026; Morgan and Partridge 2025), a view echoed in the emerging “power couple” framing
of AI growth and renewable investment (Al-Zu’bi 2025; Engel et al. 2025; Rozite et al. 2023). The
underlying logic is that renewables’ widening cost advantage makes clean procurement increasingly
attractive (International Renewable Energy Agency 2025), and AI-enabled grid optimization can
ease integration frictions (Greene-Dewasmes 2025). In this account, emissions hinge on the pace of
clean-capacity deployment.
A second view warns the opposite: rapid growth in data-center demand canentrenchfossil gen-
eration. Because many data centers are concentrated in regions with carbon-intensive grids, utilities
facing abrupt load increases often meet reliability needs by running existing coal and gas plants harder
and postponing planned retirements (Ya˜ nez-Barnuevo 2025). Industry reporting also documents cases
in which utilities repower shuttered fossil assets (Levy 2025) or commission new gas-fired capacity
specifically to serve data-center loads (Ramanan 2025). In this account, clean-capacity expansion
alone is not enough to reduce emissions. Instead, if clean capacity does not scale sufficiently in step
with compute, AI growth can create a carbonlock-inthat slows the renewable transition.
Reconciling these views is difficult because AI development and the energy transition coevolve
(Cohen et al. 2026; Netessine and Shunko 2026). Notably, the pace of the energy transition influences
economic incentives for AI development, while AI itself can drive or impede that transition through
its substantial power demand and potential grid impacts. Capturing this interplay and analyzing the
resulting equilibrium are essential to understanding how AI and energy shape each other. Existing
analyses typically treat developments in the AI and energy sectors independently, focusing on one
side (e.g., AI innovation or clean-energy investment) while holding the other side exogenous.

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment3
This paper offers an initial step toward filling that gap. We develop a model in which renewable
capacity and AI capability are set by separate actors whose choices feed back on each other: clean-
energy availability affects the cost of scaling AI, and the resulting scale changes the economic and
environmental value of additional clean capacity. To capture this interaction tractably, the baseline
model puts a welfare-maximizing policymaker on the clean-energy side and a profit-maximizing
developer on the AI side that selects a capability level (for instance, a frontier, computation-intensive
AI versus a more modest, utility-grade AI). The policymaker’s capacity choice stands in for the
policy and investment machinery that determines clean-energy availability; an extension explicitly
introduces a utility that responds to policy incentives.
Our model captures three features of the AI context. First, the compute and energy a given
capability requires depend on the prevailing scaling regime, which shapes how much renewable
investment lowers operating costs. Across regimes, the capability–compute relationship can be close
to proportional over the relevant range or exhibit sharply diminishing marginal gains from additional
compute. We capture this variation through a scaling parameter.
Second, AI markets can exhibit supermodular returns to capability: incremental breakthroughs
unlock new uses and generate disproportionately large value. As the technology matures and
key applications saturate, these returns may become submodular. We represent these differences
through the elasticity of willingness-to-pay. That elasticity sets how sharply returns curve, but that
curvature alone does not determine whether capability reaches frontier scale; what matters is how
fast willingness-to-pay rises relative to the energy needed to raise capability.
Third, the model allows AI to generate climate-relatedbenefits, particularly through adaptation
and resilience.1 Accordingly, we capture a potential trade-off: although capability is energy-intensive,
its social value could rise with climate damage because it also aids climate adaptation, even as its
energy use can worsen that damage.
Solving the model reveals two distinct ways in which AI growth can interact with the energy
transition. When the market value of capability grows at least as fast as its energy requirements,
as may be true near today’s frontier, developers have strong incentives to pursue frontier capability
even when doing so requires fossil power. Renewable investment can therefore support further AI
growth without fully displacing fossil generation. This creates an “adaptation trap”: as climate dam-
ages worsen, AI becomes more valuable for adaptation, strengthening incentives to sustain frontier
capability even while some of its electricity continues to come from fossil sources. The equilibrium
combines high AI capability with persistent emissions.
1AI may also help reduce emissions (mitigation), for example, by facilitating renewable integration or optimizing
energy efficiency (Choi et al. 2024). However, such effects are more uncertain (due to potential rebound effects)
and slower to materialize, whereas adaptation benefits are more immediate and observable in practice. We focus on
adaptation benefits as the primary social value of AI in the climate context.

4Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
When the market value of capability grows more slowly than its energy requirements, developers
become more sensitive to energy costs. Expanding renewable capacity can then lower the cost of
additional AI capability while reducing the emissions associated with it. As climate damages worsen
and AI becomes more valuable for adaptation, the policymaker has a stronger incentive to expand
clean capacity. Beyond a threshold, renewable capacity can grow enough to meet the full electricity
needs of AI development. We call this an “adaptation pathway”: greater climate stress encourages
clean-energy investment, which in turn supports further AI development without additional fossil
emissions.
We complement these analytical results with a calibrated case study that captures observed dif-
ferences in electricity markets, renewable costs, and AI demand growth. The numerical examples
show that both the adaptation trap and the adaptation pathway arise under empirically plausible
conditions. They also show that powering AI entirely with renewable energy may remain difficult in
some settings unless the cost of expanding renewable capacity falls substantially and climate policy
remains sufficiently strong.
We also examine two extensions. First, AI may itself lower renewable-energy costs, for example by
improving grid integration or accelerating innovation. Such cost reductions can have an unexpected
effect: unless they are large enough to support full decarbonization, they can make frontier AI more
attractive while leaving some fossil use in place, thereby worsening the adaptation trap. Second, com-
petition among AI developers can promote cleaner development when market potential is moderate.
Competition reduces profit margins, making firms more sensitive to energy costs and increasing their
incentives to use renewable power, which in turn encourages renewable investment. When market
potential is sufficiently strong, however, margins remain large enough to sustain frontier scaling with
fossil power, and both developers can fall into the adaptation trap.
The remainder of the paper is organized as follows. Section 2 discusses related literature. Section 3
introduces the modeling framework. Sections 4 and 5 analyze the AI developer’s and policymaker’s
decisions, respectively, deriving the main equilibrium results. Section 6 presents the case study, and
Section 7 considers the extensions. Section 8 concludes with implications for policy and for future
research on the AI–climate nexus.
2. Literature
The AI boom has made electricity a binding constraint on innovation, so energy policy increasingly
functions as technology policy. Understanding the interaction between AI and energy means studying
technological change, clean-capacity investment, and climate damages together. We organize the
related work around three streams.

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment5
2.1. Environmental Policy and Technology Innovation
First, our paper relates to work on directed innovation and carbon lock-in. In the directed technical
change tradition, policy shifts private returns to steer invention; in a canonical model, Acemoglu
et al. (2012) show that well-designed climate policy can redirect innovation toward clean technologies
and sustain the transition even after policy is relaxed. Empirically, higher energy prices and taxes
reallocate inventive activity toward cleaner technologies (Aghion et al. 2016; Popp 2002). A parallel
tradition considers why cost-effective energy-saving technologies often diffuse slowly, the so-called
“energy paradox,” and traces it to a combination of pollution and innovation-and-adoption market
failures (Jaffe and Stavins 1994; Jaffe et al. 2005), whereas a long-running debate considers whether
well-designed environmental regulation can itself stimulate offsetting innovation (Porter and van der
Linde 1995). Complementary operations management work makes the policy–diffusion margin
explicit at the firm and market level, from early models of green design responses to environmental
requirements (Chen 2001) to more recent analyses of how subsidy design, strategic supply, and
regulatory uncertainty shape adoption and investment (Chemama et al. 2019; Cohen et al. 2016;
Wang et al. 2021). We share this literature’s interest in how environmental policy shapes technology,
but the policy margin differs. Rather than steering invention between clean and dirty alternatives,
clean-energy investment here sets the scale at which a developer deploys a single energy-intensive,
adaptation-providing technology, and that equilibrium scale is what we study.
The lock-in literature starts from a different diagnosis. Increasing returns, network effects, and
institutional complementarity can entrench an inferior regime long after superior alternatives exist
(Arthur 1989). In energy systems, carbon-intensive technologies are embedded in a dense web of
infrastructure, regulation, skills, and sunk investments that together form a techno-institutional
complex resistant to change (Unruh 2000, 2002). These perspectives raise a central question for
the AI context: if policy can redirect innovation, why does carbon lock-in remain durable, and if
lock-in dominates, why do transitions occur at all? We address this question by modeling the joint
determination of the innovation margin and the capacity margin and showing that lock-in can arise
endogenously from the equilibrium interaction between private scaling incentives and public clean-
capacity choices under certain conditions. Counterintuitive incentive effects of this kind recur in the
economics of AI deployment more broadly: more reliable AI, for instance, can paradoxically make
it costlier to sustain human oversight (Bastani and Cachon 2025), and the most capable machine
need not be the one a firm should deploy once it must also motivate human effort (Guan et al.
2025); relatedly, when a human will only partially follow algorithmic advice, the best recommendation
departs from the best decision (Grand-Cl´ ement and Pauphilet 2026).

6Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
2.2. Clean Capacity Investment and Carbon Footprint of AI
Second, a literature in operations and energy economics studies clean-capacity investment under
uncertainty, accounting for intermittency and valuing operational flexibility, to meet load at accept-
able cost and reliability. Much of this work treats demand as given, or as responding to prices through
reduced-form elasticities and demand-response programs. Recent contributions endogenize strategic
behavior on the supply side: Aflaki and Netessine (2017) analyze renewable investment under inter-
mittency and strategic behavior, and Kok et al. (2020) show how operational flexibility reshapes
the optimal mix of renewable and conventional generation. Related work studies joint choices over
renewables, storage, and load control under tight resource constraints, yielding micro-foundations
for data-center and “behind-the-meter” procurement and showing how clean investment depends
on operational substitutability across these margins (Kaps et al. 2023). Closest to our two-source
energy abstraction, Peng et al. (2024) study joint operations and investment across renewable, flexi-
ble (natural-gas), and storage capacities and characterize when these resources act as substitutes or
complements. A closely related strand emphasizes contracting and market design: Gao et al. (2025)
analyze renewable power purchase agreements (PPAs) and show how contract structure and tim-
ing affect green-capacity expansion, whereas work on corporate renewable targets highlights how
commitment mechanisms and investment timing interact with uncertainty (Sunar and Birge 2019;
Trivella et al. 2023). At the decentralized margin, Gao et al. (2024) show that aggregating distributed
energy resources can improve efficiency while also creating market power concerns, and operational
constraints such as curtailment imply that installed capacity need not translate one-for-one into clean
output (Wu and Kapuscinski 2013). We differ from this stream in what is treated as endogenous:
it optimizes a supply portfolio against given or price-responsive demand, whereas we make AI load
endogenous to clean-energy availability; investment in clean capacity changes the economics of AI
scaling, which in turn changes equilibrium electricity demand.
In parallel, an emerging literature quantifies the energy use and carbon footprint of the digital econ-
omy, especially large-scale AI. Strubell et al. (2019) highlight that frontier model development can be
energy-intensive, motivating emissions accounting and efficiency efforts. Policy and industry analyses
warn that data-center electricity demand could grow rapidly with AI workloads (Greene-Dewasmes
2025; Ya˜ nez-Barnuevo 2025) and document local grid stress from clustered data-center expansion
(Ramanan 2025). Firms have responded with decarbonization commitments and record corporate
renewable procurement (BloombergNEF 2024; Google 2020; Microsoft 2020). A common limitation
is that these analyses rarely model how developers adjust capability, and thus compute intensity,
when energy becomes cheaper or cleaner. Capacity-planning and procurement models provide detail
on supply, contracts, and market design but typically treat demand as technologically passive; the
AI-footprint literature treats compute growth as an outcome rather than a strategic choice. Neither

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment7
captures that clean-capacity investment can raise equilibrium compute demand by lowering the effec-
tive marginal cost of electricity, creating scope for rebound-type effects (Gillingham et al. 2016). We
model this feedback explicitly by endogenizing both clean-capacity investment and AI scaling.
2.3. Adaptation and Mitigation
Third, a climate-policy literature examines whether adaptation can expand without weakening miti-
gation. In the benchmark framing, adaptation and mitigation are substitutes, so cheaper adaptation
lowers the marginal benefit of abatement. Integrated assessment work that incorporates adaptation
formalizes this channel and shows how the timing of adaptation shapes optimal mitigation (de Bruin
et al. 2009), with related arguments in surveys emphasizing uncertainty and learning (Ingham et al.
2007). At the same time, syntheses stress that climate policy is a portfolio problem: adaptation is
unavoidable in the near term, but without mitigation, warming can outstrip adaptive capacity (Klein
et al. 2007). This tension underlies concerns about an “adaptation moral hazard. ”
Beyond the benchmark, crowd-out is not inevitable. Adaptation can shift the distribution and
timing of losses and the political constraints on mitigation, allowing complementarity (Ingham et al.
2013). What this debate largely abstracts from is adaptation delivered by a technology with steeply
increasing returns to scale. In particular, AI-based adaptation is compute-intensive and scalable, with
complementarities between capability and deployment; with supermodular returns, small advantages
compound, and scale races become self-reinforcing (Bulow et al. 1985; Parker and Van Alstyne 2005).
In AI markets specifically, a data feedback loop known as the “AI flywheel,” in which wider adop-
tion generates more data that further improves capability, reinforces these dynamics (Gurkan and
de V´ ericourt 2022). Embedding this scaling logic into the adaptation–mitigation problem changes the
relevant margin: worsening climate damages can raise the return to capability, translating adaptation
demand into faster compute growth and, unless marginal electricity is carbon-free, higher emissions.
Our model formalizes this interaction and shows that when a technology with steeply increasing
returns delivers adaptation, how its energy interface is governed shapes whether adaptation and
mitigation are complementary or in tension.
3. Model
We develop a parsimonious model that isolates the core incentives linking AI development and
renewable investment. The model endogenizes both AI scale and the clean capacity available to
support it; for tractability, we represent their interaction as a sequential game. In a single planning
period, two actors move sequentially. A welfare-maximizing policymaker chooses renewable capacity
yintended to power AI development. A profit-maximizing AI developer then chooses an AI capability
levelx∈[0,1].

8Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
The capacityyshould be read as “dedicated” clean supply available to the developer, for example,
via long-term power purchase agreements (PPAs) or on-site generation, rather than undifferentiated
grid supply. This focus matches how AI developers often secure clean electricity and clarifies the
margin at which policy and corporate procurement interact.
3.1. Capability, Energy Demand, and Emissions
We consider a single period, a technological phase in which a prevailing paradigm governs the mapping
from compute to capability. For example, in one phase, pretraining scale drives progress: larger
datasets, more parameters, more training compute. In another, incremental compute is shifted toward
inference (“test-time” scaling). The one-period structure provides a tractable way to study how the
equilibrium between clean capacity and AI capability depends on the economics of scaling within a
phase.
Within the phase, the developer chooses an AI capability levelxthat indexes performance along
the scaling frontier. We normalize the maximum attainable performance in the phase to 1, reflecting
that improvements eventually plateau. The developer choosesx∈[0,1] to maximize profits, trading
off market value against costs.
Compute is energy-intensive. Motivated by empirical “scaling laws” that relate model performance
to training compute through approximate power laws (Hestness et al. 2017; Hoffmann et al. 2022;
Kaplan et al. 2020), we assume that achieving capabilityxrequires compute equal tox 1+α, where
α≥0 governs how rapidly compute requirements rise with performance. If each unit of compute
consumeskunits of energy, the developer’s energy demand iskx 1+α.
Developers procure electricity from the grid and from dedicated renewables (PPAs or on-site gen-
eration).2 In practice, grids are mixed and remain dominated by fossil generation. In the United
States, natural gas and coal together supply roughly three-fifths of electricity generation (U.S. Energy
Information Administration 2025b); in China, coal generates the majority of electricity (U.S. Energy
Information Administration 2025a). Renewable PPAs, by contrast, match most energy demand with
renewable generation under varying matching requirements. In the model, we abstract the two sources
as “fossil” and “renewable” to contrast carbon-intensive and carbon-free supply.
The developer incurs unit costs ofc f andc r for energy from the fossil and renewable sources,
respectively. In the main model, we interpret these parameters as unit generation costs, as in cases
in which developers use on-site energy production. Developers procuring electricity from energy
operators through PPAs or from utilities at prevailing electricity tariffs likely pay more than the
2In practice, developers’ alternative to grid power is likely a portfolio of energy resources, including dedicated
renewable generation, efficient natural-gas technologies such as on-site combined cooling, heat, and power systems,
and energy storage. We abstract from this mix and focus on the key economic and environmental attributes it typically
delivers: lower generation costs and emissions than grid power, but at the expense of substantial upfront investment.

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment9
underlying generation costs. The margins accrue to the energy operators or utilities and drive the
strategic behavior of these entities. We abstract from this strategic layer and focus on the underlying
generation cost in the main model. We refer readers to Section EC.2.1 for an extended model that
explicitly incorporates a utility, its strategic decision, and the associated cash flows.
We takecr<cf to reflect the general cost advantage of renewable sources in energy generation. For
the time period considered, we treat renewables as capacity-constrained, whereas fossil generation
can be ramped to cover residual demand. This captures the practical asymmetry that clean expansion
requires lead time (siting, interconnection, transmission, storage), whereas fossil capacity in the grid
can respond relatively quickly to load growth, including from data centers (Ramanan 2025; Ya˜ nez-
Barnuevo 2025). For example, in Virginia, which has the world’s highest concentration of data centers,
utilities have pursued aggressive generation and transmission expansion plans, including substantial
fossil capacity additions, to keep pace with AI demand growth. 3
Becausec r<cf, a profit-maximizing developer uses all available renewables first and relies on fossil
energy only for demand above renewable capacity. Accordingly, given the developer’s capability choice
xand the renewable capacityy, 4 the share of the developer’s energy demand met by renewables is
β(x,y) = min
{ y
kx1+α,1
}
.(1)
Ifkx 1+α≤y, renewables cover all energy use andβ(x,y) = 1; otherwise,β(x,y)<1.
A more rigorous formulation of eq. (1) would replace renewable capacityyin the numerator
with the quantity of renewable energy that can be effectively deployed to satisfy the developer’s
electricity demand. The distinction matters because leading renewable sources, including solar and
wind, are intermittent: the same nameplate capacity may yield different levels of usable renewable
electricity depending on natural conditions and the effectiveness of firming measures, such as energy
storage and data centers’ ability to shift or flexibly schedule workloads. Section EC.2.2 examines this
refinement explicitly: the developer’s problem retains its structure under intermittent availability,
whereas both scaling regimes tilt toward more carbon-intensive outcomes.
Market willingness-to-pay for capabilityxisθx λ, whereθ>0 denotes the valuation at the capability
frontier,x= 1, andλ>0 governs the elasticity of value with respect to capability. Whenλ>1, private
returns to capability are convex: incremental improvements can unlock new tasks and markets, so
valuation rises more than proportionally withx. When 0<λ<1, by contrast, marginal gains become
progressively less valuable. The monopoly benchmark can therefore be interpreted as a reduced-form
3We acknowledge that grid capacity is constrained in practice. However, such constraints are typically reflected
in interconnection queues for new data centers. Once connected, data centers generally rely on the utility’s obligation
to serve, under which residual demand is met through grid power.
4The model can be extended to include an existing renewable capacity levely 0 in addition to the investmenty;
all results remain robust.

10Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
representation of a regime with concentrated rents and strong incentives to race toward the frontier;
Section 7.2 relaxes this assumption by introducing competition.
Achieving a given capability entails multiple cost components (hardware, facilities, labor, and
energy). We assume energy sources differ only in their unit energy cost, normalizing other costs away.5
Equivalently,cr andc f are all-in unit compute costs under renewable versus fossil-based power.
The developer’s profit is
Π(x,y) =θx λ− ( β(x,y)cr + ( 1−β(x,y) ) cf ) kx 1+α.(2)
The optimal capability choice conditional onyisx ∗(y) .= arg maxx∈[0,1] Π(x,y).
3.2. Renewable Capacity and the Policy Objective
In practice, decisions regarding renewable-capacity investment are distributed across governments,
utilities, and private firms, including AI companies themselves. Nevertheless, public policy heav-
ily shapes investment outcomes. Governments can directly invest in clean generation, transmission,
and storage infrastructure; utility investments in renewable projects are often subject to regulatory
approval and procurement requirements such as Renewable Portfolio Standards; technology compa-
nies’ investments in clean firm power can be facilitated by policies such as Clean Transition Tariffs;
and third-party renewable developers frequently rely on financial incentives, including tax credits
and investment subsidies.
Collectively, these mechanisms imply a mapping from policy choices to renewable investment out-
comes. We therefore interpretyas the clean capacity made available to AI through this broader
investment and policy environment. The baseline model collapses these institutions into a welfare-
maximizing actor that directly choosesy; this collapse isolates the feedback between clean-energy
availability and AI scaling. This single-instrument abstraction allows us to focus on the fundamental
interaction between policy-induced clean-energy investment and market-driven AI demand growth,
suppressing implementation frictions that may arise in translating policy instruments into realized
investment outcomes. We formalize the policy-to-investment process in Section EC.2.1.
The relevant decision variable is the period-specific capacityythat is available to power the phase
of AI development under study. Although much energy infrastructure is long-lived, climate and
industrial policy are frequently revised, and AI itself is a salient driver of such revisions. The one-
period formulation can therefore be understood as capturing an investment decision within a phase,
and examining the clean-capacity response to prospective AI load within a given scaling regime.
5In practice, the energy source can affect operations (e.g., workload shifting). We abstract from these operational
margins to focus on investment and scaling incentives. A common capability-dependent non-energy cost would shift
the developer’s activation thresholds by raising the effective unit cost of compute, but it enters both energy branches
symmetrically and leaves the regime comparison betweenλand 1 +αunchanged.

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment11
A central policy concern is emissions from fossil-powered compute and the resulting climate dam-
ages. Letd 0≥0 denote the baseline emissions stock in the period considered, absent AI. This can
be interpreted as the atmospheric carbon stock above a given climate stability threshold. Lete f>0
be the carbon emissions per unit of fossil-generated electricity, and treat renewables as zero-carbon.
Given (x,y), emissions attributable to AI development are
E(x,y) =e f
(
1−β(x,y)
)
kx 1+α,(3)
so total emissions ared 0 +E(x,y). Bothd 0 andEare measured in the same unit (e.g., million metric
tons of CO 2e).
At the same time, higher AI capability can reduce the realized damages from a given emissions stock
by improving forecasting, preparedness, and other adaptation services. We capture this adaptation
channel through a reduced-form formulation in which capabilityxscales down climate damages by
a factor 1−bx, whereb∈(0,1) measures the effectiveness of AI-enabled adaptation. The resulting
climate-damage term is
D(x,y) = (1−bx)
(
d0 +E(x,y)
)
.(4)
Expanding renewable capacity is costly and increasingly so at the margin: prime sites are developed
first, and further scale requires transmission, interconnection, and balancing resources. We therefore
model investment cost as an increasing, convex functionV(y) withV(0) = 0. In an extension, we
allowVto depend on capability,V(x,y), to capture the possibility that higher AI capability lowers
the effective cost of integrating renewables, for example, through improved grid management and
planning (see Section 7.1).
The policymaker choosesyto maximize social welfare, anticipating the developer’s best response
x∗(y). Welfare includes economic surplus generated by AI (which may exceed the developer’s private
profit when there are spillovers), subtracts climate damages net of adaptation benefits, and subtracts
the investment cost of renewable capacity. A compact representation is
W(y) =ηΠ
(
x∗(y),y )
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
economic surplus
−ξD
(
x∗(y),y )
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
climate damages net of adaptation
−V(y) /bracehtipupleft/bracehtipdownright/bracehtipdownleft/bracehtipupright
renewable-investment cost
,(5)
whereη>1 captures spillovers from AI profitability to broader economic value creation andξ>0
scales the policymaker’s weight on climate damages relative to economic surplus.
It is without loss of generality to restrict the policy choice toy∈[0,k] so that dedicated renewable
energy does not exceed the maximum demandk. The optimal renewable capacity is
y∗ .= arg max
y∈[0,k]
W(y).(6)

12Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
4. Developer Capability Choice
We solve by backward induction, starting from the AI developer’s best response to renewable capacity
y. The developer chooses capabilityx∈[0,1] to maximize profits, trading off market valueθx λ against
the energy cost of supplyingkx 1+α units of electricity at an endogenous unit price determined by
the clean shareβ(x,y). A key force is how willingness-to-pay scales with capability relative to how
energy requirements scale, captured byλversus 1 +α. Intuitively, whenλ≥1 +α, returns keep pace
with energy needs, and the developer prefers higher capability; whenλ<1 +α, energy costs become
increasingly binding at highx.
We begin withλ≥1 +α, an environment in which the marginal private payoff from capability
does not taper faster than the marginal energy requirement. This aligns with convex valuations in
frontier markets and scaling regimes in which additional compute remains effective. We refer to this as
market-led scaling. When multiple capability choices yield the same profit, we assume the developer
selects the largerx.
Proposition 1.In the market-led scaling scenario in whichλ≥1 +α, there exist two thresholds
y1≤y 2 such that for any giveny∈[0,k], the optimal AI capability choicex ∗ equals
x∗(y) =



0∀y<y 1
(y
k
) 1 1+α ∀y∈[y 1,y 2)
1∀y≥y 2
(7)
Accordingly, the emissions from AI developmentE(x ∗(y),y) = 0ify<y 2. Otherwise,E(x ∗(y),y)>0
unlessy=k.
Proof.All proofs of results stated in the main text are relegated to Section EC.4.
Proposition 1 shows that the link between renewable capacity and fossil reliance can be discon-
tinuous. The developer’s best response has three regions. Wheny <y 1, the developer is inactive
(x∗(y) = 0): even modest capability would require enough fossil power that energy costs dominate
market value.
Wheny∈[y 1,y 2), the developer produces a positive-capability model but stays fully within renew-
ables. In particular,
x∗(y) =
(y
k
) 1 1+α
exactly exhausts clean capacity and yieldsE(x ∗(y),y) = 0. Renewables bind, so capability tracks the
clean-energy constraint exactly. We call this interval the “coupling zone. ”
Onceycrossesy 2, the developer jumps to the frontier choicex ∗(y) = 1. Unlessy≥k, residual
demand is met by fossil generation, and emissions become strictly positive. Thus, additional renew-
ables can shift the equilibrium from a clean, capacity-constrained regime to a frontier regime in which
fossil power is used at the margin.

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment13
The mechanism is straightforward. Underλ≥1 +α, the marginal market payoff from capability
remains large relative to the implied increase in energy requirements, so the developer is drawn
towardx= 1. Whenyis small, reaching high capability entails payingc f on a large fossil share, which
deters development or keeps it tightly constrained by clean capacity. Asyrises, the developer can
scale while remaining carbon-free. Beyondy 2, the remaining fossil cost atx= 1 is no longer decisive,
and the developer absorbs it rather than forgo frontier capability. Fory≥y 2, capability no longer
depends on renewable availability; we refer to this region as the “decoupling zone. ”
We next consider the case in which compute requirements rise faster than willingness-to-pay as
capability increases, that is,λ<1 +α. We refer to this as theresource-led scalingscenario. Define
f(c) .=
( θλ
(α+ 1)ck
) 1 1+α−λ
,
which is decreasing inc.
Proposition 2.In the resource-led scaling scenario in whichλ<1 +α, for anyy∈[0,k], the
optimal capability choice is
x∗(y) =



min{f(cf),1},ify<kf(c f)1+α,
(y
k
) 1 1+α,ify∈ [ kf(c f)1+α,kf(c r)1+α) ,
min{f(cr),1},ify≥kf(c r)1+α.
(8)
Accordingly,E(x∗(y),y) = 0fory≥kf(c f)1+α; otherwise,E(x ∗(y),y)>0unlessy=k.
Proposition 2 implies a different pattern from the market-led case. Capability remains nondecreas-
ing iny, but the best response is typically interior and varies continuously: whenλ<1 +α, the
marginal energy requirement grows faster than the marginal market payoff, so the developer becomes
increasingly sensitive to the unit energy price at highx. Expanding renewables therefore mainly
works by lowering the effective cost of capability, inducing smooth adjustments inxrather than a
jump to the frontier.
The emissions implications also reverse. For lowy, the developer behaves as if facing the fossil cost
cf and choosesx ∗(y) = min{f(cf),1}, which is independent ofyand generally entails fossil use, a
decoupling zone. Onceyreacheskf(c f)1+α, renewables suffice to support the developer’s preferred
scale without fossil generation, so emissions fall to zero. Over the intermediate range, higherylowers
the effective unit cost towardc r and can raise capability on a carbon-free basis; for sufficiently large
y, the unit cost is pinned down byc r, andx ∗(y) again becomes independent ofy.
In sum, the response to clean capacity depends on whether scaling is market-led (λ≥1 +α) or
resource-led (λ<1 +α). In the former, higherycan unlock frontier capability with residual fossil use
at the margin; in the latter, higheryprimarily substitutes renewables for fossil supply and supports
interior capability choices. The next section shows how this distinction shapes the policymaker’s
renewable investment decision.

14Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
5. Renewable Capacity in Equilibrium
Policy and industry discussions increasingly call for powering frontier AI with carbon-free electricity,
often presuming that renewable expansion will naturally follow AI’s rising load (Volcovici 2025).
However, whether this is true and whether it delivers decarbonization depend on strategic responses.
In our framework, renewable capacityyaffects welfare through two margins: it raises the clean
shareβ(x,y) at a given capability level, and it shifts equilibrium capability through the developer’s
best responsex ∗(y) (characterized in Section 4). These two margins correspond to acomposition
effect and ascaleeffect: holdingxfixed, higherydisplaces fossil generation, but higherycan also
increase total energy demand by raisingx∗(y). The policymaker choosesyanticipatingx ∗(y), and the
relevant outcome is the induced equilibrium pair (x∗(y∗),y∗) and its implied emissions and damages.
Accordingly, whether clean investment reduces emissions or instead accelerates them depends on
which effect dominates in equilibrium and, ultimately, on the prevailing AI scaling regime. We analyze
these effects in this section.
5.1. Market-Led Scaling: The Adaptation Trap
We begin with market-led scaling,λ≥1 +α, in which willingness-to-pay rises at least as fast
as energy requirements as capability increases. As Proposition 1 illustrates, in this regime, clean
capacity plays an enabling role and can move the developer’s capability choice to the frontier
even when full decarbonization is not achieved. We show that such a decoupling between frontier
capability and full decarbonization can arise at the optimal level of renewable investment.
Proposition 3.In the market-led scaling scenario in whichλ≥1 +α, at the equilibrium renew-
able capacityy ∗,
(i) if either (a)θ≤max{ 1+α λ ·cfk,crk}, or (b)V ′(k)≤η(c f−cr)+(1−b)e fξ, thenE(x ∗(y∗),y∗) = 0
holds∀d 0≥0;
(ii) otherwise, there exists a threshold ¯dm such thatE(x ∗(y∗),y∗)>0if and only ifd 0≥ ¯dm. Fur-
thermore,y∗ remains unchanged∀d 0≥ ¯dm.
Part (i) describes two cases in which the equilibrium is carbon-free even under market-led scaling.
Under (a), frontier capability is not sufficiently valuable, relative to energy costs, to justify the discrete
jump tox= 1 in Proposition 1. The developer instead chooses an interior capability level that can
be served by renewables, or remains inactive, soE(x ∗(y∗),y∗) = 0. Under (b), full decarbonization
is socially efficient: the marginal cost of expanding clean capacity tokis below its marginal benefit,
which combines the private cost savingη(c f−c r) with avoided climate damages (1−b)e fξ. The
policymaker therefore setsy ∗ =k, delivering frontier capability on carbon-free power.
Part (ii) characterizes the remaining region, in which frontier incentives are strong and the last units
of clean capacity are expensive. Here climate deterioration can tilt the equilibrium toward carbon-
intensive AI. Because damages take the form (1−bx)(d 0 +E(x,y)), a higher baseline emissions stock

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment15
d0 increases the marginal value of capability through adaptation: holding emissions fixed, a higherx
reduces the damage burden more. In the market-led regime, however, onceyis high enough to make
scaling feasible, the developer’s choice is largely pinned down by market incentives, not by marginal
energy costs. Once clean capacity suffices to support frontier scaling, further renewable investment
no longer raises capability; the remaining gain, displacing fossil electricity, may not justify the last
units of capacity. The threshold ¯dm formalizes the trade-off: beyond it, the welfare gain from inducing
frontier capability (the scale effect) is already maximized, whereas the increase in investment cost
outweighs the welfare loss from residual marginal emissions (the composition effect). Consequently,
renewable investment stops short of the decarbonization levely=k, at or moderately above the level
that triggersx ∗(y) = 1.
This logic delivers anadaptation trap. Partial clean investment is attractive because it enables
frontier capability and hence adaptation benefits. But when frontier scaling is powered at the margin
by fossil electricity, equilibrium emissions remain positive, and the worse the baseline, the greater the
value of adaptation and hence the stronger the incentive to keep enabling frontier scaling while tol-
erating residual fossil use. To summarize, carbon intensity persists under market-led scaling because
adaptation benefits from frontier capability (the scale effect) outweigh the benefits of full decar-
bonization (the composition effect).
5.2. Resource-Led Scaling: The Adaptation Pathway
We next consider resource-led scaling,λ<1 +α, in which energy requirements rise faster with capa-
bility than willingness-to-pay. In this regime, the developer’s capability choice becomes increasingly
sensitive to the unit cost of energy. Clean-energy availability therefore has greater influence over AI
scaling: by lowering the marginal cost of electricity serving AI load, it changes the private return to
scaling and can shiftx∗(y), as characterized in Proposition 2. This stronger coupling between energy
costs and capability choice yields a qualitatively different outcome from that under market-led scaling.
Proposition 4.In the resource-led scaling scenario in whichλ<1+α, at the equilibrium renew-
able capacityy ∗,
(i) ifθ≥ 1+α λ ·cfkandV ′(k)>η(c f−cr) + (1−b)efξ, thenE(x ∗(y∗),y∗)>0holds∀d 0≥0;
(ii) otherwise, there exists a threshold ¯dc such thatE(x ∗(y∗),y∗) = 0if and only ifd 0≥ ¯dc.
Part (i) identifies the corner case in which carbon-intensive AI persists: market incentives to scale
remain strong, whereas the marginal cost of fully covering AI load with renewables is high relative to
its benefits. In this region, the policymaker rationally stops short of full decarbonization, and some
of the electricity used by AI continues to come from fossil generation.
Outside this region, climate deterioration can push the equilibrium toward carbon-free AI. The
first step parallels the market-led case: a higher baseline emissions stockd 0 raises the social value of

16Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
adaptation, so the policymaker induces higher capability. The second step is where resource-led scal-
ing changes the conclusion. Because the developer is energy-cost sensitive, higher capability requires
a meaningful reduction in the effective marginal cost of scaling. This potentially aligns the welfare
gains from adaptation (through the scale effect) and mitigation (through the composition effect),
because investing in renewables accomplishes both: it substitutes away from emissions-intensive sup-
ply and lowers the energy cost faced by the developer over the relevant range. As a result, whend 0
is large enough, the policymaker finds it optimal to invest sufficiently in clean capacity so that the
induced increase inx ∗(y) occurs on carbon-free marginal electricity, yieldingE(x ∗(y∗),y∗) = 0. The
threshold ¯dc captures when adaptation value is high enough to justify this shift.
This mechanism yields anadaptation pathway. Under resource-led scaling, worsening climate con-
ditions increase the value of capability, and that increase translates into stronger incentives to expand
clean capacity, because clean capacity is precisely what makes additional capability privately viable.
In this regime, the feedback runs in a decarbonizing direction: climate stress strengthens clean invest-
ment, and clean investment supports capability growth on carbon-free power.
The adaptation pathway mechanism can be undermined by intermittency. Notably, an increase in
nameplate renewable capacity could increase emissions under high output variability when scaling
is not resource-led enough (i.e., when 1 +αis not sufficiently higher thanλ). Consequently, crossing
the threshold ¯dc may shift the equilibrium to a more carbon-intensive region, thereby triggering an
adaptation trap. We refer readers to Section EC.2.2 for details.
5.3. Policy Design Implications
The two regimes yield policy lessons that are difficult to see in analyses that hold either AI scaling or
clean-capacity expansion fixed. In particular, “net-zero AI” is an equilibrium outcome of AI–energy
interactions. The same intervention, expanding renewables, can reduce emissions in one regime and
accelerate fossil-powered scaling in another. Which regime prevails depends on the economics of
AI scaling and market demand; the central policy problem is to ensure that the composition effect
dominates the scale effect at the margin.
Accordingly, “more renewables” is not a sufficient prescription when scaling is market-led. Partial
clean investment may mainly relax a binding compute constraint, accelerating frontier scaling without
ensuring that marginal electricity is carbon-free. Avoiding the adaptation trap therefore requires
either (1) reducing the cost of the last-mile renewable expansion toy=k(through permitting,
interconnection, transmission, storage, and firming) so that condition (b) in Proposition 3(i) is met, or
(2) directly raising the private marginal cost of fossil-powered compute (for example, through carbon
pricing or clean-energy matching requirements) so that condition (a) in Proposition 3(i) is met. In
contrast, when scaling is resource-led, clean capacity is more likely to steer AI toward decarbonization

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment17
because it directly constrains the developer’s capability choice. Intermittency, nevertheless, tilts the
equilibrium toward carbon and makes the adaptation trap more prevalent, and it elevates operational
instruments that firm renewable delivery, including workload flexibility, hourly matching, and storage,
into climate-policy levers.
More generally, whether an emphasis on climate adaptation weakens or strengthens mitigation
depends on the scaling regime. In broader climate-policy debates, the relationship between adaptation
and mitigation is contested, with evidence and theory supporting both substitution and complemen-
tarity, depending on institutions and mechanisms (Remshard 2022). Our results provide a concrete
mechanism that may explain this ambiguity in the AI–energy nexus. In a market-led regime, adap-
tation motives can rationally support an equilibrium with residual fossil marginal power, weakening
mitigation; in a resource-led regime, adaptation motives can instead strengthen the case for clean
capacity, making mitigation and adaptation complements. We also note that both mechanisms hinge
on one fundamental property of adaptation: its benefits, and therefore the social value of capability,
can increase as climate conditions worsen. Our analysis shows that taking into account such inter-
actions can help policymakers understand the implications of adaptation delivered by technologies
with different scaling properties.
6. Calibration and Counterfactuals
We illustrate the model’s quantitative implications using four calibrated numerical instances
(Instances A–D). Each instance parameterizes the model using observed magnitudes for AI invest-
ment, compute intensity, and power-system costs. Instances A–C are informed by conditions in the
United States, China, and the European Union over 2023–2025, respectively. Instance D is a styl-
ized counterfactual designed to complement the first three instances and isolate the mechanisms
underlying the results.
Instances A and B satisfy the market-led conditionλ>1 +αbut differ in market potential (the
level ofθ), capturing market-led growth with strong versus limited market potential. Instance C
satisfiesλ<1 +αwith market potential comparable to that of Instance B, capturing resource-led
growth with limited market potential. Instance D mirrors Instance C except thatθtakes its Instance
A value, producing a resource-led scaling environment with strong market potential. Table 1
summarizes the parameter values for each instance. We briefly describe data sources and calibration
below; readers are referred to Section EC.5 for details.
6.1. Calibration
We start by calibrating the willingness-to-pay functionθx λ. We anchor the market-potential param-
eterθto private investment magnitudes reported in Maslej et al. (2025), adjusted to reflect other

18Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
Table 1 Nominal Parameters Used in the Case Study
Parameter Instance A Instance B Instance C Instance D
Instance-Specific Parameters
θ(Billion USD) 109.08 33.65 19.42 109.08
λ3.46 3.19 1.98 1.98
k(TWh) 325.6 275.32 311.32 311.32
cr (Billion USD/TWh) 0.05 0.048 0.065 0.065
cf (Billion USD/TWh) 0.088 0.151 0.146 0.146
V(y) (Billion USD) 0.049y 1.34 0.029y1.34 0.036y1.34 0.036y1.34
ef (MMTCO2e/TWh) 0.367 0.614 0.187 0.187
ξ(Billion USD/MMTCO 2e) 0.04 0.0135 0.095 0.095
Common Parameters
α1.467
η1.88
b0.15
Notes:Instances A and B represent market-led scaling scenarios; Instances
C and D represent resource-led scaling scenarios. Instances A and D feature
strong market potential; Instances B and C feature limited market potential.
prominent sources of R&D in AI. To estimate the willingness-to-pay elasticityλ, we relate frontier-
model capability, measured by MMMU (Massive Multi-discipline Multimodal Understanding) scores
(Yue et al. 2024), to AI investment across regions over 2023–2025. This yieldsλvalues of 3.46, 3.19,
and 1.98 for the three regions considered, indicating meaningful heterogeneity in how markets reward
marginal capability improvements. We then estimate the economic-spillover parameterηby taking
the ratio of AI’s overall economic value potential (Hatzius et al. 2023) to the profit potential of the
AI sector.
We next calibrate the scaling termx 1+α and the energy-demand scalek. As a simplification, we
assume the major markets share a common scaling exponentαbut allow for regional heterogeneity
in the level of energy intensity throughk. We estimateαby regressing regional data-center electricity
usage (International Energy Agency 2025) on frontier MMMU capability levels (Yue et al. 2024),
obtainingα= 1.467. We then calculatekin each instance based on the corresponding regional
energy-use magnitude.
Finally, we calibrate the energy and climate primitives. We treat PPA-backed renewable access
as the relevant clean procurement margin for AI developers and use data reported by International
Energy Agency (2025) to setc r to the cost of renewable PPAs with 80% hourly matching; we also use
the same source’s reported grid-price ranges to construct a mean–variance cost forc f, our measure
of the (risky) outside option of relying on general grid electricity. Renewable-investment costs take

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment19
the formV(y) =gy 1.34: the exponent is guided by construction-cost patterns across large Chinese
solar projects (Midong, Mengxi Lanhai, Tianwan offshore, and Ordos), whereasgis pinned down by
regional average construction costs (including plant, transmission, and land) adjusted for project lifes-
pans. We estimate the climate-damage weightξbased on the regional carbon prices and set the adap-
tation parameterb= 0.15 based on evidence that AI-enabled hazard mitigation can reduce projected
average losses by up to 15% (Deloitte 2025). Lastly,e f is set to the regional grid emissions intensity.
The estimates above should be read with their epistemic status in view: the case study is a cal-
ibrated illustration rather than measurement. Parameters describing energy demand, energy costs,
emissions intensity, and investment costs are comparatively well measured, but the willingness-to-
pay elasticityλrests on three annual observations from a rapidly evolving market per region, and
the associated confidence intervals are wide enough that no regional regime classification is statis-
tically firm; alternative willingness-to-pay estimators can reverse the China and EU classifications,
although the U.S. classification is robust across estimators (see Section EC.5.1). Accordingly, the four
instances are best read as scenarios that span the two scaling regimes while remaining anchored to
each region’s observable magnitudes. Because the design covers both regimes, reclassifying a region
relocates it to an instance that is already analyzed; none of the qualitative conclusions rests on any
single region’s label. Section EC.5.1 reports the uncertainty quantification, an estimator comparison,
and a measurement agenda.
6.2. Equilibrium Outcomes
We solve for equilibrium renewable investment and AI capability choices for the four instances in
Section 6.1. Figure 1 summarizes the outcomes, plotting equilibrium AI energy demand and renewable
PPA capacity. We also perform an extensive sensitivity analysis to examine the impact of parametric
changes. The key observations are as follows.
Instance AFirst, market-led scaling with strong market potential places the equilibrium in a
decoupling zone, shown in Panel (a) of Figure 1, in which renewable investment remains far below
energy demand. In this case, the adaptation trap becomes intrinsic to AI development: it arises
even without external emissions (i.e., whend 0 = 0). This is because, with a highθ, the developer
is sufficiently motivated to adoptx ∗ = 1 even when most of the energy demand is met by the grid.
This leads to substantial emissions from AI, and the adaptation benefits of frontier capability in
addressing those emissions sustain the carbon-intensive frontier equilibrium.
Sensitivity analyses indicate that restoring coupling requires substantial changes in the operating
environment so that renewable capacity materially affects the developer’s choice of AI scale. One route
is to increase the cost of fossil energy,c f, by 283.6% (under which the coupling zone in Proposition 1
exists). Alternatively, achieving a clean share of at least 50% in the decoupling zone, where the clean

20Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
50
100
150
200
250
300
350Energy (TWh)
AI energy demand
Capacity of renewable PPAs
Powered by renewable PPAs
Powered by grid electricity mix
(a) Market-Led Scaling with Strong
Market Potential (Instance A)
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
50
100
150
200
250
300Energy (TWh)
(b) Market-Led Scaling with Limited
Market Potential (Instance B)
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
20
40
60
80Energy (TWh)
(c) Resource-Led Scaling with Limited
Market Potential (Instance C)
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
50
100
150
200
250
300
350Energy (TWh)
(d) Resource-Led Scaling with Strong
Market Potential (Instance D)
Figure 1 AI Energy Demand and Renewable Energy Investment Outcomes in the Case Study. Panels plot AI
energy demand and renewable PPA capacity against the baseline emissions stockd 0 (billion metric
tons CO 2e; vertical scales differ).x ∗ values are annotated at the right of each panel and apply to the
region beyond the last marked threshold; circled markers with adjacent labels give regime-transition
thresholds. Renewable PPAs meet0.6%of demand in Instance A and12.47%in Instance D.
share is the fraction of AI energy demand met by renewable PPAs, requires reducing the clean-
capacity cost scaleg, by at least 77.4%. Improvements in energy efficiency, represented by a reduction
ink, can lower the required reduction ing.
Instance BSecond, market-led scaling with limited market potential leads to coupling whend 0
is low. Renewable capacity can therefore expand before the equilibrium transitions to the carbon-
intensive frontier, leaving a comparatively large renewable base even after decoupling occurs. This
explains why frontier AI in Panel (b) of Figure 1 is supported by a clean share of approximately
71.7%, close to the 80% policy goal discussed for China (Stan 2026). Nevertheless, the transition
into the adaptation trap occurs at a relatively low level of external climate pressure. The threshold
d0 = 8.820 billion metric tons of CO 2e corresponds to an increase of approximately 1.13 ppm in

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment21
atmospheric carbon concentration above the climate benchmark (NOAA 2025). At recent rates of
atmospheric carbon accumulation, this increase is equivalent to roughly six months of additional
concentration growth (Lindsey 2025). As another illustration, the intensity of extreme events has
risen markedly since 2020 (The Guardian 2025). Benchmarking the 2025 annual mean atmospheric
CO2 (425.6 ppm) against the 2020 annual mean (412.4 ppm) implies ad 0 of approximately 103 billion
metric tons of CO2e, far exceeding the threshold in Panel (b) (NOAA Global Monitoring Laboratory
2026). (The panels’ common horizontal range focuses on the transition region; at benchmark values
of this magnitude, every instance sits far beyond its threshold, where outcomes no longer vary with
d0.)
Sensitivity analysis shows that a further increase in market willingness-to-pay in Instance B likely
accelerates the transition to frontier AI and the trap mechanism, and sharply reduces the clean
share once in that region: increasingθby only about 5% reduces the clean share to 45.4%. One
effective countermeasure is increasing the economic-spillover parameterη(e.g., general productivity
improvements from AI deployment via better human-AI collaboration): a 30% increase in the spillover
componentη−1 restores the clean share to 66% even whenθis much larger, and a 70% increase in
η−1 helps achieve frontier AI powered by 100% renewable energy. Increasing the fossil-energy price
can produce similar effects.
Instances C and DThird, under resource-led scaling, AI expansion remains closely tied to renew-
able availability because developers are more sensitive to energy costs. With limited market potential,
the equilibrium remains coupled even atd 0 = 0, as shown in Panel (c) of Figure 1, yielding an adap-
tation pathway that operates across all levels of climate stress. This coupling, however, limits AI
development: under the baseline calibration, capability plateaus atx ∗ = 0.585.
A moderate increase in market willingness-to-pay can relax this constraint without immediately
breaking the coupling between AI and renewable capacity. For example, whenθin Instance C is
increased to the level used in Instance B, the equilibrium remains coupled and reachesx∗ = 1 onced 0
is sufficiently high (which can be interpreted as a sufficiently stringent climate policy that adopts a
low carbon-concentration benchmark when evaluatingd 0). Further increases inθ, however, eventually
create a decoupling zone. At intermediate levels of market potential, the pathway mechanism can
restore coupling, but only whend 0 is sufficiently high. Whenθreaches the level used in Instance
A, the pathway mechanism disappears altogether, and the equilibrium remains in the decoupling
zone with a low clean share, as shown in Panel (d). Thus, stimulating AI market demand can help
overcome the capability constraint under resource-led scaling, but excessive expansion can break
the link between AI growth and renewable development. Improving energy efficiency offers a less
destabilizing alternative: in the baseline Instance C, reducingkby approximately 23% is sufficient
to achievex∗ = 1 while preserving coupling.

22Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
Finally, Instance C is a moderately resource-led scaling scenario in which 1+α λ < cf cr holds and is
therefore particularly vulnerable to the impact of renewable intermittency. That is, coupling could
lead to higher emissions, and the adaptation pathway may reverse into a trap mechanism; in Instance
C, this reversal arises when the availability probability falls below roughly 0.98 (which is the ¯p
threshold in Proposition EC.5; see Section EC.2.2), so firming is essential, rather than merely helpful,
for preserving the pathway.
6.3. Discussion
Taken together, the case study shows that the adaptation-trap and adaptation-pathway mechanisms
are practically relevant but could manifest in different ways depending on the scaling environment.
Notably, high market potential effectively entrenches the adaptation trap and suppresses the adap-
tation pathway, thereby leading, under both market-led and resource-led scaling, to decoupling in
which the energy demand from AI development substantially outpaces renewable investment. A mod-
erate market potential, on the other hand, can lead to different outcomes between the two scaling
regimes: in the ranges represented by Instances B and C, market-led scaling tends to sustain frontier
capability but fall short of net zero under the adaptation trap, whereas resource-led scaling tends to
deliver cleaner energy at the cost of frontier scale under the adaptation pathway. This illustrates a
practical tension between AI development and the clean-energy transition.
Although the “power-couple” outcome, that is, frontier capability supplied fully by renewable elec-
tricity (x∗(y∗) = 1 withy ∗ =k), does not arise in the baseline calibrations, the sensitivity analyses
identify several mechanisms that can move the equilibrium in that direction. Importantly, the bind-
ing constraint differs across the two scaling regimes. Under market-led scaling, as in Instances A
and B, renewable development is the primary bottleneck: AI’s capability expands readily, but clean
capacity lacks sufficient influence over scaling. Effective interventions must therefore strengthen the
link between additional AI scale and additional clean power, for example, by lowering renewable-
investment costs, increasing the price of fossil energy, strengthening climate incentives, improving
energy efficiency, or increasing the general economic value generated by AI development. By contrast,
under resource-led scaling, as in Instance C, AI capability is the primary bottleneck. The relevant
interventions should therefore strengthen incentives for frontier capability without undermining cou-
pling, such as moderate increases in market potential and AI energy-efficiency improvements. Sec-
tion EC.1 provides an analytical characterization of this contrast: in all scenarios, the clean-capacity
cost scaleg, must lie below a threshold for a power-couple outcome to materialize. That thresh-
old, and with it the effectiveness of different interventions, depends on whether frontier capability is
achieved in the decoupling zone, where renewable development may lag behind (Instances A and B),
or in the coupling zone, where AI development may be constrained (Instance C).

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment23
Despite these differences, the results point to a common conclusion: net-zero frontier AI is unlikely
to result from any single intervention. Achieving the AI–renewable power couple requires a coordi-
nated portfolio: cheaper and easier-to-integrate clean capacity, policy that sufficiently internalizes
climate damages and broader externalities of fossil energy, and management of AI market expan-
sion and AI-driven electricity demand in a manner consistent with the prevailing scaling regime.
Even then, feasibility is limited in strongly market-led environments. In particular, rapid growth in
investment can weaken coupling, shifting the equilibrium away from net-zero frontier AI.
7. Extensions
We relax the baseline assumptions along four dimensions. Two concern the AI side of the market and
are developed here: capability may lower the cost of integrating renewables (Section 7.1), and devel-
opment may be competitive rather than monopolistic (Section 7.2). Two concern how clean capacity
is financed and physically delivered, and are developed in the electronic companion: Section EC.2.1
replaces the policymaker’s direct capacity choice with a financial incentive to which a private utility
responds, and Section EC.2.2 allows renewable output to be intermittent rather than dependable
and analyzes the firming that counters intermittency. 6 All four clarify when the equilibrium tilts
toward the adaptation trap versus the adaptation pathway. Hence, we focus on the market-led scaling
scenario in this section.
7.1. AI-Enabled Reductions in Clean-Capacity Costs
The main model assumes renewable-investment costsV(y) are independent of AI capability. In
practice, higher capability can lower the cost of deploying and integrating renewables, in particular
by improving forecasting, grid control, and storage operations, thereby easing integration frictions
(Choi et al. 2024). We capture this by allowing
V=V(x,y), ∂V(x,y) ∂x <0.
One such specification is
V(x,y) =ϕ(x)V(y),
whereϕ′(x)<0 andϕ(x)<1 for allx∈(0,1], andV(y) is the baseline cost function used in the main
model.
This extension introduces a feedback loop: higherxlowers the marginal cost ofy, strengthening
incentives to invest in renewables, relaxing the energy constraint, and potentially supporting higher
x. As a result, full decarbonization is easier to sustain; in particular, the renewable-cost threshold
for net-zero frontier AI is relaxed by a factor of 1/ϕ(1) (see Section EC.3.1).
6Fossil-side policy requires no separate extension because it operates throughc f: fossil subsidies lowerc f and
carbon pricing raises it (a full welfare accounting would also net out carbon-tax revenue as a transfer, which our
welfare function does not model), shifting the regime thresholds (for example, the condition in Proposition 3(i) and
the capability targetf(c f) in Proposition 2) without altering the two-regime structure. The counterfactual discussion
in Section 6.3 considers this lever.

24Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
50
100
150
200
250
300Energy (TWh)
AI energy demand
Capacity of renewable PPAs
Powered by renewable PPAs
Powered by grid electricity mix
(a)ϕ(x) = 1 (the main model)
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
50
100
150
200
250
300Energy (TWh) (b)ϕ(x) = 1−0.1x
0 2 4 6 8 10 12
d0 (billion metric tons CO2e)
0
50
100
150
200
250
300Energy (TWh) (c)ϕ(x) = 1−0.2x
Figure 2 Adaptation Trap under AI-Enabled Renewable Investment Cost Reduction. Illustration based on the
parametric setting of Instance B in the case study.
However, when AI-enabled cost reductions are insufficient to deliver full decarbonization, they can
instead intensify the adaptation trap by expanding the parameter region in which the mechanism
operates. Figure 2 illustrates this pattern using Instance B from the case study. With an AI-enabled
cost-reduction potential of roughly 10% (Panel (b)), an adaptation trap emerges onced 0 reaches
5.492. This cutoff is approximately 38% lower than the corresponding threshold in the absence of AI-
enabled cost reduction,d 0 = 8.820, shown in Panel (a), which reproduces Figure 1(b) for comparison.
Increasing the cost-reduction potential to 20% lowers the threshold further, as shown in Panel (c).
The intuition is straightforward: AI-enabled cost reductions make frontier scaling more attractive
in equilibrium, thereby accelerating decoupling and, under market-led scaling, bringing forward the
conditions under which the adaptation-trap mechanism arises.
Another key observation from comparing Figure 2(a) and (b) is that AI-enabled cost reduc-
tions may not translate into increased renewable-capacity investment once the equilibrium enters
the adaptation trap. This outcome arises from the loss of the scale effect as developers’ capability
choices decouple from renewable availability. Consequently, only sufficiently large cost reductions
can compensate for the loss of this lever and restore incentives for additional capacity investment.
For Instance B, illustrated in Figure 2, this cost-reduction requirement is at least 14.41%. If this
requirement is met, AI-enabled cost reductions entail a trade-off in which the adaptation trap is
more likely to occur but less fossil-dependent, as Figure 2(c) shows. Otherwise, such cost reductions
tend to entrench carbon reliance by accelerating the same carbon-intensive trap, as is the case in
Figure 2(b).
In practice, AI-enabled improvements in renewable development and integration are often cast as
both an accelerant of the energy transition and a way to shrink AI’s own footprint. Our analysis
shows that these gains depend on equilibrium responses: in some environments, efficiency improve-
ments can deepen reliance on carbon-intensive supply rather than displace it. A decarbonizing AI–
energy relationship requires more than technological complementarity: investment-side coupling must

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment25
be sustained. In particular, policy may need to preserve the scale channel so that incentives for
renewable-capacity expansion keep pace with AI-driven electricity demand.
These effects are one instance of a broader pattern that spans the renewable-promoting levers avail-
able to a policymaker. We examine two further levers in Sections EC.2.1 and EC.2.2: decentralized
investment, in which the policymaker sets a financial incentivesand a utility then chooses capacity,
and a firmed utilization factorζgoverning how much installed capacity becomes dependable renew-
able supply. Under market-led scaling,sandζreduce the carbon intensity of frontier AI yet can
hasten the adaptation trap, lowering ¯dm (forζ, only when it is not large enough to forestall the trap
entirely). Under resource-led scaling, both uniformly reinforce the adaptation pathway, lowering ¯dc.
The broader lesson is that making renewables cheaper, more usable, or better subsidized sharpens
the incentive to scale capability, so the emissions consequences turn on the scaling regime rather than
on the lever itself.
7.2. Competition Among AI Developers
The main model analyzes a single developer representing the industry. We extend the model to
explore the implications of competition between developers. Specifically, we consider two AI devel-
opers that compete by choosing capabilities (x 1,x 2) first and then prices (p 1,p 2). We refer readers
to Section EC.3.2 for model details. We note that incorporating the price decision does not affect
the main-model results in the monopoly case, so the difference observed in this extension can be
attributed to competition.
Competition can reduce the private return to incremental capability through two channels. First,
market sharing lowers the effective market potential,θ, available to each developer. Second, com-
petition can reduce the effective elasticity of equilibrium revenue with respect to capability, so that
marginal revenue grows more slowly as both developers scale. Together, these effects lower the return
to further capability expansion and increase developers’ sensitivity to energy costs. Equilibrium capa-
bility therefore becomes more responsive to renewable capacity, increasing the likelihood that renew-
able investment moderates AI expansion and strengthens coupling. Competition can thus reduce the
risk of the adaptation trap.
A caveat, however, is that whether and to what extent this potential can be realized depends on
market conditions. Figure 3 illustrates a key finding based on extensive numerical experiments. When
market potential (θ) is high, the capability decision of either developer remains primarily driven
by the market, and the coupling with renewable capacity that competition enables is not strong
enough to structurally shift the equilibrium. In this case, the equilibrium exhibits a “dual adaptation
trap” under which both developers are subject to this mechanism. The dark-blue region in Figure 3
illustrates when such an equilibrium emerges; Instance A in Section 6 becomes a case in point when

26Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
2.6 2.8 3.0 3.2 3.4 3.6 3.8
λ  (elasticity of willingness-to-pay)
50
100
150
200
250θ  (market potential, billion USD)
Figure 3 Equilibrium under the Competitive Setting. Illustration based on the parametric setting of Instance A
in the case study (except(θ,λ)), withd 0 = 10.
the market potentialθrises above$170.5 billion (assumingd 0 = 10), a plausible scenario considering
that AI investment in the U.S. reached$285.88 billion in 2025 (Sajadieh et al. 2026). At the other
extreme, reduced market investmentθmay leave revenue potential insufficient to sustain competition,
yielding a monopoly equilibrium (see the white region in Figure 3). Instance B corresponds to this
case.
Nevertheless, whenθis intermediate (see the light-blue region in Figure 3), competition can induce
partially carbon-free AI development: in equilibrium, at least one developer’s energy demand is
fully met by renewable resources despite market-led scaling. Whenλdrops below 1 +α, scaling
becomes resource-led and the adaptation pathway follows. This extension highlights that an analogous
mechanism may already be at work prior to this transition, operating through the competition lever.
The effect also persists asλrises over a meaningful range, suggesting that competition, supported by
a market with an intermediate yet substantial level of investment, can provide an effective channel
for countering the adaptation trap even under strong market-led scaling.
A policy implication follows. Antitrust and market design in AI can shape the carbon intensity of
the capability race by altering developers’ incentives to scale. When rents are highly concentrated, a
dominant developer has stronger incentives to expand compute despite reliance on carbon-intensive
power. Greater competition weakens these returns to scale and increases sensitivity to energy
costs, making renewable capacity a more effective instrument for shifting AI development toward a
carbon-free pathway.
8. Conclusion
AI and renewable energy are increasingly cast as a “power couple,” on the premise that surg-
ing AI demand will accelerate clean-energy investment and hasten decarbonization (Al-Zu’bi 2025;

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment27
Engel et al. 2025; Rozite et al. 2023). This paper examines when that premise holds and when it
fails. Rather than taking renewable supply or AI demand as given, we treat capability choices and
renewable-capacity expansion as jointly determined and show that equilibrium outcomes depend on
two primitives: how compute maps into capability and how capability maps into private value.
A key insight from our analysis is that expanding renewable capacity need not decarbonize
AI growth. When the market value of additional capability rises at least as fast as its energy
requirement, developers have strong incentives to push the frontier even when the marginal
megawatt-hour is fossil-based. When frontier capability is relatively insensitive to energy costs,
clean-capacity expansion can cease to affect AI scale before fossil electricity is fully displaced. Past
that point, additional renewable investment mainly replaces fossil generation, and that gain may not
cover the investment cost; the equilibrium can stop short of full decarbonization even as AI remains
at the frontier. This regime supports a carbon-intensive equilibrium and an “adaptation trap”: as
climate damages rise, the value of AI-enabled adaptation increases, which strengthens incentives
to enable frontier scaling on fossil energy, thereby raising emissions. By contrast, when the market
value of additional capability rises more slowly than its energy requirement, energy costs become
binding, and capability responds more directly to renewable capacity; clean investment then both
enables capability and decarbonizes marginal compute, yielding an “adaptation pathway” in which
adaptation advances through AI scaled on carbon-free power.
These regimes also clarify when “rebound” is benign and when it is harmful. Expanding renewable
supply and improving energy efficiency both lower the effective cost of compute and can accelerate
scaling. Under market-led scaling, this acceleration loosens the link between compute and clean
capacity, slowing decarbonization and increasing the risk of carbon lock-in. Under resource-led scaling,
the same cost reductions tighten that link, making renewable investment and AI growth mutually
reinforcing, provided market potential remains in the coupled range. A carbon-intensive equilibrium,
therefore, can arise from incentives and scaling economics alone, not only from slow infrastructure
or political inertia. A clean transition, on the other hand, is not guaranteed by ongoing renewable
expansion, the cost advantage of clean power, or AI-driven efficiency improvements; it requires policy
and market design that preserve the link between AI scaling and clean-capacity expansion.
Four policy lessons follow. First, policies that expand clean capacity without addressing marginal
emissions need not lower AI’s emissions intensity; policies that raise the private cost of fossil-powered
compute can be instrumental, whether through carbon pricing, carbon-free procurement require-
ments, or constraints tied to local grid emissions. Second, to strengthen the coupling between AI
growth and clean-energy deployment, policy must govern the conditions under which AI scales: the
location and timing of large loads, renewable interconnection, and rules for carbon-free matching.
Third, when market forces are exceptionally strong, energy policy may have limited leverage; pursuing

28Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
additional emissions reductions in other sectors to offset AI-related emissions may be more effective,
though evaluating cross-sector instruments lies beyond our single-sector model. Finally, the welfare
value of AI’s adaptation potential is state-dependent: as climate damages rise, the policymaker’s
optimal response can switch sharply between the trap and the pathway, implying that climate policy
should treat adaptation and mitigation as a joint design problem.
Whether AI and renewable energy reinforce each other depends on the economics of AI scaling and
on how compute growth connects to the energy system. The energy system’s equilibrium response
settles AI’s environmental consequences, and institutions shape that response. Procurement, inter-
connection constraints, and the siting and timing of data-center expansion determine whether scaling
is met by clean additions or by greater reliance on fossil generation. A clean scaling path requires
policies and market design that sustain investment-side coupling so that renewable deployment keeps
pace with compute growth. This, in turn, motivates a research agenda at the intersection of opera-
tions, markets, and political economy: measuring how workload flexibility affects marginal emissions;
designing grid-aware siting and scheduling that internalize spatial and temporal system conditions;
studying how institutions such as PPAs, interconnection rules, capacity markets, and hourly match-
ing requirements shape clean investment and the incentives to scale frontier AI; and quantifying the
substitution between compute flexibility and energy flexibility, including the latency tolerance that
governs how far AI workloads can follow renewable availability.
Acknowledgments
The authors are grateful to Vishal Agrawal, Saurabh Amin, Atalay Atasu, Hamsa Bastani, John R. Birge,
Charles J. Corbett, Jan C. Fransoo, Huseyin Gurkan, Serguei Netessine, Masha Shunko, Owen Q. Wu, and
S ¸afak Y¨ ucel for their thoughtful comments on and reactions to a preliminary draft, and to the anonymous
reviewers of the 2026 MSOM Sustainable Operations SIG for their constructive feedback. They are especially
indebted to Serguei Netessine for his excellent discussion of the paper at the Sustainable Operations SIG
of the 2026 MSOM Conference held at Harvard Business School, and they thank the session participants
for their helpful questions. They also thank participants at the Supply Chain Management Conference on
Sustainability and Social Responsibility in Supply Chains, held at the Gies College of Business, University
of Illinois Urbana-Champaign, and at the Southern California OR/OM Day at USC Marshall, where earlier
versions of this paper were presented.
References
Acemoglu D (2025) The simple macroeconomics of AI.Economic Policy40(121):13–58.
Acemoglu D, Aghion P, Bursztyn L, Hemous D (2012) The environment and directed technical change.
American Economic Review102(1):131–166.
Aflaki S, Netessine S (2017) Strategic investment in renewable energy sources: The effect of supply intermit-
tency.Manufacturing & Service Operations Management19(3):489–507.

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment29
Aghion P, Dechezleprˆ etre A, Hemous D, Martin R, et al. (2016) Carbon taxes, path dependency, and directed
technical change: Evidence from the auto industry.Journal of Political Economy124(1):1–51.
Al-Zu’bi I (2025) Energy and AI: The power couple that could usher in a net-zero world. World Economic
Forum, URLhttps://www.weforum.org/stories/2025/01/energy-ai-net-zero/.
Arthur WB (1989) Competing technologies, increasing returns, and lock-in by historical events.The Eco-
nomic Journal99(394):116–131.
Bastani H, Cachon GP (2025) The human-AI contracting paradox, working paper, The Wharton School,
University of Pennsylvania; available at SSRN.
BloombergNEF (2024) Corporate clean power buying grew 12% to new record in 2023, according to
BloombergNEF. Press release, URLhttps://about.bnef.com/insights/finance/corporate-c
lean-power-buying-grew-12-to-new-record-in-2023-according-to-bloombergnef/, accessed
2026-01-05.
Bulow JI, Geanakoplos JD, Klemperer PD (1985) Multimarket oligopoly: Strategic substitutes and comple-
ments.Journal of Political Economy93(3):488–511.
Chemama J, Cohen MC, Lobel R, Perakis G (2019) Consumer subsidies with a strategic supplier: Commit-
ment vs. flexibility.Management Science65(2):681–713.
Chen C (2001) Design for the environment: A quality-based model for green product development.Manage-
ment Science47(2):250–263.
Choi S, Jain R, Feng C, Emami P, et al. (2024) Generative AI for power grid operations. Technical report,
National Renewable Energy Laboratory (NREL), URLhttp://dx.doi.org/10.2172/2477920.
Cohen MC, Dai T, Perakis G, Agrawal N, et al. (2026) OM forum—Supply chain management in the AI era:
A vision statement from the operations management community.Manufacturing & Service Operations
Management28(3):687–705.
Cohen MC, Lobel R, Perakis G (2016) The impact of demand uncertainty on consumer subsidies for green
technology adoption.Management Science62(5):1235–1258.
de Bruin KC, Dellink RB, Tol RSJ (2009) AD-DICE: An implementation of adaptation in the DICE model.
Climatic Change95(1-2):63–81.
Deloitte (2025) AI for infrastructure resilience. Deloitte Center for Sustainable Progress, URLhttps://www.
deloitte.com/global/en/issues/climate/ai-for-infrastructure-resilience.html, accessed
2026-01-12.
Engel A, Varadarajan U, Posner D (2025) How “power couples” can help the United States win the global
AI race. RMI, URLhttps://rmi.org/how-power-couples-can-help-the-united-states-win-t
he-global-ai-race/.
Fransoo JC, Peels R, Udenio M (2026) Navigating supply chain dynamics for sustained AI growth. Cohen
MC, Dai T, eds.,AI in Supply Chains: Perspectives from Global Thought Leaders, volume 27 ofSpringer
Series in Supply Chain Management, 37–54 (Cham: Springer), series Editor: Christopher S. Tang.
Gao Z, Alshehri K, Birge JR (2024) Aggregating distributed energy resources: Efficiency and market power.
Manufacturing & Service Operations Management26(3):834–852.
Gao Z, Sunar N, Birge JR (2025) Designing renewable power purchase agreements: Impact on green energy
investment, working paper.

30Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
Gillingham K, Rapson D, Wagner G (2016) The rebound effect and energy efficiency policy.Review of
Environmental Economics and Policy10(1):68–88.
Google (2020) Our 2020 environmental report. URLhttps://blog.google/outreach-initiatives/sus
tainability/2020-environmental-report/.
Grand-Cl´ ement J, Pauphilet J (2026) The best decisions are not the best advice: Making adherence-aware
recommendations.Management Science72(1):667–692.
Greene-Dewasmes G (2025) How AI can accelerate the energy transition, rather than compete with it. World
Economic Forum, URLhttps://www.weforum.org/stories/2025/11/ai-accelerate-energy-tra
nsition/.
Guan X, Qi A, Wang S (2025) Why the best machine may not be the best: Incentivizing human-machine
collaboration, working paper, Naveen Jindal School of Management, University of Texas at Dallas;
available at SSRN.
Gurkan H, de V´ ericourt F (2022) Contracting, pricing, and data collection under the AI flywheel effect.
Management Science68(12):8791–8808.
Hatzius J, Briggs J, Kodnani D, Pierdomenico G (2023) The potentially large effects of artificial intelligence
on economic growth. Report, Goldman Sachs, URLhttps://www.gspublishing.com/content/res
earch/en/reports/2023/03/27/d64e052b-0f6e-45d7-967b-d7be35fabd16.pdf.
Hestness J, Narang S, Ardalani N, Diamos GF, et al. (2017) Deep learning scaling is predictable, empirically.
arXiv preprint arXiv:1712.00409URLhttps://arxiv.org/abs/1712.00409.
Hoffmann J, Borgeaud S, Mensch A, Buchatskaya E, et al. (2022) Training compute-optimal large language
models.Advances in Neural Information Processing Systems, neurIPS 2022; arXiv:2203.15556.
Ingham A, Ma J, Ulph A (2007) Climate change, mitigation and adaptation with uncertainty and learning.
Energy Policy35(11):5354–5369.
Ingham A, Ma J, Ulph A (2013) Can adaptation and mitigation be complements?Climatic Change120(1):39–
53.
International Energy Agency (2025) Energy and AI. Special report, International Energy Agency, Paris,
URLhttps://www.iea.org/reports/energy-and-ai, published 10 April 2025.
International Renewable Energy Agency (2025) Renewable power generation costs in 2024. Technical report,
International Renewable Energy Agency, URLhttps://www.irena.org/Publications/2025/Jun/
Renewable-Power-Generation-Costs-in-2024.
Jaffe AB, Newell RG, Stavins RN (2005) A tale of two market failures: Technology and environmental policy.
Ecological Economics54(2-3):164–174.
Jaffe AB, Stavins RN (1994) The energy paradox and the diffusion of conservation technology.Resource and
Energy Economics16(2):91–122.
Kaplan J, McCandlish S, Henighan T, Brown TB, et al. (2020) Scaling laws for neural language models.
arXiv preprint arXiv:2001.08361URLhttps://arxiv.org/abs/2001.08361.
Kaps C, Marinesi S, Netessine S (2023) When should the off-grid sun shine at night? Optimum renewable
generation and energy storage investments.Management Science69(12):7633–7650.
Klein RJT, Huq S, Denton F, Downing TE, et al. (2007) Inter-relationships between adaptation and miti-
gation. Parry ML, Canziani OF, Palutikof JP, van der Linden PJ, et al., eds.,Climate Change 2007:

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment31
Impacts, Adaptation and Vulnerability. Contribution of Working Group II to the Fourth Assessment
Report of the Intergovernmental Panel on Climate Change, 745–777 (Cambridge, UK: Cambridge Uni-
versity Press).
Kok AG, Shang K, Y¨ ucel S ¸ (2020) Investments in renewable and conventional energy: The role of operational
flexibility.Manufacturing & Service Operations Management22(5):925–941.
Levy M (2025) Coal-fired power plant, now retired, to become massive gas-powered campus for AI, data
centers. The Business Journal, URLhttps://thebusinessjournal.com/coal-fired-power-plant
-now-retired-to-become-massive-gas-powered-campus-for-ai-data-centers/.
Lindsey R (2025) Climate change: Atmospheric carbon dioxide. Climate.gov (NOAA), URLhttps://www.
climate.gov/news-features/understanding-climate/climate-change-atmospheric-carbon-d
ioxide, accessed 2026-01-12.
Maslej N, Fattorini L, Perrault R, Gil Y, et al. (2025) The AI index 2025 annual report. AI Index Steering
Committee, Institute for Human-Centered AI, Stanford University, URLhttp://dx.doi.org/10.48
550/arXiv.2504.07139, arXiv:2504.07139.
Maslej N, Fattorini L, Perrault R, Parli V, et al. (2024) The AI index 2024 annual report. AI Index Steering
Committee, Institute for Human-Centered AI, Stanford University, arXiv:2405.19522.
Microsoft (2020) Microsoft will be carbon negative by 2030. Official Microsoft Blog, URLhttps://blog
s.microsoft.com/blog/2020/01/16/microsoft-will-be-carbon-negative-by-2030/, accessed
2026-01-05.
Morgan K, Partridge B (2025) AI’s global resource race: Challenges and opportunities. S&P Global, URL
https://www.spglobal.com/en/research-insights/special-reports/look-forward/data-cen
ter-frontiers/global-ai-power-demand-challenges-opportunities, look Forward: Data Center
Frontiers (Special Report).
Netessine S, Shunko M (2026) The invisible backbone: How supply chains bring AI to life. Cohen MC, Dai T,
eds.,AI in Supply Chains, volume 27 ofSpringer Series in Supply Chain Management, 55–73 (Cham:
Springer Nature Switzerland AG), series Editor: Christopher S. Tang.
NOAA (2025) FAQ about the carbon dioxide record: How do we know how much CO2 is in the atmosphere?
NOAA Global Monitoring Laboratory, URLhttps://gml.noaa.gov/outreach/faq_cat-3.html#9,
accessed 2026-01-12.
NOAA Global Monitoring Laboratory (2026) Trends in atmospheric carbon dioxide: Globally averaged
marine surface annual mean data. URLhttps://gml.noaa.gov/ccgg/trends/, accessed July 2026.
Parker GG, Van Alstyne MW (2005) Two-sided network effects: A theory of information product design.
Management Science51(10):1494–1504.
Peng X, Wu OQ, Souza GC (2024) Renewable, flexible, and storage capacities: Friends or foes?Manufacturing
& Service Operations Management26(5):1730–1749.
Popp D (2002) Induced innovation and energy prices.American Economic Review92(1):160–180.
Porter ME, van der Linde C (1995) Toward a new conception of the environment-competitiveness relation-
ship.Journal of Economic Perspectives9(4):97–118.
Ramanan A (2025) Coal- and gas-fired power plants have a new best friend: data centers. URLhttps:
//www.utilitydive.com/news/fossil-fuel-gas-coal-climate-data-centers/753565/, opinion.

32Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment
Remshard M (2022) Does preparing for global warming mean we’ve given up? Why climate change adaptation
and mitigation go hand-in-hand. Yale Environment Review, URLhttps://environment-review.ya
le.edu/does-preparing-global-warming-mean-weve-given-why-climate-change-adaptatio
n-and-mitigation-go-hand, accessed 2026-01-05.
Rolnick D, Donti PL, Kaack LH, Kochanski K, et al. (2019) Tackling climate change with machine learning.
arXiv preprint arXiv:1906.05433URLhttps://arxiv.org/abs/1906.05433.
Rozite V, Miller J, Oh S (2023) Why AI and energy are the new power couple. International Energy Agency
Commentary, URLhttps://www.iea.org/commentaries/why-ai-and-energy-are-the-new-pow
er-couple.
Sajadieh S, Fattorini L, Perrault R, Gil Y, et al. (2026) The AI index 2026 annual report. AI Index Steering
Committee, Institute for Human-Centered AI, Stanford University, URLhttps://hai.stanford.edu
/assets/files/ai_index_report_2026.pdf.
Stan AM (2026) China’s green-power target for AI data centres runs into the grid. The Next Web, URL
https://thenextweb.com/news/china-green-power-ai-data-centres-hurdles.
Stauffer NW (2025) How artificial intelligence can help achieve a clean energy future. MIT News, URL
https://news.mit.edu/2025/how-ai-can-help-achieve-clean-energy-future-1124, online
article.
Strubell E, Ganesh A, McCallum A (2019) Energy and policy considerations for deep learning in NLP.
Korhonen A, Traum D, M` arquez L, eds.,Proceedings of the 57th Annual Meeting of the Association for
Computational Linguistics, 3645–3650 (Florence, Italy: Association for Computational Linguistics).
Sunar N, Birge JR (2019) Strategic commitment to a production schedule with uncertain supply and demand:
Renewable energy in day-ahead electricity markets.Management Science65(2):714–734.
The Guardian (2025) Nasa data reveals dramatic rise in intensity of weather events. News article, URL
https://www.theguardian.com/world/2025/jun/17/nasa-data-reveals-dramatic-rise-in-int
ensity-of-weather-events.
Trivella A, Mohseni-Taheri D, Nadarajah S (2023) Meeting corporate renewable power targets.Management
Science69(1):491–512.
Unruh GC (2000) Understanding carbon lock-in.Energy Policy28(12):817–830.
Unruh GC (2002) Escaping carbon lock-in.Energy Policy30(4):317–325.
US Energy Information Administration (2025a) China country analysis brief. Technical report, U.S. Energy
Information Administration, URLhttps://www.eia.gov/international/analysis/country/CHN,
accessed 2026-01-05.
US Energy Information Administration (2025b) Electric power monthly: Table 1.1. net generation by energy
source: Total (all sectors). Data table (annual totals include 2024); release dated December 23, 2025,
URLhttps://www.eia.gov/electricity/monthly/epm_table_grapher.php?t=table_1_01,
accessed 2026-01-05.
Volcovici V (2025) UN chief urges tech sector to power data centers with renewables.ReutersURLhttps:
//www.reuters.com/sustainability/cop/un-chief-urges-tech-sector-power-data-centers-w
ith-renewables-2025-07-22/.
Wang X, Cho SH, Scheller-Wolf A (2021) Green technology development and adoption: Competition, regu-

Gui and Dai:Power Couple? AI Growth and Renewable Energy Investment33
lation, and uncertainty—a global game approach.Management Science67(1):201–219.
Wu OQ, Kapuscinski R (2013) Curtailing intermittent generation in electrical systems.Manufacturing &
Service Operations Management15(4):578–595.
Ya˜ nez-Barnuevo M (2025) Data center energy needs could upend power grids and threaten the climate.
Environmental and Energy Study Institute (EESI), URLhttps://www.eesi.org/articles/view/d
ata-center-energy-needs-are-upending-power-grids-and-threatening-the-climate.
Yue X, Ni Y, Zhang K, Zheng T, et al. (2024) MMMU: A massive multi-discipline multimodal understanding
and reasoning benchmark for expert AGI.Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 9556–9567.

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec1
Electronic Companion to
“Power Couple? AI Growth and Renewable Energy Investment”
This electronic companion is organized in two parts. Sections EC.1 to EC.3 develop supplementary eco-
nomics: conditions under which frontier AI is powered entirely by renewables, two extensions that relax the
baseline assumptions on who invests and on what installed capacity delivers, and the formal details behind
the two extensions analyzed in the main text. Sections EC.4 and EC.5 provide technical verification: proofs
of the four results stated in the main text, followed by the calibration sources and computations behind
Table 1 and the case study. Proofs of the companion’s own results accompany their statements.
EC.1. Additional Analytical Results: Conditions for Carbon-Free Frontier AI
In the counterfactual discussion in the case study (Section 6.3), we examine conditions under which an
equilibrium arises in which the optimal AI capability choice isx∗(y∗) = 1 and the optimal renewable capacity
investment isy ∗ =k. Analytically, it can be shown that such conditions may involve (i) sufficiently low
renewable investment cost, (ii) energy demand that is not excessively high, and (iii) sufficiently adverse
climate conditions. For simplicity, we adoptV(y) =g·y µ whereµ>1 in this analysis.
Proposition EC.1.In the market-led scaling scenario, there exists an energy demand threshold ¯k, a
climate condition threshold ˆd, and two marginal renewable investment cost thresholdsg 1,g 2 such that an equi-
librium in whichx ∗(y∗) = 1andy ∗ =kis achieved if (i)k≤ ¯k,d 0≥ ˆd, andg<g 1 when θ k≤max{ cf (1+α) λ ,cr},
or (ii)g≤g 2 when θ k >max{ cf (1+α) λ ,cr}.
Proof of Proposition EC.1.First, when θ k >max{ cf (1+α) λ ,cr}, according to the fourth paragraph in the proof
of Proposition 3,x ∗ = 1 materializes only in the “decoupling zone” characterized by the third scenario in
Proposition 1. Hence, achievingy∗ =kfirst requires thaty=kmaximizes welfare along thex ∗(y) = 1 branch.
This happens whenV ′(k)≤η(c f−cr) + (1−b)efξ, which is equivalent tog≤g 0 2 .= η(cf−cr )+(1−b)efξ µkµ−1 . Second,
we need to ensure that the welfare undery=k,W(k) =η(θ−c rk)−ξ(1−b)d 0−gk µ, is no smaller than
that in the other two scenarios in Proposition 1: on the branch wherex ∗(y) = 0, welfare equals−ξd 0−gy µ
and is maximized aty= 0, soW(0) =−ξd 0;W(k)≥W(0) ifg≤g 0 3 .= η(θ−crk)+ξbd0 kµ . On the branch where
x∗(y) = (y/k)1/(1+α), the requirementW(k)≥W(y) is equivalent to
g(kµ−yµ)≤η [ θ ( 1− (y k ) λ 1+α ) −cr(k−y) ] +ξbd 0 [ 1− (y k ) 1 1+α ] .
This inequality holds at every suchyon this branch ifg≤g 0 4, where
g0 4 .= inf y1≤y<y2
η
[
θ
(
1−
(y
k
) λ
1+α
)
−cr(k−y)
]
+ξbd 0
[
1−
(y
k
) 1
1+α
]
kµ−yµ
Imposingg≤g 2
.= min{g0 2,g 0 3,g 0 4}therefore proves Proposition EC.1(ii).
Second, when θ k≤max{ cf (1+α) λ ,cr}, according to the second paragraph in the proof of Proposition 3, two
possibilities arise.

ec2e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
• cr cf < 1+α λ and θ k≤ 1+α λ cf: in this case,y 2 =k. Hence, an equilibrium in whichx ∗(y∗) = 1 andy ∗ =k
can be achieved only in the “coupling zone” in whichx∗(y) = (y k)1/(1+α). Plugging this solution into the
welfare function leads to a function that we denote byW 3(y). It can be shown that this equilibrium
is indeed achieved if (a)d 0≥ ηθλ(λ−(1+α)) αbξ , and (b)g≤min{ bd0ξ−(1+α)crηk+ηθλ (α+1)k·µkµ−1 , bd0ξ−crηk+ηθ kµ }. Condition
(a) ensures thatW 3(y) is concave, so the optimal solution is achieved either at a stationary point or
at the endpoint. Thusy ∗ =kwhenW ′ 3(k)≥0 andW 3(k)≥W(0) (i.e., renewable investment yields
higher welfare than not investing). The two terms that define thegthreshold in condition (b) ensure
that these two inequalities hold.
• cr cf ≥ 1+α λ and θ k≤cr: in this case,x∗(y) = 0 for anyy∈[0,k]. Hence, an equilibrium in whichx ∗(y∗) = 1
andy ∗ =kcannot be achieved. We imposek< θ cr to eliminate this case.
Combining the conditions on (k,d 0,g) proves Proposition EC.1(i).Q.E.D.
Although it is intuitive that ensuring net-zero frontier AI requires a sufficiently low marginal cost of
investment in renewables, Proposition EC.1 indicates that the cost threshold depends on the ratio θ k, which
measures the average market investment per unit of energy demand. If this ratio exceeds
cf (1+α)
λ (which is
equivalent toθλ≥c fk(1 +α), i.e., the marginal market value exceeds the marginal cost atx= 1), it can be
shown that maximum AI capability is achieved in the decoupling zone, independent of whethery=k. In this
case, the reduction of the marginal cost of renewable investment is driven only by the composition effect,
that is, it should be lower than the marginal benefit from displacing fossil fuel. Indeed, the proof shows that
gshould be no higher than the cost threshold identified in condition (b) in Proposition 3(i).
Otherwise, maximum AI capability may be achieved in the coupling zone, which requires full decarboniza-
tion to justify its cost. In this case, the marginal benefit of renewable investment is determined by the scale
effect, which includes the developer’s scale margin, the associated economic spillover, and the enhanced
adaptation benefits, minus the renewable energy generation cost. These components determine the (d 0,g 1)
thresholds. A caveat is that in this case, the marginal benefit of renewable investment could be negative
when frontier AI entails too high an energy cost even when powered by the cheaper renewable sources and
therefore cannot be realized. This explains the upper bound on the energy-demand scalekfor this case.
Another useful observation is that because the scale effect draws on AI’s adaptation benefits, theg 1 bound
can be much more relaxed thang 2 whend 0 is high, which suggests an avenue to circumvent the limited
renewable investment cost reduction potential, which is constrained by technology.
We show that Proposition EC.1 applies structurally to resource-led scaling scenarios. This is because the
impact of the comparison between the elasticity parametersλand 1 +αis attenuated at frontier capability
x= 1. The next proposition formalizes the finding.
Proposition EC.2.In the resource-led scaling scenario, Proposition EC.1 continues to hold if (a) the
threshold on θ k that separates cases (i) and (ii) is changed to cf (1+α) λ , (b) the thresholds on(k,d 0)are removed,
and (c) theg 1 threshold is replaced by a different one,g 3, and theg 2 threshold is replaced byg 0 2 defined in
the proof of Proposition EC.1.

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec3
Proof of Proposition EC.2.Based on Proposition 2, it can be shown that when θ k > cf (1+α) λ ,f(c f)>1, thus
only the first case (the “decoupling zone”) in Proposition 2 materializes, in whichx ∗(y) = 1 for anyy∈[0,k].
Applying the same proof for Proposition EC.1(ii) proves the result for the resource-led scaling scenario.
When θ k≤ cf (1+α) λ ,f(c f)≤1, thus the welfare function has at least two pieces. Nevertheless, it can be
shown that the equilibriumx ∗ = 1,y ∗ =kcan only be achieved in the second case, that is, the “coupling
zone” of Proposition 2. Plugging thex ∗(y) = (y k)1/(1+α) solution into the welfare function leads to the same
functionW 3(y) as defined in the proof of Proposition EC.1. It can be proven thatW 3(y) is guaranteed to be
concave in the resource-led scaling scenario (thus thed 0 threshold in Proposition EC.1 is no longer needed).
Meanwhile, we also plug thex ∗ =f(c f) solution into the welfare function and denote the resulting function
byW 4(y). Hence,y∗ =kis achieved when (a)W ′ 3(k)≥0, and (b)W 3(k)≥max y∈[0,kf(cf )1+α]W4(y). Condition
(a) is equivalent to an upper bound ongas shown in the proof of Proposition EC.1. The same can be shown
for condition (b): lety′ 4 .= arg maxy∈[0,kf(cf )1+α]W4(y). Then condition (b) is equivalent tog(k µ−(y′ 4)µ) being
no greater than a certain term that involves nog. Sincek µ−(y′ 4)µ is lower bounded byk µ−(kf(c f))µ, this
condition can be translated into a well-defined upper bound ong. Settingg 3 as the minimum between this
bound and the one that guarantees condition (a) proves the result for the case where θ k≤ cf (1+α) λ .Q.E.D.
EC.2. Additional Extensions and Robustness
This section presents two further extensions that test the robustness of our main results to richer descriptions
of how renewable capacity is financed, used, and delivered. We first consider decentralized renewable invest-
ment, replacing the policymaker’s direct choice of capacity with an arrangement in which the policymaker
sets a financial incentive and a utility makes the investment decision. We then model intermittent renewable
availability and its firming explicitly: intermittency places a strictly positive floor under emissions whenever
the developer is active, and firming restores the carbon-free outcomes at a higher marginal investment cost.
Under decentralized investment, the adaptation-trap and adaptation-pathway characterizations of Propo-
sitions 3 and 4 continue to hold, with the subsidy level determining how much clean capacity the private
market delivers. Under intermittency, the trap mechanism is reinforced, whereas the pathway mechanism
weakens, and firming restores the structure of the main model at a strictly higher marginal cost.
EC.2.1. Decentralized Renewable Investment
In this extension, we explicitly model the interaction between policy choices and renewable capacity invest-
ment. We focus on a setting in which the policymaker provides financial incentives (e.g., renewable subsidies
and tax credits), a major policy lever for stimulating renewable investment in practice. We also consider a
utility undertaking renewable capacity development, reflecting one of the primary channels through which
renewable energy investment occurs in practice.
The utility determines the renewable capacity levelyto maximize the return from renewable investment.
A stylized formulation of its objective is maximizing (p r−cr +s)·β(x ∗(y),y)·k(x ∗(y))1+α−V(y), wherep r
is the unit rate (e.g., a large-load tariff) charged for the amount of renewable energy used by the developer
under its optimal capability choices induced byy,c r is the unit renewable generation cost, andsis the

ec4e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
unit financial incentive that the policymaker provides for renewable generation. 1 Although utilities may also
recover part of their renewable investment costs from other ratepayers in practice, we abstract from these
channels and focus on the direct interaction between renewable investment and AI development. In practice,
electricity tariffs are typically subject to regulatory oversight and are therefore not readily adjusted, especially
compared to direct financial incentives such as subsidies or tax credits. Hence, we treatp r as exogenous.
We consider a three-stage game. In Stage 1, the policymaker chooses the financial incentives∈[0,¯s], where
¯srepresents fiscal constraints that limit the amount of such incentive. The social welfare function that the
policymaker maximizes equals the sum of the developer’s profit (plus associated economic spillovers) and the
utility’s return from renewable development, minus the climate damage and the fiscal spending on incentive
provision. In Stage 2, the utility determines the renewable capacity levely. Finally, in Stage 3, the developer
chooses capabilityxgiven the available renewable capacity. Relative to the main model, the developer pays
the renewable tariffp r rather thanc r, although we continue to assumep r<cf, reflecting settings in which
large-load renewable procurement provides electricity at a lower price than standard retail grid service. 2
We show that our main results are robust to the policy-investment interactions, and the likelihood and
the magnitude of the adaptation/pathway effects can be moderated by the intensity of the policy support.
We start by presenting this result for the market-led scaling scenario. Recall they 1,y 2 thresholds that define
the developer’s optimal capability choice in Proposition 1. In the extension, we modify these thresholds by
replacingc r withp r in their characterization (see the proof of Proposition 1) and denote the new thresholds
by ˆy1 and ˆy2.
Proposition EC.3.(i) Statement (i) in Proposition 3 continues to hold if any of the following condi-
tions is satisfied: (a)θ≤max{ 1+α λ ·cfk,prk}, (b)V ′(k)≤min{η(c f−pr) + (pr−cr) + (1−b)efξ,pr−
cr + ¯s}, or (c)V′(ˆy2)>p r−cr + ¯s.
(ii) Otherwise, statement (ii) in Proposition 3 holds. Furthermore, the threshold ¯dm decreases in¯s, whereas
the equilibrium renewable energy investmenty ∗ whend 0≥ ¯dm increases in¯s.
Proof of Proposition EC.3.We can prove that condition (a) leads to statement (i) in Proposition 3 based on
the same arguments in the proof of Proposition 3 (the second paragraph), because the developer’s capability
choice follows Proposition 1 withc r replaced byp r. To prove condition (b), we complement the proof in
Proposition 3 (the first paragraph) by the fact thaty ∗ =kcan be achieved if and only ifV ′(k)≤p r−cr + ¯s,
that is, there exists anslevel to induce renewable investment to fully cover AI energy demand. Lastly,
condition (c) indicates that under all feasibleslevels, the induced renewable investment does not exceed the
ˆy2 threshold, and thus the equilibrium remains in the carbon-free zone.
To prove that statement (ii) in Proposition 3 continues to hold, we need to show that when the three
conditions discussed above are violated, there are feasiblesvalues under whichx ∗ = 1 can materialize. This is
1Some renewable subsidies and tax benefits are tied to installed capacity rather than generation. This distinction
does not affect the model outcomes because, in equilibrium, the developer either utilizes the full amount of available
renewable generation or none of it.
2A more rigorous formulation would introduce a separate fossil energy pricep f >cf representing the grid elec-
tricity tariff that the developer pays. This refinement only shifts the thresholds that define the equilibrium regimes
and does not affect the insights qualitatively.

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec5
guaranteed byV ′(ˆy2)≤p r−cr + ¯s. Furthermore, becauseV′(k)>min{η(c f−pr) + (pr−cr) + (1−b)efξ,pr−
cr + ¯s}, either (i)V′(k)>p r−cr + ¯s, in which case no incentive level is sufficient to induce the utility to
invest inkamount of renewable capacity, or (ii)V ′(k)>η(c f−pr)+(p r−cr)+(1−b)e fξ, in which case even
wheny=kis feasible, it is suboptimal (based on similar arguments in the fourth paragraph in the proof
of Proposition 3). Hence, we know that whenx ∗ = 1 is achieved,y<kis guaranteed under the optimals.
Accordingly, lets∗ be the optimal incentive level, andy ∗(s∗) be the renewable investment induced. It can be
shown that wheny∗(s∗) occurs onW 2(y), which is defined in the proof of Proposition 3, it equals eithery 2 or
ˆy′ 2 .= min{y′ 2,(V′)−1(pr−cr + ¯s)}. Replacingy′ 2 with ˆy′ 2 in the proof of Proposition 3 proves that statement
(ii) continues to hold in this extension. Furthermore, we know that ˆy ′ 2 increases in ¯s, and so doesW 2(ˆy′ 2).
Therefore, the threshold ¯dm decreases in ¯saccording to its definition (withy ′ 2 replaced by ˆy′ 2) in the proof
of Proposition 3. This completes the proof of the sensitivity results in Proposition EC.3(ii).Q.E.D.
Proposition EC.3 indicates that policy support, when operating through the private investment incentives
of renewable investors, may create a trade-off between the timing and carbon intensity of an adaptation trap.
Although stronger policy support promotes renewable capacity investment and reduces the carbon intensity
of AI development, it can simultaneously accelerate the attainment of frontier capability, thereby bringing
forward the onset of the adaptation trap under the market-led scaling scenario.
Nevertheless, we show that stronger policy support can uniformly reinforce the adaptation pathway in the
resource-led scaling scenario.
Proposition EC.4.(i) Statement (i) in Proposition 4 continues to hold if either (a)θ≥ 1+α λ ·cfkand
V′(k)>min{η(c f−pr) + (pr−cr) + (1−b)efξ,pr−cr + ¯s}or (b)V ′ (kf(cf)1+α)>p r−cr + ¯s.
(ii) Otherwise, statement (ii) in Proposition 4 holds. The threshold ¯dc decreases in¯s, whereas the
equilibrium renewable energy investmenty ∗ whend 0< ¯dc is independent of¯s.
Proof of Proposition EC.4.To prove that statement (i) in Proposition 4 holds, we show that under either
of the two conditions identified, only the first case of the developer’s optimal capability choicex ∗ identified
in Proposition 2 can occur given a feasible incentive level; furthermore, the equilibrium renewable capacity
investmenty∗<k. This holds under condition (b) because it implies that the investment thresholdkf(c f)1+α
cannot be achieved by a feasible incentive level. To show the same under condition (a), we follow similar
arguments in the first paragraph of the proof of Proposition 4 ifV ′(k)>η(c f−pr) + (pr−cr) + (1−b)efξ.
Otherwise, we know thatV ′(k)>p r−cr + ¯smust hold, which indicates that there does not exist a feasible
incentivesthat can induce renewable capacity investment at levelk, and thusy ∗<kmust hold as well.
To prove that statement (ii) in Proposition 4 holds when either condition is violated, we follow the proof
of Proposition 4 (from the second paragraph onward) by replacingc r withp r. In particular, notice that
because of the ¯supper bound, the definition of the ¯dc threshold should be changed to ¯dc = min{¯d′(y),∀y∈
[kf(cf)1+α,(V′)−1(pr−cr + ¯s)]}, which decreases in ¯s. However, the equilibrium renewable capacity invest-
ment before the adaptation pathway occurs, that is, the optimaly∗ that occurs onW 1(y) defined in the proof
of Proposition 4, does not change as long asV ′ (kf(cf)1+α)≤p r−cr + ¯s, so that the entireW 1(y) piece is
preserved in the extended model.Q.E.D.

ec6e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
EC.2.2. Intermittency and Renewable Energy Utilization
The main model assumes that the renewable capacity investment is the same as the usable renewable energy
level. In practice, renewable output is stochastic: solar produces nothing at night, and wind may exhibit
multi-day lulls. This extension captures availability explicitly by modeling renewable output per unit of
installed capacity as a random variableA∈[0,1]. The renewable energy used by the AI developer is then
min{Ay,kx 1+α}, so the expected clean share of the developer’s energy consumption equals
˜β(x,y) .=EA
[
min
{ Ay
kx1+α,1
}]
Replacingβ(x,y) in the main model by ˜β(x,y) leads to the extended model.
We focus on a simple two-point distribution in whichA= 1 with probabilityp∈(0,1) andA= 0 with
probability 1−p. This stylized distribution captures the key availability contrast between full and zero
generation and offers tractability. We first characterize the developer’s optimal capability choice and emission
implications under intermittency.
Proposition EC.5.(i) Thex ∗(y)characterizations in Propositions 1 and 2 continue to hold, withc r
replaced by the blended cost˜cr
.=pcr + (1−p)cf in their thresholds.
(ii) In the market-led scaling scenario,E(x ∗(y),y) = 0only ify<y 1.E(x ∗(y),y)increases inyon[y 1,y 2)
and decreases inyon[y 2,k]. However, for anyy ′∈[y 1,y 2)andy ′′∈[y 2,k],E(x ∗(y′),y′)<E(x ∗(y′′),y′′).
(iii) In the resource-led scaling scenario,E(x ∗(y),y)decreases inyify <kf(c f)1+α, increases inyon
[kf(cf)1+α,kf(˜cr)1+α], and is constant thereafter. Furthermore, when 1+α λ < cf cr andf(c r)<1, there
exists a threshold¯psuch thatE(x ∗(k),k)>E(x ∗(0),0)ifp∈(0,¯p).
Proof of Proposition EC.5.To prove (i), note that ˜β(x,y) =p·min { y kx1+α,1 } =p·β(x,y), so the developer’s
expected energy cost equalskx 1+α [cf−(cf−cr)p·β(x,y)] =kx 1+α [cf−(cf−(pcr + (1−p)cf))β(x,y)]. This
is the main model’s energy cost withc r replaced by ˜cr
.=pcr + (1−p)cf. Because ˜cr<cf holds forp∈(0,1),
Propositions 1 and 2 apply under this substitution.
To prove (ii), it can be calculated that under market-led scaling,E(x ∗(y),y) =E 1(y) .=ef(1−p)y, which
increases inywheny∈[y 1,y 2), andE(x ∗(y),y) =E 2(y) .=efk ( 1− py k ) , which decreases inywheny∈[y 2,k].
Furthermore, it can be shown that for anyy ′∈[y 1,y 2) andy ′′∈[y 2,k],E(x ∗(y′),y′) =E 1(y′)<E 1(k) =
E2(k)≤E 2(y′′) =E(x∗(y′′),y′′). Similarly, to prove (iii), it can be calculated that under resource-led scal-
ing,E(x ∗(y),y) =E 3(y) .=ef
(
k(min{f(c f),1})
α+1
−py
)
, which decreases inywheny<kf(c f)1+α. When
y≥kf(c f)1+α,E(x ∗(y),y) =E 1(y) defined above ify≤kf(˜c r)1+α and stays constant atE(x ∗(y),y) =
E1(kf(˜cr)1+α). Finally, whenf(c r)<1,f(c f)<1 must hold, and thus we haveE(x ∗(0),0) =E 3(0) .=
ef·kf(c f)α+1. Moreover,f(˜cr)<1 also holds, soE(x ∗(k),k) =E 1(kf(˜cr)1+α). DenoteE 1(kf(˜cr)1+α) as a
functionE 4(p). It can be calculated thatE 4(p) =E 3(0) whenp= 0. Additionally, whenc r(1 +α)<c fλ,
E′ 4(p)>0 if and only ifp<p m .= cfλ−cr (1+α) (cf−cr )λ <1, indicating thatE 4(p) increases on (0,p m) and decreases
on (pm,1). Furthermore, limp↑1E4(p) = 0<E 4(0). Hence, there must exist a threshold ¯p∈(p m,1) such that
E4(p)>E 4(0) =E 3(0) ifp∈(0,¯p). This completes the proof of Proposition EC.5.Q.E.D.

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec7
Proposition EC.5 shows that intermittency tilts both scaling regimes toward carbon-intensive outcomes.
Under market-led scaling, full decarbonization is unattainable whenever the developer is active. Even in the
coupling zone in which renewable availability disciplines the developer’s capability choice, renewable capacity
fully covers AI’s energy demand only when the resource is available; fossil energy is required otherwise.
The emission-intensifying potential of renewable investment nevertheless remains visible. Once renewable
capacity exceeds the threshold that induces frontier capability, fossil energy is used regardless of realized
renewable output. Although additional renewable capacity reduces emissions within this frontier zone, the
lowest emissions attainable there remain above the highest emissions generated in the coupling zone.
Under resource-led scaling, intermittency weakens, and in some cases reverses, the emission-mitigating role
of renewable capacity. When compute requirements do not scale sufficiently faster than willingness to pay and
intermittency is severe, greater renewable capacity can deepen fossil reliance and produce higher emissions
than in the absence of renewables. The mechanism is that renewable capacity expands capability and can
raise fossil use enough to offset, or even dominate, the clean-energy contribution. In that case, renewable
expansion replicates its role under market-led scaling, functioning primarily as a capability-enabling channel
rather than an emissions-reducing one. The following corollary characterizes when this resemblance arises
for a given degree of intermittency.
Corollary EC.1.In the resource-led scaling scenario, suppose 1+α λ < cf cr andf(c r)<1, as in Proposi-
tion EC.5(iii). Then for any availability probabilityp∈(0,1),E(x ∗(k),k)>E(x ∗(0),0)if 1+α λ < cf (1−p)+crp cr .
Proof of Corollary EC.1.This proof builds upon the proof of Proposition EC.5(iii). Specifically, we can show
that the conditionp<
cfλ−cr (1+α)
(cf−cr )λ is equivalent to 1+α λ < cf (1−p)+crp cr . Thus,E 4 is an increasing function from
0 top, andE 4(p)>E 3(0) is guaranteed.Q.E.D.
Corollary EC.1 suggests that intermittency expands the regime in which renewable expansion may inten-
sify emissions beyond the original market-led scaling scenario in the main analysis. Specifically, without
intermittency, market-led and resource-led scaling are defined based on the comparison betweenλand 1 +α
in the main analysis. The presence of intermittency attenuates the disciplining power of energy cost and
shifts that comparison toλand (1 +α)· cr crp+cf (1−p), which is smaller than 1 +αfor anyp<1.
A direct implication of the above results is that intermittency strengthens the adaptation-trap mechanism
but weakens the adaptation-pathway mechanism. We discuss this insight in detail next. First, we characterize
the policymaker’s renewable capacity decision.
Proposition EC.6.In the market-led scaling scenario, the optimal renewable energy investment deci-
siony ∗ structurally follows Proposition 3, withc r replaced byc rp+c f(1−p)ande f replaced bye fpin its
conditions. Specifically,y ∗<y 2 if condition (a) in Proposition 3(i) holds under this substitution;y ∗ =kif
condition (b) holds under this substitution; and otherwise there exists a threshold ind 0 beyond whichy∗≥y 2,
paralleling Proposition 3(ii).
Proof of Proposition EC.6.The characterization follows directly from the substitutionc r↦→˜cr established in
the proof of Proposition EC.5(i), together with the calculation of expected AI emissions in the frontier zone:
under intermittency, each unit of renewable capacity reduces emissions bye fpinstead ofe f.Q.E.D.

ec8e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
Proposition EC.6 shows that intermittency reinforces the adaptation trap: condition (b) in Proposition 3(i)
becomes more stringent whenc r is replaced by the higher blended cost ˜c r ande f is reduced toe fp. Con-
sequently, a sufficiently high baseline emissions stockd 0 (the condition in Proposition 3) is more likely to
drive the equilibrium into the frontier zone (y ∗≥y 2), in which emissions are higher than in the coupling
zone according to Proposition EC.5(ii). This transition causesd 0 to deteriorate more rapidly and makes
the trap increasingly difficult to escape. Intermittency further extends the risk of an adaptation trap to the
coupling zone: even an equilibrium in this zone can worsend 0 and eventually move the equilibrium into the
higher-emission frontier zone.
Whether greater intermittency, represented by a lowerp, accelerates this transition is generally ambiguous
because two opposing forces are at work. On the one hand, intermittency erodes the cost advantage of
renewables and weakens their ability to relax scaling constraints, thereby delaying entry into the frontier
zone. On the other hand, the same weakening may induce the policymaker to invest more aggressively in
renewable capacity when the incentive to support frontier AI development is sufficiently strong. Numerical
studies suggest that the former/latter force is likely to dominate whenpis large/small.
We derive a similar result for the resource-led scaling scenario to show that the optimal capacity investment
decision structurally follows Proposition 4. Namely, the equilibrium enters the coupling zone in whichy ∗≥
kf(cf)1+α. However, because the coupling zone may lead to higher emissions due to intermittency according
to Proposition EC.5(iii) and Corollary EC.1, this transition may amount to an adaptation trap rather than
a pathway to alleviate carbon dependence.
Renewable Energy Firming:In practice, renewable intermittency can be mitigated through firming
measures such as energy storage and demand response. We capture these measures through a stylized firming
technology that converts the two-point renewable output into a constant, dependable supply ofζ≤punits of
energy per unit of installed capacity. (We assumeζ≤pbecause firming cannot deliver more energy on average
than the resource generates.) We refer toζas the firmed utilization rate. It summarizes the effectiveness of
the firming system, including storage capacity, round-trip efficiency, and the extent to which demand can be
shifted to coincide with renewable availability.
Givenζ, the share of the developer’s energy demand met by renewables equals ˆβ(x,y) = min { ζy kx1+α,1 } .
Replacingβ(x,y) by ˆβ(x,y) leads to the extended model with firming. We solve this model and show that
our main results continue to hold. Proposition EC.7 formalizes the findings.
Proposition EC.7.Assumep= 1.
(i) Statement (i) of Proposition 3 and Proposition 4 continues to hold onceV ′(k)is replaced by 1 ζ·V ′(k ζ ).
(ii) Both the adaptation trap threshold ¯dm in Proposition 3 and the adaptation pathway threshold ¯dc in
Proposition 4 decrease inζ.
Proof of Proposition EC.7.The renewables share function with firming ˆβ(x,y) is equivalent toβ(x,ζy). Hence,
by treatingζyas one variablez, the modified model is equivalent to the base model (with decision variables
{x,z}) except that the renewable investment cost functionV(y) should be replaced by ˆV(z) .=V( z ζ ). Hence,
the proofs of Proposition 3 and Proposition 4 continue to apply to the extended model with the decision

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec9
variableyreplaced byz, the corresponding threshold notation and expressions adjusted accordingly, and
V(y) changed to ˆV(z). In particular, we changeV ′(k) to ˆV′(k) =∂V( z ζ )/∂z|z=k = 1 ζ·V ′(k ζ ). This completes
the proof of Proposition EC.7(i).
To prove Proposition EC.7(ii), we first analyze the sensitivity of the adaptation trap threshold ¯dm in
Proposition 3. A key finding is that ˆV(z)− ˆV(z′ 2) =V( z ζ )−V( z′ 2 ζ ) increases inζfor allz<z 2 (z′ 2 andz 2
defined in the same way asy′ 2 andy 2 in the proof of Proposition 3). Specifically, given the convexity of theV
function, it can be calculated that∂
(
V( z ζ )−V( z′ 2 ζ ) ) /∂ζ= 1 ζ2 ( z′ 2V′(z′ 2 ζ )−zV ′(z ζ ) ) >0. Therefore, ∆W(z) =
W(z)−W 2(z′ 2), which is the counterpart of the ∆W(y) function defined in the proof of Proposition 3 and
equals a term independent ofζminus ˆV(z)− ˆV(z′ 2), decreases inζ. Consequently, the ¯d′′(z) threshold, which
is the counterpart of ¯d′′(y) in the proof of Proposition 3, decreases inζas well, and so does ¯dm, which is the
supremum of ¯d′′(z). Based on similar arguments, we show that ∆W(z), as the counterpart of the ∆W(y)
function defined in the proof of Proposition 4, increases inζ. Hence, the adaptation pathway threshold ¯dc in
Proposition 4 decreases inζaccording to how it is defined in the proof of Proposition 4.Q.E.D.
Proposition EC.7(i) suggests that although firming can restore the carbon-free outcome in the coupling
zone, it is less likely to happen than in the main model (which is a special case withζ= 1), because
imperfect energy utilization increases the marginal investment cost fromV ′(k) to ˆV′(k). In fact, comparing
the coupling condition with and without firming (presented in Proposition EC.7(i) and Proposition EC.6,
respectively) shows that coupling tends to be more challenging to achieve with firming due to the convexity
of the investment cost. The trade-off is that firming mitigates emissions once in the coupling zone. Taken
together, Proposition EC.5(ii) and Proposition EC.7 point to a common conclusion: without firming, full
decarbonization is infeasible; with firming (compared to a dependable utilization rate,p= 1, as a deterministic
benchmark), it must clear a strictly higher marginal-cost hurdle.
Nevertheless, the moderating effect of the utilization rateζcould differ across the market-led and resource-
led scaling regimes. Proposition EC.7 indicates that a higherζuniformly facilitates the adaptation pathway
in the resource-led scaling regime: it not only enlarges the parametric region in which an adaptation pathway
exists (by decreasing 1 ζV′(k ζ ) so the condition in Proposition 4(i) is less likely to hold), but also accelerates
the realization of such a pathway (by reducing the threshold ¯dc). However, a higherζmay not be universally
beneficial in the market-led scaling regime. Notably, although a sufficiently largeζreduces the likelihood
of an adaptation trap (by making the condition in Proposition 3(i) more likely to hold), whenζis not
large enough to eliminate the possibility of a trap altogether, an increase inζcould conversely speed up
the emergence of the trap (by reducing the threshold ¯dm). Although directionally distinct, the effects in the
two scaling regimes stem from the same mechanism: more effective renewable utilization incentivizes more
investment, thereby driving the equilibrium into the carbon-intensive zone in the market-led scaling regime
or the carbon-free zone in the resource-led scaling regime.
EC.3. Technical Details for the Extensions in the Main Text
This section provides formal statements and supporting derivations for the extensions discussed in the main
text. We first characterize how AI-enabled reductions in renewable investment costs affect the conditions
for full decarbonization. We then present the model formulation for the competition extension and outline
the solution approach.

ec10e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
EC.3.1. AI-Enabled Reductions in Clean-Capacity Costs
In this subsection, we formalize the finding that an AI-enabled reduction in renewable investment costs
relaxes the cost requirement for achieving full decarbonization.
Proposition EC.8.Given the renewable investment functionϕ(x)V(y)whereV(y) =g·y µ, Proposi-
tion EC.1 continues to hold if the thresholdsg 1 andg 2 are replaced by g1 ϕ(1) and g2 ϕ(1).
The proof follows that of Proposition EC.1 except for replacinggwithϕ(1)·g.
EC.3.2. Competition Among AI Developers
We provide a detailed model formulation and technical details of the competition extension. We consider
two symmetric developers that engage in capability and price competition by choosing (x1,x 2) first and then
prices (p1,p 2).
Note that this setting extends the main model in two ways: first, the number of developers is increased;
second, an additional pricing decision is introduced. To isolate the effects, we first show that extending the
main model into a price-setting monopoly does not change the results. To meaningfully model the price
decision, we introduce market heterogeneity by assuming the market willingness-to-pay parameterθ ′ is uni-
formly distributed on [0, ˜θ]. The total demand is normalized to 1. Letpdenote the monopolistic developer’s
price decision. Accordingly, customers invest ifθ ′xλ≥p, indicating that the market demand equals ˜θ−px−λ ˜θ ,
and the developer’s profit function becomes ˜Π(x,y,p) =p ˜θ−px−λ ˜θ − ( β(x,y)cr + ( 1−β(x,y) ) cf ) kx 1+α.Opti-
mizing this function over the price decision leads to ˜Π∗(x,y) = maxp≥0 ˜Π(x,y,p) = ˜θ 4xλ− ( β(x,y)cr + ( 1−
β(x,y)
)
cf
)
kx 1+α. Observe that ˜Π∗(x,y) is the same as the developer’s profit function Π(x,y) formulated in
the main model, except thatθis replaced by ˜θ/4. Therefore, we shall set ˜θ= 4θin this extension to equate
the equilibrium outcome from the price-setting monopoly and the main model so as to isolate the impact of
competition.
We are now ready to formulate the duopoly extension. Letyi be the amount of renewable investment capac-
ity that developeri= 1,2 has access to. First consider the pricing stage: given (x 1,x 2) (wherex 1>x 2 without
loss of generality) and (p1,p 2), customers invest inx 1 if their willingness to pay satisfiesθ′xλ 1−p 1≥θ′xλ 2−p 2,
which leads toθ ′≥ p1−p2 xλ 1−xλ 2 . Furthermore, for customers to make an investment,θ ′xλ 2−p 2≥0 should be satis-
fied, which givesθ ′≥p 2x−λ 2 . Hence, letC(x,y) .= ( β(x,y)cr + ( 1−β(x,y) ) cf ) kx 1+α denote the energy cost
under a given (x,y); then developer 1’s profit function equals Π1(x1,y 1,p 1,p 2) =p 1
(
˜θ− p1−p2 xλ 1−xλ 2
)
/˜θ−C(x 1,y 1).
Developer 2’s profit function equals Π 2(x2,y 2,p 1,p 2) =p 2
(
p1−p2
xλ 1−xλ 2 −p 2x−λ 2
)
/˜θ−C(x 2,y 2). Maximizing these
two profit functions together leads to a price equilibrium:p ∗ 1 = 2xλ 1(xλ 1−xλ 2)˜θ 4xλ 1−xλ 2 , andp ∗ 2 = xλ 2(xλ 1−xλ 2)˜θ 4xλ 1−xλ 2 . We plug
the price equilibrium into the developers’ profit functions and analyze the capability-choice equilibrium. This
part of the analysis becomes analytically intractable. We resort to an extensive numerical study, which leads
to the results shown in Section 7.2.
EC.4. Proofs of Analytical Results
For convenience, we rewrite the developer’s profit in equation (2) as follows: Letπ(x) .=θx λ−c·(kx 1+α).
The developer’s profit equalsπ(x) wherec=c r ifkx 1+α≤y(i.e., AI energy demand can be fully covered

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec11
by renewable sources). We denote this piece byπ cr(x). Otherwise, it equalsπ(x) wherec=βc r + (1−β)c f,
whereβ= y kx1+α ; this function can be rewritten asθx λ−cf·(kx 1+α) + (cf−cr)y, which we denote byπ cf (x).
Proof of Proposition 1.The special case of this proposition in whichλ= 1 +αcan be proven by setting
y1 =y 2 = 0 ifθ≥c fk, settingy 1 =y 2 =k+ 1 ifθ≤c rk, and settingy 1 = 0,y2 =k+ 1 ifθ∈(c rk,cfk).
To prove this proposition for the case in whichλ>1 +α, we first introduce two thresholds onθ: The
first threshold is defined as ¯θ .= (α+1)cfk λ . The second threshold, denoted by ¯¯θ, is defined as follows: Consider
the functionF(θ) =−
(
(cf−cr)k
λ
−α+λ−1
(cr
θ
) α+1
−α+λ−1
)
+cfk−θ. It can be shown thatF ′′(θ)<0, indicating
thatFis concave and thus can have at most two zeros. It can be verified that one of them isc rkbecause
F(crk) = 0. Denote the other zero, if it exists, by ¯¯θ.
We start by proving Proposition 1 for the case in whichα= 0. In this case,π′′(x)≥0 under the assumption
thatλ>1 +α= 1, indicating thatπ(x) is convex and achieves its maximum at the boundary points. As
such, we analyze two sub-cases.
•The first sub-case is one in which cr cf < 1+α λ andθ∈ ( ¯θ, ¯¯θ ) . Definey 0 1 .=k λ −α+λ−1 (cr θ ) α+1 −α+λ−1 . We also
introduce another thresholdy 0 2: Consider the functionG(y) =θ ((y k ) λ α+1−1 ) −cfk (y k−1 ) . It can be
shown thatG ′′(y)>0, indicating that the function is convex. Furthermore, it can be verified that
G(k) = 0 andG′(k)>0 whenθ> ¯θ. This implies that in the first sub-case,G(y) has another zero that
is strictly smaller thank; denote that zero byy 0 2. Hence,G(y)<0 if and only ify∈(y 0 2,k).
We further prove thaty 0 1<y 0 2. We prove this by showing thatG(y 0 1)>0. It can be shown thatG(y 0 1) =
F(θ). We show that∀θ∈( ¯θ, ¯¯θ),F(θ)>0 is satisfied. We show this in two steps. First, we show that
F(θ)>0∀θ∈(c rk, ¯¯θ). This is because when cr cf < 1+α λ , it can be calculated thatF ′(crk)>0 and
limθ→∞F(θ)<0, indicating that ¯¯θexists and is greater thanc rk, andF(θ)>0 if and only ifθ∈(c rk, ¯¯θ).
Second, we show thatc rk< ¯θ< ¯¯θand thus ( ¯θ, ¯¯θ)⊂(c rk, ¯¯θ). The inequalityc rk< ¯θdirectly follows from
the condition that cr cf < 1+α λ . To show ¯θ< ¯¯θ, we analyzeF( ¯θ). It can be shown thatF( ¯θ) = 0 when
cr =
cf (1+α)
λ ; furthermore, it can be calculated thatF( ¯θ) is strictly decreasing inc r given cr cf < 1+α λ and
λ>1 +α. This indicates thatF( ¯θ)>0 and, in turn, ¯θ< ¯¯θholds,∀c r< cf (1+α) λ . This completes the
proof thaty 0 1<y 0 2 in this sub-case. Accordingly, we can show the following.
— Wheny < y 0 1, it can be shown that (i)π cr(0)> π cr
(
(y/k) 1/(1+α)) , and (ii)π cf (1)<
πcf
(
(y/k) 1/(1+α)) , indicating that the optimal technology choice isx= 0 due to the convexity of
the functionsπ cr andπ cf . To prove (i), consider the functionJ(y) =π cr
(
(y/k) 1/(1+α)) −πcr(0). It
can be shown thatJ ′′(y)>0 and thatJ(y) has two zeros,y= 0 andy=y 0 1. Hence, if and only if
y∈(0,y 0 1),J(y)<0, and thus (i) holds. To prove (ii), note thatπ cf
(
(y/k) 1/(1+α)) −πcf (1) is the
G(y) function introduced above. BecauseG(y)>0∀y<y 0 2 andy 0 1<y 0 2, (ii) is proven.
— Based on the above observations, we know that wheny∈[y 0 1,y 0 2), (i)π cr(0)≤π cr
(
(y/k) 1/(1+α)) ,
and (ii)π cf (1)< πcf
(
(y/k) 1/(1+α)) , indicating that the optimal technology choice isx=
(y/k) 1/(1+α).
— Similarly, wheny≥y 0 2, we have (i)πcr(0)<π cr
(
(y/k) 1/(1+α)) , and (ii)π cf (1)≥π cf ( (y/k) 1/(1+α)) ,
indicating that the optimal technology choice isx= 1.

ec12e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
Hence, settingy 1 =y 0 1 andy 2 =y 0 2 proves Proposition 1 in the first sub-case.
•We then consider the second sub-case in which the condition in the first sub-case is not met.
— (A) If cr cf < 1+α λ andθ≤ ¯θ, thenG ′(k)≤0, indicating thatG(y)≥0 and, accordingly,
πcf
(
(y/k) 1/(1+α)) ≥π cf (1) holds∀y∈[0,k]. Hence, settingy 1 =y 0 1 andy 2 =kproves the
proposition.
— (B) If cr cf < 1+α λ andθ≥ ¯¯θ, thenG(y 0 1) =F(θ)≤0, which indicates thaty 0 1∈(y 0 2,k). In that case,
the solutionx= (y/k) 1/(1+α) is suboptimal. Hence, settingy 1 =y 2 = cfk−θ cf−cr proves the proposition,
because it can be shown thatπ cr(0)>π cf (1) if and only ify<
cfk−θ
cf−cr .
— (C) If cr cf ≥ 1+α λ , it can be shown that ¯¯θ≤c rk, and thusF(θ)>0 if and only ifθ∈( ¯¯θ,crk).
∗(C-i) Ifθ≥c rk, thenF(θ)≤0, that is,G(y 0 1)≤0, which is the situation discussed in (B).
∗(C-ii) Ifθ<c rk, it can be shown thaty 0 1 >k, indicating thatJ(y)≤0 and, accordingly,
πcr(0)≥π cr
(
(y/k) 1/(1+α)) ∀y∈[0,k]. Hence, the solutionx= (y/k) 1/(1+α) is also suboptimal.
Hence, applying the approach in (B) and settingy 1 =y 2 =
cfk−θ
cf−cr proves the proposition.
We then analyze the case in whichα>0. It can be shown thatπ ′′(x)<0 ifx≤ ( θ(λ−1)λ α(α+1)ck ) 1 α−λ+1 , and
π′′(x)≥0 otherwise, indicating thatπ(x) is concave first and then becomes convex asxincreases. Further-
more, it can be calculated thatπ ′(x)<0 forxsufficiently small (becauseλ−1>αin this case). These
observations indicate thatπ(x) continues to achieve its maximum at the boundary points, and the arguments
used to analyze the case in whichα= 0 continue to apply.Q.E.D.
Proof of Proposition 2.First, consider the case in whichλ≤1. In this case,π ′′(x) =θ(λ−1)λx λ−2−
α(α+ 1)ckxα−1≤0, indicating that the functionπ(x) is concave. Hence, the global maximum ofπ(x) is
achieved at its stationary point. It can be shown that wheny>k
(
θλ
(1+α)crk
) 1+α
1+α−λ
, the first pieceπ cr(x)
achieves its global maximum (if it is less than 1), and the second pieceπ cf (x) decreases. For anyy∈[
k
(
θλ
(1+α)cfk
) 1+α
1+α−λ
,k
(
θλ
(1+α)crk
) 1+α
1+α−λ
]
, the first/second piece increases/decreases, and thus the maximum
is achieved at the break point at whichx=
(y
k
) 1
1+α . For anyy<k ( θλ (1+α)cfk ) 1+α 1+α−λ , the first piece increases,
and the second piece achieves its global maximum (if it is less than 1). Incorporating the boundary constraint
thatx≤1 leads to Proposition 2 for this case.
We then consider the case in whichλ >1. In this case, it can be shown thatπ ′′(x)≥0 ifx <(
λ(λ−1)θ
α(1+α)ck
) 1
1+α−λ
andπ ′′(x)<0 otherwise, indicating thatπis convex first and then becomes concave as
xincreases. Furthermore,π ′(x) =θλx λ−1−(α+ 1)ckx α>0 forxsufficiently small (becauseλ−1<αin
this case), indicating thatx= 0 cannot be the maximum. Therefore,π(x) continues to achieve its global
maximum at a stationary point, and thus the arguments used in the previous case continue to apply.Q.E.D.
Proof of Proposition 3.Recall they 1 andy 2 thresholds identified in Proposition 1. WhenV ′(k)≤η(c f−
cr) + (1−b)efξ, it can be shown that eithery ∗<y 2 ory ∗ =k, in which casek(x ∗(y∗))1+α≤y∗ is satisfied,
indicating thatE(x ∗(y∗),y∗) = 0 always holds. To show this, assume thaty ∗∈(y 2,k). Then, according to
Proposition 1,x∗(y∗) = 1. Plugging this solution into the policymaker’s welfare function, we obtainW(y ∗) =
η(−cf(k−y ∗)−c ry∗ +θ)−ξ(1−b)(d 0 +ef(k−y∗))−V(y ∗). It can be calculated thatW ′(y∗) =η(cf−cr) +

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec13
ξ(1−b)e f−V ′(y∗). BecauseV(y) is convex andy ∗<k, we haveV ′(y∗)<V ′(k)≤η(c f−cr) + (1−b)e fξ,
indicating thatW ′(y∗)>0, which contradicts the optimality ofy ∗ as an interior solution.
Whenθ≤max{ 1+α λ ·cfk,crk}, two sub-cases arise: (i) cr cf < 1+α λ andθ≤ 1+α λ cfk, which is the ¯θthreshold
defined in the proof of Proposition 1, and (ii) cr cf ≥ 1+α λ andθ≤c rk. Case (i) corresponds to situation (A)
discussed in the second sub-case in the proof of Proposition 1, in whichy 2 =kand thus the third scenario
ofx∗ in Proposition 1 does not materialize. Hence,k(x ∗(y∗))1+α≤y∗ always holds. Case (ii) corresponds to
situation (C-ii) discussed in the proof of Proposition 1. In that case, it can be shown that becauseθ<c rk,
y1 =y 2 =
cfk−θ
cf−cr >k, indicating thatx ∗ = 0∀y∈[0,k]. Hence,k(x ∗(y∗))1+α≤y∗ always holds as well.
Combining the above two paragraphs proves Proposition 3(i).
Next, consider the case in which neither condition in Proposition 3(i) holds. This corresponds to either
the first sub-case, or situations (B) and (C-i) in the second sub-case discussed in the proof of Proposition 1.
In all of these cases, the third scenario ofx ∗ in Proposition 1 can materialize whenyis sufficiently large,
in particular, wheny=k. Hence,W(k), that is, the welfare function wheny=k, should be calculated by
plugging inx ∗(k) = 1. Based on the calculation in the first paragraph of this proof, we know that when
V′(k)>η(c f−cr) + (1−b)efξ,W ′(k)<0, implying thaty ∗<k. Ify 2≤0, then according to Proposition 1,
k(x∗(y))1+α>yholds for ally∈[0,k). Setting ¯dm to be any negative number proves Proposition 3(ii).
Ify 2>0, thenW(y) can be formulated as a piecewise function containing at least two pieces: The last
piece corresponds to theyrange of [y 2,k], in whichx ∗(y) = 1; we denote this piece byW 2. At least one other
piece corresponds to the first or second case of thex ∗ solution identified in Proposition 1. We show thaty ∗
occurs onW 2(y) if and only ifd 0 is sufficiently large. It can be calculated thatW ′′ 2 (y)<0, indicating that
W2(y) is a concave function. Hence, ify ∗ occurs onW 2(y), theny ∗ equals either the stationary point at
whichW ′ 2(y) = 0 (denoted byy′ 2) or the endpointy 2 (becausey ∗<k, as shown in the previous paragraph).
•Ifη(c f−cr)+(1−b)e fξ−V ′(y2)>0 (a condition independent ofd 0 becausey 2 is the zero of a function
that is independent ofd 0; see the proof of Proposition 1), thenW 2(y′ 2)>W 2(y2). Hence,y ∗ occurs on
W2(y) if and only ifW(y)≤W 2(y′ 2) holds for anyy<y 2. It can be calculated that for anyy≤y 2,
∂(W(y)−W 2(y′ 2))
∂d0 equals either−bξ(if the first case ofx ∗ in Proposition 1 materializes undery, i.e.,x ∗(y) =
0) or−bξ
(
1−
(y
k
) 1
α+1
)
(if the second case ofx ∗ in Proposition 1 materializes, i.e.,x ∗(y) = (y k)1/(1+α)).
Because condition (a) in Proposition 3(i) does not hold, we knowy 2<kaccording to the proof of
Proposition 1 (see the first sub-case, and situations (B) and (C-i) in the second sub-case). Hence,y<y 2
implies thaty<k. Consequently, both derivatives calculated above are negative for anyy<y 2 given
b>0 (and are independent ofd 0), indicating thatW(y)−W 2(y′ 2) is a strictly decreasing linear function
ind 0. Hence, ify∗ occurs onW 2(y) under somed′, then the same happens under anyd′′>d′, indicating
that either Proposition 3(i) or (ii) holds. To show that Proposition 3(ii) holds in this case, define
∆W(y) =W(y)−W 2(y′ 2) whend 0 = 0 for anyy<y 2. Define ¯d′′(y) = max{0,∆W(y)/| ∂(W(y)−W 2(y′ 2)) ∂d0 |},
which is finite for anyy<y 2<k. By definition,W(y)<W 2(y′ 2) whend 0> ¯d′′(y). Let ¯¯d′′ = supy<y2 ¯d′′(y).
Then, whend 0> ¯¯d′′,W(y)<W 2(y′ 2)∀y<y 2, and thusy ∗ =y′ 2, indicating that Proposition 3(ii) holds
in this sub-case if we set ¯dm = ¯¯d′′.

ec14e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
•Ifη(c f−cr) + (1−b)efξ−V ′(y2)≤0, thenW 2(y′ 2)≤W 2(y2). Replacingy′ 2 byy 2 in the arguments used
in the previous bullet point proves Proposition 3(ii) in this sub-case.Q.E.D.
Proof of Proposition 4.First, consider the conditions in Proposition 4(i):θ≥ 1+α λ cfkindicates that
k
(
θλ
(1+α)cfk
) 1+α
1+α−λ
≥k(i.e.,f(c f)≥1) givenλ<1 +α. In that case,x ∗(y) = 1∀y∈[0,k] according to Propo-
sition 2. Pluggingx ∗(y) = 1 into the welfare function leads to a function that we denote by ¯W1(y). It can
be calculated that ¯W′′ 1 (y)<0, indicating that ¯W1(y) is a concave function. It can be calculated that when
V′(k)>η(c f−cr) + (1−b)e fξ, ¯W′ 1(k)<0 and thusy ∗<k. Hence,k(x ∗(y))1+α =k>y ∗ for anyd 0. This
proves Proposition 4(i).
Next, consider the case in which the condition of Proposition 4(i) is violated. Assume the first condition
holds, yet the second condition does not, that is,θ≥ 1+α λ cfkandV ′(k)≤η(c f−cr) + (1−b)efξ. In this case,
y∗ =kbased on the analysis in the previous paragraph. Hence, setting ¯dc = 0 proves Proposition 4(ii).
Assume the first condition is violated, that is,θ< 1+α λ cfk, indicating thatk ( θλ (1+α)cfk ) 1+α 1+α−λ <k, i.e.,
f(cf)<1. In this case, the welfare functionW(y) can be formulated as a piecewise function containing
at least two pieces: The first piece corresponds to theyrange of [0,k
(
θλ
(1+α)cfk
) 1+α
1+α−λ
), in whichx ∗ =
(
θλ
(α+1)cfk
) 1
1+α−λ
; we denote this piece byW 1. At least one other piece corresponds to the second or the third
case of thex ∗ solution identified in Proposition 2. We show thaty ∗ occurs onW 1(y) if and only ifd 0 is
sufficiently small. It can be calculated thatW ′′ 1 (y)<0, indicating thatW 1(y) is a concave function. Hence,
ify∗ occurs onW 1(y), theny ∗ equals either the stationary point at whichW ′ 1(y) = 0 (denoted byy′ 1) or the
endpointy= 0.
•IfV ′(0)< η(c f −c r) + (1−b·f(c f))efξ(a condition independent ofd 0), thenW 1(y′ 1)>
W1(0). Hence,y ∗ occurs onW 1(y) if and only ifW(y)≤W 1(y′ 1) holds for anyy≥
k
(
θλ
(1+α)cfk
) 1+α
1+α−λ
. It can be calculated that for anyy≥k
(
θλ
(1+α)cfk
) 1+α
1+α−λ
, ∂(W(y)−W 1(y′ 1)) ∂d0 equals either
bξ
((y
k
) 1
α+1− ( θλ (1+α)cfk ) 1 α−λ+1 ) (if the second case ofx ∗ in Proposition 2 materializes, i.e.,x ∗(y) =
(y k)1/(1+α)) orbξ
((
min{ θλ (1+α)crk,1} ) 1 α−λ+1 − ( θλ (1+α)cfk ) 1 α−λ+1 ) (if the third case ofx∗ in Proposition 2
materializes, i.e.,x ∗(y) = min{f(cr),1}). Both derivatives are positive for anyy≥k ( θλ (1+α)cfk ) 1+α 1+α−λ
givenk
(
θλ
(1+α)cfk
) 1+α
1+α−λ
<kandb>0 (and are independent ofd 0), indicating thatW(y)−W 1(y′ 1) is
a strictly increasing linear function ind 0. Hence, ify ∗ occurs onW 1(y) under somed ′, then the same
happens under anyd ′′<d′, indicating that either Proposition 4(i) or (ii) holds. To show that Proposi-
tion 4(ii) holds in this case, define ∆W(y) =W(y)−W 1(y′ 1) whend 0 = 0 for anyy≥k ( θλ (1+α)cfk ) 1+α 1+α−λ .
Define ¯d′(y) = max{0,−∆W(y)/ ∂(W(y)−W 1(y′ 1)) ∂d0 }. By definition, whend 0> ¯d′(y),W(y)>W 1(y′ 1), which
implies thaty ∗ no longer occurs onW 1(y). Setting ¯dc = min{ ¯d′(y),∀y≥k ( θλ (1+α)cfk ) 1+α 1+α−λ }proves
Proposition 4(ii) in this sub-case.
•IfV ′(0)≥η(c f−cr) + (1−b·f(c f))efξ, thenW 1(y′ 1)≤W 1(0). Replacingy ′ 1 byy= 0 in the arguments
used in the previous bullet point proves Proposition 4(ii) in this sub-case.Q.E.D.

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec15
EC.5. Calibration and Computational Details
This section maps observable inputs into the parameter values used in Instances A–C (Instance D combines
the Instance A market size with the Instance C technology and cost parameters). We proceed in three steps.
First, we estimate the market-side relationship between investment and model capability to discipline the
demand parameters. Second, we calibrate the technology scaling relationship linking capability to electricity
use and anchor instance-specific energy-demand levels. Third, we set energy costs, emissions intensity, and
the renewable investment cost function.
EC.5.1. Market-Side Calibration
We estimate the willingness-to-pay elasticityλby regression. Letwdenote market willingness-to-pay. The
power laww=θx λ is equivalent to logw=λlogx+ logθ. For each instance, we assemble three annual
observations of (w,x) from AI investment and model capability measures for the U.S., China, and EU over
2023–2025, summarized in Table EC.1.
Table EC.1 Investment and Model Capability by Region, 2023–2025
United States China European Union
Year Invest. MMMU Invest. MMMU Invest. MMMU
2025 285.88 85.4 76.25 80.1 20.92 62.5
2024 109.08 78.2 9.29 70.3 19.42 52.5
2023 67.22 59.4 7.76 45.9 11.00 45.6
Notes:Investment is in billions of USD. MMMU scores reflect
the top-performing model in each region-year. See text for model
names and data sources.
We construct the investment inputs in Table EC.1 as follows. The 2023, 2024, and 2025 figures follow
Maslej et al. (2024), Maslej et al. (2025), and Sajadieh et al. (2026), respectively. 3,4,5 The only exception is
China’s investment figure: Sajadieh et al. (2026) acknowledge that their reported number may understate the
investment in China. For example, the Quid database, on which the estimate in Sajadieh et al. (2026) is based,
does not include internal R&D spending of domestic tech giants. Hence, we adopt another source and estimate
the investment value to be 125×0.61≈76.25, where 125 billion USD is the total AI investment in China
in 2025 and 61% is attributed to private investment. 6 We use private investment to maintain comparability
with the other investment measures, which are based on private-sector activity. We validate this estimate by
collecting major Chinese companies’ AI investment in 2025, including Alibaba (RMB120 billion)7, ByteDance
3https://hai.stanford.edu/ai-index/2024-ai-index-report/economy. Figure 4.3.10.
4https://hai.stanford.edu/ai-index/2025-ai-index-report/economy. Figure 4.3.10.
5https://hai.stanford.edu/ai-index/2026-ai-index-report/economy. Figure 4.2.11.
6https://www.secondtalent.com/resources/chinese-ai-investment-statistics/
7https://www.alibabagroup.com/en-US/document-1930116148192346112

ec16e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
(RMB150 billion)8, Tencent (RMB18 billion)9. Summing up these numbers and also including (partially) the
R&D expenditure of other companies that have heavily invested in AI (such as Huawei, Xiaomi, JD.com, and
Baidu)10, we estimate the corporate investment in AI in China in 2025 to be approximately RMB380–460
billion ($56-$68 billion). Combining this number with the Quid-based figure reported by Sajadieh et al. (2026)
gives$68.41–80.41 billion, which is consistent with the$76.25 billion figure estimated from the other source.
Model capability is measured by MMMU. The MMMU scores adopted for Instances A and B in Table EC.1
are based on the highest MMMU (Val) evaluation reported for U.S.- and China-developed models in the
corresponding year.11 The MMMU scores in Instance C are based on the performance of Mistral AI models
reported in 2024 12 and 2025. 13 No MMMU scores have been reported for Mistral’s 2023 models such as
Mistral 7B Instruct. Mistral 7B Instruct achieved a score of 60.1 in the MMLU benchmark, 14 while Pixtral
12B achieved 69.2. 15 Assuming the same percentage increase in MMLU and MMMU scores between these
two models, we estimate the MMMU score of Mistral 7B Instruct to be 45.6.
We setwto be the investment amounts andxto be the MMMU scores (normalized by 100 to lie in its
range [0,1]), and perform a linear regression for each instance. This yields aλvalue of 3.46, 3.19, and 1.98.
Three observations per region leave one residual degree of freedom, so these point estimates carry sub-
stantial statistical uncertainty. Table EC.2 reports the OLS standard errors and 95% confidence intervals:
no regional estimate rejects either scaling regime at conventional levels (each|t|<0.7 against the estimated
threshold 1 +α≈2.47), and the threshold estimate itself is imprecise. Two measurement caveats compound
the statistical one: the 2025 China figure is taken from an alternative total-investment source and validated
against an AI-Index-based component combined with a corporate-investment estimate constructed from com-
pany disclosures (see above), and compression of MMMU scores near the benchmark’s ceiling mechanically
understates late capability growth, inflating both estimated exponents. We therefore treat the estimates as
anchors for scenario construction rather than as measured classifications.
A further identification concern is that investment proxies the level of anticipated willingness to pay rather
than the willingness-to-pay function itself. Writing the proxy asw t =θtxλ t , the time-series slope estimates
λ+ ∆ logθt/∆ logxt, and the 2023–2025 expansion of market breadth (θt) biases investment-based estimates
upward. Price-based estimators drift in the opposite direction under intensifying competition and penetration
pricing, and within-year price-on-capability regressions are unstable because current prices are strategic
8https://www.reuters.com/technology/bytedance-plans-20-billion-capex-2025-mostly-ai-sources-s
ay-2025-01-23
9https://static.www.tencent.com/uploads/2026/03/18/2804dbdae364ca25b82d21bc8304f1d3.pdf
10The total R&D expenditures of these companies are Huawei (RMB192.3 billion), Xiaomi (RMB33.1 billion),
JD.com (RMB22.2 billion), and Baidu (RMB20.4 billion). Assuming 35%–65% of these R&D investments go to AI
leads to the estimated range reported above.
11https://mmmu-benchmark.github.io/
12https://mistral.ai/news/pixtral-12b
13https://llm-stats.com/models/mistral-small-3.2-24b-instruct-2506
14https://docsbot.ai/models/compare/mistral-large/mistral-7b-instruct
15https://llm-stats.com/models/pixtral-12b-2409

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec17
Table EC.2 Uncertainty and Alternative Estimators for the Market-Scaling Exponent
ˆλ(s.e.) 95% CI Investment-based Price-based a
United States 3.46 (1.79) (−19.3,26.2) market-led market-led
China 3.19 (2.98) (−34.6,41.0) market-led resource-led
European Union 1.98 (1.02) (−11.1,15.0) resource-led market-led
Threshold 1 +α2.47 (0.42) (−2.9,7.8) –
Notes:OLS on three annual observations per regression (one residual degree of free-
dom); confidence intervals uset 0.975,1 = 12.71.
a Classifications implied by fitting model prices over time, as examined in a conference
discussion of this paper and reported here as indicative pending a formal estimation;
within-year price-on-capability regressions are sample-dependent (below the threshold
for the most-used models, near it for frontier models).
objects: frontier models are often free to consumers, and less expensive models sometimes outperform more
expensive ones. As Table EC.2 reports, willingness-to-pay estimators built from model prices reverse the
China and EU classifications while agreeing with the U.S. classification. We conclude that the U.S. market-
led classification is robust across estimators, while the China and EU classifications are not determined by
presently available data. This does not disturb the analysis: the four case-study instances span both scaling
regimes by construction, so reclassifying a region relocates it among instances whose equilibria are already
characterized.
Looking ahead,λbecomes identifiable as the market matures: price-capability gradients along iso-share
curves (hedonic regressions that control for market position), or discrete-choice estimation on model usage
shares, prices, and capability indices, recover willingness to pay for capability from substitution patterns
rather than from spending. We view this as a measurement agenda that the model motivates once prices
decouple from investor subsidies.
The regression analysis also provides an estimate ofθ($371.24,$74.44,$57.57 billion for the three instances,
respectively), but it aggregates market conditions across 2023–2025 and does not target the 2024 conditions
that underlie the remaining parameter choices. We therefore anchorθto the 2024 investment levels. A literal
application ofw=θx λ would recoverθas w xλ . We do not take this route because aggregate AI investment is
best viewed as a proxy for the scale of anticipated market opportunity rather than as a direct observation
ofθx λ. This difference affects the slope (λ) and level (θ) parameters differently. For example, multiplying
all investment observations by the same factor does not change theλestimate, whereas it can scale the
θestimate proportionally. Hence, directly dividing investment figures byx λ would impose more structure
than the data can support. Instead, anchoringθ, a market-potential parameter, directly to observed 2024
investment yields a transparent and economically interpretable measure of market scale. Accordingly, we set
theθvalues in Instances A and C to be the amounts of private AI investment in the U.S. and the EU in
2024 reported by Maslej et al. (2025). 4 For Instance B, we augment the estimate by Maslej et al. (2025)
with a potential corporate-investment component. Specifically, we adopt the lower-end estimate of the 2025
corporate investment ($56 billion, as estimated above) and scale it down using the 129.9% growth in total

ec18e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
AI investment between 2024 and 2025 reported by Sajadieh et al. (2026), 5 which implies a corporate AI
investment potential of approximately$24.36 billion in 2024. Adding this amount to the Quid-based estimate
of$9.29 billion yields a total investment potential estimate of approximately$33.65 billion.
There are multiple estimates of the total economic value of Generative AI. It has been widely agreed
that AI can increase productivity and contribute to economic growth in other industries. Goldman Sachs
estimated that AI could lead to$7 trillion in global GDP growth over 10 years. 16 Acemoglu (2025) provided
a lower estimate of a 1.6% increase in global GDP for the same 10-year horizon, or about$183.78 billion per
year. We take the average of these two estimates and calculate that the annual economic spillover of AI is
approximately$441.89 billion. We divide that number by the revenue potential of the AI industry. To match
the economic value potential estimate that aggregates multi-year conditions, we adopt the regression-based
θestimate reported in the previous paragraph as a reasonable proxy of the annual revenue potential of the
AI industry within the comparable time frame. This yieldsη= 441.89/(371.24 + 74.44 + 57.57) + 1≈1.88.
The next subsection calibrates the technology scaling relationship between capability and energy use.
EC.5.2. Scaling and Energy Demand
We calibrate the technology scaling parameterαvia regression. Letvdenote the AI energy usage. The
functionv=kx 1+α is equivalent to the linear function logv= (1 +α) logx+ logk. We consider three sets of
(v,x) estimates in 2024, summarized in Table EC.3.
Table EC.3 Data-Center Electricity Consumption and Model Capability by Region, 2024
United States China European Union
Data-center electricity (TWh) 177.51 115.42 63.51
MMMU score 78.2 70.3 52.5
The energy consumption figures are based on estimates reported in Figure 2.12 by the International Energy
Agency (IEA 2025) 17. These figures measure data-center electricity consumption across all workloads rather
than AI alone: AI is the principal driver of recent growth, but it is one workload among several. We there-
fore treat them as anchoring magnitudes for the energy-demand scalekrather than as measurements of
AI-only demand. The MMMU scores are the same as those shown in Table EC.1. Linear regression based on
these estimates yields anα≈1.467. This three-point estimate carries the same caveat as theλregressions
(Table EC.2). The power-law form and curvature of the technology side are, however, documented inde-
pendently and densely in the scaling-law literature (Kaplan et al. 2020; Hoffmann et al. 2022), whereas the
market exponent has no comparable corroboration; we therefore concentrate scenario uncertainty inλ. Two
further caveats apply. First, the procedure is two-step: the pooled regression identifies the slope under a com-
mon intercept, and the region-specifickvalues are then re-anchored, soαis best read as a common-curvature
assumption disciplined by cross-regional variation rather than a jointly identified parameter. Second, log-log
16https://www.goldmansachs.com/insights/articles/generative-ai-could-raise-global-gdp-by-7-perce
nt
17https://iea.blob.core.windows.net/assets/de9dea13-b07d-42c5-a398-d1b3ae17d866/EnergyandAI.pdf

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec19
slopes depend on the benchmark’s origin: MMMU is multiple-choice with a chance floor near 25, and re-
anchoring scores at that floor yields materially smaller exponents (about 1.5 rather than 2.5 for 1 +α, with
λfalling commensurately) while preserving all three regime labels.
Although the regression analysis also provides akestimate, it does not account for the regional energy
usage differences that we intend to capture through the different instances in the case study. To reflect such
heterogeneity, we anchor thekestimate in each instance based on the actual energy consumption in the
corresponding region. Specifically, we calculatekas v x1+α wherevandxare the energy consumption and
MMMU score shown in Table EC.3, and obtain 325.6 TWh, 275.32 TWh, and 311.32 TWh for Instances
A–C, respectively.
The next subsection sets energy cost, emissions, and renewable investment parameters.
EC.5.3. Energy Costs, Emissions, and Renewable Investment
We setc r to be the lowest cost of a renewable PPA with 80% hourly matching, which is approximately 50,
48, and 65 USD per MWh according to Figure 2.19 by IEA (2025). 17
We estimatec f based on the industrial retail price range of grid electricity reported in Figure 2.19 by
IEA (2025). 17 This range is about [79.27,93.90], [87.80,150], and [109.76,200] for the U.S., China, and EU,
respectively (all numbers are in USD/MWh). Considering that the European range covers the entire EU
and thus may be an overestimate of the volatility of the industrial rates in data-center hubs, we instead
focus on the grid rates in Frankfurt, which has the highest concentration of data centers in Europe. The
wholesale rates to data centers in Frankfurt are reported to be€110–€135/MWh, 18 which lead to a range in
USD/MWh of approximately [125.13,153.63]. Consistent with the model’s interpretation ofc f andc r as unit
generation costs, we proxy both by observed procurement prices (grid rates and PPA prices, respectively).
Because the two sources are proxied symmetrically and the analysis operates mainly through the difference
cf−cr, a common retail margin largely nets out. We assume a uniform distribution of the grid rate, denoted
byr g, in the ranges defined above. To reflect developers’ risk aversion to grid rate volatility, we adopt a
mean-variance cost based on the following formula:c f =E[rg] + 0.1 Var(rg), where the coefficient 0.1 carries
units of MWh per USD so that the adjustment is expressed in USD/MWh. Accordingly, we can calculatec f
to be approximately 88, 151, and 146 USD per MWh in the three instances, respectively.
We next calibrate the renewable investment cost functionV(y). In practice, renewable-investment costs
may exhibit different curvature across the deployment path: learning, standardization, and economies of scale
can initially reduce marginal costs, whereas increasingly constrained siting, longer interconnection distances,
and the need for transmission and grid expansion can eventually cause marginal costs to rise. Because our
analysis focuses on the additional renewable capacity required to support future AI growth, we model only the
emerging convex segment. We adopt a power-law formula for this cost function:V(y) =g·y µ. The calibration
is based on solar farm investment costs in practice. To estimateµ, we collect investment information on
major solar projects in China in recent years, summarized in Table EC.4. Accordingly, it can be calculated
18https://techplustrends.com/ai-data-center-energy-cost-europe-market-guide/. We also find that the
result is insensitive to grid rate ranges as long as they are above a certain threshold. Hence, results based on the rates
in Frankfurt generally apply to other hubs (FLAP-D).

ec20e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
that the average investment cost of existing solar capacities (i.e., those of the first three projects) is 0.60
billion USD/GW. The Ordos project will increase the total capacity by 94% and, at the same time, raise the
average cost to 0.76 billion USD/GW, representing a 25% increase. Given cost functionV(y) =g·y µ, the
average investment cost isg·y µ−1. Hence, the data collected implies 1.94 µ−1 = 1.25. Solving this equation
yieldsµ≈1.34.
Table EC.4 Major Solar Projects in China
Midong Mengxi Lanhai Tianwan Ordos
Capacity (GW) 3.5 3.0 2.0 8.0
Investment (billion USD) 2.13 1.60 1.40 7.33 *
Grid connection 2024 2024 2025 2027 (expected)
* Investment estimated based on total project cost of USD 11 billion, allocated by
capacity share (8 GW solar, 4 GW wind).
Sources:PV Magazine (Midong, 19 Mengxi Lanhai 20); Saur Energy 21 (Tianwan);
Reuters22 (Ordos).
Renewable investment, from a policymaker’s perspective, includes not only the installation cost of the
plant and on-site infrastructure, but also the broader system investments required to connect and deliver
its output, including transmission expansion, grid reinforcement, land, rights-of-way, and financing. Accord-
ingly, we estimategbased on a calibration of the all-in public-system cost of utility-scale solar instead of the
directly observed installation cost. We begin with the U.S. Energy Information Administration’s capacity-
weighted average construction cost of$1.865 million/MW for solar generators entering service in 2024. 23
To capture broader transmission investment beyond the immediate grid tie-in, we assume that each MW
requires an attributable 100 MW-mile of additional transfer capability and apply the midpoint (approx-
imately$5,500/MW-mile) of the Department of Energy’s geographically varying assumptions of roughly
$2,000–$9,000/MW-mile,24 yielding an allowance of$0.55 million/MW; this assumption is intended to reflect
that marginal projects are increasingly located farther from load centers and existing transmission. We fur-
ther assume eight acres/MW, within DOE’s six-to-eight-acre planning range, 25 and value the land at the
2025 national average farm-real-estate value of$4,350 per acre, 26 adding approximately$0.035 million/MW.
Finally, because the EIA construction-cost measure excludes financing, we add a 10% construction-finance
allowance to the plant cost and a 5% system-delivery contingency to the plant, transmission, and land subto-
tal to cover uncertainty in regional grid reinforcement, transmission rights-of-way, and public planning and
23https://www.eia.gov/electricity/generatorcosts/. This measure already includes site preparation,
equipment, engineering and construction management, permitting and other owner costs, and the direct electrical
interconnection to a nearby transmission system, but excludes land acquisition and financing; hence, we do not add
a separate project-level interconnection charge.
24https://www.energy.gov/sites/default/files/2024-10/NationalTransmissionPlanningStudy-Chapter2.
pdf. Figure A-1.
25https://www.energy.gov/sites/default/files/2021-12/developing-utility-scale-renewable-electri
city.pdf
26https://www.nass.usda.gov/Publications/Todays_Reports/reports/land0825.pdf

e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investmentec21
mitigation requirements. The resulting estimate is 1.865 + 0.550 + 0.035 + 1.865×10% + (1.865 + 0.550 +
0.035)×5%≈$2.8 million/MW, or equivalently$2.8 billion/GW. 27
To translate this investment cost into the coefficientginV(y) =gy 1.34, we normalize the marginal invest-
ment cost aty= 1 GW to the all-in unit cost of$2.8 billion/GW estimated above. BecauseV ′(y) = 1.34gy0.34,
imposingV ′(1) = 2.8 yieldsg= 2.8/1.34≈2.089 billion USD per GW 1.34. We use 1 GW as the normalization
point, rather than applying the calibration to the entire existing solar capacity, because the exponent 1.34,
calibrated from projected changes in solar investment requirements between 2025 and 2027, is intended to
characterize the local curvature of the emerging convex-cost segment rather than the full historical deploy-
ment path. A relatively low normalization point therefore better represents the onset of rising marginal
costs associated with increasingly difficult siting, interconnection, and grid expansion to meet the AI energy
demand. We also cross-validate the resulting annualized cost against prevailing estimates of the levelized
cost of solar electricity and find that the calibration is of a comparable magnitude. 28 Assuming a 20-year
economic life, the amortized annual capacity-based cost function becomes 0.104·y 1.34 billion USD per year,
withymeasured in GW. The amortization is undiscounted; incorporating a cost of capital would raisegand
henceV ′(k), tightening condition (b) in Proposition 3(i) and making the adaptation trap more likely rather
than less. At a capacity factor of 20%, one GW of installed solar capacity generates 8.76×0.20 = 1.752 TWh
annually. Substitutingy GW =y TWh/1.752 therefore gives an equivalent annual energy-based cost function of
0.049·y 1.34, whereyis measured in TWh. This is theV(y) function used in Instance A.
To calibrate the coefficientgfor Instances B and C, we assume that the all-in solar investment cost across
regions scales proportionally with the prevailing cost of utility-scale solar installation. Based on available
industry estimates, we use installation costs of approximately 0.95, 0.57, and 0.70 USD/W for the U.S.,
China, and EU, respectively.29,30 We therefore scale the benchmark coefficientg= 0.049 for Instance A by the
corresponding installation-cost ratios. This yieldsg≈0.029 andg≈0.036 in Instances B and C, respectively.
Finally, we sete f in Instances A–C to be the carbon intensity of the grid in the U.S., China, and EU,
respectively, which is approximately 0.367 ton/MWh (calculated by dividing the total emissions of approxi-
mately 1.53 billion metric tons by the total generation of approximately 4.18 trillion kilowatthours 31), 0.614
ton/MWh,32 and 0.187 ton/MWh. 33 We set the climate-damage weightξto the carbon price in the corre-
sponding regions. In the U.S., the carbon price tracks around$28 per ton for regional cap-and-trade systems
such as California’s program;34 legislative frameworks such as the Whitehouse-Schatz bill targeted a starting
27The estimate excludes storage, ongoing operation and maintenance, and decommissioning costs.
28Specifically, this function we derive,V(y) = 0.049·y 1.34, implies a cost of 0.049 billion at 1TWh, which translates
into$49 per MWh, which is comparable with the prevailing range of the levelized cost of utility-scale solar in the
U.S.
29https://a1solarstore.com/blog/what-is-a-solar-farm-and-how-much-money-can-it-make-you.html
https://compareelectricity.com/research/how-much-does-a-solar-farm-cost
30https://www.solarpowereurope.org/press-releases/new-study-reveals-path-to-reshore-solar-man
ufacturing-in-europe. This article estimates that the cost of utility solar installations in Europe is about 60.8
€ct/Wp compared to 50.0€ct/Wp for a Chinese system.
31https://www.eia.gov/tools/faqs/faq.php?id=74&t=11
32https://academic.oup.com/ijlct/article/doi/10.1093/ijlct/ctae181/7762370
33See Figure 1 athttps://www.eea.europa.eu/en/analysis/indicators/greenhouse-gas-emission-intensi
ty-of-1.
34https://icapcarbonaction.com/en/ets/usa-california-cap-and-invest-program

ec22e-companion toGui and Dai:Power Couple? AI Growth and Renewable Energy Investment
fee of$52 per ton. 35 Taking the average of these estimates, we setξ= $40 per ton in Instance A. The carbon
price in China’s national Emissions Trading Scheme hovers around 90 to 106 RMB (approximately 12 to 15
USD) per ton. 36 Taking the average of these estimates, we setξ= $13.5 per ton in Instance B. The carbon
price in the EU is approximately€83.5 ($95) per ton, 37 which we use as theξvalue in Instance C. We
anchorξto observed carbon prices rather than to social-cost-of-carbon estimates. Because permit prices are
policy-constrained and typically run well below the social cost of carbon, this is a conservative valuation of
climate damages.
35https://www.c2es.org/wp-content/uploads/2021/12/carbon-pricing-proposals-in-the-117th-congres
s.pdf
36https://www.ieta.org/uploads/wp-content/Resources/Busines-briefs/2025/IETA_Business_Brief-Chi
na-final-July2025.pdf
37https://tradingeconomics.com/commodity/carbon(accessed July 2026)
