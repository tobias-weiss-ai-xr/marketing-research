---
title: Who Prices Cognitive Labor in the Age of Agents? Compute-Anchored Wages
url: https://arxiv.org/abs/2605.05558
category: digital-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Siqi Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.05558
pages: 13
chars: 41248
fetched_at: '2026-11-08T13:03:15+00:00'
kb_version: 1
---

# Who Prices Cognitive Labor in the Age of Agents? Compute-Anchored Wages

Who Prices Cognitive Labor in the Age of Agents?
Compute-Anchored Wages
Siqi Zhu
University of Illinois Urbana-Champaign
Abstract
A natural intuition about the economics of AI agents is that, because agents can be replicated at
near-zero marginal cost, they constitute a labor input in infinitely elastic supply, and therefore
drive cognitive-labor wages to zero. We argue this framing is wrong in mechanism but partially
correct in conclusion, and that the correction matters for both theory and policy.Agents are
not labor; they are a production technology that converts compute capitalK c into effective units of
cognitive laborL A. Once this is recognized, the elastic-supply margin that anchors the equilibrium
wage migrates from the labor market to the compute capital market. Building on the classic
factor-pricing framework [22], we derive aCompute-Anchored Wage (CAW) bound stating that,
on tasks where human and agent cognitive labor are substitutes, the competitive human wage is
bounded above byλ·k·r c, whererc is the rental rate of compute capital,k is the compute intensity
of one effective agent-labor unit, andλ is the relative human-to-agent productivity. We generalize
the result through constant elasticity of substitution (CES) aggregation, separate substitutable
from complementary tasks, and discuss factor-share consequences. The conclusion is concise:the
price-setter for cognitive labor is no longer the labor market.
1 Introduction
The standard textbook account of wage determination, as presented by Mankiw[22], has two ingredients:
a downward-sloping labor demand curve given by the marginal product of labor, and a labor supply curve
determined by household time allocation and demographics. Equilibrium wages clear the labor market.
The arrival of capable AI agents disturbs this picture, and the analytical question is where the disturbance
enters. A tempting accounting models agents as a new labor input that substitutes for human cognitive labor,
is reproducible at near-zero marginal cost, and has a supply curve horizontal at zero, and then reads off a
collapsing wage from that horizontal supply. We argue this accounting misplaces the elastic margin. Agents
are not a labor input; they are a technology that converts compute capital into effective cognitive labor.
Their supply elasticity is therefore inherited from the supply elasticity of compute capital, which is finite and
governed by physical and political-economic constraints such as semiconductor fab capacity, electricity, water,
land, and geopolitics. The correct model reroutes the price-determination question through the compute
capital market rather than the labor market.
A concrete instance.Consider a junior contract-review paralegal whose work consists largely of clause
extraction, redlining against templates, and summary memos. A frontier large language model performs
each of these tasks at quality close to or above the paralegal’s, at a marginal compute cost on the order of
single-digit dollars per labor-hour-equivalent at 2024–2025 prices (Section 7). The competitive wage on this
paralegal’s substitutable hours is therefore not set by the supply of paralegals; it is set by the rental rate
of compute capital, scaled by an algorithmic constant. The same logic applies to first-pass equity-research
drafting, customer-support triage, and a long list of cognitive tasks that the popular discussion classifies as
1
arXiv:2605.05558v2  [cs.AI]  8 May 2026

“automatable” without identifying the specific market in which the new price is determined.
This paper makes that rerouting explicit, derives a closed-form ceiling on competitive wages that we call the
Compute-Anchored Wage (henceforth CAW), generalizes the substitution structure via a constant elasticity
of substitution (CES) aggregator, separates wage effects across heterogeneous tasks, calibrates the bound to
current compute prices, and discusses limitations and policy. Our claim is that the analytical primitive of
where to put the elastic supply has been miscoded in much current discussion, and that fixing this miscoding
yields a sharp, testable prediction about cognitive-labor pricing. The mathematical content of the bound is
standard cost minimization; the substantive content is the identification of the elastic margin.
The remainder of the paper is organized as follows. Section 2 reviews the related literature and locates
our contribution relative to the task-based automation framework of Acemoglu and Restrepo[1, 4] and the
capital-skill complementarity tradition of Krusell et al.[21]. Section 3 sets up the textbook factor-pricing
model, Section 4 reformulates AI agents as a capital-to-labor conversion technology, and Section 5 derives the
CAW bound. Section 6 generalizes the bound to imperfect substitution via CES, while Section 7 calibrates
it to current compute prices. Section 8 visualizes the migration of the price-setter, Section 9 develops the
cross-task heterogeneity prediction, and Section 10 discusses macro factor-share consequences and policy
levers. Section 11 states limitations.
2 Related Work
Our work intersects five strands of literature. We summarize each, and then state explicitly what the
Compute-Anchored Wage (CAW) framework adds.
Factor pricing and capital–skill complementarity.The marginal-productivity theory of factor pricing
in competitive markets, codified in Mankiw[22], supplies the entire formal apparatus we use; we make no
modifications to the underlying theory, and the only re-coding is in how an AI agent enters the production
function. Closer to our setup, Krusell et al.[21] show that a CES production function in which capital
equipment complements skilled labor and substitutes for unskilled labor matches the joint behavior of the
skill premium and capital–output ratios over decades. We treat compute capitalKc as a factor that, when
paired with the inference stackϕ, becomes a quasi-substitute for human cognitive labor on a measurable
subset of tasks. The crucial difference is that in Krusell et al.[21] the substitution margin is between physical
equipment andunskilled labor; in CAW the margin is between compute capital andcognitive labor previously
regarded as the complement of capital. CAW thus inherits Krusell et al.[21]’s machinery but inverts the sign
of the implied skill premium on the substitutable margin.
Task-based automation (Acemoglu–Restrepo).The closest theoretical antecedent is the task-based
automation framework of Acemoglu and Restrepo (henceforth A–R) [1–4], in which capital automates a
contiguous subset of tasks, displacing labor on the automated margin and reinstating labor through the
creation of new tasks. Our framework can be read as a specialization of A–R to the case where the automating
capital is compute and the displaced labor is cognitive; the price effect we isolate (WH ≤λkr c) is the explicit
equilibrium consequence of A–R’s displacement effect when the automating capital is in elastic but finite
supply. We extend A–R in three ways. First, we identify a specific elastic margin, namely the compute capital
market, that anchors the equilibrium wage on automated tasks and traces the price-determination problem to
a measurable rental raterc. Second, we make the task partition explicit through an elasticity-of-substitution
parameter σ that is in principle estimable from observed factor demands. Third, we discuss the political
economy of compute-market concentration as a determinant ofrc that has no analogue in standard A–R. The
reinstatement effect of A–R is consistent with our complementary-task subsetTC and is preserved.
Skill-biased technical change and occupational exposure to AI.Katz and Murphy[18] document
the rising college premium and frame technology–skill complementarity as the principal driver. Autor et al.[9]
sharpen this into a task-based account in which information technology substitutes for routine cognitive and
manual tasks while complementing non-routine analytic and interpersonal tasks, and subsequent empirical
work (8; 7; 16) traces job polarization and the long-run race between education and technology. A nascent
empirical literature now measures occupation-level exposure to large language models: Eloundou et al.[13]
estimate that 80% of US workers could see at least 10% of their tasks affected, Felten et al.[14] provide an
2

alternative occupational exposure score, Brynjolfsson et al.[11] document a 14% productivity gain among
customer-support agents using a generative-AI assistant, and Noy and Zhang[23] find a roughly 40% time
reduction and 18% quality improvement on professional writing tasks. Our framework predicts a directional
inversion within cognitive labor itself: the salient axis becomes the substitutable–complementary mix on
which an occupation is exposed to AI agents, rather than its position on a one-dimensional skill ladder, and
these exposure studies provide the natural empirical input to theTS/TC partition and to estimatingσ on
each task.
AI in macroeconomics, general-purpose technologies, and compute supply.Aghion et al. [5]
model AI as a sequence of new general-purpose technologies that automate task production and study
balanced-growth implications; Korinek and Stiglitz[20] examine distributional consequences of AI under
capital–labor substitution; Trammell and Korinek[27] survey the macroeconomics of transformative AI; and
Korinek [19] discusses large language models specifically. Bresnahan and Trajtenberg[10] formalize GPTs as
innovations whose value derives from co-invention in downstream sectors, and Goldfarb et al.[15] provide
empirical support for treating machine learning as a GPT. On the supply side, Sevilla et al.[25] document
the doubling time of frontier-model training compute, and Cottier et al.[12] estimate the rising cost of
frontier-model training, pinning down the empirical content of therc time path that drives CAW. CAW
operates at a different level of abstraction from the macro and GPT literatures: rather than modeling growth
dynamics or diffusion, it identifies an equilibrium pricing relation that any of these dynamic models must
satisfy on the substitutable margin in any period. We do not model compute supply explicitly but rely on the
stylized fact that it is finite and only moderately elastic in the medium run because of fab capacity, energy,
water, land, and policy.
Declining labor share.Karabarbounis and Neiman [17], Piketty[24], and Autor et al.[6] document the
long-run decline in the labor share and the rise of superstar firms, and Susskind[26] provides a non-technical
synthesis. CAW refines this discussion by identifying a specific channel, the compute share of capital income,
through which capital-income concentration is now operating, and by predicting that the same mechanism
will compress wages within cognitive labor.
Summary of contribution.Our central analytical re-coding is that agents are a capital-to-labor conversion
technology rather than a labor input, and we trace its equilibrium consequences. Relative to the closest
antecedent in A–R, we add three things. We identify the compute capital market as the elastic margin that
prices substitutable cognitive labor; we proposeσ on each task as the empirical primitive that replaces the
binary “automated or not” coding; and we connect the wage bound to a quantitatively tractable factor price
rc for which there is now an active spot and contract market. The remainder of the paper develops the
consequences of that re-coding.
3 Setup: Factor Markets in the Mankiw Framework
Following the textbook factor-market model, consider a representative competitive firm with a constant-
returns-to-scale production technology
Y=F(K, L),(1)
where K is physical capital andL is labor. Profit maximization in a competitive output market with priceP
yields
W=P· ∂F ∂L , r=P· ∂F ∂K .(2)
Factor prices equal the value of the marginal product. Equilibrium in the labor market is
Ld(W) =L s(W),(3)
with Ls determined by household time allocation and demographic factors. The wageW is set by where these
curves intersect.
The question is what happens when an AI agent becomes available as a partial substitute forL. The
temptation is to add a new labor typeLA with infinitely elastic supply at zero price, mechanically forcing
W→0on the substitutable margin. We now argue this addition is the wrong primitive.
3

4 Reformulation: Agents as Capital-to-Labor Conversion
Definition 1(Agent-Produced Cognitive Labor).An agent-produced cognitive labor unitL A is the cognitive-
labor-equivalent output produced when a fixed bundle of compute capitalk (GPU-hours, energy, memory,
bandwidth, model weights amortized as IP rents) is operated for one unit of time. Formally,LA = ϕ(Kc),
whereϕis increasing and at the relevant scale approximately linear,ϕ(Kc)≈K c/k.
Remark.The function ϕ embeds the model architecture, training run, and inference stack. Improvements in
algorithmic efficiency (distillation, speculative decoding, mixture-of-experts routing, KV-cache reuse) raiseϕ
for given Kc and thus reducek. Crucially, ϕ is atechnology, not a behavioral primitive of households; it does
not enter any labor supply problem.
Remark(Heterogeneity within Kc).The compound input Kc pools three economically distinct objects. The
first is physical compute, including GPUs, accelerators, data-center capacity, and energy, which is rival and
finitely supplied. The second is model-weight intellectual property, which is non-rival and reproducible at
zero marginal cost, so that its rents are pinned down by training sunk costs and licensing structure. The
third is sunk training capital that is amortized into per-token inference prices. The CAW bound below is
governed primarily by the variable inference component, with the IP-rent component entering as a markup
over marginal compute cost. We discuss this further in Section 11.
The augmented production function is
Y=F(K o, LH , LA) =F

Ko, LH , ϕ(Kc)

,(4)
where Ko is non-compute capital,LH is human cognitive labor, andKc is compute capital with rental raterc
determined in the compute capital market. The firm’s first-order conditions become
WH =P· ∂F ∂LH ,(5)
rc =P· ∂F ∂LA ·ϕ ′(Kc).(6)
The crucial observation:LA has no household supply curve. Its supply derives entirely from the supply of
Kc, which is governed by fab capacity, energy infrastructure, data-center construction lead times, and policy.
These are finite and relatively inelastic in the short run, only moderately elastic in the long run.
5 The Compute-Anchored Wage Bound
We state the central proposition first under the strong, illustrative case of perfect substitution, then generalize.
Assumption 1(Perfect substitutability on the margin).There exists a set of tasks on which one unit of
human cognitive labor andλ units of agent-produced labor are perfect substitutes inF, so that effective
cognitive labor on these tasks aggregates asLeff = LH + λ−1LA. Equivalently, one human unit produces the
same effective cognitive output asλ agent units, so thatλ >1corresponds to humans being more productive
per unit, andλ <1to agents dominating.
Proposition 1(Compute-Anchored Wage).Under Assumption 1 and competitive factor markets, the
equilibrium human cognitive wage on the substitutable task set satisfies
WH ≤λ·k·r c (7)
in any equilibrium withLH > 0. Moreover, in any equilibrium with bothLH > 0and LA > 0, the bound holds
with equality,W H =λkr c.
Proof sketch.The unit cost of effective cognitive labor on the substitutable task ismin{WH , λkrc}, since λ
units of LA substitute for one unit ofLH and each unit ofLA requires k units of compute at rental raterc.
Three cases follow. WhenWH < λkrc, firms substitute fully towardLH on this task, so thatLd A = 0on TS
and the bound is slack but nonbinding because no agent-produced labor is used. WhenWH > λkrc, firms
4

substitute fully towardLA, so thatLd H = 0on TS; any positive supply ofLH at this wage on this task is
unemployed, and the wage cannot be sustained in any equilibrium with positive employment ofLH on TS.
Hence WH ≤λkr c in any such equilibrium. Finally, interior coexistence withLH , LA > 0on TS requires the
marginal indifferenceW H =λkr c. The detailed cost-minimization derivation is in Appendix B.
Corollary 1(Migration of the price-setter).The equilibrium wage on substitutable cognitive tasks is determined
by the parameters of the compute capital market(k, rc)and the technology parameter λ. The labor supply
curve Ls H does not appear in the binding condition. The price-setting margin has migrated from the labor
market to the compute capital market.
This is the formal content of our claim. Three clarifications are in order: wages do not collapse to zero but to
λkrc, which can be high or low depending on compute-market conditions; human workers need not become
unemployed, since they may relocate to complementary tasks (Section 9); and the bound applies only on tasks
where Assumption 1 approximately holds, not in all sectors.
6 CES Generalization: Imperfect Substitution
Perfect substitution overstates the case. Generalize via constant elasticity of substitution. Let
Leff =A

αLρ H +βL ρ A 1/ρ , σ= 1 1−ρ ,(8)
with σ∈ (0,∞ )the elasticity of substitution between human and agent cognitive labor, and CES weights
α, β >0. The effective unit cost of an agent-produced labor is its compute cost,Weff A ≡kr c, since LA = Kc/k
and the rental rate ofKc is rc. Cost minimization of(8) for one unit ofLeff delivers the conditional factor
demands and the relative-wage condition
WH
Weff A = α β  LH LA ρ−1 = α β  LH LA −1/σ .(9)
With normalization α/β = λ on the perfect-substitute limit,(9) reduces toWH = λWeff A as σ→ ∞, recovering
the CAW bound (7).
Proposition 2(Compute-driven wage compression).Hold the human-labor supply Ls H and the level of
demand for Leff fixed. Consider an exogenous increase in compute capital supply¯Kc (equivalently, a fall in
k via ϕ improvement) at a fixed rental raterc that lowers Weff A . Then in the new equilibrium the human
cognitive wage falls with semi-elasticity
∂logW H
∂logW eff A = 1− 1 σ · ∂log(L H /LA) ∂logW eff A ,(10)
and in the polar limit of perfectly elasticLs H this collapses to∂logW H /∂logW eff A = 1. As σ→ ∞, the CES
bound collapses to the perfect-substitute CAW bound(7); as σ→ 0(Leontief), LH and LA are used in fixed
proportion, the binding factor is whichever is shorter in supply, and the comparative-static channel fromWeff A
toW H vanishes.
The CES form makes precise an empirically tractable claim:the magnitude of CAWpressure on a given task
is governed by the elasticity of substitution between human and agent cognitive labor on that task. This
is the right object for empirical estimation, replacing the binary “AI replaces / does not replace” framing
common in policy discourse. Eloundou et al.[13], Felten et al.[14], Brynjolfsson et al.[11], and Noy and
Zhang [23] provide the natural empirical input.
7 A Numerical Calibration of CAW
To give the bound(7) empirical traction, we now plug in plausible 2024–2025 numbers. The exercise is
illustrative, not estimation; the goal is to show thatλkrc takes economically meaningful values that vary by
orders of magnitude across tasks.
5

Compute rental rate rc.On-demand H100 GPU rental from major cloud providers traded in the
$2–$5/GPU-hour range in 2024, with multi-year contract pricing closer to$1 .50/GPU-hour. We take
rc = $2/GPU-hour as a midpoint. Frontier-model inference is typically priced per million tokens; converting to
GPU-hour-equivalents using public throughput benchmarks for a 70B-class model on an H100 yields roughly
the same order of magnitude.
Compute intensity k.For a frontier reasoning agent producing sustained, high-quality output, current
inference stacks consume on the order of0.5–2H100-hours of compute to deliver one “hour” of effective
senior-knowledge-worker output, depending on whether the workload is interactive (heavy KV-cache reuse) or
batched. We takek = 1H100-hour per agent-labor-hour for a frontier model andk = 0.05H100-hour per
agent-labor-hour for a small distilled model on a substitutable subtask.
Productivity ratio λ.The empirical literature on LLM productivity gains [11, 23] reports time savings of
14–40% on substitutable tasks, with quality at or above human baseline. We takeλ∈ {0.5,1.0,2.0}to span
the cases where agents are absolutely more productive (λ <1), at parity (λ = 1), and where humans retain a
productivity edge (λ >1).
Implied CAW.Combining these, the boundW H ≤λkr c implies the per-hour ceilings shown in Table 1.
Distilled small model Frontier model Frontier model
(k= 0.05,r c = $2) (k= 1,r c = $2) (k= 1,r c = $5)
λ= 0.5(agent-favored) $0.05/h $1.00/h $2.50/h
λ= 1.0(parity) $0.10/h $2.00/h $5.00/h
λ= 2.0(human-favored) $0.20/h $4.00/h $10.00/h
Table 1 Illustrative CAW ceilingλkrc in US$/hour on substitutable cognitive tasks, under 2024–2025 compute prices.
Read each cell as:the binding human wage on tasks where this (λ, k, rc) configuration applies.
Two implications are immediate. First, on tasks where small distilled models suffice (high-volume classification,
summarization, first-pass document review), CAW is already binding well below any plausible human
reservation wage; the wage on such tasks is effectively pinned at the marginal-product floor. Second, on
tasks requiring frontier-model reasoning, CAW currently sits between roughly $1 and $10/hour. Any human
cognitive labor on tasks where Assumption 1 approximately holds and the frontier model is competent must
be priced under that ceiling to retain employment. Asϕ improves and k falls, every cell of Table 1 moves
down monotonically.
Sensitivity.The ceiling is linear in each of λ, k, and rc. A doubling of compute prices (e.g., from a supply
shock or geopolitical disruption) doubles CAW; a halving ofk from algorithmic improvement halves it. Thus
the empirical content of the framework is the joint trajectory(kt, rc,t)on a task-by-task basis, withσ governing
how rapidly the relevant occupational wage tracks that trajectory.
8 Visualizing the Migration of the Price-Setter
Figure 1 traces the migration of the price-setter across three panels: the textbook labor market in (a), the
compute capital market in (b), and the CAW-anchored cognitive labor market onTS in (c). The reading
order is important. Agent labor hasno household supply curve; its supply is derived from the supply of
compute capitalK c, which in the short run is steep (panel (b)) due to fab capacity, energy, and data-center
lead times. Compute demand therefore pins the rental rater∗ c in (b). Conditional on thatr∗ c, the horizontal
line at ¯WH = λkr∗ c in panel (c) is a wageceiling on human cognitive labor onTS, not an agent-labor supply
curve: it does not assert that agent supply is infinitely elastic. The human-labor supply curveLs H is drawn
but does not determine the equilibrium wage onTS. In general equilibrium, shifts in compute demand move
r∗ c in (b), and the CAW line in (c) shifts in lockstep.
6

L
W
Ld
Ls
W ∗
L∗
(a) Classic labor market
Wage set by
Ld ∩L s
Kc
rc
K s c (short-run)
K d c
r∗ c
¯Kc
(b) Compute capital market
Inelastic short-run supply
pinsr ∗ c
LH
WH
Ld H
Ls H
CAW: ¯WH =λkr ∗ c
Ld H ( ¯WH )
(c) Cognitive labor onT S
Wage ceiling givenr ∗ c;
not an agent-labor supply curve
r∗ c 7→λkr ∗ c
migration of the price-setter
Figure 1 Migration of the price-setting margin.(a) In the classic framework the wage is determined byLd ∩L s. (b)
The compute capital market: short-run supplyK s c is steep (inelastic) due to fab capacity, energy, and data-center
lead times, so compute demandK d c pins the equilibrium rental rater∗ c. (c) Cognitive labor on substitutable tasks
TS, drawnconditional on the equilibrium r∗ c inherited from panel (b): the human-labor supply curveLs H is no longer
the binding constraint (drawn dashed); the wage is capped by the horizontal line¯WH = λkr∗ c, and employment is
Ld H ( ¯WH ). The horizontal CAW line isnot an agent-labor supply curve, and the framework does not assume that
agent labor is in infinitely elastic supply. It is the wageceiling conditional on r∗ c. In general equilibrium, any shift in
compute demand re-pricesr∗ c in panel (b); the CAW line in panel (c) then shifts in step.
9 Task Heterogeneity: A Directional Inversion of Skill-Biased Technical Change
(SBTC)
Katz and Murphy[18] and the subsequent skill-biased technical change (SBTC) literature document that
information technology has historically complemented high-skill cognitive labor and substituted for routine
labor [7–9]. The CAW framework predicts a directional inversionwithin cognitive labor.
We partition tasks into two sets. The first is the set ofsubstitutable cognitive tasksT S, comprising drafting,
code generation against specifications, summarization, first-pass analysis, scheduling, retrieval, and classi-
fication. On TS, σ is large, CAW binds, andWH is anchored by λkrc; the empirical exposure scores of
Eloundou et al.[13] and Felten et al.[14] provide useful proxies for membership inTS. The second is the set
of complementary cognitive tasksT C, comprising judgment under deep uncertainty, accountability and legal
liability, relational and political work, cross-domain integration, taste, principal-agent monitoring, and any
task where ∂F/∂L H is increasing inLA. On TC, σ is small or the cross-partial∂2F/∂L H ∂LA > 0, so that
WH rises withL A.
The wage distribution across cognitive workers therefore widens, but the relevant axis is no longer traditional
skill; it is theTS/TC exposure mix of each occupation. To make this concrete, consider two occupations
with similar formal credentials. A junior contract-review paralegal performs work that is roughly 80% onTS
(clause extraction, redlining against templates, summary memos) and 20% onTC (escalation judgment). A
senior litigation associate, by contrast, performs work that is roughly 30% onTS (document review, brief
drafting) and 70% onTC (case strategy, client management, courtroom work). Under CAW the paralegal’s
wage is dominated byλkrc on the substitutable component and is squeezed downward ask falls, whereas the
associate’s wage is dominated by complementary tasks and may rise. This is consistent with the early empirical
findings of Brynjolfsson et al.[11] that productivity gains are concentrated in less-experienced workers, but it
does not by itself imply that less-experienced workers gain in compensation, since the same tasks that they
used to monopolize have been priced down. Two occupations with identical traditional skill requirements
but different TS/TC shares will diverge sharply in compensation. This is a testable cross-sectional prediction
distinct from canonical SBTC.
7

10 Macro Implications: Factor Shares
Aggregating across tasks, define the labor sharesL = WH LH /Y . As compute substitutes for human cognitive
labor onTS, the wage billWH LH shrinks on those tasks, while the compute rental billrcKc grows. The capital
share rises. Recipients of the rising capital share are owners of compute infrastructure, energy producers, and
holders of model intellectual property; these need not coincide with the historical owners of physical capital.
This connects the CAW framework to the literature on declining labor shares [6, 17] and the long-run dynamics
emphasized by Piketty[24], with an important refinement: under CAW, the capital share rises specifically
through thecompute channel. Policy interventions targeting that channel (compute taxation, public compute
provision, antitrust on accelerator markets, energy policy) have first-order effects on the cognitive-labor wage
distribution that interventions targeting the labor market do not. We discuss four such levers in turn.
Compute taxation.A tax on rc raises the CAW ceiling proportionally. Incidence depends on the elasticity
of compute supply and on the elasticity of demand for substitutable cognitive output. With moderately
inelastic compute supply in the short run, much of the tax falls on compute owners; in the long run, with
more elastic capacity expansion, incidence shifts toward output prices and ultimately toward human wages on
TS via the bound. Pigouvian arguments based on energy externalities and Ramsey arguments based on the
relative inelasticity ofKc supply both push toward positive optimalτc >0.
Public compute provision.A public option that supplies compute at marginal cost compresses the
markup component of rc and tightens the CAW ceiling. The effect is symmetric to compute taxation in
sign on rc but distributionally different: public provision lowersWH on TS, raising the consumer surplus of
cognitive output buyers without redistributing to workers onTS.
Antitrust on accelerator markets.If the accelerator market is concentrated,rc contains a markup over
marginal cost. Antitrust enforcement that erodes that markup again lowers the CAW ceiling. The substantive
question is whether the resulting consumer-surplus gains in cognitive output exceed the wage compression on
TS; under standard welfare assumptions they do, but the distributional consequences are large.
Energy policy.A binding fraction of rc is electricity cost. Policy that lowers the levelized cost of electricity
to data centers (transmission build-out, nuclear permitting, renewable subsidies) operates throughrc in the
same direction as capacity expansion. Because CAW is a price relationship that propagates through tradable
cognitive output, its incidence is largely national to global rather than local, even when underlying electricity
costs vary regionally.
11 Limitations and Boundary Conditions
Several caveats would invalidate or complicate the argument and deserve discussion.
Jevons effects.A fall in the unit cost of cognitive labor may expand demand for cognitive output enough
to raise totalLH employment even onTS tasks. CAW bounds thewage, not the wagebill, so whether total
compensation rises or falls depends on the demand elasticity for cognitive output.
Ricardian comparative advantage.Even if agents are absolutely more productive on every task, humans
retain employment via comparative advantage. Comparative advantage, however, determinesallocation rather
than price, so that wages on the substitutable margin remain anchored.
Non-productivity wage components.Liability, accountability, signaling, trust, and physical co-presence
add a non-marginal-product premium to human labor that the production-function setup does not capture.
CAW bounds the marginal-product component of wages, not the total.
Compute-market structure.The derivation assumes competitive compute markets. If compute is
monopolized, vertically integrated with model providers, or politically rationed, then rc is no longer a
competitive rental rate and the bound is replaced by a markup-adjusted version. The argument then becomes
a claim aboutpolitical economy as much as about prices.
8

Endogenous ϕ.Algorithmic improvement reduces k over time, so that CAW is a moving target, declining
secularly even at constantrc. The relevant long-run object is the joint trajectory of(kt, rc,t). As a first-pass
dynamic statement, holdingrc constant and assuming exponential improvement inϕ at rate g, the implied
CAW trajectory is ¯WH (t) = λk0e−gtrc, which converges to zero ast→ ∞ unless arrested by hardware
bottlenecks or model-quality saturation.
Endogenous task boundaries.The partition TS ∪T C shifts with the capability frontier, with tasks
migrating from TC to TS as agents improve. The empirical content of the framework therefore depends on a
measurable, time-indexed task taxonomy.
Heterogeneity of Kc.As noted in the remark on Kc heterogeneity in the reformulation,Kc is a composite
of physical compute (rival, competitive), model-weight IP (non-rival, often monopolistic), and sunk training
capital. A more refined version of CAW would carry these as separate factors with their own pricing equations.
12 Conclusion
Our claim can be stated in one sentence:on tasks where AI agents substitute for human cognitive labor, the
equilibrium wage ceiling is set in the compute capital market, not the labor market. The standard textbook
framework already contains all the machinery needed to see this; the only required correction is to recognize
agents as a capital-to-labor conversion technology rather than a labor input. Once that correction is made,
the Compute-Anchored Wage boundWH ≤λkr c follows directly from competitive cost minimization, and a
number of empirical and policy questions reorient accordingly: the relevant elasticity to estimate isσ across
task categories; the relevant macro outcome is the compute share of capital income; the relevant policy levers
are compute-market levers, not labor-market levers. The numerical calibration in Section 7 suggests CAW is
already binding on the high-volume substitutable margin and approaching binding on frontier-substitutable
tasks at present compute prices.
9

References
[1] Daron Acemoglu and Pascual Restrepo. The race between man and machine: Implications of technology for
growth, factor shares, and employment.American Economic Review, 108(6):1488–1542, 2018.
[2] Daron Acemoglu and Pascual Restrepo. Automation and new tasks: How technology displaces and reinstates
labor. Journal of Economic Perspectives, 33(2):3–30, 2019.
[3] Daron Acemoglu and Pascual Restrepo. Robots and jobs: Evidence from US labor markets.Journal of Political
Economy, 128(6):2188–2244, 2020.
[4] Daron Acemoglu and Pascual Restrepo. Tasks, automation, and the rise in U.S. wage inequality.Econometrica,
90(5):1973–2016, 2022.
[5] Philippe Aghion, Benjamin F. Jones, and Charles I. Jones. Artificial intelligence and economic growth. In Ajay
Agrawal, Joshua Gans, and Avi Goldfarb, editors,The Economics of Artificial Intelligence: An Agenda, pages
237–282. University of Chicago Press, 2019.
[6] David Autor, David Dorn, Lawrence F. Katz, Christina Patterson, and John Van Reenen. The fall of the labor
share and the rise of superstar firms.Quarterly Journal of Economics, 135(2):645–709, 2020.
[7] David H. Autor. Why are there still so many jobs? the history and future of workplace automation.Journal of
Economic Perspectives, 29(3):3–30, 2015.
[8] David H. Autor and David Dorn. The growth of low-skill service jobs and the polarization of the US labor market.
American Economic Review, 103(5):1553–1597, 2013.
[9] David H. Autor, Frank Levy, and Richard J. Murnane. The skill content of recent technological change: An
empirical exploration. Quarterly Journal of Economics, 118(4):1279–1333, 2003.
[10] Timothy F. Bresnahan and Manuel Trajtenberg. General purpose technologies: “Engines of growth”?Journal of
Econometrics, 65(1):83–108, 1995.
[11] Erik Brynjolfsson, Danielle Li, and Lindsey R. Raymond. Generative AI at work.NBER WorkingPaper No. 31161,
2023.
[12] Ben Cottier, Robi Rahman, Loredana Fattorini, Nestor Maslej, and David Owen. The rising costs of training
frontier AI models.arXiv preprint arXiv:2405.21015, 2024.
[13] Tyna Eloundou, Sam Manning, Pamela Mishkin, and Daniel Rock. GPTs are GPTs: An early look at the labor
market impact potential of large language models.arXiv preprint arXiv:2303.10130, 2023.
[14] Edward W. Felten, Manav Raj, and Robert Seamans. How will language modelers like ChatGPT affect occupations
and industries? arXiv preprint arXiv:2303.01157, 2023.
[15] Avi Goldfarb, Bledi Taska, and Florenta Teodoridis. Could machine learning be a general purpose technology? a
comparison of emerging technologies using data from online job postings.Research Policy, 52(1):104653, 2023.
[16] Claudia Goldin and Lawrence F. Katz.The Race Between Education and Technology. Harvard University Press,
2008.
[17] Loukas Karabarbounis and Brent Neiman. The global decline of the labor share.Quarterly Journal of Economics,
129(1):61–103, 2014.
[18] Lawrence F. Katz and Kevin M. Murphy. Changes in relative wages, 1963–1987: Supply and demand factors.
Quarterly Journal of Economics, 107(1):35–78, 1992.
[19] Anton Korinek. Language models and cognitive automation for economic research. NBER Working Paper
No. 30957, 2023.
[20] Anton Korinek and Joseph E. Stiglitz. Artificial intelligence and its implications for income distribution and
unemployment. In Ajay Agrawal, Joshua Gans, and Avi Goldfarb, editors,The Economics of Artificial Intelligence:
An Agenda, pages 349–390. University of Chicago Press, 2019.
[21] Per Krusell, Lee E. Ohanian, José-Víctor Ríos-Rull, and Giovanni L. Violante. Capital-skill complementarity and
inequality: A macroeconomic analysis.Econometrica, 68(5):1029–1053, 2000.
[22] N. Gregory Mankiw.Principles of Economics. Cengage Learning, 9 edition, 2020.
[23] Shakked Noy and Whitney Zhang. Experimental evidence on the productivity effects of generative artificial
intelligence. Science, 381(6654):187–192, 2023.
10

[24] Thomas Piketty.Capital in the Twenty-FirstCentury. Harvard University Press, 2014.
[25] Jaime Sevilla, Lennart Heim, Anson Ho, Tamay Besiroglu, Marius Hobbhahn, and Pablo Villalobos. Compute
trends across three eras of machine learning.2022 International Joint Conference on Neural Networks (IJCNN),
2022.
[26] Daniel Susskind.A WorldWithout Work: Technology,Automation, and How WeShould Respond. Metropolitan
Books, 2020.
[27] Philip Trammell and Anton Korinek. Economic growth under transformative AI.Annual Review of Economics,
15:567–593, 2023.
11

Appendix
A Notation Summary
For convenience we collect the symbols used throughout the paper.
•Y: aggregate output of the representative competitive firm.
•K,L: generic physical capital and labor in the Mankiw [22] setup.
•K o: non-compute physical capital.
•K c: compute capital (GPUs, accelerators, data-center capacity, energy, model-weight IP rents).
•r c: competitive rental rate of compute capital, in $/compute-unit-hour.
•L H: human cognitive labor, in labor-hours.
•L A: agent (cognitive-labor-equivalent) units, satisfyingLA =ϕ(K c)≈K c/k.
•k : compute intensity, defined as units of compute capital required per effective agent-labor unit, in
compute-units per agent-labor-hour.
•ϕ: capital-to-labor conversion technology embedding model architecture and inference stack.
•λ : relative human-to-agent productivity on the substitutable task set, where one human-labor unit produces
the same effective output asλ agent-labor units. Valuesλ >1correspond to humans being more productive
per unit, whileλ <1corresponds to agents dominating.
•W H: human cognitive wage, in $/labor-hour.
•W eff A ≡kr c: effective agent unit wage, in $/agent-labor-hour.
•σ: elasticity of substitution between human and agent cognitive labor in the CES aggregator.
•T S,T C: substitutable and complementary cognitive task sets.
B Detailed Derivation of the CAW Bound
We expand the proof sketch of Proposition 1. Under Assumption 1, the effective cognitive-labor input on the
substitutable task set isLeff = LH + λ−1LA. A profit-maximizing firm chooses(LH , LA)to minimize the cost
of producing one unit ofLeff:
min
LH , LA≥0
WH LH +r c k LA s.t.L H +λ −1LA ≥1.
Since the constraint is linear and the objective is linear, the solution is a corner whenever the per-unit cost
WH of LH and the per-unit costλkrc of effective labor delivered throughLA are unequal. If WH < λkrc, the
firm substitutes fully towardLH, so thatLd A = 0on TS. If instead WH > λkrc, the firm substitutes fully
toward LA, so thatLd H = 0on TS; any positive supply ofLH at this wage on this task is therefore unemployed,
and the wage cannot be sustained in any equilibrium withLH > 0on TS. Interior coexistence in turn requires
WH = λkrc. Across all cases consistent with positive employment,WH ≤λkr c on the substitutable margin,
with equality whenever both factors are simultaneously employed. WhenLA = 0everywhere, for example
because compute is unavailable or prohibitively expensive, the standard labor-market wage prevails and the
bound is slack.
12

C CES Algebra
Cost minimization of the CES aggregator(8) subject to producing one unit ofLeff yields the conditional
factor demands
LH = 1 A  α WH σ Λ, L A = 1 A  β Weff A σ Λ,
whereΛis the dual CES price index (a function ofWH andW eff A alone). Taking the ratio gives (9).
The two limits are immediate. Asσ→ ∞(perfect substitutes), the relative wage(9) forces WH → (α/β) Weff A ,
which under the normalizationα/β = λ recovers the perfect-substitute CAW bound. Asσ→ 0(Leontief), the
conditional demand forLH is fixed by the technology in proportion toLA, so LH and LA are used together
in fixed ratio; the binding factor is then whichever is shorter in supply. If human-labor supply is the binding
constraint at the prevailing demand forLeff, thenWH is determined byLs H and the comparative-static channel
from Weff A to WH vanishes; if compute is the binding constraint, thenWH tracks Weff A scaled by the technology
proportion.
For Proposition 2, holdingLs H and the demand forLeff fixed, totally differentiating(9) with respect toWeff A
yields
dlogW H
dlogW eff A = 1− 1 σ · dlog(L H /LA) dlogW eff A .
Under perfectly elasticLs H, WH tracks Weff A one-for-one and the second term vanishes. Under inelasticLs H,
the cross-derivative term partially offsets the direct effect, with the magnitude controlled by1/σ.
13
