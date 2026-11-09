---
title: Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining
url: https://arxiv.org/abs/2610.29663
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Xintong Liu
- Chenkai Zhang
- Yanzhao Ma
- Peng Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.29663
pages: 14
chars: 62524
fetched_at: '2026-11-08T13:31:19+00:00'
kb_version: 1
---

# Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining

Lineage-Aware Search Control for LLM-Based Evolutionary Factor Mining
Xintong Liu, Chenkai Zhang, Yanzhao Ma, Peng Yang∗
Southern University of Science and Technology (SUSTech)
Shenzhen, China
12311926@mail.sustech.edu.cn
Abstract
Formulaic alpha factor mining searches for symbolic expres-
sionsthattransformmarketdataintopredictivesignals.Recent
LLM-basedevolutionaryfactorminingmethodsuselargelan-
guagemodelsassemanticvariationoperators.Underthecon-
ventionalLLM-EAparadigm,stochasticvariationandfitness-
basedselectioncanleavethesearchweaklydirectedandcon-
centrated around a narrow set of structurally similar factors.
We argue that these limitations arise because current meth-
ods mainly organize search at the individual and population
levels,leavinglineage-levelcontrolunderused.Alineagecon-
nectssuccessivefactorvariantsthroughevolutionarydescent.
We proposeLineageEvo, which uses lineage in two coupled
forms of search control: (1) lineage-conditioned LLM vari-
ation, which distills Lineage-Scoped Search Experience into
operator-specific priors and fuses them with global opera-
tor priors, providing persistent, lineage-relevant guidance for
LLM generation; and (2) lineage-stratified search allocation,
which balances factor quality against lineage concentration
by distributing the search budget across lineages during evo-
lutionary search. Together, these mechanisms make semantic
variation more direction aware and prevent branches from
dominating the evolution, thereby promoting the discovery
of predictive and diverse factors. We evaluateLineageEvo
on CSI 500 and S&P 500 in terms of factor predictiveness,
portfolio performance, search efficiency, and lineage- and
expression-leveldiversity.LineageEvoachievesthestrongest
predictiveperformanceonbothmarkets,whileLSPSproduces
amorebalancedlineagedistributionandastructurallybroader
factorpool.Theresultssupportlineageasausefulintermedi-
ateunitforcontrollingLLM-basedevolutionaryfactorsearch.
Introduction
Formulaicalphafactorminingaimstodiscovermathematical
expressions that transform raw market data into predictive
signals for future asset returns (Kakushadze 2016). Such
factors support portfolio construction and trading, yet the
vast expression space and noisy, non-stationary data make
predictive and stable factors difficult to discover.
Earlyfactordiscoverylargelyreliedonhumanexpertswho
designed signals based on financial intuition and empirical
experience. To reduce such manual effort, automated fac-
tor mining methods have been developed, including genetic
programming (GP), reinforcement learning (RL), and other
∗Corresponding author.
machine learning approaches (Zhang et al. 2020; Yu et al.
2023; Chen et al. 2025). These methods expand the search-
able factor space and enable systematic exploration beyond
hand-craftedfactors.However,theystillrelymainlyonfixed
grammars,handcraftedoperators,orscalarrewards,limiting
semanticreasoningandadaptivereuseofsearchexperience.
Morerecently,LLM-basedfactormininghasemergedasa
promisingparadigm,usingpretrainedmodelstogenerateand
refine symbolic formulas through agent-based generation,
tree search, and graph-aware evolution (Wang et al. 2023;
Tang et al. 2025; Shi, Duan, and Li 2025; Guo et al. 2026;
Luo et al. 2026a). Large-scale pretraining provides seman-
ticpriorsoverfinancialconcepts,mathematicalexpressions,
andprogrammingpatterns,supportingfactorhypothesisgen-
eration and formula refinement. Among these approaches,
LLM-based evolutionary algorithm (LLM-EA) factor min-
ing is particularly appealing because it replaces purely syn-
tactic genetic operators with LLM-based semantic mutation
and recombination (Liu et al. 2023; Luo et al. 2026b; Ren
et al. 2025; Han et al. 2026). However, two search-control
challenges remain. First, LLM-based operators are flexible
but weakly controllable, as the mapping from prompt con-
text to offspring is implicit and difficult to steer persistently
(Liu et al. 2023; Yin et al. 2024). Second, under limited
budgets, fitness-based selection can lead to takeover, where
currently strong individuals or branches receive dispropor-
tionate search opportunities, reducing diversity and risking
premature convergence (Sudholt 2018; Gabor, Belzner, and
Linnhoff-Popien 2018).
These challenges persist because current LLM-EA factor
miningmethodsmainlyorganizesearchattheindividualand
population levels, while making limited use of lineage-level
state.Attheindividuallevel,LLMoperatorsmodifyselected
parentfactors;atthepopulationlevel,evolutionaryselection
favors high-scoring candidates. Between them, alineageis
a descent-defined factor family whose membership follows
primary evolutionary inheritance. Unlike an isolated indi-
vidualoranunstructuredpopulation,alineagepreservesthe
continuityoflocalsearchacrosssuccessivevariationevents,
making it a natural stateful unit for both persistent opera-
tor guidance and search allocation. Conventional evolution-
aryalgorithmshaveusedgenealogyandlineageinformation
for diversity preservation, selection, and inheritance analy-
sis (Burke et al. 2003; Gabor, Belzner, and Linnhoff-Popien
arXiv:2610.29663v1  [q-fin.CP]  21 Oct 2026

2018;Burlacuetal.2013).However,usinglineageasashared
scope for operator priors and search allocation remains un-
derexplored in LLM-EA factor mining.
To address these issues, we proposeLineageEvo, a
lineage-awareLLM-EAframeworkforformulaicfactormin-
ing.LineageEvorepresentsevolutionarydescentinalineage
DAG and uses lineage in two coupled forms of search con-
trol. First, it organizes Lineage-Scoped Search Experience
(LSSE) into operator-specific lineage priors and fuses them
withglobaloperatorpriorstoconditionLLM-basedmutation
and crossover. Second, Lineage-Stratified Parent Selection
(LSPS)allocatessearchopportunitiesatthelineagelevelbe-
fore selecting parent factor(s), while a separate elite archive
preserves high-quality discoveries. This design gives LLM
variationapersistentlocalcontextanddistributessubsequent
search more evenly across evolutionary branches.
Experiments on CSI 500 and S&P 500 demonstrate the
effectivenessofLineageEvoacrossmarkets.Comparedwith
thestrongestbaselineforeachmetric,LineageEvoimproves
IC by 28.3% and 12.6%, and ICIR by 9.9% and 35.8% on
CSI 500 and S&P 500, respectively, while achieving the
strongest portfolio performance on both markets. Ablation
results confirm the complementary roles of lineage-specific
andglobalpriors,whileLSPSincreaseslineageentropyfrom
0.405to2.154andaverageASTdistancefrom0.509to0.747,
preserving a broader and less concentrated factor pool. The
searchcurvefurthershowsthatLineageEvoreachesastrong
factor set rapidly, indicating efficient evolutionary search.
Our contributions are summarized as follows:
•We identify lineage-level search control as underex-
plored in LLM-EA factor mining and use it to connect
individual-level semantic variation with population-level
selection.
•We proposeLineageEvo, which represents descent-
definedfactorfamiliesinanevolutionaryDAGandorga-
nizes Lineage-Scoped Search Experience into operator-
specific lineage priors for LLM variation.
•We introduce lineage-stratified search allocation through
LSPS,whichbalanceslineagequalityagainstlineagecon-
centration, and decouple search allocation from solution
preservation through a separate elite archive.
•Experiments on CSI 500 and S&P 500 show thatLin-
eageEvooutperforms eight representative baselines in
factor performance, while preserving greater lineage and
structural diversity.
Related Work
Traditional Automated Factor Mining
Traditional automated factor mining mainly formulates al-
pha discovery as symbolic search. AutoAlpha applies GP-
style variation and quality-diversity search, AlphaGen uses
reinforcementlearning,andAlphaSAGEimprovesstructure-
aware exploration (Zhang et al. 2020; Yu et al. 2023; Chen
et al. 2025). These methods broaden automated search, but
stilllargelydependonpredefinedgrammars,handcraftedop-
erators, or scalar rewards, making it difficult to incorporate
domain semantics or adaptively reuse search experience be-
yond predefined operators.
LLM-Based Factor Mining
Recent work introduces LLMs into factor mining as seman-
tic generators, refiners, and search assistants. Alpha-GPT
explores human–AI interactive alpha generation by translat-
ing investment ideas into candidate formulas (Wang et al.
2023), while AlphaAgent develops an autonomous agent
frameworkwithoriginality,hypothesis-factoralignment,and
complexitycontrol(Tangetal.2025).Search-orientedmeth-
odsfurthercombineLLMgenerationwithMonteCarloTree
Search or graph-based retrieval to guide formula refinement
(Shi, Duan, and Li 2025; Guo et al. 2026). These meth-
odsmakefactorminingmoresemanticbyleveragingLLMs’
pretraining-induced knowledge of financial concepts, math-
ematical expressions, and programming patterns to generate
factors with richer rationales and more flexible structures.
However,assuggestedbyAlphaBench,existingLLM-based
factorminingmethodsmaystillunder-exploittheexploration
capacity of LLMs, motivating evolutionary frameworks that
embed LLMs into iterative population-based search (Luo
et al. 2026a).
LLM-EA Factor Mining
LLM-EA search combines the semantic generation ability
of LLMs with the population-based optimization mecha-
nism of evolutionary algorithms. General LLM-EA studies
use LLMs as evolutionary optimizers or hyper-heuristics,
whereLLMsgenerate,mutate,recombine,orreflectoncan-
didate solutions within an iterative search loop (Liu et al.
2023, 2024; Ye et al. 2024). In factor mining, EvoAlpha
adapts this paradigm to evolutionary alpha discovery with
LLM-generated factors (Luo et al. 2026b); TreEvo evolves
tree-structured thoughts to capture the hierarchical nature
of alpha formulas (Ren et al. 2025); and QuantaAlpha ex-
plores trajectory-level mutation and crossover to reuse ef-
fective mining experience (Han et al. 2026). These meth-
ods move beyond isolated LLM generation by introducing
evolutionaryvariationandselectionintofactorsearch.How-
ever, they still face two fundamental search-control chal-
lenges: LLM-driven variation can be flexible but weakly
controllable, while fitness-based selection can cause dom-
inant branches to monopolize the search process.
GenealogyandLineageinEvolutionaryAlgorithms
Evolutionary computation has previously used genealogy
and lineage information for diversity preservation, inher-
itance analysis, and selection (Burke et al. 2003; Gabor,
Belzner, and Linnhoff-Popien 2018; Burlacu et al. 2013).
These studies establish lineage as an evolutionary abstrac-
tion.Buildingonthisfoundation,LineageEvouseseachlin-
eage as the shared scope for accumulating operator-specific
priors and allocating subsequent search opportunities in
LLM-EA factor mining.
Method
We proposeLineageEvo, a lineage-aware evolutionary
framework for formulaic alpha factor mining with LLM-
based semantic variation. Its central idea is to associate ac-
cumulatedsearchexperienceandfuturesearchopportunities

1 Population (Lineages) 2 Lineage-Stratified
Parent Selection
(LSPS)
3 Prior Memory /
Retrieval
4 Prior
Fusion
5 LLM Generator 6 Evaluation
Pipeline
Lineage DAG /
Population
L1
...
L2
...
L3
...
LK
...
Primary inheritance edge
More lineages
Lineage-Stratified
Parent Selection
(LSPS)
(Allocation Unit)
Step 1:  Select
Lineage
...
Lineage sampling
(quality-aware,
concentration-balanced)
Step 2:  Select
Parent
Factor(s) within
Selected Lineage
...
Parent sampling
(quality-aware factor
selection)
Selected Lineage Li
Selected Parent(s) P
Prior Memory
/
Retrieval
(Conditioned on Selection)
Lineage Priors
(local priors tied
to selected lineage Li)
Lᵢ¹ ...
Lᵢ² ...
Lᵢᵐ ...
(LSSE /
lineage-scoped
search experience)
Global Priors
Successful motifs
& patterns
High-utility ops
&
templates
Factor library
&
primitive pool
Performance
statistics
...
(LSSE /
cross-lineage
search
experience)
LLM Generator
Candidate
Factor
(expression)
Validation
(Syntax /
Duplicate /
Constraints)
Evaluation /
Backtest
(Performance)
Feedback and Update
Active Pool / Elite Archive
Active Pool
(diverse candidates)
...
Elite Archive
(high-quality)
...Secondary crossover edge
(Lineage as memory
unit)
...
Prior fusion
Figure 1: Overview ofLineageEvo. LSPS first selects a lineage and then selects parent factor(s); lineage-specific and global
operator priors are subsequently retrieved and fused to condition LLM-based variation. Valid offspring are evaluated, and the
feedback path updates the lineage DAG, prior states, active population, and elite archive.
with each lineage.LineageEvouses lineage as a stateful
intermediatesearchunitbetweenindividual-levelLLMvari-
ation and population-level evolutionary selection. Specifi-
cally, lineage serves two complementary roles: (1) it defines
a local scope for accumulating operator-specific search ex-
perience, and (2) it provides a unit for allocating a limited
evaluation budget.
Figure 1 summarizes one iteration ofLineageEvo. Start-
ingfromanevolutionarystateorganizedbylineage,Lineage-
StratifiedParentSelection(LSPS)firstallocatesasearchop-
portunity to a lineage and then selects parent factor(s) from
the active population. The corresponding lineage-specific
and global operator experience is retrieved and fused into
soft guidance for LLM-based mutation or crossover. A de-
terministicallyvalidatedoffspringissubsequentlyevaluated,
afterwhichthelineagegraph,priorstates,activepopulation,
and elite archive are updated. This division of responsibil-
ities keeps the LLM focused on semantic variation, while
deterministic components govern validation, evaluation, in-
heritance, and search-state transitions.
Problem Setup and Lineage Representation
LetXdenote the market feature space andFthe symbolic
expression space induced by a factor grammar. A formulaic
alphafactorf∈ Fmapsthehistoricalobservationsofstock
ito a cross-sectional signal:
zf i,t =f(X i,≤t),(1)
wherez f i,t is the factor value at datet. Rather than seeking a
single best expression, the goal is to discover a collection of
factorsthatexhibitstrongpredictiveperformanceandtempo-
ral stability while maintaining sufficient structural diversity
duringsearch.Theresultingfactorpoolsupportsdownstream
factor selection and combination.
LineageEvoties lineage identity to the structural inheri-
tance induced by its variation operators. Mutation applies a
local modification to a leaf node or a small subtree of one
parent while preserving the remaining expression structure.
Crossover is asymmetric: the parent sampled from the first
selected lineage is fixed as the primary parent and provides
the recipient expression backbone. A subtree from the sec-
ondary parent replaces a selected primary subtree, while the
remaining primary structure is preserved.
We record these inheritance relations using a directed
acyclic graph
Gt =  V t,E t pri,E t sec  ,(2)
whereV t contains all valid factors evaluated by iterationt.
The setE t pri records the inheritance of the expression back-
bone. A mutation offspring has one primary edge from its
parent, whereas a crossover offspring has one primary edge
fromthebackboneparent.ThesetE t sec recordsthedonoran-
cestryofcrossover,preservingthecontributionoftheparent
that provides the replacement subtree.
LetR t ⊆ Vt denote the set of root factors. Since each
non-rootnodehasexactlyoneincomingprimaryinheritance

edge, its lineage root is recursively defined as
ρt(v) =
(
v, v∈ R t,
ρt(u),(u, v)∈ E t pri. (3)
The lineage associated with rootrk is consequently
Lt k =  v∈ Vt |ρ t(v) =r k 	 .(4)
A lineage is therefore a descent-defined local search fam-
ilyinducedbystructure-preservingvariation.Lineagemem-
bership follows the inherited expression backbone through
primary edges, while secondary edges retain cross-lineage
donorancestry.Becausemutationmodifiesonlyalocalcom-
ponentandcrossoverpreservestheprimarybackbone,nearby
descendants are expected to retain greater structural and
DSL-level financial-semantic continuity than factors from
unrelated lineages, as verified in Appendix. This continuity
provides the basis for using lineage as a scope for search
experience and resource allocation.
Lineage-Stratified Search Allocation
Modules 1–2 in Figure 1 implement lineage-level search al-
location. Standard individual-level fitness selection may re-
peatedlyfavorfactorsfromalreadydominantbranches,caus-
ingearlylineagetakeoverandreducingexploration(Sudholt
2018; Gabor, Belzner, and Linnhoff-Popien 2018). To miti-
gate this effect,LineageEvoorganizes its active population
by lineage:
P t =
mt[
k=1
P t k,P t k =P t ∩ Lt k,(5)
whereP t k contains the active factors belonging to lineagek,
andm t is the number of active lineages.
LSPS uses a two-stage sampling procedure. It first selects
a lineage and then selects a parent factor within that lineage.
Bothstagesuseacommonrobustqualityscore.LetMdenote
theoptimizationmetric,eitherICorICIR,anddefineT(f) =
|Mtr(f)|andV(f) =|M val(f)|. For factors satisfying
T(f) +V(f)>0, the quality score is
q(f) =αT(f) +βV(f)−γ|M tr(f)− Mval(f)|,(6)
whereα, β >0and0≤γ <min{α, β}. This guarantees
q(f)>0while penalizing both strength disagreement and
directional reversals.
For each lineage, we define a quality score and a lineage-
balance weight:
bt k = max f∈P t k q(f), d t k = 1 |P t k|+ 1 .(7)
The first term reflects the strongest active factor within the
lineage, while the second assigns greater weight to less
represented lineages. Their normalized mixture defines the
lineage-selection distribution:
πt lin(k) =λ bt kPmt
ℓ=1 bt ℓ + (1−λ) dt kPmt ℓ=1 dt ℓ ,(8)
whereλ∈[0,1]controlsthetrade-offbetweenfavoringhigh-
qualitylineagesandmaintainingexplorationacrosslineages.
After selecting lineagek, LSPS samples a parent in pro-
portion to its robust quality:
πt par(f|k) = q(f)P
g∈P t k q(g) , f∈ P t k.(9)
This two-stage probabilistic selection exploits stronger fac-
tors while preserving alternatives at both the lineage and
parent levels.
For mutation, one parent is sampled from the selected
lineage. For crossover, this first parentpa t is fixed as the
primary parent, while a secondary donorpb t is drawn from
another lineage whenever possible under the same sampling
rule.Theallocatedandinheritedlineagesthereforecoincide:
p⋆ t =p a t , ρ t+1(ft+1) =ρ t(p⋆ t ) =r k.(10)
The secondary parent contributes the donor subtree and is
retained through a secondary ancestry edge.
Search allocation and solution preservation are handled
separately. The lineage-bucketed active population governs
future parent selection, while an independent elite archive
At retains high-quality factors for final selection.
Lineage-Conditioned LLM Variation
Modules 3–5 in Figure 1 use evolutionary experience as-
sociated with each lineage to condition LLM-based seman-
tic variation. Each valid offspring produces an evolutionary
event that records the parent and offspring structures, their
expression difference, the applied operator, and train/valida-
tion evidence. A mutation event is associated with its parent
lineage,whereasacrossovereventisassociatedwiththepri-
mary lineage while retaining the secondary donor relation.
We refer to the experience accumulated within a lineage as
Lineage-Scoped Search Experience(LSSE).
Mutation and crossover require different forms of expe-
rience. Mutation priors summarize beneficial and harmful
local modifications within one lineage, whereas crossover
priors capture transferability, complementarity, and incom-
patibility between recipient and donor structures. Accord-
ingly, each lineage maintains separate priorsSt k,o foro∈
{mut,cross}, whileG t o stores the corresponding cross-
lineage experience. Mutation uses the prior of its parent lin-
eage,whereascrossoverusesbothparent-lineagepriors,with
the primary prior describing the recipient backbone and the
secondary prior providing donor-side guidance.
Thepriorsareupdatedincrementallybyanevent-triggered
LLM rewriter:
St+1 k,o = Ψo  St k,o, et+1  ,
Gt+1 o = Ψglob o  Gt o, et+1  . (11)
Here,kdenotesthemutation-parentlineageorthecrossover
primary lineage. For crossover, only the primary-lineage
prior and global crossover prior are updated because the
offspringinheritstheprimarybackbone;thesecondaryprior
remains read-only. When an improvement or degradation
trigger is activated, the rewriter uses its financial and math-
ematical knowledge to interpret how the parent–offspring
structural change alters the factor’s signal construction and

whether the performance metric change supports or contra-
dictstheexistingguidance.Itthenrevisesthestructuredprior
by strengthening supported hypotheses, weakening contra-
dictedones,andrecordingreusabletransformationprinciples
or failure warnings. Mutation updates summarize beneficial
and harmful local edits, while crossover updates describe
transferabledonorstructuresandtheircompatibilitywiththe
primarybackbone.Alightweightdeterministicmanagerval-
idates the structured output and retains the previous state if
rewriting fails.
Weusethetermpriortodenoteastructuredpre-generation
inductivebiasratherthananormalizedBayesiandistribution.
Distilled from previous evolutionary evidence and provided
before the next variation step, it biases the LLM toward his-
torically promising transformations.
LetS t denote the lineage-prior input for the current vari-
ation. The conditioning context is constructed as
Ct = Φot

St, Gt ot ;λ t kt,ot  ,(12)
whereΦ o is a deterministic fusion and prompt-rendering
policy. The emphasis parameterλt k,o is regulated from the
recent evolutionary state of lineagek, including its perfor-
mance trend and stagnation status. When the lineage con-
tinues to improve, the policy places greater emphasis on its
lineage-specific prior to exploit locally effective variation.
Under stagnation or degradation, it increases the emphasis
ontheglobalpriortointroducetransferablecross-lineageex-
perience and reduce local search bias. The policy then fuses
the two prior sources and renders the resulting context as
concise natural-language guidance for the candidate LLM.
LetP t contain either one mutation parent or an ordered
primary–secondarycrossoverpair,andletΓdenotethefactor
grammar and generation constraints. The LLM induces
ft+1 ∼p θ (· |ot, Pt, Ct,Γ).(13)
The conditioning context acts as soft semantic guidance
rather than a hard search constraint. Consequently, the LLM
retains the flexibility to construct new factor structures
while receiving persistent lineage-relevant context unavail-
able from the current parents alone.
Feedback and Search-State Update
Module 6 and the feedback path in Figure 1 complete each
searchiteration.Wesummarizethesearchstateatiterationt
as
Ωt =  Gt,P t,A t,{S t k,o}k,o,{G t o}o  .(14)
A generated expression first undergoes deterministic
checks for grammar, syntax, duplicate expressions, con-
straints,andexecutability.Invalidcandidatesdonotenterthe
evolutionaryDAGorconsumethevalid-evaluationbudget.A
validcandidateisevaluatedonthetrainingandvalidationpe-
riods, producing an eventet+1 that records its performance,
operator, parent relations, expression change, and general-
ization evidence. The search state then evolves according
to
Ωt+1 =U  Ωt, ft+1, et+1  ,(15)
whereUupdates the lineage DAG, active population, and
elite archive, and invokes the primary-lineage and global
prior updates in Equation 11 when the deterministic trigger
is satisfied.
The updated lineage state carries operator experience
acrossgenerationswhiledetermininghowsubsequentsearch
opportunities are allocated. It therefore connects persistent
LLM guidance with lineage-level population control within
a single evolutionary loop.
Experiments
We evaluateLineageEvoon formulaic alpha factor min-
ing to answer the following questions: (1) whether lineage-
aware search finds more predictive and stable factors; (2)
whether lineage and global priors provide useful guidance
forLLM-basedvariation;(3)whetherLineage-StratifiedPar-
ent Selection (LSPS) improves factor diversity and reduces
searchconcentration;and(4)whetherLineageEvogenerates
higher-quality factors efficiently in the search.
Experimental Setup
Evaluation metrics.We report IC and ICIR to measure
factor predictiveness, where IC denotes the average cross-
sectional correlation between factor values and future re-
turns, and ICIR reflects the temporal stability of IC. We
also report portfolio-level metrics, including annualized re-
turn (AR), information ratio (IR), and maximum drawdown
(MDD). AR and IR measure profitability and risk-adjusted
performance, while MDD captures downside risk. Detailed
metric definitions are provided in the supplementary mate-
rial.
Dataset.We conduct experiments on two market uni-
verses: CSI 500 in the Chinese A-share market and S&P
500 in the U.S. stock market. Both markets use the same
fixed temporal split: data from 2015-01-01 to 2020-12-31
for training, 2021-01-01 to 2022-04-30 for validation, and
2022-05-01 to 2026-04-30 for testing.
Baselines.We compareLineageEvowith representative
baselines from three categories: (1)traditional factor min-
ing methods, including Alpha158 (Yang et al. 2020), GP
(Koza 1992), AlphaGen (Yu et al. 2023), and AlphaSAGE
(Chenetal.2025);(2)LLM-basedfactorminingmethods,
includingRD-Agent(Lietal.2025)andAlphaPROBE(Guo
etal.2026);and(3)LLM-EAmethods,includingEoH(Liu
etal.2024)andReEvo(Yeetal.2024).Detaileddescriptions
of the baselines are provided in the supplementary material.
Implementation details.For all LLM-based methods,
we usedeepseek-v4-flash.LineageEvoinitializes
each run with 10 LLM-generated seed roots and targets
three mutation and two crossover offspring per genera-
tion until reachingB= 200valid evaluated factors.
LineageEvouses an active pool of 50 factors and an
elite archive of 20, with(α, β, γ) = (0.2,0.8,0.1), and
λLSPS = 0.8. We use IC as the optimization metricMin
the reported experiments. The prior improvement/degrada-
tion thresholds are(0.003,0.30)/(0.012,0.60)on CSI 500
and(0.0015,0.20)/(0.006,0.40)on S&P 500, where each

CSI 500 S&P 500
Method IC↑ICIR↑AR↑IR↑MDD↓IC↑ICIR↑AR↑IR↑MDD↓
Alpha158 0.0076 0.0787 15.50% 0.6866 31.62% 0.0081 0.0426 17.58% 0.7715 21.03%
GP 0.0074 0.0774 15.28% 0.6861 33.08% 0.0055 0.0575 21.38% 1.0958 20.55%
AlphaGen 0.0345 0.2215 15.04% 0.7176 36.31% 0.0099 0.0587 20.38% 0.9709 23.87%
AlphaSAGE 0.0230 0.1855 13.71% 0.7654 21.31% 0.0118 0.0668 18.32% 0.8539 21.62%
RD-Agent 0.0395 0.2253 14.14% 0.7199 29.48% 0.0094 0.0464 11.05% 0.7642 20.61%
AlphaPROBE 0.0385 0.2298 11.87% 0.7587 20.48% 0.0119 0.0622 5.86% 0.4597 25.55%
EoH 0.0399 0.2493 9.51% 0.5715 21.50% 0.0072 0.0404 23.13% 0.9682 21.83%
ReEvo 0.0303 0.1950 13.66% 0.6030 42.98% 0.0047 0.0267 16.10% 0.7397 18.94%
LineageEvo 0.0512 0.2740 15.55% 0.9856 19.39% 0.0134 0.0907 27.00% 1.1693 17.05%
Table 1: Main results on CSI 500 and S&P 500. Bold and underlined values denote the best and second-best results.
pair gives the absolute and relative thresholds. All meth-
ods use the same Qlib TopK-Dropout backtest with top-
K= 50,n drop = 5, daily rebalancing, and matched risk
and transaction-cost settings (Yang et al. 2020). Complete
prompt templates, DSL definitions, prior schemas, and vali-
dation rules are provided in the supplementary material.
Main Results
Table 1 comparesLineageEvowith representative tradi-
tional, LLM-based, and LLM-EA factor mining methods
on both factor-level and portfolio-level metrics. For each
method,weselectthetop20factorsfromitsfinalfactorpool
accordingtothemethod-specificselectioncriterionwhenap-
plicable,combinethemintoafactorset,andevaluatethere-
sulting combined signal under the same evaluation pipeline.
LineageEvoachieves the best result on all five metrics in
both markets. On CSI 500, it obtains an IC of 0.0512 and an
ICIR of 0.2740, together with the highest AR (15.55%) and
IR (0.9856) and the lowest MDD (19.39%). On S&P 500, it
similarlyachievesthehighestIC(0.0134),ICIR(0.0907),AR
(27.00%),andIR(1.1693),whilereducingMDDto17.05%.
TheconsistentimprovementsinICandICIRindicatethatthe
discovered factors provide both stronger out-of-sample pre-
dictiveness and greater temporal stability. Meanwhile, the
gains in AR and IR together with lower drawdown show
that these predictive improvements can translate into more
profitableandrisk-controlledportfoliosacrossbothmarkets.
Overall, the results support the effectiveness of combining
lineage-conditioned variation with lineage-level search allo-
cation.
Figure 2 shows that while achieving high predictive
power,LineageEvomaintains competitive cumulative re-
turns throughout the test period and becomes one of the
strongest-performing methods in the later stage, ultimately
finishingwiththehighestcumulativereturnamongthecom-
pared approaches.
Ablation on Search Priors
We isolate the contribution of each component in the prior
system.LineageEvouses lineage priors to capture lineage-
scopedexperienceandglobalpriorstoprovidecross-lineage
2023 2024 2025 2026
Date
0.8
1.0
1.2
1.4
1.6Cumulative Return
AlphaGen
AlphaSAGE
RD-Agent
AlphaProbe
EoH
ReEvo
LineageEvo
CSI500 Index
Figure2:Cumulativereturncurvesofdifferentfactormining
methods on CSI 500 during the test period.
regularization. Since mutation and crossover require differ-
ent forms of evolutionary experience, we also examine the
contributionsoftheircorrespondingoperator-specificpriors.
We consider the following variants:
•Full: the completeLineageEvoframework.
•w/o all priors: removes both lineage and global priors.
•w/o lineage priors: removes lineage mutation and
crossover priors while retaining global priors.
•w/oglobalpriors:removesglobalmutationandcrossover
priors while retaining lineage priors.
•w/o mutation priors: removes both lineage and global
mutation priors while retaining crossover priors.
•w/o crossover priors: removes both lineage and global
crossover priors while retaining mutation priors.
The ablation results confirm the effectiveness of the prior
system. Removing all priors reduces IC from 0.0512 to
0.0384 and ICIR from 0.2740 to 0.1994, showing that prior-
guided variation substantially improves factor quality. Re-
movinglineagepriorsproducesasimilarlylargedegradation,

Variant IC↑ICIR↑
w/o all priors 0.0384 0.1994
w/o lineage priors 0.0390 0.2041
w/o global priors 0.0495 0.2579
w/o mutation priors 0.0438 0.2673
w/o crossover priors 0.0445 0.2362
FullLineageEvo0.0512 0.2740
Table 2: Ablation study of the search-prior components on
CSI 500.
indicatingthatlineage-scopedexperienceisthemainsource
of useful guidance, while global priors alone cannot fully
capture the transformation patterns specific to each lineage.
The operator-specific ablations further reveal the important
roles of mutation and crossover priors.
Factor Diversity and Search Concentration
We evaluate how LSPS affects predictive performance, lin-
eage concentration, and expression diversity in the active
factor pool. We compareLineageEvowith a variant that
removes LSPS and samples parents directly from the active
poolwithoutlineagestratification.Lineageentropymeasures
how evenly factors are distributed across lineages, average
pairwise AST distance measures expression-level structural
diversity,andtheeffectivenumberofstructuresestimatesthe
number of non-redundant structural families in the pool.
Method IC↑ICIR↑
Lineage
Entropy↑
AST
Dist.↑
Eff.
Struct.↑
w/o LSPS 0.0381 0.2415 0.405 0.509 37.89
LineageEvo0.0512 0.2740 2.154 0.747 41.90
Table 3: Effect of LSPS on predictive performance and di-
versity on CSI 500. Higher values are better.
As shown in Table 3, LSPS improves IC from 0.0381
to 0.0512 and ICIR from 0.2415 to 0.2740, while substan-
tially increasing all three diversity measures. This joint im-
provementreflectsthequality–explorationtrade-offbuiltinto
LSPS. The quality component continues to allocate search
opportunities to lineages containing strong factors, allowing
promising structures to be refined across successive gener-
ations. Meanwhile, the lineage-balance component prevents
these branches from monopolizing the search and preserves
opportunitiesforunderrepresentedlineagesthatmaycontain
distinctbutstillpromisingdirections.Consequently,thefinal
factor pool retains high-performing descendants while cov-
ering a broader and less redundant set of structures. Such a
poolismorelikelytoprovidecomplementarycandidatesfor
factor combination, which is consistent with the higher IC
andICIRachievedbythefullmethod(Sudholt2018;Gabor,
Belzner,andLinnhoff-Popien2018;Yuetal.2023;Shietal.
2024).
Search Efficiency
We analyze whetherLineageEvocan discover high-quality
factors more efficiently under the same budget. For each
method, we track the top-5 mean-so-far absolute IC during
the search process. Specifically, at each evaluation check-
point, we collect all valid factors generated so far, select the
five factors with the highest absolute IC, and report their
average IC.
0 25 50 75 100 125
0.040
0.041
0.042
0.043
0.044
0.045
0.046
0.047
0.048
Shaded band: Top-5 mean ± 0.5 std.
LineageEvo
AlphaProbe
RD-Agent
Figure 3: Search efficiency comparison on CSI 500. The x-
axis denotes the number of valid evaluated factors, and the
y-axis reports the top-5 mean-so-far absolute IC.
Figure3showsdifferentsearchbehaviorsamongthethree
methods. RD-Agent improves quickly in the early stage but
soon saturates at a relatively low top-5 mean-so-far IC, sug-
gesting that it can rapidly identify some usable factors but
lacksa mechanismto continuouslyexploit promisingsearch
directions.AlphaPROBEimprovesmoregraduallyandeven-
tually reaches a stronger factor set than RD-Agent, but its
improvement requires more evaluations. In contrast,Lin-
eageEvomaintains a consistently higher top-5 mean-so-far
ICthroughoutmostofthesearchprocessandreachesastrong
plateauwithinabout75validevaluations.Thispatterniscon-
sistent with the intended role of lineage-conditioned priors
in preserving useful search guidance across generations.
Conclusion
Inthispaper,weproposedLineageEvo,anLLM-EAframe-
work that uses lineage as an intermediate organizational
unit for evolutionary factor mining.LineageEvocombines
lineage-conditioned priors for guiding LLM variation with
Lineage-Stratified Parent Selection for distributing search
opportunities across lineages. The resulting framework dis-
covers highly predictive and stable factors, achieves strong
investmentreturns,andpreservesamorediversefactorpool.
Future work may compare lineage with other intermediate
organizational units, such as clusters, niches, and retrieval
neighborhoods,tostudytheirrespectiveadvantagesinexpe-
rience reuse and search control.
References
Burke, E. K.;Gustafson, S. M.; Kendall, G.; andKrasnogor,
N. 2003. Is Increased Diversity in Genetic Programming

Beneficial? An Analysis of Lineage Selection. InProceed-
ings of the 2003 Congress on Evolutionary Computation,
volume 2, 1398–1405. IEEE.
Burlacu, B.; Affenzeller, M.; Kommenda, M.; Winkler, S.;
andKronberger,G.2013. VisualizationofGeneticLineages
and Inheritance Information in Genetic Programming. In
Proceedings of the 15th Annual Conference Companion on
Genetic and Evolutionary Computation, 1351–1358. ACM.
Chen, B.; Ding, H.; Shen, N.; Huang, J.; Guo, T.; Liu,
L.; and Zhang, M. 2025. AlphaSAGE: Structure-Aware
Alpha Mining via GFlowNets for Robust Exploration.
arXiv:2509.25055.
Gabor, T.; Belzner, L.; and Linnhoff-Popien, C.
2018. Inheritance-Based Diversity Measures for Ex-
plicit Convergence Control in Evolutionary Algorithms.
arXiv:1810.12470.
Guo, T.; Shen, H.; Luo, J.; Chen, B.; Ding, H.; Huang, J.;
Liu, L.; Ma, Y.; and Zhang, M. 2026. AlphaPROBE: Al-
pha Mining via Principled Retrieval and On-graph Biased
Evolution. arXiv:2602.11917.
Han,J.;Zhang,S.;Li,W.;Yang,Z.;Dong,Y.;Hu,T.;Yuan,
J.;Yu,X.;Zhu,Y.;Lou,F.;Guo,X.;Liu,Z.;Jiang,T.;An,R.;
Liu,J.;Wu,B.;Chen,R.;Wang,K.;Wang,Y.;Hu,S.;Kong,
X.; Zhang, L.; Chen, R.; and Wang, H. 2026. QuantaAlpha:
AnEvolutionaryFrameworkforLLM-DrivenAlphaMining.
arXiv:2602.07085.
Kakushadze, Z. 2016. 101 Formulaic Alphas.Wilmott,
2016(84): 72–81.
Koza, J. R. 1992.Genetic Programming: On the Program-
ming of Computers by Means of Natural Selection. MIT
Press.
Li, Y.; Yang, X.; Yang, X.; Xu, M.; Wang, X.; Liu, W.; and
Bian, J. 2025. R&D-Agent-Quant: A Multi-Agent Frame-
workforData-CentricFactorsandModelJointOptimization.
arXiv:2505.15155.
Liu, F.; Tong, X.; Yuan, M.; Lin, X.; Luo, F.; Wang, Z.; Lu,
Z.;andZhang,Q.2024.EvolutionofHeuristics:TowardsEf-
ficient Automatic Algorithm Design Using Large Language
Model. arXiv:2401.02051.
Liu, S.; Chen, C.; Qu, X.; Tang, K.; and Ong, Y.-S.
2023. Large Language Models as Evolutionary Optimizers.
arXiv:2310.19046.
Luo,H.;Ko,H.T.;Chen,J.;Sun,D.;Zhang,Y.;andLiu,C.
2026a.AlphaBench:BenchmarkingLargeLanguageModels
in Formulaic Alpha Factor Mining. InProceedings of the
International Conference on Learning Representations.
Luo, H.; Ko, H. T.; Sun, D.; Zhang, Y.; and Liu, C. 2026b.
EvoAlpha:EvolutionaryAlphaFactorDiscoverywithLarge
Language Models. InNeurIPS 2025 Workshop: Generative
AI in Finance.
Ren, J.; Zhao, J.; Liu, S.; and Yang, P. 2025. From Lin-
ear to Hierarchical: Evolving Tree-structured Thoughts for
Efficient Alpha Mining. arXiv:2508.16334.
Shi, H.; Song, W.; Zhang, X.; Shi, J.; Luo, C.; Ao, X.; Ar-
ian, H.; and Seco, L. 2024. AlphaForge: A Framework to
Mine and Dynamically Combine Formulaic Alpha Factors.
arXiv:2406.18394.
Shi, Y.; Duan, Y.; and Li, J. 2025. Navigating the Alpha
Jungle: An LLM-Powered MCTS Framework for Formulaic
Factor Mining. arXiv:2505.11122.
Sudholt, D. 2018. The Benefits of Population Diversity in
Evolutionary Algorithms: A Survey of Rigorous Runtime
Analyses. arXiv:1801.10087.
Tang, Z.; Chen, Z.; Yang, J.; Mai, J.; Zheng, Y.; Wang, K.;
Chen,J.;andLin,L.2025. AlphaAgent:LLM-DrivenAlpha
Mining with Regularized Exploration to Counteract Alpha
Decay. arXiv:2502.16789.
Wang, S.; Yuan, H.; Zhou, L.; Ni, L. M.; Shum, H.-Y.; and
Guo, J. 2023. Alpha-GPT: Human-AI Interactive Alpha
Mining for Quantitative Investment. arXiv:2308.00016.
Yang, X.; Liu, W.; Zhou, D.; Bian, J.; and Liu, T.-Y.
2020. Qlib: An AI-oriented Quantitative Investment Plat-
form. arXiv:2009.11189.
Ye, H.; Wang, J.; Cao, Z.; Berto, F.; Hua, C.; Kim,
H.; Park, J.; and Song, G. 2024. ReEvo: Large Lan-
guageModelsasHyper-HeuristicswithReflectiveEvolution.
arXiv:2402.01145.
Yin, H.; Kononova, A. V.; Bäck, T.; and van Stein, N. 2024.
Controlling the Mutation in Large Language Models for the
Efficient Evolution of Algorithms. arXiv:2412.03250.
Yu, S.; Xue, H.; Ao, X.; Pan, F.; He, J.; Tu, D.; and He, Q.
2023. Generating Synergistic Formulaic Alpha Collections
via Reinforcement Learning. arXiv:2306.12964.
Zhang,T.;Li,Y.;Jin,Y.;andLi,J.2020.AutoAlpha:AnEffi-
cientHierarchicalEvolutionaryAlgorithmforMiningAlpha
Factors in Quantitative Investment. arXiv:2002.08245.
A Case Study
Illustrativetrace.Figure4showstwosequentialmutation
events on sibling branches of the same lineage in a CSI500
run.Atgeneration30,Event1replacesTsSkewwithTsCov
between close and high returns, increasing validation|IC|
from 0.0209 to 0.0369. This event triggers both lineage and
global prior rewriting. Event 2 then receives the updated
priorsbeforegeneratingarelatedmutationonanotherbranch
of the same lineage. All reported values are absolute IC
strengths.
Rendered prior guidance.Before Event 2, Event 1 had
already triggered lineage and global prior rewriting. The
following excerpt shows the actual prior-related guidance
rendered into the mutation prompt.
Prompt A.1: Actual Prior Guidance Before Event 2
1Mutation experience for this lineage:
2- Effective pattern:
3Replacing TsSkew with TsCov between
close returns and a second
4price series, while preserving the
20-day rolling window,
5produced a strong validation IC
improvement.
6
7- Failed patterns:

Same-lineage prior transfer across sibling branches
CSI500  |  Generation 30  |  Lineage f_e31f9b51a9d7
1 Evidence creates a reusable prior
Mutation on the evidence branch
2 A sibling branch applies the prior
Later mutation call in the same lineage
PARENT
TsSkew(
  TsPctChange(close, 1), 20
)
mutation
CHILD
TsCov(
  TsPctChange(close, 1),
  TsPctChange(high, 1), 20
)
|IC_train| +0.0211
0.0165  ->  0.0376
|IC_validation| +0.0160
0.0209  ->  0.0369
PRIOR WRITTEN
Replace TsSkew with close/high-return TsCov;
keep the 20-day window.
medium confidence  |  support = 1
PRIOR READ:  TsSkew -> TsCov(close return, high return); keep window 20
SIBLING PARENT
Div(TsSkew(TsPctChange(close,1),20),
    Add(TsStd(TsPctChange(close,1),20),0.001))
mutation
PRIOR-GUIDED CHILD
Div(TsCov(TsPctChange(close,1),
          TsPctChange(high,1),20),
    Add(TsStd(TsPctChange(close,1),20),0.001))
|IC_train| +0.0242
0.0136  ->  0.0378
|IC_validation| +0.0172
0.0150  ->  0.0323
PRIOR REINFORCED
medium -> high confidence  |  support: 1 -> 2
Dashed link: prior transfer across sibling branches, not a DAG ancestry edge
persistent
lineage prior
Figure 4: A same-lineage prior-reuse case. Event 1 replacesTsSkewwith a close/high-returnTsCov, triggering a structured
prior rewrite. Event 2 receives this prior on a sibling branch, applies the same replacement while preserving its denominator,
and strengthens the pattern from medium to high confidence. The dashed connector denotes prior transfer.
8Avoid replacing TsSkew with TsCorr
or TsIr.
9Avoid introducing raw volume terms
or EMA smoothing.
10Preserve the close-return
distributional backbone.
11
12- Hint:
13TsCov with a second price-return
series may be useful, while
14correlation, smoothing, and volume-
based modifications have
15repeatedly degraded this lineage.
16
17- Bias warning: medium
18
19
20Global mutation experience:
21- Percentage-change inputs have
repeatedly strengthened covariance
22and correlation structures across
lineages.
23
24- TsCov/TsCorr structures should
operate on transformed return-like
25inputs rather than raw price or
volume levels.
26
27- Avoid TsIr substitutions,
unnecessary smoothing, and volume-
delta
28multipliers.
29
30- Last updated generation: 30
31
32
33Prior fusion decision:
34- Lineage prior weight: 0.45
35- Global prior weight: 0.55
36- Balance lineage-specific evidence
with global operator guidance.
The example illustrates the complementary roles of the
two prior levels. The lineage prior provides factor-family-
specific evidence about successful and failed transforma-
tions,whereastheglobalpriorcontributespatternsobserved
across lineages. Their relative emphasis is determined by
the fusion policy before the guidance is inserted into the
candidate-generation prompt.
B Metric Definitions
Letfdenoteaformulaicfactor,z f i,titsvalueforstockiatdate
t, andri,t+∆ the future return used as the prediction target.
LetU tbethetradablestockuniverseatdatet.Thefactor-level
and portfolio-level metrics follow standard formulaic-alpha
and Qlib evaluation practice (Kakushadze 2016; Yang et al.
2020).
Information Coefficient (IC).We compute the daily
cross-sectional Spearman correlation between factor values
and future returns:
ICt(f) = corr Spearman i∈Ut

zf i,t, ri,t+∆

.(16)
ThereportedICisthetemporalmeanofdailycross-sectional
IC:
IC(f) = 1 |T | X t∈T ICt(f).(17)

Under this implementation, IC is equivalent to RankIC.
Information Coefficient Information Ratio (ICIR).
ICIR measures the temporal stability of daily IC:
ICIR(f) = meant∈T [ICt(f)] stdt∈T [ICt(f)] +ϵ ,(18)
whereϵis used only to avoid division by zero.
Annualized Return (AR).LetR t denote the daily return
series passed to Qlib’s risk-analysis routine and letNde-
note its daily annualization scaler. Following Qlib’s default
arithmetic accumulation, we report
AR =Nmean t∈T [Rt].(19)
InformationRatio(IR).Risk-adjustedreturnismeasured
as
IR = meant∈T [Rt] stdt∈T [Rt] +ϵ √ N .(20)
Maximum Drawdown (MDD).Under arithmetic return
accumulation, letC t = P τ≤t Rτ. Qlib’s signed drawdown
statistic is
MDDsigned = min t∈T

Ct −max τ≤t Cτ

.(21)
WhenatablereportsMDDwithadownwardarrowandnon-
negative entries, we use the magnitude|MDDsigned|; when
signed values are shown, values closer to zero are better.
Validation-OrientedTestMetrics.Thefactordirectionis
fixedusingvalidationinformationbeforetestevaluation.For
a metricM, the oriented test IC is
ICoriented test (f) = sign(M val(f)) ICtest(f).(22)
Noteststatisticisusedforfactororientation,parentselection,
prior updating, or final factor selection.
Top-5 Mean-so-Far IC.LetF k denote the valid factors
discovered within the firstkvalid evaluations. Search effi-
ciency is summarized using validation IC:
Top5ICval(k) = 1 5 X f∈Top5(Fk) |ICval(f)|,(23)
whereTop5(F k)contains the five factors with the largest
absolutevalidationICdiscoveredsofar.Invalidandduplicate
attemptsdonotadvancethehorizontal-axisevaluationcount.
Lineage Entropy.Letp L be the fraction of factors in the
evaluatedpopulationstatethatbelongtolineageL.Wecom-
pute
Hlineage =−
X
L
pL logp L.(24)
Higher entropy indicates a more balanced allocation across
lineages(Sudholt2018;Gabor,Belzner,andLinnhoff-Popien
2018).
AveragePairwiseASTDistance.Wemeasureexpression-
level diversity with normalized tree-edit distance between
factor abstract syntax trees (ASTs). For a factor setS,
DAST(S) = 2 |S|(|S| −1) X i<j dAST(fi, fj).(25)
A larger value indicates greater structural dissimilarity.
Effective Number of Structures.For each factorf, let
σ(f)denote the complete structural signature of its normal-
ized AST. We apply the same canonical normalization used
forexpressiondeduplicationandretainallnodesandordered
parent–child relations in the resulting tree. Two factors be-
long to the same structural group if and only if
σ(fi) =σ(f j).(26)
Thus,thegroupscorrespondtoexactnormalizedASTstruc-
turesratherthandistance-basedclustersorpartialmotifs.Let
pc betheempiricalfrequencyofstructuralsignaturecinthe
factor set. We report
Neff = exp

−
X
c
pc logp c
!
,(27)
which gives the number of equally represented structures
with the same structural entropy.
C Baseline Descriptions
WecompareLineageEvowithrepresentativebaselinesfrom
traditional factor mining, LLM-based factor mining, and
LLM-EA factor mining.
Alpha158.Alpha158 is a standard hand-crafted factor set
provided in Qlib and serves as a non-search reference (Yang
et al. 2020).
GeneticProgramming(GP).GPprovidesaclassicalnon-
LLM evolutionary baseline based on symbolic mutation,
crossover, and fitness selection (Koza 1992).
AlphaGen.AlphaGen generates synergistic formulaic al-
pha collections through reinforcement learning (Yu et al.
2023).
AlphaSAGE.AlphaSAGE performs structure-aware fac-
tor mining with GFlowNet-based exploration (Chen et al.
2025).
RD-Agent.R&D-Agent-Quant is an LLM-based multi-
agentframeworkfordata-centricfactorandmodeloptimiza-
tion (Li et al. 2025).
AlphaPROBE.AlphaPROBE combines principled re-
trievalwithon-graphbiasedevolutionforalphamining(Guo
et al. 2026).
EoH.EvolutionofHeuristicsusesLLMstoiterativelygen-
erate, evaluate, and evolve heuristic programs (Liu et al.
2024).
ReEvo.ReEvo uses reflective evolution to guide LLM-
based heuristic search (Ye et al. 2024).

Component Parameter Setting
LLM Backenddeepseek-v4-flashthrough an OpenAI-compatible client
LLM Temperature / maximum tokens0.7/8000
LLM Timeout / retries / retry wait120s /5/5s
Search Valid-evaluation budgetB= 200
Search Initial lineage roots10LLM-generated seed factors
Search Validmutation/crossoverslotspergen-
eration
3/2
Search Maximum attempts per slot5
Population Population capacity / elite archive ca-
pacity
50/20
Population Maximum share of one lineage0.40
Expression Prompt / deterministic length limits40/50
Robust score(α, β, γ) (0.2,0.8,0.1)
LSPS Quality / diversity mixture weights(0.8,0.2)
Backtest Top-K/n drop / risk degree50/5/0.95
Backtest Rebalancing frequency Daily
Backtest Buy / sell costopen_cost= 0.0015/close_cost= 0.0025
Backtest Minimum transaction costmin_cost= 5
Finalization Number of selected factors1,5, or20, as specified
Table 4: Main implementation and evaluation parameters.
D Experimental Protocol and
Implementation Details
Markets, target, and temporal splits.We evaluate on
CSI500 and S&P 500 using daily data and a common Qlib-
compatiblepipeline(Yangetal.2020).Thepredictiontarget
is the next-period return implemented as
Ref($close,-2)/Ref($close,-1)-1.(28)
Forbothmarkets,2015-01-01to2020-12-31isusedfortrain-
ing, 2021-01-01 to 2022-04-30 for validation, and 2022-05-
01 to 2026-04-30 for testing. Training and validation data
may be used during search; the test period is accessed only
after the final selection rule and factor set are fixed.
Core experimental parameters.Table 4 summarizes the
shared configuration. Values associated with final Top-K
selectionvaryonlywhenthecorrespondingTop-1,Top-5,or
Top-20 result is explicitly reported.
Candidate generation schedule.Each LLM call returns
exactly one candidate expression. A generation targets three
valid mutation offspring and two valid crossover offspring.
Each slot permits at most five generation attempts. Invalid,
duplicate,andfailed-evaluationcandidatesareloggedbutdo
not count toward the valid-evaluation budget.
Expression grammar and deterministic validation.
Candidates may use only the configured market variables,
constants, and DSL operators. Validation checks JSON/-
expression parsing, permitted variables and operators, con-
stantsandwindowarguments,normalized-expressiondupli-
cation, expression length, Qlib executability, empty or con-
stantoutputs,andNaN/Infvalues.Onlyvalidevaluatedcan-
didates are inserted into the lineage DAG.
Optimizationmetricandrobustqualityscore.Thecon-
figured optimization metricMis IC or ICIR. For factors
satisfying|M tr(f)|+|M val(f)|>0, let
T(f) =|M tr(f)|, V(f) =|M val(f)|.(29)
Parent, lineage-quality, and final-selection decisions use
q(f) = 0.2T(f) + 0.8V(f)−0.1|M tr(f)− Mval(f)|.
(30)
The validation term receives the largest weight, while the
signeddiscrepancypenalizesbothstrengthdisagreementand
directional reversals between training and validation.
Lineage-stratified sampling.For lineagek, letb k =
maxf∈P k q(f)andd k = (|P k|+ 1) −1. The lineage dis-
tribution is
πlin(k) = 0.8 bkP
j bj
+ 0.2 dkP
j dj
.(31)
After sampling lineagek, a parent is sampled according to
πpar(f|k) = q(f)P
g∈Pk q(g) .(32)
The population updater additionally limits the fraction of
active factors belonging to any one lineage to0.40.
Mutation, crossover, and lineage inheritance.Mutation
selects one lineage and one parent. Crossover selects an an-
chorlineageandparent,thenpreferentiallysamplesthepart-
ner from another lineage using the same quality–diversity
policyovertheremaininglineages.Theparentsampledfrom
the first selected lineage becomes the primary parent. The
child inherits the primary parent’s lineage, while the other
parent is retained through a secondary crossover edge. Op-
erationally, crossover replaces or enriches a subtree of the
primary parent with a subtree-level structure from the sec-
ondary parent.

Operator-specific priors and fusion.Each lineage main-
tains separate mutation and crossover priors, and the search
maintains corresponding global operator priors. Structured
prior states are rendered into concise natural-language guid-
ance before candidate generation. A deterministic fusion
policy determines the relative emphasis on lineage-specific
and global experience; the resulting context is soft guidance
rather than a hard expression constraint. All compared vari-
ants share the same fusion and prompt infrastructure unless
a prior source is explicitly removed.
Event-triggered prior rewriting.Prior rewriting is con-
sidered only after a valid candidate has been evaluated. We
take IC as an example. LetICpar andIC child denote the IC
values of the reference parent and its offspring, respectively.
For crossover, the primary parent serves as the reference
parent. All comparisons use absolute IC strength, consistent
with the search objective.
On CSI500, an improvement trigger is activated when
|ICchild| − |ICpar| ≥max (0.003,0.30|ICpar|),(33)
whereas a degradation trigger is activated when
|ICpar| − |ICchild| ≥max (0.012,0.60|ICpar|).(34)
S&P 500 uses more sensitive thresholds. Its improvement
and degradation thresholds aremax(0.0015,0.20|IC par|)
andmax(0.006,0.40|IC par|), respectively.
When either trigger is activated, the rewriter receives the
previous structured prior together with a structured sum-
mary of the evolutionary event and returns a complete up-
dated state rather than a partial patch. A deterministic man-
ager checks the output schema, merges redundant entries,
removes low-value content, and retains the previous prior if
rewriting fails. If neither trigger is activated, the prior re-
mains unchanged. This event-triggered mechanism differs
from unrestricted free-form reflection (Ye et al. 2024).
Population and elite archive.The population is used for
futuresearchallocationandisorganizedbylineage.Theelite
archiveisupdatedindependentlyandpreservesthestrongest
evaluated factors.
Final factor selection and orientation.Final factors are
selected primarily from the elite archive using the same ro-
bustscoreq(f)definedabove.Expressionsarededuplicated
after normalization. The sign of each selected factor is fixed
usingthecorrespondingvalidationmetric,andnoteststatis-
tic participates in selection or orientation. For Top-Keval-
uation, theKhighest-scoring distinct factors are selected
directly.WhenK >1,orientedfactorvaluesarenormalized
cross-sectionallyeachdayandcombinedwithequalweights.
Backtesting protocol.Portfolio evaluation uses Qlib’s
TopkDropoutStrategywithtopk= 50,n_drop=
5,risk_degree= 0.95, and daily execution (Yang
et al. 2020). The transaction-cost configuration uses the
Qlib default values:open_cost= 0.0015for purchases,
close_cost= 0.0025forsales,andmin_cost= 5per
transaction. The same backtesting and cost configuration is
appliedconsistentlyacrossmethodswithineachmarket.AR,
IR,andMDDarecomputedfromthecost-adjustedreturnse-
ries produced by the shared backtesting pipeline.
Ablationconfigurations.Thepriorablationspreservethe
searchbudget,LLMbackend,LSPSpolicy,validationproto-
col, and all non-ablated components.w/o all priorsremoves
lineage and global prior context;w/o lineage priorsretains
only global operator priors;w/o global priorsretains only
lineage-specific priors;w/o mutation priorsremoves both
lineage and global mutation guidance; andw/o crossover
priorsanalogously removes crossover guidance. The LSPS
ablationreplaceslineage-firstallocationwithscore-weighted
sampling over the complete population while leaving candi-
date generation and evaluation unchanged.
E Prompt Templates
LineageEvouses four principal prompt families for seed
generation, mutation, crossover, and prior rewriting. Each
LLM request contains one system message and one user
message. Candidate-generation prompts share the same fac-
torDSL,look-aheadpreventionrules,expression-lengthcon-
straints, and JSON-format requirements. For readability, the
templatesbelowretaintheoperator-specificinstructions,run-
time fields, and output schemas while abbreviating repeated
DSL definitions, validation constraints, and long examples
with bracketed placeholders.
Shared candidate-generation instructions.Seed, muta-
tion,andcrossoverpromptsinstructtheLLMtouseonlythe
permitted market variables and DSL operators, avoid future
information,andgenerateexactlyoneexecutablefactor.The
performance statistics provided to the LLM are absolute IC
orICIRstrengths;thesignusedforfinalfactororientationis
not included in candidate-generation prompts.
Seed-generationprompt.Theseedpromptencouragesdi-
versityacrossinitiallineagesandasksforafinancialhypoth-
esis together with the expression.
Prompt E.1: Seed-Generation Prompt (Compressed)
1SYSTEM
2
3You are an expert quantitative
researcher. Generate exactly one
4diverse and economically plausible
seed factor using only the
5permitted DSL. Avoid look-ahead
leakage, invalid expressions,
6and unnecessary complexity. Return
strict JSON only.
7
8USER
9
10Market: <MARKET>
11Stock universe: <UNIVERSE>
12Allowed factor language:
13[Shared DSL and operator definitions
omitted.]
14
15Maximum expression length: <
LENGTH_TARGET>
16Existing or previously rejected
factors to avoid:

Prompt Trigger Main runtime inputs Required output
Seed generation Population initialization Market, stock universe, factor DSL, expression-length target,
and existing or rejected seed expressions
One factor with hypoth-
esis and metadata in
JSON
Mutation Afterselectingoneparent Parent expression and metrics, lineage and global mutation pri-
ors, search-control state, fusion decision, and retry feedback
{"factor":
"..."}
Crossover After selecting two par-
ents
Primary and secondary expressions and metrics, their lineage
priors, global crossover prior, fusion decision, and duplicate
feedback
{"factor":
"..."}
Prior rewriting Afteraninformativevalid
evolutionary event
Previousprior,parentandchildevidence,expressiondifference,
update trigger, and target JSON schema
A complete updated
prior in JSON
Table 5: Summary of the principal prompts used byLineageEvo.
17<EXISTING_OR_REJECTED_EXPRESSIONS>
18
19Generate one seed based on a distinct
financial hypothesis.
20Return:
21{
22"factor_name": "<NAME>",
23"hypothesis": "<FINANCIAL_HYPOTHESIS
>",
24"factor": "<FACTOR_EXPRESSION>",
25"expected_signal_type": "<
SIGNAL_TYPE>",
26"rationale": "<BRIEF_RATIONALE>",
27"risk_notes": "<RISKS>"
28}
Mutation prompt.The mutation prompt conditions the
LLM on one parent, the experience accumulated within
its lineage, and the corresponding global mutation prior.
Program-computed control variables specify whether the
current search state calls for conservative or broader vari-
ation.
Prompt E.2: Mutation Prompt (Compressed)
1SYSTEM
2
3<CANDIDATE_SYSTEM_MESSAGE>
4Generate exactly one mutation
candidate and return strict JSON
only.
5
6USER
7
8Parent factor: <PARENT_EXPRESSION>
9Parent predictive strengths: <
ABSOLUTE_PARENT_METRICS>
10
11Lineage mutation prior:
12<RENDERED_LINEAGE_MUTATION_PRIOR>
13
14Global mutation prior:
15<RENDERED_GLOBAL_MUTATION_PRIOR>
16
17Search-control state:
18quality_trend = <QUALITY_TREND>
19stagnation_state = <STAGNATION_STATE>
20mutation_strength = <MUTATION_STRENGTH
>
21
22Prior-fusion decision:
23local_weight = <LOCAL_WEIGHT>
24global_weight = <GLOBAL_WEIGHT>
25instruction = <FUSION_INSTRUCTION>
26
27Recent invalid reasons: <
FAILURE_FEEDBACK>
28Previous duplicate to avoid: <
DUPLICATE_EXPRESSION>
29
30Perform one coherent targeted mutation
. Preserve useful parent
31structure unless broader exploration
is requested. Treat the
32priors as soft guidance and do not
override the program-computed
33mutation strength.
34
35[Shared DSL and validation constraints
omitted.]
36
37Return only:
38{"factor": "<NEW_MUTATED_EXPRESSION>"}
Crossoverprompt.Crossoverisimplementedasymmetri-
cally.Theprimaryparentprovidestheexpressionbackbone,
whereasthesecondaryparentprovidesalocaldonorsubtree.
The prompt includes lineage experience from both parents,
but the fusion decision is centered on the primary lineage.
Prompt E.3: Crossover Prompt (Compressed)
1SYSTEM
2
3<CANDIDATE_SYSTEM_MESSAGE>
4Generate exactly one crossover
candidate and return strict JSON
only.
5
6USER
7
8Primary parent: <PRIMARY_PARENT>
9Primary predictive strengths: <
PRIMARY_METRICS>

10Secondary parent: <SECONDARY_PARENT>
11Secondary predictive strengths: <
SECONDARY_METRICS>
12
13Primary-lineage crossover prior:
14<PRIMARY_LINEAGE_PRIOR>
15
16Secondary-lineage crossover prior:
17<SECONDARY_LINEAGE_PRIOR>
18
19Global crossover prior:
20<GLOBAL_CROSSOVER_PRIOR>
21
22Prior-fusion decision: <
FUSION_DECISION>
23Previous duplicate to avoid: <
DUPLICATE_EXPRESSION>
24
25Use the primary parent as the main
expression tree. Import only a
26proper non-root subtree or transformed
structural motif from the
27secondary parent. Do not copy the
complete secondary expression.
28Keep the imported material comparable
in size and complexity to
29the replaced primary subtree, and
preserve the useful primary
30backbone.
31
32[Shared DSL and validation constraints
omitted.]
33
34Return only:
35{"factor": "<NEW_CROSSOVER_EXPRESSION
>"}
Prior-rewriting prompt.Prior rewriting is triggered only
after a valid candidate yields informative evolutionary ev-
idence. Rather than producing a free-form reflection or a
partial patch, the LLM rewrites the complete structured
prior, which is subsequently checked against a deterministic
schema.
Prompt E.4: Prior-Rewriting Prompt (Compressed)
1SYSTEM
2
3Rewrite a persistent structured prior,
not a free-form reflection
4or patch. Merge the previous knowledge
with the new evidence,
5preserve supported patterns, weaken
contradicted patterns, merge
6redundant entries, and keep the state
compact. The reported
7metrics are absolute predictive-
strength values. Do not modify
8deterministic validation, evaluation,
or search control. Return
9one complete JSON object matching the
supplied schema, with no
10Markdown.
11
12USER
13
14Target prior: <PRIOR_TARGET>
15Previous structured prior:
16<OLD_PRIOR_JSON>
17
18New evolutionary evidence:
19<EVALUATION_EVIDENCE_JSON>
20
21Expression difference: <
EXPRESSION_DIFF>
22Update trigger: <TRIGGER>
23Required JSON schema: <
TARGET_JSON_SCHEMA>
24
25Rewrite the complete prior according
to the target-specific rules.
The four rewriting targets use different schemas. A lin-
eage mutation prior records successful and failed mutation
patterns, a concise hint, and potential bias risks. A lineage
crossover prior records transferable and harmful patterns,
complementarity, heritable structures, and crossover risks.
Global mutation and crossover priors retain only patterns
that are considered transferable across lineages.
•Lineage mutation prior:
successful_mutation_patterns,
failed_mutation_patterns,hint, and
bias_risk.
•Lineage crossover prior:
transferable_patterns,
harmful_patterns,
complementarity_profile,
heritable_structures,hint, and
crossover_risk.
•Global mutation prior:
global_successful_mutation_patterns,
global_failed_mutation_patterns,
common_invalid_patterns,hint, and
last_updated_generation.
•Global crossover prior:
global_transferable_patterns,
global_harmful_patterns,
global_complementarity_patterns,hint,
andlast_updated_generation.
Duplicateretriesreusetheoriginalgenerationcontextand
append the previous duplicate expression. Mutation retries
mayalsoincluderecentdeterministicvalidationfailures.Ex-
pression validity, DSL compliance, executability, and prior-
schema validation are handled deterministically rather than
through a separate LLM repair prompt.
